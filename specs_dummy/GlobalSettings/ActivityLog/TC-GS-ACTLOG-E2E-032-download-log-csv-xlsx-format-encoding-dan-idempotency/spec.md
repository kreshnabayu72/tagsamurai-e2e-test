---
id: TC-GS-ACTLOG-E2E-032-download-log-csv-xlsx-format-encoding-dan-idempotency
title: "Download Laporan Audit CSV dan XLSX: Validasi Format, Header, Encoding UTF-8 BOM, dan Read-Only Idempotency"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-122
  - TC-GS-ACTLOG-123
  - TC-GS-ACTLOG-124
  - TC-GS-ACTLOG-125
  - TC-GS-ACTLOG-128
  - TC-GS-ACTLOG-129
  - TC-GS-ACTLOG-130
  - TC-GS-ACTLOG-131
  - TC-GS-ACTLOG-132
  - TC-GS-ACTLOG-133
  - TC-GS-ACTLOG-134
  - TC-GS-ACTLOG-135
coverage:
  web: automated
---

# Download Laporan Audit CSV dan XLSX: Validasi Format, Header, Encoding UTF-8 BOM, dan Read-Only Idempotency

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log pada kedua tab (Session dan User Action) dengan volume <= 5.000 baris

## Test Steps

### Download CSV Tab Session
1. Buka Tab Session, klik tombol Download > 'Download CSV'.
2. Verifikasi file terunduh dengan format penamaan 'Activity-Log-Session-YYYYMMDD.csv'.
3. Buka file CSV, verifikasi header memuat 10 kolom Tab Session.
4. Verifikasi file memiliki byte order mark UTF-8 BOM (0xEF, 0xBB, 0xBF) untuk kompatibilitas Excel.
5. Verifikasi stempel tanggal pada berkas mematuhi format General Settings.
### Download XLSX Tab Session
6. Klik tombol Download > 'Download XLSX'.
7. Verifikasi file terunduh dengan ekstensi .xlsx dan tipe MIME spreadsheet yang valid.
### Download Saat Filter Aktif vs Tanpa Filter
8. Terapkan filter Activity = 'Login' di Tab Session (menampilkan 5 baris).
9. Klik download CSV, verifikasi berkas terunduh hanya memuat 5 baris data yang cocok dengan filter.
10. Reset filter, lakukan download, verifikasi berkas memuat seluruh baris log.
### Download Tab User Action & Idempotency Guard
11. Pindah ke Tab User Action, klik unduh CSV dan XLSX.
12. Verifikasi penamaan file 'Activity-Log-User-Action-YYYYMMDD.csv' / '.xlsx' dan memuat 8 header kolom.
13. Kembali ke tabel Tab Session dan User Action, muat ulang halaman.
14. Verifikasi aksi mengunduh berkas TIDAK MENCATAT entri audit baru (operasi unduh bersifat read-only dan idempotent).

## Notes

- Ekspor berkas CSV/XLSX mempertahankan integritas data dan tidak mencemari audit trail.
