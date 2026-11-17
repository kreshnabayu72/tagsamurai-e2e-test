---
id: TC-FA-MYASSET-UI-115-tabel-history-konfigurasi-dan-state
title: "Tabel History: kolom tampil awal, urutan kolom, field Filter, placeholder Search, dan state data"
layer: ui-client
priority: Critical
caseType: Positive
status: draft
sourceRules: ["§4.1#p2", "§4.1c#p1", "§4.1c#r1", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r15", "§4.1c#r16", "§4.1c#r17", "§5#r1", "§5#r3", "§5#r10", "§7.1#r4", "EB-TBL-1@tabel-history", "EB-FLT-6@tabel-history"]
smoke: []
dependsOn: []
trace:
  "§4.1#p2": [13, 14, 15, 16]
  "§4.1c#p1": [2, 3]
  "§4.1c#r1": [9, 12, 13, 32]
  "§4.1c#r2": [9, 12, 13, 20, 41]
  "§4.1c#r3": [9, 12, 13, 32]
  "§4.1c#r4": [9, 12, 13, 21, 44]
  "§4.1c#r5": [9, 12, 13, 22, 47]
  "§4.1c#r6": [9, 12, 13, 23, 50]
  "§4.1c#r7": [9, 12, 13, 24, 53]
  "§4.1c#r8": [9, 12, 13, 25, 56]
  "§4.1c#r9": [10, 12, 14, 26, 31, 59]
  "§4.1c#r10": [10, 12, 14, 27, 31, 62]
  "§4.1c#r11": [9, 12, 13, 28, 36, 38]
  "§4.1c#r12": [9, 12, 13, 32]
  "§4.1c#r13": [9, 12, 13, 29, 65, 67]
  "§4.1c#r14": [9, 12, 13, 30, 69, 71]
  "§4.1c#r15": [10, 12, 14, 32]
  "§4.1c#r16": [10, 12, 14, 32]
  "§4.1c#r17": [10, 12, 14, 32]
  "§5#r1": [2, 4]
  "§5#r3": 7
  "§5#r10": [9, 12]
  "§7.1#r4": [73, 74, 82, 83, 90, 91]
  "EB-TBL-1@tabel-history": [73, 75, 76, 77, 79, 82, 84, 86, 90, 93, 94, 95, 96]
  "EB-FLT-6@tabel-history": [31, 101, 102, 106, 107, 108, 109, 110]
coverage:
  web: automated
---

# Tabel History: kolom tampil awal, urutan kolom, field Filter, placeholder Search, dan state data

## Prerequisites
- Aktor: Budi Santoso, pengguna yang login sebagai Borrower dan Assignee atas baris yang tampil.
- Layar awal: halaman My Asset, tab History.
- Komponen: Tabel History (T-MYA-03)
- Data:
  - DU-115-1: Baris History Photo `foto-LPT-2026-0012.jpg`, Name `Laptop Dell Latitude 5420 - 12`, Asset ID `LPT-2026-0012`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Returned`, Holder `Me`, TAG `Non TAG`, Category `Laptop`, Type `Borrow`, Transaction ID `BRW-2026-0151`, Handed Over At `01/11/26, 09:00`, Closed At `08/11/26, 11:00`, Handover Photo kosong, Return Photo kosong, Purpose `Keperluan operasional kantor`.
  - DU-115-2: Baris History Photo `foto-PRJ-2026-0002.jpg`, Name `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Brand `Epson`, Model/Type `EB-X06`, Group `Head Office`, Status `Unassigned`, Holder `Me`, TAG `Non TAG`, Category `Proyektor`, Type `Assignment`, Transaction ID `ASG-2026-0009`, Handed Over At `03/07/26, 10:00`, Closed At `30/10/26, 15:20`, Handover Photo kosong, Return Photo kosong, Purpose `Keperluan operasional kantor`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K1: tabel History memuat DU-115-1 dan DU-115-2 dengan konfigurasi kolom bawaan.
  - K2: tabel History belum memiliki satu pun baris, dan tidak ada Search maupun Filter aktif.
  - K3: tabel History memuat DU-115-1; respons untuk Search `Kamera Drone DJI` dan untuk Filter Type `Assignment` tidak memuat baris.
  - K4: memuat tabel History gagal karena error server.
  - K5: tabel History memuat DU-115-1 dan DU-115-2; respons untuk Filter Type `Borrow` hanya memuat DU-115-1.

## Test Steps

### Isi dan urutan toolbar
1. Tampilkan Tabel History dengan kondisi K1
2. Verifikasi toolbar memuat ikon Search, ikon Filter, dan ikon Download
3. Verifikasi urutan ikon toolbar dari kiri ke kanan adalah Search, Filter, Download
4. Verifikasi tombol `Borrow an Asset` tidak tampil di toolbar

### Placeholder Search tab History
5. Tampilkan Tabel History dengan kondisi K1
6. Klik ikon Search
7. Verifikasi kotak Search menampilkan placeholder `Search asset name, asset ID...`

### Kolom tampil awal dan urutannya
8. Tampilkan Tabel History dengan kondisi K1
9. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Holder`, `Type`, `Transaction ID`, `Handed Over At`, `Closed At`
10. Verifikasi header kolom `TAG`, `Category`, `Handover Photo`, `Return Photo`, `Purpose` tidak tampil
11. Klik header kolom Actions `⋯`
12. Verifikasi panel Column Visibility memuat daftar kolom berurutan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Holder`, `TAG`, `Category`, `Type`, `Transaction ID`, `Handed Over At`, `Closed At`, `Handover Photo`, `Return Photo`, `Purpose`
13. Verifikasi kotak centang kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Holder`, `Type`, `Transaction ID`, `Handed Over At`, `Closed At` tercentang (Hideable)
14. Verifikasi kotak centang kolom `TAG`, `Category`, `Handover Photo`, `Return Photo`, `Purpose` tidak tercentang (Curated)
15. Verifikasi semua kotak centang aktif sehingga tidak ada kolom yang terkunci tampil
16. Verifikasi daftar tidak memuat baris untuk kolom Checkbox maupun kolom Actions
17. Tutup panel Column Visibility dengan menekan `Escape`

### Field Filter tiap kolom: label dan placeholder
18. Tampilkan Tabel History dengan kondisi K1
19. Klik ikon Filter
20. Verifikasi Filter Panel memuat field `Asset Name` dengan placeholder `All asset names`
21. Verifikasi Filter Panel memuat field `Brand` dengan placeholder `All brands`
22. Verifikasi Filter Panel memuat field `Model/Type` dengan placeholder `All models`
23. Verifikasi Filter Panel memuat field `Group` dengan placeholder `All groups`
24. Verifikasi Filter Panel memuat field `Status` dengan placeholder `All statuses`
25. Verifikasi Filter Panel memuat field `Holder` dengan placeholder `All holders`
26. Verifikasi Filter Panel memuat field `TAG` dengan placeholder `All TAGs`
27. Verifikasi Filter Panel memuat field `Category` dengan placeholder `All categories`
28. Verifikasi Filter Panel memuat field `Type` dengan placeholder `All types`
29. Verifikasi Filter Panel memuat field `Handed Over At` dengan placeholder `Select date`
30. Verifikasi Filter Panel memuat field `Closed At` dengan placeholder `Select date`
31. Verifikasi Filter Panel memuat field untuk kolom TAG dan Category walaupun kedua kolom itu tidak tampil di tabel
32. Verifikasi Filter Panel tidak memuat field untuk kolom `Photo`, `Asset ID`, `Transaction ID`, `Handover Photo`, `Return Photo`, dan `Purpose`

### Tipe field Filter: multi-select searchable dan date range picker
33. Tampilkan Tabel History dengan kondisi K1
34. Klik ikon Filter
35. Klik field `Type`
36. Verifikasi daftar opsi field `Type` memiliki kotak pencarian
37. Pilih `Borrow` dan `Assignment` pada field `Type`
38. Verifikasi field `Type` menampilkan `Borrow` dan `Assignment` sebagai pilihan terpilih sekaligus
39. Tutup daftar opsi field `Type` dengan menekan `Escape`
40. Klik field `Asset Name`
41. Verifikasi daftar opsi field `Asset Name` memiliki kotak pencarian
42. Tutup daftar opsi field `Asset Name` dengan menekan `Escape`
43. Klik field `Brand`
44. Verifikasi daftar opsi field `Brand` memiliki kotak pencarian
45. Tutup daftar opsi field `Brand` dengan menekan `Escape`
46. Klik field `Model/Type`
47. Verifikasi daftar opsi field `Model/Type` memiliki kotak pencarian
48. Tutup daftar opsi field `Model/Type` dengan menekan `Escape`
49. Klik field `Group`
50. Verifikasi daftar opsi field `Group` memiliki kotak pencarian
51. Tutup daftar opsi field `Group` dengan menekan `Escape`
52. Klik field `Status`
53. Verifikasi daftar opsi field `Status` memiliki kotak pencarian
54. Tutup daftar opsi field `Status` dengan menekan `Escape`
55. Klik field `Holder`
56. Verifikasi daftar opsi field `Holder` memiliki kotak pencarian
57. Tutup daftar opsi field `Holder` dengan menekan `Escape`
58. Klik field `TAG`
59. Verifikasi daftar opsi field `TAG` memiliki kotak pencarian
60. Tutup daftar opsi field `TAG` dengan menekan `Escape`
61. Klik field `Category`
62. Verifikasi daftar opsi field `Category` memiliki kotak pencarian
63. Tutup daftar opsi field `Category` dengan menekan `Escape`
64. Klik field `Handed Over At`
65. Verifikasi panel pemilih tanggal terbuka untuk field `Handed Over At`
66. Pilih hari pertama yang tampil sebagai awal dan hari ketiga yang tampil sebagai akhir
67. Verifikasi field `Handed Over At` menampilkan satu rentang tanggal dari awal sampai akhir yang dipilih
68. Klik field `Closed At`
69. Verifikasi panel pemilih tanggal terbuka untuk field `Closed At`
70. Pilih hari pertama yang tampil sebagai awal dan hari ketiga yang tampil sebagai akhir
71. Verifikasi field `Closed At` menampilkan satu rentang tanggal dari awal sampai akhir yang dipilih

### Empty state tab History belum ada data
72. Tampilkan Tabel History dengan kondisi K2
73. Verifikasi `No history yet` tampil
74. Verifikasi `Returned and closed borrows and assignments will appear here.` tampil
75. Verifikasi `No results found` tidak tampil
76. Verifikasi `Unable to load this data.` tidak tampil
77. Verifikasi empty state tidak memuat tombol aksi

### Empty state tab History akibat Search dan Filter
78. Tampilkan Tabel History dengan kondisi K3
79. Verifikasi baris `Laptop Dell Latitude 5420 - 12` tampil
80. Klik ikon Search
81. Ketik Search `Kamera Drone DJI`, tekan Enter
82. Verifikasi `No results found` tampil
83. Verifikasi `Try adjusting your search or filter.` tampil
84. Verifikasi `No history yet` tidak tampil
85. Klik `(←)` pada kotak Search
86. Verifikasi baris `Laptop Dell Latitude 5420 - 12` tampil kembali
87. Klik ikon Filter
88. Pilih `Assignment` pada field `Type`
89. Klik `[Apply]`
90. Verifikasi `No results found` tampil
91. Verifikasi `Try adjusting your search or filter.` tampil

### Gagal muat tab History
92. Tampilkan Tabel History dengan kondisi K4
93. Verifikasi `Unable to load this data.` tampil
94. Verifikasi tombol `[Try Again]` tampil
95. Verifikasi `No history yet` tidak tampil
96. Verifikasi `No results found` tidak tampil

### Menyembunyikan kolom tidak menghapus field Filter dan tidak membatalkan filter ter-Apply
97. Tampilkan Tabel History dengan kondisi K5
98. Klik ikon Filter
99. Pilih `Borrow` pada field `Type`
100. Klik `[Apply]`
101. Verifikasi baris `Laptop Dell Latitude 5420 - 12` tampil
102. Verifikasi ikon Filter menampilkan titik penanda filter ter-Apply
103. Klik header kolom Actions `⋯`
104. Hilangkan centang kolom `Type` pada panel Column Visibility
105. Tutup panel Column Visibility dengan menekan `Escape`
106. Verifikasi header kolom `Name` tampil
107. Verifikasi header kolom `Type` tidak tampil
108. Verifikasi Filter Panel masih memuat field `Type` dengan pilihan `Borrow`
109. Verifikasi ikon Filter masih menampilkan titik penanda filter ter-Apply
110. Verifikasi baris `Laptop Dell Latitude 5420 - 12` tetap tampil
