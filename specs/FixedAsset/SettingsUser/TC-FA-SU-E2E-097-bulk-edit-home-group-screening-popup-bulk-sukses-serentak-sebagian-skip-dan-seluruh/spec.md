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
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Hana Kusuma dan Kartika Sari pada langkah 29 dan 51 serta di hook `after`. Efek pada Pre-setup: Home Group, Last Updated, dan Modified By Hana Kusuma dan Kartika Sari berubah dan entri log permanen bertambah; Eka Wulandari dan Fajar Nugroho tidak diubah.

## Test Steps

### TC-FA-SU-306: Screening popup Select Home Group varian bulk

1. Ketik Search `Gita Permata`, tekan Enter, lalu centang Gita Permata
2. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu centang Budi Santoso
3. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu centang Hana Kusuma
4. Klik Bulk Action > `Edit Home Group`
5. Verifikasi judul `Select Home Group — 3 users` (jumlah baris terpilih) tampil
6. Verifikasi popup tidak memuat daftar nama pengguna
7. Verifikasi pohon dimulai tanpa node terpilih
8. Verifikasi `[Select]` Enabled
9. Klik `[Cancel]` lalu klik Unselect All
10. Ganti isi kotak search dengan `Gita Permata`, tekan Enter, centang Gita Permata saja, lalu klik Bulk Action > `Edit Home Group`
11. Verifikasi judul `Select Home Group` (varian singular) tampil
12. Klik `[Cancel]` lalu klik Unselect All

### TC-FA-SU-307: Bulk Edit Home Group seluruh baris berubah

13. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu catat jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma sebagai baseline TC-FA-SU-307
14. Kembali ke User List, ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu catat jumlah entri `Edit Home Group` pada Tab Changelog Kartika Sari sebagai baseline TC-FA-SU-307
15. Kembali ke User List, ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu centang Hana Kusuma
16. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu centang Kartika Sari
17. Klik Bulk Action > `Edit Home Group`
18. Klik node Branch Surabaya lalu klik `[Select]`
19. Verifikasi toast "Success, home group has been updated." tampil
20. Verifikasi Home Group Kartika Sari berubah menjadi Branch Surabaya
21. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
22. Verifikasi Home Group Hana Kusuma berubah menjadi Branch Surabaya
23. Verifikasi seleksi di-reset
24. Buka Tab Changelog Hana Kusuma
25. Baca jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma
26. Kembali ke User List, ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu buka Tab Changelog Kartika Sari
27. Baca jumlah entri `Edit Home Group` pada Tab Changelog Kartika Sari
28. Verifikasi satu entri `Edit Home Group` per pengguna yang berubah tercatat: jumlah entri bertambah 1 untuk Hana Kusuma dan 1 untuk Kartika Sari dibanding baseline TC-FA-SU-307
29. Pulihkan Home Group Hana Kusuma dan Kartika Sari ke kondisi Pre-setup lewat seed API

### TC-FA-SU-308: Bulk sebagian sudah di grup tujuan

30. Kembali ke User List, ganti isi kotak search dengan `Eka Wulandari`, tekan Enter, lalu catat jumlah entri `Edit Home Group` pada Tab Changelog Eka Wulandari sebagai baseline TC-FA-SU-308
31. Kembali ke User List, ganti isi kotak search dengan `Eka Wulandari`, tekan Enter, lalu centang Eka Wulandari (Home Group Branch Surabaya)
32. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu centang Hana Kusuma
33. Klik Bulk Action > `Edit Home Group`
34. Klik node Branch Surabaya lalu klik `[Select]`
35. Verifikasi toast "Success, home group has been updated. Some items were skipped." tampil
36. Verifikasi Home Group Hana Kusuma berubah menjadi Branch Surabaya
37. Ganti isi kotak search dengan `Eka Wulandari`, tekan Enter, lalu baca jumlah entri `Edit Home Group` pada Tab Changelog Eka Wulandari
38. Verifikasi jumlah entri `Edit Home Group` Eka Wulandari sama dengan baseline TC-FA-SU-308 (baris yang sudah di Branch Surabaya di-skip tanpa entri log)

### TC-FA-SU-309: Bulk seluruh baris sudah di grup tujuan

39. Kembali ke User List, ganti isi kotak search dengan `Eka Wulandari`, tekan Enter, lalu catat jumlah entri `Edit Home Group` pada Tab Changelog Eka Wulandari sebagai baseline TC-FA-SU-309
40. Kembali ke User List, ganti isi kotak search dengan `Fajar Nugroho`, tekan Enter, lalu catat jumlah entri `Edit Home Group` pada Tab Changelog Fajar Nugroho sebagai baseline TC-FA-SU-309
41. Catat jumlah entri `Edit Home Group` pada Tab System Log aktor dan Activity Log sebagai baseline TC-FA-SU-309
42. Kembali ke User List, ganti isi kotak search dengan `Eka Wulandari`, tekan Enter, lalu centang Eka Wulandari (Home Group Branch Surabaya)
43. Ganti isi kotak search dengan `Fajar Nugroho`, tekan Enter, lalu centang Fajar Nugroho (Home Group Branch Surabaya)
44. Klik Bulk Action > `Edit Home Group`
45. Klik node Branch Surabaya lalu klik `[Select]`
46. Verifikasi toast "No changes to save." tampil (bukan toast sukses)
47. Ganti isi kotak search dengan `Eka Wulandari`, tekan Enter, lalu baca jumlah entri `Edit Home Group` pada Tab Changelog Eka Wulandari
48. Kembali ke User List, ganti isi kotak search dengan `Fajar Nugroho`, tekan Enter, lalu baca jumlah entri `Edit Home Group` pada Tab Changelog Fajar Nugroho
49. Baca jumlah entri `Edit Home Group` pada Tab System Log aktor dan Activity Log
50. Verifikasi jumlah entri `Edit Home Group` sama dengan baseline TC-FA-SU-309 pada Tab Changelog Eka Wulandari, Tab Changelog Fajar Nugroho, Tab System Log aktor, dan Activity Log
51. Pulihkan Home Group Hana Kusuma dan Kartika Sari ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baseline entri log dicatat per TC sebelum aksi pemicu (langkah 13 dan 14, 30, serta 39 sampai 41) dan selisih diverifikasi tepat sesudah aksi (langkah 28, 38, dan 50): TC-FA-SU-307 menambah 1 entri per pengguna yang berubah pada Tab Changelog target, TC-FA-SU-308 "baris yang sudah di Branch Surabaya di-skip tanpa entri log" (Eka Wulandari tidak bertambah), dan TC-FA-SU-309 "tidak ada entri log pada tiga permukaan log" (Eka Wulandari dan Fajar Nugroho tidak bertambah pada Tab Changelog target, Tab System Log aktor, dan Activity Log); ketiganya asersi jumlah dengan baseline (S-12), bukan kelas g. Satu entri yang diamati pada tiga surface ditulis satu `Verifikasi` (S-01).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 13 dan 14, 30, serta 39 sampai 41 (baseline per TC), `[Cancel]`, Unselect All, kembali ke User List, membuka Tab Changelog, dan langkah 29 serta 51 (pemulihan). Pemulihan Hana Kusuma dan Kartika Sari antara TC-FA-SU-307 dan TC-FA-SU-308 diperlukan supaya Hana Kusuma tidak sudah berada di Branch Surabaya.
- Langkah penghubung Search (R-16, bagian 8b butir 9 dan 13): User List memuat 3 halaman, sehingga tiap langkah yang mencentang, membuka Tab Changelog, atau membaca baris satu pengguna didahului Search nama persis pengguna itu (langkah 1 sampai 3, 10, 13 sampai 16, 21, 26, 30 sampai 32, 37, 39, 40, 42, 43, 47, dan 48); langkah 1 memakai "Ketik Search" karena kotak masih kosong, langkah lain memakai "ganti isi kotak search" karena kotak masih berisi nama sebelumnya. Baris bulk dicentang satu per satu dengan Search per baris.
- Jumlah langkah 51, di atas smell 35 langkah; semua blok satu kelas harness (bulk Edit Home Group fungsional) dan satu topik, tiap TC berdiri sendiri; kelebihan berasal dari Search per baris target (R-16), baseline per TC dengan selisih tepat sesudah aksi (S-12), dan satu Verifikasi per klausa Expected (S-01).
- Temuan untuk QA (S-15): (0) TC-FA-SU-306 dan TC-FA-SU-307 mencentang beberapa baris tanpa menyebut cara menemukan baris; spec memakai Search per baris dan mengasumsikan seleksi bertahan saat isi Search berganti (seperti TC-FA-SU-120 Expected a); bila tidak bertahan, QA perlu menyebut cara lain. (1) Home Group awal Kartika Sari tidak tertulis di Pre-setup TC (hanya Pending Activation dan Inactive). (2) TC-FA-SU-307 langkah 4 membuka Tab Changelog kedua pengguna dan Post Condition meminta entri pada Tab System Log aktor dan Activity Log tanpa langkah observasi; hanya Tab Changelog target yang diasersi (selisih jumlah entri, langkah 20), sedangkan Tab System Log aktor dan Activity Log untuk TC ini tidak diasersi (S-03). (3) Post Condition TC-FA-SU-308 butir kedua ("baris yang berubah menjadi Branch Surabaya") hanya diamati untuk Hana Kusuma.
