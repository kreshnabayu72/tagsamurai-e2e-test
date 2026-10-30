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
18. Verifikasi sesi edit tetap terbuka dengan baris #1 berisi input `Acme Corp 2`
19. Verifikasi `[Save]` Enabled
20. Verifikasi toast sukses tidak tampil
21. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog

### TC-GS-IMPORT-219: Save sesi Duplicate gagal 500

22. Klik `⋯` pada baris #2
23. Pilih Duplicate
24. Atur intercept jaringan agar permintaan Save dibalas 500
25. Klik `[Save]`
26. Lepas intercept jaringan
27. Verifikasi toast error "Error, failed to add row."
28. Verifikasi sesi Duplicate tetap terbuka dengan baris salinan #3 tetap tampil sebagai input
29. Verifikasi `[Save]` Enabled
30. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog

### TC-GS-IMPORT-261: Remove gagal 500

31. Klik `⋯` pada baris #3
32. Pilih Remove
33. Atur intercept jaringan agar permintaan hapus baris dibalas 500
34. Klik `[Delete]`
35. Lepas intercept jaringan
36. Verifikasi toast error "Error, failed to delete row."
37. Verifikasi dialog "Delete Row" tetap terbuka dengan item list `Row #3`
38. Verifikasi `[Delete]` Enabled
39. Klik `[Cancel]`
40. Verifikasi baris #3 `Zebra Technologies` tetap ada
41. Verifikasi footer tetap `[Import (12)]`

### TC-GS-IMPORT-681: Remove tanpa respons (timeout)

42. Klik `⋯` pada baris #3
43. Pilih Remove
44. Atur intercept jaringan agar permintaan hapus baris tidak dibalas (timeout)
45. Klik `[Delete]`
46. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
47. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
48. Verifikasi dialog "Delete Row" tetap terbuka dengan item list `Row #3`
49. Verifikasi `[Delete]` Enabled
50. Klik `[Cancel]`
51. Verifikasi baris #3 `Zebra Technologies` tetap ada
52. Verifikasi footer tetap `[Import (12)]`

### TC-GS-IMPORT-273: Bulk Delete gagal 500

53. Centang baris #2 dan #5
54. Klik `[Bulk Action ▾]`
55. Klik `[Delete]` pada overlay
56. Atur intercept jaringan agar permintaan hapus baris dibalas 500
57. Klik `[Delete]` pada dialog Delete Rows
58. Lepas intercept jaringan
59. Verifikasi toast error "Error, failed to delete row."
60. Verifikasi dialog "Delete Rows" tetap terbuka dengan item list `Row #2` dan `Row #5`
61. Verifikasi `[Delete]` Enabled
62. Klik `[Cancel]`
63. Verifikasi baris #2 `Lenovo` dan #5 `Dell` tetap ada
64. Verifikasi Bulk Action Bar menampilkan "2 Rows selected"
65. Klik `[×]` pada Bulk Action Bar

### TC-GS-IMPORT-682: Bulk Delete tanpa respons (timeout)

66. Centang baris #2
67. Centang baris #5
68. Klik `[Bulk Action ▾]`
69. Klik `[Delete]` pada overlay
70. Atur intercept jaringan agar permintaan hapus baris tidak dibalas (timeout)
71. Klik `[Delete]` pada dialog Delete Rows
72. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
73. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
74. Verifikasi dialog "Delete Rows" tetap terbuka dengan item list `Row #2` dan `Row #5`
75. Verifikasi `[Delete]` Enabled
76. Klik `[Cancel]`
77. Verifikasi baris #2 `Lenovo` dan #5 `Dell` tetap ada
78. Verifikasi Bulk Action Bar menampilkan "2 Rows selected"
79. Klik `[×]` pada Bulk Action Bar

### TC-GS-IMPORT-283: Discard Draft gagal 500

80. Siapkan draft D-01 berumur 25 jam (varian 1) dan muat ulang halaman Import > Brand
81. Klik `[Discard]` pada Unsaved Banner
82. Atur intercept jaringan agar permintaan Discard Draft dibalas 500
83. Klik `[Discard Draft]`
84. Lepas intercept jaringan
85. Verifikasi toast error "Error, failed to discard draft."
86. Verifikasi dialog "Discard Draft" tetap terbuka
87. Verifikasi `[Discard Draft]` Enabled
88. Klik `[Cancel]`
89. Verifikasi draft tetap 12 baris: footer `[Import (12)]`
90. Verifikasi Unsaved Banner tetap tampil

### TC-GS-IMPORT-684: Discard Draft tanpa respons (timeout)

91. Klik `[Discard]` pada Unsaved Banner
92. Atur intercept jaringan agar permintaan Discard Draft tidak dibalas (timeout)
93. Klik `[Discard Draft]`
94. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
95. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
96. Verifikasi dialog "Discard Draft" tetap terbuka
97. Verifikasi `[Discard Draft]` Enabled
98. Klik `[Cancel]`
99. Verifikasi draft tetap 12 baris: footer `[Import (12)]`
100. Verifikasi Unsaved Banner tetap tampil

### TC-GS-IMPORT-683: Delete All Rows tanpa respons (timeout)

101. Pulihkan draft Client A ke D-09 dan muat ulang halaman Import > Brand
102. Atur intercept jaringan agar permintaan Delete All Rows tidak dibalas (timeout)
103. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
104. Tunggu hingga toast timeout tampil, lalu lepas intercept jaringan
105. Verifikasi toast error persisten "Connection problem. Please try again." tanpa tombol aksi
106. Verifikasi tidak ada dialog yang tampil
107. Verifikasi baris pesan "Brand Name: Max. 120 characters" tetap ada di Error Summary Callout dengan `[Delete All Rows]` Enabled
108. Verifikasi Total Rows tetap 13

### TC-GS-IMPORT-685: Delete All Rows gagal 500

109. Atur intercept jaringan agar permintaan Delete All Rows dibalas 500
110. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
111. Lepas intercept jaringan
112. Verifikasi toast error "Error, failed to delete row."
113. Verifikasi tidak ada dialog yang tampil
114. Verifikasi baris pesan "Brand Name: Max. 120 characters" tetap ada di Error Summary Callout
115. Verifikasi Total Rows tetap 13

### TC-GS-IMPORT-234: Save ulang sesi Duplicate setelah respons pertama hilang

116. Pulihkan draft Client A ke D-01 dan muat ulang halaman Import > Brand
117. Klik `⋯` pada baris #2
118. Pilih Duplicate
119. Ubah Brand Name salinan menjadi `Lenovo Group {runId}-067`
120. Atur intercept jaringan agar permintaan Save diteruskan ke server tetapi responsnya dibuang (timeout)
121. Klik `[Save]`
122. Verifikasi toast error persisten "Connection problem. Please try again." tampil
123. Verifikasi sesi Duplicate tetap terbuka
124. Tutup toast "Connection problem. Please try again."
125. Lepas intercept jaringan
126. Klik `[Save]` lagi
127. Verifikasi tidak ada dialog
128. Verifikasi tidak ada toast
129. Verifikasi Staging Table me-refresh dengan draft 13 baris dan tepat satu baris `Lenovo Group {runId}-067`
130. Verifikasi footer `[Import (13)]`
131. Pulihkan draft Client A ke D-01

## Notes

- Mode: FE+BE (intercept parsial di atas backend nyata). Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fault injection / resilience (kelas b, prinsip 13b). TC-GS-IMPORT-218, 219, 261, 273, 283, 579, 681, 682, 683, 684, 685 hanya mengasersi perilaku FE atas respons yang dipaksa dan dapat dijalankan juga sebagai `Mode: mock`; TC-GS-IMPORT-234 mengasersi state server sehingga FE+BE.
- Spec memuat 131 langkah, jauh di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kegagalan 5xx dan timeout pada aksi Staging Table), tiap blok berdiri sendiri dengan intercept dan draft yang dipulihkan, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Urutan blok: sesi edit dan Duplicate (TC-GS-IMPORT-218, 579, 219), Remove dan Bulk Delete (261, 681, 273, 682), Discard Draft (283, 684), Delete All Rows (683, 685), lalu TC-GS-IMPORT-234 di akhir karena draft menjadi 13 baris.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 26, 35, 46, 58, 72, 84, 94, 104, 111, 125 (melepas intercept segera setelah pemicu), langkah 10, 21, 30 (`[Cancel]` lalu `[Discard]` menutup sesi edit atau Duplicate), langkah 39, 50, 62, 76, 88, 98 (menutup dialog), langkah 65 dan 79 (menutup Bulk Action Bar), langkah 80, 101, 116, 131 (memulihkan draft), langkah 124 (menutup toast), langkah 16, 46, 72, 94, 104 (menunggu batas waktu permintaan).
- Pembagian TC lintas spec: Save, Remove, Bulk Delete, Discard Draft, dan Delete All Rows yang gagal ada di spec ini; kegagalan Confirm Mapping dan Upload ada di spec 047.
- Temuan untuk QA:
  - Batas waktu permintaan FE tidak disebut pada TC-GS-IMPORT-579, 681, 682, 683, 684; spec menunggu sampai toast timeout tampil.
  - TC-GS-IMPORT-218, 219, dan 579 tidak menyebut cara menutup sesi edit sesudah Expected; spec menambahkan `[Cancel]` dan `[Discard]` sebagai langkah penghubung.
  - TC-GS-IMPORT-234 menuliskan "Lenovo Group" tanpa suffix; spec memakai nama bersuffix per run.
