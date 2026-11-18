---
id: TC-FA-BORROW-E2E-030-gating-group-manager
title: "Group Manager melihat aksi Borrow dalam Group binaan menurut matriks akses dan visibilitas UI"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§2.1#r17", "§2.1#r18", "§2.1#b1", "§2.1#p6", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r18"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [6, 7, 79]
  "§2.1#r2": [44, 46, 47, 53]
  "§2.1#r3": [32, 34, 60]
  "§2.1#r4": [35, 37, 40, 42]
  "§2.1#r5": [12]
  "§2.1#r6": [72, 73]
  "§2.1#r7": [10]
  "§2.1#r8": [11]
  "§2.1#r9": [14]
  "§2.1#r10": [25]
  "§2.1#r11": [17]
  "§2.1#r12": [19]
  "§2.1#r13": [27]
  "§2.1#r14": [15]
  "§2.1#r15": [64]
  "§2.1#r16": [24]
  "§2.1#r17": [8]
  "§2.1#r18": [6, 7]
  "§2.1#b1": [68, 69]
  "§2.1#p6": [65, 72]
  "§4.8#r1": [1, 3]
  "§4.8#r2": [4, 30, 31, 32]
  "§4.8#r3": [23, 24]
  "§4.8#r4": [44, 55, 59, 60]
  "§4.8#r5": [34]
  "§4.8#r6": [35, 37, 40, 42]
  "§4.8#r7": [12]
  "§4.8#r8": [10, 15, 24]
  "§4.8#r9": [64]
  "§4.8#r10": [11]
  "§4.8#r11": [14]
  "§4.8#r12": [17]
  "§4.8#r13": [19]
  "§4.8#r14": [27]
  "§4.8#r15": [25]
  "§4.8#r16": [65]
  "§4.8#r17": [72]
  "§4.8#r18": [8]
anchor: [63]
coverage:
  web: automated
---

# Group Manager melihat aksi Borrow dalam Group binaan menurut matriks akses dan visibilitas UI

## Prerequisites
- Aktor: Group Manager (cakupan Group binaan `Head Office {runId}`).
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-030-1: User `Siti Aminah {runId}`, role Group Manager, Group binaan `Head Office {runId}`, aktif.
  - DU-030-2: User `Rina Wulandari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-030-3: Karyawan `Rudi Hartono {runId}`, aktif, Home Group `Head Office {runId}`.
  - DU-030-4: Karyawan `Dewi Lestari {runId}`, aktif, Home Group `Branch Surabaya {runId}`.
  - DU-030-5: Group `Head Office {runId}`, dibina `Siti Aminah {runId}`.
  - DU-030-6: Group `Branch Surabaya {runId}`, tidak dibina `Siti Aminah {runId}`.
  - DU-030-7: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-030-8: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Rina Wulandari {runId}`.
  - DU-030-9: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Rina Wulandari {runId}`.
  - DU-030-10: BRW berstatus Extension Approval (Extend menunggu approval), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Projector Epson EB-X06 {runId}`, Duration `4 days`, Purpose `Presentasi vendor`, Requested By `Rina Wulandari {runId}`.
  - DU-030-11: BRW berstatus Extension Request (pengajuan Extend dari My Asset menunggu review), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Printer Canon G3010 {runId}`, Duration `4 days`, Purpose `Cetak dokumen audit`, Requested By `Rina Wulandari {runId}`.
  - DU-030-12: BRW berstatus Borrowed dengan Damage Report Waiting for Confirmation yang dilaporkan `Siti Aminah {runId}`, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Excavator Komatsu PC200 {runId}`, Duration `6 days`, Purpose `Pekerjaan galian`, Requested By `Rina Wulandari {runId}`.
  - DU-030-13: BRW berstatus Waiting for Approval yang approval-nya dirutekan ke `Siti Aminah {runId}` karena tidak ada approver eligible (alasan `No eligible approver`), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Meeting Mic Set {runId}`, Duration `2 days`, Purpose `Rapat tahunan`, Requested By `Rina Wulandari {runId}`.
  - DU-030-14: BRW berstatus Waiting for Approval yang diajukan aktor sendiri, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Whiteboard Digital {runId}`, Duration `2 days`, Purpose `Workshop tim`, Requested By `Siti Aminah {runId}`.
  - DU-030-15: BRW berstatus Borrowed, Group `Branch Surabaya {runId}`, Borrower `Dewi Lestari {runId}`, aset `Genset Perkins 20 kVA {runId}`, Duration `7 days`, Purpose `Cadangan listrik`, Requested By `Rina Wulandari {runId}`.
  - DU-030-16: Draft milik Borrower `Rudi Hartono {runId}`, berisi aset `Scanner Epson DS-530 {runId}` (Group `Head Office {runId}`) dan aset `Forklift Toyota 8FD {runId}` (Group `Branch Surabaya {runId}`), Total Asset `2`, Modified By `Rina Wulandari {runId}`.
  - DU-030-17: Draft milik Borrower `Dewi Lestari {runId}`, berisi aset `Mixer Beton Portable {runId}` (Group `Head Office {runId}`), Total Asset `1`, Modified By `Rina Wulandari {runId}`.
  - DU-030-18: Draft milik Borrower `Dewi Lestari {runId}`, berisi aset `Compressor Atlas Copco {runId}` (Group `Branch Surabaya {runId}`), Total Asset `1`, Modified By `Rina Wulandari {runId}`.
  - DU-030-19: Draft baru untuk Borrower `Rudi Hartono {runId}` tanpa aset, dibuat `Siti Aminah {runId}` lewat langkah spec.
- Kondisi:
  - Level Feature Suite Borrowing entitas aktor bernilai `Full`.

## Test Steps

### Menu dan tab Borrow tampil
1. Verifikasi menu `Transactions > Borrow` tampil di sidebar
2. Klik menu `Transactions > Borrow`
3. Verifikasi tab `Transactions`, `Borrowed Assets`, dan `History` tampil
4. Verifikasi tab `Drafts` tampil

### BRW dalam Group binaan tampil dan BRW di luar Group binaan tidak tampil
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi BRW milik DU-030-8 dengan Group `Head Office {runId}` tampil di tabel
7. Verifikasi BRW milik DU-030-15 dengan Group `Branch Surabaya {runId}` tidak tampil di tabel
8. Verifikasi `Download` tampil di toolbar tab `Transactions`

### Aksi baris BRW yang Waiting for Handover
9. Buka menu ⋯ pada baris BRW milik DU-030-8
10. Verifikasi aksi `Hand Over` tampil dan aktif
11. Verifikasi aksi `Remind Borrower` tampil dan aktif
12. Verifikasi aksi `Cancel Borrow` tampil dan aktif

### Aksi baris BRW yang Borrowed
13. Buka menu ⋯ pada baris BRW milik DU-030-9
14. Verifikasi aksi `Request Extension` tampil dan aktif
15. Verifikasi aksi `Return` tampil dan aktif

### Aksi baris BRW dengan Extension Approval
16. Buka menu ⋯ pada baris BRW milik DU-030-10
17. Verifikasi aksi `Cancel Extension` tampil dan aktif

### Aksi baris BRW dengan Extension Request dari My Asset
18. Buka menu ⋯ pada baris BRW milik DU-030-11
19. Verifikasi aksi `Review` tampil dan aktif

### Aksi per aset di tab Borrowed Assets
20. Klik tab `Borrowed Assets`
21. Ketik Search `{runId}`, tekan Enter
22. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
23. Verifikasi aksi `Return` tampil dan aktif
24. Verifikasi aksi `Report Missing` tampil dan aktif
25. Verifikasi aksi `Report Damaged` tampil dan aktif
26. Buka menu ⋯ pada baris aset `Excavator Komatsu PC200 {runId}`
27. Verifikasi aksi `Cancel Damage Report` tampil dan aktif

### Draft berisi aset Group binaan tampil, dapat diedit, dan Submit serta Delete dibatasi aset di luar Group binaan
28. Klik tab `Drafts`
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi Draft milik DU-030-17 dengan Total Asset `1` tampil di tabel
31. Verifikasi Draft milik DU-030-16 dengan Total Asset `2` tampil di tabel
32. Verifikasi Draft milik DU-030-18 tidak tampil di tabel
33. Buka menu ⋯ pada baris Draft milik DU-030-17
34. Verifikasi aksi `Edit` tampil dan aktif
35. Verifikasi aksi `Delete` tampil dan aktif
36. Klik `Edit`
37. Verifikasi tombol `[Submit]` tampil dan aktif pada Draft yang semua asetnya ada di Group binaan
38. Klik `[Cancel]` pada form; form belum diubah sehingga dialog Unsaved Changes tidak muncul
39. Buka menu ⋯ pada baris Draft milik DU-030-16
40. Verifikasi aksi `Delete` tampil dalam keadaan disabled dengan alasan yang menyebut siapa yang dapat dihubungi
41. Klik `Edit`
42. Verifikasi tombol `[Submit]` tampil dalam keadaan disabled dengan alasan yang menyebut siapa yang dapat dihubungi
43. Klik `[Cancel]` pada form; form belum diubah sehingga dialog Unsaved Changes tidak muncul

### Create dan Save Draft
44. Verifikasi tombol `[+ Borrow]` tampil di toolbar tab `Drafts`
45. Klik `[+ Borrow]`
46. Verifikasi tombol `[Save Draft]` tampil di form `Borrow Request`
47. Verifikasi tombol `[Submit]` tampil di form `Borrow Request`
48. Klik `[Select Borrower]`
49. Pilih Borrower `Rudi Hartono {runId}` pada dialog Select Borrower
50. Klik `[Save Draft]`
51. Klik `Draft` pada breadcrumb sehingga tab `Drafts` tampil
52. Ketik Search `{runId}`, tekan Enter
53. Verifikasi Draft baru untuk Borrower `Rudi Hartono {runId}` dengan Total Asset `0` tampil di tabel

### Titik masuk Quick Action dan Asset List
54. Buka menu Quick Action pada navbar
55. Verifikasi item `Borrow` tampil di menu Quick Action
56. Klik menu `Assets > All`
57. Ketik Search `{runId}`, tekan Enter
58. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
59. Verifikasi aksi `Borrow` tampil dan aktif
60. Verifikasi aksi `Add to Borrow Draft` tampil dan aktif

### Mark as Returned tidak tampil pada level Full
61. Ganti isi kotak search dengan `Toyota Avanza {runId}`, tekan Enter
62. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
63. Verifikasi aset `Toyota Avanza {runId}` di Group binaan berstatus `Borrowed` tampil di tabel aset
64. Verifikasi aksi `Mark as Returned` tidak tampil karena level Feature Suite Borrowing bukan `None`

### Menu Approvals > Borrow dan keputusan atas aset yang eligible
65. Verifikasi menu `Approvals > Borrow` tampil di sidebar
66. Klik menu `Approvals > Borrow`
67. Ketik Search `{runId}`, tekan Enter
68. Verifikasi pengajuan BRW milik DU-030-13 tampil di tab `Active`
69. Verifikasi pengajuan BRW milik DU-030-14 yang diajukan `Siti Aminah {runId}` sendiri tidak tampil di tab `Active`
70. Buka menu ⋯ pada baris pengajuan BRW milik DU-030-13
71. Klik `Review`
72. Verifikasi pilihan keputusan `Approve` dan `Reject` tampil dan dapat dipilih untuk aset `Meeting Mic Set {runId}`
73. Verifikasi tombol `[Submit]` tampil di footer halaman Review
74. Klik `[Cancel]` pada halaman Review; keputusan belum diisi sehingga tidak ada yang tersimpan

### Detail BRW dapat dibuka
75. Klik menu `Transactions > Borrow`
76. Ketik Search `{runId}`, tekan Enter
77. Buka menu ⋯ pada baris BRW milik DU-030-8
78. Klik `Detail`
79. Verifikasi halaman Borrow Detail BRW milik DU-030-8 terbuka dengan Borrower `Rudi Hartono {runId}`
