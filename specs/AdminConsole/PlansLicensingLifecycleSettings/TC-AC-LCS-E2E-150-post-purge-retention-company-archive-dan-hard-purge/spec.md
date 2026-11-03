---
id: TC-AC-LCS-E2E-150-post-purge-retention-company-archive-dan-hard-purge
title: "Post-Purge Retention: Company dalam Archive Tidak Terpengaruh dan Hard Purge Memakai Retention Baru"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-528
  - TC-AC-LCS-529
coverage:
  web: automated
---

# Post-Purge Retention: Company dalam Archive Tidak Terpengaruh dan Hard Purge Memakai Retention Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Akun tambahan: Principal berizin Update "Manage archived client" pada Group tempat Client berada atau ancestor-nya (Pre-setup 11); akun `manageArchivedClientPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup 15, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE), env password disediakan tim FE.
- Data: Company PT Lama Sejahtera (`Fixture.lifecycleSettings.clientLamaSejahtera`, sudah di-Hard Purge, email `ops@ptlamasejahtera.example` pada indeks arsip) dan Company PT Baru Sentosa (Pre-setup 10, TC 529; `Fixture.lifecycleSettings.clientBaruSentosa`, mencapai Hard Purge); Client baru yang dibuat spec memakai email milik kedua company itu dan dihapus di langkah penghubung dan hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan membaca Overlay Notifikasi Principal berizin dan mencatat baseline jumlah notifikasinya per penerima (S-12).
- Jendela absence notifikasi in-app: "Tunggu 5 detik tanpa memuat ulang halaman" sebelum asersi absence adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6).
- Waktu: jam server dan jam browser dimajukan bersama pada TC-AC-LCS-529 dan dipulihkan sesudahnya (S-09). Jam yang dimajukan dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` suite (S-09); suite berjalan serial (`parallel: false`) karena spec ini memakai state global (jam, job, konfigurasi tab).
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-528: Company yang sudah dalam Post-Purge Archive tidak terpengaruh perubahan Post-Purge Retention

1. Atur lewat Fixture BE: Company PT Lama Sejahtera sudah di-Hard Purge 250 hari lalu dengan Post-Purge Retention `730` dan emailnya `ops@ptlamasejahtera.example` tercatat pada indeks arsip, dan Principal berizin Update "Manage archived client" tersedia
2. Klik tab `Client Lifecycle`
3. Ubah Post-Purge Retention dari `730` menjadi `200`
4. Klik `[Save]` dan tunggu toast sukses
5. Buat Client baru dengan email User `ops@ptlamasejahtera.example`
6. Tunggu aksi selesai (Client baru tersimpan)
7. Ganti akun ke Principal berizin Update "Manage archived client" lalu buka Overlay Notifikasi
8. Verifikasi Principal berizin menerima notifikasi dalam aplikasi atas kecocokan indeks arsip PT Lama Sejahtera (retensi tetap 730 hari sejak pembersihan)
9. Buka daftar Client lalu ketik Search nama Client baru yang dibuat spec, tekan Enter
10. Buka Detail Client baru
11. Verifikasi Client baru memiliki penanda match
12. Ganti akun ke Total Control
13. Hapus Client baru yang dibuat spec dan pulihkan ketujuh tab lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-529: Company yang di-Hard Purge setelah perubahan memakai Post-Purge Retention baru

14. Atur lewat Fixture BE: Post-Purge Retention tersimpan `200`, Company PT Baru Sentosa mencapai Hard Purge setelah perubahan, dan Principal berizin Update "Manage archived client" tersedia, lalu muat ulang halaman Lifecycle Settings
15. Catat baseline jumlah notifikasi Principal berizin Update "Manage archived client"
16. Majukan jam server dan jam browser 250 hari sejak Hard Purge PT Baru Sentosa lewat Fixture BE
17. Buat Client baru dengan email User milik PT Baru Sentosa
18. Buka daftar Client lalu ketik Search nama Client baru yang dibuat spec, tekan Enter
19. Verifikasi Client baru dibuat normal dan tampil pada daftar Client
20. Ganti akun ke Principal berizin Update "Manage archived client" lalu buka Overlay Notifikasi
21. Tunggu 5 detik tanpa memuat ulang halaman
22. Verifikasi tidak ada notifikasi kecocokan baru (jumlah notifikasi sama dengan baseline; retensi 200 hari terlewati)
23. Buka daftar Client lalu ketik Search nama Client baru yang dibuat spec, tekan Enter
24. Buka Detail Client baru
25. Verifikasi tidak ada penanda match pada Client baru

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Klik tab", "Catat baseline ..." (S-12), "Ganti akun ..." ke Principal berizin (langkah 7, 20) dan kembali ke Total Control (langkah 12) sebelum langkah yang membutuhkan akun Total Control (S-07), "Tunggu aksi selesai" (langkah 6, sesudah pembuatan Client dan sebelum ganti akun; 8b butir 8), "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 21, jendela absence notifikasi; bagian 6), "Buka daftar Client lalu ketik Search ..." (langkah 9, 18, 23; S-07, R-23), "Majukan jam ...", dan "Hapus Client baru ... lalu buka ..." antar TC (S-03, S-09). Pada TC-AC-LCS-529 sesi diakhiri sebagai Principal berizin dan dikembalikan ke Total Control oleh hook `after`.
- Asersi absence pada TC-AC-LCS-529 didahului `Verifikasi` Client baru dibuat normal dan tampil pada daftar Client sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA: TC-AC-LCS-528 dan TC-AC-LCS-529 tidak menyebut nama Client baru yang dibuat; langkah Search memakai nama Client baru yang dibuat spec (nama dan cara membuat Client belum ditetapkan TC). TC-AC-LCS-529 tidak menyebut akun pembuat Client baru; spec memakai akun Total Control default suite. PT Baru Sentosa ada di Pre-setup 10 dan akun berizin di Pre-setup 15 adalah usulan yang keberadaannya perlu dikonfirmasi tim FE. Penanda match pada Detail Client dan cara membaca notifikasi tidak diuraikan di TC (S-13). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
