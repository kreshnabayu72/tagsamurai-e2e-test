---
id: TC-FA-ASSIGN-E2E-001-daftar-transactions-tampilan
title: "Daftar Transactions: kolom, badge status header, aksi baris, dan tab awal"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-01, "§4.1#r1", "§4.1#p2", "§4.1#p4", "§4.1#p5", "§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r26", "§4.1#r27", "§4.1#r28", "§5#r1", "§9.5#r1", "§9.5#r6", "§4.4#r19"]
smoke: []
dependsOn: []
trace:
  T-ASG-01: [6, 7, 8, 9, 10, 11, 14, 17, 18, 20, 21, 23, 24, 25, 27, 29, 30, 31, 33, 35, 36, 38, 42, 43, 44, 46, 51, 53, 65]
  "§4.1#r1": [3, 6]
  "§4.1#p2": [1, 6, 51, 53]
  "§4.1#p4": [9, 12, 13]
  "§4.1#p5": [15, 21, 23, 27, 29]
  "§4.1#r22": 13
  "§4.1#r23": 12
  "§4.1#r24": [9, 11]
  "§4.1#r25": 17
  "§4.1#r26": 10
  "§4.1#r27": 17
  "§4.1#r28": 17
  "§5#r1": [3, 57]
  "§9.5#r1": 2
  "§9.5#r6": 8
  "§4.4#r19": [40, 56, 60, 62, 63, 69, 71, 74, 75, 76, 78, 79, 80, 83, 87, 89, 91, 92, 97, 99]
anchor: [5, 49, 88]
coverage:
  web: automated
---

# Daftar Transactions: kolom, badge status header, aksi baris, dan tab awal

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-001-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-001-2: Group `Head Office {runId}` sebagai Group induk paling atas dan Group `Branch Surabaya {runId}` sebagai anak langsung `Head Office {runId}`.
  - DU-001-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}` dan `Branch Surabaya {runId}`; ia pengaju semua ASG DU-001-9 sampai DU-001-13.
  - DU-001-4: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-001-5: User `Sari Dewi {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Sari D`, dari `Sari Dewi {runId}`.
  - DU-001-6: User `Rina Wijaya {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Rina W`, dari `Rina Wijaya {runId}`.
  - DU-001-7: Division `Field Survey {runId}` pada Group `Branch Surabaya {runId}`; PIC lamanya `Dedi Hartono {runId}` berstatus `dinonaktifkan` sehingga Division tidak punya PIC aktif.
  - DU-001-8: Division `Finance {runId}` pada Group `Branch Surabaya {runId}`; PIC aktifnya `Dewi Anggraini {runId}`, karyawan anggota Division tanpa akses menu Assignment.
  - DU-001-9: ASG berstatus `Waiting for Handover` untuk Assignee DU-001-7, Group `Branch Surabaya {runId}`, aset `Handheld Scanner Zebra TC21 {runId}` dan `Handheld Scanner Zebra TC26 {runId}`, Total Asset `2`, tanpa PIC aktif sehingga bertanda `No PIC`; dibuat paling awal.
  - DU-001-10: ASG berstatus `Waiting for Handover` untuk Assignee DU-001-6, Group `Head Office {runId}`, aset `Printer Epson L3250 {runId}`, `Scanner Fujitsu fi-7160 {runId}`, dan `UPS APC 1000VA {runId}` menunggu handover serta `Kabel Power APC {runId}` sudah `Canceled` oleh pengaju, Total Asset `3` karena baris Canceled tidak dihitung; dibuat sesudah DU-001-9.
  - DU-001-11: ASG berstatus `Waiting for Approval` untuk Assignee DU-001-5, Group `Head Office {runId}`, aset `Laptop Lenovo T14 {runId}` dan `Laptop Lenovo T16 {runId}` menunggu persetujuan, serta `Monitor Dell P2422H {runId}` sudah `Rejected` oleh Approver, Total Asset `2` karena baris Rejected tidak dihitung; dibuat sesudah DU-001-10.
  - DU-001-12: ASG berstatus `Assigned` untuk Assignee DU-001-4, Group `Head Office {runId}`, aset `Laptop Asus ExpertBook B1 {runId}` dan `Docking Station Dell WD19 {runId}`, Total Asset `2`; dibuat sesudah DU-001-11.
  - DU-001-13: ASG berstatus `Assigned` untuk Assignee DU-001-8, Group `Branch Surabaya {runId}`, aset `Mesin Hitung Uang Glory {runId}` dan `Brankas Digital Chubb {runId}`, Total Asset `2`; dibuat sesudah DU-001-12 sehingga Last Updated-nya yang terbaru di antara kelima ASG.
  - DU-001-14: Draft untuk Assignee DU-001-5, Group `Head Office {runId}`, dengan aset `Proyektor Epson EB-X06 {runId}`; Draft tidak bernomor.
  - DU-001-15: ASG berstatus `Canceled` untuk Assignee DU-001-4 dengan aset `Printer Label Zebra ZD220 {runId}`; ASG sudah selesai sehingga hanya ada di tab History.
  - DU-001-16: parameter URL pilihan tab: `?tab=history` untuk tab History dan `?tab=assigned` untuk tab Assigned Assets.
  - DU-001-17: pengaturan state tabel: filter `Assignee Type` bernilai `Employee`, sort `Assignee` A–Z dengan kunci nama lengkap `Budi Santoso {runId}`, `Rina Wijaya {runId}`, `Sari Dewi {runId}` sehingga urutannya `Budi S`, `Rina W`, `Sari D`, dan `Rows per page` bernilai `25`.
  - Transaction ID setiap ASG dibentuk server; Transaction ID tiap baris adalah milik entri ASG-nya.

## Test Steps

### Halaman Assignment terbuka di tab Transactions
1. Verifikasi tab `Transactions`, `Drafts`, `Assigned Assets`, dan `History` tampil pada halaman Assignment
2. Verifikasi tab `Transactions` menjadi tab yang aktif saat halaman pertama kali terbuka
3. Verifikasi toolbar tab `Transactions` memuat Search, `Filter`, `Download`, dan `[+ Assign]`, dengan `[+ Assign]` di paling kanan[^drift-1]

### Tabel hanya memuat data spec ini
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi tabel memuat tepat 5 baris, yaitu baris untuk Assignee `Field Survey {runId}`, `Rina W`, `Sari D`, `Finance {runId}`, dan `Budi S`
6. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Transaction ID`, `Status`, `Group`, `Assignee`, `Assignee Type`, `Total Asset`, `Requested By`, `Request Date`, `Last Updated`
7. Verifikasi kolom `Transaction ID` pada kelima baris berformat `ASG-YYYY-NNNN`
8. Verifikasi urutan awal baris dari atas ke bawah tanpa sort pilihan pengguna: `Field Survey {runId}` (bertanda `No PIC`), `Rina W`, `Sari D`, `Finance {runId}`, `Budi S`

### Badge status header
9. Verifikasi kolom `Status` baris `Field Survey {runId}` menampilkan badge `Waiting for Handover`
10. Verifikasi kolom `Status` baris `Field Survey {runId}` menampilkan badge `No PIC` di samping status header
11. Verifikasi kolom `Status` baris `Rina W` menampilkan badge `Waiting for Handover` tanpa badge `No PIC`
12. Verifikasi kolom `Status` baris `Sari D` menampilkan badge `Waiting for Approval`
13. Verifikasi kolom `Status` baris `Finance {runId}` dan baris `Budi S` menampilkan badge `Assigned`
14. Verifikasi kolom `Status` baris `Sari D` hanya memuat badge status header `Waiting for Approval`, tanpa ringkasan baris `Rejected`
15. Verifikasi badge `No PIC` tidak tampil pada nilai kolom `Assignee` baris `Field Survey {runId}`
16. Arahkan kursor ke kolom `Status` baris `Sari D`
17. Verifikasi rincian baris per status memuat `Waiting for Approval` dan `Rejected`

### Kolom Group, Assignee, dan Assignee Type
18. Verifikasi kolom `Group` baris `Field Survey {runId}` menampilkan `Branch Surabaya {runId}`
19. Arahkan kursor ke badge Group pada baris `Field Survey {runId}`
20. Verifikasi hierarki lengkap Group tampil sebagai `Head Office {runId} > Branch Surabaya {runId}`
21. Verifikasi kolom `Assignee` baris Employee tampil sebagai `Budi S`, dari `Budi Santoso {runId}`
22. Arahkan kursor ke nilai `Budi S`
23. Verifikasi nama lengkap `Budi Santoso {runId}` tampil
24. Verifikasi kolom `Assignee Type` baris `Finance {runId}` menampilkan `Division`
25. Verifikasi kolom `Assignee Type` baris `Budi S` menampilkan `Employee`
26. Arahkan kursor ke nilai Assignee `Finance {runId}`
27. Verifikasi `PIC: Dewi Anggraini {runId}` tampil
28. Arahkan kursor ke nilai Assignee `Field Survey {runId}`
29. Verifikasi `No active PIC` tampil

### Kolom Total Asset, Requested By, dan tanggal
30. Verifikasi kolom `Total Asset` baris `Sari D` menampilkan `2`, tanpa menghitung baris `Rejected`
31. Verifikasi kolom `Total Asset` baris `Rina W` menampilkan `3`, tanpa menghitung baris `Canceled`
32. Arahkan kursor ke kolom `Total Asset` baris `Sari D`
33. Verifikasi daftar semua aset beserta status barisnya tampil, memuat `Laptop Lenovo T14 {runId}`, `Laptop Lenovo T16 {runId}`, dan `Monitor Dell P2422H {runId}` dengan `Monitor Dell P2422H {runId}` berstatus `Rejected`
34. Arahkan kursor ke kolom `Requested By` baris `Sari D`
35. Verifikasi nama lengkap `Agus Prasetyo {runId}` tampil
36. Verifikasi kolom `Request Date` dan `Last Updated` pada kelima baris berisi tanggal dan waktu

### Tautan Transaction ID membuka Assignment Detail
37. Klik tautan Transaction ID pada baris `Budi S`
38. Verifikasi Assignment Detail untuk ASG baris `Budi S` terbuka
39. Kembali ke halaman sebelumnya
40. Verifikasi kotak Search masih berisi `{runId}` dan tabel memuat tepat 5 baris

### Field filter di toolbar
41. Klik `Filter`
42. Verifikasi field filter `Status`, `No PIC`, `Group`, `Assignee`, `Assignee Type`, `Requested By`, `Total Asset`, `Request Date`, dan `Last Updated` tampil
43. Verifikasi placeholder `All statuses`, `All PIC statuses`, `All groups`, `All assignees`, `All types`, dan `All users` tampil pada field dropdown masing-masing
44. Verifikasi field `Total Asset` memuat input `Min` dan `Max`, serta field `Request Date` dan `Last Updated` memuat placeholder `Select date`
45. Klik field `No PIC`
46. Verifikasi opsi `No PIC` dan `Has PIC` tampil
47. Klik `Filter`

### Draft dan ASG selesai tidak tampil di tab Transactions
48. Ganti isi kotak search dengan `Laptop Asus ExpertBook B1 {runId}`, tekan Enter
49. Verifikasi baris `Budi S` tampil di tabel
50. Ganti isi kotak search dengan `Proyektor Epson EB-X06 {runId}`, tekan Enter
51. Verifikasi pesan `No results found` tampil karena Draft tidak ada di tab Transactions
52. Ganti isi kotak search dengan `Printer Label Zebra ZD220 {runId}`, tekan Enter
53. Verifikasi pesan `No results found` tampil karena ASG yang sudah selesai tidak ada di tab Transactions
54. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Pilihan tab tersimpan di URL dan state tab dipulihkan
55. Klik tab `History`
56. Verifikasi URL memuat `?tab=history`
57. Verifikasi toolbar tab `History` tidak memuat `[+ Assign]` sedangkan Search tetap tampil
58. Klik tab `Assigned Assets`
59. Klik sub-tab `By Assignee`
60. Verifikasi URL memuat `?tab=assigned` dan `?view=`
61. Klik tab `Transactions`
62. Verifikasi URL memuat `?tab=transactions`
63. Verifikasi kotak Search masih berisi `{runId}` dan tabel memuat tepat 5 baris

### Baris Canceled tetap tampil di rincian Total Asset
64. Arahkan kursor ke kolom `Total Asset` baris `Rina W`
65. Verifikasi daftar semua aset beserta status barisnya memuat `Printer Epson L3250 {runId}`, `Scanner Fujitsu fi-7160 {runId}`, `UPS APC 1000VA {runId}`, dan `Kabel Power APC {runId}` dengan `Kabel Power APC {runId}` berstatus `Canceled`

### State Filter, Sort, dan Search tab Transactions dipulihkan sesudah Back dan muat ulang
66. Klik `Filter`
67. Pilih `Employee` pada field `Assignee Type`
68. Klik `[Apply]`
69. Verifikasi tabel memuat tepat 3 baris, yaitu baris `Rina W`, `Sari D`, dan `Budi S`
70. Klik header kolom `Assignee`
71. Verifikasi urutan baris dari atas ke bawah: `Budi S`, `Rina W`, `Sari D`
72. Klik tautan Transaction ID pada baris `Rina W`
73. Kembali ke halaman sebelumnya
74. Verifikasi kotak Search masih berisi `{runId}`
75. Verifikasi tabel masih memuat tepat 3 baris, yaitu baris `Rina W`, `Sari D`, dan `Budi S`
76. Verifikasi urutan baris dari atas ke bawah masih `Budi S`, `Rina W`, `Sari D`
77. Muat ulang halaman
78. Verifikasi kotak Search masih berisi `{runId}`
79. Verifikasi tabel masih memuat tepat 3 baris, yaitu baris `Rina W`, `Sari D`, dan `Budi S`
80. Verifikasi urutan baris dari atas ke bawah masih `Budi S`, `Rina W`, `Sari D`

### State Rows per page dipulihkan sesudah muat ulang
81. Ubah `Rows per page` menjadi `25`
82. Muat ulang halaman
83. Verifikasi `Rows per page` masih bernilai `25`

### State sub-tab By Asset dan By Assignee terpisah
84. Klik tab `Assigned Assets`
85. Ketik Search `Laptop Asus ExpertBook B1 {runId}`, tekan Enter
86. Klik sub-tab `By Assignee`
87. Verifikasi URL tab `Assigned Assets` memuat `?view=assignee` setelah sub-tab `By Assignee` dipilih
88. Verifikasi baris `Finance {runId}` tampil di tabel sub-tab `By Assignee`
89. Verifikasi kotak Search sub-tab `By Assignee` tidak berisi `Laptop Asus ExpertBook B1 {runId}`
90. Klik sub-tab `By Asset`
91. Verifikasi URL memuat `?view=asset`
92. Verifikasi kotak Search sub-tab `By Asset` masih berisi `Laptop Asus ExpertBook B1 {runId}`

### State Search tab History dipulihkan sesudah Back dan muat ulang
93. Klik tab `History`
94. Ketik Search `Printer Label Zebra ZD220 {runId}`, tekan Enter
95. Klik tautan Transaction ID pada baris `Budi S`
96. Kembali ke halaman sebelumnya
97. Verifikasi kotak Search tab `History` masih berisi `Printer Label Zebra ZD220 {runId}` sesudah Back
98. Muat ulang halaman
99. Verifikasi kotak Search tab `History` masih berisi `Printer Label Zebra ZD220 {runId}` sesudah muat ulang

[^drift-1]: Drift PRD vs foundation. PRD §5 Global Table Rules baris Download: nama dan tooltip tombol toolbar adalah `Export`, bukan `Download`. foundation `prd-conventions.md` §9.1: icon toolbar bernama `Download` dengan tooltip `Download`, dan modul tidak menulis ulang teks tooltip itu. Diasersi: foundation, karena tombol unduh di toolbar tabel adalah pola bersama (SB-4).
