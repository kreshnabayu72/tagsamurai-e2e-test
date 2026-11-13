---
id: TC-FA-FAREG-UI-031-approval-tampilan-awal
title: "Halaman Approval: header, Accordion, dan kolom tabel aset"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06d, §4.1#r14, §4.1#p31, §4.1#r109, §4.1#r110, §4.1#r111, §4.1#r112, §4.1#r113, §4.1#r114, §4.1#r115, §4.1#r116, §4.1#r117, §4.1#r118, §4.1#r119, §4.1#r120, §4.1#r121, §4.2#p1, §4.2.4#p1, §4.2.4#p2, §4.2.4#b1, §4.2.4#b2, §4.2.5#r3]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-06d: 85
  §4.1#r14: [2, 3, 4]
  §4.1#p31: [36, 38, 39]
  §4.1#r109: 41
  §4.1#r110: [34, 35]
  §4.1#r111: [42, 44]
  §4.1#r112: [46, 48]
  §4.1#r113: [50, 52]
  §4.1#r114: [53, 55, 56]
  §4.1#r115: [58, 60]
  §4.1#r116: [62, 63, 65, 66, 68, 69]
  §4.1#r117: [78, 79]
  §4.1#r118: [80, 81, 83]
  §4.1#r119: [85, 86, 89]
  §4.1#r120: 87
  §4.1#r121: [92, 94]
  §4.2#p1: [7, 8, 9, 10, 11]
  §4.2.4#p1: [2, 3, 5]
  §4.2.4#p2: [13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30, 31, 32]
  §4.2.4#b1: [62, 63, 65, 66, 68, 69, 72, 76]
  §4.2.4#b2: [46, 48]
  §4.2.5#r3: 13
anchor: [71, 75]
coverage:
  web: automated
---

# Halaman Approval: header, Accordion, dan kolom tabel aset

## Prerequisites
- Aktor: Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1 dan Gudang 2, bukan pengaju pengajuan).
- Layar awal: Halaman Approval pengajuan yang dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-031-1: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W` dengan nama lengkap `Rina Wulandari`, Total Asset `4`, Submitted At `09/11/26, 10:20`.
  - DU-031-2: aset Name `Laptop - 128`, Category `Computers` dengan path `Electronics > Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1` dengan path `PT Sinar Mandiri > Cabang A > Gudang 1`, TAG `Verified` dengan kode Tag `E28011700000020C5A3B1F01`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-031-3: aset Name `Laptop - 129`, Category `Computers` dengan path `Electronics > Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped` dengan alasan `TAG damaged`, Condition `Damaged`, Corrections `1`, Decision `Approve`, tanpa Reason.
  - DU-031-4: aset Name `Laptop - 130`, Category `Computers` dengan path `Electronics > Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified` dengan kode Tag `E28011700000020C5A3B1F02`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-031-5: aset Name `Office Desk - 12`, Category `Furniture` dengan path `Office Furniture > Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-031-6: pengajuan Registration ID `REG-20261110-00012`, Status `Waiting for Approval`, Group `Gudang 2`, Requested By `Siti N`, Total Asset `2`, Submitted At `10/11/26, 09:15`.
  - DU-031-7: aset Name `Office Desk - 21`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 2`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-031-8: aset Name `Office Desk - 22`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 2`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
- Kondisi:
  - K1: pengajuan DU-031-1 berisi aset DU-031-2 sampai DU-031-4 dalam grup Accordion `Laptop` dan DU-031-5 dalam grup Accordion `Office Desk`, dengan Decision awal dan tanpa Reason.
  - K2: pengajuan DU-031-6 berisi aset DU-031-7 dan DU-031-8 dalam grup Accordion `Office Desk`, semuanya aset Non TAG.

## Test Steps

### Halaman Approval langsung menampilkan tabel aset
1. Tampilkan Halaman Approval dengan kondisi K1
2. Verifikasi halaman langsung menampilkan tabel aset
3. Verifikasi tidak ada tab `General Information`
4. Verifikasi tabel aset memuat kolom `Decision`
5. Verifikasi kolom `Category`, `Brand`, `Model`, `Group`, `TAG`, dan `Condition` tampil sebagai teks atau Badge statis tanpa input

### Struktur halaman Approval mengikuti SectionCard
6. Tampilkan Halaman Approval dengan kondisi K1
7. Verifikasi konten Halaman Approval dibungkus `SectionCard`
8. Verifikasi Breadcrumb tampil di luar `SectionCard` mana pun
9. Verifikasi tidak ada Page Title Header terpisah di antara Breadcrumb dan `SectionCard`
10. Verifikasi `SectionCard` tidak memiliki kontrol untuk membuka atau menutup isinya
11. Verifikasi tidak ada sidebar tree Group

### Breadcrumb Halaman Approval
12. Tampilkan Halaman Approval dengan kondisi K1
13. Verifikasi Breadcrumb tampil berurutan `Approvals`, `Registration`, `Active`, `Review`

### Judul dan info pengajuan
14. Tampilkan Halaman Approval dengan kondisi K1
15. Verifikasi judul memuat Registration ID pengajuan
16. Verifikasi judul memuat ikon copy di samping Registration ID
17. Verifikasi judul memuat Badge status pengajuan
18. Verifikasi header memuat `Submitted At`
19. Verifikasi info memuat label `Group`
20. Verifikasi info memuat Badge Group `Gudang 1`
21. Verifikasi info memuat label `Requested By`
22. Verifikasi info memuat ikon user dan Nama singkat `Rina W`
23. Arahkan kursor ke Nama singkat `Rina W`
24. Verifikasi tooltip menampilkan nama lengkap `Rina Wulandari`
25. Verifikasi info memuat label `Total Asset`

### Accordion per Asset Name
26. Tampilkan Halaman Approval dengan kondisi K1
27. Verifikasi judul Accordion memuat Asset Name `Laptop`
28. Verifikasi judul Accordion `Laptop` memuat jumlah aset `3`
29. Verifikasi judul Accordion memuat Asset Name `Office Desk`
30. Verifikasi judul Accordion `Office Desk` memuat jumlah aset `1`
31. Verifikasi Accordion tidak memiliki kotak Search
32. Verifikasi Accordion tidak memiliki Filter

### Urutan aset mengikuti kolom # dan tidak dapat diurutkan
33. Tampilkan Halaman Approval dengan kondisi K1
34. Verifikasi kolom `#` pada grup `Laptop` bernilai `1`, `2`, `3` berurutan
35. Verifikasi kolom `#` pada grup `Office Desk` dimulai dari `1`
36. Verifikasi urutan baris grup `Laptop` adalah `Laptop - 128`, `Laptop - 129`, `Laptop - 130`
37. Klik header kolom `Condition` pada grup `Laptop`
38. Verifikasi urutan baris grup `Laptop` tetap `Laptop - 128`, `Laptop - 129`, `Laptop - 130`
39. Verifikasi header kolom `Condition` tidak menampilkan indikator sort

### Kolom Checkbox dan Name
40. Tampilkan Halaman Approval dengan kondisi K1
41. Verifikasi baris `Laptop - 128` memiliki checkbox pemilihan
42. Verifikasi nama `Laptop - 128` tampil sebagai link
43. Klik nama `Laptop - 128`
44. Verifikasi panel koreksi terbuka

### Kolom Category
45. Tampilkan Halaman Approval dengan kondisi K1
46. Verifikasi baris `Laptop - 128` menampilkan Badge Category `Computers`
47. Arahkan kursor ke Badge Category `Computers` pada baris `Laptop - 128`
48. Verifikasi tooltip menampilkan path lengkap `Electronics > Computers`

### Kolom Brand dan Model
49. Tampilkan Halaman Approval dengan kondisi K1
50. Verifikasi baris `Laptop - 128` menampilkan Badge Brand `Dell`
51. Arahkan kursor ke Badge Brand `Dell` pada baris `Laptop - 128`
52. Verifikasi tooltip menampilkan nama Brand penuh `Dell`
53. Verifikasi baris `Laptop - 128` menampilkan Badge Model `Latitude 5440`
54. Arahkan kursor ke Badge Model `Latitude 5440` pada baris `Laptop - 128`
55. Verifikasi tooltip menampilkan nama Model penuh `Latitude 5440`
56. Verifikasi baris `Office Desk - 12` menampilkan Badge Model `No Model`

### Kolom Group
57. Tampilkan Halaman Approval dengan kondisi K1
58. Verifikasi baris `Laptop - 128` menampilkan Badge Group `Gudang 1`
59. Arahkan kursor ke Badge Group `Gudang 1` pada baris `Laptop - 128`
60. Verifikasi tooltip menampilkan path penuh Group `PT Sinar Mandiri > Cabang A > Gudang 1`

### Kolom TAG pada pengajuan campuran
61. Tampilkan Halaman Approval dengan kondisi K1
62. Verifikasi tabel aset memuat kolom `TAG`
63. Verifikasi baris `Laptop - 128` menampilkan Badge TAG `Verified`
64. Arahkan kursor ke Badge TAG `Verified` pada baris `Laptop - 128`
65. Verifikasi tooltip menampilkan kode Tag `E28011700000020C5A3B1F01`
66. Verifikasi baris `Laptop - 129` menampilkan Badge TAG `Skipped`
67. Arahkan kursor ke Badge TAG `Skipped` pada baris `Laptop - 129`
68. Verifikasi tooltip menampilkan alasan skip `TAG damaged`
69. Verifikasi baris `Office Desk - 12` menampilkan `No tag` di kolom `TAG`

### Kolom TAG tidak tampil bila semua aset Non TAG
70. Tampilkan Halaman Approval dengan kondisi K2
71. Verifikasi tabel aset memuat baris `Office Desk - 21`
72. Verifikasi tabel aset tidak memuat kolom `TAG`

### Tag bukan field koreksi
73. Tampilkan Halaman Approval dengan kondisi K1
74. Klik nama `Laptop - 128`
75. Verifikasi panel koreksi terbuka
76. Verifikasi panel koreksi tidak memuat field `TAG`

### Kolom Condition dan Corrections
77. Tampilkan Halaman Approval dengan kondisi K1
78. Verifikasi baris `Laptop - 128` menampilkan Condition `Normal`
79. Verifikasi baris `Laptop - 129` menampilkan Condition `Damaged`
80. Verifikasi baris `Laptop - 129` menampilkan Badge Corrections `1`
81. Verifikasi baris `Laptop - 128` menampilkan `—` di kolom `Corrections`
82. Klik Badge Corrections `1` pada baris `Laptop - 129`
83. Verifikasi dialog `Corrections` terbuka

### Decision dan Reason pada keadaan awal
84. Tampilkan Halaman Approval dengan kondisi K1
85. Verifikasi Decision setiap baris aset bernilai `Approve`
86. Verifikasi Decision tidak menampilkan placeholder
87. Verifikasi Reason setiap baris aset kosong
88. Klik Decision pada baris `Laptop - 128`
89. Verifikasi pilihan Decision `Approve`, `Return to Draft`, dan `Reject` tampil

### Row option Edit membuka panel koreksi
90. Tampilkan Halaman Approval dengan kondisi K1
91. Klik row option (titik tiga) pada baris `Laptop - 128`
92. Verifikasi pilihan `Edit` tersedia
93. Klik `Edit`
94. Verifikasi panel koreksi terbuka
