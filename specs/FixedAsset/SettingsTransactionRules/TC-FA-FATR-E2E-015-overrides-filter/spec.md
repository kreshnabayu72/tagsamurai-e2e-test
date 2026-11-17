---
id: TC-FA-FATR-E2E-015-overrides-filter
title: "Filter tabel Overrides"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r266, §4.1#r268, §4.1#r269, §4.1#r271, §4.1#r270, EB-FLT-1@tabel-overrides, EB-FLT-4@tabel-overrides, EB-FLT-3]
smoke: [EB-FLT-3]
dependsOn: []
trace:
  §4.1#r266: [20, 21, 24]
  §4.1#r268: [8, 34, 35]
  §4.1#r269: [15, 29, 30, 75]
  §4.1#r271: [70, 71]
  §4.1#r270: [59, 60, 63]
  EB-FLT-1@tabel-overrides: [8, 9, 11, 13, 15, 16, 65, 91]
  EB-FLT-4@tabel-overrides: [41, 43, 46, 50, 51, 53, 54, 75, 85, 86, 89, 97, 100, 101, 105, 106]
  EB-FLT-3: [24, 29, 30]
anchor: [5]
coverage:
  web: automated
---

# Filter tabel Overrides

## Prerequisites
- Aktor: Total Control `Rina Wulandari`.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-015-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-015-2: Group tingkat atas `Proyek Karawang {runId}`.
  - DU-015-3: Group tingkat atas `Workshop {runId}`.
  - DU-015-4: Group tingkat atas `Gudang Kota {runId}`.
  - DU-015-5: Asset Name `Excavator PC200 {runId}`, Code `EXC15-{runId}`, Category `Machinery {runId}`, UoM `Unit`.
  - DU-015-6: Asset Name `Toyota Avanza {runId}`, Code `AVZ15-{runId}`, Category `Machinery {runId}`, UoM `Unit`.
  - DU-015-7: user `Budi Santoso`, Total Control, tampil di kolom Created By sebagai `Budi S`.
  - DU-015-8: user `Dewi Anggraini`, Total Control, tampil sebagai `Dewi A`, yang tidak membuat satu pun override.
  - DU-015-9: override Group `Proyek Karawang {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (30 days)`, Created By `Rina W` (dibuat oleh `Rina Wulandari`), Created At `T0 − 5 hari`; kata kunci Search yang dipakai atasnya: `Karawang {runId}`.
  - DU-015-10: override Group `Workshop {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (20 days), Max extensions (3)`, Created By `Budi S` (dibuat oleh `Budi Santoso`), Created At `T0 − 5 hari`; kata kunci opsi filter yang dipakai: `ration` dan `Zzqx`.
  - DU-015-11: override Asset Name `Excavator PC200 {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max extensions (2)`, Created By `Rina W` (dibuat oleh `Rina Wulandari`), Created At `T0 − 2 hari`.
  - DU-015-12: override Asset Name `Toyota Avanza {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max extensions (1)`, Created By `Budi S` (dibuat oleh `Budi Santoso`), Created At `T0 − 2 hari`.
  - DU-015-13: override Group `Proyek Karawang {runId}` di Category `Machinery {runId}` transaksi `Assign`, Overridden `Need recipient confirmation (No)`, Created By `Rina W` (dibuat oleh `Rina Wulandari`), Created At `T0 − 5 hari`.
  - DU-015-15: Group tingkat atas `Kantor Pusat {runId}`.
  - DU-015-16: override Group `Kantor Pusat {runId}` di All categories transaksi `Borrow`, Overridden `Max duration (10 days)`, Created By `Rina W` (dibuat oleh `Rina Wulandari`), Created At `T0 − 2 hari`.
  - DU-015-14: Override yang dibuat spec ini bernilai: Group `Gudang Kota {runId}` dengan `Allow Borrow` `Deny` di Category `Machinery {runId}` transaksi `Borrow`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Kolom `Category` tabel Overrides tidak ditampilkan (bawaan) untuk `Rina Wulandari`.
  - Created At kelima override tab `Borrow` bernilai seperti tercatat pada datanya, dan override tab `Assign` bernilai `T0 − 5 hari`.

## Test Steps

### Opsi filter berasal dari data tabel dan dapat dicari
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
5. Verifikasi keempat baris data uji tampil di tabel Overrides: Target `Proyek Karawang {runId}`, Target `Workshop {runId}`, Target `Excavator PC200 {runId}`, dan Target `Toyota Avanza {runId}`
6. Klik ikon filter pada toolbar tabel Overrides
7. Klik field `Overridden` pada panel filter
8. Verifikasi opsi `Max duration` dan opsi `Max extensions` tampil masing-masing satu kali pada field `Overridden`
9. Verifikasi opsi `Need recipient confirmation` tidak tampil pada field `Overridden` karena hanya dimiliki override tab `Assign`
10. Ketik `ration` pada kotak cari opsi Overridden
11. Verifikasi opsi `Max duration` tampil pada hasil cari opsi Overridden
12. Ganti isi kotak cari opsi Overridden dengan `Zzqx`
13. Verifikasi `No results found` tampil pada daftar opsi Overridden
14. Klik field `Created By` pada panel filter
15. Verifikasi opsi `Rina W` dan opsi `Budi S` tampil pada field `Created By`
16. Verifikasi opsi `Dewi A` tidak tampil pada field `Created By` karena pengguna itu belum membuat override

### Filter satu field memakai OR dan antar field memakai AND
17. Klik field `Scope` pada panel filter
18. Pilih opsi `Group`
19. Klik `[Apply]`
20. Verifikasi baris `Proyek Karawang {runId}` dan baris `Workshop {runId}` dengan Scope `Group` tampil di tabel Overrides
21. Verifikasi baris `Excavator PC200 {runId}` dan baris `Toyota Avanza {runId}` tidak tampil di tabel Overrides
22. Pilih opsi `Asset Name` pada field `Scope`
23. Klik `[Apply]`
24. Verifikasi keempat baris data uji tampil karena opsi `Group` dan opsi `Asset Name` digabung dengan OR
25. Klik `[Clear Field]`
26. Pilih opsi `Group` pada field `Scope`
27. Pilih opsi `Rina W` pada field `Created By`
28. Klik `[Apply]`
29. Verifikasi baris `Proyek Karawang {runId}` dengan Scope `Group` dan Created By `Rina W` tampil karena memenuhi kedua field
30. Verifikasi baris `Workshop {runId}`, baris `Excavator PC200 {runId}`, dan baris `Toyota Avanza {runId}` tidak tampil karena tidak memenuhi kedua field
31. Klik `[Clear Field]`
32. Pilih opsi `Max extensions` pada field `Overridden`
33. Klik `[Apply]`
34. Verifikasi baris `Excavator PC200 {runId}` dengan Overridden `Max extensions (2)`, baris `Toyota Avanza {runId}` dengan Overridden `Max extensions (1)`, dan baris `Workshop {runId}` dengan Overridden `Max duration (20 days), Max extensions (3)` tampil karena Filter mencocokkan salah satu field yang diubah
35. Verifikasi baris `Proyek Karawang {runId}` tidak tampil

### Search dan Filter menghasilkan irisan dan melepas satu saringan memulihkan hasil
36. Klik `[Clear Field]`
37. Pilih opsi `Group` pada field `Scope`
38. Pilih opsi `Rina W` pada field `Created By`
39. Klik `[Apply]`
40. Ketik Search `Karawang {runId}` pada tabel Overrides, tekan Enter
41. Verifikasi baris `Proyek Karawang {runId}` tampil karena memenuhi Search dan Filter
42. Ganti isi kotak Search dengan `Excavator PC200 {runId}`, tekan Enter
43. Verifikasi `No results found` tampil karena baris `Excavator PC200 {runId}` cocok dengan Search tetapi tidak dengan Filter Scope `Group`
44. Klik `[Clear Field]`
45. Klik `[Apply]`
46. Verifikasi baris `Excavator PC200 {runId}` tampil kembali dan baris `Proyek Karawang {runId}` tidak tampil karena Search dipertahankan
47. Klik field `Scope` pada panel filter
48. Pilih opsi `Asset Name`
49. Klik `[Apply]`
50. Verifikasi baris `Excavator PC200 {runId}` dengan Scope `Asset Name` tampil karena memenuhi Search dan Filter Scope `Asset Name`
51. Verifikasi baris `Toyota Avanza {runId}` tidak tampil karena tidak cocok dengan Search `Excavator PC200 {runId}`
52. Klik `(←)` pada kotak Search
53. Verifikasi baris `Excavator PC200 {runId}` dan baris `Toyota Avanza {runId}` dengan Scope `Asset Name` tampil sesudah Search dikosongkan
54. Verifikasi baris `Proyek Karawang {runId}` dan baris `Workshop {runId}` tidak tampil karena Filter Scope `Asset Name` dipertahankan

### Filter Created At menyaring rentang tanggal
55. Klik `[Clear Field]`
56. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
57. Pada field `Created At`, pilih rentang dari `T0 − 6 hari` sampai `T0 − 4 hari`
58. Klik `[Apply]`
59. Verifikasi baris `Proyek Karawang {runId}` dan baris `Workshop {runId}` dengan Created At `T0 − 5 hari` tampil
60. Verifikasi baris `Excavator PC200 {runId}` dan baris `Toyota Avanza {runId}` tidak tampil karena Created At `T0 − 2 hari` di luar rentang
61. Pada field `Created At`, pilih rentang dari `T0 − 12 hari` sampai `T0 − 10 hari`
62. Klik `[Apply]`
63. Verifikasi `No results found` tampil karena tidak ada override yang dibuat pada rentang itu
64. Klik field `Overridden` pada panel filter
65. Verifikasi `No options available` tampil pada field `Overridden` karena tidak ada baris sumber opsi pada rentang itu

### Filter Category bekerja walau kolom Category tidak ditampilkan
66. Klik `[Clear Field]`
67. Klik field `Category` pada panel filter
68. Pilih opsi `Machinery {runId}`
69. Klik `[Apply]`
70. Verifikasi baris `Proyek Karawang {runId}`, baris `Workshop {runId}`, baris `Excavator PC200 {runId}`, dan baris `Toyota Avanza {runId}` tampil walau kolom `Category` tidak ditampilkan
71. Verifikasi baris `Kantor Pusat {runId}` dengan Category `All categories` tidak tampil sesudah Filter Category `Machinery {runId}`

### Override baru yang tidak cocok dengan Filter tidak tampil tetapi nilainya menjadi opsi
72. Klik `[Clear Field]`
73. Pilih opsi `Budi S` pada field `Created By`
74. Klik `[Apply]`
75. Verifikasi baris `Workshop {runId}` dan baris `Toyota Avanza {runId}` dengan Created By `Budi S` tampil
76. Klik `[+ Override]`
77. Pilih Scope `Group`
78. Klik `[Select Group]`
79. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
80. Centang Group `Gudang Kota {runId}`
81. Klik `[Select]`
82. Pilih Field `Allow Borrow`
83. Pilih Value `Deny`
84. Klik `[Submit]`
85. Verifikasi toast `Success, override has been added.` tampil untuk override `Gudang Kota {runId}`
86. Verifikasi baris `Gudang Kota {runId}` dengan Created By `Rina W` tidak tampil karena Filter Created By `Budi S` masih aktif
87. Klik `[Clear Field]`
88. Klik `[Apply]`
89. Verifikasi baris `Gudang Kota {runId}` dengan Overridden `Allow Borrow (Deny)` tampil sesudah Filter dilepas
90. Klik field `Overridden` pada panel filter
91. Verifikasi opsi `Allow Borrow` tampil pada field `Overridden` tanpa memuat ulang halaman

### Clear Filter dan Clear Search mempertahankan Sort
92. Ganti isi kotak Search dengan `{runId}`, tekan Enter
93. Klik `[Clear Field]`
94. Pilih opsi `Group` pada field `Scope`
95. Klik `[Apply]`
96. Klik header kolom Target pada tabel Overrides
97. Verifikasi baris `Gudang Kota {runId}` dengan Scope `Group` tampil di atas baris `Kantor Pusat {runId}` secara ascending menurut Target
98. Klik `[Clear Field]`
99. Klik `[Apply]`
100. Verifikasi baris `Excavator PC200 {runId}`, baris `Gudang Kota {runId}`, dan baris `Kantor Pusat {runId}` tampil berurutan dari atas ke bawah secara ascending menurut Target sesudah Filter dilepas
101. Verifikasi kotak Search masih berisi `{runId}` sesudah Filter dilepas
102. Pilih opsi `Group` pada field `Scope`
103. Klik `[Apply]`
104. Klik `(←)` pada kotak Search
105. Verifikasi baris `Gudang Kota {runId}` dengan Scope `Group` tampil di atas baris `Kantor Pusat {runId}` secara ascending menurut Target sesudah Search dikosongkan
106. Verifikasi baris `Excavator PC200 {runId}` tidak tampil sesudah Search dikosongkan karena Filter Scope `Group` dipertahankan
