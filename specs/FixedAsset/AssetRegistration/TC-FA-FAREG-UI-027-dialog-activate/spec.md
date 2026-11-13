---
id: TC-FA-FAREG-UI-027-dialog-activate
title: "Dialog Activate: konfirmasi Submit, Skip pairing, blok kuota, dan toast"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-REG-03", "D-REG-08", "FAREG-LOGIC-01h", "FAREG-LOGIC-01j", "FAREG-LOGIC-04j", "FAREG-LOGIC-04k", "FAREG-LOGIC-05n", "T-REG-02", "T-REG-03", "T-REG-12", "T-REG-13", "V-REG-11", "V-REG-12", "V-REG-13", "V-REG-18", "§4.1#r5", "§4.1#b12", "§4.2.3#b2", "§9.4.2#r29", "§9.6#r3", "§9.9#r9", "§9.9#r10", "§9.9#r17", "EB-ERR-1@activate", "EB-FB-1@activate", "EB-FB-2@dialog-blok", "EB-FRM-1@dialog-activate", "EB-FRM-4@skip-pairing-note", "EB-FRM-7@dialog-activate"]
smoke: []
dependsOn: []
trace:
  "D-REG-03": [4, 5, 6, 7, 24, 27, 28, 29, 41, 42, 43, 51, 52, 58, 61, 64, 66, 96, 97]
  "D-REG-08": [102, 103, 104]
  "FAREG-LOGIC-01h": [2, 7, 29]
  "FAREG-LOGIC-01j": 42
  "FAREG-LOGIC-04j": [39, 43]
  "FAREG-LOGIC-04k": [53, 57, 58, 60, 61, 63, 64, 66, 93]
  "FAREG-LOGIC-05n": [4, 8, 41, 100, 102, 106]
  "T-REG-02": [21, 35, 93, 115]
  "T-REG-03": 31
  "T-REG-12": 111
  "T-REG-13": 121
  "V-REG-11": [51, 55]
  "V-REG-12": 68
  "V-REG-13": [46, 47]
  "V-REG-18": [75, 77, 80, 83]
  "§4.1#r5": [4, 9, 27]
  "§4.1#b12": [21, 31]
  "§4.2.3#b2": [5, 6, 7, 8, 9, 24, 41, 42, 66, 96, 97]
  "§9.4.2#r29": 55
  "§9.6#r3": [21, 31, 35, 111]
  "§9.9#r9": [52, 55]
  "§9.9#r10": [68, 75, 77, 86]
  "§9.9#r17": [43, 44]
  "EB-ERR-1@activate": [111, 112, 113, 115, 121, 122]
  "EB-FB-1@activate": [21, 31, 93, 111]
  "EB-FB-2@dialog-blok": [16, 107]
  "EB-FRM-1@dialog-activate": [126, 127, 130, 132]
  "EB-FRM-4@skip-pairing-note": [75, 77]
  "EB-FRM-7@dialog-activate": [10, 12, 13, 17]
anchor: [15, 38, 74, 79, 82, 85, 129]
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
52. Verifikasi opsi Reason memuat `Device unavailable`, `TAG not yet available`, `TAG damaged`, dan `Other`
53. Verifikasi dialog memuat satu Select reason untuk ketiga aset
54. Klik `[Activate]`
55. Verifikasi pesan `You must pick a reason` tampil di bawah Select reason
56. Pilih Reason `Device unavailable`
57. Verifikasi Select reason menampilkan `Device unavailable`
58. Verifikasi Input note tidak tampil untuk Reason `Device unavailable`
59. Pilih Reason `TAG not yet available`
60. Verifikasi Select reason menampilkan `TAG not yet available`
61. Verifikasi Input note tidak tampil untuk Reason `TAG not yet available`
62. Pilih Reason `TAG damaged`
63. Verifikasi Select reason menampilkan `TAG damaged`
64. Verifikasi Input note tidak tampil untuk Reason `TAG damaged`
65. Pilih Reason `Other`
66. Verifikasi Input note tampil dengan placeholder `Enter note`
67. Klik `[Activate]`
68. Verifikasi pesan `Note must not be empty` tampil di bawah Input note

### Skip pairing Note: batas 120 karakter
69. Tampilkan Dialog Activate dengan kondisi K5
70. Klik `[Submit]` pada footer form
71. Centang checkbox `Submit them without pairing TAGs (pair later)`
72. Pilih Reason `Other`
73. Ganti isi Input note dengan `Reader TAG di Gudang 1 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456789012345678901` (120 karakter)
74. Verifikasi Input note menampilkan `Reader TAG di Gudang 1 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456789012345678901`
75. Verifikasi tidak ada pesan error di bawah Input note
76. Ganti isi Input note dengan `Reader TAG di Gudang 1 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 01234567890123456789012` (121 karakter)
77. Verifikasi pesan `Max. 120 characters` tampil di bawah Input note
78. Ganti isi Input note dengan `Reader  TAG  di  Gudang  1  sedang  diperbaiki  sehingga  pemasangan  Tag  ditunda  sampai  pekan  depan.  Kode 01234567` (120 karakter)
79. Verifikasi Input note menampilkan `Reader  TAG  di  Gudang  1  sedang  diperbaiki  sehingga  pemasangan  Tag  ditunda  sampai  pekan  depan.  Kode 01234567`
80. Verifikasi tidak ada pesan error di bawah Input note
81. Ganti isi Input note dengan `Reader TAG Kantor Cabang Medan Élan 𝒜 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456` (120 karakter)
82. Verifikasi Input note menampilkan `Reader TAG Kantor Cabang Medan Élan 𝒜 sedang diperbaiki sehingga pemasangan Tag ditunda sampai pekan depan. Kode 0123456`
83. Verifikasi tidak ada pesan error di bawah Input note
84. Ganti isi Input note dengan `R` (1 karakter)
85. Verifikasi Input note menampilkan `R`
86. Verifikasi tidak ada pesan error di bawah Input note

### Skip pairing berhasil dengan satu alasan untuk semua aset
87. Tampilkan Dialog Activate dengan kondisi K5
88. Klik `[Submit]` pada footer form
89. Centang checkbox `Submit them without pairing TAGs (pair later)`
90. Pilih Reason `Other`
91. Ganti isi Input note dengan `Reader TAG sedang diperbaiki`
92. Klik `[Activate]`
93. Verifikasi toast `Success, asset has been activated.` tampil setelah Skip pairing

### Dialog untuk satu aset hanya kurang Tag memakai peringatan tunggal
94. Tampilkan Dialog Activate dengan kondisi K6
95. Klik `[Submit]` pada footer form
96. Verifikasi dialog `Activate Assets` tampil dengan bullet `Gudang 1 · 1 asset`
97. Verifikasi peringatan `1 asset is not paired to a TAG yet.` tampil

### Kuota Group tidak cukup: dialog Cannot Activate
98. Tampilkan Dialog Activate dengan kondisi K7
99. Klik `[Submit]` pada footer form
100. Verifikasi dialog `Activate Assets` tampil tanpa pemeriksaan kuota
101. Klik `[Activate]`
102. Verifikasi dialog `Cannot Activate` tampil dengan teks `Group quota exceeded. Available slots:` diikuti sisa slot dari respons
103. Verifikasi dialog `Cannot Activate` memuat teks `Please contact administrator to increase quota.`
104. Verifikasi dialog `Cannot Activate` hanya memuat tombol `[OK]`
105. Klik `[OK]`
106. Verifikasi form `Register Asset` masih Draft dengan footer `[Save draft]` dan `[Submit]`
107. Verifikasi dialog `Cannot Activate` tertutup tanpa toast

### Activate gagal karena error server dan pulih sesudah submit ulang
108. Tampilkan Dialog Activate dengan kondisi K8
109. Klik `[Submit]` pada footer form
110. Klik `[Activate]`
111. Verifikasi toast Error dengan awalan `Error, failed to` tampil
112. Verifikasi dialog `Activate Assets` tetap terbuka dengan bullet `Gudang 1 · 3 assets`
113. Verifikasi tombol `[Activate]` aktif kembali
114. Klik `[Activate]`
115. Verifikasi toast `Success, asset has been activated.` tampil satu kali

### Activate gagal karena gangguan jaringan mempertahankan input
116. Tampilkan Dialog Activate dengan kondisi K9
117. Klik `[Submit]` pada footer form
118. Centang checkbox `Submit them without pairing TAGs (pair later)`
119. Pilih Reason `TAG damaged`
120. Klik `[Activate]`
121. Verifikasi toast Error `Connection problem. Please try again.` tampil dan dialog `Activate Assets` tetap terbuka
122. Verifikasi Select reason masih menampilkan `TAG damaged`

### Activate lambat: Saving dan satu request
123. Tampilkan Dialog Activate dengan kondisi K10
124. Klik `[Submit]` pada footer form
125. Klik `[Activate]`
126. Verifikasi tombol `[Activate]` menampilkan loading dan Disabled
127. Verifikasi `[Cancel]` dan `✕` Disabled
128. Klik `[Activate]` sekali lagi
129. Verifikasi tombol `[Activate]` masih menampilkan loading
130. Verifikasi tidak ada pengiriman Activate kedua
131. Tunggu sampai respons Activate diterima
132. Verifikasi tepat satu toast `Success, asset has been activated.` tampil
