---
id: TC-FA-ASSIGN-BE-209-handover-aturan-server
title: "Aturan Handover: scan wajib, sesi konfirmasi, jendela konfirmasi, dan handover sebagian"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.2#b29", "§9.2#b30", "§9.2#b31", "§9.2#b32", "§9.2#b33", "§9.2#b34", "§9.2#b35", "§9.2#b36", "§9.2#b37", "§9.2#p60", "§9.2#p62", "§9.2#p64", "§9.2#p65", "§9.2#p66", "F-ASSIGN-06.k1", "F-ASSIGN-06.k2", "F-ASSIGN-06.k3", "F-ASSIGN-06.k4", "F-ASSIGN-06.k5", "F-ASSIGN-06.k6", "F-ASSIGN-06.k8", "EC-ASG-15", "EC-ASG-17", "EC-ASG-51", "EC-ASG-70", "DO-ASG-08", "§9.5#r10", "§9.4.3#b8", "§10#r7", "ASSIGN-LOGIC-08a", "ASSIGN-LOGIC-08b", "ASSIGN-LOGIC-08c", "ASSIGN-LOGIC-08d", "ASSIGN-LOGIC-08e", "ASSIGN-LOGIC-08f", "ASSIGN-LOGIC-08g", "ASSIGN-LOGIC-08h", "ASSIGN-LOGIC-08i", "ASSIGN-LOGIC-08j", "ASSIGN-LOGIC-08k", "ASSIGN-LOGIC-08l", "ASSIGN-LOGIC-08m", "ASSIGN-LOGIC-08n", "ASSIGN-LOGIC-08o", "ASSIGN-LOGIC-08p", "ASSIGN-LOGIC-08q", "ASSIGN-LOGIC-08r", "ASSIGN-LOGIC-08s", "ASSIGN-LOGIC-08t", "ASSIGN-LOGIC-08u"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.2#b29": [2, 110]
  "§9.2#b30": [11, 13, 15, 21]
  "§9.2#b31": [27, 29]
  "§9.2#b32": [37, 38, 39, 49, 68]
  "§9.2#b33": [61, 71, 89]
  "§9.2#b34": 5
  "§9.2#b35": [5, 6]
  "§9.2#b36": [9, 24]
  "§9.2#b37": [49, 55]
  "§9.2#p60": [95, 98]
  "§9.2#p62": 95
  "§9.2#p64": 95
  "§9.2#p65": [95, 98]
  "§9.2#p66": 100
  "F-ASSIGN-06.k1": [5, 8]
  "F-ASSIGN-06.k2": [47, 51]
  "F-ASSIGN-06.k3": [59, 60, 70]
  "F-ASSIGN-06.k4": [43, 79, 81, 89]
  "F-ASSIGN-06.k5": [95, 98]
  "F-ASSIGN-06.k6": 49
  "F-ASSIGN-06.k8": 29
  "EC-ASG-15": [59, 60, 61, 62]
  "EC-ASG-17": [79, 80, 81, 147, 148, 149]
  "EC-ASG-51": [68, 75, 127, 133]
  "EC-ASG-70": [64, 73, 83]
  "DO-ASG-08": [79, 80, 147, 148]
  "§9.5#r10": [59, 139, 143]
  "§9.4.3#b8": [92, 136, 141]
  "§10#r7": [41, 47, 88, 131]
  "ASSIGN-LOGIC-08a": 2
  "ASSIGN-LOGIC-08b": 11
  "ASSIGN-LOGIC-08c": 21
  "ASSIGN-LOGIC-08d": 24
  "ASSIGN-LOGIC-08e": [27, 31]
  "ASSIGN-LOGIC-08f": [34, 35]
  "ASSIGN-LOGIC-08g": 37
  "ASSIGN-LOGIC-08h": [114, 116, 120, 121, 125]
  "ASSIGN-LOGIC-08i": [42, 87]
  "ASSIGN-LOGIC-08j": 88
  "ASSIGN-LOGIC-08k": 5
  "ASSIGN-LOGIC-08l": 47
  "ASSIGN-LOGIC-08m": 41
  "ASSIGN-LOGIC-08n": [59, 60, 70]
  "ASSIGN-LOGIC-08o": 55
  "ASSIGN-LOGIC-08p": 17
  "ASSIGN-LOGIC-08q": 29
  "ASSIGN-LOGIC-08r": 68
  "ASSIGN-LOGIC-08s": [104, 108]
  "ASSIGN-LOGIC-08t": 7
  "ASSIGN-LOGIC-08u": 48
---

# Aturan Handover: scan wajib, sesi konfirmasi, jendela konfirmasi, dan handover sebagian

## Prerequisites
- Aktor: Aktor Assignment `Lina Marlina {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Aktor Assignment kedua `Hendra Kusuma {runId}` (Asset Admin, cakupan Group `Head Office {runId}`, PIC Division `Finance {runId}`); Aktor Missing `Maya Sari {runId}` (pemegang hak keputusan menu Missing pada Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-209-1: User, Aktor Assignment pertama: Nama `Lina Marlina {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-209-2: User, Aktor Assignment kedua yang juga PIC Division: Nama `Hendra Kusuma {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`, PIC Division `Finance {runId}`.
  - DU-209-3: User, Aktor Missing: Nama `Maya Sari {runId}`, Role `pemegang hak keputusan menu Missing`, Cakupan Group `Head Office {runId}`.
  - DU-209-4: Assignment, ASG dengan satu baris Waiting for Approval: Assignee `Andi Pratama {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer Epson L3250 {runId}`, Status baris 1 `Waiting for Approval`.
  - DU-209-5: Assignment, ASG dengan dua baris Waiting for Handover tanpa konfirmasi penerima: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Dell Latitude {runId}`, Baris 2 `Monitor Samsung 27 {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, Photo at start `OFF`.
  - DU-209-6: Handheld Reader, Reader tersambung untuk sesi scan Handover: Nama `Reader Gudang {runId}`, Status `tersambung`.
  - DU-209-7: Assignment, ASG dengan baris ber-tag, Non TAG, dua tag, dan tag tidak terbaca: Assignee `Hana Permatasari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Router Mikrotik {runId}`, Baris 2 `Meja Kerja Kayu {runId}`, Baris 3 `Drone DJI Mavic {runId}`, Baris 4 `Kamera Sony Alpha {runId}`, Tag baris 1 `satu tag, belum diverifikasi`, Tag baris 2 `Non TAG`, Tag baris 3 `dua tag ter-pair, QR dan RFID`, Tag baris 4 `tag tidak terbaca`, Status baris `Waiting for Handover`, Need recipient confirmation `No`.
  - DU-209-8: Asset, Aset Available untuk dipilih lewat scan di form: Nama `Kipas Angin Cosmos {runId}`, Custody `Available`, Tag `satu tag`.
  - DU-209-9: Assignment, ASG dengan Photo at start ON: Assignee `Wulan Anggraini {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer Brother HL {runId}`, Baris 2 `Mouse Logitech {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, Photo at start `ON`.
  - DU-209-10: Assignment, ASG dengan dua baris yang butuh konfirmasi, semuanya lolos: Assignee `Nanda Rahman {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Proyektor BenQ {runId}`, Baris 2 `Speaker JBL {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-11: Assignment, ASG campuran: butuh konfirmasi, tanpa konfirmasi, belum dipindai, dan terverifikasi tetapi tidak dipilih: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Proyektor Epson EB {runId}`, Baris 2 `Kamera Canon EOS {runId}`, Baris 3 `Printer HP LaserJet {runId}`, Baris 4 `Scanner Fujitsu {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation baris 1 `Yes`, Need recipient confirmation baris 2 `No`, Need recipient confirmation baris 3 `Yes`, Need recipient confirmation baris 4 `Yes`, Photo at start `OFF`.
  - DU-209-12: Assignment, ASG untuk jendela konfirmasi habis: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Lenovo ThinkPad {runId}`, Baris 2 `Tablet Lenovo M10 {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-13: Assignment, ASG untuk Cancel Request dan Cancel saat sesi berjalan: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kulkas Sharp {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-14: Assignment, ASG untuk konfirmasi HP dan Confirm on This Device hampir bersamaan: Assignee `Fajar Nugroho {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Televisi LG {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-15: Assignment, ASG dengan checklist per aset dan pernyataan: Assignee `Gita Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Mesin Fotokopi Ricoh {runId}`, Baris 2 `Whiteboard Elektronik {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-16: Assignment, ASG Division dengan Aktor sebagai PIC: Assignee `Finance {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Honda EU {runId}`, PIC `Hendra Kusuma {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-17: Asset, Aset Available yang diajukan Aktor untuk dirinya sendiri: Nama `Tablet Samsung Galaxy Tab {runId}`, Custody `Available`, Calon Assignee `Hendra Kusuma {runId}`, Tipe Assignee `Employee`.
  - DU-209-18: Assignment, ASG Division yang PIC-nya diganti saat sesi berjalan: Assignee `Operasional {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Perkins {runId}`, PIC `Indah Permata {runId}`, PIC pengganti `Joko Susilo {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-19: Assignment, ASG Division yang PIC-nya dinonaktifkan saat sesi berjalan: Assignee `Logistik {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Forklift Toyota {runId}`, PIC `Rudi Hartono {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-20: Assignment, ASG yang salah satu asetnya dilaporkan hilang saat sesi berjalan: Assignee `Kartika Putri {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Dispenser Sanken {runId}`, Baris 2 `Water Heater Modena {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-21: Assignment, ASG yang Assignee-nya dinonaktifkan saat sesi berjalan: Assignee `Lestari Wulandari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Mesin Cuci Electrolux {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-22: Assignment, ASG yang salah satu barisnya melewati batas serah terima saat sesi berjalan: Assignee `Maman Suryadi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Oven Listrik Philips {runId}`, Baris 2 `Blender Philips {runId}`, Sisa batas serah terima baris 1 `10 menit`, Sisa batas serah terima baris 2 `2 hari`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-23: Assignment, ASG yang sesinya selesai dengan satu baris tidak dicentang: Assignee `Hesti Maharani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Rice Cooker Miyako {runId}`, Baris 2 `Dispenser Cosmos {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
  - DU-209-24: Assignment, ASG yang butuh konfirmasi untuk uji penyelesaian tanpa konfirmasi, Confirm tanpa pernyataan, dan batas jendela: Assignee `Joni Hartono {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kursi Ergonomis Ergotec {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`, Waktu tunggu sebelum Confirm `14 menit`.
  - DU-209-25: Assignment, ASG untuk konfirmasi HP dikomit lebih dulu lalu Confirm on This Device menyusul: Assignee `Ratna Kusumawati {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Lemari Arsip Lion {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `Yes`, Photo at start `OFF`.
- Kondisi:
  - Jendela konfirmasi Handover bernilai `15 menit`.
  - Send email notifications (Assign) bernilai `OFF`.

## Test Steps

### Hanya baris Waiting for Handover yang dapat diserahkan
1. Lina mengirim permintaan Handover untuk baris `Printer Epson L3250 {runId}` pada DU-209-4 yang berstatus `Waiting for Approval`
2. Verifikasi permintaan ditolak server dan baris `Printer Epson L3250 {runId}` tetap `Waiting for Approval`

### Handover tanpa konfirmasi penerima langsung Assigned
3. Lina memverifikasi tag baris `Laptop Dell Latitude {runId}` dan `Monitor Samsung 27 {runId}` pada DU-209-5 dengan reader `Reader Gudang {runId}` yang tersambung
4. Lina menekan `[Complete Handover]` untuk kedua baris
5. Verifikasi kedua baris berstatus `Assigned` tanpa permintaan konfirmasi kepada Assignee
6. Verifikasi Custody kedua aset `Assigned` dan status header ASG `Assigned`
7. Verifikasi Assignee `Budi Santoso {runId}` menerima notifikasi `assignment_handed_over`
8. Verifikasi Assignment Log kedua baris memuat node `Handed over` dengan Confirmation `Not required`
9. Verifikasi log reader memuat tepat satu event Event Type `Assign Handover Verify` untuk sesi handover itu

### Scan tag wajib untuk aset ber-tag
10. Lina menekan `[Complete Handover]` untuk baris `Router Mikrotik {runId}` pada DU-209-7 tanpa memverifikasi tag-nya
11. Verifikasi permintaan ditolak karena scan tag wajib bagi aset ber-tag dan baris `Router Mikrotik {runId}` tetap `Waiting for Handover`
12. Lina memindai tag aset `Monitor Samsung 27 {runId}` pada sesi Handover ASG DU-209-7
13. Verifikasi pemindaian itu ditolak dan tidak ada baris ASG DU-209-7 yang terverifikasi, karena tag bukan milik baris `Waiting for Handover` di ASG ini
14. Lina memindai satu dari dua tag aset `Drone DJI Mavic {runId}`
15. Verifikasi baris `Drone DJI Mavic {runId}` terverifikasi cukup dengan satu tag
16. Lina melewati langkah scan untuk baris `Meja Kerja Kayu {runId}` yang berkategori `Non TAG`
17. Verifikasi baris `Meja Kerja Kayu {runId}` terverifikasi tanpa scan
18. Lina melaporkan tag aset `Kamera Sony Alpha {runId}` tidak terbaca lewat `I Can't Scan the TAG`
19. Lina mengirim permintaan Handover untuk baris `Kamera Sony Alpha {runId}`
20. Hendra mengirim permintaan Handover untuk baris `Kamera Sony Alpha {runId}`
21. Verifikasi kedua permintaan ditolak dan baris `Kamera Sony Alpha {runId}` tetap `Waiting for Handover` sampai penggantian tag selesai
22. Lina mencatat jumlah event Event Type `Assign Handover Verify` pada log reader `Reader Gudang {runId}` sebelum pemindaian
23. Lina memindai aset `Kipas Angin Cosmos {runId}` dengan reader `Reader Gudang {runId}` saat menambahkannya ke form Assignment baru
24. Verifikasi jumlah event Event Type `Assign Handover Verify` pada log reader `Reader Gudang {runId}` tidak bertambah, karena pemindaian itu hanya memilih aset

### Foto Handover wajib dari kamera langsung
25. Lina mengambil satu foto dari kamera langsung untuk baris `Printer Brother HL {runId}` pada DU-209-9
26. Lina menekan `[Complete Handover]` untuk baris `Printer Brother HL {runId}`
27. Verifikasi baris `Printer Brother HL {runId}` berstatus `Assigned` dengan satu foto handover
28. Lina menekan `[Complete Handover]` untuk baris `Mouse Logitech {runId}` tanpa foto karena kamera tidak tersedia atau izin kamera ditolak
29. Verifikasi permintaan ditolak untuk baris `Mouse Logitech {runId}` dan baris itu tetap `Waiting for Handover`
30. Lina menekan `[Complete Handover]` untuk baris `Mouse Logitech {runId}` dengan berkas foto hasil unggahan
31. Verifikasi permintaan ditolak karena foto wajib berasal dari kamera langsung tanpa unggahan berkas

### Satu sesi konfirmasi untuk semua aset terverifikasi
32. Lina memverifikasi tag baris `Proyektor BenQ {runId}` dan `Speaker JBL {runId}` pada DU-209-10
33. Lina menekan `[Request Confirmation]`
34. Verifikasi satu sesi konfirmasi terbentuk untuk ASG DU-209-10 dan memuat kedua aset
35. Verifikasi kedua baris tetap `Waiting for Handover` selama sesi berjalan
36. Lina menekan `[Request Confirmation]` sekali lagi untuk ASG yang sama
37. Verifikasi ASG itu tetap memiliki satu sesi aktif dan permintaan kedua memakai sesi yang sama
38. Verifikasi Assignee `Nanda Rahman {runId}` menerima Task `Confirm Handover` dan notifikasi `assignment_confirmation_required`
39. Verifikasi Assignee `Nanda Rahman {runId}` menerima satu email konfirmasi handover yang memuat kedua aset walau Send email notifications bernilai `OFF`
40. Nanda Rahman mengonfirmasi penerimaan kedua aset dengan satu pernyataan yang dicentang dan kedua aset dicentang di checklist
41. Verifikasi kedua baris berstatus `Assigned` lewat satu konfirmasi untuk seluruh sesi
42. Verifikasi Assignment Log kedua baris memuat node `Handed over` dengan Confirmation `Accepted on phone`
43. Verifikasi Task `Confirm Handover` tidak ada lagi bagi Assignee `Nanda Rahman {runId}`

### Campuran aset butuh dan tanpa konfirmasi serta handover sebagian
44. Lina memverifikasi tag baris `Proyektor Epson EB {runId}`, `Kamera Canon EOS {runId}`, dan `Scanner Fujitsu {runId}` pada DU-209-11 dan tidak memverifikasi baris `Printer HP LaserJet {runId}`
45. Lina memilih baris `Proyektor Epson EB {runId}` dan `Kamera Canon EOS {runId}` untuk sesi ini
46. Lina menekan `[Request Confirmation]`
47. Verifikasi baris `Kamera Canon EOS {runId}` yang tanpa konfirmasi langsung `Assigned` dengan Confirmation `Not required`
48. Verifikasi sesi konfirmasi hanya memuat baris `Proyektor Epson EB {runId}`
49. Verifikasi baris `Printer HP LaserJet {runId}` dan `Scanner Fujitsu {runId}` tetap `Waiting for Handover`
50. Waktu berlalu sampai `15 menit` sejak `[Request Confirmation]` tanpa konfirmasi
51. Verifikasi baris `Kamera Canon EOS {runId}` tetap `Assigned` setelah jendela habis dan hanya baris `Proyektor Epson EB {runId}` yang kembali tanpa sesi
52. Lina memverifikasi tag baris `Printer HP LaserJet {runId}` dan `Scanner Fujitsu {runId}`
53. Lina menekan `[Request Confirmation]` dengan hanya baris `Printer HP LaserJet {runId}` dan `Scanner Fujitsu {runId}` yang dipilih untuk sesi kedua, tanpa baris `Proyektor Epson EB {runId}`
54. Citra Dewi mengonfirmasi penerimaan kedua aset sesi kedua dengan pernyataan dicentang dan kedua aset dicentang di checklist
55. Verifikasi baris `Printer HP LaserJet {runId}` dan `Scanner Fujitsu {runId}` berstatus `Assigned` sedangkan baris `Proyektor Epson EB {runId}` tetap `Waiting for Handover`

### Jendela konfirmasi habis membatalkan sesi
56. Lina memverifikasi tag baris `Laptop Lenovo ThinkPad {runId}` dan `Tablet Lenovo M10 {runId}` pada DU-209-12
57. Lina menekan `[Request Confirmation]`
58. Waktu berlalu sampai `15 menit` sejak `[Request Confirmation]` tanpa konfirmasi
59. Verifikasi sesi konfirmasi batal setelah `15 menit` tanpa konfirmasi
60. Verifikasi kedua baris tetap `Waiting for Handover`
61. Verifikasi Assignment Log tiap baris memuat node `Confirmation not received` dengan pelaku `System`
62. Verifikasi Task `Confirm Handover` tidak ada lagi bagi Assignee `Dedi Prasetyo {runId}`
63. Dedi Prasetyo menekan Confirm pada sesi yang sudah habis
64. Verifikasi Confirm ditolak server, Assignee melihat dialog `Handover No Longer Available`, dan kedua baris tidak berubah

### Cancel Request dan Cancel saat sesi berjalan
65. Lina memverifikasi tag baris `Kulkas Sharp {runId}` pada DU-209-13
66. Lina menekan `[Request Confirmation]`
67. Lina membatalkan baris `Kulkas Sharp {runId}` saat sesi konfirmasi berjalan
68. Verifikasi pembatalan ditolak dengan pesan `Handover is in progress for this asset.` dan baris `Kulkas Sharp {runId}` tetap `Waiting for Handover`
69. Lina menekan `[Cancel Request]`
70. Verifikasi sesi batal dan baris `Kulkas Sharp {runId}` tetap `Waiting for Handover`
71. Verifikasi Assignment Log baris itu memuat node `Confirmation not received` dengan penyebab `Cancel Request` oleh Aktor Assignment
72. Eko Wijaya menekan Confirm sesudah `[Cancel Request]`
73. Verifikasi Confirm ditolak server, Assignee melihat dialog `Handover No Longer Available`, dan baris tidak berubah
74. Lina membatalkan baris `Kulkas Sharp {runId}` sesudah sesi batal
75. Verifikasi pembatalan berhasil dan baris `Kulkas Sharp {runId}` berstatus `Canceled`

### Konfirmasi HP dan Confirm on This Device hampir bersamaan
76. Lina memverifikasi tag baris `Televisi LG {runId}` pada DU-209-14
77. Lina menekan `[Request Confirmation]`
78. `Confirm on This Device` oleh Lina dikomit lebih dulu, disusul hampir bersamaan konfirmasi dari HP Assignee `Fajar Nugroho {runId}`
79. Verifikasi baris `Televisi LG {runId}` berstatus `Assigned` oleh `Confirm on This Device` yang dikomit lebih dulu
80. Verifikasi konfirmasi dari HP yang masuk kedua diabaikan dan selesai tanpa error
81. Verifikasi Assignment Log baris itu memuat tepat satu node `Handed over`
82. Fajar Nugroho menekan Confirm sekali lagi
83. Verifikasi Confirm ditolak server karena konfirmasi sudah masuk lewat perangkat admin, Assignee melihat dialog `Handover No Longer Available`, dan baris tetap `Assigned`

### Checklist per aset dan pernyataan wajib dicentang
84. Lina memverifikasi tag baris `Mesin Fotokopi Ricoh {runId}` dan `Whiteboard Elektronik {runId}` pada DU-209-15
85. Lina menekan `[Request Confirmation]`
86. Lina memakai `Confirm on This Device` dengan pernyataan dicentang dan hanya baris `Mesin Fotokopi Ricoh {runId}` yang dicentang
87. Verifikasi baris `Mesin Fotokopi Ricoh {runId}` berstatus `Assigned` dengan Confirmation `Confirmed by` Lina Marlina on behalf of Gita Lestari
88. Verifikasi baris `Whiteboard Elektronik {runId}` yang tidak dicentang tetap `Waiting for Handover`
89. Verifikasi Assignment Log baris `Whiteboard Elektronik {runId}` memuat satu node `Confirmation not received`
90. Lina menekan `[Request Confirmation]` untuk baris `Whiteboard Elektronik {runId}`
91. Lina memakai `Confirm on This Device` dengan pernyataan tidak dicentang
92. Verifikasi konfirmasi ditolak dan baris `Whiteboard Elektronik {runId}` tetap `Waiting for Handover`

### Pemisahan peran: Aktor yang menjadi PIC tidak dapat menyerahkan
93. Hendra membuka `Hand Over` untuk ASG DU-209-16 yang Assignee-nya Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`
94. Hendra mengirim permintaan Handover langsung ke server untuk baris `Genset Honda EU {runId}`
95. Verifikasi permintaan ditolak server, baris tetap `Waiting for Handover`, dan tidak ada log baru
96. Lina memverifikasi tag baris `Genset Honda EU {runId}`
97. Lina menekan `[Request Confirmation]`
98. Verifikasi sesi konfirmasi terbentuk untuk PIC `Hendra Kusuma {runId}` karena Aktor Assignment lain memprosesnya
99. Hendra mengajukan Assignment atas aset `Tablet Samsung Galaxy Tab {runId}` dengan dirinya sendiri sebagai Assignee Employee
100. Verifikasi pengajuan diterima dan ASG baru terbentuk dengan Assignee `Hendra Kusuma {runId}`

### PIC berganti atau dinonaktifkan membatalkan sesi
101. Lina memverifikasi tag baris `Genset Perkins {runId}` pada DU-209-18
102. Lina menekan `[Request Confirmation]`
103. Lina mengganti PIC ASG DU-209-18 dari `Indah Permata {runId}` menjadi `Joko Susilo {runId}`
104. Verifikasi sesi batal, baris `Genset Perkins {runId}` tetap `Waiting for Handover`, dan Task `Confirm Handover` ditutup
105. Lina memverifikasi tag baris `Forklift Toyota {runId}` pada DU-209-19
106. Lina menekan `[Request Confirmation]`
107. PIC `Rudi Hartono {runId}` dinonaktifkan
108. Verifikasi sesi batal, baris `Forklift Toyota {runId}` tetap `Waiting for Handover`, dan Task `Confirm Handover` ditutup
109. Lina mengirim permintaan Handover untuk baris `Forklift Toyota {runId}` yang ditandai `No PIC`
110. Verifikasi permintaan ditolak dengan pesan `Set a PIC for this division first.` sampai Change PIC selesai

### Baris yang ditutup keluar dari sesi dan sesi aset lain berlanjut
111. Lina memverifikasi tag baris `Dispenser Sanken {runId}` dan `Water Heater Modena {runId}` pada DU-209-20
112. Lina menekan `[Request Confirmation]`
113. Maya Sari melaporkan aset `Dispenser Sanken {runId}` hilang
114. Verifikasi baris `Dispenser Sanken {runId}` berstatus `Canceled` oleh `System` dengan alasan `Asset reported missing`, keluar dari sesi, dan tampil `Not received` di hasil sesi
115. Kartika Putri mengonfirmasi penerimaan baris `Water Heater Modena {runId}` dengan pernyataan dicentang
116. Verifikasi baris `Water Heater Modena {runId}` berstatus `Assigned` karena sesi untuk aset lain berlanjut

### Baris yang ditutup oleh System keluar dari sesi dan sesi aset lain berlanjut
117. Lina memverifikasi tag baris `Oven Listrik Philips {runId}` dan `Blender Philips {runId}` pada DU-209-22
118. Lina menekan `[Request Confirmation]`
119. Waktu berlalu sampai batas serah terima baris `Oven Listrik Philips {runId}` terlampaui sementara sesi konfirmasi berjalan
120. Verifikasi baris `Oven Listrik Philips {runId}` berstatus `Canceled` oleh `System` dengan alasan `Not handed over`, keluar dari sesi, dan tampil `Not received` di hasil sesi
121. Verifikasi sesi untuk baris `Blender Philips {runId}` berlanjut dan baris itu tetap `Waiting for Handover`
122. Lina memverifikasi tag baris `Mesin Cuci Electrolux {runId}` pada DU-209-21
123. Lina menekan `[Request Confirmation]`
124. Assignee `Lestari Wulandari {runId}` dinonaktifkan
125. Verifikasi baris `Mesin Cuci Electrolux {runId}` berstatus `Canceled` oleh `System` dengan alasan `Assignee deactivated`, keluar dari sesi, dan tampil `Not received` di hasil sesi

### Cancel dapat diulang sesudah jendela habis dan sesudah sesi selesai
126. Lina membatalkan baris `Tablet Lenovo M10 {runId}` pada DU-209-12 sesudah jendela konfirmasi habis
127. Verifikasi pembatalan berhasil dan baris `Tablet Lenovo M10 {runId}` berstatus `Canceled`
128. Lina memverifikasi tag baris `Rice Cooker Miyako {runId}` dan `Dispenser Cosmos {runId}` pada DU-209-23
129. Lina menekan `[Request Confirmation]`
130. Hesti Maharani mengonfirmasi penerimaan hanya baris `Rice Cooker Miyako {runId}` dengan pernyataan dicentang sehingga sesi selesai
131. Verifikasi baris `Dispenser Cosmos {runId}` yang tidak dicentang tetap `Waiting for Handover`
132. Lina membatalkan baris `Dispenser Cosmos {runId}` sesudah sesi selesai
133. Verifikasi pembatalan berhasil dan baris `Dispenser Cosmos {runId}` berstatus `Canceled`

### Penyelesaian tanpa konfirmasi, Confirm tanpa pernyataan, dan batas jendela konfirmasi
134. Lina memverifikasi tag baris `Kursi Ergonomis Ergotec {runId}` pada DU-209-24
135. Lina mengirim permintaan menyelesaikan Handover untuk baris `Kursi Ergonomis Ergotec {runId}` tanpa sesi konfirmasi
136. Verifikasi permintaan ditolak karena baris butuh konfirmasi penerima dan baris `Kursi Ergonomis Ergotec {runId}` tetap `Waiting for Handover`
137. Lina menekan `[Request Confirmation]`
138. Waktu berlalu sampai `14 menit` sejak `[Request Confirmation]` tanpa konfirmasi
139. Verifikasi sesi konfirmasi masih aktif pada `14 menit` dan baris `Kursi Ergonomis Ergotec {runId}` tetap `Waiting for Handover`
140. Joni Hartono mengonfirmasi penerimaan baris `Kursi Ergonomis Ergotec {runId}` tanpa mencentang pernyataan
141. Verifikasi Confirm ditolak dan baris `Kursi Ergonomis Ergotec {runId}` tetap `Waiting for Handover`
142. Joni Hartono mengonfirmasi penerimaan baris `Kursi Ergonomis Ergotec {runId}` dengan pernyataan dicentang
143. Verifikasi baris `Kursi Ergonomis Ergotec {runId}` berstatus `Assigned` karena konfirmasi diterima pada `14 menit`

### Konfirmasi HP dikomit lebih dulu dan Confirm on This Device menyusul
144. Lina memverifikasi tag baris `Lemari Arsip Lion {runId}` pada DU-209-25
145. Lina menekan `[Request Confirmation]`
146. Konfirmasi dari HP Assignee `Ratna Kusumawati {runId}` dikomit lebih dulu, disusul hampir bersamaan `Confirm on This Device` oleh Lina
147. Verifikasi baris `Lemari Arsip Lion {runId}` berstatus `Assigned` dengan Confirmation `Accepted on phone`
148. Verifikasi `Confirm on This Device` yang masuk kedua diabaikan dan selesai tanpa error
149. Verifikasi Assignment Log baris itu memuat tepat satu node `Handed over`
