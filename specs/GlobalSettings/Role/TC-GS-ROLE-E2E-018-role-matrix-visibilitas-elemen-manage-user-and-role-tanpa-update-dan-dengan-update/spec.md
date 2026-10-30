---
id: TC-GS-ROLE-E2E-018-role-matrix-visibilitas-elemen-manage-user-and-role-tanpa-update-dan-dengan-update
title: "Role Matrix: Visibilitas Elemen Role & Permission untuk Manage user and role Tanpa Update dan Dengan Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-39
  - TC-GS-ROLE-40
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Role & Permission untuk Manage user and role Tanpa Update dan Dengan Update

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel di bawah.
- Langkah TC-GS-ROLE-39 dan TC-GS-ROLE-40 berbeda (aksi tulis tidak tersedia pada Lina Marlina, tersedia dengan guard target pada Hendra Wijaya) sehingga ditulis sebagai blok per role.

Role yang diuji (Tabel Data Uji Pre-setup #5, #7):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-39 | Manage user and role Create, Read, Delete tanpa Update | Lina Marlina | `manageUserAndRoleCreateDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRD_PASSWORD` (env baru) |
| TC-GS-ROLE-40 | Manage user and role C/R/U/D | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

Kontrol tabel (parameter perulangan langkah "Untuk setiap baris tabel Kontrol tabel"):

| No | Kontrol |
|---|---|
| 1 | Search |
| 2 | Filter |
| 3 | Sort |
| 4 | Pagination |
| 5 | header Column Visibility |

Baris Detail "Manage TAG" yang dikunci untuk Hendra Wijaya (parameter perulangan langkah 43):

| No | Nama baris | Kondisi target | Tooltip |
|---|---|---|---|
| 1 | Dewi Lestari | Total Control | "You don't have permission to edit." |
| 2 | Siti Nurhaliza | Read Only | "You don't have permission to edit." |
| 3 | Rina Putri | Read Only | "You don't have permission to edit." |
| 4 | Hendra Wijaya | diri sendiri | "You can't manage your own account from here." |
| 5 | Budi Santoso | Default User | "Default User cannot be modified." |

- Login Manage user and role Create, Read, Delete tanpa Update (role pertama) dilakukan di hook `before`; role berikutnya memakai langkah ganti akun eksplisit (logout lalu login). Karena spec berakhir di akun Hendra Wijaya, hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; env baru `GS_ROLE_MANAGE_CRD_PASSWORD` dan `GS_ROLE_MANAGE_CRUD_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup yang dibaca: Dewi Lestari (Total Control, Inactive; Pre-setup #3), Siti Nurhaliza dan Rina Putri (Read Only; Pre-setup #4, masing-masing punya baris role Manage TAG), Hendra Wijaya (Pre-setup #5, punya baris role Manage TAG), Doni Pratama dengan baris role Manage TAG (Pre-setup #10), Budi Santoso (Default User; Pre-setup #2) dengan baris role Manage TAG, Dewi Lestari dengan baris role Manage TAG, serta ≥ 11 user di Tab Total Control dan Tab Read Only (Pre-setup #17) agar Pagination tersedia. Baris role Manage TAG milik Dewi Lestari dan Budi Santoso disediakan tim FE. Spec tidak membuat, mengubah, atau menghapus data; menu row action dibuka lalu ditutup tanpa menjalankan Remove.
- Layar awal spec: Global Settings > Role & Permission (Tab Total Control) dibuka di hook `beforeEach`.
- Kemampuan teknis: hover pada checkbox dan row action disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-39: Visibilitas elemen untuk aktor Manage user and role tanpa Update

1. Verifikasi Download tampil pada Tab Total Control
2. Verifikasi Changelog tampil pada Tab Total Control
3. Verifikasi Tombol `[+ Assign]` Hidden pada Tab Total Control
4. Verifikasi row action `Remove` Hidden pada baris Dewi Lestari
5. Untuk setiap baris tabel Kontrol tabel (langkah 6):
6. Verifikasi kontrol tabel (baris tabel) aktif pada Tab Total Control
7. Klik Tab Read Only
8. Verifikasi Download tampil pada Tab Read Only
9. Verifikasi Changelog tampil pada Tab Read Only
10. Verifikasi Tombol `[+ Assign]` Hidden pada Tab Read Only
11. Verifikasi row action `Remove` Hidden pada baris Rina Putri
12. Klik Tab System
13. Verifikasi Role Name "Manage TAG" tampil dan dapat diklik
14. Klik `⋯` pada baris "Manage TAG"
15. Verifikasi row action `Detail` tampil
16. Tutup row action menu dengan Esc
17. Klik Role Name "Manage TAG" untuk membuka Detail
18. Verifikasi Tombol `[+ Assign]` Hidden pada Detail
19. Verifikasi kolom checkbox seleksi Hidden pada Detail
20. Verifikasi row action `Remove` Hidden pada baris Doni Pratama
21. Verifikasi checkbox Create, Update, dan Delete baris Doni Pratama tampil namun disabled
22. Hover checkbox Update baris Doni Pratama
23. Verifikasi tooltip "Read Only access cannot modify data."
24. Untuk setiap baris tabel Kontrol tabel (langkah 25):
25. Verifikasi kontrol tabel (baris tabel) aktif pada Detail

### TC-GS-ROLE-40: Visibilitas elemen untuk aktor Manage user and role dengan Update

26. Logout, lalu login sebagai Manage user and role C/R/U/D
27. Buka Global Settings > Role & Permission (Tab Total Control)
28. Verifikasi Tab Total Control aktif
29. Verifikasi Tombol `[+ Assign]` Hidden pada Tab Total Control
30. Verifikasi row action `Remove` Hidden pada baris Dewi Lestari
31. Klik Tab Read Only
32. Verifikasi Tab Read Only aktif
33. Verifikasi Tombol `[+ Assign]` Hidden pada Tab Read Only
34. Verifikasi row action `Remove` Hidden pada baris Siti Nurhaliza
35. Klik Tab System
36. Klik Role Name "Manage TAG" untuk membuka Detail
37. Verifikasi Tombol `[+ Assign]` tampil pada Detail
38. Hover checkbox Update baris Doni Pratama
39. Verifikasi checkbox Update baris Doni Pratama tampil dan enabled
40. Klik `⋯` pada baris Doni Pratama
41. Verifikasi row action `Remove` baris Doni Pratama tampil dan enabled
42. Tutup row action menu dengan Esc
43. Untuk setiap baris tabel Baris Detail yang dikunci (langkah 44 sampai 52):
44. Hover checkbox Update pada baris tersebut
45. Verifikasi checkbox Update baris tersebut tampil namun disabled
46. Verifikasi tooltip checkbox Update sesuai kolom Tooltip
47. Klik `⋯` pada baris tersebut
48. Verifikasi row action `Remove` baris tersebut tampil namun disabled
49. Hover row action `Remove` baris tersebut
50. Verifikasi tooltip row action `Remove` sesuai kolom Tooltip
51. Tutup row action menu dengan Esc
52. Verifikasi checkbox seleksi baris tersebut tampil namun disabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi) berupa matriks visibilitas elemen per role yang memuat polaritas tampil dan Hidden/disabled; `caseType` Positive mengikuti alur dominan (blok TC-GS-ROLE-40 memuat sebagian besar langkah dan aksi tulis tersedia, bagian 8).
- Spec melewati sekitar 35 langkah: 52 langkah nominal, sekitar 96 langkah dengan ekspansi perulangan (langkah 5 sampai 6 dan 24 sampai 25 masing-masing lima iterasi; langkah 43 sampai 52 lima iterasi). Semua langkah berada di satu kelas harness (Role Matrix, hanya baca dan tanpa data tulis); tiap blok role berdiri sendiri (login ulang di awal blok kedua) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan perulangan dipakai supaya tiap kontrol dan tiap baris punya `Verifikasi` sendiri (S-01).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup row action menu dengan Esc (langkah 16, 42, 51), klik Tab Read Only dan Tab System (langkah 7, 12, 31, 35), membuka Detail lewat Role Name (langkah 17, 36), serta logout lalu login (langkah 26 dan 27).
- Langkah 28 dan 32 (Tab aktif) bukan dari TC sumber; keduanya menjadi anchor permukaan untuk asersi Hidden pada langkah 29, 30, 33, dan 34 karena TC-GS-ROLE-40 Expected a tidak menyebut elemen yang tampil di Tab Total Control dan Tab Read Only. Pada TC-GS-ROLE-39, Download dan Changelog (langkah 1, 2, 8, 9) menjadi anchor.
- Pada Tab Total Control dan Tab Read Only, `Remove` diasersi Hidden pada baris tanpa membuka menu `⋯` (TC menyebut "overlay (⋯) baris tidak memuat Remove"); menu `⋯` baris tanpa aksi tidak tersedia.
- Asersi kontrol tabel aktif untuk TC-GS-ROLE-39 (Expected e) dijalankan pada Tab Total Control dan Detail.
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-GS-ROLE-39 Expected d menyebut checkbox Create/Update/Delete pada Detail "Manage TAG", sedangkan Detail Manage TAG hanya memiliki toggle Read dan Update (TC-GS-ROLE-32 dan TC-GS-ROLE-311); asersi langkah 21 mengikuti TC dan akan gagal pada Create dan Delete bila kolomnya memang tidak ada.
  - TC-GS-ROLE-40 Expected d sampai f menyebut "checkbox Update, Remove, dan checkbox seleksi", sedangkan PRD (§4.3 dan §4.8) menetapkan `Remove` sebagai row action `⋯`; spec memperlakukan `Remove` sebagai row action.
  - TC-GS-ROLE-40 menyebut baris Dewi Lestari (Total Control) dan Budi Santoso (Default User) di Detail "Manage TAG", sedangkan Pre-setup TC tidak menyatakan keduanya punya baris role Manage TAG; spec menuliskannya sebagai data yang disediakan tim FE.
  - TC-GS-ROLE-39 Expected e tidak menyebut surface untuk "aktif"; spec memakai Tab Total Control dan Detail.
  - TC-GS-ROLE-39 dan TC-GS-ROLE-40 tidak menyebut halaman tempat baris berada; spec mengasumsikan halaman 1 pada urutan default.
  - Pagination "aktif" di Detail "Manage TAG" mensyaratkan lebih dari 10 baris; Pre-setup TC tidak menyebut jumlah baris Manage TAG.
