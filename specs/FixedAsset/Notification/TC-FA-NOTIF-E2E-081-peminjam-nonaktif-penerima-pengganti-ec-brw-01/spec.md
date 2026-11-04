---
id: TC-FA-NOTIF-E2E-081-peminjam-nonaktif-penerima-pengganti-ec-brw-01
title: "Peminjam Nonaktif: Penerima Pengganti Atasan Peminjam untuk Overdue, Due Soon, Confirmation Required, dan Handover Completed (EC-BRW-01)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-318
  - TC-FA-NOTIF-401
  - TC-FA-NOTIF-402
  - TC-FA-NOTIF-403
coverage:
  web: automated
---

# Peminjam Nonaktif: Penerima Pengganti Atasan Peminjam untuk Overdue, Due Soon, Confirmation Required, dan Handover Completed (EC-BRW-01)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: atasan peminjam Budi Santoso (Pre-setup #27, `atasanBudi_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ATASANBUDI_PASSWORD`, `Fixture.fixedAssetNotification.atasanBudi`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu: Asset Admin (Pre-setup #8, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- State yang diubah dan dipulihkan: Borrower Budi Santoso (Pre-setup #11) dinonaktifkan lewat fixture BE di hook `before` dan diaktifkan kembali di hook `after`; fixture BE pemulih seed dan transaksi (Pre-setup #17 sampai #24) tidak mengubah status akun Budi Santoso. Jam server dan jam fixture pada blok TC-FA-NOTIF-401 diatur ke 22/06/26 lalu dipulihkan ke 18/06/26 sesudah job selesai dan di hook `after`.
- Data Pre-setup (tetap di environment): aset Kamera DSLR AST-2024-0141 pada BRW-2026-0342 (Pre-setup #19 dan #24), Due Date 25/06/26. Keadaan awal per blok (Borrowed dengan Due Date terlewati; Borrowed; Ready for Verification; Ready for Handover) diatur fixture BE penyetel state sumber, dijalankan sebagai langkah penghubung (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); seed dipulihkan fixture BE pemulih di hook `before`, `after`, dan antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu verifikasi scan dan handover; menjalankan job overdue harian dan job due soon harian serta menggeser jam; membaca daftar dan jumlah notifikasi per penerima, termasuk akun nonaktif Budi Santoso, per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Asersi absence atas notifikasi in-app memakai baseline per penerima (kemampuan baca BE) yang dicatat sebelum pemicu, anchor positif (akun Pre-setup #27 menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" sebelum tiap pembacaan BE absence penerima nonaktif; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah memicu job overdue dan due soon, verifikasi scan, dan handover pada BRW-2026-0342 dan AST-2024-0141 (Pre-setup #19 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Format tanggal Body item `Kamera DSLR is due on 25/06/26.` (langkah 19) mengikuti Date Format General Settings default `dd/MM/yy` dengan jam fixture hari ini 18/06/26 (zona Asia/Jakarta).
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ATASANBUDI_PASSWORD` dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-318: notifikasi jatuh tempo (overdue)

1. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
2. Atur AST-2024-0141 berstatus Borrowed dengan Due Date terlewati lewat fixture BE
3. Catat jumlah item `"Your borrowed asset is overdue"` milik akun Pre-setup #27 dan milik Budi Santoso (nonaktif) (baseline) lewat fixture BE
4. Jalankan job overdue harian hingga notifikasi tersimpan
5. Muat ulang halaman Fixed Asset > Dashboard
6. Klik Bell icon sebagai akun Pre-setup #27
7. Verifikasi (kemampuan baca BE) jumlah item `"Your borrowed asset is overdue"` milik akun Pre-setup #27 bertambah tepat 1 dari baseline
8. Verifikasi item `"Your borrowed asset is overdue"` tampil pada Dropdown Panel akun Pre-setup #27
9. Tunggu 5 detik tanpa memuat ulang halaman
10. Verifikasi jumlah item `"Your borrowed asset is overdue"` milik Budi Santoso (nonaktif) sama dengan baseline lewat fixture BE

### TC-FA-NOTIF-401: notifikasi due soon

11. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
12. Atur AST-2024-0141 berstatus Borrowed pada BRW-2026-0342 dengan Due Date 25/06/26 lewat fixture BE
13. Catat jumlah item `"Your borrowed asset is due soon"` milik akun Pre-setup #27 dan milik Budi Santoso (nonaktif) (baseline) lewat fixture BE
14. Atur jam server dan jam fixture ke 22/06/26 (H-3 untuk Due Date 25/06/26)
15. Jalankan job harian due soon hingga notifikasi tersimpan
16. Pulihkan jam server dan jam fixture ke 18/06/26
17. Muat ulang halaman Fixed Asset > Dashboard
18. Klik Bell icon sebagai akun Pre-setup #27
19. Verifikasi item `"Your borrowed asset is due soon"` dengan Body `"Kamera DSLR is due on 25/06/26."` tampil pada Dropdown Panel akun Pre-setup #27
20. Verifikasi (kemampuan baca BE) jumlah item `"Your borrowed asset is due soon"` milik akun Pre-setup #27 bertambah tepat 1 dari baseline
21. Tunggu 5 detik tanpa memuat ulang halaman
22. Verifikasi jumlah item `"Your borrowed asset is due soon"` milik Budi Santoso (nonaktif) sama dengan baseline lewat fixture BE

### TC-FA-NOTIF-402: borrow_confirmation_required

23. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
24. Atur BRW-2026-0342 (Kamera DSLR AST-2024-0141) berstatus Ready for Verification lewat fixture BE
25. Catat jumlah item `"Please confirm your borrowed asset"` milik akun Pre-setup #27 dan milik Budi Santoso (nonaktif) (baseline) lewat fixture BE
26. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan BRW-2026-0342 hingga status Waiting for Confirmation tersimpan
27. Muat ulang halaman Fixed Asset > Dashboard
28. Klik Bell icon sebagai akun Pre-setup #27
29. Verifikasi item `"Please confirm your borrowed asset"` dengan Body `"Kamera DSLR (AST-2024-0141)"` tampil pada Dropdown Panel akun Pre-setup #27
30. Verifikasi (kemampuan baca BE) jumlah item `"Please confirm your borrowed asset"` milik akun Pre-setup #27 bertambah tepat 1 dari baseline
31. Tunggu 5 detik tanpa memuat ulang halaman
32. Verifikasi jumlah item `"Please confirm your borrowed asset"` milik Budi Santoso (nonaktif) sama dengan baseline lewat fixture BE

### TC-FA-NOTIF-403: borrow_handover_completed

33. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
34. Atur BRW-2026-0342 (Kamera DSLR AST-2024-0141) berstatus Ready for Handover lewat fixture BE
35. Catat jumlah item `"Asset handover completed"` milik akun Pre-setup #27 dan milik Budi Santoso (nonaktif) (baseline) lewat fixture BE
36. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover BRW-2026-0342 hingga status handover tersimpan
37. Muat ulang halaman Fixed Asset > Dashboard
38. Klik Bell icon sebagai akun Pre-setup #27
39. Verifikasi item `"Asset handover completed"` dengan Body `"Kamera DSLR is now officially your responsibility."` tampil pada Dropdown Panel akun Pre-setup #27
40. Verifikasi (kemampuan baca BE) jumlah item `"Asset handover completed"` milik akun Pre-setup #27 bertambah tepat 1 dari baseline
41. Tunggu 5 detik tanpa memuat ulang halaman
42. Verifikasi jumlah item `"Asset handover completed"` milik Budi Santoso (nonaktif) sama dengan baseline lewat fixture BE

## Notes

- Langkah penghubung (S-03): langkah 5, 17, 27, dan 37 (muat ulang agar notifikasi hasil pemicu termuat); langkah 1, 11, 23, dan 33 (pulihkan seed antar blok); langkah 3, 13, 25, dan 35 (baseline per TC); langkah 2, 12, 24, dan 34 (precondition TC lewat fixture BE); langkah 14 dan 16 (jam; dipulihkan sebelum akun penerima dibuka, S-09).
- Langkah 9, 21, 31, dan 41 (jendela 5 detik tanpa memuat ulang halaman sebelum pembacaan BE absence penerima nonaktif, bagian 6) adalah langkah penghubung tanpa Verifikasi (S-03).
- Asersi "Budi Santoso (nonaktif) tidak menerima" dibaca lewat fixture BE (TC langkah 3 menyebut "lewat fixture BE"), dan didahului penerimaan item oleh akun Pre-setup #27 pada blok yang sama sebagai anchor positif (bagian 8b butir 2).
- Job overdue dan due soon (langkah 4 dan 15) hanya pemicu keadaan; batas waktunya diuji di spec 093 dan 095.
- Spec ini melewati sekitar 35 langkah (42). Alasan: seluruh blok satu topik (penerima pengganti atasan peminjam nonaktif), tiap blok berdiri sendiri karena diawali pemulihan seed dan transaksi, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; sebagian besar langkah adalah langkah penghubung per TC (pemulihan seed, precondition, baseline, dan muat ulang).
- Pembagian per TC: TC-FA-NOTIF-318 (langkah 1 sampai 10), TC-FA-NOTIF-401 (langkah 11 sampai 22), TC-FA-NOTIF-402 (langkah 23 sampai 32), TC-FA-NOTIF-403 (langkah 33 sampai 42).
- Temuan untuk QA:
  - TC-FA-NOTIF-318 tidak menyebut tanggal acuan jam untuk "Due Date terlewati" dan Body notifikasi overdue; hanya Title yang diasersi.
  - TC-FA-NOTIF-318, 401, 402, 403 menyebut penerima pengganti "sesuai resolusi modul Borrow" (borrow.md §6.3) tanpa mendefinisikan siapa yang menjadi penerima; spec memakai akun Pre-setup #27 sesuai Pre-setup TC.
  - Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
