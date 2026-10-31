---
id: TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface
title: "Pencatatan Log per Aksi pada Tiga Surface: Edit Alias Name, Edit Reader Power, Mark as, Cancel Request, Delete, dan Snapshot Nama Reader"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-345
  - TC-GS-HHR-346
  - TC-GS-HHR-347
  - TC-GS-HHR-348
  - TC-GS-HHR-349
  - TC-GS-HHR-350
  - TC-GS-HHR-351
  - TC-GS-HHR-353
coverage:
  web: automated
---

# Pencatatan Log per Aksi pada Tiga Surface: Edit Alias Name, Edit Reader Power, Mark as, Cancel Request, Delete, dan Snapshot Nama Reader

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini mengubah dan menghapus reader Seed Reader A dan menambah entri log Client A; aksi yang menghapus data (Cancel Request dan Delete) berada di akhir spec.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar itu lagi hanya sebagai kembali dari surface log.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Seed Reader A Client A (`Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, plan Growth, format tanggal `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, `SN-HHR-00101`, SKU-HHR-01, Jalur A, Long Range, Reader Power 30 dBm, Available), DD-02 (`Gudang Reader - 1`, `SN-HHR-00102`, SKU-HHR-03, Alias Name `Reader Gudang 02`), DD-03 (`Zebra Mobile Reader - 1`, `SN-HHR-00103`, SKU-HHR-02, Damaged), DD-05 (`Chainway C72 - 1`, Jalur B, Waiting for Approval), dan DD-07 (`Honeywell CK65 - 1`, Jalur B, Available). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya; DD-01 diidentifikasi lewat Serial Number karena DD-06 juga bernama `Zebra RFID Reader - 1`. Seed Changelog Client A (CL-01 s.d. CL-09; `Fixture.hardwareHandheldReader.seedChangelogClientA`) dipakai TC-GS-HHR-353 (entri seed `19/06/26 10:30` `Reader Gudang 02 (SKU-HHR-03)`).
- Pemulihan Seed Reader A: nilai Expected tiap TC mengasumsikan data awal yang dipulihkan (DD-01 `Available` dengan 30 dBm dan tanpa alias pada TC-GS-HHR-346, 347, 348; DD-02 beralias `Reader Gudang 02` pada TC-GS-HHR-353). Spec memulihkan Seed Reader A lewat kemampuan "pulihkan Seed Reader A lewat fixture backend" (disediakan tim FE/BE tanpa endpoint yang dikarang) pada langkah pertama tiap TC, lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Baseline log: jumlah entri total Changelog Handheld Reader, System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action) dicatat pada tiap TC sebelum aksi pemicu (S-12). Total entri tidak diasersi sebagai angka absolut; asersi memakai selisih terhadap baseline. Entri yang bertambah tidak dihapus (audit trail permanen).
- Ketiga surface mengikuti urutan kolom: Changelog (Date, Action, Device Name, Field, Old Value, New Value, Modified By), System Log aktor (Date, Action, Object, Name, Field, Old Value, New Value), Activity Log (Date, Action, Object, Name, Field, Old Value, New Value, Modified By). Entri terbaru berada di baris teratas karena urutan default Date terbaru di atas. Jam server dan jam browser disinkron (S-12); kolom Date hanya diasersi formatnya.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan jumlah dan isi entri pada tiga surface log; pemulihan Seed Reader A lewat fixture backend.
- State global: tidak ada yang diubah selain Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-345: Log Edit Alias Name

1. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
2. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
3. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
4. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
5. Buka Global Settings > Hardware > Handheld Reader
6. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Alias Name`
7. Isi `Alias Name` dengan `Reader Dock 01`
8. Klik `[Save]`
9. Tunggu aksi selesai (dialog tertutup)
10. Buka ikon Changelog Handheld Reader
11. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
12. Verifikasi entri terbaru Changelog: Action `Edit`, Device Name `Reader Dock 01 (SKU-HHR-01)`, Field `Alias Name`, Old Value `—`, New Value `Reader Dock 01`, Modified By `Sari D`
13. Tutup Modal Changelog dengan `✕`
14. Buka Global Settings > User > Detail akun aktor > tab System Log
15. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
16. Verifikasi entri terbaru System Log aktor: Action `Edit`, Object `Handheld Reader`, Name `Reader Dock 01 (SKU-HHR-01)`, Field `Alias Name`, Old Value `—`, New Value `Reader Dock 01`
17. Buka Global Settings > Activity Log > tab User Action
18. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
19. Verifikasi entri terbaru Activity Log: Action `Update Alias Name`, Object `Handheld Reader`, Name `Reader Dock 01 (SKU-HHR-01)`, Field `Alias Name`, Old Value `—`, New Value `Reader Dock 01`, Modified By `Sari D`
20. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
21. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
22. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-346: Log Edit Reader Power

23. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
24. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
25. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
26. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
27. Buka Global Settings > Hardware > Handheld Reader
28. Klik `⋯` pada baris DD-01 (Serial Number `SN-HHR-00101`), pilih `Edit Reader Power`
29. Geser slider dari 30 dBm ke 25 dBm
30. Klik `[Save]`
31. Tunggu aksi selesai (dialog tertutup)
32. Buka ikon Changelog Handheld Reader
33. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
34. Verifikasi entri terbaru Changelog: Action `Edit`, Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Reader Power`, Old Value `30 dBm`, New Value `25 dBm`, Modified By `Sari D`
35. Tutup Modal Changelog dengan `✕`
36. Buka Global Settings > User > Detail akun aktor > tab System Log
37. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
38. Verifikasi entri terbaru System Log aktor: Action `Edit`, Object `Handheld Reader`, Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Reader Power`, Old Value `30 dBm`, New Value `25 dBm`
39. Buka Global Settings > Activity Log > tab User Action
40. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
41. Verifikasi entri terbaru Activity Log: Action `Update Reader Power`, Object `Handheld Reader`, Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Reader Power`, Old Value `30 dBm`, New Value `25 dBm`, Modified By `Sari D`
42. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
43. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
44. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-353: Nama pada entri log adalah snapshot dan berubah mengikuti Alias hanya untuk entri baru

45. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
46. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog TC-GS-HHR-353, tutup modal dengan `✕`
47. Klik `⋯` pada baris DD-02 (Serial Number `SN-HHR-00102`, Alias Name `Reader Gudang 02`), pilih `Edit Alias Name`
48. Isi `Alias Name` dengan `Reader Gudang A`
49. Klik `[Save]`
50. Tunggu aksi selesai (dialog tertutup)
51. Klik `⋯` pada baris DD-02 (Serial Number `SN-HHR-00102`), pilih `Edit Alias Name`
52. Isi `Alias Name` dengan `Reader Gudang B`
53. Klik `[Save]`
54. Tunggu aksi selesai (dialog tertutup)
55. Buka ikon Changelog Handheld Reader
56. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline Changelog TC-GS-HHR-353
57. Verifikasi terdapat entri `Alias Name` pertama: Device Name `Reader Gudang A (SKU-HHR-03)`, Old Value `Reader Gudang 02`, New Value `Reader Gudang A`
58. Verifikasi terdapat entri `Alias Name` kedua: Device Name `Reader Gudang B (SKU-HHR-03)`, Old Value `Reader Gudang A`, New Value `Reader Gudang B`
59. Verifikasi entri seed `19/06/26 10:30` Device Name `Reader Gudang 02 (SKU-HHR-03)` tidak berubah
60. Tutup Modal Changelog dengan `✕`

### TC-GS-HHR-347: Log Mark as Damaged

61. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
62. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
63. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
64. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
65. Buka Global Settings > Hardware > Handheld Reader
66. Buka Overlay row action baris DD-01 (Serial Number `SN-HHR-00101`)
67. Klik `Mark as Damaged`
68. Klik `[Mark as Damaged]` pada dialog
69. Tunggu aksi selesai (dialog tertutup)
70. Buka ikon Changelog Handheld Reader
71. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
72. Verifikasi entri terbaru Changelog: Action `Edit`, Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `Available`, New Value `Damaged`, Modified By `Sari D`
73. Tutup Modal Changelog dengan `✕`
74. Buka Global Settings > User > Detail akun aktor > tab System Log
75. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
76. Verifikasi entri terbaru System Log aktor: Action `Edit`, Object `Handheld Reader`, Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `Available`, New Value `Damaged`
77. Buka Global Settings > Activity Log > tab User Action
78. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
79. Verifikasi entri terbaru Activity Log: Action `Mark as Damaged`, Object `Handheld Reader`, Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `Available`, New Value `Damaged`, Modified By `Sari D`
80. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
81. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
82. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-348: Log Mark as Missing

83. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
84. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
85. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
86. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
87. Buka Global Settings > Hardware > Handheld Reader
88. Buka Overlay row action baris DD-01 (Serial Number `SN-HHR-00101`)
89. Klik `Mark as Missing`
90. Klik `[Mark as Missing]` pada dialog
91. Tunggu aksi selesai (dialog tertutup)
92. Buka ikon Changelog Handheld Reader
93. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
94. Verifikasi entri terbaru Changelog: Action `Edit`, Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `Available`, New Value `Missing`, Modified By `Sari D`
95. Tutup Modal Changelog dengan `✕`
96. Buka Global Settings > User > Detail akun aktor > tab System Log
97. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
98. Verifikasi entri terbaru System Log aktor: Action `Edit`, Object `Handheld Reader`, Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `Available`, New Value `Missing`
99. Buka Global Settings > Activity Log > tab User Action
100. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
101. Verifikasi entri terbaru Activity Log: Action `Mark as Missing`, Object `Handheld Reader`, Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `Available`, New Value `Missing`, Modified By `Sari D`
102. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
103. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
104. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-349: Log Mark as Available

105. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
106. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
107. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
108. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
109. Buka Global Settings > Hardware > Handheld Reader
110. Buka Overlay row action baris DD-03 (Serial Number `SN-HHR-00103`, Damaged)
111. Klik `Mark as Available`
112. Klik `[Mark as Available]` pada dialog
113. Tunggu aksi selesai (dialog tertutup)
114. Buka ikon Changelog Handheld Reader
115. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
116. Verifikasi entri terbaru Changelog: Action `Edit`, Device Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Status`, Old Value `Damaged`, New Value `Available`, Modified By `Sari D`
117. Tutup Modal Changelog dengan `✕`
118. Buka Global Settings > User > Detail akun aktor > tab System Log
119. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
120. Verifikasi entri terbaru System Log aktor: Action `Edit`, Object `Handheld Reader`, Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Status`, Old Value `Damaged`, New Value `Available`
121. Buka Global Settings > Activity Log > tab User Action
122. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
123. Verifikasi entri terbaru Activity Log: Action `Mark as Available`, Object `Handheld Reader`, Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Status`, Old Value `Damaged`, New Value `Available`, Modified By `Sari D`
124. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
125. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
126. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-350: Log Cancel Request memakai Action Delete pada Changelog dan System Log

127. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
128. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
129. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
130. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
131. Buka Global Settings > Hardware > Handheld Reader
132. Buka Overlay row action baris DD-05 (`Chainway C72 - 1`, Waiting for Approval)
133. Klik `Cancel Request`
134. Klik `[Cancel Request]` pada dialog
135. Tunggu aksi selesai (dialog tertutup)
136. Buka ikon Changelog Handheld Reader
137. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
138. Verifikasi entri terbaru Changelog: Action `Delete`, Device Name `Chainway C72 - 1`, Field `Device Name`, Old Value `Chainway C72 - 1`, New Value `—`, Modified By `Sari D`
139. Tutup Modal Changelog dengan `✕`
140. Buka Global Settings > User > Detail akun aktor > tab System Log
141. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
142. Verifikasi entri terbaru System Log aktor: Action `Delete`, Object `Handheld Reader`, Name `Chainway C72 - 1`, Field `Device Name`, Old Value `Chainway C72 - 1`, New Value `—`
143. Buka Global Settings > Activity Log > tab User Action
144. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
145. Verifikasi entri terbaru Activity Log: Action `Cancel Request`, Object `Handheld Reader`, Name `Chainway C72 - 1`, Field `Device Name`, Old Value `Chainway C72 - 1`, New Value `—`, Modified By `Sari D`
146. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
147. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
148. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-351: Log Delete reader

149. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
150. Buka ikon Changelog Handheld Reader, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
151. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
152. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
153. Buka Global Settings > Hardware > Handheld Reader
154. Buka Overlay row action baris DD-07 (`Honeywell CK65 - 1`)
155. Klik `Delete`
156. Klik `[Delete]` pada dialog
157. Tunggu aksi selesai (dialog tertutup)
158. Buka ikon Changelog Handheld Reader
159. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline Changelog
160. Verifikasi entri terbaru Changelog: Action `Delete`, Device Name `Honeywell CK65 - 1`, Field `Device Name`, Old Value `Honeywell CK65 - 1`, New Value `—`, Modified By `Sari D`
161. Tutup Modal Changelog dengan `✕`
162. Buka Global Settings > User > Detail akun aktor > tab System Log
163. Verifikasi jumlah entri System Log aktor bertambah tepat 1 dari baseline System Log
164. Verifikasi entri terbaru System Log aktor: Action `Delete`, Object `Handheld Reader`, Name `Honeywell CK65 - 1`, Field `Device Name`, Old Value `Honeywell CK65 - 1`, New Value `—`
165. Buka Global Settings > Activity Log > tab User Action
166. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline Activity Log
167. Verifikasi entri terbaru Activity Log: Action `Delete`, Object `Handheld Reader`, Name `Honeywell CK65 - 1`, Field `Device Name`, Old Value `Honeywell CK65 - 1`, New Value `—`, Modified By `Sari D`
168. Verifikasi seluruh nilai pada ketiga entri berupa teks polos, bukan badge
169. Verifikasi kolom Date pada ketiga entri mengikuti format General Settings `dd/MM/yy` 24-hour
170. Buka Global Settings > Hardware > Handheld Reader


## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 5a).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 345, 346, 353, 347, 348, 349, 350, 351. Menyimpang dari urutan nomor TC sumber: TC-GS-HHR-353 (edit alias DD-02 dua kali) dipindah sebelum Mark as, sedangkan aksi yang menghapus reader (Cancel Request TC-GS-HHR-350 dan Delete TC-GS-HHR-351) berada paling akhir. Tiap TC dimulai dari Seed Reader A yang dipulihkan (langkah 1, 23, 45, 61, 83, 105, 127, 149) karena Expected tiap TC mengasumsikan data awal.
- Langkah penghubung (aksi tanpa `Verifikasi`): pemulihan dan muat ulang; pencatatan baseline (buka tiap surface, catat jumlah, kembali ke layar Handheld Reader); "Tunggu aksi selesai" sebelum berpindah surface (8b butir 8); membuka dan menutup surface log; kembali ke layar Handheld Reader. Blok baca-log berpola (buka surface, `Verifikasi` jumlah dan isi entri) tidak dihitung ke batas ukuran.
- Spec memuat 170 langkah, jauh di atas sekitar 35 langkah, dan tidak dipecah. Alasan: delapan blok TC memakai pola baca-log yang sama (satu kelas fungsional pencatatan, satu akun, tanpa harness eksternal); tiap blok dimulai dari Seed Reader A yang dipulihkan dan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; 60 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01). Memecah per aksi hanya menambah login, hook, dan pemulihan tanpa memisahkan kelas harness.
- Identifikasi entri: Expected `catat entri terbaru` dibaca sebagai entri teratas karena aksi menambah tepat satu entri (selisih jumlah terhadap baseline). Pada TC-GS-HHR-353 dua aksi terjadi pada menit yang sama sehingga urutan antar-dua-entri tidak dijamin; entri pertama dan kedua dicari berdasarkan Device Name, Old Value, dan New Value (S-12), bukan posisi.
- Asersi "tepat satu entri per surface" (Expected d tiap TC) dipenuhi lewat `Verifikasi` selisih jumlah +1 per surface; asersi "kolom Date mengikuti format General Settings" dan "nilai plain text (bukan badge)" masing-masing satu `Verifikasi` per TC atas ketiga entri (TC menyebutnya sebagai satu butir).
- Pembagian TC lintas spec: aktivasi Jalur A dan collision (TC-GS-HHR-343 dan 344) di spec 064; aksi tulis gagal 5xx tanpa entri (TC-GS-HHR-352) di spec 027; Edit No-Op tanpa entri (TC-GS-HHR-355) di spec absence 065; entri Edit Alias Name, Mark as, Cancel Request, dan Delete lewat bulk (TC-GS-HHR-219) di spec 045.
- Temuan untuk QA:
  - TC-GS-HHR-345 sampai 351 tidak menyebut cara membaca "entri terbaru" pada System Log aktor dan Activity Log selain membuka surface; spec membaca baris teratas dengan urutan default.
  - TC-GS-HHR-346 mengedit Reader Power DD-01 dari 30 dBm ke 25 dBm; nilai 25 dBm dicapai lewat slider tanpa cara penyetelan yang dinyatakan TC; spec menulis "Geser slider dari 30 dBm ke 25 dBm" mengikuti spec edit Reader Power lain.
  - TC-GS-HHR-345 sampai 351 tidak menyatakan pemulihan Seed Reader A antar TC di dalam satu spec; spec menulis pemulihan pada langkah pertama tiap blok (sesuai Catatan TC "mutasi TC sebelumnya tidak dibawa ke TC berikutnya"). Mekanisme pemulihan tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE.
  - TC-GS-HHR-350 menyebut Action `Cancel Request` hanya pada Activity Log dan Action `Delete` pada Changelog dan System Log; spec mengikuti ketiganya.
  - TC-GS-HHR-353 menulis "Entri `Alias Name` pertama/kedua" tanpa menyebut urutan baris pada tabel; spec mengasersi keberadaan kedua entri berdasarkan isi.
  - Post Condition tidak ada pada TC sumber slice ini.
