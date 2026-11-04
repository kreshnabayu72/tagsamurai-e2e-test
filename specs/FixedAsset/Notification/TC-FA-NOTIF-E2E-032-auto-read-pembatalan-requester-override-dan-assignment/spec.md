---
id: TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment
title: "Auto-Read Waiting Approval: Approve Assignment, Pembatalan Requester, Auto-Cancel, Override Group Manager, dan Almost Timeout"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-117
  - TC-FA-NOTIF-121
  - TC-FA-NOTIF-122
  - TC-FA-NOTIF-123
  - TC-FA-NOTIF-372
  - TC-FA-NOTIF-434
coverage:
  web: automated
---

# Auto-Read Waiting Approval: Approve Assignment, Pembatalan Requester, Auto-Cancel, Override Group Manager, dan Almost Timeout

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon, Dropdown Panel, dan halaman Approvals.
- Akun aktor: Approver (Borrowing & Assignment) Pre-setup #4 (`approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_APPROVERBA_PASSWORD`, fixture `Fixture.fixedAssetNotification.approverBorrowingAssignment`; nama env usulan, belum terdaftar). TC hanya menulis role tanpa nomor Pre-setup (lihat Temuan untuk QA).
- Login akun aktor pertama (Pre-setup #4) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin pembuat transaksi (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`) dan Group Manager (Pre-setup #3, `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GM_PASSWORD`). Pelaku kedua memakai sesi API, bukan sesi UI.
- Data Pre-setup: transaksi Borrow BRW-2026-0342 (Pre-setup #19), transaksi Assignment ASG-2026-0120 (Pre-setup #20). Precondition tiap TC (notifikasi `borrow_waiting_approval`, `assignment_waiting_approval`, atau `borrow_almost_timeout` varian Approver Unread untuk akun aktor) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): job `F-FATX-07` (auto-cancel) dan pembacaan `cancel_deadline_at` BRW-2026-0342 lewat fixture BE. Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0342, ASG-2026-0120) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-117: assignment_waiting_approval menjadi Read saat Approver memutuskan

1. Klik Bell icon lalu klik `[Detail]` pada item `Waiting for your approval` ASG-2026-0120
2. Pada halaman Approvals, Approve ASG-2026-0120 sampai sukses
3. Klik Bell icon
4. Verifikasi item `Waiting for your approval` ASG-2026-0120 berstatus Read
5. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-121: Transaksi dibatalkan requester membuat waiting_approval Read

6. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin pembuat (Pre-setup #8) Cancel Request BRW-2026-0342 hingga pembatalan tersimpan
7. Klik Bell icon
8. Verifikasi item `Waiting for your approval` BRW-2026-0342 berstatus Read
9. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-122: Auto-cancel F-FATX-07 membuat waiting_approval Read

10. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, baca `cancel_deadline_at` BRW-2026-0342 lewat fixture BE, atur jam server dan jam fixture ke setelah `cancel_deadline_at`, jalankan job `F-FATX-07` hingga auto-cancel BRW-2026-0342 tersimpan, lalu pulihkan jam
11. Klik Bell icon
12. Verifikasi item `Waiting for your approval` BRW-2026-0342 berstatus Read
13. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-123: Override Group Manager membuat waiting_approval Read

14. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Group Manager (Pre-setup #3) Approve BRW-2026-0342 sebagai override hingga tersimpan
15. Klik Bell icon
16. Verifikasi item `Waiting for your approval` BRW-2026-0342 berstatus Read
17. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-372: borrow_almost_timeout varian Approver Read saat requester membatalkan transaksi

18. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin pembuat (Pre-setup #8) Cancel Request BRW-2026-0342 hingga pembatalan tersimpan
19. Klik Bell icon
20. Verifikasi item `Please finish this approval — expiring soon` BRW-2026-0342 berstatus Read
21. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-434: Cancel Assignment oleh requester membuat assignment_waiting_approval Read

22. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin pembuat (Pre-setup #8) Cancel ASG-2026-0120 (`F-ASSIGN-05`) hingga pembatalan tersimpan
23. Klik Bell icon
24. Verifikasi item `Waiting for your approval` ASG-2026-0120 berstatus Read
25. Verifikasi tombol `[Detail]` tidak tampil pada item itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 10, 14, 18 dan 22. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman, dan pemicu keadaan lewat sesi API (aksi pelaku kedua, ditulis "... hingga ... tersimpan"); langkah `[Detail]` pada TC-FA-NOTIF-117 adalah jalur ke halaman Approvals.
- Pembagian per TC: TC-FA-NOTIF-117 (langkah 1 sampai 5), TC-FA-NOTIF-121 (langkah 6 sampai 9), TC-FA-NOTIF-122 (langkah 10 sampai 13), TC-FA-NOTIF-123 (langkah 14 sampai 17), TC-FA-NOTIF-372 (langkah 18 sampai 21), TC-FA-NOTIF-434 (langkah 22 sampai 25).
- Pemicu event dijalankan di modul sumber lewat sesi API aktor dan asersi hanya pada Dropdown Panel (Catatan TC). Job `F-FATX-07` (langkah 10) hanya pemicu keadaan, bukan objek uji; batas waktu dibaca dari `cancel_deadline_at` lewat fixture BE (bagian 8b butir 3).
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat penutupan `waiting_approval` oleh pembatalan, auto-cancel, dan override (dipicu sesi API, akun pengamat Approver Borrow dan Assignment), karena penyatuan dengan kelompok penerima lain jauh melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-117, 121, 122, 123, 372, dan 434 menulis role Approver (Borrowing & Assignment) tanpa nomor Pre-setup (hanya TC-FA-NOTIF-434 menulis "akun Pre-setup #4"). Spec memakai Pre-setup #4 untuk keenam TC.
  - TC-FA-NOTIF-117 hanya menulis "Klik Bell icon" lalu "Approve di halaman Approvals" tanpa jalur ke halaman Approvals; spec memakai `[Detail]` pada item sebagai jalur.
  - TC-FA-NOTIF-123 tidak menyebut akun Group Manager; spec memakai Pre-setup #3. TC-FA-NOTIF-122 tidak menyebut jam yang diatur selain "setelah `cancel_deadline_at` terlampaui"; spec memakai jam tepat setelah batas itu, nilai pastinya ditetapkan tim FE/BE.
  - TC-FA-NOTIF-121, 123, 372, dan 434 tidak menyebut status transaksi setelah pembatalan atau override; spec hanya menunggu aksi tersimpan.
