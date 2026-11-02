---
id: TC-AC-CS-E2E-065-convert-trial-requester-jalur-request
title: "Convert Trial: Requester Jalur Request"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-244
  - TC-AC-CS-246
  - TC-AC-CS-256
coverage:
  web: automated
---

# Convert Trial: Requester Jalur Request

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup global: Toggle `Require Approval for Allocation` (Settings > Role & Permission, per entitas PT Maju Bersama dan CV Karya Mandiri): OFF untuk TC-AC-CS-244, ON untuk TC-AC-CS-246 dan TC-AC-CS-256 (#23); Main Pocket saldo $25,000.00 (#20); harga SAMS Professional $7,000.00 per tahun (#27).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan ganda PT Maju Bersama pada group `Jawa` dan CV Karya Mandiri, padanan Pre-setup #43) dengan trial SAMS Growth Active (Start `10/08/26`, End `08/09/26`) tanpa term paid SAMS (bentuk Pre-setup #71). Satu seed per keadaan Convert:
  1. TC-AC-CS-244: Client `Klinik Harapan Bunda A+{runId}-065`.
  2. TC-AC-CS-246 dan TC-AC-CS-256 (256 melanjutkan hasil 246 pada Client yang sama): Client `Klinik Harapan Bunda B+{runId}-065`.
- Data Dinamis: term paid, trial Converted, hasil Cancel Request, dan entri audit trail hanya pada Client seed dan dihapus bersama seed di hook `after`. Yang dipulihkan hanya state global: toggle Require Approval for Allocation (diatur ke OFF dan ON oleh spec ini, dipulihkan ke nilai awal oleh fixture backend pemulihan state di hook `after`; setelan per entitas bersama sehingga tidak dapat dimiliki spec) dan saldo Reserved Wallet Main Pocket PT Maju Bersama yang berubah akibat Convert (hook `after`).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (status trial Active bergantung pada hari ini), dipulihkan di hook `after`; toggle Require Approval for Allocation; membaca saldo Reserved Wallet Main Pocket.

## Test Steps

### TC-AC-CS-244: Convert oleh requester biasa dengan toggle OFF juga jalur instan

1. Atur toggle Require Approval for Allocation OFF lewat kemampuan tim FE/BE
2. Ketik Search `Klinik Harapan Bunda A+{runId}-065`, tekan Enter, klik ikon `⋯` pada baris trial Active SAMS Growth lalu pilih `Convert`
3. Pilih Plan `Professional`, isi Duration `1`, klik `[Submit]` lalu klik `[Convert]` pada dialog
4. Verifikasi toast sukses "Success, subscription has been added and trial converted."
5. Klik tab `History`, ganti isi kotak search dengan `Klinik Harapan Bunda A+{runId}-065`, tekan Enter
6. Verifikasi trial berstatus Converted
7. Klik tab `Current`, ganti isi kotak search dengan `Klinik Harapan Bunda A+{runId}-065`, tekan Enter
8. Verifikasi term paid berstatus Active tanpa Waiting for Approval

### TC-AC-CS-246: Convert jalur request: term paid Waiting for Approval dan trial tetap Active

9. Atur toggle Require Approval for Allocation ON lewat kemampuan tim FE/BE, lalu ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-065`, tekan Enter
10. Catat saldo Reserved Main Pocket sebagai baseline
11. Klik ikon `⋯` pada baris trial Active SAMS Growth lalu pilih `Convert`
12. Pilih Plan `Professional`, isi Duration `1`, klik `[Submit]` lalu klik `[Convert]` pada dialog
13. Verifikasi toast sukses "Success, your request has been submitted for approval."
14. Verifikasi term paid baru berstatus Waiting for Approval dengan Plan Owner `PT Maju Bersama (Distributor)`
15. Verifikasi trial tetap Active dan belum Converted
16. Verifikasi Wallet di-Reserve sesuai Estimated Cost (saldo Reserved bertambah dibanding baseline)
17. Ganti akun: Logout lalu login sebagai Total Control Principal (`Hendra Wijaya`)
18. Buka menu Approvals > Client Subscription Tab Active, ketik Search `Klinik Harapan Bunda B+{runId}-065`, tekan Enter
19. Verifikasi pengajuan Client `Klinik Harapan Bunda B+{runId}-065` tampil dengan label `Convert Trial`

### TC-AC-CS-256: Cancel Request pada term paid Waiting for Approval hasil Convert: trial tetap Active

20. Ganti akun: Logout lalu login sebagai Create-Only Distributor (`Fajar Nugroho`)
21. Buka menu Allocation > Client Subscription (tab Current), ketik Search `Klinik Harapan Bunda B+{runId}-065`, tekan Enter
22. Catat saldo Reserved Main Pocket sebagai baseline
23. Klik ikon `⋯` pada term Waiting for Approval lalu pilih `Cancel Request`, klik `[Cancel Request]` pada dialog
24. Verifikasi toast sukses "Success, your request has been canceled."
25. Klik tab `History`, ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-065`, tekan Enter
26. Verifikasi term paid berstatus Canceled
27. Verifikasi saldo Reserved Main Pocket berkurang dibanding baseline (Reserve dilepas)
28. Klik tab `Current`, ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-065`, tekan Enter
29. Verifikasi trial tetap Active
30. Klik ikon `⋯` pada baris trial
31. Verifikasi menu memuat Convert (dapat diajukan ulang)

## Notes

- TC-AC-CS-256 melanjutkan hasil TC-AC-CS-246 (kolom Dependensi); langkah Convert TC-AC-CS-246 disalin utuh sehingga TC-AC-CS-256 tidak bergantung pada spec lain (S-04, S-06).
- Pemeriksaan Approvals (TC-AC-CS-246 butir d) oleh Total Control Principal karena requester Create-Only tidak diasumsikan punya akses Approvals; ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16), termasuk Search ulang sesudah pindah tab `History` dan `Current` dan di Approvals; `Buka menu Allocation > Client Subscription` sesudah ganti akun; pindah tab `History` dan `Current` untuk baris Converted dan Canceled; pengaturan toggle lewat fixture; baseline saldo Reserved dicatat sebelum aksi yang diasersi mengubah Reserve.
- Temuan untuk QA: (1) TC-AC-CS-246 Post Condition a (pengajuan di Approvals) sudah menjadi Expected d; Post Condition b (Reserve Wallet) sama dengan Expected d. (2) TC-AC-CS-256 butir c ("Convert dapat diajukan ulang") diamati sebagai ketersediaan row action Convert.
