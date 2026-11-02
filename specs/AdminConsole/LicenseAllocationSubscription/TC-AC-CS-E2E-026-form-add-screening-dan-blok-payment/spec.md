---
id: TC-AC-CS-E2E-026-form-add-screening-dan-blok-payment
title: "Form Add: Screening dan Blok Payment"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-101
  - TC-AC-CS-618
  - TC-AC-CS-534
  - TC-AC-CS-139
  - TC-AC-CS-102
coverage:
  web: automated
---

# Form Add: Screening dan Blok Payment

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit di langkah): Total Control Distributor PT Maju Bersama (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (General Settings Principal: Date Format `dd/MM/yy`, Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-026` (padanan Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term dan tanpa trial) untuk TC-AC-CS-139, dan Client `Client Tanpa Subscription B+{runId}-026` (kondisi sama) untuk TC-AC-CS-102 agar term hasil TC-AC-CS-139 tidak memengaruhi opsi Product; Client `Warung Kopi Senja+{runId}-026` dengan satu term Active FAMS plan Professional, Start Date 01/09/25, End Date 31/08/26, Plan Owner PT Maju Bersama (padanan Pre-setup #69), tanpa successor dan tanpa trial aktif (hanya untuk membuka form Renew pada TC-AC-CS-534).
- Wallet: Distributor PT Maju Bersama dengan satu kantong `Main Pocket` saldo tersedia $25,000.00 (Pre-setup #20); harga FAMS Professional $10,000.00 per tahun (Pre-setup #27). Saldo dibaca lewat fixture BE (kemampuan disediakan tim FE/BE) dan dipulihkan di hook `after`. Submit pada TC-AC-CS-139 membuat satu term milik Principal pada Client seed; term itu dihapus di hook `after`.

## Test Steps

### TC-AC-CS-101: Screening modal Add Subscription oleh Principal

1. Klik `[+ Subscription]` di toolbar
2. Verifikasi header modal berjudul "Add Subscription" dengan tombol silang `[✕]` di kanan atas
3. Verifikasi field berurutan: Client * (Searchable dropdown, placeholder "Select client"), Product * (placeholder "Select product"), Plan * (placeholder "Select plan"), Duration * (stepper dengan addon `year(s)`, helper "Whole years, minimum 1"), Start Date * (placeholder "Select date", helper "Cannot be earlier than today")
4. Verifikasi field Renewal Option tidak dirender
5. Verifikasi field Pay From dan blok Payment tidak dirender karena aktor Principal
6. Verifikasi Preview term baru dan Alert info efek belum tampil sebelum Plan, Duration, dan Start Date terisi
7. Verifikasi footer: checkbox "Stay on this form after submitting" rata kanan, lalu baris `[Clear Field]` dan `[Submit]` rata kanan

### TC-AC-CS-618: Nilai awal form Add Subscription

8. Amati nilai awal tiap field pada modal yang sama tanpa mengubah apa pun
9. Verifikasi Duration bernilai `1`
10. Verifikasi Start Date bernilai hari ini `19/08/26`
11. Verifikasi Client, Product, dan Plan belum berisi pilihan
12. Verifikasi Pay From tidak dirender bagi Principal
13. Verifikasi Alert info efek belum tampil karena Plan belum terisi

### TC-AC-CS-534: Form `+ Subscription` tidak memiliki field pemilih mode

14. Amati seluruh field form Add Subscription
15. Verifikasi tidak ada field pemilih mode New atau Renewal pada form Add Subscription
16. Klik `[✕]` pada header modal
17. Ketik Search `Warung Kopi Senja+{runId}-026`, tekan Enter
18. Klik ikon `⋯` pada baris Client `Warung Kopi Senja+{runId}-026`, lalu pilih `Renew`
19. Amati seluruh field form Renew Subscription
20. Verifikasi tidak ada field pemilih mode New atau Renewal pada form Renew Subscription
21. Verifikasi mode ditentukan pintu: toolbar `[+ Subscription]` = New, row action `Renew` = Renewal
22. Klik `[✕]` pada header modal
23. Klik `(←)` pada kotak Search

### TC-AC-CS-139: Principal tidak melihat Pay From maupun Payment

24. Baca saldo `Main Pocket` PT Maju Bersama lewat fixture BE sebagai baseline
25. Klik `[+ Subscription]`, lalu isi Client `Client Tanpa Subscription+{runId}-026`, Product `FAMS`, Plan `Professional`, Duration `2`
26. Verifikasi field Pay From tidak dirender
27. Verifikasi Estimated Cost dan Pocket Balance tidak tampil
28. Klik `[Submit]`
29. Verifikasi toast sukses "Success, subscription has been added." muncul
30. Verifikasi saldo `Main Pocket` sama dengan baseline, tanpa Reserve dan tanpa Capture pada Wallet

### TC-AC-CS-102: Screening modal Add Subscription oleh Distributor memuat blok Payment

31. Logout, lalu login sebagai Total Control Distributor `Eko Saputra` (Pre-setup #9)
32. Buka menu Allocation > Client Subscription
33. Klik `[+ Subscription]`
34. Verifikasi header modal berjudul "Add Subscription"
35. Isi Client `Client Tanpa Subscription B+{runId}-026`, Product `FAMS`, Plan `Professional`, Duration `2`, Start Date `19/08/26`
36. Verifikasi field Pay From * (Dropdown, helper "Wallet pocket charged for this subscription") tampil Disabled dan terisi `Main Pocket`
37. Verifikasi tampil "Estimated Cost: $20,000.00 (2 year(s) × $10,000.00/year)" dan "Your pocket balance: $25,000.00"
38. Verifikasi Alert info efek tampil di atas footer
39. Verifikasi footer: checkbox "Stay on this form after submitting" rata kanan, lalu baris `[Clear Field]` dan `[Submit]` rata kanan
40. Klik `[✕]` pada header modal
41. Verifikasi dialog Unsaved Changes tampil
42. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular; TC-AC-CS-618 memakai modal yang sama dengan TC-AC-CS-101 (satu pembukaan form untuk kasus tanpa submit).
- Langkah penghubung (S-03): `[✕]` pada form bersih (langkah 16, 22; tanpa dialog), Search untuk menemukan baris target (R-16, langkah 17), `(←)` pada kotak Search (langkah 23), menu Allocation sesudah ganti akun (langkah 32), mengisi form pada langkah 25 dan 35, dan membaca saldo baseline (langkah 24).
- Penutupan form dirty pada langkah 40 sampai 42 mengikuti S-08.
- Urutan: screening bersih lebih dulu, aksi Submit (TC-AC-CS-139) sesudahnya, ganti akun di akhir (S-10).
- TC-AC-CS-139 memicu pembuatan satu term oleh Principal; efek pada Client seed dibersihkan di hook `after`.
- Ukuran: 42 langkah, di atas 35 langkah. Alasan: semua blok satu kelas (screening form Add), memakai Client seed terpisah per blok, dan kegagalan satu blok screening tidak membuat blok lain kehilangan makna; langkah sebagian besar berupa Verifikasi per klausa Expected (S-01) dan bukan aksi berulang.
- Temuan untuk QA:
  - TC-AC-CS-102 dan TC-AC-CS-139 memakai Client Pre-setup #48 yang sama dengan Product dan Plan yang sama; TC-AC-CS-139 membuat term FAMS sehingga FAMS tidak lagi ditawarkan untuk Client itu. Spec memakai dua Client seed.
  - TC-AC-CS-102 tidak menyebut teks Alert info efek untuk Total Control Distributor; spec hanya mengasersi keberadaannya di atas footer sesuai Expected.
