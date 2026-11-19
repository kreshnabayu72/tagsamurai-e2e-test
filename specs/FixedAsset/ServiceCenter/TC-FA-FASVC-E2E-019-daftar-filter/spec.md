---
id: TC-FA-FASVC-E2E-019-daftar-filter
title: "Daftar Service Center: Filter per Field, AND antar Field, OR dalam Field, dan Irisan dengan Search"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#b2", "§5#b3", "§5#b4", "EB-FLT-1@tabel-service-center", "EB-FLT-3", "EB-FLT-4@tabel-service-center", "EB-FLT-5@tabel-service-center"]
smoke: []
dependsOn: []
trace:
  "§5#b2": [39, 40, 41, 42, 117, 122, 123, 124]
  "§5#b3": [130, 140]
  "§5#b4": [116, 118, 128, 129, 134, 135, 139, 141, 146, 147]
  "EB-FLT-1@tabel-service-center": [4, 6, 8, 10, 14, 15, 20, 23, 108]
  "EB-FLT-3": [27, 28, 29, 32, 33, 34, 35, 194, 195]
  "EB-FLT-4@tabel-service-center": [46, 47, 51, 52, 56, 59, 60, 66, 67, 73, 77, 78, 79, 91, 95, 104, 155, 156, 160, 161, 165, 168, 171, 174, 177, 185]
  "EB-FLT-5@tabel-service-center": 17
anchor: []
coverage:
  web: automated
---

# Daftar Service Center: Filter per Field, AND antar Field, OR dalam Field, dan Irisan dengan Search

## Prerequisites
- Aktor: Total Control `Rina Wijaya` (cakupan seluruh Group). Aktor lain pemicu perubahan: Total Control `Gilang Saring {runId}`.
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - DU-019-1: Group `Wilayah Saring {runId}`, anak langsung dari root pohon Group.
  - DU-019-2: Group `Cabang Saring Satu {runId}`, anak dari `Wilayah Saring {runId}`.
  - DU-019-3: Group `Cabang Saring Dua {runId}`, anak dari `Wilayah Saring {runId}`.
  - DU-019-4: Group `Cabang Saring Tiga {runId}`, anak langsung dari root pohon Group.
  - DU-019-5: Category `Mesin Saring {runId}`, induk di pohon Category.
  - DU-019-6: Category `Genset Saring {runId}`, anak dari `Mesin Saring {runId}`.
  - DU-019-7: Category `Pompa Saring {runId}`, anak dari `Mesin Saring {runId}`.
  - DU-019-8: Brand `Merek Saring Satu {runId}`, status Active di master.
  - DU-019-9: Brand `Merek Saring Dua {runId}`, status Active di master.
  - DU-019-10: Brand `Merek Saring Tiga {runId}`, status Active di master dan tidak dipakai Service Center mana pun.
  - DU-019-11: User `Gilang Saring {runId}`, role Total Control, Status `Active`; tampil `Gilang S` pada kolom Modified By.
  - DU-019-12: Service Center `Saring Alfa {runId}`, Service type `Routine`, Available to `Cabang Saring Satu {runId}`, Specialization `Genset Saring {runId}`, Brands `Merek Saring Satu {runId}`, City `Kota Saring Satu {runId}`, Usage `5`, Status `Active`, Company email `alfa@saring.example`; Last Updated jatuh pada `T0`, tanggal hari run.
  - DU-019-13: Service Center `Saring Beta {runId}`, Service type `Repair`, Available to `Cabang Saring Dua {runId}`, Specialization kosong, Brands kosong, City `Kota Saring Dua {runId}`, Usage `10`, Status `Active`, Company email `beta@saring.example`; Last Updated jatuh pada `T0`, tanggal hari run.
  - DU-019-14: Service Center `Saring Gamma {runId}`, Service type `Routine, Repair`, Available to `Cabang Saring Tiga {runId}`, Specialization `Pompa Saring {runId}`, Brands `Merek Saring Dua {runId}`, City `Kota Saring Satu {runId}`, Usage `20`, Status `Inactive`, Company email `gamma@saring.example`; Last Updated jatuh pada `T0`, tanggal hari run.
  - DU-019-15: Service Center `Saring Delta {runId}`, Service type `Routine`, Available to `Cabang Saring Satu {runId}`, `Cabang Saring Dua {runId}`, Specialization `Genset Saring {runId}`, Brands `Merek Saring Satu {runId}`, `Merek Saring Dua {runId}`, City `Kota Saring Dua {runId}`, Usage `0`, Status `Active`, Company email `delta@saring.example`; Last Updated jatuh pada `T0`, tanggal hari run.
  - DU-019-16: Service Center `Saring Epsilon {runId}`, Service type `Routine`, Available to `Cabang Saring Tiga {runId}`, Specialization kosong, Brands kosong, City `Kota Saring Tiga {runId}`, Usage `0`, Status `Active`, Company email `epsilon@saring.example`; Last Updated jatuh pada `T0`, tanggal hari run.
  - DU-019-17: Service Center `Saring Eta {runId}`, Service type `Routine`, Available to `Cabang Saring Dua {runId}`, Specialization `Pompa Saring {runId}`, Brands `Merek Saring Dua {runId}`, City `Kota Saring Dua {runId}`, Usage `2`, Status `Inactive`, Company email `eta@saring.example`; Last Updated jatuh pada `T0`, tanggal hari run.
  - DU-019-18: Service Center `Saring Teta {runId}`, Service type `Routine`, Available to `All groups`, Specialization kosong, Brands kosong, City `Kota Saring Tiga {runId}`, Usage `0`, Status `Active`, Company email `teta@saring.example`; Last Updated jatuh pada `T0`, tanggal hari run.
  - DU-019-19: Service Center `Saring Zeta {runId}`, Service type `Routine`, Available to `Cabang Saring Tiga {runId}`, City `Kota Saring Baru {runId}`, Company email `zeta@saring.example`; dibuat oleh langkah spec ini.
  - DU-019-20: Parameter filter: kata kunci pelingkup `{runId}`, Usage Min `5`, Usage Max `10`, kata kunci `All categories`, kata kunci opsi `ring Dua {runId}`, `KOTA SARING TIGA {runId}`, `Zzz Tidak Ada {runId}`, `Merek Saring {runId}`, `All brands`.
  - DU-019-21: Rentang Last Updated terhadap `T0`: `T0` sampai `T0`, `T0 − 1 hari` sampai `T0 + 1 hari`, `T0` sampai `T0 + 1 hari`, `T0 − 1 hari` sampai `T0`, dan `T0 + 1 hari` sampai `T0 + 2 hari`.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif. Date Format bernilai `dd/MM/yy`. Setup Column akun `Rina Wijaya` memakai konfigurasi bawaan (semua kolom tampil).

## Test Steps

### Opsi filter City berisi nilai DISTINCT yang dapat dicari
1. Klik ikon `Filter` pada toolbar daftar
2. Klik field `City` pada panel Filter
3. Ketik `Kota Saring Satu {runId}` pada kotak cari field `City`
4. Verifikasi hanya satu opsi `Kota Saring Satu {runId}` tampil, walau dua Service Center memakai nilai itu
5. Ganti isi kotak cari field `City` dengan `ring Dua {runId}`
6. Verifikasi opsi `Kota Saring Dua {runId}` tampil
7. Ganti isi kotak cari field `City` dengan `KOTA SARING TIGA {runId}`
8. Verifikasi opsi `Kota Saring Tiga {runId}` tampil
9. Ganti isi kotak cari field `City` dengan `Zzz Tidak Ada {runId}`
10. Verifikasi teks `No results found.` tampil di daftar opsi[^drift-1]
11. Tekan Esc untuk menutup daftar opsi `City`

### Opsi filter Brands berasal dari tabel, bukan dari master, dan nilai kosong bukan opsi
12. Klik field `Brands` pada panel Filter
13. Ketik `Merek Saring {runId}` pada kotak cari field `Brands`
14. Verifikasi opsi `Merek Saring Satu {runId}` dan `Merek Saring Dua {runId}` tampil
15. Verifikasi opsi `Merek Saring Tiga {runId}` tidak tampil, karena tidak dipakai Service Center mana pun
16. Ganti isi kotak cari field `Brands` dengan `All brands`
17. Verifikasi teks `No results found.` tampil di daftar opsi, karena nilai kosong bukan opsi[^drift-1]
18. Tekan Esc untuk menutup daftar opsi `Brands`

### Opsi Service Type dan Status memuat anggota enum yang dipakai
19. Klik field `Service Type` pada panel Filter
20. Verifikasi opsi `Routine` dan `Repair` tampil
21. Tekan Esc untuk menutup daftar opsi `Service Type`
22. Klik field `Status` pada panel Filter
23. Verifikasi opsi `Active` dan `Inactive` tampil
24. Tekan Esc untuk menutup daftar opsi `Status`

### Dalam satu field berlaku OR dan antar field berlaku AND
25. Pilih `Kota Saring Satu {runId}` pada filter `City`
26. Klik `[Apply]`
27. Verifikasi baris `Saring Alfa {runId}` tampil
28. Verifikasi baris `Saring Gamma {runId}` tampil
29. Verifikasi baris `Saring Beta {runId}` tidak tampil
30. Pilih `Kota Saring Dua {runId}` pada filter `City`
31. Klik `[Apply]`
32. Verifikasi baris `Saring Beta {runId}` tampil
33. Verifikasi baris `Saring Delta {runId}` tampil
34. Verifikasi baris `Saring Eta {runId}` tampil
35. Verifikasi baris `Saring Epsilon {runId}` tidak tampil
36. Klik (✕) pada chip `Kota Saring Dua {runId}` di filter `City`
37. Pilih `Active` pada filter `Status`
38. Klik `[Apply]`
39. Verifikasi baris `Saring Alfa {runId}` tampil karena City `Kota Saring Satu {runId}` dan Status `Active`
40. Verifikasi baris `Saring Gamma {runId}` tidak tampil karena Status `Inactive`
41. Verifikasi baris `Saring Beta {runId}` tidak tampil karena City bukan `Kota Saring Satu {runId}`
42. Verifikasi baris `Saring Eta {runId}` tidak tampil karena City bukan `Kota Saring Satu {runId}` dan Status `Inactive`

### Hasil Search dan Filter adalah irisannya, apa pun urutannya, dan melepas satu saringan memulihkan hasil
43. Klik `[Clear Field]`
44. Klik `[Apply]`
45. Ketik Search `Kota Saring Satu {runId}` pada daftar, tekan Enter
46. Verifikasi baris `Saring Alfa {runId}` tampil
47. Verifikasi baris `Saring Gamma {runId}` tampil
48. Klik ikon `Filter` pada toolbar daftar
49. Pilih `Active` pada filter `Status`
50. Klik `[Apply]`
51. Verifikasi baris `Saring Alfa {runId}` tampil
52. Verifikasi baris `Saring Gamma {runId}` tidak tampil
53. Klik `[Clear Field]`
54. Pilih `Kota Saring Dua {runId}` pada filter `City`
55. Klik `[Apply]`
56. Verifikasi empty state dengan judul `No results found` dan keterangan `Try adjusting your search or filter.` tampil
57. Klik `[Clear Field]`
58. Klik `[Apply]`
59. Verifikasi baris `Saring Alfa {runId}` tampil
60. Verifikasi baris `Saring Gamma {runId}` tampil
61. Klik `(←)` pada kotak Search
62. Klik ikon `Filter` pada toolbar daftar
63. Pilih `Active` pada filter `Status`
64. Klik `[Apply]`
65. Ketik Search `Kota Saring Satu {runId}` pada daftar, tekan Enter
66. Verifikasi baris `Saring Alfa {runId}` tampil
67. Verifikasi baris `Saring Gamma {runId}` tidak tampil
68. Klik header kolom `Name`
69. Klik header kolom `Name`
70. Klik ikon `Filter` pada toolbar daftar
71. Klik `[Clear Field]`
72. Klik `[Apply]`
73. Verifikasi baris `Saring Gamma {runId}` berada di atas baris `Saring Alfa {runId}`, karena Search dan Sort `Name` descending tetap aktif sesudah filter dilepas
74. Pilih `Inactive` pada filter `Status`
75. Klik `[Apply]`
76. Klik `(←)` pada kotak Search
77. Verifikasi baris `Saring Eta {runId}` tampil
78. Verifikasi baris `Saring Alfa {runId}` tidak tampil, karena Filter Status `Inactive` tetap aktif sesudah Search dilepas
79. Verifikasi baris `Saring Gamma {runId}` berada di atas baris `Saring Eta {runId}`, karena Sort `Name` descending dan Filter Status `Inactive` tetap aktif sesudah Search dilepas
80. Klik ikon `Filter` pada toolbar daftar
81. Klik `[Clear Field]`
82. Klik `[Apply]`

### Record yang diubah atau dibuat sehingga tidak cocok tidak tampil, dan record yang diubah sehingga cocok tampil
83. Ketik Search `Kota Saring Satu {runId}` pada daftar, tekan Enter
84. Klik ikon `Filter` pada toolbar daftar
85. Pilih `Kota Saring Satu {runId}` pada filter `City`
86. Klik `[Apply]`
87. Klik `⋯` pada baris `Saring Alfa {runId}`
88. Klik `Edit`
89. Ganti City menjadi `Kota Saring Dua {runId}`
90. Klik `[Save]`
91. Verifikasi baris `Saring Alfa {runId}` tidak tampil
92. Total Control kedua `Gilang Saring {runId}` mengubah City `Saring Epsilon {runId}` menjadi `Kota Saring Satu {runId}`
93. Klik ikon `Filter` pada toolbar daftar
94. Klik `[Apply]`
95. Verifikasi baris `Saring Epsilon {runId}` tampil
96. Klik `[+ Service Center]`
97. Isi Name `Saring Zeta {runId}`
98. Centang Service type `Routine`
99. Hilangkan centang `All groups` pada Available to
100. Centang `Cabang Saring Tiga {runId}` pada Available to
101. Isi City `Kota Saring Baru {runId}`
102. Isi Company email `zeta@saring.example`
103. Klik `[Submit]`
104. Verifikasi baris `Saring Zeta {runId}` tidak tampil
105. Klik ikon `Filter` pada toolbar daftar
106. Klik field `City` pada panel Filter
107. Ketik `Kota Saring Baru {runId}` pada kotak cari field `City`
108. Verifikasi opsi `Kota Saring Baru {runId}` tampil tanpa muat ulang halaman
109. Tekan Esc untuk menutup daftar opsi `City`
110. Klik `[Clear Field]`
111. Klik `[Apply]`

### Filter tree picker mencakup descendant dan All groups, dan Specialization serta Brands menyertakan vendor kosong
112. Ganti isi kotak search daftar dengan `{runId}`, tekan Enter
113. Klik ikon `Filter` pada toolbar daftar
114. Centang `Wilayah Saring {runId}` pada filter `Available To`
115. Klik `[Apply]`
116. Verifikasi baris `Saring Alfa {runId}` tampil karena `Cabang Saring Satu {runId}` adalah descendant dari `Wilayah Saring {runId}`
117. Verifikasi baris `Saring Teta {runId}` tampil karena Available to-nya bernilai `All groups`, yang cocok dengan semua cabang
118. Verifikasi baris `Saring Gamma {runId}` tidak tampil karena `Cabang Saring Tiga {runId}` bukan descendant dari `Wilayah Saring {runId}`
119. Klik `[Clear Field]`
120. Centang `Cabang Saring Tiga {runId}` pada filter `Available To`
121. Klik `[Apply]`
122. Verifikasi baris `Saring Gamma {runId}` tampil
123. Verifikasi baris `Saring Teta {runId}` tampil
124. Verifikasi baris `Saring Alfa {runId}` tidak tampil
125. Klik `[Clear Field]`
126. Centang `Mesin Saring {runId}` pada filter `Specialization`
127. Klik `[Apply]`
128. Verifikasi baris `Saring Alfa {runId}` tampil
129. Verifikasi baris `Saring Gamma {runId}` tampil
130. Verifikasi baris `Saring Beta {runId}` tampil karena Specialization kosong berarti semua kategori[^drift-2]
131. Klik `[Clear Field]`
132. Centang `Genset Saring {runId}` pada filter `Specialization`
133. Klik `[Apply]`
134. Verifikasi baris `Saring Delta {runId}` tampil
135. Verifikasi baris `Saring Gamma {runId}` tidak tampil
136. Klik `[Clear Field]`
137. Pilih `Merek Saring Satu {runId}` pada filter `Brands`
138. Klik `[Apply]`
139. Verifikasi baris `Saring Alfa {runId}` tampil
140. Verifikasi baris `Saring Epsilon {runId}` tampil karena Brands kosong berarti semua brand[^drift-2]
141. Verifikasi baris `Saring Gamma {runId}` tidak tampil
142. Klik `[Clear Field]`
143. Pilih `Kota Saring Dua {runId}` pada filter `City`
144. Klik `[Apply]`
145. Ganti isi kotak search daftar dengan `All categories`, tekan Enter
146. Verifikasi baris `Saring Beta {runId}` tampil karena Specialization kosong tampil sebagai `All categories`
147. Verifikasi baris `Saring Delta {runId}` tidak tampil
148. Klik ikon `Filter` pada toolbar daftar
149. Klik `[Clear Field]`
150. Klik `[Apply]`

### Filter Usage memakai batas Min dan Max inklusif
151. Ganti isi kotak search daftar dengan `{runId}`, tekan Enter
152. Klik ikon `Filter` pada toolbar daftar
153. Isi Min `5` pada filter `Usage`
154. Klik `[Apply]`
155. Verifikasi baris `Saring Alfa {runId}` tampil karena Usage `5` sama dengan Min
156. Verifikasi baris `Saring Delta {runId}` tidak tampil karena Usage `0` di bawah Min
157. Klik `[Clear Field]`
158. Isi Max `10` pada filter `Usage`
159. Klik `[Apply]`
160. Verifikasi baris `Saring Beta {runId}` tampil karena Usage `10` sama dengan Max
161. Verifikasi baris `Saring Gamma {runId}` tidak tampil karena Usage `20` di atas Max
162. Klik `[Clear Field]`

### Filter Last Updated memakai rentang hari inklusif
163. Pilih rentang tanggal `T0` sampai `T0` pada filter `Last Updated`
164. Klik `[Apply]`
165. Verifikasi baris `Saring Alfa {runId}` tampil pada rentang satu hari
166. Pilih rentang tanggal `T0 − 1 hari` sampai `T0 + 1 hari` pada filter `Last Updated`
167. Klik `[Apply]`
168. Verifikasi baris `Saring Alfa {runId}` tampil pada rentang yang melingkupi `T0`
169. Pilih rentang tanggal `T0` sampai `T0 + 1 hari` pada filter `Last Updated`
170. Klik `[Apply]`
171. Verifikasi baris `Saring Alfa {runId}` tampil karena `T0` adalah batas awal rentang
172. Pilih rentang tanggal `T0 − 1 hari` sampai `T0` pada filter `Last Updated`
173. Klik `[Apply]`
174. Verifikasi baris `Saring Alfa {runId}` tampil karena `T0` adalah batas akhir rentang
175. Pilih rentang tanggal `T0 + 1 hari` sampai `T0 + 2 hari` pada filter `Last Updated`
176. Klik `[Apply]`
177. Verifikasi empty state dengan judul `No results found` tampil, karena `T0` di luar rentang
178. Klik `[Clear Field]`
179. Klik `[Apply]`

### Filter tetap berlaku walau kolomnya disembunyikan
180. Pilih `Kota Saring Satu {runId}` pada filter `City`
181. Klik `[Apply]`
182. Klik header kolom Actions (`⋯`) pada tabel daftar
183. Hilangkan centang `City` pada panel Column Visibility
184. Tekan Esc untuk menutup panel Column Visibility
185. Verifikasi baris `Saring Gamma {runId}` tampil karena Filter City tetap berlaku
186. Klik header kolom Actions (`⋯`) pada tabel daftar
187. Centang `City` pada panel Column Visibility
188. Tekan Esc untuk menutup panel Column Visibility
189. Klik ikon `Filter` pada toolbar daftar
190. Klik `[Clear Field]`
191. Klik `[Apply]`

### Filter Modified By menyaring baris menurut pengguna pengubah terakhir
192. Pilih user `Gilang Saring {runId}` pada filter `Modified By`
193. Klik `[Apply]`
194. Verifikasi baris `Saring Epsilon {runId}` tampil karena pengubah terakhirnya `Gilang Saring {runId}`
195. Verifikasi baris `Saring Alfa {runId}` tidak tampil karena pengubah terakhirnya `Rina Wijaya`
196. Klik `[Clear Field]`
197. Klik `[Apply]`

[^drift-1]: Drift PRD vs kontrak. PRD dan foundation `prd-conventions.md` §9.8: pencarian opsi dropdown filter tanpa kecocokan menampilkan teks `"No results found"` (teks saja, tanpa ilustrasi). Kontrak `MultiSelect#41`: `No results found.` (dengan titik). Diasersi: kontrak, karena bunyi bawaan komponen tidak bisa berlaku bersama bunyi PRD (SB-7).

[^drift-2]: Drift PRD vs foundation. PRD §5 Delta: «Filter Specialization dan Brands menyertakan vendor yang kosong (`All`), karena kosong berarti semua Category / brand.» Foundation `prd-conventions.md` §9.20: «Memilih opsi apa pun menyaring keluar baris yang kosong.» Diasersi: PRD, karena delta modul menyatakan penyimpangan itu.
