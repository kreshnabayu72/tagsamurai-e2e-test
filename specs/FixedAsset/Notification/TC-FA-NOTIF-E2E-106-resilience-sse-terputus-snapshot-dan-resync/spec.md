---
id: TC-FA-NOTIF-E2E-106-resilience-sse-terputus-snapshot-dan-resync
title: "Resilience SSE: Koneksi Terputus, Sinkron Snapshot, dan Pengambilan Ulang List dengan Kontrol Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-177
  - TC-FA-NOTIF-178
  - TC-FA-NOTIF-179
coverage:
  web: automated
---

# Resilience SSE: Koneksi Terputus, Sinkron Snapshot, dan Pengambilan Ulang List dengan Kontrol Aktif

## Prerequisites

- Mode: FE+BE (jaringan browser diputus dan disambung kembali di atas backend nyata; asersi memuat state server: badge dan list sesuai snapshot server).
- Akun aktor: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17; N-01 sampai N-05 Unread, badge `5`; N-05 `Your Total Control access was removed` cocok dengan Search `access`) untuk TC-FA-NOTIF-178 dan 179, dan varian N-01 sampai N-37 (Pre-setup #17 dan #18) untuk TC-FA-NOTIF-177. Varian ditukar oleh fixture BE penukar (butir "Fixture BE penukar varian seed #18" di `suite.md`) pada langkah 19; fixture BE pemulih seed (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before`, pada langkah 9 dan 28, dan di hook `after`.
- Kemampuan teknis: emulasi jaringan browser terputus dan tersambung kembali yang memutus lalu menyambung kembali stream SSE; fixture BE pemicu event yang membuat satu notifikasi baru bagi Total Control saat jaringan browser terputus (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`). Disediakan tim FE/BE tanpa endpoint karangan (S-13). Kemampuan baca BE atas jumlah seluruh item notifikasi akun aktor (sumber baca yang sama untuk jumlah awal dan pembacaan sesudah pemicu) dipakai langkah 20 dan 27.
- Jaringan browser dipulihkan segera setelah pemicu selesai (langkah 4, 14, dan 22) dan di hook `after`.
- Langkah "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 5) menunggu nyata selama lima detik sebagai jendela sinkron snapshot SSE; lima detik adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-178: SSE tersambung kembali mengambil snapshot dan menyinkronkan badge dan panel

1. Catat nilai badge Bell icon (baseline, `5`)
2. Putuskan jaringan browser (emulasi offline) sehingga koneksi SSE terputus
3. Picu satu notifikasi baru untuk akun ini lewat fixture BE pemicu event hingga tersimpan
4. Sambungkan kembali jaringan browser
5. Tunggu 5 detik tanpa memuat ulang halaman
6. Verifikasi badge Bell icon tersinkron dengan snapshot server (bertambah 1 dari baseline langkah 1 menjadi `6`)
7. Klik Bell icon
8. Verifikasi Dropdown Panel tersinkron dengan snapshot server (notifikasi baru dari langkah 3 tampil di posisi teratas)

### TC-FA-NOTIF-179: Notification Center setelah SSE putus mengambil ulang list dari awal dengan kontrol aktif

9. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
10. Klik Bell icon lalu klik `[Show All]` untuk membuka Notification Center
11. Klik Tab `Unread`
12. Pilih Sort `Oldest`
13. Ketik Search `access`, tekan Enter
14. Putuskan jaringan browser (emulasi offline) sehingga koneksi SSE terputus, lalu sambungkan kembali jaringan browser sehingga SSE tersambung kembali
15. Verifikasi Tab `Unread` tetap aktif
16. Verifikasi Sort `Oldest` tetap aktif
17. Verifikasi Search `access` tetap aktif (kotak Search berisi `access`)
18. Verifikasi list diambil ulang dari awal (list tampil dari item paling atas)

### TC-FA-NOTIF-177: Reload halaman mengambil snapshot unread count dan 5 notifikasi terbaru tanpa replay historis

19. Tukar seed notifikasi ke varian N-01 sampai N-37 (Pre-setup #17 dan #18) lewat fixture BE penukar, lalu muat ulang halaman Fixed Asset > Dashboard
20. Catat nilai badge Bell icon (baseline jumlah Unread) dan, lewat kemampuan baca BE, jumlah seluruh item notifikasi milik akun aktor sebagai jumlah awal
21. Putuskan jaringan browser (emulasi offline) sehingga koneksi SSE terputus
22. Picu satu notifikasi baru untuk akun ini lewat fixture BE pemicu event hingga tersimpan, lalu sambungkan kembali jaringan browser
23. Muat ulang halaman
24. Klik Bell icon
25. Verifikasi badge Bell icon menampilkan jumlah Unread terkini (bertambah 1 dari baseline langkah 20)
26. Verifikasi Dropdown Panel menampilkan tepat 5 notifikasi terbaru dari snapshot
27. Verifikasi (kemampuan baca BE) jumlah seluruh item notifikasi milik akun aktor sama dengan jumlah awal langkah 20 + 1 (notifikasi dari langkah 22 tercatat tepat sekali; event yang terlewat tidak diputar ulang satu per satu)
28. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih

## Notes

- Urutan TC pada spec: TC-FA-NOTIF-178, 179, lalu 177, karena TC-FA-NOTIF-177 memakai varian seed N-01 sampai N-37 sedangkan dua TC lainnya memakai N-01 sampai N-07 (S-10: varian seed ditukar satu kali).
- Langkah penghubung (S-03): langkah 1 dan 20 (baseline badge dan jumlah awal seluruh item lewat kemampuan baca BE, S-12); langkah 3 dan 22 (pemicu notifikasi baru saat offline lewat fixture BE; langkah 22 menyambung kembali jaringan sebelum muat ulang karena muat ulang membutuhkan jaringan); langkah 5 (jendela 5 detik agar SSE tersambung kembali, tanpa `Verifikasi`); langkah 9 dan 28 (pemulihan seed antar TC, S-09); langkah 10 (jalur Notification Center lewat Bell icon dan `[Show All]`, karena TC tidak menyebut jalur lain); langkah 7 dan 24 (membuka Dropdown Panel).
- Asersi absence: tidak ada asersi absence; langkah 27 adalah asersi jumlah ("tepat sekali") yang dibaca lewat kemampuan baca BE terhadap jumlah awal langkah 20, bukan hitungan Dropdown Panel yang memuat maksimal 5 item (bagian 8b butir 10).
- Temuan untuk QA:
  - TC-FA-NOTIF-178: langkah TC tidak menyebut perubahan state saat jaringan terputus, sehingga "tersinkron dengan snapshot" tidak teramati; spec menambah satu notifikasi baru saat offline (langkah 3) sebagai pembentuk state dan mengasersi badge `6` dan item teratas.
  - TC-FA-NOTIF-177: "tidak memutar ulang event yang terlewat satu per satu" tidak punya cara pengamatan yang tertulis; spec mengasersi notifikasi saat offline tercatat tepat sekali (selisih jumlah awal + 1 lewat kemampuan baca BE, langkah 27). Langkah TC menyebut memutuskan SSE lalu memuat ulang halaman; muat ulang membutuhkan jaringan sehingga spec menyambung kembali jaringan sebelum muat ulang. Jumlah Unread awal varian N-01 sampai N-37 tidak ditulis TC; baseline dibaca dari badge.
  - TC-FA-NOTIF-179: "diambil ulang dari awal" tidak menyebut cara pengamatan; spec mengasersi list tampil dari item paling atas. Item konkret hasil Search `access` Sort `Oldest` pada Tab Unread tidak ditulis TC.
  - TC-FA-NOTIF-177, 178, dan 179: Post Condition kosong (`-`); tidak ada asersi tambahan.
