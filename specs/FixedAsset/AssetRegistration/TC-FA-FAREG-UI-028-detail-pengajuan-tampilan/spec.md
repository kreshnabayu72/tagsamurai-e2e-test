---
id: TC-FA-FAREG-UI-028-detail-pengajuan-tampilan
title: "Detail pengajuan: header, mode read-only, kolom Result dan Reason, dan footer"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [T-REG-17, §4.1#r12, §4.1#b2, §4.1#b3, §4.1#b4, §4.1#b5, §4.1#b6, §4.1#p20, §4.1#r60, §4.1#r61, §4.2#p1, §4.2.1a#b1, §4.2.1a#b2, §4.2.1a#b3, §4.2.4#b2, §4.2.5#r4]
smoke: []
dependsOn: []
trace:
  T-REG-17: 18
  §4.1#r12: [76, 77, 79]
  §4.1#b2: [80, 81]
  §4.1#b3: [28, 29, 33, 34, 37, 38, 47, 48, 52, 53]
  §4.1#b4: [83, 84, 85, 97, 98, 100]
  §4.1#b5: [86, 87, 88, 89, 90, 91]
  §4.1#b6: [92, 93]
  §4.1#p20: [58, 60, 61]
  §4.1#r60: [39, 40, 41, 49, 54]
  §4.1#r61: [42, 43, 44, 55]
  §4.2#p1: [2, 3, 4, 5, 6]
  §4.2.1a#b1: [8, 9, 10, 11, 12, 13, 14, 68, 70]
  §4.2.1a#b2: [15, 72, 74]
  §4.2.1a#b3: [20, 21, 23, 24]
  §4.2.4#b2: [64, 66]
  §4.2.5#r4: 74
anchor: [27, 32]
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
- Kondisi:
  - K1: pengajuan DU-028-1 dibuka dari sub tab Waiting for Approval oleh Hadi K sebagai pengaju, dengan aset DU-028-6 sampai DU-028-9 sesuai urutan itu.
  - K2: pengajuan DU-028-1 dibuka dari sub tab Waiting for Approval oleh pengguna ber-role Total Control yang bukan pengaju, dengan aset DU-028-6 sampai DU-028-9 sesuai urutan itu.
  - K3: pengajuan DU-028-2 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-6 sampai DU-028-9 sesuai urutan itu, dan memiliki koreksi approver.
  - K4: pengajuan DU-028-3 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-6.
  - K5: pengajuan DU-028-4 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-9.
  - K6: pengajuan DU-028-5 dibuka dari sub tab History oleh Hadi K, dengan aset DU-028-6 sampai DU-028-9 sesuai urutan itu.
  - K7: pengajuan DU-028-2 dibuka dari menu Approvals, tab History, oleh pengguna ber-role Total Control, dengan aset DU-028-6 sampai DU-028-9 sesuai urutan itu.

## Test Steps

### Struktur halaman Detail pengajuan mengikuti SectionCard
1. Tampilkan Detail pengajuan dengan kondisi K1
2. Verifikasi konten Detail pengajuan dibungkus `SectionCard`
3. Verifikasi Breadcrumb tampil di luar `SectionCard` mana pun
4. Verifikasi tidak ada Page Title Header terpisah di antara Breadcrumb dan `SectionCard`
5. Verifikasi `SectionCard` tidak memiliki kontrol untuk membuka atau menutup isinya
6. Verifikasi tidak ada sidebar tree Group

### Header dan Breadcrumb pengajuan Waiting for Approval
7. Tampilkan Detail pengajuan dengan kondisi K1
8. Verifikasi header memuat Registration ID pengajuan
9. Verifikasi header memuat ikon copy di samping Registration ID
10. Verifikasi header memuat Badge status pengajuan
11. Verifikasi header memuat `Submitted At`
12. Verifikasi header memuat label `Group`
13. Verifikasi header memuat label `Requested By`
14. Verifikasi header memuat label `Total Asset`
15. Verifikasi Breadcrumb tampil berurutan `Assets`, `Registration`, `Waiting for Approval`, `Detail`

### Salin Registration ID dari header
16. Tampilkan Detail pengajuan dengan kondisi K1
17. Klik ikon copy di samping Registration ID
18. Verifikasi toast sukses `Success, Registration ID has been copied.`

### Footer untuk pengaju pengajuan Waiting for Approval
19. Tampilkan Detail pengajuan dengan kondisi K1
20. Verifikasi footer memuat `[Close]`
21. Verifikasi footer memuat `[Cancel Registration]`

### Footer untuk bukan pengaju pengajuan Waiting for Approval
22. Tampilkan Detail pengajuan dengan kondisi K2
23. Verifikasi footer memuat `[Close]`
24. Verifikasi `[Cancel Registration]` tidak dirender

### Kolom Result dan Reason tidak ada pada pengajuan Waiting for Approval
25. Tampilkan Detail pengajuan dengan kondisi K1
26. Klik tab `Asset`
27. Verifikasi tabel aset memuat baris `Laptop - 128`
28. Verifikasi tabel aset tidak memuat kolom `Result`
29. Verifikasi tabel aset tidak memuat kolom `Reason`

### Kolom Result dan Reason tidak ada pada pengajuan Canceled
30. Tampilkan Detail pengajuan dengan kondisi K6
31. Klik tab `Asset`
32. Verifikasi tabel aset memuat baris `Laptop - 128`
33. Verifikasi tabel aset tidak memuat kolom `Result`
34. Verifikasi tabel aset tidak memuat kolom `Reason`

### Kolom Result dan Reason pada pengajuan Partially Approved
35. Tampilkan Detail pengajuan dengan kondisi K3
36. Klik tab `Asset`
37. Verifikasi tabel aset memuat kolom `Result`
38. Verifikasi tabel aset memuat kolom `Reason`
39. Verifikasi baris `Laptop - 128` menampilkan Badge Result `Approved`
40. Verifikasi baris `Laptop - 130` menampilkan Badge Result `Returned`
41. Verifikasi baris `Office Desk - 12` menampilkan Badge Result `Rejected`
42. Verifikasi Reason `Scratch on the casing is minor` pada baris `Laptop - 129` terlihat langsung tanpa hover
43. Verifikasi Reason `Photo is missing` pada baris `Laptop - 130` terlihat langsung tanpa hover
44. Verifikasi Reason pada baris `Laptop - 128` kosong

### Kolom Result dan Reason pada pengajuan Approved
45. Tampilkan Detail pengajuan dengan kondisi K4
46. Klik tab `Asset`
47. Verifikasi tabel aset memuat kolom `Result`
48. Verifikasi tabel aset memuat kolom `Reason`
49. Verifikasi baris `Laptop - 128` menampilkan Badge Result `Approved`

### Kolom Result dan Reason pada pengajuan Rejected
50. Tampilkan Detail pengajuan dengan kondisi K5
51. Klik tab `Asset`
52. Verifikasi tabel aset memuat kolom `Result`
53. Verifikasi tabel aset memuat kolom `Reason`
54. Verifikasi baris `Office Desk - 12` menampilkan Badge Result `Rejected`
55. Verifikasi Reason `Duplicate entry` pada baris `Office Desk - 12` terlihat langsung tanpa hover

### Tabel aset tidak dapat diurutkan
56. Tampilkan Detail pengajuan dengan kondisi K3
57. Klik tab `Asset`
58. Verifikasi urutan baris tabel aset `Laptop - 128`, `Laptop - 129`, `Laptop - 130`, `Office Desk - 12`
59. Klik header kolom `Result`
60. Verifikasi urutan baris tabel aset tetap `Laptop - 128`, `Laptop - 129`, `Laptop - 130`, `Office Desk - 12`
61. Verifikasi header kolom `Result` tidak menampilkan indikator sort

### Category tampil sebagai Badge node terbawah dengan tooltip path
62. Tampilkan Detail pengajuan dengan kondisi K3
63. Klik tab `Asset`
64. Verifikasi baris `Laptop - 128` menampilkan Badge Category `Computers`
65. Arahkan kursor ke Badge Category `Computers` pada baris `Laptop - 128`
66. Verifikasi tooltip menampilkan path lengkap `Electronics > Computers`

### Ikon Changes by approver membuka dialog Approver Corrections
67. Tampilkan Detail pengajuan dengan kondisi K3
68. Verifikasi header memuat ikon `Changes by approver`
69. Klik ikon `Changes by approver`
70. Verifikasi dialog `Approver Corrections` terbuka

### Breadcrumb Detail dari sub tab History
71. Tampilkan Detail pengajuan dengan kondisi K3
72. Verifikasi Breadcrumb tampil berurutan `Assets`, `Registration`, `History`, `Detail`

### Breadcrumb Detail dari menu Approvals
73. Tampilkan Detail pengajuan dengan kondisi K7
74. Verifikasi Breadcrumb tampil berurutan `Approvals`, `Registration`, `History`, `Detail`

### Mode read-only Detail pengajuan
75. Tampilkan Detail pengajuan dengan kondisi K3
76. Verifikasi tab `General Information` tampil
77. Verifikasi tab `Asset` tampil
78. Klik tab `General Information`
79. Verifikasi field `Group` tidak diulang di tab `General Information`
80. Verifikasi semua data tampil sebagai teks atau Badge statis
81. Verifikasi tidak ada field disabled

### Detail tanpa kontrol pengubah data dan tanpa kontrol keputusan
82. Tampilkan Detail pengajuan dengan kondisi K3
83. Verifikasi ikon copy di samping Registration ID tampil
84. Verifikasi footer memuat `[Close]`
85. Verifikasi `[Cancel Registration]` tidak dirender pada pengajuan yang sudah di History
86. Verifikasi tidak ada `[Save draft]`
87. Verifikasi tidak ada `[Submit]`
88. Verifikasi tidak ada kartu filter `All`, `Needs data`, dan `Ready`
89. Verifikasi tidak ada kolom `Status` Ready pada tabel aset
90. Verifikasi tidak ada badge `Complete` dan `Incomplete`
91. Verifikasi tidak ada kontrol column visibility
92. Verifikasi tidak ada kontrol keputusan `Approve`, `Return to Draft`, dan `Reject` per aset
93. Verifikasi tidak ada field koreksi approver

### Panel unit dibuka dari nama aset dan ditutup dengan Close
94. Tampilkan Detail pengajuan dengan kondisi K3
95. Klik tab `Asset`
96. Klik nama aset `Laptop - 128`
97. Verifikasi panel unit aset tampil
98. Verifikasi panel memuat tombol `Close`
99. Klik `Close` pada panel
100. Verifikasi panel unit aset tertutup
