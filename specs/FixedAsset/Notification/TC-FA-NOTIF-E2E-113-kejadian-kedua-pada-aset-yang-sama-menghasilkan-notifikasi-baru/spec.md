---
id: TC-FA-NOTIF-E2E-113-kejadian-kedua-pada-aset-yang-sama-menghasilkan-notifikasi-baru
title: "Kejadian Kedua pada Aset yang Sama Menghasilkan Notifikasi Baru: Damaged Repaired, Missing Found, dan Disposal Reported"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-377
  - TC-FA-NOTIF-412
  - TC-FA-NOTIF-413
coverage:
  web: automated
---

# Kejadian Kedua pada Aset yang Sama Menghasilkan Notifikasi Baru: Damaged Repaired, Missing Found, dan Disposal Reported

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Akun aktor: Asset Admin Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_ASSETADMIN_PASSWORD`, fixture `Fixture.fixedAssetNotification.assetAdmin`; nama env usulan, belum terdaftar). TC-FA-NOTIF-377 menulis "Asset Admin (PIC aset Kamera DSLR)", TC-FA-NOTIF-412 "Asset Admin (PIC aset Laptop - 1)", dan TC-FA-NOTIF-413 "Asset Admin (Transaction Role Disposal, Gedung A)"; ketiganya dilayani akun Pre-setup #8 dengan peran PIC dan Transaction Role Disposal yang diatur fixture BE (lihat Temuan untuk QA).
- Login akun aktor pertama (Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu event (Damaged, Mark as Repaired, Missing, Mark as Found, Cancel Disposal Report, Report Disposal) memakai sesi API aktor Asset Admin lewat fixture BE pemicu event; Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: aset Kamera DSLR AST-2024-0141, Laptop - 1 AST-2024-0067, dan Kendaraan Operasional AST-2024-0088 (Pre-setup #24). Precondition tiap TC (aset pernah Mark as Repaired, Mark as Found, atau Report Disposal dan notifikasi pertamanya Read) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok. Asersi "notifikasi baru" memakai baseline jumlah item yang dicatat tepat sebelum pemicu (bagian 8b butir 10). Kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah item notifikasi per penerima dan per Title/Body; baseline dan pembacaan sesudah pemicu memakai kemampuan baca yang sama, bukan hitungan item Dropdown Panel.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (AST-2024-0141, AST-2024-0067, AST-2024-0088) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-377: damaged_repaired kejadian kedua pada aset yang sama menghasilkan notifikasi baru

1. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon dan, lewat fixture BE, jumlah item `Asset has been repaired` untuk AST-2024-0141 milik Asset Admin (baseline)
2. Lewat sesi API Asset Admin (Pre-setup #8), tandai AST-2024-0141 Damaged kembali hingga tersimpan
3. Lewat sesi API Asset Admin, klik Mark as Repaired untuk kedua kalinya pada AST-2024-0141 hingga tersimpan
4. Klik Bell icon
5. Verifikasi (kemampuan baca BE) jumlah item `Asset has been repaired` untuk AST-2024-0141 milik Asset Admin bertambah tepat 1 dari baseline langkah 1
6. Verifikasi notifikasi baru `Asset has been repaired` untuk AST-2024-0141 tampil di posisi teratas
7. Verifikasi notifikasi baru `Asset has been repaired` untuk AST-2024-0141 berstatus Unread
8. Verifikasi notifikasi pertama `Asset has been repaired` untuk AST-2024-0141 tetap Read

### TC-FA-NOTIF-412: missing_found kejadian kedua pada aset yang sama menghasilkan notifikasi baru

9. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon dan, lewat fixture BE, jumlah item `Asset has been found` untuk Body `Laptop - 1 (AST-2024-0067)` milik Asset Admin (baseline)
10. Lewat sesi API Asset Admin (Pre-setup #8), tandai AST-2024-0067 Missing kembali hingga tersimpan
11. Lewat sesi API Asset Admin, klik Mark as Found untuk kedua kalinya pada AST-2024-0067 hingga tersimpan
12. Klik Bell icon
13. Verifikasi (kemampuan baca BE) jumlah item `Asset has been found` untuk Body `Laptop - 1 (AST-2024-0067)` milik Asset Admin bertambah tepat 1 dari baseline langkah 9
14. Verifikasi notifikasi baru `Asset has been found` untuk Body `Laptop - 1 (AST-2024-0067)` tampil di posisi teratas
15. Verifikasi notifikasi baru `Asset has been found` untuk Body `Laptop - 1 (AST-2024-0067)` berstatus Unread
16. Verifikasi notifikasi pertama `Asset has been found` untuk Body `Laptop - 1 (AST-2024-0067)` tetap Read

### TC-FA-NOTIF-413: disposal_reported kejadian kedua setelah Cancel Disposal Report menghasilkan notifikasi baru

17. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon dan, lewat fixture BE, jumlah item `Asset reported for disposal` untuk Body `Kendaraan Operasional (AST-2024-0088) was reported for disposal.` milik Asset Admin (baseline)
18. Lewat sesi API Asset Admin (Pre-setup #8), Cancel Disposal Report aset AST-2024-0088 hingga pembatalan tersimpan
19. Lewat sesi API Asset Admin, Report Disposal aset AST-2024-0088 dari Asset Detail untuk kedua kalinya hingga tersimpan
20. Klik Bell icon
21. Verifikasi (kemampuan baca BE) jumlah item `Asset reported for disposal` untuk Body `Kendaraan Operasional (AST-2024-0088) was reported for disposal.` milik Asset Admin bertambah tepat 1 dari baseline langkah 17
22. Verifikasi notifikasi baru `Asset reported for disposal` untuk Body `Kendaraan Operasional (AST-2024-0088) was reported for disposal.` tampil di posisi teratas
23. Verifikasi notifikasi baru `Asset reported for disposal` untuk Body `Kendaraan Operasional (AST-2024-0088) was reported for disposal.` berstatus Unread
24. Verifikasi notifikasi pertama `Asset reported for disposal` untuk Body `Kendaraan Operasional (AST-2024-0088) was reported for disposal.` tetap Read

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 2, 3, 9, 10, 11, 17, 18 dan 19. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, pencatatan baseline (nilai badge lewat UI, jumlah item lewat kemampuan baca BE; S-12), dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu.
- Asersi tambahan di luar Expected TC (S-03): langkah 6, 14, dan 22 (posisi teratas) membedakan notifikasi baru dari notifikasi pertama berjudul sama; selisih jumlah item terhadap baseline (langkah 5, 13, 21), dibaca lewat kemampuan baca BE yang sama dengan baseline, adalah bukti "notifikasi baru" (bagian 8b butir 10), bukan hitungan item Dropdown Panel yang hanya memuat lima item terbaru.
- Pembagian per TC: TC-FA-NOTIF-377 (langkah 1 sampai 8), TC-FA-NOTIF-412 (langkah 9 sampai 16), TC-FA-NOTIF-413 (langkah 17 sampai 24).
- Pembagian per TC lintas spec: TC-FA-NOTIF-169, 170, 171, 359, dan 362 ada di spec 042.
- Temuan untuk QA:
  - TC-FA-NOTIF-377, 412, dan 413 menulis Asset Admin dengan keterangan peran berbeda tanpa nomor Pre-setup, dan tabel Pre-setup TC tidak memuat Asset Admin PIC aset tertentu; spec memakai Pre-setup #8 dan menandai peran PIC dan Transaction Role Disposal sebagai penyetelan fixture BE (disediakan tim FE/BE).
  - TC-FA-NOTIF-377 dan 412 menulis "Tandai ... kembali lalu klik Mark as Repaired/Found" tanpa menyebut pelaku dan jalur aksi; spec memakai sesi API Asset Admin. TC-FA-NOTIF-413 menulis Report Disposal "dari Asset Detail"; spec menjalankannya lewat sesi API karena hanya memicu keadaan.
  - TC-FA-NOTIF-377 tidak menyebut Body notifikasi `Asset has been repaired`; spec mengidentifikasi item lewat judul, aset AST-2024-0141, dan urutan (item baru di atas).
