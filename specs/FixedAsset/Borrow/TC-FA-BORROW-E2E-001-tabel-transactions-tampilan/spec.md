---
id: TC-FA-BORROW-E2E-001-tabel-transactions-tampilan
title: "Tab Transactions menampilkan BRW dengan kolom, status header turunan, urutan awal, dan kontrol toolbar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1a#p1", "§4.1a#r1", "§4.1a#r2", "§4.1a#r3", "§4.1a#r4", "§4.1a#r5", "§4.1a#r6", "§4.1a#r7", "§4.1a#r8", "§4.1a#r9", "§4.1a#p5", "§4.1a#p10", "§5#r1", "§5#r12", "§9.5#r1", "§9.5#r7", "§9.5#r18"]
smoke: []
dependsOn: []
trace:
  "§4.1a#p1": [9, 23, 24, 25, 47]
  "§4.1a#r1": [51, 53]
  "§4.1a#r2": [9, 10, 13, 26, 27, 28, 29, 30, 31, 32, 33, 44, 56]
  "§4.1a#r3": [34, 35]
  "§4.1a#r4": [23]
  "§4.1a#r5": [36, 37, 38, 39, 57]
  "§4.1a#r6": [50]
  "§4.1a#r7": [40, 41]
  "§4.1a#r8": [42]
  "§4.1a#r9": [43, 44]
  "§4.1a#p5": [2, 45, 46]
  "§4.1a#p10": [2, 3, 4, 6, 54]
  "§5#r1": [2, 3, 55]
  "§5#r12": [17, 20]
  "§9.5#r1": [1]
  "§9.5#r7": [44]
  "§9.5#r18": [7]
anchor: []
coverage:
  web: automated
---

# Tab Transactions menampilkan BRW dengan kolom, status header turunan, urutan awal, dan kontrol toolbar

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-001-1), cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-001-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client.
  - Pengaju: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`; `Rina Wulandari` (Total Control, seluruh client), tampil `Rina W`.
  - DU-001-2: BRW Borrower `Andi Pratama` (tampil `Andi P`), Group `Head Office`, pengaju `Agus P`, dibuat lewat form Borrow Request. Aset `Laptop Dell Latitude 5440 {runId}` berstatus Overdue (diserahkan T0 − 5 hari dengan Duration `2 days`) dan `Monitor LG 24MK {runId}` berstatus Borrowed (diserahkan T0 − 5 hari dengan Duration `10 days`). Status header `Borrowed` dengan penanda `Overdue`, Total Asset `2`.
  - DU-001-3: BRW Borrower `Budi Santoso` (tampil `Budi S`), Group `Head Office`, pengaju `Agus P`. Aset `Printer Epson L3250 {runId}` berstatus Waiting for Handover, `Scanner Canon LiDE 400 {runId}` berstatus Waiting for Approval, dan `Proyektor BenQ MX560 {runId}` berstatus Canceled. Status header `Waiting for Handover`, Total Asset `2` karena baris Canceled tidak dihitung.
  - DU-001-4: BRW Borrower `Sari Dewanti` (tampil `Sari D`), Group `Head Office`, pengaju `Agus P`, aset `Tablet Samsung Galaxy Tab A9 {runId}` berstatus Waiting for Handover. Status header `Waiting for Handover`, Total Asset `1`. DU-001-4 dibuat dan terakhir diubah sesudah DU-001-3 terakhir diubah.
  - DU-001-5: BRW Borrower `Rudi Hartono` (tampil `Rudi H`), Group `Head Office`, pengaju `Agus P`, aset `Laptop Lenovo ThinkPad E14 {runId}` berstatus Waiting for Approval. Status header `Waiting for Approval`, Total Asset `1`.
  - DU-001-6: BRW Borrower `Maya Putri` (tampil `Maya P`), Group `Branch Surabaya`, pengaju `Rina W`. Aset `Laptop HP ProBook 450 {runId}` dan `Monitor Dell P2422H {runId}` berstatus Borrowed dengan pengajuan Extend yang menunggu approval. Status header `Extension Approval`, Total Asset `2`.
  - DU-001-7: BRW Borrower `Dewi Lestari` (tampil `Dewi L`), Group `Branch Surabaya`, pengaju `Rina W`, aset `Kamera Sony A6400 {runId}` berstatus Borrowed. Status header `Borrowed`, Total Asset `1`.
  - DU-001-8: Draft Borrower `Nina Kartika` (tampil `Nina K`), Group `Head Office`, aset `Mouse Logitech MX Master 3 {runId}`; Draft belum bernomor BRW.
  - DU-001-10: BRW Borrower `Tono Hermawan` (tampil `Tono H`), Group `Head Office`, pengaju `Agus P`. Aset `Proyektor Epson EB-X06 {runId}` berstatus Borrowed dengan pengajuan Extend dari My Asset yang menunggu review, `Kabel HDMI Premium {runId}` berstatus Borrowed, dan `Speaker Yamaha HS5 {runId}` berstatus Rejected. Status header `Extension Request`, Total Asset `2` karena baris Rejected tidak dihitung. DU-001-10 terakhir diubah sebelum DU-001-3 dan DU-001-4 terakhir diubah.
  - DU-001-9: BRW Borrower `Hendra Kusuma` (tampil `Hendra K`), Group `Head Office`, pengaju `Agus P`, aset `Kamera Canon EOS 90D {runId}` berstatus Returned. Status header `Returned`.
- Kondisi:
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan Request Date dan Last Updated.

## Test Steps

### Tab awal dan tombol toolbar tampil
1. Verifikasi tab `Transactions` aktif pada halaman `Transactions > Borrow`
2. Verifikasi tombol `Search`, `Filter`, dan `Download` tampil di toolbar tabel
3. Verifikasi tombol `[+ Borrow]` tampil di toolbar tabel
4. Verifikasi tombol `Search by Scan` tampil di toolbar tabel

### Field Filter Panel serta opsi Status dan Overdue
5. Klik `Filter`
6. Verifikasi Filter Panel memuat field `Status`, `Overdue`, `Source`, `Group`, `Borrower`, `Requested By`, `Total Asset`, `Request Date`, dan `Last Updated`
7. Verifikasi tidak ada nilai terpilih pada semua field di Filter Panel
8. Klik field `Status`
9. Verifikasi opsi `Waiting for Handover`, `Waiting for Approval`, `Extension Approval`, dan `Borrowed` tampil
10. Verifikasi opsi `Returned`, `Rejected`, dan `Canceled` tidak tampil
11. Tutup daftar opsi field `Status`
12. Klik field `Overdue`
13. Verifikasi opsi `Overdue` dan `Not overdue` tampil
14. Tutup Filter Panel tanpa klik `[Apply]`

### Draft dan BRW selesai berada di tab fasenya sendiri
15. Klik tab `Drafts`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi Draft dengan Borrower `Nina K` tampil
18. Klik tab `History`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi BRW dengan Borrower `Hendra K` dan status `Returned` tampil

### Hanya BRW yang sudah diajukan dan masih berjalan tampil di tab Transactions
21. Klik tab `Transactions`
22. Ketik Search `{runId}`, tekan Enter
23. Verifikasi hasil Search memuat 7 baris dengan Borrower `Andi P`, `Tono H`, `Budi S`, `Sari D`, `Rudi H`, `Maya P`, dan `Dewi L`
24. Verifikasi tidak ada baris dengan Borrower `Nina K`
25. Verifikasi tidak ada baris dengan Borrower `Hendra K`

### Status header turunan dari baris dan penanda Overdue
26. Verifikasi baris Borrower `Andi P` menampilkan status header `Borrowed`
27. Verifikasi baris Borrower `Andi P` menampilkan badge `Overdue` di samping status header
28. Verifikasi hanya baris Borrower `Andi P` yang menampilkan badge `Overdue`
29. Verifikasi baris Borrower `Budi S` menampilkan status header `Waiting for Handover`
30. Verifikasi baris Borrower `Sari D` menampilkan status header `Waiting for Handover`
31. Verifikasi baris Borrower `Rudi H` menampilkan status header `Waiting for Approval`
32. Verifikasi baris Borrower `Maya P` menampilkan status header `Extension Approval`
33. Verifikasi baris Borrower `Dewi L` menampilkan status header `Borrowed`

### Isi kolom Group, Total Asset, dan Requested By
34. Verifikasi baris Borrower `Andi P`, `Tono H`, `Budi S`, `Sari D`, dan `Rudi H` menampilkan Group `Head Office`
35. Verifikasi baris Borrower `Maya P` dan `Dewi L` menampilkan Group `Branch Surabaya`
36. Verifikasi baris Borrower `Andi P` menampilkan Total Asset `2`
37. Verifikasi baris Borrower `Budi S` menampilkan Total Asset `2`, tanpa menghitung baris Canceled
38. Verifikasi baris Borrower `Sari D`, `Rudi H`, dan `Dewi L` menampilkan Total Asset `1`
39. Verifikasi baris Borrower `Maya P` menampilkan Total Asset `2`
40. Verifikasi baris Borrower `Andi P`, `Tono H`, `Budi S`, `Sari D`, dan `Rudi H` menampilkan Requested By `Agus P`
41. Verifikasi baris Borrower `Maya P` dan `Dewi L` menampilkan Requested By `Rina W`

### Request Date dan Last Updated mengikuti format General Settings
42. Verifikasi Request Date baris Borrower `Andi P` tampil dengan Date Format dan Time Format General Settings
43. Verifikasi Last Updated baris Borrower `Andi P` tampil dengan Date Format dan Time Format General Settings

### Urutan awal tabel
44. Verifikasi urutan baris dari atas ke bawah adalah Borrower `Andi P` (penanda Overdue), `Tono H` (Extension Request), `Sari D`, `Budi S`, `Rudi H`, `Maya P`, lalu `Dewi L`

### Tabel tanpa checkbox, bulk action, dan kartu ringkas
45. Verifikasi tabel tidak memiliki kolom checkbox seleksi
46. Verifikasi tidak ada bulk action pada tabel
47. Verifikasi tab Transactions tidak memiliki kartu ringkas

### Kolom Source ditampilkan lewat Column Visibility
48. Klik header kolom Actions `⋯`
49. Centang `Source` pada panel Column Visibility
50. Verifikasi ketujuh baris menampilkan Source `Admin`

### Transaction ID membuka Borrow Detail
51. Verifikasi setiap baris menampilkan Transaction ID sebagai tautan
52. Klik Transaction ID baris Borrower `Rudi H`
53. Verifikasi halaman Borrow Detail BRW baris Borrower `Rudi H` terbuka dengan Transaction ID yang sama dengan baris yang diklik

### Urutan tombol toolbar
54. Verifikasi urutan tombol toolbar dari kiri ke kanan adalah `Search by Scan`, `Search`, `Filter`, `Download`, lalu `[+ Borrow]`
55. Verifikasi `[+ Borrow]` berada paling kanan di toolbar tabel

### Extension Request dan baris Rejected pada BRW
56. Verifikasi baris Borrower `Tono H` menampilkan status header `Extension Request`
57. Verifikasi baris Borrower `Tono H` menampilkan Total Asset `2`, tanpa menghitung baris Rejected
