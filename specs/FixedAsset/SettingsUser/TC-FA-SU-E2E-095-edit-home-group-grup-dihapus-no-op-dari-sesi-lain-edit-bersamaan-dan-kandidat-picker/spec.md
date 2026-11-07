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
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Gita Permata (Home Group Finance & Accounting; Group Role Manage group pada Finance & Accounting; pada blok TC-FA-SU-317 juga Role Transaksi Disposal × Asset Admin pada Finance & Accounting dan Disposal × Approver pada Accounts Payable, varian `FaUserHGT` Pre-setup #51), Hana Kusuma (Home Group General Affairs), Budi Santoso. Grup Logistics Warehouse (Pre-setup #21; Home Group Doni Prasetyo) dihapus lewat sesi API lalu dipulihkan. Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Gita Permata (langkah 9, 41), Hana Kusuma (hook `after`), dan grup Logistics Warehouse beserta Home Group yang terkait (langkah 52) dan di hook `after` (pemulihan grup setelah TC-FA-SU-316 dikerjakan hook `after`). Efek pada Pre-setup: Last Updated, Modified By, dan Group Role Gita Permata berubah, entri log permanen bertambah, dan grup Logistics Warehouse sempat terhapus (suite berjalan serial).
- Pada Settings > Role & Permission, spec memakai Detail Role Manage group dan popup Assign pada node Finance & Accounting (Table User Picker Group Role) dan Tab Transaction Role > Sub-tab Disposal popup Assign Role Transaksi (Asset Admin) pada node Finance & Accounting.

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata sebagai baseline TC-FA-SU-302

### TC-FA-SU-302: Edit Home Group ke nilai yang sudah berlaku dari sesi lain

2. Ketik Search `Gita Permata`, tekan Enter
3. Klik ⋯ pada baris Gita Permata, klik `Edit Home Group`, lalu klik node IT Infrastructure (sesi A)
4. Admin B menyimpan Home Group Gita Permata ke IT Infrastructure melalui sesi API hingga tersimpan
5. Klik `[Select]` pada sesi A
6. Verifikasi toast "No changes to save." tampil
7. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata
8. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline TC-FA-SU-302 (penyimpanan Admin B; `[Select]` sesi A tidak menambah entri)
9. Pulihkan Home Group dan Group Role Gita Permata ke kondisi Pre-setup lewat seed API

### TC-FA-SU-318: Edit bersamaan last-write-wins

10. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
11. Klik ⋯ pada baris Hana Kusuma, klik `Edit Home Group`, lalu klik node IT Infrastructure (sesi A)
12. Admin B menyimpan Home Group Hana Kusuma ke Branch Surabaya melalui sesi API hingga tersimpan
13. Klik `[Select]` pada sesi A
14. Verifikasi tidak ada dialog konflik versi
15. Verifikasi Home Group Hana Kusuma akhir mengikuti permintaan yang terakhir diterima (IT Infrastructure)

### TC-FA-SU-317: Kandidat Table User Picker Group Role dan popup Assign Role Transaksi

16. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline TC-FA-SU-317
17. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
18. Set Home Group Gita Permata ke IT Infrastructure (klik ⋯, `Edit Home Group`, klik node IT Infrastructure, `[Select]`) lalu klik `[Revoke]` pada dialog `Role Outside Constraint Will Be Revoked`
19. Tunggu aksi selesai: permintaan `[Revoke]` pada langkah 18 selesai dan dialog tertutup
20. Buka Settings > Role & Permission > Detail Role Manage group lalu buka popup Assign pada node Finance & Accounting
21. Ketik Search `Gita Permata`, tekan Enter
22. Verifikasi Gita Permata tidak muncul sebagai kandidat (empty state `No results found`)
23. Tutup popup Assign dengan `[✕]`
24. Buka Settings > Role & Permission > Tab Transaction Role > Sub-tab Disposal lalu buka popup Assign Role Transaksi (Asset Admin) pada node Finance & Accounting
25. Ketik Search `Gita Permata`, tekan Enter
26. Verifikasi Gita Permata tidak muncul sebagai kandidat popup Assign Role Transaksi (empty state `No results found`; gate Home Group yang sama, bukan penyaringan afiliasi)
27. Tutup popup Assign Role Transaksi dengan `[✕]`
28. Buka Fixed Asset > Settings > User, ganti isi kotak search dengan `Gita Permata`, tekan Enter
29. Kosongkan Home Group Gita Permata (klik ⋯, `Edit Home Group`, klik ulang node IT Infrastructure, `[Select]`)
30. Tunggu aksi selesai: permintaan `[Select]` pada langkah 29 selesai dan popup tertutup
31. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
32. Verifikasi jumlah entri `Edit Home Group` bertambah 2 dibanding baseline TC-FA-SU-317 (set Home Group beserta Revoke pada langkah 18 dan pengosongan Home Group pada langkah 29) pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
33. Buka Settings > Role & Permission > Detail Role Manage group lalu buka popup Assign pada node Finance & Accounting
34. Ketik Search `Gita Permata`, tekan Enter
35. Verifikasi Gita Permata muncul kembali sebagai kandidat
36. Tutup popup Assign dengan `[✕]`
37. Buka Settings > Role & Permission > Tab Transaction Role > Sub-tab Disposal lalu buka popup Assign Role Transaksi (Asset Admin) pada node Finance & Accounting
38. Ketik Search `Gita Permata`, tekan Enter
39. Verifikasi Gita Permata muncul kembali sebagai kandidat popup Assign Role Transaksi
40. Tutup popup Assign Role Transaksi dengan `[✕]`
41. Pulihkan Home Group, Group Role, dan Role Transaksi Gita Permata ke kondisi Pre-setup lewat seed API

### TC-FA-SU-300: Grup dihapus sebelum Select (single)

42. Buka Fixed Asset > Settings > User, ganti isi kotak search dengan `Gita Permata`, tekan Enter
43. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline TC-FA-SU-300
44. Klik ⋯ pada baris Gita Permata, klik `Edit Home Group`, dan klik node Logistics Warehouse
45. Admin B menghapus grup Logistics Warehouse melalui sesi API hingga grup terhapus
46. Klik `[Select]`
47. Verifikasi toast error "Error, failed to update home group. This group no longer exists. Please select another." tampil
48. Verifikasi pilihan dibersihkan dan popup tetap terbuka
49. Klik `[Cancel]`
50. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
51. Verifikasi jumlah entri `Edit Home Group` sama dengan baseline TC-FA-SU-300 pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
52. Pulihkan grup Logistics Warehouse lewat seed API

### TC-FA-SU-316: Grup dihapus sebelum Select (bulk)

53. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline TC-FA-SU-316
54. Centang Gita Permata
55. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
56. Centang Hana Kusuma, klik Bulk Action > `Edit Home Group`, lalu klik node Logistics Warehouse
57. Admin B menghapus grup Logistics Warehouse melalui sesi API hingga grup terhapus
58. Klik `[Select]`
59. Verifikasi toast error "Error, failed to update home group. This group no longer exists. Please select another." tampil
60. Verifikasi popup tetap terbuka dan pilihan dibersihkan
61. Klik `[Cancel]`
62. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
63. Verifikasi jumlah entri `Edit Home Group` sama dengan baseline TC-FA-SU-316 pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-302 dan TC-FA-SU-318 (tanpa penghapusan grup) diletakkan lebih dulu, lalu TC-FA-SU-317, dan TC-FA-SU-300 serta TC-FA-SU-316 (penghapusan grup) di akhir sesuai bagian 3 (aksi yang menghapus data di akhir). Pemulihan seed diperlukan antar TC karena penyimpanan Admin B dan Revoke mengubah Home Group serta Group Role.
- Pelaku kedua memakai sesi API (R-20, P-2 `[KEPUTUSAN 2026-10-30]`): tidak ada konteks UI kedua dan tidak ada butir `P-2`. TC-FA-SU-300, TC-FA-SU-302, TC-FA-SU-316, dan TC-FA-SU-318 berlabel `Manual Only — (d) dua sesi paralel`; keempatnya ditulis berurutan dengan pemicu sesi API.
- Baseline dicatat per TC dan selisih diverifikasi tepat sesudah aksi (S-12): TC-FA-SU-302 bertambah 1 entri `Edit Home Group` Gita Permata (langkah 8; penyimpanan Admin B pada langkah 4), TC-FA-SU-317 bertambah 2 (langkah 32; set Home Group beserta Revoke pada langkah 18 dan pengosongan Home Group pada langkah 29), serta TC-FA-SU-300 dan TC-FA-SU-316 tidak menambah entri (langkah 51 dan 63); pemulihan seed API tidak dihitung sebagai entri.
- Spec ini berjumlah 63 langkah dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama (Edit Home Group), berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri, baseline log per TC dengan selisih tepat sesudah aksi (S-12), Search per baris target (R-16), penutupan popup Assign (S-09), serta dua langkah menunggu aksi selesai (langkah 19 dan 30) dan tiga pemulihan seed (langkah 9, 41, 52).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1, 16, 43, dan 53 (baseline per TC), langkah 2, 10, 17, 28, 42, dan 55 (Search nama baris target sebelum membuka menu ⋯ atau mencentang, karena User List memuat 3 halaman; R-16, bagian 8b butir 9 dan 13), langkah 23, 27, 36, dan 40 (menutup popup Assign yang hanya dipakai untuk Search kandidat sebelum berpindah surface, S-09, S-03), membuka halaman lain, menutup popup dengan `[Cancel]`, serta langkah 9, 41, dan 52 (pemulihan), dan langkah 19 serta 30 (menunggu aksi `[Revoke]` dan `[Select]` selesai sebelum berpindah permukaan, bagian 8b butir 8). Search `Gita Permata` pada popup Assign adalah langkah penghubung untuk menemukan baris target (R-16); empty state `No results found` menjadi anchor positif absence.
- Temuan untuk QA (S-15): (1) TC-FA-SU-318 meminta penyimpanan "hampir bersamaan"; spec menyimpan Admin B lebih dulu lalu sesi A sehingga permintaan sesi A terakhir diterima (tidak deterministik bila benar-benar bersamaan). (2) TC-FA-SU-317 diperbarui (gate Home Group): kandidat popup Assign Role Transaksi ikut diasersi lewat Sub-tab Disposal (Asset Admin) pada node Finance & Accounting; Precondition TC-FA-SU-317 tidak memuat Pre-setup #51 padahal langkah 1 memicu dialog Revoke, sehingga spec memakai Gita Permata varian #51. TC-FA-SU-317 langkah 3 menyebut Search tanpa kolom; spec memakai Search `Gita Permata` dan hanya mengamati node Finance & Accounting (Expected "node mana pun" tidak diamati). (3) TC-FA-SU-300 dan TC-FA-SU-316 menghapus Logistics Warehouse yang merupakan Pre-setup bersama (Home Group Doni Prasetyo); pemulihan lewat seed API. (4) Post Condition TC-FA-SU-300 dan TC-FA-SU-316 (tidak ada entri baru pada tiga permukaan log) diamati lewat selisih jumlah entri terhadap baseline TC masing-masing pada tiga surface (Tab Changelog Gita Permata, Tab System Log aktor, Activity Log; langkah 51 dan 63) sebagai asersi jumlah, bukan kelas g.
