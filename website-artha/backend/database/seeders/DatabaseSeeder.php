<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use RuntimeException;

class DatabaseSeeder extends Seeder
{
    public const DEMO_PASSWORD = 'ArthaDemo2026!';

    public function run(): void
    {
        $demo = config('artha.demo');
        $email = strtolower(config('artha.admin_email'));
        $center = User::where('email', $email)->first();
        $password = null;
        if (!$center) {
            $password = $demo ? self::DEMO_PASSWORD : config('artha.admin_password');
            if (!is_string($password) || strlen($password) < 12) {
                throw new RuntimeException('Set ARTHA_ADMIN_PASSWORD to at least 12 characters before seeding.');
            }
        }
        DB::transaction(function () use ($center, $email, $demo, $password) {
            if (!$center) {
                User::create(['name' => 'Manajemen Pusat', 'email' => $email, 'role' => 'super_admin', 'active' => true, 'password' => $password]);
            }
            if (!$demo) {
                return;
            }
            $fees = ['TK' => 250000, 'SD' => 300000, 'SMP' => 350000, 'SMA' => 400000];
            foreach ($fees as $level => $fee) {
                DB::table('course_packages')->insertOrIgnore([
                    'name' => 'Reguler', 'level' => $level, 'registration_fee' => 100000, 'monthly_fee' => $fee,
                ]);
            }
            $package = DB::table('course_packages')->where(['name' => 'Reguler', 'level' => 'SD'])->first();
            $staffPassword = Hash::make(self::DEMO_PASSWORD);
            $registered = now('Asia/Makassar')->startOfMonth()->subMonth()->addDays(2)->toDateString();
            for ($i = 1; $i <= 8; $i++) {
                DB::table('branches')->insertOrIgnore(['name' => "Artha {$i}", 'address' => 'Balikpapan (data demo)']);
                $branch = DB::table('branches')->where('name', "Artha {$i}")->value('id');
                $staff = User::firstOrCreate(['email' => "cabang{$i}@artha.example"], [
                    'name' => "Admin Artha {$i}", 'branch_id' => $branch, 'role' => 'branch_admin', 'active' => true, 'password' => $staffPassword,
                ]);
                foreach ($fees as $level => $fee) {
                    DB::table('study_groups')->insertOrIgnore([
                        'branch_id' => $branch, 'name' => "{$level} Sesi A", 'level' => $level, 'schedule' => 'Senin & Rabu, 16.00', 'capacity' => 10,
                    ]);
                }
                $group = DB::table('study_groups')->where(['branch_id' => $branch, 'name' => 'SD Sesi A'])->value('id');
                if (DB::table('students')->where(['branch_id' => $branch, 'name' => "Siswa Demo {$i}", 'birth_date' => '2015-03-12'])->exists()) {
                    continue;
                }
                $student = DB::table('students')->insertGetId([
                    'branch_id' => $branch, 'name' => "Siswa Demo {$i}", 'birth_date' => '2015-03-12', 'school' => 'SD Contoh',
                    'level' => 'SD', 'guardian' => "Wali Demo {$i}", 'phone' => '081200000000', 'address' => 'Balikpapan',
                ]);
                $enrollment = DB::table('enrollments')->insertGetId([
                    'branch_id' => $branch, 'student_id' => $student, 'group_id' => $group, 'package_id' => $package->id,
                    'registered_on' => $registered, 'due_day' => 3, 'monthly_fee' => $package->monthly_fee, 'status' => 'active',
                ]);
                $total = $package->registration_fee + $package->monthly_fee;
                $bill = DB::table('tuition_bills')->insertGetId([
                    'branch_id' => $branch, 'enrollment_id' => $enrollment, 'kind' => 'registration',
                    'period' => substr($registered, 0, 7), 'due_on' => $registered, 'amount' => $total,
                ]);
                DB::table('payments')->insert([
                    'branch_id' => $branch, 'bill_id' => $bill, 'recorded_by' => $staff->id, 'method' => 'cash',
                    'status' => 'confirmed', 'amount' => $total, 'recorded_on' => $registered, 'recognized_on' => $registered,
                ]);
            }
        });
    }
}
