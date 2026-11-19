---
id: TC-FA-ASTL-UI-077-dialog-select-asset
title: "Dialog Select Asset"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-09c", "FI-21", "FI-22", "FI-23", "FI-24", "V-08", "S-45", "S-46", "D-15", "SelectAssetSetupColumn", "FLD-42", "§4.1h#b1", "§4.1h#p2", "§4.1h#p3", "§4.1h#r1", "§4.1h#r2", "§4.1h#r3", "§4.1h#r4", "§4.1h#p4", "§4.1h#p5", "§4.1h#b2", "§4.1h#b3", "§4.1h#b4", "§4.1h#b5", "§4.1h#b6", "§4.1h#b7", "§4.1h#b8", "§4.1h#b9", "§4.1h#b10", "§7.1#r2", "§7.1#p1", "EB-TBL-1@tabel-select-asset"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-09c": 5
  "FI-21": 8
  "FI-22": [9, 12]
  "FI-23": [33, 35, 74, 77]
  "FI-24": 42
  "V-08": [33, 35, 39, 74, 77]
  "S-45": 47
  "S-46": 49
  "D-15": 2
  "SelectAssetSetupColumn": [5, 18]
  "FLD-42": [8, 33]
  "§4.1h#b1": [3, 6, 7, 10, 13, 37, 39, 45, 54, 55, 77, 79, 80, 83, 84]
  "§4.1h#p2": 5
  "§4.1h#p3": [5, 18]
  "§4.1h#r1": [4, 14, 22, 30, 87, 88]
  "§4.1h#r2": 27
  "§4.1h#r3": 28
  "§4.1h#r4": 5
  "§4.1h#p4": 29
  "§4.1h#p5": 16
  "§4.1h#b2": [15, 19]
  "§4.1h#b3": 61
  "§4.1h#b4": [63, 64]
  "§4.1h#b5": [65, 67, 71]
  "§4.1h#b6": 62
  "§4.1h#b7": 68
  "§4.1h#b8": 69
  "§4.1h#b9": 61
  "§4.1h#b10": [55, 58, 59]
  "§7.1#r2": [24, 49]
  "§7.1#p1": [51, 52]
  "EB-TBL-1@tabel-select-asset": [24, 49, 51, 52]
anchor: []
coverage:
  web: automated
---
# Dialog Select Asset

## Prerequisites
- Aktor: Total Control; pada K9 dan K10 Group Manager yang mengelola group `IT` beserta descendant; pada K13 user pemegang Update di group `Cabang Bandung` beserta descendant, bukan Total Control maupun Group Manager.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Select Asset
- Data:
  - DU-077-1: Aset `Laptop Pro 16 - 1`, Asset ID `AST-0001`, Group `IT`, Category `Laptop`, Brand `Lenovo`, Model / Type `ThinkPad X1`, Status `Available`, Labels `Kritis`.
  - DU-077-2: Aset `Laptop Pro 16 - 2`, Asset ID `AST-0002`, Group `IT`, Category `Laptop`, Brand `Lenovo`, Model / Type `ThinkPad X1`, Status `Borrowed`, Labels `Audit Q4`.
  - DU-077-3: Aset `Proyektor X2 - 1`, Asset ID `AST-0010`, Group `Cabang Bandung`, Category `Proyektor`, Brand `Epson`, Model / Type `EB-X49`, Status `Available`, Labels `Garansi`.
  - DU-077-4: Aset `Genset 20kVA - 1`, Asset ID `AST-0060`, Group `Cabang Medan`, Status `Disposed`.
  - DU-077-5: Aset `Kamera Mirrorless - 1`, Asset ID `AST-0070`, Group `Cabang Bandung`, Unmanaged.
  - DU-077-6: Aset `Laptop Pro 16 - 3`, Asset ID `AST-0003`, Group `IT`, Category `Laptop`, Brand `Lenovo`, Model / Type `ThinkPad X1`, sudah ada di form transaksi.
  - DU-077-7: Aset `Meja Rapat - 1`, Asset ID `AST-0050`, Group `GA`, Category `Furnitur`, Brand `Informa`, Model / Type `Oval 8`, sudah ada di Draft lain.
  - DU-077-8: Aset `Server Rack - 1`, Asset ID `AST-0040`, Group `IT`, Status `In Repair`, tidak memenuhi syarat status transaksi.
  - DU-077-10: Aset `Proyektor X2 - 2`, Asset ID `AST-0011`, Group `Cabang Bandung Selatan` (descendant group `Cabang Bandung`), Category `Proyektor`, Brand `Epson`, Model / Type `EB-X49`, Status `Available`, Labels `Garansi`.
  - DU-077-9: Kata kunci Search tanpa hasil `Meja Bundar - 9`.
  - DU-077-11: Kata kunci Search berupa Asset ID `AST-0010`.
  - Pesan yang diharapkan untuk aset hasil pindai di luar cakupan: `This asset belongs to Cabang Bandung.`, dari pola `This asset belongs to [Group].` dan group aset DU-077-3.
- Kondisi:
  - K1: dibuka dari tombol toolbar; di tabel utama sudah tercentang DU-077-1, DU-077-4, dan DU-077-5; cakupan tulis Print Label seluruh client; aset yang dimuat adalah DU-077-1 sampai DU-077-3, sedangkan DU-077-4 (Disposed) dan DU-077-5 (Unmanaged) tidak ditampilkan di tabel dialog.
  - K2: dibuka dari tombol toolbar; belum ada aset tercentang di tabel utama; aset yang dimuat adalah DU-077-1 sampai DU-077-3.
  - K3: dibuka dari tombol toolbar; di tabel utama hanya DU-077-4 dan DU-077-5 yang tercentang; aset yang dimuat adalah DU-077-1 sampai DU-077-3, sedangkan DU-077-4 dan DU-077-5 tidak ditampilkan di tabel dialog.
  - K4: dibuka dari tombol toolbar; di tabel utama sudah tercentang DU-077-2; aset yang dimuat adalah DU-077-1 sampai DU-077-3.
  - K5: dibuka dari tombol toolbar; belum ada aset tercentang; aset yang dimuat adalah DU-077-1 sampai DU-077-3.
  - K6: data tabel sedang dimuat.
  - K7: tidak ada aset dalam cakupan tulis Print Label.
  - K8: memuat tabel gagal karena error server.
  - K9: dibuka dari tombol toolbar; aset dalam cakupan adalah DU-077-1 dan DU-077-2; DU-077-3 berada di luar cakupan.
  - K10: sama dengan K9; komponen pemindai mengembalikan aset DU-077-3.
  - K11: dibuka dari form transaksi Borrow; aset yang dimuat adalah DU-077-1, DU-077-2 (terhalang pihak Borrower yang dipilih), DU-077-6, dan DU-077-7; DU-077-8 tidak dimuat.
  - K13: dibuka dari tombol toolbar; aset dalam cakupan adalah DU-077-3 dan DU-077-10; DU-077-1 berada di luar cakupan.
  - K12: sama dengan K11 sesudah pihak Borrower diganti sehingga DU-077-2 tidak lagi terhalang.

## Test Steps

### Isi dialog dari tombol toolbar
1. Tampilkan Dialog Select Asset dengan kondisi K1
2. Verifikasi dialog berjudul `Select Asset` tampil dengan tombol `[Cancel]` dan `[Select]`
3. Verifikasi toolbar memuat penghitung aset terpilih, tombol `Search by Scan`, kotak Search, dan tombol Filter
4. Verifikasi kotak Search ber-placeholder `Search asset name or ID...`
5. Verifikasi tabel memuat kolom `Name`, `Asset ID`, `Group`, `Category`, `Brand`, `Model / Type`, `Status`, dan `Labels`
6. Verifikasi baris `Laptop Pro 16 - 1`, `Laptop Pro 16 - 2`, dan `Proyektor X2 - 1` tampil dengan Asset ID `AST-0001`, `AST-0002`, `AST-0010` dan Group `IT`, `IT`, `Cabang Bandung`
7. Verifikasi baris `Genset 20kVA - 1` dan `Kamera Mirrorless - 1` tidak tampil
8. Verifikasi baris `Laptop Pro 16 - 1` tercentang sebagai centang awal dari tabel utama
9. Verifikasi penghitung `1 asset selected` tampil
10. Verifikasi `Genset 20kVA - 1` dan `Kamera Mirrorless - 1` tidak dihitung pada penghitung dan tidak tercentang
11. Centang baris `Laptop Pro 16 - 2`
12. Verifikasi penghitung `2 assets selected` tampil
13. Verifikasi `[Select]` aktif dan footer tidak memuat penghitung
14. Verifikasi nama `Laptop Pro 16 - 1` tampil sebagai teks biasa, bukan tautan
15. Verifikasi tabel tidak memuat menu aksi baris
16. Verifikasi kolom Actions kosong dengan header ⋯ sebagai pemicu Column Visibility, dan toolbar tidak memuat tombol Setup Column
17. Klik header ⋯ pada kolom Actions
18. Verifikasi kolom `Name`, `Asset ID`, `Group`, `Category`, `Brand`, `Model / Type`, `Status`, dan `Labels` Visible dan dapat disembunyikan
19. Verifikasi checkbox seleksi baris tidak termasuk dalam daftar Column Visibility

### Search dan Filter
20. Tampilkan Dialog Select Asset dengan kondisi K1
21. Ketik Search `Laptop Pro 16 - 2`, tekan Enter
22. Verifikasi baris `Laptop Pro 16 - 2` tampil
23. Ganti isi kotak Search dengan `Meja Bundar - 9`, tekan Enter
24. Verifikasi `No results found` dan `Try adjusting your search or filter.` tampil
25. Klik `(←)` pada kotak Search
26. Klik tombol Filter
27. Verifikasi filter `Group` ber-placeholder `All groups` bertipe `Tree picker multi-select`
28. Verifikasi filter `Category` bertipe `Tree picker multi-select`
29. Verifikasi panel Filter memuat filter Group, Category, Brand, Model / Type, Status, dan Labels
30. Verifikasi panel Filter tidak memuat filter Name

### Select tanpa aset terpilih
31. Tampilkan Dialog Select Asset dengan kondisi K2
32. Klik `[Select]`
33. Verifikasi dialog `Select Asset` tetap terbuka dan teks `You must pick an asset` tampil di footer
34. Centang baris `Laptop Pro 16 - 1`
35. Verifikasi teks `You must pick an asset` tidak tampil

### Seluruh centang awal dibuang
36. Tampilkan Dialog Select Asset dengan kondisi K3
37. Verifikasi penghitung aset terpilih tidak tampil
38. Klik `[Select]`
39. Verifikasi teks `You must pick an asset` tampil di footer dan dialog `Select Asset` tetap terbuka

### Select dengan aset terpilih membuka Print Label
40. Tampilkan Dialog Select Asset dengan kondisi K4
41. Klik `[Select]`
42. Verifikasi dialog `Select Asset` tertutup dan dialog `Print Label` terbuka berisi `Laptop Pro 16 - 2`

### Search by Scan
43. Tampilkan Dialog Select Asset dengan kondisi K5
44. Klik `Search by Scan`
45. Verifikasi dialog pemindai milik komponen pemindai platform terbuka

### Loading, kosong, dan gagal memuat
46. Tampilkan Dialog Select Asset dengan kondisi K6
47. Verifikasi selama data dimuat baris data belum tampil dan `No assets available` maupun `Unable to load this data.` tidak tampil
48. Tampilkan Dialog Select Asset dengan kondisi K7
49. Verifikasi `No assets available` dan `Assets you can print labels for will appear here.` tampil
50. Tampilkan Dialog Select Asset dengan kondisi K8
51. Verifikasi teks `Unable to load this data.` dan tombol `[Try Again]` tampil
52. Verifikasi empty state `No assets available` tidak tampil

### Cakupan group aktor
53. Tampilkan Dialog Select Asset dengan kondisi K9
54. Verifikasi baris `Laptop Pro 16 - 1` dan `Laptop Pro 16 - 2` tampil
55. Verifikasi baris `Proyektor X2 - 1` tidak dimuat

### Aset hasil pindai di luar cakupan
56. Tampilkan Dialog Select Asset dengan kondisi K10
57. Klik `Search by Scan`
58. Verifikasi pesan `This asset belongs to Cabang Bandung.` tampil
59. Verifikasi nama `Proyektor X2 - 1` tidak tampil dan penghitung aset terpilih tidak bertambah

### Dialog Select Asset di form transaksi
60. Tampilkan Dialog Select Asset dengan kondisi K11
61. Verifikasi keterangan `Available assets in your groups.` tampil di bawah judul `Select Asset`
62. Verifikasi kolom `Status` tidak tampil
63. Verifikasi baris `Laptop Pro 16 - 1` tampil dan checkbox-nya dapat dicentang
64. Verifikasi baris `Server Rack - 1` tidak tampil sama sekali
65. Verifikasi baris `Laptop Pro 16 - 2` tampil dengan Eligibility `Not ready` dan checkbox Disabled
66. Arahkan kursor ke checkbox baris `Laptop Pro 16 - 2`
67. Verifikasi alasan aset terhalang oleh pihak Borrower tersampaikan pada checkbox yang Disabled
68. Verifikasi baris `Laptop Pro 16 - 3` tercentang dan checkbox Disabled dengan alasan `Already added`
69. Verifikasi baris `Meja Rapat - 1` dapat dicentang tanpa penanda Draft
70. Tampilkan Dialog Select Asset dengan kondisi K12
71. Verifikasi checkbox baris `Laptop Pro 16 - 2` aktif

### Pesan V-08 hilang saat dialog dibuka ulang
72. Tampilkan Dialog Select Asset dengan kondisi K2
73. Klik `[Select]`
74. Verifikasi teks `You must pick an asset` tampil di footer
75. Klik `[Cancel]`
76. Tampilkan Dialog Select Asset dengan kondisi K2
77. Verifikasi teks `You must pick an asset` tidak tampil

### Cakupan pemegang Update di group tertentu
78. Tampilkan Dialog Select Asset dengan kondisi K13
79. Verifikasi baris `Proyektor X2 - 1` dan `Proyektor X2 - 2` tampil
80. Verifikasi baris `Laptop Pro 16 - 1` tidak dimuat

### Select pada seleksi campuran hanya membawa aset valid
81. Tampilkan Dialog Select Asset dengan kondisi K1
82. Klik `[Select]`
83. Verifikasi dialog `Select Asset` tertutup dan dialog `Print Label` terbuka berisi `Laptop Pro 16 - 1`
84. Verifikasi dialog `Print Label` tidak memuat `Genset 20kVA - 1` maupun `Kamera Mirrorless - 1`

### Search lewat Asset ID
85. Tampilkan Dialog Select Asset dengan kondisi K2
86. Ketik Search `AST-0010`, tekan Enter
87. Verifikasi baris `Proyektor X2 - 1` tampil dengan Asset ID `AST-0010`
88. Verifikasi baris `Laptop Pro 16 - 1` tidak tampil
