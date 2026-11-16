---
id: TC-FA-FATR-BE-103-aturan-transfer-dep-transfer
title: "Evaluasi dan penegakan aturan pada transaksi Transfer"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r6", "§Aturan Logika Modul#r26", "§4.1#r127", "§4.1#r130", "§4.1#r131", "§4.1#r132", "§4.1#r133", "§4.1#r134", "§4.1#r135", "§4.1#r136", "§4.1#r137", "§4.1#r138", "§4.1#r139", "§4.1#r140", "§4.1#r141", "§4.1#r142", "§4.1#r166", "§4.1#r177", "§9.2#b92", "§9.2#b131", "§9.2#b427", "§9.2#b428", "§9.2#b429", "§9.2#b434", "§9.2#b435", "§9.2#b438", "§9.2#b384", "§9.2#b392", "§9.2#b399", "§9.2#b414", "§9.2#b416", "§9.2#b417", "§9.2#b418", "§9.2#b420", "§9.2#b424", "§9.2#b430", "§9.2#b431", "§9.2#b432", "§9.4.2#r35", "§9.4.2#r61", "§9.4.2#r82", "§9.4.2#r123", "§9.4.2#r124", "§9.4.2#r128", "§9.4.3#b9", "§9.4.4#r54", "§9.7#r6", "§9.7#r15", "§9.8#r8", "§9.8#r9", "§11#r12"]
smoke: []
dependsOn:
  - Transfer: pengajuan, Send, dan Receive
trace:
  "§Aturan Logika Modul#r6": [3, 11]
  "§Aturan Logika Modul#r26": 3
  "§4.1#r127": 111
  "§4.1#r130": [59, 60]
  "§4.1#r131": 63
  "§4.1#r132": 61
  "§4.1#r133": 69
  "§4.1#r134": 74
  "§4.1#r135": 75
  "§4.1#r136": [70, 166]
  "§4.1#r137": [77, 79]
  "§4.1#r138": [81, 162, 164]
  "§4.1#r139": [77, 81]
  "§4.1#r140": 86
  "§4.1#r141": 89
  "§4.1#r142": 93
  "§4.1#r166": [25, 27]
  "§4.1#r177": [30, 32]
  "§9.2#b92": 11
  "§9.2#b131": [49, 50, 54]
  "§9.2#b427": 21
  "§9.2#b428": 23
  "§9.2#b429": 36
  "§9.2#b434": [3, 11, 18]
  "§9.2#b435": 4
  "§9.2#b438": [97, 98, 100, 101]
  "§9.2#b384": 4
  "§9.2#b392": [109, 111, 154, 157]
  "§9.2#b399": [111, 112, 154, 155, 157, 158]
  "§9.2#b414": [107, 111, 152]
  "§9.2#b416": 114
  "§9.2#b417": 119
  "§9.2#b418": 120
  "§9.2#b420": [123, 124, 126]
  "§9.2#b424": [25, 30]
  "§9.2#b430": 40
  "§9.2#b431": [41, 42, 43, 44]
  "§9.2#b432": [28, 33]
  "§9.4.2#r35": [3, 4, 11]
  "§9.4.2#r61": [77, 81, 86, 89, 93]
  "§9.4.2#r82": [3, 7]
  "§9.4.2#r123": 16
  "§9.4.2#r124": 18
  "§9.4.2#r128": [100, 101]
  "§9.4.3#b9": [100, 101]
  "§9.4.4#r54": [144, 145]
  "§9.7#r6": [3, 7]
  "§9.7#r15": [11, 13]
  "§9.8#r8": [131, 133, 134]
  "§9.8#r9": [137, 139, 140]
  "§11#r12": [77, 81, 86]
anchor: []
---

# Evaluasi dan penegakan aturan pada transaksi Transfer

## Prerequisites
- Aktor: Wulan (DU-103-1), Rizal (DU-103-2), Hendra (DU-103-3), Citra (DU-103-4), dan Operator platform yang mengubah plan client.
- Data:
  - DU-103-1: User: Name `Wulan Pengelola {runId}`, Access Level `Total Control`, Cakupan `seluruh client`.
  - DU-103-2: User: Name `Rizal Pengaju {runId}`, Role `Aktor Transfer`, Cakupan `Group Gudang Pusat {runId}`.
  - DU-103-3: User: Name `Hendra Penerima {runId}`, Role `Aktor Transfer`, Cakupan `Group Cabang Surabaya {runId}, Cabang Depok {runId}, Cabang Bekasi {runId}, Cabang Medan {runId}`.
  - DU-103-4: User: Name `Citra Akuntansi {runId}`, Role `Accounting`, Cakupan `seluruh client`.
  - DU-103-5: User: Name `Joko Approver {runId}`, Role Transaksi `Approver`, Cakupan `Group Gudang Pusat {runId}`.
  - DU-103-6: Group: Name `Gudang Pusat {runId}`, Cost Center default `CC-GP-{runId}`.
  - DU-103-7: Group: Name `Cabang Surabaya {runId}`, Cost Center default `CC-SBY-{runId}`, Sisa kuota `50`.
  - DU-103-8: Group: Name `Cabang Depok {runId}`, Cost Center default `tidak ada`, Sisa kuota `50`.
  - DU-103-9: Group: Name `Cabang Bekasi {runId}`, Sisa kuota `3`.
  - DU-103-10: Group: Name `Cabang Medan {runId}`, Sisa kuota `2`.
  - DU-103-11: Asset: Name `Forklift Listrik 01 {runId}`, Group `Gudang Pusat {runId}`, Status `Active`.
  - DU-103-12: Asset: Name `Forklift Listrik 02 {runId}`, Group `Gudang Pusat {runId}`, Status `Active`.
  - DU-103-13: Asset: Name `Forklift Listrik 03 {runId}`, Group `Gudang Pusat {runId}`, Status `Active`.
  - DU-103-14: Asset: Name `Mesin Bubut Retak {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Condition `Damaged`.
  - DU-103-15: Asset: Name `Genset Hilang {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Condition `Missing`.
  - DU-103-16: Asset: Name `Pompa Air Ber-TAG {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`.
  - DU-103-17: Asset: Name `Meja Kerja Non TAG {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Category `Furnitur Non TAG {runId}, bertanda Non TAG`.
  - DU-103-18: Asset: Name `Kompresor Tag Rusak {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Tag `ber-tag, tag rusak`.
  - DU-103-19: Asset: Name `Printer Label Jaringan {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Tag `ber-tag, dapat di-scan`.
  - DU-103-20: Asset: Name `Troli Barang Kecil {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Cost Center `CC-GP-{runId}`.
  - DU-103-21: Asset: Name `Troli Barang Besar {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Cost Center `CC-GP-{runId}`.
  - DU-103-22: Asset: Name `Rak Besi Tinggi {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Cost Center `CC-GP-{runId}`, Penyusutan `periode berjalan sudah berjalan, bebannya tercatat pada Cost Center CC-GP-{runId}`.
  - DU-103-23: Asset: Name `Rak Besi Rendah {runId}`, Group `Gudang Pusat {runId}`, Status `Active`, Cost Center `CC-GP-{runId}`.
  - DU-103-24: Asset: Name `Lemari Arsip {n} {runId}`, Group `Gudang Pusat {runId}`, Status `Active` (4 aset, {n} berurutan 1 sampai 4).
  - DU-103-25: Asset: Name `Meja Rapat Medan {n} {runId}`, Group `Gudang Pusat {runId}`, Status `Active` (3 aset, {n} berurutan 1 sampai 3).
  - DU-103-26: Asset: Name `Kursi Lipat Draft {runId}`, Group `Gudang Pusat {runId}`, Status `Active`.
  - DU-103-27: Asset: Name `Tenda Lipat {runId}`, Group `Gudang Pusat {runId}`, Status `Active`.
  - DU-103-28: Asset: Name `Bor Listrik {n} {runId}`, Group `Gudang Pusat {runId}`, Status `Active` (4 aset, {n} berurutan 1 sampai 4).
  - DU-103-29: Asset: Name `Gerobak Dorong {n} {runId}`, Group `Gudang Pusat {runId}`, Status `Active` (3 aset, {n} berurutan 1 sampai 3).
  - DU-103-34: Asset: Name `Dongkrak Hidrolik {runId}`, Group `Gudang Pusat {runId}`, Status `Active`.
  - DU-103-35: Group: Name `Cabang Bogor {runId}`, Sisa kuota `2`.
  - DU-103-36: Asset: Name `Pallet Kayu {n} {runId}`, Group `Gudang Pusat {runId}`, Status `Active` (3 aset, {n} berurutan 1 sampai 3).
  - DU-103-37: Asset: Name `Kotak Peralatan Cadangan {runId}`, Group `Gudang Pusat {runId}`, Status `Active`.
- Kondisi:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain, karena mengubah setting entitas dan plan client.
  - Pada awal spec nilai di All categories: Allow Transfer `Allow`, Require approval untuk Transfer `OFF`, Change Cost Center with Group `Never`, In-transit overdue after `7`, Destination quota check `ON`, Photo at start `ON`, Photo at end `ON`, Transaction timeout `7`.
  - Alokasi kuota per Group aktif di client, dan Approval Workflow tersedia di plan client.
  - Rizal, Hendra, dan Citra memiliki akun aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Pengajuan Transfer yang melanggar Allow Transfer ditolak di server apa pun keadaan UI
1. Wulan menyimpan Allow Transfer `Deny` di All categories
2. Rizal mengirim pengajuan Transfer aset `Forklift Listrik 01 {runId}` ke Group `Cabang Surabaya {runId}` lewat request langsung ke server, tanpa melalui form pengajuan
3. Verifikasi pengajuan ditolak di server dan tidak ada baris Transfer untuk aset `Forklift Listrik 01 {runId}`
4. Verifikasi pesan blokir menyebut siapa yang dapat dihubungi
5. Wulan menyimpan Allow Transfer `Allow` di All categories
6. Rizal mengajukan Transfer aset `Forklift Listrik 01 {runId}` ke Group `Cabang Surabaya {runId}`
7. Verifikasi pengajuan diterima dan baris Transfer untuk aset `Forklift Listrik 01 {runId}` ada, sehingga penolakan sebelumnya berasal dari nilai Allow Transfer yang baru disimpan

### Deny pada override Asset mengalahkan Allow pada override Group
8. Wulan menambah override Group untuk Group `Gudang Pusat {runId}` di All categories dengan Allow Transfer `Allow`
9. Wulan menambah override aset untuk aset `Forklift Listrik 02 {runId}` di All categories dengan Allow Transfer `Deny`
10. Rizal mengajukan Transfer aset `Forklift Listrik 02 {runId}` ke Group `Cabang Surabaya {runId}`
11. Verifikasi pengajuan ditolak dan tidak ada baris Transfer untuk aset `Forklift Listrik 02 {runId}`, karena Deny pada override aset mengalahkan Allow pada override Group
12. Rizal mengajukan Transfer aset `Forklift Listrik 03 {runId}` ke Group `Cabang Surabaya {runId}`
13. Verifikasi pengajuan diterima dan baris Transfer untuk aset `Forklift Listrik 03 {runId}` ada, sehingga override aset hanya mengenai aset targetnya
14. Wulan menghapus override Group untuk Group `Gudang Pusat {runId}` di All categories

### Aset Damaged dapat di-Transfer dan aset Missing tidak
15. Rizal mengajukan Transfer aset `Mesin Bubut Retak {runId}`, berkondisi `Damaged`, ke Group `Cabang Surabaya {runId}`
16. Verifikasi pengajuan diterima di server, baris Transfer untuk aset `Mesin Bubut Retak {runId}` ada, dan aset tetap berkondisi `Damaged`
17. Rizal mengajukan Transfer aset `Genset Hilang {runId}`, berkondisi `Missing`, ke Group `Cabang Surabaya {runId}`
18. Verifikasi pengajuan ditolak, tidak ada baris Transfer untuk aset `Genset Hilang {runId}`, dan aset tetap berkondisi `Missing`

### Scan tag wajib dan tidak ada identifikasi manual pada langkah Send
19. Rizal mengajukan Transfer aset `Pompa Air Ber-TAG {runId}` ke Group `Cabang Surabaya {runId}`
20. Rizal melakukan Send atas baris Transfer aset `Pompa Air Ber-TAG {runId}` dengan 1 foto, tanpa scan tag
21. Verifikasi Send ditolak karena scan tag wajib saat mulai transaksi untuk aset ber-tag, dan baris tetap berstatus `Waiting for Send`
22. Rizal melakukan Send atas baris Transfer aset `Pompa Air Ber-TAG {runId}` dengan 1 foto, dengan mengisi identitas aset secara manual sebagai pengganti scan tag
23. Verifikasi Send ditolak karena tidak ada identifikasi manual untuk langkah mulai, dan baris tetap berstatus `Waiting for Send`

### Photo at start dan Photo at end mewajibkan 1 foto pada Send dan Receive
24. Rizal melakukan Send atas baris Transfer aset `Pompa Air Ber-TAG {runId}` dengan scan tag, tanpa foto
25. Verifikasi Send ditolak karena Photo at start `ON` mewajibkan 1 foto pada langkah awal Transfer, dan baris tetap berstatus `Waiting for Send`
26. Rizal melakukan Send atas baris Transfer aset `Pompa Air Ber-TAG {runId}` dengan scan tag dan 1 foto
27. Verifikasi baris Transfer aset `Pompa Air Ber-TAG {runId}` berstatus `In Transit`
28. Verifikasi Handover Note PDF dibuat untuk serah terima fisik pada Send itu
29. Hendra melakukan Receive atas baris Transfer aset `Pompa Air Ber-TAG {runId}` dengan scan tag, tanpa foto
30. Verifikasi Receive ditolak karena Photo at end `ON` mewajibkan 1 foto pada Receive, dan baris tetap berstatus `In Transit`
31. Hendra melakukan Receive atas baris Transfer aset `Pompa Air Ber-TAG {runId}` dengan scan tag dan 1 foto
32. Verifikasi baris Transfer aset `Pompa Air Ber-TAG {runId}` berstatus `Received`
33. Verifikasi Handover Note PDF dibuat untuk serah terima fisik pada Receive itu

### Category bertanda Non TAG dikecualikan dari scan tag wajib
34. Rizal mengajukan Transfer aset `Meja Kerja Non TAG {runId}`, berkategori Non TAG, ke Group `Cabang Surabaya {runId}`
35. Rizal melakukan Send atas baris Transfer aset `Meja Kerja Non TAG {runId}` dengan 1 foto, tanpa scan tag
36. Verifikasi Send diterima dan baris Transfer aset `Meja Kerja Non TAG {runId}` berstatus `In Transit`, karena Category bertanda Non TAG dikecualikan dari scan tag wajib

### Receive lewat I can't scan the TAG untuk tag rusak
37. Rizal mengajukan Transfer aset `Kompresor Tag Rusak {runId}` ke Group `Cabang Surabaya {runId}`
38. Rizal melakukan Send atas baris Transfer aset `Kompresor Tag Rusak {runId}` dengan scan tag dan 1 foto
39. Hendra melakukan Receive atas baris Transfer aset `Kompresor Tag Rusak {runId}` lewat `I can't scan the TAG` karena tag rusak, dengan 1 foto
40. Verifikasi Receive diterima dan baris Transfer aset `Kompresor Tag Rusak {runId}` berstatus `Received`
41. Verifikasi foto yang disertakan pada Receive lewat `I can't scan the TAG` tersimpan pada baris itu
42. Verifikasi cek radius dijalankan atas Receive lewat `I can't scan the TAG`
43. Verifikasi baris Receive itu diberi flag
44. Verifikasi Report TAG dibuat otomatis untuk aset `Kompresor Tag Rusak {runId}`

### Override Asset tetap berlaku sesudah aset berpindah Group
45. Wulan menambah override aset untuk aset `Printer Label Jaringan {runId}` di All categories dengan Photo at end `OFF`
46. Rizal mengajukan Transfer aset `Printer Label Jaringan {runId}` ke Group `Cabang Surabaya {runId}`
47. Rizal melakukan Send atas baris Transfer aset `Printer Label Jaringan {runId}` dengan scan tag dan 1 foto
48. Hendra melakukan Receive atas baris Transfer aset `Printer Label Jaringan {runId}` dengan scan tag, tanpa foto
49. Verifikasi Receive diterima dan baris berstatus `Received`, karena override aset memakai Photo at end `OFF`
50. Verifikasi aset `Printer Label Jaringan {runId}` kini berada di Group `Cabang Surabaya {runId}`
51. Hendra mengajukan Transfer aset `Printer Label Jaringan {runId}` dari Group `Cabang Surabaya {runId}` ke Group `Cabang Depok {runId}`
52. Hendra melakukan Send atas baris Transfer aset `Printer Label Jaringan {runId}` dengan scan tag dan 1 foto
53. Hendra melakukan Receive atas baris Transfer aset `Printer Label Jaringan {runId}` dengan scan tag, tanpa foto
54. Verifikasi Receive diterima dan baris berstatus `Received`, sehingga override aset tetap berlaku sesudah aset berpindah Group

### Change Cost Center with Group Never: Cost Center aset tidak berubah dan Accounting diberi notifikasi
55. Citra mencatat jumlah notifikasi `transfer_cost_center_review` yang ia terima
56. Rizal mengajukan Transfer aset `Troli Barang Kecil {runId}` dan `Troli Barang Besar {runId}` ke Group `Cabang Surabaya {runId}` dalam satu pengajuan
57. Rizal melakukan Send atas kedua baris Transfer dengan scan tag dan 1 foto
58. Hendra melakukan Receive atas kedua baris Transfer dengan scan tag dan 1 foto
59. Verifikasi kedua baris Transfer berstatus `Received`
60. Verifikasi Cost Center aset `Troli Barang Kecil {runId}` dan `Troli Barang Besar {runId}` tetap `CC-GP-{runId}`
61. Verifikasi Citra menerima dua notifikasi `transfer_cost_center_review` baru, satu untuk setiap baris Received
62. Citra memperbarui Cost Center aset `Troli Barang Kecil {runId}` menjadi `CC-SBY-{runId}`
63. Verifikasi Cost Center aset `Troli Barang Kecil {runId}` tersimpan sebagai `CC-SBY-{runId}`

### Change Cost Center with Group Always: Cost Center aset mengikuti Group tujuan bila ada
64. Wulan menyimpan Change Cost Center with Group `Always` di All categories
65. Citra mencatat jumlah notifikasi `transfer_cost_center_review` yang ia terima
66. Rizal mengajukan Transfer aset `Rak Besi Tinggi {runId}` ke Group `Cabang Surabaya {runId}`
67. Rizal melakukan Send atas baris Transfer aset `Rak Besi Tinggi {runId}` dengan scan tag dan 1 foto
68. Hendra melakukan Receive atas baris Transfer aset `Rak Besi Tinggi {runId}` dengan scan tag dan 1 foto
69. Verifikasi Cost Center aset `Rak Besi Tinggi {runId}` menjadi `CC-SBY-{runId}`, Cost Center default Group tujuan
70. Verifikasi beban penyusutan periode berjalan aset `Rak Besi Tinggi {runId}` tetap tercatat pada Cost Center `CC-GP-{runId}`, walau Cost Center aset sudah `CC-SBY-{runId}`
71. Rizal mengajukan Transfer aset `Rak Besi Rendah {runId}` ke Group `Cabang Depok {runId}`, yang tidak punya Cost Center default
72. Rizal melakukan Send atas baris Transfer aset `Rak Besi Rendah {runId}` dengan scan tag dan 1 foto
73. Hendra melakukan Receive atas baris Transfer aset `Rak Besi Rendah {runId}` dengan scan tag dan 1 foto
74. Verifikasi Cost Center aset `Rak Besi Rendah {runId}` tetap `CC-GP-{runId}`
75. Verifikasi Citra menerima satu notifikasi `transfer_cost_center_review` baru untuk baris Received itu

### Destination quota check: pengajuan melebihi sisa kuota Group tujuan ditolak seluruhnya
76. Rizal mengajukan satu Transfer berisi aset `Lemari Arsip 1 {runId}`, `Lemari Arsip 2 {runId}`, `Lemari Arsip 3 {runId}`, dan `Lemari Arsip 4 {runId}` ke Group `Cabang Bekasi {runId}`, yang sisa kuotanya 3
77. Verifikasi pengajuan ditolak seluruhnya karena empat aset melebihi sisa kuota Group tujuan, dan tidak ada baris Transfer dibuat untuk satu pun dari keempat aset
78. Rizal mengajukan Transfer aset `Lemari Arsip 1 {runId}` dan `Lemari Arsip 2 {runId}` ke Group `Cabang Bekasi {runId}`
79. Verifikasi pengajuan diterima dan dua baris Transfer dibuat untuk aset `Lemari Arsip 1 {runId}` dan `Lemari Arsip 2 {runId}`, karena dua aset masih di bawah sisa kuota 3
80. Rizal mengajukan Transfer aset `Lemari Arsip 3 {runId}` dan `Lemari Arsip 4 {runId}` ke Group `Cabang Bekasi {runId}`
81. Verifikasi pengajuan ditolak seluruhnya karena dua baris baru ditambah dua baris aktif lain menuju Group tujuan yang sama melebihi sisa kuota 3, dan tidak ada baris Transfer dibuat untuk aset `Lemari Arsip 3 {runId}` maupun `Lemari Arsip 4 {runId}`

### Destination quota check: pemeriksaan diulang saat Receive
82. Rizal mengajukan Transfer aset `Meja Rapat Medan 1 {runId}` ke Group `Cabang Medan {runId}`, yang sisa kuotanya 2
83. Rizal melakukan Send atas baris Transfer aset `Meja Rapat Medan 1 {runId}` dengan scan tag dan 1 foto
84. Wulan menambahkan aset `Kursi Kantor Medan 1 {runId}` dan `Kursi Kantor Medan 2 {runId}` langsung ke Group `Cabang Medan {runId}`, sehingga sisa kuota Group itu menjadi 0
85. Hendra melakukan Receive atas baris Transfer aset `Meja Rapat Medan 1 {runId}` dengan scan tag dan 1 foto
86. Verifikasi Receive ditolak karena pemeriksaan kuota Group tujuan diulang saat Receive dan sisa kuotanya 0, dan baris tetap berstatus `In Transit`

### Destination quota check OFF dan alokasi kuota per Group tidak aktif: kuota tidak diperiksa
87. Wulan menyimpan Destination quota check `OFF` di All categories
88. Rizal mengajukan Transfer aset `Meja Rapat Medan 2 {runId}` ke Group `Cabang Medan {runId}`, yang sisa kuotanya 0
89. Verifikasi pengajuan diterima dan baris Transfer untuk aset `Meja Rapat Medan 2 {runId}` ada, karena kuota Group tujuan tidak diperiksa
90. Wulan menyimpan Destination quota check `ON` di All categories
91. Alokasi kuota per Group dinonaktifkan di client
92. Rizal mengajukan Transfer aset `Meja Rapat Medan 3 {runId}` ke Group `Cabang Medan {runId}`, yang sisa kuotanya 0
93. Verifikasi pengajuan diterima dan baris Transfer untuk aset `Meja Rapat Medan 3 {runId}` ada, karena alokasi kuota per Group tidak aktif sehingga kuota Group tujuan tidak diperiksa

### Setting yang berubah saat transaksi berjalan tidak menutup otomatis Draft Transfer dan baris In Transit
94. Rizal menyimpan Draft Transfer untuk aset `Kursi Lipat Draft {runId}` ke Group `Cabang Surabaya {runId}`
95. Rizal mengajukan Transfer aset `Tenda Lipat {runId}` ke Group `Cabang Surabaya {runId}`
96. Rizal melakukan Send atas baris Transfer aset `Tenda Lipat {runId}` dengan scan tag dan 1 foto
97. Verifikasi Draft Transfer untuk aset `Kursi Lipat Draft {runId}` berstatus `Draft`
98. Verifikasi baris Transfer aset `Tenda Lipat {runId}` berstatus `In Transit`
99. Wulan menyimpan Allow Transfer `Deny` di All categories
100. Verifikasi Draft Transfer untuk aset `Kursi Lipat Draft {runId}` tetap berstatus `Draft`, tidak ditutup otomatis
101. Verifikasi baris Transfer aset `Tenda Lipat {runId}` tetap berstatus `In Transit`, tidak dibatalkan atau ditutup otomatis
102. Wulan menyimpan Allow Transfer `Allow` di All categories

### In-transit overdue after: notifikasi sekali per baris In Transit
103. Wulan menyimpan In-transit overdue after `3` di All categories
104. Rizal dan Hendra masing-masing mencatat jumlah notifikasi `transfer_transit_overdue` yang mereka terima
105. Rizal mengajukan Transfer aset `Bor Listrik 1 {runId}` dan `Bor Listrik 2 {runId}` ke Group `Cabang Surabaya {runId}` dalam satu pengajuan
106. Rizal melakukan Send atas kedua baris Transfer dengan scan tag dan 1 foto
107. Verifikasi kedua baris Transfer berstatus `In Transit`
108. Waktu berlalu sampai awal hari kalender kedua sesudah hari kedua baris masuk `In Transit`, menurut zona waktu client
109. Verifikasi belum ada notifikasi `transfer_transit_overdue` baru untuk Rizal maupun Hendra
110. Waktu berlalu sampai awal hari kalender kelima sesudah hari kedua baris masuk `In Transit`, menurut zona waktu client
111. Verifikasi Rizal, Aktor Transfer Group asal, dan Hendra, Aktor Transfer Group tujuan, masing-masing menerima dua notifikasi `transfer_transit_overdue` baru, satu untuk setiap baris In Transit
112. Verifikasi kedua baris Transfer ditandai In-transit overdue
113. Waktu berlalu sampai awal hari kalender kesembilan sesudah hari kedua baris masuk `In Transit`, menurut zona waktu client
114. Verifikasi Rizal dan Hendra masing-masing masih memiliki tepat satu notifikasi `transfer_transit_overdue` untuk baris `Bor Listrik 1 {runId}` dan tepat satu untuk baris `Bor Listrik 2 {runId}`, tanpa eskalasi atau pengulangan

### Ambang In-transit overdue after yang baru hanya berlaku untuk transaksi yang diajukan sesudah Save
115. Rizal mengajukan Transfer aset `Bor Listrik 4 {runId}` ke Group `Cabang Surabaya {runId}`
116. Wulan menyimpan In-transit overdue after `10` di All categories
117. Rizal mengajukan Transfer aset `Bor Listrik 3 {runId}` ke Group `Cabang Surabaya {runId}`
118. Waktu berlalu sampai awal hari kalender ketiga belas sesudah hari kedua baris pertama masuk `In Transit`, menurut zona waktu client
119. Verifikasi Rizal dan Hendra masing-masing tetap memiliki tepat satu notifikasi `transfer_transit_overdue` untuk baris `Bor Listrik 1 {runId}` dan tepat satu untuk baris `Bor Listrik 2 {runId}` sesudah Save ambang `10`, sehingga mengubah ambang sesudah notifikasi terkirim tidak mengirim ulang
120. Verifikasi dua notifikasi `transfer_transit_overdue` untuk baris pertama dan kedua masih ada pada Rizal dan Hendra, sehingga mengubah ambang tidak mencabut notifikasi yang sudah terkirim
121. Rizal melakukan Send atas baris Transfer aset `Bor Listrik 4 {runId}` dan `Bor Listrik 3 {runId}` dengan scan tag dan 1 foto
122. Waktu berlalu sampai awal hari kalender kelima sesudah hari kedua baris masuk `In Transit`, menurut zona waktu client
123. Verifikasi Rizal dan Hendra masing-masing menerima satu notifikasi `transfer_transit_overdue` baru untuk baris aset `Bor Listrik 4 {runId}`, yang diajukan sebelum Save ambang `10`
124. Verifikasi tidak ada notifikasi `transfer_transit_overdue` untuk baris aset `Bor Listrik 3 {runId}`, yang diajukan sesudah Save ambang `10`
125. Waktu berlalu sampai awal hari kalender kesebelas sesudah hari kedua baris masuk `In Transit`, menurut zona waktu client
126. Verifikasi Rizal dan Hendra masing-masing menerima satu notifikasi `transfer_transit_overdue` baru untuk baris aset `Bor Listrik 3 {runId}`

### Transaction timeout menutup baris Waiting for Approval dan Waiting for Send oleh System
127. Wulan menyimpan Auto-approve `OFF` untuk Transfer di All categories
128. Wulan menyimpan Require approval `ON` untuk Transfer di All categories
129. Wulan menyimpan Transaction timeout `1` hari di All categories
130. Rizal mengajukan Transfer aset `Gerobak Dorong 1 {runId}` ke Group `Cabang Surabaya {runId}`
131. Verifikasi baris Transfer aset `Gerobak Dorong 1 {runId}` berstatus `Waiting for Approval`
132. Waktu berlalu sampai 25 jam sejak baris masuk `Waiting for Approval`
133. Verifikasi baris Transfer aset `Gerobak Dorong 1 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)`
134. Verifikasi log transaksi baris itu mencatat penutupan tersebut dengan Modified By `System`
135. Wulan menyimpan Require approval `OFF` untuk Transfer di All categories
136. Rizal mengajukan Transfer aset `Gerobak Dorong 2 {runId}` ke Group `Cabang Surabaya {runId}`
137. Verifikasi baris Transfer aset `Gerobak Dorong 2 {runId}` berstatus `Waiting for Send`
138. Waktu berlalu sampai 25 jam sejak baris masuk `Waiting for Send`
139. Verifikasi baris Transfer aset `Gerobak Dorong 2 {runId}` berstatus `Canceled` dengan Note `Not sent`
140. Verifikasi log transaksi baris itu mencatat penutupan tersebut dengan Modified By `System`

### Approval Workflow tidak tersedia di plan: Require approval efektif OFF dan langkah approval dilewati
141. Wulan menyimpan Require approval `ON` untuk Transfer di All categories
142. Operator platform menonaktifkan Approval Workflow pada plan client
143. Rizal mengajukan Transfer aset `Gerobak Dorong 3 {runId}` ke Group `Cabang Surabaya {runId}`
144. Verifikasi baris Transfer aset `Gerobak Dorong 3 {runId}` langsung berstatus `Waiting for Send`, tanpa melewati `Waiting for Approval`
145. Verifikasi nilai efektif Require approval untuk Transfer adalah `OFF` walau nilai tersimpannya `ON`

### In-transit overdue after: batas lebih dari N hari kalender menurut zona waktu client
146. Operator platform mengaktifkan Approval Workflow pada plan client
147. Wulan menyimpan Require approval `OFF` untuk Transfer di All categories
148. Wulan menyimpan In-transit overdue after `3` di All categories
149. Waktu berlalu sampai pukul 23:30 menurut zona waktu client
150. Rizal mengajukan Transfer aset `Dongkrak Hidrolik {runId}` ke Group `Cabang Surabaya {runId}`
151. Rizal melakukan Send atas baris Transfer aset `Dongkrak Hidrolik {runId}` dengan scan tag dan 1 foto
152. Verifikasi baris Transfer aset `Dongkrak Hidrolik {runId}` berstatus `In Transit`
153. Waktu berlalu sampai pukul 23:45 pada hari kalender ketiga sesudah hari baris masuk `In Transit`, menurut zona waktu client, sehingga sudah lebih dari 72 jam sejak baris masuk `In Transit`
154. Verifikasi belum ada notifikasi `transfer_transit_overdue` untuk baris `Dongkrak Hidrolik {runId}` pada Rizal maupun Hendra, karena lama `In Transit` baru tepat 3 hari kalender dan belum lebih dari ambang `3`
155. Verifikasi baris Transfer aset `Dongkrak Hidrolik {runId}` belum ditandai In-transit overdue
156. Waktu berlalu sampai awal hari kalender keempat sesudah hari baris masuk `In Transit`, menurut zona waktu client
157. Verifikasi Rizal dan Hendra masing-masing menerima satu notifikasi `transfer_transit_overdue` untuk baris `Dongkrak Hidrolik {runId}`
158. Verifikasi baris Transfer aset `Dongkrak Hidrolik {runId}` ditandai In-transit overdue

### Destination quota check: hanya baris yang ber-Destination quota check ON yang dihitung
159. Alokasi kuota per Group diaktifkan di client
160. Wulan menambah override aset untuk aset `Kotak Peralatan Cadangan {runId}` di All categories dengan Destination quota check `OFF`
161. Rizal mengajukan satu Transfer berisi aset `Pallet Kayu 1 {runId}`, `Pallet Kayu 2 {runId}`, `Pallet Kayu 3 {runId}`, dan `Kotak Peralatan Cadangan {runId}` ke Group `Cabang Bogor {runId}`, yang sisa kuotanya 2
162. Verifikasi pengajuan ditolak seluruhnya karena tiga baris ber-Destination quota check `ON` melebihi sisa kuota 2, dan tidak ada baris Transfer dibuat untuk satu pun dari keempat aset
163. Rizal mengajukan satu Transfer berisi aset `Pallet Kayu 1 {runId}`, `Pallet Kayu 2 {runId}`, dan `Kotak Peralatan Cadangan {runId}` ke Group `Cabang Bogor {runId}`
164. Verifikasi pengajuan diterima dan tiga baris Transfer dibuat, karena hanya dua baris ber-Destination quota check `ON` yang dihitung terhadap sisa kuota 2, sedangkan bila baris `OFF` ikut dihitung tiga baris melebihi sisa kuota

### Perubahan Cost Center with Group Always berlaku sejak periode penyusutan berikutnya
165. Waktu berlalu sampai periode penyusutan berikutnya dimulai
166. Verifikasi beban penyusutan periode berikutnya aset `Rak Besi Tinggi {runId}` tercatat pada Cost Center `CC-SBY-{runId}`
