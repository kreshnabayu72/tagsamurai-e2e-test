---
id: TC-FA-BORROW-E2E-006-tab-borrowed-assets-by-borrower
title: "Tab Borrowed Assets By Borrower menampilkan total aset per Borrower dan halaman Borrowed Asset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1j#r34", "§4.1j#r35", "§4.1j#r36", "§4.1j#p8", "§4.1j#r37", "§4.1j#r38", "§4.2.14#p1", "§4.2.14#p2"]
smoke: []
dependsOn: []
trace:
  "§4.1j#r34": [8, 9, 15, 42, 44, 54, 55, 57, 58]
  "§4.1j#r35": [13, 14, 50, 52, 63, 65, 101]
  "§4.1j#r36": [5, 9, 10, 11, 12, 28, 46, 48, 60, 61, 106, 107]
  "§4.1j#p8": [25]
  "§4.1j#r37": [21, 25, 27]
  "§4.1j#r38": [32]
  "§4.2.14#p1": [17, 18, 19, 68, 72]
  "§4.2.14#p2": [17, 21, 27, 37, 39, 68, 69, 71, 76, 78, 82, 86, 90, 94]
anchor: []
coverage:
  web: automated
---

# Tab Borrowed Assets By Borrower menampilkan total aset per Borrower dan halaman Borrowed Asset

## Prerequisites
- Aktor: Asset Admin `Admin Aset {runId}` (DU-006-1), Group penugasan `Head Office`.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-006-1: User `Admin Aset {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - Pengaju seluruh BRW: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`).
  - DU-006-2: Borrower `Rizky Ramadhan` (tampil `Rizky R`, Employee ID `EMP-6001`) meminjam tiga aset di Group `Head Office` yang berstatus Borrowed: `Laptop HP ProBook {runId}`, `Monitor Dell P2422H {runId}`, dan `Keyboard Logitech K380 {runId}`, serta dua aset yang berstatus Overdue (Due Date `T0 − 2 hari`): `Proyektor Optoma X343 {runId}` di Group `Gudang Pusat` dan `Speaker Polytron PMA {runId}` di Group `Lantai Dua`. `Gudang Pusat` dan `Lantai Dua` adalah sub-group `Head Office`, sehingga masuk cakupan aktor. Total Asset `5`, dari tiga baris Borrowed dan dua baris Overdue; Group yang tampil pada baris Borrower ini ada 3.
  - DU-006-3: Borrower `Tono Hidayat` (tampil `Tono H`, Employee ID `EMP-6002`) meminjam dua aset yang berstatus Borrowed: `Printer Brother HL-L2320 {runId}` di Group `Head Office` dan `Scanner Epson V39 {runId}` di Group `Gudang Pusat`, serta dua aset di Group `Head Office` yang tidak dihitung: `Webcam Logitech C920 {runId}` berstatus Waiting for Handover dan `Headset Jabra Evolve {runId}` berstatus Returned. Total Asset `2`.
  - DU-006-4: Borrower `Sinta Maharani` (tampil `Sinta S`, Employee ID `EMP-6004`) meminjam `Tablet Lenovo Tab M10 {runId}` di Group `Head Office` dan `Kamera Canon M50 {runId}` di Group `Branch Surabaya`, keduanya berstatus Borrowed. Aktor hanya mencakup Group `Head Office`, sehingga Total Asset yang tampil `1`.
  - DU-006-5: Borrower `Umar Faruq` (tampil `Umar F`, Employee ID `EMP-6003`, BRW-nya dibuat lebih dulu daripada BRW Borrower `Sinta S`) meminjam satu aset Non TAG di Group `Head Office` yang berstatus Borrowed: `Kabel Roll 10 Meter {runId}`. Total Asset `1`.
  - DU-006-6: Borrower `Vina Kusuma` (tampil `Vina K`, Employee ID `EMP-6005`) meminjam dua aset di Group `Branch Surabaya` yang berstatus Borrowed: `Speaker Anker Soundcore {runId}` dan `Mikrofon Rode Wireless Go {runId}`.
- Kondisi:
  - Photo at end bernilai OFF pada aset DU-006-5.

## Test Steps

### Tab Borrowed Assets By Borrower menampilkan Borrower dalam cakupan aktor
1. Klik tab `Borrowed Assets`
2. Klik sub-tab `By Borrower`
3. Klik `Filter`
4. Klik field `Borrower`
5. Verifikasi opsi `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F` tampil dan opsi `Vina K` tidak tampil karena seluruh asetnya berada di luar cakupan aktor
6. Pilih opsi `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F`
7. Klik `[Apply]`
8. Verifikasi tabel memuat 4 baris dengan Borrower `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F`

### Urutan awal, Total Asset, Group, dan Employee ID per Borrower
9. Verifikasi urutan baris dari atas ke bawah: Borrower `Rizky R`, `Tono H`, `Sinta S`, lalu `Umar F`, dengan `Sinta S` dan `Umar F` yang Total Asset-nya sama diurutkan A–Z walau BRW dan Employee ID `Umar F` lebih awal
10. Verifikasi baris Borrower `Rizky R` menampilkan Total Asset `5`, dihitung dari tiga baris Borrowed dan dua baris Overdue, dan baris Borrower `Tono H` menampilkan Total Asset `2` tanpa menghitung baris Waiting for Handover dan Returned
11. Verifikasi baris Borrower `Sinta S` menampilkan Total Asset `1` tanpa menghitung aset di luar cakupan aktor
12. Verifikasi baris Borrower `Umar F` menampilkan Total Asset `1`
13. Verifikasi baris Borrower `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F` menampilkan Group `Head Office`
14. Verifikasi baris Borrower `Sinta S` tidak menampilkan Group `Branch Surabaya`
15. Verifikasi baris Borrower `Rizky R` menampilkan Employee ID `EMP-6001`

### Halaman Borrowed Asset dibuka dari nama Borrower
16. Klik nama Borrower `Rizky R`
17. Verifikasi halaman `Borrowed Asset` terbuka dengan Borrower `Rizky R` dan memuat aset `Laptop HP ProBook {runId}`, `Monitor Dell P2422H {runId}`, `Keyboard Logitech K380 {runId}`, `Proyektor Optoma X343 {runId}`, dan `Speaker Polytron PMA {runId}`
18. Verifikasi tabel aset tidak memuat kolom `Borrower` dan halaman tidak memuat sub-tab `By Asset` maupun `By Borrower`
19. Verifikasi breadcrumb memuat `Transactions > Borrow > Borrowed Assets > Detail`
20. Klik `⋯` pada baris aset `Laptop HP ProBook {runId}`
21. Verifikasi menu baris memuat `Return`, `Request Extension`, `Report Damaged`, `Report Missing`, dan `Borrow Log`
22. Tutup menu baris
23. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Row action Detail membuka halaman Borrowed Asset
24. Klik `⋯` pada baris Borrower `Tono H`
25. Verifikasi menu baris memuat `Detail`
26. Klik `Detail`
27. Verifikasi halaman `Borrowed Asset` terbuka dengan Borrower `Tono H` dan memuat aset `Printer Brother HL-L2320 {runId}` dan `Scanner Epson V39 {runId}`
28. Verifikasi halaman `Borrowed Asset` Borrower `Tono H` tidak memuat aset `Webcam Logitech C920 {runId}` dan `Headset Jabra Evolve {runId}`
29. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Download tabel By Borrower
30. Klik `Download`
31. Pilih `Download as CSV`
32. Verifikasi berkas terunduh dengan nama `Borrowed-Borrowers` dan memuat 4 baris data yang tampil di tabel

### Halaman Borrowed Asset tanpa aset yang dipinjam
33. Klik nama Borrower `Umar F`
34. Klik `⋯` pada baris aset `Kabel Roll 10 Meter {runId}`
35. Klik `Return`
36. Klik `[Submit]`
37. Verifikasi toast `Success, 1 asset has been returned.` tampil
38. Kembali ke halaman `Borrowed Asset` Borrower `Umar F` lewat segmen Origin Tab pada breadcrumb
39. Verifikasi halaman menampilkan `No borrowed assets` dan `Assets held by this borrower will appear here.`

### Sort dan Search pada tabel By Borrower
40. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb
41. Klik header kolom `Borrower`
42. Verifikasi urutan Borrower dari atas ke bawah: `Rizky R`, `Sinta S`, lalu `Tono H`
43. Klik header kolom `Borrower`
44. Verifikasi urutan Borrower dari atas ke bawah: `Tono H`, `Sinta S`, lalu `Rizky R`
45. Klik header kolom `Total Asset`
46. Verifikasi urutan Total Asset menaik: `Sinta S` (`1`), `Tono H` (`2`), lalu `Rizky R` (`5`)
47. Klik header kolom `Total Asset`
48. Verifikasi urutan Total Asset menurun: `Rizky R` (`5`), `Tono H` (`2`), lalu `Sinta S` (`1`)
49. Klik header kolom `Group`
50. Verifikasi urutan Borrower dari atas ke bawah menurut jumlah Group menaik: `Sinta S` (1 Group), `Tono H` (2 Group), lalu `Rizky R` (3 Group)[^drift-1]
51. Klik header kolom `Group`
52. Verifikasi urutan Borrower dari atas ke bawah menurut jumlah Group menurun: `Rizky R` (3 Group), `Tono H` (2 Group), lalu `Sinta S` (1 Group)[^drift-1]
53. Ketik Search `Tono Hidayat`, tekan Enter
54. Verifikasi baris Borrower `Tono H` tampil
55. Verifikasi baris Borrower `Rizky R` tidak tampil
56. Ganti isi kotak search dengan `EMP-6004`, tekan Enter
57. Verifikasi baris Borrower `Sinta S` tampil
58. Verifikasi baris Borrower `Tono H` tidak tampil
59. Ganti isi kotak search dengan `5`, tekan Enter
60. Verifikasi baris Borrower `Rizky R` tampil dengan Total Asset `5`
61. Verifikasi baris Borrower `Tono H` tidak tampil
62. Ganti isi kotak search dengan `Head Office`, tekan Enter
63. Verifikasi baris Borrower `Sinta S` tampil
64. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
65. Verifikasi baris Borrower `Sinta S` tidak tampil karena Group `Branch Surabaya` berada di luar cakupan aktor
66. Klik `(←)` pada kotak Search

### Halaman Borrowed Asset memakai toolbar, kolom, filter, bulk, dan aksi yang sama dengan By Asset
67. Klik nama Borrower `Rizky R`
68. Verifikasi toolbar halaman Borrowed Asset memuat `Search by Scan`, `Search`, `Filter`, dan `Download`
69. Verifikasi urutan kolom tabel aset dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Due Date`, `Remaining`, lalu `Transaction ID`
70. Klik `Filter`
71. Verifikasi Filter Panel memuat field `Asset Name`, `Brand`, `Model/Type`, `Group`, `Status`, `TAG`, `Category`, `Due Date`, `Handed Over At`, `Extensions`, `Source`, dan `Handed Over By`
72. Verifikasi Filter Panel tidak memuat field `Borrower`
73. Klik `Filter`
74. Centang baris aset `Laptop HP ProBook {runId}`
75. Centang baris aset `Monitor Dell P2422H {runId}`
76. Verifikasi aksi bulk `Return` aktif
77. Klik aksi bulk `Return`
78. Verifikasi halaman `Return Asset` terbuka dengan Borrower `Rizky R` dan aset `Laptop HP ProBook {runId}` serta `Monitor Dell P2422H {runId}`
79. Kembali ke halaman `Borrowed Asset` Borrower `Rizky R` lewat segmen Origin Tab pada breadcrumb
80. Klik `⋯` pada baris aset `Laptop HP ProBook {runId}`
81. Klik `Request Extension`
82. Verifikasi halaman `Extension Request` terbuka dengan baris aset `Laptop HP ProBook {runId}` saja
83. Kembali ke halaman `Borrowed Asset` Borrower `Rizky R` lewat segmen Origin Tab pada breadcrumb
84. Klik `⋯` pada baris aset `Laptop HP ProBook {runId}`
85. Klik `Report Damaged`
86. Verifikasi dialog `Report Damaged` terbuka untuk aset `Laptop HP ProBook {runId}`
87. Tutup dialog `Report Damaged` tanpa menyimpan
88. Klik `⋯` pada baris aset `Laptop HP ProBook {runId}`
89. Klik `Report Missing`
90. Verifikasi dialog `Report Missing` terbuka untuk aset `Laptop HP ProBook {runId}`
91. Tutup dialog `Report Missing` tanpa menyimpan
92. Klik `⋯` pada baris aset `Laptop HP ProBook {runId}`
93. Klik `Borrow Log`
94. Verifikasi dialog Borrow Log terbuka untuk aset `Laptop HP ProBook {runId}`
95. Tutup dialog Borrow Log

### Filter Group dan Total Asset pada tabel By Borrower
96. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb
97. Klik `Filter`
98. Klik field `Group`
99. Pilih node `Head Office`
100. Klik `[Apply]`
101. Verifikasi baris Borrower `Rizky R`, `Tono H`, dan `Sinta S` tampil
102. Klik field `Total Asset`
103. Isi `Min` dengan `2`
104. Isi `Max` dengan `3`
105. Klik `[Apply]`
106. Verifikasi baris Borrower `Tono H` tampil dengan Total Asset `2`
107. Verifikasi baris Borrower `Rizky R` dan `Sinta S` tidak tampil

[^drift-1]: Drift PRD vs foundation. PRD §4.1j tabel T-BRW-14 kolom Group: Sort `Alphabetical (A–Z)`. Foundation `prd-conventions.md` §9.7, aturan kolom «+N more»: ascending = paling sedikit Group duluan, descending = paling banyak duluan. Diasersi: foundation, karena kolom Group yang merender beberapa badge dalam satu sel adalah pola bersama (SB-4).
