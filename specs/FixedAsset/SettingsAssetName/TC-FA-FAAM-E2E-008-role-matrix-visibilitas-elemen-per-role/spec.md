---
id: TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Tab Asset Name per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-44
  - TC-FA-FAAM-45
  - TC-FA-FAAM-46
  - TC-FA-FAAM-47
  - TC-FA-FAAM-48
  - TC-FA-FAAM-49
  - TC-FA-FAAM-50
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tab Asset Name per Role

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Akun role lain login lewat langkah Ganti akun eksplisit (akun dan env dibaca dari tabel di bawah); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture. Semua nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; spec ini tidak memakai seed API per TC dan tidak memakai sesi API aktor.
- Role yang diuji (Pre-setup #1 s.d. #7; `{namaCompany}` = nama company uji):

| Role | Akun (Pre-setup) | Env password | `[+ Asset Name]` | Kolom checkbox seleksi | Isi menu `⋯` baris `Dell Latitude` |
|---|---|---|---|---|---|
| Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` (#1) | `Spectra.env.FA_TC_PASSWORD` | tampil dan aktif | tampil | `Detail`, `Edit`, `Delete` |
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` (#2) | `Spectra.env.FA_RO_PASSWORD` | Hidden | Hidden | `Detail` |
| Permission Read | `permissionRead_automated_{namaCompany}@qwertysystem.net` (#3) | `Spectra.env.FA_PR_PASSWORD` | Hidden | Hidden | `Detail` |
| Create-Only | `createOnly_automated_{namaCompany}@qwertysystem.net` (#4) | `Spectra.env.FA_CO_PASSWORD` | tampil dan aktif | Hidden | `Detail` |
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` (#5) | `Spectra.env.FA_UO_PASSWORD` | Hidden | Hidden | `Detail`, `Edit` |
| Delete-Only | `deleteOnly_automated_{namaCompany}@qwertysystem.net` (#6) | `Spectra.env.FA_DO_PASSWORD` | Hidden | tampil | `Detail`, `Delete` |
| Create-Delete | `createDelete_automated_{namaCompany}@qwertysystem.net` (#7) | `Spectra.env.FA_CD_PASSWORD` | tampil dan aktif | tampil | `Detail`, `Delete` |

- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10) dan `MacBook Pro` (#12) sebagai satu-satunya Asset Name Category Locked pada client utama (hitungan Needs Update 1). Baris `Dell Latitude` ditemukan lewat Search. Bulk Action Bar diamati dengan mencentang satu baris tanpa menjalankan aksi Delete.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-44: Visibilitas elemen untuk pemegang Total Control

1. Amati sidebar FAMS
2. Verifikasi item menu `Settings > Asset Master` tampil di sidebar
3. Ketik Search `Dell Latitude`, tekan Enter
4. Verifikasi tab `Asset Name` menampilkan List, Detail, Download, dan Changelog dengan state Show dan aktif (Search, Filter, Sort, Pagination, Column Visibility)
5. Verifikasi tombol `[+ Asset Name]` tampil dan aktif
6. Verifikasi kolom checkbox seleksi tampil
7. Klik icon `⋯` baris `Dell Latitude`
8. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail`, `Edit`, `Delete` saja
9. Tekan Esc untuk menutup menu `⋯`
10. Centang satu baris (`Dell Latitude`)
11. Verifikasi Bulk Action Bar tampil (hanya aksi Delete)
12. Hapus centang baris (Unselect)
13. Verifikasi Notice Category Locked `1 asset name needs a category update.` dengan aksi `Show only this` tampil di atas tabel

### TC-FA-FAAM-45: Visibilitas elemen untuk pemegang Read Only

14. Ganti akun: Logout, login sebagai Read Only (`readOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
15. Amati sidebar FAMS
16. Verifikasi item menu `Settings > Asset Master` tampil di sidebar
17. Ketik Search `Dell Latitude`, tekan Enter
18. Verifikasi tab `Asset Name` menampilkan List, Detail, Download, dan Changelog dengan state Show dan aktif (Search, Filter, Sort, Pagination, Column Visibility)
19. Verifikasi tombol `[+ Asset Name]` Hidden (tidak dirender)
20. Verifikasi kolom checkbox seleksi Hidden (tidak dirender) sehingga tidak ada baris yang dapat dicentang
21. Verifikasi Bulk Action Bar Hidden (tidak dirender)
22. Klik icon `⋯` baris `Dell Latitude`
23. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail` saja
24. Tekan Esc untuk menutup menu `⋯`
25. Verifikasi Notice Category Locked `1 asset name needs a category update.` dengan aksi `Show only this` tampil di atas tabel

### TC-FA-FAAM-46: Visibilitas elemen untuk pemegang Permission Read

26. Ganti akun: Logout, login sebagai Permission Read (`permissionRead_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_PR_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
27. Amati sidebar FAMS
28. Verifikasi item menu `Settings > Asset Master` tampil di sidebar
29. Ketik Search `Dell Latitude`, tekan Enter
30. Verifikasi tab `Asset Name` menampilkan List, Detail, Download, dan Changelog dengan state Show dan aktif (Search, Filter, Sort, Pagination, Column Visibility)
31. Verifikasi tombol `[+ Asset Name]` Hidden (tidak dirender)
32. Verifikasi kolom checkbox seleksi Hidden (tidak dirender) sehingga tidak ada baris yang dapat dicentang
33. Verifikasi Bulk Action Bar Hidden (tidak dirender)
34. Klik icon `⋯` baris `Dell Latitude`
35. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail` saja
36. Tekan Esc untuk menutup menu `⋯`
37. Verifikasi Notice Category Locked `1 asset name needs a category update.` dengan aksi `Show only this` tampil di atas tabel

### TC-FA-FAAM-47: Visibilitas elemen untuk pemegang Create-Only

38. Ganti akun: Logout, login sebagai Create-Only (`createOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_CO_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
39. Amati sidebar FAMS
40. Verifikasi item menu `Settings > Asset Master` tampil di sidebar
41. Ketik Search `Dell Latitude`, tekan Enter
42. Verifikasi tab `Asset Name` menampilkan List, Detail, Download, dan Changelog dengan state Show dan aktif (Search, Filter, Sort, Pagination, Column Visibility)
43. Verifikasi tombol `[+ Asset Name]` tampil dan aktif
44. Verifikasi kolom checkbox seleksi Hidden (tidak dirender) sehingga tidak ada baris yang dapat dicentang
45. Verifikasi Bulk Action Bar Hidden (tidak dirender)
46. Klik icon `⋯` baris `Dell Latitude`
47. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail` saja
48. Tekan Esc untuk menutup menu `⋯`
49. Verifikasi Notice Category Locked `1 asset name needs a category update.` dengan aksi `Show only this` tampil di atas tabel

### TC-FA-FAAM-48: Visibilitas elemen untuk pemegang Update-Only

50. Ganti akun: Logout, login sebagai Update-Only (`updateOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_UO_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
51. Amati sidebar FAMS
52. Verifikasi item menu `Settings > Asset Master` tampil di sidebar
53. Ketik Search `Dell Latitude`, tekan Enter
54. Verifikasi tab `Asset Name` menampilkan List, Detail, Download, dan Changelog dengan state Show dan aktif (Search, Filter, Sort, Pagination, Column Visibility)
55. Verifikasi tombol `[+ Asset Name]` Hidden (tidak dirender)
56. Verifikasi kolom checkbox seleksi Hidden (tidak dirender) sehingga tidak ada baris yang dapat dicentang
57. Verifikasi Bulk Action Bar Hidden (tidak dirender)
58. Klik icon `⋯` baris `Dell Latitude`
59. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail`, `Edit` saja
60. Tekan Esc untuk menutup menu `⋯`
61. Verifikasi Notice Category Locked `1 asset name needs a category update.` dengan aksi `Show only this` tampil di atas tabel

### TC-FA-FAAM-49: Visibilitas elemen untuk pemegang Delete-Only

62. Ganti akun: Logout, login sebagai Delete-Only (`deleteOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_DO_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
63. Amati sidebar FAMS
64. Verifikasi item menu `Settings > Asset Master` tampil di sidebar
65. Ketik Search `Dell Latitude`, tekan Enter
66. Verifikasi tab `Asset Name` menampilkan List, Detail, Download, dan Changelog dengan state Show dan aktif (Search, Filter, Sort, Pagination, Column Visibility)
67. Verifikasi tombol `[+ Asset Name]` Hidden (tidak dirender)
68. Verifikasi kolom checkbox seleksi tampil
69. Klik icon `⋯` baris `Dell Latitude`
70. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail`, `Delete` saja
71. Tekan Esc untuk menutup menu `⋯`
72. Centang satu baris (`Dell Latitude`)
73. Verifikasi Bulk Action Bar tampil (hanya aksi Delete)
74. Hapus centang baris (Unselect)
75. Verifikasi Notice Category Locked `1 asset name needs a category update.` dengan aksi `Show only this` tampil di atas tabel

### TC-FA-FAAM-50: Visibilitas elemen untuk pemegang Create-Delete

76. Ganti akun: Logout, login sebagai Create-Delete (`createDelete_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_CD_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
77. Amati sidebar FAMS
78. Verifikasi item menu `Settings > Asset Master` tampil di sidebar
79. Ketik Search `Dell Latitude`, tekan Enter
80. Verifikasi tab `Asset Name` menampilkan List, Detail, Download, dan Changelog dengan state Show dan aktif (Search, Filter, Sort, Pagination, Column Visibility)
81. Verifikasi tombol `[+ Asset Name]` tampil dan aktif
82. Verifikasi kolom checkbox seleksi tampil
83. Klik icon `⋯` baris `Dell Latitude`
84. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail`, `Delete` saja
85. Tekan Esc untuk menutup menu `⋯`
86. Centang satu baris (`Dell Latitude`)
87. Verifikasi Bulk Action Bar tampil (hanya aksi Delete)
88. Hapus centang baris (Unselect)
89. Verifikasi Notice Category Locked `1 asset name needs a category update.` dengan aksi `Show only this` tampil di atas tabel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular (satu blok per role).
- Spec Role Matrix visibilitas elemen (bagian 3a) memuat kedua polaritas (tampil dan Hidden), sehingga title tidak memuat kata "Positif" atau "Negatif".
- Spec ditulis per blok role, bukan perulangan: langkah tiap role hampir identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), dan role dengan kolom checkbox tampil (Total Control, Delete-Only, Create-Delete) memuat langkah centang dan Bulk Action Bar yang tidak dimiliki role lain (bagian 3a, keputusan 2026-10-21 dan 2026-10-30).
- Alasan spec melewati sekitar 35 langkah (89 langkah): seluruh blok memeriksa satu permukaan (tab Asset Name) dengan satu daftar elemen dan berbeda hanya akun dan hasil per role; kegagalan satu blok role tidak menghilangkan makna blok role lain. Tidak ada langkah yang diulang selain struktur blok per role (bagian 3 prinsip 13, "Alasan wajib di Notes").
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): Ganti akun pada langkah 14, 26, 38, 50, 62, 76; Search `Dell Latitude` untuk menemukan baris target (R-16) pada langkah 3, 17, 29, 41, 53, 65, 79; menutup menu `⋯` dengan Esc; mencentang dan menghapus centang baris (S-09).
- Langkah "Buka tab Asset Name" Langkah uji TC dilakukan oleh hook `beforeEach` untuk Total Control dan oleh langkah Ganti akun untuk role lain.
- Asersi `Hidden` (tombol `[+ Asset Name]`, checkbox, Bulk Action Bar, aksi menu) memakai Verifikasi tab `Asset Name` pada tiap blok sebagai anchor permukaan (bagian 8b butir 2 dan 11); menu `⋯` memuat `Detail` (dan item lain) dalam satu `Verifikasi` yang berisi daftar utuh sehingga anchor positif ikut diasersi.
- Temuan untuk QA:
  - TC-45 sampai TC-50 Expected f menyebut Notice Category Locked tampil bagi semua role, tetapi Langkah uji tidak menyebut klik `Show only this`; spec mengasersi hanya tampilnya notice dan aksinya.
  - TC-44, TC-49, dan TC-50 Langkah 4 "Centang satu baris" tidak menyebut baris yang dicentang; spec mencentang baris `Dell Latitude` yang sudah ditemukan lewat Search, lalu menghapus centang.
