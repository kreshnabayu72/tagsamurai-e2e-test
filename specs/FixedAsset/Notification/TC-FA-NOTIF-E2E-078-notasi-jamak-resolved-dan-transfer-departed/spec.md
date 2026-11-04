---
id: TC-FA-NOTIF-E2E-078-notasi-jamak-resolved-dan-transfer-departed
title: "Notasi Jamak Notifikasi Resolved Approved dan Transfer Departed untuk Asset Admin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-299
  - TC-FA-NOTIF-300
  - TC-FA-NOTIF-301
  - TC-FA-NOTIF-302
  - TC-FA-NOTIF-303
coverage:
  web: automated
---

# Notasi Jamak Notifikasi Resolved Approved dan Transfer Departed untuk Asset Admin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`; pemohon BRW-2026-0341, TRF-2026-0056, DSP-2026-0031, dan ASG-2026-0121, serta penerima di group tujuan Transfer). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Approver Borrowing & Assignment (Pre-setup #4, `Spectra.env.FA_APPROVERBA_PASSWORD`), Approver Transfer (Pre-setup #5, `Spectra.env.FA_APPROVERTRF_PASSWORD`), dan Approver Disposal (Pre-setup #6, `Spectra.env.FA_APPROVERDSP_PASSWORD`).
- Data Pre-setup (tetap di environment): transaksi BRW-2026-0341 (Pre-setup #19), ASG-2026-0121 (Pre-setup #20), TRF-2026-0056 (Pre-setup #21), dan DSP-2026-0031 (Pre-setup #22), masing-masing 2 aset (Pre-setup #24); keadaan awal per blok (Waiting for Approval; TRF-2026-0056 Waiting for Departure untuk TC-FA-NOTIF-303) disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Keadaan awal tiap blok diatur fixture BE penyetel state sumber sesudah pemulihan seed (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu Approve oleh Approver dan konfirmasi Departure Transfer lewat sesi API aktor; membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu Approve dan konfirmasi Departure pada BRW-2026-0341, ASG-2026-0121, TRF-2026-0056, dan DSP-2026-0031 (Pre-setup #19 sampai #22 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_APPROVERBA_PASSWORD`, `FA_APPROVERTRF_PASSWORD`, dan `FA_APPROVERDSP_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-299: borrow_resolved varian Approved dengan 2 aset

1. Pulihkan seed lalu atur BRW-2026-0341 dua aset Waiting for Approval lewat fixture BE penyetel state sumber
2. Catat jumlah item `"Your request has been approved"` milik Asset Admin (baseline) lewat fixture BE
3. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status Approved tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai penerima
6. Verifikasi (kemampuan baca BE) jumlah item `"Your request has been approved"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
7. Verifikasi Title item teratas `"Your request has been approved"`
8. Verifikasi Body item teratas `"BRW-2026-0341 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-300: transfer_resolved varian Approved dengan 2 aset

9. Pulihkan seed lalu atur TRF-2026-0056 dua aset Waiting for Approval lewat fixture BE penyetel state sumber
10. Catat jumlah item `"Your request has been approved"` milik Asset Admin (baseline) lewat fixture BE
11. Dari akun Approver Transfer (Pre-setup #5, sesi API), Approve TRF-2026-0056 hingga status Approved tersimpan
12. Muat ulang halaman Fixed Asset > Dashboard
13. Klik Bell icon sebagai penerima
14. Verifikasi (kemampuan baca BE) jumlah item `"Your request has been approved"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
15. Verifikasi Title item teratas `"Your request has been approved"`
16. Verifikasi Body item teratas `"TRF-2026-0056 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-301: disposal_resolved varian Approved dengan 2 aset

17. Pulihkan seed lalu atur DSP-2026-0031 dua aset Waiting for Approval lewat fixture BE penyetel state sumber
18. Catat jumlah item `"Your request has been approved"` milik Asset Admin (baseline) lewat fixture BE
19. Dari akun Approver Disposal (Pre-setup #6, sesi API), Approve DSP-2026-0031 hingga status Approved tersimpan
20. Muat ulang halaman Fixed Asset > Dashboard
21. Klik Bell icon sebagai penerima
22. Verifikasi (kemampuan baca BE) jumlah item `"Your request has been approved"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
23. Verifikasi Title item teratas `"Your request has been approved"`
24. Verifikasi Body item teratas `"DSP-2026-0031 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-302: assignment_resolved varian Approved dengan 2 aset

25. Pulihkan seed lalu atur ASG-2026-0121 dua aset Waiting for Approval lewat fixture BE penyetel state sumber
26. Catat jumlah item `"Your request has been approved"` milik Asset Admin (baseline) lewat fixture BE
27. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve ASG-2026-0121 hingga status Approved tersimpan
28. Muat ulang halaman Fixed Asset > Dashboard
29. Klik Bell icon sebagai penerima
30. Verifikasi (kemampuan baca BE) jumlah item `"Your request has been approved"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
31. Verifikasi Title item teratas `"Your request has been approved"`
32. Verifikasi Body item teratas `"ASG-2026-0121 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-303: transfer_departed dengan 2 aset

33. Pulihkan seed lalu atur TRF-2026-0056 dua aset Waiting for Departure lewat fixture BE penyetel state sumber
34. Catat jumlah item `"Asset incoming transfer ready for arrival"` milik Asset Admin (baseline) lewat fixture BE
35. Dari akun pelaku Departure (sesi API), konfirmasi Departure TRF-2026-0056 (Waiting for Departure) hingga status Departure tersimpan
36. Muat ulang halaman Fixed Asset > Dashboard
37. Klik Bell icon sebagai penerima (Asset Admin group tujuan)
38. Verifikasi (kemampuan baca BE) jumlah item `"Asset incoming transfer ready for arrival"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
39. Verifikasi Title item teratas `"Asset incoming transfer ready for arrival"`
40. Verifikasi Body item teratas `"TRF-2026-0056 (2 Assets)"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

## Notes

- Langkah penghubung (S-03): langkah 4, 12, 20, 28, dan 36 (muat ulang agar notifikasi hasil pemicu termuat); langkah 1, 9, 17, 25, dan 33 (pulihkan seed dan atur precondition TC lewat fixture BE penyetel state sumber); langkah 2, 10, 18, 26, dan 34 (baseline per TC, bagian 8b butir 10).
- Pemicu event dijalankan di modul sumber lewat sesi API aktor dan asersi hanya pada Bell icon dan Dropdown Panel (Catatan TC).
- Pembagian per TC: TC-FA-NOTIF-299 (langkah 1 sampai 8), TC-FA-NOTIF-300 (langkah 9 sampai 16), TC-FA-NOTIF-301 (langkah 17 sampai 24), TC-FA-NOTIF-302 (langkah 25 sampai 32), TC-FA-NOTIF-303 (langkah 33 sampai 40).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruh blok satu topik (notasi jamak untuk penerima Asset Admin yang sama), tiap blok berdiri sendiri karena diawali pemulihan seed, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; tiga dari tiap delapan langkah blok adalah langkah penghubung per TC (pemulihan seed, baseline, dan muat ulang).
- Temuan untuk QA:
  - TC-FA-NOTIF-299 sampai 302 menulis pemicu "Approver Approve" tanpa menyebut akun; spec memetakan Approver Borrowing & Assignment ke Pre-setup #4, Approver Transfer ke #5, dan Approver Disposal ke #6.
  - TC-FA-NOTIF-303 menulis precondition "penerima uji ditetapkan pemilik produk" tanpa menyebut akun penerima dan akun pelaku Departure; spec memakai Asset Admin (Pre-setup #8) sebagai penerima dan menandai akun pelaku Departure sebagai kemampuan sesi API yang disediakan tim FE/BE.
  - Kolom Post Condition kelima TC kosong (`-`); tidak ada yang diasersi.
