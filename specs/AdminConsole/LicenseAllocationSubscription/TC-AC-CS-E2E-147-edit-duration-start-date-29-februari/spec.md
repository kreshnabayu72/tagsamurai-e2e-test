---
id: TC-AC-CS-E2E-147-edit-duration-start-date-29-februari
title: "Edit Duration: Start Date 29 Februari Menghitung Ulang End Date"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-584
coverage:
  web: automated
---

# Edit Duration: Start Date 29 Februari Menghitung Ulang End Date

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager scope Group `Jawa`, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; langkah TC dependensi TC-AC-CS-579 dijalankan lewat seeding API): Client `Client Tanpa Subscription+{runId}-147` (padanan Pre-setup #48, group `Jawa`) dengan term SAMS Growth Pending milik aktor, Start Date `29/02/28`, Duration 1 tahun (End Date `27/02/29`), Reserve $3,000.00 pada `Main Pocket` (Tabel Data Uji Dinamis #8).
- State global yang diubah (suite serial): toggle `Require Approval for Allocation` PT Maju Bersama (Pre-setup #23) ON (bypass Group Manager); saldo `Main Pocket` $25,000.00 (Pre-setup #20) dan Reserve; harga SAMS Growth $3,000.00 per tahun (Pre-setup #27); semuanya dipulihkan di hook `after` lewat fixture BE (disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): membaca Reserve Wallet lewat fixture BE.

## Test Steps

### TC-AC-CS-584: Edit Duration pada term mode New dengan Start Date 29 Februari menghitung ulang End Date

1. Ketik Search `Client Tanpa Subscription+{runId}-147`, tekan Enter
2. Klik ikon `⋯` pada baris term Pending, lalu pilih `Edit`
3. Ubah Duration dari `1` menjadi `4`
4. Klik `[Save]`
5. Verifikasi toast sukses "Success, subscription has been updated." muncul
6. Buka Detail term dengan klik baris term
7. Verifikasi Start Date `29/02/28` dan End Date `28/02/32` (29/02/32 ada sehingga tanggal ulang tahun 29/02/32, lalu dikurangi 1 hari)
8. Verifikasi Reserve disesuaikan menjadi $12,000.00 (dibaca lewat fixture BE)
9. Verifikasi status tetap Pending
10. Kembali ke List lewat sidebar Allocation > Client Subscription
11. Ketik Search `Client Tanpa Subscription+{runId}-147`, tekan Enter
12. Klik ikon `⋯` pada baris term Pending, lalu pilih `Edit`
13. Ubah Duration dari `4` menjadi `1`
14. Klik `[Save]`
15. Verifikasi toast sukses "Success, subscription has been updated." muncul
16. Buka Detail term dengan klik baris term
17. Verifikasi End Date `27/02/29` (29/02/29 tidak ada sehingga tanggal ulang tahun 28/02/29, lalu dikurangi 1 hari)
18. Verifikasi Reserve disesuaikan menjadi $3,000.00 (dibaca lewat fixture BE)
19. Verifikasi status tetap Pending

## Notes

- TC-AC-CS-579 (pembuat term) ada di spec 036.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; langkah 1, 11), dan kembali ke List lewat sidebar (langkah 10; klik sidebar mereset Search, Sort, dan Filter).
- Toast pada langkah 15 (Save Duration `1`) adalah asersi tambahan sebagai anchor Save selesai sebelum membuka Detail (S-03).
- Temuan untuk QA:
  - TC-AC-CS-584 Expected b tidak menyebut toast untuk Save Duration `1`; langkah 15 adalah asersi tambahan sebagai anchor.
  - Tabel Data Uji Dinamis #8 dibuat TC-AC-CS-579 (dependensi); spec ini membangun state itu lewat seeding API.
