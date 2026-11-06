---
id: TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user
title: "Role Matrix Positif Create: Add Subgroup oleh Manage Group R+C dan Group Manager, [+] Group oleh Default User, Auto-Assign Creator"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-64
  - TC-FA-GRP-68
  - TC-FA-GRP-72
  - TC-FA-GRP-132
  - TC-FA-GRP-890
coverage:
  web: automated
---

# Role Matrix Positif Create: Add Subgroup oleh Manage Group R+C dan Group Manager, [+] Group oleh Default User, Auto-Assign Creator

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec ditulis per blok role karena langkah tiap role berbeda):

| Role | Akun (Pre-setup) | Password | Blok langkah |
|---|---|---|---|
| Manage Group R+C scope Region West (TC-FA-GRP-64, 132, 890) | No 6 `manageGroupCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRC_PASSWORD` | langkah 1 sampai 41 |
| Group Manager scope Region West (TC-FA-GRP-68) | No 4 `groupManagerGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | langkah 42 sampai 58 |
| Default User (TC-FA-GRP-72) | No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` | langkah 59 sampai 66 |

- Login di hook `before` spec ini sebagai Manage Group R+C; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk ketiga akun disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); hook suite hanya menyetel akun aktor default suite.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9): Global HQ > Region West > Branch West 1 > Room 301. Region West tercakup penugasan Group Manager user D, yaitu Pre-setup No 4 (akun yang sama dengan aktor TC-FA-GRP-68), dengan baris pola GM sudah terbentuk di Region West (precondition TC-FA-GRP-132, 890, dan 68); penugasan dan baris pola itu disediakan tim FE/BE tanpa endpoint karangan.
- Data Dinamis (dibuat oleh langkah spec, dihapus di hook `after` lewat API):

| TC | Nama TC | Nama dibuat | Induk |
|---|---|---|---|
| TC-FA-GRP-64 | West Annex | `West Annex {runId}-020` | Region West |
| TC-FA-GRP-132 | West Lab | `West Lab {runId}-020` | Region West |
| TC-FA-GRP-890 | West Log | `West Log {runId}-020` | Region West |
| TC-FA-GRP-68 | node baru di bawah Room 301 (nama tidak disebut TC) | `Room Child {runId}-020` | Room 301 |
| TC-FA-GRP-72 | DU Root | `DU Root {runId}-020` | level 1 |

- Kemampuan teknis: fixture BE (membaca assignment Manage Group aktor, menghapus data milik spec), kemampuan membaca assignment (tab Group Role dan Transaction Role) dan log modul Role & Permission, kemampuan membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11), dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Penerima notifikasi yang diamati pada TC-FA-GRP-890 dan TC-FA-GRP-68 (aktor Group Manager, user D) serta user pembaca baris pola pada TC-FA-GRP-132 (hanya dibaca): Default User No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net` dan Read Only No 3 `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Role Manage Group R+C (TC-FA-GRP-64)

1. Klik (⋯) pada node Region West di sidebar
2. Klik `Add Subgroup`
3. Isi Group Name `West Annex {runId}-020`
4. Klik [Submit]
5. Verifikasi toast sukses `Success, group has been created.`
6. Klik chevron node Region West untuk expand
7. Verifikasi `West Annex {runId}-020` muncul di bawah Region West
8. Verifikasi aktor mendapat auto-assign Manage Group CRUD di `West Annex {runId}-020` sesuai pembacaan fixture BE

### Role Manage Group R+C (TC-FA-GRP-132)

9. Klik (⋯) pada node Region West di sidebar
10. Klik `Add Subgroup`
11. Isi Group Name `West Lab {runId}-020`
12. Klik [Submit]
13. Verifikasi toast sukses `Success, group has been created.`
14. Klik (⋯) pada node `West Lab {runId}-020` di sidebar
15. Verifikasi menu memuat Detail, Add Subgroup, Edit, Delete (CRUD penuh walau di parent hanya R+C)
16. Tutup menu dengan Esc
17. Baca assignment Manage Group aktor pada `West Lab {runId}-020` lewat kemampuan baca modul Role & Permission
18. Verifikasi assignment Manage Group C/R/U/D aktor di `West Lab {runId}-020` tercatat
19. Baca tab Group Role pada `West Lab {runId}-020` untuk user Total Control (Pre-setup No 1 dan Default User) dan Read Only (Pre-setup No 3) lewat kemampuan baca modul Role & Permission
20. Verifikasi baris pola Group Role terbentuk di `West Lab {runId}-020` untuk setiap user Total Control (termasuk Default User) dengan seluruh baris Group Role CRUD penuh
21. Verifikasi baris pola Group Role terbentuk di `West Lab {runId}-020` untuk setiap user Read Only dengan seluruh baris Group Role Read saja
22. Baca tab Group Role dan tab Transaction Role user D (Pre-setup No 4 `groupManagerGroups_automated_{namaCompany}@qwertysystem.net`) pada `West Lab {runId}-020` lewat kemampuan baca modul Role & Permission
23. Verifikasi baris pola GM terbentuk di `West Lab {runId}-020` untuk user D dengan seluruh Group Role katalog kecuali `Manage user & role` dengan CRUD penuh sesuai kolom yang berlaku
24. Verifikasi baris pola GM user D di `West Lab {runId}-020` memuat `Asset Admin` dan `Approver` pada setiap Jenis Transaksi
25. Verifikasi baris pola GM user D sudah terbentuk pada pembacaan pertama sesudah toast sukses Create (dalam transaksi atomik yang sama dengan Create)

### Role Manage Group R+C (TC-FA-GRP-890)

26. Catat baseline sebelum pemicu: jumlah notifikasi in-app tiap penerima (Default User dan Read Only)
27. Klik (⋯) pada node Region West di sidebar
28. Klik `Add Subgroup`
29. Isi Group Name `West Log {runId}-020`
30. Klik [Submit]
31. Tunggu aksi selesai (modal Add Subgroup tertutup)
32. Tunggu 5 detik tanpa memuat ulang halaman
33. Verifikasi jumlah notifikasi in-app tiap penerima sama dengan baseline langkah 26
34. Baca log modul Role & Permission lewat kemampuan baca log
35. Verifikasi Role & Permission mencatat assignment Manage Group aktor ke `West Log {runId}-020`
36. Verifikasi log Role & Permission memuat satu entri `Assign` per assignment hasil salinan dari Region West ke `West Log {runId}-020`, per baris Group Role dan per baris Transaction Role, termasuk baris pola Group Role dan Transaction Role Total Control/Read Only serta baris pola GM user D
37. Verifikasi Action entri hasil salinan tersebut adalah `Assign` biasa (bukan `Assign (via Group Manager)`) dan Modified By adalah aktor pembuat Subgroup (format `[First Name] [Last Initial]`)
38. Klik ikon `Changelog`
39. Ketik Search `West Log {runId}-020`, tekan Enter
40. Verifikasi Changelog: Group hanya memuat satu baris untuk `West Log {runId}-020`, yaitu baris Create
41. Tutup Modal Changelog dengan ✕

### Role Group Manager (TC-FA-GRP-68)

42. Logout dari akun Manage Group R+C
43. Login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
44. Buka Fixed Asset > Settings > Groups
45. Klik toggle expand-all pada sidebar
46. Catat baseline sebelum pemicu: jumlah notifikasi in-app aktor Group Manager
47. Klik (⋯) pada node Room 301 di sidebar
48. Klik `Add Subgroup`
49. Isi Group Name `Room Child {runId}-020`
50. Klik [Submit]
51. Verifikasi toast sukses `Success, group has been created.`
52. Verifikasi `Room Child {runId}-020` muncul sebagai node baru di bawah Room 301 pada sidebar
53. Baca tab Group Role dan tab Transaction Role aktor Group Manager pada `Room Child {runId}-020` lewat kemampuan baca modul Role & Permission
54. Verifikasi aktor Group Manager memiliki baris pola GM pada `Room Child {runId}-020` karena penugasannya mencakup Room 301
55. Baca log modul Role & Permission untuk `Room Child {runId}-020` lewat kemampuan baca log
56. Verifikasi Modified By entri `Assign` baris pola GM pada `Room Child {runId}-020` adalah aktor Group Manager (format `[First Name] [Last Initial]`)
57. Tunggu 5 detik tanpa memuat ulang halaman
58. Verifikasi jumlah notifikasi in-app aktor Group Manager sama dengan baseline langkah 46

### Role Default User (TC-FA-GRP-72)

59. Logout dari akun Group Manager
60. Login sebagai Default User dengan `Spectra.env.FA_DU_PASSWORD`
61. Buka Fixed Asset > Settings > Groups
62. Klik [+] Group
63. Isi Group Name `DU Root {runId}-020`
64. Klik [Submit]
65. Verifikasi toast sukses `Success, group has been created.`
66. Verifikasi aktor tidak mendapat auto-assign creator pada `DU Root {runId}-020` sesuai pembacaan fixture BE (node `DU Root {runId}-020` tampil di sidebar)

## Notes

- Spec melewati sekitar 35 langkah (66 langkah): seluruh blok adalah satu kelas (Role Matrix positif Create) pada dataset Region West yang sama, tiap blok berdiri sendiri (satu role per blok, data dibuat dan dihapus sendiri), dan memisahkannya hanya menggandakan login, hook, dan cleanup.
- Spec ditulis per blok role karena langkah tiap role berbeda (aksi dan target berbeda) dan ganti akun menuntut langkah eksplisit (bagian 3a).
- Langkah penghubung (S-03): langkah 6 (expand Region West), langkah 16 (menutup menu), langkah 19, 22, 26, 34, 46, 53, dan 55 (pembacaan baris pola, baseline notifikasi, dan log lewat kemampuan baca), langkah 31 (tunggu aksi selesai, 8b butir 8), langkah 32 dan 57 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11), langkah 39 (Search di Modal Changelog untuk menemukan baris target, R-16), langkah 41 (menutup modal), langkah 42 sampai 44 dan 59 sampai 61 (ganti akun eksplisit), langkah 45 (expand-all).
- Pembagian TC lintas spec: Role Matrix positif Edit ada di spec 021, Delete di spec 022.
- P-1 (asersi absence di spec asal): asersi tanpa notifikasi in-app pada TC-890 (langkah 32 dan 33) berasal dari aksi Add Subgroup yang sama dengan aksi TC-890 dan memakai baseline sendiri (langkah 26); aksi itu juga membentuk salinan assignment yang diasersi langkah 36 dan 37, sehingga asersi tidak dipindah ke spec absence. Hal yang sama berlaku untuk asersi tanpa notifikasi in-app aktor Group Manager pada TC-68 (langkah 57 dan 58, baseline langkah 46): aksi Add Subgroup di bawah Room 301 yang sama juga membentuk baris pola GM yang diasersi langkah 54 dan 56. Alur lengkap Create Subgroup oleh GM di descendant ada di spec 291 dan spec 292.
- Temuan untuk QA:
  - TC-FA-GRP-132 dan 890 meminta pembacaan Settings > Role & Permission oleh aktor R+C yang tidak jelas berhak mengakses modul itu; spec memakai kemampuan baca assignment dan log yang disediakan tim FE/BE.
  - Post Condition TC-FA-GRP-132 ("Total User West Lab mencakup aktor, user B, user C, dan user D") tidak punya langkah observasi di TC sehingga tidak diasersi; pengaruh baris pola GM pada Total User masih NC-12 (Menunggu konfirmasi, PRD FAGRP-LOGIC-03k).
  - TC-FA-GRP-132 Expected f menyebut baris pola Group Role terbentuk "dalam transaksi atomik yang sama dengan Create"; atomisitas tidak teramati dari UI sehingga spec mengasersi hasilnya (langkah 20 dan 21, dan langkah 25 untuk baris pola GM user D).
  - TC-FA-GRP-68 tidak menyebut nama node baru dan TC-FA-GRP-72 tidak menyebut cara cek "tanpa auto-assign creator"; spec memakai nama bersuffix dan pembacaan fixture BE.
  - TC-FA-GRP-132 Pre c dan TC-FA-GRP-68 memakai user D (Pre-setup No 4) dengan penugasan GM yang mencakup Region West dan baris pola GM "sudah terbentuk" tanpa mekanisme seeding yang ditegaskan di TC; spec menuliskannya sebagai kemampuan tim FE/BE tanpa endpoint karangan.
  - TC-FA-GRP-68 Expected c ("tanpa notifikasi") tidak menyebut cara membuka notifikasi in-app aktor Group Manager; spec memakai kemampuan baca jumlah notifikasi per penerima.
