<?php

namespace App\Services;

use App\Models\User;
use Illuminate\Database\Query\Builder;
use Illuminate\Support\Facades\DB;

class OperationalQueries
{
    public function __construct(private BillSchedule $schedule) {}

    public static function scoped(Builder $query, User $user, string $column = 'branch_id'): Builder
    {
        return $query->when(!$user->isCenter(), fn (Builder $q) => $q->where($column, $user->branch_id));
    }

    public static function groups(): Builder
    {
        return DB::table('study_groups as g')->join('branches as b', 'b.id', '=', 'g.branch_id')
            ->select('g.*', 'b.name as branch_name')->selectSub(
                DB::table('enrollments as e')->selectRaw('COUNT(*)')->whereColumn('e.group_id', 'g.id')->whereIn('e.status', ['active', 'pending']), 'occupied'
            );
    }

    public static function bills(): Builder
    {
        $sum = fn (string $status) => DB::table('payments as p')->selectRaw('COALESCE(SUM(p.amount), 0)')
            ->whereColumn('p.bill_id', 't.id')->where('p.status', $status);
        return DB::table('tuition_bills as t')->join('enrollments as e', 'e.id', '=', 't.enrollment_id')
            ->join('students as s', 's.id', '=', 'e.student_id')->join('study_groups as g', 'g.id', '=', 'e.group_id')
            ->join('branches as b', 'b.id', '=', 't.branch_id')
            ->select('t.*', 's.name as student_name', 's.phone', 's.guardian', 's.level', 'g.name as group_name', 'b.name as branch_name')
            ->selectSub($sum('confirmed'), 'paid')->selectSub($sum('pending'), 'pending');
    }

    public static function payments(): Builder
    {
        return DB::table('payments as p')->join('tuition_bills as t', 't.id', '=', 'p.bill_id')
            ->join('enrollments as e', 'e.id', '=', 't.enrollment_id')->join('students as s', 's.id', '=', 'e.student_id')
            ->join('branches as b', 'b.id', '=', 'p.branch_id')->join('course_packages as cp', 'cp.id', '=', 'e.package_id')
            ->join('users as u', 'u.id', '=', 'p.recorded_by')
            ->select('p.*', 's.name as student_name', 't.kind', 't.period', 't.amount as bill_amount', 'b.name as branch_name',
                'cp.name as package_name', 'u.name as cashier', 'b.address as branch_address')
            ->selectSub(DB::table('payments as x')->selectRaw('COALESCE(SUM(x.amount), 0)')
                ->whereColumn('x.bill_id', 't.id')->where('x.status', 'confirmed'), 'bill_paid');
    }

    public static function reconciliations(): Builder
    {
        return DB::table('daily_reconciliations as r')->join('branches as b', 'b.id', '=', 'r.branch_id')
            ->join('users as u', 'u.id', '=', 'r.closed_by')->select('r.*', 'b.name as branch_name', 'u.name as cashier');
    }

    public function workspace(User $user): array
    {
        $today = BillSchedule::today();
        $this->schedule->issue($user, $today);
        $branches = self::scoped(DB::table('branches'), $user, 'id')->orderBy('id')->get();
        $bills = self::scoped(self::bills(), $user, 't.branch_id')->orderByDesc('due_on')->orderByDesc('t.id')->get()
            ->map(function ($row) use ($today) {
                foreach (['amount', 'paid', 'pending'] as $key) {
                    $row->$key = (int) $row->$key;
                }
                $row->overdue = $row->paid < $row->amount && $row->due_on < $today;
                $row->status = match (true) {
                    $row->paid >= $row->amount => 'paid', $row->pending > 0 => 'pending',
                    $row->overdue => 'overdue', $row->paid > 0 => 'partial', default => 'unpaid',
                };
                return $row;
            });
        return [
            'today' => $today,
            'user' => ['id' => $user->id, 'name' => $user->name, 'role' => $user->role, 'branch_id' => $user->branch_id,
                'branch_name' => $user->isCenter() ? null : $branches->first()?->name],
            'branches' => $branches,
            'users' => $user->isCenter() ? DB::table('users as u')->join('branches as b', 'b.id', '=', 'u.branch_id')
                ->where('u.role', 'branch_admin')->orderBy('u.name')
                ->get(['u.id', 'u.name', 'u.email', 'u.branch_id', 'u.active', 'b.name as branch_name']) : [],
            'packages' => DB::table('course_packages')->orderBy('level')->orderBy('name')->get(),
            'groups' => self::scoped(self::groups(), $user, 'g.branch_id')->orderBy('g.name')->get(),
            'students' => self::scoped(DB::table('students as s')->join('enrollments as e', 'e.student_id', '=', 's.id')
                ->join('study_groups as g', 'g.id', '=', 'e.group_id')->join('branches as b', 'b.id', '=', 's.branch_id')
                ->join('course_packages as cp', 'cp.id', '=', 'e.package_id'), $user, 's.branch_id')
                ->orderBy('s.name')->get(['s.*', 'e.id as enrollment_id', 'e.status', 'e.registered_on', 'e.due_day',
                    'e.group_id', 'e.package_id', 'g.name as group_name', 'b.name as branch_name', 'cp.name as package_name']),
            'bills' => $bills,
            'payments' => self::scoped(self::payments(), $user, 'p.branch_id')->orderByDesc('p.id')->get()
                ->map(function ($row) {
                    $row->bill_paid = (int) $row->bill_paid;
                    return $row;
                }),
            'reconciliations' => self::scoped(self::reconciliations(), $user, 'r.branch_id')->orderByDesc('r.day')->get(),
        ];
    }

    public function revenue(array $filters): array
    {
        $rows = DB::table('branches as b')->leftJoin('payments as p', fn ($join) => $join
            ->on('p.branch_id', '=', 'b.id')->where('p.status', 'confirmed')
            ->whereBetween('p.recognized_on', [$filters['from'], $filters['to']]))
            ->when($filters['branch'] ?? null, fn ($q, $branch) => $q->where('b.id', $branch))
            ->select('b.id', 'b.name as branch_name')
            ->selectRaw("COALESCE(SUM(CASE WHEN p.method='cash' THEN p.amount END),0) AS cash,
                COALESCE(SUM(CASE WHEN p.method='transfer' THEN p.amount END),0) AS transfer, COUNT(p.id) AS transactions")
            ->groupBy('b.id', 'b.name')->orderBy('b.id')->get()->map(fn ($row) => [
                'id' => (int) $row->id, 'branch_name' => $row->branch_name,
                'cash' => (int) $row->cash, 'transfer' => (int) $row->transfer, 'transactions' => (int) $row->transactions,
            ])->all();
        return ['from' => $filters['from'], 'to' => $filters['to'], 'branch' => (string) ($filters['branch'] ?? ''), 'rows' => $rows];
    }
}
