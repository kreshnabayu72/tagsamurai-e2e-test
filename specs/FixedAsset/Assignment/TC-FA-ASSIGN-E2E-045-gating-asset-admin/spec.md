---
id: TC-FA-ASSIGN-E2E-045-gating-asset-admin
title: "Gating Asset Admin: elemen Show, Hidden, dan Disabled menurut matriks role"
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
  "§2.1#r3": [61, 63]
  "§2.1#r4": [64, 65, 67, 70]
  "§2.1#r5": [24, 34]
  "§2.1#r6": 2
  "§2.1#r7": 22
  "§2.1#r8": 23
  "§2.1#r9": 31
  "§2.1#r10": 43
  "§2.1#r11": 44
  "§2.1#r12": 53
  "§2.1#r13": 45
  "§2.1#r14": 46
  "§2.1#r15": 35
  "§2.1#r16": [15, 39, 40]
  "§4.8#r1": [1, 11]
  "§4.8#r2": 12
  "§4.8#r3": [43, 45, 49, 50]
  "§4.8#r4": 4
  "§4.8#r5": 63
  "§4.8#r6": [64, 65, 67, 70]
  "§4.8#r7": 24
  "§4.8#r8": [22, 23, 27, 28, 31, 49]
  "§4.8#r9": 44
  "§4.8#r10": 53
  "§4.8#r11": 57
  "§4.8#r12": 45
  "§4.8#r13": 46
  "§4.8#r14": 74
  "§4.8#r15": 2
  "§4.8#r16": 2
  "§4.8#r17": 35
anchor: [14, 38, 56, 60, 73]
coverage:
  web: automated
---

# Gating Asset Admin: elemen Show, Hidden, dan Disabled menurut matriks role

## Prerequisites
- Aktor: Asset Admin, user DU-045-1, mengerjakan seluruh langkah; Assignee dan pengaju adalah user lain di Data
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-045-1: User (Aktor Asset Admin), Name `Adi Pratama {runId}`, Role `Asset Admin`, Cakupan `Group penugasan Head Office {runId} beserta descendant IT Head Office {runId}`, Tampil sebagai Assignee `Adi P`
  - DU-045-2: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-045-3: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`, Tampil sebagai pengaju `Agus P`
  - DU-045-4: Group (Group utama), Name `Head Office {runId}`, Sub-group `IT Head Office {runId}`
  - DU-045-5: Group (Group cabang), Name `Branch Surabaya {runId}`
  - DU-045-6: Division (Division dengan PIC), Name `Finance {runId}`, PIC `Budi Santoso {runId}`, Anggota lain `Sari Dewi {runId}`
  - DU-045-7: Draft (Draft berisi aset satu Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Laptop Dell Latitude 5420 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-045-8: Draft (Draft berisi aset dua Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId} dan Branch Surabaya {runId}`, Aset 1 `Monitor LG 24 {runId}`, Group Aset 1 `Head Office {runId}`, Aset 2 `Toyota Avanza {runId}`, Group Aset 2 `Branch Surabaya {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-045-9: Draft (Draft berisi aset satu Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Aset `Genset Honda EU22 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-045-10: Assignment (ASG Waiting for Handover Employee), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-045-11: Assignment (ASG Waiting for Handover Division), Assignee `Finance {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Projector Epson EB-X49 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Budi Santoso {runId}`
  - DU-045-12: Assignment (ASG Waiting for Handover di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Waiting for Handover`, Aset `Tablet Samsung Tab S8 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-045-13: Assignment (ASG Waiting for Approval), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Server Dell R740 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Hendra Wijaya {runId}`
  - DU-045-14: Assignment (ASG milik aktor sebagai Assignee), Assignee `Adi Pratama {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset 1 `Scanner Canon DR-C225 {runId}`, Aset 2 `Keyboard Logitech K380 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Aset Assigned `Scanner Canon DR-C225 {runId}`, Aset Waiting for Handover `Keyboard Logitech K380 {runId}`
  - DU-045-15: Assignment (ASG Assigned dengan laporan Damaged dan Missing), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset 1 `Camera Sony A7 {runId}`, Aset 2 `Laptop Asus ExpertBook {runId}`, Aset 3 `Tablet Lenovo Tab M10 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Laporan Damaged `Laptop Asus ExpertBook {runId} dilaporkan oleh Adi Pratama {runId}, Waiting for Confirmation`, Laporan Missing `Tablet Lenovo Tab M10 {runId} dilaporkan oleh Budi Santoso {runId}, Waiting for Confirmation`
  - DU-045-16: Assignment (ASG Assigned di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Assigned`, Aset `Drone DJI Mavic 3 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-045-17: Assignment (ASG Assigned di sub-group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `IT Head Office {runId}`, Status `Assigned`, Aset `Laptop Lenovo ThinkPad T14 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-045-18: User (Approver aset DU-045-13), Name `Hendra Wijaya {runId}`, Role `Approver`, Cakupan `Group penugasan Head Office {runId} beserta descendant IT Head Office {runId}`
- Kondisi:
  - Feature Suite Assignment berada pada level `Full`

## Test Steps

### Menu Assignment di sidebar
1. Verifikasi menu `Transactions > Assignment` tampil di sidebar
2. Verifikasi menu `Approvals > Assignment` tidak tampil di sidebar

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
32. Ganti isi kotak Search dengan `Server Dell R740 {runId}`, tekan Enter
33. Buka menu ⋯ pada baris ASG yang memuat aset `Server Dell R740 {runId}`
34. Verifikasi aksi `Cancel Assignment` tampil dan aktif untuk ASG yang diajukan `Agus P`, siapa pun pengajunya
35. Verifikasi tombol `Download` tampil pada toolbar tab `Transactions`

### Aksi per aset pada tab Assigned Assets
36. Klik tab `Assigned Assets`
37. Ketik Search `{runId}`, tekan Enter
38. Verifikasi aset `Camera Sony A7 {runId}` dari ASG milik `Budi S` tampil pada By Asset
39. Verifikasi aset `Drone DJI Mavic 3 {runId}` dengan Group `Branch Surabaya {runId}` tidak tampil pada By Asset
40. Verifikasi aset `Laptop Lenovo ThinkPad T14 {runId}` dengan Group `IT Head Office {runId}` tampil pada By Asset
41. Ganti isi kotak Search dengan `Camera Sony A7 {runId}`, tekan Enter
42. Buka menu ⋯ pada baris aset `Camera Sony A7 {runId}`
43. Verifikasi aksi `Unassign` tampil dan aktif
44. Verifikasi aksi `Report Damaged` tampil dan aktif
45. Verifikasi aksi `Report Missing` tampil dan aktif
46. Verifikasi aksi `Mark as Unassigned` tidak tampil karena level Feature Suite bukan `None`
47. Ganti isi kotak Search dengan `Scanner Canon DR-C225 {runId}`, tekan Enter
48. Buka menu ⋯ pada baris aset `Scanner Canon DR-C225 {runId}`
49. Verifikasi aksi `Unassign` tampil dan aktif karena aktor Assignee ASG aset ini dapat menerimanya dengan syarat pemrosesan sendiri
50. Verifikasi aksi `Unassign` tidak memiliki alasan disabled
51. Ganti isi kotak Search dengan `Laptop Asus ExpertBook {runId}`, tekan Enter
52. Buka menu ⋯ pada baris aset `Laptop Asus ExpertBook {runId}`
53. Verifikasi aksi `Cancel Damage Report` tampil untuk laporan kerusakan milik aktor yang masih `Waiting for Confirmation`
54. Ganti isi kotak Search dengan `Tablet Lenovo Tab M10 {runId}`, tekan Enter
55. Buka menu ⋯ pada baris aset `Tablet Lenovo Tab M10 {runId}`
56. Verifikasi aksi `Assignment Log` tampil
57. Verifikasi aksi `Cancel Missing Report` tidak tampil

### Tab Drafts dan aksi Draft
58. Klik tab `Drafts`
59. Ketik Search `{runId}`, tekan Enter
60. Verifikasi Draft dengan aset `Laptop Dell Latitude 5420 {runId}` dan Group `Head Office {runId}` tampil
61. Verifikasi Draft dengan aset `Genset Honda EU22 {runId}` dan Group `Branch Surabaya {runId}` tidak tampil
62. Ganti isi kotak Search dengan `Toyota Avanza {runId}`, tekan Enter
63. Verifikasi aksi `Edit` tampil pada Draft yang memuat aset `Monitor LG 24 {runId}` dan `Toyota Avanza {runId}`
64. Verifikasi aksi `Delete` tampil Disabled pada Draft yang memuat aset `Monitor LG 24 {runId}` dan `Toyota Avanza {runId}` karena ada aset di luar Group aktor
65. Verifikasi alasan `Some assets are outside your groups. Ask another admin to delete.` tersampaikan pada aksi `Delete` yang disabled
66. Klik `Edit` pada Draft yang memuat aset `Monitor LG 24 {runId}` dan `Toyota Avanza {runId}`
67. Verifikasi tombol `[Submit]` tampil Disabled karena ada aset di luar Group aktor
68. Klik `[Cancel]` pada form yang belum diubah
69. Ganti isi kotak Search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
70. Verifikasi aksi `Delete` tampil dan aktif pada Draft yang memuat aset `Laptop Dell Latitude 5420 {runId}`

### Task Confirm Handover di My Asset
71. Buka menu Profile pada navbar
72. Klik `My Asset`
73. Verifikasi aset `Scanner Canon DR-C225 {runId}` tampil pada tab `Assigned`
74. Verifikasi Task `Confirm Handover` tidak tampil


