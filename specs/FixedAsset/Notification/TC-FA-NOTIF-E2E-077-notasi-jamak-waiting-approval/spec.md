---
id: TC-FA-NOTIF-E2E-077-notasi-jamak-waiting-approval
title: "Notasi Jamak Notifikasi Waiting for Approval untuk Approver: Borrow, Assignment, Transfer, dan Disposal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-295
  - TC-FA-NOTIF-296
  - TC-FA-NOTIF-297
  - TC-FA-NOTIF-298
coverage:
  web: automated
---

# Notasi Jamak Notifikasi Waiting for Approval untuk Approver: Borrow, Assignment, Transfer, dan Disposal

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role karena Approver tiap jenis transaksi berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-295, TC-FA-NOTIF-296 | Approver (Borrowing & Assignment, Gedung A) | #4 | `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment` |
  | TC-FA-NOTIF-297 | Approver (Transfer, Gedung A) | #5 | `approverTransfer_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERTRF_PASSWORD` | `Fixture.fixedAssetNotification.approverTransfer` |
  | TC-FA-NOTIF-298 | Approver (Disposal, Gedung A) | #6 | `approverDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSP_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposal` |

- Login akun aktor pertama (Approver Borrowing & Assignment, Pre-setup #4) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Data Pre-setup (tetap di environment): transaksi BRW-2026-0341 (Pre-setup #19), ASG-2026-0121 (Pre-setup #20), TRF-2026-0056 (Pre-setup #21), dan DSP-2026-0031 (Pre-setup #22), masing-masing 2 aset (Pre-setup #24); Approval ON untuk keempat jenis transaksi. Keadaan awal dan Approval ON disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Keadaan awal tiap blok diatur fixture BE penyetel state sumber sesudah pemulihan seed (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu submit Borrow, Assignment, Transfer, dan Request Disposal formal lewat sesi API aktor; membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang men-submit BRW-2026-0341, ASG-2026-0121, TRF-2026-0056, dan DSP-2026-0031 (Pre-setup #19 sampai #22 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_APPROVERBA_PASSWORD`, `FA_APPROVERTRF_PASSWORD`, `FA_APPROVERDSP_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-295: borrow_waiting_approval dengan 2 aset

1. Pulihkan seed lalu atur Approval ON dan BRW-2026-0341 dua aset berupa draf siap submit lewat fixture BE penyetel state sumber
2. Catat jumlah item `"Waiting for your approval"` milik Approver Borrowing & Assignment (baseline) lewat fixture BE
3. Dari akun Asset Admin (Pre-setup #8, sesi API), submit BRW-2026-0341 (2 aset) dengan Approval ON hingga status Waiting for Approval tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai penerima
6. Verifikasi (kemampuan baca BE) jumlah item `"Waiting for your approval"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
7. Verifikasi Title item teratas `"Waiting for your approval"`
8. Verifikasi Body item teratas `"BRW-2026-0341 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-296: assignment_waiting_approval dengan 2 aset

9. Pulihkan seed lalu atur Approval ON dan ASG-2026-0121 dua aset berupa draf siap submit lewat fixture BE penyetel state sumber
10. Catat jumlah item `"Waiting for your approval"` milik Approver Borrowing & Assignment (baseline) lewat fixture BE
11. Dari akun Asset Admin (Pre-setup #8, sesi API), submit ASG-2026-0121 (2 aset) dengan Approval ON hingga status Waiting for Approval tersimpan
12. Muat ulang halaman Fixed Asset > Dashboard
13. Klik Bell icon sebagai penerima
14. Verifikasi (kemampuan baca BE) jumlah item `"Waiting for your approval"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
15. Verifikasi Title item teratas `"Waiting for your approval"`
16. Verifikasi Body item teratas `"ASG-2026-0121 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-297: transfer_waiting_approval dengan 2 aset

17. Pulihkan seed lalu atur Approval ON dan TRF-2026-0056 dua aset berupa draf siap submit lewat fixture BE penyetel state sumber
18. Catat jumlah item `"Waiting for your approval"` milik Approver Transfer (baseline) lewat fixture BE
19. Dari akun Asset Admin (Pre-setup #8, sesi API), submit TRF-2026-0056 (2 aset) dengan Approval ON hingga status Waiting for Approval tersimpan
20. Logout, lalu login sebagai Approver Transfer (Gedung A, Pre-setup #5), lalu buka Fixed Asset > Dashboard
21. Klik Bell icon sebagai penerima
22. Verifikasi (kemampuan baca BE) jumlah item `"Waiting for your approval"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
23. Verifikasi Title item teratas `"Waiting for your approval"`
24. Verifikasi Body item teratas `"TRF-2026-0056 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-298: disposal_waiting_approval dengan 2 aset

25. Pulihkan seed lalu atur Approval ON dan DSP-2026-0031 dua aset berupa draf siap submit lewat fixture BE penyetel state sumber
26. Catat jumlah item `"Waiting for your approval"` milik Approver Disposal (baseline) lewat fixture BE
27. Dari akun Asset Admin (Pre-setup #8, sesi API), ajukan Request Disposal formal DSP-2026-0031 (2 aset) dengan Approval ON hingga status Waiting for Approval tersimpan
28. Logout, lalu login sebagai Approver Disposal (Gedung A, Pre-setup #6), lalu buka Fixed Asset > Dashboard
29. Klik Bell icon sebagai penerima
30. Verifikasi (kemampuan baca BE) jumlah item `"Waiting for your approval"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
31. Verifikasi Title item teratas `"Waiting for your approval"`
32. Verifikasi Body item teratas `"DSP-2026-0031 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

## Notes

- Langkah penghubung (S-03): langkah 4 dan 12 (muat ulang agar notifikasi hasil pemicu termuat); langkah 1, 9, 17, dan 25 (pulihkan seed dan atur precondition TC lewat fixture BE penyetel state sumber); langkah 2, 10, 18, dan 26 (baseline per TC, bagian 8b butir 10); langkah 20 dan 28 (ganti akun dan buka Fixed Asset > Dashboard).
- Pemicu event dijalankan di modul sumber lewat sesi API aktor dan asersi hanya pada Bell icon dan Dropdown Panel (Catatan TC).
- Pembagian per TC: TC-FA-NOTIF-295 (langkah 1 sampai 8), TC-FA-NOTIF-296 (langkah 9 sampai 16), TC-FA-NOTIF-297 (langkah 17 sampai 24), TC-FA-NOTIF-298 (langkah 25 sampai 32).
- Temuan untuk QA:
  - TC-FA-NOTIF-295 sampai 298 menulis role penerima tanpa nomor Pre-setup dan pemicu "submit" tanpa akun pelaku; spec memetakan Approver Borrowing & Assignment ke Pre-setup #4, Approver Transfer ke #5, Approver Disposal ke #6, dan memakai sesi API Asset Admin (Pre-setup #8) sebagai pengaju.
  - TC-FA-NOTIF-295 sampai 298 menulis precondition hanya "Approval ON"; keadaan awal transaksi (draf siap submit) tidak disebut dan disiapkan fixture BE pemulih seed.
  - Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
