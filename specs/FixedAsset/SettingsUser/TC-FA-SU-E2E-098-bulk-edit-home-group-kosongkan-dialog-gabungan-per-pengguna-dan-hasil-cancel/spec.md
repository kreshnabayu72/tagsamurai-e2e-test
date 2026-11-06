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
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21). Pengguna: Gita Permata (Home Group Finance & Accounting; Group Role Manage group pada Finance & Accounting; Role Transaksi Disposal × Asset Admin pada Finance & Accounting, Disposal × Approver pada Accounts Payable, dan Damaged × Staff pada IT Infrastructure; varian `FaUserHGT` Pre-setup #51), Hana Kusuma (Home Group General Affairs, dikosongkan lebih dulu pada langkah 2), Wawan Setiawan (beberapa Group Role di luar constraint IT Infrastructure; varian `FaUserHGT` Pre-setup #51), Eka Wulandari (Home Group Branch Surabaya). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Group Role dan Role Transaksi pada langkah 11, 21, dan 33 serta di hook `after`. Efek pada Pre-setup: Home Group, Group Role, Last Updated, dan Modified By Gita Permata, Hana Kusuma, dan Wawan Setiawan berubah dan entri log permanen bertambah.

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab Changelog Hana Kusuma, Tab Changelog Wawan Setiawan, Tab Changelog Eka Wulandari, Tab System Log aktor, dan Activity Log sebagai baseline; catat daftar Global Role, Group Role, dan Transaction Role Gita Permata

### TC-FA-SU-312: Bulk tanpa memilih node mengosongkan Home Group

2. Kosongkan Home Group Hana Kusuma (klik ⋯ pada baris Hana Kusuma, `Edit Home Group`, klik ulang node General Affairs yang ter-highlight, lalu `[Select]`)
3. Centang Gita Permata dan Hana Kusuma (Hana tanpa Home Group)
4. Klik Bulk Action > `Edit Home Group`
5. Klik `[Select]` tanpa memilih node
6. Verifikasi tidak ada dialog
7. Verifikasi Home Group Gita Permata menjadi `—`
8. Verifikasi peran Gita Permata tidak berubah dibanding yang dicatat pada baseline
9. Verifikasi Home Group Hana Kusuma tetap tanpa Home Group (di-skip sebagai tanpa perubahan)
10. Verifikasi toast "Success, home group has been updated. Some items were skipped." tampil
11. Pulihkan Home Group dan Group Role Gita Permata serta Home Group Hana Kusuma ke kondisi Pre-setup lewat seed API

### TC-FA-SU-313: Dialog gabungan per pengguna, Cancel satu pengguna

12. Centang Gita Permata dan Wawan Setiawan
13. Klik Bulk Action > `Edit Home Group`, klik node IT Infrastructure, lalu klik `[Select]`
14. Verifikasi dialog D-10 pengguna pertama tampil dengan nama Gita Permata pada bullet
15. Klik `[Cancel]` pada dialog pengguna pertama
16. Verifikasi dialog D-10 pengguna kedua tampil dengan nama Wawan Setiawan pada bullet
17. Klik `[Revoke]` pada dialog pengguna kedua
18. Verifikasi toast "Success, home group has been updated. Some items were skipped." tampil
19. Verifikasi Home Group Gita Permata tidak berubah (Cancel hanya membatalkan pengguna itu)
20. Verifikasi Home Group Wawan Setiawan berubah menjadi IT Infrastructure
21. Pulihkan Home Group dan Group Role Gita Permata dan Wawan Setiawan ke kondisi Pre-setup lewat seed API

### TC-FA-SU-314: Seluruh pengguna di-Cancel pada dialog D-10

22. Kembali ke User List lalu centang Gita Permata dan Wawan Setiawan
23. Klik Bulk Action > `Edit Home Group`, klik node IT Infrastructure, lalu klik `[Select]`
24. Klik `[Cancel]` pada dialog pengguna pertama dan pada dialog pengguna kedua
25. Verifikasi tidak ada perubahan tersimpan pada Gita Permata dan Wawan Setiawan
26. Verifikasi tidak ada toast dan daftar tidak berubah

### TC-FA-SU-315: Campuran Cancel dan sudah di grup tujuan

27. Centang Gita Permata dan Eka Wulandari (sudah di Branch Surabaya)
28. Klik Bulk Action > `Edit Home Group`, klik node Branch Surabaya, lalu klik `[Select]`
29. Klik `[Cancel]` pada dialog Gita Permata
30. Verifikasi toast "No changes to save." tampil
31. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab Changelog Hana Kusuma, Tab Changelog Wawan Setiawan, Tab Changelog Eka Wulandari, Tab System Log aktor, dan Activity Log
32. Verifikasi jumlah entri bertambah 1 untuk Gita Permata (TC-FA-SU-312, New Value `—`), 1 untuk Wawan Setiawan (TC-FA-SU-313), dan 1 untuk Hana Kusuma (pengosongan Home Group pada langkah 2, sesudah baseline langkah 1), serta tidak berubah untuk Eka Wulandari dibanding baseline pada Tab Changelog target, Tab System Log aktor, dan Activity Log
33. Pulihkan Home Group dan Group Role Gita Permata dan Wawan Setiawan serta Home Group Hana Kusuma ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Entri log diamati sekali pada akhir spec dengan satu baseline (langkah 1). Selisih kumulatif memuat TC-FA-SU-312 (satu entri `Edit Home Group` New Value `—` untuk pengguna yang berubah) dan asersi "tidak ada entri log" TC-FA-SU-314 serta TC-FA-SU-315 sebagai asersi jumlah dengan baseline (S-12), bukan kelas g.
- Hana Kusuma bertambah 1 entri karena langkah 2 (persiapan TC-FA-SU-312) mengosongkan Home Group-nya sesudah baseline langkah 1; Eka Wulandari tidak berubah.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), kembali ke User List, dan langkah 11, 21, 33 (pemulihan). Pemulihan antar TC memastikan Gita Permata (Group Role dan Role Transaksi) dan Wawan Setiawan (Group Role) memiliki penugasan di luar constraint untuk dialog D-10 per pengguna (TC-FA-SU-313, Pre-setup #51).
- Temuan untuk QA (S-15): (1) TC-FA-SU-313 diperbarui (Pre-setup #51): kedua pengguna punya Group Role atau Role Transaksi di luar constraint sehingga dialog D-10 muncul per pengguna; bullet Role Transaksi Gita Permata tidak disebut Expected sehingga langkah 14 hanya mengasersi nama pengguna pada bullet. Urutan dialog per pengguna pada TC-FA-SU-313 (pengguna pertama Gita Permata, kedua Wawan Setiawan) mengikuti urutan centang; TC tidak menyebut urutan dialog. (2) TC-FA-SU-315 tidak menyebut node tujuan; spec memakai Branch Surabaya (Home Group Eka Wulandari). (3) TC-FA-SU-312 langkah 3 menyebut "tanpa memilih node" sedangkan pengosongan Hana Kusuma dilakukan lewat klik ulang node (TC-FA-SU-288). (4) Post Condition TC-FA-SU-313 (entri `Edit Home Group` pengguna lain) diamati lewat selisih jumlah.
