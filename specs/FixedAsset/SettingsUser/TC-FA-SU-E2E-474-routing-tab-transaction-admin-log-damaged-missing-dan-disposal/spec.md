---
id: TC-FA-SU-E2E-474-routing-tab-transaction-admin-log-damaged-missing-dan-disposal
title: "Routing Tab Transaction Admin Log: Damaged, Missing, dan Disposal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1186
  - TC-FA-SU-1187
coverage:
  web: automated
---

# Routing Tab Transaction Admin Log: Damaged, Missing, dan Disposal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua Budi Santoso (Pelapor admin) bertindak lewat sesi API; aktor Lina Marlina mengamati Tab Transaction Admin Log. Sesi pelaku kedua hanya memicu state tanpa asersi di dalamnya. Akun pelaku kedua disediakan tim FE: Budi Santoso `Spectra.env.FA_BUDI_PASSWORD` (nama usulan).
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Damaged dan Missing masing-masing berisi 4 baris sesuai Pre-setup #29 TC (Damaged: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`; Missing: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed aset khusus spec ini (disediakan tim FE lewat seed API di hook `before`, dihapus di hook `after`, tidak memengaruhi Pre-setup #29): `Tablet Samsung Tab - 6` berstatus Damaged (TC-FA-SU-1186); `Laptop Dell Latitude - 11` berstatus Damaged dan `Printer HP LaserJet - 4` berstatus Missing (TC-FA-SU-1187).
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): Report Missing dari tab Damaged (modul Damaged) dan Report Disposal dari tab Damaged dan dari tab Missing; dijalankan lewat sesi API, ditulis "... hingga ... tersimpan" (R-20). Entri log yang tercipta pada Tab Transaction Admin Log Budi Santoso bersifat permanen dan tidak dibersihkan; hitungan memakai baseline relatif (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1186: Routing: Report Missing dari tab Damaged tercatat di sub-tab Missing, bukan di sub-tab Damaged

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Missing
2. Catat jumlah baris sub-tab Missing sebagai baseline
3. Klik Sub-tab Damaged
4. Catat jumlah baris sub-tab Damaged sebagai baseline
5. Lakukan Report Missing atas aset `Tablet Samsung Tab - 6` sebagai Budi Santoso (Pelapor admin) dari tab Damaged pada modul Damaged lewat sesi API hingga laporan tersimpan
6. Tunggu aksi selesai, lalu tekan F5 pada halaman Detail
7. Klik Sub-tab Missing
8. Verifikasi baris teratas sub-tab Missing memiliki Activity `Reported missing` dan Name `Tablet Samsung Tab - 6`
9. Verifikasi Date baris itu adalah tanggal hari aksi
10. Verifikasi jumlah baris sub-tab Missing bertambah tepat satu dari baseline (dicatat sekali oleh modul Missing)
11. Klik Sub-tab Damaged
12. Verifikasi sub-tab Damaged tidak menampilkan baris untuk `Tablet Samsung Tab - 6`
13. Verifikasi jumlah baris sub-tab Damaged sama dengan baseline
14. Verifikasi keempat baris Pre-setup #29 sub-tab Damaged tidak berubah: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`

### TC-FA-SU-1187: Routing: Report Disposal dari Damaged dan dari Missing tercatat di sub-tab Disposal

15. Catat jumlah baris sub-tab Damaged sebagai baseline
16. Klik Sub-tab Missing
17. Catat jumlah baris sub-tab Missing sebagai baseline
18. Lakukan Report Disposal atas aset `Laptop Dell Latitude - 11` sebagai Budi Santoso dari tab Damaged lewat sesi API hingga laporan tersimpan
19. Lakukan Report Disposal atas aset `Printer HP LaserJet - 4` sebagai Budi Santoso dari tab Missing lewat sesi API hingga laporan tersimpan
20. Tunggu aksi selesai, lalu tekan F5 pada halaman Detail
21. Klik Sub-tab Disposal
22. Klik icon Search, ketik Search `Laptop Dell Latitude - 11`, tekan Enter
23. Verifikasi sub-tab Disposal menampilkan baris dengan Name `Laptop Dell Latitude - 11`
24. Ganti isi kotak search dengan `Printer HP LaserJet - 4`, tekan Enter
25. Verifikasi sub-tab Disposal menampilkan baris dengan Name `Printer HP LaserJet - 4`
26. Kosongkan isi kotak search, tekan Enter
27. Klik `←` pada kotak Search
28. Klik Sub-tab Damaged
29. Verifikasi jumlah baris sub-tab Damaged sama dengan baseline
30. Verifikasi sub-tab Damaged tidak menampilkan baris untuk `Laptop Dell Latitude - 11`
31. Klik Sub-tab Missing
32. Verifikasi jumlah baris sub-tab Missing sama dengan baseline
33. Verifikasi sub-tab Missing tidak menampilkan baris untuk `Printer HP LaserJet - 4`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pencatatan baseline jumlah baris (S-12), pemuatan ulang halaman Detail, pembukaan Search dan pengosongannya, serta perpindahan sub-tab.
- Pembagian TC lintas spec: struktur, Search, Sort, Filter, dan Download sub-tab Damaged ada di spec 468 sampai 470; sub-tab Missing di spec 471 sampai 473; aksi pemegang (TC-FA-SU-1188) ada di spec 475.
- Klausa absence ("tidak menampilkan baris") ditulis sebagai asersi jumlah terhadap baseline yang dicatat tepat sebelum pemicu (S-12); komparator pada surface yang sama adalah baris `Reported missing` pada TC-FA-SU-1186 dan baris Disposal pada TC-FA-SU-1187.
- Nilai Activity pada sub-tab Disposal dibaca dari modul Disposal dan tidak di-assert (sesuai Expected a TC-FA-SU-1187).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1186 dan 1187 menyebut aksi "Sebagai Budi Santoso ... lakukan Report Missing atau Report Disposal" lewat UI modul lain tanpa menyatakan akun, kredensial, atau jalur aksi; spec memicunya lewat sesi API (R-20) karena objek asersi adalah baris di Tab Transaction Admin Log aktor, bukan UI modul pemicu. Bila tim menghendaki titik masuk UI sebagai objek uji, spec perlu konteks browser kedua. (2) Seed khusus TC dinyatakan "tidak memengaruhi Pre-setup #29", tetapi aksinya menulis baris baru ke log Budi Santoso (sub-tab Missing dan Disposal) yang juga dibaca spec 468 sampai 473; spec ini mengasersi jumlah lewat baseline, dan spec pembaca Pre-setup #29 mengasersi baris seed lewat nilainya. Bila suite berjalan paralel, jumlah absolut dapat bergeser; mohon QA menetapkan pengguna Pelapor khusus spec atau urutan jalan. (3) Nama aset seed memakai literal TC (`Laptop Dell Latitude - 11`, `Printer HP LaserJet - 4`, `Tablet Samsung Tab - 6`); increment dibangkitkan sistem sehingga seed harus menjamin nama itu. (4) TC-FA-SU-1187 menyebut aksi atas dua aset tanpa urutan; spec menjalankan aset Damaged lalu aset Missing.
