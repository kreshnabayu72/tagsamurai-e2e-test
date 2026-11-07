---
id: TC-FA-SU-E2E-098-bulk-edit-home-group-kosongkan-dialog-gabungan-per-pengguna-dan-hasil-cancel
title: "Bulk Edit Home Group: Kosongkan, Dialog Gabungan per Pengguna, dan Hasil Cancel"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-312
  - TC-FA-SU-313
  - TC-FA-SU-314
  - TC-FA-SU-315
coverage:
  web: automated
---

# Bulk Edit Home Group: Kosongkan, Dialog Gabungan per Pengguna, dan Hasil Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21). Pengguna: Gita Permata (Home Group Finance & Accounting; Group Role Manage group pada Finance & Accounting; Role Transaksi Disposal × Asset Admin pada Finance & Accounting, Disposal × Approver pada Accounts Payable, dan Damaged × Staff pada IT Infrastructure; varian `FaUserHGT` Pre-setup #51), Hana Kusuma (Home Group General Affairs, dikosongkan lebih dulu pada langkah 3), Wawan Setiawan (beberapa Group Role di luar constraint IT Infrastructure; varian `FaUserHGT` Pre-setup #51), Eka Wulandari (Home Group Branch Surabaya). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Group Role dan Role Transaksi pada langkah 19, 33, dan 54 serta di hook `after`. Efek pada Pre-setup: Home Group, Group Role, Last Updated, dan Modified By Gita Permata, Hana Kusuma, dan Wawan Setiawan berubah dan entri log permanen bertambah.

## Test Steps

1. Catat daftar Global Role, Group Role, dan Transaction Role Gita Permata sebagai baseline peran

### TC-FA-SU-312: Bulk tanpa memilih node mengosongkan Home Group

2. Ketik Search `Hana Kusuma`, tekan Enter
3. Kosongkan Home Group Hana Kusuma (klik ⋯ pada baris Hana Kusuma, `Edit Home Group`, klik ulang node General Affairs yang ter-highlight, lalu `[Select]`)
4. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log sebagai baseline TC-FA-SU-312
5. Centang Hana Kusuma (Hana tanpa Home Group)
6. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
7. Centang Gita Permata
8. Klik Bulk Action > `Edit Home Group`
9. Klik `[Select]` tanpa memilih node
10. Verifikasi tidak ada dialog
11. Verifikasi toast "Success, home group has been updated. Some items were skipped." tampil
12. Verifikasi Home Group Gita Permata menjadi `—`
13. Verifikasi peran Gita Permata tidak berubah dibanding yang dicatat pada baseline peran (langkah 1)
14. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
15. Verifikasi Home Group Hana Kusuma tetap tanpa Home Group (di-skip sebagai tanpa perubahan)
16. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log
17. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline langkah 4 pada Tab Changelog Gita Permata (New Value `—`), Tab System Log aktor, dan Activity Log
18. Verifikasi jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma tidak berubah dibanding baseline langkah 4
19. Pulihkan Home Group dan Group Role Gita Permata serta Home Group Hana Kusuma ke kondisi Pre-setup lewat seed API

### TC-FA-SU-313: Dialog gabungan per pengguna, Cancel satu pengguna

20. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
21. Centang Gita Permata
22. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
23. Centang Wawan Setiawan
24. Klik Bulk Action > `Edit Home Group`, klik node IT Infrastructure, lalu klik `[Select]`
25. Verifikasi dialog D-10 pengguna pertama tampil dengan nama Gita Permata pada bullet
26. Klik `[Cancel]` pada dialog pengguna pertama
27. Verifikasi dialog D-10 pengguna kedua tampil dengan nama Wawan Setiawan pada bullet
28. Klik `[Revoke]` pada dialog pengguna kedua
29. Verifikasi toast "Success, home group has been updated. Some items were skipped." tampil
30. Verifikasi Home Group Wawan Setiawan berubah menjadi IT Infrastructure
31. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
32. Verifikasi Home Group Gita Permata tidak berubah (Cancel hanya membatalkan pengguna itu)
33. Pulihkan Home Group dan Group Role Gita Permata dan Wawan Setiawan ke kondisi Pre-setup lewat seed API

### TC-FA-SU-314: Seluruh pengguna di-Cancel pada dialog D-10

34. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
35. Centang Gita Permata
36. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
37. Centang Wawan Setiawan
38. Klik Bulk Action > `Edit Home Group`, klik node IT Infrastructure, lalu klik `[Select]`
39. Klik `[Cancel]` pada dialog pengguna pertama dan pada dialog pengguna kedua
40. Verifikasi tidak ada toast dan daftar tidak berubah
41. Verifikasi tidak ada perubahan tersimpan pada Wawan Setiawan
42. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
43. Verifikasi tidak ada perubahan tersimpan pada Gita Permata

### TC-FA-SU-315: Campuran Cancel dan sudah di grup tujuan

44. Klik ikon `(×)` pada Bulk Actions Bar
45. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
46. Centang Gita Permata
47. Ganti isi kotak search dengan `Eka Wulandari`, tekan Enter
48. Centang Eka Wulandari (sudah di Branch Surabaya)
49. Klik Bulk Action > `Edit Home Group`, klik node Branch Surabaya, lalu klik `[Select]`
50. Klik `[Cancel]` pada dialog Gita Permata
51. Verifikasi toast "No changes to save." tampil
52. Ganti isi kotak search dengan `Gita Permata`, tekan Enter, klik nama Gita Permata, lalu buka Tab Changelog, muat ulang sampai entri tampil
53. Verifikasi entri teratas Tab Changelog Gita Permata adalah `Edit Home Group` dengan New Value `—` (entri tambahan dari TC-FA-SU-312)
54. Pulihkan Home Group dan Group Role Gita Permata dan Wawan Setiawan serta Home Group Hana Kusuma ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Jumlah langkah 54, di atas smell 35 langkah; satu skenario Bulk Edit Home Group pada pengguna Pre-setup yang sama dengan pemulihan seed antar TC. Kelebihan berasal dari baseline dan selisih log TC-FA-SU-312 (S-12), Search per baris target (R-16), dan Search per pengguna sebelum asersi (bagian 8b butir 13), bukan dari pengulangan makna.
- Entri log diamati hanya untuk TC-FA-SU-312, karena hanya TC itu yang diamati lewat Tab Changelog target di spec ini: baseline dicatat tepat sebelum aksi (langkah 4) dan selisih dibaca tepat sesudah aksi (langkah 16, S-12). Selisih TC-FA-SU-312 memuat satu entri `Edit Home Group` pada Gita Permata (New Value `—`). Entri log TC-FA-SU-313, TC-FA-SU-314, dan TC-FA-SU-315 tidak diasersi (lihat Temuan untuk QA butir 6).
- Pengosongan Home Group Hana Kusuma (langkah 3, persiapan TC-FA-SU-312) dilakukan sebelum baseline langkah 4 sehingga entrinya tidak masuk selisih TC-FA-SU-312; Hana Kusuma di-skip dan tidak berubah pada TC-FA-SU-312.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline peran), langkah 4 (baseline log), langkah 16 (membaca jumlah entri), langkah 19, 33, dan 54 (pemulihan), langkah 44 (menghapus seleksi sebelum TC-FA-SU-315, S-09), serta Search untuk menemukan baris target (langkah 2, 6, 14, 20, 22, 31, 34, 36, 42, 45, 47, dan 52; R-16 dan butir 8b.13, memakai "ganti isi kotak search" bila kotak sudah berisi) yang pada langkah 52 dilanjutkan membuka Tab Changelog Gita Permata; langkah sesudahnya membuktikan isi entri New Value `—` TC-FA-SU-312. Search pada langkah 42 menyempitkan tabel ke Gita Permata sebelum asersi atasnya (langkah 41 mengasersi Wawan Setiawan lebih dulu). Seleksi dihapus pada langkah 44 karena seleksi tetap dipertahankan setelah aksi bulk yang tidak di-commit (kedua dialog di-Cancel pada TC-FA-SU-314) dan baru di-reset setelah aksi bulk ter-commit (S-09, PRD); tanpa langkah itu Gita Permata dan Wawan Setiawan masih tercentang dan langkah 46 justru membatalkan centang Gita Permata. Pemulihan antar TC memastikan Gita Permata (Group Role dan Role Transaksi) dan Wawan Setiawan (Group Role) memiliki penugasan di luar constraint untuk dialog D-10 per pengguna (TC-FA-SU-313, Pre-setup #51).
- Temuan untuk QA (S-15): (1) TC-FA-SU-313 diperbarui (Pre-setup #51): kedua pengguna punya Group Role atau Role Transaksi di luar constraint sehingga dialog D-10 muncul per pengguna; bullet Role Transaksi Gita Permata tidak disebut Expected sehingga langkah 25 hanya mengasersi nama pengguna pada bullet. Urutan dialog per pengguna pada TC-FA-SU-313 (pengguna pertama Gita Permata, kedua Wawan Setiawan) mengikuti urutan centang; TC tidak menyebut urutan dialog. (2) TC-FA-SU-315 tidak menyebut node tujuan; spec memakai Branch Surabaya (Home Group Eka Wulandari). (3) TC-FA-SU-312 langkah 3 menyebut "tanpa memilih node" sedangkan pengosongan Hana Kusuma dilakukan lewat klik ulang node (TC-FA-SU-288). (4) Post Condition TC-FA-SU-312 (entri `Edit Home Group`) diamati lewat selisih jumlah dengan baseline tepat sebelum aksi; langkah 4, 16, dan 17 mengasersi tiga surface (Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log), sedangkan TC-FA-SU-312 hanya punya Post Condition tanpa Expected atau langkah observasi untuk ketiga surface itu; mohon konfirmasi apakah asersi Tab System Log aktor dan Activity Log dipertahankan atau diturunkan ke Tab Changelog saja. (5) Pemilihan dua pengguna pada TC-FA-SU-312, 313, 314, dan 315 lewat Search per baris mengasumsikan seleksi bertahan saat isi Search berganti (seperti lintas halaman); mohon konfirmasi. (6) Post Condition TC-FA-SU-313 (entri `Edit Home Group` pada Tab Changelog target, Tab System Log aktor, dan Activity Log), TC-FA-SU-314 dan TC-FA-SU-315 (tidak ada entri baru pada tiga permukaan log) tidak punya langkah observasi di TC; asersi log tiga surface dihapus dari spec dan dicatat di sini untuk QA.
