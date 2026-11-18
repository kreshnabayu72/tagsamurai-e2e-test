---
id: TC-FA-ASSIGN-E2E-009-tab-history
title: "Tab History: By Transaction dan By Asset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-15, T-ASG-16, "§4.1#r3", "§9.5#r5", "§9.5#r15"]
smoke: []
dependsOn: []
trace:
  T-ASG-15: [2, 5, 6, 7, 8, 9, 10, 15, 16, 19, 22, 24, 26, 28, 31, 32, 88, 89, 92, 94, 96, 98]
  T-ASG-16: [34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 51, 55, 58, 60, 62, 64, 67, 68, 71, 72, 73, 74, 76, 79, 81, 83, 84]
  "§4.1#r3": 35
  "§9.5#r5": [6, 39]
  "§9.5#r15": [12, 13]
anchor: [4, 37]
coverage:
  web: automated
---

# Tab History: By Transaction dan By Asset

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-009-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-009-2: Group `Head Office {runId}` sebagai Group induk dan Group `Branch Bandung {runId}` sebagai anak langsung `Head Office {runId}`.
  - DU-009-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju semua ASG DU-009-8 sampai DU-009-11.
  - DU-009-4: User `Rina Wijaya {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pelapor Report Missing pada aset DU-009-11 dan bukan Assignee.
  - DU-009-5: User `Sari Dewi {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Sari D`, dari `Sari Dewi {runId}`.
  - DU-009-6: User `Budi Santoso {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-009-7: User `Wulan Hartati {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Wulan H`, dari `Wulan Hartati {runId}`.
  - DU-009-8: ASG berstatus `Unassigned` untuk Assignee DU-009-5 dengan aset `Laptop Dell Latitude 5420 {runId}` beralias `Lap-Dell-5420 {runId}` dan ber-TAG QR, Total Asset `1`; Asset ID dan kode TAG aset itu dibentuk server dan menjadi milik aset itu; aset diserahkan oleh DU-009-4 dengan Purpose `Kerja lapangan Bandung {runId}` dan foto handover tersedia, lalu di-Unassign dan diterima oleh DU-009-3 dengan foto unassign tersedia; pelaku peristiwa terbaru DU-009-3; ditutup pertama.
  - DU-009-9: ASG berstatus `Rejected` untuk Assignee DU-009-6, Group `Branch Bandung {runId}`, dengan aset `Excavator PC200 {runId}` dan `Excavator PC210 {runId}` yang keduanya `Rejected` pada saat yang sama, Total Asset `2`; ditolak Approver dengan Reason `Anggaran belum disetujui`; ditutup keempat.
  - DU-009-10: ASG berstatus `Canceled` untuk Assignee DU-009-7 dengan aset `Camera Sony A7 {runId}`, Total Asset `1`; dibatalkan manual oleh pengaju tanpa Reason, tanpa foto handover maupun foto unassign; ditutup kelima.
  - DU-009-12: Acuan waktu T0 adalah tanggal dan waktu saat spec dijalankan; rentang default tab History adalah dari T0 − 90 hari sampai T0.
  - DU-009-11: ASG berstatus `Assigned` untuk Assignee DU-009-5 yang masih aktif: aset `Laptop Asus ExpertBook B1 {runId}` `Unassigned` dengan marker `Damaged` (ditutup kedua), aset `Tablet Samsung Tab S8 {runId}` `Unassigned` dengan marker `Missing` yang dilaporkan `Rina Wijaya {runId}` (ditutup ketiga), dan aset `Mouse Logitech MX Master {runId}` masih `Assigned`, sehingga ASG ini tetap di tab Transactions.

## Test Steps

### History By Transaction dan rentang awal
1. Klik tab `History`
2. Verifikasi sub-tab `By Transaction` menjadi view awal tab `History` dan URL memuat `?view=transaction`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi tabel memuat tepat 3 baris, yaitu baris untuk Assignee `Sari D`, `Budi S`, dan `Wulan H`
5. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Transaction ID`, `Status`, `Group`, `Assignee`, `Total Asset`, `Requested By`, `Request Date`, `Last Updated`
6. Verifikasi urutan awal baris dari atas ke bawah menurut Last Updated terbaru: `Wulan H`, `Budi S`, `Sari D`
7. Verifikasi kolom `Status` baris `Sari D` menampilkan badge `Unassigned` tanpa marker, baris `Budi S` menampilkan `Rejected`, dan baris `Wulan H` menampilkan `Canceled`
8. Verifikasi kolom `Total Asset` baris `Budi S` menampilkan `2` karena semua baris dihitung termasuk yang `Rejected`, dan baris `Sari D` serta `Wulan H` menampilkan `1`
9. Verifikasi baris untuk ASG yang masih punya baris aktif dengan Assignee `Sari D` tidak tampil sebagai baris tambahan sehingga hanya ada satu baris `Sari D`
10. Verifikasi kolom `Transaction ID` ketiga baris berformat `ASG-YYYY-NNNN`
11. Klik `Filter`
12. Verifikasi field `Last Updated` berisi rentang 90 hari terakhir, yaitu dari T0 − 90 hari sampai T0
13. Verifikasi ikon `Filter` menampilkan indikator filter aktif karena rentang itu ter-Apply
14. Klik field `Status`
15. Verifikasi opsi `Unassigned`, `Rejected`, dan `Canceled` tampil
16. Verifikasi opsi `Unassigned · Damaged` dan `Unassigned · Missing` tidak tampil karena marker hanya melekat per baris aset
17. Klik `Filter`
18. Klik `⋯` pada baris `Sari D`
19. Verifikasi menu aksi baris memuat `Detail`
20. Tutup menu aksi baris

### Hover kolom sub-tab By Transaction
21. Arahkan kursor ke kolom `Status` baris `Budi S`
22. Verifikasi rincian baris memuat status `Rejected`
23. Arahkan kursor ke kolom `Total Asset` baris `Budi S`
24. Verifikasi daftar semua baris beserta statusnya memuat `Excavator PC200 {runId}` dan `Excavator PC210 {runId}` dengan status `Rejected`
25. Arahkan kursor ke kolom `Group` baris `Budi S`
26. Verifikasi hierarki lengkap Group tampil sebagai `Head Office {runId} > Branch Bandung {runId}`
27. Arahkan kursor ke kolom `Assignee` baris `Budi S`
28. Verifikasi nama lengkap Assignee `Budi Santoso {runId}` tampil pada hover baris `Budi S`

### Export sub-tab By Transaction
29. Klik `Download`[^drift-1]
30. Klik `Download as CSV`
31. Verifikasi berkas `Assignment-History-By-Transaction.csv` terunduh
32. Verifikasi berkas yang diunduh memuat tepat 3 baris data sesuai tabel yang tersaring dan header yang sama dengan kolom tabel yang tampil

### History By Asset
33. Klik sub-tab `By Asset`
34. Verifikasi URL tab `History` memuat `?view=asset`
35. Verifikasi sub-tab pill `By Transaction` dan `By Asset` tampil di tab `History`
36. Ganti isi kotak search dengan `{runId}`, tekan Enter
37. Verifikasi tabel memuat tepat 6 baris, yaitu aset `Camera Sony A7 {runId}`, `Excavator PC200 {runId}`, `Excavator PC210 {runId}`, `Tablet Samsung Tab S8 {runId}`, `Laptop Asus ExpertBook B1 {runId}`, dan `Laptop Dell Latitude 5420 {runId}`
38. Verifikasi aset `Mouse Logitech MX Master {runId}` tidak tampil karena barisnya masih `Assigned`
39. Verifikasi urutan baris menurut Last Updated terbaru: `Camera Sony A7 {runId}`, lalu `Excavator PC200 {runId}` dan `Excavator PC210 {runId}` tanpa urutan antar keduanya, lalu `Tablet Samsung Tab S8 {runId}`, `Laptop Asus ExpertBook B1 {runId}`, dan `Laptop Dell Latitude 5420 {runId}`
40. Verifikasi header kolom tampil berurutan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Handed Over At`, `Unassigned At`, `Transaction ID`, `Assignee`, `Last Updated`
41. Verifikasi kolom `Reason`, `Handover Photo`, `Unassign Photo`, `Purpose`, `TAG`, dan `Category` tidak tampil secara awal
42. Verifikasi kolom `Status` baris `Laptop Asus ExpertBook B1 {runId}` menampilkan `Unassigned` dengan badge kedua `Damaged` dan baris `Tablet Samsung Tab S8 {runId}` menampilkan `Unassigned` dengan badge kedua `Missing`
43. Verifikasi kolom `Status` baris `Excavator PC200 {runId}` menampilkan `Rejected` dan baris `Camera Sony A7 {runId}` menampilkan `Canceled`
44. Verifikasi kolom `Handed Over At` dan `Unassigned At` baris `Excavator PC200 {runId}` dan `Camera Sony A7 {runId}` menampilkan `—` karena tidak pernah diserahkan
45. Verifikasi kolom `Handed Over At` dan `Unassigned At` baris `Laptop Dell Latitude 5420 {runId}` terisi tanggal
46. Verifikasi kolom `Brand` dan `Model/Type` baris `Laptop Dell Latitude 5420 {runId}` menampilkan `—`
47. Verifikasi kolom `Assignee` baris `Laptop Dell Latitude 5420 {runId}` menampilkan `Sari D`
48. Arahkan kursor ke kolom `Unassigned At` baris `Tablet Samsung Tab S8 {runId}`
49. Verifikasi tooltip `Reported missing by [Reporter]` tampil dengan Reporter `Rina Wijaya {runId}`
50. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
51. Verifikasi menu aksi baris memuat `Assignment Log`
52. Tutup menu aksi baris

### Filter Status sub-tab By Asset
53. Klik `Filter`
54. Klik field `Status`
55. Verifikasi opsi `Unassigned`, `Unassigned · Damaged`, `Unassigned · Missing`, `Rejected`, dan `Canceled` tampil
56. Klik `Filter`

### Hover kolom sub-tab By Asset
57. Arahkan kursor ke kolom `Handed Over At` baris `Laptop Dell Latitude 5420 {runId}`
58. Verifikasi `Rina Wijaya {runId}` tampil sebagai penyerah aset pada hover `Handed Over At`
59. Arahkan kursor ke kolom `Unassigned At` baris `Laptop Dell Latitude 5420 {runId}`
60. Verifikasi `Agus Prasetyo {runId}` tampil sebagai pihak yang menerima aset
61. Arahkan kursor ke kolom `Last Updated` baris `Laptop Dell Latitude 5420 {runId}`
62. Verifikasi `Agus Prasetyo {runId}` tampil sebagai pelaku peristiwa terbaru
63. Arahkan kursor ke kolom `Assignee` baris `Laptop Dell Latitude 5420 {runId}`
64. Verifikasi nama lengkap Assignee `Sari Dewi {runId}` tampil pada hover baris `Laptop Dell Latitude 5420 {runId}`

### Export sub-tab By Asset
65. Klik `Download`[^drift-1]
66. Klik `Download as CSV`
67. Verifikasi berkas `Assignment-History-By-Asset.csv` terunduh
68. Verifikasi berkas yang diunduh memuat tepat 6 baris data sesuai tabel yang tersaring dan header yang sama dengan kolom tabel yang tampil

### Nilai kolom Reason, Purpose, dan foto sub-tab By Asset
69. Klik header kolom `Actions`
70. Beri centang kolom `Reason`, `Handover Photo`, `Unassign Photo`, dan `Purpose` pada panel Column Visibility
71. Verifikasi kolom `Reason` baris `Excavator PC200 {runId}` menampilkan `Anggaran belum disetujui`
72. Verifikasi kolom `Reason` baris `Camera Sony A7 {runId}` menampilkan `—` karena dibatalkan manual tanpa Reason
73. Verifikasi kolom `Reason` baris `Laptop Dell Latitude 5420 {runId}` menampilkan `—` karena berstatus `Unassigned`
74. Verifikasi kolom `Purpose` baris `Laptop Dell Latitude 5420 {runId}` menampilkan `Kerja lapangan Bandung {runId}`
75. Klik thumbnail kolom `Handover Photo` baris `Laptop Dell Latitude 5420 {runId}`
76. Verifikasi pratinjau foto handover terbuka
77. Tutup pratinjau foto
78. Klik thumbnail kolom `Unassign Photo` baris `Laptop Dell Latitude 5420 {runId}`
79. Verifikasi pratinjau foto unassign terbuka
80. Tutup pratinjau foto

### Kolom foto kosong untuk baris tanpa foto
81. Verifikasi kolom `Handover Photo` dan `Unassign Photo` baris `Camera Sony A7 {runId}` menampilkan `—` karena belum ada foto

### Field filter dan placeholder di kedua sub-tab
82. Klik `Filter`
83. Verifikasi field filter `Status`, `Brand`, `Model/Type`, `Group`, `Assignee`, `TAG`, `Category`, `Handed Over At`, `Unassigned At`, dan `Last Updated` tampil di sub-tab `By Asset`
84. Verifikasi placeholder `All statuses`, `All brands`, `All models`, `All groups`, `All assignees`, `All tags`, dan `All categories` tampil pada field dropdown masing-masing, serta field `Handed Over At` dan `Unassigned At` memuat placeholder `Select date`
85. Klik `Filter`
86. Klik sub-tab `By Transaction`
87. Klik `Filter`
88. Verifikasi field filter `Status`, `Group`, `Assignee`, `Total Asset`, `Requested By`, `Request Date`, dan `Last Updated` tampil di sub-tab `By Transaction`
89. Verifikasi placeholder `All statuses`, `All groups`, `All assignees`, dan `All users` tampil pada field dropdown masing-masing, field `Total Asset` memuat input `Min` dan `Max`, serta field `Request Date` memuat placeholder `Select date`
90. Klik `Filter`

### Search sub-tab By Transaction mencakup nama aset, Asset ID, alias, dan kode TAG
91. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
92. Verifikasi baris `Sari D` tampil di sub-tab `By Transaction` karena nama aset ikut dicari
93. Ganti isi kotak search dengan Asset ID milik aset `Laptop Dell Latitude 5420 {runId}`, tekan Enter
94. Verifikasi baris `Sari D` tampil di sub-tab `By Transaction` karena Asset ID aset ikut dicari
95. Ganti isi kotak search dengan alias aset `Laptop Dell Latitude 5420 {runId}`, yaitu `Lap-Dell-5420 {runId}`, tekan Enter
96. Verifikasi baris `Sari D` tampil di sub-tab `By Transaction` karena alias aset ikut dicari
97. Ganti isi kotak search dengan kode TAG milik aset `Laptop Dell Latitude 5420 {runId}`, tekan Enter
98. Verifikasi baris `Sari D` tampil di sub-tab `By Transaction` karena kode TAG aset ikut dicari

[^drift-1]: Drift PRD vs foundation. PRD §4.1k Matriks Aksi baris Export: nama tombol toolbar adalah `Export`, bukan `Download`. foundation `prd-conventions.md` §9.1: icon toolbar bernama `Download` dengan tooltip `Download`, dan modul tidak menulis ulang teks tooltip itu. Diasersi: foundation, karena tombol unduh di toolbar tabel adalah pola bersama (SB-4).
