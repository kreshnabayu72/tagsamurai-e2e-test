---
id: TC-FA-BORROW-E2E-031-gating-asset-admin
title: "Asset Admin melihat aksi Borrow dalam Group penugasan menurut matriks akses dan visibilitas UI"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§2.1#r17", "§2.1#r18", "§2.1#b2", "§2.1#p5", "§2.1#p7", "§2.1#p8", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r18"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [7, 8, 70]
  "§2.1#r2": [45, 47, 48, 54]
  "§2.1#r3": [33, 35, 61]
  "§2.1#r4": [36, 38, 41, 43]
  "§2.1#r5": [13]
  "§2.1#r6": [2]
  "§2.1#r7": [11]
  "§2.1#r8": [12]
  "§2.1#r9": [15]
  "§2.1#r10": [26]
  "§2.1#r11": [18]
  "§2.1#r12": [20]
  "§2.1#r13": [28]
  "§2.1#r14": [16]
  "§2.1#r15": [65]
  "§2.1#r16": [25]
  "§2.1#r17": [9]
  "§2.1#r18": [7, 8, 73]
  "§2.1#b2": [45, 60, 79, 80]
  "§2.1#p5": [13]
  "§2.1#p7": [2]
  "§2.1#p8": [2]
  "§4.8#r1": [1, 4]
  "§4.8#r2": [5, 31, 32, 33]
  "§4.8#r3": [24, 25]
  "§4.8#r4": [45, 56, 60, 61]
  "§4.8#r5": [35]
  "§4.8#r6": [36, 38, 41, 43]
  "§4.8#r7": [13]
  "§4.8#r8": [11, 16, 25]
  "§4.8#r9": [65]
  "§4.8#r10": [12]
  "§4.8#r11": [15]
  "§4.8#r12": [18]
  "§4.8#r13": [20]
  "§4.8#r14": [28]
  "§4.8#r15": [26]
  "§4.8#r16": [2]
  "§4.8#r17": [2]
  "§4.8#r18": [9]
anchor: [64, 78]
coverage:
  web: automated
---

# Asset Admin melihat aksi Borrow dalam Group penugasan menurut matriks akses dan visibilitas UI

## Prerequisites
- Aktor: Asset Admin (cakupan Group penugasan `Head Office {runId}`), dan pemegang hak Update Manage asset & TAG saja `Bagas Prasetyo {runId}`.
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-031-1: User `Agus Pratama {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-031-2: User `Lina Sari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-031-3: User `Siti Aminah {runId}`, role Group Manager, Group binaan `Head Office {runId}`, aktif.
  - DU-031-4: Karyawan `Rudi Hartono {runId}`, aktif, Home Group `Head Office {runId}`.
  - DU-031-5: Karyawan `Dewi Lestari {runId}`, aktif, Home Group `Branch Surabaya {runId}`.
  - DU-031-6: Group `Head Office {runId}`, penugasan `Agus Pratama {runId}`.
  - DU-031-7: Group `Branch Surabaya {runId}`, bukan penugasan `Agus Pratama {runId}`.
  - DU-031-8: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-031-9: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Lina Sari {runId}`.
  - DU-031-10: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Lina Sari {runId}`.
  - DU-031-11: BRW berstatus Extension Approval (Extend menunggu approval), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Projector Epson EB-X06 {runId}`, Duration `4 days`, Purpose `Presentasi vendor`, Requested By `Lina Sari {runId}`.
  - DU-031-12: BRW berstatus Extension Request (pengajuan Extend dari My Asset menunggu review), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Printer Canon G3010 {runId}`, Duration `4 days`, Purpose `Cetak dokumen audit`, Requested By `Lina Sari {runId}`.
  - DU-031-13: BRW berstatus Borrowed dengan Damage Report Waiting for Confirmation yang dilaporkan `Agus Pratama {runId}`, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Excavator Komatsu PC200 {runId}`, Duration `6 days`, Purpose `Pekerjaan galian`, Requested By `Lina Sari {runId}`.
  - DU-031-14: BRW berstatus Waiting for Approval yang approval-nya dirutekan ke `Siti Aminah {runId}` karena tidak ada approver eligible (alasan `No eligible approver`), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Meeting Mic Set {runId}`, Duration `2 days`, Purpose `Rapat tahunan`, Requested By `Lina Sari {runId}`.
  - DU-031-15: BRW berstatus Borrowed, Group `Branch Surabaya {runId}`, Borrower `Dewi Lestari {runId}`, aset `Genset Perkins 20 kVA {runId}`, Duration `7 days`, Purpose `Cadangan listrik`, Requested By `Lina Sari {runId}`.
  - DU-031-16: Draft milik Borrower `Rudi Hartono {runId}`, berisi aset `Scanner Epson DS-530 {runId}` (Group `Head Office {runId}`) dan aset `Forklift Toyota 8FD {runId}` (Group `Branch Surabaya {runId}`), Total Asset `2`, Modified By `Lina Sari {runId}`.
  - DU-031-17: Draft milik Borrower `Dewi Lestari {runId}`, berisi aset `Mixer Beton Portable {runId}` (Group `Head Office {runId}`), Total Asset `1`, Modified By `Lina Sari {runId}`.
  - DU-031-18: Draft milik Borrower `Dewi Lestari {runId}`, berisi aset `Compressor Atlas Copco {runId}` (Group `Branch Surabaya {runId}`), Total Asset `1`, Modified By `Lina Sari {runId}`.
  - DU-031-19: Draft baru untuk Borrower `Rudi Hartono {runId}` tanpa aset, dibuat `Agus Pratama {runId}` lewat langkah spec.
  - DU-031-20: Group `IT Support {runId}`, turunan dari Group penugasan `Head Office {runId}`.
  - DU-031-21: BRW berstatus Waiting for Handover, Group `IT Support {runId}`, Borrower `Rudi Hartono {runId}`, aset `Server Dell PowerEdge R740 {runId}`, Duration `2 days`, Purpose `Migrasi server`, Requested By `Lina Sari {runId}`.
  - DU-031-22: User `Bagas Prasetyo {runId}`, hanya memegang hak Update Manage asset & TAG (bukan Total Control, Group Manager, maupun Asset Admin), Group `Head Office {runId}`, aktif.
- Kondisi:
  - Level Feature Suite Borrowing entitas aktor bernilai `Full`.
  - Akun `Bagas Prasetyo {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Menu Borrow tampil dan menu Approvals > Borrow tidak tampil
1. Verifikasi menu `Transactions > Borrow` tampil di sidebar
2. Verifikasi menu `Approvals > Borrow` tidak tampil di sidebar
3. Klik menu `Transactions > Borrow`
4. Verifikasi tab `Transactions`, `Borrowed Assets`, dan `History` tampil
5. Verifikasi tab `Drafts` tampil

### BRW dalam Group penugasan tampil dan BRW di luar Group penugasan tidak tampil
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi BRW milik DU-031-9 dengan Group `Head Office {runId}` tampil di tabel
8. Verifikasi BRW milik DU-031-15 dengan Group `Branch Surabaya {runId}` tidak tampil di tabel
9. Verifikasi `Download` tampil di toolbar tab `Transactions`

### Aksi baris BRW yang Waiting for Handover dan diajukan Asset Admin lain
10. Buka menu ⋯ pada baris BRW milik DU-031-9
11. Verifikasi aksi `Hand Over` tampil dan aktif
12. Verifikasi aksi `Remind Borrower` tampil dan aktif
13. Verifikasi aksi `Cancel Borrow` tampil dan aktif untuk BRW yang diajukan `Lina Sari {runId}`

### Aksi baris BRW yang Borrowed
14. Buka menu ⋯ pada baris BRW milik DU-031-10
15. Verifikasi aksi `Request Extension` tampil dan aktif
16. Verifikasi aksi `Return` tampil dan aktif

### Aksi baris BRW dengan Extension Approval yang diajukan Asset Admin lain
17. Buka menu ⋯ pada baris BRW milik DU-031-11
18. Verifikasi aksi `Cancel Extension` tampil dan aktif untuk BRW yang diajukan `Lina Sari {runId}`

### Aksi baris BRW dengan Extension Request dari My Asset
19. Buka menu ⋯ pada baris BRW milik DU-031-12
20. Verifikasi aksi `Review` tampil dan aktif

### Aksi per aset di tab Borrowed Assets
21. Klik tab `Borrowed Assets`
22. Ketik Search `{runId}`, tekan Enter
23. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
24. Verifikasi aksi `Return` tampil dan aktif
25. Verifikasi aksi `Report Missing` tampil dan aktif
26. Verifikasi aksi `Report Damaged` tampil dan aktif
27. Buka menu ⋯ pada baris aset `Excavator Komatsu PC200 {runId}`
28. Verifikasi aksi `Cancel Damage Report` tampil dan aktif

### Draft berisi aset Group penugasan tampil siapa pun pembuatnya, dan Submit serta Delete dibatasi aset di luar Group penugasan
29. Klik tab `Drafts`
30. Ketik Search `{runId}`, tekan Enter
31. Verifikasi Draft milik DU-031-17 dengan Total Asset `1` tampil di tabel
32. Verifikasi Draft milik DU-031-16 dengan Total Asset `2` tampil di tabel
33. Verifikasi Draft milik DU-031-18 tidak tampil di tabel
34. Buka menu ⋯ pada baris Draft milik DU-031-17
35. Verifikasi aksi `Edit` tampil dan aktif
36. Verifikasi aksi `Delete` tampil dan aktif
37. Klik `Edit`
38. Verifikasi tombol `[Submit]` tampil dan aktif pada Draft yang semua asetnya ada di Group penugasan
39. Klik `[Cancel]` pada form; form belum diubah sehingga dialog Unsaved Changes tidak muncul
40. Buka menu ⋯ pada baris Draft milik DU-031-16
41. Verifikasi aksi `Delete` tampil dalam keadaan disabled dengan alasan yang menyebut siapa yang dapat dihubungi
42. Klik `Edit`
43. Verifikasi tombol `[Submit]` tampil dalam keadaan disabled dengan alasan yang menyebut siapa yang dapat dihubungi
44. Klik `[Cancel]` pada form; form belum diubah sehingga dialog Unsaved Changes tidak muncul

### Create dan Save Draft
45. Verifikasi tombol `[+ Borrow]` tampil di toolbar tab `Drafts`
46. Klik `[+ Borrow]`
47. Verifikasi tombol `[Save Draft]` tampil di form `Borrow Request`
48. Verifikasi tombol `[Submit]` tampil di form `Borrow Request`
49. Klik `[Select Borrower]`
50. Pilih Borrower `Rudi Hartono {runId}` pada dialog Select Borrower
51. Klik `[Save Draft]`
52. Klik `Draft` pada breadcrumb sehingga tab `Drafts` tampil
53. Ketik Search `{runId}`, tekan Enter
54. Verifikasi Draft baru untuk Borrower `Rudi Hartono {runId}` dengan Total Asset `0` tampil di tabel

### Titik masuk Quick Action dan Asset List
55. Buka menu Quick Action pada navbar
56. Verifikasi item `Borrow` tampil di menu Quick Action
57. Klik menu `Assets > All`
58. Ketik Search `{runId}`, tekan Enter
59. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
60. Verifikasi aksi `Borrow` tampil dan aktif
61. Verifikasi aksi `Add to Borrow Draft` tampil dan aktif

### Mark as Returned tidak tampil pada level Full
62. Ganti isi kotak search dengan `Toyota Avanza {runId}`, tekan Enter
63. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
64. Verifikasi aset `Toyota Avanza {runId}` di Group penugasan berstatus `Borrowed` tampil di tabel aset
65. Verifikasi aksi `Mark as Returned` tidak tampil karena level Feature Suite Borrowing bukan `None`

### BRW yang menunggu approval dapat dibuka dari halaman Borrow
66. Klik menu `Transactions > Borrow`
67. Ketik Search `{runId}`, tekan Enter
68. Buka menu ⋯ pada baris BRW milik DU-031-14
69. Klik `Detail`
70. Verifikasi halaman Borrow Detail BRW milik DU-031-14 dengan status `Waiting for Approval` terbuka

### BRW dalam Group turunan dari Group penugasan tampil
71. Klik menu `Transactions > Borrow`
72. Ketik Search `{runId}`, tekan Enter
73. Verifikasi BRW milik DU-031-21 dengan Group `IT Support {runId}`, turunan dari `Head Office {runId}`, tampil di tabel

### Pemegang hak Update Manage asset & TAG saja bukan Aktor Borrow
74. Masuk sebagai `Bagas Prasetyo {runId}`
75. Klik menu `Assets > All`
76. Ketik Search `{runId}`, tekan Enter
77. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
78. Verifikasi baris aset `Laptop Lenovo T14 {runId}` tampil di tabel aset
79. Verifikasi aksi `Borrow` tidak tampil bagi pemegang hak Update Manage asset & TAG saja
80. Verifikasi aksi `Add to Borrow Draft` tidak tampil bagi pemegang hak Update Manage asset & TAG saja
