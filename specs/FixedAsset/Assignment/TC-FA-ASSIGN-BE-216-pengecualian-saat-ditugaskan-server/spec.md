---
id: TC-FA-ASSIGN-BE-216-pengecualian-saat-ditugaskan-server
title: "Report Missing, Report Damaged, tag diganti, dan aset Missing saat ditugaskan"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§3#p10", "ASSIGN-LOGIC-16b", "ASSIGN-LOGIC-16c", "ASSIGN-LOGIC-16d", "ASSIGN-LOGIC-16e", "ASSIGN-LOGIC-16f", "ASSIGN-LOGIC-16g", "ASSIGN-LOGIC-16h", "ASSIGN-LOGIC-16i", "ASSIGN-LOGIC-16j", "ASSIGN-LOGIC-16k", "ASSIGN-LOGIC-16l", "ASSIGN-LOGIC-16m", "ASSIGN-LOGIC-16n", "ASSIGN-LOGIC-16o", "ASSIGN-LOGIC-16p", "ASSIGN-LOGIC-16q", "ASSIGN-LOGIC-16r", "ASSIGN-LOGIC-16s", "ASSIGN-LOGIC-16t", "ASSIGN-LOGIC-16u", "ASSIGN-LOGIC-16v", "ASSIGN-LOGIC-16w", "ASSIGN-LOGIC-16x", "ASSIGN-LOGIC-16y", "ASSIGN-LOGIC-16z", "ASSIGN-LOGIC-16aa", "ASSIGN-LOGIC-16ab", "ASSIGN-LOGIC-16ac", "ASSIGN-LOGIC-16ai", "ASSIGN-LOGIC-16aj", "ASSIGN-LOGIC-16ak", "ASSIGN-LOGIC-16al", "ASSIGN-LOGIC-16am", "ASSIGN-LOGIC-16an", "ASSIGN-LOGIC-16ao"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§3#p10": [6, 42]
  "ASSIGN-LOGIC-16b": 3
  "ASSIGN-LOGIC-16c": 4
  "ASSIGN-LOGIC-16d": 13
  "ASSIGN-LOGIC-16e": 14
  "ASSIGN-LOGIC-16f": 15
  "ASSIGN-LOGIC-16g": 17
  "ASSIGN-LOGIC-16h": [20, 23]
  "ASSIGN-LOGIC-16i": 33
  "ASSIGN-LOGIC-16j": 35
  "ASSIGN-LOGIC-16k": [38, 46]
  "ASSIGN-LOGIC-16l": [38, 39, 46]
  "ASSIGN-LOGIC-16m": 63
  "ASSIGN-LOGIC-16n": [40, 56, 63]
  "ASSIGN-LOGIC-16o": [44, 48, 79]
  "ASSIGN-LOGIC-16p": [51, 56]
  "ASSIGN-LOGIC-16q": 65
  "ASSIGN-LOGIC-16r": 68
  "ASSIGN-LOGIC-16s": [55, 61]
  "ASSIGN-LOGIC-16t": 55
  "ASSIGN-LOGIC-16u": 72
  "ASSIGN-LOGIC-16v": [11, 81, 82, 84]
  "ASSIGN-LOGIC-16w": 29
  "ASSIGN-LOGIC-16x": 26
  "ASSIGN-LOGIC-16y": 30
  "ASSIGN-LOGIC-16z": [31, 85, 87, 91, 93]
  "ASSIGN-LOGIC-16aa": 8
  "ASSIGN-LOGIC-16ab": [9, 95]
  "ASSIGN-LOGIC-16ac": 76
  "ASSIGN-LOGIC-16ai": 2
  "ASSIGN-LOGIC-16aj": 5
  "ASSIGN-LOGIC-16ak": 36
  "ASSIGN-LOGIC-16al": 41
  "ASSIGN-LOGIC-16am": 58
  "ASSIGN-LOGIC-16an": 53
  "ASSIGN-LOGIC-16ao": 61
---

# Report Missing, Report Damaged, tag diganti, dan aset Missing saat ditugaskan

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Aktor Missing `Maya Sari {runId}` (pemegang hak keputusan menu Missing); Aktor Damaged `Dian Anggraeni {runId}` (pemegang hak keputusan menu Damaged); `Fitri Handayani {runId}` (Asset Admin yang juga memegang hak keputusan menu Missing pada Group `Head Office {runId}`); `Tono Wibowo {runId}` (Asset Admin yang juga memegang hak Aktor Damaged pada Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-216-1: User, Aktor Assignment pelapor: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-216-2: User, Aktor Missing: Nama `Maya Sari {runId}`, Role `pemegang hak keputusan menu Missing`, Cakupan Group `Head Office {runId}`.
  - DU-216-3: User, Aktor Damaged: Nama `Dian Anggraeni {runId}`, Role `pemegang hak keputusan menu Damaged`, Cakupan Group `Head Office {runId}`.
  - DU-216-4: User, Aktor Assignment yang juga memegang hak Aktor Damaged: Nama `Tono Wibowo {runId}`, Role `Asset Admin dan pemegang hak keputusan menu Damaged`, Cakupan Group `Head Office {runId}`.
  - DU-216-5: Assignment, ASG dengan dua baris Assigned: satu dilaporkan hilang oleh Aktor Assignment, satu tidak: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Tablet iPad {runId}`, Baris 2 `Handphone Samsung {runId}`, Status baris `Assigned`.
  - DU-216-6: Assignment, ASG dengan empat baris Assigned yang dilaporkan hilang oleh Assignee dengan akhir berbeda: Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Acer Swift {runId}`, Baris 2 `Monitor LG UltraWide {runId}`, Baris 3 `Printer HP LaserJet {runId}`, Baris 4 `Kamera Sony Alpha {runId}`, Status baris `Assigned`.
  - DU-216-7: Assignment, ASG dengan satu baris Waiting for Approval dan satu baris Waiting for Handover yang asetnya dilaporkan hilang: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Speaker JBL {runId}`, Baris 2 `Router Mikrotik {runId}`, Status baris 1 `Waiting for Approval`, Status baris 2 `Waiting for Handover`.
  - DU-216-8: Draft, Draft yang memuat aset yang dilaporkan hilang: Assignee `Fani Rahmawati {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Kamera Fujifilm {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-216-9: Assignment, ASG dengan lima baris Assigned untuk laporan Damaged dengan akhir berbeda: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Olympus {runId}`, Baris 2 `Lensa Canon {runId}`, Baris 3 `Flash Godox {runId}`, Baris 4 `Tripod Manfrotto {runId}`, Baris 5 `Mic Shure {runId}`, Status baris `Assigned`, What happened `Lensa retak`.
  - DU-216-10: Assignment, ASG dengan baris Assigned yang dilaporkan rusak langsung oleh pelapor berhak Aktor Damaged: Assignee `Gita Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Lampu Studio {runId}`, Status baris `Assigned`.
  - DU-216-11: Assignment, ASG dengan baris Assigned yang tag-nya diganti: Assignee `Hadi Susanto {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Handy Talkie Motorola {runId}`, Status baris `Assigned`, Tag `tag lama diganti dengan tag baru`.
  - DU-216-12: Assignment, ASG Division dengan baris Assigned yang dilaporkan rusak oleh PIC: Assignee `Operasional {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Genset Cummins {runId}`, Status baris `Assigned`, PIC `Indah Permata {runId}`, What happened `Mesin overheat`, Foto laporan `satu foto`.
  - DU-216-13: Assignment, ASG dengan baris Waiting for Handover untuk pemindaian aset Missing saat Handover: Assignee `Joko Widodo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Meja Lipat Lifetime {runId}`, Status baris `Waiting for Handover`.
  - DU-216-14: Assignment, ASG dengan baris Assigned yang dilaporkan hilang oleh Assignee lalu di-Unassign: Assignee `Kiki Amelia {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Router Cisco {runId}`, Status baris `Assigned`, Condition awal `Normal`.
  - DU-216-15: User, Aktor Assignment yang juga Aktor Missing: Nama `Fitri Handayani {runId}`, Role `Asset Admin dan pemegang hak keputusan menu Missing`, Cakupan Group `Head Office {runId}`.
- Kondisi:
  - Condition awal semua aset `Normal`.

## Test Steps

### Report Missing oleh Aktor Assignment menutup baris saat itu juga
1. Rina melaporkan aset `Tablet iPad {runId}` pada DU-216-5 hilang dari halaman Assignment
2. Verifikasi laporan langsung berstatus `Missing` tanpa review dan kotak dampak menyebut ASG yang ditutup
3. Verifikasi baris `Tablet iPad {runId}` ditutup `Unassigned` dengan marker `Missing` saat itu juga tanpa scan
4. Verifikasi status global aset `Tablet iPad {runId}` menjadi `Missing`
5. Verifikasi baris `Handphone Samsung {runId}` di ASG yang sama tetap `Assigned`
6. Verifikasi Assignment Log baris `Tablet iPad {runId}` memuat node `Reported missing by [Actor]`

### Aset Missing yang dipindai tidak dapat diproses
7. Rina memindai aset `Tablet iPad {runId}` pada halaman Unassign untuk Assignee `Budi Santoso {runId}`
8. Verifikasi pemindaian ditolak dengan pesan `[Asset Name] is reported missing.` beserta tautan `[View Missing Log]`
9. Verifikasi penolakan itu tidak memuat `[Mark as Found]` bagi Rina karena Rina bukan Aktor Missing
10. Rina memindai aset `Tablet iPad {runId}` saat menambahkannya ke form Assignment baru
11. Verifikasi pemindaian hanya dicatat sebagai deteksi dan status global aset `Tablet iPad {runId}` tetap `Missing`

### Report Missing oleh Assignee: dikonfirmasi
12. Assignee `Citra Dewi {runId}` pada DU-216-6 melaporkan aset `Laptop Acer Swift {runId}` hilang dari tampilan Assignee
13. Verifikasi record laporan berstatus `Waiting for Confirmation`
14. Verifikasi status global aset `Laptop Acer Swift {runId}` langsung `Missing`
15. Verifikasi baris `Laptop Acer Swift {runId}` tetap `Assigned` dengan badge `Reported Missing`
16. Maya mengonfirmasi laporan aset `Laptop Acer Swift {runId}`
17. Verifikasi baris `Laptop Acer Swift {runId}` ditutup `Unassigned` dengan marker `Missing`

### Report Missing oleh Assignee: dibatalkan atau ditolak
18. Assignee `Citra Dewi {runId}` melaporkan aset `Monitor LG UltraWide {runId}` hilang
19. Assignee `Citra Dewi {runId}` membatalkan laporannya lewat `Cancel Missing Report`
20. Verifikasi badge `Reported Missing` pada baris `Monitor LG UltraWide {runId}` hilang dan baris tetap `Assigned`
21. Assignee `Citra Dewi {runId}` melaporkan aset `Printer HP LaserJet {runId}` hilang
22. Maya menolak laporan aset `Printer HP LaserJet {runId}`
23. Verifikasi badge `Reported Missing` pada baris `Printer HP LaserJet {runId}` hilang dan baris tetap `Assigned`

### Unassign baris yang laporan pemegangnya masih menunggu
24. Assignee `Citra Dewi {runId}` melaporkan aset `Kamera Sony Alpha {runId}` hilang
25. Rina membuka halaman Unassign untuk Assignee `Citra Dewi {runId}`
26. Verifikasi daftar Unassign memuat baris `Kamera Sony Alpha {runId}` dengan badge `Reported Missing` yang bertautan ke Missing Log
27. Rina memverifikasi tag baris `Kamera Sony Alpha {runId}`
28. Rina menekan `[Submit]` pada halaman Unassign
29. Verifikasi baris `Kamera Sony Alpha {runId}` berstatus `Unassigned` tanpa menunggu keputusan laporan
30. Verifikasi Custody aset `Kamera Sony Alpha {runId}` kembali `Available` di Group asal `Head Office {runId}`
31. Verifikasi record laporan tetap `Waiting for Confirmation` sampai Maya menolak atau menandainya `Found` untuk memulihkan Condition

### Permintaan belum diserahkan ditutup saat aset dilaporkan hilang
32. Maya melaporkan aset `Speaker JBL {runId}` dan `Router Mikrotik {runId}` pada DU-216-7 hilang
33. Verifikasi baris `Speaker JBL {runId}` dan `Router Mikrotik {runId}` berstatus `Canceled` oleh `System` dengan alasan `Asset reported missing`
34. Maya melaporkan aset `Kamera Fujifilm {runId}` yang ada di Draft pada DU-216-8 hilang
35. Verifikasi Draft `Fani Rahmawati {runId}` tidak diubah dan tetap memuat `Kamera Fujifilm {runId}`
36. Verifikasi aset `Kamera Fujifilm {runId}` di Draft itu ditandai tidak layak

### Report Damaged oleh Assignee
37. Assignee `Dedi Prasetyo {runId}` pada DU-216-9 melaporkan aset `Kamera Olympus {runId}` rusak dari tampilan Assignee dengan satu foto dan What happened `Lensa retak`
38. Verifikasi record laporan berstatus `Waiting for Confirmation` dan dibuat dari satu foto beserta What happened
39. Verifikasi status global aset `Kamera Olympus {runId}` langsung `Damaged`
40. Verifikasi baris `Kamera Olympus {runId}` tetap `Assigned` dengan badge `Reported Damaged`
41. Verifikasi notifikasi `assignment_damage_reported` terkirim
42. Verifikasi Assignment Log baris itu memuat node `Damage reported by [Reporter]`
43. Assignee `Dedi Prasetyo {runId}` membatalkan laporan rusak miliknya sendiri
44. Verifikasi laporan ditarik oleh pelapornya dan badge `Reported Damaged` hilang

### Report Damaged oleh Aktor Assignment dan pembatalan oleh pelapor sendiri
45. Rina melaporkan aset `Lensa Canon {runId}` rusak dari Assignment Detail dengan satu foto dan What happened `Lensa retak`
46. Verifikasi record laporan Rina berstatus `Waiting for Confirmation` dan status global aset `Lensa Canon {runId}` langsung `Damaged`
47. Rina membatalkan laporan rusak miliknya sendiri dari Assignment Detail
48. Verifikasi laporan ditarik oleh Rina sebagai pelapornya

### Laporan pelapor lain dan keputusan hanya oleh Aktor Damaged
49. Assignee `Dedi Prasetyo {runId}` melaporkan aset `Flash Godox {runId}` rusak
50. Rina membatalkan laporan Dedi atas aset `Flash Godox {runId}`
51. Verifikasi pembatalan ditolak karena laporan pelapor lain tidak dapat dibatalkan Aktor Assignment
52. Rina mengonfirmasi laporan aset `Flash Godox {runId}`
53. Verifikasi keputusan Rina ditolak karena Aktor Assignment tidak memutuskan laporan
54. Dian mengonfirmasi laporan aset `Flash Godox {runId}` lewat menu keputusan
55. Verifikasi status global aset `Flash Godox {runId}` tetap `Damaged` oleh keputusan Aktor Damaged
56. Verifikasi baris `Flash Godox {runId}` tetap `Assigned` dengan badge `Damaged` setelah dikonfirmasi
57. Assignee `Dedi Prasetyo {runId}` membatalkan laporan yang sudah `Damaged` atas aset `Flash Godox {runId}`
58. Verifikasi pembatalan ditolak karena laporan `Damaged` tidak dapat dibatalkan

### Laporan ditolak mengembalikan keadaan seperti sebelum laporan
59. Assignee `Dedi Prasetyo {runId}` melaporkan aset `Tripod Manfrotto {runId}` rusak
60. Dian menolak laporan aset `Tripod Manfrotto {runId}`
61. Verifikasi status global aset `Tripod Manfrotto {runId}` kembali seperti sebelum laporan dan badge `Reported Damaged` hilang

### Pelapor berhak Aktor Damaged, Mark as Repaired, dan Unassign
62. Tono melaporkan aset `Lampu Studio {runId}` pada DU-216-10 rusak
63. Verifikasi laporan Tono langsung `Damaged` tanpa menunggu konfirmasi dan baris `Lampu Studio {runId}` berbadge `Damaged`
64. Dian menandai aset `Lampu Studio {runId}` sebagai repaired selama aset tetap `Assigned`
65. Verifikasi status global aset `Lampu Studio {runId}` kembali ke Condition sebelumnya dan badge `Damaged` pada baris hilang
66. Rina memverifikasi tag baris `Lampu Studio {runId}`
67. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Gita Lestari {runId}`
68. Verifikasi baris `Lampu Studio {runId}` berstatus `Unassigned` tanpa marker `Damaged`

### Unassign tanpa menunggu keputusan laporan Damaged
69. Assignee `Dedi Prasetyo {runId}` melaporkan aset `Mic Shure {runId}` rusak
70. Rina memverifikasi tag baris `Mic Shure {runId}`
71. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Dedi Prasetyo {runId}` atas baris `Mic Shure {runId}`
72. Verifikasi baris `Mic Shure {runId}` berstatus `Unassigned` dengan marker `Damaged` tanpa menunggu keputusan laporan

### Tag diganti saat ditugaskan
73. Tag aset `Handy Talkie Motorola {runId}` pada DU-216-11 diganti dengan tag baru
74. Rina memverifikasi tag baru baris `Handy Talkie Motorola {runId}`
75. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Hadi Susanto {runId}`
76. Verifikasi tag lama tidak dibutuhkan karena Unassign memakai tag baru dan baris `Handy Talkie Motorola {runId}` selesai `Unassigned`

### Pembatalan laporan Damaged oleh PIC sebagai pelapor
77. PIC `Indah Permata {runId}` pada DU-216-12 melaporkan aset `Genset Cummins {runId}` rusak dari tampilan PIC dengan satu foto dan What happened `Mesin overheat`
78. PIC `Indah Permata {runId}` membatalkan laporan rusak miliknya sendiri dari tampilan PIC
79. Verifikasi laporan ditarik oleh PIC sebagai pelapornya dan badge `Reported Damaged` pada baris `Genset Cummins {runId}` hilang

### Aset Missing yang dipindai pada Handover dan Unassign hanya dicatat sebagai deteksi
80. Rina memindai aset `Tablet iPad {runId}` pada Handover baris `Meja Lipat Lifetime {runId}` pada DU-216-13
81. Verifikasi pemindaian hanya dicatat sebagai deteksi dan baris `Meja Lipat Lifetime {runId}` tetap `Waiting for Handover`
82. Verifikasi status global aset `Tablet iPad {runId}` tetap `Missing`
83. Rina memindai aset `Tablet iPad {runId}` pada halaman Unassign untuk Assignee `Budi Santoso {runId}`
84. Verifikasi status global aset `Tablet iPad {runId}` tetap `Missing` setelah pemindaian itu

### Keputusan Aktor Missing sesudah Unassign memulihkan Condition
85. Verifikasi status global aset `Kamera Sony Alpha {runId}` tetap `Missing` sesudah baris `Unassigned`
86. Maya menolak laporan aset `Kamera Sony Alpha {runId}`
87. Verifikasi Condition aset `Kamera Sony Alpha {runId}` pulih ke `Normal` dan status global aset tidak lagi `Missing`
88. Assignee `Kiki Amelia {runId}` pada DU-216-14 melaporkan aset `Router Cisco {runId}` hilang
89. Rina memverifikasi tag baris `Router Cisco {runId}`
90. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Kiki Amelia {runId}`
91. Verifikasi status global aset `Router Cisco {runId}` tetap `Missing` dan record laporan tetap `Waiting for Confirmation` sesudah Unassign
92. Maya menekan `[Mark as Found]` pada laporan aset `Router Cisco {runId}`
93. Verifikasi Condition aset `Router Cisco {runId}` pulih ke `Normal` dan status global aset tidak lagi `Missing`

### Penolakan scan aset Missing memuat Mark as Found bagi Aktor Missing
94. Fitri memindai aset `Tablet iPad {runId}` pada halaman Unassign untuk Assignee `Budi Santoso {runId}`
95. Verifikasi penolakan pemindaian itu memuat `[Mark as Found]` karena Fitri adalah Aktor Missing di Group aset
