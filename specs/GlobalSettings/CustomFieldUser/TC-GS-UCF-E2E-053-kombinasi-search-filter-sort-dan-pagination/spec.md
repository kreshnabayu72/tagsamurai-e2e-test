---
id: TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination
title: "Kombinasi Search, Filter, Sort, dan Pagination Tabel Custom Field: Irisan, Clear, Empty State, Reset Halaman, dan Perubahan Data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-214
  - TC-GS-UCF-215
  - TC-GS-UCF-216
  - TC-GS-UCF-217
  - TC-GS-UCF-505
  - TC-GS-UCF-506
  - TC-GS-UCF-507
  - TC-GS-UCF-218
  - TC-GS-UCF-219
  - TC-GS-UCF-220
  - TC-GS-UCF-504
  - TC-GS-UCF-231
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination Tabel Custom Field: Irisan, Clear, Empty State, Reset Halaman, dan Perubahan Data

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`):
  - `Cost Center`: Dropdown; Placeholder `Select cost center`; Required Yes; Active; Modified By `Budi S`.
  - `Employee Grade`: Text; Required No; Active; `Siti R`.
  - `Job Description`: Text Area; Required No; Active; `Siti R`.
  - `Bonus`: Numeric; Required No; Active; `Budi S`.
  - `Office Phone`: Phone; Placeholder `Enter phone number`; Required Yes; Active; `Budi S`.
  - `Joining Date`: Date; Required No; Inactive; `Budi S`.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type` (Dropdown), `Shirt Size` (Dropdown), `Emergency Phone` (Phone), `Birth Date` (Date), `Tax ID` (Text; Placeholder `Enter tax ID number`; Required Yes), `Work Notes` (Text Area), `Annual Target` (Numeric), `badge number` (Text); Required No kecuali `Tax ID`; Active; Modified By `Sari D`. Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme disediakan tim FE/BE, endpoint tidak ditulis di spec). Nama literal tanpa suffix karena asersi urutan, jumlah 14 baris, dan kata kunci Search bergantung pada nama (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini. Total Custom Field Client A tepat 14 saat TC-GS-UCF-214 sampai 219 dan 231 berjalan (halaman 1 berisi 10 baris dan halaman 2 berisi 4 baris pada ukuran halaman 10).
- Data Dinamis milik spec (nama bersuffix per run; fixture baru `Fixture.customFieldUser.combinedSeed053`): `Filter Mut {runId}-053` (Text; dibuat lewat UI pada TC-GS-UCF-220) dan `Edit Hide Probe {runId}-053` (D-234: Text; Placeholder kosong; di-seed lewat API oleh akun Total Control Client A pada langkah yang menyebutnya, lalu di-rename menjadi `Visible Probe {runId}-053` oleh TC-GS-UCF-504). Keduanya dibuat sesudah TC lain agar total 14 baris tidak berubah untuk TC sebelumnya.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`. Klik sidebar mereset Search, Sort, dan Filter, sehingga pemulihan state ditulis eksplisit sebagai langkah penghubung.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Filter Mut {runId}-053`, `Edit Hide Probe {runId}-053` atau `Visible Probe {runId}-053` (record yang sama), dan field Population yang dibuat hook `before`; pulihkan preferensi visibilitas, urutan, dan pin kolom tabel utama ke default (8 kolom terlihat) dan ukuran halaman ke 10.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pembacaan indikator sort pada header, urutan baris, nilai Search, chip Filter Panel, indikator titik ikon Filter, halaman aktif, dan ukuran halaman; membuka Overlay Column Visibility dan Modal Setup Column.
- State global: ukuran halaman diubah ke 25 oleh TC-GS-UCF-216 (langkah 21) dan dikembalikan ke 10 (langkah 105 dan 122); visibilitas kolom Data Type disembunyikan lalu dipulihkan oleh TC-GS-UCF-219 (langkah 99 dan 104). Search, Filter, dan Sort dipulihkan lewat langkah penghubung di akhir tiap blok.

## Test Steps

### TC-GS-UCF-214: Search lalu Filter menghasilkan irisan

1. Ketik Search `phone`, tekan Enter
2. Klik Filter
3. Pilih Required `Yes`, klik [Apply]
4. Klik icon Filter untuk menutup panel
5. Verifikasi tabel menampilkan tepat satu baris `Office Phone`
6. Verifikasi baris `Emergency Phone` tidak tampil (Required No)
7. Verifikasi keyword `phone` tetap terisi
8. Klik `(←)`
9. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-215: Filter lalu Search menghasilkan irisan yang sama

10. Klik Filter
11. Pilih Required `Yes`, klik [Apply]
12. Klik icon Filter untuk menutup panel
13. Ketik Search `phone`, tekan Enter
14. Verifikasi tabel menampilkan tepat satu baris `Office Phone` (identik dengan urutan Search lalu Filter)
15. Verifikasi icon Filter menampilkan indikator filter aktif
16. Klik `(←)`
17. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-216: Kombinasi Search, Filter, Sort, dan page size

18. Ketik Search `phone`, tekan Enter
19. Klik Filter, pilih Required `No`, klik [Apply], lalu klik icon Filter untuk menutup panel
20. Klik header Field Name dua kali (descending)
21. Ubah ukuran halaman tabel ke 25
22. Verifikasi tabel menampilkan tepat satu baris `Emergency Phone` (nama memuat `phone` dan Required No)
23. Verifikasi keyword `phone` tetap terisi
24. Verifikasi icon Filter menampilkan indikator filter aktif
25. Verifikasi indikator sort descending aktif pada header Field Name
26. Klik header Field Name sekali lagi (sort kembali netral)
27. Klik `(←)`
28. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-217: Pelepasan Search dan Filter saling independen serta pemulihan empty state

29. Ketik Search `phone`, tekan Enter
30. Klik Filter, pilih Data Type `Text`, klik [Apply], lalu klik icon Filter untuk menutup panel
31. Verifikasi empty state "No results found" tampil (Search `phone` dan filter Text tidak beririsan)
32. Klik `✕` pada Search, tekan Enter
33. Verifikasi tabel menampilkan tepat tiga baris: `badge number`, `Employee Grade`, dan `Tax ID` (filter Text tetap aktif)
34. Ketik Search `zzqx`, tekan Enter
35. Verifikasi empty state "No results found" tampil (Search `zzqx` dan filter Text)
36. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel
37. Verifikasi Search `zzqx` tetap terisi
38. Verifikasi tabel tetap menampilkan empty state "No results found"
39. Klik `✕` pada Search, tekan Enter
40. Verifikasi tabel kembali menampilkan 14 baris
41. Klik `(←)`

### TC-GS-UCF-505: Search dengan dua field Filter menghasilkan irisan ketiganya

42. Ketik Search `number`, tekan Enter
43. Verifikasi tabel menampilkan tepat empat baris: `badge number`, `Emergency Phone`, `Office Phone`, dan `Tax ID`
44. Klik Filter
45. Pilih Data Type `Phone`, klik [Apply]
46. Verifikasi tabel menampilkan tepat dua baris: `Emergency Phone` dan `Office Phone`
47. Verifikasi baris `badge number` dan `Tax ID` tidak tampil (tersaring keluar oleh Data Type)
48. Tambahkan Modified By `Budi S` pada panel yang sama, klik [Apply]
49. Verifikasi tabel menampilkan tepat satu baris `Office Phone` (Modified By `Budi S`)
50. Verifikasi keyword `number` tetap terisi
51. Verifikasi chip `Phone` pada field Data Type dan chip `Budi S` pada field Modified By tetap aktif
52. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel
53. Klik `(←)`

### TC-GS-UCF-506: Clear Field saat Search dan Sort aktif mempertahankan keyword dan arah sort

54. Ketik Search `number`, tekan Enter
55. Verifikasi tabel menampilkan tepat empat baris: `badge number`, `Emergency Phone`, `Office Phone`, dan `Tax ID`
56. Klik Filter
57. Pilih Required `Yes`, klik [Apply]
58. Verifikasi tabel menampilkan tepat dua baris: `Office Phone` dan `Tax ID`
59. Klik icon Filter untuk menutup panel
60. Klik header Data Type dua kali (descending)
61. Verifikasi sort Data Type descending aktif
62. Verifikasi urutan baris: `Tax ID` (Text) lalu `Office Phone` (Phone)
63. Klik Filter
64. Klik [Clear Field], klik [Apply]
65. Verifikasi keyword `number` tetap terisi
66. Verifikasi sort Data Type descending tetap aktif
67. Verifikasi tabel memuat empat baris berurutan: `badge number`, `Tax ID`, `Emergency Phone`, lalu `Office Phone`
68. Klik icon Filter untuk menutup panel
69. Klik header Data Type sekali lagi (sort kembali netral)
70. Klik `(←)`

### TC-GS-UCF-507: Mengosongkan Search saat Filter dan Sort aktif mempertahankan filter dan arah sort

71. Ketik Search `phone`, tekan Enter
72. Klik Filter
73. Pilih Required `Yes`, klik [Apply]
74. Klik icon Filter untuk menutup panel
75. Verifikasi tabel menampilkan tepat satu baris `Office Phone`
76. Klik header Data Type dua kali (descending)
77. Klik `✕` pada Search, tekan Enter
78. Verifikasi filter Required `Yes` tetap aktif (icon Filter menampilkan indikator filter aktif)
79. Verifikasi sort Data Type descending tetap aktif
80. Verifikasi tabel memuat tiga baris berurutan: `Tax ID` (Text), `Office Phone` (Phone), lalu `Cost Center` (Dropdown)
81. Klik header Data Type sekali lagi (sort kembali netral)
82. Klik `(←)`
83. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-218: Mengganti kolom sort tidak mereset Search dan Filter

84. Ketik Search `phone`, tekan Enter
85. Klik Filter, pilih Required `No`, klik [Apply], lalu klik icon Filter untuk menutup panel
86. Klik header Field Name
87. Klik header Data Type
88. Verifikasi keyword `phone` tetap terisi
89. Verifikasi icon Filter menampilkan indikator filter aktif
90. Verifikasi tabel menampilkan tepat satu baris `Emergency Phone`
91. Verifikasi sort berpindah ke Data Type ascending
92. Verifikasi header Field Name kembali netral
93. Klik header Data Type dua kali lagi (sort kembali netral)
94. Klik `(←)`
95. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-219: Filter tetap tersedia dan berlaku saat kolomnya di-hide

96. Klik Filter
97. Pilih Data Type `Phone`, klik [Apply]
98. Klik icon Filter untuk menutup panel
99. Klik ikon `⋯` pada header kolom Actions, uncheck `Data Type`, tutup Overlay Column Visibility
100. Verifikasi tabel menampilkan tepat dua baris: `Emergency Phone` dan `Office Phone`
101. Klik Filter
102. Verifikasi field Data Type tetap ada di Filter Panel
103. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel
104. Pulihkan konfigurasi: buka Modal Setup Column, klik [Reset to Default], klik [Save]

### TC-GS-UCF-231: Search, Apply filter, dan ganti page size mengembalikan ke halaman 1; sort tidak

105. Ubah ukuran halaman tabel kembali ke 10
106. Klik Next (pindah ke halaman 2)
107. Verifikasi halaman 2 aktif
108. Ketik Search `o`, tekan Enter
109. Verifikasi halaman 1 aktif
110. Klik Next (pindah ke halaman 2 lagi)
111. Klik Filter, pilih Required `No`, klik [Apply]
112. Verifikasi halaman 1 aktif
113. Klik icon Filter untuk menutup panel
114. Klik Next (pindah ke halaman 2)
115. Klik header Field Name
116. Verifikasi halaman 2 aktif (sort tidak mengembalikan ke halaman 1)
117. Ubah ukuran halaman tabel ke 25
118. Verifikasi halaman 1 aktif
119. Klik header Field Name dua kali lagi (sort kembali netral)
120. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel
121. Klik `(←)`
122. Ubah ukuran halaman tabel kembali ke 10

### TC-GS-UCF-220: Field baru yang tidak cocok filter aktif tidak muncul di tabel tersaring

123. Klik Filter
124. Pilih Data Type `Phone`, klik [Apply]
125. Klik icon Filter untuk menutup panel
126. Klik [+ Custom Field]
127. Isi Field Name `Filter Mut {runId}-053`
128. Pilih Data Type `Text`
129. Klik [Submit]
130. Verifikasi toast sukses "Success, custom field has been created."
131. Verifikasi tabel tersaring menampilkan tepat dua baris: `Emergency Phone` dan `Office Phone`
132. Verifikasi baris `Filter Mut {runId}-053` tidak tampil
133. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-504: Edit Field Name yang membuat baris tidak lagi cocok Search menghilangkannya

134. Buat lewat API field `Edit Hide Probe {runId}-053` (Text; Placeholder kosong) hingga tersimpan, lalu muat ulang halaman (F5)
135. Ketik Search `Hide Probe`, tekan Enter
136. Verifikasi tabel menampilkan tepat satu baris `Edit Hide Probe {runId}-053`
137. Klik `⋯` pada baris `Edit Hide Probe {runId}-053`, klik Edit
138. Ubah Field Name menjadi `Visible Probe {runId}-053`
139. Klik [Save]
140. Verifikasi toast sukses "Success, custom field has been updated."
141. Verifikasi keyword `Hide Probe` tetap terisi
142. Verifikasi empty state Title "No results found" tampil
143. Verifikasi empty state Description "Try adjusting your search or filter." tampil
144. Klik `(←)`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 144 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu topik dan satu dataset (interaksi Search, Filter, Sort, dan Pagination tabel utama), satu akun, tanpa mengubah data Pre-setup atau Population; tiap blok TC dimulai dari Search, Filter, dan Sort yang dikosongkan dan tetap bermakna bila blok lain gagal. Blok perubahan data (TC-GS-UCF-220 dan TC-GS-UCF-504) berada paling akhir sehingga kegagalan keras di dalamnya tidak menutupi blok sebelumnya.
- Urutan TC tidak mengikuti urutan nomor TC sumber: TC-GS-UCF-231 (reset halaman) ditaruh sebelum TC-GS-UCF-220 dan TC-GS-UCF-504 karena kedua TC itu membuat field milik spec dan mengubah total baris 14 yang diandalkan TC-GS-UCF-231 (halaman 2 berisi 4 baris); TC-GS-UCF-220 dan TC-GS-UCF-504 membuat dan mengubah data sehingga ditaruh paling akhir (prinsip 3 butir 5 konvensi). `Edit Hide Probe {runId}-053` dibuat pada langkah 134, sesudah blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 12, 19, 30, 36, 59, 68, 74, 85, 98, 113, 120, 125, dan 133 (menutup Filter Panel dan atau mengosongkan Filter dengan `[Clear Field]` lalu `[Apply]`); langkah 8, 16, 27, 41, 53, 70, 82, 94, 121, dan 144 (`(←)` menutup input dan mengosongkan keyword); langkah 26, 69, 81, 93, dan 119 (klik header sekali atau dua kali lagi hingga sort kembali netral setelah siklus tiga klik); langkah 32, 39, dan 77 (`✕` pada Search, tekan Enter, mengosongkan Search); langkah 104 (pemulihan Setup Column yang dituliskan TC-GS-UCF-219 langkah 4); langkah 105 dan 122 (ukuran halaman 10 sebelum dan sesudah TC-GS-UCF-231); langkah 134 (seeding field milik spec lewat API di tengah spec, alasan di butir urutan di atas).
- Model panel: TC tidak menyatakan apakah Filter Panel tetap terbuka sesudah `[Apply]`; spec memperlakukannya tetap terbuka dan menutupnya lewat klik icon Filter sebelum aksi di luar panel (lihat Temuan untuk QA).
- Pembagian TC lintas spec: Search tabel utama (TC-GS-UCF-10, 190 sampai 200, 311, 379, 510) ada di spec 051; Filter Panel tabel utama (TC-GS-UCF-201 sampai 213, 221, 351 sampai 354, 397) di spec 052; Sort di spec 054; Pagination di spec 055; Setup Column di spec 056.
- Asersi absence (langkah 6, 47, dan 132) beranchor positif pada baris yang tampil pada `Verifikasi` sebelumnya (langkah 5, 46, dan 131). Langkah 107 (halaman 2 aktif) adalah `Verifikasi` baseline tambahan di luar Expected TC sebelum Search pada TC-GS-UCF-231 (S-03).
- Temuan untuk QA:
  - TC tidak konsisten soal Filter Panel sesudah `[Apply]` (tetap terbuka atau menutup): TC-GS-UCF-505 langkah 4 menulis "Klik Filter" setelah Apply sebelumnya, sedangkan TC-GS-UCF-212 dan 213 menyiratkan panel tetap terbuka. Spec mengasumsikan tetap terbuka.
  - TC-GS-UCF-216 langkah 4 menyebut "Sort Field Name descending" tanpa jumlah klik; spec memakai dua klik sesuai siklus sort tiga state (klik 1 ascending, klik 2 descending; TC-GS-UCF-506 dan 507 menulis "dua kali" untuk descending).
  - TC-GS-UCF-216 dan TC-GS-UCF-217 Expected tidak menyebut ukuran halaman; asersi "14 baris" pada TC-GS-UCF-217 membutuhkan ukuran halaman 25, yang diatur oleh langkah TC-GS-UCF-216 (langkah 21) dan dikembalikan ke 10 pada langkah 105.
  - TC-GS-UCF-219 menulis langkah pemulihan Setup Column sebagai langkah 4 (bukan bagian Expected); spec menuliskannya sebagai langkah penghubung.
  - TC-GS-UCF-231 tidak menyebut jumlah hasil Search `o` dan filter Required `No`; halaman 2 pada langkah 110 dan 114 hanya ada bila hasilnya lebih dari 10 baris. Spec mengikuti TC (11 field Required No semuanya cocok dengan `o` karena kolom Required memuat `No`).
  - TC-GS-UCF-220 tidak menyebut Data Type field `Filter Mut`; spec memakai `Text` (D-86: Text).
  - Post Condition TC-GS-UCF-220 dan TC-GS-UCF-504 tanpa langkah observasi; tidak diasersi (data dibersihkan hook `after`).
  - Keputusan NC yang berbeda dari API/LLD (NC-06): TC-GS-UCF-505 dan 506 mengharapkan Search `number` mencocokkan Placeholder efektif `Emergency Phone`, `Office Phone` (`Enter phone number`), dan `Tax ID` (`Enter tax ID number`) selain Field Name `badge number`; asersi mengikuti TC dan PRD, dan dapat gagal pada backend nyata sampai API/LLD menyesuaikan pencarian Placeholder.
