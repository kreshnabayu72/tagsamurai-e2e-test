---
id: TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role
title: "Role Matrix Aksi Baris: Descendant Scope CRUD, Klik Nama oleh Read-Only/Read Saja, dan Node Excess Tanpa Edit/Add Subgroup per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-60
  - TC-FA-GRP-71
  - TC-FA-GRP-73
  - TC-FA-GRP-75
  - TC-FA-GRP-76
  - TC-FA-GRP-77
coverage:
  web: automated
---

# Role Matrix Aksi Baris: Descendant Scope CRUD, Klik Nama oleh Read-Only/Read Saja, dan Node Excess Tanpa Edit/Add Subgroup per Role

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut langkah eksplisit):

| Role | Akun (Pre-setup) | Password | TC | Blok langkah |
|---|---|---|---|---|
| Total Control | No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | TC-FA-GRP-75 | langkah 1 sampai 7 |
| Group Manager scope Region West (termasuk West Excess) | No 4 `groupManagerGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | TC-FA-GRP-76 | langkah 8 sampai 17 |
| Manage Group CRUD scope Region West (termasuk West Excess) | No 5 `manageGroupCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGCRUD_PASSWORD` | TC-FA-GRP-77, 60 | langkah 18 sampai 31 |
| Manage Group R saja scope Region West | No 6 `manageGroupRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGR_PASSWORD` | TC-FA-GRP-71 | langkah 32 sampai 38 |
| Read Only | No 3 `readOnlyGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-GRP-73 | langkah 39 sampai 46 |

- Login di hook `before` spec ini sebagai Total Control (akun default suite); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite untuk Total Control; untuk keempat akun lain disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE).
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Global HQ > Region West > Branch West 1 > Room 301 (cucu Region West), Head Office. Node `West Excess` (Excess, anak langsung Region West dalam scope Group Manager dan Manage Group CRUD) tidak ada di Tabel A; disediakan tim FE/BE sebagai fixture (node berstatus Excess; lihat Temuan untuk QA).
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak menjalankan aksi tulis dan tidak mengubah state global.

## Test Steps

### Role Total Control (TC-FA-GRP-75)

1. Klik node Region West di sidebar
2. Klik (⋯) pada baris `West Excess`
3. Verifikasi menu baris hanya memuat Detail dan Delete (Edit dan Add Subgroup tidak dirender)
4. Tutup menu dengan Esc
5. Klik (⋯) pada node `West Excess` di sidebar
6. Verifikasi menu sidebar hanya memuat Detail dan Delete (Edit dan Add Subgroup tidak dirender)
7. Tutup menu dengan Esc

### Role Group Manager (TC-FA-GRP-76)

8. Logout dari akun Total Control
9. Login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
10. Buka Fixed Asset > Settings > Groups
11. Klik node Region West di sidebar
12. Klik (⋯) pada baris `West Excess`
13. Verifikasi menu baris hanya memuat Detail dan Delete (Edit dan Add Subgroup tidak dirender)
14. Tutup menu dengan Esc
15. Klik (⋯) pada node `West Excess` di sidebar
16. Verifikasi menu sidebar hanya memuat Detail dan Delete (Edit dan Add Subgroup tidak dirender)
17. Tutup menu dengan Esc

### Role Manage Group CRUD (TC-FA-GRP-77 dan TC-FA-GRP-60)

18. Logout dari akun Group Manager
19. Login sebagai Manage Group CRUD dengan `Spectra.env.FA_MGCRUD_PASSWORD`
20. Buka Fixed Asset > Settings > Groups
21. Klik node Region West di sidebar
22. Klik (⋯) pada baris `West Excess`
23. Verifikasi menu baris hanya memuat Detail dan Delete (Edit dan Add Subgroup tidak dirender)
24. Tutup menu dengan Esc
25. Klik (⋯) pada node `West Excess` di sidebar
26. Verifikasi menu sidebar hanya memuat Detail dan Delete (Edit dan Add Subgroup tidak dirender)
27. Tutup menu dengan Esc
28. Klik node Branch West 1 di sidebar
29. Klik (⋯) pada baris Room 301
30. Verifikasi menu baris Room 301 memuat Detail, Add Subgroup, Edit, Delete (wewenang turun ke descendant)
31. Tutup menu dengan Esc

### Role Manage Group R saja (TC-FA-GRP-71)

32. Logout dari akun Manage Group CRUD
33. Login sebagai Manage Group R saja dengan `Spectra.env.FA_MGR_PASSWORD`
34. Buka Fixed Asset > Settings > Groups
35. Klik node Region West di sidebar
36. Klik nama Branch West 1 pada baris tabel
37. Verifikasi Popup Detail Group terbuka
38. Verifikasi popup bersifat read-only tanpa tombol tulis

### Role Read Only (TC-FA-GRP-73)

39. Logout dari akun Manage Group R saja
40. Login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
41. Buka Fixed Asset > Settings > Groups
42. Klik nama Head Office pada baris tabel
43. Verifikasi Popup Detail Group terbuka
44. Klik Tab Users
45. Verifikasi Tab Users tampil
46. Verifikasi popup bersifat read-only tanpa tombol tulis

## Notes

- Spec melewati sekitar 35 langkah (46 langkah): seluruh blok adalah satu kelas (Role Matrix aksi baris, hanya membaca menu dan popup tanpa aksi tulis) pada dataset Region West yang sama, tiap blok berdiri sendiri (satu role per blok), dan memisahkannya hanya menggandakan login, hook, dan cleanup.
- Langkah penghubung (S-03): langkah 1, 11, 21, 28, 35 (memilih node agar baris target tampil), langkah 4, 7, 14, 17, 24, 27, 31 (menutup menu), langkah 8 sampai 10, 18 sampai 20, 32 sampai 34, 39 sampai 41 (ganti akun eksplisit dan membuka layar).
- Urutan TC dalam spec mengikuti urutan akun agar ganti akun seminimal mungkin: 75, 76, 77, 60, 71, 73.
- Temuan untuk QA:
  - Node `West Excess` tidak ada di Tabel Data Uji Pre-setup maupun Dinamis; TC-FA-GRP-75 sampai 77 hanya menyebut "Node West Excess berstatus Excess". Spec meminta fixture dari tim FE/BE.
  - TC-FA-GRP-71 dan 73 tidak menyebut elemen yang menandai popup "read-only"; spec mengasersi tidak adanya tombol tulis dengan anchor popup yang terbuka.
  - TC-FA-GRP-73 langkah 3 ("buka Tab Users") tidak punya Expected sendiri; Expected TC hanya popup read-only dan tidak ada tombol tulis.
