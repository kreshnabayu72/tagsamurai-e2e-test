---
id: TC-FA-ASSIGN-UI-105-dialog-select-asset
title: "Dialog Select Asset: pilih aset dan tombol Select"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-04, "EB-TBL-9@select-asset", "EB-TBL-3@kolom-label-select-asset"]
smoke: []
dependsOn: []
trace:
  T-ASG-04: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 26, 28, 29, 30, 31, 33, 35, 36, 38, 47, 49, 52, 56, 68, 70, 72, 74, 76, 77, 79, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 94, 97, 99, 100]
  "EB-TBL-9@select-asset": [40, 42, 43]
  "EB-TBL-3@kolom-label-select-asset": [57, 58, 59, 60, 61, 63, 65]
anchor: []
coverage:
  web: automated
---
# Dialog Select Asset: pilih aset dan tombol Select

## Prerequisites
- Aktor: Asset Admin dengan cakupan Group `Head Office` dan `Branch Surabaya`.
- Layar awal: form Assignment Request dengan dialog Select Asset dibuka dari `[+ Asset]`.
- Komponen: Dialog Select Asset
- Data:
  - DU-105-1: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Brand `—`, Model/Type `—`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`, tanpa Label.
  - DU-105-2: Aset `Laptop Dell Latitude 5420 - 11`, Asset ID `LPT-2026-0011`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`, satu Label `Inventaris Kantor`.
  - DU-105-3: Aset `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Group `Branch Surabaya`, Approval Rule `Needs approval`, Confirmation Rule `Yes`, dua Label dengan urutan input `Pool Surabaya` lalu `Kendaraan Operasional`.
  - DU-105-4: Aset `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Group `Head Office`, Approval Rule `Needs approval (all must approve)`, Confirmation Rule `Yes`, empat Label dengan urutan input `Proyek Tambang`, `Alat Berat`, `Sewa Jangka Panjang`, `Kritis`. Chip yang diharapkan `+2 more`, dari 4 Label dikurangi 2 badge.
  - DU-105-5: Aset `Printer HP M404 - 3`, Asset ID `PRN-2026-0003`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `No`; tipe Division tidak diizinkan untuk aset ini.
  - DU-105-6: Aset `Laptop Dell Latitude 5420 - 12`, Asset ID `LPT-2026-0012`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-105-7: Assignee karyawan `Budi Santoso` (budi.s@client.com), Position `Warehouse Staff`, Division `Logistics`, Status `Active`.
  - DU-105-8: Assignee Division `Finance`.
  - DU-105-9: Aset `Laptop Dell Latitude 5420 - 13`, Asset ID `LPT-2026-0013`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`, memegang seluruh Label master data entitas, yaitu `Alat Berat`, `Inventaris Kantor`, dan `Kritis`.
  - DU-105-10: Aset `Handheld Zebra TC21 - 1`, Asset ID `HHT-2026-0001`, Brand `Zebra Technologies`, Model/Type `Handheld Reader Pro`, Group `Floor 1` dengan hierarki lengkap `Head Office > Floor 1`, Approval Rule `No approval`, Confirmation Rule `Yes`; Need recipient confirmation efektif aktif, bukti foto yang diminta hanya Photo at start.
  - DU-105-11: Aset `Forklift Toyota - 2`, Asset ID `FRK-2026-0002`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`; Allowed assignee efektif hanya Division, sehingga untuk Assignee karyawan Eligibility `Not ready` dengan alasan `This asset can't be assigned to an employee.`.
- Kondisi:
  - K1: Assignee belum dipilih; daftar berisi DU-105-1 sampai DU-105-5; kolom Label tidak ditampilkan.
  - K2: Assignee DU-105-7 terpilih; daftar berisi DU-105-1 dan DU-105-3; keterangan yang diharapkan `Available assets in your groups. Eligibility is checked for Budi Santoso.`, dari Assignee `Budi Santoso`.
  - K3: Assignee DU-105-8 terpilih; daftar berisi DU-105-1 dan DU-105-5; keterangan yang diharapkan `Available assets in your groups. Eligibility is checked for Finance.`, dari Assignee `Finance`; alasan yang diharapkan untuk DU-105-5 `This asset can't be assigned to a division.`.
  - K4: Assignee DU-105-7 terpilih dan sudah memegang aset sebanyak Max assets per assignee efektif; daftar berisi DU-105-6.
  - K5: Assignee belum dipilih; daftar berisi DU-105-1 sampai DU-105-4; kolom Label tersembunyi di Setup Column.
  - K6: Assignee belum dipilih; daftar berisi DU-105-1 sampai DU-105-4; tidak ada baris tercentang.
  - K7: Assignee belum dipilih; kolom Label tampil; master data Label entitas berisi tiga Label `Alat Berat`, `Inventaris Kantor`, dan `Kritis`; daftar berisi DU-105-9; badge yang diharapkan `All Labels`, dari pola `All [Entitas]` dengan entitas Label.
  - K8: Assignee belum dipilih; daftar berisi DU-105-10.
  - K9: Assignee DU-105-7 terpilih; daftar berisi DU-105-11.

## Test Steps

### Keterangan tanpa Assignee, toolbar, kolom, dan footer
1. Tampilkan Dialog Select Asset dengan kondisi K1
2. Verifikasi judul dialog `Select Asset`
3. Verifikasi keterangan di bawah judul memuat `Available assets in your groups.`
4. Verifikasi keterangan tidak memuat kalimat kedua `Eligibility is checked for`
5. Verifikasi toolbar memuat Search by Scan, Search, dan Filter
6. Verifikasi kotak Search memuat placeholder `Search asset name or ID...`
7. Verifikasi kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Approval Rule`, `Confirmation Rule`, dan `Eligibility` tampil
8. Verifikasi kolom `TAG`, `Category`, dan `Label` tidak tampil
9. Verifikasi kolom `Max Duration` tidak tampil
10. Verifikasi dialog Select Asset memuat tombol `[Cancel]` dan `[Select]`

### Isi sel baris aset
11. Tampilkan Dialog Select Asset dengan kondisi K1
12. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Asset ID `LPT-2026-0010`
13. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Brand `—`
14. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Model/Type `—`
15. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Group `Head Office`
16. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Approval Rule `No approval`
17. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Confirmation Rule `Yes`
18. Verifikasi baris `Toyota Avanza - 6` menampilkan Approval Rule `Needs approval`
19. Verifikasi baris `Excavator PC200 - 4` menampilkan Approval Rule `Needs approval (all must approve)`
20. Verifikasi baris `Printer HP M404 - 3` menampilkan Confirmation Rule `No`
21. Verifikasi setiap baris menampilkan Eligibility `Ready` karena Assignee belum dipilih

### Assignee karyawan terpilih menyebut namanya di keterangan
22. Tampilkan Dialog Select Asset dengan kondisi K2
23. Verifikasi keterangan di bawah judul memuat `Available assets in your groups. Eligibility is checked for Budi Santoso.`
24. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Eligibility `Ready`
25. Centang baris `Laptop Dell Latitude 5420 - 10`
26. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tercentang

### Tipe Division tidak diizinkan: baris Not ready tidak bisa dicentang
27. Tampilkan Dialog Select Asset dengan kondisi K3
28. Verifikasi keterangan di bawah judul memuat `Available assets in your groups. Eligibility is checked for Finance.`
29. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Eligibility `Ready`
30. Verifikasi baris `Printer HP M404 - 3` menampilkan Eligibility `Not ready`
31. Verifikasi checkbox baris `Printer HP M404 - 3` disabled dan alasan `This asset can't be assigned to a division.` tersampaikan padanya
32. Klik checkbox baris `Printer HP M404 - 3`
33. Verifikasi baris `Printer HP M404 - 3` tidak tercentang

### Max assets per assignee tercapai: baris Not ready tidak bisa dicentang
34. Tampilkan Dialog Select Asset dengan kondisi K4
35. Verifikasi baris `Laptop Dell Latitude 5420 - 12` menampilkan Eligibility `Not ready`
36. Verifikasi checkbox baris `Laptop Dell Latitude 5420 - 12` disabled dan alasan batas Max assets per assignee tersampaikan padanya
37. Klik checkbox baris `Laptop Dell Latitude 5420 - 12`
38. Verifikasi baris `Laptop Dell Latitude 5420 - 12` tidak tercentang

### Select tanpa pilihan menampilkan error inline
39. Tampilkan Dialog Select Asset dengan kondisi K6
40. Verifikasi `[Select]` pada dialog Select Asset enabled
41. Klik `[Select]`
42. Verifikasi pesan error inline `You must pick an asset` tampil di atas tombol footer
43. Verifikasi dialog Select Asset tetap terbuka karena pilihan tidak dikirim

### Pilih aset lintas Group lalu Select
44. Tampilkan Dialog Select Asset dengan kondisi K6
45. Centang baris `Laptop Dell Latitude 5420 - 10`
46. Centang baris `Toyota Avanza - 6`
47. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan `Toyota Avanza - 6` tercentang walau Group-nya berbeda
48. Klik `[Select]`
49. Verifikasi dialog Select Asset tertutup

### Cancel menutup dialog
50. Tampilkan Dialog Select Asset dengan kondisi K6
51. Klik `[Cancel]`
52. Verifikasi dialog Select Asset tertutup

### Kolom Label: nol, satu, dua, dan lebih dari dua Label
53. Tampilkan Dialog Select Asset dengan kondisi K5
54. Buka Setup Column
55. Centang `Label` pada Setup Column
56. Verifikasi kolom `Label` tampil
57. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan `—` pada kolom `Label`
58. Verifikasi baris `Laptop Dell Latitude 5420 - 11` menampilkan badge `Inventaris Kantor` pada kolom `Label`
59. Verifikasi baris `Toyota Avanza - 6` menampilkan badge `Kendaraan Operasional` lalu `Pool Surabaya` pada kolom `Label`
60. Verifikasi baris `Excavator PC200 - 4` menampilkan badge `Alat Berat` lalu `Kritis` pada kolom `Label`
61. Verifikasi baris `Excavator PC200 - 4` menampilkan chip `+2 more`[^drift-1]
62. Klik chip `+2 more` pada baris `Excavator PC200 - 4`
63. Verifikasi popover memuat semua Label baris itu, yaitu `Alat Berat`, `Kritis`, `Proyek Tambang`, dan `Sewa Jangka Panjang`


### Kolom Label: seluruh Label master tampil sebagai satu badge
64. Tampilkan Dialog Select Asset dengan kondisi K7
65. Verifikasi baris `Laptop Dell Latitude 5420 - 13` menampilkan badge tunggal `All Labels` pada kolom `Label`

### Hover kolom Brand, Model/Type, Group, dan Approval Rule
66. Tampilkan Dialog Select Asset dengan kondisi K8
67. Arahkan kursor ke badge Brand pada baris `Handheld Zebra TC21 - 1`
68. Verifikasi hover Brand menyampaikan nama penuh `Zebra Technologies`
69. Arahkan kursor ke badge Model/Type pada baris `Handheld Zebra TC21 - 1`
70. Verifikasi hover Model/Type menyampaikan nama penuh `Handheld Reader Pro`
71. Arahkan kursor ke badge Group pada baris `Handheld Zebra TC21 - 1`
72. Verifikasi hover Group menyampaikan hierarki lengkap `Head Office > Floor 1`
73. Arahkan kursor ke Approval Rule pada baris `Handheld Zebra TC21 - 1`
74. Verifikasi hover Approval Rule menyampaikan Need recipient confirmation dan bukti foto yang diminta menurut aturan efektif aset itu

### Tipe Employee tidak diizinkan: baris Not ready tidak bisa dicentang
75. Tampilkan Dialog Select Asset dengan kondisi K9
76. Verifikasi baris `Forklift Toyota - 2` menampilkan Eligibility `Not ready`
77. Verifikasi checkbox baris `Forklift Toyota - 2` disabled dan alasan `This asset can't be assigned to an employee.` tersampaikan padanya
78. Klik checkbox baris `Forklift Toyota - 2`
79. Verifikasi baris `Forklift Toyota - 2` tidak tercentang

### Filter Panel memuat field menurut kolom yang dapat difilter
80. Tampilkan Dialog Select Asset dengan kondisi K1
81. Klik ikon Filter
82. Verifikasi Filter Panel dialog Select Asset memuat field `Name` dengan placeholder `All asset names`
83. Verifikasi Filter Panel dialog Select Asset memuat field `Brand` dengan placeholder `All brands`
84. Verifikasi Filter Panel dialog Select Asset memuat field `Model/Type` dengan placeholder `All models`
85. Verifikasi Filter Panel dialog Select Asset memuat field `Group` dengan placeholder `All groups`
86. Verifikasi Filter Panel dialog Select Asset memuat field `TAG` dengan placeholder `All tags`
87. Verifikasi Filter Panel dialog Select Asset memuat field `Category` dengan placeholder `All categories`
88. Verifikasi Filter Panel dialog Select Asset memuat field `Approval Rule` dengan placeholder `All approval rules`
89. Verifikasi Filter Panel dialog Select Asset memuat field `Confirmation Rule` dengan placeholder `All confirmation rules`
90. Verifikasi Filter Panel dialog Select Asset memuat field `Label` dengan placeholder `All labels`
91. Verifikasi Filter Panel dialog Select Asset memuat field `Eligibility` dengan placeholder `All eligibility`

### Kolom yang dapat diurutkan
92. Tampilkan Dialog Select Asset dengan kondisi K1
93. Verifikasi header kolom `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Approval Rule`, `Confirmation Rule`, dan `Eligibility` dapat diurutkan
94. Verifikasi header kolom `Photo` tidak dapat diurutkan

### Setup Column: kolom yang dapat disembunyikan
95. Tampilkan Dialog Select Asset dengan kondisi K1
96. Buka Setup Column
97. Verifikasi kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Approval Rule`, `Confirmation Rule`, dan `Eligibility` masing-masing dapat disembunyikan lewat Setup Column
98. Hilangkan centang `Brand` pada Setup Column
99. Verifikasi kolom `Name` tetap tampil pada dialog Select Asset
100. Verifikasi kolom `Brand` tidak tampil

[^drift-1]: Drift PRD vs foundation. PRD §4.1d (T-ASG-04 Setup Column, baris Label): format `1–2 badge lalu +N`. foundation `prd-conventions.md` §21.1: lebih dari 2 item tampil 2 badge dan chip `+N more`, N = total − 2, klik chip membuka popover daftar semua. Diasersi: foundation, karena kolom multi-badge adalah pola bersama (SB-4).
