---
id: TC-FA-DAMAGED-UI-103-tabel-active-seleksi-bulk
title: "Seleksi bulk sub-tab Active: checkbox Disabled dengan tooltip pada baris bukan Damaged atau berpenanda Missing, Bulk Action Bar, Selection Limit, dialog blok D-DMG-07 dan D-DMG-13, serta bulk gagal 5xx"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-07, D-DMG-13, "§4.2.4#p7", "§4.4#r13", S-DMG-08, V-DMG-02, V-DMG-08, EB-BLK-1@tabel-active, EB-BLK-4, EB-BLK-6, EB-TBL-5@checkbox-bukan-damaged, EB-TBL-5@checkbox-penanda-missing, EB-FB-2@dialog-blok-disposal, "§4.2.4#r10", "§6#p2", D-DISP-13, "§4.2.4#r11", "§9.4.2#r32"]
smoke: []
dependsOn: []
trace:
  T-DMG-01: [2, 3, 4, 5, 9, 10, 18, 20, 23, 130, 132, 133, 134]
  D-DMG-07: [49, 50, 52, 140, 141, 142, 143, 150, 151, 152, 154, 156, 164, 165, 175, 176, 186, 187]
  D-DMG-13: [63, 64, 65, 66, 69, 204, 205, 206, 207, 209]
  "§4.2.4#p7": [50, 51, 141, 142, 143]
  "§4.4#r13": [38, 53, 195, 196, 198, 204, 207]
  S-DMG-08: [36, 47]
  V-DMG-02: [12]
  V-DMG-08: [49]
  EB-BLK-1@tabel-active: [15, 16, 17, 18, 20, 21, 22, 25, 27, 31, 40, 55, 75, 76, 166, 177, 188]
  EB-BLK-4: [82, 83, 89, 90]
  EB-BLK-6: [94, 95, 96, 100, 101, 105, 106, 114, 115, 122, 124, 125, 127]
  EB-TBL-5@checkbox-bukan-damaged: [3, 4, 5, 7]
  EB-TBL-5@checkbox-penanda-missing: [9, 10, 12]
  EB-FB-2@dialog-blok-disposal: [41, 56, 67, 167, 178, 189]
  "§4.2.4#r10": [49, 50, 51, 52, 53, 55, 56]
  "§6#p2": [63, 64, 65, 69, 195, 196, 198, 204, 205, 206, 207]
  D-DISP-13: [38, 52, 64, 65, 66, 141, 142, 143]
  "§4.2.4#r11": [63, 64, 65, 66, 67, 69, 204, 205, 206, 207, 209]
  "§9.4.2#r32": [195, 196, 198, 204, 205, 206]
anchor: []
coverage:
  web: automated
---

# Seleksi bulk sub-tab Active: checkbox Disabled dengan tooltip pada baris bukan Damaged atau berpenanda Missing, Bulk Action Bar, Selection Limit, dialog blok D-DMG-07 dan D-DMG-13, serta bulk gagal 5xx

## Prerequisites
- Aktor: Total Control (Aktor Damaged).
- Layar awal: halaman Assets, tab `Damaged`, sub-tab `Active`.
- Komponen: Tabel T-DMG-01 (sub-tab Active)
- Data:
  - DU-103-1: Record `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, Status `Damaged`.
  - DU-103-2: Record `Tablet Samsung Tab A8 - 3`, Asset ID `TAB-2026-0003`, Group `Head Office`, Status `Damaged`.
  - DU-103-3: Record `Toyota Avanza - 2`, Asset ID `VEH-2026-0002`, Group `Branch Surabaya`, Status `Damaged`.
  - DU-103-4: Record `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Status `Waiting for Confirmation`.
  - DU-103-5: Record `Printer HP LaserJet M404 - 8`, Asset ID `PRN-2026-0008`, Group `Head Office`, Status `Reported Disposal`.
  - DU-103-6: Record `Monitor Dell P2422H - 6`, Asset ID `MON-2026-0006`, Group `Warehouse`, Status `In Disposal Process`.
  - DU-103-7: Record `Camera Canon EOS - 3`, Asset ID `CAM-2026-0003`, Group `Head Office`, Status `Damaged` dengan penanda `Missing`.
  - DU-103-8: Record `Drill Bosch GSB - 6`, Asset ID `DRL-2026-0006`, Group `Warehouse`, Status `Damaged` dengan penanda `Reported Missing`.
  - Tombol Select All pada K1 bernilai `Select All (3 records)` dan menjadi `Unselect All (3 records)` dari 3 record Damaged yang checkbox-nya aktif (DU-103-1 sampai DU-103-3).
  - DU-103-9: 12 record `Pallet Jack Manual - {n}` (n = 1 sampai 12), Group `Head Office`, Status `Damaged`.
  - DU-103-10: 999 record `Pallet Jack Manual - {n}` (n = 1 sampai 999), Group `Head Office`, Status `Damaged`; tombol `Unselect All (999 records)` dari 999 record yang seluruhnya terpilih.
  - DU-103-11: 1000 record `Pallet Jack Manual - {n}` (n = 1 sampai 1000), Group `Head Office`, Status `Damaged`.
  - DU-103-12: 1001 record `Pallet Jack Manual - {n}` (n = 1 sampai 1001), Group `Head Office`, Status `Damaged`.
  - DU-103-13: 1200 record `Pallet Jack Manual - {n}` (n = 1 sampai 1200), Group `Head Office`, Status `Damaged`.
  - DU-103-14: 6 record `Pallet Jack Manual - {n}` (n = 1 sampai 6), Group `Head Office`, Status `Damaged`.
  - DU-103-15: 300 record `Hand Truck Steel - {n}` (n = 1 sampai 300), Group `Warehouse`, Status `Damaged`.
  - DU-103-17: 4 record `Hydraulic Jack Steel - {n}` (n = 1 sampai 4), Group `Head Office`, Status `Damaged`.
  - DU-103-18: Record `Welding Machine Lincoln - 1`, Asset ID `WLD-2026-0001`, Group `Head Office`, Status `Waiting for Confirmation`.
  - DU-103-19: Record `Welding Machine Lincoln - 2`, Asset ID `WLD-2026-0002`, Group `Head Office`, Status `Reported Disposal`.
  - DU-103-20: Record `Welding Machine Lincoln - 3`, Asset ID `WLD-2026-0003`, Group `Head Office`, Status `In Disposal Process`.
- Kondisi:
  - K1: daftar memuat DU-103-1 sampai DU-103-8; Selection Limit bernilai `1000`; Level Feature Suite Disposal bernilai `Full`; aktor berhak menjalankan Report Disposal.
  - K2: daftar memuat 12 record pada DU-103-9 dengan ukuran halaman bawaan; Selection Limit bernilai `1000`.
  - K3: daftar memuat 999 record pada DU-103-10; Selection Limit bernilai `1000`.
  - K4: daftar memuat 1000 record pada DU-103-11; Selection Limit bernilai `1000`.
  - K5: daftar memuat 1001 record pada DU-103-12; Selection Limit bernilai `1000`.
  - K6: daftar memuat DU-103-13 dan DU-103-15 sehingga saringan Group `Head Office` menghasilkan 1200 record; Selection Limit bernilai `1000`.
  - K7: daftar memuat 6 record pada DU-103-14; Selection Limit bernilai `5`.
  - K8: daftar seperti K1; permintaan Report Disposal diterima server.
  - K9: daftar seperti K1; permintaan Report Disposal gagal karena error server.
  - K10: daftar seperti K1; permintaan Report Disposal gagal karena timeout.
  - K11: daftar seperti K1; saat dialog `D-DISP-13` dikirim, seluruh record terpilih sudah tidak Damaged.
  - K12: daftar memuat 4 record pada DU-103-17 dan DU-103-18 sampai DU-103-20; Selection Limit bernilai `5`.
  - K13: daftar memuat 12 record pada DU-103-9 dan DU-103-3 sebagai satu-satunya record Damaged lain; Selection Limit bernilai `1000`; aktor berhak menjalankan Report Disposal; daftar aset terpilih pada dialog `Cannot Report Disposal` lebih panjang daripada tinggi dialog.
  - K14: daftar seperti K1; saat `Report Disposal` pada Bulk Action diklik, DU-103-2 sudah tidak Damaged sedangkan DU-103-1 masih Damaged; permintaan Report Disposal diterima server dengan record yang tidak layak dilewati.
  - K15: daftar seperti K1; saat `Report Disposal` pada Bulk Action diklik, DU-103-1 dan DU-103-2 sudah tidak Damaged.

## Test Steps

### Checkbox Disabled pada baris bukan Damaged
1. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
2. Verifikasi checkbox baris `Projector Epson EB-X06 - 2` aktif
3. Verifikasi checkbox baris `Laptop Dell Latitude 5420 - 4` Disabled
4. Verifikasi checkbox baris `Printer HP LaserJet M404 - 8` Disabled
5. Verifikasi checkbox baris `Monitor Dell P2422H - 6` Disabled
6. Arahkan pointer ke checkbox baris `Laptop Dell Latitude 5420 - 4`
7. Verifikasi alasan `Only damaged records can be selected.` tersampaikan pada checkbox yang Disabled

### Checkbox Disabled pada baris berpenanda Missing
8. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
9. Verifikasi checkbox baris `Camera Canon EOS - 3` Disabled
10. Verifikasi checkbox baris `Drill Bosch GSB - 6` Disabled
11. Arahkan pointer ke checkbox baris `Camera Canon EOS - 3`
12. Verifikasi alasan `This asset is reported missing.` tersampaikan pada checkbox yang Disabled

### Bulk Action Bar, Select All, dan checkbox header
13. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
14. Centang baris `Projector Epson EB-X06 - 2`
15. Verifikasi tombol `Bulk Action` tampil[^drift-2]
16. Verifikasi jumlah terpilih `1` tampil pada bar
17. Verifikasi checkbox header berstatus indeterminate
18. Verifikasi tombol `Select All (3 records)` tampil dengan jumlah tidak menghitung baris yang checkbox-nya Disabled
19. Klik `Select All (3 records)`
20. Verifikasi jumlah terpilih `3` tampil pada bar
21. Verifikasi tombol `Unselect All (3 records)` tampil[^drift-1]
22. Verifikasi checkbox header tercentang
23. Verifikasi checkbox baris `Laptop Dell Latitude 5420 - 4` tidak tercentang
24. Hapus centang baris `Tablet Samsung Tab A8 - 3`
25. Verifikasi tombol `Select All (3 records)` tampil kembali
26. Klik `✕` pada bar
27. Verifikasi bar aksi massal tidak tampil

### Seleksi bertahan saat pindah halaman
28. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K2
29. Centang baris `Pallet Jack Manual - 1`
30. Klik tombol halaman `2`
31. Verifikasi jumlah terpilih `1` tetap tampil pada bar

### Bulk Report Disposal satu Group membuka dialog Reason
32. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
33. Centang baris `Projector Epson EB-X06 - 2`
34. Centang baris `Tablet Samsung Tab A8 - 3`
35. Klik `Bulk Action`[^drift-2]
36. Verifikasi item `Report Disposal` tampil dan aktif
37. Klik `Report Disposal`
38. Verifikasi dialog `D-DISP-13` terbuka dengan satu isian `Reason` untuk seluruh aset terpilih
39. Tekan `Esc`
40. Verifikasi jumlah terpilih `2` tetap tampil pada bar
41. Verifikasi tidak ada toast yang tampil

### Seleksi lintas Group diblok dialog Cannot Report Disposal
42. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
43. Centang baris `Projector Epson EB-X06 - 2`
44. Centang baris `Tablet Samsung Tab A8 - 3`
45. Centang baris `Toyota Avanza - 2`
46. Klik `Bulk Action`[^drift-2]
47. Verifikasi item `Report Disposal` tampil dan aktif walau seleksi lintas Group
48. Klik `Report Disposal`
49. Verifikasi dialog `Cannot Report Disposal` terbuka
50. Verifikasi pesan `Selected assets come from more than one group. Select assets from one group.` tampil
51. Verifikasi seluruh aset terpilih `Projector Epson EB-X06 - 2`, `Tablet Samsung Tab A8 - 3`, dan `Toyota Avanza - 2` tampil sebagai bullet tanpa diringkas
52. Verifikasi tombol `[OK]` tampil
53. Verifikasi dialog `D-DISP-13` tidak terbuka
54. Klik `[OK]`
55. Verifikasi jumlah terpilih `3` tetap tampil pada bar
56. Verifikasi tidak ada toast yang tampil

### Semua record dilewati saat Submit diblok dialog Cannot Report Disposal
57. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K11
58. Centang baris `Projector Epson EB-X06 - 2`
59. Centang baris `Tablet Samsung Tab A8 - 3`
60. Klik `Bulk Action`[^drift-2]
61. Klik `Report Disposal`
62. Kirim dialog `D-DISP-13` dengan Reason `Kerusakan tidak dapat diperbaiki`
63. Verifikasi dialog `Cannot Report Disposal` terbuka
64. Verifikasi pesan `None of the selected records can be reported for disposal.` tampil
65. Verifikasi seluruh record terpilih `Projector Epson EB-X06 - 2` dan `Tablet Samsung Tab A8 - 3` tampil sebagai bullet beserta keterangan per record tanpa diringkas
66. Verifikasi tombol `[OK]` tampil
67. Verifikasi tidak ada toast yang tampil
68. Klik `[OK]`
69. Verifikasi jumlah terpilih `2` tetap tampil pada bar

### Seleksi bersih sesudah aksi diterima server
70. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K8
71. Centang baris `Projector Epson EB-X06 - 2`
72. Klik `Bulk Action`[^drift-2]
73. Klik `Report Disposal`
74. Kirim dialog `D-DISP-13` dengan Reason `Kerusakan tidak dapat diperbaiki`
75. Verifikasi bar aksi massal tidak tampil
76. Verifikasi checkbox baris `Projector Epson EB-X06 - 2` tidak tercentang

### Bulk gagal karena timeout mempertahankan bar dan seleksi
77. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K10
78. Centang baris `Projector Epson EB-X06 - 2`
79. Klik `Bulk Action`[^drift-2]
80. Klik `Report Disposal`
81. Kirim dialog `D-DISP-13` dengan Reason `Kerusakan tidak dapat diperbaiki`
82. Verifikasi toast `Connection problem. Please try again.` tampil
83. Verifikasi bar aksi massal tetap tampil dengan jumlah terpilih `1`

### Bulk gagal karena error server mempertahankan bar dan seleksi
84. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K9
85. Centang baris `Projector Epson EB-X06 - 2`
86. Klik `Bulk Action`[^drift-2]
87. Klik `Report Disposal`
88. Kirim dialog `D-DISP-13` dengan Reason `Kerusakan tidak dapat diperbaiki`
89. Verifikasi toast error tampil
90. Verifikasi bar aksi massal tetap tampil dengan jumlah terpilih `1`

### Select All di bawah Selection Limit
91. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K3
92. Centang baris `Pallet Jack Manual - 1`
93. Klik `Select All (999 records)`
94. Verifikasi jumlah terpilih `999` tampil pada bar
95. Verifikasi tombol `Unselect All (999 records)` tampil[^drift-1]
96. Verifikasi tidak ada toast batas yang tampil

### Select All tepat di Selection Limit
97. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
98. Centang baris `Pallet Jack Manual - 1`
99. Klik `Select All (1000 records)`
100. Verifikasi jumlah terpilih `1000` tampil pada bar
101. Verifikasi tidak ada toast batas yang tampil

### Select All di atas Selection Limit dipotong ke batas
102. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K5
103. Centang baris `Pallet Jack Manual - 1`
104. Klik `Select All (1001 records)`
105. Verifikasi toast `Error, only the first 1000 of 1001 rows were selected. Narrow your filter to include the rest.` tampil
106. Verifikasi jumlah terpilih `1000` tampil pada bar

### Select All pada hasil tersaring di atas Selection Limit
107. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K6
108. Klik ikon Filter
109. Klik field `Group`
110. Centang node `Head Office`
111. Klik `[Apply]`
112. Centang baris `Pallet Jack Manual - 1`
113. Klik `Select All (1200 records)`
114. Verifikasi toast `Error, only the first 1000 of 1200 rows were selected. Narrow your filter to include the rest.` tampil
115. Verifikasi jumlah terpilih `1000` tampil pada bar

### Seleksi manual diblok di batas yang diturunkan
116. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K7
117. Centang baris `Pallet Jack Manual - 1`
118. Centang baris `Pallet Jack Manual - 2`
119. Centang baris `Pallet Jack Manual - 3`
120. Centang baris `Pallet Jack Manual - 4`
121. Centang baris `Pallet Jack Manual - 5`
122. Verifikasi checkbox baris `Pallet Jack Manual - 6` Disabled
123. Arahkan pointer ke checkbox baris `Pallet Jack Manual - 6`
124. Verifikasi alasan `You've reached the maximum selection of 5 rows.` tersampaikan pada checkbox yang Disabled
125. Verifikasi jumlah terpilih `5` tetap tampil pada bar
126. Hapus centang baris `Pallet Jack Manual - 5`
127. Verifikasi checkbox baris `Pallet Jack Manual - 6` aktif

### Baris Disabled tidak dihitung pada Selection Limit yang diturunkan
128. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K12
129. Centang baris `Hydraulic Jack Steel - 1`
130. Verifikasi tombol `Select All (4 records)` tampil
131. Klik `Select All (4 records)`
132. Verifikasi jumlah terpilih `4` tampil pada bar
133. Verifikasi tidak ada toast batas yang tampil
134. Verifikasi checkbox baris `Welding Machine Lincoln - 1`, `Welding Machine Lincoln - 2`, dan `Welding Machine Lincoln - 3` tidak tercentang

### Daftar aset dialog Cannot Report Disposal tidak diringkas dan bisa digulir
135. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K13
136. Centang baris `Toyota Avanza - 2`
137. Klik `Select All (13 records)`
138. Klik `Bulk Action`[^drift-2]
139. Klik `Report Disposal`
140. Verifikasi dialog `Cannot Report Disposal` terbuka
141. Verifikasi seluruh 13 aset terpilih `Pallet Jack Manual - 1`, `Pallet Jack Manual - 2`, `Pallet Jack Manual - 3`, `Pallet Jack Manual - 4`, `Pallet Jack Manual - 5`, `Pallet Jack Manual - 6`, `Pallet Jack Manual - 7`, `Pallet Jack Manual - 8`, `Pallet Jack Manual - 9`, `Pallet Jack Manual - 10`, `Pallet Jack Manual - 11`, `Pallet Jack Manual - 12`, dan `Toyota Avanza - 2` tampil sebagai bullet pada dialog `Cannot Report Disposal`
142. Verifikasi daftar aset pada dialog `Cannot Report Disposal` berada dalam wadah yang bisa digulir
143. Verifikasi tidak ada teks ringkasan jumlah aset pengganti daftar nama pada dialog `Cannot Report Disposal`

### Aksesibilitas dialog Cannot Report Disposal
144. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
145. Centang baris `Projector Epson EB-X06 - 2`
146. Centang baris `Tablet Samsung Tab A8 - 3`
147. Centang baris `Toyota Avanza - 2`
148. Klik `Bulk Action`[^drift-2]
149. Klik `Report Disposal`
150. Verifikasi dialog `Cannot Report Disposal` memiliki peran dialog modal yang berlabel judul `Cannot Report Disposal` untuk teknologi bantu
151. Verifikasi fokus berada pada elemen di dalam dialog `Cannot Report Disposal`
152. Verifikasi tombol tutup dialog `Cannot Report Disposal` memiliki nama aksesibel `Close dialog`
153. Tekan `Tab` sebanyak 10 kali
154. Verifikasi fokus tetap berada pada elemen di dalam dialog `Cannot Report Disposal`
155. Tekan `Shift+Tab` sebanyak 10 kali
156. Verifikasi fokus tetap berada pada elemen di dalam dialog `Cannot Report Disposal`

### Esc menutup dialog Cannot Report Disposal tanpa memproses seleksi
157. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
158. Centang baris `Projector Epson EB-X06 - 2`
159. Centang baris `Tablet Samsung Tab A8 - 3`
160. Centang baris `Toyota Avanza - 2`
161. Klik `Bulk Action`[^drift-2]
162. Klik `Report Disposal`
163. Tekan `Esc`
164. Verifikasi dialog `Cannot Report Disposal` tertutup
165. Verifikasi dialog `D-DISP-13` tidak terbuka
166. Verifikasi jumlah terpilih `3` tetap tampil pada bar
167. Verifikasi tidak ada toast yang tampil

### Klik latar gelap menutup dialog Cannot Report Disposal tanpa memproses seleksi
168. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
169. Centang baris `Projector Epson EB-X06 - 2`
170. Centang baris `Tablet Samsung Tab A8 - 3`
171. Centang baris `Toyota Avanza - 2`
172. Klik `Bulk Action`[^drift-2]
173. Klik `Report Disposal`
174. Klik latar gelap di luar dialog `Cannot Report Disposal`
175. Verifikasi dialog `Cannot Report Disposal` tertutup
176. Verifikasi dialog `D-DISP-13` tidak terbuka
177. Verifikasi jumlah terpilih `3` tetap tampil pada bar
178. Verifikasi tidak ada toast yang tampil

### Tombol tutup menutup dialog Cannot Report Disposal tanpa memproses seleksi
179. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
180. Centang baris `Projector Epson EB-X06 - 2`
181. Centang baris `Tablet Samsung Tab A8 - 3`
182. Centang baris `Toyota Avanza - 2`
183. Klik `Bulk Action`[^drift-2]
184. Klik `Report Disposal`
185. Klik tombol tutup `Close dialog` pada dialog `Cannot Report Disposal`
186. Verifikasi dialog `Cannot Report Disposal` tertutup
187. Verifikasi dialog `D-DISP-13` tidak terbuka
188. Verifikasi jumlah terpilih `3` tetap tampil pada bar
189. Verifikasi tidak ada toast yang tampil

### Sebagian record tidak layak saat klik: dialog Reason hanya berisi record yang layak
190. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K14
191. Centang baris `Projector Epson EB-X06 - 2`
192. Centang baris `Tablet Samsung Tab A8 - 3`
193. Klik `Bulk Action`[^drift-2]
194. Klik `Report Disposal`
195. Verifikasi dialog `D-DISP-13` terbuka dengan `Projector Epson EB-X06 - 2` sebagai record yang akan dilaporkan
196. Verifikasi `Tablet Samsung Tab A8 - 3` tidak termasuk dalam dialog `D-DISP-13`
197. Kirim dialog `D-DISP-13` dengan Reason `Kerusakan tidak dapat diperbaiki`
198. Verifikasi toast `Success, asset has been reported for disposal. Some items were skipped.` tampil

### Semua record tidak layak saat klik diblok dialog Cannot Report Disposal
199. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K15
200. Centang baris `Projector Epson EB-X06 - 2`
201. Centang baris `Tablet Samsung Tab A8 - 3`
202. Klik `Bulk Action`[^drift-2]
203. Klik `Report Disposal`
204. Verifikasi dialog `Cannot Report Disposal` terbuka
205. Verifikasi pesan `None of the selected records can be reported for disposal.` tampil
206. Verifikasi seluruh record terpilih `Projector Epson EB-X06 - 2` dan `Tablet Samsung Tab A8 - 3` tampil sebagai bullet beserta keterangan per record tanpa diringkas
207. Verifikasi dialog `D-DISP-13` tidak terbuka
208. Klik `[OK]`
209. Verifikasi tidak ada toast yang tampil

[^drift-1]: Drift foundation vs kontrak komponen. PRD §4.1a menyerahkan seleksi bulk pada `prd-conventions.md` §8. Foundation `prd-conventions.md` §8: «button berubah (toggle) menjadi "Unselect All"». Kontrak `BulkActionButton#41`: `Unselect All (N records)`. Diasersi: kontrak, karena label tombol dirender komponen BulkActionButton (SB-7).

[^drift-2]: Drift PRD vs foundation. PRD §4.1a Bulk Action Bar: «| Report Disposal | Disposal | dark |» (aksi tampil sebagai item tabel Bulk Action Bar). Foundation `prd-conventions.md` §8: «Button "Bulk Action" (dropdown trigger) — klik membuka overlay berisi daftar aksi». Diasersi: foundation, karena bulk bar adalah pola bersama (SB-4).
