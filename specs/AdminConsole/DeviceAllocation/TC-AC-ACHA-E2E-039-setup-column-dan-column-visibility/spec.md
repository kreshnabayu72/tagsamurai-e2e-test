---
id: TC-AC-ACHA-E2E-039-setup-column-dan-column-visibility
title: "Setup Column dan Column Visibility pada List Device Allocation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-326
  - TC-AC-ACHA-327
  - TC-AC-ACHA-328
  - TC-AC-ACHA-329
  - TC-AC-ACHA-330
  - TC-AC-ACHA-331
  - TC-AC-ACHA-332
  - TC-AC-ACHA-333
  - TC-AC-ACHA-334
  - TC-AC-ACHA-335
  - TC-AC-ACHA-336
  - TC-AC-ACHA-337
  - TC-AC-ACHA-338
  - TC-AC-ACHA-339
  - TC-AC-ACHA-340
  - TC-AC-ACHA-341
coverage:
  web: automated
---

# Setup Column dan Column Visibility pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-11: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Kolom tabel (13 kolom berurutan di overlay dan popup): Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost. Sembilan kolom pertama bawaan (Hideable, tercentang), empat kolom terakhir tambahan (Curated, tidak tercentang). Kolom Actions (`⋯`) tidak termasuk daftar.
- Data uji kolom Hideable (K1), diulang per baris tabel pada TC-AC-ACHA-328 dan TC-AC-ACHA-332:

  | Kolom |
  |---|
  | Allocation ID |
  | Category |
  | Type |
  | Quantity |
  | From |
  | Client |
  | Allocated By |
  | Status |
  | Last Updated |

- Data uji kolom Curated (K2), diulang per baris tabel pada TC-AC-ACHA-329 dan TC-AC-ACHA-333:

  | Kolom |
  |---|
  | Notes |
  | Payment |
  | Paid From |
  | Cost |

- Data uji TC-AC-ACHA-330 (geser kelas K1, diulang per baris tabel; urutan penuh di preview sesudah kolom dipindah ke posisi terakhir dengan keempat kolom Curated dicentang):

  | Kolom yang dipindah | Urutan penuh di preview |
  |---|---|
  | Allocation ID | Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost, Allocation ID |
  | Category | Allocation ID, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost, Category |
  | Type | Allocation ID, Category, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost, Type |
  | Quantity | Allocation ID, Category, Type, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost, Quantity |
  | From | Allocation ID, Category, Type, Quantity, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost, From |
  | Client | Allocation ID, Category, Type, Quantity, From, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost, Client |
  | Allocated By | Allocation ID, Category, Type, Quantity, From, Client, Status, Last Updated, Notes, Payment, Paid From, Cost, Allocated By |
  | Status | Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Last Updated, Notes, Payment, Paid From, Cost, Status |
  | Last Updated | Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Notes, Payment, Paid From, Cost, Last Updated |

- Data uji TC-AC-ACHA-331 (geser kelas K2, diulang per baris tabel; urutan penuh di preview sesudah kolom dipindah ke posisi pertama):

  | Kolom yang dipindah | Urutan penuh di preview |
  |---|---|
  | Notes | Notes, Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Payment, Paid From, Cost |
  | Payment | Payment, Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Paid From, Cost |
  | Paid From | Paid From, Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Cost |
  | Cost | Cost, Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From |

- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom tabel Device Allocation di browser (localStorage) dipakai sebagai pemulihan antar TC dan di hook `after`; mengamati pembekuan kolom (pin) lewat scroll horizontal tabel; drag and drop baris di overlay dan popup; Logout dan Login ulang akun aktor di browser yang sama (TC-AC-ACHA-340).
- State yang diubah: konfigurasi kolom tersimpan di browser (Setup Column dan overlay Column Visibility). Setiap TC yang mengubahnya diakhiri langkah pemulihan "Hapus preferensi kolom ... muat ulang halaman (F5)"; hook `after` suite menjadi cadangan.
- Sesi: TC-AC-ACHA-340 paling akhir karena Logout lalu Login ulang akun aktor; hook `after` mengembalikan sesi ke akun default suite.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-326: Screening overlay Column Visibility

1. Klik ikon `⋯` pada header kolom terakhir
2. Verifikasi overlay Column Visibility tampil tanpa backdrop
3. Verifikasi overlay memuat 13 kolom berurutan: Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated, Notes, Payment, Paid From, Cost
4. Verifikasi sembilan kolom bawaan (Allocation ID sampai Last Updated) berstatus `☑ Hideable checked & enabled`
5. Verifikasi empat kolom tambahan (Notes, Payment, Paid From, Cost) berstatus `☐ Curated unchecked & enabled`
6. Verifikasi setiap baris punya drag handle
7. Verifikasi item `Setup Column...` ada di bagian bawah overlay
8. Verifikasi tidak ada kolom Locked
9. Tutup overlay Column Visibility

### TC-AC-ACHA-337: Guard satu kolom tersisa di overlay

10. Klik ikon `⋯` pada header kolom terakhir
11. Hapus centang kolom Allocation ID, Category, Type, Quantity, From, Client, Allocated By, dan Status satu per satu di overlay hingga tersisa kolom Last Updated
12. Arahkan kursor ke checkbox kolom Last Updated
13. Verifikasi checkbox kolom Last Updated (satu-satunya kolom tampil) disabled
14. Verifikasi tooltip "At least one column must remain visible."
15. Centang kembali kolom Allocation ID sehingga dua kolom tampil
16. Verifikasi semua checkbox kolom kembali aktif
17. Tutup overlay Column Visibility
18. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-339: Overlay menerapkan perubahan langsung

19. Klik ikon `⋯` pada header kolom terakhir
20. Hapus centang kolom Quantity di overlay
21. Seret kolom Status ke posisi pertama di overlay
22. Verifikasi perubahan overlay ter-apply langsung ke tabel tanpa Save (kolom Quantity tidak tampil dan kolom Status menjadi kolom pertama)
23. Tutup overlay Column Visibility
24. Muat ulang halaman (F5)
25. Verifikasi kolom Quantity tetap tersembunyi setelah F5
26. Verifikasi kolom Status tetap menjadi kolom pertama setelah F5
27. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-327: Screening popup Setup Column dan Preview

28. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
29. Verifikasi header popup memuat judul "Setup Column", deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.", dan ikon close `[×]`
30. Verifikasi body memuat daftar 13 kolom dengan checkbox (sembilan `☑`, empat `☐`)
31. Verifikasi body memuat drag handle per baris
32. Verifikasi body memuat ikon Pin per baris
33. Verifikasi Live Preview tabel di bawah daftar menampilkan urutan header
34. Verifikasi Live Preview menampilkan data sel yang tidak tertukar
35. Verifikasi Live Preview menampilkan styling badge
36. Verifikasi footer memuat `[Reset to Default]` (text, primary) dan `[Save]` (filled, success) rata kanan
37. Verifikasi tidak ada `[Cancel]` di footer
38. Klik `[×]` pada popup

### TC-AC-ACHA-336: Close atau Esc membuang perubahan popup

39. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
40. Hapus centang kolom Status dan Quantity di popup
41. Verifikasi tabel di balik popup merefleksikan perubahan sementara (kolom Status dan Quantity tidak tampil)
42. Klik `[×]` pada popup
43. Verifikasi seluruh perubahan dibuang: tabel kembali ke konfigurasi tersimpan terakhir (kolom Status dan Quantity tampil)
44. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
45. Hapus centang kolom Status dan Quantity di popup
46. Tekan Esc
47. Verifikasi seluruh perubahan dibuang: tabel kembali ke konfigurasi tersimpan terakhir (kolom Status dan Quantity tampil)

### TC-AC-ACHA-328: Ceklis dan unceklis kelas K1 (Hideable bawaan) di popup

48. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
49. Untuk setiap baris tabel Data uji kolom Hideable (K1) (langkah 49 sampai 52): hapus centang kolom itu di popup
50. Verifikasi kolom itu hilang dari preview
51. Centang kembali kolom itu
52. Verifikasi kolom itu muncul kembali di preview di posisi semula
53. Hapus centang kolom Quantity dan From di popup
54. Klik `[Save]`
55. Verifikasi tabel tidak menampilkan kolom Quantity dan From
56. Muat ulang halaman (F5)
57. Verifikasi konfigurasi tersimpan tetap berlaku setelah F5 (kolom Quantity dan From tidak tampil)
58. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-329: Ceklis dan unceklis kelas K2 (Curated tambahan) di popup

59. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
60. Untuk setiap baris tabel Data uji kolom Curated (K2) (langkah 60 sampai 61): centang kolom itu di popup
61. Verifikasi kolom itu ditambahkan ke preview
62. Klik `[Save]`
63. Verifikasi tabel menampilkan kolom Notes, Payment, Paid From, dan Cost
64. Muat ulang halaman (F5)
65. Verifikasi keempat kolom Curated tetap tampil setelah F5
66. Verifikasi total 13 kolom tampil tidak melewati batas Max Visible Columns
67. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
68. Untuk setiap baris tabel Data uji kolom Curated (K2) (langkah 68 sampai 69): hapus centang kolom itu di popup
69. Verifikasi kolom itu disembunyikan kembali dari preview
70. Klik `[×]` pada popup
71. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-330: Geser (drag reorder) kelas K1

72. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
73. Centang kolom Notes, Payment, Paid From, dan Cost di popup
74. Untuk setiap baris tabel Data uji TC-AC-ACHA-330 (langkah 74 sampai 76): seret kolom itu ke posisi terakhir di popup
75. Verifikasi urutan kolom di preview sesuai kolom "Urutan penuh di preview" baris tabel itu
76. Seret kolom itu kembali ke posisi semula
77. Seret kolom Status ke posisi pertama di popup
78. Klik `[Save]`
79. Muat ulang halaman (F5)
80. Verifikasi kolom Status tampil sebagai kolom pertama setelah F5
81. Verifikasi urutan tabel sama dengan urutan yang ditata di modal (Status, Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Last Updated, Notes, Payment, Paid From, Cost)
82. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-331: Geser (drag reorder) kelas K2

83. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
84. Centang kolom Notes, Payment, Paid From, dan Cost di popup
85. Untuk setiap baris tabel Data uji TC-AC-ACHA-331 (langkah 85 sampai 87): seret kolom itu ke posisi pertama di popup
86. Verifikasi urutan kolom di preview sesuai kolom "Urutan penuh di preview" baris tabel itu
87. Seret kolom itu kembali ke posisi semula
88. Seret kolom Cost ke posisi pertama di popup
89. Klik `[Save]`
90. Muat ulang halaman (F5)
91. Verifikasi kolom Cost tampil sebagai kolom pertama setelah F5
92. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-332: Pin dan Unpin kelas K1

93. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
94. Centang kolom Notes, Payment, Paid From, dan Cost di popup
95. Klik `[Save]`
96. Untuk setiap baris tabel Data uji kolom Hideable (K1) (langkah 96 sampai 106): klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
97. Klik ikon Pin kolom itu di popup
98. Verifikasi ikon Pin kolom itu berubah menjadi aktif
99. Klik `[Save]`
100. Scroll tabel secara horizontal
101. Verifikasi kolom itu membeku di sisi kiri saat tabel di-scroll horizontal
102. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
103. Klik ikon Pin kolom itu di popup (Unpin)
104. Klik `[Save]`
105. Scroll tabel secara horizontal
106. Verifikasi bekuan kolom itu terlepas (kolom ikut tergulir)
107. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
108. Klik ikon Pin kolom Allocation ID di popup
109. Klik `[Save]`
110. Muat ulang halaman (F5)
111. Verifikasi kolom Allocation ID tetap beku setelah F5
112. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-333: Pin dan Unpin kelas K2

113. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
114. Centang kolom Notes, Payment, Paid From, dan Cost di popup
115. Klik `[Save]`
116. Untuk setiap baris tabel Data uji kolom Curated (K2) (langkah 116 sampai 125): klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
117. Klik ikon Pin kolom itu di popup
118. Klik `[Save]`
119. Scroll tabel secara horizontal
120. Verifikasi kolom itu membeku di sisi kiri saat tabel di-scroll horizontal
121. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
122. Klik ikon Pin kolom itu di popup (Unpin)
123. Klik `[Save]`
124. Scroll tabel secara horizontal
125. Verifikasi bekuan kolom itu terlepas (kolom ikut tergulir)
126. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-334: Guard Pin ke-4 (maksimum 3 kolom)

127. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
128. Centang kolom Notes, Payment, Paid From, dan Cost di popup
129. Klik ikon Pin kolom Allocation ID, Category, dan Type di popup
130. Arahkan kursor ke ikon Pin kolom Quantity
131. Verifikasi ikon Pin kolom Quantity disabled
132. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first."
133. Klik ikon Pin kolom Type di popup (Unpin)
134. Verifikasi ikon Pin kolom Quantity kembali aktif
135. Klik `[×]` pada popup

### TC-AC-ACHA-335: Reset to Default

136. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
137. Hapus centang kolom Quantity di popup
138. Centang kolom Cost di popup
139. Seret kolom Status ke posisi pertama di popup
140. Klik ikon Pin kolom Client di popup
141. Klik `[Reset to Default]`
142. Verifikasi preview kembali ke default modul: sembilan kolom bawaan tampil sesuai urutan awal (Allocation ID, Category, Type, Quantity, From, Client, Allocated By, Status, Last Updated)
143. Verifikasi tidak ada kolom yang dipin di preview
144. Verifikasi empat kolom tambahan (Notes, Payment, Paid From, Cost) tersembunyi
145. Klik `[Save]`
146. Verifikasi tabel memakai konfigurasi default (sembilan kolom bawaan, tanpa pin)
147. Muat ulang halaman (F5)
148. Verifikasi konfigurasi default tetap tersimpan setelah F5
149. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-338: Guard satu kolom tersisa di popup

150. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
151. Hapus centang kolom Allocation ID, Category, Type, Quantity, From, Client, Allocated By, dan Status satu per satu di popup hingga tersisa kolom Last Updated
152. Arahkan kursor ke checkbox kolom Last Updated
153. Verifikasi checkbox kolom Last Updated disabled
154. Verifikasi tooltip "At least one column must remain visible."
155. Verifikasi preview pada tabel di balik popup menampilkan satu kolom data `Last Updated`
156. Klik `[Save]`
157. Verifikasi popup tertutup
158. Verifikasi tabel tetap menampilkan satu kolom data `Last Updated`
159. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-341: Kolom Actions pinned kanan dan tidak muncul di Setup Column

160. Klik ikon `⋯` pada header kolom terakhir
161. Centang kolom Notes, Payment, Paid From, dan Cost di overlay Column Visibility
162. Tutup overlay Column Visibility
163. Scroll tabel secara horizontal
164. Verifikasi kolom Actions (`⋯`) terpin di sisi kanan tabel
165. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
166. Verifikasi kolom Actions tidak punya baris di popup Setup Column
167. Verifikasi tidak ada kolom checkbox di kiri tabel
168. Klik `[×]` pada popup
169. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

### TC-AC-ACHA-340: Persistensi konfigurasi kolom di cache browser

170. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
171. Klik ikon Pin kolom Allocation ID di popup
172. Centang kolom Notes di popup
173. Klik `[Save]`
174. Logout dari akun aktor
175. Login dengan akun aktor Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`
176. Buka Allocation > Device Allocation
177. Klik ikon `⋯` pada header kolom terakhir, klik `Setup Column...`
178. Verifikasi ikon Pin kolom Allocation ID aktif di popup
179. Klik `[×]` pada popup
180. Verifikasi kolom Notes tampil di tabel
181. Hapus preferensi kolom tabel Device Allocation di browser (kemampuan disediakan tim FE), muat ulang halaman (F5)

## Notes

- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-5). Seluruh TC primer spec ini (TC-AC-ACHA-326 sampai 341) dikerjakan di sini.
- Urutan dalam spec menyimpang dari urutan nomor TC: screening overlay (TC-326), TC overlay (TC-337, TC-339), screening popup (TC-327), TC-336, kelas K1 dan K2 (TC-328 sampai TC-335), TC-338, TC-341, lalu TC-340 paling akhir karena Logout dan Login ulang. Tiap TC tidak bergantung pada hasil TC lain: tiap TC diakhiri pemulihan preferensi kolom (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): pembukaan dan penutupan overlay Column Visibility dan popup Setup Column; pemulihan "Hapus preferensi kolom tabel ... muat ulang halaman (F5)" di akhir tiap TC yang mengubah konfigurasi (bukan `[Reset to Default]`, bagian 4); centang kolom Curated di awal TC yang membutuhkannya; penyiapan Pin dan Unpin per kolom. Perubahan overlay langsung diterapkan dan tersimpan (TC-AC-ACHA-339), sehingga TC-AC-ACHA-337 dan TC-AC-ACHA-339 juga diakhiri pemulihan.
- Perulangan (bagian 8b butir 7), langkah tidak bersyarat: langkah 49 sampai 52 (sembilan kolom K1), 58 sampai 59 dan 66 sampai 67 (empat kolom K2), 72 sampai 74 (sembilan kolom), 83 sampai 85 (empat kolom), 94 sampai 104 (sembilan kolom), dan 114 sampai 123 (empat kolom). Iterasi Pin membuka popup per kolom karena `[Save]` menutup popup dan Unpin dilakukan sesudah scroll.
- Spec memiliki 179 langkah nominal dan jauh lebih banyak setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Setup Column dan Column Visibility) pada tabel dan akun yang sama; tiap TC berdiri sendiri dengan pemulihan di akhirnya sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna; ekspansi berasal dari perulangan per kolom data tanpa langkah bersyarat (bagian 3 prinsip 13, Setup Column tetap satu spec selama dataset dan harness-nya sama).
- Asersi tambahan (S-03): TC-AC-ACHA-332 menutup dengan pin Allocation ID, Save, F5 untuk klausa "setelah F5 kolom yang dipin tetap beku" (TC memakai "satu kolom dipin dan disimpan"; spec memilih kolom pertama). TC-AC-ACHA-340 mengamati Pin lewat ikon Pin aktif di popup (TC tidak menyebut cara mengamati) dan Notes lewat tabel. TC-AC-ACHA-335 memecah Expected a menjadi tiga `Verifikasi` (urutan awal, tanpa pin, empat kolom tambahan tersembunyi). TC-AC-ACHA-336 dijalankan dua kali (klik `[×]` dan Esc) karena Expected b menyebut keduanya.
- Pemisahan topik satu dataset (prinsip 1): Search, Filter Panel, Sort, Setup Column, kombinasi kontrol, dan Pagination List memakai dataset Seed List yang sama (Pre-setup #48) dan dipisah menjadi spec 036 sampai 041 karena gabungannya jauh melewati batas ukuran (spec Setup Column dan Column Visibility ini saja 179 langkah nominal, belum termasuk ekspansi perulangan). Pemisahan per kontrol dipertahankan karena tiap spec memulai dari kondisi default yang dipulihkan di akhir spec dan di hook `after` (kolom default), sehingga kegagalan keras satu spec tidak membuat spec lain kehilangan makna; di dalam spec ini tiap TC mengakhiri dengan pemulihan state (S-09) dan tidak bergantung pada hasil TC lain, sehingga spec tetap satu (tanpa pemisah nyata: akun, kelas harness, dan dataset sama).
- Temuan untuk QA:
  - TC-AC-ACHA-326, 327, 337, 339, 341 menyatakan `FE Test: UI Only` tetapi spec ini berjalan terhadap backend nyata (Mode FE+BE) karena berbagi dataset seed dengan TC lain Setup Column; tidak ada asersi state backend.
  - TC-AC-ACHA-329 (langkah uji ketiga) meminta menghapus centang keempat kolom sesudah F5 tanpa Expected yang mengamati hasil akhirnya; spec mengasersi kolom disembunyikan dari preview lalu menutup popup dengan `[×]` (perubahan dibuang).
  - TC-AC-ACHA-330 dan 331 Expected menulis urutan 13 kolom penuh per kolom data (disalin ke tabel Data uji); TC-330 bergantung pada keempat kolom Curated dicentang di langkah uji pertama.
  - TC-AC-ACHA-334 Expected a menyebut "ikon Pin kolom lain disabled" tanpa menyebut kolom; spec mengamati kolom Quantity (kolom yang disebut pada langkah uji ketiga TC).
  - TC-AC-ACHA-340 Expected menyebut "tersimpan di cache browser (`localStorage`) per tabel"; spec hanya mengamati efeknya (Pin dan Notes tetap berlaku) dan tidak membaca `localStorage` langsung.
