---
id: TC-GS-POS-E2E-032-setup-column-modal-tabel-utama
title: "Popup Setup Column Tabel Position: Screening, Footer, Search, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Popup Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-181
  - TC-GS-POS-182
  - TC-GS-POS-183
  - TC-GS-POS-184
  - TC-GS-POS-185
  - TC-GS-POS-186
  - TC-GS-POS-187
  - TC-GS-POS-188
  - TC-GS-POS-189
  - TC-GS-POS-190
  - TC-GS-POS-191
coverage:
  web: automated
---

# Popup Setup Column Tabel Position: Screening, Footer, Search, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Popup Changelog

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record), dipakai sebagai precondition TC, tidak diasersi.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.populationSeed032`): 13 Position `HR Business Partner {runId}-032`, `IT Support Specialist {runId}-032`, `Temporary Staff {runId}-032`, `iOS Developer {runId}-032`, `Legal Counsel {runId}-032`, `Marketing Executive {runId}-032`, `Quality Assurance Analyst {runId}-032`, `Data Engineer {runId}-032`, `Office Administrator {runId}-032`, `Logistics Coordinator {runId}-032`, `Payroll Specialist {runId}-032`, `Security Officer {runId}-032`, `Training Coordinator {runId}-032`. Seeding lewat API mencatat entri Create di Popup Changelog (PRD §4.1.2) sehingga tabel Changelog memiliki 7 kolom untuk TC-GS-POS-190 dan 191. Ke-13 Position dipakai sebagai precondition TC (Data Dinamis No. 1-13), tidak diasersi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-032` yang masih ada; pulihkan preferensi visibilitas, urutan, dan pin kolom tabel utama Position dan tabel Popup Changelog di browser ke default; pulihkan ukuran viewport.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: drag-and-drop item daftar kolom; mengubah ukuran viewport sehingga tabel dapat di-scroll horizontal (TC-GS-POS-186) dan memulihkannya; scroll horizontal tabel dan pembacaan kolom beku; muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka); pembacaan state disabled checkbox dan tooltip.
- State global: preferensi kolom (visibilitas, urutan, pin) tersimpan di browser per pengguna per tabel; spec memulihkannya lewat langkah penghubung di akhir tiap TC yang menyimpannya dan hook `after` sebagai cadangan. Tidak ada state lain yang diubah.

## Test Steps

### TC-GS-POS-181: Screening Popup Setup Column tabel utama

1. Klik ikon `⋯` pada header kolom Actions
2. Klik item `Setup Column...`
3. Verifikasi Header: Title "Setup Column"
4. Verifikasi Header: icon `[✕]`
5. Verifikasi Header: subtitle "Manage column visibility, reorder, and freeze columns."
6. Verifikasi Body: input search dengan placeholder "Search column name..."
7. Verifikasi Body: daftar memuat `Name` ☑
8. Verifikasi Body: daftar memuat `Name` dengan drag handle `⠿`
9. Verifikasi Body: daftar memuat `Name` dengan kontrol Pin
10. Verifikasi Body: daftar memuat `Last Updated` ☑
11. Verifikasi Body: daftar memuat `Last Updated` dengan drag handle `⠿`
12. Verifikasi Body: daftar memuat `Last Updated` dengan kontrol Pin
13. Verifikasi Footer rata kanan
14. Verifikasi Footer: tombol `[Reset to Default]` tampil
15. Verifikasi Footer: tombol `[Reset to Default]` bergaya text, primary
16. Verifikasi Footer: tombol `[Save]` tampil
17. Verifikasi Footer: tombol `[Save]` bergaya filled, success

### TC-GS-POS-182: Footer tanpa tombol Cancel

18. Verifikasi Footer hanya berisi `[Reset to Default]` dan `[Save]`
19. Verifikasi Footer tidak memiliki tombol `[Cancel]`
20. Verifikasi `[✕]` tampil di header popup
21. Tekan Esc
22. Verifikasi Popup Setup Column tertutup

### TC-GS-POS-183: Search nama kolom

23. Klik ikon `⋯` pada header kolom Actions
24. Klik item `Setup Column...`
25. Ketik `Last` pada input search "Search column name..."
26. Verifikasi daftar kolom hanya menampilkan `Last Updated`
27. Kosongkan input search "Search column name..."
28. Klik `[✕]` pada Popup Setup Column

### TC-GS-POS-189: Kolom terakhir yang tampil tidak bisa di-uncheck

29. Klik ikon `⋯` pada header kolom Actions
30. Klik item `Setup Column...`
31. Uncheck `Last Updated`
32. Hover checkbox `Name`
33. Verifikasi checkbox `Name` disabled
34. Verifikasi checkbox `Name` tetap tampil di daftar kolom
35. Verifikasi Tooltip "At least one column must remain visible."
36. Klik `[✕]` pada Popup Setup Column

### TC-GS-POS-188: Tutup via ✕ atau Esc membuang perubahan

37. Klik ikon `⋯` pada header kolom Actions
38. Klik item `Setup Column...`
39. Uncheck `Last Updated`
40. Klik `[✕]` pada Popup Setup Column
41. Verifikasi kolom Last Updated tetap tampil di tabel (perubahan preview dibuang)
42. Klik ikon `⋯` pada header kolom Actions
43. Klik item `Setup Column...`
44. Drag `Last Updated` ke atas `Name`
45. Tekan Esc
46. Verifikasi urutan kolom tabel tetap `Name | Last Updated`

### TC-GS-POS-184: Hide dan unhide kolom kelas Hideable (Name, Last Updated)

47. Klik ikon `⋯` pada header kolom Actions
48. Klik item `Setup Column...`
49. Uncheck `Name`
50. Verifikasi tabel di belakang popup (preview) tanpa kolom Name
51. Klik `[Save]`
52. Tekan F5
53. Verifikasi kolom Last Updated tampil di tabel
54. Verifikasi kolom Name tetap tersembunyi
55. Klik ikon `⋯` pada header kolom Actions
56. Klik item `Setup Column...`
57. Centang `Name`
58. Uncheck `Last Updated`
59. Verifikasi tabel di belakang popup (preview) tanpa kolom Last Updated
60. Klik `[Save]`
61. Tekan F5
62. Verifikasi kolom Name tampil lagi
63. Verifikasi kolom Last Updated tetap tersembunyi
64. Klik ikon `⋯` pada header kolom Actions
65. Klik item `Setup Column...`
66. Centang `Last Updated`
67. Klik `[Save]`
68. Verifikasi kolom Name tampil
69. Verifikasi kolom Last Updated tampil

### TC-GS-POS-185: Drag reorder kelas Hideable

70. Klik ikon `⋯` pada header kolom Actions
71. Klik item `Setup Column...`
72. Drag `Last Updated` ke atas `Name`
73. Verifikasi tabel di belakang popup (preview) berurutan `Last Updated | Name`
74. Klik `[Save]`
75. Tekan F5
76. Verifikasi urutan kolom tabel tetap `Last Updated | Name`
77. Klik ikon `⋯` pada header kolom Actions
78. Klik item `Setup Column...`
79. Drag `Name` ke atas `Last Updated`
80. Klik `[Save]`
81. Verifikasi urutan kolom tabel kembali `Name | Last Updated`

### TC-GS-POS-186: Pin kolom kelas Hideable

82. Persempit viewport browser sehingga tabel dapat di-scroll horizontal
83. Klik ikon `⋯` pada header kolom Actions
84. Klik item `Setup Column...`
85. Pin `Name`
86. Klik `[Save]`
87. Scroll tabel secara horizontal
88. Verifikasi kolom Name tetap beku di kiri saat tabel di-scroll
89. Tekan F5
90. Scroll tabel secara horizontal
91. Verifikasi kolom Name tetap ter-pin setelah F5
92. Klik ikon `⋯` pada header kolom Actions
93. Klik item `Setup Column...`
94. Pin `Last Updated`
95. Klik `[Save]`
96. Scroll tabel secara horizontal
97. Verifikasi kolom Last Updated ikut beku di kiri
98. Klik ikon `⋯` pada header kolom Actions
99. Klik item `Setup Column...`
100. Unpin `Name`
101. Unpin `Last Updated`
102. Klik `[Save]`
103. Pulihkan ukuran viewport browser

### TC-GS-POS-187: Reset to Default

104. Klik ikon `⋯` pada header kolom Actions
105. Klik item `Setup Column...`
106. Uncheck `Last Updated`
107. Pin `Name`
108. Klik `[Save]`
109. Klik ikon `⋯` pada header kolom Actions
110. Klik item `Setup Column...`
111. Klik `[Reset to Default]`
112. Verifikasi tabel di belakang popup (preview) berurutan `Name | Last Updated`
113. Verifikasi tabel di belakang popup (preview) menampilkan kolom Name dan Last Updated
114. Verifikasi kontrol Pin `Name` dan `Last Updated` tidak aktif (tanpa pin)
115. Klik `[Save]`
116. Tekan F5
117. Verifikasi tabel menampilkan kolom `Name | Last Updated` (konfigurasi default tetap)
118. Klik ikon `⋯` pada header kolom Actions
119. Klik item `Setup Column...`
120. Verifikasi kontrol Pin `Name` dan `Last Updated` tidak aktif (tanpa pin)
121. Klik `[✕]` pada Popup Setup Column

### TC-GS-POS-190: Preferensi kolom tabel utama tidak memengaruhi Popup Changelog

122. Klik ikon `⋯` pada header kolom Actions
123. Klik item `Setup Column...`
124. Uncheck `Last Updated`
125. Klik `[Save]`
126. Klik ikon `Changelog` pada toolbar
127. Klik ikon `⋯` pada header kolom Actions di tabel Popup Changelog
128. Verifikasi Overlay Column Visibility Popup Changelog memuat 7 kolom ☑: `Date`, `Action`, `Position Name`, `Field`, `Old Value`, `New Value`, `Modified By`
129. Verifikasi tabel Popup Changelog menampilkan 7 kolom: `Date`, `Action`, `Position Name`, `Field`, `Old Value`, `New Value`, `Modified By`
130. Tutup Overlay Column Visibility Popup Changelog
131. Tutup Popup Changelog dengan `✕` di header
132. Klik ikon `⋯` pada header kolom Actions
133. Klik item `Setup Column...`
134. Centang `Last Updated`
135. Klik `[Save]`

### TC-GS-POS-191: Preferensi kolom Popup Changelog tidak memengaruhi tabel utama

136. Klik ikon `Changelog` pada toolbar
137. Klik ikon `⋯` pada header kolom Actions di tabel Popup Changelog
138. Klik item `Setup Column...`
139. Uncheck `Field`
140. Klik `[Save]`
141. Tutup Popup Changelog dengan `✕` di header
142. Verifikasi tabel utama tetap berurutan `Name | Last Updated` sesuai konfigurasi tersimpannya
143. Klik ikon `Changelog` pada toolbar
144. Klik ikon `⋯` pada header kolom Actions di tabel Popup Changelog
145. Klik item `Setup Column...`
146. Centang `Field`
147. Klik `[Save]`
148. Tutup Popup Changelog dengan `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 181, 182, 183, 189, 188, 184, 185, 186, 187, 190, 191. TC yang tidak menyimpan perubahan (181 sampai 183, 189, 188) lebih dulu, lalu TC yang menyimpan konfigurasi (184 sampai 187), lalu TC lintas Popup Changelog (190, 191). Urutan ini menyimpang dari urutan TC sumber (181 sampai 191). Layar awal Global Settings > User > Position dibuka di hook `beforeEach` dan dipakai bersama semua TC.
- TC-GS-POS-182 dan 183 memulai dengan "Buka Popup Setup Column" yang identik dengan langkah 1 sampai 2 TC-GS-POS-181; popup dari TC-GS-POS-181 dilanjutkan tanpa dibuka ulang untuk TC-GS-POS-182. Popup ditutup dengan Esc pada langkah 21 (Expected b TC-GS-POS-182) sehingga TC-GS-POS-183 membuka popup lagi di langkah 23 sampai 24 dan menutupnya di langkah 28; jumlah pembukaan popup tidak melebihi jumlah kejadian menutup.
- Langkah penghubung (aksi tanpa `Verifikasi`; membersihkan atau memulihkan state sebelum TC berikutnya mengandalkannya): langkah 23 dan 24 (buka ulang popup sesudah Esc), langkah 27 dan 28 (kosongkan search, tutup popup), langkah 36 (tutup popup), langkah 82 dan 103 (persempit dan pulihkan viewport), langkah 98 sampai 102 (unpin kedua kolom dan Save sesudah TC-GS-POS-186), langkah 104 sampai 108 (membangun konfigurasi awal TC-GS-POS-187 sesuai langkah 1 TC sumber), langkah 121 (tutup popup), langkah 130 dan 131 (tutup overlay dan Popup Changelog), langkah 132 sampai 135 (tampilkan kembali Last Updated sesudah TC-GS-POS-190), dan langkah 143 sampai 148 (tampilkan kembali Field sesudah TC-GS-POS-191).
- Langkah 87, 90, dan 96 (scroll horizontal) ditambahkan karena kolom beku hanya teramati saat tabel di-scroll; setelah F5 pada langkah 89, scroll diulang di langkah 90 sebelum asersi langkah 91.
- Langkah 117 dan 120 mengamati konfigurasi default setelah F5 (urutan kolom pada tabel dan kontrol Pin pada popup); popup dibuka kembali di langkah 118 sampai 119 dan ditutup di langkah 121.
- Hover dan tooltip pada langkah 32 sampai 35 diasersi sebelum langkah yang mengubah state-nya (tutup popup pada langkah 36).
- Langkah 53 (kolom Last Updated tampil di tabel sesudah F5) adalah asersi tambahan di luar Expected TC-GS-POS-184 (S-03). Fungsinya anchor positif bagi absence langkah 54 (kolom Name tetap tersembunyi): halaman sudah termuat sesudah muat ulang (konvensi bagian 8b butir 2). Pada blok F5 berikutnya anchor-nya langkah 62 (kolom Name tampil lagi, Expected b TC-GS-POS-184), yang ditulis sebelum absence Last Updated pada langkah 63.
- Expected b TC-GS-POS-182 diasersi di langkah 20 (`[✕]` tampil di header) dan langkah 21 sampai 22 (Esc menutup popup). Perilaku `[✕]` dan Esc membuang perubahan diasersi di TC-GS-POS-188 (langkah 40 sampai 46).
- Spec memuat 148 langkah (di atas smell sekitar 35 langkah). Seluruhnya satu kelas (Popup Setup Column tabel utama beserta Popup Changelog sebagai sisi independensi, dataset sama, satu akun, tanpa mengubah data Position; bagian 3 konvensi menyatakan Setup Column tetap satu spec), dan tiap blok TC mengembalikan konfigurasi kolom ke default sehingga blok sesudahnya tetap bermakna bila blok sebelumnya gagal. Spec ini dapat dipisah menjadi TC tanpa simpan (181 sampai 183, 188, 189) dan TC yang menyimpan konfigurasi (184 sampai 187, 190, 191) bila QA menginginkan spec lebih pendek.
- Pembagian TC lintas spec: Overlay Column Visibility tabel utama (TC-GS-POS-177 sampai 180) ada di spec 031; Setup Column Popup Changelog (TC-GS-POS-229 sampai 236) ada di spec 042.
- Temuan untuk QA:
  - TC-GS-POS-190 mensyaratkan Popup Changelog memiliki 7 kolom, tetapi precondition TC tidak menyebut entri Changelog; spec mengandalkan entri Create hasil seeding API (hook `before`).
  - TC-GS-POS-190 dan 191 menyebut "Overlay Column Visibility modal" dan "Setup Column modal" pada Popup Changelog tanpa menyebut cara pembukaannya; spec memakai pola yang sama dengan tabel utama (`⋯` pada header Actions lalu `Setup Column...`).
  - TC-GS-POS-186 mensyaratkan "viewport sempit" tanpa menyebut lebar; ukurannya ditentukan di tahap script.
  - TC-GS-POS-186 tidak menyebut apakah pin Name dipertahankan saat Last Updated di-pin (Expected b hanya menyebut Last Updated ikut beku); spec hanya mengasersi Last Updated.
