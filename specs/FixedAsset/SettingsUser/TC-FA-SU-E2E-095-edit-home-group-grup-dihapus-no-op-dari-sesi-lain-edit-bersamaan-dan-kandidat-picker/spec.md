---
id: TC-FA-SU-E2E-095-edit-home-group-grup-dihapus-no-op-dari-sesi-lain-edit-bersamaan-dan-kandidat-picker
title: "Edit Home Group: Grup Dihapus, No-op dari Sesi Lain, Edit Bersamaan, dan Kandidat Picker Role & Permission"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-300
  - TC-FA-SU-302
  - TC-FA-SU-316
  - TC-FA-SU-317
  - TC-FA-SU-318
coverage:
  web: automated
---

# Edit Home Group: Grup Dihapus, No-op dari Sesi Lain, Edit Bersamaan, dan Kandidat Picker Role & Permission

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua (Admin B, Pre-setup #13) memakai sesi API akun aktor (login API password, token tidak dihitung sebagai sesi web) untuk menyimpan Home Group dan menghapus grup. Kemampuan disediakan tim BE/FE; sesi UI kedua tidak dipakai.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Gita Permata (Home Group Finance & Accounting; Group Role Manage group pada Finance & Accounting), Hana Kusuma (Home Group General Affairs), Budi Santoso. Grup Logistics Warehouse (Pre-setup #21; Home Group Doni Prasetyo) dihapus lewat sesi API lalu dipulihkan. Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Gita Permata (langkah 6, 22), Hana Kusuma (hook `after`), dan grup Logistics Warehouse beserta Home Group yang terkait (langkah 29) dan di hook `after` (pemulihan grup setelah TC-FA-SU-316 dikerjakan hook `after`). Efek pada Pre-setup: Last Updated, Modified By, dan Group Role Gita Permata berubah, entri log permanen bertambah, dan grup Logistics Warehouse sempat terhapus (suite berjalan serial).
- Pada Settings > Role & Permission, spec memakai Detail Role Manage group dan popup Assign pada node Finance & Accounting (Table User Picker Group Role).

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline

### TC-FA-SU-302: Edit Home Group ke nilai yang sudah berlaku dari sesi lain

2. Klik ⋯ pada baris Gita Permata, klik `Edit Home Group`, lalu klik node IT Infrastructure (sesi A)
3. Admin B menyimpan Home Group Gita Permata ke IT Infrastructure melalui sesi API hingga tersimpan
4. Klik `[Select]` pada sesi A
5. Verifikasi toast "No changes to save." tampil
6. Pulihkan Home Group dan Group Role Gita Permata ke kondisi Pre-setup lewat seed API

### TC-FA-SU-318: Edit bersamaan last-write-wins

7. Klik ⋯ pada baris Hana Kusuma, klik `Edit Home Group`, lalu klik node IT Infrastructure (sesi A)
8. Admin B menyimpan Home Group Hana Kusuma ke Branch Surabaya melalui sesi API hingga tersimpan
9. Klik `[Select]` pada sesi A
10. Verifikasi tidak ada dialog konflik versi
11. Verifikasi Home Group Hana Kusuma akhir mengikuti permintaan yang terakhir diterima (IT Infrastructure)

### TC-FA-SU-317: Kandidat Table User Picker Group Role

12. Set Home Group Gita Permata ke IT Infrastructure (klik ⋯, `Edit Home Group`, klik node IT Infrastructure, `[Select]`) lalu klik `[Revoke]` pada dialog `Role Outside Constraint Will Be Revoked`
13. Tunggu aksi selesai: permintaan `[Revoke]` pada langkah 12 selesai dan dialog tertutup
14. Buka Settings > Role & Permission > Detail Role Manage group lalu buka popup Assign pada node Finance & Accounting
15. Ketik Search `Gita Permata`, tekan Enter
16. Verifikasi Gita Permata tidak muncul sebagai kandidat (empty state `No results found`)
17. Buka Fixed Asset > Settings > User lalu kosongkan Home Group Gita Permata (klik ⋯, `Edit Home Group`, klik ulang node IT Infrastructure, `[Select]`)
18. Tunggu aksi selesai: permintaan `[Select]` pada langkah 17 selesai dan popup tertutup
19. Buka Settings > Role & Permission > Detail Role Manage group lalu buka popup Assign pada node Finance & Accounting
20. Ketik Search `Gita Permata`, tekan Enter
21. Verifikasi Gita Permata muncul kembali sebagai kandidat
22. Pulihkan Home Group dan Group Role Gita Permata ke kondisi Pre-setup lewat seed API

### TC-FA-SU-300: Grup dihapus sebelum Select (single)

23. Buka Fixed Asset > Settings > User lalu klik ⋯ pada baris Gita Permata, klik `Edit Home Group`, dan klik node Logistics Warehouse
24. Admin B menghapus grup Logistics Warehouse melalui sesi API hingga grup terhapus
25. Klik `[Select]`
26. Verifikasi toast error "Error, failed to update home group. This group no longer exists. Please select another." tampil
27. Verifikasi pilihan dibersihkan dan popup tetap terbuka
28. Klik `[Cancel]`
29. Pulihkan grup Logistics Warehouse lewat seed API

### TC-FA-SU-316: Grup dihapus sebelum Select (bulk)

30. Centang Gita Permata dan Hana Kusuma, klik Bulk Action > `Edit Home Group`, lalu klik node Logistics Warehouse
31. Admin B menghapus grup Logistics Warehouse melalui sesi API hingga grup terhapus
32. Klik `[Select]`
33. Verifikasi toast error "Error, failed to update home group. This group no longer exists. Please select another." tampil
34. Verifikasi popup tetap terbuka dan pilihan dibersihkan
35. Klik `[Cancel]`
36. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
37. Verifikasi jumlah entri Gita Permata bertambah 3 dibanding baseline (penyimpanan Admin B pada TC-FA-SU-302 langkah 3, set Home Group beserta Revoke pada TC-FA-SU-317 langkah 12, dan pengosongan Home Group pada TC-FA-SU-317 langkah 17) sehingga sesi A pada TC-FA-SU-302 serta TC-FA-SU-300 dan TC-FA-SU-316 tidak menambah entri

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-302 dan TC-FA-SU-318 (tanpa penghapusan grup) diletakkan lebih dulu, lalu TC-FA-SU-317, dan TC-FA-SU-300 serta TC-FA-SU-316 (penghapusan grup) di akhir sesuai bagian 3 (aksi yang menghapus data di akhir). Pemulihan seed diperlukan antar TC karena penyimpanan Admin B dan Revoke mengubah Home Group serta Group Role.
- Pelaku kedua memakai sesi API (R-20, P-2 `[KEPUTUSAN 2026-10-30]`): tidak ada konteks UI kedua dan tidak ada butir `P-2`. TC-FA-SU-300, TC-FA-SU-302, TC-FA-SU-316, dan TC-FA-SU-318 berlabel `Manual Only — (d) dua sesi paralel`; keempatnya ditulis berurutan dengan pemicu sesi API.
- Selisih akhir langkah 37 adalah 3 entri `Edit Home Group` Gita Permata (langkah 3, 12, dan 17); pemulihan seed API tidak dihitung sebagai entri.
- Spec ini berjumlah 37 langkah dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama (Edit Home Group), berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri serta dua langkah menunggu aksi selesai (langkah 13 dan 18) dan tiga pemulihan seed (langkah 6, 22, 29).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), membuka halaman lain, menutup popup dengan `[Cancel]`, serta langkah 6, 22, dan 29 (pemulihan), dan langkah 13 serta 18 (menunggu aksi `[Revoke]` dan `[Select]` selesai sebelum berpindah permukaan, bagian 8b butir 8). Search `Gita Permata` pada popup Assign adalah langkah penghubung untuk menemukan baris target (R-16); empty state `No results found` menjadi anchor positif absence.
- Temuan untuk QA (S-15): (1) TC-FA-SU-318 meminta penyimpanan "hampir bersamaan"; spec menyimpan Admin B lebih dulu lalu sesi A sehingga permintaan sesi A terakhir diterima (tidak deterministik bila benar-benar bersamaan). (2) TC-FA-SU-317 langkah 3 menyebut Search tanpa kolom; spec memakai Search `Gita Permata` dan hanya mengamati node Finance & Accounting (Expected "node mana pun" tidak diamati). (3) TC-FA-SU-300 dan TC-FA-SU-316 menghapus Logistics Warehouse yang merupakan Pre-setup bersama (Home Group Doni Prasetyo); pemulihan lewat seed API. (4) Post Condition TC-FA-SU-300 dan TC-FA-SU-316 (tidak ada entri baru pada tiga permukaan log) diamati lewat selisih jumlah entri pada tiga surface langkah akhir (Tab Changelog Gita Permata, Tab System Log aktor, Activity Log) sebagai asersi jumlah, bukan kelas g.
