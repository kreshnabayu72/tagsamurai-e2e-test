---
id: TC-FA-FAREG-UI-027-dialog-activate
title: "Dialog Activate: konfirmasi Submit, Skip pairing, blok kuota, dan toast"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-REG-03", "D-REG-08", "FAREG-LOGIC-01h", "FAREG-LOGIC-01j", "FAREG-LOGIC-04j", "FAREG-LOGIC-04k", "FAREG-LOGIC-05n", "T-REG-02", "T-REG-03", "T-REG-12", "T-REG-13", "V-REG-11", "V-REG-12", "V-REG-13", "V-REG-18", "§4.1#r5", "§4.1#b12", "§4.2.3#b2", "§9.4.2#r29", "§9.6#r3", "§9.9#r9", "§9.9#r10", "§9.9#r17", "EB-ERR-1@activate", "EB-FB-1@activate", "EB-FB-2@dialog-blok", "EB-FRM-1@dialog-activate", "EB-FRM-4@skip-pairing-note", "EB-FRM-7@dialog-activate"]
smoke: []
dependsOn: []
trace:
  "D-REG-03": [4, 5, 6, 7, 24, 27, 28, 29, 41, 42, 43, 51, 53, 60, 63, 66, 68, 100, 101, 148]
  "D-REG-08": [106, 107, 108, 141, 143]
  "FAREG-LOGIC-01h": [2, 7, 29]
  "FAREG-LOGIC-01j": 42
  "FAREG-LOGIC-04j": [39, 43]
  "FAREG-LOGIC-04k": [54, 59, 60, 62, 63, 65, 66, 68, 97]
  "FAREG-LOGIC-05n": [4, 8, 41, 104, 106, 110, 139, 141, 143]
  "T-REG-02": [21, 35, 97, 119]
  "T-REG-03": [31, 151]
  "T-REG-12": [115, 147]
  "T-REG-13": [125, 155]
  "V-REG-11": [51, 56]
  "V-REG-12": 71
  "V-REG-13": [46, 47]
  "V-REG-18": [79, 81, 84, 87, 162, 163]
  "§4.1#r5": [4, 9, 27]
  "§4.1#b12": [21, 31]
  "§4.2.3#b2": [5, 6, 7, 8, 9, 24, 41, 42, 68, 100, 101]
  "§9.4.2#r29": 56
  "§9.6#r3": [21, 31, 35, 115]
  "§9.9#r9": [53, 56]
  "§9.9#r10": [71, 79, 81, 90]
  "§9.9#r17": [43, 44]
  "EB-ERR-1@activate": [115, 116, 117, 119, 125, 126, 147, 148, 149, 151, 155, 156]
  "EB-FB-1@activate": [21, 31, 97, 115, 147, 151]
  "EB-FB-2@dialog-blok": [16, 111]
  "EB-FRM-1@dialog-activate": [130, 131, 134, 136]
  "EB-FRM-4@skip-pairing-note": [79, 81]
  "EB-FRM-7@dialog-activate": [10, 12, 13, 17, 52, 57, 69, 72]
anchor: [15, 38, 78, 83, 86, 89, 133]
coverage:
  web: automated
---

# Dialog Activate: konfirmasi Submit, Skip pairing, blok kuota, dan toast

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft > Edit
- Komponen: Dialog Activate
- Data:
  - DU-027-1: Group `Gudang 1`, Approval Workflow OFF.
  - DU-027-2: Group `Gudang 2`, Approval Workflow ON.
  - DU-027-3: Item `Laptop Dell Latitude 5440` dengan Quantity `3`; aset `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, dan `Laptop Dell Latitude 5440 - 3`, seluruh data Tingkat 2 dan Tag terisi.
  - DU-027-4: Item `Printer Epson L3250` dengan Quantity `1`; aset `Printer Epson L3250 - 1`, seluruh data Tingkat 2 dan Tag terisi.
  - DU-027-5: Item `Laptop Dell Latitude 5440` dengan Quantity `3`; ketiga aset hanya kurang Tag (Tingkat 2 lain terisi).
  - DU-027-6: Item `Printer Epson L3250` dengan Quantity `1`; aset hanya kurang Tag (Tingkat 2 lain terisi).
  - DU-027-7: kuota Group `Gudang 1` tidak cukup untuk tiga aset sehingga Activate ditolak `QUOTA_EXCEEDED`.
  - DU-027-20: kuota Group `Gudang 2` tidak cukup untuk tiga aset sehingga Submit for Approval ditolak `QUOTA_EXCEEDED`.
  - DU-027-21: Skip pairing Note berisi emoji `Reader rusak 😊`.
  - DU-027-8: teks dialog `Gudang 1 · 3 assets`, `Gudang 1 · 1 asset`, `3 assets are not paired to a TAG yet.`, dan `1 asset is not paired to a TAG yet.`
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Group DU-027-1 dan Item DU-027-3; Approval Workflow OFF.
  - K2: form `Edit` draft tersimpan dengan Group DU-027-1 dan Item DU-027-4; Approval Workflow OFF.
  - K3: form `Edit` draft tersimpan dengan Group DU-027-2 dan Item DU-027-3; Approval Workflow ON; pengajuan masuk antrean Approvals.
  - K4: form `Edit` draft tersimpan dengan Group DU-027-2 dan Item DU-027-3; Approval Workflow ON; pengajuan di-approve otomatis (`FAREG-LOGIC-06l`).
  - K5: form `Edit` draft tersimpan dengan Group DU-027-1 dan Item DU-027-5; Approval Workflow OFF.
  - K6: form `Edit` draft tersimpan dengan Group DU-027-1 dan Item DU-027-6; Approval Workflow OFF.
  - K7: form `Edit` draft tersimpan dengan Group DU-027-1 dan Item DU-027-3; Approval Workflow OFF; kuota DU-027-7.
  - K8: sama dengan K1; Activate gagal karena error server pada percobaan pertama dan berhasil pada percobaan kedua.
  - K9: sama dengan K5; Activate gagal karena gangguan jaringan.
  - K10: sama dengan K1; respons Activate lambat.
  - K11: form `Edit` draft tersimpan dengan Group DU-027-2 dan Item DU-027-3; Approval Workflow ON; kuota DU-027-20.
  - K12: sama dengan K3; Submit for Approval gagal karena error server pada percobaan pertama dan berhasil pada percobaan kedua.
  - K13: sama dengan K3; Submit for Approval gagal karena gangguan jaringan.

## Test Steps
### Dialog Activate saat Approval Workflow OFF: isi, tombol, aksesibilitas, dan Cancel
1. Tampilkan Dialog Activate dengan kondisi K1
2. Verifikasi tombol `[Submit]` pada footer form aktif
3. Klik `[Submit]` pada footer form
4. Verifikasi dialog `Activate Assets` berukuran LG tampil
5. Verifikasi bullet `Gudang 1 · 3 assets` tampil
6. Verifikasi pertanyaan `Are you sure you want to activate it?` tampil
7. Verifikasi dialog memuat tombol `[Cancel]` dan `[Activate]`
8. Verifikasi dialog tidak memuat rincian kuota
9. Verifikasi dialog tidak memuat checkbox `Submit them without pairing TAGs (pair later)`
10. Verifikasi fokus berada di dalam dialog `Activate Assets`
11. Tekan `Tab` sampai melewati kontrol terakhir dialog
12. Verifikasi fokus tetap berada di dalam dialog `Activate Assets`
13. Verifikasi `✕` memiliki label aksesibel
14. Klik `[Cancel]`
15. Verifikasi form `Register Asset` tampil dengan tombol `[Submit]` pada footer
16. Verifikasi tidak ada toast yang tampil sesudah `[Cancel]`
17. Verifikasi fokus kembali ke tombol `[Submit]`

### Activate berhasil memunculkan toast sukses
18. Tampilkan Dialog Activate dengan kondisi K1
19. Klik `[Submit]` pada footer form
20. Klik `[Activate]`
21. Verifikasi toast `Success, asset has been activated.` tampil

### Dialog Activate untuk satu aset memakai bentuk tunggal
22. Tampilkan Dialog Activate dengan kondisi K2
23. Klik `[Submit]` pada footer form
24. Verifikasi dialog `Activate Assets` tampil dengan bullet `Gudang 1 · 1 asset`

### Dialog Submit for Approval saat Approval Workflow ON
25. Tampilkan Dialog Activate dengan kondisi K3
26. Klik `[Submit]` pada footer form
27. Verifikasi dialog `Submit for Approval` tampil dengan bullet `Gudang 2 · 3 assets`
28. Verifikasi pertanyaan `Are you sure you want to submit it for approval?` tampil
29. Verifikasi dialog memuat tombol `[Cancel]` dan `[Submit for Approval]`
30. Klik `[Submit for Approval]`
31. Verifikasi toast `Success, registration has been submitted.` tampil

### Pengajuan yang di-approve otomatis memakai toast aktivasi
32. Tampilkan Dialog Activate dengan kondisi K4
33. Klik `[Submit]` pada footer form
34. Klik `[Submit for Approval]`
35. Verifikasi toast `Success, asset has been activated.` tampil setelah pengajuan di-approve otomatis

### Aset hanya kurang Tag: peringatan, checkbox Skip, dan Skip diputuskan di dialog
36. Tampilkan Dialog Activate dengan kondisi K5
37. Klik tab `Asset`
38. Verifikasi tabel aset memuat `Laptop Dell Latitude 5440 - 1`
39. Verifikasi kontrol Skip per aset tidak tampil pada tabel aset
40. Klik `[Submit]` pada footer form
41. Verifikasi dialog `Activate Assets` tampil dengan bullet `Gudang 1 · 3 assets`
42. Verifikasi peringatan `3 assets are not paired to a TAG yet.` tampil
43. Verifikasi checkbox `Submit them without pairing TAGs (pair later)` tampil
44. Verifikasi checkbox `Submit them without pairing TAGs (pair later)` berstatus tidak tercentang
45. Klik `[Activate]`
46. Verifikasi pesan `Choose to submit without pairing, or pair the TAGs first.` tampil di dialog
47. Verifikasi dialog `Activate Assets` tetap terbuka

### Skip pairing: Reason wajib dan Input note hanya untuk Other
48. Tampilkan Dialog Activate dengan kondisi K5
49. Klik `[Submit]` pada footer form
50. Centang checkbox `Submit them without pairing TAGs (pair later)`
51. Verifikasi Select reason menampilkan placeholder `Select reason`
52. Verifikasi Select reason memiliki atribut aria-required
53. Verifikasi opsi Reason memuat `Device unavailable`, `TAG not yet available`, `TAG damaged`, dan `Other`
54. Verifikasi dialog memuat satu Select reason untuk ketiga aset
55. Klik `[Activate]`
56. Verifikasi pesan `You must pick a reason` tampil di bawah Select reason
57. Verifikasi Select reason memiliki atribut aria-describedby yang menunjuk pesan `You must pick a reason`
58. Pilih Reason `Device unavailable`
59. Verifikasi Select reason menampilkan `Device unavailable`
60. Verifikasi Input note tidak tampil untuk Reason `Device unavailable`
61. Pilih Reason `TAG not yet available`
62. Verifikasi Select reason menampilkan `TAG not yet available`
63. Verifikasi Input note tidak tampil untuk Reason `TAG not yet available`
64. Pilih Reason `TAG damaged`
65. Verifikasi Select reason menampilkan `TAG damaged`
66. Verifikasi Input note tidak tampil untuk Reason `TAG damaged`
67. Pilih Reason `Other`
68. Verifikasi Input note tampil dengan placeholder `Enter note`
69. Verifikasi Input note memiliki atribut aria-required
70. Klik `[Activate]`
71. Verifikasi pesan `Note must not be empty` tampil di bawah Input note
72. Verifikasi Input note memiliki atribut aria-describedby yang menunjuk pesan `Note must not be empty`

### Skip pairing Note: batas 120 karakter
73. Tampilkan Dialog Activate dengan kondisi K5
74. Klik `[Submit]` pada footer form
75. Centang checkbox `Submit them without pairing TAGs (pair later)`
76. Pilih Reason `Other`
77. Ganti isi Input note dengan `Reader TAG di Gudang 1 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456789012345678901` (120 karakter)
78. Verifikasi Input note menampilkan `Reader TAG di Gudang 1 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456789012345678901`
79. Verifikasi tidak ada pesan error di bawah Input note
80. Ganti isi Input note dengan `Reader TAG di Gudang 1 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 01234567890123456789012` (121 karakter)
81. Verifikasi pesan `Max. 120 characters` tampil di bawah Input note
82. Ganti isi Input note dengan `Reader  TAG  di  Gudang  1  sedang  diperbaiki  sehingga  pemasangan  Tag  ditunda  sampai  pekan  depan.  Kode 01234567` (120 karakter)
83. Verifikasi Input note menampilkan `Reader  TAG  di  Gudang  1  sedang  diperbaiki  sehingga  pemasangan  Tag  ditunda  sampai  pekan  depan.  Kode 01234567`
84. Verifikasi tidak ada pesan error di bawah Input note
85. Ganti isi Input note dengan `Reader TAG Kantor Cabang Medan Élan 𝒜 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456` (120 karakter)
86. Verifikasi Input note menampilkan `Reader TAG Kantor Cabang Medan Élan 𝒜 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456`
87. Verifikasi tidak ada pesan error di bawah Input note
88. Ganti isi Input note dengan `R` (1 karakter)
89. Verifikasi Input note menampilkan `R`
90. Verifikasi tidak ada pesan error di bawah Input note

### Skip pairing berhasil dengan satu alasan untuk semua aset
91. Tampilkan Dialog Activate dengan kondisi K5
92. Klik `[Submit]` pada footer form
93. Centang checkbox `Submit them without pairing TAGs (pair later)`
94. Pilih Reason `Other`
95. Ganti isi Input note dengan `Reader TAG sedang diperbaiki`
96. Klik `[Activate]`
97. Verifikasi toast `Success, asset has been activated.` tampil setelah Skip pairing

### Dialog untuk satu aset hanya kurang Tag memakai peringatan tunggal
98. Tampilkan Dialog Activate dengan kondisi K6
99. Klik `[Submit]` pada footer form
100. Verifikasi dialog `Activate Assets` tampil dengan bullet `Gudang 1 · 1 asset`
101. Verifikasi peringatan `1 asset is not paired to a TAG yet.` tampil

### Kuota Group tidak cukup: dialog Cannot Activate
102. Tampilkan Dialog Activate dengan kondisi K7
103. Klik `[Submit]` pada footer form
104. Verifikasi dialog `Activate Assets` tampil tanpa pemeriksaan kuota
105. Klik `[Activate]`
106. Verifikasi dialog `Cannot Activate` tampil dengan teks `Group quota exceeded. Available slots:` diikuti sisa slot dari respons
107. Verifikasi dialog `Cannot Activate` memuat teks `Please contact administrator to increase quota.`
108. Verifikasi dialog `Cannot Activate` hanya memuat tombol `[OK]`
109. Klik `[OK]`
110. Verifikasi form `Register Asset` masih Draft dengan footer `[Save draft]` dan `[Submit]`
111. Verifikasi dialog `Cannot Activate` tertutup tanpa toast

### Activate gagal karena error server dan pulih sesudah submit ulang
112. Tampilkan Dialog Activate dengan kondisi K8
113. Klik `[Submit]` pada footer form
114. Klik `[Activate]`
115. Verifikasi toast Error dengan awalan `Error, failed to` tampil
116. Verifikasi dialog `Activate Assets` tetap terbuka dengan bullet `Gudang 1 · 3 assets`
117. Verifikasi tombol `[Activate]` aktif kembali
118. Klik `[Activate]`
119. Verifikasi toast `Success, asset has been activated.` tampil satu kali

### Activate gagal karena gangguan jaringan mempertahankan input
120. Tampilkan Dialog Activate dengan kondisi K9
121. Klik `[Submit]` pada footer form
122. Centang checkbox `Submit them without pairing TAGs (pair later)`
123. Pilih Reason `TAG damaged`
124. Klik `[Activate]`
125. Verifikasi toast Error `Connection problem. Please try again.` tampil dan dialog `Activate Assets` tetap terbuka
126. Verifikasi Select reason masih menampilkan `TAG damaged`

### Activate lambat: Saving dan satu request
127. Tampilkan Dialog Activate dengan kondisi K10
128. Klik `[Submit]` pada footer form
129. Klik `[Activate]`
130. Verifikasi tombol `[Activate]` menampilkan loading dan Disabled
131. Verifikasi `[Cancel]` dan `✕` Disabled
132. Klik `[Activate]` sekali lagi
133. Verifikasi tombol `[Activate]` masih menampilkan loading
134. Verifikasi tidak ada pengiriman Activate kedua
135. Tunggu sampai respons Activate diterima
136. Verifikasi tepat satu toast `Success, asset has been activated.` tampil

### Kuota Group tidak cukup saat Approval Workflow ON: dialog Cannot Activate
137. Tampilkan Dialog Activate dengan kondisi K11
138. Klik `[Submit]` pada footer form
139. Verifikasi dialog `Submit for Approval` tampil tanpa pemeriksaan kuota
140. Klik `[Submit for Approval]`
141. Verifikasi dialog `Cannot Activate` tampil dengan teks `Group quota exceeded. Available slots:` diikuti sisa slot dari respons
142. Klik `[OK]`
143. Verifikasi form `Register Asset` masih Draft dengan footer `[Save draft]` dan `[Submit]`

### Submit for Approval gagal karena error server dan pulih sesudah submit ulang
144. Tampilkan Dialog Activate dengan kondisi K12
145. Klik `[Submit]` pada footer form
146. Klik `[Submit for Approval]`
147. Verifikasi toast Error dengan awalan `Error, failed to` tampil sesudah `[Submit for Approval]`
148. Verifikasi dialog `Submit for Approval` tetap terbuka dengan bullet `Gudang 2 · 3 assets`
149. Verifikasi tombol `[Submit for Approval]` aktif kembali
150. Klik `[Submit for Approval]`
151. Verifikasi toast `Success, registration has been submitted.` tampil satu kali

### Submit for Approval gagal karena gangguan jaringan
152. Tampilkan Dialog Activate dengan kondisi K13
153. Klik `[Submit]` pada footer form
154. Klik `[Submit for Approval]`
155. Verifikasi toast Error `Connection problem. Please try again.` tampil dan dialog `Submit for Approval` tetap terbuka
156. Verifikasi tombol `[Submit for Approval]` aktif kembali

### Skip pairing Note menerima emoji
157. Tampilkan Dialog Activate dengan kondisi K5
158. Klik `[Submit]` pada footer form
159. Centang checkbox `Submit them without pairing TAGs (pair later)`
160. Pilih Reason `Other`
161. Ganti isi Input note dengan `Reader rusak 😊`
162. Verifikasi Input note menampilkan `Reader rusak 😊` utuh
163. Verifikasi tidak ada pesan error di bawah Input note
