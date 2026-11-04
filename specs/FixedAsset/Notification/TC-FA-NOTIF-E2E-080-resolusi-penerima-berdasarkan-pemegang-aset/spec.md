---
id: TC-FA-NOTIF-E2E-080-resolusi-penerima-berdasarkan-pemegang-aset
title: "Resolusi Penerima Notifikasi Berdasarkan Pemegang Aset: Group Manager, Borrower, Assignee, dan PIC Admin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-315
  - TC-FA-NOTIF-316
  - TC-FA-NOTIF-317
  - TC-FA-NOTIF-319
coverage:
  web: automated
---

# Resolusi Penerima Notifikasi Berdasarkan Pemegang Aset: Group Manager, Borrower, Assignee, dan PIC Admin

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role karena penerima berbeda per TC dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-315 | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |
  | TC-FA-NOTIF-316 | Borrower Budi Santoso | #11 | `borrowerBudi_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_BORROWER_PASSWORD` | `Fixture.fixedAssetNotification.borrowerBudi` |
  | TC-FA-NOTIF-317 | Assignee Siti Rahmawati | #12 | `assigneeSiti_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSIGNEE_PASSWORD` | `Fixture.fixedAssetNotification.assigneeSiti` |
  | TC-FA-NOTIF-319 | Asset Admin (PIC pembuat BRW-2026-0342) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |

- Login akun aktor pertama (Group Manager, Pre-setup #3) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu Mark as Repaired dan Mark as Found: Asset Admin (Pre-setup #8) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 dan Laptop - 1 AST-2024-0067 (Pre-setup #24, Gedung A), transaksi BRW-2026-0342 (Pre-setup #19). Keadaan awal per blok (aset Damaged tanpa pemegang dan PIC; Damaged dan Borrowed oleh Budi Santoso; Missing dan Assigned ke Siti Rahmawati; BRW-2026-0342 Waiting for Confirmation dengan sisa 24 jam) diatur fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dan fixture BE penyetel state sumber, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE penyetel state aset dan transaksi; fixture BE pemicu Mark as Repaired dan Mark as Found; menjalankan job `F-FATX-07` langkah 2 (butir "Kemampuan menjalankan job latar" di `suite.md`); membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Asersi TC-FA-NOTIF-315, 316, dan 317 bersyarat pada Open Item #6 PRD (menunggu keputusan produk) dan dapat direvisi.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang menyetel state dan memicu Mark as Repaired, Mark as Found, serta job `F-FATX-07` pada AST-2024-0141 dan AST-2024-0067 (Pre-setup #24) dan BRW-2026-0342 (Pre-setup #19) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_GM_PASSWORD`, `FA_BORROWER_PASSWORD`, `FA_ASSIGNEE_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-315: aset Available tanpa pemegang atau PIC, penerima Group Manager

1. Catat jumlah item `"Asset has been repaired"` milik Group Manager Gedung A (baseline) lewat fixture BE
2. Atur aset Kamera DSLR AST-2024-0141 berstatus Damaged, Available tanpa pemegang dan tanpa PIC aset, di Gedung A lewat fixture BE
3. Dari akun Asset Admin (Pre-setup #8, sesi API), Mark as Repaired aset AST-2024-0141 hingga status repaired tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai Group Manager
6. Verifikasi (kemampuan baca BE) jumlah item `"Asset has been repaired"` bertambah tepat 1 dari baseline
7. Verifikasi item `"Asset has been repaired"` dengan Body `"Kamera DSLR (AST-2024-0141) has been repaired and is ready for use."` tampil pada Dropdown Panel Group Manager

### TC-FA-NOTIF-316: aset Borrowed, penerima pemegang saat ini

8. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
9. Catat jumlah item `"Asset has been repaired"` milik Budi Santoso (baseline) lewat fixture BE
10. Atur aset AST-2024-0141 berstatus Damaged dan Borrowed oleh Budi Santoso lewat fixture BE
11. Dari akun Asset Admin (Pre-setup #8, sesi API), Mark as Repaired aset AST-2024-0141 hingga status repaired tersimpan
12. Logout, lalu login sebagai Budi Santoso (Pre-setup #11), lalu buka Fixed Asset > Dashboard
13. Klik Bell icon sebagai Budi Santoso
14. Verifikasi (kemampuan baca BE) jumlah item `"Asset has been repaired"` bertambah tepat 1 dari baseline
15. Verifikasi item `"Asset has been repaired"` tampil pada Dropdown Panel Budi Santoso sebagai pemegang saat ini

### TC-FA-NOTIF-317: aset Assigned, penerima Assignee pemegang saat ini

16. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
17. Catat jumlah item `"Asset has been found"` milik Siti Rahmawati (baseline) lewat fixture BE
18. Atur aset AST-2024-0067 berstatus Missing dan Assigned ke Siti Rahmawati lewat fixture BE
19. Dari akun Asset Admin (Pre-setup #8, sesi API), Mark as Found aset AST-2024-0067 hingga status found tersimpan
20. Logout, lalu login sebagai Siti Rahmawati (Pre-setup #12), lalu buka Fixed Asset > Dashboard
21. Klik Bell icon sebagai Siti Rahmawati
22. Verifikasi (kemampuan baca BE) jumlah item `"Asset has been found"` bertambah tepat 1 dari baseline
23. Verifikasi item `"Asset has been found"` tampil pada Dropdown Panel Siti Rahmawati

### TC-FA-NOTIF-319: almost_timeout varian PIC admin pada Waiting for Confirmation

24. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
25. Atur BRW-2026-0342 berstatus Waiting for Confirmation dengan timeout snapshot 3 hari dan sisa 24 jam lewat fixture BE
26. Jalankan job `F-FATX-07` langkah 2 hingga notifikasi tersimpan
27. Logout, lalu login sebagai Asset Admin (Pre-setup #8), lalu buka Fixed Asset > Dashboard
28. Klik Bell icon
29. Verifikasi item `"Please finish this transaction — expiring soon"` untuk BRW-2026-0342 tampil pada Dropdown Panel
30. Verifikasi tombol `[Detail]` tampil pada item `"Please finish this transaction — expiring soon"` (actionable)

## Notes

- Langkah penghubung (S-03): langkah 4 (muat ulang agar notifikasi hasil pemicu termuat); langkah 8, 16, dan 24 (pulihkan seed antar blok); langkah 1, 9, dan 17 (baseline per TC, bagian 8b butir 10); langkah 2, 10, 18, dan 25 (precondition TC lewat fixture BE); langkah 12, 20, dan 27 (ganti akun dan buka Fixed Asset > Dashboard).
- Job `F-FATX-07` (langkah 26) hanya pemicu keadaan, bukan objek uji.
- Asersi langkah 6, 7, 14, 15, 22, dan 23 (TC-FA-NOTIF-315, 316, 317) bersyarat pada Open Item #6 PRD.
- Pembagian per TC: TC-FA-NOTIF-315 (langkah 1 sampai 7), TC-FA-NOTIF-316 (langkah 8 sampai 15), TC-FA-NOTIF-317 (langkah 16 sampai 23), TC-FA-NOTIF-319 (langkah 24 sampai 30).
- Temuan untuk QA:
  - TC-FA-NOTIF-315, 316, dan 317 tidak menyebut akun pelaku Mark as Repaired dan Mark as Found; spec memakai sesi API Asset Admin (Pre-setup #8).
  - TC-FA-NOTIF-315, 316, 317 menulis penerima tanpa nomor Pre-setup; spec memakai Pre-setup #3, #11, dan #12.
  - TC-FA-NOTIF-316 mengharapkan penerima pemegang saat ini tetapi tidak menyebut apakah PIC aset juga menerima; tidak diasersi.
  - Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
