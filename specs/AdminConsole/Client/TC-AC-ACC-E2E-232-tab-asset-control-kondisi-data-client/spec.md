---
id: TC-AC-ACC-E2E-232-tab-asset-control-kondisi-data-client
title: "Tab Asset Control Tampil Tanpa Dibatasi Subscription dan Plan, Empty State, dan Reader Name Alias"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-306
  - TC-AC-ACC-337
  - TC-AC-ACC-892
  - TC-AC-ACC-893
  - TC-AC-ACC-894
coverage:
  web: automated
---

# Tab Asset Control Tampil Tanpa Dibatasi Subscription dan Plan, Empty State, dan Reader Name Alias

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup: C-10 "PT Lintas Jaringan" (TC-AC-ACC-337, dibaca saja; Tabel A2 mencatat kuota Asset Control Total 1 / Used 1 / Available 0).
- Data fixture Tabel A3 (hanya dibaca, tidak diubah): C-AST-4 "PT Uji Reader Alias" (Asset Control Total 2 / Used 2; Station Active #1 dari SFR Alias Name "Alias Gudang" dengan Device Name "SFR-200-A"; Station Active #2 dari SFR tanpa Alias Name dengan Device Name "SFR-200-B").
- Data Dinamis milik spec (kembaran fixture; skrip seed di hook `before`, bukan lewat UI; dihapus di hook `after`; Generate Enrollment QR menulis token Active sehingga spec tidak memakai C-AST-2 dan C-AST-3 bersama [S-06]; Company Name bersuffix `{runId}-232`, atribut setara baris fixture asal di Tabel A3 (Partner CV Mitra Sejati; Group Area Jakarta; FAMS Active), nama SFR, Station, dan Tablet di dalam kembaran sama dengan fixture asal karena terlingkup pada Client kembaran):
  - "PT Paket Free {runId}-232" (kembaran C-AST-2, TC-AC-ACC-892): Active; FAMS Active plan Free; Asset Control Total 2 / Used 0 / Available 2; Storage Total 5 GB / Used 0 GB; tanpa token Enrollment QR Active; dengan SFR bertipe Asset Control tanpa station aktif disediakan tim FE.
  - "PT Paket Enterprise {runId}-232" (kembaran C-AST-3, TC-AC-ACC-893): Active; FAMS Active plan Enterprise; kuota dan Storage sama dengan kembaran Free; tanpa token Active; dengan SFR bertipe Asset Control tanpa station aktif disediakan tim FE.
- Data Dinamis milik spec (dibuat lewat API seeding di hook `before`, dihapus di `after`): Client "PT Tanpa Subscription {runId}-232" (belum pernah memiliki subscription, kuota Asset Control 0) untuk TC-AC-ACC-306; Client "PT Station Tanpa Tablet {runId}-232" dengan satu Station tanpa tablet untuk TC-AC-ACC-337 (nama Station disediakan tim FE).
- Kemampuan teknis: penambahan kuota Asset Control lewat License Allocation (sesi API aktor, disediakan tim FE/BE); jam server dapat dimajukan (pemulihan token Active hasil TC-AC-ACC-892 dan TC-AC-ACC-893 ke Expired dengan memajukan jam server 15 menit di hook `after`, lalu jam dipulihkan).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- State global: jam server dimajukan lalu dipulihkan di hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-306: Tab Asset Control tampil tanpa dipengaruhi status subscription produk

1. Ketik Search "PT Tanpa Subscription {runId}-232" di List Client, tekan Enter, lalu klik Company Name hasilnya
2. Verifikasi Tab Asset Control tampil di navigasi tab
3. Tambahkan kuota Asset Control sebesar 2 untuk Client itu lewat License Allocation tanpa subscription aktif hingga kuota tersimpan
4. Muat ulang Detail (F5)
5. Verifikasi Tab Asset Control tampil di navigasi tab
6. Klik Tab Asset Control
7. Verifikasi Station Quota menampilkan Total 2

### TC-AC-ACC-337: Empty state Station List dan Tablet List

8. Klik breadcrumb "Client", ketik Search "PT Lintas Jaringan", tekan Enter, lalu klik Company Name "PT Lintas Jaringan"
9. Klik Tab Asset Control
10. Verifikasi empty state Station List: "No stations registered" dengan deskripsi "Stations will appear here once the client sets up their Asset Control readers."
11. Klik breadcrumb "Client", ketik Search "PT Station Tanpa Tablet {runId}-232", tekan Enter, lalu klik Company Name hasilnya
12. Klik Tab Asset Control
13. Klik row Station tanpa tablet untuk expand Tablet List
14. Verifikasi empty state Tablet List: "No tablets connected to this station" dengan deskripsi "Tablets registered to this station will appear here."

### TC-AC-ACC-892: Client plan Free

15. Klik breadcrumb "Client", ketik Search "PT Paket Free {runId}-232", tekan Enter, lalu klik Company Name "PT Paket Free {runId}-232"
16. Verifikasi navigasi tab memuat `Subscription`, `TAG`, `Hardware`, `Asset Control`, `Storage`
17. Klik Tab Asset Control
18. Verifikasi Station Quota: Total 2, Used 0, Available 2
19. Verifikasi tombol [Generate Enrollment QR] tampil dan aktif
20. Klik [Generate Enrollment QR]
21. Verifikasi dialog dengan Title "Enrollment QR" tampil (tanpa dialog blok)
22. Klik [Close]
23. Klik Tab Storage
24. Verifikasi Tab Storage tampil dengan Quota Total (GB) 5, Used (GB) 0, Available (GB) 5

### TC-AC-ACC-893: Client plan Enterprise

25. Klik breadcrumb "Client", ketik Search "PT Paket Enterprise {runId}-232", tekan Enter, lalu klik Company Name "PT Paket Enterprise {runId}-232"
26. Verifikasi navigasi tab memuat `Subscription`, `TAG`, `Hardware`, `Asset Control`, `Storage`
27. Klik Tab Asset Control
28. Verifikasi Station Quota: Total 2, Used 0, Available 2
29. Verifikasi tombol [Generate Enrollment QR] tampil dan aktif
30. Klik [Generate Enrollment QR]
31. Verifikasi dialog dengan Title "Enrollment QR" tampil (tanpa dialog blok)
32. Klik [Close]
33. Klik Tab Storage
34. Verifikasi Tab Storage tampil dengan Quota Total (GB) 5, Used (GB) 0, Available (GB) 5

### TC-AC-ACC-894: Reader Name memakai Alias Name SFR dan fallback ke Device Name

35. Klik breadcrumb "Client", ketik Search "PT Uji Reader Alias", tekan Enter, lalu klik Company Name "PT Uji Reader Alias"
36. Klik Tab Asset Control
37. Verifikasi baris SFR pertama menampilkan Reader Name "Alias Gudang" (Alias Name)
38. Verifikasi baris SFR kedua menampilkan Reader Name "SFR-200-B" (Device Name karena Alias Name kosong)

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 8, 11, 15, 25, 35 (Search dan buka Detail Client; hook suite hanya membuka List Client) serta klik breadcrumb "Client" yang mengembalikan ke List; langkah 22 dan 32 (menutup dialog Enrollment QR).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas (baca atas Tab Asset Control tiap Client, aksi hanya membuka dialog Enrollment QR) dan tiap blok memakai Client sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Replika S-06 [KEPUTUSAN 2026-11-03]: aksi [Generate Enrollment QR] pada TC-AC-ACC-892 dan 893 menulis token Active, sehingga spec memakai kembaran C-AST-2 dan C-AST-3 bersuffix `{runId}-232` (seed di `before`, cleanup di `after`); C-10 dan C-AST-4 hanya dibaca dan tetap memakai fixture asal.
- Temuan untuk QA:
  - TC-AC-ACC-306 memakai "PT Baru Daftar" (Pre-setup C-09, dipakai juga untuk Delete di spec lain) dan Step 3 menambah kuota Asset Control; spec memakai Client milik sendiri bersuffix agar C-09 tidak berubah. Besaran alokasi kuota tidak disebut TC (Expected "Total sesuai alokasi"); spec memakai 2.
  - TC-AC-ACC-337 langkah 2 ("Expand Station tanpa tablet") tidak punya Station tanpa tablet di Pre-setup C-10 "PT Lintas Jaringan" (Tabel A2 mencatat Used 1 tetapi Expected langkah 1 adalah "No stations registered"); spec memakai Client milik sendiri untuk empty state Tablet List. Precondition TC perlu dilengkapi.
  - TC-AC-ACC-892 dan TC-AC-ACC-893 tidak punya Post Condition pemulihan token Active hasil klik [Generate Enrollment QR]; spec memulihkan lewat memajukan jam server 15 menit di hook `after` (pola Post Condition TC-AC-ACC-896).
  - TC-AC-ACC-892 dan TC-AC-ACC-893 menegaskan dialog "Enrollment QR" tampil tanpa dialog blok, tetapi data C-AST-2 dan C-AST-3 tidak menyebut SFR bertipe Asset Control tanpa station aktif yang memenuhi syarat; spec mengandalkan SFR yang disediakan tim FE (lihat Prerequisites).
