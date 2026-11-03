---
id: TC-FA-SU-E2E-097-bulk-edit-home-group-screening-popup-bulk-sukses-serentak-sebagian-skip-dan-seluruh
title: "Bulk Edit Home Group: Screening Popup Bulk, Sukses Serentak, Sebagian Skip, dan Seluruh Skip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-306
  - TC-FA-SU-307
  - TC-FA-SU-308
  - TC-FA-SU-309
coverage:
  web: automated
---

# Bulk Edit Home Group: Screening Popup Bulk, Sukses Serentak, Sebagian Skip, dan Seluruh Skip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21). Pengguna: Gita Permata, Budi Santoso, Hana Kusuma, Kartika Sari (Pending Activation), Eka Wulandari dan Fajar Nugroho (keduanya Home Group Branch Surabaya). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Hana Kusuma dan Kartika Sari pada langkah 20 dan 32 serta di hook `after`. Efek pada Pre-setup: Home Group, Last Updated, dan Modified By Hana Kusuma dan Kartika Sari berubah dan entri log permanen bertambah; Eka Wulandari dan Fajar Nugroho tidak diubah.

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab Changelog Kartika Sari, Tab Changelog Eka Wulandari, Tab Changelog Fajar Nugroho, Tab System Log aktor, dan Activity Log sebagai baseline

### TC-FA-SU-306: Screening popup Select Home Group varian bulk

2. Centang Gita Permata, Budi Santoso, dan Hana Kusuma
3. Klik Bulk Action > `Edit Home Group`
4. Verifikasi judul `Select Home Group — 3 users` (jumlah baris terpilih) tampil
5. Verifikasi popup tidak memuat daftar nama pengguna
6. Verifikasi pohon dimulai tanpa node terpilih
7. Verifikasi `[Select]` Enabled
8. Klik `[Cancel]` lalu klik Unselect All
9. Centang Gita Permata saja lalu klik Bulk Action > `Edit Home Group`
10. Verifikasi judul `Select Home Group` (varian singular) tampil
11. Klik `[Cancel]` lalu klik Unselect All

### TC-FA-SU-307: Bulk Edit Home Group seluruh baris berubah

12. Centang Hana Kusuma dan Kartika Sari
13. Klik Bulk Action > `Edit Home Group`
14. Klik node Branch Surabaya lalu klik `[Select]`
15. Verifikasi toast "Success, home group has been updated." tampil
16. Verifikasi Home Group Hana Kusuma dan Kartika Sari berubah menjadi Branch Surabaya
17. Verifikasi seleksi di-reset
18. Buka Tab Changelog Hana Kusuma dan Tab Changelog Kartika Sari
19. Verifikasi satu entri `Edit Home Group` per pengguna yang berubah tercatat
20. Pulihkan Home Group Hana Kusuma dan Kartika Sari ke kondisi Pre-setup lewat seed API

### TC-FA-SU-308: Bulk sebagian sudah di grup tujuan

21. Kembali ke User List lalu centang Eka Wulandari (Home Group Branch Surabaya) dan Hana Kusuma
22. Klik Bulk Action > `Edit Home Group`
23. Klik node Branch Surabaya lalu klik `[Select]`
24. Verifikasi toast "Success, home group has been updated. Some items were skipped." tampil
25. Verifikasi Home Group Hana Kusuma berubah menjadi Branch Surabaya

### TC-FA-SU-309: Bulk seluruh baris sudah di grup tujuan

26. Centang Eka Wulandari dan Fajar Nugroho (keduanya Home Group Branch Surabaya)
27. Klik Bulk Action > `Edit Home Group`
28. Klik node Branch Surabaya lalu klik `[Select]`
29. Verifikasi toast "No changes to save." tampil (bukan toast sukses)
30. Baca jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab Changelog Kartika Sari, Tab Changelog Eka Wulandari, Tab Changelog Fajar Nugroho, Tab System Log aktor, dan Activity Log
31. Verifikasi jumlah entri bertambah 2 untuk Hana Kusuma (TC-FA-SU-307 dan TC-FA-SU-308), 1 untuk Kartika Sari, dan tidak berubah untuk Eka Wulandari serta Fajar Nugroho dibanding baseline pada Tab Changelog target, Tab System Log aktor, dan Activity Log
32. Pulihkan Home Group Hana Kusuma dan Kartika Sari ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Entri log diamati sekali pada akhir spec dengan satu baseline (langkah 1). Selisih kumulatif memuat asersi TC-FA-SU-308 "baris yang sudah di Branch Surabaya di-skip tanpa entri log" (Eka Wulandari tidak bertambah) dan TC-FA-SU-309 "tidak ada entri log pada tiga permukaan log" (Eka Wulandari dan Fajar Nugroho tidak bertambah); keduanya asersi jumlah dengan baseline (S-12), bukan kelas g. Satu entri yang diamati pada tiga surface ditulis satu `Verifikasi` (S-01).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), `[Cancel]`, Unselect All, kembali ke User List, membuka Tab Changelog, dan langkah 20 serta 32 (pemulihan). Pemulihan Hana Kusuma dan Kartika Sari antara TC-FA-SU-307 dan TC-FA-SU-308 diperlukan supaya Hana Kusuma tidak sudah berada di Branch Surabaya.
- Temuan untuk QA (S-15): (1) Home Group awal Kartika Sari tidak tertulis di Pre-setup TC (hanya Pending Activation dan Inactive). (2) TC-FA-SU-307 langkah 4 membuka Tab Changelog kedua pengguna dan Post Condition meminta entri pada Tab System Log aktor dan Activity Log; diamati lewat selisih jumlah pada akhir spec. (3) Post Condition TC-FA-SU-308 butir kedua ("baris yang berubah menjadi Branch Surabaya") hanya diamati untuk Hana Kusuma.
