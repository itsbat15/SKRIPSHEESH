<?php

namespace Tests\Feature;

use Carbon\CarbonImmutable;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\TestCase;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\DB;
use Illuminate\Testing\TestResponse;

class OperationsTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();
        $this->travelTo(CarbonImmutable::parse('2026-01-31 12:00', 'Asia/Makassar'));
        config(['artha.demo' => true, 'artha.admin_email' => 'pusat@artha.example']);
        $this->seed();
    }

    private function login(string $identity): string
    {
        return $this->postJson('/api/artha/login', ['email' => "{$identity}@artha.example", 'password' => 'ArthaDemo2026!'])
            ->assertOk()->json('token');
    }

    private function api(string $token, string $method, string $path, array $data = [], bool $multipart = false): TestResponse
    {
        $this->app['auth']->forgetGuards();
        $headers = ['Authorization' => "Bearer {$token}", 'Accept' => 'application/json'];
        return $multipart ? $this->post('/api/artha/'.$path, $data, $headers) : $this->json($method, '/api/artha/'.$path, $data, $headers);
    }

    private function group(int $branch): int
    {
        return DB::table('study_groups')->where(['branch_id' => $this->branch($branch), 'level' => 'SD'])->value('id');
    }

    private function branch(int $number): int
    {
        return DB::table('branches')->where('name', "Artha {$number}")->value('id');
    }

    private function registration(array $values = []): array
    {
        return $values + [
            'name' => 'Siswa Baru', 'birth_date' => '2016-04-10', 'school' => 'SD Uji', 'level' => 'SD',
            'guardian' => 'Wali Uji', 'phone' => '081211112222', 'address' => 'Balikpapan',
            'package_id' => DB::table('course_packages')->where('level', 'SD')->value('id'),
            'group_id' => $this->group(1), 'method' => 'cash', 'amount' => 400000,
        ];
    }

    private function transfer(): array
    {
        return ['method' => 'transfer', 'sender' => 'Wali Uji', 'transfer_on' => '2026-01-31',
            'proof' => UploadedFile::fake()->createWithContent('bukti.pdf', "%PDF-1.7\n1 0 obj\n<<>>\nendobj\n%%EOF\n")];
    }

    public function test_authentication_role_and_branch_isolation(): void
    {
        $this->getJson('/api/artha/workspace')->assertUnauthorized();
        $this->postJson('/api/artha/login', ['email' => 'cabang1@artha.example', 'password' => 'salah'])->assertUnauthorized();
        $branch = $this->login('cabang1');
        $center = $this->login('pusat');
        $this->api($branch, 'GET', 'workspace')->assertOk()->assertJsonCount(1, 'branches')->assertJsonMissing(['name' => 'Siswa Demo 2']);
        $this->api($center, 'GET', 'workspace')->assertOk()->assertJsonCount(8, 'branches')->assertJsonFragment(['name' => 'Siswa Demo 2']);
        $this->api($branch, 'GET', 'reports/revenue?from=2026-01-01&to=2026-01-31')->assertForbidden();
        $this->api($branch, 'POST', 'enrollments', $this->registration(['group_id' => $this->group(2)]))->assertNotFound();
        $this->api($center, 'POST', 'enrollments', $this->registration())->assertForbidden();
        $this->api($center, 'POST', 'staff', ['name' => 'Staf', 'email' => 'cabang1@artha.example', 'branch_id' => $this->branch(1),
            'password' => 'DemoSandi2026!', 'active' => 1])->assertConflict();
        $this->api($branch, 'POST', 'logout')->assertOk();
        $this->api($branch, 'GET', 'workspace')->assertUnauthorized();
    }

    public function test_registration_capacity_cash_receipt_and_clamped_due_date(): void
    {
        $branch = $this->login('cabang1');
        $other = $this->login('cabang2');
        $payment = $this->api($branch, 'POST', 'enrollments', $this->registration(['amount' => 100000]))->assertCreated()->json('paymentId');
        $bill = DB::table('payments')->where('id', $payment)->value('bill_id');
        $this->api($branch, 'GET', "payments/{$payment}/receipt")->assertConflict();
        $this->api($other, 'POST', "bills/{$bill}/payments", ['method' => 'cash', 'amount' => 300000])->assertNotFound();
        $this->api($branch, 'POST', 'enrollments', $this->registration())->assertConflict();
        $this->api($branch, 'POST', "bills/{$bill}/payments", ['method' => 'cash', 'amount' => 300000])->assertCreated();
        $this->api($other, 'GET', "payments/{$payment}/receipt")->assertNotFound();
        $pdf = $this->api($branch, 'GET', "payments/{$payment}/receipt")->assertOk()->assertHeader('Content-Type', 'application/pdf');
        $this->assertStringStartsWith('%PDF-', $pdf->getContent());
        $this->api($branch, 'GET', 'workspace')->assertOk()->assertJsonFragment(['student_name' => 'Siswa Baru', 'due_on' => '2026-02-28']);
        DB::table('study_groups')->where('id', $this->group(1))->update(['capacity' => 2]);
        $this->api($branch, 'POST', 'enrollments', $this->registration(['name' => 'Siswa Penuh']))->assertConflict();
    }

    public function test_transfer_review_rejection_retry_and_proof_permissions(): void
    {
        $branch = $this->login('cabang1');
        $other = $this->login('cabang2');
        $center = $this->login('pusat');
        $id = $this->api($branch, 'POST', 'enrollments', $this->registration($this->transfer()), true)->assertCreated()->json('paymentId');
        $this->api($other, 'GET', "payments/{$id}/proof")->assertNotFound();
        $this->api($center, 'GET', "payments/{$id}/proof")->assertOk()->assertHeader('Content-Type', 'application/pdf');
        $this->api($branch, 'PATCH', "payments/{$id}/review", ['decision' => 'approve'])->assertForbidden();
        $this->api($center, 'PATCH', "payments/{$id}/review", ['decision' => 'reject'])->assertUnprocessable();
        $this->api($center, 'PATCH', "payments/{$id}/review", ['decision' => 'reject', 'reason' => 'Nominal berbeda'])->assertOk();
        $this->api($branch, 'GET', 'workspace')->assertOk()->assertJsonFragment(['rejection_reason' => 'Nominal berbeda']);
        $bill = DB::table('payments')->where('id', $id)->value('bill_id');
        $retry = $this->api($branch, 'POST', "bills/{$bill}/payments", $this->transfer() + ['amount' => 400000], true)->assertCreated()->json('paymentId');
        $this->api($center, 'PATCH', "payments/{$retry}/review", ['decision' => 'approve'])->assertOk();
        $this->api($branch, 'GET', "payments/{$retry}/receipt")->assertOk();
    }

    public function test_cash_close_discrepancy_approval_overdue_and_report_formats(): void
    {
        $branch = $this->login('cabang1');
        $other = $this->login('cabang2');
        $center = $this->login('pusat');
        $pending = $this->api($branch, 'POST', 'enrollments', $this->registration($this->transfer() + ['name' => 'Siswa Transfer']), true)
            ->assertCreated()->json('paymentId');
        $this->api($branch, 'POST', 'enrollments', $this->registration())->assertCreated();
        $this->api($branch, 'POST', 'reconciliations', ['physical' => 399000])->assertUnprocessable();
        $this->api($branch, 'POST', 'reconciliations', ['physical' => 399000, 'note' => 'Periksa penghitungan'])->assertCreated();
        $this->api($branch, 'POST', 'enrollments', $this->registration(['name' => 'Kas Ditutup']))->assertConflict();
        $close = DB::table('daily_reconciliations')->where('branch_id', $this->branch(1))->first();
        $this->assertSame('needs_review', $close->status);
        $this->api($other, 'GET', "reconciliations/{$close->id}/document")->assertNotFound();
        $this->api($center, 'PATCH', "reconciliations/{$close->id}/approval")->assertOk();
        $this->api($branch, 'GET', "reconciliations/{$close->id}/document")->assertOk()->assertHeader('Content-Type', 'application/pdf');
        $this->api($center, 'PATCH', "payments/{$pending}/review", ['decision' => 'approve'])->assertOk();
        $this->assertSame('2026-02-01', DB::table('payments')->where('id', $pending)->value('recognized_on'));
        $this->api($branch, 'GET', 'workspace')->assertOk()->assertJsonFragment(['overdue' => true]);
        $report = 'reports/revenue?from=2026-01-31&to=2026-01-31';
        $this->api($center, 'GET', $report.'&branch=')->assertOk()->assertJsonCount(8, 'rows');
        $this->api($center, 'GET', $report.'&branch='.$this->branch(1))->assertOk()->assertJsonPath('rows.0.cash', 400000);
        $this->api($center, 'GET', $report.'&format=pdf')->assertOk()->assertHeader('Content-Type', 'application/pdf');
        $xlsx = $this->api($center, 'GET', $report.'&format=xlsx')->assertOk();
        $this->assertStringStartsWith('PK', $xlsx->streamedContent());
    }
}
