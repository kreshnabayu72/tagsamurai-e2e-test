---
id: TC-AC-LA-E2E-076-job-pada-client-suspended
title: "Job Sistem pada Alokasi Milik Client Suspended"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-278
  - TC-AC-LA-523
  - TC-AC-LA-524
coverage:
  web: automated
---

# Job Sistem pada Alokasi Milik Client Suspended

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: Klinik Beku (#29, status Suspended, FAMS Professional Paid Active), kantong wallet (#33), Product Price (#34), Approval Timeout 3 hari (#40), Data Seed pada Klinik Beku (#71, #78, #79) yang dibuat saat Client Active lalu Client berstatus Suspended.
- Data Dinamis (seeding per blok lewat langkah penghubung pada fixture backend yang disediakan tim FE/BE, bukan di hook `before`, supaya job time-travel satu blok tidak memproses seed blok lain; milik spec ini, tanpa menumpang baris #71, #78, #79): untuk TC-AC-LA-278 satu term successor Renewal FAMS Professional Klinik Beku berstatus Pending (1 Jan 2027 sampai 31 Dec 2027) dengan alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 oleh `Dewi A` (Cost $3,650.00 di-Reserve); untuk TC-AC-LA-523 satu alokasi `Waiting for Approval` Concurrent User +5 (Cost $150.00 di-Reserve); untuk TC-AC-LA-524 satu alokasi `Active` Concurrent User +10 ke FAMS Professional (End Date 31 Dec 2026). Tiap seed dibuat saat Client Active pada langkah pembuka blok, lalu Client diubah ke Suspended oleh fixture backend yang disediakan tim FE/BE; term successor dan seed blok 278 dipulihkan di akhir blok itu. Allocation ID dibaca dari hasil seeding. Hook `after` membersihkan seed yang tersisa.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk mengatur jam server dan jam browser ke nilai absolut (zona waktu Plan Owner), menunggu satu siklus job, dan mengubah status Client Klinik Beku. Jam dipulihkan sebelum membuka log (S-09). Status Client dipulihkan ke keadaan awal di hook `after`.
- Kemampuan baca saldo kantong (Balance, Reserved, Available) Distributor PT Maju Bersama (disediakan tim FE/BE; TC dan PRD tidak menyebut halaman atau endpointnya) dipakai untuk baseline Balance sebelum job berjalan.
- State global yang diubah: jam server dan jam browser, status Client Klinik Beku. Dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-278: Activation Transition tetap berjalan pada alokasi milik Client Suspended

1. Ubah status Client Klinik Beku menjadi aktif lewat fixture backend hingga tersimpan
2. Seed term successor Renewal FAMS Professional Klinik Beku berstatus Pending (1 Jan 2027 sampai 31 Dec 2027) dan alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 oleh `Dewi A` (seed 278, Cost $3,650.00 di-Reserve) saat Client Active, lalu ubah status Client Klinik Beku menjadi Suspended lewat fixture backend hingga tersimpan, dan baca Allocation ID
3. Catat Balance kantong Distributor PT Maju Bersama (dibaca lewat kemampuan baca saldo kantong)
4. Atur jam server dan jam browser ke 1 Jan 2027 (Start Date term), lalu tunggu satu siklus job Activation Transition
5. Pulihkan jam server dan jam browser, buka tab Current, ketik Search Allocation ID seed 278, tekan Enter
6. Verifikasi status alokasi `Active` walau Client berstatus Suspended
7. Klik row action `Allocation Log` pada baris seed 278
8. Verifikasi Allocation Log memuat `Allocation activated` tanpa `by [PIC]`
9. Tutup modal Allocation Log
10. Buka Wallet
11. Verifikasi Reserve $3,650.00 di-Capture (Balance kantong Distributor berkurang $3,650.00 dari Balance yang dicatat sebelum job berjalan)
12. Pulihkan term successor dan seed 278 lewat fixture backend hingga tersimpan

### TC-AC-LA-523: Timeout Auto-Cancel tetap berjalan pada alokasi milik Client Suspended

13. Ubah status Client Klinik Beku menjadi aktif lewat fixture backend hingga tersimpan
14. Seed alokasi `Waiting for Approval` Concurrent User +5 FAMS Professional Klinik Beku oleh `Dewi A` (seed 523, Cost $150.00 di-Reserve) saat Client Active, lalu ubah status Client Klinik Beku menjadi Suspended lewat fixture backend hingga tersimpan, dan baca Allocation ID
15. Catat Balance kantong Distributor PT Maju Bersama (dibaca lewat kemampuan baca saldo kantong)
16. Atur jam server dan jam browser melewati SLA 3 hari seed 523, lalu tunggu satu siklus job Timeout Auto-Cancel
17. Pulihkan jam, buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 523, tekan Enter
18. Verifikasi status alokasi `Canceled` oleh sistem walau Client berstatus Suspended
19. Klik row action `Allocation Log` pada baris seed 523
20. Verifikasi Allocation Log memuat `Allocation auto-canceled` tanpa `by [PIC]`
21. Verifikasi Description `Reason: Approval timeout`
22. Tutup modal Allocation Log
23. Buka Wallet
24. Verifikasi Reserve $150.00 dilepas (Balance kantong sama dengan Balance yang dicatat sebelum job berjalan)

### TC-AC-LA-524: Expiry Transition tetap berjalan pada alokasi milik Client Suspended

25. Ubah status Client Klinik Beku menjadi aktif lewat fixture backend hingga tersimpan
26. Seed alokasi `Active` Concurrent User +10 ke FAMS Professional Klinik Beku (End Date 31 Dec 2026) oleh `Dewi A` (seed 524) saat Client Active, lalu ubah status Client Klinik Beku menjadi Suspended lewat fixture backend hingga tersimpan, dan baca Allocation ID
27. Buka Subscription Detail > License Quota term, lalu catat kuota term sebagai baseline
28. Atur jam server dan jam browser ke 1 Jan 2027 00:01 (zona waktu Plan Owner), lalu tunggu satu siklus job Expiry Transition
29. Pulihkan jam, buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 524, tekan Enter
30. Verifikasi status alokasi `Expired` walau Client berstatus Suspended
31. Verifikasi baris seed 524 berada di tab History
32. Klik row action `Allocation Log` pada baris seed 524
33. Verifikasi Allocation Log memuat `Allocation expired` tanpa `by [PIC]`
34. Verifikasi Description `Reason: Subscription term ended`
35. Tutup modal Allocation Log
36. Buka Subscription Detail > License Quota term
37. Verifikasi kuota term berkurang 10 dari kuota term yang dicatat sebelum job berjalan
38. Buka Wallet
39. Verifikasi Capture atas alokasi seed 524 tampil pada Wallet (anchor)
40. Verifikasi tidak ada refund wallet

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2, 14, 26 (seed per blok saat Client Active lalu Client di-Suspend, lewat fixture backend: job time-travel satu blok tidak boleh memproses seed blok lain, S-09), 1, 13, 25 (memulihkan status Client Klinik Beku menjadi aktif sebelum seed tiap blok, karena Client masih Suspended dari blok sebelumnya atau dari Pre-setup #29 dan seed dibuat saat Client Active), 12 (memulihkan term successor dan seed blok 278), 5, 17, 29 (memulihkan jam sebelum membuka log, S-09; Search dan tab untuk menemukan baris target, R-16; langkah 17 dan 29 membuka List dari Wallet atau Subscription Detail lalu mengetik Search pada kotak yang kosong di halaman yang baru dimuat, tanpa `✕`, S-14), 7, 10, 19, 23, 32, 36, 38, 27 (membuka surface), 3 dan 27 (Catat baseline, S-12).
- Langkah 3 dan 15 (Catat baseline Balance kantong sebelum job berjalan, S-12), langkah 27 (Catat baseline kuota term sebelum job Expiry Transition, S-12), langkah 9, 22, dan 35 (menutup modal Allocation Log sebelum membuka surface lain, S-09) adalah langkah penghubung tanpa Verifikasi. Langkah 39 adalah anchor positif asersi absence `tidak ada refund wallet` pada langkah 40 (entri Capture seed 524 tampil pada Wallet yang sama, 8b butir 2).
- Penyimpangan data (S-06): TC memakai baris Pre-setup #71, #78, #79; spec memakai seed milik spec dengan keadaan yang sama agar Pre-setup bersama tidak berubah. Status Suspended Klinik Beku (#29) diubah menjadi aktif sebelum tiap seed (langkah 1, 13, 25) dan menjadi Suspended lagi pada tiap langkah seed; keadaan awal (Suspended) dipulihkan di hook `after`.
- Spec melewati sekitar 35 langkah (40 langkah). Alasan pertahanan: seluruh blok satu kelas harness (job sistem pada alokasi milik Client Suspended) dengan Client dan dataset yang sama, tiap blok berdiri sendiri dengan seed sendiri yang dibuat pada langkah pembuka blok, dan langkah di atas 35 adalah langkah penghubung (menutup modal) serta anchor Wallet; blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-278, 523, 524 berbagi Pre-setup #71, #78, #79 pada Client yang sama tanpa seed per TC; spec membuat seed per blok.
  - TC-AC-LA-278, 523, 524 menyebut "Tidak ada aktor login saat job berjalan; Total Control Principal membuka List setelahnya"; spec memakai Pre-setup #1 sebagai pengamat sejak hook `before`.
  - TC-AC-LA-524 Expected b ("Kuota term berkurang 10 tanpa refund wallet") tidak menyebut cara pengamatan kuota; spec memakai Subscription Detail > License Quota (modul pemilik di luar modul ini) dan Wallet.
  - TC-AC-LA-278, 523, 524 tidak menyebut akun admin dan mekanisme yang menyetel Client ke Suspended; disediakan tim FE.
