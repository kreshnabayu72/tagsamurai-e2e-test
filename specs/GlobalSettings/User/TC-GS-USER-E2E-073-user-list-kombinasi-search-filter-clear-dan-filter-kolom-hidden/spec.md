---
id: TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "User List: Kombinasi Search dan Filter (Irisan, Clear dengan Sort Aktif, Filter Kolom Hidden, Nol Baris, Custom Field, dan Create Tidak Cocok Filter)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-430
  - TC-GS-USER-431
  - TC-GS-USER-432
  - TC-GS-USER-433
  - TC-GS-USER-434
  - TC-GS-USER-463
  - TC-GS-USER-464
coverage:
  web: automated
---

# User List: Kombinasi Search dan Filter (Irisan, Clear dengan Sort Aktif, Filter Kolom Hidden, Nol Baris, Custom Field, dan Create Tidak Cocok Filter)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan Master Data No. 22-23, Custom Field aktif No. 24, hanya dibaca): Division `Finance` dan `Logistics`, Custom Field `Blood Type` (Dropdown) dan `Emergency Phone` (Phone, Required).
- Data Dinamis, di-seed lewat API di hook `before`. Kemampuan seeding user lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD). Field wajib yang bukan objek uji: Access sesuai tabel, Division sesuai tabel, dan Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) dengan Country Code `🇮🇩 +62` dan Number `81234567890`.
  - U-1: Name `Indra Wibowo {runId}-073`, Email `indrawibowo+{runId}-073@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`.
  - U-2: Name `Indra Saputra {runId}-073`, Email `indrasaputra+{runId}-073@qwertysystem.net`, Division `Logistics`, Access `Fixed Asset`.
  - U-3: Name `Kirana Dewanti {runId}-073`, Email `kiranadewanti+{runId}-073@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`.
  - Seeding minimal (S-11): U-1 dan U-2 sama-sama memuat `Indra` dengan Division berbeda (irisan Search dan Filter); U-3 memuat Division `Finance` tanpa `Indra` (dikecualikan oleh Search). Nama U-1 dan U-2 membuat urutan Name ascending (Saputra, Wibowo) berbeda dari urutan Division ascending (Finance, Logistics) pada TC-GS-USER-432.
  - U-4 dibuat lewat UI oleh spec (TC-GS-USER-464): Name `Lukas Budiman {runId}-073`, Email `lukasbudiman+{runId}-073@qwertysystem.net`, Division `Logistics`, Access `Fixed Asset`, Emergency Phone sama dengan seed. Dihapus di hook `after` lewat API menurut Email.
  - Cleanup di hook `after` (tidak berasumsi seeding atau Create berhasil penuh): hapus U-1 sampai U-4 lewat API.
- State yang diubah dan dipulihkan: ukuran halaman 100 (langkah 1) dikembalikan ke 10 (langkah 88); Search ditutup di langkah 10, 31, dan 60, dan Filter dikosongkan lewat `[Clear Field]` di langkah 12, 23, 43, 57, 70, dan 85; sort Division dikembalikan ke default (langkah 31 dan sesudahnya); kolom `Division` di-hide lalu dicentang kembali (TC-GS-USER-433); kolom `Blood Type` dicentang lewat Setup Column lalu dihilangkan lewat Overlay (TC-GS-USER-463). Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (Setup Column > `[Reset to Default]`, `[Save]`, atau penghapusan preferensi kolom User List di browser; mekanisme disediakan tim FE/BE).
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: mengisi field Phone Custom Field (Country Code dan Number) pada modal Create; membaca state sort pada header kolom.

## Test Steps

### Persiapan tampilan

1. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-430: Search lalu Filter menghasilkan irisan

2. Klik icon Search, ketik `Indra`, tekan Enter
3. Klik icon Filter
4. Pilih opsi `Finance` pada Division
5. Klik `[Apply]`
6. Verifikasi hasil adalah irisan Search dan Filter: baris `Indra Wibowo {runId}-073` (nama memuat `Indra`, Division `Finance`) tampil
7. Verifikasi baris `Indra Saputra {runId}-073` (nama memuat `Indra`, Division `Logistics`) tidak tampil
8. Verifikasi baris `Kirana Dewanti {runId}-073` (Division `Finance`, nama tidak memuat `Indra`) tidak tampil
9. Verifikasi keyword di kotak Search tidak ter-reset: tetap `Indra`
10. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
11. Klik icon Filter
12. Klik `[Clear Field]`
13. Klik `[Apply]`

### TC-GS-USER-431: Filter lalu Search menghasilkan irisan

14. Klik icon Filter
15. Pilih opsi `Finance` pada Division
16. Klik `[Apply]`
17. Klik icon Search, ketik `Indra`, tekan Enter
18. Verifikasi hasil adalah irisan Filter dan Search: baris `Indra Wibowo {runId}-073` tampil
19. Verifikasi baris `Indra Saputra {runId}-073` tidak tampil
20. Verifikasi baris `Kirana Dewanti {runId}-073` tidak tampil

### TC-GS-USER-432: Clear filter saat Search dan Sort aktif

21. Klik header Division
22. Klik icon Filter
23. Klik `[Clear Field]`
24. Klik `[Apply]`
25. Verifikasi kotak Search tetap berisi `Indra`
26. Verifikasi sort Division ascending tetap aktif
27. Verifikasi urutan mengikuti sort Division ascending: baris `Indra Wibowo {runId}-073` (Finance) berada di atas baris `Indra Saputra {runId}-073` (Logistics)
28. Verifikasi Filter terlepas: baris `Indra Saputra {runId}-073` (Logistics) tampil kembali
29. Klik header Division
30. Klik header Division
31. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-433: Filter tetap tersedia untuk kolom yang di-hide

32. Klik icon Filter
33. Pilih opsi `Finance` pada Division
34. Klik `[Apply]`
35. Klik header kolom Column Visibility (⋯)
36. Hilangkan centang `Division`
37. Tekan Esc untuk menutup Overlay Column Visibility
38. Verifikasi kolom `Division` tidak tampil di tabel
39. Verifikasi Filter tetap aktif menyaring: baris `Indra Wibowo {runId}-073` dan baris `Kirana Dewanti {runId}-073` (Division `Finance`) tampil
40. Verifikasi Filter tetap aktif menyaring: baris `Indra Saputra {runId}-073` (Division `Logistics`) tidak tampil
41. Klik icon Filter
42. Verifikasi field filter `Division` tetap ada di Filter Panel
43. Klik `[Clear Field]`
44. Klik `[Apply]`
45. Klik header kolom Column Visibility (⋯)
46. Centang `Division`
47. Tekan Esc untuk menutup Overlay Column Visibility

### TC-GS-USER-434: Kombinasi Search + Filter menghasilkan 0 baris lalu pulih saat salah satu dilepas

48. Klik icon Search, ketik `Kirana`, tekan Enter
49. Verifikasi baris `Kirana Dewanti {runId}-073` tampil
50. Klik icon Filter
51. Pilih opsi `Logistics` pada Division
52. Klik `[Apply]`
53. Verifikasi tabel menampilkan ilustrasi no result
54. Verifikasi tabel menampilkan teks `No results found`
55. Verifikasi tabel menampilkan teks `Try adjusting your search or filter.`
56. Klik icon Filter
57. Klik `[Clear Field]`
58. Klik `[Apply]`
59. Verifikasi setelah filter dilepas: baris hasil search `Kirana Dewanti {runId}-073` tampil kembali
60. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-463: Custom Field aktif muncul sebagai kolom curated dan filter sesuai tipe

61. Klik header kolom Column Visibility (⋯)
62. Klik `Setup Column...`
63. Centang `Blood Type`
64. Klik `[Save]`
65. Verifikasi kolom `Blood Type` tampil di tabel
66. Klik icon Filter
67. Verifikasi filter `Blood Type` tersedia di Filter Panel
68. Verifikasi filter `Blood Type` bertipe multi-select
69. Verifikasi filter `Blood Type` memiliki placeholder `All blood types`
70. Klik `[Clear Field]`
71. Klik `[Apply]`
72. Klik header kolom Column Visibility (⋯)
73. Hilangkan centang `Blood Type`
74. Tekan Esc untuk menutup Overlay Column Visibility

### TC-GS-USER-464: Create user yang tidak cocok filter aktif tidak muncul di tabel terfilter

75. Klik icon Filter
76. Pilih opsi `Finance` pada Division
77. Klik `[Apply]`
78. Verifikasi baris `Indra Wibowo {runId}-073` (Division `Finance`) tampil
79. Klik `[+ User]` di Table Tools
80. Isi First Name `Lukas`, Last Name `Budiman {runId}-073`, Division `Logistics`, Email `lukasbudiman+{runId}-073@qwertysystem.net`, centang Access `Fixed Asset`, isi Emergency Phone dengan Country Code `🇮🇩 +62` dan Number `81234567890`
81. Klik `[Submit]`
82. Verifikasi toast sukses: "Success, user has been created."
83. Verifikasi user baru `Lukas Budiman {runId}-073` tidak tampil di tabel selama filter Division `Finance` aktif
84. Klik icon Filter
85. Klik `[Clear Field]`
86. Klik `[Apply]`
87. Verifikasi setelah filter dilepas: baris `Lukas Budiman {runId}-073` tampil di tabel (user baru memang tercipta)

### Pemulihan state

88. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Urutan TC sumber (430, 431, 432, 433, 434, 463, 464) dipertahankan; TC-GS-USER-464 (membuat data) berada paling akhir.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 agar baris seed berada di halaman yang sama); sesudah tiap blok: menutup Search lewat `(←)` dan mengosongkan Filter lewat `Klik icon Filter`, `Klik [Clear Field]`, `Klik [Apply]` (S-09); langkah 29 sampai 30 (dua klik header Division mengembalikan sort ke default); `Klik [Clear Field]`, `Klik [Apply]` dan pencentangan kembali `Division` pada TC-GS-USER-433; pembersihan Filter dan penghilangan centang `Blood Type` pada TC-GS-USER-463; langkah 88 (ukuran halaman 10).
- Langkah 1 TC-GS-USER-432 ("Search keyword, Enter") dipenuhi state Search `Indra` dari TC-GS-USER-431; "Terapkan filter" dipenuhi Filter `Division = Finance` dari TC-GS-USER-431, sehingga hanya sort (Division) dan pengosongan Filter yang ditulis ulang.
- Asersi tambahan (S-03, dicatat alasannya): TC-GS-USER-433 memuat `Verifikasi` kolom `Division` tidak tampil sebagai anchor bahwa aksi hide berhasil sebelum Filter diasersi; TC-GS-USER-464 memuat `Verifikasi` toast sukses dan `Verifikasi` user baru tampil sesudah Filter dilepas sebagai anchor positif bahwa user tercipta (8b butir 2); TC-GS-USER-432 memuat `Verifikasi` urutan Division ascending supaya arah sort teramati (urutan Name ascending berbeda); TC-GS-USER-431 dan 430 memuat `Verifikasi` baris U-3 tidak tampil supaya irisan (bukan hanya Search atau Filter) teramati.
- Label menu Setup Column: TC-GS-USER-463 menyebut "Buka Setup Column" tanpa label; spec memakai item `Setup Column...` di Overlay Column Visibility sesuai TC-GS-USER-441 dan 442.
- Spec melewati sekitar 35 langkah karena tujuh TC kombinasi berbagi satu layar dan satu dataset (U-1 sampai U-3) dan satu kelas harness (fungsional). Blok Search dan Filter (TC-GS-USER-430 sampai 434) berdiri sendiri dan dikembalikan ke keadaan bersih di akhir tiap blok; TC-GS-USER-463 dan 464 memakai layar yang sama. Satu-satunya aksi yang membuat data (TC-GS-USER-464) ditaruh paling akhir dan dihapus di `after`.
- Pembagian TC lintas spec: Search di spec 071; Filter Panel (opsi, OR, AND, rentang) di spec 072; Sort, Pagination, dan kombinasi empat kontrol di spec 074; Setup Column di spec 075; Download di spec 076 dan 077.
- Temuan untuk QA:
  - TC-GS-USER-463: placeholder filter Custom Field ditulis `All [plural noun]` tanpa nilai literal. Spec mengasersi `All blood types` (turunan dari label `Blood Type`); QA perlu menetapkan bentuk jamak yang benar.
  - TC-GS-USER-464: TC tidak menyebut field wajib lain pada Create; spec mengisi Emergency Phone karena Custom Field itu Required (Tabel Pre-setup No. 24). TC juga tidak menyebut cara memastikan user tercipta; spec menambahkan anchor (lihat butir asersi tambahan).
  - TC-GS-USER-432: TC tidak menyebut kolom yang di-sort; spec memilih Division karena urutannya berbeda dari urutan default Name.
  - TC-GS-USER-430 sampai 434: keyword dan opsi filter tidak disebut konkret di TC (hanya "keyword", "terapkan filter"); spec memakai `Indra`, `Kirana`, dan Division `Finance`/`Logistics` dari data seed.
