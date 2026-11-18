---
id: TC-FA-ASSIGN-UI-119-tabel-drafts-bulk-bar
title: "Tabel Drafts: mekanik seleksi dan Bulk Action Bar"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-BLK-1@tabel-drafts", "EB-BLK-4", "EB-BLK-6", "§5#r6"]
smoke: []
dependsOn: []
trace:
  "EB-BLK-1@tabel-drafts": [3, 4, 7, 8, 12, 13, 14, 17, 19, 20, 22, 28, 30, 31, 38, 39]
  "EB-BLK-4": [46, 47, 54, 55]
  "EB-BLK-6": [59, 60, 62, 64]
  "§5#r6": [68, 72, 74, 75, 77, 78, 80, 81, 83, 84, 86, 87, 89, 90, 92, 93]
coverage:
  web: automated
---

# Tabel Drafts: mekanik seleksi dan Bulk Action Bar

## Prerequisites
- Aktor: Aktor Assignment; Approver untuk tabel Approvals > Assignment (K12 dan K13).
- Layar awal: Transactions > Assignment, tab Drafts; Approvals > Assignment untuk K12 dan K13.
- Komponen: Tabel Drafts
- Data:
  - DU-119-1: Draft Assignee `Budi S`, Assignee Type `Employee`, Group `Head Office`, Total Asset `2`, Origin `New`, Modified By `Rina W`, Last Updated `09 Nov 2026, 08:01`.
  - DU-119-2: Draft Assignee `Finance`, Assignee Type `Division`, Group `Head Office +1`, Total Asset `4`, Origin `Restored by system`, Modified By `System`, Last Updated `08 Nov 2026, 09:45`.
  - DU-119-3: Draft Assignee `Sari D`, Assignee Type `Employee`, Group `Head Office`, Total Asset `2`, Origin `New`, Modified By `Rina W`, Last Updated `30 Sep 2026, 16:10`.
  - DU-119-4: 25 Draft dengan pola Assignee `Karyawan Draf {n}`, Assignee Type `Employee`, Group `Head Office`, Total Asset `1`, Origin `New`, Modified By `Rina W`, Last Updated `09 Nov 2026, 08:01`.
  - DU-119-5: 1005 Draft dengan pola Assignee `Karyawan Draf {n}`, Assignee Type `Employee`, Group `Head Office`, Total Asset `1`, Origin `New`, Modified By `Rina W`, Last Updated `09 Nov 2026, 20:00` untuk `Karyawan Draf 1` dan mundur satu menit untuk setiap n berikutnya, sehingga setiap baris punya Last Updated berbeda dan `Karyawan Draf 1` paling baru.
  - DU-119-6: Assignment `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `09 Nov 2026, 19:00`, Last Updated `09 Nov 2026, 20:40`.
  - DU-119-7: Assigned asset Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Assigned`, Assigned Since `12 Oct 2026`, Transaction ID `ASG-2026-0041`, Assignee `Budi S`.
  - DU-119-8: Assignee `Budi S`, Assignee Type `Employee`, Group `Head Office`, Total Asset `6`.
  - DU-119-9: History Transaction ID `ASG-2026-0065`, Status `Unassigned`, Group `Head Office`, Assignee `Sari D`, Total Asset `1`, Requested By `Rina W`, Request Date `03 Nov 2026, 09:00`, Last Updated `08 Nov 2026, 17:12`.
  - DU-119-10: History asset Photo `laptop-dell-latitude-5420-61.jpg`, Name `Laptop Dell Latitude 5420 - 61`, Asset ID `LPT-2026-0061`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Unassigned`, Handed Over At `03 Nov 2026`, Unassigned At `08 Nov 2026, 17:12`, Transaction ID `ASG-2026-0065`, Assignee `Sari D`, Last Updated `08 Nov 2026, 17:12`.
  - DU-119-11: Pengajuan approval Active `ASG-2026-0070`, Group `Head Office`, Assignee `Sari D`, Total Asset `2`, Requested By `Agus P`, Request Date `09 Nov 2026, 14:00`.
  - DU-119-12: Pengajuan approval History `ASG-2026-0067`, Status `Approved`, Group `Head Office`, Assignee `Sari D`, Total Asset `2`, Requested By `Agus P`, Request Date `08 Nov 2026, 10:00`, Decided Date `08 Nov 2026, 11:00`.
  - DU-119-13: Baris aset pada Assignment Detail Photo `laptop-dell-latitude-5420-21.jpg`, Name `Laptop Dell Latitude 5420 - 21`, Asset ID `LPT-2026-0021`, Brand `—`, Model/Type `—`, Status `Waiting for Handover`, Handed Over At `—`, Confirmation `—`, Approval `Not required`, Handover Photo `—`, Unassign Photo `—`.
- Kondisi:
  - K1: daftar Tabel Drafts berisi DU-119-1 sampai DU-119-3.
  - K2: daftar Tabel Drafts berisi DU-119-4, ukuran halaman bawaan `10`.
  - K3: seperti K1, dan Bulk Delete dijawab sukses.
  - K4: seperti K1, dan Bulk Delete dijawab error server 5xx.
  - K5: seperti K1, dan Bulk Delete tidak dijawab sampai batas waktu (timeout).
  - K6: Selection Limit bernilai `1000`, dan daftar Tabel Drafts berisi DU-119-5 dengan urutan tampil bawaan (Last Updated terbaru dulu), ukuran halaman bawaan `10`.
  - K7: daftar Tabel Transactions berisi DU-119-6.
  - K8: daftar tabel Assigned Assets By Asset berisi DU-119-7.
  - K9: daftar tabel Assigned Assets By Assignee berisi DU-119-8.
  - K10: daftar tabel History By Transaction berisi DU-119-9.
  - K11: daftar tabel History By Asset berisi DU-119-10.
  - K12: daftar tabel Approvals > Assignment Active berisi DU-119-11.
  - K13: daftar tabel Approvals > Assignment History berisi DU-119-12.
  - K14: daftar tabel Assets pada Assignment Detail berisi DU-119-13.

## Test Steps

### Checkbox header dan status indeterminate
1. Tampilkan Tabel Drafts dengan kondisi K1
2. Centang baris `Budi S`
3. Verifikasi checkbox header berstatus indeterminate
4. Verifikasi bar bulk menampilkan `1 Draft selected`
5. Centang baris `Finance`
6. Centang baris `Sari D`
7. Verifikasi checkbox header tercentang penuh
8. Verifikasi bar bulk menampilkan `3 Drafts selected`

### Klik ✕ membersihkan seleksi
9. Tampilkan Tabel Drafts dengan kondisi K1
10. Centang baris `Budi S`
11. Klik `✕` pada bar bulk
12. Verifikasi baris `Budi S` tetap tampil di tabel
13. Verifikasi baris `Budi S` tidak tercentang
14. Verifikasi bar bulk tidak tampil

### Seleksi bertahan saat pindah halaman
15. Tampilkan Tabel Drafts dengan kondisi K2
16. Centang checkbox header
17. Verifikasi bar bulk menampilkan `10 Drafts selected`
18. Klik tombol halaman `2`
19. Verifikasi bar bulk tetap menampilkan `10 Drafts selected`
20. Verifikasi checkbox header belum tercentang pada halaman `2`
21. Klik tombol halaman `1`
22. Verifikasi checkbox header tercentang penuh pada halaman `1`

### Cancel dialog konfirmasi tidak memproses apa pun
23. Tampilkan Tabel Drafts dengan kondisi K1
24. Centang baris `Budi S`
25. Centang baris `Sari D`
26. Klik `Bulk Action`
27. Klik `Delete`
28. Verifikasi dialog `Delete Drafts` tampil
29. Klik `[Go Back]`
30. Verifikasi baris `Budi S` dan `Sari D` tetap tampil di tabel
31. Verifikasi bar bulk tetap menampilkan `2 Drafts selected`

### Seleksi bersih sesudah aksi selesai
32. Tampilkan Tabel Drafts dengan kondisi K3
33. Centang baris `Budi S`
34. Centang baris `Sari D`
35. Klik `Bulk Action`
36. Klik `Delete`
37. Klik `[Delete]`
38. Verifikasi toast `Success, draft has been deleted.` tampil
39. Verifikasi bar bulk tidak tampil

### Bulk gagal dengan error server 5xx
40. Tampilkan Tabel Drafts dengan kondisi K4
41. Centang baris `Budi S`
42. Centang baris `Sari D`
43. Klik `Bulk Action`
44. Klik `Delete`
45. Klik `[Delete]`
46. Verifikasi toast `Error, failed to delete draft.` tampil
47. Verifikasi bar bulk tetap menampilkan `2 Drafts selected`

### Bulk gagal karena timeout
48. Tampilkan Tabel Drafts dengan kondisi K5
49. Centang baris `Budi S`
50. Centang baris `Sari D`
51. Klik `Bulk Action`
52. Klik `Delete`
53. Klik `[Delete]`
54. Verifikasi toast `Connection problem. Please try again.` tampil
55. Verifikasi bar bulk tetap menampilkan `2 Drafts selected`

### Select All melebihi Selection Limit dipotong ke batas
56. Tampilkan Tabel Drafts dengan kondisi K6
57. Centang checkbox header
58. Klik `Select All (1005 records)`
59. Verifikasi toast `Error, only the first 1000 of 1005 rows were selected. Narrow your filter to include the rest.` tampil
60. Verifikasi bar bulk menampilkan `1000 Drafts selected`
61. Ganti isi `Jump to page` dengan `101`, tekan Enter
62. Verifikasi checkbox baris `Karyawan Draf 1001` disabled
63. Arahkan kursor ke checkbox baris `Karyawan Draf 1001`
64. Verifikasi tooltip `You've reached the maximum selection of 1000 rows.` tampil

### Bulk Action tabel Drafts hanya menawarkan Delete
65. Tampilkan Tabel Drafts dengan kondisi K1
66. Centang baris `Budi S`
67. Klik `Bulk Action`
68. Verifikasi opsi menu Bulk Action hanya `Delete`

### Bulk Action tabel Assigned Assets By Asset menawarkan Unassign
69. Tampilkan tabel Assigned Assets By Asset dengan kondisi K8
70. Centang baris `Laptop Dell Latitude 5420 - 4`
71. Klik `Bulk Action`
72. Verifikasi opsi menu Bulk Action hanya `Unassign`

### Tabel Transactions tanpa Bulk
73. Tampilkan Tabel Transactions dengan kondisi K7
74. Verifikasi baris `ASG-2026-0071` tampil di tabel Transactions
75. Verifikasi kolom checkbox tidak tampil pada tabel Transactions

### Tabel Assigned Assets By Assignee tanpa Bulk
76. Tampilkan tabel Assigned Assets By Assignee dengan kondisi K9
77. Verifikasi baris `Budi S` tampil di tabel By Assignee
78. Verifikasi kolom checkbox tidak tampil pada tabel By Assignee

### Tabel History By Transaction tanpa Bulk
79. Tampilkan tabel History By Transaction dengan kondisi K10
80. Verifikasi baris `ASG-2026-0065` tampil di tabel History By Transaction
81. Verifikasi kolom checkbox tidak tampil pada tabel History By Transaction

### Tabel History By Asset tanpa Bulk
82. Tampilkan tabel History By Asset dengan kondisi K11
83. Verifikasi baris `LPT-2026-0061` tampil di tabel History By Asset
84. Verifikasi kolom checkbox tidak tampil pada tabel History By Asset

### Tabel Approvals > Assignment Active tanpa Bulk
85. Tampilkan tabel Approvals > Assignment Active dengan kondisi K12
86. Verifikasi baris `ASG-2026-0070` tampil di tabel Approvals Active
87. Verifikasi kolom checkbox tidak tampil pada tabel Approvals Active

### Tabel Approvals > Assignment History tanpa Bulk
88. Tampilkan tabel Approvals > Assignment History dengan kondisi K13
89. Verifikasi baris `ASG-2026-0067` tampil di tabel Approvals History
90. Verifikasi kolom checkbox tidak tampil pada tabel Approvals History

### Tabel Assets pada Assignment Detail tanpa Bulk
91. Tampilkan tabel Assets pada Assignment Detail dengan kondisi K14
92. Verifikasi baris `LPT-2026-0021` tampil di tabel Assets Assignment Detail
93. Verifikasi kolom checkbox tidak tampil pada tabel Assets Assignment Detail
