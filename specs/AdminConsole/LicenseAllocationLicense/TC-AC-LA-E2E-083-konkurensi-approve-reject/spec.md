---
id: TC-AC-LA-E2E-083-konkurensi-approve-reject
title: "Konkurensi Approve dan Reject: Keputusan Ganda, Cancel dan Edit Saat Review Terbuka"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-255
  - TC-AC-LA-256
  - TC-AC-LA-257
  - TC-AC-LA-258
coverage:
  web: automated
---

# Konkurensi Approve dan Reject: Keputusan Ganda, Cancel dan Edit Saat Review Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Additional Approver `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` (`Maya Tanjung`, Pre-setup #11), password `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup #41): empat alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve), satu untuk tiap TC (TC-AC-LA-255, 256, 257, 258). Allocation ID dibaca dari hasil seeding.
- Pelaku kedua: sesi API aktor (login API tidak dihitung sebagai sesi web, `suite.md`): requester `Dewi Anggraini` (Cancel dan Edit) dan approver pertama `Fajar Nugroho` (Approve pada TC-AC-LA-255). Maya Tanjung memakai sesi UI karena hasilnya diasersi.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-256: Approve pada alokasi yang dibatalkan requester

1. Buka Approvals > License Allocation
2. Klik `[Review]` pada alokasi seed 256
3. Pelaku kedua (sesi API `Dewi Anggraini`) membatalkan alokasi seed 256 hingga tersimpan
4. Tunggu aksi selesai
5. Pilih Approve dan klik Submit
6. Verifikasi dialog `Request No Longer Available` tampil
7. Verifikasi alokasi seed 256 tidak diproses (status tetap `Canceled`)
8. Klik `[OK]` untuk menutup dialog `Request No Longer Available`

### TC-AC-LA-257: Alokasi diedit setelah Review dibuka, D-05

9. Buka Approvals > License Allocation
10. Klik `[Review]` pada alokasi seed 257
11. Pelaku kedua (sesi API `Dewi Anggraini`) mengubah Quantity alokasi seed 257 dan menyimpannya hingga tersimpan
12. Tunggu aksi selesai
13. Pilih Approve dan klik Submit
14. Verifikasi dialog `Transaction Data Has Changed` dengan Body `The data for this request was changed while you were reviewing it. The latest data has been loaded. Please review it again before deciding.`
15. Verifikasi keputusan tidak diproses (status seed 257 tetap `Waiting for Approval`)
16. Tutup dialog `Transaction Data Has Changed` lewat tombol penutup dialog (disediakan tim FE)

### TC-AC-LA-258: D-01 didahulukan dari D-05

17. Buka Approvals > License Allocation
18. Klik `[Review]` pada alokasi seed 258
19. Pelaku kedua (sesi API `Dewi Anggraini`) membatalkan alokasi seed 258 hingga tersimpan
20. Tunggu aksi selesai
21. Pilih Approve dan klik Submit
22. Verifikasi dialog D-01 `Request No Longer Available` tampil
23. Verifikasi dialog `Transaction Data Has Changed` (D-05) tidak tampil
24. Verifikasi keputusan tidak diproses (status seed 258 tetap `Canceled`)
25. Klik `[OK]` untuk menutup dialog D-01 `Request No Longer Available`

### TC-AC-LA-255: Approve atau Reject ulang pada alokasi yang sudah diputus

26. Ganti akun: logout `Fajar Nugroho`, login sebagai `Maya Tanjung` dengan `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`, lalu buka Approvals > License Allocation
27. Klik `[Review]` pada alokasi seed 255
28. Pelaku kedua (sesi API `Fajar Nugroho`) meng-Approve alokasi seed 255 hingga tersimpan
29. Tunggu aksi selesai
30. Pilih Reject, isi Rejection Reason `Kuota tidak sesuai`, dan klik Submit
31. Verifikasi approver kedua menerima dialog konflik `Approval cannot be made. This has already been resolved.`
32. Verifikasi inbox Approvals di-refresh
33. Verifikasi status seed 255 tetap sesuai keputusan pertama (`Completed`)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor agar blok akun Fajar (TC-AC-LA-256, 257, 258) berurutan sebelum satu kali ganti akun ke Maya (TC-AC-LA-255).
- Langkah penghubung (S-03): langkah 1, 9, 17 (membuka Approvals; 26 juga ganti akun), langkah 4, 12, 20, 29 (menunggu aksi selesai karena berganti sesi, 8b butir 8), langkah 8, 16, 25 (menutup dialog sebelum langkah berikutnya, S-09; `[OK]` pada D-01 mengikuti TC-AC-LA-201 dan 225).
- Pelaku kedua lewat sesi API (langkah 3, 11, 19, 28) tidak memakai butir `P-2` (bagian 3). Sesi UI Maya pada TC-AC-LA-255 adalah akun aktor yang hasilnya diasersi.
- Temuan untuk QA:
  - TC-AC-LA-255 Langkah 1 ("Dua approver membuka Review alokasi yang sama") dan Langkah 2 ("Approver pertama Approve") tidak menyebut akun approver pertama; spec memakai Pre-setup #10 lewat sesi API dan Maya Tanjung (#11) di UI.
  - TC-AC-LA-255 Expected c tidak menyebut keputusan pertama yang tercatat; spec mengasersi status `Completed` (Approve).
  - TC-AC-LA-258 Precondition d ("Alokasi dibatalkan requester kemudian diedit") bertentangan dengan Langkah 2 yang hanya membatalkan dan tidak ada langkah edit; edit atas alokasi Canceled tidak dimungkinkan UI. Spec hanya memicu Cancel.
  - TC-AC-LA-257 dan TC-AC-LA-258 tidak menyebut tombol penutup dialog `Transaction Data Has Changed` dan D-01; spec menutup dialog D-01 dengan `[OK]` (langkah 8, 25, mengikuti TC-AC-LA-201 dan 225) dan dialog D-05 lewat tombol penutup yang disediakan tim FE (langkah 16). Hook `beforeEach` suite berjalan sekali per spec sehingga tidak menutup dialog di antara blok.
  - TC-AC-LA-256 Expected tidak menyebut status akhir; status `Canceled` diturunkan dari pembatalan requester.
