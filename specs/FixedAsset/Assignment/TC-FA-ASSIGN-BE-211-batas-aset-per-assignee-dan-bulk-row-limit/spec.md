---
id: TC-FA-ASSIGN-BE-211-batas-aset-per-assignee-dan-bulk-row-limit
title: "Max assets per assignee dan Bulk Transaction Row Limit"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["ASSIGN-LOGIC-01m", "§9.2#p21", "§9.2#p23", "§9.2#p25", "§9.2#p26", "§9.2#p27", "§9.2#p28", "§9.2#p29", "§9.2#b9", "§9.2#b10", "§9.2#b11", "§9.2#b12", "§9.2#p31", "§9.2#b13", "§9.2#b14", "§9.2#b15", "§9.2#b16", "EC-ASG-04", "EC-ASG-90", "EC-ASG-91", "EC-ASG-92", "V-ASG-13", "F-ASSIGN-03.k4", "§9.5#r8", "ASSIGN-LOGIC-10a", "ASSIGN-LOGIC-10b", "ASSIGN-LOGIC-10c", "ASSIGN-LOGIC-10d", "ASSIGN-LOGIC-10e", "ASSIGN-LOGIC-10f"]
smoke: []
dependsOn: []
owner: BE
trace:
  "ASSIGN-LOGIC-01m": [31, 36]
  "§9.2#p21": [4, 5]
  "§9.2#p23": 6
  "§9.2#p25": 6
  "§9.2#p26": 4
  "§9.2#p27": [5, 6]
  "§9.2#p28": [10, 11]
  "§9.2#p29": 10
  "§9.2#b9": 12
  "§9.2#b10": 13
  "§9.2#b11": 14
  "§9.2#b12": [26, 28, 29]
  "§9.2#p31": 31
  "§9.2#b13": [31, 38]
  "§9.2#b14": [36, 38]
  "§9.2#b15": [31, 32, 34, 53, 54]
  "§9.2#b16": [40, 44, 56, 58, 60]
  "EC-ASG-04": 23
  "EC-ASG-90": 36
  "EC-ASG-91": [40, 42]
  "EC-ASG-92": 34
  "V-ASG-13": [4, 19, 21]
  "F-ASSIGN-03.k4": [31, 32, 42]
  "§9.5#r8": 31
  "ASSIGN-LOGIC-10a": [4, 5, 16, 21, 23, 46, 48, 50, 51]
  "ASSIGN-LOGIC-10b": [5, 11]
  "ASSIGN-LOGIC-10c": 28
  "ASSIGN-LOGIC-10d": 18
  "ASSIGN-LOGIC-10e": [4, 10]
  "ASSIGN-LOGIC-10f": 19
---

# Max assets per assignee dan Bulk Transaction Row Limit

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}` dan `Branch Surabaya {runId}`); Aktor Assignment kedua `Agus Pratama {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Approver `Mira Handayani {runId}` (cakupan Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-211-1: User, Aktor Assignment pertama: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId} dan Branch Surabaya {runId}`.
  - DU-211-2: User, Aktor Assignment kedua: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-211-3: User, Approver Group: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-211-4: Assignment, Baris aktif Budi: satu Laptop dan dua Projector: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Acer Swift {runId}`, Baris 2 `Proyektor Epson EB {runId}`, Baris 3 `Proyektor BenQ MH {runId}`, Status baris `Assigned`, Category baris 1 `Laptop`, Category baris 2 `Projector`, Category baris 3 `Projector`.
  - DU-211-5: Aset, Dua Laptop dan satu Projector Available yang diajukan dalam satu form: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop HP ProBook {runId}`, Aset 2 `Laptop Lenovo IdeaPad {runId}`, Aset 3 `Proyektor Optoma HD {runId}`, Category aset 1 `Laptop`, Category aset 2 `Laptop`, Category aset 3 `Projector`, Require approval `OFF`.
  - DU-211-6: Aset, Satu Laptop dan satu Projector Available yang diajukan dalam satu form: Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Dell Inspiron {runId}`, Aset 2 `Proyektor Sony VPL {runId}`, Category aset 1 `Laptop`, Category aset 2 `Projector`, Require approval aset 1 `OFF`, Require approval aset 2 `ON`, Approver aset 2 `Mira Handayani {runId}`.
  - DU-211-7: Aset, Satu Laptop Available untuk Assignee tanpa baris aktif: Assignee `Fani Rahmawati {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Asus ExpertBook {runId}`, Category aset 1 `Laptop`, Require approval `OFF`.
  - DU-211-8: Assignment, Baris aktif Dewi: satu Laptop: Assignee `Dewi Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop MSI Modern {runId}`, Status baris `Assigned`, Category baris 1 `Laptop`.
  - DU-211-9: Aset, Dua Laptop Available yang diajukan dua Aktor berbeda untuk Dewi hampir bersamaan: Assignee `Dewi Lestari {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Toshiba Satellite {runId}`, Aset 2 `Laptop Acer Aspire {runId}`, Category aset 1 `Laptop`, Category aset 2 `Laptop`, Pengaju aset 1 `Rina Wijaya {runId}`, Pengaju aset 2 `Agus Pratama {runId}`, Require approval `OFF`.
  - DU-211-10: Assignment, Baris aktif Gilang melebihi batas efektif yang kini lebih kecil: Assignee `Gilang Pratama {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Dell Latitude A {runId}`, Baris 2 `Laptop Dell Latitude B {runId}`, Baris 3 `Laptop Dell Latitude C {runId}`, Status baris `Assigned`, Category baris `Laptop`, Batas efektif Category Laptop `2`.
  - DU-211-11: Aset, Satu Laptop Available yang diajukan untuk Gilang: Assignee `Gilang Pratama {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Dell Vostro {runId}`, Category aset 1 `Laptop`, Require approval `OFF`.
  - DU-211-12: Assignment, Baris aktif Hadi: empat Monitor pada Category dengan batas 0: Assignee `Hadi Susanto {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Monitor Dell P2422 {runId}`, Baris 2 `Monitor LG 24MK {runId}`, Baris 3 `Monitor Samsung S24 {runId}`, Baris 4 `Monitor HP E24 {runId}`, Status baris `Assigned`, Category baris `Monitor`, Batas efektif Category Monitor `0`.
  - DU-211-13: Aset, Dua Monitor Available yang diajukan untuk Hadi: Assignee `Hadi Susanto {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Monitor BenQ GW2480 {runId}`, Aset 2 `Monitor AOC 24B1 {runId}`, Category aset 1 `Monitor`, Category aset 2 `Monitor`, Require approval `OFF`.
  - DU-211-14: Draft, Draft A untuk Eka berisi dua Laptop: Assignee `Eka Saputra {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Zenbook A {runId}`, Aset 2 `Laptop Zenbook B {runId}`, Category aset `Laptop`, Require approval `OFF`.
  - DU-211-15: Draft, Draft B untuk Eka berisi satu Laptop yang sama dengan Draft A dan satu Laptop lain: Assignee `Eka Saputra {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Zenbook A {runId}`, Aset 2 `Laptop Zenbook C {runId}`, Category aset `Laptop`, Require approval `OFF`.
  - DU-211-16: Aset, Daftar Assignment Request satu aset lebih banyak dari Bulk Transaction Row Limit: Assignee `Indra Kusuma {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Kursi Ergonomis Ergotec {runId}`, Jumlah aset di form `Bulk Transaction Row Limit ditambah satu`, Require approval `OFF`.
  - DU-211-17: Aset, Daftar dari dua Group yang tiap Group di bawah batas tetapi total melebihi Bulk Transaction Row Limit: Assignee `Joko Susilo {runId}`, Tipe Assignee `Employee`, Group aset 1 `Head Office {runId}`, Group aset 2 `Branch Surabaya {runId}`, Jumlah aset per Group `kurang dari Bulk Transaction Row Limit`, Jumlah aset total `Bulk Transaction Row Limit ditambah satu`, Nama aset contoh Group 1 `Meja Rapat Olympic {runId}`, Nama aset contoh Group 2 `Lemari Arsip Brother {runId}`.
  - DU-211-18: Draft, Draft untuk Kiki dengan baris lebih banyak dari Bulk Transaction Row Limit: Assignee `Kiki Amelia {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Rak Gudang Besi {runId}`, Aset tambahan yang belum ada di Draft `Lemari Besi Alba {runId}`, Jumlah aset di Draft `Bulk Transaction Row Limit ditambah satu`.
  - DU-211-19: Assignment, ASG dengan daftar Unassign satu aset lebih banyak dari Bulk Transaction Row Limit: Assignee `Lutfi Hakim {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Sofa Informa {runId}`, Status baris `Assigned`, Jumlah aset di daftar `Bulk Transaction Row Limit ditambah satu`.
  - DU-211-20: Assignment, Baris aktif Yuliana: dua Laptop menunggu approval: Assignee `Yuliana Putri {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Fujitsu Lifebook A {runId}`, Baris 2 `Laptop Fujitsu Lifebook B {runId}`, Status baris `Waiting for Approval`, Category baris `Laptop`, Batas efektif Category Laptop `2`.
  - DU-211-21: Aset, Satu Laptop Available yang diajukan untuk Yuliana: Assignee `Yuliana Putri {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Axioo Hype {runId}`, Category aset 1 `Laptop`, Require approval `OFF`.
  - DU-211-22: Assignment, Baris Zainal: satu Laptop aktif dan tiga Laptop yang sudah selesai: Assignee `Zainal Arifin {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Advan Workplus {runId}`, Baris 2 `Laptop Zyrex M232 {runId}`, Baris 3 `Laptop Infinix Inbook {runId}`, Baris 4 `Laptop Realme Book {runId}`, Status baris 1 `Assigned`, Status baris 2 `Unassigned`, Status baris 3 `Rejected`, Status baris 4 `Canceled`, Category baris `Laptop`, Batas efektif Category Laptop `2`.
  - DU-211-23: Aset, Satu Laptop Available yang diajukan untuk Zainal: Assignee `Zainal Arifin {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Huawei Matebook {runId}`, Category aset 1 `Laptop`, Require approval `OFF`.
  - DU-211-24: Aset, Daftar dari dua Group yang tiap ASG hasil pecahan di bawah batas Category Laptop tetapi totalnya melebihi: Assignee `Nana Marlina {runId}` tanpa baris aktif, Tipe Assignee `Employee`, Aset 1 `Laptop Samsung Galaxy Book {runId}`, Aset 2 `Laptop Asus Zenbook Flip {runId}`, Aset 3 `Laptop LG Gram {runId}`, Group aset 1 `Head Office {runId}`, Group aset 2 `Head Office {runId}`, Group aset 3 `Branch Surabaya {runId}`, Category aset `Laptop`, Jumlah aset per Group `2 dan 1`, Jumlah aset total `3`, Batas efektif Category Laptop `2`, Require approval `OFF`.
  - DU-211-25: Assignment, Baris aktif Oki: dua Laptop pada batas Category Laptop: Assignee `Oki Firmansyah {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Laptop Vaio SX14 A {runId}`, Baris 2 `Laptop Vaio SX14 B {runId}`, Status baris `Assigned`, Category baris `Laptop`, Batas efektif Category Laptop `2`.
  - DU-211-26: Aset, Daftar Laptop satu aset lebih banyak dari Bulk Transaction Row Limit yang juga melebihi Max assets per assignee: Assignee `Oki Firmansyah {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Aset 1 `Laptop Vaio Z {runId}`, Category aset `Laptop`, Jumlah aset di form `Bulk Transaction Row Limit ditambah satu`, Require approval `OFF`.
  - DU-211-27: Assignment, ASG Waiting for Handover dengan daftar satu aset lebih banyak dari Bulk Transaction Row Limit, Need recipient confirmation Yes: Assignee `Putri Maharani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Meja Kerja Olympic {runId}`, Status baris `Waiting for Handover`, Jumlah aset di daftar `Bulk Transaction Row Limit ditambah satu`, Verifikasi scan `semua baris sudah diverifikasi`.
  - DU-211-28: Assignment, ASG Waiting for Handover dengan daftar satu aset lebih banyak dari Bulk Transaction Row Limit, Need recipient confirmation No: Assignee `Rudi Hermawan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kursi Kantor Chitose {runId}`, Status baris `Waiting for Handover`, Jumlah aset di daftar `Bulk Transaction Row Limit ditambah satu`, Verifikasi scan `semua baris sudah diverifikasi`.
  - DU-211-29: Assignment, ASG Waiting for Approval dengan daftar satu aset lebih banyak dari Bulk Transaction Row Limit: Assignee `Sari Dewanti {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Lemari Arsip Lion {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`, Jumlah aset di daftar `Bulk Transaction Row Limit ditambah satu`.
- Kondisi:
  - Max assets per assignee efektif untuk Category `Laptop` bernilai `2` dan untuk Category `Projector` mengikuti Company default `5`.
  - Max assets per assignee efektif untuk Category `Monitor` bernilai `0`.
  - Bulk Transaction Row Limit bernilai nilai platform yang sedang berlaku dan tidak diubah spec ini.

## Test Steps

### Pengajuan melebihi Max assets per assignee ditolak seluruhnya
1. Rina membuka form Assignment Request untuk Assignee `Budi Santoso {runId}` yang memegang `Laptop Acer Swift {runId}`, `Proyektor Epson EB {runId}`, dan `Proyektor BenQ MH {runId}` pada DU-211-4
2. Rina menambahkan `Laptop HP ProBook {runId}`, `Laptop Lenovo IdeaPad {runId}`, dan `Proyektor Optoma HD {runId}` ke form pada DU-211-5
3. Rina menekan `[Submit]`
4. Verifikasi baris Laptop ditolak dengan pesan `[Assignee] can hold up to [N] assets at a time.` untuk Assignee `Budi Santoso {runId}` dan N `2` karena 1 baris aktif ditambah 2 baris baru melebihi batas Category `Laptop`
5. Verifikasi baris `Proyektor Optoma HD {runId}` ditolak karena 3 baris aktif ditambah 3 baris baru melebihi Company default `5`, yang dihitung lintas Category
6. Verifikasi tidak ada ASG yang terbentuk dan ketiga aset tetap `Available`

### Pengajuan tepat di batas lolos dan hasilnya per baris
7. Rina membuka form Assignment Request untuk Assignee `Budi Santoso {runId}`
8. Rina menambahkan `Laptop Dell Inspiron {runId}` dan `Proyektor Sony VPL {runId}` ke form pada DU-211-6
9. Rina menekan `[Submit]`
10. Verifikasi baris `Laptop Dell Inspiron {runId}` lolos karena 1 baris aktif ditambah 1 baris baru sama dengan batas Category `Laptop` dan nilai Category tidak dijumlahkan dengan Company default
11. Verifikasi baris `Proyektor Sony VPL {runId}` lolos karena 3 baris aktif ditambah 2 baris baru sama dengan `5`
12. Verifikasi kedua aset berCustody `In Assignment Process` dan aturan efektif tiap baris tersimpan sebagai snapshot
13. Verifikasi baris `Laptop Dell Inspiron {runId}` yang Require approval OFF berstatus `Waiting for Handover` dengan Approval `Not required`
14. Verifikasi baris `Proyektor Sony VPL {runId}` yang Require approval ON berstatus `Waiting for Approval` dan masuk pengajuan approval ASG itu

### Pengajuan di bawah batas lolos
15. Rina mengajukan `Laptop Asus ExpertBook {runId}` untuk Assignee `Fani Rahmawati {runId}` pada DU-211-7
16. Verifikasi pengajuan lolos karena 0 baris aktif ditambah 1 baris baru di bawah batas Category `Laptop`

### Submit bersamaan untuk Assignee yang sama
17. Rina menekan `[Submit]` untuk `Laptop Toshiba Satellite {runId}` dan Agus menekan `[Submit]` untuk `Laptop Acer Aspire {runId}` bagi Assignee `Dewi Lestari {runId}` pada DU-211-8 dan DU-211-9 hampir bersamaan
18. Verifikasi Assignee `Dewi Lestari {runId}` memegang paling banyak `2` baris aktif Laptop dan hanya satu pengajuan yang dikomit
19. Verifikasi pengajuan yang kalah dihitung ulang terhadap jumlah baris aktif terbaru dan ditolak dengan pesan `[Assignee] can hold up to [N] assets at a time.` untuk Assignee `Dewi Lestari {runId}` dan N `2`

### Baris aktif lama di atas batas tidak terpengaruh
20. Rina mengajukan `Laptop Dell Vostro {runId}` untuk Assignee `Gilang Pratama {runId}` pada DU-211-10 dan DU-211-11
21. Verifikasi pengajuan ditolak karena jumlah baris aktif sudah melebihi batas efektif `2` dan ketiga baris Assigned milik `Gilang Pratama {runId}` tidak berubah

### Max assets per assignee bernilai 0 berarti tanpa batas
22. Rina mengajukan `Monitor BenQ GW2480 {runId}` dan `Monitor AOC 24B1 {runId}` untuk Assignee `Hadi Susanto {runId}` pada DU-211-12 dan DU-211-13
23. Verifikasi pengajuan lolos tanpa batas walau `Hadi Susanto {runId}` sudah memegang empat baris aktif Monitor, sehingga total 4 baris aktif ditambah 2 baris baru `6` melebihi Company default `5` yang tidak dipakai

### Draft tidak dihitung dan Draft menjadi ASG
24. Rina menyimpan Draft A untuk Assignee `Eka Saputra {runId}` berisi `Laptop Zenbook A {runId}` dan `Laptop Zenbook B {runId}` pada DU-211-14
25. Rina menyimpan Draft B untuk Assignee `Eka Saputra {runId}` berisi `Laptop Zenbook A {runId}` dan `Laptop Zenbook C {runId}` pada DU-211-15
26. Verifikasi kedua Draft tersimpan tanpa nomor ASG dan tanpa mengunci aset
27. Rina menekan `[Submit]` pada Draft A
28. Verifikasi Draft A menjadi ASG dengan nomor baru dan lolos walau Draft B memuat dua baris Laptop, karena baris Draft tidak dihitung terhadap batas
29. Verifikasi Draft B tetap tidak berubah dan masih memuat `Laptop Zenbook A {runId}`

### Bulk Transaction Row Limit pada Assignment Request
30. Rina menekan `[Submit]` pada form untuk Assignee `Indra Kusuma {runId}` yang berisi satu aset lebih banyak dari Bulk Transaction Row Limit pada DU-211-16
31. Verifikasi Submit ditolak karena jumlah aset melebihi Bulk Transaction Row Limit, dicek lebih dulu sebelum validasi lain
32. Verifikasi tidak ada ASG yang terbentuk dan tidak ada baris yang berubah
33. Rina mengirim Submit langsung ke server tanpa form dengan jumlah aset yang sama
34. Verifikasi server memvalidasi ulang jumlah aset dengan nilai Bulk Transaction Row Limit yang berlaku saat permintaan diterima dan menolaknya
35. Rina menekan `[Submit]` pada form untuk Assignee `Joko Susilo {runId}` yang berisi aset dari Group `Head Office {runId}` dan Group `Branch Surabaya {runId}` pada DU-211-17
36. Verifikasi Submit ditolak karena total aset dihitung sebelum dipecah per Group walau tiap Group di bawah batas

### Bulk Transaction Row Limit pada Unassign dan Draft
37. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Lutfi Hakim {runId}` dengan daftar yang berisi satu aset lebih banyak dari Bulk Transaction Row Limit pada DU-211-19
38. Verifikasi Unassign ditolak karena jumlah aset melebihi Bulk Transaction Row Limit dan baris `Sofa Informa {runId}` tetap `Assigned`
39. Rina menekan `[Save Draft]` untuk Assignee `Kiki Amelia {runId}` dengan baris yang lebih banyak dari Bulk Transaction Row Limit pada DU-211-18
40. Verifikasi Draft tersimpan dan batas baru dicek saat Submit
41. Rina menekan `[Submit]` pada Draft `Kiki Amelia {runId}`
42. Verifikasi Submit Draft itu ditolak karena batas dicek saat Submit
43. Rina menekan `Add to Assignment Draft` untuk aset `Lemari Besi Alba {runId}` pada Draft `Kiki Amelia {runId}`
44. Verifikasi aset ditambahkan ke Draft tanpa dibatasi Bulk Transaction Row Limit

### Baris menunggu approval dihitung dan baris selesai tidak dihitung
45. Rina mengajukan `Laptop Axioo Hype {runId}` untuk Assignee `Yuliana Putri {runId}` pada DU-211-20 dan DU-211-21
46. Verifikasi pengajuan ditolak dengan pesan `[Assignee] can hold up to [N] assets at a time.` untuk Assignee `Yuliana Putri {runId}` dan N `2` karena 2 baris `Waiting for Approval` dihitung sebagai baris aktif ditambah 1 baris baru melebihi batas Category `Laptop`
47. Rina mengajukan `Laptop Huawei Matebook {runId}` untuk Assignee `Zainal Arifin {runId}` pada DU-211-22 dan DU-211-23
48. Verifikasi pengajuan lolos karena hanya 1 baris `Assigned` yang dihitung ditambah 1 baris baru sama dengan batas Category `Laptop`, sedangkan baris `Unassigned`, `Rejected`, dan `Canceled` tidak dihitung

### Baris baru dihitung di seluruh pengajuan sebelum dipecah per Group
49. Rina mengajukan `Laptop Samsung Galaxy Book {runId}` dan `Laptop Asus Zenbook Flip {runId}` dari Group `Head Office {runId}` serta `Laptop LG Gram {runId}` dari Group `Branch Surabaya {runId}` dalam satu form untuk Assignee `Nana Marlina {runId}` pada DU-211-24
50. Verifikasi pengajuan ditolak dengan pesan `[Assignee] can hold up to [N] assets at a time.` untuk Assignee `Nana Marlina {runId}` dan N `2` karena baris baru di seluruh pengajuan dihitung walau tiap ASG hasil pecahan (2 aset dan 1 aset) tidak melebihi batas Category `Laptop`
51. Verifikasi tidak ada ASG yang terbentuk dan ketiga aset tetap `Available`

### Batas jumlah aset dicek sebelum validasi lain
52. Rina menekan `[Submit]` pada form untuk Assignee `Oki Firmansyah {runId}` yang berisi satu aset lebih banyak dari Bulk Transaction Row Limit dan seluruhnya Laptop, sehingga melebihi Max assets per assignee juga, pada DU-211-25 dan DU-211-26
53. Verifikasi Submit ditolak karena jumlah aset melebihi Bulk Transaction Row Limit tanpa baris yang ditandai ditolak karena Max assets per assignee
54. Verifikasi tidak ada ASG yang terbentuk dan tidak ada baris yang berubah

### Handover dan Review tidak dibatasi Bulk Transaction Row Limit
55. Rina menekan `[Request Confirmation]` pada Handover untuk ASG `Putri Maharani {runId}` pada DU-211-27
56. Verifikasi permintaan konfirmasi diterima walau jumlah aset melebihi Bulk Transaction Row Limit
57. Rina menekan `[Complete Handover]` pada Handover untuk ASG `Rudi Hermawan {runId}` pada DU-211-28
58. Verifikasi handover selesai walau jumlah aset melebihi Bulk Transaction Row Limit
59. Mira menyetujui ASG `Sari Dewanti {runId}` di Review pada DU-211-29
60. Verifikasi keputusan Review diterima walau jumlah aset melebihi Bulk Transaction Row Limit
