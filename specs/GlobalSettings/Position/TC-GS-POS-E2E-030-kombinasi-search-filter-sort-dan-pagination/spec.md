---
id: TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination
title: "Kombinasi Search, Filter, Sort, dan Pagination Tabel Position: Siklus Sort, Irisan, Clear, Empty State, dan Reset Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-165
  - TC-GS-POS-166
  - TC-GS-POS-167
  - TC-GS-POS-168
  - TC-GS-POS-169
  - TC-GS-POS-170
  - TC-GS-POS-171
  - TC-GS-POS-172
  - TC-GS-POS-173
  - TC-GS-POS-174
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination Tabel Position: Siklus Sort, Irisan, Clear, Empty State, dan Reset Halaman

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`. Klik sidebar mereset Search, Sort, dan Filter, sehingga pemulihan state ditulis eksplisit sebagai langkah (blok pemulihan akhir dan langkah penghubung antar-TC).
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record).
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.combinedSeed030`): 13 Position `HR Business Partner {runId}-030`, `IT Support Specialist {runId}-030`, `Temporary Staff {runId}-030`, `iOS Developer {runId}-030`, `Legal Counsel {runId}-030`, `Marketing Executive {runId}-030`, `Quality Assurance Analyst {runId}-030`, `Data Engineer {runId}-030`, `Office Administrator {runId}-030`, `Logistics Coordinator {runId}-030`, `Payroll Specialist {runId}-030`, `Security Officer {runId}-030`, `Training Coordinator {runId}-030`. Dengan 7 record Pre-setup, jumlah baris tabel N = 20 (ukuran halaman 10 sehingga halaman 2 ada; hasil Search `a` pada data ini minimal 11 baris sehingga halaman 2 juga ada). Total Position tepat 20 saat spec berjalan karena suite berjalan serial (`suite.md`) dan Position seed spec lain sudah dibersihkan hook `after` spec itu.
- Nilai tanggal yang dibaca hook `before` lewat API seeding (disediakan tim FE/BE, tanpa mengarang endpoint) dan dipakai di Filter Last Updated: D = tanggal seeding hari run (tanggal populasi, sesuai Time Zone General Settings); T_min = tanggal Last Updated terlama di antara seluruh Position entitas (rentang T_min sampai hari ini mencakup seluruh data).
- Last Updated record Pre-setup 10 sampai 16 lebih lama dari D (kondisi data disediakan tim FE/BE; spec tidak mengubah record Pre-setup). Dengan demikian kolom Last Updated memuat dua nilai distinct untuk asersi sort (langkah 12, 15): Pre-setup (lebih lama) dan seed (D). Filter satu hari D hanya memuat Position seed, sehingga `Sales Coordinator` (Pre-setup 16) tidak masuk hasil Filter D.
- General Settings Date/Time Format dan Time Zone tidak diubah spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-030` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pembacaan indikator sort, urutan baris, nilai Search, nilai rentang Filter, ukuran halaman, dan halaman aktif; tidak ada form terbuka sehingga tidak ada dialog `beforeunload`.
- State global: ukuran halaman diubah ke 25 (langkah 126) dan dikembalikan ke 10 (langkah 132); Search, Filter, dan Sort dipulihkan lewat langkah penghubung dan blok pemulihan akhir (langkah 132 sampai 138). Spec hanya membaca data tabel; tidak ada Position yang diubah atau dihapus. Flag Guided Tooltip diatur hook suite.

## Test Steps

### TC-GS-POS-167: Sort Name, siklus 3 klik

1. Klik header Name
2. Verifikasi indikator panah ↑ pada header Name
3. Verifikasi urutan baris Name A-Z tanpa memperhatikan kapitalisasi: `iOS Developer {runId}-030` tampil sebelum `IT Manager`
4. Klik header Name lagi
5. Verifikasi indikator panah ↓ pada header Name
6. Verifikasi urutan baris Name Z-A: `Warehouse Supervisor` tampil sebelum `Training Coordinator {runId}-030`
7. Klik header Name ketiga kali
8. Verifikasi indikator panah pada header Name hilang
9. Verifikasi urutan baris kembali default Name A-Z: `iOS Developer {runId}-030` tampil sebelum `IT Manager`

### TC-GS-POS-168: Sort Last Updated, siklus 3 klik

10. Klik header Last Updated
11. Verifikasi indikator panah ↑ (Oldest First) pada header Last Updated
12. Verifikasi urutan baris Last Updated dari yang terlama ke yang terbaru
13. Klik header Last Updated lagi
14. Verifikasi indikator panah ↓ (Newest First) pada header Last Updated
15. Verifikasi urutan baris Last Updated dari yang terbaru ke yang terlama
16. Klik header Last Updated ketiga kali
17. Verifikasi indikator panah pada header Last Updated hilang
18. Verifikasi urutan baris kembali Name A-Z

### TC-GS-POS-169: Pindah kolom sort mereset kolom sebelumnya

19. Klik header Name
20. Klik header Name lagi (Z-A, ↓)
21. Klik header Last Updated
22. Verifikasi indikator sort pada header Name kembali netral
23. Verifikasi header Last Updated aktif Oldest First (↑)
24. Klik header Last Updated lagi (Newest First)
25. Klik header Last Updated ketiga kali

### TC-GS-POS-165: Search lalu Filter menghasilkan irisan

26. Ketik Search `Coordinator`, tekan Enter
27. Klik ikon Filter untuk membuka panel
28. Pilih Last Updated dari tanggal D hingga tanggal D
29. Klik `[Apply]` (Filter Panel tetap terbuka)
30. Klik ikon Filter untuk menutup panel
31. Verifikasi baris `Logistics Coordinator {runId}-030` dan `Training Coordinator {runId}-030` tampil
32. Verifikasi setiap baris tabel memuat `Coordinator` pada Name
33. Verifikasi setiap baris tabel memiliki Last Updated bertanggal D
34. Verifikasi keyword Search `Coordinator` tetap terisi
35. Catat daftar nama baris hasil sebagai pembanding TC-GS-POS-166
36. Klik `✕` pada Search, tekan Enter
37. Klik ikon Filter untuk membuka panel
38. Klik `[Clear Field]`
39. Klik `[Apply]`
40. Klik ikon Filter untuk menutup panel

### TC-GS-POS-166: Filter lalu Search menghasilkan irisan yang sama

41. Klik ikon Filter untuk membuka panel
42. Pilih Last Updated dari tanggal D hingga tanggal D
43. Klik `[Apply]` (Filter Panel tetap terbuka)
44. Klik ikon Filter untuk menutup panel
45. Ketik Search `Coordinator`, tekan Enter
46. Verifikasi daftar nama baris hasil identik dengan yang dicatat pada langkah 35
47. Klik ikon Filter untuk membuka panel
48. Verifikasi Filter Last Updated tetap ter-apply dengan rentang tanggal D hingga tanggal D
49. Klik ikon Filter untuk menutup panel
50. Klik `✕` pada Search, tekan Enter
51. Klik ikon Filter untuk membuka panel
52. Klik `[Clear Field]`
53. Klik `[Apply]`
54. Klik ikon Filter untuk menutup panel

### TC-GS-POS-173: Pemulihan dari empty state kombinasi Search + Filter

55. Klik ikon Filter untuk membuka panel
56. Pilih Last Updated dari tanggal D hingga tanggal D
57. Klik `[Apply]` (Filter Panel tetap terbuka)
58. Klik ikon Filter untuk menutup panel
59. Ketik Search `Astronaut`, tekan Enter
60. Verifikasi area tabel menampilkan Illustration
61. Verifikasi area tabel menampilkan Title "No results found"
62. Verifikasi area tabel menampilkan Description "Try adjusting your search or filter."
63. Klik `←` pada Search
64. Verifikasi baris `Legal Counsel {runId}-030` tampil di tabel
65. Verifikasi tabel kembali menampilkan baris sesuai filter: setiap baris memiliki Last Updated bertanggal D
66. Klik ikon Filter untuk membuka panel
67. Klik `[Clear Field]`
68. Klik `[Apply]`
69. Klik ikon Filter untuk menutup panel

### TC-GS-POS-171: Clear Filter saat Search dan Sort aktif

70. Ketik Search `a`, tekan Enter
71. Klik header Name
72. Klik header Name lagi (Z-A)
73. Klik ikon Filter untuk membuka panel
74. Pilih Last Updated dari tanggal D hingga tanggal D
75. Klik `[Apply]` (Filter Panel tetap terbuka)
76. Klik `[Clear Field]`
77. Klik `[Apply]`
78. Verifikasi Filter Panel tanpa nilai ter-apply (filter terlepas)
79. Klik ikon Filter untuk menutup panel
80. Verifikasi keyword Search `a` tetap terisi
81. Verifikasi sort Name Z-A (indikator panah ↓) tetap berlaku

### TC-GS-POS-172: Clear Search saat Filter dan Sort aktif

82. Klik ikon Filter untuk membuka panel
83. Pilih Last Updated dari tanggal D hingga tanggal D
84. Klik `[Apply]` (Filter Panel tetap terbuka)
85. Klik `✕` pada Search, tekan Enter
86. Verifikasi Search terlepas (kolom Search kosong)
87. Verifikasi Filter Last Updated tetap ter-apply dengan rentang tanggal D hingga tanggal D
88. Klik ikon Filter untuk menutup panel
89. Verifikasi sort Name Z-A (indikator panah ↓) tetap berlaku
90. Klik ikon Filter untuk membuka panel
91. Klik `[Clear Field]`
92. Klik `[Apply]`
93. Klik ikon Filter untuk menutup panel
94. Klik header Name

### TC-GS-POS-174: Search dan Apply Filter mereset pagination ke halaman 1

95. Pindah ke halaman 2 pada Pagination
96. Verifikasi halaman aktif 2
97. Ketik Search `a`, tekan Enter
98. Verifikasi halaman aktif 1
99. Pindah ke halaman 2 pada Pagination
100. Verifikasi halaman aktif 2
101. Klik ikon Filter untuk membuka panel
102. Pilih Last Updated dari tanggal T_min hingga hari ini
103. Klik `[Apply]` (Filter Panel tetap terbuka)
104. Verifikasi halaman aktif 1
105. Klik ikon Filter untuk menutup panel
106. Klik `✕` pada Search, tekan Enter
107. Klik ikon Filter untuk membuka panel
108. Klik `[Clear Field]`
109. Klik `[Apply]`
110. Klik ikon Filter untuk menutup panel

### TC-GS-POS-170: Kombinasi Search + Filter + Sort + ukuran halaman

111. Ketik Search `a`, tekan Enter
112. Klik ikon Filter untuk membuka panel
113. Pilih Last Updated dari tanggal T_min hingga hari ini
114. Klik `[Apply]` (Filter Panel tetap terbuka)
115. Klik ikon Filter untuk menutup panel
116. Verifikasi baris `Legal Counsel {runId}-030` tampil di tabel
117. Verifikasi setiap baris tabel memuat `a` pada Name
118. Verifikasi setiap baris tabel memiliki Last Updated dalam rentang tanggal T_min hingga hari ini
119. Klik header Name
120. Klik header Name lagi (Z-A)
121. Verifikasi urutan baris Name Z-A
122. Verifikasi keyword Search `a` tetap terisi
123. Klik ikon Filter untuk membuka panel
124. Verifikasi Filter Last Updated tetap ter-apply dengan rentang tanggal T_min hingga hari ini
125. Klik ikon Filter untuk menutup panel
126. Ubah ukuran halaman ke 25
127. Verifikasi keyword Search `a` tetap terisi
128. Klik ikon Filter untuk membuka panel
129. Verifikasi Filter Last Updated tetap ter-apply dengan rentang tanggal T_min hingga hari ini
130. Klik ikon Filter untuk menutup panel
131. Verifikasi sort Name Z-A (indikator panah ↓) tetap berlaku

### Pemulihan state

132. Ubah ukuran halaman kembali ke 10
133. Klik header Name ketiga kali
134. Klik `✕` pada Search, tekan Enter
135. Klik ikon Filter untuk membuka panel
136. Klik `[Clear Field]`
137. Klik `[Apply]`
138. Klik ikon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 167, 168, 169, 165, 166, 173, 171, 172, 174, 170. Sort murni (167 sampai 169) lebih dulu karena tidak memakai Search maupun Filter; TC yang hanya menyentuh Search dan Filter (165, 166, 173) menyusul; TC-GS-POS-174 (halaman 2) ditaruh sebelum TC-GS-POS-170 karena TC-GS-POS-170 mengubah ukuran halaman ke 25. Urutan ini menyimpang dari urutan TC sumber (165 sampai 174). Layar awal dibuka di hook `beforeEach` dan dipakai bersama semua TC.
- Model Filter Panel mengikuti TC-GS-POS-160 sampai 166 dan 170: panel tetap terbuka sesudah `[Apply]` dan ditutup dengan klik ikon Filter. Tiap pembukaan panel untuk memilih rentang atau `[Clear Field]` berpasangan dengan penutupan sesudah `[Apply]`; "Klik ikon Filter untuk membuka panel" tidak pernah jatuh sesudah `[Apply]` tanpa penutupan. Pada TC-GS-POS-171 dan 172, `[Clear Field]` atau `✕` pada Search dikerjakan pada panel yang masih terbuka sesudah `[Apply]` (langkah 75 sampai 77, langkah 84 sampai 87); TC tidak menyebut penutupan panel, dan spec menutupnya pada langkah 79, 88, dan 93.
- Langkah penghubung (aksi tanpa `Verifikasi`; membersihkan state sebelum TC berikutnya mengandalkannya): langkah 24 sampai 25 (reset sort Last Updated), langkah 35 (mencatat pembanding), langkah 36 sampai 40, 49 sampai 54, 66 sampai 69, 88, 90 sampai 94, 106 sampai 110, dan 132 sampai 138 (menutup panel, melepas Search, melepas Filter, mereset sort, dan mengembalikan ukuran halaman ke 10). Buka dan tutup Filter Panel pada langkah yang hanya mengamati nilai Filter ter-apply (langkah 47 sampai 49, 123 sampai 125, 128 sampai 130) tidak mengubah state.
- Search `a` dan sort Name Z-A pada awal TC-GS-POS-172 berasal dari langkah 70 sampai 72 TC-GS-POS-171 (identik dengan langkah 1 TC-GS-POS-172) dan Filter (langkah 82 sampai 84) ditambahkan sesudahnya; urutan terapan tidak memengaruhi Expected karena ketiganya bersifat independen.
- Langkah 31 (baris `Logistics Coordinator {runId}-030` dan `Training Coordinator {runId}-030` tampil) adalah anchor positif yang ditaruh sebelum asersi "setiap baris" pada langkah 32 dan 33 supaya asersi "hanya menampilkan baris yang memuat Coordinator dan bertanggal D" tidak lolos pada hasil kosong. Langkah 64 dan 116 (baris `Legal Counsel {runId}-030` tampil) adalah anchor positif tambahan di luar Expected TC untuk asersi "setiap baris" pada langkah 65, 117, dan 118. Asersi urutan konkret pada langkah 3, 6, dan 9 menjadi contoh nyata dari urutan case-insensitive pada data di atas.
- Tidak ada asersi log; spec hanya membaca data tabel.
- Spec memuat 138 langkah (di atas smell sekitar 35 langkah). Seluruhnya satu kelas (Search, Filter, Sort, dan Pagination tabel Position yang berbagi dataset yang sama; bagian 3 konvensi), satu akun, tanpa aksi yang mengubah data; tiap blok TC dibersihkan lewat langkah penghubung sehingga memulai dari state tabel bersih dan tetap bermakna bila blok lain gagal. Spec ini dapat dipisah menjadi sort murni (TC-GS-POS-167 sampai 169) dan kombinasi (TC-GS-POS-165, 166, 170 sampai 174) bila QA menginginkan spec lebih pendek.
- Temuan untuk QA:
  - TC-GS-POS-165, 166, 171, 172, dan 173 menyebut Filter "satu hari (tanggal populasi)" tanpa menyatakan tanggal yang dipakai, dan Last Updated record Pre-setup 10 sampai 16 (terutama 15 dan 16 hasil Import) tidak dijamin lebih lama dari tanggal seeding; spec memakai D = tanggal seeding hari run dan menuliskan kondisi "Pre-setup lebih lama dari D" sebagai kebutuhan yang disediakan tim FE/BE.
  - TC-GS-POS-170 dan 174 menyebut "rentang yang mencakup seluruh data" tanpa menyatakan batas awal; spec memakai T_min yang dibaca hook `before`.
  - TC-GS-POS-174 langkah 3 menulis "Pindah ke halaman 2 lagi (bila ada)". Spec menulis tanpa kondisi karena hasil Search `a` pada data seeding minimal 11 baris (halaman 2 selalu ada) dan menambah `Verifikasi` halaman aktif 2 sebelum Search dan sebelum Filter.
  - TC-GS-POS-173 menulis "Klik `←` pada Search" tanpa menyebut apakah keyword Search ikut terhapus; Expected hanya menyebut tabel kembali sesuai filter, sehingga keadaan kolom Search sesudah `←` tidak diasersi.
  - Precondition TC-GS-POS-165 sampai 174 menyebut "Data Dinamis No. 1-13 dan Pre-setup No. 10-16" tanpa nama bersuffix; spec men-seed 13 nama itu dengan suffix `{runId}-030` (N = 20).
  - PRD (`position.md`) tidak menyatakan keadaan Filter Panel sesudah `[Apply]`; model "tetap terbuka, ditutup dengan klik ikon Filter" berasal dari TC-GS-POS-160 sampai 166 dan 170. TC-GS-POS-171 sampai 174 tidak menyebut penutupan panel.
