---
id: TC-FA-FASVC-E2E-015-changelog-modal-isi-entri
title: "Changelog Gabungan: Entri per Field untuk Create, Edit, Inactivate, Activate, dan Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FASVC-LOGIC-09a", "FASVC-LOGIC-09h", "FASVC-LOGIC-01e", "§8#r6", "§8#p1", "§8#p2", "§8#r10", "§8#r11", "§8#r12", "§8#r13", "§8#r14", "§8#p4", "§8#p6", "MR-FASVC-08d", "EB-LOG-1", "EB-LOG-2", "§8#r1", "§8#r2", "§8#r3", "§8#r4", "§8#p3"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-09a": [20, 27, 57, 78, 79, 91, 92, 129, 142]
  "FASVC-LOGIC-09h": 121
  "FASVC-LOGIC-01e": 66
  "§8#r6": [17, 23, 24, 59, 60, 113, 141, 142, 165, 166, 167, 168, 170]
  "§8#p1": 121
  "§8#p2": [20, 57, 78, 79, 91, 92, 129]
  "§8#r10": 91
  "§8#r11": 92
  "§8#r12": 78
  "§8#r13": 79
  "§8#r14": [129, 130, 131, 132, 133, 174, 175, 176, 177, 178]
  "§8#p4": [23, 58, 59, 60]
  "§8#p6": [104, 105, 141, 189, 190]
  "MR-FASVC-08d": 66
  "EB-LOG-1": [61, 62, 64, 137]
  "EB-LOG-2": 67
  "§8#r1": 17
  "§8#r2": 16
  "§8#r3": [20, 21, 22, 23, 24, 25, 26, 64, 78, 165, 166, 167, 168, 169, 170, 174]
  "§8#r4": [20, 57, 78, 79, 91, 92, 129]
  "§8#p3": [20, 57, 78, 79, 129]
anchor: []
coverage:
  web: automated
---

# Changelog Gabungan: Entri per Field untuk Create, Edit, Inactivate, Activate, dan Delete

## Prerequisites
- Aktor: Total Control `Rina Wijaya` (tampil `Rina W` pada kolom Modified By), cakupan seluruh Group.
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - DU-015-1: Group `Wilayah Jawa {runId}`, anak langsung dari root pohon Group.
  - DU-015-2: Group `Cabang Barat {runId}`, anak dari `Wilayah Jawa {runId}`.
  - DU-015-3: Group `Cabang Timur {runId}`, anak dari `Wilayah Jawa {runId}`.
  - DU-015-4: Category `Mesin Industri {runId}`, induk di pohon Category.
  - DU-015-5: Category `Genset {runId}`, anak dari `Mesin Industri {runId}`.
  - DU-015-6: Category `Kompresor {runId}`, anak dari `Mesin Industri {runId}`.
  - DU-015-7: Brand `Perkins {runId}`, status Active di master.
  - DU-015-8: Brand `Atlas Copco {runId}`, status Active di master.
  - DU-015-9: Service Center `Montir Cepat {runId}`, Service type `Repair`, Available to hanya `Cabang Barat {runId}`, Country `Indonesia`, City `Bandung`, Company email `montir@montircepat.example`, Status `Active`, Usage `0`; Specialization, Brands, Notes, dan Province / State kosong.
  - DU-015-10: Service Center `Rakitan Kencana {runId}`, Service type `Routine`, Available to hanya `Cabang Barat {runId}`, City `Semarang`, Company email `rakitan@kencana.example`, Status `Active`, Usage `0`.
  - DU-015-11: Service Center `Bengkel Alfa {runId}`, Service type `Routine`, Available to `Cabang Barat {runId}`, Specialization `Genset {runId}`, Brands `Perkins {runId}`, City `Jakarta Selatan`, Company email `kontak@bengkelalfa.example`; dibuat oleh langkah spec ini.
  - DU-015-12: Berkas PDF `Sertifikat-Bengkel.pdf`, berukuran 200 KB.
  - DU-015-13: Service Center `Pusat Servis Sigma {runId}`, Service type `Routine`, City `Surabaya`, Company email `sigma@pusatservis.example`, Status `Inactive`, Available to kosong; sebelumnya Available to-nya hanya `Cabang Sementara {runId}`, lalu Group itu dihapus dari master sebelum spec dimulai sehingga perubahannya tercatat oleh `System`.
  - DU-015-14: Service Center `Bengkel Beta {runId}`, Service type `Routine`, Available to `Cabang Barat {runId}`, Country `Malaysia`, Province / State `Selangor`, City `Shah Alam`, Postal code `50480`, Address line `Jalan Pahlawan No. 8`, Company phone `+60 3555123456`, Contact persons `Budi Santoso, budi@bengkelbeta.example` dan `Sari Dewi, +60 3555009900`; dibuat oleh langkah spec ini.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif.

## Test Steps

### Create menulis entri Created per field
1. Klik ikon `Changelog` pada toolbar daftar
2. Ketik Search `Rakitan Kencana {runId}` pada modal Changelog, tekan Enter
3. Catat jumlah baris hasil Search sebagai jumlah awal entri `Rakitan Kencana {runId}`
4. Tutup modal Changelog lewat icon close
5. Klik `[+ Service Center]`
6. Isi Name `Bengkel Alfa {runId}`
7. Centang Service type `Routine`
8. Hilangkan centang `All groups` pada Available to
9. Centang `Cabang Barat {runId}` pada Available to
10. Centang `Genset {runId}` pada Specialization
11. Pilih `Perkins {runId}` pada Brands
12. Isi City `Jakarta Selatan`
13. Isi Company email `kontak@bengkelalfa.example`
14. Klik `[Submit]`
15. Klik ikon `Changelog` pada toolbar daftar
16. Verifikasi judul modal `Changelog: Service Center` tampil
17. Verifikasi tabel modal memuat header kolom `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
18. Pilih ukuran halaman `25` pada paginasi modal
19. Ketik Search `Bengkel Alfa {runId}` pada modal Changelog, tekan Enter
20. Verifikasi baris dengan Action `Created`, Service Center Name `Bengkel Alfa {runId}`, Field `Name`, Old Value `—`, dan New Value `Bengkel Alfa {runId}`
21. Verifikasi baris dengan Action `Created`, Field `Service type`, Old Value `—`, dan New Value `Routine`
22. Verifikasi baris dengan Action `Created`, Field `Available to`, Old Value `—`, dan New Value `Cabang Barat {runId}`
23. Verifikasi baris dengan Action `Created`, Field `Specialization`, dan New Value `Genset {runId}` tanpa nama induk `Mesin Industri {runId}`
24. Verifikasi baris dengan Action `Created`, Field `Brands`, dan New Value `Perkins {runId}`
25. Verifikasi baris dengan Action `Created`, Field `City`, Old Value `—`, dan New Value `Jakarta Selatan`
26. Verifikasi baris dengan Action `Created`, Field `Company email`, Old Value `—`, dan New Value `kontak@bengkelalfa.example`
27. Verifikasi Modified By pada baris dengan Action `Created` dan Field `Name` berisi `Rina W`
28. Tutup modal Changelog lewat icon close

### Edit menulis satu entri per field yang berubah dan entri lama tetap bernama snapshot setelah rename
29. Ketik Search `Bengkel Alfa {runId}` pada daftar, tekan Enter
30. Klik `⋯` pada baris `Bengkel Alfa {runId}`
31. Klik `Edit`
32. Ganti Name menjadi `Bengkel Alfa Prima {runId}`
33. Klik `[Save]`
34. Ganti isi kotak search daftar dengan `Bengkel Alfa Prima {runId}`, tekan Enter
35. Klik `⋯` pada baris `Bengkel Alfa Prima {runId}`
36. Klik `Edit`
37. Centang Service type `Repair`
38. Hilangkan centang Service type `Routine`
39. Klik `[Save]`
40. Klik `⋯` pada baris `Bengkel Alfa Prima {runId}`
41. Klik `Edit`
42. Centang `Cabang Timur {runId}` pada Available to
43. Klik `[Save]`
44. Klik `⋯` pada baris `Bengkel Alfa Prima {runId}`
45. Klik `Edit`
46. Centang `Kompresor {runId}` pada Specialization
47. Pilih `Atlas Copco {runId}` pada Brands
48. Klik `[Save]`
49. Klik `⋯` pada baris `Bengkel Alfa Prima {runId}`
50. Klik `Edit`
51. Ganti Name menjadi `Bengkel Alfa Utama {runId}`
52. Isi Notes `Mitra resmi servis genset {runId}`
53. Klik `[Save]`
54. Klik ikon `Changelog` pada toolbar daftar
55. Pilih ukuran halaman `25` pada paginasi modal
56. Ketik Search `Bengkel Alfa Prima {runId}` pada modal Changelog, tekan Enter
57. Verifikasi baris dengan Action `Updated`, Field `Service type`, Old Value `Routine`, dan New Value `Repair`
58. Verifikasi baris dengan Action `Updated`, Field `Available to`, Old Value `Cabang Barat {runId}`, dan New Value `Cabang Barat {runId}, Cabang Timur {runId}`
59. Verifikasi baris dengan Action `Updated`, Field `Specialization`, Old Value `Genset {runId}`, dan New Value `Genset {runId}, Kompresor {runId}`
60. Verifikasi baris dengan Action `Updated`, Field `Brands`, Old Value `Perkins {runId}`, dan New Value `Atlas Copco {runId}, Perkins {runId}`
61. Verifikasi baris dengan Action `Updated`, Field `Name`, Old Value `Bengkel Alfa Prima {runId}`, dan New Value `Bengkel Alfa Utama {runId}`
62. Verifikasi hasil Search memuat tepat satu baris dengan Field `Service type`
63. Ganti isi kotak search modal dengan `Mitra resmi servis genset {runId}`, tekan Enter
64. Verifikasi baris dengan Action `Updated`, Field `Notes`, Old Value `—`, dan New Value `Mitra resmi servis genset {runId}`
65. Ganti isi kotak search modal dengan `Bengkel Alfa {runId}`, tekan Enter
66. Verifikasi baris dengan Action `Created` dan Field `Name` tetap ber-Service Center Name `Bengkel Alfa {runId}` sesudah dua kali rename
67. Verifikasi baris dengan Action `Updated` dan Field `Name` tetap ber-Old Value `Bengkel Alfa {runId}` dan New Value `Bengkel Alfa Prima {runId}` sesudah rename kedua
68. Tutup modal Changelog lewat icon close

### Inactivate dan Activate menulis entri Status
69. Ganti isi kotak search daftar dengan `Bengkel Alfa Utama {runId}`, tekan Enter
70. Klik `⋯` pada baris `Bengkel Alfa Utama {runId}`
71. Klik `Inactivate`
72. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
73. Klik `⋯` pada baris `Bengkel Alfa Utama {runId}`
74. Klik `Activate`
75. Klik `[Activate]` pada dialog `Activate Service Center`
76. Klik ikon `Changelog` pada toolbar daftar
77. Ketik Search `Bengkel Alfa Utama {runId}` pada modal Changelog, tekan Enter
78. Verifikasi baris dengan Action `Inactivated`, Field `Status`, Old Value `Active`, dan New Value `Inactive`
79. Verifikasi baris dengan Action `Activated`, Field `Status`, Old Value `Inactive`, dan New Value `Active`
80. Tutup modal Changelog lewat icon close

### Lampiran ditambah dan dihapus menulis entri Attachments
81. Klik `⋯` pada baris `Bengkel Alfa Utama {runId}`
82. Klik `Edit`
83. Unggah berkas `Sertifikat-Bengkel.pdf` pada Attachments
84. Klik `[Save]`
85. Klik `⋯` pada baris `Bengkel Alfa Utama {runId}`
86. Klik `Edit`
87. Klik ikon hapus pada baris file di Attachments
88. Klik `[Save]`
89. Klik ikon `Changelog` pada toolbar daftar
90. Ketik Search `Bengkel Alfa Utama {runId}` pada modal Changelog, tekan Enter
91. Verifikasi baris dengan Action `Attachment added`, Field `Attachments`, Old Value `—`, dan New Value sama dengan nama berkas pada baris file yang diunggah
92. Verifikasi baris dengan Action `Attachment removed`, Field `Attachments`, Old Value sama dengan nama berkas pada baris file yang dihapus, dan New Value `—`
93. Tutup modal Changelog lewat icon close

### Mengosongkan Specialization dan Brands menulis entri daftar kosong
94. Klik `⋯` pada baris `Bengkel Alfa Utama {runId}`
95. Klik `Edit`
96. Hilangkan centang `Genset {runId}` pada Specialization
97. Hilangkan centang `Kompresor {runId}` pada Specialization
98. Klik (✕) pada chip `Atlas Copco {runId}` di Brands
99. Klik (✕) pada chip `Perkins {runId}` di Brands
100. Klik `[Save]`
101. Klik `[Save]` pada dialog `Widen Coverage`
102. Klik ikon `Changelog` pada toolbar daftar
103. Ketik Search `Bengkel Alfa Utama {runId}` pada modal Changelog, tekan Enter
104. Verifikasi baris dengan Action `Updated`, Field `Specialization`, Old Value `Genset {runId}, Kompresor {runId}`, dan New Value `All categories`
105. Verifikasi baris dengan Action `Updated`, Field `Brands`, Old Value `Atlas Copco {runId}, Perkins {runId}`, dan New Value `All brands`
106. Catat jumlah baris hasil Search sebagai jumlah entri `Bengkel Alfa Utama {runId}`
107. Tutup modal Changelog lewat icon close

### Edit tanpa perubahan tidak menulis entri
108. Klik `⋯` pada baris `Bengkel Alfa Utama {runId}`
109. Klik `Edit`
110. Klik `[Save]` tanpa mengubah isian
111. Klik ikon `Changelog` pada toolbar daftar
112. Ketik Search `Bengkel Alfa Utama {runId}` pada modal Changelog, tekan Enter
113. Verifikasi jumlah baris hasil Search sama dengan jumlah yang dicatat pada langkah 106
114. Tutup modal Changelog lewat icon close

### Download dan membuka Detail tidak menulis entri
115. Klik ikon `Download` pada toolbar daftar
116. Klik `Download as CSV`
117. Klik Name `Bengkel Alfa Utama {runId}` pada baris
118. Klik `Service Center` pada breadcrumb halaman Detail
119. Klik ikon `Changelog` pada toolbar daftar
120. Ketik Search `Bengkel Alfa Utama {runId}` pada modal Changelog, tekan Enter
121. Verifikasi jumlah baris hasil Search sama dengan jumlah yang dicatat pada langkah 106
122. Tutup modal Changelog lewat icon close

### Delete menulis entri Deleted per field terisi
123. Ganti isi kotak search daftar dengan `Montir Cepat {runId}`, tekan Enter
124. Klik `⋯` pada baris `Montir Cepat {runId}`
125. Klik `Delete`
126. Klik `[Delete]` pada dialog `Delete Service Center`
127. Klik ikon `Changelog` pada toolbar daftar
128. Ketik Search `Montir Cepat {runId}` pada modal Changelog, tekan Enter
129. Verifikasi baris dengan Action `Deleted`, Field `Name`, Old Value `Montir Cepat {runId}`, dan New Value `—`
130. Verifikasi baris dengan Action `Deleted`, Field `Service type`, Old Value `Repair`, dan New Value `—`
131. Verifikasi baris dengan Action `Deleted`, Field `Available to`, Old Value `Cabang Barat {runId}`, dan New Value `—`
132. Verifikasi baris dengan Action `Deleted`, Field `City`, Old Value `Bandung`, dan New Value `—`
133. Verifikasi baris dengan Action `Deleted`, Field `Company email`, Old Value `montir@montircepat.example`, dan New Value `—`
134. Tutup modal Changelog lewat icon close

### Record pembanding tidak mendapat entri
135. Klik ikon `Changelog` pada toolbar daftar
136. Ketik Search `Rakitan Kencana {runId}` pada modal Changelog, tekan Enter
137. Verifikasi jumlah baris hasil Search sama dengan jumlah yang dicatat pada langkah 3
138. Tutup modal Changelog lewat icon close

### Perubahan oleh System tercatat dengan Modified By System
139. Klik ikon `Changelog` pada toolbar daftar
140. Ketik Search `Pusat Servis Sigma {runId}` pada modal Changelog, tekan Enter
141. Verifikasi baris dengan Action `Updated`, Field `Available to`, Old Value `Cabang Sementara {runId}`, New Value `—`, dan Modified By `System`
142. Verifikasi baris dengan Action `Inactivated`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By `System`
143. Tutup modal Changelog lewat icon close

### Create menulis entri per bagian alamat, telepon perusahaan, dan kontak
144. Klik `[+ Service Center]`
145. Isi Name `Bengkel Beta {runId}`
146. Centang Service type `Routine`
147. Hilangkan centang `All groups` pada Available to
148. Centang `Cabang Barat {runId}` pada Available to
149. Pilih Country `Malaysia`
150. Isi Province / State `Selangor`
151. Isi City `Shah Alam`
152. Isi Postal code `50480`
153. Isi Address line `Jalan Pahlawan No. 8`
154. Isi Company phone dengan Dial Code `+60` dan nomor `3555123456`
155. Klik `[+ Contact person]`
156. Isi Contact name `Budi Santoso`
157. Isi Contact email `budi@bengkelbeta.example`
158. Klik `[+ Contact person]`
159. Isi Contact name pada Contact person 2 `Sari Dewi`
160. Isi Contact phone pada Contact person 2 dengan Dial Code `+60` dan nomor `3555009900`
161. Klik `[Submit]`
162. Klik ikon `Changelog` pada toolbar daftar
163. Pilih ukuran halaman `25` pada paginasi modal
164. Ketik Search `Bengkel Beta {runId}` pada modal Changelog, tekan Enter
165. Verifikasi baris dengan Action `Created`, Field `Country`, Old Value `—`, dan New Value `Malaysia`
166. Verifikasi baris dengan Action `Created`, Field `Province / State`, Old Value `—`, dan New Value `Selangor`
167. Verifikasi baris dengan Action `Created`, Field `Postal code`, Old Value `—`, dan New Value `50480`
168. Verifikasi baris dengan Action `Created`, Field `Address line`, Old Value `—`, dan New Value `Jalan Pahlawan No. 8`
169. Verifikasi baris dengan Action `Created`, Field `Company phone`, dan Old Value `—`
170. Verifikasi baris dengan Action `Created`, Field `Contact 2 · Phone`, dan Old Value `—`
171. Tutup modal Changelog lewat icon close

### Delete menulis baris Country dan tidak menulis baris untuk field yang kosong
172. Klik ikon `Changelog` pada toolbar daftar
173. Ketik Search `Montir Cepat {runId}` pada modal Changelog, tekan Enter
174. Verifikasi baris dengan Action `Deleted`, Field `Country`, Old Value `Indonesia`, dan New Value `—`
175. Verifikasi tidak ada baris dengan Action `Deleted` dan Field `Specialization`
176. Verifikasi tidak ada baris dengan Action `Deleted` dan Field `Brands`
177. Verifikasi tidak ada baris dengan Action `Deleted` dan Field `Notes`
178. Verifikasi tidak ada baris dengan Action `Deleted` dan Field `Province / State`
179. Tutup modal Changelog lewat icon close

### Specialization dan Brands yang semula kosong dicatat dengan Old Value `All categories` dan `All brands`
180. Ganti isi kotak search daftar dengan `Bengkel Alfa Utama {runId}`, tekan Enter
181. Klik `⋯` pada baris `Bengkel Alfa Utama {runId}`
182. Klik `Edit`
183. Centang `Genset {runId}` pada Specialization
184. Pilih `Perkins {runId}` pada Brands
185. Klik `[Save]`
186. Klik ikon `Changelog` pada toolbar daftar
187. Pilih ukuran halaman `25` pada paginasi modal
188. Ketik Search `Bengkel Alfa Utama {runId}` pada modal Changelog, tekan Enter
189. Verifikasi baris dengan Action `Updated`, Field `Specialization`, Old Value `All categories`, dan New Value `Genset {runId}`
190. Verifikasi baris dengan Action `Updated`, Field `Brands`, Old Value `All brands`, dan New Value `Perkins {runId}`
191. Tutup modal Changelog lewat icon close
