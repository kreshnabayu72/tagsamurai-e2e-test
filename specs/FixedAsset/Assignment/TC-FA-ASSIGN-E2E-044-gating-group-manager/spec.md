---
id: TC-FA-ASSIGN-E2E-044-gating-group-manager
title: "Gating Group Manager: elemen Show, Hidden, dan Disabled menurut matriks role"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [15, 18]
  "§2.1#r2": [6, 7, 8]
  "§2.1#r3": [58, 60]
  "§2.1#r4": [61, 62, 64, 67]
  "§2.1#r5": 24
  "§2.1#r6": 72
  "§2.1#r7": 22
  "§2.1#r8": 23
  "§2.1#r9": 31
  "§2.1#r10": 40
  "§2.1#r11": 41
  "§2.1#r12": 50
  "§2.1#r13": 42
  "§2.1#r14": 43
  "§2.1#r15": 32
  "§2.1#r16": [15, 36, 37]
  "§4.8#r1": [1, 11]
  "§4.8#r2": 12
  "§4.8#r3": [40, 42, 46, 47]
  "§4.8#r4": [4, 79]
  "§4.8#r5": 60
  "§4.8#r6": [61, 62, 64, 67]
  "§4.8#r7": 24
  "§4.8#r8": [22, 23, 27, 28, 31, 46]
  "§4.8#r9": 41
  "§4.8#r10": 50
  "§4.8#r11": 54
  "§4.8#r12": 42
  "§4.8#r13": 43
  "§4.8#r14": 77
  "§4.8#r15": 2
  "§4.8#r16": 72
  "§4.8#r17": 32
anchor: [14, 35, 53, 57, 70, 76]
coverage:
  web: automated
---

# Gating Group Manager: elemen Show, Hidden, dan Disabled menurut matriks role

## Prerequisites
- Aktor: Group Manager, user DU-044-1, mengerjakan seluruh langkah; Assignee dan pengaju adalah user lain di Data
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-044-1: User (Aktor Group Manager), Name `Gina Mahendra {runId}`, Role `Group Manager`, Cakupan `Group binaan Head Office {runId} beserta sub-group IT Head Office {runId}`, Tampil sebagai Assignee `Gina M`
  - DU-044-2: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-044-3: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`, Tampil sebagai pengaju `Agus P`
  - DU-044-4: Group (Group utama), Name `Head Office {runId}`, Sub-group `IT Head Office {runId}`
  - DU-044-5: Group (Group cabang), Name `Branch Surabaya {runId}`
  - DU-044-6: Division (Division dengan PIC), Name `Finance {runId}`, PIC `Budi Santoso {runId}`, Anggota lain `Sari Dewi {runId}`
  - DU-044-7: Draft (Draft berisi aset satu Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Laptop Dell Latitude 5420 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-044-8: Draft (Draft berisi aset dua Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId} dan Branch Surabaya {runId}`, Aset 1 `Monitor LG 24 {runId}`, Group Aset 1 `Head Office {runId}`, Aset 2 `Toyota Avanza {runId}`, Group Aset 2 `Branch Surabaya {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-044-9: Draft (Draft berisi aset satu Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Aset `Genset Honda EU22 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-044-10: Assignment (ASG Waiting for Handover Employee), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-044-11: Assignment (ASG Waiting for Handover Division), Assignee `Finance {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Projector Epson EB-X49 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Budi Santoso {runId}`
  - DU-044-12: Assignment (ASG Waiting for Handover di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Waiting for Handover`, Aset `Tablet Samsung Tab S8 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-044-13: Assignment (ASG Waiting for Approval), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Server Dell R740 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Gina Mahendra {runId}`
  - DU-044-14: Assignment (ASG milik aktor sebagai Assignee), Assignee `Gina Mahendra {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset 1 `Scanner Canon DR-C225 {runId}`, Aset 2 `Keyboard Logitech K380 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Aset Assigned `Scanner Canon DR-C225 {runId}`, Aset Waiting for Handover `Keyboard Logitech K380 {runId}`
  - DU-044-15: Assignment (ASG Assigned dengan laporan Damaged dan Missing), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset 1 `Camera Sony A7 {runId}`, Aset 2 `Laptop Asus ExpertBook {runId}`, Aset 3 `Tablet Lenovo Tab M10 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Laporan Damaged `Laptop Asus ExpertBook {runId} dilaporkan oleh Gina Mahendra {runId}, Waiting for Confirmation`, Laporan Missing `Tablet Lenovo Tab M10 {runId} dilaporkan oleh Budi Santoso {runId}, Waiting for Confirmation`
  - DU-044-16: Assignment (ASG Assigned di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Assigned`, Aset `Drone DJI Mavic 3 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-044-17: Assignment (ASG Assigned di sub-group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `IT Head Office {runId}`, Status `Assigned`, Aset `Laptop Lenovo ThinkPad T14 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
- Kondisi:
  - Feature Suite Assignment berada pada level `Full`
  - Aturan approval aset `Server Dell R740 {runId}` menunjuk aktor sebagai approver; pengaju bukan aktor

## Test Steps

### Menu Assignment di sidebar
1. Verifikasi menu `Transactions > Assignment` tampil di sidebar
2. Verifikasi menu `Approvals > Assignment` tampil di sidebar

### Quick Action Assign membuka form Assignment Request
3. Klik Quick Action pada navbar
4. Verifikasi item `Assign` tampil pada menu Quick Action
5. Klik `Assign`
6. Verifikasi form `Assignment Request` terbuka
7. Verifikasi tombol `[Save Draft]` tampil
8. Verifikasi tombol `[Submit]` tampil
9. Klik `[Cancel]` pada form yang belum diubah

### Daftar dan Detail ASG sesuai cakupan
10. Klik menu `Transactions > Assignment`
11. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tampil
12. Verifikasi tab `Drafts` tampil
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi ASG dengan Group `Head Office {runId}` tampil pada daftar
15. Verifikasi ASG dengan Group `Branch Surabaya {runId}` tidak tampil pada daftar
16. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
17. Klik Transaction ID pada baris ASG yang memuat aset `Printer HP M404 {runId}`
18. Verifikasi Assignment Detail terbuka dan memuat aset `Printer HP M404 {runId}`

### Aksi baris ASG pada tab Transactions
19. Klik menu `Transactions > Assignment`
20. Ketik Search `Printer HP M404 {runId}`, tekan Enter
21. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
22. Verifikasi aksi `Hand Over` tampil dan aktif
23. Verifikasi aksi `Remind Assignee` tampil dan aktif
24. Verifikasi aksi `Cancel Assignment` tampil dan aktif
25. Ganti isi kotak Search dengan `Keyboard Logitech K380 {runId}`, tekan Enter
26. Buka menu ⋯ pada baris ASG yang memuat aset `Keyboard Logitech K380 {runId}`
27. Verifikasi aksi `Hand Over` tampil dan aktif karena aktor Assignee ASG ini dapat memprosesnya dengan syarat pemrosesan sendiri
28. Verifikasi aksi `Remind Assignee` tampil dan aktif untuk aktor Assignee ASG ini
29. Ganti isi kotak Search dengan `Projector Epson EB-X49 {runId}`, tekan Enter
30. Buka menu ⋯ pada baris ASG yang memuat aset `Projector Epson EB-X49 {runId}`
31. Verifikasi aksi `Change PIC` tampil dan aktif
32. Verifikasi tombol `Download` tampil pada toolbar tab `Transactions`

### Aksi per aset pada tab Assigned Assets
33. Klik tab `Assigned Assets`
34. Ketik Search `{runId}`, tekan Enter
35. Verifikasi aset `Camera Sony A7 {runId}` dari ASG milik `Budi S` tampil pada By Asset
36. Verifikasi aset `Drone DJI Mavic 3 {runId}` dengan Group `Branch Surabaya {runId}` tidak tampil pada By Asset
37. Verifikasi aset `Laptop Lenovo ThinkPad T14 {runId}` dengan Group `IT Head Office {runId}` tampil pada By Asset
38. Ganti isi kotak Search dengan `Camera Sony A7 {runId}`, tekan Enter
39. Buka menu ⋯ pada baris aset `Camera Sony A7 {runId}`
40. Verifikasi aksi `Unassign` tampil dan aktif
41. Verifikasi aksi `Report Damaged` tampil dan aktif
42. Verifikasi aksi `Report Missing` tampil dan aktif
43. Verifikasi aksi `Mark as Unassigned` tidak tampil karena level Feature Suite bukan `None`
44. Ganti isi kotak Search dengan `Scanner Canon DR-C225 {runId}`, tekan Enter
45. Buka menu ⋯ pada baris aset `Scanner Canon DR-C225 {runId}`
46. Verifikasi aksi `Unassign` tampil dan aktif karena aktor Assignee ASG aset ini dapat menerimanya dengan syarat pemrosesan sendiri
47. Verifikasi aksi `Unassign` tidak memiliki alasan disabled
48. Ganti isi kotak Search dengan `Laptop Asus ExpertBook {runId}`, tekan Enter
49. Buka menu ⋯ pada baris aset `Laptop Asus ExpertBook {runId}`
50. Verifikasi aksi `Cancel Damage Report` tampil untuk laporan kerusakan milik aktor yang masih `Waiting for Confirmation`
51. Ganti isi kotak Search dengan `Tablet Lenovo Tab M10 {runId}`, tekan Enter
52. Buka menu ⋯ pada baris aset `Tablet Lenovo Tab M10 {runId}`
53. Verifikasi aksi `Assignment Log` tampil
54. Verifikasi aksi `Cancel Missing Report` tidak tampil

### Tab Drafts dan aksi Draft
55. Klik tab `Drafts`
56. Ketik Search `{runId}`, tekan Enter
57. Verifikasi Draft dengan aset `Laptop Dell Latitude 5420 {runId}` dan Group `Head Office {runId}` tampil
58. Verifikasi Draft dengan aset `Genset Honda EU22 {runId}` dan Group `Branch Surabaya {runId}` tidak tampil
59. Ganti isi kotak Search dengan `Toyota Avanza {runId}`, tekan Enter
60. Verifikasi aksi `Edit` tampil pada Draft yang memuat aset `Monitor LG 24 {runId}` dan `Toyota Avanza {runId}`
61. Verifikasi aksi `Delete` tampil Disabled pada Draft yang memuat aset `Monitor LG 24 {runId}` dan `Toyota Avanza {runId}` karena ada aset di luar Group aktor
62. Verifikasi alasan `Some assets are outside your groups. Ask another admin to delete.` tersampaikan pada aksi `Delete` yang disabled
63. Klik `Edit` pada Draft yang memuat aset `Monitor LG 24 {runId}` dan `Toyota Avanza {runId}`
64. Verifikasi tombol `[Submit]` tampil Disabled karena ada aset di luar Group aktor
65. Klik `[Cancel]` pada form yang belum diubah
66. Ganti isi kotak Search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
67. Verifikasi aksi `Delete` tampil dan aktif pada Draft yang memuat aset `Laptop Dell Latitude 5420 {runId}`

### Antrean Approvals > Assignment dan keputusan per aset
68. Klik menu `Approvals > Assignment`
69. Ketik Search `{runId}`, tekan Enter
70. Verifikasi pengajuan dengan Assignee `Budi S` dan Group `Head Office {runId}` tampil pada tab `Active`
71. Klik `Review` pada pengajuan dengan Assignee `Budi S`
72. Verifikasi pilihan `Approve` dan `Reject` tampil pada kolom `Approval` aset `Server Dell R740 {runId}`
73. Klik `[Cancel]` pada footer halaman Review tanpa memutuskan

### Task Confirm Handover di My Asset
74. Buka menu Profile pada navbar
75. Klik `My Asset`
76. Verifikasi aset `Scanner Canon DR-C225 {runId}` tampil pada tab `Assigned`
77. Verifikasi Task `Confirm Handover` tidak tampil

### Tombol `[+ Assign]` pada toolbar tab Transactions
78. Klik menu `Transactions > Assignment`
79. Verifikasi tombol `[+ Assign]` tampil pada toolbar tab `Transactions`


