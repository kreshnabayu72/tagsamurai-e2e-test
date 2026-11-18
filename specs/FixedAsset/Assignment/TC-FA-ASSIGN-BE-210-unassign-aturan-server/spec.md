---
id: TC-FA-ASSIGN-BE-210-unassign-aturan-server
title: "Aturan Unassign: Aktor Assignment, marker, dan partial unassign"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.2#b38", "§9.2#b39", "§9.2#b40", "§9.2#b41", "§9.2#b42", "§9.2#b43", "§9.2#b44", "§9.2#b45", "§9.2#b46", "F-ASSIGN-07.k2", "F-ASSIGN-07.k5", "§9.4.3#b9", "§9.4.3#b12", "ASSIGN-LOGIC-09a", "ASSIGN-LOGIC-09b", "ASSIGN-LOGIC-09c", "ASSIGN-LOGIC-09d", "ASSIGN-LOGIC-09e", "ASSIGN-LOGIC-09f", "ASSIGN-LOGIC-09g", "ASSIGN-LOGIC-09h", "ASSIGN-LOGIC-09i", "ASSIGN-LOGIC-09j", "ASSIGN-LOGIC-09k", "ASSIGN-LOGIC-09l", "ASSIGN-LOGIC-09m", "ASSIGN-LOGIC-09n", "ASSIGN-LOGIC-09o", "ASSIGN-LOGIC-09p", "ASSIGN-LOGIC-09q", "ASSIGN-LOGIC-09r", "ASSIGN-LOGIC-09s", "ASSIGN-LOGIC-09t", "ASSIGN-LOGIC-09u", "ASSIGN-LOGIC-09v"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.2#b38": [3, 4, 7, 10, 16, 62, 65, 68, 71]
  "§9.2#b39": [21, 27]
  "§9.2#b40": [47, 49]
  "§9.2#b41": [58, 59]
  "§9.2#b42": [28, 37]
  "§9.2#b43": [14, 33, 34, 35]
  "§9.2#b44": [12, 13]
  "§9.2#b45": 25
  "§9.2#b46": 14
  "F-ASSIGN-07.k2": [25, 26]
  "F-ASSIGN-07.k5": [58, 59]
  "§9.4.3#b9": 16
  "§9.4.3#b12": [3, 7]
  "ASSIGN-LOGIC-09a": [3, 10]
  "ASSIGN-LOGIC-09b": 11
  "ASSIGN-LOGIC-09c": 18
  "ASSIGN-LOGIC-09d": 21
  "ASSIGN-LOGIC-09e": [24, 32]
  "ASSIGN-LOGIC-09f": [33, 74]
  "ASSIGN-LOGIC-09g": [41, 43, 76]
  "ASSIGN-LOGIC-09h": 35
  "ASSIGN-LOGIC-09i": 45
  "ASSIGN-LOGIC-09j": 38
  "ASSIGN-LOGIC-09k": [13, 39]
  "ASSIGN-LOGIC-09l": 32
  "ASSIGN-LOGIC-09m": 12
  "ASSIGN-LOGIC-09n": 24
  "ASSIGN-LOGIC-09o": 16
  "ASSIGN-LOGIC-09p": [47, 52]
  "ASSIGN-LOGIC-09q": 55
  "ASSIGN-LOGIC-09r": 27
  "ASSIGN-LOGIC-09s": 36
  "ASSIGN-LOGIC-09t": 34
  "ASSIGN-LOGIC-09u": 36
  "ASSIGN-LOGIC-09v": 12
---

# Aturan Unassign: Aktor Assignment, marker, dan partial unassign

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`, Group asal aset); Aktor Assignment `Agus Pratama {runId}` (Asset Admin, cakupan Group `Branch Surabaya {runId}`); Aktor Damaged `Dian Anggraeni {runId}` (pemegang hak keputusan menu Damaged pada Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-210-1: User, Aktor Assignment di Group asal aset: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-210-2: User, Aktor Assignment di Group lain: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Branch Surabaya {runId}`.
  - DU-210-3: User, Aktor Damaged: Nama `Dian Anggraeni {runId}`, Role `pemegang hak keputusan menu Damaged`, Cakupan Group `Head Office {runId}`.
  - DU-210-4: Handheld Reader, Reader tersambung untuk sesi scan Unassign: Nama `Reader Gudang {runId}`, Status `tersambung`, Status saat sesi Unassign DU-210-8 `diputus`.
  - DU-210-5: Assignment, ASG dengan satu baris Assigned di Group asal, Group aset kemudian berubah: Assignee `Wawan Setiawan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Genset Yamaha {runId}`, Status baris `Assigned`, Tag baris 1 `satu tag, sudah terverifikasi pada sesi Unassign`.
  - DU-210-6: Assignment, ASG dengan satu baris Assigned untuk Assignee yang mencoba Unassign: Assignee `Xaverius Putra {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor LG UltraWide {runId}`, Status baris `Assigned`.
  - DU-210-7: Assignment, ASG dengan tiga baris Assigned: Photo at end ON, OFF, dan baris yang tidak dimasukkan: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Asus Vivobook {runId}`, Baris 2 `Proyektor Optoma {runId}`, Baris 3 `Tablet Lenovo Tab {runId}`, Status baris `Assigned`, Tag baris 1 `satu tag`, Tag baris 2 `satu tag`, Tag baris 3 `satu tag`, Photo at start baris 1 `ON`, Photo at end baris 1 `ON`, Photo at end baris 2 `OFF`, Photo at end baris 3 `OFF`.
  - DU-210-8: Assignment, ASG dengan empat baris Assigned: laporan Damaged menunggu, laporan Damaged final, tanpa laporan, laporan dibuat di halaman Unassign: Assignee `Sari Wulandari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Fujifilm {runId}`, Baris 2 `Printer Canon Pixma {runId}`, Baris 3 `Speaker Bose {runId}`, Baris 4 `Mesin Cuci Electrolux {runId}`, Status baris `Assigned`, Laporan baris 1 `Damaged, Waiting for Confirmation`, Laporan baris 2 `Damaged, sudah dikonfirmasi`, Laporan baris 3 `tanpa laporan`, Laporan baris 4 `dibuat di halaman Unassign`, Description laporan baris 4 `Pintu mesin tidak menutup rapat`.
  - DU-210-9: Assignment, ASG dengan satu baris Assigned yang dilaporkan hilang: Assignee `Tono Hartanto {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Dispenser Cosmos {runId}`, Status baris `Assigned`.
  - DU-210-10: Assignment, ASG dengan satu baris Assigned bertag tidak terbaca dan Photo at end OFF: Assignee `Umar Fauzi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Router Cisco {runId}`, Status baris `Assigned`, Tag baris 1 `tag tidak terbaca`, Photo at end baris 1 `OFF`.
  - DU-210-11: Assignment, ASG dengan satu baris Waiting for Handover bertag tidak terbaca: Assignee `Vina Maharani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Switch Cisco Catalyst {runId}`, Status baris `Waiting for Handover`, Tag baris 1 `tag tidak terbaca`, Need recipient confirmation `No`.
  - DU-210-12: Assignment, ASG dengan daftar Unassign satu aset lebih banyak dari Bulk Transaction Row Limit: Assignee `Yuliana Sari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kursi Ergonomis {runId}`, Status baris `Assigned`, Jumlah aset di daftar `Bulk Transaction Row Limit ditambah satu`.
  - DU-210-13: Assignment, ASG Waiting for Handover untuk Handover sesudah Group aset berubah: Assignee `Bayu Setiadi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Genset Kohler {runId}`, Status baris `Waiting for Handover`, Tag baris 1 `satu tag, sudah terverifikasi pada sesi Handover`, Need recipient confirmation `No`, Photo at start `OFF`.
  - DU-210-14: Group, Group asal yang dipindah di bawah induk lain: Nama `Head Office {runId}`, Induk setelah dipindah `Region Jawa Timur {runId}`.
  - DU-210-15: Assignment, ASG dengan satu baris Assigned untuk Unassign sesudah hierarki Group berubah: Assignee `Citra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Panel Listrik Schneider {runId}`, Status baris `Assigned`, Tag baris 1 `satu tag`, Photo at end baris 1 `OFF`.
  - DU-210-16: Assignment, ASG dengan satu baris Assigned yang laporan Damaged-nya menunggu lalu dibatalkan pelapor: Assignee `Ayu Rahmawati {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kompresor Swan {runId}`, Status baris `Assigned`, Tag baris 1 `satu tag`, Photo at end baris 1 `OFF`, Laporan baris 1 `Damaged, Waiting for Confirmation`, Pelapor laporan baris 1 `Ayu Rahmawati {runId}`.
- Kondisi:
  - Photo at end per baris seperti di entri data.

## Test Steps

### Unassign hanya di Group asal oleh Aktor Assignment
1. Agus memindai tag baris `Genset Yamaha {runId}` pada halaman Unassign untuk Assignee `Wawan Setiawan {runId}`
2. Agus menekan `[Submit]` pada halaman Unassign untuk Assignee `Wawan Setiawan {runId}` dengan tag baris `Genset Yamaha {runId}` yang sudah terverifikasi
3. Verifikasi pemindaian dan Submit oleh Agus keduanya ditolak server karena Agus tidak punya cakupan Group asal `Head Office {runId}`, dan baris `Genset Yamaha {runId}` tetap `Assigned`
4. Verifikasi Aktor Assignment Group asal `Rina Wijaya {runId}` menerima notifikasi `assignment_pickup_needed` untuk menjemput aset
5. Group aset `Genset Yamaha {runId}` diubah menjadi `Branch Surabaya {runId}`
6. Agus menekan `[Submit]` pada halaman Unassign yang sama dengan tag baris `Genset Yamaha {runId}` yang sudah terverifikasi
7. Verifikasi Unassign tetap ditolak dan baris `Genset Yamaha {runId}` tetap di Group asal `Head Office {runId}` walau Group aset sudah berubah
8. Rina memverifikasi tag baris `Genset Yamaha {runId}`
9. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Wawan Setiawan {runId}`
10. Verifikasi baris `Genset Yamaha {runId}` berstatus `Unassigned` oleh Aktor Assignment yang punya cakupan Group asal
11. Verifikasi Assignment Log baris itu memuat node `Unassigned by [Receiver]` dengan Receiver `Rina Wijaya {runId}` sebagai penerima fisik di admin
12. Verifikasi Assignee `Wawan Setiawan {runId}` menerima notifikasi `assignment_unassigned` tanpa langkah konfirmasi dari Assignee
13. Verifikasi status header ASG DU-210-5 menjadi `Unassigned` karena semua baris aktif selesai
14. Verifikasi aset `Genset Yamaha {runId}` berstatus Custody `Available` dengan Group `Branch Surabaya {runId}` dan tidak ada Transfer yang terbentuk otomatis, dengan Condition tidak berubah

### Assignee tidak dapat memulai Unassign
15. Assignee `Xaverius Putra {runId}` mengirim permintaan Unassign langsung ke server untuk baris `Monitor LG UltraWide {runId}`
16. Verifikasi permintaan ditolak server dan baris `Monitor LG UltraWide {runId}` tetap `Assigned`

### Scan tag wajib, foto Photo at end, dan partial unassign
17. Rina menekan `[Submit]` pada halaman Unassign untuk baris `Laptop Asus Vivobook {runId}` tanpa memverifikasi tag-nya
18. Verifikasi Unassign ditolak karena scan tag wajib dan baris `Laptop Asus Vivobook {runId}` tetap `Assigned`
19. Rina memverifikasi tag baris `Laptop Asus Vivobook {runId}` dan `Proyektor Optoma {runId}` dengan reader `Reader Gudang {runId}` yang tersambung
20. Rina menekan `[Submit]` tanpa foto Unassign untuk baris `Laptop Asus Vivobook {runId}` yang Photo at end `ON`
21. Verifikasi Unassign ditolak karena foto 1 per aset wajib bila Photo at end `ON` dan tidak ada baris yang berubah
22. Rina mengambil satu foto Unassign untuk baris `Laptop Asus Vivobook {runId}`
23. Rina menekan `[Submit]` untuk baris `Laptop Asus Vivobook {runId}` dan `Proyektor Optoma {runId}` tanpa memasukkan baris `Tablet Lenovo Tab {runId}`
24. Verifikasi baris `Laptop Asus Vivobook {runId}` dan `Proyektor Optoma {runId}` berstatus `Unassigned`
25. Verifikasi baris `Tablet Lenovo Tab {runId}` yang tidak dimasukkan tetap `Assigned`
26. Verifikasi status header ASG DU-210-7 tetap `Assigned` karena masih ada baris aktif
27. Verifikasi baris `Laptop Asus Vivobook {runId}` menyimpan foto handover dan foto Unassign sebagai dua foto yang keduanya tersedia pada baris itu
28. Verifikasi log reader memuat tepat satu event Event Type `Assign Unassign Verify` dengan Transaction ID sama dengan nomor ASG DU-210-7

### Marker Damaged mengikuti record dan baris tanpa marker
29. Dengan reader `Reader Gudang {runId}` yang sudah diputus, Rina memverifikasi tag baris `Kamera Fujifilm {runId}`, `Printer Canon Pixma {runId}`, `Speaker Bose {runId}`, dan `Mesin Cuci Electrolux {runId}` pada DU-210-8
30. Rina membuat laporan rusak pada halaman Unassign untuk baris `Mesin Cuci Electrolux {runId}` dengan satu foto dan Description `Pintu mesin tidak menutup rapat`
31. Rina menekan `[Submit]` untuk keempat baris tanpa membawa pilihan hasil
32. Verifikasi keempat baris berstatus `Unassigned` tanpa menunggu keputusan atas laporan rusak
33. Verifikasi baris `Kamera Fujifilm {runId}`, `Printer Canon Pixma {runId}`, dan `Mesin Cuci Electrolux {runId}` bermarker `Damaged` karena punya record laporan rusak yang aktif, termasuk laporan yang dibuat di halaman Unassign
34. Verifikasi baris `Speaker Bose {runId}` tanpa marker `Damaged` dan Condition asetnya tidak berubah
35. Verifikasi baris `Kamera Fujifilm {runId}` tidak memunculkan Damage Report kedua dan marker menautkan ke record yang sudah ada
36. Verifikasi marker tiap baris ditetapkan dari record aktif aset tanpa pilihan hasil manual di halaman Unassign
37. Verifikasi log reader `Reader Gudang {runId}` tidak memuat event baru untuk ASG DU-210-8 karena reader sudah diputus
38. Verifikasi Assignment Log tiap baris menyimpan status akhir `Unassigned` beserta marker sebagai riwayat baris
39. Verifikasi status header ASG DU-210-8 tetap `Unassigned` setelah semua baris selesai
40. Dian menolak laporan rusak baris `Kamera Fujifilm {runId}`
41. Verifikasi marker `Damaged` pada baris `Kamera Fujifilm {runId}` hilang karena record ditolak
42. Dian menandai aset `Printer Canon Pixma {runId}` sebagai repaired
43. Verifikasi marker `Damaged` pada baris `Printer Canon Pixma {runId}` tidak berubah setelah aset di-repair

### Marker Missing dari laporan Missing
44. Rina melaporkan aset `Dispenser Cosmos {runId}` hilang dari halaman Assignment
45. Verifikasi baris `Dispenser Cosmos {runId}` berstatus `Unassigned` dengan marker `Missing` tanpa halaman Unassign

### Tag tidak terbaca saat Unassign
46. Rina melaporkan tag aset `Router Cisco {runId}` tidak terbaca lewat `I Can't Scan the TAG` pada halaman Unassign
47. Verifikasi Assignment Log baris `Router Cisco {runId}` memuat node `TAG reported` dan identifikasi manual diperbolehkan di langkah Unassign
48. Rina menekan `[Submit]` untuk baris `Router Cisco {runId}` tanpa foto Unassign padahal Photo at end `OFF`
49. Verifikasi Unassign ditolak karena foto Unassign wajib bagi tag yang diidentifikasi manual dan baris tetap `Assigned`
50. Rina mengambil satu foto Unassign untuk baris `Router Cisco {runId}`
51. Rina menekan `[Submit]` untuk baris `Router Cisco {runId}`
52. Verifikasi baris `Router Cisco {runId}` berstatus `Unassigned`

### Tag tidak terbaca memblokir Handover
53. Rina melaporkan tag aset `Switch Cisco Catalyst {runId}` tidak terbaca lewat `I Can't Scan the TAG` pada sesi Handover
54. Rina menekan `[Complete Handover]` untuk baris `Switch Cisco Catalyst {runId}`
55. Verifikasi Handover ditolak dan baris `Switch Cisco Catalyst {runId}` tetap `Waiting for Handover`

### Daftar Unassign melebihi Bulk Transaction Row Limit
56. Rina memverifikasi tag seluruh aset di daftar Unassign untuk Assignee `Yuliana Sari {runId}` yang berisi satu aset lebih banyak dari Bulk Transaction Row Limit
57. Rina menekan `[Submit]` pada halaman Unassign
58. Verifikasi Unassign ditolak karena jumlah aset melebihi Bulk Transaction Row Limit
59. Verifikasi tidak ada baris ASG milik Assignee `Yuliana Sari {runId}` yang berubah

### Handover tetap di Group asal sesudah Group aset berubah
60. Group aset `Genset Kohler {runId}` pada DU-210-13 diubah menjadi `Branch Surabaya {runId}`
61. Agus mengirim permintaan Handover untuk baris `Genset Kohler {runId}` yang tag-nya sudah terverifikasi
62. Verifikasi Handover ditolak server karena Agus tidak punya cakupan Group asal `Head Office {runId}` dan baris `Genset Kohler {runId}` tetap `Waiting for Handover`
63. Rina memverifikasi tag baris `Genset Kohler {runId}`
64. Rina menekan `[Complete Handover]` untuk baris `Genset Kohler {runId}`
65. Verifikasi baris `Genset Kohler {runId}` berstatus `Assigned` oleh Aktor Assignment yang punya cakupan Group asal `Head Office {runId}`

### Unassign tetap di Group asal sesudah hierarki Group berubah
66. Group `Head Office {runId}` pada DU-210-14 dipindah menjadi di bawah Group `Region Jawa Timur {runId}`
67. Agus memindai tag baris `Panel Listrik Schneider {runId}` pada halaman Unassign untuk Assignee `Citra Kusuma {runId}`
68. Verifikasi pemindaian ditolak server karena baris `Panel Listrik Schneider {runId}` tetap di Group asal `Head Office {runId}` walau hierarki Group berubah dan Agus tidak punya cakupan Group asal
69. Rina memverifikasi tag baris `Panel Listrik Schneider {runId}`
70. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Citra Kusuma {runId}`
71. Verifikasi baris `Panel Listrik Schneider {runId}` berstatus `Unassigned` oleh Aktor Assignment yang punya cakupan Group asal `Head Office {runId}` walau hierarki Group berubah

### Marker Damaged hilang bila laporan dibatalkan
72. Rina memverifikasi tag baris `Kompresor Swan {runId}` pada DU-210-16
73. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Ayu Rahmawati {runId}`
74. Verifikasi baris `Kompresor Swan {runId}` berstatus `Unassigned` dengan marker `Damaged` karena laporan rusak masih `Waiting for Confirmation`
75. Ayu Rahmawati membatalkan laporan rusak baris `Kompresor Swan {runId}` lewat `Cancel Damage Report`
76. Verifikasi marker `Damaged` pada baris `Kompresor Swan {runId}` hilang karena record dibatalkan
