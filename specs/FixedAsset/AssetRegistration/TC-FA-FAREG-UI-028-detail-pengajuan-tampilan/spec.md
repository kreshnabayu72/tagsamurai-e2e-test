---
id: TC-FA-FAREG-UI-028-detail-pengajuan-tampilan
title: "Detail pengajuan: header, mode read-only, kolom Result dan Reason, dan footer"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-REG-17, §4.1#r12, §4.1#b2, §4.1#b3, §4.1#b4, §4.1#b5, §4.1#b6, §4.1#p20, §4.1#r60, §4.1#r61, §4.2#p1, §4.2.1a#b1, §4.2.1a#b2, §4.2.1a#b3, §4.2.4#b2, §4.2.5#r4]
smoke: []
dependsOn: []
trace:
  T-REG-17: 15
  §4.1#r12: [73, 74, 76]
  §4.1#b2: [77, 78]
  §4.1#b3: [25, 26, 30, 31, 34, 35, 44, 45, 49, 50]
  §4.1#b4: [80, 81, 82, 94, 95, 97]
  §4.1#b5: [83, 84, 85, 86, 87, 88]
  §4.1#b6: [89, 90]
  §4.1#p20: [55, 57, 58]
  §4.1#r60: [36, 37, 38, 46, 51]
  §4.1#r61: [39, 40, 41, 52]
  §4.2#p1: 3
  §4.2.1a#b1: [5, 6, 7, 8, 9, 10, 11, 65, 67, 100, 103, 106, 109]
  §4.2.1a#b2: [12, 69, 71]
  §4.2.1a#b3: [17, 18, 20, 21]
  §4.2.4#b2: [61, 63]
  §4.2.5#r4: 71
anchor: [2, 24, 29, 99, 102, 105, 108]
coverage:
  web: automated
---

# Detail pengajuan: header, mode read-only, kolom Result dan Reason, dan footer

## Prerequisites
- Aktor: Hadi K (pengaju pengajuan, role Manage asset & TAG, cakupan Group terkelola), dan pengguna ber-role Total Control (cakupan seluruh client) yang bukan pengaju pengajuan.
- Layar awal: halaman Detail pengajuan, dimuat dengan kondisi tiap blok langkah.
- Komponen: Detail pengajuan
- Data:
  - DU-028-1: pengajuan Registration ID `REG-20261108-00011`, Status `Waiting for Approval`, Group `Kantor Pusat`, Requested By `Hadi K`, Total Asset `4`, Submitted At `08/11/26, 14:02`.
  - DU-028-2: pengajuan Registration ID `REG-20261103-00004`, Status `Partially Approved`, Group `Kantor Pusat`, Requested By `Hadi K`, Total Asset `4`, Submitted At `03/11/26, 10:12`.
  - DU-028-3: pengajuan Registration ID `REG-20261104-00009`, Status `Approved`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `1`, Submitted At `04/11/26, 15:30`.
  - DU-028-4: pengajuan Registration ID `REG-20261102-00001`, Status `Rejected`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `1`, Submitted At `02/11/26, 09:48`.
  - DU-028-5: pengajuan Registration ID `REG-20261101-00006`, Status `Canceled`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `4`, Submitted At `01/11/26, 17:05`.
  - DU-028-6: aset Name `Laptop - 128`, Category `Computers` dengan path `Electronics > Computers`, Result `Approved`, tanpa Reason.
  - DU-028-7: aset Name `Laptop - 129`, Category `Computers` dengan path `Electronics > Computers`, Result `Approved`, Reason `Scratch on the casing is minor`.
  - DU-028-8: aset Name `Laptop - 130`, Category `Computers` dengan path `Electronics > Computers`, Result `Returned`, Reason `Photo is missing`.
  - DU-028-9: aset Name `Office Desk - 12`, Category `Furniture` dengan path `Office Furniture > Furniture`, Result `Rejected`, Reason `Duplicate entry`.
  - DU-028-10: aset Name `Laptop - 128`, Category `Computers` dengan path `Electronics > Computers`, tanpa Result dan tanpa Reason (pengajuan belum diputuskan atau dibatalkan).
  - DU-028-11: aset Name `Laptop - 129`, Category `Computers` dengan path `Electronics > Computers`, tanpa Result dan tanpa Reason.
  - DU-028-12: aset Name `Laptop - 130`, Category `Computers` dengan path `Electronics > Computers`, tanpa Result dan tanpa Reason.
  - DU-028-13: aset Name `Office Desk - 12`, Category `Furniture` dengan path `Office Furniture > Furniture`, tanpa Result dan tanpa Reason.
- Kondisi:
  - K1: pengajuan DU-028-1 dibuka dari sub tab Waiting for Approval oleh Hadi K sebagai pengaju, dengan aset DU-028-10 sampai DU-028-13 sesuai urutan itu.
  - K2: pengajuan DU-028-1 dibuka dari sub tab Waiting for Approval oleh pengguna ber-role Total Control yang bukan pengaju, dengan aset DU-028-10 sampai DU-028-13 sesuai urutan itu.
  - K3: pengajuan DU-028-2 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-6 sampai DU-028-9 sesuai urutan itu, dan memiliki koreksi approver.
  - K4: pengajuan DU-028-3 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-6, tanpa koreksi approver.
  - K5: pengajuan DU-028-4 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-9.
  - K6: pengajuan DU-028-5 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-10 sampai DU-028-13 sesuai urutan itu.
  - K7: pengajuan DU-028-2 dibuka dari menu Approvals, tab History, oleh pengguna ber-role Total Control, dengan aset DU-028-6 sampai DU-028-9 sesuai urutan itu.

## Test Steps

### Halaman Detail pengajuan tanpa sidebar tree Group
1. Tampilkan Detail pengajuan dengan kondisi K1
2. Verifikasi header memuat Registration ID `REG-20261108-00011`
3. Verifikasi tidak ada sidebar tree Group

### Header dan Breadcrumb pengajuan Waiting for Approval
4. Tampilkan Detail pengajuan dengan kondisi K1
5. Verifikasi header memuat Registration ID `REG-20261108-00011`
6. Verifikasi header memuat ikon copy di samping Registration ID
7. Verifikasi header memuat Badge status `Waiting for Approval`
8. Verifikasi header memuat `Submitted At` `08/11/26, 14:02`
9. Verifikasi header memuat `Group` `Kantor Pusat`
10. Verifikasi header memuat `Requested By` `Hadi K`
11. Verifikasi header memuat `Total Asset` `4`
12. Verifikasi Breadcrumb tampil berurutan `Assets`, `Registration`, `Waiting for Approval`, `Detail`

### Salin Registration ID dari header
13. Tampilkan Detail pengajuan dengan kondisi K1
14. Klik ikon copy di samping Registration ID
15. Verifikasi toast sukses `Success, Registration ID has been copied.`

### Footer untuk pengaju pengajuan Waiting for Approval
16. Tampilkan Detail pengajuan dengan kondisi K1
17. Verifikasi footer memuat `[Close]`
18. Verifikasi footer memuat `[Cancel Registration]`

### Footer untuk bukan pengaju pengajuan Waiting for Approval
19. Tampilkan Detail pengajuan dengan kondisi K2
20. Verifikasi footer memuat `[Close]`
21. Verifikasi `[Cancel Registration]` tidak dirender

### Kolom Result dan Reason tidak ada pada pengajuan Waiting for Approval
22. Tampilkan Detail pengajuan dengan kondisi K1
23. Klik tab `Asset`
24. Verifikasi tabel aset memuat baris `Laptop - 128`
25. Verifikasi tabel aset tidak memuat kolom `Result`
26. Verifikasi tabel aset tidak memuat kolom `Reason`

### Kolom Result dan Reason tidak ada pada pengajuan Canceled
27. Tampilkan Detail pengajuan dengan kondisi K6
28. Klik tab `Asset`
29. Verifikasi tabel aset memuat baris `Laptop - 128`
30. Verifikasi tabel aset tidak memuat kolom `Result`
31. Verifikasi tabel aset tidak memuat kolom `Reason`

### Kolom Result dan Reason pada pengajuan Partially Approved
32. Tampilkan Detail pengajuan dengan kondisi K3
33. Klik tab `Asset`
34. Verifikasi tabel aset memuat kolom `Result`
35. Verifikasi tabel aset memuat kolom `Reason`
36. Verifikasi baris `Laptop - 128` menampilkan Badge Result `Approved`
37. Verifikasi baris `Laptop - 130` menampilkan Badge Result `Returned`
38. Verifikasi baris `Office Desk - 12` menampilkan Badge Result `Rejected`
39. Verifikasi Reason `Scratch on the casing is minor` pada baris `Laptop - 129` terlihat langsung tanpa hover
40. Verifikasi Reason `Photo is missing` pada baris `Laptop - 130` terlihat langsung tanpa hover
41. Verifikasi Reason pada baris `Laptop - 128` kosong

### Kolom Result dan Reason pada pengajuan Approved
42. Tampilkan Detail pengajuan dengan kondisi K4
43. Klik tab `Asset`
44. Verifikasi tabel aset memuat kolom `Result`
45. Verifikasi tabel aset memuat kolom `Reason`
46. Verifikasi baris `Laptop - 128` menampilkan Badge Result `Approved`

### Kolom Result dan Reason pada pengajuan Rejected
47. Tampilkan Detail pengajuan dengan kondisi K5
48. Klik tab `Asset`
49. Verifikasi tabel aset memuat kolom `Result`
50. Verifikasi tabel aset memuat kolom `Reason`
51. Verifikasi baris `Office Desk - 12` menampilkan Badge Result `Rejected`
52. Verifikasi Reason `Duplicate entry` pada baris `Office Desk - 12` terlihat langsung tanpa hover

### Tabel aset tidak dapat diurutkan
53. Tampilkan Detail pengajuan dengan kondisi K3
54. Klik tab `Asset`
55. Verifikasi urutan baris tabel aset `Laptop - 128`, `Laptop - 129`, `Laptop - 130`, `Office Desk - 12`
56. Klik header kolom `Result`
57. Verifikasi urutan baris tabel aset tetap `Laptop - 128`, `Laptop - 129`, `Laptop - 130`, `Office Desk - 12`
58. Verifikasi header kolom `Result` tidak menampilkan indikator sort

### Category tampil sebagai Badge node terbawah dengan tooltip path
59. Tampilkan Detail pengajuan dengan kondisi K3
60. Klik tab `Asset`
61. Verifikasi baris `Laptop - 128` menampilkan Badge Category `Computers`
62. Arahkan kursor ke Badge Category `Computers` pada baris `Laptop - 128`
63. Verifikasi tooltip menampilkan path lengkap `Electronics > Computers`

### Ikon Changes by approver membuka dialog Approver Corrections
64. Tampilkan Detail pengajuan dengan kondisi K3
65. Verifikasi header memuat ikon `Changes by approver`
66. Klik ikon `Changes by approver`
67. Verifikasi dialog `Approver Corrections` terbuka

### Breadcrumb Detail dari sub tab History
68. Tampilkan Detail pengajuan dengan kondisi K3
69. Verifikasi Breadcrumb tampil berurutan `Assets`, `Registration`, `History`, `Detail`

### Breadcrumb Detail dari menu Approvals
70. Tampilkan Detail pengajuan dengan kondisi K7
71. Verifikasi Breadcrumb tampil berurutan `Approvals`, `Registration`, `History`, `Detail`

### Mode read-only Detail pengajuan
72. Tampilkan Detail pengajuan dengan kondisi K3
73. Verifikasi tab `General Information` tampil
74. Verifikasi tab `Asset` tampil
75. Klik tab `General Information`
76. Verifikasi field `Group` tidak diulang di tab `General Information`
77. Verifikasi semua data tampil sebagai teks atau Badge statis
78. Verifikasi tidak ada field disabled

### Detail tanpa kontrol pengubah data dan tanpa kontrol keputusan
79. Tampilkan Detail pengajuan dengan kondisi K3
80. Verifikasi ikon copy di samping Registration ID tampil
81. Verifikasi footer memuat `[Close]`
82. Verifikasi `[Cancel Registration]` tidak dirender pada pengajuan yang sudah di History
83. Verifikasi tidak ada `[Save draft]`
84. Verifikasi tidak ada `[Submit]`
85. Verifikasi tidak ada kartu filter `All`, `Needs data`, dan `Ready`
86. Verifikasi tidak ada kolom `Status` Ready pada tabel aset
87. Verifikasi tidak ada badge `Complete` dan `Incomplete`
88. Verifikasi tidak ada kontrol column visibility
89. Verifikasi tidak ada kontrol keputusan `Approve`, `Return to Draft`, dan `Reject` per aset
90. Verifikasi tidak ada field koreksi approver

### Panel unit dibuka dari nama aset dan ditutup dengan Close
91. Tampilkan Detail pengajuan dengan kondisi K3
92. Klik tab `Asset`
93. Klik nama aset `Laptop - 128`
94. Verifikasi panel unit aset tampil
95. Verifikasi panel memuat tombol `Close`
96. Klik `Close` pada panel
97. Verifikasi panel unit aset tertutup

### Ikon Changes by approver tidak tampil pada pengajuan Waiting for Approval
98. Tampilkan Detail pengajuan dengan kondisi K1
99. Verifikasi Badge status di header `Waiting for Approval`
100. Verifikasi ikon `Changes by approver` tidak tampil di header

### Ikon Changes by approver tidak tampil pada pengajuan Rejected
101. Tampilkan Detail pengajuan dengan kondisi K5
102. Verifikasi Badge status di header `Rejected`
103. Verifikasi ikon `Changes by approver` tidak tampil di header

### Ikon Changes by approver tidak tampil pada pengajuan Canceled
104. Tampilkan Detail pengajuan dengan kondisi K6
105. Verifikasi Badge status di header `Canceled`
106. Verifikasi ikon `Changes by approver` tidak tampil di header

### Ikon Changes by approver tidak tampil pada pengajuan Approved tanpa koreksi approver
107. Tampilkan Detail pengajuan dengan kondisi K4
108. Verifikasi Badge status di header `Approved`
109. Verifikasi ikon `Changes by approver` tidak tampil di header
