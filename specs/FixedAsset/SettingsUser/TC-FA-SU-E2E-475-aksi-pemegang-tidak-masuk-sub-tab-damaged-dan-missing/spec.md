---
id: TC-FA-SU-E2E-475-aksi-pemegang-tidak-masuk-sub-tab-damaged-dan-missing
title: "Aksi dari My Asset Tidak Masuk Tab Transaction Admin Log Sub-tab Damaged dan Missing"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1188
coverage:
  web: automated
---

# Aksi dari My Asset Tidak Masuk Tab Transaction Admin Log Sub-tab Damaged dan Missing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua Rina Wijaya (pemegang aset) dan Budi Santoso (Pelapor admin) bertindak lewat sesi API; aktor Lina Marlina mengamati Tab Transaction Admin Log dan Tab User Log Budi Santoso. Sesi pelaku kedua hanya memicu state tanpa asersi di dalamnya. Akun pelaku kedua disediakan tim FE: Rina Wijaya `Spectra.env.FA_RINA_PASSWORD` dan Budi Santoso `Spectra.env.FA_BUDI_PASSWORD` (nama usulan).
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Damaged dan Missing masing-masing berisi 4 baris sesuai Pre-setup #29 TC (Damaged: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`; Missing: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed aset khusus spec ini (disediakan tim FE lewat seed API di hook `before`, dihapus di hook `after`, tidak memengaruhi Pre-setup #29): aset `Monitor LG 24 - 6` dengan laporan Missing aktif atas nama pemegang Rina Wijaya; aset `Monitor LG 24 - 8` dipegang Budi Santoso (Budi Santoso berhak Update Group aset, Pelapor admin) tanpa laporan Damaged atau Missing aktif.
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): Cancel Report dari My Asset oleh pemegang serta Report Missing dan Cancel Report dari My Asset oleh Pelapor admin, dijalankan lewat sesi API dan ditulis "... hingga ... tersimpan" (R-20). Entri log yang dibuat spec lain pada Tab Transaction Admin Log Budi Santoso bersifat permanen dan tidak dibersihkan; hitungan memakai baseline relatif (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Missing
2. Catat jumlah baris sub-tab Missing sebagai baseline
3. Klik Sub-tab Damaged
4. Catat jumlah baris sub-tab Damaged sebagai baseline
5. Lakukan Cancel Report atas laporan `Monitor LG 24 - 6` sebagai Rina Wijaya (pemegang aset) dari My Asset lewat sesi API hingga pembatalan tersimpan
6. Lakukan Report Missing atas `Monitor LG 24 - 8` sebagai Budi Santoso (Pelapor admin, pemegang aset) dari My Asset lewat sesi API hingga laporan tersimpan
7. Lakukan Cancel Report atas laporan `Monitor LG 24 - 8` sebagai Budi Santoso dari My Asset lewat sesi API hingga pembatalan tersimpan
8. Tunggu aksi selesai, lalu tekan F5 pada halaman Detail
9. Klik Sub-tab Missing
10. Verifikasi keempat baris Pre-setup #29 sub-tab Missing tampil: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`
11. Verifikasi jumlah baris sub-tab Missing sama dengan baseline
12. Verifikasi sub-tab Missing tidak menambah baris untuk `Monitor LG 24 - 6` (aksi pemegang dari My Asset tidak masuk Transaction Admin Log)
13. Verifikasi sub-tab Missing tidak menambah baris untuk `Monitor LG 24 - 8` (Report Missing dan Cancel Report dari My Asset tidak masuk Transaction Admin Log, juga bila pelakunya Pelapor admin)
14. Klik Sub-tab Damaged
15. Verifikasi keempat baris Pre-setup #29 sub-tab Damaged tampil: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`
16. Verifikasi jumlah baris sub-tab Damaged sama dengan baseline
17. Verifikasi sub-tab Damaged tidak menambah baris untuk `Monitor LG 24 - 6`
18. Verifikasi sub-tab Damaged tidak menambah baris untuk `Monitor LG 24 - 8`
19. Klik Tab User Log
20. Verifikasi riwayat aksi Budi Santoso atas `Monitor LG 24 - 8` tampil di Tab User Log (nilai Activity tidak di-assert)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pencatatan baseline jumlah baris (S-12), pemicuan state lewat sesi API (R-20), pemuatan ulang halaman Detail, perpindahan sub-tab, dan pembukaan Tab User Log.
- Pembagian TC lintas spec: routing Report Missing dan Report Disposal (TC-FA-SU-1186 dan 1187) ada di spec 474; struktur, Search, Sort, Filter, dan Download sub-tab Damaged dan Missing ada di spec 468 sampai 473.
- Klausa absence ("tidak menambah baris") ditulis sebagai asersi jumlah terhadap baseline yang dicatat tepat sebelum pemicu (S-12), didahului `Verifikasi` keempat baris Pre-setup #29 pada sub-tab yang sama sebagai anchor positif (8b.2).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1188 menyebut tindakan Rina Wijaya (pemegang aset) tanpa menyatakan akun, kredensial, atau jalur aksi; spec memicunya lewat sesi API (R-20) dengan akun kedua disediakan tim FE. (2) Seed khusus TC dinyatakan "tidak memengaruhi Pre-setup #29", tetapi spec 474 menulis baris baru ke log Budi Santoso yang juga dibaca spec ini; asersi jumlah memakai baseline sehingga tetap berlaku untuk urutan jalan serial, dan hasil absolut dapat bergeser bila suite paralel. (3) TC-FA-SU-1188 tidak menyebut baris pembanding positif pada sub-tab Missing dan Damaged; anchor memakai keempat baris Pre-setup #29. (4) TC-FA-SU-1188 butir d tidak menyebut nilai Activity di Tab User Log (rujukan `my-asset.md` §8); spec mengasersi hanya kehadiran riwayat aset `Monitor LG 24 - 8`. (5) Seed `Monitor LG 24 - 8` ditambahkan atas Data Uji TC-FA-SU-1188; akun Budi Santoso sebagai pelaku kedua disediakan tim FE.
