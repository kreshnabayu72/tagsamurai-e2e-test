---
id: TC-AC-CS-E2E-039-add-distributor-biaya-nol-renewal-rank-lebih-rendah-dan-new
title: "Add: Distributor Biaya Nol, Renewal Rank Lebih Rendah, dan New Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-155
  - TC-AC-CS-153
  - TC-AC-CS-174
  - TC-AC-CS-175
coverage:
  web: automated
---

# Add: Distributor Biaya Nol, Renewal Rank Lebih Rendah, dan New Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor PT Maju Bersama (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Akun kedua (ganti akun eksplisit, TC-AC-CS-175): Create pada Manage allocation dan Manage active client, Distributor PT Maju Bersama (Pre-setup #92) `createClientSub_automated_{namaCompany}@qwertysystem.net` (`Bayu Setiawan`), password `Spectra.env.AC_SUB_CREATECLIENT_PASSWORD`; kembali ke akun pertama (#9) sebagai approver.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`, beserta term, Client, dan Default User yang dibuat spec): Client `Client Tanpa Subscription+{runId}-039` (padanan Pre-setup #48) dan Custom Plan FAMS `Maju Nol` milik PT Maju Bersama dengan harga setiap feature $0.00 per tahun (Pre-setup #135) untuk TC-AC-CS-155; Client `Warung Kopi Senja+{runId}-039` dengan term Active FAMS plan Professional $10,000.00 per tahun (Captured), Start Date 01/09/25, End Date 31/08/26, Plan Owner PT Maju Bersama, tanpa successor (padanan Pre-setup #69) untuk TC-AC-CS-153; Company Name Client baru `Toko Baru Sentosa+{runId}-039` (TC-AC-CS-174) dan `Toko Baru Makmur+{runId}-039` (TC-AC-CS-175).
- Nilai field wajib lain form inline Client baru (PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, Division; `client/PRD/client.md` §4.2d dan F-ACC-02; form inline tidak punya field Position) dirujuk lewat `Fixture.license-allocation-subscription` dengan nilai valid sesuai master data dan email bersuffix `+{runId}-039`.
- Wallet: `Main Pocket` PT Maju Bersama saldo tersedia $25,000.00 (Pre-setup #20); harga FAMS Growth $4,000.00 per tahun dan FAMS Professional $10,000.00 per tahun (Pre-setup #27). Saldo dibaca lewat fixture BE dan dipulihkan di hook `after`.
- State global yang diubah dan pemulihannya (suite serial): toggle `Require Approval for Allocation` PT Maju Bersama (Pre-setup #23) diatur ON pada langkah 30 lewat fixture BE (TC-AC-CS-175) dan dipulihkan di hook `after`.

## Test Steps

### TC-AC-CS-155: Add dengan biaya $0 diproses tanpa Reserve dan Capture

1. Baca saldo `Main Pocket` lewat fixture BE sebagai baseline
2. Klik `[+ Subscription]`
3. Pilih Client `Client Tanpa Subscription+{runId}-039`, Product `FAMS`, Plan `Maju Nol`, Duration `1`, Start Date `19/08/26`
4. Verifikasi preview menampilkan "Estimated Cost: $0.00 (1 year(s) × $0.00/year)"
5. Verifikasi tidak ada Alert Danger V-11 maupun tooltip V-15
6. Klik `[Submit]`
7. Verifikasi toast sukses "Success, subscription has been added." muncul
8. Ketik Search `Client Tanpa Subscription+{runId}-039`, tekan Enter
9. Verifikasi term plan `Maju Nol` berstatus Active
10. Verifikasi Plan Owner `PT Maju Bersama (Distributor)`
11. Verifikasi saldo `Main Pocket` tetap sama dengan baseline $25,000.00, tanpa Reserve maupun Capture
12. Klik `(←)` pada kotak Search

### TC-AC-CS-153: Renewal ke rank lebih rendah dikenai charge penuh tanpa refund selisih

13. Ketik Search `Warung Kopi Senja+{runId}-039`, tekan Enter
14. Klik ikon `⋯` pada baris term Active, lalu pilih `Renew`
15. Pilih Renewal Option `Change plan`, pilih Plan `Growth`, isi Duration `1`
16. Verifikasi Estimated Cost "$4,000.00 (1 year(s) × $4,000.00/year)" dibebankan penuh
17. Klik `[Submit]`
18. Verifikasi Submit berhasil dengan toast sukses "Success, your renewal has been scheduled and will take effect on 01/09/26."
19. Verifikasi saldo `Main Pocket` berkurang tepat $4,000.00 tanpa pengembalian selisih dari term Professional lama (dibaca lewat fixture BE)
20. Klik `(←)` pada kotak Search, lalu pulihkan saldo `Main Pocket` ke $25,000.00 lewat fixture BE

### TC-AC-CS-174: Opsi `[+ New Client]` membuat Client, Default User, dan term sekaligus

21. Klik `[+ Subscription]`, lalu buka dropdown Client dan pilih `[+ New Client]`
22. Verifikasi form Create Client inline dengan field wajib Create tampil
23. Isi field wajib form inline Client baru dengan Company Name `Toko Baru Sentosa+{runId}-039`
24. Pilih Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
25. Klik `[Submit]`
26. Tunggu aksi selesai (dialog/modal tertutup)
27. Verifikasi Client `Toko Baru Sentosa+{runId}-039` dan Default User dibuat bersamaan dengan term (dibaca lewat fixture BE)
28. Ketik Search `Toko Baru Sentosa+{runId}-039`, tekan Enter
29. Verifikasi term SAMS baru tampil di tab `Current`
30. Klik `(←)` pada kotak Search, lalu atur toggle `Require Approval for Allocation` PT Maju Bersama ON lewat fixture BE

### TC-AC-CS-175: Client baru dan Default User tidak di-rollback saat pengajuan akhirnya ditolak

31. Logout, lalu login sebagai `Bayu Setiawan` (Pre-setup #92)
32. Buka menu Allocation > Client Subscription
33. Klik `[+ Subscription]`, lalu buka dropdown Client dan pilih `[+ New Client]`
34. Verifikasi form Create Client inline dengan field wajib Create tampil
35. Isi field wajib form inline Client baru dengan Company Name `Toko Baru Makmur+{runId}-039`, lalu pilih Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
36. Klik `[Submit]`
37. Tunggu aksi selesai (dialog/modal tertutup)
38. Logout, lalu login sebagai Total Control Distributor `Eko Saputra` (Pre-setup #9)
39. Buka Approvals > Client Subscription dari sidebar
40. Pilih radio Reject pada pengajuan Client `Toko Baru Makmur+{runId}-039`
41. Isi `Rejection Reason` dengan `Identitas Client belum terverifikasi`
42. Klik `[Submit Decision]`
43. Konfirmasi pada dialog Konfirmasi Reject
44. Tunggu aksi selesai (dialog/modal tertutup)
45. Buka Allocation > Client Subscription dari sidebar, lalu klik tab `History`
46. Ketik Search `Toko Baru Makmur+{runId}-039`, tekan Enter
47. Verifikasi term berstatus Rejected tampil di tab `History`
48. Buka Client List dari sidebar
49. Verifikasi Client `Toko Baru Makmur+{runId}-039` dan Default User-nya tetap ada tanpa subscription
50. Verifikasi tidak ada rollback pembuatan Client (Client dan Default User masih ada, dibaca lewat fixture BE)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan: aksi tanpa ganti akun lebih dulu, TC-AC-CS-175 dengan ganti akun di akhir (S-10).
- Langkah penghubung (S-03): baseline saldo (langkah 1), Search untuk menemukan baris target (R-16; langkah 8, 13, 28, 46), `(←)` pada kotak Search (langkah 12, 20, 30), pemulihan saldo dan pengaturan toggle lewat fixture BE (langkah 20 dan 30; pengecualian suite 2026-10-30), dan pindah halaman lewat sidebar (langkah 39, 45, 48).
- Ganti akun eksplisit di langkah 31 dan 38 (S-07); langkah 32 membuka menu Allocation > Client Subscription sesudah login. `Tunggu aksi selesai (dialog/modal tertutup)` sesudah Submit dan konfirmasi tanpa asersi hasil (langkah 26, 37, 44; 8b.8). Aksi Reject oleh approver pada langkah 40 sampai 44 adalah bagian alur TC-AC-CS-175 Langkah 3, bukan sesi API.
- Ukuran: 50 langkah, di atas 35 langkah. Alasan pertahanan: semua blok satu kelas (fungsional Add oleh Distributor), tiap blok memakai Client dan Plan seed sendiri dan tidak bergantung pada blok lain, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pemecahan lebih lanjut menambah login dan hook tanpa menambah isolasi.
- Temuan untuk QA:
  - TC-AC-CS-174 dan TC-AC-CS-175 tidak menyebut nilai field wajib form inline Client baru; ditulis sebagai fixture "disediakan tim FE" dan form inline tidak punya field Position (F-ACC-02).
  - TC-AC-CS-175 Precondition menyebut aktor Create-Only dengan akun `Bayu Setiawan` yang juga punya Create pada Manage active client; spec mengikuti Precondition.
  - TC-AC-CS-153 Expected c "Submit tetap berhasil" tidak menyebut teks toast; spec memakai toast baku T-09 yang dinyatakan TC-AC-CS-148 untuk Renew terjadwal.
  - TC-AC-CS-174 Expected a "Client dan Default User dibuat bersamaan" tidak menyebut surface pengecekan; spec memakai pembacaan lewat fixture BE.
