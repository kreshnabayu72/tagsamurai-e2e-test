---
id: TC-FA-NOTIF-E2E-065-disposal-reported-dan-penerima
title: "Penerimaan Notifikasi Disposal Reported: Flag Ringan Report Disposal dan Bukan Waiting for Approval"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-254
  - TC-FA-NOTIF-411
coverage:
  web: automated
---
# Penerimaan Notifikasi Disposal Reported: Flag Ringan Report Disposal dan Bukan Waiting for Approval

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | Approver (Disposal, Gedung A) | #6 | `approverDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSP_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposal` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Report Disposal aset AST-2024-0088 dari Asset Detail sebagai flag ringan (bukan request disposal).
- Login akun aktor pertama (Asset Admin (Gedung A), Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): aset Kendaraan Operasional AST-2024-0088 In Use di Gedung A (Pre-setup #22 dan #24). Spec mengubah aset menjadi ter-report; fixture BE pemulih mengembalikannya di awal tiap blok.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah Report Disposal pada aset AST-2024-0088 (Pre-setup #22 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi absence atas notifikasi in-app memakai baseline badge Bell icon per penerima yang dicatat sebelum pemicu, anchor positif (penerima sah menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_APPROVERDSP_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-254: Notifikasi disposal_reported diterima: Report Disposal sebagai flag ringan

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Aset Kendaraan Operasional (AST-2024-0088) In Use di Gedung A
2. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Asset Admin (Pre-setup #8, sesi API), Report Disposal aset AST-2024-0088 dari Asset Detail sebagai flag ringan hingga laporan tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Asset reported for disposal"` dan Body `"Kendaraan Operasional (AST-2024-0088) was reported for disposal."` (dari template `"[Asset Name] ([Asset ID]) was reported for disposal."`)
10. Verifikasi icon `information-line` dengan severity `warning` pada item
11. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
12. Klik judul item tersebut (bukan tombol)
13. Verifikasi halaman tujuan `/fams/transactions-disposal?tab=reported&highlight=AST-2024-0088` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-411: Report Disposal mengirim disposal_reported dan tidak mengirim disposal_waiting_approval

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Aset Kendaraan Operasional (AST-2024-0088) In Use di Gedung A
16. Ganti akun: logout, lalu login sebagai Approver (Disposal, Gedung A) (Pre-setup #6) dengan `Spectra.env.FA_APPROVERDSP_PASSWORD`, lalu buka Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Approver (Disposal) sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Asset Admin (Pre-setup #8, sesi API), Report Disposal aset AST-2024-0088 dari Asset Detail sebagai flag ringan hingga laporan tersimpan
19. Klik Bell icon
20. Verifikasi item `"Asset reported for disposal"` dengan Body `"Kendaraan Operasional (AST-2024-0088) was reported for disposal."` tampil pada Dropdown Panel Approver (Disposal)
21. Verifikasi badge Bell icon Approver (Disposal) bertambah tepat 1 dari baseline langkah 17
22. Tunggu 5 detik tanpa memuat ulang halaman
23. Verifikasi item `"Waiting for your approval"` tidak tampil pada Dropdown Panel Approver (Disposal)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15 (penyiapan kondisi data lewat fixture BE); langkah 16 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 17 (pencatatan baseline badge Bell icon (S-12)); langkah 22 (jendela 5 detik tanpa memuat ulang halaman (bagian 6 konvensi)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Blok TC-FA-NOTIF-411: asersi absence item `Waiting for your approval` didahului anchor positif (item `Asset reported for disposal` tampil) dan selisih badge tepat 1 dari baseline; TC tidak menyebut Body item yang dicek tidak ada.
- Spec 065 dan 116 sama-sama memakai AST-2024-0088; spec 065 menguji item dan tautan untuk Asset Admin dan Approver (Disposal), sedangkan spec 116 menguji cakupan penerima per role, sehingga aset dipulihkan fixture BE di awal tiap blok.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-254 menulis login "Asset Admin (Transaction Role Disposal, Gedung A)" tanpa nomor Pre-setup; spec memakai Asset Admin Pre-setup #8.
  - TC-FA-NOTIF-411 Expected (b) "Tidak ada item Waiting for your approval untuk Report Disposal itu" tidak menyebut Body item; spec mengasersi tidak ada item berjudul itu dan selisih badge tepat 1 (S-03).
