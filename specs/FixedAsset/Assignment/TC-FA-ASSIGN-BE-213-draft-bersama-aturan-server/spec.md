---
id: TC-FA-ASSIGN-BE-213-draft-bersama-aturan-server
title: "Draft bersama: cakupan, versi, dan tanpa kunci aset"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.2#b56", "§9.2#b57", "§9.2#b58", "§9.2#b59", "§9.2#b60", "§9.2#b61", "§9.2#p73", "§9.2#r25", "§9.2#r26", "§9.2#r27", "§9.2#r28", "§9.2#r29", "§9.2#r30", "§9.2#r31", "§9.2#r32", "§9.2#r33", "§9.2#r34", "§9.4.3#b2", "ASSIGN-LOGIC-13a", "ASSIGN-LOGIC-13b", "ASSIGN-LOGIC-13c", "ASSIGN-LOGIC-13d", "ASSIGN-LOGIC-13e", "ASSIGN-LOGIC-13f", "ASSIGN-LOGIC-13g", "ASSIGN-LOGIC-13h", "ASSIGN-LOGIC-13i", "ASSIGN-LOGIC-13j", "ASSIGN-LOGIC-13k", "ASSIGN-LOGIC-13l", "ASSIGN-LOGIC-13m", "ASSIGN-LOGIC-13n", "ASSIGN-LOGIC-13o", "ASSIGN-LOGIC-13p", "ASSIGN-LOGIC-13q", "ASSIGN-LOGIC-13r", "ASSIGN-LOGIC-13s"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.2#b56": [2, 4]
  "§9.2#b57": [10, 12]
  "§9.2#b58": [42, 43, 45]
  "§9.2#b59": [21, 38, 40]
  "§9.2#b60": [47, 49]
  "§9.2#b61": [53, 54, 56, 103, 105, 107]
  "§9.2#p73": 69
  "§9.2#r25": [69, 71, 72]
  "§9.2#r26": [74, 75]
  "§9.2#r27": [79, 80]
  "§9.2#r28": [82, 83]
  "§9.2#r29": 87
  "§9.2#r30": [89, 91]
  "§9.2#r31": [93, 95]
  "§9.2#r32": [58, 59, 60, 63, 108]
  "§9.2#r33": [65, 67]
  "§9.2#r34": [76, 110, 112, 117, 119]
  "§9.4.3#b2": 4
  "ASSIGN-LOGIC-13a": 2
  "ASSIGN-LOGIC-13b": 6
  "ASSIGN-LOGIC-13c": 2
  "ASSIGN-LOGIC-13d": 3
  "ASSIGN-LOGIC-13e": [10, 12]
  "ASSIGN-LOGIC-13f": 27
  "ASSIGN-LOGIC-13g": [15, 17]
  "ASSIGN-LOGIC-13h": [20, 21]
  "ASSIGN-LOGIC-13i": [23, 25, 29, 32, 97, 98]
  "ASSIGN-LOGIC-13j": 51
  "ASSIGN-LOGIC-13k": [34, 36]
  "ASSIGN-LOGIC-13l": 30
  "ASSIGN-LOGIC-13m": 4
  "ASSIGN-LOGIC-13n": 5
  "ASSIGN-LOGIC-13o": 17
  "ASSIGN-LOGIC-13p": 27
  "ASSIGN-LOGIC-13q": [38, 40]
  "ASSIGN-LOGIC-13r": [7, 49, 100, 101]
  "ASSIGN-LOGIC-13s": 8
---

# Draft bersama: cakupan, versi, dan tanpa kunci aset

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); `Agus Pratama {runId}` (Asset Admin, cakupan Group `Branch Surabaya {runId}` saja); `Tono Wibowo {runId}` (Asset Admin, cakupan Group `Head Office {runId}` dan `Branch Surabaya {runId}`); `Mila Anggraini {runId}` (Monitoring & Report, cakupan Group `Head Office {runId}`); pembuat Draft `Nina Marlina {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Aktor Missing `Maya Sari {runId}` (pemegang hak keputusan menu Missing pada Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-213-1: User, Aktor Assignment pembuat Draft: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-213-2: User, Aktor Assignment dengan cakupan satu Group saja: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Branch Surabaya {runId}`.
  - DU-213-3: User, Aktor Assignment dengan cakupan dua Group: Nama `Tono Wibowo {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId} dan Branch Surabaya {runId}`.
  - DU-213-4: User, Pemantau tanpa hak Aktor Assignment: Nama `Mila Anggraini {runId}`, Role `Monitoring & Report`, Cakupan Group `Head Office {runId}`.
  - DU-213-5: User, Pembuat Draft yang kemudian dinonaktifkan: Nama `Nina Marlina {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-213-6: Draft, Draft bersama dengan dua aset Head Office dan satu aset Branch Surabaya, Purpose kosong: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Laptop Acer Aspire 5 {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Printer Canon LBP {runId}`, Group aset 2 `Head Office {runId}`, Aset 3 `Mobil Toyota Avanza {runId}`, Group aset 3 `Branch Surabaya {runId}`, Purpose `kosong`, Note `Pengajuan bersama`, Allowed assignee aset 2 `Employee saja`, Division pengganti `Finance {runId}`, PIC pengganti `Hendra Kusuma {runId}`, Purpose baru baris 3 `Operasional cabang`, Note baru `Pengajuan bersama cabang`, Note baru Tono `Pengajuan bersama Tono`.
  - DU-213-7: Draft, Draft yang asetnya terakhir dikeluarkan: Assignee `Cahya Ningrum {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Kursi Kerja Kulit {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-213-8: Draft, Draft yang di-Submit Aktor dengan cakupan semua Group: Assignee `Dewi Lestari {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Monitor Philips 24 {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Motor Honda Beat {runId}`, Group aset 2 `Branch Surabaya {runId}`, Purpose `Kunjungan lapangan`.
  - DU-213-9: Draft, Draft yang dihapus Aktor dengan cakupan semua Group: Assignee `Eka Saputra {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Speaker Aktif {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Kipas Meja {runId}`, Group aset 2 `Branch Surabaya {runId}`.
  - DU-213-10: Draft, Draft A berisi aset yang juga ada di Draft B: Assignee `Fani Rahmawati {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Proyektor Epson EB {runId}`, Group aset 1 `Head Office {runId}`, Purpose `Presentasi`.
  - DU-213-11: Draft, Draft B berisi aset yang sama dengan Draft A: Assignee `Gani Mahendra {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Proyektor Epson EB {runId}`, Group aset 1 `Head Office {runId}`, Purpose `Pelatihan`.
  - DU-213-12: Draft, Draft pertama Assignee dengan dua Draft: Assignee `Hana Permatasari {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Laptop Asus A {runId}`, Group aset 1 `Head Office {runId}`, Purpose baris 1 `Pekerjaan harian`, Aset yang ditambahkan `Laptop Asus B {runId}`.
  - DU-213-13: Draft, Draft kedua Assignee yang sama: Assignee `Hana Permatasari {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Kamera Sony Alpha {runId}`, Group aset 1 `Head Office {runId}`, Aset yang ditambahkan `Laptop Asus C {runId}`.
  - DU-213-14: Draft, Draft pertama untuk Delete sekaligus: Assignee `Indah Permata {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Meja Rapat Olympic {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-213-15: Draft, Draft kedua untuk Delete sekaligus: Assignee `Joko Susilo {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Lemari Arsip Brother {runId}`, Group aset 1 `Head Office {runId}`.
  - DU-213-16: Draft, Draft yang diubah dua Aktor dari versi yang sama: Assignee `Kiki Amelia {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Rak Gudang Besi {runId}`, Group aset 1 `Head Office {runId}`, Note awal `Versi awal`, Note Rina `Perubahan Rina`, Note Tono `Perubahan Tono`.
  - DU-213-17: Draft, Draft yang Assignee-nya dan pembuatnya dinonaktifkan: Assignee `Lina Hartati {runId}`, Tipe Assignee `Employee`, Pembuat `Nina Marlina {runId}`, Aset 1 `Dispenser Miyako {runId}`, Group aset 1 `Head Office {runId}`, Assignee pengganti `Wulan Sari {runId}`, Pesan Assignee tidak aktif `Lina Hartati {runId} is no longer active. Pick another assignee.`.
  - DU-213-18: Assignment, ASG dengan Assignee yang resign: satu baris Waiting for Handover, satu baris Assigned, dan satu baris Waiting for Approval: Assignee `Mario Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kompor Rinnai {runId}`, Baris 2 `Kipas Dyson {runId}`, Baris 3 `Pemanggang Oxone {runId}`, Status baris 1 `Waiting for Handover`, Status baris 2 `Assigned`, Status baris 3 `Waiting for Approval`.
  - DU-213-19: Assignment, ASG Division yang PIC-nya dinonaktifkan: Assignee `Pemasaran {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Proyektor Hitachi {runId}`, Status baris `Waiting for Handover`, PIC `Novi Andriani {runId}`, PIC pengganti `Wati Susanti {runId}`.
  - DU-213-20: Assignment, ASG dengan dua baris Assigned yang dilaporkan hilang lewat dua jalur: Assignee `Oscar Pratama {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Tablet iPad {runId}`, Baris 2 `Handphone Samsung {runId}`, Status baris `Assigned`.
  - DU-213-21: User, Aktor Missing: Nama `Maya Sari {runId}`, Role `pemegang hak keputusan menu Missing`, Cakupan Group `Head Office {runId}`.
  - DU-213-22: Assignment, ASG dengan baris Assigned yang dilaporkan rusak oleh Assignee: Assignee `Putri Ayu {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Olympus {runId}`, Status baris `Assigned`, Description laporan `Lensa retak`.
  - DU-213-23: Assignment, ASG dengan baris Assigned yang di-Unassign dari Group lain: Assignee `Qori Ramadhan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Meja Resepsionis {runId}`, Status baris `Assigned`.
  - DU-213-24: Assignment, ASG dengan baris Assigned yang tag-nya diganti: Assignee `Rudi Hartono {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Handy Talkie Motorola {runId}`, Status baris `Assigned`, Tag `tag lama diganti dengan tag baru`.
  - DU-213-25: Assignment, ASG dua aset tertukar: satu milik Assignee ini dan satu milik Assignee lain: Assignee `Sinta Dewi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Speaker Polytron {runId}`, Status baris `Assigned`, Aset tertukar milik Assignee lain `Speaker Sharp {runId}`, Assignee lain `Tania Putri {runId}`.
  - DU-213-26: Asset, Aset Available yang tidak sedang ditugaskan: Nama `Radio Panasonic {runId}`, Custody `Available`.
  - DU-213-27: Assignment, ASG dengan baris Waiting for Handover yang Allow Assign asetnya kemudian menjadi Deny: Assignee `Umar Fauzi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Radio Sony {runId}`, Status baris `Waiting for Handover`, Allow Assign override Asset `Allow, lalu diubah menjadi Deny`.
  - DU-213-28: Asset, Aset Available dengan Allow Assign override Asset Deny: Nama `Radio JVC {runId}`, Custody `Available`, Allow Assign override Asset `Deny`, Kontak override `Maya Sari {runId}`.
  - DU-213-29: Draft, Draft yang semua barisnya layak dan memuat dua Group: Assignee `Wawan Setiawan {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Meja Kerja Jati {runId}`, Group aset 1 `Head Office {runId}`, Aset 2 `Lemari Besi Sentra {runId}`, Group aset 2 `Branch Surabaya {runId}`, Purpose `Operasional kantor`.
  - DU-213-30: Draft, Draft atas nama Assignee yang kemudian dinonaktifkan: Assignee `Mario Santoso {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Blender Philips {runId}`, Group aset 1 `Head Office {runId}`, Pesan Assignee tidak aktif `Mario Santoso {runId} is no longer active. Pick another assignee.`.
  - DU-213-31: Assignment, ASG dengan dua baris Assigned untuk Disposal dan perubahan Condition: Assignee `Hendro Kusumo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Scanner Epson DS {runId}`, Baris 2 `Printer Brother HL {runId}`, Status baris `Assigned`, Condition aset `Normal`, Condition baru baris 1 `Damaged`.
- Kondisi:
  - Transaction timeout memakai nilai yang berlaku untuk entitas aktor dan tidak diubah spec ini.

## Test Steps

### Save Draft tanpa kunci aset, snapshot, dan nomor
1. Rina menekan `[Save Draft]` pada form Assignment Request untuk Assignee `Budi Santoso {runId}` dengan aset `Laptop Acer Aspire 5 {runId}`, `Printer Canon LBP {runId}`, dan `Mobil Toyota Avanza {runId}` tanpa Purpose pada DU-213-6
2. Verifikasi Draft tersimpan sebagai pengajuan yang belum di-Submit dengan satu Assignee `Budi Santoso {runId}`
3. Verifikasi Purpose boleh kosong selama Draft
4. Verifikasi ketiga aset tetap Custody `Available`, tanpa kunci aset, tanpa snapshot aturan efektif, dan tanpa nomor ASG
5. Verifikasi Draft memuat aset dari dua Group `Head Office {runId}` dan `Branch Surabaya {runId}` tanpa dipecah sebelum Submit
6. Verifikasi penyimpanan pengajuan sebelum Submit hanya berupa Draft dan tidak ada fitur Prelist
7. Verifikasi Transaction admin log mencatat `Rina Wijaya {runId}` sebagai pembuat Draft
8. Verifikasi Draft tampil dengan Modified By `Rina Wijaya {runId}` dan Last Updated

### Akses dan edit Draft menurut cakupan Group
9. Agus membuka tab Drafts
10. Verifikasi Draft `Budi Santoso {runId}` tampil bagi Agus karena cakupannya meliputi satu aset di Draft, bukan hanya bagi pembuatnya
11. Mila membuka tab Drafts
12. Verifikasi Draft `Budi Santoso {runId}` tidak tampil bagi Mila karena Monitoring & Report tidak punya hak Aktor Assignment
13. Agus mengubah Purpose baris `Mobil Toyota Avanza {runId}` menjadi `Operasional cabang`
14. Agus menyimpan Draft
15. Verifikasi perubahan Purpose baris `Mobil Toyota Avanza {runId}` tersimpan
16. Agus mengeluarkan baris `Laptop Acer Aspire 5 {runId}` dari Draft
17. Verifikasi pengeluaran ditolak dan baris di luar cakupan Agus tetap di Draft sebagai read-only dengan nama aset dan Group
18. Agus mengubah Note Draft menjadi `Pengajuan bersama cabang`
19. Agus mengganti Assignee Draft menjadi `Finance {runId}` bertipe `Division` dengan PIC `Hendra Kusuma {runId}`
20. Verifikasi Note, tipe Assignee, Assignee, dan PIC Draft berubah karena setiap Aktor yang boleh mengedit Draft dapat mengubahnya
21. Verifikasi kelayakan semua baris dievaluasi ulang termasuk baris di luar cakupan Agus: baris `Printer Canon LBP {runId}` ditandai dengan alasan `This asset can't be assigned to a division.`
22. Agus menekan `[Submit]` pada Draft itu
23. Verifikasi Submit ditolak karena cakupan Agus tidak meliputi semua Group di Draft
24. Agus menghapus Draft itu
25. Verifikasi Delete ditolak dan Draft tetap ada

### Draft tanpa aset hanya terlihat oleh pembuatnya
26. Rina mengeluarkan baris `Kursi Kerja Kulit {runId}` sebagai aset terakhir dari Draft `Cahya Ningrum {runId}` pada DU-213-7
27. Verifikasi Draft `Cahya Ningrum {runId}` hanya terlihat oleh `Rina Wijaya {runId}` dan tidak terlihat oleh `Tono Wibowo {runId}`

### Submit dan Delete oleh Aktor yang cakupannya meliputi semua Group
28. Tono menekan `[Submit]` pada Draft `Dewi Lestari {runId}` pada DU-213-8
29. Verifikasi Submit berhasil karena cakupan Tono meliputi semua Group di Draft
30. Verifikasi pengaju ASG yang terbentuk adalah `Tono Wibowo {runId}` sebagai Aktor yang menekan Submit
31. Tono menghapus Draft `Eka Saputra {runId}` pada DU-213-9
32. Verifikasi Delete berhasil karena cakupan Tono meliputi semua Group di Draft

### Satu aset di beberapa Draft
33. Rina menyimpan Draft A untuk `Fani Rahmawati {runId}` dan Draft B untuk `Gani Mahendra {runId}` yang sama-sama memuat `Proyektor Epson EB {runId}` pada DU-213-10 dan DU-213-11
34. Verifikasi kedua Draft tersimpan walau memuat aset yang sama
35. Rina menekan `[Submit]` pada Draft A
36. Verifikasi Draft A menjadi ASG dan Custody `Proyektor Epson EB {runId}` menjadi `In Assignment Process`
37. Rina membuka Draft B
38. Verifikasi baris `Proyektor Epson EB {runId}` di Draft B ditandai tidak layak dan tidak dihapus diam-diam
39. Rina menekan `[Submit]` pada Draft B tanpa mengeluarkan baris itu
40. Verifikasi Submit Draft B ditolak karena kelayakan dievaluasi ulang saat Submit

### Add to Assignment Draft idempoten dan warisan Purpose
41. Rina memilih `Add to Assignment Draft` untuk `Laptop Asus A {runId}` dan `Laptop Asus B {runId}` ke Draft pertama Assignee `Hana Permatasari {runId}` pada DU-213-12
42. Verifikasi `Laptop Asus A {runId}` yang sudah ada dilewati dan hanya `Laptop Asus B {runId}` masuk dengan Purpose `Pekerjaan harian` yang mewarisi baris terakhir
43. Verifikasi Assignee `Hana Permatasari {runId}` yang punya dua Draft dapat memilih salah satu Draft atau membuat Draft baru
44. Rina memilih `Add to Assignment Draft` untuk `Laptop Asus C {runId}` dan memilih membuat Draft baru untuk Assignee `Hana Permatasari {runId}` yang sudah punya Draft pada DU-213-13
45. Verifikasi Draft baru terbentuk untuk Assignee yang sama dan tidak menimpa dua Draft yang sudah ada

### Draft tanpa timeout dan Delete sekaligus
46. Waktu berlalu sampai Transaction timeout terlewati tanpa Draft `Indah Permata {runId}` dan `Joko Susilo {runId}` pada DU-213-14 dan DU-213-15 di-Submit
47. Verifikasi kedua Draft tidak pernah dihapus otomatis dan tetap ada
48. Tono menghapus kedua Draft sekaligus
49. Verifikasi kedua Draft terhapus dan Transaction admin log memuat satu entri per Draft yang dihapus

### Perubahan bersamaan dijaga versi
50. Rina dan Tono menyimpan perubahan Note atas Draft `Kiki Amelia {runId}` pada DU-213-16 dari versi yang sama hampir bersamaan
51. Verifikasi penyimpan pertama berhasil dan penyimpan kedua ditolak dengan `Draft Changed` tanpa menimpa perubahan pertama

### Assignee atau pembuat Draft dinonaktifkan
52. Assignee `Lina Hartati {runId}` pada DU-213-17 dinonaktifkan
53. Verifikasi Draft atas nama `Lina Hartati {runId}` tetap ada
54. Verifikasi Draft itu menampilkan `Lina Hartati {runId} is no longer active. Pick another assignee.` sampai Aktor memilih Assignee lain
55. Pembuat Draft `Nina Marlina {runId}` dinonaktifkan
56. Verifikasi Draft tetap ada dan dapat dilanjutkan Rina sebagai Aktor lain dalam cakupan

### Assignee resign: baris menunggu ditutup dan baris Assigned masuk Unassign
57. Assignee `Mario Santoso {runId}` pada DU-213-18 dinonaktifkan
58. Verifikasi baris `Kompor Rinnai {runId}` berstatus `Canceled` dengan alasan `Assignee deactivated`
59. Verifikasi Draft atas nama `Mario Santoso {runId}` pada DU-213-30 tetap ada dan menampilkan `Mario Santoso {runId} is no longer active. Pick another assignee.`
60. Verifikasi baris `Kipas Dyson {runId}` yang `Assigned` masuk daftar Unassign offboarding dan exit clearance tertahan
61. Rina memverifikasi tag baris `Kipas Dyson {runId}`
62. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Mario Santoso {runId}`
63. Verifikasi baris `Kipas Dyson {runId}` berstatus `Unassigned` dan exit clearance tidak tertahan lagi

### PIC dinonaktifkan membuat No PIC
64. PIC `Novi Andriani {runId}` pada DU-213-19 dinonaktifkan
65. Verifikasi baris `Proyektor Hitachi {runId}` diberi `No PIC` dan notifikasi `assignment_pic_required` terkirim
66. Rina menekan `[Complete Handover]` untuk baris `Proyektor Hitachi {runId}`
67. Verifikasi Handover diblokir sampai `Change PIC` selesai dan baris tetap `Waiting for Handover`

### Aset hilang lewat dua jalur
68. Rina melaporkan aset `Tablet iPad {runId}` pada DU-213-20 hilang dari halaman Assignment
69. Verifikasi baris `Tablet iPad {runId}` ditutup `Unassigned` dengan marker `Missing` dan status global aset menjadi hilang
70. Assignee `Oscar Pratama {runId}` melaporkan aset `Handphone Samsung {runId}` hilang dari tampilan Assignee
71. Verifikasi record laporan berstatus `Waiting for Confirmation` dan baris `Handphone Samsung {runId}` tetap `Assigned` dengan badge `Reported Missing`
72. Verifikasi notifikasi `missing_*` terkirim untuk kedua laporan

### Aset rusak saat ditugaskan, Unassign tanpa Damage Report kedua, dan transaksi lain menunggu
73. Assignee `Putri Ayu {runId}` melaporkan aset `Kamera Olympus {runId}` pada DU-213-22 rusak dengan Description `Lensa retak`
74. Verifikasi status global aset `Kamera Olympus {runId}` menjadi `Damaged` dan baris tetap `Assigned` dengan badge `Reported Damaged`
75. Verifikasi Repair tidak dimulai selama aset `Kamera Olympus {runId}` masih Assigned
76. Verifikasi permintaan transaksi lain untuk aset `Kamera Olympus {runId}` ditolak dan perubahan Condition menunggu Unassign
77. Rina memverifikasi tag baris `Kamera Olympus {runId}`
78. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Putri Ayu {runId}`
79. Verifikasi Unassign baris yang punya Damage Report tidak diblokir
80. Verifikasi tidak ada Damage Report kedua yang terbentuk

### Aset diserahkan ke Group lain saat Unassign ditolak
81. Agus menekan `[Submit]` pada halaman Unassign untuk Assignee `Qori Ramadhan {runId}` atas baris `Meja Resepsionis {runId}` pada DU-213-23
82. Verifikasi Unassign ditolak karena aset ada di Group asal `Head Office {runId}` dan baris tetap `Assigned`
83. Verifikasi Aktor Assignment Group asal `Rina Wijaya {runId}` menerima notifikasi `assignment_pickup_needed`

### Tag diganti saat ditugaskan
84. Tag aset `Handy Talkie Motorola {runId}` pada DU-213-24 diganti dengan tag baru
85. Rina memverifikasi tag baru baris `Handy Talkie Motorola {runId}`
86. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Rudi Hartono {runId}`
87. Verifikasi Unassign berhasil memakai tag baru dan baris `Handy Talkie Motorola {runId}` berstatus `Unassigned`

### Dua aset tertukar saat kembali
88. Rina memindai aset `Speaker Sharp {runId}` yang milik Assignee `Tania Putri {runId}` pada halaman Unassign untuk Assignee `Sinta Dewi {runId}` pada DU-213-25
89. Verifikasi pemindaian ditolak dengan pesan `Error, this asset isn't assigned to [Assignee].`
90. Rina memindai aset `Radio Panasonic {runId}` yang tidak sedang ditugaskan pada halaman Unassign yang sama
91. Verifikasi pemindaian ditolak dengan pesan `Error, this asset isn't assigned.`

### Setting berubah saat berjalan tidak memengaruhi penugasan berjalan
92. Allow Assign pada override Asset `Radio Sony {runId}` pada DU-213-27 diubah menjadi `Deny` setelah Submit
93. Verifikasi baris `Radio Sony {runId}` tetap berjalan sebagai `Waiting for Handover` sesuai snapshot
94. Rina mengajukan aset `Radio JVC {runId}` pada DU-213-28 yang Allow Assign override Asset-nya `Deny`
95. Verifikasi pengajuan baru ditolak karena Allow Assign berlaku untuk pengajuan berikutnya

### Submit oleh Aktor tanpa cakupan semua Group ditolak pada Draft yang semua barisnya layak
96. Agus menekan `[Submit]` pada Draft atas nama `Wawan Setiawan {runId}` pada DU-213-29 yang memuat aset dari Group `Head Office {runId}` dan `Branch Surabaya {runId}`
97. Verifikasi Submit ditolak karena cakupan Agus tidak meliputi Group `Head Office {runId}`, bukan karena kelayakan baris
98. Verifikasi Draft atas nama `Wawan Setiawan {runId}` tetap Draft tanpa nomor ASG

### Pengubah Draft tercatat di Transaction admin log
99. Tono menyimpan Draft pada DU-213-6 dengan Note `Pengajuan bersama Tono`
100. Verifikasi Transaction admin log mencatat `Tono Wibowo {runId}` sebagai pengubah Draft itu
101. Verifikasi Transaction admin log mencatat `Agus Pratama {runId}` sebagai pengubah Draft itu dari penyimpanan perubahan Purpose baris `Mobil Toyota Avanza {runId}`

### Pesan Assignee tidak aktif hilang setelah Assignee lain dipilih
102. Rina membuka Draft atas nama `Lina Hartati {runId}` pada DU-213-17
103. Verifikasi Draft menampilkan `Lina Hartati {runId} is no longer active. Pick another assignee.`
104. Rina menyimpan Draft itu dengan Assignee `Wulan Sari {runId}`
105. Verifikasi pesan `Lina Hartati {runId} is no longer active. Pick another assignee.` tidak lagi tampil pada Draft atas nama `Wulan Sari {runId}`
106. Rina menekan `[Submit]` pada Draft atas nama `Wulan Sari {runId}`
107. Verifikasi ASG baru terbentuk untuk Assignee `Wulan Sari {runId}` sehingga Draft dapat dilanjutkan Rina walau pembuatnya `Nina Marlina {runId}` sudah dinonaktifkan

### Baris Waiting for Approval atas nama Assignee yang dinonaktifkan
108. Verifikasi baris `Pemanggang Oxone {runId}` pada DU-213-18 yang berstatus `Waiting for Approval` berstatus `Canceled` dengan alasan `Assignee deactivated` setelah Assignee `Mario Santoso {runId}` dinonaktifkan

### Disposal dan perubahan Condition menunggu Unassign
109. Rina mengajukan Disposal untuk aset `Printer Brother HL {runId}` pada DU-213-31 selagi baris berstatus `Assigned`
110. Verifikasi permintaan Disposal ditolak selagi baris `Assigned`
111. Rina mengubah Condition aset `Scanner Epson DS {runId}` dari `Normal` menjadi `Damaged` selagi baris berstatus `Assigned`
112. Verifikasi perubahan Condition ditolak dan Condition aset tetap `Normal`
113. Rina memverifikasi tag baris `Scanner Epson DS {runId}`
114. Rina memverifikasi tag baris `Printer Brother HL {runId}`
115. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Hendro Kusumo {runId}`
116. Rina mengubah Condition aset `Scanner Epson DS {runId}` dari `Normal` menjadi `Damaged` setelah Unassign
117. Verifikasi perubahan Condition diterima dan Condition aset menjadi `Damaged`
118. Rina mengajukan Disposal untuk aset `Printer Brother HL {runId}` setelah Unassign
119. Verifikasi permintaan Disposal diterima
