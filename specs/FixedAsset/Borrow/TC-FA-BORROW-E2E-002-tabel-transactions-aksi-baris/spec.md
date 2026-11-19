---
id: TC-FA-BORROW-E2E-002-tabel-transactions-aksi-baris
title: "Aksi baris tabel Transactions tampil menurut status baris, aktor, dan syarat tiap aksi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1a#p3", "§4.1a#r10", "§4.1a#r11", "§4.1a#r12", "§4.1a#r13", "§4.1a#r14", "§4.1a#r15", "§4.1a#r16", "§4.1a#r17", "§4.1a#r18", "§4.1a#r19", "§4.1a#p4"]
smoke: []
dependsOn: []
trace:
  "§4.1a#p3": [4]
  "§4.1a#r10": [4, 9, 13, 25, 62]
  "§4.1a#r11": [6]
  "§4.1a#r12": [6]
  "§4.1a#r13": [4, 10, 14, 25, 44]
  "§4.1a#r14": [4, 10, 14, 25, 40, 41]
  "§4.1a#r15": [5, 10, 13, 17, 22, 25, 48]
  "§4.1a#r16": [5, 10, 13, 17, 21, 25, 54]
  "§4.1a#r17": [5, 10, 28, 30, 32]
  "§4.1a#r18": [4, 9, 14, 18, 25, 35, 37]
  "§4.1a#r19": [6, 58]
  "§4.1a#p4": [48, 49, 50, 54, 55]
anchor: [2]
coverage:
  web: automated
---

# Aksi baris tabel Transactions tampil menurut status baris, aktor, dan syarat tiap aksi

## Prerequisites
- Aktor: Asset Admin `Admin Aset {runId}` (DU-002-1), Group penugasan `Head Office`.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-002-1: User `Admin Aset {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - Pengaju seluruh BRW: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`. Seluruh BRW berada di Group `Head Office` dan dibuat lewat form Borrow Request.
  - DU-002-2: BRW Borrower `Anton Wijaya` (tampil `Anton W`), aset `Laptop Asus Vivobook 14 {runId}` berstatus Waiting for Handover.
  - DU-002-3: BRW Borrower `Bambang Santoso` (tampil `Bambang S`), aset `Printer Canon G3010 {runId}` berstatus Waiting for Approval.
  - DU-002-4: BRW Borrower `Citra Lestari` (tampil `Citra L`), aset `Monitor Samsung S24 {runId}` berstatus Borrowed (diserahkan T0 − 1 hari dengan Duration `10 days`).
  - DU-002-5: BRW Borrower `Dian Pratiwi` (tampil `Dian P`), aset `Laptop Acer Aspire 5 {runId}` berstatus Overdue (diserahkan T0 − 6 hari dengan Duration `2 days`).
  - DU-002-6: BRW Borrower `Eko Prasetyo` (tampil `Eko P`), aset `Kamera Nikon D5600 {runId}` berstatus Borrowed dan memiliki Damage Report aktif berstatus Waiting for Confirmation.
  - DU-002-7: BRW Borrower `Fajar Nugroho` (tampil `Fajar N`) dengan tiga aset: `Proyektor Epson EB-X06 {runId}` berstatus Waiting for Handover, `Tablet Lenovo Tab M10 {runId}` dan `Speaker JBL Charge 5 {runId}` berstatus Borrowed.
  - DU-002-8: BRW Borrower `Gita Anggraini` (tampil `Gita A`), aset `Laptop Dell Inspiron 15 {runId}` berstatus Borrowed dengan pengajuan Extend yang menunggu approval; status header `Extension Approval`.

## Test Steps

### Hasil Search memuat BRW milik spec ini
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi hasil Search memuat 7 baris dengan Borrower `Anton W`, `Bambang S`, `Citra L`, `Dian P`, `Eko P`, `Fajar N`, dan `Gita A`

### Menu aksi baris BRW Waiting for Handover
3. Klik `⋯` pada baris Borrower `Anton W`
4. Verifikasi menu baris memuat `Detail`, `Hand Over`, `Remind Borrower`, dan `Cancel Borrow`
5. Verifikasi menu baris tidak memuat `Request Extension`, `Return`, dan `Cancel Extension`
6. Verifikasi menu baris tidak memuat `Edit`, `Delete`, `Review`, dan `Download`
7. Tutup menu baris

### Menu aksi baris BRW Waiting for Approval
8. Klik `⋯` pada baris Borrower `Bambang S`
9. Verifikasi menu baris memuat `Detail` dan `Cancel Borrow`
10. Verifikasi menu baris tidak memuat `Hand Over`, `Remind Borrower`, `Request Extension`, `Return`, dan `Cancel Extension`
11. Tutup menu baris

### Menu aksi baris BRW Borrowed
12. Klik `⋯` pada baris Borrower `Citra L`
13. Verifikasi menu baris memuat `Detail`, `Request Extension`, dan `Return`
14. Verifikasi menu baris tidak memuat `Cancel Borrow`, `Hand Over`, dan `Remind Borrower`
15. Tutup menu baris

### Menu aksi baris BRW Overdue
16. Klik `⋯` pada baris Borrower `Dian P`
17. Verifikasi menu baris memuat `Request Extension` dan `Return`
18. Verifikasi menu baris tidak memuat `Cancel Borrow`
19. Tutup menu baris

### Menu aksi baris BRW Borrowed yang memiliki Damage Report
20. Klik `⋯` pada baris Borrower `Eko P`
21. Verifikasi menu baris memuat `Return`
22. Verifikasi menu baris tidak memuat `Request Extension`
23. Tutup menu baris

### Menu aksi baris BRW dengan campuran status baris
24. Klik `⋯` pada baris Borrower `Fajar N`
25. Verifikasi menu baris memuat `Detail`, `Hand Over`, `Remind Borrower`, `Request Extension`, `Return`, dan `Cancel Borrow`
26. Tutup menu baris

### Cancel Extension menarik pengajuan Extend yang menunggu approval
27. Klik `⋯` pada baris Borrower `Gita A`
28. Verifikasi menu baris memuat `Cancel Extension`
29. Klik `Cancel Extension`
30. Verifikasi dialog `Cancel Extension` memuat teks `Are you sure you want to cancel it?`
31. Klik `[Go Back]` pada dialog
32. Verifikasi baris Borrower `Gita A` tetap menampilkan status header `Extension Approval`

### Cancel Borrow meminta konfirmasi dan Go Back tidak membatalkan BRW
33. Klik `⋯` pada baris Borrower `Bambang S`
34. Klik `Cancel Borrow`
35. Verifikasi dialog `Cancel Borrow` memuat teks `Are you sure you want to cancel it?`
36. Klik `[Go Back]` pada dialog
37. Verifikasi baris Borrower `Bambang S` tetap menampilkan status header `Waiting for Approval`

### Remind Borrower mengirim pengingat tanpa mengubah status baris
38. Klik `⋯` pada baris Borrower `Anton W`
39. Klik `Remind Borrower`
40. Verifikasi toast `Success, reminder has been sent to Anton Wijaya.` tampil
41. Verifikasi baris Borrower `Anton W` tetap menampilkan status header `Waiting for Handover`

### Hand Over membuka halaman Handover
42. Klik `⋯` pada baris Borrower `Anton W`
43. Klik `Hand Over`
44. Verifikasi halaman Handover terbuka untuk BRW baris Borrower `Anton W` dengan aset `Laptop Asus Vivobook 14 {runId}`
45. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb

### Request Extension membuka halaman Extend per aset
46. Klik `⋯` pada baris Borrower `Fajar N`
47. Klik `Request Extension`
48. Verifikasi halaman `Extension Request` terbuka dengan baris untuk aset `Tablet Lenovo Tab M10 {runId}` dan `Speaker JBL Charge 5 {runId}`
49. Verifikasi aset `Proyektor Epson EB-X06 {runId}` tidak tampil pada halaman `Extension Request`
50. Verifikasi `Extend By` dan `Reason` kosong pada setiap baris
51. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb

### Return membuka halaman Return per aset
52. Klik `⋯` pada baris Borrower `Fajar N`
53. Klik `Return`
54. Verifikasi halaman `Return Asset` terbuka dengan daftar aset yang memuat `Tablet Lenovo Tab M10 {runId}` dan `Speaker JBL Charge 5 {runId}`
55. Verifikasi daftar aset pada halaman `Return Asset` tidak memuat `Proyektor Epson EB-X06 {runId}`
56. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb

### Download di toolbar menawarkan CSV dan XLSX
57. Klik `Download` di toolbar tabel
58. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
59. Tutup popover Download

### Detail membuka Borrow Detail
60. Klik `⋯` pada baris Borrower `Citra L`
61. Klik `Detail`
62. Verifikasi halaman Borrow Detail terbuka untuk BRW baris Borrower `Citra L`
