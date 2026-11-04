---
id: TC-FA-NOTIF-E2E-112-auto-read-multi-approver-almost-timeout-dan-approver-or-lintas-sesi
title: "Auto-Read Multi-Approver: Almost Timeout hingga Auto-Cancel dan Task Diselesaikan Pihak Lain pada Approver OR"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-129
  - TC-FA-NOTIF-364
coverage:
  web: automated
---

# Auto-Read Multi-Approver: Almost Timeout hingga Auto-Cancel dan Task Diselesaikan Pihak Lain pada Approver OR

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon, Dropdown Panel, dan halaman Approvals.
- Spec ditulis per blok role karena penerima yang diamati berganti dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-129 dan 364 (Approver A) | Approver (Borrowing & Assignment) A | #4 | `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment` |
  | TC-FA-NOTIF-129 dan 364 (Approver B) | Approver (Borrowing & Assignment) B | #15 | `approverBorrowingAssignment2_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA2_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment2` |
  | TC-FA-NOTIF-364 (Approver C) | Total Control pemegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A (Approver C) | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |

- Login akun aktor pertama (Pre-setup #4) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Approver A (Pre-setup #4) pada TC-FA-NOTIF-129. Sesi UI dipakai bergantian per akun (ganti akun eksplisit), bukan paralel.
- Data Pre-setup: transaksi Borrow BRW-2026-0341 (2 aset, Pre-setup #19). TC-FA-NOTIF-129: dua approver level AND (A dan B) menerima `borrow_almost_timeout` varian Approver Unread. TC-FA-NOTIF-364: tiga approver level OR (A, B, dan C) menerima `borrow_waiting_approval` BRW-2026-0341 Unread. Kedua keadaan dibentuk fixture BE pemulih dan fixture BE pemicu di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): job `F-FATX-07` (auto-cancel) pada TC-FA-NOTIF-129. Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0341) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-129: Multi-approver almost_timeout varian Approver mengikuti aturan waiting_approval

1. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, siapkan notifikasi almost timeout varian Approver BRW-2026-0341 berstatus Unread untuk Approver A dan Approver B lewat fixture BE pemicu event, lalu lewat sesi API Approver A (Pre-setup #4) Approve BRW-2026-0341 (belum final) hingga tersimpan
2. Muat ulang halaman Fixed Asset > Dashboard, lalu klik Bell icon sebagai Approver A
3. Verifikasi item `Please finish this approval — expiring soon` BRW-2026-0341 milik Approver A berstatus Read
4. Logout, lalu login sebagai Approver (Borrowing & Assignment) kedua (Pre-setup #15), lalu buka Fixed Asset > Dashboard
5. Klik Bell icon sebagai Approver B
6. Verifikasi item `Please finish this approval — expiring soon` BRW-2026-0341 milik Approver B tetap Unread
7. Atur jam server dan jam fixture ke setelah `cancel_deadline_at` BRW-2026-0341 (dibaca lewat fixture BE), jalankan job `F-FATX-07` hingga auto-cancel BRW-2026-0341 tersimpan, lalu pulihkan jam
8. Muat ulang halaman Fixed Asset > Dashboard, lalu klik Bell icon sebagai Approver B
9. Verifikasi item `Please finish this approval — expiring soon` BRW-2026-0341 milik Approver B berstatus Read

### TC-FA-NOTIF-364: Task diselesaikan pihak lain saat notifikasi masih ada di banyak penerima

10. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Approver A (Pre-setup #4), buka Fixed Asset > Dashboard, klik Bell icon, lalu klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0341
11. Pada halaman Approvals, Approve BRW-2026-0341 sebagai Approver A hingga berhasil tersimpan
12. Logout, lalu login sebagai Approver (Borrowing & Assignment) kedua (Pre-setup #15), lalu buka Fixed Asset > Dashboard
13. Klik Bell icon sebagai Approver B
14. Verifikasi item `Waiting for your approval` BRW-2026-0341 milik Approver B berstatus Read
15. Verifikasi tombol `[Detail]` tidak tampil pada item itu
16. Logout, lalu login sebagai Total Control (Pre-setup #1), lalu buka Fixed Asset > Dashboard
17. Klik Bell icon sebagai Approver C
18. Verifikasi item `Waiting for your approval` BRW-2026-0341 milik Approver C berstatus Read
19. Verifikasi tombol `[Detail]` tidak tampil pada item itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 4, 7, 10, 12 dan 16. Langkah pembuka blok memuat pemulihan fixture BE dan pemicu lewat sesi API; langkah ganti akun adalah ganti akun eksplisit (S-07); langkah jam dan job adalah pemicu keadaan (kemudian jam dipulihkan); langkah `[Detail]` adalah jalur ke halaman Approvals.
- Pembagian per TC: TC-FA-NOTIF-129 (langkah 1 sampai 9), TC-FA-NOTIF-364 (langkah 10 sampai 19).
- P-12: TC-FA-NOTIF-129 dan TC-FA-NOTIF-364 adalah TC kelas c (lebih dari satu akun penerima) yang memakai job `F-FATX-07` dan jam server hanya sebagai pemicu keadaan yang diamati (TC-FA-NOTIF-129 langkah 7). Akun kedua dan ketiga adalah pengamat read-only, pelaku Approver A pada TC-FA-NOTIF-129 lewat sesi API, dan tidak ada kelas b atau h lain di spec ini. Kemampuan jam dan sesi dinyatakan di Prerequisites.
- Pembagian per TC lintas spec: TC-FA-NOTIF-124 sampai 128 ada di spec 033.
- Pada TC-FA-NOTIF-129 Expected a (item Approver A Read, item Approver B Unread) diasersi pada langkah 3 dan 6; TC menulis Langkah 2 "Klik Bell icon sebagai Approver A dan Approver B" dalam satu langkah, yang di spec dipecah per akun dengan ganti akun eksplisit.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat kasus multi-approver almost timeout dan Approver OR lintas sesi yang menukar akun A, B, dan C, karena penyatuan dengan spec 033 menambah ganti akun dan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-129 dan 364 menulis Approver A, B, dan C tanpa nomor Pre-setup pada TC-FA-NOTIF-129; TC-FA-NOTIF-364 menulis A = Pre-setup #4, B = #15, C = #1 dan spec memakai pemetaan itu untuk kedua TC.
  - TC-FA-NOTIF-129 menulis Langkah 1 "Approver A Approve (belum final)" tanpa menyebut sesi; karena Approver A tidak dibuka di UI pada langkah itu, spec memakai sesi API Approver A. Jam pada Langkah 3 "Auto-cancel transaksi lewat job `F-FATX-07`" tidak disebut; spec memakai jam setelah `cancel_deadline_at`.
  - TC-FA-NOTIF-364 tidak menyebut Expected untuk item milik Approver A sendiri; hanya item Approver B dan C yang diasersi.
