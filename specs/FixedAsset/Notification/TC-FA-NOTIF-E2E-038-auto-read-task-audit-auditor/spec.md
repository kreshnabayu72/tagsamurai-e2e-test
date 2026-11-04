---
id: TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor
title: "Auto-Read Task Audit untuk Auditor: Finish Audit, Stop, Cancel, dan Perpindahan Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-140
  - TC-FA-NOTIF-141
  - TC-FA-NOTIF-142
  - TC-FA-NOTIF-143
  - TC-FA-NOTIF-144
  - TC-FA-NOTIF-369
  - TC-FA-NOTIF-370
  - TC-FA-NOTIF-371
coverage:
  web: automated
---

# Auto-Read Task Audit untuk Auditor: Finish Audit, Stop, Cancel, dan Perpindahan Status

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Akun aktor: Auditor Rina Wijaya Pre-setup #13 (`auditorRina_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_AUDITOR_PASSWORD`, fixture `Fixture.fixedAssetNotification.auditorRina`; nama env usulan, belum terdaftar).
- Login akun aktor pertama (Pre-setup #13) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu perubahan state (Finish Audit, Stop, Cancel) memakai sesi API aktor: Auditor (Pre-setup #13) dan Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: `Task Audit Q3-Gedung A` (Pre-setup #23; status per TC: In Audit, Grace Period, atau Overdue). Precondition tiap TC (notifikasi `audit_task_started` atau `audit_task_grace_period` Unread untuk Auditor) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): scheduler harian audit (TC-FA-NOTIF-144 dan 371). Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (Task Audit Q3-Gedung A) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-140: audit_task_started Read saat Finish Audit disubmit

1. Lewat sesi API Auditor (Pre-setup #13) Finish Audit Task Audit Q3-Gedung A hingga tersimpan
2. Klik Bell icon sebagai Auditor
3. Verifikasi notifikasi `New audit task started` Task Audit Q3-Gedung A berstatus Read
4. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-141: audit_task_grace_period Read saat Finish Audit disubmit

5. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Auditor (Pre-setup #13) Finish Audit Task Audit Q3-Gedung A hingga tersimpan
6. Klik Bell icon sebagai Auditor
7. Verifikasi notifikasi `Audit task entering grace period` Task Audit Q3-Gedung A berstatus Read
8. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-142: audit_task_started Read saat task Stopped

9. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Stop Task Audit Q3-Gedung A hingga tersimpan
10. Klik Bell icon sebagai Auditor
11. Verifikasi notifikasi `New audit task started` Task Audit Q3-Gedung A berstatus Read
12. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-143: audit_task_grace_period Read saat task Stopped

13. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Stop Task Audit Q3-Gedung A hingga tersimpan
14. Klik Bell icon sebagai Auditor
15. Verifikasi notifikasi `Audit task entering grace period` Task Audit Q3-Gedung A berstatus Read
16. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-144: audit_task_started Read saat task berpindah ke status berikutnya

17. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu jalankan scheduler harian audit pada jam server dan jam fixture yang diatur sampai Task Audit Q3-Gedung A berpindah status hingga tersimpan, lalu pulihkan jam
18. Klik Bell icon sebagai Auditor
19. Verifikasi notifikasi `New audit task started` Task Audit Q3-Gedung A berstatus Read
20. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-369: audit_task_started Read saat task Canceled

21. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Cancel Task Audit Q3-Gedung A hingga pembatalan tersimpan
22. Klik Bell icon sebagai Auditor
23. Verifikasi notifikasi `New audit task started` Task Audit Q3-Gedung A berstatus Read
24. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-370: audit_task_grace_period Read saat task Canceled

25. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Cancel Task Audit Q3-Gedung A hingga pembatalan tersimpan
26. Klik Bell icon sebagai Auditor
27. Verifikasi notifikasi `Audit task entering grace period` Task Audit Q3-Gedung A berstatus Read
28. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-371: audit_task_grace_period Read saat task berpindah ke Overdue dan notifikasi overdue baru

29. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu jalankan scheduler harian audit pada jam server dan jam fixture yang diatur sampai Task Audit Q3-Gedung A berpindah dari Grace Period ke Overdue hingga tersimpan, lalu pulihkan jam
30. Klik Bell icon sebagai Auditor
31. Verifikasi notifikasi `Audit task entering grace period` Task Audit Q3-Gedung A berstatus Read
32. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu
33. Verifikasi notifikasi baru `Audit task is overdue` varian Auditor Task Audit Q3-Gedung A tampil berstatus Unread
34. Verifikasi tombol `[Mark as Read]` tampil pada notifikasi `Audit task is overdue`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 9, 13, 17, 21, 25 dan 29. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu.
- Pembagian per TC: TC-FA-NOTIF-140 (langkah 1 sampai 4), TC-FA-NOTIF-141 (langkah 5 sampai 8), TC-FA-NOTIF-142 (langkah 9 sampai 12), TC-FA-NOTIF-143 (langkah 13 sampai 16), TC-FA-NOTIF-144 (langkah 17 sampai 20), TC-FA-NOTIF-369 (langkah 21 sampai 24), TC-FA-NOTIF-370 (langkah 25 sampai 28), TC-FA-NOTIF-371 (langkah 29 sampai 34).
- Scheduler harian audit pada TC-FA-NOTIF-144 dan 371 hanya pemicu perpindahan status, bukan objek uji; spec job waktu audit ada di spec 099.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat notifikasi Task Audit milik Auditor, karena penerima kelompok lain memakai akun berbeda dan penyatuan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-140 sampai 144 dan 369 sampai 371 menulis Auditor (Rina Wijaya) tanpa nomor Pre-setup (hanya data Pre-setup #23 disebut pada TC-FA-NOTIF-369 sampai 371); spec memakai Pre-setup #13.
  - TC-FA-NOTIF-140 dan 141 menulis "Lakukan: Finish Audit task" dan TC-FA-NOTIF-142 dan 143 menulis "Lakukan: Stop task" tanpa menyebut pelaku dan status awal task; spec memakai sesi API Auditor untuk Finish Audit dan sesi API Asset Admin untuk Stop (TC-FA-NOTIF-369 dan 370 menyebut Asset Admin untuk Cancel), dan mengandalkan fixture BE menyiapkan status awal.
  - TC-FA-NOTIF-144 dan 371 menulis "jalankan scheduler sampai task berpindah status" tanpa jam pasti; nilai pastinya ditetapkan tim FE/BE. TC-FA-NOTIF-371 Expected b tidak menyebut judul tombol selain `[Mark as Read]`.
