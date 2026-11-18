---
id: TC-FA-BORROW-E2E-029-gating-total-control
title: "Total Control melihat aksi Borrow menurut matriks akses dan visibilitas UI"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§2.1#r17", "§2.1#r18", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r18"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [6, 7, 70]
  "§2.1#r2": [37, 39, 40, 46]
  "§2.1#r3": [32, 53]
  "§2.1#r4": [33, 35]
  "§2.1#r5": [12]
  "§2.1#r6": [63, 64]
  "§2.1#r7": [10]
  "§2.1#r8": [11]
  "§2.1#r9": [14]
  "§2.1#r10": [25]
  "§2.1#r11": [17]
  "§2.1#r12": [19]
  "§2.1#r13": [27]
  "§2.1#r14": [15]
  "§2.1#r15": [57]
  "§2.1#r16": [24]
  "§2.1#r17": [8]
  "§2.1#r18": [6, 7]
  "§4.8#r1": [1, 3]
  "§4.8#r2": [4, 30]
  "§4.8#r3": [23, 24]
  "§4.8#r4": [37, 48, 52, 53]
  "§4.8#r5": [32]
  "§4.8#r6": [33, 35]
  "§4.8#r7": [12]
  "§4.8#r8": [10, 15, 24]
  "§4.8#r9": [57]
  "§4.8#r10": [11]
  "§4.8#r11": [14]
  "§4.8#r12": [17]
  "§4.8#r13": [19]
  "§4.8#r14": [27]
  "§4.8#r15": [25]
  "§4.8#r16": [58]
  "§4.8#r17": [63]
  "§4.8#r18": [8]
anchor: [56]
coverage:
  web: automated
---

# Total Control melihat aksi Borrow menurut matriks akses dan visibilitas UI

## Prerequisites
- Aktor: Total Control (cakupan seluruh client).
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-029-1: User `Maya Putri {runId}`, role Total Control, cakupan seluruh client, aktif.
  - DU-029-2: User `Rina Wulandari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-029-3: Karyawan `Rudi Hartono {runId}`, aktif, Home Group `Head Office {runId}`.
  - DU-029-4: Karyawan `Dewi Lestari {runId}`, aktif, Home Group `Branch Surabaya {runId}`.
  - DU-029-5: Group `Head Office {runId}`.
  - DU-029-6: Group `Branch Surabaya {runId}`.
  - DU-029-7: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-029-8: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Rina Wulandari {runId}`.
  - DU-029-9: BRW berstatus Borrowed, Group `Branch Surabaya {runId}`, Borrower `Dewi Lestari {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Rina Wulandari {runId}`.
  - DU-029-10: BRW berstatus Extension Approval (Extend menunggu approval), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Projector Epson EB-X06 {runId}`, Duration `4 days`, Purpose `Presentasi vendor`, Requested By `Rina Wulandari {runId}`.
  - DU-029-11: BRW berstatus Extension Request (pengajuan Extend dari My Asset menunggu review), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Printer Canon G3010 {runId}`, Duration `4 days`, Purpose `Cetak dokumen audit`, Requested By `Rina Wulandari {runId}`.
  - DU-029-12: BRW berstatus Borrowed dengan Damage Report Waiting for Confirmation yang dilaporkan `Maya Putri {runId}`, Group `Branch Surabaya {runId}`, Borrower `Dewi Lestari {runId}`, aset `Excavator Komatsu PC200 {runId}`, Duration `6 days`, Purpose `Pekerjaan galian`, Requested By `Rina Wulandari {runId}`.
  - DU-029-13: BRW berstatus Waiting for Approval, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Meeting Mic Set {runId}`, Duration `2 days`, Purpose `Rapat tahunan`, Requested By `Rina Wulandari {runId}`; tidak ada approver eligible untuk aset itu sehingga approval dirutekan ke `Maya Putri {runId}` (alasan `No eligible approver`).
  - DU-029-14: Draft milik Borrower `Rudi Hartono {runId}`, berisi aset `Scanner Epson DS-530 {runId}` (Group `Head Office {runId}`) dan aset `Forklift Toyota 8FD {runId}` (Group `Branch Surabaya {runId}`), Total Asset `2`, Modified By `Rina Wulandari {runId}`.
  - DU-029-15: Draft baru untuk Borrower `Rudi Hartono {runId}` tanpa aset, dibuat `Maya Putri {runId}` lewat langkah spec.
- Kondisi:
  - Level Feature Suite Borrowing entitas aktor bernilai `Full`.

## Test Steps

### Menu dan tab Borrow tampil
1. Verifikasi menu `Transactions > Borrow` tampil di sidebar
2. Klik menu `Transactions > Borrow`
3. Verifikasi tab `Transactions`, `Borrowed Assets`, dan `History` tampil
4. Verifikasi tab `Drafts` tampil

### BRW dari seluruh Group tampil di tab Transactions
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi BRW milik DU-029-8 dengan Group `Head Office {runId}` tampil di tabel
7. Verifikasi BRW milik DU-029-9 dengan Group `Branch Surabaya {runId}` tampil di tabel
8. Verifikasi `Download` tampil di toolbar tab `Transactions`

### Aksi baris BRW yang Waiting for Handover
9. Buka menu ⋯ pada baris BRW milik DU-029-8
10. Verifikasi aksi `Hand Over` tampil dan aktif
11. Verifikasi aksi `Remind Borrower` tampil dan aktif
12. Verifikasi aksi `Cancel Borrow` tampil dan aktif

### Aksi baris BRW yang Borrowed
13. Buka menu ⋯ pada baris BRW milik DU-029-9
14. Verifikasi aksi `Request Extension` tampil dan aktif
15. Verifikasi aksi `Return` tampil dan aktif

### Aksi baris BRW dengan Extension Approval
16. Buka menu ⋯ pada baris BRW milik DU-029-10
17. Verifikasi aksi `Cancel Extension` tampil dan aktif

### Aksi baris BRW dengan Extension Request dari My Asset
18. Buka menu ⋯ pada baris BRW milik DU-029-11
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

### Draft dengan aset di dua Group dapat diedit, di-Submit, dan di-Delete
28. Klik tab `Drafts`
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi Draft milik DU-029-14 untuk Borrower `Rudi Hartono {runId}` dengan Total Asset `2` tampil di tabel
31. Buka menu ⋯ pada baris Draft milik DU-029-14
32. Verifikasi aksi `Edit` tampil dan aktif
33. Verifikasi aksi `Delete` tampil dan aktif
34. Klik `Edit`
35. Verifikasi tombol `[Submit]` tampil dan aktif pada Draft berisi aset dari dua Group
36. Klik `[Cancel]` pada form; form belum diubah sehingga dialog Unsaved Changes tidak muncul

### Create dan Save Draft
37. Verifikasi tombol `[+ Borrow]` tampil di toolbar tab `Drafts`
38. Klik `[+ Borrow]`
39. Verifikasi tombol `[Save Draft]` tampil di form `Borrow Request`
40. Verifikasi tombol `[Submit]` tampil di form `Borrow Request`
41. Klik `[Select Borrower]`
42. Pilih Borrower `Rudi Hartono {runId}` pada dialog Select Borrower
43. Klik `[Save Draft]`
44. Klik `Draft` pada breadcrumb sehingga tab `Drafts` tampil
45. Ketik Search `{runId}`, tekan Enter
46. Verifikasi Draft baru untuk Borrower `Rudi Hartono {runId}` dengan Total Asset `0` tampil di tabel

### Titik masuk Quick Action dan Asset List
47. Buka menu Quick Action pada navbar
48. Verifikasi item `Borrow` tampil di menu Quick Action
49. Klik menu `Assets > All`
50. Ketik Search `{runId}`, tekan Enter
51. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
52. Verifikasi aksi `Borrow` tampil dan aktif
53. Verifikasi aksi `Add to Borrow Draft` tampil dan aktif

### Mark as Returned tidak tampil pada level Full
54. Ganti isi kotak search dengan `Toyota Avanza {runId}`, tekan Enter
55. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
56. Verifikasi baris aset `Toyota Avanza {runId}` berstatus `Borrowed` tampil di tabel
57. Verifikasi aksi `Mark as Returned` tidak tampil karena level Feature Suite Borrowing bukan `None`

### Menu Approvals > Borrow dan keputusan atas aset yang eligible
58. Verifikasi menu `Approvals > Borrow` tampil di sidebar
59. Klik menu `Approvals > Borrow`
60. Ketik Search `{runId}`, tekan Enter
61. Buka menu ⋯ pada baris pengajuan BRW milik DU-029-13
62. Klik `Review`
63. Verifikasi pilihan keputusan `Approve` dan `Reject` tampil dan dapat dipilih untuk aset `Meeting Mic Set {runId}`
64. Verifikasi tombol `[Submit]` tampil di footer halaman Review
65. Klik `[Cancel]` pada halaman Review; keputusan belum diisi sehingga tidak ada yang tersimpan

### Detail BRW dapat dibuka
66. Klik menu `Transactions > Borrow`
67. Ketik Search `{runId}`, tekan Enter
68. Buka menu ⋯ pada baris BRW milik DU-029-8
69. Klik `Detail`
70. Verifikasi halaman Borrow Detail BRW milik DU-029-8 terbuka dengan Borrower `Rudi Hartono {runId}`
