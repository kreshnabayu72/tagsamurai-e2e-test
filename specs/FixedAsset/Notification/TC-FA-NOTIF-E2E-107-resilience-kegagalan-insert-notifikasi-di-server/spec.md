---
id: TC-FA-NOTIF-E2E-107-resilience-kegagalan-insert-notifikasi-di-server
title: "Resilience Server: Kegagalan Insert Notifikasi pada Submit Borrow dan Job Terjadwal Borrow"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-360
  - TC-FA-NOTIF-361
  - TC-FA-NOTIF-418
coverage:
  web: automated
---

# Resilience Server: Kegagalan Insert Notifikasi pada Submit Borrow dan Job Terjadwal Borrow

## Prerequisites

- Mode: FE+BE (kegagalan insert dipaksa di sisi server lewat fixture BE; tidak dapat di-intercept dari browser).
- Akun aktor pertama: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Akun ini memegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A dan menjadi penerima notifikasi pada TC-FA-NOTIF-360 dan 361. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit pada langkah 23): Asset Admin PIC pembuat BRW-2026-0341 dan BRW-2026-0342 (Pre-setup #8), `assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`; juga sebagai pelaku Submit lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`) pada langkah 4. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17; N-01 sampai N-05 Unread, badge `5`; Body N-01 `BRW-2026-0341 (2 Assets)`), transaksi Borrow BRW-2026-0342 (1 aset Kamera DSLR AST-2024-0141) dan BRW-2026-0341 (2 aset Proyektor AST-2024-0150 dan Laptop - 2 AST-2024-0068) (Pre-setup #19 dan #24). Spec mengubah kedua transaksi (langkah 4, 12, 15, 20, 22, 26, 33); fixture BE pemulih seed notifikasi dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before`, pada langkah 12 dan 22, dan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan, S-13):
  - fixture BE kegagalan: pemaksaan kegagalan insert notifikasi pada aksi Submit Borrow Request, untuk satu transaksi saja pada job terjadwal (BRW-2026-0341), dan pemulihannya (butir "Fixture BE kegagalan" di `suite.md`);
  - kemampuan menjalankan job latar `F-FATX-07` (langkah almost_timeout dan langkah 3 auto-cancel) dan mengatur transaksi yang memenuhi syarat almost_timeout atau batas auto-cancel terlampaui (butir "Kemampuan menjalankan job latar" di `suite.md`);
  - fixture BE untuk membaca status transaksi.
- Asersi absence atas notifikasi in-app memakai baseline badge per penerima yang dicatat tepat sebelum pemicu, anchor positif, dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Env var `FA_TC_PASSWORD` dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk kedua akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Pengecualian S-06/S-12 butir A-16: notifikasi seed N-01 sampai N-07 (Pre-setup #17) serta transaksi BRW-2026-0341 dan BRW-2026-0342 (Pre-setup #19 sampai #24) dipakai literal tanpa suffix `{runId}-107` sebagai target Submit, pemicu job, dan auto-cancel, karena ID transaksi dibangkitkan sistem, ditulis literal di Expected TC, dan notifikasi seed hanya ada untuk akun Pre-setup. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (langkah 12 dan 22); suite berjalan serial (`parallel: false`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-360: Kegagalan insert notifikasi membatalkan aksi pemicu dan tidak meninggalkan notifikasi

1. Klik Bell icon
2. Catat nilai badge Bell icon sebagai baseline
3. Paksa kegagalan insert notifikasi di server pada aksi Submit Borrow Request lewat fixture BE
4. Dari akun Asset Admin (Pre-setup #8, sesi API), Submit Borrow Request BRW-2026-0342 hingga respons Submit diterima
5. Verifikasi aksi Submit gagal
6. Periksa status BRW-2026-0342 lewat fixture BE
7. Verifikasi transaksi BRW-2026-0342 tidak tercatat (tidak berstatus Waiting for Approval)
8. Pulihkan kegagalan insert notifikasi lewat fixture BE, lalu tunggu 5 detik tanpa memuat ulang halaman
9. Verifikasi Dropdown Panel tetap memuat item N-01 sampai N-05 (anchor positif)
10. Verifikasi tidak ada item dengan Body `BRW-2026-0342 (1 Asset)` pada Dropdown Panel
11. Verifikasi badge Bell icon sama dengan baseline langkah 2

### TC-FA-NOTIF-361: Kegagalan insert pada satu item job terjadwal tidak menghentikan job dan item dievaluasi ulang

12. Pulihkan seed notifikasi dan transaksi Pre-setup #17 sampai #24 lewat fixture BE pemulih, atur BRW-2026-0341 dan BRW-2026-0342 berstatus Waiting for Approval yang memenuhi syarat almost_timeout lewat fixture BE, lalu muat ulang halaman Fixed Asset > Dashboard
13. Klik Bell icon, lalu catat nilai badge Bell icon (baseline)
14. Paksa kegagalan insert notifikasi untuk BRW-2026-0341 saja lewat fixture BE
15. Jalankan job `F-FATX-07` hingga selesai
16. Verifikasi badge Bell icon bertambah 1 dari baseline langkah 13
17. Verifikasi Dropdown Panel memuat item `"Please finish this approval — expiring soon"` dengan Body memuat BRW-2026-0342
18. Tunggu 5 detik tanpa memuat ulang halaman
19. Verifikasi tidak ada item `"Please finish this approval — expiring soon"` dengan Body memuat BRW-2026-0341
20. Pulihkan kegagalan insert lewat fixture BE, lalu jalankan job `F-FATX-07` hingga selesai
21. Verifikasi Dropdown Panel memuat item `"Please finish this approval — expiring soon"` dengan Body memuat BRW-2026-0341

### TC-FA-NOTIF-418: Kegagalan insert saat auto-cancel di-rollback hanya untuk item itu dan dievaluasi ulang

22. Pulihkan seed notifikasi dan transaksi Pre-setup #17 sampai #24 lewat fixture BE pemulih, lalu atur BRW-2026-0341 dan BRW-2026-0342 berstatus Waiting for Approval dengan batas auto-cancel terlampaui lewat fixture BE
23. Logout, lalu login sebagai Asset Admin PIC pembuat (Pre-setup #8) dengan `Spectra.env.FA_ASSETADMIN_PASSWORD`, lalu buka Fixed Asset > Dashboard
24. Klik Bell icon, lalu catat nilai badge Bell icon (baseline)
25. Paksa kegagalan insert notifikasi `borrow_auto_canceled` untuk BRW-2026-0341 saja lewat fixture BE
26. Jalankan job `F-FATX-07` langkah 3 hingga selesai
27. Periksa status BRW-2026-0341 dan BRW-2026-0342 lewat fixture BE
28. Verifikasi BRW-2026-0342 berstatus Canceled
29. Verifikasi Dropdown Panel memuat item `"Your request was canceled automatically"` dengan Body memuat BRW-2026-0342
30. Verifikasi BRW-2026-0341 tetap berstatus Waiting for Approval
31. Tunggu 5 detik tanpa memuat ulang halaman
32. Verifikasi tidak ada item `"Your request was canceled automatically"` dengan Body memuat BRW-2026-0341
33. Pulihkan kegagalan insert lewat fixture BE, lalu jalankan job `F-FATX-07` langkah 3 hingga selesai
34. Periksa status BRW-2026-0341 lewat fixture BE
35. Verifikasi BRW-2026-0341 berstatus Canceled
36. Verifikasi Dropdown Panel memuat item `"Your request was canceled automatically"` dengan Body memuat BRW-2026-0341

## Notes

- Kegagalan sisi server (kelas b) tidak dapat di-intercept dari browser; pemicunya fixture BE, kemampuan teknisnya tercantum di Prerequisites, dan pemulihannya ditulis sebagai langkah (langkah 8, 20, dan 33) serta di hook `after`.
- Langkah penghubung (S-03): langkah 1 dan 13 serta 24 (membuka Dropdown Panel dan mencatat baseline, S-12); langkah 8, 18, dan 31 (jendela 5 detik, bagian 6 konvensi); langkah 12 dan 22 (pemulihan seed dan pengaturan state transaksi antar TC, S-09); langkah 23 (ganti akun eksplisit, S-07); langkah 27 dan 34 (membaca status transaksi lewat fixture BE); langkah 4 (pelaku Submit lewat sesi API).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 10 didahului langkah 9 (Dropdown Panel memuat item yang ada); langkah 19 didahului langkah 17 dan jendela langkah 18 (item BRW-2026-0342 dari job yang sama tampil); langkah 32 didahului langkah 29 dan jendela langkah 31 (notifikasi BRW-2026-0342 dari job yang sama tampil).
- Pada TC-FA-NOTIF-418 urutan TC "Klik Bell icon sebagai PIC pembuat" (langkah 4 TC) dibaca setelah langkah 2 dan 3 TC: Dropdown Panel dibuka pada langkah 24 dan diamati sesudah job pertama (langkah 29 dan 32) dan sesudah job kedua (langkah 36), supaya Expected a dan b masing-masing punya `Verifikasi` tepat setelah aksinya (R-03).
- Asersi tambahan di luar Expected TC (S-03): badge sama dengan baseline (langkah 11) dan badge bertambah 1 dari baseline (langkah 16) memakai baseline per penerima karena Dropdown Panel hanya memuat lima item terbaru (bagian 8b butir 10); status transaksi diperiksa lewat fixture BE (langkah 6, 7, 27 sampai 30, 34, 35) karena TC tidak menyebut cara pengamatan UI.
- Alasan melewati ambang sekitar 35 langkah: 36 langkah, semua blok satu kelas (kegagalan insert notifikasi di server, kelas b) dan tiap blok berdiri sendiri dengan seed dipulihkan; dua langkah di antaranya adalah jendela 5 detik sebelum asersi absence (langkah 18 dan 31).
- `P-2`: job latar `F-FATX-07` (kelas d; langkah 15, 20, 26, dan 33) hanya memicu kondisi yang diuji pada TC-FA-NOTIF-361 dan 418; objek asersinya adalah kegagalan insert notifikasi di server (kelas b), bukan perilaku job.
- Pembagian TC lintas spec: TC kegagalan insert untuk perpindahan status task audit (TC-FA-NOTIF-419) dan penilaian kuota License (TC-FA-NOTIF-448) ada di spec 122, karena datasetnya berbeda (task audit Pre-setup #23 dan kuota client Pre-setup #34, bukan transaksi Borrow) sehingga pemulihan state dan akun penerimanya berbeda.
- Temuan untuk QA:
  - TC-FA-NOTIF-360: "Notification Center penerima" tidak menyebut akun penerima atau tingkat Approver; spec memakai Total Control Pre-setup #1 yang memegang Transaction Role Approver (Borrowing & Assignment). Akun pelaku Submit tidak ditulis TC (Asset Admin Pre-setup #8 diambil dari TC-FA-NOTIF-418). "Aksi Submit gagal" dan "transaksi tidak tercatat" tidak menyebut bentuk respons atau status; spec mengasersi kegagalan respons dan status transaksi lewat fixture BE.
  - TC-FA-NOTIF-361: Expected tidak menulis penerima, judul, maupun Body notifikasi almost_timeout; spec memakai judul varian Approver `"Please finish this approval — expiring soon"` (dari TC-FA-NOTIF-153) dengan penerima Total Control Pre-setup #1 dan mengidentifikasi item lewat Body yang memuat nomor transaksi (Body persisnya tidak tertulis). Login TC adalah Total Control tanpa menyebut varian penerima.
  - TC-FA-NOTIF-418: status Canceled dan Waiting for Approval transaksi tidak punya cara pengamatan UI yang tertulis; diperiksa lewat fixture BE.
  - TC-FA-NOTIF-360, 361, dan 418: Post Condition kosong (`-`); tidak ada asersi tambahan.
