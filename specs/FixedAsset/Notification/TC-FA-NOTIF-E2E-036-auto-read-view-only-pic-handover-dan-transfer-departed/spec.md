---
id: TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed
title: "Auto-Read Borrow untuk PIC Admin dan Borrower: Return, Extend, Handover, Cancel, dan Notifikasi View-Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-136
  - TC-FA-NOTIF-137
  - TC-FA-NOTIF-138
  - TC-FA-NOTIF-139
  - TC-FA-NOTIF-155
  - TC-FA-NOTIF-156
coverage:
  web: automated
---

# Auto-Read Borrow untuk PIC Admin dan Borrower: Return, Extend, Handover, Cancel, dan Notifikasi View-Only

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Spec ditulis per blok role karena PIC admin dan Borrower memakai akun berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-136, 137, 155, 156 (PIC admin) | Asset Admin (PIC admin) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | TC-FA-NOTIF-138, 139 (Borrower) | Borrower Budi Santoso | #11 | `borrowerBudi_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_BORROWER_PASSWORD` | `Fixture.fixedAssetNotification.borrowerBudi` |

- Login akun aktor pertama (Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu perubahan state (Return, Extend, handover, Cancel Request) memakai sesi API aktor PIC admin (Pre-setup #8) lewat fixture BE pemicu event; Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: transaksi Borrow BRW-2026-0341 (2 aset Proyektor AST-2024-0150 dan Laptop - 2 AST-2024-0068, keduanya melewati Due Date) dan BRW-2026-0342 (Kamera DSLR AST-2024-0141; Pre-setup #19 dan #24). Precondition tiap TC (notifikasi `borrow_overdue` per aset, `borrow_due_soon`, atau `borrow_almost_timeout` varian PIC admin Unread) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0341, BRW-2026-0342, AST-2024-0141) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-136: borrow_overdue varian PIC admin Read saat aset dikembalikan tanpa menunggu aset lain

1. Lewat sesi API PIC admin (Pre-setup #8), Return aset Proyektor (AST-2024-0150) saja pada BRW-2026-0341 hingga pengembalian tersimpan
2. Klik Bell icon sebagai PIC admin
3. Verifikasi notifikasi `Your borrowed asset is overdue` aset Proyektor (AST-2024-0150) berstatus Read
4. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi aset Proyektor
5. Verifikasi notifikasi `Your borrowed asset is overdue` aset kedua Laptop - 2 (AST-2024-0068) tetap Unread
6. Verifikasi tombol `[Detail]` tampil pada notifikasi aset kedua

### TC-FA-NOTIF-137: borrow_overdue varian PIC admin Read saat Extend membuat Due Date >= hari ini

7. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API PIC admin (Pre-setup #8) Extend durasi peminjaman AST-2024-0141 sehingga Due Date setelah hari ini hingga tersimpan
8. Klik Bell icon sebagai PIC admin
9. Verifikasi notifikasi `Your borrowed asset is overdue` varian PIC admin AST-2024-0141 berstatus Read
10. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-155: almost_timeout varian PIC admin Read saat transaksi lanjut ke fase committed

11. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API PIC admin (Pre-setup #8) selesaikan handover BRW-2026-0342 sehingga fase committed hingga tersimpan
12. Klik Bell icon sebagai PIC admin
13. Verifikasi item `Please finish this transaction — expiring soon` BRW-2026-0342 berstatus Read
14. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-156: almost_timeout varian PIC admin Read saat transaksi dibatalkan

15. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API PIC admin (Pre-setup #8) Cancel Request BRW-2026-0342 hingga pembatalan tersimpan
16. Klik Bell icon sebagai PIC admin
17. Verifikasi item `Please finish this transaction — expiring soon` BRW-2026-0342 berstatus Read
18. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-138: borrow_overdue varian Borrower view-only tetap Unread saat aset dikembalikan

19. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Borrower Budi Santoso (Pre-setup #11), buka Fixed Asset > Dashboard
20. Lewat sesi API PIC admin (Pre-setup #8), Return aset AST-2024-0141 hingga pengembalian tersimpan
21. Klik Bell icon sebagai Borrower
22. Verifikasi notifikasi `Your borrowed asset is overdue` varian Borrower AST-2024-0141 tetap Unread
23. Verifikasi tombol `[Mark as Read]` tampil pada notifikasi itu

### TC-FA-NOTIF-139: borrow_due_soon view-only tetap Unread saat Extend

24. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API PIC admin (Pre-setup #8) Extend durasi peminjaman AST-2024-0141 hingga tersimpan
25. Klik Bell icon sebagai Borrower
26. Verifikasi notifikasi `Your borrowed asset is due soon` AST-2024-0141 tetap Unread
27. Verifikasi tombol `[Mark as Read]` tampil pada notifikasi itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 7, 11, 15, 19, 20 dan 24. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu.
- Pembagian per TC: TC-FA-NOTIF-136 (langkah 1 sampai 6), TC-FA-NOTIF-137 (langkah 7 sampai 10), TC-FA-NOTIF-155 (langkah 11 sampai 14), TC-FA-NOTIF-156 (langkah 15 sampai 18), TC-FA-NOTIF-138 (langkah 19 sampai 23), TC-FA-NOTIF-139 (langkah 24 sampai 27).
- Urutan TC di spec: 136, 137, 155, 156 (PIC admin), lalu 138, 139 (Borrower), dikelompokkan per akun supaya ganti akun hanya sekali.
- TC-FA-NOTIF-149 sampai 152 (assignment_accepted dan transfer_departed) ada di spec 037.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat notifikasi PIC admin (Auto-Read) dan Borrower (view-only) pada transaksi Borrow, karena penerima kelompok lain memakai akun berbeda dan penyatuan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-136, 137, 155, dan 156 menulis role Asset Admin (PIC admin) tanpa nomor Pre-setup dan TC-FA-NOTIF-138 dan 139 menulis Borrower (Budi Santoso) tanpa nomor Pre-setup; spec memakai Pre-setup #8 dan #11.
  - TC-FA-NOTIF-137 dan 139 menulis "Extend durasi peminjaman" tanpa menyebut pelaku; spec memakai sesi API PIC admin (Pre-setup #8). TC-FA-NOTIF-138 menulis "oleh PIC admin" untuk Return, dan TC-FA-NOTIF-155 serta 156 tidak menyebut pelaku handover dan Cancel Request; spec memakai sesi API PIC admin.
  - TC-FA-NOTIF-136 dan 139 tidak menyebut judul notifikasi `borrow_overdue` varian PIC admin dan `borrow_due_soon` selain event type; spec mengidentifikasi item lewat Title katalog PRD §5.1a, aset, dan Body aset.
