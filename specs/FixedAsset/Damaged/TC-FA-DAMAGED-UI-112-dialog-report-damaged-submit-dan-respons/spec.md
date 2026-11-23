---
id: TC-FA-DAMAGED-UI-112-dialog-report-damaged-submit-dan-respons
title: "Submit Dialog Report Damaged: tanpa konfirmasi kedua, saving, toast sukses dan gagal, aset dilewati tetap tampil dengan dialog terbuka, gagal 5xx/timeout, dan dialog Unsaved Changes"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FI-DMG-03, "§4.4#r3", TS-DMG-01, TS-DMG-02, TS-DMG-10, V-DMG-10, "§4.2.4#p13", "§9.6#r1", EB-FB-1@report-damaged, EB-FB-2@cancel-report-damaged, EB-FB-4, EB-FRM-1@report-damaged, EB-FRM-2@report-damaged, EB-ERR-1@report-damaged, "§Aturan Logika Modul#r93", "§Aturan Logika Modul#r94", "§Aturan Logika Modul#r95", V-DMG-20, TS-DMG-11, EC-DMG-38, "§7.3#p1", "§4.2.3#b1", "§9.2#b9", "§9.9#p4"]
smoke: []
dependsOn: []
trace:
  FI-DMG-03: [8]
  "§4.4#r3": [6, 25]
  TS-DMG-01: [6, 52, 84]
  TS-DMG-02: [25, 75]
  TS-DMG-10: [33]
  V-DMG-10: [34, 35, 43, 44, 45, 46]
  "§4.2.4#p13": [101, 109, 111, 159, 160]
  "§9.6#r1": [6, 25, 33, 52, 84, 85, 141, 142, 143]
  EB-FB-1@report-damaged: [6, 25, 52, 75]
  EB-FB-2@cancel-report-damaged: [96, 97]
  EB-FB-4: [10, 58, 129]
  EB-FRM-1@report-damaged: [7, 16, 17, 19, 118, 119]
  EB-FRM-2@report-damaged: [88, 89, 92, 93, 101, 102, 103, 105, 107]
  EB-ERR-1@report-damaged: [52, 53, 54, 55, 56, 60, 61, 67, 68, 69, 76, 85]
  "§Aturan Logika Modul#r93": [126, 133, 141, 166]
  "§Aturan Logika Modul#r94": [130, 151, 152]
  "§Aturan Logika Modul#r95": [130, 131, 132, 142, 143]
  V-DMG-20: [126, 127, 129]
  TS-DMG-11: [126, 141, 149, 166]
  EC-DMG-38: [126, 130, 131, 132, 141, 142, 143, 166, 167, 168, 169, 170]
  "§7.3#p1": [141, 166]
  "§4.2.3#b1": [124, 126, 130]
  "§9.2#b9": [126]
  "§9.9#p4": [127]
anchor: [158]
coverage:
  web: automated
---

# Submit Dialog Report Damaged: tanpa konfirmasi kedua, saving, toast sukses dan gagal, aset dilewati tetap tampil dengan dialog terbuka, gagal 5xx/timeout, dan dialog Unsaved Changes

## Prerequisites
- Aktor: Pelapor admin (Aktor Damaged pada Group aset); pada K3 dan K8 pelapor umum.
- Layar awal: Dialog Report Damaged belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Report Damaged (D-DMG-01)
- Data:
  - DU-112-1: Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`.
  - DU-112-2: Asset `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`.
  - DU-112-3: Asset `Scanner Fujitsu fi-7160 - 2`, Asset ID `SCN-2026-0002`, Group `Head Office`.
  - DU-112-4: laporan valid lengkap untuk satu aset: What happened `Layar retak dan perangkat tidak menyala` dan foto `kerusakan-layar.jpeg`.
  - DU-112-5: laporan valid lengkap untuk dua aset: What happened `Bodi perangkat retak dan tidak dapat dipakai`, foto `kerusakan-proyektor.jpeg` untuk `Projector Epson EB-X06 - 2`, foto `kerusakan-scanner.jpeg` untuk `Scanner Fujitsu fi-7160 - 2`.
  - DU-112-6: Storage penuh: usage ledger Storage client sama dengan kuota, `50.0 GB` dari `50.0 GB`.
  - DU-112-7: Storage melebihi kuota: usage ledger `51.2 GB`, kuota `50.0 GB`.
  - DU-112-8: Storage client tanpa baris ledger Storage: kuota `0.0 GB` dan usage `0.0 GB`.
- Kondisi:
  - K1: satu aset terpilih (DU-112-1), What happened dan foto belum diisi.
  - K2: satu aset terpilih (DU-112-1); respons simpan lambat lalu sukses.
  - K3: satu aset terpilih (DU-112-1), pelapor umum; respons simpan sukses.
  - K4: dua aset terpilih (DU-112-2 dan DU-112-3); respons simpan menyatakan `Scanner Fujitsu fi-7160 - 2` baru saja dilaporkan orang lain, aset lainnya diproses.
  - K5: dua aset terpilih (DU-112-2 dan DU-112-3); respons simpan menyatakan kedua aset baru saja dilaporkan orang lain.
  - K6: satu aset terpilih (DU-112-1); respons simpan pertama gagal karena error server, respons berikutnya sukses.
  - K7: satu aset terpilih (DU-112-1); permintaan simpan melewati batas waktu.
  - K8: satu aset terpilih (DU-112-1), pelapor umum; respons simpan gagal karena error server.
  - K9: dua aset terpilih (DU-112-2 dan DU-112-3); respons simpan gagal karena error server.
  - K10: satu aset terpilih (DU-112-1); Storage penuh DU-112-6; respons simpan ditolak karena Storage penuh.
  - K11: dua aset terpilih (DU-112-2 dan DU-112-3); Storage melebihi kuota DU-112-7; respons simpan ditolak karena Storage penuh.
  - K12: satu aset terpilih (DU-112-1); respons simpan pertama ditolak karena Storage penuh DU-112-6, respons berikutnya sukses (Storage dibebaskan).
  - K13: satu aset terpilih (DU-112-1); client tanpa baris ledger Storage DU-112-8; respons simpan ditolak karena Storage penuh.

## Test Steps

### Submit sukses oleh pelapor admin tanpa konfirmasi kedua
1. Tampilkan Dialog Report Damaged dengan kondisi K1
2. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
3. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
4. Klik `Apply` pada dialog `Adjust photo`
5. Klik `[Report Damaged]`
6. Verifikasi toast `Success, asset has been reported damaged.` tampil
7. Verifikasi dialog Report Damaged tertutup
8. Verifikasi tidak ada dialog konfirmasi yang tampil sesudah `[Report Damaged]` diklik
9. Waktu berlalu sampai 4 detik sejak toast tampil
10. Verifikasi toast `Success, asset has been reported damaged.` tidak tampil lagi

### Saving state selama simpan berjalan
11. Tampilkan Dialog Report Damaged dengan kondisi K2
12. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
13. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
14. Klik `Apply` pada dialog `Adjust photo`
15. Klik `[Report Damaged]`
16. Verifikasi tombol `[Report Damaged]` berada dalam saving state dan tidak bisa diklik
17. Verifikasi tombol `✕`, tombol `[Cancel]`, isian `What happened*`, dan pemilih foto `Damaged Photo*` tidak bisa dioperasikan selama simpan berjalan
18. Klik `[Report Damaged]` sekali lagi
19. Verifikasi hanya satu permintaan simpan yang terkirim

### Submit sukses oleh pelapor umum
20. Tampilkan Dialog Report Damaged dengan kondisi K3
21. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
22. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
23. Klik `Apply` pada dialog `Adjust photo`
24. Klik `[Report Damaged]`
25. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Sebagian aset dilewati tetap tampil dengan dialog terbuka
26. Tampilkan Dialog Report Damaged dengan kondisi K4
27. Isi `What happened*` dengan `Bodi perangkat retak dan tidak dapat dipakai`
28. Pilih berkas foto `kerusakan-proyektor.jpeg` pada pemilih foto aset `Projector Epson EB-X06 - 2`
29. Klik `Apply` pada dialog `Adjust photo`
30. Pilih berkas foto `kerusakan-scanner.jpeg` pada pemilih foto aset `Scanner Fujitsu fi-7160 - 2`
31. Klik `Apply` pada dialog `Adjust photo`
32. Klik `[Report Damaged]`
33. Verifikasi toast `Success, asset has been reported damaged. Some items were skipped.` tampil
34. Verifikasi dialog Report Damaged tetap terbuka sesudah sebagian aset dilewati
35. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Scanner Fujitsu fi-7160 - 2`

### Semua aset dilewati tanpa toast sukses
36. Tampilkan Dialog Report Damaged dengan kondisi K5
37. Isi `What happened*` dengan `Bodi perangkat retak dan tidak dapat dipakai`
38. Pilih berkas foto `kerusakan-proyektor.jpeg` pada pemilih foto aset `Projector Epson EB-X06 - 2`
39. Klik `Apply` pada dialog `Adjust photo`
40. Pilih berkas foto `kerusakan-scanner.jpeg` pada pemilih foto aset `Scanner Fujitsu fi-7160 - 2`
41. Klik `Apply` pada dialog `Adjust photo`
42. Klik `[Report Damaged]`
43. Verifikasi dialog Report Damaged tetap terbuka sesudah semua aset dilewati
44. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Projector Epson EB-X06 - 2`
45. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Scanner Fujitsu fi-7160 - 2`
46. Verifikasi tidak ada toast sukses yang tampil

### Gagal 5xx pada satu aset lalu berhasil sesudah pulih
47. Tampilkan Dialog Report Damaged dengan kondisi K6
48. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
49. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
50. Klik `Apply` pada dialog `Adjust photo`
51. Klik `[Report Damaged]`
52. Verifikasi toast `Error, failed to report damage.` tampil
53. Verifikasi dialog Report Damaged tetap terbuka sesudah simpan gagal
54. Verifikasi isian `What happened*` masih berisi `Layar retak dan perangkat tidak menyala`
55. Verifikasi foto `kerusakan-layar.jpeg` masih tampil pada pemilih foto `Damaged Photo*`
56. Verifikasi tombol `[Report Damaged]` aktif lagi
57. Waktu berlalu sampai 10 detik sejak toast tampil
58. Verifikasi toast `Error, failed to report damage.` masih tampil
59. Klik `[Report Damaged]`
60. Verifikasi toast `Success, asset has been reported damaged.` tampil
61. Verifikasi dialog Report Damaged tertutup

### Timeout pada simpan
62. Tampilkan Dialog Report Damaged dengan kondisi K7
63. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
64. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
65. Klik `Apply` pada dialog `Adjust photo`
66. Klik `[Report Damaged]`
67. Verifikasi toast `Connection problem. Please try again.` tampil untuk simpan Report Damaged yang melewati batas waktu
68. Verifikasi dialog Report Damaged tetap terbuka dengan isian `What happened*` berisi `Layar retak dan perangkat tidak menyala`
69. Verifikasi tombol `[Report Damaged]` aktif lagi

### Gagal 5xx pada laporan pelapor umum
70. Tampilkan Dialog Report Damaged dengan kondisi K8
71. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
72. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
73. Klik `Apply` pada dialog `Adjust photo`
74. Klik `[Report Damaged]`
75. Verifikasi toast `Error, failed to send your report.` tampil
76. Verifikasi dialog Report Damaged tetap terbuka sesudah laporan pelapor umum gagal

### Gagal 5xx pada laporan beberapa aset
77. Tampilkan Dialog Report Damaged dengan kondisi K9
78. Isi `What happened*` dengan `Bodi perangkat retak dan tidak dapat dipakai`
79. Pilih berkas foto `kerusakan-proyektor.jpeg` pada pemilih foto aset `Projector Epson EB-X06 - 2`
80. Klik `Apply` pada dialog `Adjust photo`
81. Pilih berkas foto `kerusakan-scanner.jpeg` pada pemilih foto aset `Scanner Fujitsu fi-7160 - 2`
82. Klik `Apply` pada dialog `Adjust photo`
83. Klik `[Report Damaged]`
84. Verifikasi toast `Error, failed to report damage.` tampil
85. Verifikasi dialog Report Damaged tetap terbuka dengan blok aset `Projector Epson EB-X06 - 2` dan `Scanner Fujitsu fi-7160 - 2`

### Menutup form bersih dengan tombol tutup
86. Tampilkan Dialog Report Damaged dengan kondisi K1
87. Klik `✕` pada dialog
88. Verifikasi dialog Report Damaged tertutup
89. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil

### Menutup form bersih dengan Esc
90. Tampilkan Dialog Report Damaged dengan kondisi K1
91. Tekan `Esc`
92. Verifikasi dialog Report Damaged tertutup
93. Verifikasi tidak ada dialog `Unsaved Changes` yang tampil

### Cancel pada form bersih tidak memunculkan toast
94. Tampilkan Dialog Report Damaged dengan kondisi K1
95. Klik `[Cancel]`
96. Verifikasi dialog Report Damaged tertutup
97. Verifikasi tidak ada toast yang tampil sesudah `[Cancel]` pada Report Damaged

### Menutup form kotor memunculkan dialog Unsaved Changes
98. Tampilkan Dialog Report Damaged dengan kondisi K1
99. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
100. Klik `✕` pada dialog
101. Verifikasi dialog `Unsaved Changes` tampil
102. Verifikasi dialog `Unsaved Changes` memuat pesan `You have unsaved changes. Are you sure you want to leave?`
103. Verifikasi dialog `Unsaved Changes` memuat tombol `[Leave]` dan `[Cancel]`
104. Klik `[Cancel]` pada dialog `Unsaved Changes`[^drift-1]
105. Verifikasi dialog `Unsaved Changes` tertutup dan dialog Report Damaged tetap terbuka dengan isian `What happened*` berisi `Layar retak dan perangkat tidak menyala`
106. Klik area backdrop di luar dialog Report Damaged
107. Verifikasi dialog Report Damaged tetap terbuka dengan isian `What happened*` berisi `Layar retak dan perangkat tidak menyala` dan dialog `Unsaved Changes` tidak tampil
108. Tekan `Esc`
109. Verifikasi dialog `Unsaved Changes` tampil
110. Klik `[Leave]`
111. Verifikasi dialog Report Damaged tertutup

### Klik ganda saat simpan menghasilkan satu toast dan dialog tertutup
112. Tampilkan Dialog Report Damaged dengan kondisi K2
113. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
114. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
115. Klik `Apply` pada dialog `Adjust photo`
116. Klik `[Report Damaged]`
117. Klik `[Report Damaged]` sekali lagi
118. Verifikasi toast `Success, asset has been reported damaged.` tampil satu kali sesudah respons simpan diterima
119. Verifikasi dialog Report Damaged tertutup sesudah respons simpan diterima

### Storage penuh pada satu aset: Submit ditolak dengan toast Error persisten
120. Tampilkan Dialog Report Damaged dengan kondisi K10
121. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
122. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
123. Klik `Apply` pada dialog `Adjust photo`
124. Verifikasi tombol `[Report Damaged]` tidak Disabled sebelum diklik
125. Klik `[Report Damaged]`
126. Verifikasi toast `Error, failed to report damage. Storage is full (50.0 GB of 50.0 GB used).` tampil
127. Verifikasi tidak ada caption error di bawah pemilih foto `Damaged Photo*`
128. Waktu berlalu sampai 10 detik sejak toast tampil
129. Verifikasi toast `Error, failed to report damage. Storage is full (50.0 GB of 50.0 GB used).` masih tampil
130. Verifikasi dialog Report Damaged tetap terbuka walau Damaged Photo wajib sudah terisi
131. Verifikasi isian `What happened*` masih berisi `Layar retak dan perangkat tidak menyala`
132. Verifikasi foto `kerusakan-layar.jpeg` masih tampil pada pemilih foto `Damaged Photo*`
133. Verifikasi tombol `[Report Damaged]` aktif lagi

### Storage penuh pada laporan beberapa aset ditolak seluruhnya
134. Tampilkan Dialog Report Damaged dengan kondisi K11
135. Isi `What happened*` dengan `Bodi perangkat retak dan tidak dapat dipakai`
136. Pilih berkas foto `kerusakan-proyektor.jpeg` pada pemilih foto aset `Projector Epson EB-X06 - 2`
137. Klik `Apply` pada dialog `Adjust photo`
138. Pilih berkas foto `kerusakan-scanner.jpeg` pada pemilih foto aset `Scanner Fujitsu fi-7160 - 2`
139. Klik `Apply` pada dialog `Adjust photo`
140. Klik `[Report Damaged]`
141. Verifikasi toast `Error, failed to report damage. Storage is full (51.2 GB of 50.0 GB used).` tampil
142. Verifikasi dialog Report Damaged tetap terbuka dengan blok aset `Projector Epson EB-X06 - 2` dan `Scanner Fujitsu fi-7160 - 2`
143. Verifikasi tidak ada keterangan `Already reported damaged` pada aset mana pun

### Submit ulang berhasil sesudah Storage dibebaskan
144. Tampilkan Dialog Report Damaged dengan kondisi K12
145. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
146. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
147. Klik `Apply` pada dialog `Adjust photo`
148. Klik `[Report Damaged]`
149. Verifikasi toast `Error, failed to report damage. Storage is full (50.0 GB of 50.0 GB used).` tampil
150. Klik `[Report Damaged]`
151. Verifikasi toast `Success, asset has been reported damaged.` tampil
152. Verifikasi dialog Report Damaged tertutup

### Guard Unsaved Changes dilepas sesudah Submit sukses
153. Tampilkan Dialog Report Damaged dengan kondisi K1
154. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
155. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
156. Klik `Apply` pada dialog `Adjust photo`
157. Klik `[Report Damaged]`
158. Verifikasi toast `Success, asset has been reported damaged.` tampil
159. Verifikasi dialog Report Damaged tertutup
160. Verifikasi dialog `Unsaved Changes` tidak tampil sesudah Submit sukses pada form yang terisi

### Client tanpa baris ledger Storage dianggap berkuota 0: Submit ditolak
161. Tampilkan Dialog Report Damaged dengan kondisi K13
162. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
163. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
164. Klik `Apply` pada dialog `Adjust photo`
165. Klik `[Report Damaged]`
166. Verifikasi toast `Error, failed to report damage. Storage is full (0.0 GB of 0.0 GB used).` tampil
167. Verifikasi dialog Report Damaged tetap terbuka walau Damaged Photo wajib sudah terisi
168. Verifikasi isian `What happened*` masih berisi `Layar retak dan perangkat tidak menyala`
169. Verifikasi foto `kerusakan-layar.jpeg` masih tampil pada pemilih foto `Damaged Photo*`
170. Verifikasi tombol `[Report Damaged]` aktif lagi

[^drift-1]: Drift ekspektasi baku vs kontrak komponen. PRD `prd-conventions.md` §24.1c hanya menyebut `Esc` pada form dan tidak menyebut `Esc` pada dialog Unsaved Changes; ekspektasi baku EB-FRM-2 butir (c): `Esc` pada dialog itu sama dengan `[Cancel]`. Kontrak `DialogForm#23`: Esc pada konfirmasi tidak berbuat apa-apa kecuali `closeOnEscape: true` diberikan di `discardConfirm`, dan `DialogForm#35`: Esc pada konfirmasi yang terbuka diabaikan. Diasersi: kontrak, sehingga dialog Unsaved Changes ditutup dengan klik `[Cancel]`.
