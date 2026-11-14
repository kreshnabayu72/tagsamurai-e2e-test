---
id: TC-FA-MISS-E2E-004-tab-active-filter
title: "Tab Active: opsi filter DISTINCT, hasil saringan per field, kombinasi dengan Search, dan filter Long missing"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-FLT-1@tabel-active, EB-FLT-4@tabel-active, EB-FLT-5@tabel-active, §4.1a#p1, §9.2#b14, §9.5#r9, §4.1#p5, EB-FLT-3]
smoke: [EB-FLT-3]
dependsOn: []
trace:
  EB-FLT-1@tabel-active: [5, 8, 11, 17, 19, 21, 23, 29, 34, 80, 125, 138]
  EB-FLT-4@tabel-active: [52, 53, 56, 60, 65, 68, 133, 136, 149, 164, 168]
  EB-FLT-5@tabel-active: [17, 77]
  §4.1a#p1: [5, 39, 73]
  §9.2#b14: 8
  §9.5#r9: 3
  §4.1#p5: [11, 14]
  EB-FLT-3: [39, 40, 44, 45, 46, 47, 84, 89, 93, 97, 101, 106, 110, 114, 118, 154, 155]
anchor: [27, 32, 123, 143]
coverage:
  web: automated
---

# Tab Active: opsi filter DISTINCT, hasil saringan per field, kombinasi dengan Search, dan filter Long missing

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets, tab Missing, sub-tab Active.
- Data:
  - DU-004-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-004-2: Karyawan `Gita Permata {runId}` tanpa akun, memegang aset sehingga PIC-nya yang melapor atas namanya.
  - DU-004-3: User `Rudi Hartono {runId}`, pemegang (Borrower) yang menjadi PIC `Gita Permata {runId}`, tanpa hak Aktor Missing.
  - DU-004-4: User `Hari Santoso {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing.
  - DU-004-5: User `Indra Kusuma {runId}`, role Group Manager pada Group `Gedung B {runId}`.
  - DU-004-6: User `Kirana Putri {runId}`, role Manage asset & TAG (Read), yang tidak menjadi Last Holder maupun pelapor record mana pun.
  - DU-004-7: Record `Waiting for Confirmation` untuk aset `Unit Alfa {runId}` (Group `Gedung A {runId}`, tanpa Brand, Purchase Cost `1000000`), Source `Reported by holder`, Last Holder `Gita Permata {runId}`, Reported By PIC `Rudi Hartono {runId}` atas nama `Gita Permata {runId}`, Reported Date T0 − 1 hari pukul `07:15`.
  - DU-004-8: Record `Missing` untuk aset `Unit Beta {runId}` (Group `Gedung A {runId}`, TAG `RFID`, Brand `Merk Alfa {runId}`, Purchase Cost `2000000`), Source `Borrow`, Last Holder `Hari Santoso {runId}`, pemindai terakhir reader `Gate B reader {runId}` pada T0 − 13 hari, Reported By `Hari Santoso {runId}`, Reported Date T0 − 10 hari pukul `09:00`.
  - DU-004-9: Record `Missing` untuk aset `Unit Gamma {runId}` (Group `Gedung B {runId}`, TAG `RFID`, Brand `Merk Beta {runId}`, Purchase Cost `3000000`), Source `Borrow`, Last Holder `Hari Santoso {runId}`, pemindai terakhir reader `Gate B reader {runId}` pada T0 − 15 hari, Reported By `Indra Kusuma {runId}`, Reported Date T0 − 12 hari pukul `09:00`.
  - DU-004-10: Record `Missing` untuk aset `Unit Delta {runId}` (Group `Gedung B {runId}`, Brand `Merk Gamma {runId}`, Purchase Cost `4000000`), Source `Manual`, tanpa Last Holder, Reported By `Indra Kusuma {runId}`, Reported Date T0 − 35 hari pukul `09:00`; Days Missing `35 days` melewati Long missing after sehingga memuat penanda `Long missing`.
  - DU-004-11: Record `Reported Disposal` untuk aset `Unit Epsilon {runId}` (Group `Gedung A {runId}`, Brand `Merk Delta {runId}`, Purchase Cost `5000000`), Source `Borrow`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 40 hari pukul `09:00`.
  - DU-004-12: Record `Missing` untuk aset `Unit Zeta {runId}` (Group `Gedung C {runId}`, Brand `Merk Epsilon {runId}`, Purchase Cost `6000000`), Source `Transfer`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 5 hari pukul `09:00`.
  - DU-004-13: Record `Missing` untuk aset `Unit Eta {runId}` (Group `Gedung C {runId}`, Brand `Merk Zeta {runId}`, Purchase Cost `7000000`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 7 hari pukul `09:00`, tanpa pembaruan sehingga Last Updated sama dengan Reported Date; record ini yang diberi Add Update agar keluar dari saringan Last Updated lama.
  - DU-004-14: Record `Missing` untuk aset `Unit Theta {runId}` (Group `Gedung C {runId}`, Brand `Merk Eta {runId}`, Purchase Cost `8000000`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 2 hari pukul `09:00`, tanpa pembaruan sehingga Last Updated sama dengan Reported Date; record ini yang diberi Add Update agar masuk ke saringan Last Updated hari ini.
  - DU-004-15: Record `In Disposal Process` untuk aset `Unit Iota {runId}` (Group `Gedung A {runId}`, Brand `Merk Theta {runId}`, Purchase Cost `9000000`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 60 hari pukul `09:00`.
  - DU-004-16: Update `Pemeriksaan ruang arsip dimulai {runId}` yang dibuat aktor pada record DU-004-14.
  - DU-004-17: Update `Pemeriksaan gudang cadangan selesai {runId}` yang dibuat aktor pada record DU-004-13.
  - DU-004-18: kata kunci pencarian opsi `psil`, potongan dari tengah Brand `Merk Epsilon {runId}`.
  - DU-004-19: kata kunci pencarian opsi `merk gamma {runId}`, Brand `Merk Gamma {runId}` dengan huruf kapital berbeda.
  - DU-004-20: kata kunci pencarian opsi `zzzopsi`, yang tidak cocok dengan opsi mana pun.
  - DU-004-21: kata kunci Search `{runId} tidakada` yang tidak cocok dengan kolom mana pun.
  - DU-004-22: rentang Reported Date dari T0 − 11 hari sampai T0 − 6 hari, memuat DU-004-8 dan DU-004-13 di dalamnya.
  - DU-004-23: rentang Reported Date dari T0 − 12 hari sampai T0 − 10 hari; DU-004-9 tepat di hari awal dan DU-004-8 tepat di hari akhir.
  - DU-004-24: rentang Reported Date dari T0 − 10 hari sampai T0 − 10 hari, satu hari saja.
  - DU-004-25: rentang Reported Date dari T0 − 30 hari sampai T0 − 20 hari, yang tidak memuat record DU-004-7 sampai DU-004-15.
  - DU-004-26: rentang Last Updated dari T0 sampai T0, hanya hari ini.
  - DU-004-27: rentang Last Updated dari T0 − 8 hari sampai T0 − 6 hari.
  - DU-004-28: rentang Purchase Cost Min `3000000` dan Max `5000000`; DU-004-9 tepat di Min dan DU-004-11 tepat di Max.
  - DU-004-29: rentang Purchase Cost hanya Min `8000000`.
  - DU-004-30: rentang Purchase Cost hanya Max `2000000`.
  - DU-004-31: rentang Purchase Cost dengan Min `9000000` lebih besar dari Max `1000000`.
  - DU-004-32: rentang Last Seen dari T0 − 14 hari sampai T0 − 12 hari; pemindaian DU-004-8 berada di dalamnya dan pemindaian DU-004-9 di luarnya.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - Long missing after bernilai `30`.
  - T0 adalah waktu spec dijalankan; tanggal pada entri di atas dihitung relatif terhadap T0.
  - Record DU-004-7 sampai DU-004-15 dibuat tanpa entri Changelog sehingga Modified By-nya `System`.

## Test Steps

### Filter Panel terbuka tanpa saringan bawaan
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon Filter
3. Verifikasi tidak ada field Filter Panel yang berisi nilai ter-Apply dan ikon Filter tidak berbadge titik

### Opsi filter berisi nilai DISTINCT dari baris tabel
4. Buka field `Status`
5. Verifikasi opsi field `Status` memuat tepat `Waiting for Confirmation`, `Missing`, `Reported Disposal`, dan `In Disposal Process`, masing-masing sekali walau `Missing` dimiliki enam baris
6. Tutup daftar opsi `Status`
7. Buka field `Source`
8. Verifikasi opsi field `Source` memuat tepat `Reported by holder`, `Borrow`, `Manual`, dan `Transfer`, masing-masing sekali walau `Manual` dimiliki empat baris
9. Tutup daftar opsi `Source`
10. Buka field `Last Holder`
11. Verifikasi opsi field `Last Holder` memuat `Gita Permata {runId}` dan `Hari Santoso {runId}` dan tidak memuat `Kirana Putri {runId}`, karena master user yang tidak menjadi Last Holder tidak menjadi opsi
12. Tutup daftar opsi `Last Holder`
13. Buka field `Reported By`
14. Verifikasi opsi field `Reported By` memuat `Rudi Hartono {runId}` sebagai PIC pelaku, `Hari Santoso {runId}`, `Indra Kusuma {runId}`, dan `Rina Wijaya {runId}`, dan tidak memuat `Gita Permata {runId}` maupun `Kirana Putri {runId}`
15. Tutup daftar opsi `Reported By`
16. Buka field `Brand`
17. Verifikasi opsi field `Brand` memuat delapan Brand `Merk Alfa {runId}`, `Merk Beta {runId}`, `Merk Gamma {runId}`, `Merk Delta {runId}`, `Merk Epsilon {runId}`, `Merk Zeta {runId}`, `Merk Eta {runId}`, `Merk Theta {runId}` dan tidak memuat nilai kosong walau `Unit Alfa {runId}` tidak punya Brand
18. Cari opsi dengan mengetik `psil` di kotak cari opsi `Brand`
19. Verifikasi opsi `Brand` tinggal `Merk Epsilon {runId}`
20. Ganti isi kotak cari opsi `Brand` dengan `merk gamma {runId}`
21. Verifikasi opsi `Brand` tinggal `Merk Gamma {runId}` walau huruf kapital berbeda
22. Ganti isi kotak cari opsi `Brand` dengan `zzzopsi`
23. Verifikasi opsi `Brand` menampilkan `No results found`
24. Kosongkan kotak cari opsi `Brand`
25. Tutup daftar opsi `Brand`

### Opsi mengikuti baris tabel yang sedang tampil, termasuk Search
26. Ganti isi kotak search dengan `Gedung C {runId}`, tekan Enter
27. Verifikasi tabel memuat baris `Unit Zeta {runId}`, `Unit Eta {runId}`, `Unit Theta {runId}`
28. Buka field `Status`
29. Verifikasi opsi field `Status` hanya `Missing` karena ketiga baris yang tampil berstatus `Missing`, dan tidak memuat `Waiting for Confirmation`, `Reported Disposal`, maupun `In Disposal Process`
30. Tutup daftar opsi `Status`
31. Ganti isi kotak search dengan `{runId} tidakada`, tekan Enter
32. Verifikasi `No results found` tampil
33. Buka field `Status`
34. Verifikasi daftar opsi `Status` menampilkan `No options available` karena tabel sumber tidak memuat baris
35. Tutup daftar opsi `Status`
36. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Hasil saringan: OR dalam satu field dan AND antar field
37. Pada field `Status` pilih opsi `Missing` dan `Waiting for Confirmation`
38. Klik `[Apply]`
39. Verifikasi tabel memuat baris `Unit Alfa {runId}`, `Unit Beta {runId}`, `Unit Gamma {runId}`, `Unit Delta {runId}`, `Unit Zeta {runId}`, `Unit Eta {runId}`, `Unit Theta {runId}` yang berstatus `Missing` atau `Waiting for Confirmation`, dan ikon Filter berbadge titik
40. Verifikasi baris `Unit Epsilon {runId}` dan `Unit Iota {runId}` tidak tampil
41. Pada field `Source` pilih opsi `Borrow`
42. Hapus pilihan `Waiting for Confirmation` dari field `Status`
43. Klik `[Apply]`
44. Verifikasi tabel memuat baris `Unit Beta {runId}`, `Unit Gamma {runId}` yang berstatus `Missing` dan ber-Source `Borrow`
45. Verifikasi baris `Unit Delta {runId}`, `Unit Zeta {runId}`, `Unit Eta {runId}`, `Unit Theta {runId}` yang hanya berstatus `Missing` tidak tampil
46. Verifikasi baris `Unit Epsilon {runId}` yang hanya ber-Source `Borrow` tidak tampil
47. Verifikasi baris `Unit Alfa {runId}`, `Unit Iota {runId}` yang tidak berstatus `Missing` dan tidak ber-Source `Borrow` tidak tampil

### Kombinasi Search dan Filter, dan pelepasan satu kontrol
48. Klik `[Clear Field]`
49. Pada field `Status` pilih opsi `Missing`
50. Klik `[Apply]`
51. Ganti isi kotak search dengan `Gedung A {runId}`, tekan Enter
52. Verifikasi tabel memuat baris `Unit Beta {runId}` saja, yaitu irisan Search `Gedung A {runId}` dan Filter `Status` `Missing`
53. Verifikasi baris `Unit Alfa {runId}`, `Unit Epsilon {runId}`, `Unit Iota {runId}` yang hanya cocok dengan Search tidak tampil, dan baris `Unit Gamma {runId}`, `Unit Delta {runId}`, `Unit Zeta {runId}`, `Unit Eta {runId}`, `Unit Theta {runId}` yang hanya cocok dengan Filter tidak tampil
54. Klik `[Clear Field]`
55. Klik `[Apply]`
56. Verifikasi tabel memuat baris `Unit Alfa {runId}`, `Unit Beta {runId}`, `Unit Epsilon {runId}`, `Unit Iota {runId}` yang cocok dengan Search `Gedung A {runId}` saja karena Filter dilepas dan Search dipertahankan
57. Pada field `Status` pilih opsi `Missing`
58. Klik `[Apply]`
59. Klik `(←)` pada kotak Search
60. Verifikasi ikon Filter tetap berbadge titik dan field `Status` tetap memilih `Missing` karena Search dilepas dan Filter dipertahankan
61. Ketik Search `Gedung C {runId}`, tekan Enter
62. Pada field `Status` pilih opsi `Waiting for Confirmation`
63. Hapus pilihan `Missing` dari field `Status`
64. Klik `[Apply]`
65. Verifikasi `No results found` tampil karena Search dan Filter masing-masing punya hasil tetapi irisannya kosong
66. Klik `[Clear Field]`
67. Klik `[Apply]`
68. Verifikasi tabel memuat kembali baris `Unit Zeta {runId}`, `Unit Eta {runId}`, `Unit Theta {runId}` karena satu saringan dilepas
69. Klik `(←)` pada kotak Search

### Filter Long missing, kolom tersembunyi, dan nilai kosong
70. Ketik Search `{runId}`, tekan Enter
71. Centang `Long missing` pada kolom Days Missing di Filter Panel
72. Klik `[Apply]`
73. Verifikasi tabel memuat baris `Unit Delta {runId}` saja, satu-satunya record `Missing` yang melewati `30` hari
74. Klik `[Clear Field]`
75. Pada field `Brand` pilih opsi `Merk Alfa {runId}`
76. Klik `[Apply]`
77. Verifikasi tabel memuat baris `Unit Beta {runId}` dan tidak memuat baris `Unit Alfa {runId}` yang Brand-nya kosong, walau kolom `Brand` tersembunyi
78. Klik `[Clear Field]`
79. Pada field `Brand` pilih kedelapan opsi `Merk Alfa {runId}`, `Merk Beta {runId}`, `Merk Gamma {runId}`, `Merk Delta {runId}`, `Merk Epsilon {runId}`, `Merk Zeta {runId}`, `Merk Eta {runId}`, `Merk Theta {runId}`
80. Verifikasi field `Brand` merangkum chip yang tidak muat sebagai `+N more`, dengan jumlah chip tampil ditambah N sama dengan delapan
81. Klik `[Clear Field]`

### Filter Group dengan tree picker
82. Centang node `Gedung C {runId}` pada field `Group`
83. Klik `[Apply]`
84. Verifikasi tabel memuat baris `Unit Zeta {runId}`, `Unit Eta {runId}`, `Unit Theta {runId}` yang ber-Group `Gedung C {runId}`
85. Klik `[Clear Field]`
86. Klik `[Apply]`

### Filter rentang tanggal Reported Date
87. Pilih rentang Reported Date sesuai DU-004-22
88. Klik `[Apply]`
89. Verifikasi tabel memuat baris `Unit Beta {runId}`, `Unit Eta {runId}` yang Reported Date-nya berada di dalam rentang
90. Klik `[Clear Field]`
91. Pilih rentang Reported Date sesuai DU-004-23
92. Klik `[Apply]`
93. Verifikasi tabel memuat baris `Unit Gamma {runId}` yang tepat di hari awal dan baris `Unit Beta {runId}` yang tepat di hari akhir, dan tidak memuat baris `Unit Delta {runId}`, `Unit Eta {runId}`
94. Klik `[Clear Field]`
95. Pilih rentang Reported Date sesuai DU-004-24
96. Klik `[Apply]`
97. Verifikasi tabel memuat baris `Unit Beta {runId}` saja karena Start dan End jatuh di hari yang sama
98. Klik `[Clear Field]`
99. Pilih rentang Reported Date sesuai DU-004-25
100. Klik `[Apply]`
101. Verifikasi `No results found` tampil karena tidak ada record spec ini yang Reported Date-nya berada di luar rentang tersebut
102. Klik `[Clear Field]`
103. Klik `[Apply]`

### Filter rentang numerik Purchase Cost
104. Isi field `Purchase Cost` dengan Min `3000000` dan Max `5000000`
105. Klik `[Apply]`
106. Verifikasi tabel memuat baris `Unit Gamma {runId}`, `Unit Delta {runId}`, `Unit Epsilon {runId}` yang nilainya tepat di Min, di antara, dan tepat di Max
107. Klik `[Clear Field]`
108. Isi field `Purchase Cost` dengan Min `8000000` saja
109. Klik `[Apply]`
110. Verifikasi tabel memuat baris `Unit Theta {runId}`, `Unit Iota {runId}` dan tidak memuat baris `Unit Eta {runId}`
111. Klik `[Clear Field]`
112. Isi field `Purchase Cost` dengan Max `2000000` saja
113. Klik `[Apply]`
114. Verifikasi tabel memuat baris `Unit Alfa {runId}`, `Unit Beta {runId}` dan tidak memuat baris `Unit Gamma {runId}`
115. Klik `[Clear Field]`
116. Isi field `Purchase Cost` dengan Min `9000000` dan Max `1000000`
117. Klik `[Apply]`
118. Verifikasi tabel memuat baris `Unit Iota {runId}` yang Purchase Cost-nya `9000000` saja, karena Max `1000000` yang lebih kecil dari Min dinaikkan oleh komponen menjadi `9000000` tanpa pesan error sehingga rentang menjadi `9000000` sampai `9000000`
119. Klik `[Clear Field]`
120. Klik `[Apply]`

### Record yang diubah masuk ke saringan Last Updated hari ini
121. Pilih rentang Last Updated sesuai DU-004-26
122. Klik `[Apply]`
123. Verifikasi `No results found` tampil karena tidak ada record spec ini yang Last Updated-nya hari ini
124. Buka field `Modified By`
125. Verifikasi opsi field `Modified By` tidak memuat `Rina Wijaya {runId}`
126. Tutup daftar opsi `Modified By`
127. Klik `[Clear Field]`
128. Klik `[Apply]`
129. Klik `⋯` pada baris `Unit Theta {runId}`
130. Klik `Add Update` pada menu
131. Isi Update dengan `Pemeriksaan ruang arsip dimulai {runId}`
132. Klik `[Add Update]`
133. Verifikasi dialog `Add Update` tertutup sesudah Update disimpan
134. Pilih rentang Last Updated sesuai DU-004-26
135. Klik `[Apply]`
136. Verifikasi tabel memuat baris `Unit Theta {runId}` karena Last Updated-nya kini hari ini
137. Buka field `Modified By`
138. Verifikasi opsi field `Modified By` kini memuat `Rina Wijaya {runId}` tanpa memuat ulang halaman
139. Tutup daftar opsi `Modified By`
140. Klik `[Clear Field]`

### Record yang diubah keluar dari saringan Last Updated lama
141. Pilih rentang Last Updated sesuai DU-004-27
142. Klik `[Apply]`
143. Verifikasi tabel memuat baris `Unit Eta {runId}` yang Last Updated-nya berada di dalam rentang
144. Klik `⋯` pada baris `Unit Eta {runId}`
145. Klik `Add Update` pada menu
146. Isi Update dengan `Pemeriksaan gudang cadangan selesai {runId}`
147. Klik `[Add Update]`
148. Klik `[Apply]`
149. Verifikasi baris `Unit Eta {runId}` tidak tampil karena Last Updated-nya kini hari ini
150. Klik `[Clear Field]`
151. Klik `[Apply]`

### Filter rentang tanggal Last Seen
152. Pilih rentang Last Seen dari `T0 − 14 hari` sampai `T0 − 12 hari` sesuai DU-004-32
153. Klik `[Apply]`
154. Verifikasi tabel memuat baris `Unit Beta {runId}` yang pemindaian terakhirnya berada di dalam rentang
155. Verifikasi baris `Unit Gamma {runId}` yang pemindaiannya di luar rentang dan baris `Unit Alfa {runId}` yang belum pernah terpindai tidak tampil
156. Klik `[Clear Field]`
157. Klik `[Apply]`

### Clear Filter dan Clear Search mempertahankan Sort
158. Ganti isi kotak search dengan `Gedung C {runId}`, tekan Enter
159. Klik header `Name`
160. Pada field `Status` pilih opsi `Missing`
161. Klik `[Apply]`
162. Klik `[Clear Field]`
163. Klik `[Apply]`
164. Verifikasi urutan baris dari atas ke bawah: `Unit Eta {runId}`, `Unit Theta {runId}`, `Unit Zeta {runId}`, menurut sort `Name` ascending yang tetap aktif walau Filter dilepas, berbeda dari urutan default `Unit Eta {runId}`, `Unit Zeta {runId}`, `Unit Theta {runId}`
165. Pada field `Status` pilih opsi `Missing`
166. Klik `[Apply]`
167. Klik `(←)` pada kotak Search
168. Verifikasi header `Name` tetap berindikator sort ascending walau Search dilepas
169. Klik `[Clear Field]`
170. Klik `[Apply]`
