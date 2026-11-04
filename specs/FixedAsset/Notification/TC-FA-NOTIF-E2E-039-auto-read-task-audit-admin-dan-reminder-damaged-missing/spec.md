---
id: TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing
title: "Auto-Read Task Audit untuk Asset Admin dan Reminder Damaged dan Missing untuk Group Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-145
  - TC-FA-NOTIF-146
  - TC-FA-NOTIF-147
  - TC-FA-NOTIF-148
  - TC-FA-NOTIF-157
  - TC-FA-NOTIF-158
  - TC-FA-NOTIF-159
  - TC-FA-NOTIF-160
coverage:
  web: automated
---

# Auto-Read Task Audit untuk Asset Admin dan Reminder Damaged dan Missing untuk Group Manager

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Spec ditulis per blok role karena penerima yang diamati berbeda per TC dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-145, 146, 147 (Asset Admin) | Asset Admin (PIC admin) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | TC-FA-NOTIF-148 (Auditor) | Auditor Rina Wijaya | #13 | `auditorRina_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AUDITOR_PASSWORD` | `Fixture.fixedAssetNotification.auditorRina` |
  | TC-FA-NOTIF-157, 158, 159, 160 (Group Manager Gedung A) | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |

- Login akun aktor pertama (Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu perubahan state (Update Task, Period Rollover, Mark as Repaired, Mark as Found, Report Disposal) memakai sesi API aktor akun yang sama dengan penerima atau Asset Admin (Pre-setup #8) lewat fixture BE pemicu event; Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: `Task Audit Q3-Gedung A` (Pre-setup #23, Overdue); aset Kamera DSLR AST-2024-0141 (Damaged) dan Laptop - 1 AST-2024-0067 (Missing) (Pre-setup #24). Precondition tiap TC (notifikasi `audit_task_overdue` varian Asset Admin atau Auditor, `damaged_reminder`, atau `missing_reminder` Unread) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): Period Rollover (TC-FA-NOTIF-147). Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (Task Audit Q3-Gedung A, AST-2024-0141, AST-2024-0067) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-145: audit_task_overdue varian Asset Admin Read saat Update Task Extend

1. Lewat sesi API Asset Admin (Pre-setup #8) Update Task Extend Task Audit Q3-Gedung A hingga tersimpan
2. Klik Bell icon
3. Verifikasi notifikasi `Audit task is overdue` varian Asset Admin Task Audit Q3-Gedung A berstatus Read
4. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-146: audit_task_overdue varian Asset Admin Read saat Update Task Stop

5. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Update Task Stop Task Audit Q3-Gedung A hingga tersimpan
6. Klik Bell icon
7. Verifikasi notifikasi `Audit task is overdue` varian Asset Admin Task Audit Q3-Gedung A berstatus Read
8. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-147: audit_task_overdue varian Asset Admin Read saat Period Rollover

9. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu atur jam server dan jam fixture ke waktu Period Rollover, jalankan Period Rollover yang menghentikan Task Audit Q3-Gedung A hingga tersimpan, lalu pulihkan jam
10. Klik Bell icon
11. Verifikasi notifikasi `Audit task is overdue` varian Asset Admin Task Audit Q3-Gedung A berstatus Read
12. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-148: audit_task_overdue varian Auditor view-only tetap Unread saat Update Task

13. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Auditor Rina Wijaya (Pre-setup #13), buka Fixed Asset > Dashboard
14. Lewat sesi API Asset Admin (Pre-setup #8), Update Task Extend Task Audit Q3-Gedung A hingga tersimpan
15. Klik Bell icon sebagai Auditor
16. Verifikasi notifikasi `Audit task is overdue` varian Auditor tetap Unread
17. Verifikasi tombol `[Mark as Read]` tampil pada notifikasi itu

### TC-FA-NOTIF-157: damaged_reminder Read saat Mark as Repaired

18. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Group Manager (Pre-setup #3), buka Fixed Asset > Dashboard
19. Lewat sesi API Group Manager, Mark as Repaired aset AST-2024-0141 hingga tersimpan
20. Klik Bell icon
21. Verifikasi notifikasi `Damaged asset is still unresolved` berstatus Read
22. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-158: damaged_reminder Read saat Report Disposal

23. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Group Manager (Pre-setup #3) Report Disposal aset AST-2024-0141 hingga tersimpan
24. Klik Bell icon
25. Verifikasi notifikasi `Damaged asset is still unresolved` berstatus Read
26. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-159: missing_reminder Read saat Mark as Found

27. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Group Manager (Pre-setup #3) Mark as Found aset AST-2024-0067 hingga tersimpan
28. Klik Bell icon
29. Verifikasi notifikasi `Missing asset is still under investigation` berstatus Read
30. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-160: missing_reminder Read saat Report Disposal

31. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Group Manager (Pre-setup #3) Report Disposal aset AST-2024-0067 hingga tersimpan
32. Klik Bell icon
33. Verifikasi notifikasi `Missing asset is still under investigation` berstatus Read
34. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 9, 13, 14, 18, 19, 23, 27 dan 31. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu.
- Pembagian per TC: TC-FA-NOTIF-145 (langkah 1 sampai 4), TC-FA-NOTIF-146 (langkah 5 sampai 8), TC-FA-NOTIF-147 (langkah 9 sampai 12), TC-FA-NOTIF-148 (langkah 13 sampai 17), TC-FA-NOTIF-157 (langkah 18 sampai 22), TC-FA-NOTIF-158 (langkah 23 sampai 26), TC-FA-NOTIF-159 (langkah 27 sampai 30), TC-FA-NOTIF-160 (langkah 31 sampai 34).
- Urutan TC di spec: 145, 146, 147 (Asset Admin), 148 (Auditor), lalu 157, 158, 159, 160 (Group Manager), dikelompokkan per akun supaya ganti akun hanya dua kali.
- Period Rollover pada TC-FA-NOTIF-147 hanya pemicu keadaan, bukan objek uji.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat `audit_task_overdue` milik Asset Admin dan Auditor serta reminder Damaged dan Missing milik Group Manager, karena penerima kelompok lain memakai akun berbeda dan penyatuan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-145, 146, dan 147 menulis Asset Admin, TC-FA-NOTIF-148 Auditor (Rina Wijaya), dan TC-FA-NOTIF-157 sampai 160 Group Manager (Gedung A) tanpa nomor Pre-setup; spec memakai Pre-setup #8, #13, dan #3.
  - TC-FA-NOTIF-145 sampai 147 menulis "Lakukan: Update Task Extend/Stop" dan "Period Rollover" tanpa pelaku dan jam; spec memakai sesi API Asset Admin (Pre-setup #8) dan jam yang diatur tim FE/BE. TC-FA-NOTIF-157 sampai 160 tidak menyebut pelaku; spec memakai sesi API Group Manager.
  - TC-FA-NOTIF-145 sampai 148 dan 157 sampai 160 tidak menyebut Title notifikasi selain event type; spec mengidentifikasi item lewat Title katalog PRD §5.1 dan varian penerima.
