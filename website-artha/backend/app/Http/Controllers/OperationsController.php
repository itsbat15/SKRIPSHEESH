<?php

namespace App\Http\Controllers;

use App\Services\BillSchedule;
use App\Services\Documents;
use App\Services\OperationalQueries;
use App\Services\OperationalWrites;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Validation\ValidationException;
use Symfony\Component\HttpFoundation\Response;

class OperationsController
{
    public function __construct(private OperationalQueries $queries, private OperationalWrites $writes, private Documents $documents) {}

    public function workspace(Request $request): JsonResponse
    {
        return response()->json($this->queries->workspace($request->user()));
    }

    private function bio(Request $request): array
    {
        $data = $request->validate([
            'name' => 'required|string|max:200', 'birth_date' => ['required', 'date_format:Y-m-d', 'before_or_equal:'.BillSchedule::today()],
            'school' => 'required|string|max:200', 'level' => 'required|in:TK,SD,SMP,SMA',
            'guardian' => 'required|string|max:200', 'phone' => 'required|string|max:24', 'address' => 'required|string|max:400',
        ]);
        $data['phone'] = preg_replace('/[\s()+-]/', '', $data['phone']);
        if (!preg_match('/^(?:0|62)[1-9]\d{7,12}$/D', $data['phone'])) {
            throw ValidationException::withMessages(['phone' => 'Nomor WhatsApp tidak valid.']);
        }
        return $data;
    }

    private function payment(Request $request): array
    {
        $payment = $request->validate(['method' => 'required|in:cash,transfer', 'amount' => 'required|integer|between:1,2000000000']);
        if ($payment['method'] === 'cash') {
            return $payment;
        }
        $transfer = $request->validate([
            'sender' => 'required|string|max:200',
            'transfer_on' => ['required', 'date_format:Y-m-d', 'before_or_equal:'.BillSchedule::today()],
            'proof' => 'required|file|mimetypes:image/jpeg,image/png,application/pdf',
        ]);
        return $payment + [
            'sender' => $transfer['sender'], 'transfer_on' => $transfer['transfer_on'],
            'mime' => $transfer['proof']->getMimeType(), 'contents' => $transfer['proof']->get(),
        ];
    }

    public function register(Request $request): JsonResponse
    {
        $ids = $request->validate(['package_id' => 'required|integer|min:1', 'group_id' => 'required|integer|min:1']);
        $id = $this->writes->register($request->user(), $this->bio($request), $ids['package_id'], $ids['group_id'], $this->payment($request));
        return response()->json(['paymentId' => $id], 201);
    }

    public function pay(Request $request, int $bill): JsonResponse
    {
        $id = $this->writes->pay($request->user(), $bill, $this->payment($request));
        return response()->json(['paymentId' => $id], 201);
    }

    public function reviewPayment(Request $request, int $payment): JsonResponse
    {
        $data = $request->validate(['decision' => 'required|in:approve,reject', 'reason' => 'required_if:decision,reject|nullable|string|max:400']);
        $this->writes->reviewPayment($request->user(), $payment, $data);
        return response()->json(['ok' => true]);
    }

    public function close(Request $request): JsonResponse
    {
        $data = $request->validate(['physical' => 'required|integer|between:0,1000000000000', 'note' => 'nullable|string|max:400']);
        $this->writes->close($request->user(), $data);
        return response()->json(['ok' => true], 201);
    }

    public function approveClose(Request $request, int $close): JsonResponse
    {
        $this->writes->approveClose($request->user(), $close);
        return response()->json(['ok' => true]);
    }

    public function saveGroup(Request $request, ?int $id = null): JsonResponse
    {
        $data = $request->validate([
            'name' => 'required|string|max:200', 'level' => 'required|in:TK,SD,SMP,SMA',
            'schedule' => 'required|string|max:200', 'capacity' => 'required|integer|between:1,200', 'active' => 'required|boolean',
        ]);
        $this->writes->saveGroup($request->user(), $id, $data);
        return response()->json(['ok' => true], $id === null ? 201 : 200);
    }

    public function saveStudent(Request $request, int $id): JsonResponse
    {
        $changes = $request->validate(['group_id' => 'required|integer|min:1', 'active' => 'required|boolean']);
        $this->writes->saveStudent($request->user(), $id, $this->bio($request), $changes['group_id'], $changes['active']);
        return response()->json(['ok' => true]);
    }

    public function saveBranch(Request $request, ?int $id = null): JsonResponse
    {
        $data = $request->validate(['name' => 'required|string|max:200', 'address' => 'required|string|max:400', 'active' => 'required|boolean']);
        $this->writes->saveBranch($id, $data);
        return response()->json(['ok' => true], $id === null ? 201 : 200);
    }

    public function savePackage(Request $request, ?int $id = null): JsonResponse
    {
        $data = $request->validate([
            'name' => 'required|string|max:200', 'level' => 'required|in:TK,SD,SMP,SMA', 'active' => 'required|boolean',
            'registration_fee' => 'required|integer|between:0,1000000000', 'monthly_fee' => 'required|integer|between:1,1000000000',
        ]);
        $this->writes->savePackage($id, $data);
        return response()->json(['ok' => true], $id === null ? 201 : 200);
    }

    public function saveUser(Request $request, ?int $id = null): JsonResponse
    {
        $data = $request->validate([
            'name' => 'required|string|max:200', 'email' => 'required|email:rfc|max:200', 'active' => 'required|boolean',
            'branch_id' => 'required|integer|exists:branches,id',
            'password' => [$id === null ? 'required' : 'nullable', 'string', 'min:12', 'max:128'],
        ]);
        $data['email'] = strtolower($data['email']);
        $this->writes->saveUser($id, $data);
        return response()->json(['ok' => true], $id === null ? 201 : 200);
    }

    public function proof(Request $request, int $payment): Response
    {
        $proof = OperationalQueries::scoped(DB::table('payment_proofs as f')->join('payments as p', 'p.id', '=', 'f.payment_id'),
            $request->user(), 'p.branch_id')->where('p.id', $payment)->first(['f.*']);
        abort_unless($proof, 404, 'Bukti transfer tidak ditemukan.');
        $extension = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'application/pdf' => 'pdf'][$proof->file_type];
        return response($proof->body, 200, ['Content-Type' => $proof->file_type,
            'Content-Disposition' => "inline; filename=\"bukti-{$payment}.{$extension}\"",
            'Content-Security-Policy' => "default-src 'none'"]);
    }

    public function receipt(Request $request, int $payment): Response
    {
        $row = OperationalQueries::scoped(OperationalQueries::payments(), $request->user(), 'p.branch_id')
            ->where(['p.id' => $payment, 'p.status' => 'confirmed'])->first();
        abort_unless($row, 404, 'Pembayaran tidak ditemukan atau belum terkonfirmasi.');
        abort_if($row->bill_paid < $row->bill_amount, 409, 'Kuitansi terbit setelah tagihan lunas.');
        return $this->documents->receipt($row);
    }

    public function closeDocument(Request $request, int $close): Response
    {
        $row = OperationalQueries::scoped(OperationalQueries::reconciliations(), $request->user(), 'r.branch_id')->where('r.id', $close)->first();
        abort_unless($row, 404, 'Rekonsiliasi tidak ditemukan.');
        return $this->documents->reconciliation($row);
    }

    public function report(Request $request): Response
    {
        $filters = $request->validate([
            'from' => 'required|date_format:Y-m-d', 'to' => 'required|date_format:Y-m-d|after_or_equal:from',
            'branch' => 'nullable|integer|exists:branches,id', 'format' => 'nullable|in:json,pdf,xlsx',
        ]);
        $report = $this->queries->revenue($filters);
        return match ($filters['format'] ?? 'json') {
            'pdf' => $this->documents->revenuePdf($report), 'xlsx' => $this->documents->revenueExcel($report),
            default => response()->json($report),
        };
    }
}
