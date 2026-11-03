---
id: TC-AC-CS-E2E-064-convert-trial-group-manager-jalur-instan
title: "Convert Trial: Group Manager Jalur Instan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-243
  - TC-AC-CS-245
  - TC-AC-CS-255
coverage:
  web: automated
---

# Convert Trial: Group Manager Jalur Instan

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Group Manager scope Group Jawa Distributor PT Maju Bersama, Dewi Anggraini (Pre-setup #5), `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_GM_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup baca-saja/global: Group Manager `Dewi Anggraini` (#5) bypass; Main Pocket saldo $25,000.00 (#20); harga SAMS Professional $7,000.00 per tahun (#27); tanggal acuan uji `19/08/26` (#28).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan ganda PT Maju Bersama pada group `Jawa` dan CV Karya Mandiri, padanan Pre-setup #43). Satu seed per keadaan Convert:
  1. TC-AC-CS-243: Client `Klinik Harapan Bunda A+{runId}-064` dengan trial SAMS Growth Active (Start `10/08/26`, End `08/09/26`, Plan Owner CV Karya Mandiri) tanpa term paid SAMS (bentuk Pre-setup #71).
  2. TC-AC-CS-245 dan TC-AC-CS-255 (255 melanjutkan hasil 245 pada Client yang sama): Client `Klinik Harapan Bunda B+{runId}-064` dengan term paid SAMS Growth Active (End Date `14/09/26`, Plan Owner PT Maju Bersama) dan trial SAMS Professional Active (Plan Owner CV Karya Mandiri) (bentuk Pre-setup #73).
- Data Dinamis: term paid, trial Converted, hasil Cancel Request, dan entri audit trail hanya pada Client seed dan dihapus bersama seed di hook `after`. Yang dipulihkan hanya state global: saldo Captured dan Reserved Wallet Main Pocket PT Maju Bersama yang berubah akibat Convert dan Cancel Request (dikembalikan oleh fixture backend pemulihan state di hook `after`; Wallet bersama tidak dapat dimiliki spec) dan jam server dan browser (hook `after`).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`); membaca saldo Captured dan Reserved Wallet Main Pocket; membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-243: Convert jalur instan mode New: trial Converted dan term paid Active hari ini

1. Ketik Search `Klinik Harapan Bunda A+{runId}-064`, tekan Enter, lalu catat jumlah entri Changelog Client `Klinik Harapan Bunda A+{runId}-064` — SAMS dan saldo Captured Main Pocket sebagai baseline
2. Klik ikon `⋯` pada baris trial Active SAMS Growth lalu pilih `Convert`
3. Pilih Plan `Professional`, isi Duration `1` lalu klik `[Submit]`
4. Klik `[Convert]`
5. Verifikasi toast sukses "Success, subscription has been added and trial converted."
6. Klik tab `History`, ganti isi kotak search dengan `Klinik Harapan Bunda A+{runId}-064`, tekan Enter
7. Verifikasi baris trial berstatus Converted
8. Klik tab `Current`, ganti isi kotak search dengan `Klinik Harapan Bunda A+{runId}-064`, tekan Enter
9. Verifikasi term paid baru berstatus Active dengan Start Date `19/08/26` (tidak ada jeda dengan trial)
10. Verifikasi Plan Owner term paid `PT Maju Bersama (Distributor)`
11. Verifikasi Wallet Main Pocket di-Capture $7,000.00 (saldo Captured bertambah $7,000.00 dibanding baseline)
12. Buka modal Changelog Client `Klinik Harapan Bunda A+{runId}-064` — SAMS
13. Verifikasi jumlah entri Changelog bertambah satu dibanding baseline
14. Verifikasi entri baru Action `Convert`, Field `Subscription Type`, Old `Trial — Growth`, New `Professional (Paid)`

### TC-AC-CS-245: Convert jalur instan mode Renewal: term paid Pending dan trial Converted

15. Tutup modal Changelog, ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-064`, tekan Enter, klik ikon `⋯` pada baris trial lalu pilih `Convert`
16. Pilih Plan `Professional`, isi Duration `1` lalu klik `[Submit]`
17. Klik `[Convert]`
18. Verifikasi toast sukses "Success, plan has been changed and trial converted."
19. Klik tab `History`, ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-064`, tekan Enter
20. Verifikasi trial berstatus Converted
21. Klik tab `Current`, ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-064`, tekan Enter
22. Verifikasi term paid baru berstatus Pending dengan Start Date `15/09/26`
23. Verifikasi predecessor term paid tetap Active sampai flip
24. Buka Detail term paid baru
25. Verifikasi Previous Subscription term baru menunjuk term paid predecessor, bukan baris trial

### TC-AC-CS-255: Cancel Request pada term paid Pending hasil Convert: trial tetap Converted

26. Kembali ke List, lalu catat saldo Reserved Main Pocket sebagai baseline
27. Ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-064`, tekan Enter
28. Klik ikon `⋯` pada term Pending lalu pilih `Cancel Request`
29. Klik `[Cancel Request]`
30. Verifikasi toast sukses "Success, your request has been canceled."
31. Klik tab `History`, ganti isi kotak search dengan `Klinik Harapan Bunda B+{runId}-064`, tekan Enter
32. Verifikasi term paid berstatus Canceled
33. Verifikasi saldo Reserved Main Pocket berkurang dibanding baseline (Reserve dilepas)
34. Verifikasi trial tetap Converted dan tidak direvert ke Active

## Notes

- TC-AC-CS-255 melanjutkan hasil TC-AC-CS-245 pada spec yang sama (kolom Dependensi); langkah Convert TC-AC-CS-245 disalin utuh sehingga TC-AC-CS-255 tidak bergantung pada spec lain (S-04, S-06).
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16), termasuk Search ulang sesudah pindah tab `History` dan `Current`; tutup modal Changelog sebelum aksi berikutnya; kembali ke List dari Detail; baseline saldo Captured dan jumlah entri Changelog dicatat sebelum aksi supaya asersi Capture dan "entri baru" memakai selisih (S-12); log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- Temuan untuk QA: (1) TC-AC-CS-243 butir d "Sisa hari trial hangus" tidak punya cara pengamatan di TC sehingga hanya Capture $7,000.00 yang diasersi. (2) TC-AC-CS-245 butir c menyebut Start Date `15/09/26` tanpa menyebut sumbernya; spec memakai End Date predecessor `14/09/26` + 1 hari dari Pre-setup #73.
