---
id: TC-FA-BORROW-E2E-034-plan-level-none
title: "Level Feature Suite Borrowing None menampilkan menu disabled, menolak URL langsung, dan membatasi aksi ke wind-down"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.11#r21", "§9.11#r22", "§9.11#r23", "§9.11#r24", "§9.11#r25", "§9.11#r26", "§9.11#r27", "§9.11#r28", "§9.11#r29", "§9.11#r30", "§9.11#r31", "§9.11#r32", "§9.11#r33", "§9.11#r34", "§9.11#r35"]
smoke: []
dependsOn: []
trace:
  "§9.11#r21": [8]
  "§9.11#r22": [9, 12]
  "§9.11#r23": [17, 18, 19, 22]
  "§9.11#r24": [27, 28]
  "§9.11#r25": [39]
  "§9.11#r26": [61, 62, 63, 64]
  "§9.11#r27": [22]
  "§9.11#r28": [33]
  "§9.11#r29": [42, 43]
  "§9.11#r30": [46, 49]
  "§9.11#r31": [51, 52]
  "§9.11#r32": [56, 67]
  "§9.11#r33": [57]
  "§9.11#r34": [58, 59]
  "§9.11#r35": [24, 26, 59]
anchor: [11, 16, 36, 38, 41, 45, 48]
coverage:
  web: automated
---

# Level Feature Suite Borrowing None menampilkan menu disabled, menolak URL langsung, dan membatasi aksi ke wind-down

## Prerequisites
- Aktor: Total Control, lalu Borrower dan pengaju pada langkah «Masuk sebagai».
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-034-1: Entitas `Nusantara Teknik {runId}`, status Active, level Feature Suite Borrowing `Full` sebelum T-0 dan `None` sesudah T-0.
  - DU-034-2: User `Maya Putri {runId}`, role Total Control, cakupan seluruh client, aktif.
  - DU-034-3: User `Rina Wulandari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-034-4: User `Rudi Hartono {runId}`, karyawan tanpa role Borrow, aktif, Home Group `Head Office {runId}`.
  - DU-034-5: Group `Head Office {runId}`.
  - DU-034-6: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-034-7: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Rina Wulandari {runId}`.
  - DU-034-8: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Rina Wulandari {runId}`.
  - DU-034-9: BRW berstatus Overdue (Due date terlewat), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Excavator Komatsu PC200 {runId}`, Duration `6 days`, Purpose `Pekerjaan galian`, Requested By `Rina Wulandari {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `Nusantara Teknik {runId}` yang tidak dipakai spec lain.
  - Level Feature Suite Borrowing entitas itu bernilai `Full` sampai langkah 6 dan bernilai `None` sesudahnya.
  - Akun `Rudi Hartono {runId}` dan `Rina Wulandari {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Level turun ke None pada T-0: menu Borrow disabled, Approvals dan Quick Action tidak menampilkan Borrow
1. Masuk sebagai Borrower `Rudi Hartono {runId}`
2. Catat jumlah notifikasi `borrow_auto_canceled`, `borrow_returned`, `borrow_due_soon`, dan `borrow_overdue` di Notification Center sebagai baseline Borrower
3. Masuk sebagai pengaju `Rina Wulandari {runId}`
4. Catat jumlah notifikasi `borrow_auto_canceled` di Notification Center sebagai baseline pengaju
5. Masuk sebagai Total Control `Maya Putri {runId}`

6. Level Feature Suite Borrowing entitas `Nusantara Teknik {runId}` turun dari `Full` ke `None` pada T-0
7. Muat ulang halaman

8. Verifikasi menu `Transactions > Borrow` tampil dalam keadaan disabled dengan chip `Upgrade`
9. Verifikasi menu `Approvals > Borrow` tidak tampil di sidebar
10. Buka menu Quick Action pada navbar
11. Verifikasi menu Quick Action terbuka
12. Verifikasi item `Borrow` tidak tampil di menu Quick Action

### Tabel aset: aksi Borrow tidak tampil dan Mark as Returned hanya pada aset Borrowed
13. Klik menu `Assets > All`
14. Ketik Search `{runId}`, tekan Enter
15. Buka menu ⋯ pada baris aset `Laptop Lenovo T14 {runId}`
16. Verifikasi aset `Laptop Lenovo T14 {runId}` berstatus `Available` tampil di tabel aset entitas khusus
17. Verifikasi aksi `Borrow` tidak tampil
18. Verifikasi aksi `Add to Borrow Draft` tidak tampil
19. Verifikasi aksi `Mark as Returned` tidak tampil pada aset yang tidak Borrowed
20. Ganti isi kotak search dengan `Toyota Avanza {runId}`, tekan Enter
21. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
22. Verifikasi aksi `Mark as Returned` tampil dan aktif pada aset `Toyota Avanza {runId}` yang Borrowed
23. Ganti isi kotak search dengan `Excavator Komatsu PC200 {runId}`, tekan Enter
24. Verifikasi baris aset `Excavator Komatsu PC200 {runId}` menampilkan badge `Overdue`

### Halaman detail aset Overdue
25. Buka halaman detail aset `Excavator Komatsu PC200 {runId}`
26. Verifikasi badge `Overdue` tampil di halaman detail aset
27. Verifikasi aksi `Mark as Returned` tampil di header halaman detail aset
28. Verifikasi Transaction log Borrow aset `Excavator Komatsu PC200 {runId}` tetap terbaca di halaman detail aset

### Mark as Returned pada aset Borrowed
29. Klik menu `Assets > All`
30. Ketik Search `Toyota Avanza {runId}`, tekan Enter
31. Buka menu ⋯ pada baris aset `Toyota Avanza {runId}`
32. Klik `Mark as Returned`
33. Verifikasi dialog Mark as Returned memuat pilihan hasil `Returned`, `Missing`, dan `Damaged`
34. Pilih hasil `Returned` pada dialog Mark as Returned
35. Konfirmasi dialog Mark as Returned
36. Verifikasi toast `Success, asset has been marked as returned.` tampil

### Transaction Settings tanpa bagian Borrow
37. Buka halaman Transaction Settings
38. Verifikasi halaman Transaction Settings terbuka
39. Verifikasi bagian Borrow tidak tampil di Transaction Settings

### Role & Permission tanpa pengaturan role Borrow
40. Buka pengaturan Role & Permission sub-tab `Borrowing & Assignment`
41. Verifikasi sub-tab `Borrowing & Assignment` terbuka
42. Verifikasi pengaturan role Borrow tidak tampil di sub-tab `Borrowing & Assignment`
43. Verifikasi penugasan Role Transaksi `Asset Admin` milik `Rina Wulandari {runId}` tetap tampil

### Dashboard dan Reports tanpa laporan atau widget Borrow
44. Buka halaman Dashboard
45. Verifikasi halaman Dashboard terbuka
46. Verifikasi widget Borrow tidak tampil di Dashboard
47. Buka halaman Reports
48. Verifikasi halaman Reports terbuka
49. Verifikasi laporan Borrow tidak tampil di Reports

### User Detail tetap menampilkan log
50. Buka User Detail `Rina Wulandari {runId}`
51. Verifikasi `Transaction admin log` pada User Detail tetap terbaca
52. Verifikasi `User log` pada User Detail tetap terbaca

### Notifikasi Borrower
53. Masuk sebagai Borrower `Rudi Hartono {runId}`
54. Job pengingat jatuh tempo dan Overdue berjalan
55. Buka Notification Center
56. Verifikasi jumlah notifikasi `borrow_auto_canceled` bertambah satu dibanding baseline Borrower
57. Verifikasi jumlah notifikasi `borrow_returned` bertambah satu dibanding baseline Borrower
58. Verifikasi jumlah notifikasi `borrow_due_soon` sama dengan baseline Borrower
59. Verifikasi jumlah notifikasi `borrow_overdue` sama dengan baseline Borrower

### Halaman pinjaman pribadi Borrower pada level None
60. Buka halaman pinjaman pribadi Borrower dari menu Profile
61. Verifikasi tab `Borrowed` tampil dan memuat pinjaman berjalan aset `Excavator Komatsu PC200 {runId}`
62. Verifikasi baris pinjaman aset `Excavator Komatsu PC200 {runId}` tidak memuat aksi `Cancel`, `Return`, `Report Damaged`, `Report Missing`, maupun `Request Extension`
63. Verifikasi tab `History` tampil dan hanya dapat dibaca
64. Verifikasi Task `Confirm Handover` tidak ada

### Notifikasi pengaju
65. Masuk sebagai pengaju `Rina Wulandari {runId}`
66. Buka Notification Center
67. Verifikasi jumlah notifikasi `borrow_auto_canceled` bertambah satu dibanding baseline pengaju
