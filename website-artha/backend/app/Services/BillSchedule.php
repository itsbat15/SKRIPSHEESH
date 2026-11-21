<?php

namespace App\Services;

use App\Models\User;
use Carbon\CarbonImmutable;
use Illuminate\Support\Facades\DB;

class BillSchedule
{
    public static function today(): string
    {
        return now('Asia/Makassar')->toDateString();
    }

    public static function nextPeriod(string $period): string
    {
        return CarbonImmutable::parse($period.'-01', 'Asia/Makassar')->addMonth()->format('Y-m');
    }

    public static function dueDate(string $period, int $day): string
    {
        $month = CarbonImmutable::parse($period.'-01', 'Asia/Makassar');
        return $month->day(min($day, $month->daysInMonth))->toDateString();
    }

    public function issue(User $user, string $day): void
    {
        $through = self::nextPeriod(substr($day, 0, 7));
        $branches = OperationalQueries::scoped(DB::table('branches'), $user, 'id')->where('active', 1)->orderBy('id')->pluck('id');
        foreach ($branches as $branch) {
            DB::transaction(function () use ($branch, $through) {
                if (!DB::table('branches')->where('id', $branch)->where('active', 1)->lockForUpdate()->first()) {
                    return;
                }
                $this->issueForBranch($branch, $through);
            }, 3);
        }
    }

    public function issueForBranch(int $branch, string $through, ?int $enrollmentId = null): void
    {
        $enrollments = DB::table('enrollments as e')->where('e.branch_id', $branch)->where('e.status', 'active')
            ->when($enrollmentId, fn ($query, $id) => $query->where('e.id', $id))
            ->select('e.id', 'e.due_day', 'e.monthly_fee', 'e.registered_on', 'e.billing_resumes_on')->selectSub(
                DB::table('tuition_bills')->selectRaw('MAX(period)')->whereColumn('enrollment_id', 'e.id')->where('kind', 'tuition'), 'last_period'
            )->get();
        $bills = [];
        foreach ($enrollments as $enrollment) {
            $from = self::nextPeriod($enrollment->last_period ?? substr($enrollment->registered_on, 0, 7));
            if ($enrollment->billing_resumes_on) {
                $from = max($from, substr($enrollment->billing_resumes_on, 0, 7));
            }
            for ($period = $from; $period <= $through; $period = self::nextPeriod($period)) {
                $bills[] = ['branch_id' => $branch, 'enrollment_id' => $enrollment->id, 'kind' => 'tuition',
                    'period' => $period, 'due_on' => self::dueDate($period, $enrollment->due_day), 'amount' => $enrollment->monthly_fee];
            }
        }
        foreach (array_chunk($bills, 500) as $chunk) {
            DB::table('tuition_bills')->insertOrIgnore($chunk);
        }
    }
}
