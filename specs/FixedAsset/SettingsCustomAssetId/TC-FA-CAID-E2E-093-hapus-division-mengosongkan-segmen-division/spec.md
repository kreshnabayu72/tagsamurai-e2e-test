---
id: TC-FA-CAID-E2E-093-hapus-division-mengosongkan-segmen-division
title: "Hapus Division dari Master: Segmen Division Menjadi 0000"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-288
coverage:
  web: automated
---

# Hapus Division dari Master: Segmen Division Menjadi 0000

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Division Delete (Pre-setup No 30; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE; pengguna Sarah Johnson), password `Spectra.env.FA_DIVDEL_TC_PASSWORD` (nama usulan; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Global Settings > User > Division, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Division Delete (No 30): Division `Procurement` (Code `PRC`) tanpa pengguna terkait; aset E1 Draft `JKT/LAP/T490/PRC/0926/1`, E2 Active `JKT/LAP/T490/PRC/0926/2`, E3 Disposed `JKT/LAP/T490/PRC/0926/3`; konfigurasi B3; General Settings Date Format `dd/MM/yy`, Time Format 24 jam (No 27). Seluruhnya di-seed hook `before` dan milik spec ini.
- Data Dinamis: Division `Procurement` dihapus (Dinamis No 10); dipulihkan oleh seed reset Company.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md). Kolom Changed At diasersi dengan toleransi satu menit terhadap waktu aksi yang dicatat sesudah klik `[Delete]`; jam server dan jam browser sinkron.
- State global: Division dan aset Company Division Delete diubah; hook `after` memulihkan Company Division Delete ke seed awal dan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Global Settings > User > Division
2. Klik `⋯` pada baris `Procurement` lalu `Delete`
3. Klik `[Delete]` pada dialog `Delete Division`, lalu catat waktu aksi
4. Verifikasi toast sukses `Success, division has been deleted.` tampil
5. Buka Fixed Asset > Assets > All Assets dan perhatikan E1, E2, E3
6. Verifikasi E1 menjadi `JKT/LAP/T490/0000/0926/1` dan E2 menjadi `JKT/LAP/T490/0000/0926/2`: hanya segmen Division yang berubah menjadi `0000`
7. Verifikasi E3 (Disposed) tetap `JKT/LAP/T490/PRC/0926/3`
8. Buka Detail E1
9. Buka tab `Histori Aset`
10. Verifikasi entri teratas memuat Old Asset ID `JKT/LAP/T490/PRC/0926/1`, New Asset ID `JKT/LAP/T490/0000/0926/1`, Reason `Division Change`, Changed At berisi tanggal dan jam aksi dalam format General Settings (dd/MM/yy, 24 jam, toleransi satu menit), dan Changed By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Langkah penghubung: langkah 1 (buka halaman), 3 (catat waktu aksi), 5, 8, 9 (navigasi dan perhatikan).
- Temuan untuk QA:
  - Email akun Total Control Company Division Delete tidak tertulis di Pre-setup TC.
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
