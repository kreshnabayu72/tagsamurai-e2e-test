---
id: TC-FA-NOTIF-E2E-033-auto-read-multi-approver-and-scope-both-dan-dual-group
title: "Auto-Read Multi-Approver AND, Scope Both Transfer, dan Dual-Group Disposal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-124
  - TC-FA-NOTIF-125
  - TC-FA-NOTIF-126
  - TC-FA-NOTIF-127
  - TC-FA-NOTIF-128
coverage:
  web: automated
---

# Auto-Read Multi-Approver AND, Scope Both Transfer, dan Dual-Group Disposal

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon, Dropdown Panel, dan halaman Approvals.
- Spec ditulis per blok role karena penerima yang diamati berganti per TC dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-124 (Approver A, lalu B) | Approver (Borrowing & Assignment) A | #4 | `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment` |
  | TC-FA-NOTIF-124, 125, 126 (Approver B) | Approver (Borrowing & Assignment) B | #15 | `approverBorrowingAssignment2_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA2_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment2` |
  | TC-FA-NOTIF-127 (Group Tujuan) | Approver Gedung B (Group Tujuan Transfer) | #32 | `approverGedungB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERGDGB_PASSWORD` | `Fixture.fixedAssetNotification.approverGedungB` |
  | TC-FA-NOTIF-128 (Disposal) | Approver (Disposal) | #6 | `approverDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSP_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposal` |

- Pelaku lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Approver A (Pre-setup #4) pada TC-FA-NOTIF-125 dan 126; Approver Group Asal Transfer (Pre-setup #5, `approverTransfer_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERTRF_PASSWORD`) pada TC-FA-NOTIF-127; Approver Origin Group Disposal pada TC-FA-NOTIF-128 (akun tidak ada di Pre-setup TC; disediakan tim FE). Pelaku kedua memakai sesi API, bukan sesi UI.
- Login akun aktor pertama (Pre-setup #4) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: transaksi Borrow BRW-2026-0341 (2 aset, approval level AND dengan Approver A dan B; Pre-setup #19 dan #15), Transfer TRF-2026-0055 (`approval_scope=both`; Pre-setup #21), Disposal DSP-2026-0030 (dual-group; Pre-setup #22). Precondition tiap TC (notifikasi `Waiting for your approval` Unread untuk tiap approver; pada TC-FA-NOTIF-125 Approver A sudah Approve) dibentuk fixture BE pemulih dan fixture BE pemicu di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0341, TRF-2026-0055, DSP-2026-0030) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-124: Multi-approver AND: hanya milik approver yang memutuskan menjadi Read

1. Klik Bell icon lalu klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0341
2. Pada halaman Approvals, Approve BRW-2026-0341 sebagai Approver A (keputusan belum final) hingga berhasil tersimpan
3. Klik Bell icon sebagai Approver A
4. Verifikasi item `Waiting for your approval` BRW-2026-0341 milik Approver A berstatus Read
5. Verifikasi tombol `[Detail]` tidak tampil pada item itu
6. Logout, lalu login sebagai Approver (Borrowing & Assignment) kedua (Pre-setup #15), lalu buka Fixed Asset > Dashboard
7. Klik Bell icon sebagai Approver B
8. Verifikasi item `Waiting for your approval` BRW-2026-0341 milik Approver B tetap Unread
9. Verifikasi tombol `[Detail]` tampil pada item itu

### TC-FA-NOTIF-125: Multi-approver AND: item approver terakhir Read saat keputusan akhir Approved

10. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard sebagai Approver B, lalu lewat sesi API Approver A (Pre-setup #4) Approve BRW-2026-0341 hingga tersimpan, klik Bell icon, lalu klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0341
11. Pada halaman Approvals, Approve BRW-2026-0341 sebagai Approver B sehingga keputusan akhir Approved hingga berhasil tersimpan
12. Klik Bell icon sebagai Approver B
13. Verifikasi item `Waiting for your approval` BRW-2026-0341 milik Approver B berstatus Read
14. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-126: Multi-approver: Reject final membuat notifikasi penerima lain Read

15. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard sebagai Approver B, lalu lewat sesi API Approver A (Pre-setup #4) Reject BRW-2026-0341 hingga keputusan akhir Rejected tersimpan
16. Klik Bell icon sebagai Approver B
17. Verifikasi item `Waiting for your approval` BRW-2026-0341 milik Approver B berstatus Read
18. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-127: Approval scope Both pada Transfer: sisi Not Involved mengikuti keputusan akhir

19. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Approver Group Tujuan (Pre-setup #32), buka Fixed Asset > Dashboard, lalu lewat sesi API Approver Group Asal (Pre-setup #5) Reject TRF-2026-0055 hingga keputusan akhir Rejected tersimpan
20. Klik Bell icon sebagai Approver Group Tujuan
21. Verifikasi item `Waiting for your approval` TRF-2026-0055 milik Approver Group Tujuan berstatus Read
22. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-128: Dual-group Disposal: sisi gugur karena Reject sisi lain

23. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Approver Disposal (Pre-setup #6), buka Fixed Asset > Dashboard, lalu lewat sesi API Approver Origin Group Reject DSP-2026-0030 hingga keputusan akhir tersimpan
24. Klik Bell icon sebagai Approver Disposal
25. Verifikasi item `Waiting for your approval` DSP-2026-0030 milik Approver Disposal berstatus Read
26. Verifikasi tombol `[Detail]` tidak tampil pada item itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 10, 15, 19 dan 23. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keputusan pihak lain lewat sesi API (ditulis "... hingga ... tersimpan"); langkah `[Detail]` adalah jalur ke halaman Approvals; langkah 6 adalah ganti akun eksplisit (S-07).
- Pembagian per TC: TC-FA-NOTIF-124 (langkah 1 sampai 9), TC-FA-NOTIF-125 (langkah 10 sampai 14), TC-FA-NOTIF-126 (langkah 15 sampai 18), TC-FA-NOTIF-127 (langkah 19 sampai 22), TC-FA-NOTIF-128 (langkah 23 sampai 26).
- Pembagian per TC lintas spec: TC-FA-NOTIF-129 (almost_timeout multi-approver dengan job) dan TC-FA-NOTIF-364 (tiga approver level OR) ada di spec 112.
- Alasan blok per role: tiap TC mengamati akun penerima yang berbeda (Approver A lalu B, B, Group Tujuan, Approver Disposal), sehingga ganti akun memerlukan langkah eksplisit (bagian 3a, keputusan 2026-10-30).
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat keputusan multi-approver, scope Both, dan dual-group yang mengamati beberapa akun approver berurutan, karena penyatuan dengan kelompok lain menambah ganti akun dan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-124 sampai 126 menulis "Approver A" dan "Approver B" tanpa nomor Pre-setup; spec memakai Pre-setup #4 untuk A dan #15 ("Approver kedua (AND/OR)") untuk B. TC-FA-NOTIF-127 dan 128 tidak menyebut akun Group Asal, Group Tujuan, Origin Group, dan Approver Disposal; spec memakai Pre-setup #32 (Group Tujuan Transfer), #5 (Approver Transfer sebagai Group Asal), dan #6 (Approver Disposal); akun Approver Origin Group Disposal tidak ada di Pre-setup TC.
  - TC-FA-NOTIF-125 menulis "Approver A sudah Approve" sebagai precondition tanpa menyebut cara membentuknya; spec membentuknya lewat sesi API Approver A. TC-FA-NOTIF-124 menulis "Approver A Approve" pada Langkah sementara precondition login adalah Approver A; spec mengikuti dengan Approve lewat UI.
  - TC-FA-NOTIF-127 menulis Expected "saat keputusan akhir Rejected" tanpa menyebut efek bila Group Tujuan sudah memutuskan lebih dulu; spec hanya mengikuti alur Reject dari Group Asal.
