---
id: TC-FA-MISS-E2E-007-tab-history-tampilan-tabel
title: "Tab History: kolom default, Duration, Resolved By, nilai beku, urutan default, dan Missing Log read-only"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1b#r1, §4.1b#r2, §4.1b#r3, §4.1b#r4, §4.1b#r5, §4.1b#r6, §4.1b#r7, §4.1b#r8, §4.1b#r9, §4.1b#r10, §4.1b#r11, §4.1b#r12, §4.1b#r13, §4.1b#r14, §4.1b#r15, §4.1b#r16, §4.1b#r17, §4.1b#r18, §4.1b#r19, §4.1b#r20, §4.1b#r21, §4.1b#r22, §4.1b#r23, §4.1b#r24, §4.1b#r25, §4.1b#r26, §4.1b#r27, §4.1b#p1, §4.1b#p3, §9.5#r3, §5#r5, §4.1#p3, §1.2#r17, §4.1#r2, §9.2#b16, §4.4#r1, §10#r5]
smoke: []
dependsOn: []
trace:
  §4.1b#r1: [11, 18]
  §4.1b#r2: [11, 19, 32]
  §4.1b#r3: [11, 20]
  §4.1b#r4: [12, 15]
  §4.1b#r5: [12, 15]
  §4.1b#r6: [12, 15]
  §4.1b#r7: [12, 15]
  §4.1b#r8: [11, 30]
  §4.1b#r9: [11, 21]
  §4.1b#r10: [11, 22]
  §4.1b#r11: [11, 23, 24]
  §4.1b#r12: [11, 25]
  §4.1b#r13: [11, 26]
  §4.1b#r14: [11, 27]
  §4.1b#r15: [11, 28]
  §4.1b#r16: [11, 29]
  §4.1b#r17: [12, 15]
  §4.1b#r18: [12, 15]
  §4.1b#r19: [12, 15]
  §4.1b#r20: [12, 15]
  §4.1b#r21: [12, 15]
  §4.1b#r22: [12, 15]
  §4.1b#r23: [12, 15]
  §4.1b#r24: [12, 15, 67, 76, 79, 81, 83, 86, 92, 93]
  §4.1b#r25: [12, 15, 31]
  §4.1b#r26: [12, 15, 56]
  §4.1b#r27: [12, 15]
  §4.1b#p1: [9, 10, 21, 23, 30, 31, 32, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 72]
  §4.1b#p3: [34, 35, 37]
  §9.5#r3: 8
  §5#r5: 10
  §4.1#p3: [11, 15, 26, 29]
  §1.2#r17: 7
  §4.1#r2: [5, 9]
  §9.2#b16: 7
  §4.4#r1: [5, 8]
  §10#r5: 7
anchor: [84]
coverage:
  web: automated
---

# Tab History: kolom default, Duration, Resolved By, nilai beku, urutan default, dan Missing Log read-only

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-007-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini, tampil sebagai `Rina W`, dari `Rina Wijaya {runId}`.
  - DU-007-2: User `Sari Dewi {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing, kemudian dinonaktifkan; tampil sebagai `Sari D`, dari `Sari Dewi {runId}`.
  - DU-007-3: User `Agus Prasetyo {runId}`, role Manage asset & TAG (Update); tampil sebagai `Agus P`, dari `Agus Prasetyo {runId}`.
  - DU-007-4: User `Budi Santoso {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-007-5: User `Joko Susilo {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing; tampil sebagai `Joko S`, dari `Joko Susilo {runId}`.
  - DU-007-6: Record `Found` untuk aset `Kamera Baru {runId}` yang namanya sebelum record selesai `Kamera Lama {runId}`, Source `Borrow`, Last Holder `Sari Dewi {runId}`, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 30 hari pukul `09:00`, Resolved By `Rina Wijaya {runId}`, Resolved Date T0 − 24 hari pukul `14:10`; Duration `6 days`, dari selisih 6 hari kalender. Saat record selesai Group aset `Gudang Lama {runId}` dan Purchase Cost `5000000`; sesudahnya aset dipindah ke Group `Gudang Baru {runId}` dan Purchase Cost menjadi `5500000`. Saat record selesai Category aset `Elektronik {runId}`, Asset Value (Commercial) `4200000`, dan Asset Value (Fiscal) `4000000`; sesudahnya Category menjadi `Peralatan Studio {runId}`, Asset Value (Commercial) `3900000`, dan Asset Value (Fiscal) `3800000`. Data aset terkini: Brand `Sonora {runId}` (sebelum record selesai `Merk Lama {runId}`), Model/Type `Alpha 7 {runId}`, TAG `RFID`, Labels `Studio {runId}`, Division `Produksi {runId}`, Measurement `Pcs`, Asset Class `Peralatan {runId}`, Register Date T0 − 400 hari, Purchase Date T0 − 410 hari, dan daftar garansi aset `Garansi Unit {runId}` sampai T0 + 300 hari serta `Garansi Servis {runId}` sampai T0 + 540 hari, sehingga Warranty Expiry (Warranty until terdekat) T0 + 300 hari. Asset ID dibentuk server dan menjadi milik entri ini.
  - DU-007-7: Record `Disposed` untuk aset `Bor Listrik {runId}` (Group `Gudang Lama {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Agus Prasetyo {runId}`, Reported Date T0 − 70 hari pukul `08:00`, Resolved By `System`, Resolved Date T0 − 8 hari pukul `00:00`; Duration `62 days`, dari selisih 62 hari kalender.
  - DU-007-8: Record `Rejected` untuk aset `Mesin Foto {runId}` (Group `Gudang Lama {runId}`), Source `Reported by holder`, Last Holder `Budi Santoso {runId}`, Reported By `Budi Santoso {runId}`, Reported Date T0 − 10 hari pukul `08:30`, Resolved By `Rina Wijaya {runId}`, Resolved Date T0 − 9 hari pukul `09:15`; Duration `1 day`, dari selisih 1 hari kalender.
  - DU-007-9: Record `Canceled` untuk aset `Pemindai Gudang {runId}` (Group `Gudang Lama {runId}`), Source `Reported by holder`, Last Holder `Joko Susilo {runId}`, Reported By `Joko Susilo {runId}`, Reported Date T0 − 12 hari pukul `13:00`, Resolved By `Joko Susilo {runId}` sebagai pelapor, Resolved Date T0 − 11 hari pukul `08:20`; Duration `1 day`, dari selisih 1 hari kalender.
  - DU-007-10: Record `Found` untuk aset `Gerinda Tangan {runId}` (Group `Gudang Lama {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Agus Prasetyo {runId}`, Reported Date T0 − 55 hari, Resolved By `Wulan Pertiwi {runId}` (DU-007-12), Resolved Date T0 − 50 hari; Duration `5 days`, dari selisih 5 hari kalender.
  - DU-007-11: Record `Canceled` untuk aset `Gerinda Tangan {runId}` yang sama dengan DU-007-10 karena aset itu hilang berulang, Source `Reported by holder`, Last Holder `Budi Santoso {runId}`, Reported By `Budi Santoso {runId}`, Reported Date T0 − 45 hari, Resolved By `Budi Santoso {runId}`, Resolved Date T0 − 44 hari; Duration `1 day`, dari selisih 1 hari kalender.
  - DU-007-12: User `Wulan Pertiwi {runId}`, role Manage asset & TAG (Update), menyelesaikan record DU-007-10 lalu dinonaktifkan; tampil sebagai `Wulan P`, dari `Wulan Pertiwi {runId}`.
  - DU-007-13: Daftar garansi tambahan: aset `Bor Listrik {runId}` (DU-007-7) punya `Garansi Bor {runId}` sampai T0 + 100 hari, aset `Pemindai Gudang {runId}` (DU-007-9) punya `Garansi Pemindai {runId}` sampai T0 + 200 hari, dan aset `Mesin Foto {runId}` (DU-007-8) punya `Garansi Mesin Foto {runId}` sampai T0 + 450 hari. Aset `Gerinda Tangan {runId}` (DU-007-10 dan DU-007-11) tanpa garansi. Warranty until terdekat: `Bor Listrik {runId}` T0 + 100 hari, `Pemindai Gudang {runId}` T0 + 200 hari, `Kamera Baru {runId}` T0 + 300 hari (DU-007-6), dan `Mesin Foto {runId}` T0 + 450 hari.
  - DU-007-14: kata kunci Search `Garansi Unit {runId}`, nama garansi aset DU-007-6 yang hanya ada di daftar garansi dan tidak cocok dengan kolom lain.
  - DU-007-15: rentang Warranty Expiry dari T0 + 150 hari sampai T0 + 350 hari, memuat Warranty until terdekat `Pemindai Gudang {runId}` (T0 + 200 hari) dan `Kamera Baru {runId}` (T0 + 300 hari), dan tidak memuat T0 + 100 hari maupun T0 + 450 hari.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; tanggal pada entri di atas dihitung relatif terhadap T0.

## Test Steps

### Sub-tab History tersimpan di URL dan terisolasi dari sort tab Active
1. Klik tab `Missing` pada halaman Assets
2. Klik header `Reported Date` pada tabel tab Active
3. Klik sub-tab `History`
4. Muat ulang halaman
5. Verifikasi sub-tab `History` tetap aktif sesudah halaman dimuat ulang karena sub-tab tersimpan di URL
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi tabel memuat baris untuk `Kamera Baru {runId}`, `Bor Listrik {runId}`, `Mesin Foto {runId}`, `Pemindai Gudang {runId}` yang berstatus `Found`, `Disposed`, `Rejected`, dan `Canceled`
8. Verifikasi urutan baris dari atas ke bawah: `Bor Listrik {runId}`, `Mesin Foto {runId}`, `Pemindai Gudang {runId}`, `Kamera Baru {runId}`, lalu dua baris `Gerinda Tangan {runId}`, yaitu Resolved Date terbaru dulu, walau tabel tab Active sedang diurutkan menurut `Reported Date`

### Toolbar dan kolom tab History
9. Verifikasi toolbar tab History memuat Search, Filter, dan Download, dan tidak memuat `[Scan Found Asset]`
10. Verifikasi tabel tab History tidak memiliki kolom Checkbox dan tidak menampilkan aksi bulk
11. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Group`, `Status`, `Source`, `Last Holder`, `Reported By`, `Reported Date`, `Duration`, `Resolved By`, `Resolved Date`, dengan `Status` tepat setelah `Group` dan `Resolved Date` sebagai kolom data terakhir sebelum Actions
12. Verifikasi kolom `Brand`, `Model/Type`, `TAG`, `Category`, `Alias Name`, `Measurement`, `Division`, `Labels`, `Asset Class`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, `Asset Value (Fiscal)` tidak tampil sebagai kolom bawaan
13. Klik header kolom Actions
14. Klik `Setup Column...`
15. Verifikasi di modal `Setup Column` kolom `Photo`, `Name`, `Asset ID`, `Group`, `Status`, `Source`, `Last Holder`, `Reported By`, `Reported Date`, `Duration`, `Resolved By`, `Resolved Date` tercentang dan kolom `Brand`, `Model/Type`, `TAG`, `Category`, `Alias Name`, `Measurement`, `Division`, `Labels`, `Asset Class`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, `Asset Value (Fiscal)` tidak tercentang
16. Centang kolom `Purchase Cost`
17. Klik `[Save]`

### Isi sel dari data awal
18. Verifikasi kolom Photo menampilkan foto aset atau avatar inisial pada setiap baris
19. Verifikasi kolom Name setiap baris berformat `[Asset Name] - [Increment]`, dengan nama aset `Bor Listrik {runId}`, `Mesin Foto {runId}`, `Pemindai Gudang {runId}`, `Kamera Baru {runId}`, `Gerinda Tangan {runId}` dan Increment milik entri datanya
20. Verifikasi kolom Asset ID setiap baris menampilkan Asset ID milik entri datanya, DU-007-6 sampai DU-007-11
21. Verifikasi kolom Status menampilkan `Found` pada baris `Kamera Baru {runId}`, `Disposed` pada baris `Bor Listrik {runId}`, `Rejected` pada baris `Mesin Foto {runId}`, dan `Canceled` pada baris `Pemindai Gudang {runId}`
22. Verifikasi kolom Source menampilkan `Borrow` pada baris `Kamera Baru {runId}`, `Manual` pada baris `Bor Listrik {runId}`, dan `Reported by holder` pada baris `Mesin Foto {runId}` dan `Pemindai Gudang {runId}`
23. Verifikasi kolom Last Holder menampilkan `Sari D` pada baris `Kamera Baru {runId}`, `Budi S` pada baris `Mesin Foto {runId}`, dan `Joko S` pada baris `Pemindai Gudang {runId}`, dan `Sari D` tetap tampil walau penggunanya sudah dinonaktifkan
24. Verifikasi kolom Last Holder menampilkan `—` pada baris `Bor Listrik {runId}` karena asetnya tidak dipegang
25. Verifikasi kolom Reported By menampilkan `Rina W` pada baris `Kamera Baru {runId}`, `Agus P` pada baris `Bor Listrik {runId}`, `Budi S` pada baris `Mesin Foto {runId}`, dan `Joko S` pada baris `Pemindai Gudang {runId}`
26. Verifikasi kolom Reported Date baris `Kamera Baru {runId}` menampilkan tanggal T0 − 30 hari dengan format `DD/MM/YY` dan jam `09:00`
27. Verifikasi kolom Duration menampilkan `6 days` pada baris `Kamera Baru {runId}`, `62 days` pada baris `Bor Listrik {runId}`, dan `1 day` pada baris `Mesin Foto {runId}` dan `Pemindai Gudang {runId}`
28. Verifikasi kolom Resolved By menampilkan `Rina W` pada baris `Kamera Baru {runId}` dan `Mesin Foto {runId}`, `System` pada baris `Bor Listrik {runId}` yang `Disposed`, dan `Joko S` pada baris `Pemindai Gudang {runId}` yang dibatalkan pelapornya
29. Verifikasi kolom Resolved Date baris `Kamera Baru {runId}` menampilkan tanggal T0 − 24 hari dengan format `DD/MM/YY` dan jam `14:10`

### Nilai beku saat record selesai dan nilai yang mengikuti aset terkini
30. Verifikasi kolom Group baris `Kamera Baru {runId}` menampilkan `Gudang Lama {runId}`, nilai yang dibekukan saat record selesai, dan bukan `Gudang Baru {runId}`
31. Verifikasi kolom Purchase Cost baris `Kamera Baru {runId}` menampilkan nilai beku `5000000` dan bukan `5500000`
32. Verifikasi kolom Name baris `Kamera Baru {runId}` menampilkan nama aset terkini dan bukan `Kamera Lama {runId}`

### Missing Log read-only dari tab History
33. Klik `⋯` pada baris `Bor Listrik {runId}`
34. Verifikasi menu baris `Bor Listrik {runId}` memuat `Missing Log`
35. Verifikasi menu baris `Bor Listrik {runId}` tidak memuat `Report Disposal`, `Mark as Found`, `Add Update`, `Review`, maupun `Cancel Disposal Report`
36. Klik `Missing Log` pada menu
37. Verifikasi dialog `Missing Log` terbuka untuk record baris `Bor Listrik {runId}` tanpa tombol `[Reject]` dan `[Confirm]`
38. Tekan Esc untuk menutup dialog `Missing Log`

### Kolom beku dan kolom turunan aset pada record yang sudah selesai
39. Klik header kolom Actions
40. Klik `Setup Column...`
41. Centang kolom `Category`
42. Centang kolom `Asset Value (Commercial)`
43. Centang kolom `Asset Value (Fiscal)`
44. Centang kolom `Brand`
45. Centang kolom `Model/Type`
46. Centang kolom `TAG`
47. Centang kolom `Labels`
48. Centang kolom `Division`
49. Centang kolom `Measurement`
50. Centang kolom `Asset Class`
51. Centang kolom `Register Date`
52. Centang kolom `Purchase Date`
53. Centang kolom `Warranty Expiry`
54. Klik `[Save]`
55. Verifikasi kolom Category baris `Kamera Baru {runId}` menampilkan `Elektronik {runId}`, nilai yang dibekukan saat record selesai, dan bukan `Peralatan Studio {runId}`
56. Verifikasi kolom Asset Value (Commercial) baris `Kamera Baru {runId}` menampilkan nilai beku `4200000` dan bukan `3900000`
57. Verifikasi kolom Asset Value (Fiscal) baris `Kamera Baru {runId}` menampilkan nilai beku `4000000` dan bukan `3800000`
58. Verifikasi kolom Brand baris `Kamera Baru {runId}` menampilkan `Sonora {runId}`, data aset terkini, dan bukan `Merk Lama {runId}`
59. Verifikasi kolom Model/Type baris `Kamera Baru {runId}` menampilkan `Alpha 7 {runId}` sesuai data aset terkini
60. Verifikasi kolom TAG baris `Kamera Baru {runId}` menampilkan ikon `RFID` sesuai data aset terkini
61. Verifikasi kolom Labels baris `Kamera Baru {runId}` menampilkan `Studio {runId}` sesuai data aset terkini
62. Verifikasi kolom Division baris `Kamera Baru {runId}` menampilkan `Produksi {runId}` sesuai data aset terkini
63. Verifikasi kolom Measurement baris `Kamera Baru {runId}` menampilkan `Pcs` sesuai data aset terkini
64. Verifikasi kolom Asset Class baris `Kamera Baru {runId}` menampilkan `Peralatan {runId}` sesuai data aset terkini
65. Verifikasi kolom Register Date baris `Kamera Baru {runId}` menampilkan tanggal T0 − 400 hari dengan format `DD/MM/YY` sesuai data aset terkini
66. Verifikasi kolom Purchase Date baris `Kamera Baru {runId}` menampilkan tanggal T0 − 410 hari dengan format `DD/MM/YY` sesuai data aset terkini
67. Verifikasi kolom Warranty Expiry baris `Kamera Baru {runId}` menampilkan Warranty until terdekat dari daftar garansi aset, yaitu tanggal T0 + 300 hari dengan format `DD/MM/YY` sesuai data aset terkini, dan bukan tanggal T0 + 540 hari

### Aset yang pernah hilang berulang tampil sebagai dua baris
68. Ganti isi kotak search dengan `Gerinda Tangan {runId}`, tekan Enter
69. Verifikasi tabel memuat dua baris untuk aset `Gerinda Tangan {runId}`: satu berstatus `Canceled` dengan Duration `1 day` dan satu berstatus `Found` dengan Duration `5 days`
70. Klik `(←)` pada kotak Search

### Resolved By tetap tampil bila penggunanya dinonaktifkan
71. Ganti isi kotak search dengan `Gerinda Tangan {runId}`, tekan Enter
72. Verifikasi kolom Resolved By baris `Gerinda Tangan {runId}` yang berstatus `Found` menampilkan `Wulan P` walau penggunanya sudah dinonaktifkan
73. Klik `(←)` pada kotak Search

### Warranty Expiry menampilkan daftar seluruh garansi
74. Ketik Search `Kamera Baru {runId}`, tekan Enter
75. Arahkan kursor ke sel kolom Warranty Expiry baris `Kamera Baru {runId}`
76. Verifikasi daftar seluruh garansi aset tampil dengan format `[Warranty name] — [tanggal]`: `Garansi Unit {runId}` bertanggal T0 + 300 hari dan `Garansi Servis {runId}` bertanggal T0 + 540 hari, dengan tanggal berformat `DD/MM/YY`
77. Klik `(←)` pada kotak Search

### Warranty Expiry diurutkan menurut Warranty until terdekat
78. Ketik Search `{runId}`, tekan Enter
79. Verifikasi kolom Warranty Expiry menampilkan tanggal T0 + 100 hari pada baris `Bor Listrik {runId}`, T0 + 200 hari pada baris `Pemindai Gudang {runId}`, T0 + 300 hari pada baris `Kamera Baru {runId}`, dan T0 + 450 hari pada baris `Mesin Foto {runId}`, dengan format `DD/MM/YY`, dan `—` pada kedua baris `Gerinda Tangan {runId}` karena asetnya tanpa garansi
80. Klik header `Warranty Expiry`
81. Verifikasi urutan baris dari atas ke bawah menurut Oldest First atas Warranty until terdekat: `Bor Listrik {runId}`, `Pemindai Gudang {runId}`, `Kamera Baru {runId}`, `Mesin Foto {runId}`, lalu kedua baris `Gerinda Tangan {runId}` yang tanpa garansi di akhir, dengan `Kamera Baru {runId}` sebelum `Mesin Foto {runId}` walau garansi terjauhnya (T0 + 540 hari) lebih akhir
82. Klik header `Warranty Expiry`
83. Verifikasi urutan baris dari atas ke bawah menurut Newest First atas Warranty until terdekat: kedua baris `Gerinda Tangan {runId}` yang tanpa garansi di awal, lalu `Mesin Foto {runId}`, `Kamera Baru {runId}`, `Pemindai Gudang {runId}`, `Bor Listrik {runId}`

### Warranty Expiry tidak ikut dicari oleh Search
84. Verifikasi baris `Kamera Baru {runId}` tampil pada hasil Search `{runId}`
85. Ganti isi kotak search dengan `Garansi Unit {runId}`, tekan Enter
86. Verifikasi `No results found` dan `Try adjusting your search or filter.` tampil karena Warranty Expiry bukan kolom yang dicari Search, walau baris `Kamera Baru {runId}` memuat garansi `Garansi Unit {runId}`
87. Klik `(←)` pada kotak Search

### Filter rentang Warranty Expiry memakai Warranty until terdekat
88. Ketik Search `{runId}`, tekan Enter
89. Klik ikon Filter
90. Pilih rentang Warranty Expiry dari `T0 + 150 hari` sampai `T0 + 350 hari` sesuai DU-007-15
91. Klik `[Apply]`
92. Verifikasi tabel memuat baris `Pemindai Gudang {runId}` yang Warranty until terdekatnya T0 + 200 hari dan baris `Kamera Baru {runId}` yang T0 + 300 hari, keduanya di dalam rentang
93. Verifikasi baris `Bor Listrik {runId}` yang Warranty until terdekatnya T0 + 100 hari, baris `Mesin Foto {runId}` yang T0 + 450 hari, dan kedua baris `Gerinda Tangan {runId}` yang tanpa garansi, tidak tampil
94. Klik `[Clear Field]`
95. Klik `[Apply]`
96. Klik `(←)` pada kotak Search
