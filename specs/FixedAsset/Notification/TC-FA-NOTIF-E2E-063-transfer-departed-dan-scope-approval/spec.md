---
id: TC-FA-NOTIF-E2E-063-transfer-departed-dan-scope-approval
title: "Penerimaan Notifikasi Transfer Departed dan Scope Approval Group Asal atau Group Tujuan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-250
  - TC-FA-NOTIF-404
  - TC-FA-NOTIF-405
coverage:
  web: automated
---
# Penerimaan Notifikasi Transfer Departed dan Scope Approval Group Asal atau Group Tujuan

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | Approver (Borrowing & Assignment dan Transfer, Gedung B) | #32 | `approverGedungB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERGDGB_PASSWORD` | `Fixture.fixedAssetNotification.approverGedungB` |
  | Approver (Transfer, Gedung A) | #5 | `approverTransfer_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERTRF_PASSWORD` | `Fixture.fixedAssetNotification.approverTransfer` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Men-submit Transfer Request dan mengonfirmasi Departure.
- Login akun aktor pertama (Asset Admin (Gedung A), Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): TRF-2026-0055 (1 aset Available di Gedung A, tujuan Gedung B; Pre-setup #21 dan #24); Approver (Transfer) Gedung A Pre-setup #5; Approver Gedung B Pre-setup #32 (Approver Borrowing & Assignment dan Transfer di Gedung B, tanpa peran di Gedung A). Scope approval Transfer (`origin_only` atau `destination_only`) diatur lewat fixture BE pada langkah penyiapan.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu submit dan konfirmasi Departure pada TRF-2026-0055 (Pre-setup #21 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Asersi absence atas notifikasi in-app memakai baseline badge Bell icon per penerima yang dicatat sebelum pemicu, anchor positif (penerima sah menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD`, `FA_APPROVERGDGB_PASSWORD`, `FA_APPROVERTRF_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-250: Notifikasi transfer_departed diterima: Departure dikonfirmasi, status In Transfer Process

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): TRF-2026-0055 Waiting for Departure
2. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Asset Admin (Pre-setup #8, sesi API), konfirmasi Departure TRF-2026-0055 (F-XFER-03 langkah 6; F-XFER-12) hingga status In Transfer Process tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Asset incoming transfer ready for arrival"` dan Body `"TRF-2026-0055 (1 Asset)"` (dari template `"[Transaction ID] (1 Asset)"`)
10. Verifikasi icon `time-line` dengan severity `primary` pada item
11. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
12. Klik `[Detail]` pada item tersebut
13. Verifikasi halaman tujuan `/fams/transactions-transfer/TRF-2026-0055` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-404: transfer_waiting_approval dengan scope approval hanya Group Asal diterima approver Group Asal saja

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Approval Transfer ON dengan scope approval `origin_only`; Approver (Transfer) Gedung A (Pre-setup #5) dan Approver Gedung B (Pre-setup #32) memegang peran masing-masing
16. Ganti akun: logout, lalu login sebagai Approver (Borrowing & Assignment dan Transfer, Gedung B) (Pre-setup #32) dengan `Spectra.env.FA_APPROVERGDGB_PASSWORD`, lalu buka Fixed Asset > Dashboard
17. Catat jumlah pada badge Bell icon Approver Gedung B sebagai baseline (0 bila badge tidak tampil)
18. Dari akun Asset Admin (Pre-setup #8, sesi API), submit Transfer Request TRF-2026-0055 aset Gedung A ke Gedung B hingga status Waiting for Approval tersimpan
19. Ganti akun: logout, lalu login sebagai Approver (Transfer, Gedung A) (Pre-setup #5) dengan `Spectra.env.FA_APPROVERTRF_PASSWORD`, lalu buka Fixed Asset > Dashboard
20. Klik Bell icon
21. Verifikasi item `"Waiting for your approval"` dengan Body `"TRF-2026-0055 (1 Asset)"` tampil pada Dropdown Panel Approver Group Asal
22. Ganti akun: logout, lalu login sebagai Approver (Borrowing & Assignment dan Transfer, Gedung B) (Pre-setup #32) dengan `Spectra.env.FA_APPROVERGDGB_PASSWORD`, lalu buka Fixed Asset > Dashboard
23. Tunggu 5 detik tanpa memuat ulang halaman
24. Klik Bell icon
25. Verifikasi Dropdown Panel Approver Gedung B tampil
26. Verifikasi item `"Waiting for your approval"` dengan Body `"TRF-2026-0055 (1 Asset)"` tidak tampil pada Dropdown Panel Approver Group Tujuan
27. Verifikasi badge Bell icon Approver Gedung B sama dengan baseline langkah 17 (tidak bertambah)

### TC-FA-NOTIF-405: transfer_waiting_approval dengan scope approval hanya Group Tujuan diterima approver Group Tujuan saja

28. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Approval Transfer ON dengan scope approval `destination_only`; Approver (Transfer) Gedung A (Pre-setup #5) dan Approver Gedung B (Pre-setup #32) memegang peran masing-masing
29. Ganti akun: logout, lalu login sebagai Approver (Transfer, Gedung A) (Pre-setup #5) dengan `Spectra.env.FA_APPROVERTRF_PASSWORD`, lalu buka Fixed Asset > Dashboard
30. Catat jumlah pada badge Bell icon Approver (Transfer) sebagai baseline (0 bila badge tidak tampil)
31. Dari akun Asset Admin (Pre-setup #8, sesi API), submit Transfer Request TRF-2026-0055 aset Gedung A ke Gedung B hingga status Waiting for Approval tersimpan
32. Ganti akun: logout, lalu login sebagai Approver (Borrowing & Assignment dan Transfer, Gedung B) (Pre-setup #32) dengan `Spectra.env.FA_APPROVERGDGB_PASSWORD`, lalu buka Fixed Asset > Dashboard
33. Klik Bell icon
34. Verifikasi item `"Waiting for your approval"` dengan Body `"TRF-2026-0055 (1 Asset)"` tampil pada Dropdown Panel Approver Group Tujuan
35. Ganti akun: logout, lalu login sebagai Approver (Transfer, Gedung A) (Pre-setup #5) dengan `Spectra.env.FA_APPROVERTRF_PASSWORD`, lalu buka Fixed Asset > Dashboard
36. Tunggu 5 detik tanpa memuat ulang halaman
37. Klik Bell icon
38. Verifikasi Dropdown Panel Approver (Transfer) tampil
39. Verifikasi item `"Waiting for your approval"` dengan Body `"TRF-2026-0055 (1 Asset)"` tidak tampil pada Dropdown Panel Approver Group Asal
40. Verifikasi badge Bell icon Approver (Transfer) sama dengan baseline langkah 30 (tidak bertambah)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 28 (penyiapan kondisi data lewat fixture BE); langkah 16, 19, 22, 29, 32, 35 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2, 17, 30 (pencatatan baseline badge Bell icon (S-12)); langkah 23, 36 (jendela 5 detik tanpa memuat ulang halaman (bagian 6 konvensi)).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (40 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Langkah 25 dan 38 (Dropdown Panel Approver tampil) adalah asersi tambahan di luar Expected TC sebagai anchor permukaan sebelum asersi absence (S-03; bagian 8b butir 2).
- Spec 063 memuat Departed dan scope approval atas TRF-2026-0055; keputusan approval ada di spec 062, dibedakan karena akun penerima dan kondisi data awal berbeda.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-250 menulis "penerima uji ditetapkan pemilik produk" dan login "Asset Admin (group tujuan)" tanpa nomor Pre-setup; spec memakai Asset Admin Pre-setup #8 dan penerimanya perlu dikonfirmasi pemilik produk.
  - TC-FA-NOTIF-404 dan 405 menyebut scope approval `origin_only` dan `destination_only` tanpa langkah UI untuk mengaturnya; spec mengaturnya lewat fixture BE yang disediakan tim FE/BE.
  - TC-FA-NOTIF-404 dan 405 tidak mencatat badge awal akun positif; baseline hanya untuk akun negatif (klausa "badge tidak bertambah").
