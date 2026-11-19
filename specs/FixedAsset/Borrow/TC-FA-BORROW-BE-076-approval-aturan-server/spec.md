---
id: TC-FA-BORROW-BE-076-approval-aturan-server
title: "Approval per aset: approver snapshot, mode Any one dan All, self-approval guard, fallback, dan keputusan sekaligus"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["BORROW-LOGIC-06a", "BORROW-LOGIC-06b", "BORROW-LOGIC-06c", "BORROW-LOGIC-06d", "BORROW-LOGIC-06e", "BORROW-LOGIC-06f", "BORROW-LOGIC-06g", "BORROW-LOGIC-06h", "BORROW-LOGIC-06i", "BORROW-LOGIC-06j", "BORROW-LOGIC-06k", "BORROW-LOGIC-06l", "BORROW-LOGIC-06m", "BORROW-LOGIC-06n", "BORROW-LOGIC-06o", "BORROW-LOGIC-06p", "BORROW-LOGIC-06q", "BORROW-LOGIC-07a", "BORROW-LOGIC-07b", "BORROW-LOGIC-07c", "BORROW-LOGIC-07d", "BORROW-LOGIC-07e", "BORROW-LOGIC-07f", "BORROW-LOGIC-07g", "BORROW-LOGIC-07h", "BORROW-LOGIC-07i", "BORROW-LOGIC-07j", "BORROW-LOGIC-07k", "BORROW-LOGIC-07l", "V-BRW-15", "EC-BRW-08", "EC-BRW-09", "EC-BRW-10", "EC-BRW-109", "EC-BRW-110", "EC-BRW-13", "EC-BRW-133", "EC-BRW-70", "F-BORROW-04.k1", "F-BORROW-04.k2", "F-BORROW-04.k3", "F-BORROW-04.k4", "F-BORROW-04.k5", "F-BORROW-04.k8", "§2.2#r2", "§9.2#b25", "§9.2#b27", "§9.2#b30", "§9.2#r34", "§9.2#r35", "§9.2#p25", "§9.2#p27", "§9.2#p28", "§9.2#r45", "§9.3#b2", "§10#r5"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-06a": 15
  "BORROW-LOGIC-06b": 12
  "BORROW-LOGIC-06c": [70, 71]
  "BORROW-LOGIC-06d": 13
  "BORROW-LOGIC-06e": 14
  "BORROW-LOGIC-06f": 22
  "BORROW-LOGIC-06g": 22
  "BORROW-LOGIC-06h": [72, 73]
  "BORROW-LOGIC-06i": 72
  "BORROW-LOGIC-06j": 71
  "BORROW-LOGIC-06k": 14
  "BORROW-LOGIC-06l": [16, 77]
  "BORROW-LOGIC-06m": [16, 17]
  "BORROW-LOGIC-06n": [42, 101, 104, 106]
  "BORROW-LOGIC-06o": 42
  "BORROW-LOGIC-06p": [44, 81, 82, 87, 88]
  "BORROW-LOGIC-06q": [45, 79]
  "BORROW-LOGIC-07a": 19
  "BORROW-LOGIC-07b": [52, 53]
  "BORROW-LOGIC-07c": [3, 52, 58]
  "BORROW-LOGIC-07d": 18
  "BORROW-LOGIC-07e": [26, 35]
  "BORROW-LOGIC-07f": 30
  "BORROW-LOGIC-07g": 28
  "BORROW-LOGIC-07h": 30
  "BORROW-LOGIC-07i": [27, 32]
  "BORROW-LOGIC-07j": 37
  "BORROW-LOGIC-07k": [2, 8, 10]
  "BORROW-LOGIC-07l": [6, 7]
  "V-BRW-15": [2, 6, 7]
  "EC-BRW-08": [52, 58]
  "EC-BRW-09": [2, 6, 7, 10]
  "EC-BRW-10": 55
  "EC-BRW-109": 74
  "EC-BRW-110": 75
  "EC-BRW-13": 62
  "EC-BRW-133": 72
  "EC-BRW-70": 67
  "F-BORROW-04.k1": [12, 13, 14]
  "F-BORROW-04.k2": [6, 55]
  "F-BORROW-04.k3": 52
  "F-BORROW-04.k4": [2, 4, 98]
  "F-BORROW-04.k5": [45, 46, 48, 79]
  "F-BORROW-04.k8": [62, 67]
  "§2.2#r2": 45
  "§9.2#b25": [49, 63, 68, 73, 83, 84, 89, 92]
  "§9.2#b27": [20, 77]
  "§9.2#b30": [44, 81, 82, 87, 88]
  "§9.2#r34": [26, 28, 35]
  "§9.2#r35": [27, 32, 37]
  "§9.2#p25": [38, 40, 94, 96]
  "§9.2#p27": [62, 67]
  "§9.2#p28": 24
  "§9.2#r45": [24, 38, 87]
  "§9.3#b2": [19, 47]
  "§10#r5": 99
---

# Approval per aset: approver snapshot, mode Any one dan All, self-approval guard, fallback, dan keputusan sekaligus

## Prerequisites
- Aktor: Aktor Borrow `Dian Permata {runId}`, Asset Admin dengan cakupan `Head Office {runId}` dan satu-satunya Total Control, sebagai pengaju.
  - Approver `Rina Wijaya {runId}`, `Sari Wulandari {runId}`, `Tono Prasetyo {runId}`, `Agus Salim {runId}`, dan `Bayu Nugroho {runId}` (pemegang Role Transaksi Approver pada `Head Office {runId}`), serta Group Manager `Gita Pramesti {runId}`, masing-masing hanya untuk keputusan atau pengamatan yang disebut di langkah.
  - `Dian Permata {runId}` sebagai Total Control juga menjadi aktor yang menonaktifkan Approver, mencabut penugasan Role Transaksi Approver, dan mengubah Approval type override Asset di langkah yang menyebut namanya.
  - Borrower `Wati Handayani {runId}` dan `Yoga Pratama {runId}` tidak memegang peran approval dan tidak memutuskan apa pun.
- Data:
  - DU-076-1: Group, Group asal aset dengan Group Manager Gita: Name `Head Office {runId}`, Group Manager `Gita Pramesti {runId}`.
  - DU-076-2: Group, Group turunan Head Office; approver diwarisi dari Group induk: Name `Head Office Gudang {runId}`, Group induk `Head Office {runId}`.
  - DU-076-3: Group, Group asal tanpa approver lain dan tanpa Group Manager lain: Name `Gudang Terpencil {runId}`, Approver `Dian Permata {runId}`, Group Manager `Dian Permata {runId}`.
  - DU-076-4: User, Borrower yang juga pemegang Role Transaksi Approver pada Group Head Office: Name `Budi Santoso {runId}`, Group `Head Office {runId}`, Role `Approver`, Status `Aktif`.
  - DU-076-5: User, Aktor Borrow pengaju, Asset Admin, dan Total Control: Name `Dian Permata {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`, Total Control `ya`.
  - DU-076-6: User, Pemegang Role Approver pada Group Head Office: Name `Rina Wijaya {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-7: User, Pemegang Role Approver pada Group Head Office: Name `Sari Wulandari {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-8: User, Pemegang Role Approver pada Group Head Office: Name `Tono Prasetyo {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-9: User, Pemegang Role Group Manager pada Group Head Office: Name `Gita Pramesti {runId}`, Role `Group Manager`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-10: User, Approver yang kemudian dinonaktifkan: Name `Agus Salim {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-11: Asset, Aset yang dipinjam: Name `Laptop Dell Latitude {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-12: Asset, Aset yang dipinjam: Name `Laptop HP ProBook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-13: Asset, Aset yang dipinjam: Name `Excavator Komatsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `All`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-14: Asset, Aset yang dipinjam: Name `Bulldozer Caterpillar {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `All`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-15: Asset, Aset yang dipinjam: Name `Genset Honda {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Tono Prasetyo {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-16: Asset, Aset yang dipinjam: Name `Projector Epson EB {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Auto-approve `sampai 3 hari`, Approver `Tono Prasetyo {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-17: Asset, Aset yang dipinjam: Name `Camera Canon EOS {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Auto-approve `sampai 3 hari`, Approver `Tono Prasetyo {runId}`, Approval type `Any one`, Category `Peralatan Kantor {runId}`.
  - DU-076-18: Asset, Aset yang dipinjam: Name `Forklift Toyota {runId}`, Group asal `Head Office Gudang {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `diwarisi dari Group induk: Tono Prasetyo {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-19: Asset, Aset yang dipinjam: Name `Mesin Bor Bosch {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Agus Salim {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-20: Asset, Aset yang dipinjam: Name `Printer HP LaserJet {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Budi Santoso {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-21: Asset, Aset yang dipinjam: Name `Scanner Epson {runId}`, Group asal `Gudang Terpencil {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Dian Permata {runId}`.
  - DU-076-22: Asset, Aset yang dipinjam: Name `Monitor Dell {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`, Status baris `Borrowed`, Category `Peralatan Kantor {runId}`, Override Asset `Max duration 10 Days`, Max extensions `2`, Auto-approve `tidak ada`.
  - DU-076-23: Asset, Aset yang dipinjam: Name `Monitor LG UltraWide {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`, Status baris `Borrowed`, Category `Peralatan Kantor {runId}`, Override Asset `Max duration 10 Days`, Max extensions `2`, Auto-approve `tidak ada`.
  - DU-076-24: Asset, Aset yang dipinjam: Name `Tablet Samsung {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-25: Asset, Aset yang dipinjam: Name `Speaker JBL {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-26: Asset, Aset yang dipinjam: Name `Kamera Sony {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-076-27: BRW, BRW awal Budi pertama dengan baris Monitor Dell Borrowed: Borrower `Budi Santoso {runId}`, Aset 1 `Monitor Dell {runId}`, Status 1 `Borrowed`, Duration 1 `5`, Unit 1 `Days`.
  - DU-076-28: BRW, BRW awal Budi kedua dengan baris Monitor LG UltraWide Borrowed: Borrower `Budi Santoso {runId}`, Aset 1 `Monitor LG UltraWide {runId}`, Status 1 `Borrowed`, Duration 1 `5`, Unit 1 `Days`.
  - DU-076-29: BRW, BRW awal dengan satu pengajuan Borrow dan dua pengajuan Extension yang semuanya sudah diputuskan Rina: Borrower `Budi Santoso {runId}`, Pengajuan 1 `Borrow` (Request Date `T0 − 12 hari, pukul 09:00`, Decided Date `T0 − 11 hari, pukul 10:00`), Pengajuan 2 `Extension` (Request Date `T0 − 8 hari, pukul 09:00`, Decided Date `T0 − 7 hari, pukul 10:00`), Pengajuan 3 `Extension` (Request Date `T0 − 4 hari, pukul 09:00`, Decided Date `T0 − 3 hari, pukul 10:00`), Approver `Rina Wijaya {runId}`, Keputusan `Approved`.
  - DU-076-30: BRW, BRW awal dengan dua aset, Aset 1 sudah diputuskan Sari dan Aset 2 belum diputuskan Rina, untuk melihat progres approval: Borrower `Budi Santoso {runId}`, Aset 1 `Laptop Asus Vivobook {runId}`, Keputusan Sari `Approved`, Approval Note Sari `Disetujui untuk proyek gudang`, Approve Duration Sari `3`, Aset 2 `Monitor Samsung Odyssey {runId}`, Keputusan Rina `belum diputuskan`.
  - DU-076-31: User, Borrower yang tidak memegang peran approval: Name `Wati Handayani {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-076-32: User, Borrower yang tidak memegang peran approval: Name `Yoga Pratama {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-076-33: User, Approver yang penugasan Role Transaksi Approver-nya kemudian dicabut: Name `Bayu Nugroho {runId}`, Role `Approver`, Cakupan `Head Office {runId}`, Status `Aktif`.
  - DU-076-34: User, Karyawan aktif tanpa akun login dengan PIC yang memegang Role Approver: Name `Hendra Kusuma {runId}`, Akun login `tidak ada`, PIC `Tono Prasetyo {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-076-35: Asset, Aset yang dipinjam: Name `Router Cisco {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-076-36: Asset, Aset yang dipinjam: Name `Switch Juniper {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Tono Prasetyo {runId}`.
  - DU-076-37: Asset, Aset yang dipinjam: Name `Firewall Fortinet {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-076-38: Asset, Aset yang dipinjam: Name `Access Point Ubiquiti {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Tono Prasetyo {runId}`.
  - DU-076-39: Asset, Aset yang dipinjam: Name `Server Dell PowerEdge {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-076-40: Asset, Aset yang dipinjam: Name `Rak Server APC {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-076-41: Asset, Aset yang dipinjam: Name `Kompresor Atlas {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `All`, Approver `Tono Prasetyo {runId}`.
  - DU-076-42: Asset, Aset yang dipinjam: Name `Mesin Cetak Heidelberg {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `All`, Approver `Budi Santoso {runId}, Dian Permata {runId}, dan Rina Wijaya {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-43: Asset, Aset yang dipinjam: Name `Mesin Gerinda Makita {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Bayu Nugroho {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-44: Asset, Aset yang dipinjam: Name `Lemari Arsip {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `Any one`, Approver `Tono Prasetyo {runId}`.
  - DU-076-45: Asset, Aset yang dipinjam: Name `Laptop Asus Vivobook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `In Borrow Process`, Require approval `ON`, Approval type `Any one`, Approver `Sari Wulandari {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-46: Asset, Aset yang dipinjam: Name `Monitor Samsung Odyssey {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `In Borrow Process`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-076-47: Category, Category aset yang diajukan Budi dengan batas Max assets per borrower sendiri: Name `Peralatan Kantor {runId}`, Max assets per borrower `20`.
  - DU-076-48: Asset, Aset mode All yang masih menunggu approver kedua sesudah approver pertama memutuskan: Name `Crane Tadano {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Approval type `All`, Approver `Rina Wijaya {runId} dan Sari Wulandari {runId}`.
- Kondisi:
  - Daftar approver tiap aset di entri data menjadi snapshot saat Submit.
  - Transaction timeout Company default berlaku sebagai nilai lingkungan.
  - Max assets per borrower Category `Peralatan Kantor {runId}` bernilai `20` (DU-076-47) dan menggantikan Company default untuk aset di Category itu; nilai itu cukup untuk seluruh baris aktif Borrower `Budi Santoso {runId}`.
  - `Dian Permata {runId}` adalah satu-satunya Total Control entitas aktor, dan Group Manager `Gudang Terpencil {runId}` adalah `Dian Permata {runId}`.

## Test Steps

### Self-approval guard dan fallback
1. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Printer HP LaserJet {runId}` dan `Mesin Cetak Heidelberg {runId}`
2. Verifikasi `Budi Santoso {runId}` dikeluarkan dari daftar approver aset `Printer HP LaserJet {runId}` karena Borrower, dan daftar yang kosong dirutekan ke fallback Group Manager `Gita Pramesti {runId}`
3. Verifikasi pengajuan atas aset `Printer HP LaserJet {runId}` memuat log node `Approval rerouted` oleh System dengan alasan `No eligible approver`
4. Verifikasi pada aset `Mesin Cetak Heidelberg {runId}` yang bermode All, `Dian Permata {runId}` sebagai pengaju dan `Budi Santoso {runId}` sebagai Borrower dikeluarkan dan tidak dihitung sebagai suara yang dibutuhkan sehingga hanya `Rina Wijaya {runId}` yang tersisa, dan satu orang tidak dihitung dua kali pada satu aset
5. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Scanner Epson {runId}`
6. Verifikasi Submit ditolak dengan `There is no eligible approver for [Asset Name]. Ask someone else to submit this borrow.` karena daftar approver dan seluruh fallback habis oleh self-approval guard
7. Verifikasi tidak ada BRW yang dibuat untuk aset `Scanner Epson {runId}`
8. Verifikasi pengaju `Dian Permata {runId}` dan Borrower dikeluarkan dari daftar approver tiap aset di transaksi itu
9. Aktor Borrow mengirim Submit untuk Borrower tanpa akun login `Hendra Kusuma {runId}` dengan aset `Lemari Arsip {runId}`
10. Verifikasi PIC Borrower `Tono Prasetyo {runId}` dikeluarkan dari daftar approver aset `Lemari Arsip {runId}`, dan daftar yang kosong dirutekan ke fallback Group Manager `Gita Pramesti {runId}`

### Pengajuan approval per Transaction ID dan aturan per aset
11. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Laptop Dell Latitude {runId}`, `Excavator Komatsu {runId}`, `Genset Honda {runId}`, `Projector Epson EB {runId}`, `Camera Canon EOS {runId}`, dan `Forklift Toyota {runId}`, Duration `2` Days untuk `Projector Epson EB {runId}` dan Duration `5` Days untuk aset lain, sehingga Submit itu menjadi dua BRW dengan Transaction ID berbeda: satu untuk Group `Head Office {runId}` dan satu untuk Group `Head Office Gudang {runId}` yang memuat `Forklift Toyota {runId}`
12. Verifikasi baris Waiting for Approval di BRW Group `Head Office {runId}` hasil Submit itu masuk satu pengajuan approval tipe `Borrow` per Transaction ID
13. Verifikasi ID pengajuan yang tampil adalah Transaction ID BRW itu
14. Verifikasi pengajuan di BRW Group `Head Office {runId}` tidak dipecah menurut himpunan approver atau Approval type walaupun aset di dalamnya punya Approval type `Any one`, `All`, dan satu approver
15. Verifikasi approval satu level tanpa rantai approval
16. Verifikasi baris `Projector Epson EB {runId}` berstatus `Waiting for Handover` dan dicatat Auto-approved beserta aturan dan versi setting karena Duration baris itu memenuhi Auto-approve
17. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Waiting for Approval` karena Duration baris itu melebihi batas Auto-approve, sehingga Auto-approve dinilai per baris
18. Verifikasi daftar approver di-snapshot per baris saat Submit
19. Verifikasi approver tiap baris adalah pemegang Role Transaksi `Approver` pada Group aset, dan baris `Forklift Toyota {runId}` di Group turunan `Head Office Gudang {runId}` memuat `Tono Prasetyo {runId}` dari Group ancestor
20. Verifikasi baris `Excavator Komatsu {runId}` yang nilai efektif Require approval-nya ON berstatus `Waiting for Approval` saat Submit, sehingga baris langsung `Waiting for Handover` tanpa approval hanya terjadi bila nilai efektif Require approval OFF

### Mode Any one, All, dan satu approver
21. Approver `Rina Wijaya {runId}` mengirim keputusan Approve hanya untuk aset `Laptop Dell Latitude {runId}` tanpa memutuskan aset `Excavator Komatsu {runId}` yang juga miliknya dalam pengajuan itu
22. Verifikasi keputusan sebagian ditolak karena seluruh aset milik approver diputuskan sekaligus dalam satu Submit
23. Approver `Rina Wijaya {runId}` mengirim keputusan Reject untuk aset `Laptop Dell Latitude {runId}` dan `Excavator Komatsu {runId}` dalam satu Submit tanpa Approval note
24. Verifikasi Reject ditolak dengan `Approval note must not be empty` karena Reject wajib disertai Approval note
25. Approver `Rina Wijaya {runId}` mengirim keputusan Approve untuk aset `Laptop Dell Latitude {runId}` dan `Excavator Komatsu {runId}` dalam satu Submit
26. Verifikasi aset `Laptop Dell Latitude {runId}` berstatus `Waiting for Handover` karena keputusan pertama Approve pada mode Any one
27. Verifikasi aset `Excavator Komatsu {runId}` tetap `Waiting for Approval` karena mode All butuh semua approver snapshot
28. Verifikasi aset `Laptop Dell Latitude {runId}` keluar dari Active approver `Sari Wulandari {runId}` dan tidak tercatat di Active maupun History-nya, tanpa notifikasi
29. Approver `Sari Wulandari {runId}` mengirim keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` atas aset `Laptop Dell Latitude {runId}` dan keputusan Approve atas aset `Excavator Komatsu {runId}` dalam satu Submit sesudah keputusan `Rina Wijaya {runId}` atas `Laptop Dell Latitude {runId}` masuk lebih dulu
30. Verifikasi keputusan itu ditolak dengan `You can no longer approve this request because it has already been done by another approver.` dan tidak tersimpan untuk `Laptop Dell Latitude {runId}` maupun `Excavator Komatsu {runId}`
31. Approver `Sari Wulandari {runId}` mengirim keputusan Approve untuk aset `Excavator Komatsu {runId}`
32. Verifikasi aset `Excavator Komatsu {runId}` berstatus `Waiting for Handover` karena semua approver snapshot menyetujui
33. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Laptop HP ProBook {runId}` dan `Bulldozer Caterpillar {runId}`
34. Approver `Sari Wulandari {runId}` mengirim keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` untuk aset `Laptop HP ProBook {runId}` lebih dulu, dan Approve untuk aset `Bulldozer Caterpillar {runId}`
35. Verifikasi aset `Laptop HP ProBook {runId}` berstatus `Rejected` karena keputusan pertama Reject pada mode Any one menolak aset itu
36. Approver `Rina Wijaya {runId}` mengirim keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` untuk aset `Bulldozer Caterpillar {runId}`
37. Verifikasi aset `Bulldozer Caterpillar {runId}` langsung berstatus `Rejected` karena satu penolakan pada mode All menolak aset itu
38. Verifikasi Reject melepas Custody aset `Bulldozer Caterpillar {runId}` dan tidak memengaruhi aset lain, dan baris yang ditolak dapat diajukan ulang sebagai BRW baru
39. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Bulldozer Caterpillar {runId}` yang sebelumnya ditolak
40. Verifikasi BRW baru terbentuk dengan Transaction ID berbeda dari BRW sebelumnya dan baris `Bulldozer Caterpillar {runId}` berstatus `Waiting for Approval`

### Keputusan per aset, Bulk, dan keterlihatan pengajuan
41. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Genset Honda {runId}` yang approver-nya `Tono Prasetyo {runId}`
42. Verifikasi keputusan ditolak karena approver hanya memutuskan aset yang approver-nya dia dan belum ia putuskan
43. Approver `Rina Wijaya {runId}` mengirim Bulk Approve atas aset `Genset Honda {runId}` dan `Camera Canon EOS {runId}` yang approver-nya `Tono Prasetyo {runId}`
44. Verifikasi Bulk Approve tidak menyimpan keputusan untuk aset yang bukan milik approver itu, sehingga `Genset Honda {runId}` dan `Camera Canon EOS {runId}` tetap `Waiting for Approval`
45. Verifikasi pengajuan muncul di Active bagi `Tono Prasetyo {runId}` karena ia approver dari paling sedikit satu aset yang belum ia putuskan
46. Verifikasi pengajuan tidak muncul di Active bagi `Agus Salim {runId}` yang bukan approver aset mana pun di dalamnya
47. Verifikasi Group Manager `Gita Pramesti {runId}` di luar daftar snapshot tidak dapat memutuskan aset sebelum pengajuan dirutekan ulang
48. Verifikasi aset milik approver lain tampil read-only `Not your approval`
49. Verifikasi status pengajuan di BRW Group `Head Office {runId}` tampil `Waiting` selama sebagian asetnya belum diputuskan

### Approver Reroute dan snapshot approver
50. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Mesin Bor Bosch {runId}`
51. `Dian Permata {runId}` menonaktifkan Approver `Agus Salim {runId}` saat pengajuan masih menunggu
52. Verifikasi pengajuan dirutekan ke Group Manager `Gita Pramesti {runId}` dengan log node `Approval rerouted` alasan `Approver removed`
53. Verifikasi snapshot approver tidak ditulis ulang dan keputusan pertama penerima fallback final
54. `Dian Permata {runId}` mengubah Approval type override Asset baris `Mesin Bor Bosch {runId}` dari Any one menjadi All saat pengajuan menunggu
55. Verifikasi aset `Mesin Bor Bosch {runId}` memakai snapshot saat Submit
56. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Mesin Gerinda Makita {runId}`
57. `Dian Permata {runId}` mencabut penugasan Role Transaksi `Approver` dari `Bayu Nugroho {runId}` saat pengajuan masih menunggu
58. Verifikasi pengajuan dirutekan ke Group Manager `Gita Pramesti {runId}` dengan log node `Approval rerouted` alasan `Approver removed`

### Pengajuan dibatalkan atau ditutup sistem saat Review terbuka
59. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Tablet Samsung {runId}`
60. Aktor Borrow membatalkan pengajuan `Borrow` atas `Tablet Samsung {runId}` saat Review approver `Rina Wijaya {runId}` terbuka
61. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Tablet Samsung {runId}`
62. Verifikasi keputusan ditolak dengan `This borrow was canceled by [Name].` dan tidak tersimpan
63. Verifikasi status pengajuan `Borrow` atas `Tablet Samsung {runId}` tampil `Canceled`
64. Aktor Borrow mengirim Submit untuk Borrower `Budi Santoso {runId}` dengan aset `Speaker JBL {runId}`
65. Waktu berlalu sampai Transaction timeout pengajuan `Borrow` atas `Speaker JBL {runId}` terlewati saat Review approver `Rina Wijaya {runId}` terbuka
66. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Speaker JBL {runId}`
67. Verifikasi keputusan `Rina Wijaya {runId}` atas aset `Speaker JBL {runId}` ditolak dengan `This borrow was canceled automatically ([Reason]).` dan tidak tersimpan
68. Verifikasi status pengajuan `Borrow` atas `Speaker JBL {runId}` tampil `Canceled` karena ditutup sistem

### History per pengajuan dan Extension per Submit Extend
69. Aktor Borrow mengirim Submit Extend untuk Borrower `Budi Santoso {runId}` atas aset `Monitor Dell {runId}` dan `Monitor LG UltraWide {runId}` dari dua BRW berbeda, masing-masing Extend by `2` Days dan Reason `Proyek belum selesai`
70. Verifikasi Submit Extend itu menghasilkan satu pengajuan tipe `Extension` per BRW
71. Verifikasi BRW milik DU-076-29 memuat dua pengajuan tipe `Extension` ber-Transaction ID sama yang dibedakan Request Date
72. Verifikasi History Approvals approver `Rina Wijaya {runId}` memuat tiga entri ber-Transaction ID sama milik BRW DU-076-29 dengan Type `Borrow`, `Extension`, dan `Extension`, dibedakan Request Date dan Decided Date, tidak digabung
73. Verifikasi hanya pengajuan yang sudah diputuskan approver itu yang masuk History
74. Verifikasi keputusan baru dari History untuk pengajuan yang sudah ditutup ditolak dan keputusan tiap aset tampil sebagai hasil
75. Verifikasi pada BRW milik DU-076-30, progres approval aset `Laptop Asus Vivobook {runId}` milik approver `Sari Wulandari {runId}` yang dibuka `Rina Wijaya {runId}` hanya memuat status dan waktu keputusan, tanpa Approval Note `Disetujui untuk proyek gudang` dan Approve Duration `3` approver lain

### Baris tanpa Require approval langsung Waiting for Handover
76. Aktor Borrow mengirim Submit untuk Borrower `Wati Handayani {runId}` dengan aset `Kamera Sony {runId}`, Duration `3` Days
77. Verifikasi baris `Kamera Sony {runId}` langsung berstatus `Waiting for Handover` tanpa menunggu approval dan dicatat Auto-approved beserta aturan dan versi setting karena Require approval aset itu OFF

### Bulk Approve atas pilihan campuran aset milik approver dan bukan miliknya
78. Aktor Borrow mengirim Submit untuk Borrower `Wati Handayani {runId}` dengan aset `Router Cisco {runId}` dan `Switch Juniper {runId}`, Duration `5` Days
79. Verifikasi pengajuan itu muncul di Active bagi `Rina Wijaya {runId}` dan `Tono Prasetyo {runId}` karena masing-masing approver dari satu aset di dalamnya yang belum ia putuskan
80. Approver `Rina Wijaya {runId}` mengirim Bulk Approve atas aset `Router Cisco {runId}` dan `Switch Juniper {runId}`
81. Verifikasi aset `Router Cisco {runId}` berstatus `Waiting for Handover` karena satu persetujuan berlaku untuk satu aset milik approver itu
82. Verifikasi aset `Switch Juniper {runId}` tetap `Waiting for Approval` karena Bulk Approve hanya berlaku untuk aset terpilih milik approver itu
83. Verifikasi pengajuan itu tampil di History Approvals `Rina Wijaya {runId}` dengan status `Approved`
84. Verifikasi pengajuan itu tidak tampil di History Approvals `Tono Prasetyo {runId}` karena ia belum memutuskan asetnya

### Bulk Reject atas pilihan campuran dengan Approval note
85. Aktor Borrow mengirim Submit untuk Borrower `Wati Handayani {runId}` dengan aset `Firewall Fortinet {runId}` dan `Access Point Ubiquiti {runId}`, Duration `5` Days
86. Approver `Rina Wijaya {runId}` mengirim Bulk Reject dengan Approval note `Tidak sesuai kebutuhan` atas aset `Firewall Fortinet {runId}` dan `Access Point Ubiquiti {runId}`
87. Verifikasi aset `Firewall Fortinet {runId}` berstatus `Rejected` dan Custody aset itu dilepas karena Reject berlaku untuk aset milik approver itu
88. Verifikasi aset `Access Point Ubiquiti {runId}` tetap `Waiting for Approval` karena Bulk Reject hanya berlaku untuk aset terpilih milik approver itu
89. Verifikasi pengajuan itu tampil di History Approvals `Rina Wijaya {runId}` dengan status `Rejected`

### Keputusan campuran Approve dan Reject menghasilkan status Partially Approved
90. Aktor Borrow mengirim Submit untuk Borrower `Yoga Pratama {runId}` dengan aset `Server Dell PowerEdge {runId}`, `Rak Server APC {runId}`, dan `Kompresor Atlas {runId}`, Duration `5` Days
91. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Server Dell PowerEdge {runId}` dan keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` atas aset `Rak Server APC {runId}` dalam satu Submit
92. Verifikasi pengajuan itu tampil di History Approvals `Rina Wijaya {runId}` dengan status `Partially Approved`

### Satu approver saja menentukan aset pada mode Any one dan All
93. Approver `Tono Prasetyo {runId}` mengirim keputusan Approve atas aset `Kompresor Atlas {runId}` yang bermode All dengan satu approver
94. Verifikasi aset `Kompresor Atlas {runId}` berstatus `Waiting for Handover` karena keputusan satu-satunya approver langsung menentukan aset pada mode All
95. Approver `Tono Prasetyo {runId}` mengirim keputusan Approve atas aset `Genset Honda {runId}` dan `Camera Canon EOS {runId}` dalam satu Submit
96. Verifikasi aset `Genset Honda {runId}` dan `Camera Canon EOS {runId}` berstatus `Waiting for Handover` karena keputusan satu-satunya approver langsung menentukan aset pada mode Any one

### Mode All dengan pengaju dan Borrower yang dikeluarkan, satu level approval
97. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Mesin Cetak Heidelberg {runId}` pada pengajuan dari Submit pertama spec ini
98. Verifikasi aset `Mesin Cetak Heidelberg {runId}` berstatus `Waiting for Handover` karena persetujuan `Rina Wijaya {runId}` memenuhi syarat Approved mode All tanpa suara pengaju dan Borrower
99. Verifikasi tidak ada level approver berikutnya dan tidak ada approver lain berstatus menunggu untuk aset `Mesin Cetak Heidelberg {runId}` sesudah keputusan itu

### Approver tidak memutuskan ulang aset yang sudah ia putuskan
100. Approver `Rina Wijaya {runId}` mengirim keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` atas aset `Laptop Dell Latitude {runId}` yang sudah ia putuskan Approve
101. Verifikasi keputusan itu ditolak karena approver hanya memutuskan aset yang belum ia putuskan, dan aset `Laptop Dell Latitude {runId}` tetap berstatus `Waiting for Handover`

### Approver tidak memutuskan ulang aset mode All yang masih menunggu approver lain
102. Aktor Borrow mengirim Submit untuk Borrower `Yoga Pratama {runId}` dengan aset `Crane Tadano {runId}`, Duration `5` Days
103. Approver `Rina Wijaya {runId}` mengirim keputusan Approve atas aset `Crane Tadano {runId}`
104. Verifikasi aset `Crane Tadano {runId}` tetap `Waiting for Approval` karena mode All masih menunggu `Sari Wulandari {runId}`
105. Approver `Rina Wijaya {runId}` mengirim keputusan Reject dengan Approval note `Tidak sesuai kebutuhan` atas aset `Crane Tadano {runId}` yang sudah ia putuskan Approve
106. Verifikasi keputusan itu ditolak karena approver hanya memutuskan aset yang belum ia putuskan, dan aset `Crane Tadano {runId}` tetap `Waiting for Approval` dengan keputusan Approve `Rina Wijaya {runId}` tidak berubah
