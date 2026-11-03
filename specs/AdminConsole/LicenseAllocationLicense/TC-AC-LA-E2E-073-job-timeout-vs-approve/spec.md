---
id: TC-AC-LA-E2E-073-job-timeout-vs-approve
title: "Job Timeout Auto-Cancel vs Approve pada Batas SLA"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-465
  - TC-AC-LA-485
coverage:
  web: automated
---

# Job Timeout Auto-Cancel vs Approve pada Batas SLA

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38), Approval Timeout 3 hari (#40), Dewi A sebagai requester seed (#4).
- Data Dinamis (seeding per blok lewat langkah penghubung pada fixture backend yang disediakan tim FE/BE, bukan di hook `before`, supaya job time-travel blok TC-AC-LA-465 tidak membatalkan seed blok TC-AC-LA-485; milik spec ini, bentuknya sama dengan Pre-setup #41): satu alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve) per blok, untuk TC-AC-LA-465 dan TC-AC-LA-485. Allocation ID dan waktu Submit (T0) tiap seed dibaca dari hasil seeding. Hook `after` membersihkan seed yang tersisa.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk mengatur jam server dan jam browser ke nilai absolut (T0 + durasi, margin terhadap batas di bawah 5 menit: batas SLA T0 + 3 hari, selisih 1 menit), menunggu satu siklus job. Jam dipulihkan sebelum membuka log (S-09) dan di hook `after`.
- State global yang diubah: jam server dan jam browser; dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-465: Approve menang atas Timeout pada batas SLA

1. Seed alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (seed 465, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
2. Buka Approvals > License Allocation
3. Atur jam server dan jam browser ke T0 seed 465 + 2 hari 23 jam 59 menit
4. Klik `[Review]` pada alokasi seed 465 dan pilih Approve
5. Klik Submit
6. Verifikasi status seed 465 `Completed` berstatus lisensi `Active`
7. Buka Wallet Distributor PT Maju Bersama
8. Verifikasi Reserve seed 465 di-Capture pada Wallet
9. Atur jam server dan jam browser ke T0 seed 465 + 3 hari 1 menit
10. Tunggu satu siklus job
11. Pulihkan jam server dan jam browser ke waktu nyata
12. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed 465, tekan Enter, lalu buka Allocation Log baris itu
13. Verifikasi Allocation Log memuat entri `Allocation approved` (anchor)
14. Verifikasi tidak ada entri `Allocation auto-canceled`
15. Verifikasi status seed 465 tetap `Active`
16. Buka Wallet
17. Verifikasi tidak ada Release atas Reserve seed 465

### TC-AC-LA-485: Approve setelah Timeout Auto-Cancel menampilkan dialog Request No Longer Available

18. Seed alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (seed 485, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
19. Buka Approvals > License Allocation
20. Klik `[Review]` pada alokasi seed 485 dan pilih Approve sebelum SLA 3 hari terlewati
21. Atur jam server dan jam browser ke T0 seed 485 + 3 hari 1 menit
22. Tunggu satu siklus job Timeout Auto-Cancel
23. Pulihkan jam server dan jam browser ke waktu nyata
24. Klik Submit keputusan Approve
25. Verifikasi dialog `Request No Longer Available` tampil
26. Verifikasi keputusan tidak diproses
27. Klik `[OK]` untuk menutup dialog `Request No Longer Available`
28. Buka Allocation > License Allocation tab History, ketik Search Allocation ID seed 485, tekan Enter
29. Verifikasi status seed 485 tetap `Canceled` oleh sistem
30. Buka Wallet
31. Verifikasi tidak ada Capture atas Reserve seed 485
32. Verifikasi Reserve sudah dilepas oleh Timeout (Balance tidak berubah)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 18 (seed per blok lewat fixture backend: job time-travel satu blok tidak boleh membatalkan seed blok lain, S-09), 2 dan 19 (membuka Approvals), 11 dan 23 (memulihkan jam sebelum membuka log atau menekan Submit, S-09), 7 (membuka Wallet sebelum asersi Capture seed 465), 12, 16, 28, 30 (membuka surface dan Search untuk menemukan baris target, R-16), 27 (menutup dialog `Request No Longer Available` dengan `[OK]` sebelum membuka surface lain, S-09).
- Langkah 23 memulihkan jam sebelum Submit; tampilan dialog Review tetap terbuka karena tidak ada penghitung mundur UI yang diasersi.
- Langkah 14 adalah asersi absence dengan anchor positif pada langkah 13 (entri `Allocation approved` pada surface yang sama); langkah 17 beranchor Verifikasi Wallet pada langkah 8.
- P-1: asersi tidak ada entri `Allocation auto-canceled` (langkah 14) dan tidak ada Release (langkah 17) bergantung pada state berat time-travel yang dibangun di spec yang sama; keduanya beranchor positif.
- Temuan untuk QA:
  - TC-AC-LA-465 Langkah 2 ("Klik Submit saat waktu server masih 2 hari 23 jam 59 menit") dan TC-AC-LA-485 Langkah 1 tidak menyebut jam browser; keduanya diatur bersama jam server.
  - TC-AC-LA-465 Expected b ("tidak ada Release") tidak menyebut cara pengamatan; spec memakai Wallet dan Allocation Log.
  - TC-AC-LA-485 tidak menyebut tombol penutup dialog `Request No Longer Available`; langkah 27 memakai `[OK]` sesuai bentuk D-01 pada TC-AC-LA-225.
  - TC-AC-LA-465 dan TC-AC-LA-485 berbagi Pre-setup #41 tanpa seed per TC; spec membuat seed per blok.
  - TC-AC-LA-485 Expected b ("tidak ada Capture") dan c tidak menyebut cara membedakan Reserve dilepas dari Capture selain Balance; spec memakai Wallet.
