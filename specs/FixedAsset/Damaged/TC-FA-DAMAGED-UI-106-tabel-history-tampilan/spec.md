---
id: TC-FA-DAMAGED-UI-106-tabel-history-tampilan
title: "Tabel sub-tab History: kolom awal, Resolved By (termasuk System), Resolved Date, Duration, badge status selesai, toolbar tanpa Search by Scan, tanpa Checkbox, aksi Damage Log saja, dan state kosong"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-02, "§4.1#r2", "§5#r1", S-DMG-13, S-DMG-14, EB-TBL-1@tabel-history, EB-TBL-4@kolom-resolved-by, EB-FLT-6@tabel-history]
smoke: []
dependsOn: []
trace:
  T-DMG-02: [2, 3, 4, 5, 6, 8, 9, 10, 11, 16, 17, 18, 19, 20, 21, 29, 30, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 96, 98, 99, 100, 101, 103, 105, 108]
  "§4.1#r2": [26]
  "§5#r1": [23, 24, 25]
  S-DMG-13: [32, 33]
  S-DMG-14: [36, 37]
  EB-TBL-1@tabel-history: [32, 33, 36, 37, 38, 40, 41, 42]
  EB-TBL-4@kolom-resolved-by: [13, 15, 16]
  EB-FLT-6@tabel-history: [47, 48, 52, 53, 54, 56]
anchor: []
coverage:
  web: automated
---

# Tabel sub-tab History: kolom awal, Resolved By (termasuk System), Resolved Date, Duration, badge status selesai, toolbar tanpa Search by Scan, tanpa Checkbox, aksi Damage Log saja, dan state kosong

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab `Damaged`, sub-tab `History`.
- Komponen: Tabel T-DMG-02 (sub-tab History)
- Data:
  - DU-106-1: Record `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Group `Head Office`, Status `Repaired`, Source `Borrow return`, Photo `laptop-dell-latitude-5420-9.jpg`, Last Holder `Sari Dewi` (tampil `Sari D`, dari `Sari Dewi`; Division `Operations`, Employee ID `EMP-0145`), Reported By `Rina Wijaya`, Reported Date `12/10/26, 09:00` dari `2026-10-12T02:00:00Z`, Duration `6 days` dari 6 hari kalender, Resolved By `Rina Wijaya` (tampil `Rina W`, dari `Rina Wijaya`), Resolved Date `18/10/26, 14:10` dari `2026-10-18T07:10:00Z`.
  - DU-106-2: Record `Drill Bosch GSB - 4`, Asset ID `DRL-2026-0004`, Group `Warehouse`, Status `Disposed`, Source `Audit`, Reported By `Agus Prasetyo`, Reported Date `01/08/26, 08:00` dari `2026-08-01T01:00:00Z`, Duration `62 days` dari 62 hari kalender, Resolved By `System`, Resolved Date `02/10/26, 00:00` dari `2026-10-01T17:00:00Z`.
  - DU-106-3: Record `Camera Canon EOS - 1`, Asset ID `CAM-2026-0001`, Group `Head Office`, Status `Rejected`, Source `Reported by holder`, Reported By `Budi`, Reported Date `05/11/26, 08:30` dari `2026-11-05T01:30:00Z`, Duration `1 day` dari 1 hari kalender, Resolved By `Rina Wijaya`, Resolved Date `06/11/26, 09:15` dari `2026-11-06T02:15:00Z`.
  - DU-106-4: Record `Scanner Fujitsu fi-7160 - 2`, Asset ID `SCN-2026-0002`, Group `Head Office`, Status `Canceled`, Source `Reported by holder`, Reported By `Dewi Anggraini` (tampil `Dewi A`, dari `Dewi Anggraini`), Reported Date `08/11/26, 10:00` dari `2026-11-08T03:00:00Z`, Duration `1 day` dari 1 hari kalender, Resolved By `Dewi Anggraini`, Resolved Date `09/11/26, 08:00` dari `2026-11-09T01:00:00Z`.
  - DU-106-7: Record `Handheld Scanner Zebra TC21 - 2`, Asset ID `HSC-2026-0002`, Group `Head Office`, Status `Repaired`, Source `Reported by holder`, Last Holder `Tono Rahmat` tanpa akun (tampil `Tono R`, dari `Tono Rahmat`; Division `Finance`, PIC `Sinta Maharani` sehingga hover memuat `PIC: Sinta Maharani`, Employee ID `EMP-0217`), Reported By laporan PIC `Sinta Maharani` atas nama `Tono Rahmat` (tampil `Sinta M on behalf of Tono R`, dari `Sinta Maharani` dan `Tono Rahmat`), Reported Date `03/11/26, 09:30` dari `2026-11-03T02:30:00Z`, Duration `2 days` dari 2 hari kalender, Resolved By `Rina Wijaya`, Resolved Date `05/11/26, 11:00` dari `2026-11-05T04:00:00Z`.
  - DU-106-8: Record `Projector Epson EB-X06 - 5`, Asset ID `PRJ-2026-0005`, Group `Head Office`, Status `Repaired`, Source `Registration`, tanpa Damaged Photo, Reported By `Rina Wijaya`, Reported Date `02/11/26, 09:00` dari `2026-11-02T02:00:00Z`, Duration `3 days` dari 3 hari kalender, Resolved By `Rina Wijaya`, Resolved Date `05/11/26, 13:45` dari `2026-11-05T06:45:00Z`.
  - DU-106-5: Daftar record selesai kosong untuk entitas yang belum menyelesaikan record apa pun (jumlah record `0`).
- Kondisi:
  - K1: daftar memuat DU-106-1 sampai DU-106-4 dengan kolom bawaan Setup Column; Date Format bernilai `dd/MM/yy`; Time Format bernilai `24h`; Time Zone bernilai `Asia/Jakarta`.
  - K2: daftar kosong sesuai DU-106-5.
  - K3: daftar memuat DU-106-1; pencarian `Printer Hilang` tidak cocok dengan record mana pun sehingga jawaban daftar kosong.
  - K4: memuat daftar gagal karena error server.
  - K5: daftar seperti K1; aktor berhak melihat nilai finansial.
  - K6: daftar memuat DU-106-7 dan DU-106-8 dengan kolom bawaan Setup Column; Date Format bernilai `dd/MM/yy`; Time Format bernilai `24h`; Time Zone bernilai `Asia/Jakarta`.

## Test Steps

### Kolom awal tabel History
1. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
2. Verifikasi header kolom `Photo`, `Name`, `Asset ID`, `Group`, `Status`, `Source`, `Last Holder`, `Reported By`, `Reported Date`, `Duration`, `Resolved By`, dan `Resolved Date` tampil
3. Verifikasi header kolom `Brand`, `Model/Type`, `TAG`, `Category`, `Alias Name`, `Measurement`, `Division`, `Labels`, `Asset Class`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tidak dirender
4. Verifikasi header kolom `Days Damaged`, `Last Updated`, dan `Modified By` tidak dirender
5. Verifikasi checkbox seleksi tidak dirender pada header maupun pada baris
6. Verifikasi `Laptop Dell Latitude 5420 - 9` tampil sebagai tautan pada kolom `Name`

### Badge status record selesai
7. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
8. Verifikasi badge status `Repaired` tampil pada baris `Laptop Dell Latitude 5420 - 9`
9. Verifikasi badge status `Disposed` tampil pada baris `Drill Bosch GSB - 4`
10. Verifikasi badge status `Rejected` tampil pada baris `Camera Canon EOS - 1`
11. Verifikasi badge status `Canceled` tampil pada baris `Scanner Fujitsu fi-7160 - 2`

### Resolved By, Resolved Date, dan Duration
12. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
13. Verifikasi kolom `Resolved By` baris `Laptop Dell Latitude 5420 - 9` menampilkan `Rina W`
14. Arahkan pointer ke `Rina W` pada kolom `Resolved By` baris `Laptop Dell Latitude 5420 - 9`
15. Verifikasi nama lengkap `Rina Wijaya` tampil
16. Verifikasi kolom `Resolved By` baris `Drill Bosch GSB - 4` menampilkan `System`
17. Verifikasi kolom `Resolved Date` baris `Laptop Dell Latitude 5420 - 9` menampilkan `18/10/26, 14:10`
18. Verifikasi kolom `Resolved Date` baris `Drill Bosch GSB - 4` menampilkan `02/10/26, 00:00`
19. Verifikasi kolom `Duration` baris `Laptop Dell Latitude 5420 - 9` menampilkan `6 days`
20. Verifikasi kolom `Duration` baris `Camera Canon EOS - 1` menampilkan `1 day`
21. Verifikasi kolom `Duration` baris `Drill Bosch GSB - 4` menampilkan `62 days`

### Toolbar tanpa Search by Scan
22. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
23. Verifikasi kotak Search tampil dengan placeholder `Search asset name or ID...`
24. Verifikasi tombol `Search by Scan` tidak tampil
25. Verifikasi kontrol Filter dan Download tampil di toolbar
26. Verifikasi toolbar dan tabel T-DMG-02 tampil bersama pada sub-tab `History`

### Aksi baris hanya Damage Log
27. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
28. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 9`
29. Verifikasi menu memuat `Damage Log`
30. Verifikasi aksi `Review`, `Mark as Repaired`, `Report Disposal`, `Report Missing`, dan `Cancel Disposal Report` tidak dirender

### State kosong alami
31. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K2
32. Verifikasi judul `No resolved records yet` tampil
33. Verifikasi deskripsi `Repaired, disposed, rejected, and canceled reports will appear here.` tampil

### State kosong tersaring
34. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K3
35. Ketik Search `Printer Hilang`, tekan Enter
36. Verifikasi judul `No results found` tampil
37. Verifikasi deskripsi `Try adjusting your search or filter.` tampil
38. Verifikasi judul `No resolved records yet` tidak tampil

### Gagal muat bukan state kosong
39. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K4
40. Verifikasi pesan `Unable to load this data.` tampil
41. Verifikasi tombol `[Try Again]` tampil
42. Verifikasi judul `No resolved records yet` tidak tampil

### Menyembunyikan kolom tidak menghapus field dan saringan filter
43. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
44. Klik ikon Filter
45. Pilih opsi `Rejected` pada field `Status`
46. Klik `[Apply]`
47. Verifikasi baris `Camera Canon EOS - 1` tampil
48. Verifikasi baris `Laptop Dell Latitude 5420 - 9` tidak tampil
49. Klik ikon Filter
50. Klik header kolom Actions (`⋯`)
51. Hapus centang `Status` pada daftar kolom
52. Verifikasi header kolom `Status` tidak dirender
53. Verifikasi baris `Camera Canon EOS - 1` tetap tampil
54. Verifikasi baris `Laptop Dell Latitude 5420 - 9` tetap tidak tampil
55. Klik ikon Filter
56. Verifikasi field `Status` tetap ada pada Filter Panel dan memuat chip `Rejected`

### Placeholder field Filter pada kolom bawaan History
57. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K5
58. Klik ikon Filter
59. Verifikasi field `Asset Name` tampil dengan placeholder `All asset names`
60. Verifikasi field `Group` tampil dengan placeholder `All groups`
61. Verifikasi field `Status` tampil dengan placeholder `All statuses`
62. Verifikasi field `Source` tampil dengan placeholder `All sources`
63. Verifikasi field `Last Holder` tampil dengan placeholder `All holders`
64. Verifikasi field `Reported By` tampil dengan placeholder `All users`
65. Verifikasi field `Reported Date` tampil dengan placeholder `Select date`
66. Verifikasi field `Duration` tampil dengan dua input berplaceholder `Min` dan `Max`
67. Verifikasi field `Resolved By` tampil dengan placeholder `All users`
68. Verifikasi field `Resolved Date` tampil dengan placeholder `Select date`

### Placeholder field Filter pada kolom tersembunyi History
69. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K5
70. Klik ikon Filter
71. Verifikasi field `Brand` tampil dengan placeholder `All brands`
72. Verifikasi field `Model/Type` tampil dengan placeholder `All models`
73. Verifikasi field `TAG` tampil dengan placeholder `All TAGs`
74. Verifikasi field `Category` tampil dengan placeholder `All categories`
75. Verifikasi field `Measurement` tampil dengan placeholder `All units`
76. Verifikasi field `Division` tampil dengan placeholder `All divisions`
77. Verifikasi field `Label` tampil dengan placeholder `All labels`
78. Verifikasi field `Asset Class` tampil dengan placeholder `All asset classes`
79. Verifikasi field `Register Date` tampil dengan placeholder `Select date`
80. Verifikasi field `Purchase Date` tampil dengan placeholder `Select date`
81. Verifikasi field `Warranty Expiry` tampil dengan placeholder `Select date`
82. Verifikasi field `Purchase Cost` tampil dengan dua input berplaceholder `Min` dan `Max`
83. Verifikasi field `Asset Value (Commercial)` tampil dengan dua input berplaceholder `Min` dan `Max`
84. Verifikasi field `Asset Value (Fiscal)` tampil dengan dua input berplaceholder `Min` dan `Max`

### Hover Last Holder dan Reported By pada tabel History
85. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
86. Verifikasi kolom `Last Holder` baris `Laptop Dell Latitude 5420 - 9` menampilkan `Sari D`
87. Arahkan pointer ke `Sari D` pada kolom `Last Holder` baris `Laptop Dell Latitude 5420 - 9`
88. Verifikasi nama lengkap pemegang `Sari Dewi` tampil
89. Verifikasi Division pemegang `Operations` tampil
90. Verifikasi Employee ID pemegang `EMP-0145` tampil
91. Verifikasi kolom `Reported By` baris `Scanner Fujitsu fi-7160 - 2` menampilkan `Dewi A`
92. Arahkan pointer ke `Dewi A` pada kolom `Reported By` baris `Scanner Fujitsu fi-7160 - 2`
93. Verifikasi nama lengkap pelapor `Dewi Anggraini` tampil

### Pemegang tanpa akun dan laporan PIC pada tabel History
94. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K6
95. Verifikasi kolom `Last Holder` baris `Handheld Scanner Zebra TC21 - 2` menampilkan `Tono R`
96. Verifikasi kolom `Reported By` baris `Handheld Scanner Zebra TC21 - 2` menampilkan `Sinta M on behalf of Tono R`
97. Arahkan pointer ke `Tono R` pada kolom `Last Holder` baris `Handheld Scanner Zebra TC21 - 2`
98. Verifikasi nama lengkap pemegang `Tono Rahmat` tampil
99. Verifikasi Division pemegang `Finance` tampil
100. Verifikasi `PIC: Sinta Maharani` tampil pada hover pemegang
101. Verifikasi Employee ID pemegang `EMP-0217` tampil

### Kolom Photo pada tabel History
102. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K1
103. Verifikasi foto `laptop-dell-latitude-5420-9.jpg` tampil pada kolom `Photo` baris `Laptop Dell Latitude 5420 - 9`
104. Klik foto pada kolom `Photo` baris `Laptop Dell Latitude 5420 - 9`
105. Verifikasi pratinjau besar foto `laptop-dell-latitude-5420-9.jpg` tampil
106. Tekan `Esc`
107. Tampilkan Tabel T-DMG-02 (sub-tab History) dengan kondisi K6
108. Verifikasi avatar inisial tampil pada kolom `Photo` baris `Projector Epson EB-X06 - 5`
