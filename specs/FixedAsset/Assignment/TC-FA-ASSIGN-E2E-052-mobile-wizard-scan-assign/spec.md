---
id: TC-FA-ASSIGN-E2E-052-mobile-wizard-scan-assign
title: "Mobile Scan > Assign: wizard, kartu aset, dan offline"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.6#p1", "§4.6#p3", "§4.6#b1", "§4.6#b2", "§4.6#b3", "§4.6#b4", "§4.6#b5", "§4.6#b6", "§10#r8", "EC-ASG-74", "§4.2.13#b3"]
smoke: []
dependsOn: []
trace:
  "§4.6#p1": 4
  "§4.6#p3": [16, 17, 26, 28, 31, 32, 36, 46, 48, 50, 51, 52, 55, 56, 58, 59, 61, 64, 67, 70, 71, 72]
  "§4.6#b1": [20, 21]
  "§4.6#b2": [3, 6, 8, 9, 11, 12, 13, 113, 116, 117]
  "§4.6#b3": [29, 34, 37, 39, 43, 136, 139]
  "§4.6#b4": [81, 83, 84, 87, 128, 129]
  "§4.6#b5": [89, 90]
  "§4.6#b6": [74, 94, 98, 100, 102, 104, 105]
  "§10#r8": 4
  "EC-ASG-74": [102, 105, 108, 109]
  "§4.2.13#b3": [3, 6]
anchor: [42, 66, 112]
coverage:
  android: manual
---

# Mobile Scan > Assign: wizard, kartu aset, dan offline

## Prerequisites
- Aktor: Asset Admin `Adi Pratama {runId}` (DU-052-1) pada aplikasi native Android, lalu Read Only `Rudi Kurniawan {runId}` (DU-052-19) pada kelompok terakhir; `Agus Prasetyo {runId}` memicu perubahan sebagai pengaju
- Layar awal: Menu Scan pada aplikasi Android
- Data:
  - DU-052-1: User (Aktor Asset Admin), Name `Adi Pratama {runId}`, Role `Asset Admin`, Cakupan `Group penugasan Head Office {runId} beserta descendant IT Head Office {runId}`
  - DU-052-2: User (Assignee Employee dengan kartu karyawan QR), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-052-3: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`
  - DU-052-4: User (Anggota Division), Name `Sari Dewi {runId}`, Role `tanpa role Assignment`
  - DU-052-5: Group (Group utama), Name `Head Office {runId}`, Sub-group `IT Head Office {runId}`
  - DU-052-6: Group (Group di luar cakupan aktor), Name `Branch Surabaya {runId}`
  - DU-052-7: Division (Division dengan PIC), Name `Finance {runId}`, PIC `Budi Santoso {runId}`, Anggota lain `Sari Dewi {runId}`
  - DU-052-8: Category (Kategori yang hanya boleh ditugaskan ke Employee), Name `Kendaraan {runId}`, Allowed assignee `Employee saja`
  - DU-052-9: Asset (Aset Available dalam cakupan), Name `Laptop Dell Latitude 5420 {runId}`, Group `Head Office {runId}`, Status `Available`, TAG `QR`
  - DU-052-10: Asset (Aset Available di sub-group dengan approval), Name `Laptop Lenovo ThinkPad T14 {runId}`, Group `IT Head Office {runId}`, Status `Available`, TAG `QR`, Approver `Agus Prasetyo {runId}`
  - DU-052-11: Asset (Aset Available kategori Kendaraan), Name `Toyota Avanza {runId}`, Group `Head Office {runId}`, Status `Available`, Kategori `Kendaraan {runId}`, TAG `QR`
  - DU-052-12: Asset (Aset Available yang diambil ASG lain di tengah wizard), Name `Keyboard Logitech K380 {runId}`, Group `Head Office {runId}`, Status `Available`, TAG `QR`
  - DU-052-13: Asset (Aset Available di luar cakupan aktor), Name `Monitor LG 24 {runId}`, Group `Branch Surabaya {runId}`, Status `Available`, TAG `QR`
  - DU-052-14: Assignment (ASG Waiting for Handover yang membuat aset tidak layak), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-052-15: Assignment (ASG Assigned), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Camera Sony A7 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-052-16: Draft (Draft yang sudah tersimpan di server), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Mouse Logitech MX Master {runId}`, Purpose `Perangkat kerja tim lapangan`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-052-17: Assignment (Input Purpose perubahan Draft yang ditolak), Purpose `Pinjaman sementara tim audit`, Aset `Mouse Logitech MX Master {runId}`
  - DU-052-18: Assignment (Input Purpose wizard), Purpose `Perangkat kerja tim lapangan`, Aset `Laptop Dell Latitude 5420 {runId}`
  - DU-052-19: User (Aktor Read Only), Name `Rudi Kurniawan {runId}`, Role `Read Only`, Cakupan `Seluruh client`
  - DU-052-20: User (Karyawan tanpa akun login), Name `Tono Wibowo {runId}`, Akun login `Tidak ada`
  - DU-052-21: Division (Division tanpa anggota yang bisa login), Name `Logistik {runId}`, Anggota `Tidak ada yang bisa login`
  - DU-052-22: Category (Kategori yang menolak Allow Assign), Name `Peralatan Terlarang {runId}`, Allow Assign efektif `Deny`
  - DU-052-23: Asset (Aset Available pada kategori yang menolak Allow Assign), Name `Printer Epson L3250 {runId}`, Group `Head Office {runId}`, Status `Available`, Kategori `Peralatan Terlarang {runId}`, TAG `QR`
  - DU-052-24: Asset (Aset Available yang diambil ASG lain saat Review), Name `Monitor Dell P2422H {runId}`, Group `Head Office {runId}`, Status `Available`, TAG `QR`
  - DU-052-25: Assignment (Input Purpose aksi massal), Purpose `Pemakaian bersama tim audit`, Aset `Laptop Dell Latitude 5420 {runId}` dan `Laptop Lenovo ThinkPad T14 {runId}`
- Kondisi:
  - Feature Suite Assignment berada pada level `Full`
  - Akun `Adi Pratama {runId}` dan `Rudi Kurniawan {runId}` aktif, dan aplikasi native Android terpasang di perangkat
  - Max assets per assignee efektif bernilai `5` (nilai Company default) untuk `Laptop Dell Latitude 5420 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, dan `Toyota Avanza {runId}`, tanpa override per Category atau per aset

## Test Steps

### Hasil scan pertama untuk aset tersedia
1. Buka menu Scan pada aplikasi Android
2. Scan TAG aset `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi tombol `[Assign]` tampil
4. Verifikasi aplikasi native Android menampilkan kode, nama `Laptop Dell Latitude 5420 {runId}`, dan status `Available` aset hasil scan

### Hasil scan pertama untuk aset yang sedang ditugaskan
5. Scan TAG aset `Camera Sony A7 {runId}`
6. Verifikasi tombol `[Unassign]` tampil

### Hasil scan pertama untuk aset tidak layak
7. Scan TAG aset `Printer HP M404 {runId}`
8. Verifikasi tombol `[Assign]` tampil Disabled
9. Verifikasi alasan `This asset is already in another transaction.` tampil di bawah tombol `[Assign]` untuk aset `Printer HP M404 {runId}`

### Hasil scan pertama untuk aset di luar cakupan Group
10. Scan TAG aset `Monitor LG 24 {runId}`
11. Verifikasi pesan `This asset belongs to` diikuti nama Group `Branch Surabaya {runId}` tampil
12. Verifikasi identitas, foto, dan atribut aset `Monitor LG 24 {runId}` tidak tampil
13. Verifikasi tombol `[Assign]` tidak tampil

### Langkah 1 Asset
14. Scan TAG aset `Laptop Dell Latitude 5420 {runId}`
15. Ketuk `[Assign]`
16. Verifikasi kode, nama `Laptop Dell Latitude 5420 {runId}`, dan status `Available` aset tampil pada langkah Asset
17. Verifikasi tombol `[+ Scan more]` tampil
18. Ketuk `[+ Scan more]`
19. Scan TAG aset `Printer HP M404 {runId}`
20. Verifikasi alasan `This asset is already in another transaction.` tampil untuk aset `Printer HP M404 {runId}`
21. Verifikasi aset `Printer HP M404 {runId}` tidak ditambahkan ke daftar aset
22. Ketuk `[+ Scan more]`
23. Scan TAG aset `Laptop Lenovo ThinkPad T14 {runId}`
24. Ketuk `[+ Scan more]`
25. Scan TAG aset `Toyota Avanza {runId}`
26. Verifikasi aset `Laptop Dell Latitude 5420 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, dan `Toyota Avanza {runId}` tampil pada daftar aset

### Langkah 2 Assignee dengan scan kartu karyawan
27. Lanjut ke langkah Assignee
28. Verifikasi tab `Employees` dan `Divisions` tampil
29. Verifikasi karyawan `Tono Wibowo {runId}` pada tab `Employees` berstatus `Blocked` dengan alasan `No login account. Only employees who can sign in can be assignees.`
30. Scan QR kartu karyawan `Budi Santoso {runId}`
31. Verifikasi Assignee `Budi S` terpilih
32. Verifikasi teks bantu `3 of 5 assigned` tampil

### Langkah 2 Assignee Division memunculkan pilihan PIC
33. Ketuk tab `Divisions`
34. Verifikasi `Logistik {runId}` pada tab `Divisions` berstatus `Blocked` dengan alasan `No member can sign in, so no one can be the PIC.`
35. Pilih `Finance {runId}` pada tab `Divisions`
36. Verifikasi pilihan PIC tampil
37. Verifikasi kartu aset `Toyota Avanza {runId}` ditandai caption ⚠ `This asset can no longer be assigned.` karena tidak lolos Allowed assignee
38. Ketuk ikon ⚠ pada kartu aset `Toyota Avanza {runId}`
39. Verifikasi alasan `This asset can't be assigned to a division.` tersampaikan pada tooltip ⚠ kartu aset `Toyota Avanza {runId}`
40. Buka menu ⋯ pada kartu aset `Toyota Avanza {runId}`
41. Klik `Remove from List`
42. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` tetap tampil pada daftar aset
43. Verifikasi kartu aset `Toyota Avanza {runId}` tidak ada lagi pada daftar aset
44. Ketuk tab `Employees`
45. Cari nama `Budi Santoso {runId}` pada tab `Employees`
46. Verifikasi `Budi Santoso {runId}` tampil pada hasil pencarian
47. Pilih `Budi Santoso {runId}` dari hasil pencarian
48. Verifikasi Assignee `Budi S` terpilih

### Langkah 3 Purpose per aset
49. Lanjut ke langkah Purpose
50. Verifikasi satu kartu Purpose untuk aset `Laptop Dell Latitude 5420 {runId}` dan satu untuk aset `Laptop Lenovo ThinkPad T14 {runId}`
51. Verifikasi Purpose pada kartu aset `Laptop Dell Latitude 5420 {runId}` dan `Laptop Lenovo ThinkPad T14 {runId}` kosong sebelum diisi
52. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` tidak menampilkan kotak seleksi
53. Ketuk kartu aset `Laptop Dell Latitude 5420 {runId}`
54. Isi Purpose dengan `Perangkat kerja tim lapangan`
55. Verifikasi Purpose `Perangkat kerja tim lapangan` tampil pada kartu aset `Laptop Dell Latitude 5420 {runId}`
56. Verifikasi kartu aset `Laptop Lenovo ThinkPad T14 {runId}` mewarisi Purpose `Perangkat kerja tim lapangan` dari kartu aset `Laptop Dell Latitude 5420 {runId}`
57. Tekan lama kartu aset `Laptop Dell Latitude 5420 {runId}`
58. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` terpilih
59. Verifikasi kotak seleksi kosong muncul pada kartu aset `Laptop Lenovo ThinkPad T14 {runId}`
60. Ketuk kartu aset `Laptop Lenovo ThinkPad T14 {runId}`
61. Verifikasi bar aksi massal tampil dengan tombol `[Set Purpose]`
62. Ketuk `[Set Purpose]`
63. Isi Purpose dengan `Pemakaian bersama tim audit`
64. Verifikasi Purpose `Pemakaian bersama tim audit` tampil pada kartu aset `Laptop Dell Latitude 5420 {runId}` dan `Laptop Lenovo ThinkPad T14 {runId}` yang terpilih
65. Ketuk `[✕]` pada bar aksi massal
66. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` dan `Laptop Lenovo ThinkPad T14 {runId}` tetap tampil pada daftar Purpose
67. Verifikasi kotak seleksi tidak tampil pada kartu aset `Laptop Dell Latitude 5420 {runId}` dan `Laptop Lenovo ThinkPad T14 {runId}`
68. Isi Purpose kartu aset `Laptop Lenovo ThinkPad T14 {runId}` dengan `Perangkat kerja tim lapangan`

### Langkah 4 Review dan Submit
69. Lanjut ke langkah Review
70. Verifikasi pembagian ASG per Group tampil untuk Group `Head Office {runId}` dan Group `IT Head Office {runId}`
71. Verifikasi blok Approval menyebut approver `Agus Prasetyo {runId}` dan Approval type untuk aset `Laptop Lenovo ThinkPad T14 {runId}`
72. Verifikasi blok Approval aset `Laptop Dell Latitude 5420 {runId}` menyebut `No approval needed: [Asset Name].` dengan `[Asset Name]` berisi `Laptop Dell Latitude 5420 {runId}`
73. Ketuk `[Submit]`
74. Verifikasi pengajuan terkirim saat perangkat online

### Kartu yang tidak lagi layak di tengah wizard
75. Scan TAG aset `Keyboard Logitech K380 {runId}`
76. Ketuk `[Assign]`
77. Lanjut ke langkah Assignee
78. Scan QR kartu karyawan `Budi Santoso {runId}`
79. `Agus Prasetyo {runId}` mengajukan ASG yang memuat aset `Keyboard Logitech K380 {runId}`
80. Lanjut ke langkah berikutnya
81. Verifikasi kartu aset `Keyboard Logitech K380 {runId}` ditandai caption ⚠ `This asset can no longer be assigned.`
82. Ketuk ikon ⚠ pada kartu aset `Keyboard Logitech K380 {runId}`
83. Verifikasi alasan `This asset is already in another transaction.` tersampaikan pada tooltip ⚠ kartu aset `Keyboard Logitech K380 {runId}`
84. Verifikasi tombol `[Submit]` diblokir selama kartu aset `Keyboard Logitech K380 {runId}` masih ada
85. Buka menu ⋯ pada kartu aset `Keyboard Logitech K380 {runId}`
86. Klik `Remove from List`
87. Verifikasi tombol `[Submit]` tidak lagi diblokir

### Aksi cepat pada kartu penugasan
88. Buka daftar penugasan pada aplikasi Android
89. Verifikasi kartu aset `Printer HP M404 {runId}` berstatus `Waiting for Handover` menampilkan aksi cepat `[Hand Over]`
90. Verifikasi kartu aset `Camera Sony A7 {runId}` berstatus `Assigned` menampilkan aksi cepat `[Unassign]`

### Perilaku offline
91. Perangkat berada dalam keadaan offline
92. Mulai wizard Assign dengan aset `Mouse Logitech MX Master {runId}`
93. Ketuk `[Save Draft]`
94. Verifikasi Draft baru tersimpan di perangkat
95. Buka Draft yang sudah tersimpan di server untuk aset `Mouse Logitech MX Master {runId}`
96. Isi Purpose Draft itu dengan `Pinjaman sementara tim audit`
97. Ketuk `[Save Draft]`
98. Verifikasi perubahan Draft yang sudah ada tidak tersimpan selama offline
99. Ketuk `[Submit]`
100. Verifikasi pengajuan tidak terkirim selama offline
101. Scan TAG aset `Printer HP M404 {runId}` pada halaman Handover dan ambil foto Handover
102. Verifikasi hasil scan dan foto tersimpan lokal dengan status `Pending sync`
103. Scan TAG aset `Camera Sony A7 {runId}` pada halaman Unassign dan ambil foto Unassign
104. Verifikasi hasil scan dan foto Unassign tersimpan lokal dengan status `Pending sync`
105. Verifikasi konfirmasi dan perubahan status menunggu online
106. `Agus Prasetyo {runId}` membatalkan ASG yang memuat aset `Printer HP M404 {runId}`
107. Perangkat kembali online dan sinkronisasi berjalan
108. Verifikasi ASG yang memuat aset `Printer HP M404 {runId}` berstatus `Canceled` mengikuti server
109. Verifikasi aktor diberi tahu bahwa perubahan lokal tidak dipakai

### Tombol Assign tidak tampil bagi aktor tanpa hak Assignment
110. Masuk sebagai Read Only `Rudi Kurniawan {runId}` pada aplikasi Android
111. Scan TAG aset `Laptop Dell Latitude 5420 {runId}`
112. Verifikasi hasil scan aset `Laptop Dell Latitude 5420 {runId}` tampil
113. Verifikasi tombol `[Assign]` tidak tampil

### Alasan aturan Transaction Settings pada tombol Assign
114. Masuk sebagai Asset Admin `Adi Pratama {runId}` pada aplikasi Android
115. Scan TAG aset `Printer Epson L3250 {runId}`
116. Verifikasi tombol `[Assign]` tampil Disabled
117. Verifikasi alasan `Assigning isn't allowed for [Category].` dengan `[Category]` berisi `Peralatan Terlarang {runId}` tampil di bawah tombol `[Assign]`

### Kelayakan dinilai ulang saat Submit
118. Scan TAG aset `Monitor Dell P2422H {runId}`
119. Ketuk `[Assign]`
120. Lanjut ke langkah Assignee
121. Scan QR kartu karyawan `Budi Santoso {runId}`
122. Lanjut ke langkah Purpose
123. Ketuk kartu aset `Monitor Dell P2422H {runId}`
124. Isi Purpose dengan `Perangkat kerja tim lapangan`
125. Lanjut ke langkah Review
126. `Agus Prasetyo {runId}` mengajukan ASG yang memuat aset `Monitor Dell P2422H {runId}`
127. Ketuk `[Submit]`
128. Verifikasi pengajuan tidak terkirim karena kelayakan aset dinilai ulang saat Submit
129. Verifikasi kartu aset `Monitor Dell P2422H {runId}` ditandai caption ⚠ `This asset can no longer be assigned.`

### Caption ⚠ hilang setelah Assignee diganti
130. Buka menu Scan pada aplikasi Android
131. Scan TAG aset `Toyota Avanza {runId}`
132. Ketuk `[Assign]`
133. Lanjut ke langkah Assignee
134. Ketuk tab `Divisions`
135. Pilih `Finance {runId}` pada tab `Divisions`
136. Verifikasi kartu aset `Toyota Avanza {runId}` ditandai caption ⚠ `This asset can no longer be assigned.` karena tidak lolos Allowed assignee
137. Ketuk tab `Employees`
138. Scan QR kartu karyawan `Budi Santoso {runId}`
139. Verifikasi kartu aset `Toyota Avanza {runId}` tidak lagi ditandai caption ⚠ `This asset can no longer be assigned.`
