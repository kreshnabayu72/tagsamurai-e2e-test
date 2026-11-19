---
id: TC-FA-BORROW-BE-072-kelayakan-dan-submit
title: "Server mengevaluasi kelayakan tiap baris saat Submit, batas Max assets per borrower, dan menolak seluruh Submit bila satu baris gagal"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["BORROW-LOGIC-01a", "BORROW-LOGIC-01b", "BORROW-LOGIC-01c", "BORROW-LOGIC-01d", "BORROW-LOGIC-01e", "BORROW-LOGIC-01f", "BORROW-LOGIC-01g", "BORROW-LOGIC-01h", "BORROW-LOGIC-01i", "BORROW-LOGIC-01j", "BORROW-LOGIC-01k", "BORROW-LOGIC-01l", "BORROW-LOGIC-01m", "BORROW-LOGIC-03a", "BORROW-LOGIC-03b", "BORROW-LOGIC-03c", "BORROW-LOGIC-03d", "BORROW-LOGIC-03e", "BORROW-LOGIC-03f", "EC-BRW-02", "EC-BRW-03", "EC-BRW-04", "EC-BRW-05", "EC-BRW-06", "EC-BRW-07", "EC-BRW-100", "EC-BRW-101", "EC-BRW-102", "EC-BRW-112", "EC-BRW-113", "EC-BRW-118", "EC-BRW-119", "EC-BRW-120", "EC-BRW-126", "EC-BRW-131", "EC-BRW-176", "EC-BRW-35", "EC-BRW-45", "EC-BRW-47", "EC-BRW-48", "EC-BRW-49", "EC-BRW-50", "EC-BRW-51", "EC-BRW-53", "EC-BRW-54", "EC-BRW-78", "EC-BRW-98", "EC-BRW-99", "F-BORROW-03.k1", "F-BORROW-03.k2", "F-BORROW-03.k3", "F-BORROW-03.k4", "F-BORROW-03.k5", "F-BORROW-03.k6", "F-BORROW-03.k7", "F-BORROW-03.k8", "F-BORROW-03.k9", "§9.2#p9", "§9.2#b7", "§9.2#b8", "§9.2#b9", "§9.2#b11", "§9.2#b12", "§9.2#p19", "§9.2#b14", "§9.2#b15", "§9.2#p21", "§9.2#p22", "§9.2#b65", "§9.4.3#b4", "§9.5#r9", "§9.5#r13", "§9.5#r14", "§10#r1", "§10#r3", "§10#r7", "EB-ERR-4"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-01a": 71
  "BORROW-LOGIC-01b": 4
  "BORROW-LOGIC-01c": 72
  "BORROW-LOGIC-01d": 74
  "BORROW-LOGIC-01e": 69
  "BORROW-LOGIC-01f": [73, 77, 88]
  "BORROW-LOGIC-01g": 73
  "BORROW-LOGIC-01h": 89
  "BORROW-LOGIC-01i": 82
  "BORROW-LOGIC-01j": 93
  "BORROW-LOGIC-01k": 73
  "BORROW-LOGIC-01l": 90
  "BORROW-LOGIC-01m": 87
  "BORROW-LOGIC-03a": [20, 111]
  "BORROW-LOGIC-03b": 24
  "BORROW-LOGIC-03c": [13, 14]
  "BORROW-LOGIC-03d": 13
  "BORROW-LOGIC-03e": 20
  "BORROW-LOGIC-03f": 12
  "EC-BRW-02": [68, 76]
  "EC-BRW-03": [56, 57]
  "EC-BRW-04": [15, 105, 106]
  "EC-BRW-05": 43
  "EC-BRW-06": 68
  "EC-BRW-07": 75
  "EC-BRW-100": 6
  "EC-BRW-101": [2, 126]
  "EC-BRW-102": 10
  "EC-BRW-112": [19, 110, 111, 112]
  "EC-BRW-113": [26, 27]
  "EC-BRW-118": [30, 37, 39]
  "EC-BRW-119": 32
  "EC-BRW-120": 31
  "EC-BRW-126": [33, 34]
  "EC-BRW-131": [35, 114, 116]
  "EC-BRW-176": 70
  "EC-BRW-35": 24
  "EC-BRW-45": 75
  "EC-BRW-47": [17, 85]
  "EC-BRW-48": 17
  "EC-BRW-49": 17
  "EC-BRW-50": 16
  "EC-BRW-51": [18, 108]
  "EC-BRW-53": 63
  "EC-BRW-54": 73
  "EC-BRW-78": 65
  "EC-BRW-98": [102, 103]
  "EC-BRW-99": 4
  "F-BORROW-03.k1": [94, 95]
  "F-BORROW-03.k2": [12, 13]
  "F-BORROW-03.k3": [26, 43, 46, 51, 118]
  "F-BORROW-03.k4": [29, 34, 41]
  "F-BORROW-03.k5": [76, 77]
  "F-BORROW-03.k6": [66, 69, 83]
  "F-BORROW-03.k7": [4, 10]
  "F-BORROW-03.k8": [2, 126]
  "F-BORROW-03.k9": [56, 57]
  "§9.2#p9": [44, 118, 120, 122]
  "§9.2#b7": [46, 48, 120]
  "§9.2#b8": [43, 118]
  "§9.2#b9": [49, 119]
  "§9.2#b11": [78, 79, 80, 124]
  "§9.2#b12": [81, 124]
  "§9.2#p19": 4
  "§9.2#b14": 8
  "§9.2#b15": 6
  "§9.2#p21": [56, 58, 60]
  "§9.2#p22": 128
  "§9.2#b65": [51, 54]
  "§9.4.3#b4": 22
  "§9.5#r9": [4, 103]
  "§9.5#r13": 69
  "§9.5#r14": [66, 69, 99]
  "§10#r1": 22
  "§10#r3": 72
  "§10#r7": 15
  "EB-ERR-4": [5, 21]
---

# Server mengevaluasi kelayakan tiap baris saat Submit, batas Max assets per borrower, dan menolak seluruh Submit bila satu baris gagal

## Prerequisites
- Aktor: Aktor Borrow (Asset Admin) yang cakupannya meliputi `Head Office {runId}`, `Branch Surabaya {runId}`, dan `Branch Kosong {runId}`.
  - Aktor Borrow kedua `Rina Wijaya {runId}` (DU-072-13), Asset Admin dengan cakupan `Head Office {runId}`, hanya untuk Submit bersamaan.
  - Borrower `Gita Pramesti {runId}` (DU-072-9), hanya untuk Borrow Now atas dirinya sendiri.
- Data:
  - DU-072-1: Group, Group asal dengan Division: Name `Head Office {runId}`, Division `Operasional {runId}`.
  - DU-072-2: Group, Group asal dengan Division berbeda: Name `Branch Surabaya {runId}`, Division `Pemasaran {runId}`.
  - DU-072-3: Group, Group turunan dari Group Head Office: Name `Head Office Gudang {runId}`, Group induk `Head Office {runId}`, Division `Operasional {runId}`.
  - DU-072-4: Group, Group asal tanpa Division: Name `Branch Kosong {runId}`, Division `tanpa Division`.
  - DU-072-5: User, Borrower karyawan aktif dengan akun login: Name `Budi Santoso {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-6: User, Borrower karyawan aktif dengan akun login: Name `Sari Wulandari {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-7: User, Borrower karyawan aktif dengan akun login: Name `Dewi Anggraini {runId}`, Group `Head Office Gudang {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-8: User, Borrower karyawan aktif dengan akun login: Name `Tono Prasetyo {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-9: User, Borrower karyawan aktif dengan akun login: Name `Gita Pramesti {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-10: User, Borrower karyawan aktif dengan akun login: Name `Hendra Kusuma {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-11: User, Borrower karyawan aktif dengan akun login: Name `Bambang Setiawan {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-12: User, Borrower yang dinonaktifkan sesudah Draft atasnya disimpan: Name `Eko Nugroho {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Nonaktif`.
  - DU-072-13: User, Aktor Borrow kedua dengan cakupan Group Head Office: Name `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`.
  - DU-072-14: Asset, Aset yang dipinjam: Name `Laptop Dell Latitude {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`, Category `Peralatan Pelatihan {runId}`.
  - DU-072-15: Asset, Aset yang dipinjam: Name `Projector Epson EB {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Auto-approve `sampai 3 hari`, Category `Peralatan Pelatihan {runId}`.
  - DU-072-16: Asset, Aset yang dipinjam: Name `Camera Canon EOS {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Self service `ON`, Category `Peralatan Pelatihan {runId}`.
  - DU-072-17: Asset, Aset yang dipinjam: Name `Meeting Mic Set {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`, Category `Peralatan Pelatihan {runId}`.
  - DU-072-18: Asset, Aset yang dipinjam: Name `Excavator Komatsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Category `Peralatan Pelatihan {runId}`.
  - DU-072-19: Asset, Aset yang dipinjam: Name `Toyota Innova {runId}`, Group asal `Branch Surabaya {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`, Category `Peralatan Pelatihan {runId}`.
  - DU-072-20: Draft, Draft Borrow atas nama Budi yang memuat aset dari dua Group asal: Borrower `Budi Santoso {runId}`, Note `Peminjaman untuk kegiatan pelatihan`, Aset 1 `Laptop Dell Latitude {runId}`, Duration 1 `7`, Unit 1 `Days`, Purpose 1 `Training`, Aset 2 `Projector Epson EB {runId}`, Duration 2 `3`, Unit 2 `Days`, Purpose 2 `Training`, Aset 3 `Camera Canon EOS {runId}`, Duration 3 `3`, Unit 3 `Days`, Purpose 3 `Event`, Aset 4 `Meeting Mic Set {runId}`, Duration 4 `3`, Unit 4 `Hours`, Purpose 4 `Training`, Aset 5 `Excavator Komatsu {runId}`, Duration 5 `3`, Unit 5 `Days`, Purpose 5 `Event`, Aset 6 `Toyota Innova {runId}`, Duration 6 `5`, Unit 6 `Days`, Purpose 6 `Training`.
  - DU-072-21: Asset, Aset yang dipinjam: Name `Printer HP LaserJet {runId}`, Group asal `Head Office {runId}`, Condition `Damaged`, Custody `Available`, Allow Borrow efektif `Allow`.
  - DU-072-22: Asset, Aset yang dipinjam: Name `Scanner Epson {runId}`, Group asal `Head Office {runId}`, Condition `Damaged`, Custody `Available`, Status `Deleted`.
  - DU-072-23: Asset, Aset yang dipinjam: Name `Kamera Sony {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, TAG `perlu diganti`.
  - DU-072-24: Asset, Aset yang dipinjam: Name `Speaker JBL {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-25: Asset, Aset yang dipinjam: Name `Proyektor BenQ {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, TAG `perlu diganti`, Allow Borrow efektif `Deny`.
  - DU-072-26: Asset, Aset yang dipinjam: Name `Genset Honda {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Override Asset `Deny`, Allow Borrow efektif `Deny`.
  - DU-072-27: BRW, BRW awal Bambang yang memegang aset Kamera Sony: Borrower `Bambang Setiawan {runId}`, Aset `Kamera Sony {runId}`, Status baris `Waiting for Handover`, Custody aset `In Borrow Process`.
  - DU-072-28: BRW, BRW awal Budi yang memegang aset Speaker JBL: Borrower `Budi Santoso {runId}`, Aset `Speaker JBL {runId}`, Status baris `Waiting for Handover`, Custody aset `In Borrow Process`.
  - DU-072-29: Draft, Draft Budi yang disimpan sebelum kondisi aset berubah: Borrower `Budi Santoso {runId}`, Note `Peminjaman untuk survei lapangan`, Aset 1 `Laptop Dell Latitude {runId}`, Aset 2 `Printer HP LaserJet {runId}`, Aset 3 `Scanner Epson {runId}`, Aset 4 `Kamera Sony {runId}`, Aset 5 `Speaker JBL {runId}`, Aset 6 `Proyektor BenQ {runId}`, Aset 7 `Genset Honda {runId}`, Aset 8 `Dispenser Sanyo {runId}`, Duration `2`, Unit `Days`, Purpose `Survei`.
  - DU-072-30: Asset, Aset yang dipinjam: Name `Tablet Samsung {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-31: Draft, Draft atas nama Eko yang disimpan saat Eko masih aktif: Borrower `Eko Nugroho {runId}`, Aset 1 `Tablet Samsung {runId}`, Duration `2`, Unit `Days`, Purpose `Dinas luar`.
  - DU-072-32: Asset, Aset yang dipinjam: Name `Forklift Toyota {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Allowed borrower `Same Group only`.
  - DU-072-33: Asset, Aset yang dipinjam: Name `Bor Listrik Makita {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Allowed borrower `Same Division only`.
  - DU-072-34: Asset, Aset yang dipinjam: Name `Mesin Fotokopi Ricoh {runId}`, Group asal `Branch Surabaya {runId}`, Condition `Normal`, Custody `Available`, Allowed borrower `Same Division only`.
  - DU-072-35: Asset, Aset yang dipinjam: Name `Meja Rapat Oval {runId}`, Group asal `Branch Kosong {runId}`, Condition `Normal`, Custody `Available`, Allowed borrower `Same Division only`.
  - DU-072-36: Asset, Aset yang dipinjam: Name `Pompa Air Honda {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Allowed borrower `semua karyawan, dari override Asset`.
  - DU-072-37: Draft, Draft atas nama Dewi yang memuat lima aset dengan Allowed borrower berbeda: Borrower `Dewi Anggraini {runId}`, Aset 1 `Forklift Toyota {runId}`, Aset 2 `Bor Listrik Makita {runId}`, Aset 3 `Mesin Fotokopi Ricoh {runId}`, Aset 4 `Meja Rapat Oval {runId}`, Aset 5 `Pompa Air Honda {runId}`, Duration `2`, Unit `Days`, Purpose `Perawatan gudang`.
  - DU-072-38: Asset, Aset yang dipinjam: Name `Laptop Lenovo ThinkPad {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `In Borrow Process`, Category `Laptop {runId}`.
  - DU-072-39: Asset, Aset yang dipinjam: Name `Laptop HP ProBook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`, Category `Laptop {runId}`.
  - DU-072-40: Asset, Aset yang dipinjam: Name `Projector Optoma {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-41: Asset, Aset yang dipinjam: Name `Projector Sony {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-42: Asset, Aset yang dipinjam: Name `Laptop Asus Vivobook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-43: BRW, BRW awal Sari: dua Laptop dan satu Projector aktif, satu Projector Returned: Borrower `Sari Wulandari {runId}`, Aset 1 `Laptop Lenovo ThinkPad {runId}`, Status 1 `Waiting for Approval`, Aset 2 `Laptop HP ProBook {runId}`, Status 2 `Borrowed`, Aset 3 `Projector Optoma {runId}`, Status 3 `Borrowed`, Aset 4 `Projector Sony {runId}`, Status 4 `Returned`.
  - DU-072-44: Draft, Draft Sari yang memuat satu Laptop dan tidak dihitung sebagai baris aktif: Borrower `Sari Wulandari {runId}`, Aset 1 `Laptop Asus Vivobook {runId}`, Duration `2`, Unit `Days`, Purpose `Survei`.
  - DU-072-45: Category, Category Laptop dengan batas Max assets per borrower sendiri: Name `Laptop {runId}`, Max assets per borrower `2`.
  - DU-072-46: Asset, Aset yang dipinjam: Name `Laptop Acer Swift {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop {runId}`.
  - DU-072-47: Asset, Aset yang dipinjam: Name `Projector ViewSonic {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-48: Asset, Aset yang dipinjam: Name `Projector Hitachi {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-49: Asset, Aset yang dipinjam: Name `Projector Panasonic {runId}`, Group asal `Branch Surabaya {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-50: Asset, Aset yang dipinjam: Name `Laptop Toshiba {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Status baris `Overdue`.
  - DU-072-51: BRW, BRW awal Tono dengan satu baris Overdue: Borrower `Tono Prasetyo {runId}`, Aset `Laptop Toshiba {runId}`, Status baris `Overdue`.
  - DU-072-52: Asset, Aset yang dipinjam: Name `Tablet Lenovo {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-53: Asset, Aset yang dipinjam: Name `Mobil Avanza {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-54: Asset, Aset yang dipinjam: Name `Pompa Celup Shimizu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Max duration `5`, Unit `Days`.
  - DU-072-55: Asset, Aset yang dipinjam: Name `Monitor Dell {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-56: Asset, Aset yang dipinjam: Name `Kursi Ergonomis {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-57: Asset, Aset volume di Group Head Office, jumlah separuh Bulk Transaction Row Limit dibulatkan ke atas: Name `Aset Batas HO {n} {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Self service `ON`.
  - DU-072-58: Asset, Aset volume di Group Branch Surabaya, sisanya ditambah satu: Name `Aset Batas BS {n} {runId}`, Group asal `Branch Surabaya {runId}`, Condition `Normal`, Custody `Available`, Self service `ON`.
  - DU-072-59: Draft, Draft Gita berisi seluruh aset volume: Borrower `Gita Pramesti {runId}`, Aset `seluruh Aset Batas HO {n} {runId} dan seluruh Aset Batas BS {n} {runId}`, Duration `1`, Unit `Days`, Purpose `Inventarisasi`.
  - DU-072-60: Category, Category untuk aset pelatihan dengan batas Max assets per borrower sendiri: Name `Peralatan Pelatihan {runId}`, Max assets per borrower `10`.
  - DU-072-61: Asset, Aset yang dipinjam, Activity Lock aktif sejak Draft Budi disimpan: Name `Dispenser Sanyo {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Activity Lock `Under Maintenance`.
  - DU-072-62: User, Borrower karyawan aktif tanpa Division: Name `Fajar Ramadhan {runId}`, Group `Head Office {runId}`, Division `tanpa Division`, Status `Aktif`.
  - DU-072-63: Asset, Aset yang dipinjam dari Group ber-Division: Name `Mesin Bubut Krisbow {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Allowed borrower `Same Division only`.
  - DU-072-64: Asset, Aset yang dipinjam dengan Allow Borrow Deny dan batas Duration: Name `Genset Yanmar {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Allow Borrow efektif `Deny`, Max duration `5`, Unit `Days`.
  - DU-072-65: Asset, Aset yang dipinjam dengan Require approval ON dan Auto-approve: Name `Mesin Las Krisbow {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `ON`, Auto-approve `sampai 3 hari`.
  - DU-072-66: User, Borrower karyawan aktif dengan akun login: Name `Rudi Hartono {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-072-67: Asset, Aset yang dipinjam: Name `Laptop Fujitsu Lifebook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `In Borrow Process`, Category `Laptop {runId}`.
  - DU-072-68: Asset, Aset yang dipinjam: Name `Projector Philips {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`.
  - DU-072-69: Asset, Aset yang dipinjam: Name `Projector Acer {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`.
  - DU-072-70: BRW, BRW awal Rudi: satu Laptop Waiting for Handover dan dua Projector Borrowed: Borrower `Rudi Hartono {runId}`, Aset 1 `Laptop Fujitsu Lifebook {runId}`, Status 1 `Waiting for Handover`, Aset 2 `Projector Philips {runId}`, Status 2 `Borrowed`, Aset 3 `Projector Acer {runId}`, Status 3 `Borrowed`.
  - DU-072-71: Asset, Aset yang dipinjam: Name `Laptop MSI Modern {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop {runId}`.
  - DU-072-72: Asset, Aset yang dipinjam: Name `Laptop Gigabyte Aero {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop {runId}`.
  - DU-072-73: Asset, Aset yang dipinjam: Name `Projector LG {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
  - DU-072-74: Asset, Aset yang dipinjam: Name `Rak Arsip Lion {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`.
- Kondisi:
  - Bulk Transaction Row Limit berlaku sebagai nilai lingkungan yang lebih besar daripada Max assets per borrower Company default `5`; jumlah aset DU-072-57 ditambah DU-072-58 sama dengan batas itu ditambah satu, dan jumlah di masing-masing Group asal tidak melebihi batas.
  - Max assets per borrower Company default bernilai `5`; Category `Laptop {runId}` bernilai `2` (DU-072-45) dan Category `Peralatan Pelatihan {runId}` bernilai `10` (DU-072-60); nilai Category menggantikan Company default untuk aset di Category itu.
  - Block new borrow when overdue bernilai ON.
  - Sejak DU-072-29 disimpan: Condition `Printer HP LaserJet {runId}` berubah menjadi `Damaged`, `Scanner Epson {runId}` dihapus dan Condition-nya `Damaged`, `Kamera Sony {runId}` masuk BRW `Bambang Setiawan {runId}` (DU-072-27), TAG `Proyektor BenQ {runId}` berubah menjadi `perlu diganti`, dan `Dispenser Sanyo {runId}` (DU-072-61) berstatus Activity Lock `Under Maintenance`.
  - DU-072-12 dinonaktifkan sesudah DU-072-31 disimpan.
  - Time Zone penyewa dipakai untuk jam akhir Due date baris Days.
  - Pada kelompok terakhir, entitas aktor berstatus Suspended.

## Test Steps

### Jumlah aset melebihi Bulk Transaction Row Limit ditolak
1. Aktor Borrow menyimpan Draft atas nama `Gita Pramesti {runId}` berisi seluruh `Aset Batas HO {n} {runId}` dan seluruh `Aset Batas BS {n} {runId}`
2. Verifikasi Draft tersimpan walaupun jumlah barisnya melebihi Bulk Transaction Row Limit
3. Aktor Borrow mengirim Submit atas Draft atas nama `Gita Pramesti {runId}`
4. Verifikasi Submit ditolak karena jumlah aset melebihi Bulk Transaction Row Limit, tanpa ada baris yang diproses
5. Verifikasi tidak ada BRW atas nama `Gita Pramesti {runId}` dan Custody seluruh aset di Draft tetap `Available`
6. Verifikasi penolakan berlaku walaupun jumlah aset di tiap Group asal tidak melebihi batas, karena jumlah dihitung sebelum dipecah menjadi beberapa BRW
7. Borrower `Gita Pramesti {runId}` mengirim Borrow Now atas dirinya sendiri dengan seluruh `Aset Batas HO {n} {runId}` dan seluruh `Aset Batas BS {n} {runId}`
8. Verifikasi Borrow Now ditolak karena jumlah aset melebihi Bulk Transaction Row Limit
9. Aktor Borrow mengirim Submit atas Draft atas nama `Gita Pramesti {runId}` langsung ke server tanpa melalui form
10. Verifikasi server menolak Submit itu dengan nilai Bulk Transaction Row Limit yang berlaku saat request diterima

### Draft dengan baris tidak layak ditolak seluruhnya
11. Aktor Borrow mengirim Submit atas Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan`
12. Verifikasi Submit ditolak seluruhnya dan tidak ada BRW yang dibuat
13. Verifikasi semua baris bermasalah ditandai sekaligus dengan caption `This asset can no longer be borrowed.`
14. Verifikasi baris `Laptop Dell Latitude {runId}` yang layak tidak ditandai
15. Verifikasi baris `Printer HP LaserJet {runId}` ditandai dengan alasan `This asset is [Status] and can't be borrowed.` walaupun Allow Borrow efektif Allow
16. Verifikasi baris `Scanner Epson {runId}` ditandai dengan alasan `This asset has been deleted.` walaupun Condition aset itu `Damaged`
17. Verifikasi baris `Kamera Sony {runId}` ditandai dengan alasan `This asset is already in another transaction.` karena aset sudah diambil BRW lain sejak Draft disimpan, walaupun TAG aset itu perlu diganti
18. Verifikasi baris `Speaker JBL {runId}` ditandai dengan alasan `This asset is already in another transaction.` karena Borrower sudah meminjam aset yang sama di BRW lain
19. Verifikasi baris `Proyektor BenQ {runId}` yang gagal dua aturan sekaligus hanya memuat satu alasan, yaitu `This asset can't be borrowed until its TAG is replaced.`
20. Verifikasi baris `Genset Honda {runId}` yang gagal Deny pada override dan Allow Borrow efektif Deny hanya memuat satu alasan, yaitu `Can't be borrowed: this asset is not available for borrowing. Contact [Name] (Manage asset & TAG).`
21. Verifikasi Custody seluruh aset di Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan` tidak berubah oleh Submit yang ditolak
22. Verifikasi aset `Kamera Sony {runId}` hanya berada di BRW milik `Bambang Setiawan {runId}` dan tidak berada di dua BRW aktif
23. Aktor Borrow mengirim Submit atas Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan` langsung ke server tanpa melalui form
24. Verifikasi evaluasi server identik dengan Submit lewat form: Submit ditolak dan baris `Kamera Sony {runId}` ditandai dengan alasan `This asset is already in another transaction.`

### Borrower nonaktif ditolak
25. Aktor Borrow mengirim Submit atas Draft atas nama `Eko Nugroho {runId}`
26. Verifikasi Submit ditolak dengan `[Name] is no longer active. Pick another borrower.` pada field Borrower
27. Verifikasi baris aset `Tablet Samsung {runId}` di Draft atas nama `Eko Nugroho {runId}` tidak berubah dan Draft tetap tersimpan

### Allowed borrower dinilai per aset
28. Aktor Borrow mengirim Submit atas Draft atas nama `Dewi Anggraini {runId}`
29. Verifikasi Submit ditolak dan tidak ada BRW yang dibuat
30. Verifikasi hanya baris `Forklift Toyota {runId}`, `Mesin Fotokopi Ricoh {runId}`, dan `Meja Rapat Oval {runId}` yang ditandai, dan baris `Bor Listrik Makita {runId}` dan `Pompa Air Honda {runId}` tidak ditandai
31. Verifikasi baris `Pompa Air Honda {runId}` dinilai dengan aturan efektifnya sendiri dan lolos
32. Verifikasi baris `Forklift Toyota {runId}` tidak lolos karena Borrower berada di Group turunan dari Group asal aset dan Group turunan tidak dihitung, dengan pesan blokir `[Borrower] can't borrow assets from [Group].`
33. Verifikasi baris `Bor Listrik Makita {runId}` lolos karena Division Borrower sama dengan Division Group asal aset walaupun Group Borrower berbeda
34. Verifikasi baris `Mesin Fotokopi Ricoh {runId}` tidak lolos karena Division Borrower berbeda dengan Division Group asal aset
35. Verifikasi baris `Meja Rapat Oval {runId}` tidak lolos karena Group asal aset tidak punya Division
36. Aktor Borrow mengeluarkan baris `Forklift Toyota {runId}`, `Mesin Fotokopi Ricoh {runId}`, dan `Meja Rapat Oval {runId}` dari Draft atas nama `Dewi Anggraini {runId}`
37. Verifikasi baris `Bor Listrik Makita {runId}` dan `Pompa Air Honda {runId}` tidak berubah
38. Aktor Borrow mengirim Submit atas Draft atas nama `Dewi Anggraini {runId}`
39. Verifikasi Submit berhasil dan satu BRW tercipta atas nama `Dewi Anggraini {runId}`

### Duration melebihi Max duration aset ditolak
40. Aktor Borrow mengirim Submit untuk Borrower `Hendra Kusuma {runId}` dengan aset `Pompa Celup Shimizu {runId}`, Duration `9` Days
41. Verifikasi Submit ditolak karena Duration melebihi Max duration aset `5` Days

### Max assets per borrower dihitung dari nilai efektif
42. Aktor Borrow mengirim Submit untuk Borrower `Sari Wulandari {runId}` dengan aset `Laptop Acer Swift {runId}`
43. Verifikasi Submit ditolak dengan `[Name] can borrow up to [Max] assets at a time.` karena baris aktif Laptop `2` ditambah baris baru melebihi batas Category `Laptop {runId}`
44. Verifikasi baris `Laptop Acer Swift {runId}` dihitung terhadap nilai efektif Category `2` yang menggantikan Company default, bukan dijumlahkan dengannya
45. Aktor Borrow mengirim Submit untuk Borrower `Sari Wulandari {runId}` dengan aset `Projector ViewSonic {runId}`, `Projector Hitachi {runId}`, dan `Projector Panasonic {runId}`
46. Verifikasi Submit ditolak karena jumlah aset seluruh pengajuan, termasuk semua BRW hasil pecahan, ditambah seluruh baris aktif Borrower melebihi Company default `5`
47. Aktor Borrow mengirim Submit untuk Borrower `Sari Wulandari {runId}` dengan aset `Projector ViewSonic {runId}` dan `Projector Hitachi {runId}`
48. Verifikasi Submit berhasil karena seluruh baris aktif Borrower ditambah baris baru tepat sama dengan Company default `5`
49. Verifikasi baris berstatus `Returned` dan baris di Draft atas nama `Sari Wulandari {runId}` tidak dihitung sebagai baris aktif

### Block new borrow when overdue
50. Aktor Borrow mengirim Submit untuk Borrower `Tono Prasetyo {runId}` dengan aset `Tablet Lenovo {runId}`
51. Verifikasi Submit ditolak dengan `[Name] has an overdue borrow: [Asset Code], due [Date]. Return it first.`
52. Aktor Borrow menyelesaikan Return atas baris `Laptop Toshiba {runId}` milik Borrower `Tono Prasetyo {runId}`
53. Aktor Borrow mengirim Submit untuk Borrower `Tono Prasetyo {runId}` dengan aset `Tablet Lenovo {runId}`
54. Verifikasi Submit berhasil sesudah semua baris Overdue Borrower berstatus `Returned`

### Dua Submit bersamaan atas aset yang sama
55. Aktor Borrow dan Aktor Borrow kedua `Rina Wijaya {runId}` mengirim Submit bersamaan untuk Borrower `Hendra Kusuma {runId}` atas aset `Mobil Avanza {runId}`
56. Verifikasi tepat satu BRW aktif memuat aset `Mobil Avanza {runId}`
57. Verifikasi Submit yang tidak berhasil ditolak dengan `This asset is already in [BRW No.].`
58. Verifikasi Custody aset `Mobil Avanza {runId}` menjadi `In Borrow Process` bersamaan dengan status baris yang memegangnya
59. Aktor Borrow mengirim Report Damaged atas aset `Mobil Avanza {runId}`
60. Verifikasi Report Damaged ditolak karena aset masih `In Borrow Process` dan belum Handover

### Add to Borrow Draft idempoten dan membuat Draft baru bila perlu
61. Aktor Borrow menambahkan aset `Kursi Ergonomis {runId}` ke Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan` lewat Add to Borrow Draft
62. Aktor Borrow menambahkan aset `Kursi Ergonomis {runId}` sekali lagi ke Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan` lewat Add to Borrow Draft
63. Verifikasi Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan` memuat satu baris `Kursi Ergonomis {runId}` dan tidak digandakan
64. Aktor Borrow menambahkan aset `Kursi Ergonomis {runId}` ke Borrower `Hendra Kusuma {runId}` yang tidak punya Draft
65. Verifikasi Draft baru atas nama `Hendra Kusuma {runId}` dibuat otomatis tanpa Transaction ID

### Submit lolos menghasilkan BRW per Group dengan baris dan snapshot
66. Verifikasi Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk kegiatan pelatihan` tidak punya Transaction ID sebelum Submit
67. Aktor Borrow mengirim Submit atas Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk kegiatan pelatihan`
68. Verifikasi Submit berhasil dan menghasilkan satu BRW per Group asal, yaitu `Head Office {runId}` dan `Branch Surabaya {runId}`
69. Verifikasi tiap BRW mendapat Transaction ID baru berformat `BRW-YYYY-NNNN` pada saat Submit
70. Verifikasi aset dari kedua Group asal diterima tanpa penolakan satu Group dan Submit memecahnya per Group
71. Verifikasi BRW `Head Office {runId}` memuat satu header dan lima baris, satu baris per aset
72. Verifikasi header menyimpan Borrower `Budi Santoso {runId}`, Group asal `Head Office {runId}`, dan Note `Peminjaman untuk kegiatan pelatihan`, dengan Borrower tunggal untuk satu form
73. Verifikasi tiap baris menyimpan Duration dan Purpose sendiri: `Laptop Dell Latitude {runId}` Duration `7` Purpose `Training`, dan `Camera Canon EOS {runId}` Duration `3` Purpose `Event`, termasuk Duration `3` yang sama untuk `Projector Epson EB {runId}` dan `Camera Canon EOS {runId}` yang disamakan lewat bulk action
74. Verifikasi header tidak menyimpan Duration unit dan satuan `Days` atau `Hours` melekat pada tiap baris menurut aturan efektif asetnya
75. Verifikasi satu BRW `Head Office {runId}` memuat baris Days dan baris Hours, dan Duration, Due date, serta Overdue dihitung per baris menurut satuannya
76. Verifikasi Custody tiap baris menjadi `In Borrow Process`
77. Verifikasi aturan efektif tiap baris di-snapshot beserta versi setting, nilai efektif, daftar approver, dan Approval type
78. Verifikasi baris `Laptop Dell Latitude {runId}` dan `Meeting Mic Set {runId}` berstatus `Waiting for Handover` karena Require approval OFF
79. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Waiting for Handover` karena Self service ON, walaupun Require approval ON dan aset itu tidak punya batas Auto-approve
80. Verifikasi baris `Projector Epson EB {runId}` berstatus `Waiting for Handover` dan dicatat Auto-approved beserta aturan karena Duration baris itu tidak melebihi batas Auto-approve
81. Verifikasi baris `Excavator Komatsu {runId}` berstatus `Waiting for Approval` dan masuk pengajuan approval BRW itu
82. Verifikasi Due date semua baris bernilai `—` sebelum handover

### Draft lain yang memuat aset itu tidak diubah
83. Verifikasi baris `Laptop Dell Latitude {runId}` di Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan` tidak diubah oleh Submit yang berhasil
84. Aktor Borrow mengirim Submit atas Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan`
85. Verifikasi baris `Laptop Dell Latitude {runId}` ditandai dengan caption `This asset can no longer be borrowed.` dan alasan `This asset is already in another transaction.`

### Due date ditetapkan saat handover
86. Aktor Borrow menyelesaikan Handover baris `Laptop Dell Latitude {runId}` dan `Meeting Mic Set {runId}` dengan konfirmasi Borrower
87. Verifikasi kedua baris berstatus `Borrowed` dan Due date terisi
88. Verifikasi Handed Over At baris `Laptop Dell Latitude {runId}` terisi dengan waktu handover
89. Verifikasi Due date baris `Laptop Dell Latitude {runId}` adalah tanggal handover ditambah 6 hari, berakhir pukul 23:59:59 menurut Time Zone penyewa, dari Duration `7` Days
90. Verifikasi Due date baris `Meeting Mic Set {runId}` adalah jam handover ditambah 3 jam, dari Duration `3` Hours

### Status header dihitung ulang dari baris
91. Aktor Borrow membatalkan baris `Projector Epson EB {runId}` lewat Cancel Borrow per baris
92. Aktor Borrow membatalkan baris `Camera Canon EOS {runId}` lewat Cancel Borrow per baris
93. Verifikasi status header BRW `Head Office {runId}` dihitung ulang dari baris menjadi `Waiting for Approval` dan tidak diubah langsung
94. Verifikasi baris yang sudah selesai diabaikan dalam penentuan status header selama masih ada baris aktif
95. Verifikasi baris `Projector Epson EB {runId}` dan `Camera Canon EOS {runId}` tetap tampil dengan status `Canceled` di tabel Assets BRW itu

### Nomor BRW tidak dipakai ulang
96. Aktor Borrow mengirim Submit untuk Borrower `Hendra Kusuma {runId}` dengan aset `Monitor Dell {runId}`
97. Aktor Borrow membatalkan BRW hasil Submit itu
98. Aktor Borrow mengirim Submit untuk Borrower `Hendra Kusuma {runId}` dengan aset `Monitor Dell {runId}`
99. Verifikasi BRW baru mendapat Transaction ID berbeda dari BRW yang dibatalkan

### Batas tepat Bulk Transaction Row Limit lolos
100. Aktor Borrow mengeluarkan satu aset `Aset Batas BS {n} {runId}` dari Draft atas nama `Gita Pramesti {runId}`
101. Aktor Borrow mengirim Submit atas Draft atas nama `Gita Pramesti {runId}`
102. Verifikasi Submit tidak ditolak karena Bulk Transaction Row Limit

### Validasi lain tetap berjalan atas Submit yang lolos Bulk Transaction Row Limit
103. Verifikasi Submit atas Draft atas nama `Gita Pramesti {runId}` ditolak oleh validasi lain dengan `[Name] can borrow up to [Max] assets at a time.` karena jumlah aset melebihi Max assets per borrower Company default `5`

### Perubahan TAG dan Activity Lock sejak Draft disimpan ditandai
104. Aktor Borrow mengirim Submit atas Draft atas nama `Budi Santoso {runId}` dengan Note `Peminjaman untuk survei lapangan`
105. Verifikasi baris `Proyektor BenQ {runId}` ditandai dengan alasan `This asset can't be borrowed until its TAG is replaced.` karena TAG aset berubah sejak Draft disimpan
106. Verifikasi baris `Dispenser Sanyo {runId}` ditandai dengan alasan `This asset is [Status] and can't be borrowed.` karena Activity Lock aset berubah menjadi `Under Maintenance` sejak Draft disimpan

### Aset yang sudah dipinjam Borrower itu ditolak saat dipilih
107. Aktor Borrow memilih aset `Speaker JBL {runId}` untuk Borrower `Budi Santoso {runId}`
108. Verifikasi pemilihan ditolak dengan `[Name] already has this asset in [BRW No.]. Use Extend instead.` beserta tautan ke BRW yang memegang aset itu

### Baris tidak layak yang Duration-nya melebihi Max duration
109. Aktor Borrow mengirim Submit untuk Borrower `Hendra Kusuma {runId}` dengan aset `Genset Yanmar {runId}`, Duration `9` Days
110. Verifikasi baris `Genset Yanmar {runId}` ditandai dengan caption `This asset can no longer be borrowed.`
111. Verifikasi baris `Genset Yanmar {runId}` hanya memuat satu alasan, yaitu `Borrowing isn't allowed for [Category].`, karena Allow Borrow dievaluasi sebelum Limits
112. Verifikasi Duration `9` Days yang melebihi Max duration aset `5` Days tetap ditolak dengan error Duration `Max. [Limit] days` yang terpisah dari alasan baris

### Borrower atau Group asal tanpa Division ditolak untuk Same Division only
113. Aktor Borrow mengirim Submit untuk Borrower `Fajar Ramadhan {runId}` dengan aset `Mesin Bubut Krisbow {runId}`
114. Verifikasi Submit ditolak dengan pesan blokir `[Borrower] can't borrow assets from [Group].` karena Borrower tidak punya Division sedangkan Group asal aset punya Division
115. Aktor Borrow mengirim Submit untuk Borrower `Fajar Ramadhan {runId}` dengan aset `Meja Rapat Oval {runId}`
116. Verifikasi Submit ditolak dengan pesan blokir `[Borrower] can't borrow assets from [Group].` karena Borrower dan Group asal aset sama-sama tidak punya Division

### Pengajuan campuran dinilai per baris terhadap nilai efektifnya sendiri
117. Aktor Borrow mengirim Submit untuk Borrower `Rudi Hartono {runId}` dengan aset `Laptop MSI Modern {runId}`, `Laptop Gigabyte Aero {runId}`, dan `Projector LG {runId}`
118. Verifikasi Submit ditolak dengan `[Name] can borrow up to [Max] assets at a time.` karena baris Laptop dinilai terhadap Category `2`: `1` baris aktif Laptop ditambah `2` baris baru melebihi batas
119. Verifikasi baris `Laptop Fujitsu Lifebook {runId}` berstatus `Waiting for Handover` dihitung sebagai baris aktif
120. Verifikasi baris `Projector LG {runId}` dinilai terhadap Company default `5`: `3` baris aktif ditambah `3` baris baru melebihi batas
121. Aktor Borrow mengirim Submit untuk Borrower `Rudi Hartono {runId}` dengan aset `Laptop MSI Modern {runId}` dan `Projector LG {runId}`
122. Verifikasi Submit berhasil karena Laptop `1` ditambah `1` tidak melebihi Category `2` dan Projector `3` ditambah `2` tidak melebihi Company default `5`

### Auto-approve tidak terpenuhi bila Duration melebihi batas Auto-approve
123. Aktor Borrow mengirim Submit untuk Borrower `Dewi Anggraini {runId}` dengan aset `Mesin Las Krisbow {runId}`, Duration `5` Days
124. Verifikasi baris `Mesin Las Krisbow {runId}` berstatus `Waiting for Approval` dan masuk pengajuan approval BRW itu karena Duration `5` Days melebihi batas Auto-approve aset `sampai 3 hari`

### Add to Borrow Draft melewati Bulk Transaction Row Limit tetap tersimpan
125. Aktor Borrow menambahkan aset `Rak Arsip Lion {runId}` ke Draft atas nama `Gita Pramesti {runId}` lewat Add to Borrow Draft sehingga jumlah barisnya melebihi Bulk Transaction Row Limit
126. Verifikasi aset `Rak Arsip Lion {runId}` tersimpan di Draft atas nama `Gita Pramesti {runId}` walaupun jumlah barisnya melebihi Bulk Transaction Row Limit

### Aksi tulis ditolak saat entitas Suspended
127. Aktor Borrow mengirim Submit atas Draft atas nama `Hendra Kusuma {runId}`
128. Verifikasi Submit ditolak karena semua aksi tulis Aktor ditolak server pada entitas Suspended
