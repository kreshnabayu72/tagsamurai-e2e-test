---
id: TC-FA-ASSIGN-E2E-004-transactions-filter
title: "Filter pada tab Transactions"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-FLT-1@tabel-transactions", EB-FLT-3, "EB-FLT-4@tabel-transactions", "EB-FLT-5@tabel-transactions"]
smoke: []
dependsOn: []
trace:
  "EB-FLT-1@tabel-transactions": [5, 6, 8, 10, 12, 14, 97, 101]
  EB-FLT-3: [18, 19, 22, 26, 27]
  "EB-FLT-4@tabel-transactions": [32, 33, 34, 36, 38, 41, 43, 49, 50, 54, 55, 58, 62, 63, 66, 69, 72, 75, 77, 79, 81, 83, 92, 108, 112, 115, 116, 124, 126, 129, 130, 131, 135, 136, 137]
  "EB-FLT-5@tabel-transactions": 46
anchor: [2, 88, 96, 105, 123]
coverage:
  web: automated
---

# Filter pada tab Transactions

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-004-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-004-2: Group `Head Office {runId}`.
  - DU-004-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju semua ASG DU-004-12 sampai DU-004-18, DU-004-40, dan DU-004-42.
  - DU-004-4: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-004-5: User `Sari Dewi {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Sari D`, dari `Sari Dewi {runId}`.
  - DU-004-6: User `Rina Wijaya {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Rina W`, dari `Rina Wijaya {runId}`.
  - DU-004-7: User `Dewi Anggraini {runId}`, karyawan aktif ber-akun login tanpa akses menu Assignment; anggota Division `Gudang Pusat {runId}`, `Pusat Logistik {runId}`, dan `Field Survey {runId}`, dan PIC aktif dua Division pertama.
  - DU-004-8: Division `Gudang Pusat {runId}` dengan PIC aktif `Dewi Anggraini {runId}`.
  - DU-004-9: Division `Pusat Logistik {runId}` dengan PIC aktif `Dewi Anggraini {runId}`.
  - DU-004-10: Division `Field Survey {runId}`; PIC lamanya `Dedi Hartono {runId}` berstatus `dinonaktifkan` sehingga tidak ada PIC aktif.
  - DU-004-11: Division `Arsip Lama {runId}` yang tidak menjadi Assignee ASG mana pun.
  - DU-004-12: ASG berstatus `Waiting for Approval` untuk Assignee DU-004-4, aset `Monitor LG 24MK430 {runId}`, `Keyboard Logitech K380 {runId}`, `Mouse Logitech M331 {runId}`, `Headset Jabra Evolve {runId}`, dan `Webcam Logitech C920 {runId}`, Total Asset `5`; dibuat pertama.
  - DU-004-13: ASG berstatus `Waiting for Approval` untuk Assignee Division `Gudang Pusat {runId}`, aset `Rak Besi Lion {runId}` dan `Troli Barang Krisbow {runId}`, Total Asset `2`; dibuat kedua.
  - DU-004-14: ASG berstatus `Assigned` untuk Assignee DU-004-5, aset `Laptop Dell Latitude 5440 {runId}`, `Tas Laptop Targus {runId}`, dan `Charger Dell 65W {runId}`, Total Asset `3`; dibuat ketiga.
  - DU-004-15: ASG berstatus `Assigned` untuk Assignee Division `Pusat Logistik {runId}`, tujuh aset `Forklift Toyota {runId}`, `Pallet Jack Hyster {runId}`, `Timbangan Digital Ohaus {runId}`, `Scanner Barcode Honeywell {runId}`, `Rak Pallet Besi {runId}`, `Troli Besi Dolly {runId}`, dan `Kardus Pack Besar {runId}`, Total Asset `7`; dibuat keempat.
  - DU-004-16: ASG berstatus `Waiting for Handover` untuk Assignee Division `Field Survey {runId}`, aset `Handheld GPS Garmin {runId}`, Total Asset `1`, bertanda `No PIC`; dibuat kelima. Spec ini mengganti PIC-nya lewat `Change PIC`.
  - DU-004-17: ASG berstatus `Waiting for Handover` untuk Assignee DU-004-6, aset `Tablet Samsung Tab A8 {runId}`, `Power Bank Anker {runId}`, `Casing Tablet Spigen {runId}`, dan `Stylus Samsung S Pen {runId}`, Total Asset `4`; dibuat keenam.
  - DU-004-39: Division `Distribusi Barat {runId}` pada Group `Head Office {runId}` dengan PIC aktif `Dewi Anggraini {runId}`; belum menjadi Assignee ASG mana pun.
  - DU-004-41: Division `Distribusi Timur {runId}` pada Group `Head Office {runId}` dengan PIC aktif `Dewi Anggraini {runId}`; belum menjadi Assignee ASG mana pun.
  - DU-004-18: ASG berstatus `Canceled` untuk Assignee DU-004-6 dengan aset `Printer Brother HL {runId}`; ASG sudah selesai sehingga hanya ada di tab History.
  - DU-004-45: Aset `Lemari Arsip Brother {runId}` berstatus `Available` di Group `Head Office {runId}` (dalam cakupan `Agus Prasetyo {runId}`), belum ditugaskan; ia aset ASG DU-004-40 yang dibuat langkah spec ini.
  - DU-004-46: Aset `Meja Lipat Olympic {runId}` berstatus `Available` di Group `Head Office {runId}` (dalam cakupan `Agus Prasetyo {runId}`), belum ditugaskan; ia aset ASG DU-004-42 yang dibuat langkah spec ini.
  - DU-004-47: Acuan waktu T0 adalah tanggal saat spec dijalankan; semua ASG DU-004-12 sampai DU-004-17 diajukan pada T0.

## Test Steps

### Opsi filter berasal dari data tabel
1. Ganti isi kotak search dengan `Agus Prasetyo {runId}`, tekan Enter
2. Verifikasi tabel memuat tepat 6 baris, yaitu baris untuk Assignee `Budi S`, `Gudang Pusat {runId}`, `Sari D`, `Pusat Logistik {runId}`, `Field Survey {runId}`, dan `Rina W`
3. Klik `Filter`
4. Klik field `Status`
5. Verifikasi opsi `Waiting for Approval`, `Waiting for Handover`, dan `Assigned` tampil masing-masing satu kali
6. Verifikasi opsi `Canceled`, `Rejected`, dan `Unassigned` tidak tampil karena tidak ada baris dengan status itu di tab `Transactions`
7. Klik field `Assignee`
8. Verifikasi opsi `Gudang Pusat {runId}` tampil dan opsi `Arsip Lama {runId}` tidak tampil karena bukan Assignee ASG mana pun
9. Ketik `dang Pus` pada kotak cari di dalam dropdown `Assignee`
10. Verifikasi opsi `Gudang Pusat {runId}` tampil
11. Ganti isi kotak cari di dalam dropdown `Assignee` dengan `GUDANG PUSAT {runId}`
12. Verifikasi opsi `Gudang Pusat {runId}` tampil walau huruf besar dan kecilnya berbeda
13. Ganti isi kotak cari di dalam dropdown `Assignee` dengan `{runId} tidakada`
14. Verifikasi pesan `No results found` tampil di dalam dropdown `Assignee`

### Satu field: opsi cocok, tidak cocok, dan OR
15. Klik field `Status`
16. Pilih opsi `Waiting for Approval` pada field `Status`
17. Klik `[Apply]`
18. Verifikasi baris `Budi S` dan `Gudang Pusat {runId}` tampil karena statusnya `Waiting for Approval`
19. Verifikasi baris `Sari D`, `Pusat Logistik {runId}`, `Field Survey {runId}`, dan `Rina W` tidak tampil karena statusnya bukan `Waiting for Approval`
20. Pilih opsi `Assigned` pada field `Status`
21. Klik `[Apply]`
22. Verifikasi baris `Budi S`, `Gudang Pusat {runId}`, `Sari D`, dan `Pusat Logistik {runId}` tampil karena statusnya salah satu dari `Waiting for Approval` atau `Assigned`

### AND antar field
23. Pilih opsi `Waiting for Approval` saja pada field `Status` dengan menghapus pilihan `Assigned`
24. Pilih opsi `Employee` pada field `Assignee Type`
25. Klik `[Apply]`
26. Verifikasi baris `Budi S` tampil karena memenuhi kedua saringan
27. Verifikasi baris `Gudang Pusat {runId}`, `Sari D`, dan `Pusat Logistik {runId}` tidak tampil karena masing-masing hanya memenuhi satu saringan atau tidak memenuhi keduanya

### Irisan Search dan Filter
28. Klik `[Clear Field]`
29. Pilih opsi `Waiting for Approval` pada field `Status`
30. Klik `[Apply]`
31. Ganti isi kotak search dengan `Pusat`, tekan Enter
32. Verifikasi baris `Gudang Pusat {runId}` tampil karena cocok dengan Search dan Filter
33. Verifikasi baris `Pusat Logistik {runId}` tidak tampil karena hanya cocok dengan Search
34. Verifikasi baris `Budi S` tidak tampil karena hanya cocok dengan Filter
35. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
36. Verifikasi pesan `No results found` tampil karena Search dan Filter masing-masing punya hasil tetapi irisannya kosong
37. Klik `(←)` pada kotak Search
38. Verifikasi baris `Budi S` dan `Gudang Pusat {runId}` tampil lagi dan Filter `Waiting for Approval` tetap berlaku
39. Ganti isi kotak search dengan `Pusat`, tekan Enter
40. Klik `[Clear Field]`
41. Verifikasi tabel belum berubah dan hanya baris `Gudang Pusat {runId}` yang tampil
42. Klik `[Apply]`
43. Verifikasi baris `Gudang Pusat {runId}` dan `Pusat Logistik {runId}` tampil karena Search `Pusat` tetap berlaku tanpa Filter
44. Klik `(←)` pada kotak Search

### Filter tanpa kolom dan perubahan record yang keluar atau masuk saringan
45. Klik field `No PIC`
46. Verifikasi opsi `No PIC` dan `Has PIC` tampil tanpa opsi untuk nilai kosong
47. Pilih opsi `No PIC` pada field `No PIC`
48. Klik `[Apply]`
49. Verifikasi baris `Field Survey {runId}` tampil karena bertanda `No PIC`
50. Verifikasi baris `Rina W` dan `Budi S` tidak tampil karena tidak bertanda `No PIC`
51. Klik `⋯` pada baris `Field Survey {runId}`
52. Klik `Change PIC`
53. Pilih user `Dewi Anggraini {runId}` pada dialog Select User, lalu klik `[Select]`
54. Verifikasi toast `Success, PIC has been changed to [Name].` tampil dengan nama PIC baru `Dewi Anggraini {runId}`
55. Verifikasi baris `Field Survey {runId}` tidak lagi tampil karena tidak bertanda `No PIC`
56. Pilih opsi `Has PIC` pada field `No PIC` dengan menghapus pilihan `No PIC`
57. Klik `[Apply]`
58. Verifikasi baris `Field Survey {runId}` tampil karena sekarang memenuhi saringan `Has PIC`

### Rentang Total Asset
59. Klik `[Clear Field]`
60. Isi `Min` dengan `2` dan `Max` dengan `5` pada field `Total Asset`
61. Klik `[Apply]`
62. Verifikasi baris `Gudang Pusat {runId}` (`2`) dan `Budi S` (`5`) tampil karena batas rentang inklusif
63. Verifikasi baris `Pusat Logistik {runId}` (`7`) dan `Field Survey {runId}` (`1`) tidak tampil
64. Isi hanya `Min` dengan `5` pada field `Total Asset` dengan mengosongkan `Max`
65. Klik `[Apply]`
66. Verifikasi baris `Budi S` (`5`) dan `Pusat Logistik {runId}` (`7`) tampil, dan baris `Gudang Pusat {runId}` tidak tampil
67. Isi hanya `Max` dengan `2` pada field `Total Asset` dengan mengosongkan `Min`
68. Klik `[Apply]`
69. Verifikasi baris `Gudang Pusat {runId}` (`2`) dan `Field Survey {runId}` (`1`) tampil, dan baris `Budi S` tidak tampil
70. Isi `Min` dengan `5` dan `Max` dengan `2` pada field `Total Asset`
71. Klik `[Apply]`
72. Verifikasi pesan `No results found` tampil karena tidak ada nilai di antara `5` dan `2`

### Rentang Request Date
73. Klik `[Clear Field]`
74. Pilih rentang `Request Date` dari T0 − 2 hari sampai T0 + 2 hari, lalu klik `[Apply]`
75. Verifikasi keenam baris `Budi S`, `Gudang Pusat {runId}`, `Sari D`, `Pusat Logistik {runId}`, `Field Survey {runId}`, dan `Rina W` tampil karena tanggal pengajuannya T0
76. Pilih rentang `Request Date` dari T0 − 10 hari sampai T0 − 5 hari, lalu klik `[Apply]`
77. Verifikasi pesan `No results found` tampil karena rentang berada sebelum tanggal pengajuan
78. Pilih rentang `Request Date` dari T0 sampai T0 + 3 hari, lalu klik `[Apply]`
79. Verifikasi keenam baris tampil karena batas awal rentang tepat T0
80. Pilih rentang `Request Date` dari T0 − 3 hari sampai T0, lalu klik `[Apply]`
81. Verifikasi keenam baris tampil karena batas akhir rentang tepat T0
82. Pilih rentang `Request Date` dari T0 sampai T0, lalu klik `[Apply]`
83. Verifikasi keenam baris tampil karena rentang satu hari memuat T0

### Filter pada kolom yang disembunyikan
84. Klik `[Clear Field]`
85. Klik `[Apply]`
86. Klik header kolom `Actions`
87. Hilangkan centang kolom `Assignee Type` pada panel Column Visibility
88. Verifikasi kolom `Assignee Type` tidak tampil di tabel
89. Klik field `Assignee Type`
90. Pilih opsi `Division` pada field `Assignee Type`
91. Klik `[Apply]`
92. Verifikasi baris `Gudang Pusat {runId}`, `Pusat Logistik {runId}`, dan `Field Survey {runId}` tampil dan baris `Budi S` tidak tampil walau kolom `Assignee Type` disembunyikan

### Record baru muncul sebagai opsi Assignee tanpa muat ulang
93. Klik `[Clear Field]`
94. Klik `[Apply]`
95. Klik field `Assignee`
96. Verifikasi opsi `Gudang Pusat {runId}` tampil
97. Verifikasi opsi `Distribusi Barat {runId}` tidak tampil karena belum menjadi Assignee ASG mana pun
98. Klik field `Status`
99. Asset Admin `Agus Prasetyo {runId}` mengajukan Assignment untuk Assignee Division `Distribusi Barat {runId}` dengan aset `Lemari Arsip Brother {runId}`, sehingga ASG berstatus `Waiting for Handover`
100. Klik field `Assignee`
101. Verifikasi opsi `Distribusi Barat {runId}` tampil tanpa muat ulang halaman

### Record baru yang tidak cocok dengan Filter aktif tidak tampil
102. Klik field `Status`
103. Pilih opsi `Waiting for Approval` pada field `Status`
104. Klik `[Apply]`
105. Verifikasi baris `Budi S` dan `Gudang Pusat {runId}` tampil karena statusnya `Waiting for Approval`
106. Asset Admin `Agus Prasetyo {runId}` mengajukan Assignment untuk Assignee Division `Distribusi Timur {runId}` dengan aset `Meja Lipat Olympic {runId}`, sehingga ASG berstatus `Waiting for Handover`
107. Klik `[Apply]`
108. Verifikasi baris `Distribusi Timur {runId}` tidak tampil karena statusnya bukan `Waiting for Approval`

### Search dulu lalu Filter menghasilkan irisan yang sama
109. Klik `[Clear Field]`
110. Klik `[Apply]`
111. Ganti isi kotak search dengan `Pusat {runId}`, tekan Enter
112. Verifikasi baris `Gudang Pusat {runId}` dan `Pusat Logistik {runId}` tampil karena cocok dengan Search
113. Pilih opsi `Waiting for Approval` pada field `Status`
114. Klik `[Apply]`
115. Verifikasi baris `Gudang Pusat {runId}` tampil karena cocok dengan Search dan Filter
116. Verifikasi baris `Pusat Logistik {runId}` tidak tampil karena hanya cocok dengan Search
117. Klik `(←)` pada kotak Search

### Clear Filter dan Clear Search mempertahankan Sort
118. Klik `[Clear Field]`
119. Klik `[Apply]`
120. Ketik Search `Agus Prasetyo {runId}`, tekan Enter
121. Pilih opsi `Employee` pada field `Assignee Type`
122. Klik `[Apply]`
123. Verifikasi baris `Budi S`, `Rina W`, dan `Sari D` tampil karena Assignee Type `Employee`
124. Verifikasi baris `Gudang Pusat {runId}` tidak tampil karena Assignee Type `Division`
125. Klik header kolom `Assignee`
126. Verifikasi urutan baris `Budi S`, `Rina W`, `Sari D` dari atas ke bawah sesuai nama lengkap A–Z
127. Klik `[Clear Field]`
128. Klik `[Apply]`
129. Verifikasi baris `Gudang Pusat {runId}` tampil karena Filter dilepas
130. Verifikasi kotak Search masih berisi `Agus Prasetyo {runId}`
131. Verifikasi baris `Budi S` tampil sebelum baris `Rina W`, dan baris `Rina W` sebelum baris `Sari D`, karena Sort `Assignee` A–Z tetap berlaku
132. Pilih opsi `Employee` pada field `Assignee Type`
133. Klik `[Apply]`
134. Klik `(←)` pada kotak Search
135. Verifikasi baris `Budi S`, `Rina W`, dan `Sari D` tampil
136. Verifikasi baris `Gudang Pusat {runId}` tidak tampil karena Filter `Employee` tetap berlaku
137. Verifikasi baris `Budi S` tampil sebelum baris `Rina W`, dan baris `Rina W` sebelum baris `Sari D`, karena Sort `Assignee` A–Z tetap berlaku
