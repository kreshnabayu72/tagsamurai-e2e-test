---
id: TC-FA-NOTIF-E2E-059-assignment-menunggu-persetujuan-dan-hasil-keputusan
title: "Penerimaan Notifikasi Assignment: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-238
  - TC-FA-NOTIF-239
  - TC-FA-NOTIF-240
coverage:
  web: automated
---
# Penerimaan Notifikasi Assignment: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Approver (Borrowing & Assignment, Gedung A) | #4 | `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment` |
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Men-submit Assignment Request.
- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Approver (Borrowing & Assignment, Gedung A) (Pre-setup #4, `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERBA_PASSWORD`). Approve atau Reject ASG-2026-0120 (Approver Borrowing & Assignment).
- Login akun aktor pertama (Approver (Borrowing & Assignment, Gedung A), Pre-setup #4) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): ASG-2026-0120 (Laptop - 1 AST-2024-0067; Pre-setup #20), aset Pre-setup #24. Spec mengubah status ASG-2026-0120 per blok; fixture BE pemulih mengembalikannya. Rejection Reason dibaca dari `Fixture.fixedAssetNotification.rejectionReason` (data TC `Budget belum tersedia`) dan diketik pada aksi Reject.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu submit, Approve, dan Reject pada ASG-2026-0120 dan aset AST-2024-0067 (Pre-setup #20 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_APPROVERBA_PASSWORD`, `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-238: Notifikasi assignment_waiting_approval diterima: Submit Assignment Request dengan approval ON

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Approval Assignment ON; aset Laptop - 1 (AST-2024-0067) Available, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Approver (Borrowing & Assignment) sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Asset Admin (Pre-setup #8, sesi API), submit Assignment Request aset Laptop - 1 (AST-2024-0067) dengan approval ON hingga ASG-2026-0120 berstatus Waiting for Approval tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Approver (Borrowing & Assignment) bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Waiting for your approval"` dan Body `"ASG-2026-0120 (1 Asset)"` (dari template `"[Transaction ID] (1 Asset)"`)
10. Verifikasi icon `time-line` dengan severity `primary` pada item
11. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
12. Klik `[Detail]` pada item tersebut
13. Verifikasi halaman tujuan `/fams/approvals/borrowing-assignment/ASG-2026-0120` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-239: Notifikasi assignment_resolved varian Approved diterima: Approver Approve

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Approval
16. Ganti akun: logout, lalu login sebagai Asset Admin (Gedung A) (Pre-setup #8) dengan `Spectra.env.FA_ASSETADMIN_PASSWORD`, lalu buka Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Approver (Borrowing & Assignment, Pre-setup #4, sesi API), Approve ASG-2026-0120 hingga status Approved tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Your request has been approved"` dan Body `"ASG-2026-0120 (1 Asset)"` (dari template `"[Transaction ID] (1 Asset)"`)
25. Verifikasi icon `checkbox-circle-line` dengan severity `success` pada item
26. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
27. Klik judul item tersebut (bukan tombol)
28. Verifikasi halaman tujuan `/fams/transactions-assignment/ASG-2026-0120` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-240: Notifikasi assignment_resolved varian Rejected diterima: Approver Reject

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Approval, lalu muat ulang halaman Fixed Asset > Dashboard
31. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
32. Dari akun Approver (Borrowing & Assignment, Pre-setup #4, sesi API), Reject ASG-2026-0120 dengan alasan `Fixture.fixedAssetNotification.rejectionReason` hingga status Rejected tersimpan
33. Klik Bell icon
34. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 31
35. Verifikasi item baru berada di posisi teratas Dropdown Panel
36. Verifikasi Title item baru bold
37. Verifikasi dot Unread tampil pada item baru
38. Verifikasi item menampilkan Title `"Your request has been rejected"` dan Body `"ASG-2026-0120: "` diikuti `Fixture.fixedAssetNotification.rejectionReason` (dari template `"[Transaction ID]: [Rejection Reason]"`)
39. Verifikasi icon `close-circle-line` dengan severity `danger` pada item
40. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
41. Klik judul item tersebut (bukan tombol)
42. Verifikasi halaman tujuan `/fams/transactions-assignment/ASG-2026-0120` terbuka
43. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 34

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30 (penyiapan kondisi data lewat fixture BE; pada langkah 1 dan 30 diikuti muat ulang halaman Fixed Asset > Dashboard sebelum baseline); langkah 16 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 17, 31 (pencatatan baseline badge Bell icon (S-12)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (43 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Spec 059, 060, dan 061 memakai ASG-2026-0120 yang sama, terbagi per tahap (persetujuan; penerimaan Assignee, handover, dan expired; decline dan accepted); transaksi dipulihkan fixture BE di awal tiap blok.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - Penerima TC-FA-NOTIF-239 dan 240 ditulis "Asset Admin (pemohon ASG-2026-0120)" tanpa nomor Pre-setup; spec memakai Asset Admin Pre-setup #8.
