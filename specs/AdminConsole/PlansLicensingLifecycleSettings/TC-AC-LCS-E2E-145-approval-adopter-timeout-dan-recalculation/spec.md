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
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-508: Pengajuan Device Allocation baru memakai Approval Timeout saat diajukan dan auto-cancel setelah batas

1. Klik tab `Approval Settings`
2. Ubah Approval Timeout dari `3` menjadi `2`
3. Klik `[Save]` dan tunggu toast sukses
4. Ajukan Device Allocation yang memerlukan approval lewat sesi API aktor lain hingga tersimpan berstatus `Waiting for Approval`
5. Majukan jam server dan jam browser 2 hari lewat Fixture BE, lalu picu job Timeout Auto-Cancel modul Device Allocation
6. Buka pengajuan Device Allocation tersebut
7. Verifikasi status pengajuan `Canceled`
8. Verifikasi log pengajuan memuat "Canceled by system (approval timeout — no decision within 2 days)"
9. Verifikasi pemohon menerima notifikasi pembatalan
10. Verifikasi approver aktif menerima notifikasi pembatalan

### TC-AC-LCS-509: Save Approval Timeout menghitung ulang batas pengajuan Waiting for Approval yang sudah ada

11. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 1 hari lalu (batas awal 3 hari)
12. Klik tab `Approval Settings`
13. Ubah Approval Timeout dari `3` menjadi `2`
14. Klik `[Save]` dan tunggu toast sukses
15. Tunggu Recalculate Job modul Device Allocation selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
16. Majukan jam server dan jam browser hingga 2 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel
17. Buka pengajuan Device Allocation tersebut
18. Verifikasi status pengajuan `Canceled` pada batas 2 hari sejak pengajuan awal (batas lama 3 hari tidak berlaku)

### TC-AC-LCS-510: Batas baru kurang dari 24 jam mengirim ulang warning H-24 seketika

19. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 36 jam lalu (batas awal 3 hari, belum menerima warning H-24)
20. Klik tab `Approval Settings`
21. Ubah Approval Timeout dari `3` menjadi `2`
22. Klik `[Save]` dan tunggu toast sukses
23. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
24. Verifikasi warning H-24 terkirim ke approver aktif segera setelah recalculation, tanpa menunggu siklus pemeriksaan berkala
25. Verifikasi warning H-24 terkirim ke pemohon segera setelah recalculation, tanpa menunggu siklus pemeriksaan berkala

### TC-AC-LCS-511: Batas baru yang sudah terlewat mendapat toleransi 24 jam dari waktu simpan dan tidak auto-cancel instan

26. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 2,5 hari lalu (batas awal 3 hari)
27. Klik tab `Approval Settings`
28. Ubah Approval Timeout dari `3` menjadi `1`
29. Klik `[Save]` dan tunggu toast sukses
30. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
31. Buka pengajuan Device Allocation tersebut
32. Verifikasi status pengajuan tetap `Waiting for Approval`
33. Verifikasi warning H-24 terkirim
34. Majukan jam server dan jam browser 23 jam lewat Fixture BE, lalu picu job Timeout Auto-Cancel
35. Verifikasi status pengajuan tetap `Waiting for Approval`
36. Majukan jam server dan jam browser 2 jam lagi lewat Fixture BE, lalu picu job Timeout Auto-Cancel
37. Verifikasi status pengajuan `Canceled` (batas sama dengan waktu simpan ditambah 24 jam)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC), "Atur lewat Fixture BE ..." (precondition TC), "Tunggu Recalculate Job ..." (idiom polling kueri status job, batas 2 menit), "Majukan jam ..." dan "Pulihkan ..." antar TC (S-03, S-09, R-10).
- Alasan lebih dari sekitar 35 langkah: empat blok memakai pola yang sama (Save Approval Timeout lalu majukan jam dan picu job), semuanya satu kelas harness yang sama, dan tiap blok diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-AC-LCS-508 menulis "→ status `Waiting for Approval`" pada langkah pengajuan tanpa menjadikannya Expected; spec tidak mengasersinya (S-02). Mekanisme job Recalculate dan Timeout Auto-Cancel, kueri status job, dan pembacaan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
