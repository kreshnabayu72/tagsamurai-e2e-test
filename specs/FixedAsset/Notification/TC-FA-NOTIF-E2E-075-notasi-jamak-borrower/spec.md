---
id: TC-FA-NOTIF-E2E-075-notasi-jamak-borrower
title: "Notasi Jamak Notifikasi Borrow untuk Borrower: Satu Notifikasi per Transaksi dan Satu per Aset untuk Pengingat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-289
  - TC-FA-NOTIF-290
  - TC-FA-NOTIF-310
  - TC-FA-NOTIF-313
  - TC-FA-NOTIF-314
coverage:
  web: automated
---

# Notasi Jamak Notifikasi Borrow untuk Borrower: Satu Notifikasi per Transaksi dan Satu per Aset untuk Pengingat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Borrower Budi Santoso (Pre-setup #11, `borrowerBudi_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_BORROWER_PASSWORD`, `Fixture.fixedAssetNotification.borrowerBudi`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0341 dengan 2 aset, Proyektor AST-2024-0150 dan Laptop - 2 AST-2024-0068 (Pre-setup #19 dan #24); keadaan awal transaksi per blok (Ready for Verification, Ready for Handover, Waiting for Confirmation, Borrowed dengan Due Date 25/06/26) disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Tanggal acuan fixture "hari ini" adalah 18/06/26. Keadaan awal tiap blok diatur fixture BE penyetel state sumber sesudah pemulihan seed (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu event modul sumber (verifikasi scan, handover, aksi konfirmasi Borrower) lewat sesi API aktor; menjalankan job overdue harian dan job due soon harian serta menggeser jam server dan jam fixture bersama (butir "Kemampuan menjalankan job latar" di `suite.md`); membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Format tanggal Body item mengikuti Date Format General Settings default `dd/MM/yy` dengan jam fixture hari ini 18/06/26 (zona Asia/Jakarta); BRW-2026-0341 Borrowed dengan Due Date 25/06/26 (Proyektor AST-2024-0150 dan Laptop - 2 AST-2024-0068) pada blok TC-FA-NOTIF-313 dan TC-FA-NOTIF-314 disiapkan fixture BE, dan ambang H-1 tercapai pada jam 24/06/26.
- State global: jam server dan jam fixture pada blok TC-FA-NOTIF-313 dan TC-FA-NOTIF-314 diatur ke 26/06/26 dan 24/06/26, lalu dipulihkan ke 18/06/26 segera sesudah job selesai dan di hook `after`. Seed notifikasi dan transaksi dipulihkan di hook `after`.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu verifikasi scan, handover, konfirmasi, dan job overdue serta due soon pada transaksi BRW-2026-0341 (Pre-setup #19 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_BORROWER_PASSWORD` dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-289: borrow_confirmation_required dengan 2 aset

1. Pulihkan seed lalu atur BRW-2026-0341 dua aset Ready for Verification lewat fixture BE penyetel state sumber
2. Catat jumlah item `"Please confirm your borrowed asset"` milik Budi Santoso (baseline) lewat fixture BE
3. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan BRW-2026-0341 (2 aset) hingga status Waiting for Confirmation tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai penerima
6. Verifikasi (kemampuan baca BE) jumlah item `"Please confirm your borrowed asset"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
7. Verifikasi Title item teratas `"Please confirm your borrowed asset"`
8. Verifikasi Body item teratas `"BRW-2026-0341 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-290: borrow_handover_completed dengan 2 aset

9. Pulihkan seed lalu atur BRW-2026-0341 dua aset Ready for Handover lewat fixture BE penyetel state sumber
10. Catat jumlah item `"Asset handover completed"` milik Budi Santoso (baseline) lewat fixture BE
11. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover fisik BRW-2026-0341 (2 aset) hingga status handover tersimpan
12. Muat ulang halaman Fixed Asset > Dashboard
13. Klik Bell icon sebagai penerima
14. Verifikasi (kemampuan baca BE) jumlah item `"Asset handover completed"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
15. Verifikasi Title item teratas `"Asset handover completed"`
16. Verifikasi Body item teratas `"BRW-2026-0341 (2 Assets) is now officially your responsibility."` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-310: Auto-Read tingkat transaksi

17. Pulihkan seed lalu atur BRW-2026-0341 dua aset Ready for Verification sebagai keadaan awal pembentuk precondition notifikasi `borrow_confirmation_required` Unread (dibentuk langkah 19) lewat fixture BE penyetel state sumber
18. Catat jumlah item `"Please confirm your borrowed asset"` milik Budi Santoso (baseline) lewat fixture BE
19. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan BRW-2026-0341 (2 aset) hingga notifikasi `borrow_confirmation_required` tersimpan (dipakai sebagai precondition TC, tidak diasersi)
20. Dari akun Budi Santoso (sesi API), konfirmasi transaksi BRW-2026-0341 (seluruh aset) hingga konfirmasi tersimpan
21. Muat ulang halaman Fixed Asset > Dashboard
22. Klik Bell icon
23. Verifikasi (kemampuan baca BE) jumlah item `"Please confirm your borrowed asset"` bertambah tepat 1 dari baseline (satu notifikasi untuk transaksi)
24. Verifikasi item `"Please confirm your borrowed asset"` BRW-2026-0341 berstatus Read
25. Verifikasi item `"Please confirm your borrowed asset"` BRW-2026-0341 tanpa tombol
26. Verifikasi tidak ada item `"Please confirm your borrowed asset"` untuk BRW-2026-0341 yang berstatus Unread (tidak ada keadaan Read parsial per aset)

### TC-FA-NOTIF-313: borrow_overdue dua aset

27. Pulihkan seed lalu atur BRW-2026-0341 dua aset Borrowed (Proyektor AST-2024-0150 dan Laptop - 2 AST-2024-0068) dengan Due Date 25/06/26 dan pengingat overdue aktif lewat fixture BE penyetel state sumber
28. Catat jumlah item `"Your borrowed asset is overdue"` milik Budi Santoso (baseline) lewat fixture BE
29. Atur jam server dan jam fixture ke 26/06/26
30. Jalankan job overdue harian hingga notifikasi tersimpan
31. Pulihkan jam server dan jam fixture ke 18/06/26
32. Muat ulang halaman Fixed Asset > Dashboard
33. Klik Bell icon
34. Verifikasi (kemampuan baca BE) jumlah item `"Your borrowed asset is overdue"` bertambah tepat 2 dari baseline (satu notifikasi per aset)
35. Verifikasi Body salah satu item `"Proyektor was due on 25/06/26."`
36. Verifikasi Body item lain `"Laptop - 2 was due on 25/06/26."`

### TC-FA-NOTIF-314: borrow_due_soon dua aset

37. Pulihkan seed lalu atur BRW-2026-0341 dua aset Borrowed (Proyektor AST-2024-0150 dan Laptop - 2 AST-2024-0068) dengan Due Date 25/06/26 lewat fixture BE penyetel state sumber
38. Catat jumlah item `"Your borrowed asset is due soon"` milik Budi Santoso (baseline) lewat fixture BE
39. Atur jam server dan jam fixture ke 24/06/26
40. Jalankan job due soon harian hingga notifikasi tersimpan
41. Pulihkan jam server dan jam fixture ke 18/06/26
42. Muat ulang halaman Fixed Asset > Dashboard
43. Klik Bell icon
44. Verifikasi (kemampuan baca BE) jumlah item `"Your borrowed asset is due soon"` bertambah tepat 2 dari baseline (satu notifikasi per aset)
45. Verifikasi Body salah satu item `"Proyektor is due on 25/06/26."`
46. Verifikasi Body item lain `"Laptop - 2 is due on 25/06/26."`

## Notes

- Langkah penghubung (S-03): langkah 4, 12, 21, 32, dan 42 (muat ulang agar notifikasi hasil pemicu termuat); langkah 1, 9, 17, 27, dan 37 (pulihkan seed dan atur precondition TC lewat fixture BE penyetel state sumber); langkah 2, 10, 18, 28, dan 38 (baseline per TC, bagian 8b butir 10); langkah 19 (precondition TC-FA-NOTIF-310: notifikasi Unread harus ada sebelum konfirmasi); langkah 31 dan 41 (pulihkan jam sebelum akun penerima dibuka, S-09).
- Pemicu event dijalankan di modul sumber lewat sesi API aktor dan asersi hanya pada Bell icon dan Dropdown Panel (Catatan TC). Job overdue dan due soon (langkah 30 dan 40) hanya pemicu keadaan, bukan objek uji; batas waktunya diuji di spec 093 dan 095.
- Pembagian per TC: TC-FA-NOTIF-289 (langkah 1 sampai 8), TC-FA-NOTIF-290 (langkah 9 sampai 16), TC-FA-NOTIF-310 (langkah 17 sampai 26), TC-FA-NOTIF-313 (langkah 27 sampai 36), TC-FA-NOTIF-314 (langkah 37 sampai 46).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruh blok satu topik (notasi jamak Borrow untuk satu akun Borrower), tiap blok berdiri sendiri karena diawali pemulihan seed, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; lebih dari separuh langkah adalah langkah penghubung per TC (pemulihan seed, baseline, muat ulang, dan pengaturan jam).
- Temuan untuk QA:
  - TC-FA-NOTIF-289, 290, 310 tidak menyebut akun pelaku pemicu (verifikasi scan, handover, konfirmasi) dan layar tempat Borrower mengonfirmasi (TC-FA-NOTIF-310 langkah 1 hanya "Konfirmasi transaksi ... (seluruh aset)"). Spec memakai sesi API Asset Admin (Pre-setup #8) untuk verifikasi scan dan handover, dan sesi API Budi Santoso untuk konfirmasi; layar konfirmasi tidak diasersi.
  - TC-FA-NOTIF-289, 290, 310 tidak menyebut keadaan awal selain "Ready for Verification" atau "Ready for Handover"; precondition "notifikasi Unread" TC-FA-NOTIF-310 tidak punya Expected sendiri, sehingga spec membentuknya lewat pemicu verifikasi scan (langkah 19).
  - TC-FA-NOTIF-313 dan 314 tidak menulis akun pemicu job dan tidak menyebut pemulihan jam; spec mengikuti kemampuan job dan jam di `suite.md`.
  - Kolom Post Condition TC-FA-NOTIF-289, 290, 310, 313, dan 314 kosong (`-`); tidak ada yang diasersi.
