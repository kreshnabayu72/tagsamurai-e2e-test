---
id: TC-FA-MISS-E2E-036-report-disposal-dep-transactions-disposal
title: "Report Disposal satu record dan Cancel Disposal Report: status Reported Disposal, Mark as Found Hidden, kembali Missing, node Disposal"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.1#r5", "§4.1a#r33", "§4.1a#r34", "§4.4#r9", "§4.4#r11", "§4.2.4#r21", "§4.2.4#r22", "§4.2.4#p8", "§4.2.4#p14", "§7.2#r4", "§7.2#r16", "§7.2#r17", "§7.3#r10", "§9.6#r9", "§9.2#r3", "§9.2#r4", "§9.2#b28", "§9.2#b29", "§9.4.2#r11", "§9.4.2#r12", "§9.4.4#r14", "§9.4.4#r15", "§8.1#r15", "§8.1#r16", "§8.1#r17", "§8.1#r18", "§8#r11", "§8.1#p2", "§9.7#r5", "§9.8#p2", "§3#p8", "§4.3#r3", "§4.3#r6", "§2.1#r9", "§2.1#r10", "§2.1#b5", "§4.8#r8", "§4.1#r11", "§4.1#r8", "§6#r2", "§6#r3", "§9.2#p11", "§9.2#p12", "§9.2#p13", "§11#r7", "§1#b4", "§1.2#r17", "§1.2#r20", "§1.2#r21", "§1.2#r93", "§1.2#r94", "§1.2#r95", "§1.2#r96", "§1.2#r97", "§1.2#r98", "§1.2#r99", "§1.2#r100", "§1.2#r34", "§1.2#r35", "§1.2#r112", "§10#r4", "§8.2#b2", "§9.4.1#r3", "EB-FB-1@report-disposal", "EB-FB-1@cancel-disposal-report", "§1.2#r44"]
smoke: []
dependsOn: ["Transactions Disposal: dialog Report Disposal D-DISP-13", "Transactions Disposal: tab Reported > Decline dan Cancel Report", "Transactions Disposal: Dispose > form Request Lost / Write-off"]
trace:
  "§9.1#r5": [10, 19]
  "§4.1a#r33": [4, 73]
  "§4.1a#r34": [14, 55]
  "§4.4#r9": [6, 10]
  "§4.4#r11": [19]
  "§4.2.4#r21": [10]
  "§4.2.4#r22": [19]
  "§4.2.4#p8": [16]
  "§4.2.4#p14": [6, 87]
  "§7.2#r4": [16]
  "§7.2#r16": [10]
  "§7.2#r17": [19]
  "§7.3#r10": [18]
  "§9.6#r9": [9, 18]
  "§9.2#r3": [10]
  "§9.2#r4": [51]
  "§9.2#b28": [10, 19, 61]
  "§9.2#b29": [14, 51, 83, 91]
  "§9.4.2#r11": [36, 38]
  "§9.4.2#r12": [13, 21, 54]
  "§9.4.4#r14": [23, 38, 67]
  "§9.4.4#r15": [13, 24]
  "§8.1#r15": [23]
  "§8.1#r16": [38]
  "§8.1#r17": [24]
  "§8.1#r18": [67]
  "§8#r11": [23, 24, 38, 67]
  "§8.1#p2": [61, 77]
  "§9.7#r5": [10, 19, 61]
  "§9.8#p2": [10, 19, 61]
  "§3#p8": [10, 19, 36, 51, 61]
  "§4.3#r3": [13, 54]
  "§4.3#r6": [55]
  "§2.1#r9": [4]
  "§2.1#r10": [14]
  "§2.1#b5": [4, 14]
  "§4.8#r8": [4, 14]
  "§4.1#r11": [6]
  "§4.1#r8": [16]
  "§6#r2": [54]
  "§6#r3": [55]
  "§9.2#p11": [10, 51]
  "§9.2#p12": [61]
  "§9.2#p13": [13, 54]
  "§11#r7": [10, 77]
  "§1#b4": [77]
  "§1.2#r17": [10, 51]
  "§1.2#r20": [19, 36]
  "§1.2#r21": [61]
  "§1.2#r93": [10]
  "§1.2#r94": [10]
  "§1.2#r95": [6, 51]
  "§1.2#r96": [51]
  "§1.2#r97": [51]
  "§1.2#r98": [19]
  "§1.2#r99": [14, 55]
  "§1.2#r100": [10, 51]
  "§1.2#r34": [6]
  "§1.2#r35": [6]
  "§1.2#r112": [71, 73]
  "§10#r4": [64, 65]
  "§8.2#b2": [9, 18]
  "§9.4.1#r3": [13, 54]
  "EB-FB-1@report-disposal": [9]
  "EB-FB-1@cancel-disposal-report": [18]
  "§1.2#r44": [77]
anchor: [3, 12, 53, 82]
coverage:
  web: automated
---

# Report Disposal satu record dan Cancel Disposal Report: status Reported Disposal, Mark as Found Hidden, kembali Missing, node Disposal

## Prerequisites
- Aktor: Total Control `Rina W`, yang juga Aktor Disposal.
- Layar awal: Assets > Missing > Active.
- Data:
  - DU-036-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, dengan record Missing berstatus `Missing`.
  - DU-036-2: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing`.
  - DU-036-3: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing`.
  - DU-036-4: Asset `Drill Bosch GSB {runId}`, Group `Warehouse`, dengan record Missing berstatus `Disposed` yang ditutup `System` pada Disposal Executed, beserta Disposal No. milik entri ini.
  - DU-036-5: Asset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing` yang dilaporkan pada `T0 − 34 hari`.
  - DU-036-6: Asset `Camera Canon EOS {runId}`, Group `Head Office`, tanpa record Missing, dengan Disposal Report berstatus `Reported`.
  - DU-036-7: Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`.
  - DU-036-8: Reason `Aset hilang saat pemindahan gudang`.
  - DU-036-9: Reason `Aset tidak ada di lokasi terakhir`.
  - DU-036-10: Reason Decline `Aset masih dalam penelusuran`.
  - DU-036-11: What happened `Kamera hilang dari ruang studio setelah sesi foto`.
- Kondisi:
  - Long missing after bernilai `30`.
  - Date Format bernilai `DD/MM/YY`.
  - Time Format bernilai `HH:mm`.
  - Akun `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Disposal lalu Cancel Disposal Report atas satu record
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Mark as Found` tampil pada menu
4. Verifikasi aksi `Report Disposal` tampil pada menu
5. Klik `Report Disposal`
6. Verifikasi dialog `Report Disposal` hanya memuat isian `Reason`
7. Isi Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`
8. Kirim dialog Report Disposal
9. Verifikasi toast `Success, disposal report has been created.` tampil
10. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab Active berstatus `Reported Disposal`
11. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
12. Verifikasi aksi `Missing Log` tampil pada menu
13. Verifikasi aksi `Mark as Found` tidak tampil pada menu
14. Verifikasi aksi `Cancel Disposal Report` tampil pada menu
15. Klik `Cancel Disposal Report`
16. Verifikasi dialog `Cancel Disposal Report` terbuka
17. Kirim dialog Cancel Disposal Report
18. Verifikasi toast sukses Cancel Disposal Report tampil
19. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` kembali berstatus `Missing`
20. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
21. Verifikasi aksi `Mark as Found` tampil kembali pada menu

### Node Disposal di Missing Log
22. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
23. Verifikasi dialog Missing Log memuat node `Disposal reported by` oleh `Rina W` dengan Report ID dan Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`
24. Verifikasi dialog Missing Log memuat node `Disposal report canceled by` oleh `Rina W` dengan Back to Missing `Yes`
25. Tutup dialog Missing Log dengan `✕`

### Decline Report oleh Aktor Disposal mengembalikan record ke Missing
26. Ganti isi kotak search dengan `Hand Pallet Truck {runId}`, tekan Enter
27. Buka menu `⋯` pada baris `Hand Pallet Truck {runId}`
28. Klik `Report Disposal`
29. Isi Reason `Aset hilang saat pemindahan gudang`
30. Kirim dialog Report Disposal
31. Buka tab `Reported` pada `Transactions > Disposal`
32. Lakukan Decline atas Report `Hand Pallet Truck {runId}` dengan Reason `Aset masih dalam penelusuran`
33. Buka halaman `Assets`
34. Klik tab `Missing`
35. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
36. Verifikasi baris `Hand Pallet Truck {runId}` berstatus `Missing`
37. Klik `Hand Pallet Truck {runId}` pada kolom Name
38. Verifikasi dialog Missing Log memuat node `Disposal report declined by` oleh `Rina W` dengan Reason `Aset masih dalam penelusuran` dan Back to Missing `Yes`
39. Tutup dialog Missing Log dengan `✕`

### Dispose menjadikan record In Disposal Process dan batalnya baris mengembalikan ke Missing
40. Ganti isi kotak search dengan `Scanner Zebra DS2208 {runId}`, tekan Enter
41. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
42. Klik `Report Disposal`
43. Isi Reason `Aset tidak ada di lokasi terakhir`
44. Kirim dialog Report Disposal
45. Buka tab `Reported` pada `Transactions > Disposal`
46. Klik `Dispose` pada Report `Scanner Zebra DS2208 {runId}`
47. Kirim form Request Disposal jenis `Lost` atas `Scanner Zebra DS2208 {runId}`
48. Buka halaman `Assets`
49. Klik tab `Missing`
50. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
51. Verifikasi baris `Scanner Zebra DS2208 {runId}` berstatus `In Disposal Process`
52. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
53. Verifikasi aksi `Missing Log` tampil pada menu
54. Verifikasi aksi `Mark as Found` tidak tampil pada menu
55. Verifikasi aksi `Cancel Disposal Report` tidak tampil pada menu
56. Tutup menu `⋯` dengan tombol Esc
57. Batalkan baris Request Disposal atas `Scanner Zebra DS2208 {runId}` di `Transactions > Disposal`
58. Buka halaman `Assets`
59. Klik tab `Missing`
60. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
61. Verifikasi baris `Scanner Zebra DS2208 {runId}` kembali berstatus `Missing`

### Record Disposed tampil di History dengan node Disposed
62. Klik sub-tab `History`
63. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
64. Verifikasi baris `Drill Bosch GSB {runId}` berstatus `Disposed`
65. Verifikasi kolom Resolved By pada baris itu `System`
66. Klik `Drill Bosch GSB {runId}` pada kolom Name
67. Verifikasi dialog Missing Log memuat node `Disposed` oleh `System` dengan Disposal No. milik DU-036-4
68. Tutup dialog Missing Log dengan `✕`

### Record Long missing mendapat saran Report Disposal
69. Klik sub-tab `Active`
70. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
71. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId}` memuat penanda `Long missing`
72. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
73. Verifikasi aksi `Report Disposal` tampil pada menu

### Report Missing atas aset dengan Disposal Report Reported
74. Rina W melaporkan `Camera Canon EOS {runId}` hilang lewat Report Missing dengan What happened `Kamera hilang dari ruang studio setelah sesi foto`
75. Buka tab `Reported` pada `Transactions > Disposal`
76. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
77. Verifikasi Report atas `Camera Canon EOS {runId}` berstatus `Canceled` dengan alasan `Asset reported missing` oleh `System`

### Aksi Cancel Disposal Report tidak tampil pada record Missing
78. Buka halaman `Assets`
79. Klik tab `Missing`
80. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
81. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
82. Verifikasi aksi `Report Disposal` tampil pada menu
83. Verifikasi aksi `Cancel Disposal Report` tidak tampil pada menu
84. Tutup menu `⋯` dengan tombol Esc

### Dialog Report Disposal memuat aset yang dipilih
85. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
86. Klik `Report Disposal`
87. Verifikasi dialog `Report Disposal` memuat aset `Laptop Lenovo ThinkPad T14 {runId}`
88. Tutup dialog Report Disposal tanpa mengirim

### Cancel Disposal Report membatalkan Report di tab Reported
89. Buka tab `Reported` pada `Transactions > Disposal`
90. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
91. Verifikasi Report atas `Laptop Dell Latitude 5420 {runId}` berstatus `Canceled`
