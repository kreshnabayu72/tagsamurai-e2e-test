---
id: TC-FA-BORROW-E2E-004-tabel-transactions-kolom-paginasi-download
title: "Setup Column bertahan sesudah muat ulang, paginasi, dan Download tabel Transactions mengikuti saringan dan kolom tampil"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceRules: ["F-BORROW-17", "§5#r3", "§5#r7", "§5#r9", "EB-FB-2@download", "EB-KOL-2@tabel-transactions", "EB-DL-1@tabel-transactions", "EB-DL-2@tabel-transactions", "EB-DL-3@tabel-transactions", "EB-DL-4"]
smoke: ["EB-DL-4"]
dependsOn: []
trace:
  "F-BORROW-17": [41, 51, 56]
  "§5#r3": [1, 3, 5, 8, 10, 13, 15, 17, 19, 22, 28, 32, 73, 74, 76, 79, 81, 82]
  "§5#r7": [37, 40, 45]
  "§5#r9": [127]
  "EB-FB-2@download": [42]
  "EB-KOL-2@tabel-transactions": [89, 90, 92, 93, 94, 104, 105, 106, 107, 109, 110, 112, 113, 114, 116, 117]
  "EB-DL-1@tabel-transactions": [41, 51, 56]
  "EB-DL-2@tabel-transactions": [42]
  "EB-DL-3@tabel-transactions": [40, 45]
  "EB-DL-4": [60, 63]
anchor: []
coverage:
  web: automated
---

# Setup Column bertahan sesudah muat ulang, paginasi, dan Download tabel Transactions mengikuti saringan dan kolom tampil

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-004-2), cakupan seluruh client, di entitas khusus `Entitas Borrow Paginasi {runId}` (DU-004-1) yang tidak dipakai spec lain.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-004-1: Entitas `Entitas Borrow Paginasi {runId}`, Group `Head Office`.
  - DU-004-2: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client.
  - DU-004-3: User `Admin Lain {runId}`, role Total Control, cakupan seluruh client; belum pernah mengubah kolom tabel Transactions.
  - DU-004-4: 10 BRW Group `Head Office` berstatus Waiting for Handover, Borrower `Peminjam A{n} {runId}`, masing-masing satu aset dengan Total Asset `1`.
  - DU-004-5: 91 BRW Group `Head Office` berstatus Borrowed, Borrower `Peminjam B{n} {runId}`, masing-masing satu aset dengan Total Asset `1`.
  - DU-004-6: 101 aset `Aset Uji {n} {runId}`, masing-masing milik satu BRW di atas.
  - Seluruh BRW di entitas ini berjumlah 101 dan tidak ada BRW lain, sehingga tabel memuat 11 halaman pada 10 baris per halaman dan halaman 11 memuat 1 baris.
  - DU-004-7: nomor halaman yang diketik: `0`, `-1`, `12`, dan `abc`.
  - DU-004-8: Search `Tidak Ada {runId}` yang tidak cocok dengan baris mana pun.
- Kondisi:
  - Akun `Admin Borrow {runId}` dan akun `Admin Lain {runId}` aktif, dan kredensialnya disediakan fase 2.

## Test Steps

### Paginasi bawaan dan pilihan ukuran halaman
1. Verifikasi tabel memuat 10 baris di halaman 1
2. Isi nomor halaman dengan `11`, tekan Enter
3. Verifikasi halaman 11 memuat 1 baris
4. Klik pilihan jumlah baris per halaman
5. Verifikasi pilihan `10`, `25`, `50`, dan `100` tampil dan tidak ada pilihan `All`
6. Pilih `100`
7. Pindah ke halaman 1
8. Verifikasi halaman 1 memuat 100 baris
9. Pindah ke halaman 2
10. Verifikasi halaman 2 memuat 1 baris
11. Pilih `10`

### Nomor halaman yang tidak valid
12. Isi nomor halaman dengan `0`, tekan Enter
13. Verifikasi tabel tetap memuat baris data
14. Isi nomor halaman dengan `-1`, tekan Enter
15. Verifikasi tabel tetap memuat baris data
16. Isi nomor halaman dengan `12`, tekan Enter
17. Verifikasi tabel tetap memuat baris data
18. Isi nomor halaman dengan `abc`, tekan Enter
19. Verifikasi tabel tetap memuat baris data

### Search dan Apply Filter mengembalikan paginasi ke halaman 1
20. Pindah ke halaman 3
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi halaman aktif adalah halaman 1
23. Pindah ke halaman 3
24. Klik `Filter`
25. Klik field `Status`
26. Pilih opsi `Borrowed`
27. Klik `[Apply]`
28. Verifikasi halaman aktif adalah halaman 1 dan tabel memuat lebih dari satu halaman hasil
29. Klik `[Clear Field]`
30. Pilih opsi `Waiting for Handover` pada field `Status`
31. Klik `[Apply]`
32. Verifikasi tabel memuat 10 baris di halaman 1 dan tidak ada halaman 2

### Download tanpa Search dan Filter memuat semua baris, tanpa toast sukses
33. Klik `[Clear Field]`
34. Klik `[Apply]`
35. Klik `(←)` pada kotak Search
36. Arahkan kursor ke tombol `Download`
37. Verifikasi nama fungsi `Download` tersampaikan pada tombol `Download` saat kursor diarahkan
38. Klik `Download`
39. Pilih `Download as CSV`
40. Verifikasi berkas terunduh dengan nama `Borrow-Transactions` dan ekstensi `.csv`
41. Verifikasi berkas memuat 101 baris data, tidak dibatasi 10 baris halaman
42. Verifikasi tidak ada toast sukses yang tampil
43. Klik `Download`
44. Pilih `Download as XLSX`
45. Verifikasi berkas terunduh dengan nama `Borrow-Transactions` dan ekstensi `.xlsx`

### Download mengikuti Filter dan kolom yang ditampilkan
46. Klik `Filter`
47. Pilih opsi `Waiting for Handover` pada field `Status`
48. Klik `[Apply]`
49. Klik `Download`
50. Pilih `Download as CSV`
51. Verifikasi berkas memuat 10 baris data
52. Klik header kolom Actions `⋯`
53. Hapus centang `Group` pada panel Column Visibility
54. Klik `Download`
55. Pilih `Download as CSV`
56. Verifikasi berkas memuat 10 baris data tanpa kolom `Group`
57. Klik `[Clear Field]`
58. Klik `[Apply]`

### Download dengan nol baris menghasilkan berkas berisi header saja
59. Ketik Search `Tidak Ada {runId}`, tekan Enter
60. Verifikasi tabel tidak memuat baris dan menampilkan `No results found` untuk Search `Tidak Ada {runId}`
61. Klik `Download`
62. Pilih `Download as CSV`
63. Verifikasi berkas hanya memuat baris header dan tidak memuat baris data
64. Klik `(←)` pada kotak Search

### Pemulihan state List sesudah muat ulang, Back dari Detail, dan klik menu yang sama
65. Ketik Search `{runId}`, tekan Enter
66. Klik `Filter`
67. Isi Total Asset `Min` dengan `1` dan `Max` dengan `1`
68. Klik `[Apply]`
69. Klik header kolom `Status`
70. Klik header kolom `Status`
71. Pindah ke halaman 11
72. Muat ulang halaman
73. Verifikasi isi kotak search tetap `{runId}` dan halaman aktif tetap halaman 11
74. Verifikasi baris di halaman 11 berstatus `Waiting for Handover`, sehingga Sort tetap berlaku
75. Klik `Filter`
76. Verifikasi field Total Asset di Filter Panel tetap berisi `Min` `1` dan `Max` `1`
77. Klik Transaction ID pada baris di halaman 11
78. Kembali ke halaman `Transactions > Borrow` lewat tombol Back browser
79. Verifikasi isi kotak search tetap `{runId}` dan halaman aktif tetap halaman 11
80. Klik menu `Borrow` pada sidebar
81. Verifikasi kotak Search kosong dan halaman aktif adalah halaman 1
82. Verifikasi seluruh 10 baris di halaman 1 berstatus `Waiting for Handover`, sehingga Sort kembali ke urutan awal

### Setup Column menyimpan kolom tambahan, urutan, dan pin ke akun
83. Klik header kolom Actions `⋯`
84. Klik `Setup Column...`
85. Centang `Source` pada modal Setup Column
86. Seret kolom `Status` ke posisi paling atas daftar kolom
87. Klik ikon pin pada kolom `Status`
88. Klik `[Save]`
89. Verifikasi kolom `Source` tampil
90. Verifikasi kolom `Status` menjadi kolom pertama dan tetap di-pin

### Konfigurasi kolom tersimpan di akun
91. Muat ulang halaman
92. Verifikasi kolom `Group` tidak tampil
93. Verifikasi kolom `Source` tampil
94. Verifikasi kolom `Status` menjadi kolom pertama dan tetap di-pin
95. Ketik Search `{runId}`, tekan Enter
96. Klik `Filter`
97. Isi Total Asset `Min` dengan `1` dan `Max` dengan `1`
98. Klik `[Apply]`
99. Klik header kolom `Status`
100. Klik header kolom `Status`
101. Pindah ke halaman 11
102. Keluar dari akun
103. Masuk kembali sebagai `Admin Borrow {runId}`
104. Verifikasi kolom `Group` tidak tampil
105. Verifikasi kolom `Source` tampil
106. Verifikasi kolom `Status` menjadi kolom pertama dan tetap di-pin
107. Verifikasi kotak Search kosong dan halaman aktif adalah halaman 1, karena Search dan paginasi tidak tersimpan di akun
108. Klik `Filter`
109. Verifikasi tidak ada nilai terpilih pada semua field di Filter Panel, karena Filter tidak tersimpan di akun
110. Verifikasi seluruh 10 baris di halaman 1 berstatus `Waiting for Handover`, sehingga urutan awal tabel berlaku dan Sort tidak tersimpan di akun
111. Buka halaman `Transactions > Borrow` di sesi browser lain dengan akun `Admin Borrow {runId}`
112. Verifikasi kolom `Group` tidak tampil di sesi browser lain
113. Verifikasi kolom `Source` tampil
114. Verifikasi kolom `Status` menjadi kolom pertama dan tetap di-pin
115. Masuk sebagai `Admin Lain {runId}`
116. Verifikasi kolom `Group` tampil
117. Verifikasi kolom `Source` tidak tampil

### Setidaknya satu kolom tetap tampil
118. Masuk sebagai `Admin Borrow {runId}`
119. Klik header kolom Actions `⋯`
120. Hapus centang `Status` pada panel Column Visibility
121. Hapus centang `Borrower` pada panel Column Visibility
122. Hapus centang `Total Asset` pada panel Column Visibility
123. Hapus centang `Requested By` pada panel Column Visibility
124. Hapus centang `Request Date` pada panel Column Visibility
125. Hapus centang `Last Updated` pada panel Column Visibility
126. Hapus centang `Source` pada panel Column Visibility
127. Verifikasi kotak centang `Transaction ID` disabled dengan tooltip `At least one column must remain visible.`
