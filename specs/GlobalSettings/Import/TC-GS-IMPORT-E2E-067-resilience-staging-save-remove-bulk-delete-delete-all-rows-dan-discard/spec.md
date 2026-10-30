---
id: TC-GS-IMPORT-E2E-067-resilience-staging-save-remove-bulk-delete-delete-all-rows-dan-discard
title: "Resilience Staging: Save, Remove, Bulk Delete, Delete All Rows, dan Discard Draft Gagal 5xx atau Tanpa Respons (Timeout atau Jaringan Putus)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-218
  - TC-GS-IMPORT-219
  - TC-GS-IMPORT-234
  - TC-GS-IMPORT-261
  - TC-GS-IMPORT-273
  - TC-GS-IMPORT-283
  - TC-GS-IMPORT-579
  - TC-GS-IMPORT-681
  - TC-GS-IMPORT-682
  - TC-GS-IMPORT-683
  - TC-GS-IMPORT-684
  - TC-GS-IMPORT-685
coverage:
  web: automated
---

# Resilience Staging: Save, Remove, Bulk Delete, Delete All Rows, dan Discard Draft Gagal 5xx atau Tanpa Respons (Timeout atau Jaringan Putus)

## Prerequisites

- Mode: FE+BE (backend nyata dengan `Spectra.intercept()` parsial). Asersi TC-GS-IMPORT-234 mengasersi state server (draft 13 baris) sehingga membutuhkan backend nyata. Suite serial (`parallel: false`); lihat `suite.md`.
- Intercept pada permintaan Save sesi edit, Save sesi Duplicate, hapus baris (Remove dan Bulk Delete), Delete All Rows, dan Discard Draft: dibalas 500, tidak dibalas (timeout), atau diteruskan ke server dengan respons dibuang (TC-GS-IMPORT-234). Intercept dilepas segera setelah pemicu selesai. Batas waktu permintaan FE tidak tertulis di TC; spec menunggu sampai toast timeout tampil.
- Akun: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC):
  - D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, #2 `Lenovo`, #3 `Zebra Technologies`, #5 `Dell`).
  - D-09 draft Brand 13 baris (D-01 ditambah baris #13 `error` Brand Name 121 karakter) untuk TC-GS-IMPORT-683 dan 685.
  - D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil, untuk TC-GS-IMPORT-283 dan 684.
  - Nama baris salinan TC-GS-IMPORT-234 bersuffix per run: `Lenovo Group {runId}-067`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft dipulihkan ke D-01 atau D-09 antar blok; hook `after` melepas intercept yang tersisa.

## Test Steps

### TC-GS-IMPORT-218: Save sesi edit gagal 500

1. Klik `⋯` pada baris #1
2. Pilih Edit
3. Ubah Brand Name baris #1 menjadi `Acme Corporation`
4. Atur intercept jaringan agar permintaan Save dibalas 500
5. Klik `[Save]`
6. Lepas intercept jaringan
7. Verifikasi toast error "Error, failed to update row."
8. Verifikasi sesi edit tetap terbuka dengan baris #1 berisi input `Acme Corporation`
9. Verifikasi `[Save]` Enabled
10. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog

### TC-GS-IMPORT-579: Save sesi edit tanpa respons (timeout)

11. Klik `⋯` pada baris #1
12. Pilih Edit
13. Ubah Brand Name baris #1 menjadi `Acme Corp 2`
14. Atur intercept jaringan agar permintaan Save tidak dibalas (timeout)
15. Klik `[Save]`
16. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
17. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
18. Tutup toast "Connection problem. Please try again."
19. Verifikasi sesi edit tetap terbuka dengan baris #1 berisi input `Acme Corp 2`
20. Verifikasi `[Save]` Enabled
21. Verifikasi toast sukses tidak tampil
22. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog

### TC-GS-IMPORT-219: Save sesi Duplicate gagal 500

23. Klik `⋯` pada baris #2
24. Pilih Duplicate
25. Atur intercept jaringan agar permintaan Save dibalas 500
26. Klik `[Save]`
27. Lepas intercept jaringan
28. Verifikasi toast error "Error, failed to add row."
29. Verifikasi sesi Duplicate tetap terbuka dengan baris salinan #3 tetap tampil sebagai input
30. Verifikasi `[Save]` Enabled
31. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog

### TC-GS-IMPORT-261: Remove gagal 500

32. Klik `⋯` pada baris #3
33. Pilih Remove
34. Atur intercept jaringan agar permintaan hapus baris dibalas 500
35. Klik `[Delete]`
36. Lepas intercept jaringan
37. Verifikasi toast error "Error, failed to delete row."
38. Verifikasi dialog "Delete Row" tetap terbuka dengan item list `Row #3`
39. Verifikasi `[Delete]` Enabled
40. Klik `[Cancel]`
41. Verifikasi baris #3 `Zebra Technologies` tetap ada
42. Verifikasi footer tetap `[Import (12)]`

### TC-GS-IMPORT-681: Remove tanpa respons (timeout)

43. Klik `⋯` pada baris #3
44. Pilih Remove
45. Atur intercept jaringan agar permintaan hapus baris tidak dibalas (timeout)
46. Klik `[Delete]`
47. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
48. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
49. Tutup toast "Connection problem. Please try again."
50. Verifikasi dialog "Delete Row" tetap terbuka dengan item list `Row #3`
51. Verifikasi `[Delete]` Enabled
52. Klik `[Cancel]`
53. Verifikasi baris #3 `Zebra Technologies` tetap ada
54. Verifikasi footer tetap `[Import (12)]`

### TC-GS-IMPORT-273: Bulk Delete gagal 500

55. Centang baris #2 dan #5
56. Klik `[Bulk Action ▾]`
57. Klik `[Delete]` pada overlay
58. Atur intercept jaringan agar permintaan hapus baris dibalas 500
59. Klik `[Delete]` pada dialog Delete Rows
60. Lepas intercept jaringan
61. Verifikasi toast error "Error, failed to delete row."
62. Verifikasi dialog "Delete Rows" tetap terbuka dengan item list `Row #2` dan `Row #5`
63. Verifikasi `[Delete]` Enabled
64. Klik `[Cancel]`
65. Verifikasi baris #2 `Lenovo` dan #5 `Dell` tetap ada
66. Verifikasi Bulk Action Bar menampilkan "2 Rows selected"
67. Klik `[×]` pada Bulk Action Bar

### TC-GS-IMPORT-682: Bulk Delete tanpa respons (timeout)

68. Centang baris #2
69. Centang baris #5
70. Klik `[Bulk Action ▾]`
71. Klik `[Delete]` pada overlay
72. Atur intercept jaringan agar permintaan hapus baris tidak dibalas (timeout)
73. Klik `[Delete]` pada dialog Delete Rows
74. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
75. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
76. Tutup toast "Connection problem. Please try again."
77. Verifikasi dialog "Delete Rows" tetap terbuka dengan item list `Row #2` dan `Row #5`
78. Verifikasi `[Delete]` Enabled
79. Klik `[Cancel]`
80. Verifikasi baris #2 `Lenovo` dan #5 `Dell` tetap ada
81. Verifikasi Bulk Action Bar menampilkan "2 Rows selected"
82. Klik `[×]` pada Bulk Action Bar

### TC-GS-IMPORT-283: Discard Draft gagal 500

83. Siapkan draft D-01 berumur 25 jam (varian 1) dan muat ulang halaman Import > Brand
84. Klik `[Discard]` pada Unsaved Banner
85. Atur intercept jaringan agar permintaan Discard Draft dibalas 500
86. Klik `[Discard Draft]`
87. Lepas intercept jaringan
88. Verifikasi toast error "Error, failed to discard draft."
89. Verifikasi dialog "Discard Draft" tetap terbuka
90. Verifikasi `[Discard Draft]` Enabled
91. Klik `[Cancel]`
92. Verifikasi draft tetap 12 baris: footer `[Import (12)]`
93. Verifikasi Unsaved Banner tetap tampil

### TC-GS-IMPORT-684: Discard Draft tanpa respons (timeout)

94. Klik `[Discard]` pada Unsaved Banner
95. Atur intercept jaringan agar permintaan Discard Draft tidak dibalas (timeout)
96. Klik `[Discard Draft]`
97. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
98. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
99. Tutup toast "Connection problem. Please try again."
100. Verifikasi dialog "Discard Draft" tetap terbuka
101. Verifikasi `[Discard Draft]` Enabled
102. Klik `[Cancel]`
103. Verifikasi draft tetap 12 baris: footer `[Import (12)]`
104. Verifikasi Unsaved Banner tetap tampil

### TC-GS-IMPORT-683: Delete All Rows tanpa respons (timeout)

105. Pulihkan draft Client A ke D-09 dan muat ulang halaman Import > Brand
106. Atur intercept jaringan agar permintaan Delete All Rows tidak dibalas (timeout)
107. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
108. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
109. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
110. Tutup toast "Connection problem. Please try again."
111. Verifikasi tidak ada dialog yang tampil
112. Verifikasi baris pesan "Brand Name: Max. 120 characters" tetap ada di Error Summary Callout dengan `[Delete All Rows]` Enabled
113. Verifikasi Total Rows tetap 13

### TC-GS-IMPORT-685: Delete All Rows gagal 500

114. Atur intercept jaringan agar permintaan Delete All Rows dibalas 500
115. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
116. Lepas intercept jaringan
117. Verifikasi toast error "Error, failed to delete row."
118. Verifikasi tidak ada dialog yang tampil
119. Verifikasi baris pesan "Brand Name: Max. 120 characters" tetap ada di Error Summary Callout
120. Verifikasi Total Rows tetap 13

### TC-GS-IMPORT-234: Save ulang sesi Duplicate setelah respons pertama hilang

121. Pulihkan draft Client A ke D-01 dan muat ulang halaman Import > Brand
122. Klik `⋯` pada baris #2
123. Pilih Duplicate
124. Ubah Brand Name salinan menjadi `Lenovo Group {runId}-067`
125. Atur intercept jaringan agar permintaan Save diteruskan ke server tetapi responsnya dibuang (timeout)
126. Klik `[Save]`
127. Verifikasi toast error persisten "Connection problem. Please try again." tampil
128. Verifikasi sesi Duplicate tetap terbuka
129. Tutup toast "Connection problem. Please try again."
130. Lepas intercept jaringan
131. Klik `[Save]` lagi
132. Verifikasi tidak ada dialog
133. Verifikasi tidak ada toast
134. Verifikasi Staging Table me-refresh dengan draft 13 baris dan tepat satu baris `Lenovo Group {runId}-067`
135. Verifikasi footer `[Import (13)]`
136. Pulihkan draft Client A ke D-01

## Notes

- Mode: FE+BE (intercept parsial di atas backend nyata). Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fault injection / resilience (kelas b, prinsip 13b). TC-GS-IMPORT-218, 219, 261, 273, 283, 579, 681, 682, 683, 684, 685 hanya mengasersi perilaku FE atas respons yang dipaksa dan dapat dijalankan juga sebagai `Mode: mock`; TC-GS-IMPORT-234 mengasersi state server sehingga FE+BE.
- Spec memuat 136 langkah, jauh di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kegagalan 5xx dan timeout pada aksi Staging Table), tiap blok berdiri sendiri dengan intercept dan draft yang dipulihkan, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Urutan blok: sesi edit dan Duplicate (TC-GS-IMPORT-218, 579, 219), Remove dan Bulk Delete (261, 681, 273, 682), Discard Draft (283, 684), Delete All Rows (683, 685), lalu TC-GS-IMPORT-234 di akhir karena draft menjadi 13 baris.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 27, 36, 47, 60, 74, 87, 97, 108, 116, 130 (melepas intercept segera setelah pemicu), langkah 10, 22, 31 (`[Cancel]` lalu `[Discard]` menutup sesi edit atau Duplicate), langkah 40, 52, 64, 79, 91, 102 (menutup dialog), langkah 67 dan 82 (menutup Bulk Action Bar), langkah 83, 105, 121, 136 (memulihkan draft), langkah 18, 49, 76, 99, 110, 129 (menutup toast persisten supaya tidak terbawa ke langkah berikutnya), langkah 16, 47, 74, 97, 108 (menunggu batas waktu permintaan).
- Pembagian TC lintas spec: Save, Remove, Bulk Delete, Discard Draft, dan Delete All Rows yang gagal ada di spec ini; kegagalan Confirm Mapping dan Upload ada di spec 047.
- Temuan untuk QA:
  - Batas waktu permintaan FE tidak disebut pada TC-GS-IMPORT-579, 681, 682, 683, 684; spec menunggu sampai toast timeout tampil.
  - TC-GS-IMPORT-218, 219, dan 579 tidak menyebut cara menutup sesi edit sesudah Expected; spec menambahkan `[Cancel]` dan `[Discard]` sebagai langkah penghubung.
  - TC-GS-IMPORT-579, 681, 682, 684, dan 683 tidak menyebut penutupan toast persisten "Connection problem. Please try again."; spec menambahkan langkah menutup toast sebagai langkah penghubung.
  - TC-GS-IMPORT-234 menuliskan "Lenovo Group" tanpa suffix; spec memakai nama bersuffix per run.
