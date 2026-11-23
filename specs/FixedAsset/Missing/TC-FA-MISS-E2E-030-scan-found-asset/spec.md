---
id: TC-FA-MISS-E2E-030-scan-found-asset
title: "Scan Found Asset: pemindaian langsung membuka Mark as Found terverifikasi, dan guard berurutan menampilkan Cannot Mark as Found"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r3", "§4.2.1#b2", "§4.4#r2", "§4.2.4#r18", "§9.2#b18", "§6#r5", "§6#r6", "§6#r7", "§6#r8", "§6#p2", "§6#p3", "§7.2#r6", "§7.2#r12", "§4.2.4#p11", "§9.4.2#r24", "§9.4.2#r25", "§9.4.2#r26", "§9.4.4#r5", "§2.1#r12", "§9.2#b41", "§9.2#b42", "§9.2#b44", "§4.8#r11", "§9.9#r2", "§6#r4", "§4.3#r8", "§9.9#p3", "§1.2#r113"]
smoke: []
dependsOn: []
trace:
  "§4.1#r3": [8, 13, 17, 24, 48, 68]
  "§4.2.1#b2": [48, 49, 65, 70, 71, 72]
  "§4.4#r2": [48, 51, 54]
  "§4.2.4#r18": 48
  "§9.2#b18": [8, 13, 17, 24, 37]
  "§6#r5": [13, 93, 97, 101, 105]
  "§6#r6": [8, 9]
  "§6#r7": [17, 88]
  "§6#r8": 24
  "§6#p2": [8, 13, 17, 24, 79, 80, 84, 88, 109, 110]
  "§6#p3": [13, 31, 35]
  "§7.2#r6": [8, 31, 35]
  "§7.2#r12": [8, 13, 17, 24, 31, 35]
  "§4.2.4#p11": [8, 13, 17, 24, 31, 35]
  "§9.4.2#r24": 13
  "§9.4.2#r25": [8, 9]
  "§9.4.2#r26": [17, 88, 89]
  "§9.4.4#r5": [8, 9, 13, 17]
  "§2.1#r12": [5, 8]
  "§9.2#b41": 56
  "§9.2#b42": [20, 27]
  "§9.2#b44": [8, 9]
  "§4.8#r11": 3
  "§9.9#r2": [41, 44]
  "§6#r4": 44
  "§4.3#r8": 48
  "§9.9#p3": 41
  "§1.2#r113": [113, 114, 115, 116]
anchor: [4, 64]
coverage:
  web: manual
---

# Scan Found Asset: pemindaian langsung membuka Mark as Found terverifikasi, dan guard berurutan menampilkan Cannot Mark as Found

## Prerequisites
- Aktor: Group Manager dengan Group binaan `Head Office {runId}`, yang punya sub-group `Finance Room {runId}`; pembaca TAG tersedia bagi aktor, dan aktor adalah Last holder record DU-030-5 dan DU-030-9.
- Layar awal: halaman Assets.
- Data:
  - DU-030-1: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`, TAG `QR`.
  - DU-030-2: Missing record, Name `Hand Pallet Truck {runId} - 3`, Asset ID `HPT-0003 {runId}`, Group `Warehouse {runId}` (di luar Group binaan), Status `Missing`, Source `Manual`, Last Holder `—`, TAG `QR`.
  - DU-030-3: Asset, Name `Scanner Zebra DS2208 {runId} - 2`, Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `SCN-0002 {runId}`, Group `Finance Room {runId}`, Status `Available`, TAG `QR`, tanpa record Missing berjalan.
  - DU-030-4: Missing record, Name `Projector Epson EB-X06 {runId} - 7`, Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `PRJ-0007 {runId}`, Group `Head Office {runId}`, Status `Reported Disposal`, Source `Audit`, Last Holder `—`, TAG `QR`.
  - DU-030-5: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Borrow`, Last Holder `aktor spec ini`, TAG `QR`.
  - DU-030-6: Missing record, Name `Printer HP LaserJet M404 {runId} - 5`, Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `PRN-0005 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`, TAG `QR`.
  - DU-030-7: Missing record, Asset Name `Tablet Samsung Galaxy Tab {runId}`, Group `Finance Room {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing), TAG `QR`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-8: Missing record, Asset Name `Genset Honda EU22 {runId}`, Group `Warehouse {runId}` (di luar Group binaan), Status `Reported Disposal`, Source `Audit`, Last Holder `—`, TAG `QR`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-9: Missing record, Asset Name `Compressor Atlas Copco {runId}`, Group `Finance Room {runId}`, Status `Reported Disposal`, Source `Borrow`, Last Holder `aktor spec ini`, TAG `QR`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-10: Missing record, Asset Name `Printer Brother HL-L2350 {runId}`, Group `Head Office {runId}`, Status `In Disposal Process`, Source `Manual`, Last Holder `—`, TAG `QR`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-11: Asset, Asset Name `Camera Canon EOS {runId}`, Group `Finance Room {runId}`, Status `Available`, TAG `QR`, dengan record sebelumnya berstatus `Found` dan tanpa record Missing berjalan. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-12: Asset, Asset Name `Drill Bosch GSB {runId}`, Group `Finance Room {runId}`, Status `Disposed`, TAG `QR`, dengan record sebelumnya berstatus `Disposed` dan tanpa record Missing berjalan. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-13: Asset, Asset Name `Speaker JBL PartyBox {runId}`, Group `Finance Room {runId}`, Status `Available`, TAG `QR`, dengan record sebelumnya berstatus `Rejected` dan tanpa record Missing berjalan. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-14: Asset, Asset Name `Webcam Logitech C920 {runId}`, Group `Finance Room {runId}`, Status `Available`, TAG `QR`, dengan record sebelumnya berstatus `Canceled` dan tanpa record Missing berjalan. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-030-15: Asset, Asset Name `Welding Machine Lincoln {runId}`, Group `Warehouse {runId}` (di luar Group binaan), Status `Available`, TAG `QR`, tanpa record Missing berjalan.

## Test Steps

### Tombol Scan Found Asset tampil dan cakupan Group aktor
1. Klik tab `Missing`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi tombol `Scan Found Asset` tampil di toolbar tab Active
4. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 22` tampil
5. Verifikasi baris `Hand Pallet Truck {runId} - 3` dengan Group `Warehouse {runId}` tidak tampil

### Guard aset di luar cakupan Group aktor
6. Klik `Scan Found Asset`
7. Pindai TAG milik aset `Hand Pallet Truck {runId} - 3`
8. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `You don't have access to this asset.`
9. Verifikasi pesan dialog `Cannot Mark as Found` tidak memuat nama aset `Hand Pallet Truck {runId} - 3`
10. Klik `[OK]`

### Guard aset tanpa record Missing berjalan
11. Klik `Scan Found Asset`
12. Pindai TAG milik aset `Scanner Zebra DS2208 {runId} - 2`
13. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is not reported missing.` dengan Asset Name `Scanner Zebra DS2208 {runId}`
14. Klik `[OK]`

### Guard record dalam disposal
15. Klik `Scan Found Asset`
16. Pindai TAG milik aset `Projector Epson EB-X06 {runId} - 7`
17. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is in disposal. Mark as Found is not available.` dengan Asset Name `Projector Epson EB-X06 {runId}`
18. Klik `[OK]`
19. Klik nama `Projector Epson EB-X06 {runId} - 7`
20. Verifikasi node `Detected by scan` tampil di dialog Missing Log
21. Klik `✕` pada dialog Missing Log

### Guard aktor adalah Last holder
22. Klik `Scan Found Asset`
23. Pindai TAG milik aset `Monitor LG 27UL500 {runId} - 11`
24. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `You were holding this asset. Ask another admin.`
25. Klik `[OK]`
26. Klik nama `Monitor LG 27UL500 {runId} - 11`
27. Verifikasi node `Detected by scan` tampil di dialog Missing Log
28. Klik `✕` pada dialog Missing Log

### TAG tidak terdaftar dan TAG tidak terbaca
29. Klik `Scan Found Asset`
30. Pindai TAG yang tidak terdaftar pada aset mana pun
31. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `This TAG is not registered to any asset.`
32. Klik `[OK]`
33. Klik `Scan Found Asset`
34. Pindai TAG yang tidak dapat dibaca
35. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `Unable to read the TAG. Try again.`
36. Klik `[OK]`
37. Verifikasi baris `Monitor LG 27UL500 {runId} - 11` dengan Status `Missing` tampil

### Mark as Found lewat aksi baris: submit sebelum verifikasi dan TAG bukan milik aset
38. Klik menu ⋯ pada baris `Printer HP LaserJet M404 {runId} - 5`
39. Klik `Mark as Found`
40. Klik `[Mark as Found]`
41. Verifikasi caption error `Scan TAG must not be empty` tampil di bawah field Scan TAG
42. Klik `[Scan TAG]`
43. Pindai TAG milik aset `Laptop Dell Latitude 5420 {runId} - 22`
44. Verifikasi pesan `This TAG doesn't belong to [Asset Name].` tampil dengan Asset Name `Printer HP LaserJet M404 {runId}`
45. Klik `[Cancel]` pada dialog Mark as Found (form belum diubah)

### Scan Found Asset berhasil membuka Mark as Found terverifikasi
46. Klik `Scan Found Asset`
47. Pindai TAG milik aset `Laptop Dell Latitude 5420 {runId} - 22`
48. Verifikasi dialog `Mark as Found` terbuka dengan Scan TAG berstatus `Verified`
49. Verifikasi kotak Search tetap berisi `{runId}`
50. Klik `[Mark as Found]`
51. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan Asset Name `Laptop Dell Latitude 5420 {runId}`
52. Klik sub-tab `History`
53. Ketik Search `{runId}`, tekan Enter
54. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 22` dengan Status `Found` tampil
55. Klik nama `Laptop Dell Latitude 5420 {runId} - 22`
56. Verifikasi node `Detected by scan` tampil di dialog Missing Log
57. Klik `✕` pada dialog Missing Log

### Scan Found Asset atas record Waiting for Confirmation membuka Mark as Found terverifikasi tanpa mengubah Filter
58. Klik sub-tab `Active`
59. Ketik Search `{runId}`, tekan Enter
60. Klik `Filter`
61. Pilih `Missing` pada field `Status`
62. Klik `Apply`
63. Klik `Filter`
64. Verifikasi tabel memuat baris `Printer HP LaserJet M404 {runId}` dengan Status `Missing` sesudah filter `Status` ter-Apply
65. Verifikasi baris `Tablet Samsung Galaxy Tab {runId}` tidak tampil
66. Klik `Scan Found Asset`
67. Pindai TAG milik aset `Tablet Samsung Galaxy Tab {runId}`
68. Verifikasi dialog `Mark as Found` terbuka dengan Scan TAG berstatus `Verified`
69. Klik `[Cancel]` pada dialog Mark as Found (form belum diubah)
70. Verifikasi ikon Filter berbadge titik karena filter `Status` masih ter-Apply
71. Verifikasi baris `Printer HP LaserJet M404 {runId}` dengan Status `Missing` masih tampil
72. Verifikasi baris `Tablet Samsung Galaxy Tab {runId}` masih tidak tampil
73. Klik `Filter`
74. Klik `Clear Field`
75. Klik `Apply`
76. Klik `Filter`

### Urutan guard: aset di luar cakupan lebih dulu daripada record dalam disposal
77. Klik `Scan Found Asset`
78. Pindai TAG milik aset `Genset Honda EU22 {runId}`
79. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `You don't have access to this asset.`
80. Verifikasi pesan dialog `Cannot Mark as Found` tidak memuat nama aset `Genset Honda EU22 {runId}`
81. Klik `[OK]`

### Urutan guard: record dalam disposal lebih dulu daripada aktor Last holder
82. Klik `Scan Found Asset`
83. Pindai TAG milik aset `Compressor Atlas Copco {runId}`
84. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is in disposal. Mark as Found is not available.` dengan Asset Name `Compressor Atlas Copco {runId}`
85. Klik `[OK]`

### Guard record In Disposal Process
86. Klik `Scan Found Asset`
87. Pindai TAG milik aset `Printer Brother HL-L2350 {runId}`
88. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is in disposal. Mark as Found is not available.` dengan Asset Name `Printer Brother HL-L2350 {runId}`
89. Verifikasi dialog `Mark as Found` tidak terbuka
90. Klik `[OK]`

### Guard aset dengan record selesai Found
91. Klik `Scan Found Asset`
92. Pindai TAG milik aset `Camera Canon EOS {runId}`
93. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is not reported missing.` dengan Asset Name `Camera Canon EOS {runId}`
94. Klik `[OK]`

### Guard aset dengan record selesai Disposed
95. Klik `Scan Found Asset`
96. Pindai TAG milik aset `Drill Bosch GSB {runId}`
97. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is not reported missing.` dengan Asset Name `Drill Bosch GSB {runId}`
98. Klik `[OK]`

### Guard aset dengan record selesai Rejected
99. Klik `Scan Found Asset`
100. Pindai TAG milik aset `Speaker JBL PartyBox {runId}`
101. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is not reported missing.` dengan Asset Name `Speaker JBL PartyBox {runId}`
102. Klik `[OK]`

### Guard aset dengan record selesai Canceled
103. Klik `Scan Found Asset`
104. Pindai TAG milik aset `Webcam Logitech C920 {runId}`
105. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `[Asset Name] is not reported missing.` dengan Asset Name `Webcam Logitech C920 {runId}`
106. Klik `[OK]`

### Urutan guard: aset di luar cakupan lebih dulu daripada tanpa record Missing berjalan
107. Klik `Scan Found Asset`
108. Pindai TAG milik aset `Welding Machine Lincoln {runId}`
109. Verifikasi dialog `Cannot Mark as Found` tampil dengan pesan `You don't have access to this asset.`
110. Verifikasi pesan dialog `Cannot Mark as Found` tidak memuat nama aset `Welding Machine Lincoln {runId}`
111. Klik `[OK]`

### Confirm Disabled pada record Waiting for Confirmation yang sudah terdeteksi scan
112. Klik nama `Tablet Samsung Galaxy Tab {runId}` pada kolom Name
113. Verifikasi node `Detected by scan` tampil di dialog Missing Log
114. Verifikasi `[Confirm]` Disabled pada footer dialog Missing Log dengan alasan `This asset was scanned on [date]. Reject the report or mark it as found.`
115. Verifikasi `[Reject]` tersedia pada footer dialog Missing Log
116. Verifikasi aksi `Mark as Found` tersedia untuk record `Tablet Samsung Galaxy Tab {runId}`
117. Klik `✕` pada dialog Missing Log
