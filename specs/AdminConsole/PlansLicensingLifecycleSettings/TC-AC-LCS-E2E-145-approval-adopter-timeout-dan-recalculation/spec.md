---
id: TC-AC-LCS-E2E-145-approval-adopter-timeout-dan-recalculation
title: "Approval Settings Konsumen: Timeout Auto-Cancel, Recalculation Batas, dan Warning H-24 pada Device Allocation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-508
  - TC-AC-LCS-509
  - TC-AC-LCS-510
  - TC-AC-LCS-511
coverage:
  web: automated
---

# Approval Settings Konsumen: Timeout Auto-Cancel, Recalculation Batas, dan Warning H-24 pada Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Device Allocation uji berstatus `Waiting for Approval` diajukan oleh aktor lain; umur pengajuan diatur per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC). Akun pemohon dan approver aktif disediakan tim FE (tidak tertulis di Pre-setup TC); notifikasi keduanya dibaca lewat kemampuan baca notifikasi yang mengembalikan jumlah notifikasi per penerima (pemohon dan approver aktif).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan membaca notifikasi pemohon dan approver aktif, serta sesi API aktor lain untuk mengajukan Device Allocation.
- Waktu: jam server dan jam browser dimajukan bersama (countdown UI berjalan di jam klien); jam dipulihkan sesudah tiap TC (S-09, R-08). Jam yang dimajukan dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` suite (S-09); suite berjalan serial (`parallel: false`) karena spec ini memakai state global (jam, job, konfigurasi tab).
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-508: Pengajuan Device Allocation baru memakai Approval Timeout saat diajukan dan auto-cancel setelah batas

1. Klik tab `Approval Settings`
2. Ubah Approval Timeout dari `3` menjadi `2`
3. Klik `[Save]` dan tunggu toast sukses
4. Ajukan Device Allocation yang memerlukan approval lewat sesi API aktor lain hingga tersimpan berstatus `Waiting for Approval`
5. Catat jumlah notifikasi pemohon lewat kemampuan baca notifikasi sebagai baseline
6. Catat jumlah notifikasi approver aktif lewat kemampuan baca notifikasi sebagai baseline
7. Majukan jam server dan jam browser 2 hari lewat Fixture BE, lalu picu job Timeout Auto-Cancel modul Device Allocation
8. Tunggu aksi selesai
9. Buka halaman daftar pengajuan Device Allocation
10. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
11. Buka pengajuan Device Allocation tersebut
12. Verifikasi status pengajuan `Canceled`
13. Verifikasi log pengajuan memuat "Canceled by system (approval timeout — no decision within 2 days)"
14. Verifikasi jumlah notifikasi pembatalan pemohon bertambah tepat satu dari baseline
15. Verifikasi jumlah notifikasi pembatalan approver aktif bertambah tepat satu dari baseline

### TC-AC-LCS-509: Save Approval Timeout menghitung ulang batas pengajuan Waiting for Approval yang sudah ada

16. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 1 hari lalu (batas awal 3 hari), lalu buka Plans & Licensing > Lifecycle Settings
17. Klik tab `Approval Settings`
18. Ubah Approval Timeout dari `3` menjadi `2`
19. Klik `[Save]` dan tunggu toast sukses
20. Tunggu Recalculate Job modul Device Allocation selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
21. Majukan jam server dan jam browser hingga 2 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel
22. Tunggu aksi selesai
23. Buka halaman daftar pengajuan Device Allocation
24. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
25. Buka pengajuan Device Allocation tersebut
26. Verifikasi status pengajuan `Canceled` pada batas 2 hari sejak pengajuan awal (batas lama 3 hari tidak berlaku)

### TC-AC-LCS-510: Batas baru kurang dari 24 jam mengirim ulang warning H-24 seketika

27. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 36 jam lalu (batas awal 3 hari, belum menerima warning H-24), lalu buka Plans & Licensing > Lifecycle Settings
28. Klik tab `Approval Settings`
29. Ubah Approval Timeout dari `3` menjadi `2`
30. Catat jumlah notifikasi approver aktif lewat kemampuan baca notifikasi sebagai baseline
31. Catat jumlah notifikasi pemohon lewat kemampuan baca notifikasi sebagai baseline
32. Klik `[Save]` dan tunggu toast sukses
33. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
34. Verifikasi jumlah notifikasi warning H-24 approver aktif bertambah tepat satu dari baseline segera setelah recalculation, tanpa menunggu siklus pemeriksaan berkala
35. Verifikasi jumlah notifikasi warning H-24 pemohon bertambah tepat satu dari baseline segera setelah recalculation, tanpa menunggu siklus pemeriksaan berkala

### TC-AC-LCS-511: Batas baru yang sudah terlewat mendapat toleransi 24 jam dari waktu simpan dan tidak auto-cancel instan

36. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 2,5 hari lalu (batas awal 3 hari), lalu buka Plans & Licensing > Lifecycle Settings
37. Klik tab `Approval Settings`
38. Ubah Approval Timeout dari `3` menjadi `1`
39. Catat jumlah notifikasi approver aktif lewat kemampuan baca notifikasi sebagai baseline
40. Catat jumlah notifikasi pemohon lewat kemampuan baca notifikasi sebagai baseline
41. Klik `[Save]` dan tunggu toast sukses
42. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
43. Buka halaman daftar pengajuan Device Allocation
44. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
45. Buka pengajuan Device Allocation tersebut
46. Verifikasi status pengajuan tetap `Waiting for Approval`
47. Verifikasi jumlah notifikasi warning H-24 approver aktif bertambah tepat satu dari baseline
48. Verifikasi jumlah notifikasi warning H-24 pemohon bertambah tepat satu dari baseline
49. Majukan jam server dan jam browser 23 jam lewat Fixture BE, lalu picu job Timeout Auto-Cancel
50. Tunggu aksi selesai
51. Muat ulang halaman dan buka ulang pengajuan Device Allocation tersebut
52. Verifikasi status pengajuan tetap `Waiting for Approval`
53. Majukan jam server dan jam browser 2 jam lagi lewat Fixture BE, lalu picu job Timeout Auto-Cancel
54. Tunggu aksi selesai
55. Muat ulang halaman dan buka ulang pengajuan Device Allocation tersebut
56. Verifikasi status pengajuan `Canceled` (batas sama dengan waktu simpan ditambah 24 jam)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC), "Atur lewat Fixture BE ..." (precondition TC), "Tunggu Recalculate Job ..." (idiom polling kueri status job, batas 2 menit), "Majukan jam ..." dan "Pulihkan ..." antar TC, yang pada langkah 16, 27, 36 diakhiri "lalu buka Plans & Licensing > Lifecycle Settings" karena layar terakhir adalah detail pengajuan (S-03, S-07, S-09, R-10); "Buka pengajuan Device Allocation tersebut" (langkah 11, 25, 45) sebelum membaca status atau log di detail pengajuan; "Catat jumlah notifikasi ... sebagai baseline" (langkah 5, 6, 30, 31, 39, 40) sebelum pemicu agar `Verifikasi` notifikasi memakai selisih per penerima (S-12); "Tunggu aksi selesai" (langkah 8, 22, 50, 54) sesudah picu job Timeout Auto-Cancel tanpa asersi, sebelum berpindah surface atau memuat ulang (8b.8); "Buka halaman daftar pengajuan Device Allocation" (langkah 9, 23, 43) sebelum Search pertama tiap blok agar Search dan `Verifikasi` baris berada di halaman yang benar (S-07, R-23); "Muat ulang halaman dan buka ulang pengajuan Device Allocation tersebut" (langkah 51, 55) sebelum membaca status setelah job dipicu lagi agar status tidak dibaca dari detail yang sudah terbuka (8b.5); "Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter" (langkah 10, 24, 44) sebelum membuka pengajuan (R-16, R-23).
- Temuan untuk QA: nama dan jalur menu halaman daftar pengajuan Device Allocation tidak tertulis di TC (TC-AC-LCS-508 sampai 511) maupun PRD; langkah "Buka halaman daftar pengajuan Device Allocation" memakai deskripsi generik sampai TC menetapkan halamannya.
- Temuan untuk QA: TC-AC-LCS-511 menulis "warning H-24 terkirim" tanpa menyebut penerima; spec mengasersi approver aktif dan pemohon seperti TC-AC-LCS-510. Nomor pengajuan Device Allocation uji tidak tertulis di Pre-setup TC; spec memakai nomor hasil seeding Fixture BE.
- Alasan lebih dari sekitar 35 langkah (56 langkah): spec memuat empat TC (TC-AC-LCS-508 sampai 511) dengan 15, 11, 9, dan 21 langkah; TC-AC-LCS-509 sampai 511 diseed ulang lewat Fixture BE di langkah pertamanya (langkah pertama TC-AC-LCS-508 adalah klik tab `Approval Settings`), dan langkah TC-AC-LCS-511 bertambah karena Expected-nya menuntut tiga pembacaan status pada tiga titik jam (setelah Save, setelah 23 jam, setelah 2 jam lagi) yang masing-masing didahului pemicu job, tunggu, dan muat ulang.
- Temuan untuk QA: TC-AC-LCS-508 menulis "→ status `Waiting for Approval`" pada langkah pengajuan tanpa menjadikannya Expected; spec tidak mengasersinya (S-02). Mekanisme job Recalculate dan Timeout Auto-Cancel, kueri status job, dan pembacaan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
