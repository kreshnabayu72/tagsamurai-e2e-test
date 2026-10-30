---
id: TC-GS-UCF-E2E-052-filter-panel-tabel-utama
title: "Filter Panel Tabel Utama Custom Field: Screening, Logika OR dan AND, Chip, Opsi Dinamis, Draft, Clear Field, dan Retensi F5"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-201
  - TC-GS-UCF-202
  - TC-GS-UCF-203
  - TC-GS-UCF-204
  - TC-GS-UCF-205
  - TC-GS-UCF-206
  - TC-GS-UCF-207
  - TC-GS-UCF-208
  - TC-GS-UCF-209
  - TC-GS-UCF-210
  - TC-GS-UCF-211
  - TC-GS-UCF-212
  - TC-GS-UCF-213
  - TC-GS-UCF-221
  - TC-GS-UCF-351
  - TC-GS-UCF-352
  - TC-GS-UCF-353
  - TC-GS-UCF-354
  - TC-GS-UCF-397
coverage:
  web: automated
---

# Filter Panel Tabel Utama Custom Field: Screening, Logika OR dan AND, Chip, Opsi Dinamis, Draft, Clear Field, dan Retensi F5

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Untuk TC-GS-UCF-206 dan TC-GS-UCF-353 spec berganti ke Total Control Client B (Lina Kusuma, Modified By `Lina K`) `totalControl_automated_qaTeam2@qwertysystem.net` dengan `Spectra.env.GS_CLIENTB_TC_PASSWORD` lewat langkah ganti akun eksplisit (langkah 158); hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`):
  - `Cost Center`: Dropdown `Finance`, `Operations`, `Marketing`; Required Yes; Active; Modified By `Budi S`; Last Updated 11 Sep 2026.
  - `Employee Grade`: Text; Required No; Active; `Siti R`; 10 Sep 2026.
  - `Job Description`: Text Area; Required No; Active; `Siti R`; 10 Sep 2026.
  - `Bonus`: Numeric Decimal Places 2; Required No; Active; `Budi S`; 9 Sep 2026.
  - `Office Phone`: Phone; Required Yes; Active; `Budi S`; 9 Sep 2026.
  - `Joining Date`: Date; Required No; Inactive; `Budi S`; 9 Sep 2026.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type` (Dropdown), `Shirt Size` (Dropdown), `Emergency Phone` (Phone), `Birth Date` (Date), `Tax ID` (Text; Required Yes), `Work Notes` (Text Area), `Annual Target` (Numeric), `badge number` (Text); Required No kecuali `Tax ID`; Active; Modified By `Sari D`; Last Updated hari seeding (di luar rentang 9 sampai 11 Sep 2026). Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme disediakan tim FE/BE, endpoint tidak ditulis di spec). Nama literal tanpa suffix karena asersi jumlah 14 baris, nama baris, dan opsi dropdown bergantung pada nama (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini. Total Custom Field Client A tepat 14 saat spec berjalan.
- Data Pre-setup Client B (tetap di environment, tidak diubah spec ini): 10 Custom Field bertipe Text, seluruhnya Active, Required `No`, Modified By `Lina K` (fixture backend; disediakan tim FE/BE). Dipakai TC-GS-UCF-206 dan TC-GS-UCF-353. `Client B Eleven` (D-87, field ke-11) bukan data Pre-setup: Data Dinamis milik spec 055 (di-seed idempotent di spec 055 dan dihapus sendiri oleh TC-GS-UCF-233); spec ini tidak membaca dan tidak bergantung pada Eleven (keputusan K-9 B, 2026-10-29).
- Data Dinamis milik spec: `Client B Pick {runId}-052` (Dropdown dengan value `One`) dibuat oleh langkah UI TC-GS-UCF-353 pada Client B; fixture baru `Fixture.customFieldUser.filterSeed052`. TC-GS-UCF-206 dan TC-GS-UCF-353 tidak bergantung pada hasil TC-GS-UCF-233 (spec 055).
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field (Client A); spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`. Setelah ganti akun ke Client B (langkah 158), halaman dibuka lewat langkah eksplisit.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Client B Pick {runId}-052` dan field Population yang dibuat hook `before`; kembalikan sesi ke Total Control Client A; pulihkan ukuran halaman ke 10, ukuran viewport, dan filter yang masih ter-Apply.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor Client A dan Client B dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pembacaan chip, state centang opsi dropdown, indikator titik pada ikon Filter, dan nilai rentang Last Updated; mengubah ukuran viewport (1024px) dan memulihkannya; `Spectra.intercept()` untuk menunda respons opsi Filter (TC-GS-UCF-354), dilepas segera setelah pemicu (S-09); muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka saat F5).
- General Settings Date Format Client A tidak diubah spec ini; tanggal rentang Last Updated diinput dan dibaca sesuai format yang berlaku.
- State global: ukuran halaman diubah ke 25 (langkah 1) dan dikembalikan ke 10 (langkah 157); viewport 1024px (langkah 70) dipulihkan (langkah 77). Filter Panel selalu dikosongkan kembali lewat `[Clear Field]` dan `[Apply]` pada akhir tiap blok TC.

## Test Steps

### Persiapan

1. Ubah ukuran halaman tabel ke 25

### TC-GS-UCF-201: Screening Filter Panel

2. Klik Filter
3. Verifikasi field `Active` berupa multi-select searchable dengan placeholder "All statuses"
4. Verifikasi field `Data Type` berupa multi-select searchable dengan placeholder "All data types"
5. Verifikasi field `Required` berupa multi-select searchable dengan placeholder "All required"
6. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder "All users"
7. Verifikasi field `Last Updated` berupa date range picker dengan placeholder "Select date"
8. Verifikasi tombol `[Clear Field]` (text) di kiri dan tombol `[Apply]` (filled) di kanan
9. Verifikasi icon Filter menjadi gelap saat panel terbuka
10. Klik icon Filter untuk menutup panel

### TC-GS-UCF-202: Filter per kelas dropdown multi-select

11. Klik Filter
12. Buka dropdown Active, pilih `Inactive`, klik [Apply]
13. Verifikasi tabel menampilkan tepat satu baris `Joining Date`
14. Klik [Clear Field]
15. Buka dropdown Data Type, pilih `Dropdown`, klik [Apply]
16. Verifikasi tabel menampilkan tepat tiga baris: `Blood Type`, `Cost Center`, dan `Shirt Size`
17. Klik [Clear Field]
18. Buka dropdown Required, pilih `Yes`, klik [Apply]
19. Verifikasi tabel menampilkan tepat tiga baris: `Cost Center`, `Office Phone`, dan `Tax ID`
20. Klik [Clear Field]
21. Buka dropdown Modified By, pilih `Siti R`, klik [Apply]
22. Verifikasi tabel menampilkan tepat dua baris: `Employee Grade` dan `Job Description`
23. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-203: Dua opsi dalam satu field berlogika OR

24. Klik Filter
25. Pilih Data Type `Date` dan `Phone`
26. Verifikasi dua chip `Date` dan `Phone` berada di dalam field Data Type
27. Klik [Apply]
28. Verifikasi tabel menampilkan tepat empat baris: `Birth Date`, `Joining Date`, `Emergency Phone`, dan `Office Phone`
29. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-204: Kombinasi dua field filter berlogika AND

30. Klik Filter
31. Pilih Data Type `Dropdown` dan Required `Yes`
32. Klik [Apply]
33. Verifikasi tabel menampilkan tepat satu baris `Cost Center`
34. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-205: Filter Last Updated rentang tanggal inklusif

35. Klik Filter
36. Pilih Last Updated 10 Sep 2026 sampai 10 Sep 2026
37. Verifikasi input rentang Last Updated menampilkan tanggal sesuai Date Format General Settings
38. Klik [Apply]
39. Verifikasi tabel menampilkan tepat dua baris: `Employee Grade` dan `Job Description`
40. Ganti rentang Last Updated menjadi 9 Sep 2026 sampai 10 Sep 2026, klik [Apply]
41. Verifikasi tabel menampilkan tepat lima baris: `Bonus`, `Office Phone`, `Joining Date`, `Employee Grade`, dan `Job Description` (batas inklusif)
42. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-207: Search di dalam dropdown filter

43. Klik Filter
44. Buka dropdown Active, ketik `inac`
45. Verifikasi dropdown Active menampilkan tepat satu opsi `Inactive`
46. Buka dropdown Data Type, ketik `PH`
47. Verifikasi dropdown Data Type menampilkan tepat satu opsi `Phone`
48. Buka dropdown Required, ketik `ye`
49. Verifikasi dropdown Required menampilkan tepat satu opsi `Yes`
50. Buka dropdown Modified By, ketik `sar`
51. Verifikasi dropdown Modified By menampilkan tepat satu opsi `Sari D`
52. Verifikasi pencarian internal dropdown tidak memfilter tabel sebelum [Apply] (tabel masih 14 baris)
53. Klik icon Filter untuk menutup panel

### TC-GS-UCF-208: Hapus chip lewat (✕) meng-uncheck opsinya

54. Klik Filter
55. Pilih Data Type `Date`, `Phone`, dan `Text`
56. Klik `(✕)` pada chip `Phone`
57. Verifikasi chip `Phone` hilang
58. Verifikasi chip `Date` dan `Text` tetap tampil
59. Buka dropdown Data Type
60. Verifikasi checkbox `Phone` ter-uncheck
61. Klik [Apply]
62. Verifikasi tabel menampilkan tepat lima baris: `Birth Date`, `Joining Date`, `badge number`, `Employee Grade`, dan `Tax ID`
63. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-209: Uncheck opsi di dropdown menghapus chip

64. Klik Filter
65. Pilih Data Type `Date`, `Phone`, dan `Text`
66. Buka dropdown Data Type, uncheck `Date`
67. Verifikasi chip `Date` hilang dari field
68. Verifikasi chip `Phone` dan `Text` tetap tampil
69. Klik icon Filter untuk menutup panel (draft tidak di-Apply)

### TC-GS-UCF-210: Banyak chip diringkas menjadi chip +N more

70. Atur lebar viewport 1024px
71. Klik Filter
72. Pilih seluruh enam opsi Data Type: `Text`, `Text Area`, `Dropdown`, `Date`, `Numeric`, `Phone`
73. Verifikasi chip yang tidak muat diringkas dalam satu chip `+N more`
74. Verifikasi jumlah chip tampil ditambah N sama dengan 6
75. Verifikasi field Data Type tidak melebar keluar panel
76. Klik icon Filter untuk menutup panel
77. Pulihkan lebar viewport ke ukuran semula

### TC-GS-UCF-211: Menutup Filter Panel tanpa Apply membuang draft

78. Klik Filter
79. Pilih Data Type `Phone`, klik [Apply]
80. Verifikasi tabel menampilkan tepat dua baris: `Emergency Phone` dan `Office Phone`
81. Pilih juga Data Type `Date` tanpa [Apply]
82. Klik ulang icon Filter untuk menutup panel
83. Verifikasi tabel tetap menampilkan tepat dua baris hasil Phone: `Emergency Phone` dan `Office Phone`
84. Klik icon Filter untuk membuka kembali panel
85. Verifikasi chip `Phone` tampil di field Data Type
86. Verifikasi chip `Date` tidak ada di field Data Type (draft dibuang)
87. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-212: Clear Field mengosongkan kriteria dan Apply memulihkan seluruh baris

88. Klik Filter
89. Pilih Data Type `Phone`, klik [Apply]
90. Klik [Clear Field]
91. Verifikasi field Active kosong
92. Verifikasi field Data Type kosong
93. Verifikasi field Required kosong
94. Verifikasi field Modified By kosong
95. Verifikasi field Last Updated kosong
96. Klik [Apply]
97. Verifikasi tabel kembali menampilkan 14 baris
98. Klik icon Filter untuk menutup panel

### TC-GS-UCF-213: Ikon Filter menampilkan titik indikator

99. Klik Filter
100. Pilih Required `Yes`, klik [Apply]
101. Klik icon Filter untuk menutup panel
102. Verifikasi titik indikator tampil di ikon Filter saat panel tertutup
103. Klik Filter
104. Klik [Clear Field], klik [Apply]
105. Verifikasi titik indikator hilang dari ikon Filter
106. Klik icon Filter untuk menutup panel

### TC-GS-UCF-221: Opsi filter tidak dipersempit oleh filternya sendiri

107. Klik Filter
108. Pilih Data Type `Text`, klik [Apply]
109. Buka dropdown Data Type
110. Verifikasi dropdown Data Type tetap menawarkan keenam tipe: `Text`, `Text Area`, `Dropdown`, `Date`, `Numeric`, dan `Phone`
111. Buka dropdown Required
112. Verifikasi dropdown Required menawarkan tepat dua opsi `Yes` dan `No` (dari field Text: `Tax ID` Yes; `badge number` dan `Employee Grade` No)
113. Buka dropdown Modified By
114. Verifikasi dropdown Modified By menawarkan tepat dua opsi `Sari D` dan `Siti R` (pelaku field Text)
115. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-351: Refresh F5 mempertahankan Filter Panel yang diterapkan

116. Klik Filter
117. Pilih Data Type `Phone`, klik [Apply]
118. Tekan F5
119. Verifikasi ikon Filter tampil pada Table Tools (halaman termuat ulang)
120. Verifikasi icon Filter menampilkan indikator filter aktif
121. Verifikasi tabel menampilkan tepat dua baris: `Emergency Phone` dan `Office Phone`
122. Klik Filter
123. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-352: Chip Active, Required, dan Modified By

124. Klik Filter
125. Buka dropdown Active, pilih `Active` dan `Inactive`, klik `(✕)` pada chip `Inactive`
126. Verifikasi `(✕)` menghapus chip `Inactive`
127. Verifikasi opsi `Inactive` ter-uncheck
128. Verifikasi chip `Active` tetap tampil
129. Buka dropdown Required, pilih `Yes` dan `No`, lalu uncheck `Yes` di dalam dropdown
130. Verifikasi chip `Yes` hilang
131. Verifikasi chip `No` tetap tampil
132. Buka dropdown Modified By, pilih `Budi S` dan `Siti R`, klik `(✕)` pada chip `Budi S`
133. Verifikasi `(✕)` menghapus chip `Budi S`
134. Verifikasi opsi `Budi S` ter-uncheck
135. Verifikasi chip `Siti R` tetap tampil
136. Klik [Apply]
137. Verifikasi tabel menampilkan tepat dua baris: `Employee Grade` dan `Job Description` (AND antar field, OR dalam satu field)
138. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-354: Indikator loading pada dropdown opsi Filter

139. Pasang intercept yang menunda respons opsi Filter (network throttling)
140. Klik Filter
141. Buka dropdown Modified By
142. Verifikasi dropdown menampilkan indikator loading selama opsi dimuat
143. Verifikasi opsi `Budi S`, `Siti R`, dan `Sari D` tampil setelah opsi dimuat
144. Lepas intercept pada respons opsi Filter
145. Klik icon Filter untuk menutup panel

### TC-GS-UCF-397: Empty state hasil Filter tanpa Search

146. Klik Filter
147. Buka dropdown Active, pilih `Inactive`
148. Buka dropdown Required, pilih `Yes`
149. Klik [Apply]
150. Verifikasi Illustration tampil
151. Verifikasi Title "No results found"
152. Verifikasi Description "Try adjusting your search or filter."
153. Verifikasi tabel tidak menampilkan baris
154. Verifikasi Search tetap kosong
155. Verifikasi icon Filter menampilkan indikator filter aktif (badge titik)
156. Klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel
157. Ubah ukuran halaman tabel kembali ke 10

### Ganti akun ke Total Control Client B

158. Ganti akun: Logout, lalu login sebagai Total Control Client B (Lina Kusuma) `totalControl_automated_qaTeam2@qwertysystem.net`
159. Buka Global Settings > User > Custom Field

### TC-GS-UCF-206: Opsi dropdown filter di-populate dari data tabel saat ini

160. Klik Filter
161. Buka dropdown Active
162. Verifikasi dropdown Active menawarkan tepat satu opsi `Active`
163. Buka dropdown Data Type
164. Verifikasi dropdown Data Type menawarkan tepat satu opsi `Text`
165. Buka dropdown Required
166. Verifikasi dropdown Required menawarkan tepat satu opsi `No`
167. Buka dropdown Modified By
168. Verifikasi dropdown Modified By menawarkan tepat satu opsi `Lina K`
169. Klik icon Filter untuk menutup panel

### TC-GS-UCF-353: Opsi Data Type bertambah setelah field bertipe baru dibuat

170. Klik Filter, buka dropdown Data Type
171. Verifikasi dropdown Data Type hanya memuat `Text`
172. Klik icon Filter untuk menutup panel
173. Klik [+ Custom Field]
174. Isi Field Name `Client B Pick {runId}-052`
175. Pilih Data Type `Dropdown`
176. Ketik value `One`, tekan Enter
177. Klik [Submit]
178. Tunggu aksi selesai
179. Klik Filter, buka dropdown Data Type
180. Verifikasi dropdown Data Type memuat `Text`
181. Verifikasi dropdown Data Type memuat `Dropdown`
182. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 182 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu topik dan satu dataset (Filter Panel tabel utama), tanpa mengubah data Pre-setup atau Population; tiap blok TC dimulai dari Filter Panel kosong dan tetap bermakna bila blok lain gagal. Bagian Client B (langkah 158 sampai 182) memakai Step ganti akun eksplisit dan tetap bermakna walau bagian Client A gagal keras (bagian 3 konvensi, pengecualian beda akun); TC-GS-UCF-353 membuat data sehingga ditaruh paling akhir.
- Urutan TC tidak mengikuti urutan nomor TC sumber: TC-GS-UCF-206 dan TC-GS-UCF-353 (Client B) ditaruh di akhir karena butuh ganti akun dan TC-GS-UCF-353 membuat data; TC-GS-UCF-397 (Filter kosong) dan TC-GS-UCF-354 (menunda respons opsi) ditaruh setelah blok Client A lain agar tidak mengganggu asersi jumlah 14 baris.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 157 (ukuran halaman 25 agar 14 baris tampil pada satu halaman, lalu dikembalikan ke 10); langkah 10, 23, 29, 34, 42, 53, 63, 69, 76, 87, 98, 101, 106, 115, 123, 138, 145, 156, 169, dan 182 (menutup Filter Panel dan atau mengosongkan Filter dengan `[Clear Field]` lalu `[Apply]` sebelum TC berikutnya); langkah 14, 17, dan 20 (`[Clear Field]` di antara kelas filter pada TC-GS-UCF-202, sesuai "Kosongkan" pada langkah TC); langkah 70 dan 77 (viewport 1024px dan pemulihannya); langkah 139 dan 144 (pasang dan lepas intercept); langkah 158 dan 159 (ganti akun dan buka halaman Client B); langkah 178 (tunggu aksi selesai sebelum membuka Filter).
- Model panel: TC tidak menyatakan apakah Filter Panel tetap terbuka sesudah `[Apply]`. TC-GS-UCF-211 dan 213 ("Tutup panel" sesudah Apply) menyiratkan tetap terbuka, sedangkan TC-GS-UCF-505 sampai 507 menulis "Klik Filter" lagi. Spec memperlakukan panel tetap terbuka sesudah `[Apply]` dan menutupnya lewat klik icon Filter sebelum aksi di luar panel (lihat Temuan untuk QA).
- Verifikasi tambahan di luar Expected TC (anchor positif, S-03): langkah 80 (hasil Phone tampil sebelum `Date` dipilih sebagai draft pada TC-GS-UCF-211) menjadi pembanding untuk langkah 83; langkah 119 (halaman termuat sesudah F5) menjadi anchor sebelum asersi keadaan filter; langkah 171 (dropdown hanya memuat `Text`) berasal dari Expected a TC-GS-UCF-353; langkah 120 (icon Filter menampilkan indikator filter aktif) bukan bagian Expected TC-GS-UCF-351, dipertahankan sebagai bukti filter masih aktif sesudah muat ulang (S-03).
- TC-GS-UCF-206 dan TC-GS-UCF-353 mencantumkan dependensi TC-GS-UCF-233 (Client B memiliki 11 field); spec ini tidak bergantung pada TC-GS-UCF-233 dan hanya membaca 10 field Pre-setup Client B, tanpa `Client B Eleven` (Data Dinamis milik spec 055, yang men-seed dan menghapusnya sendiri). TC-GS-UCF-233 ada di spec 055.
- Pembagian TC lintas spec: Search tabel utama (TC-GS-UCF-10, 190 sampai 200, 311, 379, 510) ada di spec 051; kombinasi Search, Filter, Sort, dan Pagination (TC-GS-UCF-214 sampai 220, 231, 504 sampai 507) di spec 053; Sort di spec 054; Setup Column di spec 056.
- Temuan untuk QA:
  - TC tidak konsisten soal Filter Panel sesudah `[Apply]` (tetap terbuka atau menutup): TC-GS-UCF-213 langkah 2 dan TC-GS-UCF-211 langkah 3 menutup panel secara eksplisit, sedangkan TC-GS-UCF-212 langkah 2 langsung `[Clear Field]` tanpa membuka ulang dan TC-GS-UCF-505 langkah 4 menulis "Klik Filter". Spec mengasumsikan tetap terbuka.
  - TC-GS-UCF-202 langkah 2 sampai 4 menulis "Kosongkan" tanpa menyebut cara; spec memakai `[Clear Field]` lalu memilih opsi berikutnya dan `[Apply]`.
  - TC-GS-UCF-205 tidak menyebut cara memilih tanggal dan teks tanggal literal sesuai Date Format; spec memilih lewat date picker dan mengasersi tampilan format yang berlaku.
  - TC-GS-UCF-210 tidak menyebut lebar viewport awal; spec memulihkan ke ukuran semula sesudah blok.
  - TC-GS-UCF-354 tidak menyebut durasi penundaan respons opsi Filter dan endpoint-nya; intercept dan durasi disediakan tim FE.
  - Keputusan NC yang berbeda dari API/LLD (NC-24): TC-GS-UCF-221 mengharapkan opsi Data Type tidak dipersempit oleh filternya sendiri (exclude-self); LLD `/options` mempersempit facet oleh filternya sendiri. Asersi mengikuti TC dan PRD; langkah 110 dapat gagal pada backend nyata sampai LLD diselaraskan.
  - TC-GS-UCF-206 dan TC-GS-UCF-353 mencantumkan field `Client B Field` dan "field Text lainnya" tanpa menyebut nama 10 field lain; spec hanya mengasersi opsi dropdown dan tidak memakai nama field Client B.
  - TC-GS-UCF-353 langkah 3 tidak menyebut apakah popup Create tertutup sesudah `[Submit]` (checkbox Stay tidak dicentang); spec menunggu aksi selesai (langkah 178) sebelum membuka Filter.
  - Email akun Total Control Client B diambil dari Tabel Data Uji Pre-setup TC (`totalControl_automated_qaTeam2@qwertysystem.net`); nama env `GS_CLIENTB_TC_PASSWORD` sudah terdaftar di `.env.example`.
  - Post Condition TC-GS-UCF-353 menyebut `Client B Pick (Client B)` tanpa langkah observasi; tidak diasersi. Data dihapus lewat hook `after`.
