---
id: TC-AC-ACHA-E2E-037-filter-panel-list
title: "Filter Panel pada List Device Allocation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-7
  - TC-AC-ACHA-9
  - TC-AC-ACHA-297
  - TC-AC-ACHA-298
  - TC-AC-ACHA-299
  - TC-AC-ACHA-300
  - TC-AC-ACHA-301
  - TC-AC-ACHA-302
  - TC-AC-ACHA-303
  - TC-AC-ACHA-304
  - TC-AC-ACHA-305
  - TC-AC-ACHA-306
  - TC-AC-ACHA-307
  - TC-AC-ACHA-308
  - TC-AC-ACHA-309
  - TC-AC-ACHA-310
  - TC-AC-ACHA-311
  - TC-AC-ACHA-312
  - TC-AC-ACHA-313
  - TC-AC-ACHA-314
coverage:
  web: automated
---

# Filter Panel pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-6: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Data Dinamis: TC-AC-ACHA-314 membuat satu alokasi baru (BLE Gateway, Client `PT Cipta Kreasi`, Quantity `1`, pengirim PT ABC, jalur langsung) lewat sesi API aktor; Allocation ID baru ditangkap dari respons pembuatan (Dynamic Reference) dan tidak di-hardcode. Alokasi ini tidak dapat dihapus lewat UI; seed dipulihkan ke Seed List 30 baris lewat fixture API Pre-setup #20 di hook `after` (disediakan tim FE/BE). TC-AC-ACHA-314 ditaruh paling akhir karena menambah baris ke tabel.
- Kemampuan teknis (disediakan tim FE): sesi API aktor (login API password akun aktor, bukan sesi web; dinyatakan di `suite.md`) untuk membuat alokasi; menampilkan atau menyembunyikan kolom lewat overlay Column Visibility; menghapus preferensi kolom di browser.
- State yang diubah: kolom Cost ditampilkan di TC-AC-ACHA-301 dan disembunyikan di TC-AC-ACHA-312; filter dan Search dibersihkan di akhir tiap TC. Alokasi baru TC-AC-ACHA-314 dipulihkan di hook `after`.
- Preferensi kolom tabel (Setup Column) tersimpan di browser; hook `after` suite menghapusnya (kemampuan disediakan tim FE, didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-297: Screening Filter Panel

1. Klik ikon Filter
2. Verifikasi ikon Filter berubah gelap saat panel terbuka
3. Verifikasi panel di bawah toolbar memuat 10 field berurutan: `Category` (placeholder "All categories"), `Type` ("All types"), `Quantity` (input `Min` dan `Max`), `From` ("All senders"), `Client` ("All clients"), `Allocated By` ("All users"), `Status` ("All statuses"), `Last Updated` ("Select date"), `Paid From` ("All sources"), `Cost` (input `Min` dan `Max`)
4. Verifikasi susunan maksimum 4 field per baris (4, 4, 2)
5. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan) di bawah field
6. Verifikasi field `Paid From` dan `Cost` tersedia di panel walau kolomnya Hidden secara default
7. Verifikasi tidak ada field untuk Allocation ID, Notes, dan Payment
8. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-303: Guard kolom non-filterable

9. Klik ikon Filter
10. Cari field untuk kolom Allocation ID, Notes, dan Payment di Filter Panel
11. Verifikasi tidak ada field filter untuk Allocation ID (identifier), Notes (free text), maupun Payment (deterministik dari From); penyaringan Allocation ID dan Notes hanya lewat Search
12. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-298: Opsi dropdown filter di-populate dari data tabel

13. Klik ikon Filter
14. Buka dropdown Category
15. Verifikasi opsi Category berasal dari data tabel (DISTINCT): `RFID`, `NFC`, `BLE`, `GPS`, `Handheld Reader`, `Smart Fixed Reader`, `BLE Gateway`
16. Verifikasi dropdown Category multi-select searchable dengan kotak pencarian di dalamnya
17. Tutup dropdown Category
18. Buka dropdown Type
19. Verifikasi opsi Type: `Object TAG`, `User TAG`, `Long Range`, `Short Range` (tidak ada opsi untuk nilai kosong `—`)
20. Verifikasi dropdown Type multi-select searchable dengan kotak pencarian di dalamnya
21. Tutup dropdown Type
22. Buka dropdown From
23. Verifikasi opsi From: `PT ABC`, `PT Global Distribusi`, `CV Mitra Solusi`, `PT Nusa Distribusi`
24. Verifikasi dropdown From multi-select searchable dengan kotak pencarian di dalamnya
25. Tutup dropdown From
26. Buka dropdown Client
27. Verifikasi opsi Client: `PT Sejahtera Logistik`, `PT Retail Makmur`, `PT Manufaktur Unggul`, `PT Bintang Timur`
28. Verifikasi dropdown Client multi-select searchable dengan kotak pencarian di dalamnya
29. Tutup dropdown Client
30. Buka dropdown Paid From
31. Verifikasi opsi Paid From: `PT ABC (Principal)` dan `PT Global Distribusi (Distributor)` (Principal tidak punya sumber kantong sehingga tidak menyumbang opsi)
32. Verifikasi dropdown Paid From multi-select searchable dengan kotak pencarian di dalamnya
33. Tutup dropdown Paid From
34. Buka dropdown Status
35. Verifikasi opsi Status: `Completed`, `Waiting for Approval`, `Rejected`, `Canceled`
36. Verifikasi dropdown Status multi-select searchable dengan kotak pencarian di dalamnya
37. Tutup dropdown Status
38. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-308: Pencarian internal dropdown filter

39. Klik ikon Filter
40. Buka dropdown Category, ketik `gate` pada kotak pencarian internal
41. Verifikasi daftar opsi menyempit menjadi `BLE Gateway` saja (substring, tidak case-sensitive)
42. Ganti isi kotak pencarian internal dengan `zzz`
43. Verifikasi teks `No results found` tampil di dalam dropdown tanpa ilustrasi
44. Tutup dropdown Category
45. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-307: Overflow chip menjadi +N more

46. Klik ikon Filter
47. Pilih enam opsi Category: `RFID`, `NFC`, `BLE`, `GPS`, `Handheld Reader`, `Smart Fixed Reader`
48. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field dan sisanya diringkas dalam satu chip `+N more` (jumlah chip tampil ditambah N sama dengan 6)
49. Verifikasi field tidak melebar keluar panel dan tidak digulir horizontal
50. Klik `[Clear Field]`
51. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-299: Filter per kelas F1, multi-select searchable From, Client, Allocated By, dan Paid From

52. Klik ikon Filter
53. Pilih From `PT Nusa Distribusi`, klik `[Apply]`
54. Verifikasi From `PT Nusa Distribusi`: 3 baris dengan baris teratas `HALC-20260908-00004`, `HALC-20260906-00003`, `HALC-20260903-00004`
55. Klik `[Clear Field]`, klik `[Apply]`
56. Pilih Client `PT Retail Makmur`, klik `[Apply]`
57. Verifikasi Client `PT Retail Makmur`: 6 baris dengan baris teratas `HALC-20260908-00001`, `HALC-20260907-00001`, `HALC-20260905-00003`
58. Klik `[Clear Field]`, klik `[Apply]`
59. Pilih Allocated By `Budi S`, klik `[Apply]`
60. Verifikasi Allocated By `Budi S`: 6 baris dengan baris teratas `HALC-20260908-00002`, `HALC-20260906-00002`, `HALC-20260905-00002`
61. Klik `[Clear Field]`, klik `[Apply]`
62. Pilih Paid From `PT Global Distribusi (Distributor)`, klik `[Apply]`
63. Verifikasi Paid From `PT Global Distribusi (Distributor)`: 6 baris (baris pengirim CV Mitra Solusi) dengan baris teratas `HALC-20260908-00001`, `HALC-20260907-00001`, `HALC-20260905-00003`
64. Klik `[Clear Field]`, klik `[Apply]`
65. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-300: Filter per kelas F1e, multi-select searchable Category, Type, dan Status

66. Klik ikon Filter
67. Pilih Category `NFC`, klik `[Apply]`
68. Verifikasi Category `NFC`: 4 baris dengan baris teratas `HALC-20260908-00004`, `HALC-20260906-00002`, `HALC-20260904-00001`
69. Klik `[Clear Field]`, klik `[Apply]`
70. Pilih Type `Long Range`, klik `[Apply]`
71. Verifikasi Type `Long Range`: 2 baris dengan baris teratas `HALC-20260906-00001`, `HALC-20260902-00003`
72. Verifikasi baris dengan Type `—` tersaring keluar
73. Klik `[Clear Field]`, klik `[Apply]`
74. Pilih Status `Waiting for Approval`, klik `[Apply]`
75. Verifikasi Status `Waiting for Approval`: 7 baris dengan baris teratas `HALC-20260909-00002`, `HALC-20260908-00004`, `HALC-20260907-00001`
76. Klik `[Clear Field]`, klik `[Apply]`
77. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-301: Filter per kelas F2, rentang angka Quantity dan Cost inklusif

78. Klik ikon `⋯` pada header kolom terakhir
79. Centang kolom Cost di overlay Column Visibility
80. Tutup overlay Column Visibility
81. Klik ikon Filter
82. Verifikasi input Quantity memiliki placeholder `Min` dan `Max`
83. Verifikasi input Cost memiliki placeholder `Min` dan `Max`
84. Isi Quantity `Min` `100` dan `Max` `300`, klik `[Apply]`
85. Verifikasi Quantity 100 sampai 300 (batas inklusif): 4 baris dengan baris teratas `HALC-20260907-00001`, `HALC-20260906-00003`, `HALC-20260904-00002`
86. Klik `[Clear Field]`, klik `[Apply]`
87. Isi Quantity `Min` `250` dan `Max` `250`, klik `[Apply]`
88. Verifikasi Quantity 250 sampai 250: 1 baris dengan baris teratas `HALC-20260907-00001`
89. Klik `[Clear Field]`, klik `[Apply]`
90. Isi Cost `Min` `100` dan `Max` `200`, klik `[Apply]`
91. Verifikasi Cost 100 sampai 200: 9 baris dengan baris teratas `HALC-20260909-00003`, `HALC-20260908-00002`, `HALC-20260908-00001`
92. Verifikasi baris dengan Cost `—` (pengirim Principal) tidak ikut
93. Klik `[Clear Field]`, klik `[Apply]`
94. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-312: Filter independen dari visibilitas kolom

95. Klik ikon Filter
96. Isi Cost `Min` `100` dan `Max` `200`, klik `[Apply]`
97. Klik ikon `⋯` pada header kolom terakhir
98. Hilangkan centang kolom Cost di overlay Column Visibility
99. Tutup overlay Column Visibility
100. Tutup Filter Panel (klik ikon Filter)
101. Klik ikon Filter
102. Verifikasi filter Cost yang sudah di-Apply tetap aktif: tabel tetap menampilkan 9 baris dengan baris teratas `HALC-20260909-00003`, `HALC-20260908-00002`, `HALC-20260908-00001`
103. Verifikasi field `Cost` tetap ada di Filter Panel walau kolomnya disembunyikan
104. Klik `[Clear Field]`, klik `[Apply]`
105. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-302: Filter per kelas F3, date range inklusif Last Updated

106. Klik ikon Filter
107. Verifikasi field Last Updated berupa satu date range picker dengan placeholder "Select date"
108. Pilih rentang Last Updated `03/09/26` sampai `04/09/26`
109. Verifikasi nilai terpilih tampil dengan Date Format `dd/MM/yy`
110. Klik `[Apply]`
111. Verifikasi rentang dua hari (inklusif di kedua ujung): 7 baris dengan baris teratas `HALC-20260904-00003`, `HALC-20260904-00002`, `HALC-20260904-00001`
112. Klik `[Clear Field]`, klik `[Apply]`
113. Pilih rentang Last Updated `03/09/26` sampai `03/09/26`, klik `[Apply]`
114. Verifikasi satu hari (Start = End): 4 baris dengan baris teratas `HALC-20260903-00004`, `HALC-20260903-00003`, `HALC-20260903-00002`
115. Klik `[Clear Field]`, klik `[Apply]`
116. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-311: Nilai kosong tersaring keluar saat filter kolom dipakai

117. Klik ikon Filter
118. Pilih Type `Object TAG`, klik `[Apply]`
119. Verifikasi hanya baris bertipe `Object TAG` tampil: 4 baris dengan baris teratas `HALC-20260909-00002`, `HALC-20260907-00001`, `HALC-20260903-00004`
120. Verifikasi baris dengan Type `—` (NFC, BLE, dan Category tanpa Type lainnya) tidak tampil
121. Klik `[Clear Field]`, klik `[Apply]`
122. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-304: OR di dalam field dan AND antar field

123. Klik ikon Filter
124. Pilih Status `Completed` dan `Rejected` pada satu field, klik `[Apply]`
125. Verifikasi dua opsi pada satu field memakai logika OR: 20 baris dengan baris teratas `HALC-20260909-00003`, `HALC-20260909-00001`, `HALC-20260908-00003`
126. Tambahkan From `PT Global Distribusi`, klik `[Apply]`
127. Verifikasi dua field berbeda memakai logika AND: 10 baris dengan baris teratas `HALC-20260909-00003`, `HALC-20260909-00001`, `HALC-20260908-00002`
128. Klik `[Clear Field]`, klik `[Apply]`
129. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-305: Hapus chip lewat tombol silang menyinkronkan checkbox

130. Klik ikon Filter
131. Pilih Status `Completed` dan `Rejected`
132. Verifikasi dua chip tampil di dalam field Status
133. Klik `(✕)` pada chip `Completed`
134. Verifikasi chip `Completed` terhapus dan chip `Rejected` tetap
135. Buka dropdown Status
136. Verifikasi centang `Completed` kosong di dalam dropdown
137. Tutup dropdown Status
138. Klik `[Apply]`
139. Verifikasi tabel menampilkan 4 baris (hanya Rejected) dengan baris teratas `HALC-20260908-00002`, `HALC-20260906-00003`, `HALC-20260903-00002`
140. Klik `[Clear Field]`, klik `[Apply]`
141. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-306: Hapus centang di dalam dropdown menyinkronkan chip

142. Klik ikon Filter
143. Pilih Status `Completed` dan `Rejected`
144. Buka dropdown Status, hapus centang `Completed` dari dalam dropdown
145. Verifikasi chip `Completed` hilang dari field dan chip `Rejected` tetap
146. Tutup dropdown Status
147. Klik `[Apply]`
148. Verifikasi tabel menampilkan 4 baris dengan baris teratas `HALC-20260908-00002`, `HALC-20260906-00003`, `HALC-20260903-00002`
149. Klik `[Clear Field]`, klik `[Apply]`
150. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-309: Menutup panel tanpa Apply membuang draft

151. Klik ikon Filter
152. Pilih Status `Completed` tanpa klik `[Apply]`
153. Klik di luar panel
154. Klik ikon Filter
155. Verifikasi field Status kembali kosong
156. Verifikasi tabel tetap menampilkan 30 baris (tiga halaman)
157. Pilih Status `Rejected`, klik `[Apply]`
158. Klik ikon Filter untuk menutup panel
159. Klik ikon Filter untuk membuka kembali panel
160. Verifikasi panel yang dibuka kembali menampilkan nilai ter-Apply terakhir (Status `Rejected`)
161. Klik `[Clear Field]`, klik `[Apply]`
162. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-310: Indikator filter aktif

163. Klik ikon Filter
164. Pilih Status `Completed`, klik `[Apply]`
165. Tutup Filter Panel (klik ikon Filter)
166. Verifikasi badge titik (tanpa angka) muncul pada ikon Filter saat panel tertutup
167. Klik ikon Filter
168. Verifikasi badge titik tetap tampil pada ikon Filter saat panel terbuka
169. Klik `[Clear Field]`, klik `[Apply]`
170. Verifikasi badge titik hilang dari ikon Filter
171. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-313: Apply Filter mereset ke halaman 1

172. Ketik `2` pada input nomor halaman, tekan Enter
173. Verifikasi tabel berada di halaman 2
174. Klik ikon Filter
175. Pilih Status `Completed`, klik `[Apply]`
176. Verifikasi tabel kembali ke halaman 1
177. Klik `[Clear Field]`, klik `[Apply]`
178. Tutup Filter Panel (klik ikon Filter)

### TC-AC-ACHA-7: Empty state Filtered saat Search tidak menemukan hasil

179. Ketik Search `zzzzqqqq`, tekan Enter
180. Verifikasi tabel menampilkan empty state Filtered dengan ilustrasi, judul "No results found", dan deskripsi "Try adjusting your search or filter."
181. Verifikasi teks "No device allocations yet" tidak tampil

### TC-AC-ACHA-9: Pemulihan dari empty state Filtered setelah salah satu penyaring dilepas

182. Verifikasi tabel kosong dengan "No results found" (Search `zzzzqqqq` dari TC sebelumnya masih aktif)
183. Klik ikon Filter
184. Pilih Status `Completed`, klik `[Apply]`
185. Klik ikon `(✕)` pada Search, tekan Enter pada input kosong
186. Verifikasi Search dilepas dan tabel pulih menampilkan baris berstatus Completed (16 baris) tanpa memuat ulang halaman
187. Verifikasi filter Status `Completed` tetap aktif
188. Klik `[Clear Field]`, klik `[Apply]`
189. Tutup Filter Panel (klik ikon Filter)
190. Klik `(←)` pada kotak Search

### TC-AC-ACHA-314: Opsi filter mengikuti data tabel

191. Klik ikon Filter
192. Pelaku kedua (sesi API Total Control Principal) membuat alokasi BLE Gateway untuk Client `PT Cipta Kreasi` hingga alokasi tersimpan
193. Buka dropdown Client
194. Verifikasi opsi `PT Cipta Kreasi` muncul pada dropdown Client tanpa memuat ulang halaman
195. Tutup dropdown Client
196. Tutup Filter Panel (klik ikon Filter)

## Notes

- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 1b dan 4a-2). Seluruh TC primer spec ini dikerjakan di sini. TC-AC-ACHA-7 dan TC-AC-ACHA-9 (empty state Filtered, bagian 1b) ditaruh di spec ini karena memakai Search dan Filter Panel; keduanya berurutan sesudah TC filter lain dan sebelum TC-AC-ACHA-314 yang menambah baris.
- Urutan dalam spec menyimpang dari urutan nomor TC: screening Filter Panel (TC-297, TC-303, TC-298, TC-308, TC-307) di awal, TC-AC-ACHA-312 langsung sesudah TC-AC-ACHA-301 karena memakai kolom Cost yang sama, dan TC-AC-ACHA-314 paling akhir karena membuat alokasi baru yang mengubah dataset.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): "Tutup Filter Panel (klik ikon Filter)" di akhir tiap TC (panel tetap terbuka sesudah `[Apply]`), `[Clear Field]` lalu `[Apply]` untuk membersihkan filter, pembukaan dan penutupan dropdown dan overlay Column Visibility, `[Clear Field]` pada draft yang tidak di-Apply, serta penutupan Search `(←)` di akhir TC-AC-ACHA-9. Pelaku kedua TC-AC-ACHA-314 memakai sesi API aktor (bukan konteks UI kedua) sehingga tidak memakai `P-2`.
- Asersi tambahan (S-03): TC-AC-ACHA-313 `Verifikasi` tabel berada di halaman 2 sebelum Filter dipakai, supaya "kembali ke halaman 1" bermakna; TC-AC-ACHA-9 memuat `Verifikasi` tabel kosong di awal sebagai anchor (Expected a TC). Pada TC-AC-ACHA-7 klausa "No device allocations yet tidak tampil" mengandalkan anchor `No results found` pada langkah sebelumnya.
- Spec memiliki 196 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Filter Panel List) pada dataset seed dan akun yang sama; tiap TC berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna) dan semua TC kelas harness yang sama (tanpa harness tambahan); 20 TC sumber masing-masing butuh beberapa pasang `[Apply]` dan `[Clear Field]`.
- Pemisahan topik satu dataset (prinsip 1): Search, Filter Panel, Sort, Setup Column, kombinasi kontrol, dan Pagination List memakai dataset Seed List yang sama (Pre-setup #48) dan dipisah menjadi spec 036 sampai 041 karena gabungannya jauh melewati batas ukuran (spec Filter Panel ini saja 196 langkah). Pemisahan per kontrol dipertahankan karena tiap spec memulai dari kondisi default yang dipulihkan di akhir spec dan di hook `after` (tanpa Filter), sehingga kegagalan keras satu spec tidak membuat spec lain kehilangan makna; di dalam spec ini tiap TC mengakhiri dengan pemulihan state (S-09) dan tidak bergantung pada hasil TC lain, sehingga spec tetap satu (tanpa pemisah nyata: akun, kelas harness, dan dataset sama).
- Temuan untuk QA:
  - TC-AC-ACHA-314 ("Pada sesi lain buat alokasi BLE Gateway untuk Client `PT Cipta Kreasi` oleh PT ABC") tidak menyebut Quantity, Type, atau jalur; spec memakai Quantity `1` jalur langsung (Principal, Payment Free) melalui kemampuan pelaku kedua "disediakan tim FE/BE" (R-20).
  - TC-AC-ACHA-9 Expected b menyebut "tanpa reload" tanpa langkah observasi; spec tidak menyertakan muat ulang halaman dan tidak mengasersi "tanpa reload" terpisah.
  - TC-AC-ACHA-301 dan TC-AC-ACHA-312 mensyaratkan kolom Cost ditampilkan lewat Setup Column tanpa menyebut cara; spec memakai overlay Column Visibility.
  - TC-AC-ACHA-303 Expected memuat klausa "penyaringan Allocation ID dan Notes hanya lewat Search" yang merupakan kesimpulan tanpa observasi terpisah (pencarian Allocation ID dan Notes diuji di spec 036); spec menulisnya satu `Verifikasi` bersama klausa tidak adanya field.
  - TC-AC-ACHA-297 butir d ("Paid From dan Cost tersedia walau kolomnya Hidden secara default") tidak punya langkah yang menjamin kolom masih Hidden; spec bergantung pada preferensi kolom default (browser bersih, hook `after` menghapus preferensi kolom).
