---
id: TC-FA-NOTIF-E2E-065-disposal-ready-to-execute-dan-report-disposal-tanpa-waiting-approval
title: "Penerimaan Notifikasi Disposal Ready to Execute dan Report Disposal dari Damaged yang Tidak Mengirim Waiting for Approval"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-254
  - TC-FA-NOTIF-411
coverage:
  web: automated
---
# Penerimaan Notifikasi Disposal Ready to Execute dan Report Disposal dari Damaged yang Tidak Mengirim Waiting for Approval

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | Approver (Disposal, Gedung A) | #6 | `approverDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSP_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposal` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Approver (Disposal, Gedung A) (Pre-setup #6, `approverDisposal_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERDSP_PASSWORD`). Approve DSP-2026-0030 sehingga baris menjadi Waiting for Execution (blok TC-FA-NOTIF-254).
- Pelaku pemicu lewat sesi API aktor: Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Report Disposal aset AST-2024-0088 dari tab Damaged dengan Reason, lalu Submit dialog (blok TC-FA-NOTIF-411). Aksi ini hanya membuat Disposal Report di tab Reported, bukan DSP.
- Login akun aktor pertama (Asset Admin (Gedung A), Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): DSP-2026-0030 Waiting for Approval di Gedung A dengan pemohon Asset Admin Pre-setup #8 (Pre-setup #19 sampai #24; blok TC-FA-NOTIF-254) dan aset Kendaraan Operasional AST-2024-0088 Condition Damaged dengan record Damaged di Gedung A (Pre-setup #19 sampai #24; blok TC-FA-NOTIF-411, Approval Disposal ON). Spec mengubah status DSP-2026-0030 dan membuat Disposal Report atas AST-2024-0088; fixture BE pemulih mengembalikannya di awal tiap blok.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah Approve DSP-2026-0030 dan Report Disposal aset AST-2024-0088 (Pre-setup #19 sampai #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi absence atas notifikasi in-app memakai baseline badge Bell icon per penerima yang dicatat sebelum pemicu dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_APPROVERDSP_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-254: Notifikasi disposal_ready_to_execute diterima: baris menjadi Waiting for Execution setelah Approve

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): DSP-2026-0030 Waiting for Approval di Gedung A dengan pemohon Asset Admin Pre-setup #8
2. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Approver (Disposal, Pre-setup #6, sesi API), Approve DSP-2026-0030 hingga baris berstatus Waiting for Execution tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Disposal is ready to execute"` dan Body `"DSP-2026-0030 (1 Asset) is ready to execute"` (dari template `"[Transaction ID] (1 Asset) is ready to execute"`)
10. Verifikasi icon `time-line` dengan severity `primary` pada item
11. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
12. Klik `[Detail]` pada item tersebut
13. Verifikasi halaman tujuan `/fams/transactions-disposal/DSP-2026-0030` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-411: Report Disposal dari Damaged hanya membuat Disposal Report dan mengirim disposal_reported, bukan disposal_waiting_approval

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Approval Disposal ON; aset Kendaraan Operasional (AST-2024-0088) Condition Damaged dengan record Damaged di Gedung A
16. Ganti akun: logout, lalu login sebagai Approver (Disposal, Gedung A) (Pre-setup #6) dengan `Spectra.env.FA_APPROVERDSP_PASSWORD`, lalu buka Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Approver (Disposal) sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Asset Admin (Pre-setup #8, sesi API), Report Disposal aset AST-2024-0088 dari tab Damaged dengan Reason, lalu Submit dialog hingga Disposal Report tersimpan
19. Klik Bell icon
20. Tunggu 5 detik tanpa memuat ulang halaman
21. Verifikasi item `"Waiting for your approval"` tidak tampil pada Dropdown Panel Approver (Disposal)
22. Verifikasi item `"Asset reported for disposal"` tidak tampil pada Dropdown Panel Approver (Disposal)
23. Verifikasi badge Bell icon Approver (Disposal) tidak bertambah dari baseline langkah 17
24. Buka Fixed Asset > Transactions Disposal
25. Verifikasi tidak ada DSP baru yang terbentuk dari Report AST-2024-0088 pada Transactions Disposal (Report bukan transaksi)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15 (penyiapan kondisi data lewat fixture BE); langkah 16 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 17 (pencatatan baseline badge Bell icon (S-12)); langkah 20 (jendela 5 detik tanpa memuat ulang halaman (bagian 6 konvensi)); langkah 24 (navigasi ke Transactions Disposal untuk asersi Expected b).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Blok TC-FA-NOTIF-411 bersifat Negative: Approver Disposal bukan Aktor Disposal sehingga bukan penerima `disposal_reported`, dan belum ada DSP sehingga tidak ada `disposal_waiting_approval`. Event `disposal_reported` yang dikirim ke Aktor Disposal diuji pada TC-FA-NOTIF-549 sampai 551 (tidak dipetakan ke spec ini).
- Spec 065 dan 116 sama-sama memakai data Pre-setup bersama (AST-2024-0088 dan DSP-2026-0030), sehingga fixture BE memulihkannya di awal tiap blok.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-254 menulis login "Asset Admin (Transaction Role Disposal, Gedung A; pemohon DSP-2026-0030)" tanpa nomor Pre-setup; spec memakai Asset Admin Pre-setup #8.
  - TC-FA-NOTIF-411 Expected (a) tidak menyebut Body item `"Waiting for your approval"`; spec mengasersi tidak ada item berjudul itu dan item `"Asset reported for disposal"`, ditambah badge tidak bertambah dari baseline (S-03). Expected (b) "Tidak ada DSP baru terbentuk" tidak menyebut halaman asersinya; spec memakai Transactions Disposal (pilihan spec, S-03).
  - TC-FA-NOTIF-411 menyatakan Approver Disposal bukan Aktor Disposal; asersi absence ini bergantung pada akun Pre-setup #6 yang tidak memegang peran Aktor Disposal pada data Pre-setup (perlu dicek QA).
