---
id: TC-FA-BORROW-BE-077-handover-aturan-server
title: "Handover: scan wajib, foto, konfirmasi Borrower, Due date, dan handover sebagian"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["BORROW-LOGIC-08a", "BORROW-LOGIC-08b", "BORROW-LOGIC-08c", "BORROW-LOGIC-08d", "BORROW-LOGIC-08e", "BORROW-LOGIC-08f", "BORROW-LOGIC-08g", "BORROW-LOGIC-08h", "BORROW-LOGIC-08i", "BORROW-LOGIC-08j", "BORROW-LOGIC-08k", "BORROW-LOGIC-08l", "BORROW-LOGIC-08m", "BORROW-LOGIC-08n", "BORROW-LOGIC-08o", "BORROW-LOGIC-08p", "BORROW-LOGIC-08q", "BORROW-LOGIC-08r", "BORROW-LOGIC-08s", "BORROW-LOGIC-08t", "BORROW-LOGIC-08u", "BORROW-LOGIC-08v", "BORROW-LOGIC-08w", "BORROW-LOGIC-08x", "BORROW-LOGIC-08y", "BORROW-LOGIC-08z", "EC-BRW-116", "EC-BRW-117", "EC-BRW-134", "EC-BRW-14", "EC-BRW-15", "EC-BRW-156", "EC-BRW-16", "EC-BRW-165", "EC-BRW-17", "EC-BRW-18", "EC-BRW-19", "EC-BRW-20", "EC-BRW-30b", "EC-BRW-38", "EC-BRW-43", "EC-BRW-46", "EC-BRW-52", "EC-BRW-71", "EC-BRW-83", "EC-BRW-84", "EC-BRW-89", "F-BORROW-06.k1", "F-BORROW-06.k10", "F-BORROW-06.k2", "F-BORROW-06.k3", "F-BORROW-06.k4", "F-BORROW-06.k5", "F-BORROW-06.k6", "F-BORROW-06.k7", "F-BORROW-06.k8", "F-BORROW-06.k9", "§9.2#b36", "§9.2#b37", "§9.2#b41", "§9.5#r15"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-08a": [3, 6, 7]
  "BORROW-LOGIC-08b": 87
  "BORROW-LOGIC-08c": 58
  "BORROW-LOGIC-08d": 13
  "BORROW-LOGIC-08e": 68
  "BORROW-LOGIC-08f": 22
  "BORROW-LOGIC-08g": 11
  "BORROW-LOGIC-08h": 13
  "BORROW-LOGIC-08i": [33, 43]
  "BORROW-LOGIC-08j": 34
  "BORROW-LOGIC-08k": 45
  "BORROW-LOGIC-08l": 47
  "BORROW-LOGIC-08m": 49
  "BORROW-LOGIC-08n": 51
  "BORROW-LOGIC-08o": 57
  "BORROW-LOGIC-08p": 53
  "BORROW-LOGIC-08q": 54
  "BORROW-LOGIC-08r": 94
  "BORROW-LOGIC-08s": 103
  "BORROW-LOGIC-08t": 106
  "BORROW-LOGIC-08u": 66
  "BORROW-LOGIC-08v": [26, 28]
  "BORROW-LOGIC-08w": [37, 38]
  "BORROW-LOGIC-08x": 70
  "BORROW-LOGIC-08y": 91
  "BORROW-LOGIC-08z": [104, 105]
  "EC-BRW-116": [22, 23, 24, 26, 28, 29, 31]
  "EC-BRW-117": [34, 35, 37, 40, 151]
  "EC-BRW-134": [93, 94]
  "EC-BRW-14": [127, 128, 129, 130, 131]
  "EC-BRW-15": 68
  "EC-BRW-156": [135, 136, 138]
  "EC-BRW-16": [19, 20]
  "EC-BRW-165": [117, 118, 120, 121]
  "EC-BRW-17": 72
  "EC-BRW-18": 86
  "EC-BRW-19": [64, 65]
  "EC-BRW-20": [147, 148]
  "EC-BRW-30b": [140, 141, 142, 143]
  "EC-BRW-38": [115, 116]
  "EC-BRW-43": [58, 60]
  "EC-BRW-46": 59
  "EC-BRW-52": [107, 108, 109, 111, 112]
  "EC-BRW-71": [74, 75, 76, 81, 82, 83]
  "EC-BRW-83": [91, 92, 93]
  "EC-BRW-84": [97, 98, 99]
  "EC-BRW-89": [123, 125]
  "F-BORROW-06.k1": [6, 9, 115, 133, 135]
  "F-BORROW-06.k10": [147, 149]
  "F-BORROW-06.k2": [58, 60, 106, 107, 110]
  "F-BORROW-06.k3": [4, 13, 15, 17, 68]
  "F-BORROW-06.k4": [34, 35, 37, 38, 43, 151]
  "F-BORROW-06.k5": [56, 93]
  "F-BORROW-06.k6": [86, 97, 98]
  "F-BORROW-06.k7": 94
  "F-BORROW-06.k8": [72, 74, 79]
  "F-BORROW-06.k9": 65
  "§9.2#b36": 55
  "§9.2#b37": [61, 62, 63]
  "§9.2#b41": [153, 155]
  "§9.5#r15": [58, 113]
---

# Handover: scan wajib, foto, konfirmasi Borrower, Due date, dan handover sebagian

## Prerequisites
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office {runId}` (DU-077-1) sebagai pemberi Handover; Borrower `Rina Wijaya {runId}`, karyawan aktif dengan akun login (DU-077-2); Group Manager `Siti Aminah {runId}` untuk `Head Office {runId}` (DU-077-3); Total Control `Dewi Lestari {runId}` (DU-077-4); Asset Admin `Hendra Kusuma {runId}` dengan Group penugasan `Branch Surabaya {runId}` (DU-077-5); karyawan tanpa akun login `Budi Santoso {runId}` dengan PIC `Agus Pratama {runId}` (DU-077-6).
- Data:
  - DU-077-1 sampai DU-077-6: pengguna seperti di Aktor.
  - DU-077-7: Handheld Reader `Reader Gudang {runId}`.
  - DU-077-8: baris `Waiting for Handover` aset ber-tag (TAG QR dan RFID ter-pair) `Laptop Dell Latitude {runId}`, Category `Laptop`, Duration `3 Days`, Photo at start `ON`, Borrower `Rina Wijaya {runId}`.
  - DU-077-9: baris `Waiting for Handover` aset ber-tag `Proyektor Epson {runId}`, Category `Proyektor`, Duration `5 Days`, Photo at start `ON`, Borrower `Rina Wijaya {runId}`; tag aset ini sudah discan saat ditambahkan ke form Borrow Request.
  - DU-077-10: baris `Waiting for Handover` aset `Kursi Lipat Rapat {runId}`, Category `Non TAG`, Duration `2 Days`, Photo at start `OFF`.
  - DU-077-11: baris `Waiting for Handover` aset ber-tag `Kamera Mirrorless {runId}`, Category `Kamera`, Duration `4 Days`, Photo at start `OFF`; tag aset ini tidak terbaca.
  - DU-077-12: baris `Waiting for Handover` aset `Printer Warna Epson {runId}`, Category `Printer`, Duration `2 Days`; status aset `Unmanaged`.
  - DU-077-8 sampai DU-077-12 berada dalam satu BRW milik Borrower `Rina Wijaya {runId}` di Group `Head Office {runId}`.
  - DU-077-13: baris `Waiting for Approval` aset `Monitor Samsung {runId}`, Category `Monitor`, Duration `3 Days`, Borrower `Rina Wijaya {runId}`, dalam BRW terpisah.
  - DU-077-14: baris `Waiting for Handover` aset `Meeting Mic Set {runId}`, Category `Peralatan Rapat`, Duration `12 Hours`; Due date yang diharapkan `10:00` hari berikutnya dari waktu handover `22:00`.
  - DU-077-15: baris `Waiting for Handover` aset `Walkie Talkie Motorola {runId}`, Category `Peralatan Komunikasi`, Duration `6 Hours`; Due date yang diharapkan `04:00` hari berikutnya dari waktu handover `22:00`. DU-077-14 dan DU-077-15 berada dalam satu BRW Borrower `Rina Wijaya {runId}`.
  - DU-077-16: baris `Waiting for Handover` aset ber-tag `Speaker Portable JBL {runId}`, Category `Audio`, Duration `2 Days`, Photo at start `OFF`.
  - DU-077-17: baris `Waiting for Handover` aset ber-tag `Mikrofon Wireless Shure {runId}`, Category `Audio`, Duration `2 Days`, Photo at start `OFF`. DU-077-16 dan DU-077-17 berada dalam satu BRW Borrower `Rina Wijaya {runId}`.
  - DU-077-18: baris `Waiting for Handover` aset ber-tag `Tripod Kamera {runId}`, Category `Aksesori Kamera`, Duration `2 Days`, Photo at start `OFF`, Borrower `Agus Pratama {runId}`.
  - DU-077-19: baris `Waiting for Handover` aset ber-tag `Genset Portable {runId}`, Category `Peralatan Lapangan`, Duration `2 Days`, Photo at start `OFF`, Borrower `Budi Santoso {runId}`.
  - DU-077-20: baris `Waiting for Handover` aset ber-tag `Laptop Lenovo ThinkPad {runId}`, Category `Laptop`, Duration `3 Days`, Borrower `Rina Wijaya {runId}`, dengan Requester `Agus Pratama {runId}`.
  - DU-077-21: aset `Drone DJI Mavic {runId}`, Category `Drone`, record Missing berstatus `Missing` dan baris pinjamannya `Returned` dengan penanda `Missing`.
- Kondisi:
  - Photo at start bernilai `ON` untuk `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}`, dan `OFF` untuk aset lain di spec ini.
  - Photo at end bernilai `ON` untuk `Proyektor Epson {runId}`, dan `OFF` untuk aset lain di spec ini.
  - Send email notifications bernilai `OFF`.
  - Handheld Reader `Reader Gudang {runId}` tersambung hanya pada langkah yang menyebutnya.

## Test Steps

### Penyerahan dapat dimulai kapan saja setelah Waiting for Handover
1. Waktu berlalu 2 hari sejak baris `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}` menjadi `Waiting for Handover`, belum melewati batas pengambilan
2. Asset Admin memindai salah satu tag `Laptop Dell Latitude {runId}`
3. Verifikasi baris `Laptop Dell Latitude {runId}` terverifikasi walau sudah dua hari menunggu, tanpa tanggal Start
4. Verifikasi scan salah satu tag yang ter-pair sudah cukup untuk memverifikasi baris itu

### Hanya baris Waiting for Handover di Group aset yang dapat diserahkan
5. Asset Admin memindai tag `Monitor Samsung {runId}` pada Handover
6. Verifikasi server menolak scan itu dengan pesan `Error, this asset is still waiting for approval from [Names].`
7. Verifikasi baris `Monitor Samsung {runId}` tetap `Waiting for Approval`
8. Asset Admin `Hendra Kusuma {runId}` memindai tag `Proyektor Epson {runId}` pada Handover
9. Verifikasi server menolak scan itu dengan pesan `Error, this asset belongs to [Group].` karena Handover hanya di Group aset

### Scan tag wajib untuk aset ber-tag dan scan form tidak dihitung
10. Asset Admin membuka Handover atas BRW yang memuat `Proyektor Epson {runId}`
11. Verifikasi baris `Proyektor Epson {runId}` berstatus `Unverified` walau tagnya sudah discan saat ditambahkan ke form, karena scan saat menambah aset hanya memilih aset
12. Asset Admin mengirim Request Confirmation untuk `Proyektor Epson {runId}` tanpa memindai tag di Handover
13. Verifikasi server menolak permintaan itu dengan pesan `Verify at least one asset with Verify Asset.` karena aset tetap harus discan di halaman Handover setelah `[Submit]`
14. Asset Admin memindai tag `Tripod Kamera {runId}` pada Handover BRW yang memuat `Proyektor Epson {runId}`
15. Verifikasi server menolak scan itu dengan pesan `Error, this TAG belongs to [Asset Code], not in this borrow.`
16. Asset Admin memverifikasi `Proyektor Epson {runId}` dengan scan tag memakai reader genggam `Reader Gudang {runId}`
17. Verifikasi baris `Proyektor Epson {runId}` terverifikasi

### Tag tidak terbaca tidak dapat diserahkan oleh siapa pun
18. Asset Admin memindai tag `Kamera Mirrorless {runId}` yang tidak terbaca
19. Verifikasi handover `Kamera Mirrorless {runId}` tidak dapat dimulai karena tagnya tidak terbaca
20. Verifikasi Asset Admin dapat melaporkannya lewat `I Can't Scan the TAG` dan memakai aset lain
21. Asset Admin menjalankan `I Can't Scan the TAG` pada baris `Kamera Mirrorless {runId}`
22. Verifikasi aset yang tagnya tidak terbaca hanya dilaporkan lewat `I Can't Scan the TAG` dan laporannya dibuat sebagai Report TAG biasa
23. Verifikasi baris `Kamera Mirrorless {runId}` nonaktif dengan teks `TAG reported. Replace the TAG to hand over.`
24. Verifikasi Borrow Log mencatat node `TAG reported by [Reporter]` dengan daftar TAG
25. Group Manager `Siti Aminah {runId}` memindai tag `Kamera Mirrorless {runId}` pada Handover
26. Verifikasi baris `Kamera Mirrorless {runId}` tidak dapat diverifikasi atau diserahkan oleh Group Manager
27. Total Control `Dewi Lestari {runId}` memindai tag `Kamera Mirrorless {runId}` pada Handover
28. Verifikasi baris `Kamera Mirrorless {runId}` tidak dapat diverifikasi atau diserahkan oleh Total Control tanpa override
29. Verifikasi `Proyektor Epson {runId}` tetap dapat diserahkan karena baris lain tidak terpengaruh
30. Replace TAG atas `Kamera Mirrorless {runId}` selesai
31. Verifikasi baris `Kamera Mirrorless {runId}` langsung kembali `Unverified` dan dapat discan lagi

### Foto handover satu per aset dari kamera langsung
32. Asset Admin memverifikasi `Laptop Dell Latitude {runId}` dengan scan tag dan mengirim Request Confirmation untuk `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}` tanpa foto karena kamera tidak tersedia
33. Verifikasi server menolak permintaan itu dengan pesan `2 assets need a handover photo.`
34. Verifikasi Handover tidak dapat diselesaikan untuk baris itu karena foto tidak dapat diambil
35. Verifikasi toast `Error, camera is not available. Allow camera access or use the mobile app.` dikembalikan
36. Asset Admin mengirim berkas foto dari galeri sebagai foto handover `Laptop Dell Latitude {runId}`
37. Verifikasi foto handover hanya diterima dari kamera langsung, tanpa unggah file atau galeri
38. Verifikasi tidak ada fallback ketika kamera langsung tidak tersedia
39. Asset Admin mengirim Request Confirmation untuk `Kursi Lipat Rapat {runId}` yang Photo at start-nya `OFF`, tanpa foto
40. Verifikasi baris `Kursi Lipat Rapat {runId}` tanpa kendala foto dapat diproses walau foto aset lain tidak dapat diambil
41. Asset Admin membatalkan permintaan konfirmasi `Kursi Lipat Rapat {runId}` dengan `Cancel Request`
42. Asset Admin mengambil 1 foto handover dari kamera langsung untuk setiap aset `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}`
43. Verifikasi foto handover diterima 1 per aset ketika Photo at start `ON`

### Satu sesi konfirmasi untuk semua aset terverifikasi dan sesi tunggal per BRW
44. Asset Admin mengirim Request Confirmation untuk semua aset terverifikasi di sesi itu
45. Verifikasi satu permintaan konfirmasi dikirim untuk semua aset terverifikasi di sesi itu dan sesi `Waiting for Confirmation` (`D-BRW-19`) aktif di perangkat admin
46. Asset Admin mengirim Request Confirmation kedua pada BRW yang sama saat sesi aktif
47. Verifikasi hanya satu sesi konfirmasi aktif per BRW
48. Asset Admin mengirim Cancel Borrow atas baris `Laptop Dell Latitude {runId}` selama jendela konfirmasi berjalan
49. Verifikasi Cancel ditolak dengan pesan `Handover is in progress for this asset.`
50. Aset `Proyektor Epson {runId}` dijadikan Unmanaged selama sesi konfirmasi aktif
51. Verifikasi baris di dalam sesi dikecualikan dari operasi sistem: baris `Proyektor Epson {runId}` tetap `Waiting for Handover` selama jendela 15 menit
52. Borrower menekan Accept pada konfirmasi handover tanpa mengubah centang aset
53. Verifikasi checklist aset sesi itu semua tercentang secara default
54. Verifikasi aset tercentang `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}` menjadi `Borrowed`
55. Verifikasi setiap baris yang selesai menjadi `Borrowed`, Custody `Borrowed`, dan status header dihitung ulang
56. Verifikasi konfirmasi Borrower lewat Accept diterima dan email konfirmasi tetap terkirim walau Send email notifications `OFF`
57. Verifikasi operasi Unmanaged atas `Proyektor Epson {runId}` diterapkan setelah sesi selesai
58. Verifikasi Due date `Laptop Dell Latitude {runId}` adalah tanggal handover + 2 hari pukul `23:59:59`, bukan dihitung dari waktu `Waiting for Handover`
59. Verifikasi Due date `Proyektor Epson {runId}` adalah tanggal handover + 4 hari pukul `23:59:59` dan dihitung sendiri dari waktu handover yang sama
60. Verifikasi Borrower tetap mendapat Duration penuh dan Due date dikirim ke Borrower
61. Verifikasi Event Type event itu adalah `Borrow Handover Verify`
62. Verifikasi hanya satu event dicatat ke log reader untuk sesi handover itu
63. Verifikasi pemakaian reader genggam saat scan Handover dicatat ke log reader
64. Verifikasi baris yang discan dan dikonfirmasi menjadi `Borrowed`
65. Verifikasi baris `Kursi Lipat Rapat {runId}` yang tidak discan tetap `Waiting for Handover`
66. Verifikasi handover sebagian diperbolehkan

### Non TAG, centang minimal satu, jendela habis, Cancel Request, dan Accept ganda
67. Asset Admin mengirim Request Confirmation untuk `Kursi Lipat Rapat {runId}` tanpa scan
68. Verifikasi Category `Non TAG` dikecualikan dari scan dan langkah scan dilewati
69. Borrower mengonfirmasi tanpa mencentang satu aset pun
70. Verifikasi konfirmasi ditolak karena minimal satu aset tercentang dan baris tetap `Waiting for Handover`
71. Waktu berlalu 15 menit sejak permintaan konfirmasi dikirim
72. Verifikasi handover batal dan baris `Kursi Lipat Rapat {runId}` tetap `Waiting for Handover`
73. Borrower menekan Confirm setelah jendela konfirmasi habis
74. Verifikasi server menolak konfirmasi yang masuk setelah jendela habis
75. Verifikasi Borrower melihat dialog `Handover No Longer Available` varian jendela habis
76. Verifikasi baris tidak berubah
77. Asset Admin mengirim Request Confirmation baru untuk `Kursi Lipat Rapat {runId}`
78. Asset Admin menekan `Cancel Request`
79. Verifikasi handover batal dan semua aset sesi itu tetap `Waiting for Handover`
80. Borrower menekan Confirm setelah admin menekan `Cancel Request`
81. Verifikasi server menolak konfirmasi yang masuk setelah `Cancel Request`
82. Verifikasi Borrower melihat dialog `Handover No Longer Available` varian sesuai penyebab
83. Verifikasi baris tetap `Waiting for Handover`
84. Asset Admin mengirim Request Confirmation baru untuk `Kursi Lipat Rapat {runId}`
85. Borrower menekan Accept dua kali
86. Verifikasi aksi Accept ganda menghasilkan satu efek: `Kursi Lipat Rapat {runId}` menjadi `Borrowed` satu kali
87. Verifikasi baris dalam satu BRW diserahkan pada waktu berbeda: Due date `Kursi Lipat Rapat {runId}` dihitung dari waktu handover-nya sendiri

### Confirm on This Device oleh admin atas nama Borrower
88. Asset Admin memverifikasi `Speaker Portable JBL {runId}` dan `Mikrofon Wireless Shure {runId}` dengan scan tag
89. Asset Admin mengirim Request Confirmation untuk kedua aset
90. Asset Admin memilih `Confirm on This Device`, menghapus centang `Mikrofon Wireless Shure {runId}`, dan mencentang pernyataan di `D-BRW-20`
91. Verifikasi konfirmasi lewat dialog Confirm Receipt (`D-BRW-20`) di perangkat admin diterima
92. Verifikasi konfirmasi itu hanya berlaku untuk aset yang dicentang sebagai diterima dan setelah pernyataan dicentang
93. Verifikasi `Speaker Portable JBL {runId}` menjadi `Borrowed` dengan penanda `Confirmed by [Aktor] on behalf of [Borrower]`
94. Verifikasi `Mikrofon Wireless Shure {runId}` yang tidak tercentang tetap `Waiting for Handover` dengan keterangan `Not received`
95. Asset Admin mengirim Request Confirmation untuk `Mikrofon Wireless Shure {runId}`
96. Asset Admin menekan `Confirm on This Device` dan Borrower menekan Accept hampir bersamaan
97. Verifikasi konfirmasi pertama yang masuk yang berlaku untuk `Mikrofon Wireless Shure {runId}`
98. Verifikasi konfirmasi yang masuk kedua diabaikan tanpa error
99. Verifikasi hanya satu handover tercatat untuk `Mikrofon Wireless Shure {runId}`

### Waktu handover baris Hours
100. Asset Admin memverifikasi `Meeting Mic Set {runId}` dan `Walkie Talkie Motorola {runId}` dengan scan tag
101. Asset Admin mengirim Request Confirmation untuk kedua aset
102. Borrower menekan Accept untuk kedua aset pada pukul `22:00`
103. Verifikasi waktu handover baris Hours adalah saat Borrower menyelesaikan konfirmasi
104. Verifikasi kedua aset yang dikonfirmasi dalam satu aksi memakai satu timestamp yang sama sebagai Handed Over At
105. Verifikasi timestamp yang sama itu menjadi dasar Due date kedua aset
106. Verifikasi `Return by [Date]` pada `D-BRW-19` adalah perkiraan sekarang + Duration dan dapat berbeda hingga jendela konfirmasi 15 menit
107. Verifikasi Due date `Meeting Mic Set {runId}` adalah jam handover + 12 hours, yaitu `10:00` hari berikutnya
108. Verifikasi Due date `Walkie Talkie Motorola {runId}` adalah jam handover + 6 hours, yaitu `04:00` hari berikutnya
109. Verifikasi Due date baris Hours menyimpan tanggal dan jam dan boleh melewati hari
110. Verifikasi Due date baris Days dibaca menurut Time Zone General Settings penyewa, dengan tanggal handover dibaca di zona yang sama
111. Verifikasi Due soon dan Overdue baris Hours dihitung dari waktu penuh, dengan Overdue 1 jam setelah Due date
112. Verifikasi Remaining dan Returned At baris Hours memakai jam penuh, bukan tanggal
113. Verifikasi Due date baris Hours dihitung dari jam handover + Duration jam, dengan waktu handover saat Borrower menyelesaikan konfirmasi

### Aktor yang juga Borrower atau PIC memproses sendiri
114. Asset Admin `Agus Pratama {runId}` membuka Handover atas BRW yang Borrower-nya adalah dirinya sendiri, dengan baris `Tripod Kamera {runId}`
115. Verifikasi Asset Admin yang menjadi Borrower BRW itu diizinkan memproses Handover pinjamannya sendiri
116. Verifikasi izin itu berlaku karena Group asal `Tripod Kamera {runId}` berada dalam cakupan Group penugasan `Head Office {runId}` Asset Admin itu
117. Verifikasi scan TAG wajib untuk `Tripod Kamera {runId}` yang diproses sendiri oleh Borrower-nya
118. Verifikasi `I Can't Scan the TAG` tidak tersedia untuk `Tripod Kamera {runId}`
119. Asset Admin memindai tag `Tripod Kamera {runId}` dan menyelesaikan Handover dengan `[Hand Over]`
120. Verifikasi handover selesai dengan `Confirmed (self)` tanpa sesi konfirmasi
121. Verifikasi Borrow Log menandai handover dengan `Self-processed`
122. Asset Admin `Agus Pratama {runId}` yang menjadi PIC `Budi Santoso {runId}` membuka Handover atas baris `Genset Portable {runId}`
123. Verifikasi PIC Borrower tanpa akun diizinkan memproses dengan syarat scan TAG wajib dan tanpa `I Can't Scan the TAG`
124. Asset Admin memindai tag `Genset Portable {runId}` dan menyelesaikan Handover dengan `[Hand Over]`
125. Verifikasi handover selesai dengan `Confirmed (self)` dan Borrow Log `Self-processed`

### Baris yang tidak diambil sampai Transaction timeout
126. Job Transaction timeout berjalan setelah baris `Laptop Lenovo ThinkPad {runId}` melewati batas Transaction timeout sejak `Waiting for Handover`
127. Verifikasi baris menjadi `Canceled` dengan alasan `Not picked up` dan masuk riwayat
128. Verifikasi asetnya kembali ke Draft baru `Restored from [BRW No.]` dan Custody kembali `Available`
129. Verifikasi pengingat H-1 dikirim sebagai `borrow_almost_timeout` varian PIC admin ke Requester `Agus Pratama {runId}`
130. Verifikasi Borrower `Rina Wijaya {runId}` tidak menerima pengingat `borrow_almost_timeout`
131. Verifikasi notifikasi saat baris ditutup mengikuti `borrow_auto_canceled`
132. Asset Admin memindai tag `Laptop Lenovo ThinkPad {runId}` pada Handover
133. Verifikasi Handover ditolak karena baris sudah lewat batas pengambilan dan tidak lagi `Waiting for Handover`

### Aset Unmanaged dan aset yang record Missing-nya berstatus Missing
134. Asset Admin memindai tag `Printer Warna Epson {runId}` pada Handover
135. Verifikasi Handover ditolak dengan alasan status aset
136. Verifikasi baris tetap `Waiting for Handover` sampai Transaction timeout
137. Asset Admin mengirim Cancel Borrow atas baris `Printer Warna Epson {runId}`
138. Verifikasi Cancel tetap diperbolehkan dan baris menjadi `Canceled`
139. Asset Admin memindai tag `Drone DJI Mavic {runId}` pada Handover
140. Verifikasi scan ditolak dengan pesan `[Asset Name] is reported missing.`
141. Verifikasi tidak ada aksi lain yang dijalankan atas aset itu
142. Verifikasi scan dicatat sebagai deteksi
143. Verifikasi status aset dan baris `Returned` dengan penanda `Missing` tidak berubah

### Handover offline dan penyelesaian konflik sinkronisasi
144. Asset Admin menyimpan scan dan foto Handover saat offline untuk baris `Genset Portable {runId}`
145. Aktor lain mengubah baris `Genset Portable {runId}`
146. Asset Admin terhubung kembali dan sinkron
147. Verifikasi scan dan foto offline diterima dengan status `Pending sync`
148. Verifikasi konflik saat sinkron dimenangkan server dan Aktor diberi tahu
149. Verifikasi konfirmasi dan perubahan status baris menunggu online

### Pemakaian Handheld Reader saat Return
150. Asset Admin mengirim Return `Proyektor Epson {runId}` tanpa foto karena kamera tidak tersedia
151. Verifikasi Return tidak dapat diselesaikan karena foto Return tidak dapat diambil, dengan aturan yang sama seperti foto Handover
152. Asset Admin mengembalikan `Proyektor Epson {runId}` dengan 1 foto Return dan scan tag memakai reader genggam `Reader Gudang {runId}`
153. Verifikasi satu event Event Type `Borrow Return Verify` dengan Transaction ID nomor BRW dicatat ke log reader untuk sesi Return itu
154. Asset Admin mengembalikan `Laptop Dell Latitude {runId}` tanpa reader genggam tersambung
155. Verifikasi tidak ada entri log reader untuk Return `Laptop Dell Latitude {runId}`
