<?php

namespace App\Services;

use Dompdf\Dompdf;
use Dompdf\Options;
use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use Symfony\Component\HttpFoundation\Response;

class Documents
{
    private static function cash(int $amount): string
    {
        return 'Rp '.number_format($amount, 0, ',', '.');
    }

    private function pdf(string $filename, string $title, string $subheading, array $lines): Response
    {
        $options = new Options(['defaultFont' => 'DejaVu Sans', 'isRemoteEnabled' => false]);
        $document = new Dompdf($options);
        $document->setPaper('a4');
        $document->loadHtml(view('document', compact('title', 'subheading', 'lines'))->render(), 'UTF-8');
        $document->render();
        return response($document->output(), 200, ['Content-Type' => 'application/pdf', 'Content-Disposition' => "inline; filename=\"{$filename}\""]);
    }

    public function receipt(object $row): Response
    {
        $number = 'ARTHA-'.str_pad((string) $row->id, 6, '0', STR_PAD_LEFT);
        $kind = $row->kind === 'registration' ? 'Pendaftaran dan SPP pertama' : 'SPP bulanan';
        $method = $row->method === 'cash' ? 'Tunai' : 'Transfer bank';
        return $this->pdf("kuitansi-{$row->id}.pdf", 'Kuitansi Pembayaran', "{$row->branch_name} | {$row->branch_address}", [
            'Nomor transaksi' => $number, 'Siswa' => $row->student_name,
            'Paket dan periode' => "{$row->package_name} | {$row->period} | {$kind}",
            'Tanggal transaksi' => $row->recorded_on, 'Tanggal pembukuan' => $row->recognized_on,
            'Metode' => $method, 'Nominal transaksi' => self::cash($row->amount),
            'Total tagihan' => self::cash($row->bill_amount), 'Status tagihan' => 'Lunas', 'Dicatat oleh' => $row->cashier,
        ]);
    }

    public function reconciliation(object $row): Response
    {
        return $this->pdf("kas-harian-{$row->id}.pdf", 'Berita Acara Kas Harian', "{$row->branch_name} | {$row->day}", [
            'Petugas' => $row->cashier, 'Tunai sistem' => self::cash($row->cash), 'Transfer sistem' => self::cash($row->transfer),
            'Kas fisik' => self::cash($row->physical), 'Selisih (fisik dikurangi sistem)' => self::cash($row->physical - $row->cash),
            'Catatan' => $row->note ?? '-', 'Status' => ['submitted' => 'Ditutup', 'needs_review' => 'Perlu ditinjau', 'approved' => 'Disetujui'][$row->status],
        ]);
    }

    public function revenuePdf(array $report): Response
    {
        $lines = [];
        $total = 0;
        foreach ($report['rows'] as $row) {
            $total += $row['cash'] + $row['transfer'];
            $lines[$row['branch_name']] = 'Tunai '.self::cash($row['cash']).' | Transfer '.self::cash($row['transfer'])
                .' | Total '.self::cash($row['cash'] + $row['transfer']).' ('.$row['transactions'].' transaksi)';
        }
        $lines['Total pendapatan'] = self::cash($total);
        return $this->pdf('rekap-artha.pdf', 'Rekapitulasi Pendapatan', "Periode {$report['from']} sampai {$report['to']}", $lines);
    }

    public function revenueExcel(array $report): Response
    {
        $book = new Spreadsheet();
        $sheet = $book->getActiveSheet();
        $sheet->setTitle('Pendapatan');
        $sheet->fromArray([['Rekapitulasi Pendapatan Bimbel Artha', $report['from'], $report['to']],
            ['Cabang', 'Tunai (Rp)', 'Transfer (Rp)', 'Total (Rp)', 'Jumlah transaksi']]);
        $sheet->getStyle('A2:E2')->getFont()->setBold(true);
        $i = 3;
        $cash = $transfer = $transactions = 0;
        foreach ($report['rows'] as $row) {
            $sheet->setCellValueExplicit("A{$i}", $row['branch_name'], \PhpOffice\PhpSpreadsheet\Cell\DataType::TYPE_STRING);
            $sheet->fromArray([[$row['cash'], $row['transfer'], $row['cash'] + $row['transfer'], $row['transactions']]], null, "B{$i}", true);
            $cash += $row['cash'];
            $transfer += $row['transfer'];
            $transactions += $row['transactions'];
            $i++;
        }
        $sheet->fromArray([['Total', $cash, $transfer, $cash + $transfer, $transactions]], null, "A{$i}", true);
        foreach (['A', 'B', 'C', 'D', 'E'] as $column) {
            $sheet->getColumnDimension($column)->setWidth($column === 'A' ? 43 : 24);
        }
        return response()->streamDownload(function () use ($book) {
            (new Xlsx($book))->save('php://output');
        }, 'rekap-artha.xlsx', ['Content-Type' => 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']);
    }
}
