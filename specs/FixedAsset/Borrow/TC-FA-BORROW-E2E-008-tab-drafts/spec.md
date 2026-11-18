---
id: TC-FA-BORROW-E2E-008-tab-drafts
title: "Tab Drafts menampilkan Draft bersama, Origin, aksi Edit dan Delete, serta Bulk Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1l#p1", "§4.1l#p2", "§4.1l#r1", "§4.1l#r2", "§4.1l#r3", "§4.1l#r4", "§4.1l#r5", "§4.1l#r6", "§4.1l#p6", "§4.1l#r7", "§4.1l#r8", "§4.1l#r9", "§4.1l#r10", "§4.1l#p7", "§9.5#r3", "EB-BLK-2@tabel-drafts", "EB-BLK-3"]
smoke: []
dependsOn: []
trace:
  "§4.1l#p1": [3, 4]
  "§4.1l#p2": [5]
  "§4.1l#r1": [4, 12, 26]
  "§4.1l#r2": [7, 8, 19]
  "§4.1l#r3": [9, 10, 19]
  "§4.1l#r4": [11]
  "§4.1l#r5": [13]
  "§4.1l#r6": [6, 15, 17]
  "§4.1l#p6": [29]
  "§4.1l#r7": [26, 29, 31, 34]
  "§4.1l#r8": [35, 76, 78, 79]
  "§4.1l#r9": [47, 49, 50, 55, 57, 58, 63, 65, 66, 70, 72]
  "§4.1l#r10": [23]
  "§4.1l#p7": [21]
  "§9.5#r3": [6]
  "EB-BLK-2@tabel-drafts": [38, 40, 42]
  "EB-BLK-3": [55, 57, 58, 63, 70, 72]
anchor: []
coverage:
  web: automated
---

# Tab Drafts menampilkan Draft bersama, Origin, aksi Edit dan Delete, serta Bulk Delete

## Prerequisites
- Aktor: Asset Admin `Admin Aset {runId}` (DU-008-1), Group penugasan `Head Office`.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-008-1: User `Admin Aset {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - Pengubah seluruh Draft: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`; `Rina Wulandari` (Total Control, seluruh client), tampil `Rina W`; dan `System`. Seluruh Draft berada dalam cakupan aktor atau memuat sedikitnya satu aset di Group `Head Office`.
  - DU-008-2: Draft Borrower `Ardi Wicaksono` (tampil `Ardi W`), Origin `New`, Group `Head Office`, aset `Laptop Dell Vostro 3510 {runId}` dan `Mouse Logitech M221 {runId}`, Total Asset `2`, Modified By `Agus P`, Last Updated `T0 − 1 hari`.
  - DU-008-3: Draft Borrower `Bella Safira` (tampil `Bella S`), Origin `Restored`, Group `Head Office`, aset `Printer HP LaserJet M111 {runId}` yang tidak lagi layak dipinjam, Total Asset `1`, Modified By `Rina W`, Last Updated `T0 − 2 hari`, berasal dari BRW yang dibatalkan dengan opsi Save as Draft to edit.
  - DU-008-4: Draft Borrower `Cahyo Utomo` (tampil `Cahyo U`), Origin `Restored by system`, Group `Head Office` (aset `Scanner Epson DS-530 {runId}` dan `Mouse Pad Gaming {runId}`) dan Group `Branch Surabaya` (aset `Kamera Canon M200 {runId}` dan `Lensa Canon EF-M 18-55 {runId}`), Total Asset `4`, Modified By `System`, Last Updated `T0 − 3 hari`.
  - DU-008-5: Draft tanpa aset Borrower `Dedi Kurniawan` (tampil `Dedi K`), Origin `New`, dibuat `Admin Aset {runId}`, Group `—`, Total Asset `0`.
  - DU-008-6: Draft Borrower `Eka Pratiwi` (tampil `Eka P`), Origin `New`, Group `Head Office`, aset `Proyektor Optoma HD146X {runId}`, Last Updated `T0 − 5 hari`.
  - DU-008-7: Draft Borrower `Fahmi Rahman` (tampil `Fahmi R`), Origin `New`, Group `Head Office`, aset `Speaker JBL Flip 6 {runId}`, Last Updated `T0 − 6 hari`.
  - DU-008-8: Draft Borrower `Gilang Pratama` (tampil `Gilang P`), Origin `New`, Group `Head Office`, aset `Tablet Samsung Tab S9 {runId}`, Last Updated `T0 − 7 hari`.
  - DU-008-9: Draft Borrower `Hesti Wulandari` (tampil `Hesti W`), Origin `New`, Group `Head Office`, aset `Kamera Sony ZV-E10 {runId}`, Last Updated `T0 − 8 hari`.
  - DU-008-10: Draft Borrower `Indra Gunawan` (tampil `Indra G`), Origin `New`, Group `Head Office`, aset `Monitor LG UltraWide 29 {runId}`, Last Updated `T0 − 9 hari`.
  - Kecuali DU-008-5, Modified By DU-008-6 sampai DU-008-10 adalah `Agus P`.

## Test Steps

### Teks bantu, kolom, dan urutan awal tabel Drafts
1. Klik tab `Drafts`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi teks bantu `Drafts don't reserve assets. Submit to lock them.` tampil di atas tabel
4. Verifikasi hasil Search memuat 8 Draft dengan Borrower `Ardi W`, `Bella S`, `Cahyo U`, `Eka P`, `Fahmi R`, `Gilang P`, `Hesti W`, dan `Indra G`
5. Verifikasi tabel Drafts tidak memiliki kolom `Transaction ID` karena Draft belum bernomor BRW
6. Verifikasi urutan baris dari atas ke bawah: Borrower `Ardi W`, `Bella S`, `Cahyo U`, `Eka P`, `Fahmi R`, `Gilang P`, `Hesti W`, lalu `Indra G`
7. Verifikasi baris Borrower `Ardi W` menampilkan Group `Head Office`
8. Verifikasi baris Borrower `Cahyo U` menampilkan Group `Head Office` dan `Branch Surabaya`
9. Verifikasi baris Borrower `Ardi W` menampilkan Total Asset `2` dan baris Borrower `Cahyo U` menampilkan Total Asset `4`
10. Verifikasi baris Borrower `Bella S` menampilkan Total Asset `1` dengan tanda `⚠` karena asetnya tidak lagi layak
11. Verifikasi baris Borrower `Ardi W` menampilkan Origin `New`, baris Borrower `Bella S` menampilkan Origin `Restored`, dan baris Borrower `Cahyo U` menampilkan Origin `Restored by system`
12. Verifikasi baris Borrower `Bella S` menampilkan `Restored from` beserta nomor BRW asal pada baris kedua kolom Borrower
13. Verifikasi baris Borrower `Ardi W` menampilkan Modified By `Agus P`, baris Borrower `Bella S` menampilkan `Rina W`, dan baris Borrower `Cahyo U` menampilkan `System`
14. Arahkan kursor ke Last Updated baris Borrower `Ardi W`
15. Verifikasi tooltip `1 day ago` tampil
16. Arahkan kursor ke Last Updated baris Borrower `Bella S`
17. Verifikasi tooltip `2 days ago` tampil
18. Ganti isi kotak search dengan `Dedi K`, tekan Enter
19. Verifikasi baris Borrower `Dedi K` menampilkan Group `—` dan Total Asset `0`, karena Draft belum memuat aset
20. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Toolbar tab Drafts dan tombol Borrow
21. Verifikasi tombol `Search by Scan`, `Search`, `Filter`, dan `[+ Borrow]` tampil di toolbar
22. Klik `[+ Borrow]`
23. Verifikasi form Borrow Request kosong terbuka tanpa Borrower terpilih
24. Klik `[Cancel]` pada form Borrow Request yang belum diisi

### Edit Draft lewat Borrower dan row action
25. Klik Borrower `Ardi W`
26. Verifikasi form Borrow Request mode edit terbuka dengan Borrower `Ardi W` dan aset `Laptop Dell Vostro 3510 {runId}` serta `Mouse Logitech M221 {runId}`
27. Klik `[Cancel]` pada form yang belum diubah
28. Klik `⋯` pada baris Borrower `Ardi W`
29. Verifikasi menu baris memuat `Edit` dan `Delete`
30. Klik `Edit`
31. Verifikasi form Borrow Request mode edit terbuka dengan Borrower `Ardi W`
32. Klik `[Cancel]` pada form yang belum diubah
33. Klik `⋯` pada baris Borrower `Cahyo U`
34. Verifikasi menu baris memuat `Edit` karena cakupan aktor meliputi sedikitnya satu Group di Draft
35. Verifikasi `Delete` pada menu baris disabled dengan tooltip `Some assets are outside your groups.`
36. Tutup menu baris

### Select All memilih lintas halaman dan kembali saat uncheck parsial
37. Centang baris Borrower `Ardi W`
38. Verifikasi bar bulk menampilkan tombol `Select All (8 records)`
39. Klik `Select All (8 records)`
40. Verifikasi tombol berubah menjadi `Unselect All`
41. Hapus centang baris Borrower `Ardi W`
42. Verifikasi tombol kembali menjadi `Select All (8 records)` dengan jumlah total tetap 8
43. Klik ikon `×` pada bar bulk

### Bulk Delete satu Draft
44. Centang baris Borrower `Eka P`
45. Klik `Bulk Action`
46. Klik `Delete`
47. Verifikasi dialog memuat teks `This draft will be removed. Are you sure you want to delete it?`
48. Klik `[Delete]` pada dialog
49. Verifikasi toast `Success, draft has been deleted.` tampil
50. Verifikasi baris Borrower `Eka P` tidak tampil dan baris Borrower `Ardi W` tetap tampil

### Bulk Delete beberapa Draft dengan konfirmasi klik ganda
51. Centang baris Borrower `Fahmi R`
52. Centang baris Borrower `Gilang P`
53. Klik `Bulk Action`
54. Klik `Delete`
55. Verifikasi dialog `Delete Drafts` memuat Draft `Fahmi R` dan `Gilang P` serta teks `Are you sure you want to delete them?`
56. Klik ganda `[Delete]` pada dialog
57. Verifikasi satu toast `Success, draft has been deleted.` tampil
58. Verifikasi baris Borrower `Fahmi R` dan `Gilang P` tidak tampil

### Bulk Delete campuran Draft yang bisa dihapus dan Draft di luar cakupan
59. Centang baris Borrower `Hesti W`
60. Centang baris Borrower `Cahyo U`
61. Klik `Bulk Action`
62. Klik `Delete`
63. Verifikasi dialog memuat teks `The following will be deleted:`, `The following have groups outside your access and will be skipped:`, dan `Are you sure you want to continue?`
64. Klik `[Continue]` pada dialog
65. Verifikasi toast `Success, draft has been deleted. Some items were skipped (outside your groups).` tampil
66. Verifikasi baris Borrower `Hesti W` tidak tampil dan baris Borrower `Cahyo U` tetap tampil

### Bulk Delete yang seluruh pilihannya di luar cakupan
67. Centang baris Borrower `Cahyo U`
68. Klik `Bulk Action`
69. Klik `Delete`
70. Verifikasi dialog `Cannot Delete Drafts` memuat teks `None of the selected drafts can be deleted because they have groups outside your access.`
71. Klik `[OK]` pada dialog
72. Verifikasi baris Borrower `Cahyo U` tetap tampil dan masih tercentang
73. Klik ikon `×` pada bar bulk

### Delete satu Draft lewat row action
74. Klik `⋯` pada baris Borrower `Indra G`
75. Klik `Delete`
76. Verifikasi dialog `Delete Draft` memuat teks `This draft will be removed. Are you sure you want to delete it?`
77. Klik `[Delete]` pada dialog
78. Verifikasi toast `Success, draft has been deleted.` tampil
79. Verifikasi baris Borrower `Indra G` tidak tampil dan baris Borrower `Ardi W` tetap tampil
