---
id: TC-FA-NOTIF-E2E-102-multi-tab-approver-dan-flag-tooltip-lintas-perangkat
title: "Multi-Konteks: Flag Guided Tooltip Lintas Perangkat dan Auto-Read Approver Lintas Tab"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-57
  - TC-FA-NOTIF-116
  - TC-FA-NOTIF-384
coverage:
  web: automated
---

# Multi-Konteks: Flag Guided Tooltip Lintas Perangkat dan Auto-Read Approver Lintas Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control tur (Pre-setup #31), `totalControlTour_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOTIFTOUR_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControlTour`; akun tanpa flag `guided_tooltip_seen_fa-notification`, notifikasi N-01 sampai N-07 (Pre-setup #17) tersedia. Login di hook `before` spec ini (perangkat A); halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit pada langkah 13): Approver Borrowing & Assignment Gedung A (Pre-setup #4), `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_APPROVERBA_PASSWORD`, `Fixture.fixedAssetNotification.approverBorrowingAssignment`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu (hanya sesi API aktor, butir "Sesi API aktor" di `suite.md`): Asset Admin (Pre-setup #8), `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`, men-submit BRW-2026-0342.
- Pengecualian flag Guided Tooltip (butir "Flag Guided Tooltip" di `suite.md`): akun #31 tidak disetel true oleh hook suite. Langkah 1 memastikan flag `guided_tooltip_seen_fa-notification` akun #31 belum ada lewat fixture BE penyetel flag, dan hook `after` memulihkan flag akun #31 ke keadaan belum ada. Flag akun #4 true (hook suite `before` men-set dan `after` memulihkannya).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17, akun #31); transaksi Borrow BRW-2026-0342 (1 aset Kamera DSLR AST-2024-0141, Gedung A > Lantai 1 > Ruang 101; Pre-setup #19 dan #24) dengan notifikasi `borrow_waiting_approval` BRW-2026-0342 Unread bagi Approver (Pre-setup #19). Spec mengubah BRW-2026-0342 menjadi Waiting for Approval lalu Approved (langkah 14, 19, 26, 29); fixture BE pemulih seed notifikasi dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before`, pada langkah 14 dan 26, dan di hook `after`.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah submit dan Approve BRW-2026-0342 serta pembacaan seed N-01 sampai N-07 (Pre-setup #17 dan #19) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis: dua konteks browser dengan akun yang sama sebagai perangkat A dan B (TC-FA-NOTIF-57) dan dua tab browser dengan akun yang sama (TC-FA-NOTIF-116 dan 384); tab atau perangkat kedua menjadi objek asersi (bagian 3 prinsip 13c); fixture BE penyetel flag Guided Tooltip dan fixture BE pemicu Submit Borrow disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Asersi absence atas notifikasi in-app dan tur memakai anchor positif ditambah jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Env var `FA_NOTIFTOUR_TC_PASSWORD`, `FA_APPROVERBA_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-57: Guided tooltip, flag seen tersimpan per akun lintas perangkat

1. Pastikan flag `guided_tooltip_seen_fa-notification` akun #31 belum ada lewat fixture BE penyetel flag, lalu muat ulang halaman Fixed Asset > Dashboard di perangkat A
2. Pada perangkat A, buka Notification Center untuk pertama kali
3. Verifikasi tur muncul otomatis dengan indikator `Step 1 of 3` (anchor: tur sempat tampil)
4. Pada perangkat A, klik `[Next]` dua kali
5. Pada perangkat A, klik `[Done]`
6. Tunggu aksi selesai
7. Buka perangkat B (konteks browser kedua), login dengan akun yang sama (Pre-setup #31) dengan `Spectra.env.FA_NOTIFTOUR_TC_PASSWORD`, lalu buka Fixed Asset > Dashboard
8. Pada perangkat B, buka Notification Center
9. Verifikasi Notification Center tampil pada perangkat B
10. Tunggu 5 detik tanpa memuat ulang halaman
11. Verifikasi tur tidak muncul otomatis pada perangkat B
12. Tutup perangkat B

### TC-FA-NOTIF-116: Auto-Read, submit di satu tab membuat notifikasi Read di tab lain real-time

13. Logout, lalu login sebagai Approver (Borrowing & Assignment, Pre-setup #4) dengan `Spectra.env.FA_APPROVERBA_PASSWORD`, lalu buka Fixed Asset > Dashboard di tab A
14. Pulihkan seed notifikasi dan transaksi Pre-setup #17 sampai #24 lewat fixture BE pemulih, lalu dari akun Asset Admin (Pre-setup #8, sesi API) Submit Borrow Request BRW-2026-0342 hingga status Waiting for Approval tersimpan
15. Muat ulang halaman Fixed Asset > Dashboard di tab A, lalu buka tab B baru pada Fixed Asset > Dashboard dengan akun yang sama
16. Buka Dropdown Panel di tab A dan tab B (klik Bell icon pada tiap tab)
17. Verifikasi item `"Waiting for your approval"` BRW-2026-0342 berstatus Unread tampil pada tab B (anchor positif)
18. Pada tab B, catat nilai badge Bell icon (baseline)
19. Pada tab A, buka halaman Approvals untuk BRW-2026-0342 lalu Approve BRW-2026-0342 sampai sukses
20. Tunggu aksi selesai
21. Pindah ke tab B tanpa memuat ulang halaman
22. Verifikasi item BRW-2026-0342 pada tab B berubah menjadi Read
23. Verifikasi item BRW-2026-0342 pada tab B tanpa tombol `[Detail]`
24. Verifikasi badge Bell icon pada tab B berkurang dari baseline langkah 18
25. Tutup tab B

### TC-FA-NOTIF-384: Tab Unread, item actionable hilang real-time saat Auto-Read dari sesi lain

26. Pulihkan seed notifikasi dan transaksi Pre-setup #17 sampai #24 lewat fixture BE pemulih, lalu dari akun Asset Admin (Pre-setup #8, sesi API) Submit Borrow Request BRW-2026-0342 hingga status Waiting for Approval tersimpan
27. Pada tab A, muat ulang halaman Fixed Asset > Dashboard, klik Bell icon, klik `[Show All]`, lalu klik Tab `Unread`
28. Verifikasi item `"Waiting for your approval"` BRW-2026-0342 tampil pada Tab Unread tab A (anchor positif)
29. Buka tab B baru pada Fixed Asset > Dashboard dengan akun yang sama, lalu buka halaman Approvals untuk BRW-2026-0342 dan Approve BRW-2026-0342 sampai sukses
30. Tunggu aksi selesai
31. Pindah ke tab A tanpa memuat ulang halaman
32. Verifikasi Notification Center tab A tampil dengan Tab `Unread` aktif (anchor permukaan)
33. Verifikasi item `"Waiting for your approval"` BRW-2026-0342 hilang dari Tab Unread tab A
34. Klik Tab `All` pada tab A
35. Verifikasi item `"Waiting for your approval"` BRW-2026-0342 tetap tampil sebagai Read pada Tab All tab A

## Notes

- Spec kelas c (multi-konteks): perangkat B (TC-FA-NOTIF-57) dan tab B (TC-FA-NOTIF-116) menjadi objek asersi; tab A pada TC-FA-NOTIF-384 diasersi setelah tab B bertindak. Pelaku Asset Admin yang hanya men-submit memakai sesi API (bukan konteks kedua).
- Langkah penghubung (S-03): langkah 1 dan 14 serta 26 (penyetelan flag dan pemulihan seed antar TC); langkah 6, 20, dan 30 (tunggu aksi selesai, bagian 8b butir 8); langkah 13 (ganti akun eksplisit, S-07); langkah 15, 16, 21, 29, dan 31 (membuka dan memindah tab); langkah 18 (baseline badge tab B, S-12); langkah 19 dan 29 (membuka halaman Approvals untuk BRW-2026-0342 karena TC hanya menulis "Approve sampai sukses"); langkah 27 (jalur Notification Center lewat Bell icon dan `[Show All]`, karena TC tidak menyebut jalur lain); langkah 10 (jendela 5 detik, bagian 6 konvensi).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 11 didahului langkah 3 dan 9 (tur sempat tampil pada perangkat A dan Notification Center perangkat B tampil); langkah 23 didahului langkah 22 (item tab B tampil sebagai Read); langkah 33 didahului langkah 28 dan 32 (item sempat tampil pada Tab Unread dan Notification Center termuat).
- TC-FA-NOTIF-57: langkah 4 dan 5 menyalin pola `[Next]` dua kali lalu `[Done]` dari TC tur (TC-FA-NOTIF-50) karena TC hanya menulis "Selesaikan tour di perangkat A dengan `[Done]`".
- BRW-2026-0342 juga dipakai spec 056; spec ini berdiri sendiri karena objek ujinya multi-konteks (dua tab atau perangkat) dengan Approve lewat UI, dan transaksi dipulihkan fixture BE antar blok.
- Temuan untuk QA:
  - TC-FA-NOTIF-57: Post Condition kosong; tidak ada asersi tambahan. Cara membuat dua perangkat tidak ditulis TC (dua konteks browser dengan akun yang sama; sesi web akun yang sama pada perangkat B dapat mengeluarkan sesi perangkat A, tidak diasersi).
  - TC-FA-NOTIF-116: "Approve BRW-2026-0342" tidak menyebut jalur UI (halaman Approvals) dan "Read tanpa tombol" tidak menyebut tombol yang dimaksud; spec mengasersi `[Detail]` hilang. Tidak ada nomor Pre-setup untuk akun Approver pada Precondition (diambil dari role: Pre-setup #4).
  - TC-FA-NOTIF-384: Precondition menulis Pre-setup #19 tetapi item Unread sesuai transaksi yang disubmit; Approver tidak disebut nomor Pre-setup (diambil dari role: #4).
  - TC-FA-NOTIF-116 dan 384: Post Condition kosong; tidak ada asersi tambahan.
