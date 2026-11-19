---
id: TC-FA-ASSIGN-UI-113-halaman-unassign-daftar-dan-validasi
title: "Halaman Unassign: daftar aset, Verification, Photo, dan Submit"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-10, "§4.1#r8", "§4.2.6#p1", "§4.2.6#p2", "§4.2.6#p3", "§4.2.6#b1", "§4.2.6#b2", "§4.2.6#b3", "§4.2.6#b4", "§4.2.6#b5", "§4.2.6#b6", "§4.2.6#b7", "§4.2.6#b8", "§4.2.6#b9", "§4.2.6#b10", "§4.2.6#b11", "§4.2.6#b12", "§4.2.6#b13", "§4.2.6#b14", "§4.2.6#b15", "§4.2.6#b16", "§4.2.6#b17", "§4.2.6#b18", "§4.2.6#b19", "§4.2.6#b20", "§4.2.6#b21", FI-ASG-43, FI-ASG-44, FI-ASG-45, FI-ASG-46, FI-ASG-57, FI-ASG-58, FI-ASG-59, FI-ASG-60, FI-ASG-61, FI-ASG-70, FI-ASG-71, FI-ASG-72, FI-ASG-73, FLD-ASG-10, FLD-ASG-11, FLD-ASG-12, FLD-ASG-13, V-ASG-27, V-ASG-28, V-ASG-29, FLD-ASG-18, FLD-ASG-19, S-ASG-25, "EB-FRM-4@description-report-damaged", ASSIGN-LOGIC-15a, FI-ASG-55, FI-ASG-64, FI-ASG-65]
smoke: []
dependsOn: []
trace:
  T-ASG-10: [30, 31, 32, 238, 239, 240, 241, 243, 244, 246, 247, 248, 249, 251, 254, 256, 257]
  "§4.1#r8": 32
  "§4.2.6#p1": 9
  "§4.2.6#p2": [2, 3, 4, 5, 6, 7, 11, 12, 14, 15, 16, 19, 20, 190, 191, 193, 194, 216, 219, 222, 225, 229]
  "§4.2.6#p3": [23, 54]
  "§4.2.6#b1": 29
  "§4.2.6#b2": [54, 56, 60, 64]
  "§4.2.6#b3": [68, 69]
  "§4.2.6#b4": [73, 74]
  "§4.2.6#b5": [78, 79]
  "§4.2.6#b6": [83, 84]
  "§4.2.6#b7": [86, 87]
  "§4.2.6#b8": [93, 94, 96, 209, 210, 211, 213]
  "§4.2.6#b9": [99, 103, 106, 115, 120]
  "§4.2.6#b10": [124, 125]
  "§4.2.6#b11": [116, 121]
  "§4.2.6#b12": 78
  "§4.2.6#b13": [83, 131, 133, 134]
  "§4.2.6#b14": [136, 137, 138, 186, 187, 219, 229]
  "§4.2.6#b15": [16, 141, 145, 198, 205, 206, 218, 221, 228, 266, 270]
  "§4.2.6#b16": [127, 128]
  "§4.2.6#b17": [89, 90, 91]
  "§4.2.6#b18": [147, 148, 157, 180, 182, 223, 225, 259]
  "§4.2.6#b19": 115
  "§4.2.6#b20": [129, 263]
  "§4.2.6#b21": [115, 117]
  FI-ASG-43: [29, 33, 42, 233, 235]
  FI-ASG-44: [35, 37, 38]
  FI-ASG-45: [43, 235]
  FI-ASG-46: [25, 27]
  FI-ASG-57: [93, 94, 96, 209, 210, 211, 213]
  FI-ASG-58: [115, 120, 157]
  FI-ASG-59: [99, 103, 106]
  FI-ASG-60: 109
  FI-ASG-61: [115, 117]
  FI-ASG-70: [141, 198, 199, 218, 221, 228]
  FI-ASG-71: [145, 205, 206]
  FI-ASG-72: [145, 205]
  FI-ASG-73: [266, 270]
  FLD-ASG-10: [3, 4, 5, 109, 190, 191]
  FLD-ASG-11: 112
  FLD-ASG-12: [86, 87, 103]
  FLD-ASG-13: [93, 106, 138, 209, 213]
  V-ASG-27: 109
  V-ASG-28: 112
  V-ASG-29: [150, 151]
  FLD-ASG-18: [147, 150, 259]
  FLD-ASG-19: [147, 151, 155, 161]
  S-ASG-25: [45, 46, 49, 50]
  "EB-FRM-4@description-report-damaged": [155, 156, 161, 162, 166, 167, 171, 172, 176, 177]
  ASSIGN-LOGIC-15a: [82, 83, 133]
  FI-ASG-55: [82, 83, 84]
  FI-ASG-64: [131, 133]
  FI-ASG-65: 131
anchor: [262]
coverage:
  web: automated
---
# Halaman Unassign: daftar aset, Verification, Photo, dan Submit

## Prerequisites
- Aktor: Asset Admin pada Group `Head Office`.
- Layar awal: halaman Unassign, dibuka dari aksi `Unassign` pada Assignment Detail atau Assigned Assets By Asset.
- Komponen: Halaman Unassign
- Data:
  - DU-113-1: Assignee Name `Budi Santoso`, Tipe `Employee`, Opsi `Budi Santoso (Employee)`, Jumlah aset `3 assets`.
  - DU-113-2: Assignee Name `Finance`, Tipe `Division`, Opsi `Finance (Division)`, Jumlah aset `1 asset`.
  - DU-113-3: Baris aset Unassign Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Brand `—`, Model/Type `—`, TAG `NFC`, Status `Assigned`, Transaction ID `ASG-2026-0041`, Group `Head Office`, Assigned Since `12 Oct 2026`, Verification `Unverified`.
  - DU-113-4: Baris aset Unassign Name `Laptop Dell Latitude 5420 - 40`, Asset ID `LPT-2026-0040`, Brand `—`, Model/Type `—`, TAG `NFC`, Status `Assigned`, Transaction ID `ASG-2026-0031`, Group `Head Office`, Assigned Since `03 Oct 2026`, Verification `Unverified`.
  - DU-113-5: Baris aset Unassign Name `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Brand `—`, Model/Type `—`, TAG `Non TAG`, Status `Assigned`, Transaction ID `ASG-2026-0041`, Group `Head Office`, Assigned Since `12 Oct 2026`, Verification `Non TAG`.
  - DU-113-6: Baris aset Unassign Name `Printer HP M404 - 3`, Asset ID `PRN-2026-0003`, Brand `—`, Model/Type `—`, TAG `RFID`, Status `Reported Damaged`, Transaction ID `ASG-2026-0041`, Group `Head Office`, Assigned Since `12 Oct 2026`, Verification `Unverified`.
  - DU-113-7: Baris aset Unassign Name `Camera Sony A7 - 9`, Asset ID `CAM-2026-0009`, Brand `—`, Model/Type `—`, TAG `NFC`, Status `Assigned`, Transaction ID `ASG-2026-0044`, Group `Head Office`, Assigned Since `12 Oct 2026`, Verification `Unverified`.
  - DU-113-8: Aset Name `Tablet Samsung Tab S8 - 2`, Asset ID `TAB-2026-0002`.
  - DU-113-9: Aset Name `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Assignee `Sari Dewi`.
  - DU-113-10: Aset Name `Forklift Toyota 8FD - 1`, Asset ID `FLT-2026-0001`, Group `Branch Surabaya`.
  - DU-113-11: Description Report Damaged Description `KerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakan`.
  - DU-113-12: Description Report Damaged Description `KerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanx`.
  - DU-113-13: Description Report Damaged Description ` KerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakan `.
  - DU-113-14: Description Report Damaged Description `Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Lay`.
  - DU-113-15: Description Report Damaged Description `KérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKerusakán`.
  - DU-113-16: Search Kata kunci `Tanpa Hasil`.
  - DU-113-17: Baris aset Unassign Name `Monitor LG 27UL - 2`, Asset ID `MON-2026-0002`, Brand `—`, Model/Type `—`, TAG `NFC`, Status `Assigned`, Transaction ID `ASG-2026-0041`, Group `Head Office`, Assigned Since `12 Oct 2026`, Verification `Verified` setelah scan.
  - DU-113-18: Kata kunci field Assignee `Fin`.
  - DU-113-19: Baris aset Unassign Name `Proyektor Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Brand `—`, Model/Type `—`, TAG `NFC`, Status `Reported Damaged`, Transaction ID `ASG-2026-0041`, Group `Head Office`, Assigned Since `12 Oct 2026`, Verification `Unverified`; laporan Damaged tersimpan milik Aktor sendiri dan masih `Waiting for Confirmation`.
  - DU-113-20: Baris dialog Name `Genset Perkins 20kVA - 3`, Asset ID `GEN-2026-0003`, Transaction ID `ASG-2026-0041`, Group `Floor 1` dengan hierarki lengkap `Head Office > Floor 1`, Assigned Since `12 Oct 2026`, tanpa foto utama.
- Kondisi:
  - K1: halaman dibuka tanpa Assignee terpilih dan daftar kosong; opsi Assignee berisi DU-113-1 dan DU-113-2; opsi yang diharapkan `Budi Santoso (Employee)` dan `Finance (Division)`, jumlah `3 assets` dan `1 asset`; Photo at end OFF.
  - K2: Assignee DU-113-1 terpilih; daftar berisi DU-113-3 dan DU-113-4, keduanya `Unverified`; Photo at end OFF.
  - K3: dialog Select Asset Unassign dibuka untuk Assignee DU-113-1; daftar berisi DU-113-3 dan DU-113-4; belum ada baris tercentang.
  - K4: dialog Select Asset Unassign dibuka untuk Assignee DU-113-1; tidak ada aset lain yang dipegang Assignee di Group Aktor; daftar kosong.
  - K5: seperti K3; Search DU-113-16 tidak menemukan baris mana pun.
  - K6: seperti K2; scan TAG aset DU-113-3 berhasil.
  - K7: seperti K2; scan TAG aset DU-113-17, ber-TAG, milik Assignee yang sama dan belum ada di daftar, berhasil.
  - K8: halaman dibuka tanpa Assignee terpilih; scan TAG aset DU-113-3 berhasil.
  - K9: seperti K2; scan TAG aset DU-113-8 ditolak; pesan yang diharapkan `Error, this asset isn't assigned.`.
  - K10: seperti K2; scan TAG aset DU-113-9 ditolak; pesan yang diharapkan `Error, this asset isn't assigned to Budi Santoso.`, dari Assignee `Budi Santoso`.
  - K11: seperti K2; scan TAG aset DU-113-10 ditolak; pesan yang diharapkan `Error, unassign this asset in Branch Surabaya.`, dari Group DU-113-10.
  - K12: halaman dibuka tanpa Assignee terpilih; scan TAG aset DU-113-7 (`Camera Sony A7 - 9`), penugasan Aktor sendiri, diterima; Assignee terisi dari aset itu.
  - K13: Assignee DU-113-1 terpilih; daftar berisi DU-113-3 (`Unverified`), DU-113-5 (`Non TAG`), dan DU-113-6 (status `Reported Damaged`).
  - K14: seperti K2; Photo at end ON; belum ada foto.
  - K15: seperti K2; Photo at end ON; kedua baris Verified tanpa foto.
  - K16: seperti K2; keduanya Unverified; Submit ditekan.
  - K17: halaman dibuka tanpa Assignee terpilih dan daftar kosong; Submit ditekan.
  - K18: Assignee DU-113-1 terpilih dan daftar kosong; Submit ditekan.
  - K19: seperti K2; DU-113-3 Verified; Submit berhasil; aset DU-113-4 tidak dimasukkan ke daftar, sehingga daftar hanya DU-113-3; semua aset dalam daftar berasal dari ASG asal yang sama; toast yang diharapkan `Success, 1 asset has been unassigned.`.
  - K20: seperti K19; aset dalam daftar berasal dari beberapa ASG; toast yang diharapkan `Success, 2 assets have been unassigned.`.
  - K21: Assignee penugasan Aktor sendiri terpilih; daftar memuat DU-113-7 `Verified` lewat scan TAG tanpa penanda ⚠; Submit berhasil; toast yang diharapkan `Success, 1 asset has been unassigned.`.
  - K22: seperti K2; DU-113-3 tetap Unverified dan belum difoto; aksi `I Can't Scan the TAG` pada DU-113-3 selesai dengan Report TAG varian identifikasi manual; Photo at end OFF.
  - K23: seperti K2; Photo at end ON; DU-113-3 Verified, difoto, dan dilaporkan Damaged di halaman ini.
  - K24: seperti K2; DU-113-3 sudah Report Damaged di halaman ini dengan Description DU-113-11.
  - K25: seperti K13; dialog Select Asset Unassign yang dibuka lewat `[+ Asset]` sesudah baris DU-113-6 dikeluarkan memuat DU-113-6.
  - K26: dialog Report Damaged dibuka dari row action `Report Damaged` pada DU-113-3; belum ada isian.
  - K27: seperti K26; foto sudah diambil.
  - K28: seperti K27; Description diisi DU-113-11.
  - K29: seperti K27; Description diisi DU-113-12.
  - K30: seperti K27; Description diisi DU-113-13.
  - K31: seperti K27; Description diisi DU-113-14.
  - K32: seperti K27; Description diisi DU-113-15.
  - K34: seperti K14; kamera tidak tersedia atau izin kamera ditolak.
  - K35: seperti K14; DU-113-3 sudah difoto dengan satu foto.
  - K36: Assignee DU-113-1 terpilih; daftar berisi DU-113-3 (`Unverified`), DU-113-5 (`Non TAG`), DU-113-6 (laporan milik Assignee), dan DU-113-19 (laporan milik Aktor).
  - K37: dialog Select Asset Unassign dibuka untuk Assignee DU-113-1; daftar berisi DU-113-20.
  - K33: halaman Unassign memuat aset sebanyak Bulk Transaction Row Limit ditambah 1; Verification sudah diisi dan Unassign Photo sudah terisi.

## Test Steps

### Titik masuk dan SectionCard 1: field Assignee dan opsinya
1. Tampilkan Halaman Unassign dengan kondisi K1
2. Verifikasi halaman Unassign tampil tanpa judul halaman terpisah dan tanpa Transaction ID
3. Verifikasi field Assignee memuat placeholder `Select assignee`
4. Verifikasi opsi Assignee `Budi Santoso (Employee)` tampil dengan jumlah `3 assets`
5. Verifikasi opsi Assignee `Finance (Division)` tampil dengan jumlah `1 asset`
6. Verifikasi toolbar memuat `[+ Asset]` dan `[Verify Asset]`
7. Verifikasi footer memuat `[Cancel]` dan `[Submit]`

### Dari aksi Unassign, Assignee dan aset terisi otomatis
8. Tampilkan Halaman Unassign dengan kondisi K2
9. Verifikasi Assignee `Budi Santoso` sudah terisi dan daftar memuat `Laptop Dell Latitude 5420 - 4` dan `Laptop Dell Latitude 5420 - 40`

### Daftar aset form-only: kolom dan row action
10. Tampilkan Halaman Unassign dengan kondisi K2
11. Verifikasi daftar memuat kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `TAG`, `Status`, `Transaction ID`, `Group`, `Assigned Since`, `Verification`, dan `Unassign Photo`
12. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan Transaction ID `ASG-2026-0041` dan Assigned Since `12 Oct 2026`
13. Buka row action pada baris `Laptop Dell Latitude 5420 - 4`
14. Verifikasi row action memuat `I Can't Scan the TAG`, `Report Damaged`, dan `Remove from List`
15. Verifikasi daftar tidak memakai paginasi
16. Verifikasi bulk action `Remove from List` belum tampil sebelum ada baris tercentang

### Mengganti Assignee mengosongkan daftar
17. Tampilkan Halaman Unassign dengan kondisi K2
18. Pilih Assignee `Finance (Division)`
19. Verifikasi Assignee `Finance` terpilih
20. Verifikasi daftar aset kosong

### Aksi Aturan Interaksi Field: Unassign berlaku satu pemicu per baris
21. Tampilkan Halaman Unassign dengan kondisi K2
22. Centang baris `Laptop Dell Latitude 5420 - 4`
23. Verifikasi bulk action `Remove from List` tampil setelah satu baris tercentang

### + Asset disabled sampai Assignee dipilih
24. Tampilkan Halaman Unassign dengan kondisi K1
25. Verifikasi `[+ Asset]` disabled
26. Pilih Assignee `Budi Santoso (Employee)`
27. Verifikasi `[+ Asset]` aktif

### Dialog Select Asset Unassign: judul, kolom, dan pilihan
28. Tampilkan Dialog Select Asset Unassign dengan kondisi K3
29. Verifikasi judul dialog Select Asset Unassign `Select Asset`
30. Verifikasi kotak Search memuat placeholder `Search asset name, asset ID, or transaction ID...`
31. Verifikasi dialog memuat kolom `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Group`, dan `Assigned Since`
32. Verifikasi baris `Laptop Dell Latitude 5420 - 4` dan `Laptop Dell Latitude 5420 - 40` tampil sebagai dua baris terpisah dengan Asset ID `LPT-2026-0004` dan `LPT-2026-0040`
33. Verifikasi dialog memuat tombol `[Cancel]` dan `[Select]`

### Select tanpa pilihan menampilkan caption error dan Select tetap aktif
34. Tampilkan Dialog Select Asset Unassign dengan kondisi K3
35. Verifikasi `[Select]` pada dialog Select Asset Unassign enabled
36. Klik `[Select]`
37. Verifikasi caption error `You must pick an asset` tampil di footer dialog
38. Verifikasi dialog Select Asset Unassign tetap terbuka karena pilihan tidak dikirim

### Aset yang dipilih masuk ke daftar sebagai Unverified
39. Tampilkan Dialog Select Asset Unassign dengan kondisi K3
40. Centang baris `Laptop Dell Latitude 5420 - 40`
41. Klik `[Select]`
42. Verifikasi dialog Select Asset Unassign tertutup
43. Verifikasi baris `Laptop Dell Latitude 5420 - 40` masuk ke daftar dengan Verification `Unverified`

### Empty state dialog Select Asset Unassign
44. Tampilkan Dialog Select Asset Unassign dengan kondisi K4
45. Verifikasi empty state memuat judul `No assets to add`
46. Verifikasi empty state memuat teks `This assignee has no other assigned assets in your groups.`

### Empty state akibat Search tanpa hasil
47. Tampilkan Dialog Select Asset Unassign dengan kondisi K5
48. Ketik Search `Tanpa Hasil`, tekan Enter
49. Verifikasi empty state dialog Select Asset Unassign memuat judul `No results found`
50. Verifikasi empty state dialog Select Asset Unassign memuat teks `Try adjusting your search or filter.`

### Verify Asset menerapkan hasil scan tanpa dialog
51. Tampilkan Halaman Unassign dengan kondisi K6
52. Klik `[Verify Asset]`
53. Pindai TAG aset `Laptop Dell Latitude 5420 - 4`
54. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan Verification `Verified` tanpa dialog
55. Pindai TAG aset `Laptop Dell Latitude 5420 - 4` sekali lagi
56. Verifikasi baris `Laptop Dell Latitude 5420 - 4` tetap `Verified` dan daftar tidak berubah

### Scan aset lain milik Assignee menambahkannya sebagai Verified
57. Tampilkan Halaman Unassign dengan kondisi K7
58. Klik `[Verify Asset]`
59. Pindai TAG aset `Monitor LG 27UL - 2`
60. Verifikasi baris `Monitor LG 27UL - 2` ditambahkan ke daftar dengan Verification `Verified`

### Assignee terisi dari aset pertama yang discan
61. Tampilkan Halaman Unassign dengan kondisi K8
62. Klik `[Verify Asset]`
63. Pindai TAG aset `Laptop Dell Latitude 5420 - 4`
64. Verifikasi Assignee `Budi Santoso` terisi dari aset pertama yang discan

### Scan ditolak: aset tidak sedang ditugaskan
65. Tampilkan Halaman Unassign dengan kondisi K9
66. Klik `[Verify Asset]`
67. Pindai TAG aset `Tablet Samsung Tab S8 - 2`
68. Verifikasi toast `Error, this asset isn't assigned.` tampil
69. Verifikasi baris `Laptop Dell Latitude 5420 - 4` tetap `Unverified` dan daftar tidak berubah

### Scan ditolak: aset ditugaskan ke Assignee lain
70. Tampilkan Halaman Unassign dengan kondisi K10
71. Klik `[Verify Asset]`
72. Pindai TAG aset `Toyota Avanza - 6`
73. Verifikasi toast `Error, this asset isn't assigned to Budi Santoso.` tampil
74. Verifikasi daftar tidak berubah

### Scan ditolak: Group asal di luar cakupan Aktor
75. Tampilkan Halaman Unassign dengan kondisi K11
76. Klik `[Verify Asset]`
77. Pindai TAG aset `Forklift Toyota 8FD - 1`
78. Verifikasi toast `Error, unassign this asset in Branch Surabaya.` tampil
79. Verifikasi daftar tidak berubah

### Scan diterima: penugasan Aktor sendiri
80. Tampilkan Halaman Unassign dengan kondisi K12
81. Klik `[Verify Asset]`
82. Pindai TAG aset `Camera Sony A7 - 9`
83. Verifikasi baris `Camera Sony A7 - 9` tampil di daftar dengan Verification `Verified` tanpa toast error
84. Verifikasi baris `Camera Sony A7 - 9` tidak ditandai ⚠

### Verification mengikuti status TAG aset
85. Tampilkan Halaman Unassign dengan kondisi K13
86. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan Verification `Unverified`
87. Verifikasi baris `Excavator PC200 - 4` menampilkan Verification `Non TAG` tanpa perlu scan

### Kolom Status: Assigned dan Reported Damaged tetap dapat di-Unassign
88. Tampilkan Halaman Unassign dengan kondisi K13
89. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan Status `Assigned`
90. Verifikasi baris `Printer HP M404 - 3` menampilkan Status `Reported Damaged`
91. Verifikasi baris `Printer HP M404 - 3` tetap berada di daftar dan dapat di-Unassign

### Unassign Photo wajib bila Photo at end ON
92. Tampilkan Halaman Unassign dengan kondisi K14
93. Verifikasi baris `Laptop Dell Latitude 5420 - 4` memuat tombol ambil foto pada kolom `Unassign Photo`
94. Verifikasi sumber foto pada kolom `Unassign Photo` hanya kamera tanpa pilihan file atau galeri

### Unassign Photo tanpa foto bila Photo at end OFF
95. Tampilkan Halaman Unassign dengan kondisi K2
96. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan `—` pada kolom `Unassign Photo`

### Submit dengan aset belum terverifikasi
97. Tampilkan Halaman Unassign dengan kondisi K16
98. Klik `[Submit]`
99. Verifikasi ringkasan error `2 assets are not verified. Scan them with Verify Asset.` tampil di atas tombol
100. Klik `[Verify Asset]`
101. Pindai TAG aset `Laptop Dell Latitude 5420 - 4`
102. Klik `[Submit]`
103. Verifikasi ringkasan error `1 asset is not verified. Scan it with Verify Asset.` tampil di atas tombol

### Submit dengan aset tanpa foto
104. Tampilkan Halaman Unassign dengan kondisi K15
105. Klik `[Submit]`
106. Verifikasi ringkasan error `2 assets need an unassign photo.` tampil di atas tombol

### Submit tanpa Assignee
107. Tampilkan Halaman Unassign dengan kondisi K17
108. Klik `[Submit]`
109. Verifikasi error `You must pick an assignee` tampil di bawah field Assignee

### Submit dengan daftar kosong
110. Tampilkan Halaman Unassign dengan kondisi K18
111. Klik `[Submit]`
112. Verifikasi ringkasan error `Add at least one asset to unassign.` tampil di atas tombol

### Submit berhasil untuk aset dari ASG asal yang sama
113. Tampilkan Halaman Unassign dengan kondisi K19
114. Klik `[Submit]`
115. Verifikasi toast `Success, 1 asset has been unassigned.` tampil setelah Submit berhasil
116. Verifikasi tujuan lanjutan sesudah Submit berhasil adalah `Assignment Detail` karena semua aset berasal dari ASG asal
117. Verifikasi `Laptop Dell Latitude 5420 - 40` tidak ikut diproses karena tidak ada di daftar

### Submit berhasil untuk aset dari beberapa ASG
118. Tampilkan Halaman Unassign dengan kondisi K20
119. Klik `[Submit]`
120. Verifikasi toast `Success, 2 assets have been unassigned.` tampil setelah Submit berhasil
121. Verifikasi tujuan lanjutan sesudah Submit berhasil adalah tab `Assigned Assets` karena aset berasal dari beberapa ASG

### Submit melebihi Bulk Transaction Row Limit pada halaman Unassign
122. Tampilkan Halaman Unassign dengan kondisi K33
123. Klik `[Submit]`
124. Verifikasi dialog blok `Bulk Transaction Row Limit` muncul pada halaman Unassign karena daftar melebihi batas
125. Verifikasi daftar, Verification, dan Unassign Photo tidak direset

### Tanpa pilihan hasil dan tanpa konfirmasi Assignee
126. Tampilkan Halaman Unassign dengan kondisi K2
127. Verifikasi daftar tidak memuat kolom `Assess`, `Compare`, maupun `Damage`
128. Verifikasi tidak ada pilihan hasil Unassign selain `[Submit]`
129. Verifikasi halaman tidak memuat kontrol konfirmasi Assignee

### Pemrosesan sendiri: baris penugasan Aktor sendiri
130. Tampilkan Halaman Unassign dengan kondisi K21
131. Verifikasi baris `Camera Sony A7 - 9` tidak ditandai ⚠ dan aksi `I Can't Scan the TAG` tidak tersedia pada baris itu
132. Klik `[Submit]`
133. Verifikasi toast `Success, 1 asset has been unassigned.` tampil
134. Verifikasi halaman Unassign ditutup setelah Unassign selesai

### Aksi I Can't Scan the TAG: identifikasi manual dan foto wajib
135. Tampilkan Halaman Unassign dengan kondisi K22
136. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan status `TAG Reported`
137. Verifikasi baris `Laptop Dell Latitude 5420 - 4` tetap dapat discan
138. Verifikasi kolom `Unassign Photo` baris `Laptop Dell Latitude 5420 - 4` memuat tombol ambil foto walau Photo at end OFF, karena fotonya wajib

### Remove from List tanpa dialog dan membuang isian halaman
139. Tampilkan Halaman Unassign dengan kondisi K23
140. Klik row action `Remove from List` pada baris `Laptop Dell Latitude 5420 - 4`
141. Verifikasi baris `Laptop Dell Latitude 5420 - 4` keluar dari daftar tanpa dialog
142. Klik `[+ Asset]`
143. Centang baris `Laptop Dell Latitude 5420 - 4`
144. Klik `[Select]`
145. Verifikasi baris `Laptop Dell Latitude 5420 - 4` kembali ke daftar sebagai `Unverified` tanpa laporan kerusakan


### Report Damaged dari halaman Unassign: Photo dan Description wajib
146. Tampilkan Dialog Report Damaged Unassign dengan kondisi K26
147. Verifikasi dialog memuat Photo satu foto dan Description dengan placeholder `Enter description`
148. Verifikasi dialog memuat tombol `[Cancel]` dan `[Report]`
149. Klik `[Report]`
150. Verifikasi error `Photo must not be empty` tampil
151. Verifikasi error `Description must not be empty` tampil

### Description tepat di batas panjang diterima
152. Tampilkan Dialog Report Damaged Unassign dengan kondisi K28
153. Isi Description `KerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakan` (360 karakter)
154. Klik `[Report]`
155. Verifikasi dialog Report Damaged tertutup
156. Verifikasi pesan `Max. 360 characters` tidak tampil
157. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan badge `Reported Damaged` pada kolom Status

### Description satu karakter melewati batas ditolak
158. Tampilkan Dialog Report Damaged Unassign dengan kondisi K29
159. Isi Description `KerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanx` (361 karakter)
160. Klik `[Report]`
161. Verifikasi pesan `Max. 360 characters` tampil
162. Verifikasi dialog Report Damaged tetap terbuka

### Description tepat di batas dengan spasi tepi diterima
163. Tampilkan Dialog Report Damaged Unassign dengan kondisi K30
164. Isi Description ` KerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakanKerusakan `
165. Klik `[Report]`
166. Verifikasi dialog Report Damaged tertutup
167. Verifikasi pesan `Max. 360 characters` tidak tampil

### Description tepat di batas dengan spasi tengah diterima
168. Tampilkan Dialog Report Damaged Unassign dengan kondisi K31
169. Isi Description `Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Layar retak parah sehingga tampilan tidak terbaca. Lay` (360 karakter)
170. Klik `[Report]`
171. Verifikasi dialog Report Damaged tertutup
172. Verifikasi pesan `Max. 360 characters` tidak tampil

### Description tepat di batas dengan huruf beraksen diterima
173. Tampilkan Dialog Report Damaged Unassign dengan kondisi K32
174. Isi Description `KérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKérusakanKerusakán` (360 karakter)
175. Klik `[Report]`
176. Verifikasi dialog Report Damaged tertutup
177. Verifikasi pesan `Max. 360 characters` tidak tampil

### Edit Damage Report terisi isian sebelumnya dan Cancel Damage Report
178. Tampilkan Halaman Unassign dengan kondisi K24
179. Klik row action `Edit Damage Report` pada baris `Laptop Dell Latitude 5420 - 4`
180. Verifikasi dialog Report Damaged terisi isian Description sebelumnya
181. Klik `[Cancel]`
182. Verifikasi laporan pada baris `Laptop Dell Latitude 5420 - 4` dapat diperbaiki lewat `Edit Damage Report`

### Scan berhasil membatalkan Report TAG manual
183. Tampilkan Halaman Unassign dengan kondisi K22
184. Klik `[Verify Asset]`
185. Pindai TAG aset `Laptop Dell Latitude 5420 - 4`
186. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan Verification `Verified`
187. Verifikasi baris `Laptop Dell Latitude 5420 - 4` tidak lagi menampilkan status `TAG Reported`

### Field Assignee dapat dicari
188. Tampilkan Halaman Unassign dengan kondisi K1
189. Ketik `Fin` pada field Assignee
190. Verifikasi opsi `Finance (Division)` tampil
191. Verifikasi opsi `Budi Santoso (Employee)` tidak tampil

### Halaman tanpa counter jumlah aset
192. Tampilkan Halaman Unassign dengan kondisi K2
193. Verifikasi daftar memuat baris `Laptop Dell Latitude 5420 - 4` dan `Laptop Dell Latitude 5420 - 40`
194. Verifikasi halaman tidak menampilkan counter jumlah aset yang di-Unassign

### Bulk Remove from List tanpa dialog
195. Tampilkan Halaman Unassign dengan kondisi K2
196. Centang baris `Laptop Dell Latitude 5420 - 4`
197. Klik bulk action `Remove from List`
198. Verifikasi baris `Laptop Dell Latitude 5420 - 4` keluar dari daftar tanpa dialog
199. Verifikasi baris `Laptop Dell Latitude 5420 - 40` tetap berada di daftar

### Remove from List membuang foto dan laporan kerusakan
200. Tampilkan Halaman Unassign dengan kondisi K23
201. Klik row action `Remove from List` pada baris `Laptop Dell Latitude 5420 - 4`
202. Klik `[+ Asset]`
203. Centang baris `Laptop Dell Latitude 5420 - 4`
204. Klik `[Select]`
205. Verifikasi baris `Laptop Dell Latitude 5420 - 4` kembali ke daftar tanpa foto pada kolom `Unassign Photo`
206. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan Status `Assigned`

### Kamera tidak tersedia pada Unassign Photo
207. Tampilkan Halaman Unassign dengan kondisi K34
208. Klik tombol ambil foto pada kolom `Unassign Photo` baris `Laptop Dell Latitude 5420 - 4`
209. Verifikasi toast `Error, camera is not available. Allow camera access or use the mobile app.` tampil setelah tombol ambil foto pada kolom `Unassign Photo` diklik
210. Verifikasi kolom `Unassign Photo` baris `Laptop Dell Latitude 5420 - 4` tetap kosong tanpa pilihan file atau galeri
211. Verifikasi tombol ambil foto pada baris `Laptop Dell Latitude 5420 - 40` tetap tersedia

### Unassign Photo terisi satu foto per aset
212. Tampilkan Halaman Unassign dengan kondisi K35
213. Verifikasi kolom `Unassign Photo` baris `Laptop Dell Latitude 5420 - 4` memuat satu foto

### Syarat tampil row action menurut keadaan baris
214. Tampilkan Halaman Unassign dengan kondisi K36
215. Buka row action pada baris `Laptop Dell Latitude 5420 - 4`
216. Verifikasi row action memuat `I Can't Scan the TAG` dan `Report Damaged`
217. Buka row action pada baris `Excavator PC200 - 4`
218. Verifikasi row action memuat `Remove from List`
219. Verifikasi row action tidak memuat `I Can't Scan the TAG` karena aset `Non TAG`
220. Buka row action pada baris `Printer HP M404 - 3`
221. Verifikasi row action memuat `Remove from List`
222. Verifikasi row action tidak memuat `Report Damaged` karena laporan sudah ada
223. Verifikasi row action tidak memuat `Cancel Damage Report` karena laporannya milik Assignee
224. Buka row action pada baris `Proyektor Epson EB-X06 - 2`
225. Verifikasi row action memuat `Cancel Damage Report` karena laporannya milik Aktor dan masih `Waiting for Confirmation`

### Row action aset yang sudah Verified
226. Tampilkan Halaman Unassign dengan kondisi K6
227. Buka row action pada baris `Laptop Dell Latitude 5420 - 4`
228. Verifikasi row action memuat `Remove from List`
229. Verifikasi row action tidak memuat `I Can't Scan the TAG` karena aset sudah `Verified`

### Dialog Select Asset Unassign: multi-select
230. Tampilkan Dialog Select Asset Unassign dengan kondisi K3
231. Centang baris `Laptop Dell Latitude 5420 - 4`
232. Centang baris `Laptop Dell Latitude 5420 - 40`
233. Verifikasi baris `Laptop Dell Latitude 5420 - 4` dan `Laptop Dell Latitude 5420 - 40` tercentang bersamaan
234. Klik `[Select]`
235. Verifikasi baris `Laptop Dell Latitude 5420 - 4` dan `Laptop Dell Latitude 5420 - 40` masuk ke daftar dengan Verification `Unverified`

### Dialog Select Asset Unassign: Filter Panel
236. Tampilkan Dialog Select Asset Unassign dengan kondisi K3
237. Klik ikon Filter
238. Verifikasi Filter Panel dialog Select Asset Unassign memuat field `Name` dengan placeholder `All asset names`
239. Verifikasi Filter Panel dialog Select Asset Unassign memuat field `Transaction ID` dengan placeholder `All transactions`
240. Verifikasi Filter Panel dialog Select Asset Unassign memuat field `Group` dengan placeholder `All groups`
241. Verifikasi Filter Panel dialog Select Asset Unassign memuat field rentang tanggal `Assigned Since` dengan placeholder `Select date`

### Dialog Select Asset Unassign: kolom yang dapat diurutkan
242. Tampilkan Dialog Select Asset Unassign dengan kondisi K3
243. Verifikasi header kolom `Name`, `Asset ID`, `Transaction ID`, `Group`, dan `Assigned Since` pada dialog Select Asset Unassign dapat diurutkan
244. Verifikasi header kolom `Photo` pada dialog Select Asset Unassign tidak dapat diurutkan

### Dialog Select Asset Unassign: isi sel dan hover Group
245. Tampilkan Dialog Select Asset Unassign dengan kondisi K37
246. Verifikasi baris `Genset Perkins 20kVA - 3` menampilkan Transaction ID `ASG-2026-0041`
247. Verifikasi baris `Genset Perkins 20kVA - 3` menampilkan Assigned Since `12 Oct 2026`
248. Verifikasi baris `Genset Perkins 20kVA - 3` menampilkan Group `Floor 1`
249. Verifikasi baris `Genset Perkins 20kVA - 3` menampilkan placeholder gambar standar pada kolom `Photo`
250. Arahkan kursor ke badge Group pada baris `Genset Perkins 20kVA - 3`
251. Verifikasi hover Group pada dialog Select Asset Unassign menyampaikan hierarki lengkap `Head Office > Floor 1`

### Dialog Select Asset Unassign: Setup Column
252. Tampilkan Dialog Select Asset Unassign dengan kondisi K3
253. Buka Setup Column
254. Verifikasi kolom `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Group`, dan `Assigned Since` masing-masing dapat disembunyikan lewat Setup Column
255. Hapus centang `Assigned Since` pada Setup Column
256. Verifikasi kolom `Name` pada dialog Select Asset Unassign tetap tampil
257. Verifikasi kolom `Assigned Since` tidak tampil

### Dialog Report Damaged: foto hanya dari kamera
258. Tampilkan Dialog Report Damaged Unassign dengan kondisi K26
259. Verifikasi sumber foto pada dialog Report Damaged adalah kamera, tanpa pilihan file atau galeri

### Tanpa permintaan konfirmasi kepada Assignee sesudah Submit berhasil
260. Tampilkan Halaman Unassign dengan kondisi K19
261. Klik `[Submit]`
262. Verifikasi toast `Success, 1 asset has been unassigned.` tampil sesudah Submit berhasil
263. Verifikasi tidak ada popup atau Task konfirmasi kepada Assignee

### Remove from List atas baris berlaporan Assignee: laporan tidak hilang
264. Tampilkan Halaman Unassign dengan kondisi K25
265. Klik row action `Remove from List` pada baris `Printer HP M404 - 3`
266. Verifikasi baris `Printer HP M404 - 3` keluar dari daftar tanpa dialog
267. Klik `[+ Asset]`
268. Centang baris `Printer HP M404 - 3`
269. Klik `[Select]`
270. Verifikasi baris `Printer HP M404 - 3` kembali ke daftar dengan Status `Reported Damaged`
