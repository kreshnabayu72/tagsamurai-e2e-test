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
- Data: Device Allocation uji berstatus `Waiting for Approval` diajukan oleh aktor lain; umur pengajuan diatur per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC). Akun pemohon dan approver aktif disediakan tim FE (tidak tertulis di Pre-setup TC); notifikasi keduanya dibaca lewat kemampuan baca notifikasi.
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
8. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
9. Buka pengajuan Device Allocation tersebut
10. Verifikasi status pengajuan `Canceled`
11. Verifikasi log pengajuan memuat "Canceled by system (approval timeout — no decision within 2 days)"
12. Verifikasi jumlah notifikasi pembatalan pemohon bertambah tepat satu dari baseline
13. Verifikasi jumlah notifikasi pembatalan approver aktif bertambah tepat satu dari baseline

### TC-AC-LCS-509: Save Approval Timeout menghitung ulang batas pengajuan Waiting for Approval yang sudah ada

14. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 1 hari lalu (batas awal 3 hari)
15. Klik tab `Approval Settings`
16. Ubah Approval Timeout dari `3` menjadi `2`
17. Klik `[Save]` dan tunggu toast sukses
18. Tunggu Recalculate Job modul Device Allocation selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
19. Majukan jam server dan jam browser hingga 2 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel
20. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
21. Buka pengajuan Device Allocation tersebut
22. Verifikasi status pengajuan `Canceled` pada batas 2 hari sejak pengajuan awal (batas lama 3 hari tidak berlaku)

### TC-AC-LCS-510: Batas baru kurang dari 24 jam mengirim ulang warning H-24 seketika

23. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 36 jam lalu (batas awal 3 hari, belum menerima warning H-24)
24. Klik tab `Approval Settings`
25. Ubah Approval Timeout dari `3` menjadi `2`
26. Catat jumlah notifikasi approver aktif lewat kemampuan baca notifikasi sebagai baseline
27. Catat jumlah notifikasi pemohon lewat kemampuan baca notifikasi sebagai baseline
28. Klik `[Save]` dan tunggu toast sukses
29. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
30. Verifikasi jumlah notifikasi warning H-24 approver aktif bertambah tepat satu dari baseline segera setelah recalculation, tanpa menunggu siklus pemeriksaan berkala
31. Verifikasi jumlah notifikasi warning H-24 pemohon bertambah tepat satu dari baseline segera setelah recalculation, tanpa menunggu siklus pemeriksaan berkala

### TC-AC-LCS-511: Batas baru yang sudah terlewat mendapat toleransi 24 jam dari waktu simpan dan tidak auto-cancel instan

32. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 2,5 hari lalu (batas awal 3 hari)
33. Klik tab `Approval Settings`
34. Ubah Approval Timeout dari `3` menjadi `1`
35. Catat jumlah notifikasi approver aktif lewat kemampuan baca notifikasi sebagai baseline
36. Catat jumlah notifikasi pemohon lewat kemampuan baca notifikasi sebagai baseline
37. Klik `[Save]` dan tunggu toast sukses
38. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
39. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
40. Buka pengajuan Device Allocation tersebut
41. Verifikasi status pengajuan tetap `Waiting for Approval`
42. Verifikasi jumlah notifikasi warning H-24 approver aktif bertambah tepat satu dari baseline
43. Verifikasi jumlah notifikasi warning H-24 pemohon bertambah tepat satu dari baseline
44. Majukan jam server dan jam browser 23 jam lewat Fixture BE, lalu picu job Timeout Auto-Cancel
45. Verifikasi status pengajuan tetap `Waiting for Approval`
46. Majukan jam server dan jam browser 2 jam lagi lewat Fixture BE, lalu picu job Timeout Auto-Cancel
47. Verifikasi status pengajuan `Canceled` (batas sama dengan waktu simpan ditambah 24 jam)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC), "Atur lewat Fixture BE ..." (precondition TC), "Tunggu Recalculate Job ..." (idiom polling kueri status job, batas 2 menit), "Majukan jam ..." dan "Pulihkan ..." antar TC (S-03, S-09, R-10); "Catat jumlah notifikasi ... sebagai baseline" (langkah 5, 6, 26, 27, 35, 36) sebelum pemicu agar `Verifikasi` notifikasi memakai selisih per penerima (S-12); "Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter" (langkah 8, 20, 39) sebelum membuka pengajuan (R-16, R-23).
- Temuan untuk QA: TC-AC-LCS-511 menulis "warning H-24 terkirim" tanpa menyebut penerima; spec mengasersi approver aktif dan pemohon seperti TC-AC-LCS-510. Nomor pengajuan Device Allocation uji tidak tertulis di Pre-setup TC; spec memakai nomor hasil seeding Fixture BE.
- Alasan lebih dari sekitar 35 langkah: empat blok memakai pola yang sama (Save Approval Timeout lalu majukan jam dan picu job), semuanya satu kelas harness yang sama, dan tiap blok diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-AC-LCS-508 menulis "→ status `Waiting for Approval`" pada langkah pengajuan tanpa menjadikannya Expected; spec tidak mengasersinya (S-02). Mekanisme job Recalculate dan Timeout Auto-Cancel, kueri status job, dan pembacaan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
