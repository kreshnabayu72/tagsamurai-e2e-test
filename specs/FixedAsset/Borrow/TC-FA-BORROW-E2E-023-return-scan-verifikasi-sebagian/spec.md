---
id: TC-FA-BORROW-E2E-023-return-scan-verifikasi-sebagian
title: "Halaman Return memilih Borrower dan aset, memverifikasi lewat scan, dan mengembalikan sebagian atau seluruh aset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-109", "FI-BRW-115", "FI-BRW-116", "FI-BRW-117", "FI-BRW-118", "FI-BRW-126", "FI-BRW-127", "FI-BRW-128", "FI-BRW-129", "FI-BRW-130", "FI-BRW-131", "FI-BRW-132", "FI-BRW-146", "FI-BRW-147", "FI-BRW-148", "FI-BRW-149", "FI-BRW-92", "FI-BRW-93", "FI-BRW-94", "FI-BRW-95", "FI-BRW-96", "FI-BRW-97", "FI-BRW-98", "FI-BRW-99", "V-BRW-34", "V-BRW-35", "§4.2.6#p1", "§4.2.6#p2", "§4.4#r12"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-109": 54
  "FI-BRW-115": 53
  "FI-BRW-116": 71
  "FI-BRW-117": 72
  "FI-BRW-118": [52, 70]
  "FI-BRW-126": 34
  "FI-BRW-127": 36
  "FI-BRW-128": 44
  "FI-BRW-129": 48
  "FI-BRW-130": 48
  "FI-BRW-131": 59
  "FI-BRW-132": 54
  "FI-BRW-146": 52
  "FI-BRW-147": 57
  "FI-BRW-148": 55
  "FI-BRW-149": 56
  "FI-BRW-92": 12
  "FI-BRW-93": 14
  "FI-BRW-94": [14, 16]
  "FI-BRW-95": 18
  "FI-BRW-96": 8
  "FI-BRW-97": [20, 25]
  "FI-BRW-98": 20
  "FI-BRW-99": 22
  "V-BRW-34": 24
  "V-BRW-35": [20, 22]
  "§4.2.6#p1": 8
  "§4.2.6#p2": [7, 10]
  "§4.4#r12": 20
anchor: [29]
coverage:
  web: automated
---

# Halaman Return memilih Borrower dan aset, memverifikasi lewat scan, dan mengembalikan sebagian atau seluruh aset

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office` saja; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-023-1: BRW Group `Head Office`, Borrower `Joko Widodo {runId}`, Photo at end OFF, berisi baris `Borrowed` aset DU-023-2, DU-023-3, DU-023-4, dan DU-023-5.
  - DU-023-2: aset `Laptop Acer Swift {runId}`, TAG `RFID`, Group `Head Office`.
  - DU-023-3: aset `Kamera Sony ZV {runId}`, TAG `QR` yang tidak dapat dipindai, Group `Head Office`; Note laporan TAG yang dicoba `Label TAG rusak terkena air`, Report Type `Unreadable`.
  - DU-023-4: aset `Tripod Velbon {runId}`, TAG `NFC`, Group `Head Office`.
  - DU-023-5: aset `Drone DJI Mini {runId}`, TAG `RFID`, Group `Head Office`, dengan laporan Damaged dari Borrower `Joko Widodo {runId}` berstatus `Waiting for Confirmation`.
  - DU-023-6: aset `Gimbal Zhiyun {runId}`, Group `Branch Surabaya`, baris `Borrowed` atas nama `Joko Widodo {runId}` pada BRW DU-023-9.
  - DU-023-7: aset `Monitor Dell {runId}`, Group `Head Office`, baris `Borrowed` atas nama `Kartika Sari {runId}` pada BRW DU-023-10.
  - DU-023-8: aset `Printer Epson {runId}`, Group `Head Office`, tidak sedang dipinjam.
  - DU-023-11: BRW Group `Head Office`, Borrower `Joko Widodo {runId}`, Photo at end OFF, berisi baris `Borrowed` aset DU-023-12.
  - DU-023-12: aset `Speaker Bose {runId}`, TAG `RFID`, Group `Head Office`.
  - Asset ID tiap aset dibentuk sistem dan menjadi milik entri aset itu.

## Test Steps

### Return dari Borrowed Assets mengisi Borrower dan aset otomatis
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik tab `Borrowed Assets`
4. Ketik Search `Laptop Acer Swift {runId}`, tekan Enter
5. Klik menu ⋯ pada baris aset DU-023-2
6. Klik `Return`
7. Verifikasi halaman `Return Asset` tampil dengan judul tanpa Transaction ID
8. Verifikasi field Borrower terisi `Joko Widodo {runId}` otomatis dan daftar aset memuat aset DU-023-2 dengan Verification `Unverified`
9. Klik field Borrower
10. Verifikasi opsi `Joko Widodo {runId}` menampilkan `5 assets`, yaitu aset yang dapat diterima Aktor ini, tanpa aset Group `Branch Surabaya`
11. Tekan Esc untuk menutup daftar opsi Borrower

### Verify Asset menerapkan hasil scan langsung ke daftar
12. Verifikasi tombol `[Verify Asset]` tampil pada toolbar Return
13. Scan TAG aset DU-023-2 lewat `[Verify Asset]`
14. Verifikasi baris DU-023-2 `Verified` tanpa dialog tambahan
15. Scan TAG aset DU-023-2 lewat `[Verify Asset]`
16. Verifikasi daftar tetap memuat satu baris DU-023-2 `Verified` karena scan ulang diabaikan
17. Scan TAG aset DU-023-4 lewat `[Verify Asset]`
18. Verifikasi baris DU-023-4 ditambahkan langsung ke daftar dengan Verification `Verified`

### Scan ditolak dengan toast error dan daftar tidak berubah
19. Scan TAG aset DU-023-8 lewat `[Verify Asset]`
20. Verifikasi toast `Error, this asset isn't borrowed.` tampil
21. Scan TAG aset DU-023-7 lewat `[Verify Asset]`
22. Verifikasi toast `Error, this asset isn't borrowed by [Borrower].` tampil dengan [Borrower] berisi `Kartika Sari {runId}`
23. Scan TAG aset DU-023-6 lewat `[Verify Asset]`
24. Verifikasi toast `Error, return this asset to [Group].` tampil dengan [Group] berisi `Branch Surabaya`
25. Verifikasi daftar tetap memuat hanya baris DU-023-2 dan DU-023-4 yang `Verified`

### I Can't Scan the TAG mewajibkan Return Photo
26. Klik `[+ Asset]`
27. Pilih aset DU-023-3 pada dialog Select Asset
28. Klik `[Select]`
29. Verifikasi baris DU-023-3 masuk ke daftar dengan Verification `Unverified`
30. Klik menu ⋯ pada baris DU-023-3
31. Klik `I Can't Scan the TAG`
32. Isi Note laporan dengan `Label TAG rusak terkena air`
33. Klik tombol kirim laporan pada dialog Report TAG
34. Verifikasi baris DU-023-3 menampilkan Verification `TAG Reported` dan Report TAG dibuat dengan Report Type `Unreadable`
35. Klik `[Submit]`
36. Verifikasi ringkasan error `1 asset needs a return photo.` tampil di atas tombol karena Return Photo baris DU-023-3 wajib walau Photo at end OFF
37. Ambil foto pada kolom Return Photo baris DU-023-3

### Remove from List membuang baris tanpa dialog
38. Klik `[+ Asset]`
39. Pilih aset DU-023-5 pada dialog Select Asset
40. Klik `[Select]`
41. Scan TAG aset DU-023-5 lewat `[Verify Asset]`
42. Klik menu ⋯ pada baris DU-023-5
43. Klik `Remove from List`
44. Verifikasi baris DU-023-5 hilang dari daftar langsung tanpa dialog
45. Klik `[+ Asset]`
46. Pilih aset DU-023-5 pada dialog Select Asset
47. Klik `[Select]`
48. Verifikasi baris DU-023-5 kembali dengan Verification `Unverified` dan Return Photo kosong, tanpa status Verified dan foto sebelumnya
49. Klik menu ⋯ pada baris DU-023-5
50. Klik `Remove from List`

### Partial return: aset yang tidak ada di daftar tetap Borrowed
51. Klik `[Submit]`
52. Verifikasi tidak ada popup konfirmasi Borrower dan toast `Success, 3 assets have been returned.` langsung tampil
53. Verifikasi halaman Borrow Detail BRW milik DU-023-1 tampil karena semua aset yang dikembalikan berasal dari BRW itu
54. Verifikasi baris aset DU-023-2, DU-023-3, dan DU-023-4 `Returned` dan dikelompokkan pada BRW milik DU-023-1
55. Verifikasi baris aset DU-023-5 tetap `Borrowed`
56. Verifikasi status header BRW milik DU-023-1 tetap `Borrowed` karena masih ada baris aktif
57. Verifikasi Borrower pada header BRW tetap `Joko Widodo {runId}` sesuai BRW
58. Klik menu ⋯ pada baris aset DU-023-5
59. Verifikasi baris aset DU-023-5 tetap memuat badge `Reported Damaged` dan laporan Borrower tetap `Waiting for Confirmation`

### Return aset dari beberapa BRW kembali ke tab Borrowed Assets
60. Klik tab `Borrowed Assets`
61. Ketik Search `Drone DJI Mini {runId}`, tekan Enter
62. Klik menu ⋯ pada baris aset DU-023-5
63. Klik `Return`
64. Klik `[+ Asset]`
65. Pilih aset DU-023-12 pada dialog Select Asset
66. Klik `[Select]`
67. Scan TAG aset DU-023-5 lewat `[Verify Asset]`
68. Scan TAG aset DU-023-12 lewat `[Verify Asset]`
69. Klik `[Submit]`
70. Verifikasi toast `Success, 2 assets have been returned.` tampil
71. Verifikasi halaman kembali ke tab `Borrowed Assets` karena aset yang dikembalikan berasal dari lebih dari satu BRW
72. Verifikasi halaman tidak berpindah ke My Asset History karena Return dijalankan Aktor Borrow, bukan Borrower self-service
