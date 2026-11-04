---
id: TC-FA-NOTIF-E2E-064-disposal-menunggu-persetujuan-dan-hasil-keputusan
title: "Penerimaan Notifikasi Disposal: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-251
  - TC-FA-NOTIF-252
  - TC-FA-NOTIF-253
coverage:
  web: automated
---
# Penerimaan Notifikasi Disposal: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Approver (Disposal, Gedung A) | #6 | `approverDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSP_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposal` |
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Mengajukan Request Disposal formal.
- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Approver (Disposal, Gedung A) (Pre-setup #6, `approverDisposal_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERDSP_PASSWORD`). Approve atau Reject DSP-2026-0030 (Approver Disposal).
- Login akun aktor pertama (Approver (Disposal, Gedung A), Pre-setup #6) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): DSP-2026-0030 Pre-setup #22. Spec mengubah status DSP-2026-0030 per blok; fixture BE pemulih mengembalikannya. Rejection Reason dibaca dari `Fixture.fixedAssetNotification.rejectionReason` (data TC `Budget belum tersedia`) dan diketik pada aksi Reject.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu pengajuan, Approve, dan Reject pada DSP-2026-0030 (Pre-setup #22) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_APPROVERDSP_PASSWORD`, `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-251: Notifikasi disposal_waiting_approval diterima: Request Disposal formal dengan approval ON

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Approval Disposal ON; Request Disposal formal DSP-2026-0030, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Approver (Disposal) sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Asset Admin (Pre-setup #8, sesi API), ajukan Request Disposal formal (F-DISP-11) hingga DSP-2026-0030 berstatus Waiting for Approval tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Approver (Disposal) bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Waiting for your approval"` dan Body `"DSP-2026-0030 (1 Asset)"` (dari template `"[Transaction ID] (1 Asset)"`)
10. Verifikasi icon `time-line` dengan severity `primary` pada item
11. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
12. Klik `[Detail]` pada item tersebut
13. Verifikasi halaman tujuan `/fams/approvals/disposal/DSP-2026-0030` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-252: Notifikasi disposal_resolved varian Approved diterima: Approver Approve

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): DSP-2026-0030 Waiting for Approval
16. Ganti akun: logout, lalu login sebagai Asset Admin (Gedung A) (Pre-setup #8) dengan `Spectra.env.FA_ASSETADMIN_PASSWORD`, lalu buka Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Approver (Disposal, Pre-setup #6, sesi API), Approve DSP-2026-0030 hingga status Approved tersimpan
19. Klik Bell icon
20. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 17
21. Verifikasi item baru berada di posisi teratas Dropdown Panel
22. Verifikasi Title item baru bold
23. Verifikasi dot Unread tampil pada item baru
24. Verifikasi item menampilkan Title `"Your request has been approved"` dan Body `"DSP-2026-0030 (1 Asset)"` (dari template `"[Transaction ID] (1 Asset)"`)
25. Verifikasi icon `checkbox-circle-line` dengan severity `success` pada item
26. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
27. Klik judul item tersebut (bukan tombol)
28. Verifikasi halaman tujuan `/fams/transactions-disposal/DSP-2026-0030` terbuka
29. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 20

### TC-FA-NOTIF-253: Notifikasi disposal_resolved varian Rejected diterima: Approver Reject

30. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): DSP-2026-0030 Waiting for Approval
31. Muat ulang halaman Fixed Asset > Dashboard
32. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
33. Dari akun Approver (Disposal, Pre-setup #6, sesi API), Reject DSP-2026-0030 dengan alasan `Fixture.fixedAssetNotification.rejectionReason` hingga status Rejected tersimpan
34. Klik Bell icon
35. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 32
36. Verifikasi item baru berada di posisi teratas Dropdown Panel
37. Verifikasi Title item baru bold
38. Verifikasi dot Unread tampil pada item baru
39. Verifikasi item menampilkan Title `"Your request has been rejected"` dan Body `"DSP-2026-0030: "` diikuti `Fixture.fixedAssetNotification.rejectionReason` (dari template `"[Transaction ID]: [Rejection Reason]"`)
40. Verifikasi icon `close-circle-line` dengan severity `danger` pada item
41. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
42. Klik judul item tersebut (bukan tombol)
43. Verifikasi halaman tujuan `/fams/transactions-disposal/DSP-2026-0030` terbuka
44. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 35

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 30 (penyiapan kondisi data lewat fixture BE; pada langkah 1 diikuti muat ulang halaman Fixed Asset > Dashboard sebelum baseline); langkah 16 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 17, 32 (pencatatan baseline badge Bell icon (S-12)); langkah 31 (muat ulang halaman Fixed Asset > Dashboard sesudah pemulihan seed dan sebelum pencatatan baseline; juga menutup Dropdown Panel blok sebelumnya (S-09, S-14)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (44 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - Penerima TC-FA-NOTIF-252 dan 253 ditulis "Asset Admin (pemohon DSP-2026-0030)" tanpa nomor Pre-setup; spec memakai Asset Admin Pre-setup #8.
