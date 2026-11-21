<?php

namespace App\Services;

use App\Models\User;
use Carbon\CarbonImmutable;
use Closure;
use Illuminate\Support\Facades\DB;

class OperationalWrites
{
    public function __construct(private BillSchedule $schedule) {}

    private function branchWrite(User $user, Closure $write): mixed
    {
        return DB::transaction(function () use ($user, $write) {
            $branch = DB::table('branches')->where('id', $user->branch_id)->lockForUpdate()->first();
            abort_unless($branch?->active && User::staff()->whereKey($user->id)->where('branch_id', $branch->id)
                ->where('active', true)->lockForUpdate()->first(), 403, 'Akses telah berubah. Masuk kembali.');
            return $write((int) $branch->id);
        }, 3);
    }

    private function group(int $branch, int $id): object
    {
        $row = OperationalQueries::groups()->where('g.id', $id)->where('g.branch_id', $branch)->first();
        abort_unless($row, 404, 'Kelompok belajar tidak ditemukan.');
        return $row;
    }

    private function openCashDay(int $branch, string $day): void
    {
        abort_if(DB::table('daily_reconciliations')->where(['branch_id' => $branch, 'day' => $day])->exists(),
            409, 'Kas hari ini telah ditutup. Catat pembayaran tunai pada hari operasional berikutnya.');
    }

    private function postingDay(int $branch, string $day): string
    {
        while (DB::table('daily_reconciliations')->where(['branch_id' => $branch, 'day' => $day])->exists()) {
            $day = CarbonImmutable::parse($day)->addDay()->toDateString();
        }
        return $day;
    }

    private function activateIfPaid(object $bill): void
    {
        if ($bill->kind === 'registration' && DB::table('payments')->where('bill_id', $bill->id)
            ->where('status', 'confirmed')->sum('amount') >= $bill->amount) {
            DB::table('enrollments')->where(['id' => $bill->enrollment_id, 'status' => 'pending'])->update(['status' => 'active']);
        }
    }

    private function recordPayment(User $user, object $bill, array $payment, string $day): int
    {
        $cash = $payment['method'] === 'cash';
        if ($cash) {
            $this->openCashDay($bill->branch_id, $day);
        }
        $reserved = DB::table('payments')->where('bill_id', $bill->id)->where('status', '!=', 'rejected')->sum('amount');
        abort_if($payment['amount'] > $bill->amount - $reserved, 422, 'Nominal melebihi sisa tagihan yang belum dibayar atau sedang diverifikasi.');
        $id = DB::table('payments')->insertGetId([
            'branch_id' => $bill->branch_id, 'bill_id' => $bill->id, 'recorded_by' => $user->id,
            'method' => $payment['method'], 'status' => $cash ? 'confirmed' : 'pending', 'amount' => $payment['amount'],
            'recorded_on' => $day, 'recognized_on' => $cash ? $day : null,
            'sender' => $payment['sender'] ?? null, 'transfer_on' => $payment['transfer_on'] ?? null,
        ]);
        if ($cash) {
            $this->activateIfPaid($bill);
        } else {
            DB::table('payment_proofs')->insert(['payment_id' => $id, 'file_type' => $payment['mime'], 'body' => $payment['contents']]);
        }
        return $id;
    }

    public function register(User $user, array $bio, int $packageId, int $groupId, array $payment): int
    {
        return $this->branchWrite($user, function (int $branch) use ($user, $bio, $packageId, $groupId, $payment) {
            $day = BillSchedule::today();
            $package = DB::table('course_packages')->where(['id' => $packageId, 'active' => 1])->first();
            abort_unless($package, 404, 'Paket belajar tidak ditemukan.');
            $group = $this->group($branch, $groupId);
            abort_unless($group->active && $group->level === $bio['level'] && $package->level === $bio['level'],
                422, 'Jenjang paket dan kelompok harus sesuai dengan siswa, dan kelompok harus aktif.');
            abort_if($group->occupied >= $group->capacity, 409, 'Kelompok belajar penuh. Pilih sesi lain.');
            abort_if(DB::table('students')->where(['branch_id' => $branch, 'name' => $bio['name'], 'birth_date' => $bio['birth_date']])->exists(),
                409, 'Siswa dengan nama dan tanggal lahir yang sama sudah terdaftar.');
            $student = DB::table('students')->insertGetId($bio + ['branch_id' => $branch]);
            $enrollment = DB::table('enrollments')->insertGetId([
                'branch_id' => $branch, 'student_id' => $student, 'group_id' => $group->id, 'package_id' => $package->id,
                'registered_on' => $day, 'due_day' => (int) substr($day, 8), 'monthly_fee' => $package->monthly_fee, 'status' => 'pending',
            ]);
            $amount = $package->registration_fee + $package->monthly_fee;
            $bill = [
                'branch_id' => $branch, 'enrollment_id' => $enrollment, 'kind' => 'registration',
                'period' => substr($day, 0, 7), 'due_on' => $day, 'amount' => $amount,
            ];
            $bill['id'] = DB::table('tuition_bills')->insertGetId($bill);
            return $this->recordPayment($user, (object) $bill, $payment, $day);
        });
    }

    public function pay(User $user, int $id, array $payment): int
    {
        return $this->branchWrite($user, function (int $branch) use ($user, $id, $payment) {
            $bill = DB::table('tuition_bills')->where(['id' => $id, 'branch_id' => $branch])->first();
            abort_unless($bill, 404, 'Tagihan tidak ditemukan.');
            return $this->recordPayment($user, $bill, $payment, BillSchedule::today());
        });
    }

    public function reviewPayment(User $user, int $id, array $data): void
    {
        $branch = DB::table('payments')->where('id', $id)->value('branch_id');
        abort_unless($branch, 404, 'Pembayaran tidak ditemukan.');
        DB::transaction(function () use ($user, $id, $data, $branch) {
            DB::table('branches')->where('id', $branch)->lockForUpdate()->first();
            $payment = DB::table('payments')->where(['id' => $id, 'method' => 'transfer', 'status' => 'pending'])->first();
            abort_unless($payment, 404, 'Tidak ada pembayaran transfer yang menunggu pemeriksaan.');
            $approved = $data['decision'] === 'approve';
            DB::table('payments')->where('id', $id)->update([
                'status' => $approved ? 'confirmed' : 'rejected',
                'recognized_on' => $approved ? $this->postingDay($branch, BillSchedule::today()) : null,
                'reviewed_by' => $user->id, 'reviewed_at' => now(),
                'rejection_reason' => $approved ? null : $data['reason'],
            ]);
            if ($approved) {
                $this->activateIfPaid(DB::table('tuition_bills')->find($payment->bill_id));
            }
        }, 3);
    }

    public function close(User $user, array $data): void
    {
        $this->branchWrite($user, function (int $branch) use ($user, $data) {
            $day = BillSchedule::today();
            $this->openCashDay($branch, $day);
            $totals = DB::table('payments')->where(['branch_id' => $branch, 'status' => 'confirmed', 'recognized_on' => $day])
                ->groupBy('method')->selectRaw('method, SUM(amount) total')->pluck('total', 'method');
            $cash = (int) $totals->get('cash', 0);
            $difference = (int) $data['physical'] !== $cash;
            abort_if($difference && empty($data['note']), 422, 'Catatan wajib diisi bila ada selisih kas.');
            DB::table('daily_reconciliations')->insert([
                'branch_id' => $branch, 'closed_by' => $user->id, 'day' => $day, 'cash' => $cash,
                'transfer' => (int) $totals->get('transfer', 0), 'physical' => $data['physical'],
                'note' => $data['note'] ?? null, 'status' => $difference ? 'needs_review' : 'submitted',
            ]);
        });
    }

    public function approveClose(User $user, int $id): void
    {
        $changed = DB::table('daily_reconciliations')->where('id', $id)->where('status', '!=', 'approved')
            ->update(['status' => 'approved', 'reviewed_by' => $user->id, 'reviewed_at' => now()]);
        abort_unless($changed, 404, 'Data tidak ditemukan atau sudah disetujui.');
    }

    public function saveGroup(User $user, ?int $id, array $data): void
    {
        $this->branchWrite($user, function (int $branch) use ($id, $data) {
            if ($id === null) {
                DB::table('study_groups')->insert($data + ['branch_id' => $branch]);
                return;
            }
            $group = $this->group($branch, $id);
            abort_if($data['capacity'] < $group->occupied || ($group->occupied && $data['level'] !== $group->level), 422,
                'Kapasitas tidak boleh di bawah jumlah peserta dan jenjang tidak dapat berubah selama masih ada peserta.');
            DB::table('study_groups')->where('id', $id)->update($data);
        });
    }

    public function saveStudent(User $user, int $id, array $bio, int $groupId, bool $active): void
    {
        $this->branchWrite($user, function (int $branch) use ($id, $bio, $groupId, $active) {
            $student = DB::table('students')->where(['id' => $id, 'branch_id' => $branch])->first();
            $enrollment = DB::table('enrollments')->where(['student_id' => $id, 'branch_id' => $branch])->first();
            abort_unless($student && $enrollment, 404, 'Siswa tidak ditemukan.');
            $group = $this->group($branch, $groupId);
            abort_unless($student->level === $bio['level'] && $student->level === $group->level, 422, 'Jenjang siswa dan kelompok harus sesuai.');
            $status = $active ? ($enrollment->status === 'pending' ? 'pending' : 'active') : 'inactive';
            if ($status !== 'inactive' && ($group->id !== $enrollment->group_id || $enrollment->status === 'inactive')) {
                abort_unless($group->active && $group->occupied < $group->capacity, 409, 'Kelompok belajar tidak aktif atau penuh.');
            }
            $changes = ['group_id' => $group->id, 'status' => $status];
            if ($status === 'active' && $enrollment->status === 'inactive') {
                $bill = OperationalQueries::bills()->where('t.enrollment_id', $enrollment->id)->where('t.kind', 'registration')->first();
                abort_unless($bill && $bill->paid >= $bill->amount, 422, 'Lunasi biaya pendaftaran sebelum mengaktifkan siswa.');
                $changes['billing_resumes_on'] = BillSchedule::today();
            } elseif ($status === 'inactive' && $enrollment->status === 'active') {
                $period = substr(BillSchedule::today(), 0, 7);
                $this->schedule->issueForBranch($branch, $period, $enrollment->id);
                DB::table('tuition_bills')->where(['enrollment_id' => $enrollment->id, 'kind' => 'tuition'])
                    ->where('period', '>', $period)->whereNotExists(
                        DB::table('payments')->selectRaw('1')->whereColumn('bill_id', 'tuition_bills.id')
                    )->delete();
            }
            DB::table('students')->where('id', $id)->update($bio);
            DB::table('enrollments')->where('id', $enrollment->id)->update($changes);
        });
    }

    public function saveBranch(?int $id, array $data): void
    {
        DB::transaction(function () use ($id, $data) {
            if ($id === null) {
                DB::table('branches')->insert($data);
                return;
            }
            $branch = DB::table('branches')->where('id', $id)->lockForUpdate()->first();
            abort_unless($branch, 404, 'Cabang tidak ditemukan.');
            DB::table('branches')->where('id', $id)->update($data);
            if (!(bool) $data['active']) {
                User::staff()->where('branch_id', $id)->eachById(fn (User $user) => $user->tokens()->delete());
            }
        }, 3);
    }

    public function saveUser(?int $id, array $data): void
    {
        DB::transaction(function () use ($id, $data) {
            if ($id === null) {
                User::create($data + ['role' => 'branch_admin']);
                return;
            }
            $user = User::staff()->whereKey($id)->lockForUpdate()->first();
            abort_unless($user, 404, 'Akun staf tidak ditemukan.');
            if (empty($data['password'])) {
                unset($data['password']);
            }
            $user->update($data);
            $user->tokens()->delete();
        }, 3);
    }

    public function savePackage(?int $id, array $data): void
    {
        if ($id === null) {
            DB::table('course_packages')->insert($data);
            return;
        }
        abort_unless(DB::table('course_packages')->where('id', $id)->exists(), 404, 'Paket belajar tidak ditemukan.');
        DB::table('course_packages')->where('id', $id)->update($data);
    }
}
