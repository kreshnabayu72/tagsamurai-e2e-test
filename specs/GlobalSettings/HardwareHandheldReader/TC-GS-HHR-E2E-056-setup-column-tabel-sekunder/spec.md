---
id: TC-GS-HHR-E2E-056-setup-column-tabel-sekunder
title: "Setup Column Tabel Sekunder Handheld Reader: Screening, Hide/Show, Reorder, Pin, Reset to Default, Tutup Tanpa Simpan, dan Kolom Terakhir pada Modal Changelog, Tab Usage, Popup Event Log Activate, dan Tab Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-292
  - TC-GS-HHR-293
  - TC-GS-HHR-294
  - TC-GS-HHR-295
  - TC-GS-HHR-296
  - TC-GS-HHR-297
  - TC-GS-HHR-298
  - TC-GS-HHR-299
  - TC-GS-HHR-300
  - TC-GS-HHR-301
  - TC-GS-HHR-302
  - TC-GS-HHR-303
  - TC-GS-HHR-304
  - TC-GS-HHR-305
coverage:
  web: automated
---

# Setup Column Tabel Sekunder Handheld Reader: Screening, Hide/Show, Reorder, Pin, Reset to Default, Tutup Tanpa Simpan, dan Kolom Terakhir pada Modal Changelog, Tab Usage, Popup Event Log Activate, dan Tab Changelog

## Prerequisites

- Mode: FE+BE (backend nyata). Preferensi kolom (visibilitas, urutan, pin) tersimpan per tabel di browser dan menjadi permanen setelah `[Save]`; tabel dimuat dari backend nyata.
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader dengan konfigurasi kolom seluruh tabel sekunder pada default.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis dipakai sebagai precondition TC, tidak diasersi (asersi spec ini hanya menyangkut kolom, bukan isi baris), dibuat lewat fixture backend sebelum eksekusi dan dipulihkan antar TC oleh fixture backend: Seed Reader A (10 reader DD-01 sampai DD-10), Seed Usage Event reader DD-01 (UE-01 sampai UE-06), Seed Changelog Client A (CL-01 sampai CL-09; entri reader DD-03 `Zebra Mobile Reader - 1` untuk Tab Changelog Popup Detail), dan Seed Event Log Client A (EL-01 sampai EL-05). Spec tidak mengubah data reader. Reader DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`, sehingga baris DD-01 dikenali lewat Serial Number `SN-HHR-00101` dan DD-03 lewat `SN-HHR-00103`.
- Data uji surface (perulangan per baris tabel; `<Surface>` dan kolom diambil dari baris tabel; "kolom pertama", "kolom kedua", dan "kolom terakhir" mengacu ke urutan default pada kolom Kolom default):

| Surface | Cara buka | Kolom default (urutan) | Kolom pertama | Kolom kedua | Kolom terakhir |
|---|---|---|---|---|---|
| `Modal Changelog` | Klik ikon Changelog | `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By` | `Date` | `Action` | `Modified By` |
| `Tab Usage Popup Detail` | Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`) lalu pilih tab `Usage` | `Date`, `Product`, `Event Type`, `Transaction ID`, `PIC` | `Date` | `Product` | `PIC` |
| `Popup Event Log Activate` | Klik ikon Event Log | `Date`, `Range Type`, `Device Name`, `Result`, `PIC` | `Date` | `Range Type` | `PIC` |
| `Tab Changelog Popup Detail` | Klik `Device Name` baris DD-03 (Serial Number `SN-HHR-00103`) lalu pilih tab `Changelog` | `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` | `Date` | `Action` | `Modified By` |

- Perulangan per surface: langkah 77 sampai 93 (TC-GS-HHR-300), 94 sampai 107 (TC-GS-HHR-301), 108 sampai 122 (TC-GS-HHR-302), 123 sampai 133 (TC-GS-HHR-303), 134 sampai 140 (TC-GS-HHR-304), dan 141 sampai 150 (TC-GS-HHR-305), masing-masing 4 iterasi (urutan baris tabel Data uji surface).
- Kemampuan teknis: kontrol ukuran viewport sehingga tabel surface dapat digulir horizontal; menyeret (drag and drop) baris kolom pada Popup Setup Column; mengarahkan kursor ke checkbox disabled untuk membaca tooltip; membaca urutan dan posisi kolom tabel; membaca dan menghapus preferensi kolom tabel di penyimpanan browser.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: konfigurasi kolom keempat tabel sekunder dikembalikan ke default (seluruh kolom tampil berurutan, tanpa pin) lewat langkah pemulihan eksplisit di akhir tiap iterasi yang mengubahnya; hook `after` sebagai cadangan (`[Reset to Default]` lalu `[Save]` pada tiap surface, atau penghapusan preferensi kolom tabel sekunder di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-HHR-292: Screening Overlay Column Visibility Modal Changelog

1. Klik ikon Changelog
2. Klik header kolom Actions `(⋯)` pada tabel
3. Verifikasi daftar kolom berurutan `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi checkbox seluruh kolom tercentang
5. Verifikasi checkbox seluruh kolom enabled
6. Verifikasi tidak ada kolom Curated pada daftar
7. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-HHR-293: Screening Popup Setup Column Modal Changelog

8. Klik item `Setup Column...` di bagian bawah overlay
9. Verifikasi judul `Setup Column`
10. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi ikon `[✕]`
12. Verifikasi baris kolom berurutan `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By`
13. Verifikasi tiap baris kolom tercentang
14. Verifikasi tiap baris kolom memiliki drag handle
15. Verifikasi tiap baris kolom memiliki ikon Pin
16. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil pada footer
17. Verifikasi tidak ada tombol `[Cancel]` pada footer
18. Klik `[✕]` (tutup popup tanpa Save)
19. Tutup Modal Changelog (penutupan surface sebelum surface berikutnya)

### TC-GS-HHR-294: Screening Overlay Column Visibility Tab Usage Popup Detail

20. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`) lalu pilih tab `Usage`
21. Klik header kolom Actions `(⋯)` pada tabel
22. Verifikasi daftar kolom berurutan `Date`, `Product`, `Event Type`, `Transaction ID`, `PIC`
23. Verifikasi checkbox seluruh kolom tercentang
24. Verifikasi checkbox seluruh kolom enabled
25. Verifikasi tidak ada kolom Curated pada daftar
26. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-HHR-295: Screening Popup Setup Column Tab Usage Popup Detail

27. Klik item `Setup Column...` di bagian bawah overlay
28. Verifikasi judul `Setup Column`
29. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
30. Verifikasi ikon `[✕]`
31. Verifikasi baris kolom berurutan `Date`, `Product`, `Event Type`, `Transaction ID`, `PIC`
32. Verifikasi tiap baris kolom tercentang
33. Verifikasi tiap baris kolom memiliki drag handle
34. Verifikasi tiap baris kolom memiliki ikon Pin
35. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil pada footer
36. Verifikasi tidak ada tombol `[Cancel]` pada footer
37. Klik `[✕]` (tutup popup tanpa Save)
38. Tutup Tab Usage Popup Detail (penutupan surface sebelum surface berikutnya)

### TC-GS-HHR-296: Screening Overlay Column Visibility Popup Event Log Activate

39. Klik ikon Event Log
40. Klik header kolom Actions `(⋯)` pada tabel
41. Verifikasi daftar kolom berurutan `Date`, `Range Type`, `Device Name`, `Result`, `PIC`
42. Verifikasi checkbox seluruh kolom tercentang
43. Verifikasi checkbox seluruh kolom enabled
44. Verifikasi tidak ada kolom Curated pada daftar
45. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-HHR-297: Screening Popup Setup Column Popup Event Log Activate

46. Klik item `Setup Column...` di bagian bawah overlay
47. Verifikasi judul `Setup Column`
48. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
49. Verifikasi ikon `[✕]`
50. Verifikasi baris kolom berurutan `Date`, `Range Type`, `Device Name`, `Result`, `PIC`
51. Verifikasi tiap baris kolom tercentang
52. Verifikasi tiap baris kolom memiliki drag handle
53. Verifikasi tiap baris kolom memiliki ikon Pin
54. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil pada footer
55. Verifikasi tidak ada tombol `[Cancel]` pada footer
56. Klik `[✕]` (tutup popup tanpa Save)
57. Tutup Popup Event Log Activate (penutupan surface sebelum surface berikutnya)

### TC-GS-HHR-298: Screening Overlay Column Visibility Tab Changelog Popup Detail

58. Klik `Device Name` baris DD-03 (Serial Number `SN-HHR-00103`) lalu pilih tab `Changelog`
59. Klik header kolom Actions `(⋯)` pada tabel
60. Verifikasi daftar kolom berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
61. Verifikasi checkbox seluruh kolom tercentang
62. Verifikasi checkbox seluruh kolom enabled
63. Verifikasi tidak ada kolom Curated pada daftar
64. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-HHR-299: Screening Popup Setup Column Tab Changelog Popup Detail

65. Klik item `Setup Column...` di bagian bawah overlay
66. Verifikasi judul `Setup Column`
67. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
68. Verifikasi ikon `[✕]`
69. Verifikasi baris kolom berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
70. Verifikasi tiap baris kolom tercentang
71. Verifikasi tiap baris kolom memiliki drag handle
72. Verifikasi tiap baris kolom memiliki ikon Pin
73. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil pada footer
74. Verifikasi tidak ada tombol `[Cancel]` pada footer
75. Klik `[✕]` (tutup popup tanpa Save)
76. Tutup Tab Changelog Popup Detail (penutupan surface sebelum surface berikutnya)

### TC-GS-HHR-300: Ceklis kolom di Popup Setup Column tabel sekunder

77. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
78. Klik header kolom Actions `(⋯)` pada tabel surface
79. Klik item `Setup Column...` di bagian bawah overlay
80. Lepas centang kolom pertama
81. Verifikasi kolom pertama hilang dari preview
82. Klik `[Save]`
83. Verifikasi kolom pertama hilang dari tabel
84. Muat ulang halaman (F5)
85. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
86. Verifikasi kolom kedua tampil di tabel (pembanding sebelum asersi absence)
87. Verifikasi kolom pertama tetap hilang dari tabel
88. Klik header kolom Actions `(⋯)` pada tabel surface
89. Klik item `Setup Column...` di bagian bawah overlay
90. Centang kembali kolom pertama
91. Klik `[Save]`
92. Verifikasi kolom pertama tampil kembali di tabel
93. Tutup surface `<Surface>`

### TC-GS-HHR-301: Reorder kolom di Popup Setup Column tabel sekunder

94. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
95. Klik header kolom Actions `(⋯)` pada tabel surface
96. Klik item `Setup Column...` di bagian bawah overlay
97. Seret kolom terakhir ke posisi paling atas daftar
98. Klik `[Save]`
99. Verifikasi kolom terakhir menjadi kolom data pertama pada tabel
100. Muat ulang halaman (F5)
101. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
102. Verifikasi kolom terakhir tetap menjadi kolom data pertama pada tabel
103. Klik header kolom Actions `(⋯)` pada tabel surface
104. Klik item `Setup Column...` di bagian bawah overlay
105. Klik `[Reset to Default]` (pemulihan urutan kolom)
106. Klik `[Save]`
107. Tutup surface `<Surface>`

### TC-GS-HHR-302: Pin kolom di Popup Setup Column tabel sekunder

108. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
109. Klik header kolom Actions `(⋯)` pada tabel surface
110. Klik item `Setup Column...` di bagian bawah overlay
111. Klik ikon Pin kolom pertama
112. Klik `[Save]`
113. Gulir tabel secara horizontal ke tepi kanan
114. Verifikasi kolom pertama tetap di posisinya (freeze kiri) saat tabel digulir horizontal
115. Gulir tabel secara horizontal kembali ke tepi kiri
116. Klik header kolom Actions `(⋯)` pada tabel surface
117. Klik item `Setup Column...` di bagian bawah overlay
118. Klik ikon Pin kolom pertama lagi (Unpin)
119. Klik `[Save]`
120. Gulir tabel secara horizontal ke tepi kanan
121. Verifikasi kolom pertama ikut bergeser saat tabel digulir horizontal
122. Tutup surface `<Surface>`

### TC-GS-HHR-303: Reset to Default di Popup Setup Column tabel sekunder

123. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
124. Klik header kolom Actions `(⋯)` pada tabel surface
125. Klik item `Setup Column...` di bagian bawah overlay
126. Sembunyikan kolom kedua
127. Klik `[Save]`
128. Klik header kolom Actions `(⋯)` pada tabel surface
129. Klik item `Setup Column...` di bagian bawah overlay
130. Klik `[Reset to Default]`
131. Klik `[Save]`
132. Verifikasi kolom pertama sampai terakhir tampil dengan urutan default awal sesuai kolom `Kolom default (urutan)` tabel Data uji surface
133. Tutup surface `<Surface>`

### TC-GS-HHR-304: Menutup Popup Setup Column tabel sekunder dengan X atau Esc membuang perubahan

134. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
135. Klik header kolom Actions `(⋯)` pada tabel surface
136. Klik item `Setup Column...` di bagian bawah overlay
137. Sembunyikan kolom kedua
138. Klik `[✕]`
139. Verifikasi kolom kedua tetap tampil di tabel
140. Tutup surface `<Surface>`

### TC-GS-HHR-305: Guard kolom terakhir di Popup Setup Column tabel sekunder

141. Buka surface `<Surface>` (cara pada kolom Cara buka tabel Prerequisites)
142. Klik header kolom Actions `(⋯)` pada tabel surface
143. Klik item `Setup Column...` di bagian bawah overlay
144. Lepas centang semua kolom kecuali kolom pertama
145. Arahkan kursor ke checkbox kolom pertama
146. Verifikasi tooltip checkbox kolom pertama `At least one column must remain visible.`
147. Verifikasi checkbox kolom pertama disabled
148. Klik checkbox kolom pertama
149. Klik `[✕]` (tutup popup tanpa Save)
150. Tutup surface `<Surface>`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`, section 4a-5.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (292 sampai 305) dipertahankan; delapan TC screening (292 sampai 299) di awal sebelum aksi yang mengubah konfigurasi kolom.
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan popup Setup Column tanpa Save dan penutupan surface pada akhir tiap blok screening dan tiap iterasi; `[Reset to Default]` lalu `[Save]` pada akhir tiap iterasi TC-GS-HHR-301 (pemulihan urutan kolom); menggulir tabel kembali ke tepi kiri pada TC-GS-HHR-302; pembukaan kembali surface sesudah muat ulang halaman (F5), karena muat ulang menutup surface.
- Langkah yang diulang per baris tabel Prerequisites (idiom "Untuk setiap baris tabel"): langkah 77 sampai 93, 94 sampai 107, 108 sampai 122, 123 sampai 133, 134 sampai 140, dan 141 sampai 150, masing-masing 4 iterasi. Tiap `Verifikasi` yang diulang tetap satu per klausa. Pembukaan surface, header Actions, dan `Setup Column...` adalah prefix berulang.
- Spec memuat 150 langkah nominal (sekitar 372 langkah dengan ekspansi blok ulang; di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas harness (fungsional, Popup Setup Column pada empat tabel sekunder), satu akun, satu dataset, tanpa aksi yang mengubah data reader; tiap iterasi memulihkan konfigurasi kolom surface ke default sebelum iterasi berikutnya (hook `after` sebagai cadangan), sehingga kegagalan satu blok atau surface tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Setup Column tabel Daftar Reader (TC-GS-HHR-277 sampai 291) ada di spec 055; isi dan mekanik Search, Filter, Sort Modal Changelog (TC-GS-HHR-326 sampai 336) di spec 061; Pagination tabel sekunder (TC-GS-HHR-325) di spec 060.
- Temuan untuk QA:
  - TC-GS-HHR-294 dan 295: TC tidak menyebut tab aktif saat Popup Detail dibuka lewat klik `Device Name`; spec memilih tab `Usage` secara eksplisit sebagai bagian cara buka.
  - TC-GS-HHR-300 sampai 305: Langkah Uji menyebut "kolom pertama", "kolom terakhir", atau "satu kolom" tanpa nama kolom; spec memakai kolom pertama/terakhir menurut urutan default tiap surface, dan kolom kedua untuk "satu kolom" pada TC-GS-HHR-303 dan 304 (supaya tidak berimpit dengan kolom pertama pada TC-GS-HHR-300), serta mempertahankan kolom pertama sebagai kolom tersisa pada TC-GS-HHR-305.
  - TC-GS-HHR-302: TC tidak menyebut syarat tabel sekunder dapat digulir horizontal pada 5 sampai 7 kolom; spec mengandalkan lebar viewport (kemampuan kontrol viewport di Prerequisites).
  - TC-GS-HHR-304: judul menyebut "X atau Esc" tetapi Langkah Uji hanya menutup dengan `[✕]`; spec mengikuti Langkah Uji (penutupan lewat `Esc` pada tabel Daftar Reader ada di TC-GS-HHR-287, spec 055).
  - TC-GS-HHR-301: Expected menyebut "bertahan setelah F5" tetapi Langkah Uji tidak memuat refresh; spec menambah muat ulang halaman (TC-GS-HHR-300 sudah memuatnya). Muat ulang halaman menutup surface, sehingga surface dibuka kembali.
  - TC-GS-HHR-292 sampai 305: cara membuka surface pada TC-GS-HHR-300 sampai 305 dirujuk ke "TC screening masing-masing"; spec menyalin cara buka ke tabel Data uji surface (S-04).
  - Mekanisme menghapus preferensi kolom di browser dan membaca posisi kolom tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.
