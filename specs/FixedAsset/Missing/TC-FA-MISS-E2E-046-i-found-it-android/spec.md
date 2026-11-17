---
id: TC-FA-MISS-E2E-046-i-found-it-android
title: "Search by Scan di mobile: sheet reported missing, I found it mengirim deteksi, foto, dan lokasi tanpa mengubah status; Mark as Found bagi yang berhak"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.6#p1", "§4.6#b1", "§4.6#b2", "§4.6#b4", "§4.6#b5", "§2.1#r4", "§2.1#b3", "§4.8#r4", "§7.3#r12", "§9.6#r8", "§9.7#r10", "§9.8#r5", "§9.5#r7", "§8#r10", "§8.1#r12", "§9.2#b41", "§9.2#b47", "§10#r7", "§9.3#b1", "§4.2.4#p2", "§9.9#p4", "EB-FB-1@i-found-it", "EB-ERR-1@i-found-it"]
smoke: []
dependsOn: []
trace:
  "§4.6#p1": [3, 5, 21, 41]
  "§4.6#b1": [5, 9, 64, 85, 90, 95, 100]
  "§4.6#b2": [6, 7, 8, 10, 12, 13, 81]
  "§4.6#b4": [44, 45, 46, 59, 60, 61, 67, 72, 73, 74, 76, 77, 113, 114, 115, 119]
  "§4.6#b5": [21, 22, 119]
  "§2.1#r4": [9, 29, 33, 37, 46, 65, 77]
  "§2.1#b3": [6, 7, 8, 10, 12, 13, 81]
  "§4.8#r4": [9, 29, 33, 37, 46, 65, 77]
  "§7.3#r12": [16, 51]
  "§9.6#r8": [15, 16, 52, 53]
  "§9.7#r10": [21, 24, 25]
  "§9.8#r5": [16, 19]
  "§9.5#r7": 19
  "§8#r10": [16, 121]
  "§8.1#r12": [12, 16, 81]
  "§9.2#b41": [76, 77]
  "§9.2#b47": 64
  "§10#r7": 2
  "§9.3#b1": [72, 73, 74, 75]
  "§4.2.4#p2": [67, 68]
  "§9.9#p4": [12, 13]
  "EB-FB-1@i-found-it": [16, 51, 56]
  "EB-ERR-1@i-found-it": [51, 52, 53, 54, 56, 105, 106, 107, 108, 110]
anchor: [2, 84, 89, 94, 99, 118]
coverage:
  android: manual
---

# Search by Scan di mobile: sheet reported missing, I found it mengirim deteksi, foto, dan lokasi tanpa mengubah status; Mark as Found bagi yang berhak

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}`, Group Manager `Andi Pratama {runId}`, Manage asset & TAG (Update) `Dewi Anggraini {runId}`, Accounting `Maya Rahmawati {runId}`, Read Only `Sari Dewanti {runId}`, View asset value `Bima Santoso {runId}`, dan pemegang `Joko Susilo {runId}`.
- Layar awal: layar mana pun yang menampilkan navbar dengan `Search by Scan`.
- Data:
  - DU-046-1: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22` (Asset Name `Laptop Dell Latitude 5420 {runId}`), Asset ID `LPT 0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Borrow`, Last Holder `Andi Pratama {runId}`, TAG `TAG QR 0022 {runId}`.
  - DU-046-2: Missing record, Name `Projector Epson EB-X06 {runId} - 7` (Asset Name `Projector Epson EB-X06 {runId}`), Asset ID `PRJ 0007 {runId}`, Group `Finance Room {runId}`, Status `Reported Disposal`, Source `Stock opname`, Last Holder `—`, TAG `TAG QR 0007 {runId}`.
  - DU-046-3: pengguna `Rina Wulandari {runId}`, Role Total Control, cakupan seluruh client.
  - DU-046-4: pengguna `Andi Pratama {runId}`, Role Group Manager, cakupan Group `Finance Room {runId}`; pemegang aset `Laptop Dell Latitude 5420 {runId} - 22` saat dilaporkan hilang (Last holder).
  - DU-046-5: pengguna `Dewi Anggraini {runId}`, Role Manage asset & TAG (Update), cakupan Group `Warehouse {runId}`, tanpa akses ke Group `Finance Room {runId}`.
  - DU-046-6: pengguna `Maya Rahmawati {runId}`, Role Accounting, cakupan seluruh client.
  - DU-046-7: pengguna `Sari Dewanti {runId}`, Role Read Only, cakupan seluruh client.
  - DU-046-8: pengguna `Bima Santoso {runId}`, Role View asset value, cakupan Group `Finance Room {runId}`.
  - DU-046-9: pengguna `Joko Susilo {runId}`, tanpa Group Role, pemegang aset `Hand Pallet Truck {runId} - 3`.
  - DU-046-10: berkas Photo `foto-laptop-ditemukan {runId}.jpg`, format JPG, ukuran 2 MB.
  - DU-046-11: Missing record, Name `Printer HP LaserJet Pro {runId} - 12` (Asset Name `Printer HP LaserJet Pro {runId}`), Asset ID `PRN 0012 {runId}`, Group `Finance Room {runId}`, Status `In Disposal Process`, Source `Stock opname`, Last Holder `—`, TAG `TAG QR 0012 {runId}`.
- Kondisi:
  - Semua aktor berada di client yang sama dengan DU-046-1, DU-046-2, dan DU-046-11, dan TAG `TAG QR 0022 {runId}` `TAG QR 0007 {runId}`, serta `TAG QR 0012 {runId}` terbaca saat dipindai.
  - Izin lokasi perangkat diberikan saat `Sari Dewanti {runId}` mengirim `[I found it]` dan ditolak saat `Dewi Anggraini {runId}` mengirimnya.
  - Submit kedua `Sari Dewanti {runId}` terjadi kurang dari 1 jam sesudah Submit pertamanya.
  - Pengiriman `[I found it]` pertama oleh `Sari Dewanti {runId}` dijawab lambat sehingga keadaan sedang mengirim teramati.
  - Pengiriman `[I found it]` pertama oleh `Andi Pratama {runId}` gagal karena error server; pengiriman berikutnya berhasil.
  - Pengiriman `[I found it]` pertama oleh `Joko Susilo {runId}` tidak dijawab sampai melewati batas waktu; pengiriman berikutnya berhasil.

## Test Steps

### Aplikasi native tanpa halaman Missing
1. Masuk sebagai `Sari Dewanti {runId}`
2. Verifikasi navbar aplikasi native menampilkan `Search by Scan`
3. Verifikasi halaman `Missing` dengan sub-tab `Active` dan `History` tidak tersedia

### Sheet aset Missing mengirim I found it dengan Photo dan lokasi
4. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
5. Verifikasi sheet `This asset is reported missing.` tampil
6. Verifikasi badge status record `Missing` tampil pada sheet
7. Verifikasi Asset Name `Laptop Dell Latitude 5420 {runId}` tampil pada sheet
8. Verifikasi Group `Finance Room {runId}` tampil pada sheet
9. Verifikasi `[I found it]` tampil
10. Verifikasi sheet tidak menampilkan `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
11. Pilih Photo `foto-laptop-ditemukan {runId}.jpg` (ukuran 2 MB)
12. Verifikasi Photo `foto-laptop-ditemukan {runId}.jpg` terpilih pada sheet
13. Verifikasi tidak ada pesan error ukuran atau format pada Photo
14. Klik `[I found it]`
15. Verifikasi `[I found it]` tidak bisa diklik selama permintaan berjalan
16. Verifikasi toast `Success, asset has been reported found.` tampil

### Submit kedua pengguna yang sama dalam jendela 1 jam
17. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
18. Klik `[I found it]`
19. Verifikasi toast `Success, asset has been reported found.` tampil

### Status aset tetap Missing sesudah I found it
20. Buka Asset Detail aset `Laptop Dell Latitude 5420 {runId} - 22`
21. Verifikasi banner `Reported missing on [Date].` tampil
22. Verifikasi banner tidak memiliki `[View]`
23. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
24. Verifikasi sheet `This asset is reported missing.` tampil
25. Verifikasi badge status record `Missing` tampil pada sheet
26. Tutup sheet hasil scan

### I found it tersedia bagi Accounting, View asset value, dan pemegang
27. Masuk sebagai `Maya Rahmawati {runId}`
28. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
29. Verifikasi `[I found it]` tampil
30. Tutup sheet hasil scan
31. Masuk sebagai `Bima Santoso {runId}`
32. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
33. Verifikasi `[I found it]` tampil
34. Tutup sheet hasil scan
35. Masuk sebagai `Joko Susilo {runId}`
36. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
37. Verifikasi `[I found it]` tampil
38. Tutup sheet hasil scan

### Pemegang melihat Report Missing di kartu aset yang dipegang
39. Masuk sebagai `Joko Susilo {runId}`
40. Buka kartu `My Asset` aset `Hand Pallet Truck {runId} - 3`
41. Verifikasi `Report Missing` tampil pada kartu

### Last holder mendapat alasan tanpa Mark as Found
42. Masuk sebagai `Andi Pratama {runId}`
43. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
44. Verifikasi `You were holding this asset. Ask another admin.` tampil
45. Verifikasi `[Mark as Found]` tidak dirender
46. Verifikasi `[I found it]` tampil
47. Tutup sheet hasil scan

### Kegagalan server mempertahankan sheet dan input
48. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
49. Pilih Photo `foto-laptop-ditemukan {runId}.jpg` (ukuran 2 MB)
50. Klik `[I found it]`
51. Verifikasi toast `Error, failed to report asset as found.` tampil
52. Verifikasi sheet hasil scan tetap terbuka
53. Verifikasi Photo `foto-laptop-ditemukan {runId}.jpg` masih terpilih pada sheet
54. Verifikasi `[I found it]` aktif kembali
55. Klik `[I found it]`
56. Verifikasi toast `Success, asset has been reported found.` tampil

### Aset dalam proses disposal tanpa Mark as Found
57. Masuk sebagai `Rina Wulandari {runId}`
58. Pindai TAG `TAG QR 0007 {runId}` lewat `Search by Scan` pada navbar
59. Verifikasi `[Asset Name] is in disposal. Mark as Found is not available.` tampil dengan `[Asset Name]` berisi `Projector Epson EB-X06 {runId}`
60. Verifikasi `[Mark as Found]` tidak dirender
61. Verifikasi `[I found it]` tampil
62. Tutup sheet hasil scan

### Mark as Found bagi Aktor Missing yang berhak
63. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
64. Verifikasi `[Mark as Found]` tampil
65. Verifikasi `[I found it]` tampil
66. Klik `[Mark as Found]`
67. Verifikasi sheet `Mark as Found` terbuka dengan field `Scan TAG`, `Found at`, `Asset Status`, `Photo`, dan `Note`
68. Verifikasi footer sheet memuat `[Cancel]` dan `[Mark as Found]`
69. Klik `[Cancel]` pada sheet `Mark as Found` (form belum diubah)

### Pengguna di luar cakupan Group tetap mendapat I found it
70. Masuk sebagai `Dewi Anggraini {runId}`
71. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
72. Verifikasi badge status record `Missing` tampil pada sheet
73. Verifikasi Asset Name `Laptop Dell Latitude 5420 {runId}` tampil pada sheet
74. Verifikasi Group `Finance Room {runId}` tampil pada sheet
75. Verifikasi sheet tidak menampilkan `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
76. Verifikasi `[Mark as Found]` tidak dirender
77. Verifikasi `[I found it]` tampil
78. Tutup sheet hasil scan

### Izin lokasi ditolak tidak menghalangi Submit
79. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
80. Klik `[I found it]`
81. Verifikasi toast `Success, asset has been reported found.` tampil

### Mark as Found tidak dirender bagi pengguna tanpa hak Aktor Missing
82. Masuk sebagai `Sari Dewanti {runId}`
83. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
84. Verifikasi `[I found it]` tampil
85. Verifikasi `[Mark as Found]` tidak dirender
86. Tutup sheet hasil scan
87. Masuk sebagai `Maya Rahmawati {runId}`
88. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
89. Verifikasi `[I found it]` tampil
90. Verifikasi `[Mark as Found]` tidak dirender
91. Tutup sheet hasil scan
92. Masuk sebagai `Bima Santoso {runId}`
93. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
94. Verifikasi `[I found it]` tampil
95. Verifikasi `[Mark as Found]` tidak dirender
96. Tutup sheet hasil scan
97. Masuk sebagai `Joko Susilo {runId}`
98. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
99. Verifikasi `[I found it]` tampil
100. Verifikasi `[Mark as Found]` tidak dirender
101. Tutup sheet hasil scan

### Timeout mempertahankan sheet dan input
102. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
103. Pilih Photo `foto-laptop-ditemukan {runId}.jpg` (ukuran 2 MB)
104. Klik `[I found it]`
105. Verifikasi toast `Connection problem. Please try again.` tampil
106. Verifikasi sheet hasil scan tetap terbuka
107. Verifikasi Photo `foto-laptop-ditemukan {runId}.jpg` masih terpilih pada sheet
108. Verifikasi `[I found it]` aktif kembali
109. Klik `[I found it]`
110. Verifikasi toast `Success, asset has been reported found.` tampil

### Aset In Disposal Process tanpa Mark as Found
111. Masuk sebagai `Rina Wulandari {runId}`
112. Pindai TAG `TAG QR 0012 {runId}` lewat `Search by Scan` pada navbar
113. Verifikasi `[Asset Name] is in disposal. Mark as Found is not available.` tampil dengan `[Asset Name]` berisi `Printer HP LaserJet Pro {runId}`
114. Verifikasi `[Mark as Found]` tidak dirender
115. Verifikasi `[I found it]` tampil
116. Tutup sheet hasil scan

### Aktor Missing mengirim I found it tanpa View Missing Log di mobile
117. Pindai TAG `TAG QR 0022 {runId}` lewat `Search by Scan` pada navbar
118. Verifikasi `[Mark as Found]` tampil
119. Verifikasi `[View Missing Log]` tidak dirender pada sheet hasil scan
120. Klik `[I found it]`
121. Verifikasi toast `Success, asset has been reported found.` tampil
