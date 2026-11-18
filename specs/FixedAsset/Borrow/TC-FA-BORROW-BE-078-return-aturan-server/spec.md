---
id: TC-FA-BORROW-BE-078-return-aturan-server
title: "Return: tempat Group asal, partial return, penanda status akhir, dan aksi pada baris yang sudah Returned"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["BORROW-LOGIC-09a", "BORROW-LOGIC-09b", "BORROW-LOGIC-09c", "BORROW-LOGIC-09d", "BORROW-LOGIC-09e", "BORROW-LOGIC-09f", "BORROW-LOGIC-09g", "BORROW-LOGIC-09h", "BORROW-LOGIC-09i", "BORROW-LOGIC-09j", "BORROW-LOGIC-09k", "BORROW-LOGIC-09l", "BORROW-LOGIC-09m", "BORROW-LOGIC-09n", "BORROW-LOGIC-09o", "BORROW-LOGIC-09p", "BORROW-LOGIC-09q", "BORROW-LOGIC-09r", "EC-BRW-104", "EC-BRW-154", "EC-BRW-157", "EC-BRW-161", "EC-BRW-162", "EC-BRW-25", "EC-BRW-26", "EC-BRW-27", "EC-BRW-28", "EC-BRW-29", "EC-BRW-30a", "EC-BRW-91", "F-BORROW-08.k1", "F-BORROW-08.k2", "F-BORROW-08.k3", "F-BORROW-08.k4", "F-BORROW-08.k5", "F-BORROW-08.k6", "F-BORROW-08.k7", "V-BRW-38", "§9.2#b42", "§9.2#b43", "§9.2#b45", "§9.2#r51", "§9.2#r53", "§9.4.3#b8"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-09a": [2, 87]
  "BORROW-LOGIC-09b": 90
  "BORROW-LOGIC-09c": [88, 91]
  "BORROW-LOGIC-09d": 12
  "BORROW-LOGIC-09e": [14, 20]
  "BORROW-LOGIC-09f": [29, 31]
  "BORROW-LOGIC-09g": 32
  "BORROW-LOGIC-09h": 37
  "BORROW-LOGIC-09i": 54
  "BORROW-LOGIC-09j": 58
  "BORROW-LOGIC-09k": 61
  "BORROW-LOGIC-09l": 56
  "BORROW-LOGIC-09m": 63
  "BORROW-LOGIC-09n": 65
  "BORROW-LOGIC-09o": 47
  "BORROW-LOGIC-09p": 40
  "BORROW-LOGIC-09q": 34
  "BORROW-LOGIC-09r": 95
  "EC-BRW-104": [97, 98]
  "EC-BRW-154": [73, 75, 77]
  "EC-BRW-157": [67, 69, 71]
  "EC-BRW-161": [79, 82]
  "EC-BRW-162": [8, 10]
  "EC-BRW-25": [2, 3, 4]
  "EC-BRW-26": [15, 16, 18]
  "EC-BRW-27": 22
  "EC-BRW-28": [41, 43, 44]
  "EC-BRW-29": [34, 35, 36]
  "EC-BRW-30a": [73, 74, 75, 76]
  "EC-BRW-91": [90, 91, 92, 93, 94]
  "F-BORROW-08.k1": [2, 3, 8]
  "F-BORROW-08.k2": [14, 16, 24, 29, 32]
  "F-BORROW-08.k3": [67, 69, 71, 73]
  "F-BORROW-08.k4": [51, 52]
  "F-BORROW-08.k5": [34, 35, 36, 41, 42]
  "F-BORROW-08.k6": [87, 90]
  "F-BORROW-08.k7": [79, 82]
  "V-BRW-38": 51
  "§9.2#b42": [38, 51, 55]
  "§9.2#b43": [45, 48, 49]
  "§9.2#b45": 39
  "§9.2#r51": [84, 85]
  "§9.2#r53": [26, 27]
  "§9.4.3#b8": 5
---

# Return: tempat Group asal, partial return, penanda status akhir, dan aksi pada baris yang sudah Returned

## Prerequisites
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office {runId}` sebagai penerima Return (DU-078-1); Borrower `Rina Wijaya {runId}` (DU-078-2); Asset Admin `Hendra Kusuma {runId}` dengan Group penugasan `Branch Surabaya {runId}` (DU-078-3); Requester BRW `Tika Rahma {runId}`, Asset Admin dengan Group penugasan `Head Office {runId}` (DU-078-4); Borrower self-service `Sari Dewi {runId}` (DU-078-5); Asset Admin `Joko Susilo {runId}` dengan Group penugasan `Region Timur {runId}` (DU-078-6); Asset Admin `Wawan Hartono {runId}` dengan Group penugasan `Region Barat {runId}` (DU-078-7); Asset Admin `Maya Putri {runId}` dengan hak Aktor Missing dan Aktor Damaged (DU-078-8).
- Data:
  - DU-078-1 sampai DU-078-8: pengguna seperti di Aktor.
  - DU-078-9: baris `Borrowed` aset `Laptop Dell Latitude {runId}`, Category `Laptop`, Duration `3 Days`, Photo at end `ON`, foto handover tersimpan, Borrower `Rina Wijaya {runId}`, di BRW A dengan Requester `Tika Rahma {runId}`.
  - DU-078-10: baris `Borrowed` aset `Proyektor Epson {runId}`, Category `Proyektor`, Duration `5 Days`, Photo at end `OFF`, di BRW A.
  - DU-078-11: baris `Overdue` aset `Monitor Samsung {runId}`, Category `Monitor`, Duration `1 Days`, Photo at end `OFF`, di BRW A.
  - DU-078-12: baris `Borrowed` aset ber-tag `Kamera Canon EOS {runId}` yang tagnya tidak terbaca dan belum punya laporan terbuka, di BRW B bersama DU-078-13.
  - DU-078-13: baris `Borrowed` aset ber-tag `Lensa Sigma {runId}` yang tagnya tidak terbaca dan sudah punya laporan terbuka, di BRW B.
  - DU-078-14: baris `Borrowed` aset ber-tag `Speaker Portable JBL {runId}` yang tagnya diganti saat dipinjam, di BRW C bersama DU-078-15 dan DU-078-16.
  - DU-078-15: baris `Borrowed` aset `Mikrofon Wireless Shure {runId}` dengan laporan rusak aktif berstatus `Waiting for Confirmation`.
  - DU-078-16: baris `Borrowed` aset `Tripod Kamera {runId}` tanpa laporan rusak saat Return.
  - DU-078-17: baris `Borrowed` aset `Genset Portable {runId}`, di BRW D bersama DU-078-18.
  - DU-078-18: baris `Borrowed` aset `Drone Mini {runId}` dengan laporan hilang Borrower berstatus `Waiting for Confirmation`.
  - DU-078-19: baris `Borrowed` aset `Printer Warna Epson {runId}` berstatus `Unmanaged`, di BRW E bersama DU-078-20 dan DU-078-21.
  - DU-078-20: baris `Borrowed` aset `Server Rack Mini {runId}` dengan Activity Lock `In Audit`.
  - DU-078-21: baris `Borrowed` aset `Mesin Bor Listrik {runId}` dengan Activity Lock `Under Maintenance`.
  - DU-078-22: baris `Borrowed` aset ber-tag `Walkie Talkie Motorola {runId}`, di BRW F.
  - DU-078-23: baris `Borrowed` aset `Kursi Lipat Rapat {runId}` di Group `Gudang Timur {runId}` yang parent-nya awalnya `Region Barat {runId}` dan dipindah ke parent `Region Timur {runId}`.
  - DU-078-24: baris `Borrowed` self-service aset ber-tag `Camera Sony Alpha {runId}`, Borrower `Sari Dewi {runId}`, Photo at end `ON`.
  - DU-078-25: baris `Borrowed` self-service aset ber-tag `Gimbal DJI {runId}`, Borrower `Sari Dewi {runId}`, Photo at end `OFF`.
  - DU-078-26: aset `Aset Pinjam Batas {n} {runId}` berstatus `Borrowed` dalam satu BRW; jumlah aset di daftar Return sama dengan Bulk Transaction Row Limit ditambah satu.
  - DU-078-27: aset `Drone DJI Mavic {runId}`, Category `Drone`, record Missing berstatus `Missing`.
- Kondisi:
  - Bulk Transaction Row Limit berlaku sebagai nilai lingkungan.
  - Photo at end bernilai `ON` untuk `Laptop Dell Latitude {runId}` dan `Camera Sony Alpha {runId}`, dan `OFF` untuk aset lain di spec ini.
  - Group `Gudang Timur {runId}` dipindah dari parent `Region Barat {runId}` ke parent `Region Timur {runId}` hanya pada langkah yang menyebutnya.

## Test Steps

### Return hanya di Group asal oleh Aktor Borrow yang berwenang
1. Asset Admin `Hendra Kusuma {runId}` memindai tag `Proyektor Epson {runId}` pada Return
2. Verifikasi server menolak Return itu dengan pesan `Error, return this asset to [Group].`
3. Verifikasi Borrow tidak mengirim notifikasi kepada Aktor Borrow Group asal atas percobaan Return dari Group lain
4. Verifikasi baris `Proyektor Epson {runId}` tetap `Borrowed`
5. Verifikasi Return oleh Aktor Borrow di luar Group asal aset tidak diizinkan
6. Group `Gudang Timur {runId}` dipindah dari parent `Region Barat {runId}` ke parent `Region Timur {runId}` saat baris `Kursi Lipat Rapat {runId}` berjalan
7. Asset Admin `Wawan Hartono {runId}` memindai tag `Kursi Lipat Rapat {runId}` pada Return
8. Verifikasi Return ditolak karena cakupan dihitung ulang mengikuti hierarki baru
9. Asset Admin `Joko Susilo {runId}` memindai tag `Kursi Lipat Rapat {runId}` pada Return dan menyelesaikannya
10. Verifikasi baris berjalan ikut cakupan baru sehingga Aktor Borrow berwenang di posisi Group yang baru dapat menyelesaikan Return

### Scan tag wajib, identifikasi manual, tag diganti, aset hilang, dan aset tertukar
11. Asset Admin `Agus Pratama {runId}` mengirim Return `Laptop Dell Latitude {runId}` tanpa memindai tag
12. Verifikasi server menolak Return karena scan tag wajib
13. Asset Admin memilih `I Can't Scan the TAG` pada langkah scan Return atas `Kamera Canon EOS {runId}`
14. Verifikasi identifikasi manual diperbolehkan pada langkah scan Return
15. Verifikasi Report TAG dibuat karena tag `Kamera Canon EOS {runId}` belum punya laporan terbuka
16. Verifikasi Borrow Log BRW B mencatat node `TAG reported by [Reporter]` dengan daftar TAG milik `Kamera Canon EOS {runId}`
17. Asset Admin memilih `I Can't Scan the TAG` pada langkah scan Return atas `Lensa Sigma {runId}`
18. Verifikasi hanya catatan yang ditambahkan karena tag `Lensa Sigma {runId}` sudah punya laporan terbuka
19. Asset Admin memilih `I Can't Scan the TAG` pada langkah foto Return atas `Laptop Dell Latitude {runId}`
20. Verifikasi identifikasi manual tidak diterima di luar langkah scan Return
21. Asset Admin memindai tag baru `Speaker Portable JBL {runId}` yang menggantikan tag lama saat dipinjam
22. Verifikasi tag baru dipakai dan Return dapat dilanjutkan
23. Asset Admin memindai tag `Drone DJI Mavic {runId}` pada Return
24. Verifikasi Return ditolak dengan pesan `[Asset Name] is reported missing.`
25. Borrower `Sari Dewi {runId}` memindai tag `Proyektor Epson {runId}` pada Return `Gimbal DJI {runId}`
26. Verifikasi scan memperlihatkan aset sebenarnya dan aset yang dipinjam Borrower lain ditolak dengan pesan `Error, this asset isn't borrowed by [Borrower].`
27. Verifikasi baris `Gimbal DJI {runId}` tetap `Borrowed` setelah scan aset tertukar

### Foto Return satu per aset ditampilkan berdampingan dengan foto handover
28. Asset Admin mengirim Return `Laptop Dell Latitude {runId}` tanpa foto Return
29. Verifikasi server menolak Return karena foto 1 per aset wajib bila Photo at end `ON`
30. Asset Admin mengambil 1 foto Return `Laptop Dell Latitude {runId}` dari kamera langsung
31. Verifikasi foto Return diterima 1 per aset
32. Verifikasi foto handover dan foto Return aset yang sama tersedia berdampingan

### Kembali lebih awal dan Return sebagian
33. Asset Admin memindai tag `Laptop Dell Latitude {runId}` dan menyelesaikan Return sebelum Due date
34. Verifikasi kembali lebih awal diperbolehkan kapan saja
35. Verifikasi Returned At dicatat sama dengan waktu Return
36. Verifikasi Due date rencana tidak berubah dan tetap tersimpan untuk laporan
37. Verifikasi status baris yang selesai selalu `Returned`
38. Verifikasi Custody aset `Laptop Dell Latitude {runId}` menjadi `Available` dan Condition tidak berubah
39. Verifikasi Group asal aset tidak berubah karena pemindahan permanen memakai Transfer manual setelah `Returned`
40. Verifikasi Return sebagian diperbolehkan
41. Verifikasi baris yang belum kembali `Proyektor Epson {runId}` tetap `Borrowed`
42. Verifikasi baris yang belum kembali `Monitor Samsung {runId}` tetap `Overdue`
43. Verifikasi status header mengikuti baris aktif yang masih `Borrowed` atau `Overdue`
44. Verifikasi baris `Laptop Dell Latitude {runId}` yang kembali tercatat di riwayat By Asset
45. Verifikasi Borrower dan Requester `Tika Rahma {runId}` menerima `borrow_returned` untuk Return sebagian itu karena Requester berbeda dari pelaku Return dan Borrower
46. Asset Admin menyelesaikan Return `Proyektor Epson {runId}` dan `Monitor Samsung {runId}`
47. Verifikasi status header tetap `Returned` bila semua baris selesai
48. Verifikasi setiap Return selesai, termasuk Return penutup, mengirim `borrow_returned` ke Borrower dan ke Requester `Tika Rahma {runId}`
49. Verifikasi BRW menjadi `Returned` tanpa notifikasi tambahan saat semua baris aktif kembali

### Aksi pada baris yang sudah Returned ditolak
50. Asset Admin mengirim aksi Return atas baris `Laptop Dell Latitude {runId}` yang sudah `Returned`
51. Verifikasi server menolak aksi itu dengan Dialog Blok `This asset has already been returned.`
52. Verifikasi baris `Laptop Dell Latitude {runId}` tidak berubah oleh aksi yang ditolak

### Penanda Damaged dan Missing sebagai status akhir baris
53. Asset Admin menyelesaikan Return `Mikrofon Wireless Shure {runId}` yang punya laporan rusak aktif berstatus `Waiting for Confirmation`
54. Verifikasi baris menjadi `Returned` dengan penanda `Damaged` tanpa pilihan manual
55. Verifikasi aset `Mikrofon Wireless Shure {runId}` menjadi `Available` dengan Condition `Damaged`
56. Verifikasi penanda adalah bagian status transaksi dan terpisah dari status global aset
57. Asset Admin `Maya Putri {runId}` menolak laporan rusak atas `Mikrofon Wireless Shure {runId}`
58. Verifikasi penanda `Damaged` hilang karena laporan di-Reject, setelah mengikuti laporan itu sampai final
59. Asset Admin menyelesaikan Return `Tripod Kamera {runId}`
60. Laporan rusak dibuat atas `Tripod Kamera {runId}` setelah Return
61. Verifikasi laporan rusak yang dibuat setelah Return tidak memberi penanda pada baris itu
62. Asset Admin `Maya Putri {runId}` melaporkan hilang `Genset Portable {runId}` dengan hak Aktor Missing
63. Verifikasi baris ditutup otomatis menjadi `Returned` dengan penanda `Missing` tanpa halaman Return
64. Aset `Genset Portable {runId}` ditemukan kembali sehingga status global aset berubah
65. Verifikasi penanda `Missing` tersimpan sebagai riwayat baris dan tidak berubah setelah status global aset berubah

### Return tetap dapat diselesaikan walau aset Unmanaged, Activity Lock, atau laporan hilang menunggu
66. Asset Admin menyelesaikan Return `Printer Warna Epson {runId}` yang berstatus `Unmanaged`
67. Verifikasi Return tetap boleh karena menyelesaikan transaksi berjalan
68. Asset Admin menyelesaikan Return `Server Rack Mini {runId}` yang ber-Activity Lock `In Audit`
69. Verifikasi Return tetap boleh walau aset `In Audit`
70. Asset Admin menyelesaikan Return `Mesin Bor Listrik {runId}` yang ber-Activity Lock `Under Maintenance`
71. Verifikasi Return tetap boleh walau aset `Under Maintenance`
72. Asset Admin memindai tag `Drone Mini {runId}` dan menyelesaikan Return saat laporan hilang Borrower berstatus `Waiting for Confirmation`
73. Verifikasi baris menjadi `Returned` dan Custody aset kembali `Available` di Group asal
74. Verifikasi baris `Drone Mini {runId}` tampil dengan badge `Reported Missing`
75. Verifikasi scan dicatat sebagai deteksi dan `missing_detected` dikirim ke `Maya Putri {runId}` sebagai Aktor Missing
76. Verifikasi record laporan tetap `Waiting for Confirmation` sampai Aktor Missing menindaklanjuti
77. Verifikasi `Confirm` pada record itu Disabled dengan alasan `This asset was scanned on [Date]. Reject the report or mark it as found.`

### Return offline di perangkat
78. Asset Admin menyimpan scan dan foto Return `Walkie Talkie Motorola {runId}` saat HP offline
79. Verifikasi scan dan foto Return disimpan lokal dengan status `Pending sync`
80. Aktor lain mengubah baris `Walkie Talkie Motorola {runId}`
81. HP terhubung kembali dan sinkron
82. Verifikasi konflik saat sinkron Return dimenangkan server dan Aktor Return diberi tahu

### Return self-service oleh Borrower atau dititipkan ke Aktor Borrow
83. Borrower `Sari Dewi {runId}` mengembalikan `Gimbal DJI {runId}` ke Group `Branch Surabaya {runId}`
84. Verifikasi Return ditolak di Return karena Borrower mengembalikan ke Group lain dari Group asal aset
85. Verifikasi Borrow tidak mengirim notifikasi kepada Aktor Borrow Group asal atas percobaan Return ke Group lain
86. Borrower `Sari Dewi {runId}` menjalankan sendiri Return `Gimbal DJI {runId}` di Group asal dengan scan tag
87. Verifikasi Return self-service oleh Borrower sendiri diperbolehkan dengan urutan yang sama seperti Return biasa
88. Verifikasi node `Returned` Borrow Log menampilkan `Returned via self-service by [Borrower]`
89. Asset Admin `Agus Pratama {runId}` menerima Return `Camera Sony Alpha {runId}` yang dititipkan Borrower `Sari Dewi {runId}`, dengan 1 foto Return
90. Verifikasi pinjaman self-service juga boleh diterima Aktor Borrow dan hasilnya sama seperti Return biasa
91. Verifikasi Received By adalah `Agus Pratama {runId}` dan node `Returned` Borrow Log menampilkan `Returned to [Receiver]`
92. Verifikasi foto Return diminta bila Photo at end `ON`
93. Verifikasi notifikasi Review tidak dikirim
94. Verifikasi Borrower `Sari Dewi {runId}` menerima `borrow_returned` seperti biasa
95. Verifikasi tidak ada kolom Received By di tabel karena penerima hanya tampil di node `Returned`

### Jumlah aset di daftar Return melebihi batas
96. Asset Admin mengirim Return atas `Aset Pinjam Batas {n} {runId}` sejumlah Bulk Transaction Row Limit ditambah satu
97. Verifikasi server menolak Return itu dengan Dialog Blok `D-BRW-18` dan tidak ada baris yang diproses
98. Verifikasi daftar aset tidak direset
