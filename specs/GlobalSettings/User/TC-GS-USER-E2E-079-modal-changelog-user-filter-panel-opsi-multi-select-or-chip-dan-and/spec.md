---
id: TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Modal Changelog User: Filter Panel (Opsi Dropdown, Multi-Select per Field, Logika OR, Search Dropdown, Chip, Rentang Date, dan Logika AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-477
  - TC-GS-USER-478
  - TC-GS-USER-479
  - TC-GS-USER-480
  - TC-GS-USER-481
  - TC-GS-USER-482
  - TC-GS-USER-483
  - TC-GS-USER-484
  - TC-GS-USER-485
coverage:
  web: automated
---

# Modal Changelog User: Filter Panel (Opsi Dropdown, Multi-Select per Field, Logika OR, Search Dropdown, Chip, Rentang Date, dan Logika AND)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite: login di hook `before`, hook `after` mengembalikan sesi ke akun ini. Nama singkat di kolom Modified By: `Siti N` (tooltip `Siti Nurhaliza`). Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role, Full CRUD (Fajar Nugroho), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4); kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`. Dipakai hanya untuk memicu entri Changelog dengan Modified By kedua `Fajar N` (nama singkat dibentuk seperti `Siti N`; TC tidak menyebutnya), sehingga kolom Modified By punya sedikitnya dua nilai distinct (S-11). Tidak ada sesi UI kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Seeding minimal (S-11; lewat API di hook `before`, berurutan; kemampuan seeding user dan perubahan user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Tiap user seed diberi Position `Staff` (Tabel Data Uji Pre-setup No. 22), Division `Finance` (No. 23), dan Access `Fixed Asset` (No. 26), email `<nama>+{runId}-079@qwertysystem.net`. Kuota user plan cukup untuk user seed milik spec ini (disediakan tim FE). Hanya data yang dipakai `Verifikasi` yang di-seed; keempat kolom yang difilter punya sedikitnya dua nilai distinct):
  - U-1: Create `Alfa {runId}-079` oleh Siti Nurhaliza (Action Create, Field Name, Modified By `Siti N`), lalu Edit Position `Staff` menjadi `Supervisor` oleh Siti Nurhaliza (Action Edit, Field Position).
  - U-2: Create `Beta {runId}-079` oleh Fajar Nugroho (Action Create, Modified By `Fajar N`), lalu Deactivate oleh Siti Nurhaliza (Action Deactivate, Field Status (Global)).
  - Nilai distinct yang tersedia: Action `Create`, `Edit`, `Deactivate`; User Name `Alfa {runId}-079`, `Beta {runId}-079`; Field `Name`, `Position`, `Status (Global)`; Modified By `Siti N`, `Fajar N`. Seluruh entri seed hari uji dipakai TC-GS-USER-484.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1 dan U-2 bila masih ada; kembalikan sesi ke akun default suite. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: kontrol date range picker (memilih rentang hari uji dan rentang 1 Jan 2020 sampai 31 Jan 2020); mengetik di kolom pencarian dropdown filter; membaca seluruh entri Changelog Client (nilai distinct Action, User Name, Field, dan Modified By) sebagai pembanding opsi dropdown pada TC-GS-USER-478 (disediakan tim FE/BE; TC tidak menyebut cara); membaca warna icon Filter (gelap saat panel terbuka) dan badge titik pada icon Filter (tampil selama filter ter-Apply).
- Precondition TC-GS-USER-477 sampai 485: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); riwayat Changelog terisi.
- Suite serial (`parallel: false`). Changelog bersifat append-only dan dipakai bersama spec lain: asersi memakai pola baris (nilai bersuffix `{runId}-079`), bukan jumlah baris total, kecuali dinyatakan lain. Spec ini tidak mengubah atau menghapus data Pre-setup (S-06).
- State global yang diubah: tidak ada (Filter Panel hanya state tampilan modal).

## Test Steps

### TC-GS-USER-477: Screening Filter Panel
1. Klik icon Changelog di Table Tools
2. Klik icon Filter di modal
3. Verifikasi field `Action`: multi-select searchable dengan placeholder `All actions`
4. Verifikasi field `User Name`: multi-select searchable dengan placeholder `All users`
5. Verifikasi field `Field`: multi-select searchable dengan placeholder `All fields`
6. Verifikasi field `Modified By`: multi-select searchable dengan placeholder `All users`
7. Verifikasi field `Date`: date range picker dengan placeholder `Select date`
8. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
### TC-GS-USER-478: Opsi dropdown diambil dari nilai yang ada di tabel
9. Buka dropdown Action
10. Ketik `Creat` pada kolom pencarian dropdown Action
11. Verifikasi opsi `Create` tersedia
12. Ganti isi kolom pencarian dropdown dengan `Edit`
13. Verifikasi opsi `Edit` tersedia
14. Ganti isi kolom pencarian dropdown dengan `Deactiv`
15. Verifikasi opsi `Deactivate` tersedia
16. Ganti isi kolom pencarian dropdown dengan `Gamma {runId}-079`
17. Verifikasi tidak ada opsi tampil
18. Tutup dropdown Action
19. Buka dropdown User Name
20. Ketik `Alfa {runId}-079` pada kolom pencarian dropdown User Name
21. Verifikasi opsi `Alfa {runId}-079` tersedia
22. Ganti isi kolom pencarian dropdown dengan `Beta {runId}-079`
23. Verifikasi opsi `Beta {runId}-079` tersedia
24. Ganti isi kolom pencarian dropdown dengan `Gamma {runId}-079`
25. Verifikasi tidak ada opsi tampil
26. Tutup dropdown User Name
27. Buka dropdown Field
28. Ketik `Name` pada kolom pencarian dropdown Field
29. Verifikasi opsi `Name` tersedia
30. Ganti isi kolom pencarian dropdown dengan `Posit`
31. Verifikasi opsi `Position` tersedia
32. Ganti isi kolom pencarian dropdown dengan `Status`
33. Verifikasi opsi `Status (Global)` tersedia
34. Ganti isi kolom pencarian dropdown dengan `Gamma {runId}-079`
35. Verifikasi tidak ada opsi tampil
36. Tutup dropdown Field
37. Buka dropdown Modified By
38. Ketik `Siti N` pada kolom pencarian dropdown Modified By
39. Verifikasi opsi `Siti N` tersedia
40. Ganti isi kolom pencarian dropdown dengan `Fajar N`
41. Verifikasi opsi `Fajar N` tersedia
42. Ganti isi kolom pencarian dropdown dengan `Gamma {runId}-079`
43. Verifikasi tidak ada opsi tampil
44. Tutup dropdown Modified By dan Filter Panel
### TC-GS-USER-479: Filter multi-select per field menyaring baris
45. Klik icon Filter, pilih opsi `Edit` pada Action, klik `[Apply]`
46. Verifikasi field Action: badge titik tampil pada icon Filter
47. Verifikasi sedikitnya satu baris tampil di tabel
48. Verifikasi field Action: semua baris tampil bernilai Action `Edit`
49. Verifikasi field Action: baris Edit `Alfa {runId}-079` tampil
50. Klik icon Filter
51. Verifikasi field Action: icon Filter berubah gelap
52. Klik `[Clear Field]`, lalu klik `[Apply]`
53. Klik icon Filter, pilih opsi `Beta {runId}-079` pada User Name, klik `[Apply]`
54. Verifikasi field User Name: badge titik tampil pada icon Filter
55. Verifikasi sedikitnya satu baris tampil di tabel
56. Verifikasi field User Name: semua baris tampil bernilai User Name `Beta {runId}-079`
57. Verifikasi field User Name: baris Create `Beta {runId}-079` tampil
58. Klik icon Filter
59. Verifikasi field User Name: icon Filter berubah gelap
60. Klik `[Clear Field]`, lalu klik `[Apply]`
61. Klik icon Filter, pilih opsi `Status (Global)` pada Field, klik `[Apply]`
62. Verifikasi field Field: badge titik tampil pada icon Filter
63. Verifikasi sedikitnya satu baris tampil di tabel
64. Verifikasi field Field: semua baris tampil bernilai Field `Status (Global)`
65. Verifikasi field Field: baris Deactivate `Beta {runId}-079` tampil
66. Klik icon Filter
67. Verifikasi field Field: icon Filter berubah gelap
68. Klik `[Clear Field]`, lalu klik `[Apply]`
69. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, klik `[Apply]`
70. Verifikasi field Modified By: badge titik tampil pada icon Filter
71. Verifikasi sedikitnya satu baris tampil di tabel
72. Verifikasi field Modified By: semua baris tampil bernilai Modified By `Fajar N`
73. Verifikasi field Modified By: baris Create `Beta {runId}-079` tampil
74. Klik icon Filter
75. Verifikasi field Modified By: icon Filter berubah gelap
76. Klik `[Clear Field]`, lalu klik `[Apply]`
### TC-GS-USER-480: Dua opsi dalam satu field digabung OR
77. Klik icon Filter, pilih opsi `Create` dan `Edit` pada Action, klik `[Apply]`
78. Verifikasi baris Action `Create` (`Alfa {runId}-079`) tampil
79. Verifikasi baris Action `Edit` (`Alfa {runId}-079`) tampil
80. Verifikasi semua baris tampil bernilai Action `Create` atau `Edit`
81. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
### TC-GS-USER-481: Search di dalam dropdown filter mempersempit opsi
82. Klik icon Filter, buka dropdown Action
83. Verifikasi opsi `Create` dan `Edit` tampil sebelum mengetik
84. Ketik `CREA` pada kolom pencarian dropdown Action
85. Verifikasi opsi `Create` tampil (tersaring substring tanpa membedakan huruf besar kecil)
86. Verifikasi opsi `Edit` tidak tampil
87. Ganti isi kolom pencarian dropdown dengan `zzz`
88. Verifikasi tidak ada opsi yang cocok
89. Tutup dropdown Action
### TC-GS-USER-482: Hapus chip via (X) meng-uncheck opsi
90. Pilih opsi `Create` lalu `Edit` pada Action
91. Verifikasi chip `Create` dan `Edit` tampil
92. Klik (X) pada chip pertama (`Create`)
93. Verifikasi chip `Create` hilang
94. Verifikasi chip `Edit` tetap tampil
95. Buka dropdown Action
96. Verifikasi checkbox opsi `Create` ter-uncheck
97. Tutup dropdown Action
### TC-GS-USER-483: Uncheck opsi di dropdown menghapus chip
98. Klik `[Clear Field]`, pilih opsi `Create` lalu `Edit` pada Action
99. Buka dropdown Action, hilangkan centang opsi kedua (`Edit`)
100. Verifikasi chip `Edit` hilang
101. Verifikasi chip `Create` tetap tampil
102. Tutup dropdown Action, klik `[Clear Field]`
### TC-GS-USER-484: Filter date range
103. Pilih rentang tanggal hari uji pada Date
104. Verifikasi tanggal di input Date mengikuti Date Format General Settings
105. Klik `[Apply]`
106. Verifikasi sedikitnya satu baris tampil di tabel
107. Verifikasi semua baris tampil bertanggal dalam rentang hari uji
108. Verifikasi baris Create `Alfa {runId}-079` tampil
109. Klik icon Filter, klik `[Clear Field]`, pilih rentang tanggal 1 Jan 2020 sampai 31 Jan 2020 pada Date, klik `[Apply]`
110. Verifikasi baris di luar rentang tidak tampil (pesan `No results found`)
111. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
### TC-GS-USER-485: Kombinasi dua field filter digabung AND
112. Klik icon Filter, pilih opsi `Create` pada Action dan opsi `Fajar N` pada Modified By, klik `[Apply]`
113. Verifikasi sedikitnya satu baris tampil di tabel
114. Verifikasi semua baris tampil bernilai Action `Create` dan Modified By `Fajar N`
115. Verifikasi baris Create `Beta {runId}-079` tampil
116. Verifikasi baris Create `Alfa {runId}-079` (Modified By `Siti N`) tidak tampil
117. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Tiap `[Apply]` pada TC-GS-USER-479 diikuti `Verifikasi` badge titik pada icon Filter (Expected TC-GS-USER-479 a-d: badge titik tampil selama filter ter-Apply); `Verifikasi` icon Filter gelap hanya sesudah `Klik icon Filter` (panel terbuka). Urutan TC dalam spec mengikuti TC sumber (477 sampai 485). Screening (477) dan TC yang hanya mengamati dropdown (478) di awal; TC tanpa penyaringan data (481 sampai 483) tidak mengubah hasil tabel. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): pada TC-GS-USER-478 tiap opsi seed diasersi sesudah mengetik nama opsi pada kolom pencarian dropdown (`Creat`, `Edit`, `Deactiv`; `Alfa {runId}-079`, `Beta {runId}-079`; `Name`, `Posit`, `Status`; `Siti N`, `Fajar N`), lalu `Ganti isi kolom pencarian dropdown` ke opsi berikutnya. Sesudah anchor positif opsi seed, tiap dropdown (Action, User Name, Field, Modified By) mengetik nilai yang tidak pernah dibuat (`Gamma {runId}-079`) dan `Verifikasi tidak ada opsi tampil` (absence dengan anchor positif, bagian 8b butir 2), lalu menutup dropdown (langkah 9 sampai 44). Dropdown memuat nilai seluruh entri Changelog Client, sehingga membaca seluruh daftar opsi tanpa menyaring tidak dapat dibuktikan terhadap seed. Pencarian dropdown dianggap kembali kosong sesudah dropdown ditutup (sama seperti TC-GS-USER-481 yang menutup dropdown Action di langkah 89 lalu TC-GS-USER-482 membukanya kembali di langkah 95). `Klik icon Filter, klik [Clear Field], klik [Apply]` di akhir tiap blok yang menyaring (melepas filter sebelum blok berikutnya), serta menutup dropdown dan Filter Panel. Langkah `[Clear Field]` + `[Apply]` pada TC-GS-USER-479 adalah langkah TC.
- Langkah tambahan atas TC (S-03): `Verifikasi` baris seed tampil pada TC-GS-USER-479, 480, 484, 485 adalah anchor positif untuk asersi "semua baris" dan ketiadaan baris (bagian 8b butir 2); `Verifikasi` opsi `Create`, `Edit` tampil dan chip tampil pada TC-GS-USER-481 dan 482 adalah pembanding sebelum penyaringan dan sebelum penghapusan chip. Rentang 1 Jan 2020 sampai 31 Jan 2020 pada TC-GS-USER-484 mengasersi bahwa baris di luar rentang tidak tampil.
- Anchor positif (bagian 8b butir 2): sebelum tiap asersi "semua baris" pada TC-GS-USER-479 (Action, User Name, Field, Modified By), 484, dan 485 ada `Verifikasi sedikitnya satu baris tampil di tabel` agar asersi universal tidak lolos pada tabel kosong.
- Asersi "semua baris" membaca baris yang tampil pada halaman 1 hasil penyaringan; baris seed bersuffix `{runId}-079` dipakai sebagai anchor sehingga entri dari run atau spec lain tidak memengaruhi hasil.
- Pembagian TC Modal Changelog User: screening dan Search ada di spec 078, kombinasi Search+Filter ada di spec 080, Sort dan Pagination ada di spec 081, Setup Column ada di spec 082, Download ada di spec 083.
- Spec melewati sekitar 35 langkah (117 langkah) karena tiap field filter pada TC-GS-USER-478 dan 479 memerlukan aksi dan `Verifikasi` sendiri (S-01); semua blok satu layar (Filter Panel Modal Changelog User), satu akun aktor, dan satu dataset seed, serta tiap blok melepas filter di akhirnya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: (1) TC-GS-USER-478 "hanya nilai yang genuinely muncul di baris tabel ini" (himpunan opsi sama dengan himpunan nilai seluruh entri Changelog Client) tidak dapat dibuktikan: dropdown memuat nilai seluruh Client dan tidak ada sumber nilai pembanding di TC, PRD, atau LLD. Spec mengasersi bahwa tiap opsi seed tersedia sesudah mengetik namanya di pencarian dropdown dan bahwa nilai yang tidak pernah dibuat (`Gamma {runId}-079`) tidak menghasilkan opsi pada keempat dropdown; klausa penuh "himpunan opsi sama dengan seluruh nilai pada baris tabel" tidak diasersi. Perbaikan yang diperlukan di TC-GS-USER-478 (dan 467): rumuskan Expected relatif terhadap data seed (opsi seed tersedia dan tidak ada opsi untuk nilai yang tidak pernah dibuat), bukan terhadap himpunan seluruh entri Client. Untuk jalur TC-GS-USER-478 ini opsi Action `Create` dan `Edit` juga diasersi pada TC-GS-USER-480 dan 481. (2) TC-GS-USER-479 "icon Filter berubah gelap" tidak menyebut cara membaca warna; kemampuan membaca indikator disediakan tim FE. (3) TC-GS-USER-484 Data Uji "rentang tanggal sesuai data" tidak menyebut rentang; spec memakai rentang hari uji (berisi baris seed) dan rentang 1 Jan 2020 sampai 31 Jan 2020. (4) TC-GS-USER-485 Data Uji "2 field" tidak menyebut field dan nilainya; spec memakai Action `Create` dan Modified By `Fajar N`. (5) TC-GS-USER-478 dan 485 tidak menyebut teks opsi Modified By; spec memakai nama singkat seperti di kolom tabel (`Siti N`, `Fajar N`). (6) TC-GS-USER-481 tidak menyebut teks yang ditampilkan saat tidak ada opsi cocok; spec hanya mengasersi tidak ada opsi.
