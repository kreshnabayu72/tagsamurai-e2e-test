---
id: TC-FA-FATR-BE-098-approval-borrow-dep-borrow
title: "Approval dan penentuan approver pada transaksi Borrow"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r83", "§4.1#r95", "§4.1#r200", "§4.1#r202", "§4.1#r203", "§4.1#r204", "§4.1#r205", "§9.2#b379", "§9.2#b380", "§9.2#b381", "§9.2#b440", "§9.2#b442", "§9.2#b443", "§9.2#b444", "§9.2#b447", "§9.2#b448", "§9.2#b449", "§9.2#b450", "§9.2#b452", "§9.2#b454", "§9.2#b455", "§9.2#b456", "§9.2#b457", "§9.2#b459", "§9.2#b460", "§9.2#b463", "§9.2#b464", "§9.2#b465", "§9.2#b467", "§9.2#b468", "§9.2#b469", "§9.2#b470", "§9.2#b471", "§9.2#b474", "§9.2#b475", "§9.2#b476", "§9.2#b487", "§9.2#b488", "§9.2#b489", "§9.2#b490", "§9.2#b491", "§9.2#b492", "§9.2#b493", "§9.2#b462", "§9.2#b472", "§9.2#b478", "§9.2#b479", "§9.2#b482", "§9.2#b480", "§9.2#b481", "§9.2#b495", "§9.2#b496", "§9.2#b497", "§9.2#b498", "§9.2#b501", "§9.2#b503", "§9.2#b533", "§9.2#b534", "§9.2#b536", "§9.2#b537", "§9.2#b539", "§9.2#b540", "§9.2#b548", "§9.2#b549", "§9.2#b550", "§9.2#b551", "§9.2#b552", "§9.2#b554", "§9.4.1#r20", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r42", "§9.4.2#r62", "§9.4.2#r138", "§9.4.2#r139", "§9.4.2#r156", "§9.4.2#r157", "§9.4.2#r158", "§9.4.2#r160", "§9.4.3#b4", "§9.4.4#r11", "§9.4.4#r48", "§9.4.4#r49", "§9.4.4#r50", "§9.4.4#r53", "§9.8#r1", "§9.8#r3", "§9.8#r10", "§9.8#r11", "§9.8#r12", "§9.10.1#p10", "§10#b1", "§4.1#r189", "§4.1#r99", "§9.2#r11", "§9.4.2#r19"]
smoke: []
dependsOn:
  - "Borrow: pengajuan, Extension, dan Return"
trace:
  "§Aturan Logika Modul#r83": [80]
  "§4.1#r95": [110, 115]
  "§4.1#r200": [124]
  "§4.1#r202": [2, 96]
  "§4.1#r203": [5]
  "§4.1#r204": [9, 11]
  "§4.1#r205": [6, 11, 13, 16, 17, 145, 146]
  "§9.2#b379": [99, 101, 102, 127, 129, 130, 158, 159, 162, 163, 166, 167]
  "§9.2#b380": [2]
  "§9.2#b381": [3]
  "§9.2#b440": [5]
  "§9.2#b442": [7]
  "§9.2#b443": [2]
  "§9.2#b444": [139]
  "§9.2#b447": [3, 29]
  "§9.2#b448": [29]
  "§9.2#b449": [31]
  "§9.2#b450": [24, 27]
  "§9.2#b452": [34, 40, 149]
  "§9.2#b454": [5]
  "§9.2#b455": [5, 20]
  "§9.2#b456": [9, 13]
  "§9.2#b457": [6, 16, 17, 145, 146]
  "§9.2#b459": [65]
  "§9.2#b460": [65, 70]
  "§9.2#b463": [74]
  "§9.2#b464": [76]
  "§9.2#b465": [68, 72, 74]
  "§9.2#b467": [85, 89]
  "§9.2#b468": [85, 87]
  "§9.2#b469": [82]
  "§9.2#b470": [83]
  "§9.2#b471": [87, 91]
  "§9.2#b474": [40]
  "§9.2#b475": [41]
  "§9.2#b476": [43]
  "§9.2#b487": [40, 151]
  "§9.2#b488": [55, 56, 169, 170]
  "§9.2#b489": [45, 58, 61]
  "§9.2#b490": [45, 154, 155]
  "§9.2#b491": [61, 63]
  "§9.2#b492": [38]
  "§9.2#b493": [34]
  "§9.2#b462": [66, 71]
  "§9.2#b472": [93]
  "§9.2#b478": [43]
  "§9.2#b479": [51]
  "§9.2#b482": [53]
  "§9.2#b480": [43, 48]
  "§9.2#b481": [48]
  "§9.2#b495": [104, 108]
  "§9.2#b496": [104, 106, 108, 112, 132, 134]
  "§9.2#b497": [117, 119]
  "§9.2#b498": [104]
  "§9.2#b501": [66, 71, 74, 83, 121]
  "§9.2#b503": [122]
  "§9.2#b533": [5]
  "§9.2#b534": [6, 13]
  "§9.2#b536": [82]
  "§9.2#b537": [82]
  "§9.2#b539": [40]
  "§9.2#b540": [43]
  "§9.2#b548": [65, 70]
  "§9.2#b549": [65, 70]
  "§9.2#b550": [71]
  "§9.2#b551": [66]
  "§9.2#b552": [67]
  "§9.2#b554": [76]
  "§9.4.1#r20": [85, 89]
  "§9.4.2#r37": [78, 79]
  "§9.4.2#r40": [82, 85]
  "§9.4.2#r42": [20, 21, 22]
  "§9.4.2#r62": [66, 71, 74, 83, 121, 122]
  "§9.4.2#r138": [40]
  "§9.4.2#r139": [41]
  "§9.4.2#r156": [65, 70]
  "§9.4.2#r157": [66, 71]
  "§9.4.2#r158": [67]
  "§9.4.2#r160": [76]
  "§9.4.3#b4": [85, 89]
  "§9.4.4#r11": [41, 42]
  "§9.4.4#r48": [20]
  "§9.4.4#r49": [83]
  "§9.4.4#r50": [41, 42]
  "§9.4.4#r53": [65]
  "§9.8#r1": [139, 140]
  "§9.8#r3": [141, 142]
  "§9.8#r10": [83, 84]
  "§9.8#r11": [66, 67]
  "§9.8#r12": [41, 42]
  "§9.10.1#p10": [78, 79]
  "§10#b1": [7]
  "§4.1#r189": [122]
  "§4.1#r99": [117, 119]
  "§9.2#r11": [40, 55, 56]
  "§9.4.2#r19": [40, 55]
owner: BE
---

# Approval dan penentuan approver pada transaksi Borrow

## Prerequisites
- Aktor: Rina Wulandari {runId} (Total Control) mengubah setting dan mengajukan; Hana Pertiwi {runId} (Aktor Borrow) mengajukan atas nama Borrower; Rudi Hartono {runId}, Rani Kusuma {runId}, Sari Handayani {runId}, Sinta Maharani {runId}, dan Wawan Setiawan {runId} (Approver Borrow) memutuskan; Gani Prakoso {runId}, Gina Anggraeni {runId}, Gino Wibowo {runId}, Gita Rahayu {runId}, dan Gerry Kusuma {runId} (Group Manager) memutuskan; Tomi Arsyad {runId} (Total Control) termasuk approver fallback; Rudi Hartono {runId} dan Sari Handayani {runId} juga berperan Aktor Borrow dan mengajukan atas nama Borrower; Borrower sesuai entri data.
- Data:
  - DU-098-1: Group, Group `Gudang Induk {runId}`; Group induk.
  - DU-098-2: Group, Group `Gudang Anak {runId}`, Group induk `Gudang Induk {runId}`; Group turunan dari Gudang Induk.
  - DU-098-3: Group, Group `Gudang Tanpa Approver {runId}`; Group tanpa Role Transaksi Approver, ada satu Group Manager.
  - DU-098-4: Group, Group `Gudang Dua Manager {runId}`; Group tanpa Approver, ada dua Group Manager.
  - DU-098-5: Group, Group `Gudang Tanpa Manager {runId}`; Group tanpa Approver dan tanpa Group Manager.
  - DU-098-6: Group, Group `Gudang Satu Approver {runId}`; Group dengan satu Approver.
  - DU-098-7: Group, Group `Gudang Satu Approver B {runId}`; Group dengan satu Approver kedua.
  - DU-098-8: Group, Group `Gudang Gani {runId}`; Group yang Approver dan Group Manager-nya orang yang sama.
  - DU-098-9: Group, Group `Gudang Wawan {runId}`; Group dengan dua Approver, salah satunya Borrower.
  - DU-098-10: Category, Category `Alat Berat {runId}`, TAG Type `RFID`; Category aset yang dipinjam.
  - DU-098-11: User, Nama `Rina Wulandari {runId}`, Peran `Total Control`; Total Control, pengaju dan pemutus approval.
  - DU-098-12: User, Nama `Hana Pertiwi {runId}`, Peran `Aktor Borrow`, Group `Gudang Induk {runId} beserta descendant, Gudang Tanpa Approver {runId}, Gudang Tanpa Manager {runId}, Gudang Dua Manager {runId} beserta descendant, Gudang Wawan {runId}, Gudang Satu Approver B {runId}, dan Gudang GM Nonaktif {runId}`; Aktor Borrow yang mengajukan atas nama Borrower.
  - DU-098-13: User, Nama `Rudi Hartono {runId}`, Peran `Aktor Borrow dan Approver Borrow`, Group `Gudang Induk {runId} beserta descendant`, Status `Active`; Approver eligible, juga mengajukan Borrow atas nama Borrower.
  - DU-098-14: User, Nama `Rani Kusuma {runId}`, Peran `Approver Borrow`, Group `Gudang Induk {runId} beserta descendant`, Status `Active`; Approver eligible kedua.
  - DU-098-15: User, Nama `Ina Sulastri {runId}`, Peran `Approver Borrow`, Group `Gudang Induk {runId} beserta descendant`, Status `Inactive`; Approver yang tidak eligible karena Inactive.
  - DU-098-16: User, Nama `Rio Saputra {runId}`, Peran `Approver Borrow`, Group `Gudang Induk {runId} beserta descendant`, Status `Active`, Akses `Read Only`; Approver yang tidak eligible karena Read Only.
  - DU-098-17: User, Nama `Lia Permata {runId}`, Peran `Approver Borrow`, Group `Gudang Induk {runId} beserta descendant`, Status `Active`, Lisensi `tanpa lisensi addon`; Approver yang tidak eligible karena tanpa lisensi addon.
  - DU-098-18: User, Nama `Gani Prakoso {runId}`, Peran `Group Manager`, Group `Gudang Induk {runId} dan Gudang Gani {runId}`; Group Manager yang menaungi Gudang Induk dan Gudang Gani, juga Approver di Gudang Gani.
  - DU-098-19: User, Nama `Gina Anggraeni {runId}`, Peran `Group Manager`, Group `Gudang Tanpa Approver {runId}`; Group Manager Gudang Tanpa Approver.
  - DU-098-20: User, Nama `Gino Wibowo {runId}`, Peran `Group Manager`, Group `Gudang Dua Manager {runId}`; Group Manager pertama Gudang Dua Manager.
  - DU-098-21: User, Nama `Gita Rahayu {runId}`, Peran `Group Manager`, Group `Gudang Dua Manager {runId}`; Group Manager kedua Gudang Dua Manager.
  - DU-098-22: User, Nama `Sari Handayani {runId}`, Peran `Aktor Borrow dan Approver Borrow`, Group `Gudang Satu Approver {runId}`, Status `Active`; Satu-satunya Approver Gudang Satu Approver, juga mengajukan Borrow atas nama Borrower.
  - DU-098-23: User, Nama `Sinta Maharani {runId}`, Peran `Approver Borrow`, Group `Gudang Satu Approver B {runId}`, Status `Active`; Satu-satunya Approver Gudang Satu Approver B.
  - DU-098-24: User, Nama `Wawan Setiawan {runId}`, Peran `Approver Borrow`, Group `Gudang Wawan {runId}`, Status `Active`; Approver sekaligus Borrower.
  - DU-098-25: User, Nama `Bima Nugraha {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-26: User, Nama `Citra Dewi {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-27: User, Nama `Dedi Kurniawan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-28: User, Nama `Eka Putri {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-29: User, Nama `Fitri Amelia {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-30: User, Nama `Gilang Ramadhan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-31: User, Nama `Hendra Gunawan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-32: User, Nama `Indah Permatasari {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-33: User, Nama `Joko Widodo {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-34: User, Nama `Kirana Larasati {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-35: User, Nama `Lukman Hakim {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-36: User, Nama `Mira Oktaviani {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-37: Asset, Asset `Pompa Beton Schwing {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan Approval type Any one approver.
  - DU-098-38: Asset, Asset `Mixer Truck Scania {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Approval type All approvers (AND).
  - DU-098-39: Asset, Asset `Crane Tower Potain {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Approval type All approvers (AND) untuk Reject.
  - DU-098-40: Asset, Asset `Hoist Konstruksi Alimak {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset untuk keputusan bersamaan.
  - DU-098-41: Asset, Asset `Genset Perkins 100kVA {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Approval type All approvers (AND) dan Approver tidak eligible.
  - DU-098-42: Asset, Asset `Bulldozer Komatsu D65 {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Anak {runId}`, Status `Available`; aset di Group turunan.
  - DU-098-43: Asset, Asset `Wheel Loader Caterpillar {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Approval type All approvers (AND), keputusan Group Manager.
  - DU-098-44: Asset, Asset `Excavator Sany SY215 {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Approval type All approvers (AND), Group Manager tidak dihitung.
  - DU-098-45: Asset, Asset `Compactor Dynapac {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Tanpa Approver {runId}`, Status `Available`; aset di Group tanpa Approver.
  - DU-098-46: Asset, Asset `Backhoe Loader Case {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Tanpa Approver {runId}`, Status `Available`; aset kedua di Group tanpa Approver.
  - DU-098-47: Asset, Asset `Roller Hamm {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Dua Manager {runId}`, Status `Available`; aset dengan override Approval type All approvers (AND) di Group dua Group Manager.
  - DU-098-48: Asset, Asset `Motor Grader Volvo {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Tanpa Manager {runId}`, Status `Available`; aset di Group tanpa Approver dan tanpa Group Manager.
  - DU-098-49: Asset, Asset `Dump Truck Mitsubishi {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset yang diajukan Total Control.
  - DU-098-50: Asset, Asset `Forklift Komatsu {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Anak {runId}`, Status `Available`; aset yang diajukan Group Manager Group induk.
  - DU-098-51: Asset, Asset `Scissor Lift Skyjack {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Require approval OFF.
  - DU-098-52: Asset, Asset `Telehandler JLG {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Satu Approver {runId}`, Status `Available`; aset di Group dengan satu Approver.
  - DU-098-53: Asset, Asset `Skid Steer Bobcat {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset yang diajukan Approver.
  - DU-098-54: Asset, Asset `Tower Light Generac {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Wawan {runId}`, Status `Available`; aset yang Borrower-nya juga Approver.
  - DU-098-55: Asset, Asset `Concrete Vibrator Wacker {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Gani {runId}`, Status `Available`; aset di Group yang Approver dan Group Manager-nya sama.
  - DU-098-56: Asset, Asset `Welding Machine Lincoln {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Satu Approver B {runId}`, Status `Available`; aset dengan override Approval type All approvers (AND), satu Approver.
  - DU-098-57: Asset, Asset `Paver Vogele {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset untuk Auto-approve batas inklusif.
  - DU-098-58: Asset, Asset `Asphalt Cutter Husqvarna {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset untuk Auto-approve di atas batas.
  - DU-098-59: Asset, Asset `Genset Portable Hours A {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Duration unit Hours.
  - DU-098-60: Asset, Asset `Genset Portable Hours B {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Duration unit Hours.
  - DU-098-61: Asset, Asset `Tamping Rammer Wacker {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset baris pertama pengajuan campuran, Auto-approve ON.
  - DU-098-62: Asset, Asset `Plate Compactor Bomag {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset baris kedua pengajuan campuran, override Auto-approve OFF.
  - DU-098-63: Asset, Asset `Mesin Las Genset Honda {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Self service ON.
  - DU-098-64: Asset, Asset `Chain Hoist Kito {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset untuk pengajuan yang melewati batas timeout.
  - DU-098-65: Asset, Asset `Jackhammer Makita {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Allow Borrow Deny.
  - DU-098-66: Asset, Asset `Boring Machine Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset untuk pengajuan yang melanggar Max duration.
  - DU-098-67: Borrow, Borrower `Oscar Pranata {runId}`, Asset `Cutting Torch Harris {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Borrowed`, Duration `2 hari`, Handover `T0`; baris Borrowed total 2 hari untuk Extension Auto-approve.
  - DU-098-68: Borrow, Borrower `Oscar Pranata {runId}`, Asset `Pemotong Pipa Ridgid {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Borrowed`, Duration `2 hari`, Handover `T0`; baris Borrowed total 2 hari untuk Extension dengan approval.
  - DU-098-69: Borrow, Borrower `Oscar Pranata {runId}`, Asset `Pompa Lumpur Grundfos {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Borrowed`, Duration `12 hari`, Handover `T0`; baris Borrowed untuk Extension Waiting for Approval yang melewati batas.
  - DU-098-70: Borrow, Borrower `Oscar Pranata {runId}`, Asset `Bor Pile Soilmec {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Borrowed`, Duration `12 hari`, Handover `T0`, Extension `1 hari menunggu review Aktor Borrow sejak T0`; baris Borrowed dengan override Require approval OFF untuk Extension Waiting for Review.
  - DU-098-71: Asset, Asset `Boom Lift Haulotte {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan override Require approval OFF untuk Borrow kedua.
  - DU-098-72: User, Nama `Oscar Pranata {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower dengan baris Borrowed untuk Extension.
  - DU-098-73: User, Nama `Nanda Pratiwi {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower yang meminjam sendiri lewat Borrow Now tanpa baris aktif.
  - DU-098-74: User, Nama `Tomi Arsyad {runId}`, Akses `Total Control`; Total Control kedua untuk himpunan approver fallback.
  - DU-098-75: Group, Group `Gudang Sub Dua Manager {runId}`, Group induk `Gudang Dua Manager {runId}`; Group turunan dari Gudang Dua Manager tanpa Approver, ada satu Group Manager sendiri.
  - DU-098-76: User, Nama `Gerry Kusuma {runId}`, Peran `Group Manager`, Group `Gudang Sub Dua Manager {runId}`; Group Manager Gudang Sub Dua Manager.
  - DU-098-77: Asset, Asset `Mesin Press Hidrolik {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Sub Dua Manager {runId}`, Status `Available`; aset di Group turunan Gudang Dua Manager tanpa Approver.
  - DU-098-78: Asset, Asset `Hydraulic Press Enerpac {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Dua Manager {runId}`, Status `Available`; aset di Gudang Dua Manager tanpa override AND untuk Any one approver pada fallback.
  - DU-098-79: Asset, Asset `Skid Loader Gehl {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Anak {runId}`, Status `Available`; aset di Gudang Anak untuk keputusan Group Manager lewat ancestor.
  - DU-098-80: Asset, Asset `Skid Loader New Holland {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Anak {runId}`, Status `Available`; aset di Gudang Anak dengan override Allowed borrower Same Group only.
  - DU-098-81: Asset, Asset `Pompa Submersible Tsurumi {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Available`; aset dengan Approval type Any one approver untuk Reject.
  - DU-098-82: Borrow, Borrower `Oscar Pranata {runId}`, Asset `Mesin Bubut Krisbow {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Borrowed`, Duration `1 hari`, Handover `T0`, Extension `satu Extension Approved sebesar 1 hari`; baris Borrowed dengan Duration 1 hari dan satu Extension Approved 1 hari, override Max extensions 2.
  - DU-098-83: Borrow, Borrower `Oscar Pranata {runId}`, Asset `Mesin Frais Mini {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Borrowed`, Duration `2 hari`, Handover `T0`, Extension `satu Extension Approved sebesar 1 hari`; baris Borrowed dengan Duration 2 hari dan satu Extension Approved 1 hari, override Max extensions 2.
  - DU-098-84: Asset, Asset `Bulldozer Kobelco {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Anak {runId}`, Status `Available`; aset dengan override Allow Borrow Deny dan Allowed borrower Same Group only.
  - DU-098-85: Group, Group `Gudang GM Nonaktif {runId}`; Group tanpa Approver, satu-satunya Group Manager-nya berstatus Inactive.
  - DU-098-86: User, Nama `Hasan Basri {runId}`, Peran `Group Manager`, Group `Gudang GM Nonaktif {runId}`, Status `Inactive`; Group Manager nonaktif Gudang GM Nonaktif.
  - DU-098-87: User, Nama `Putra Wijaya {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Induk {runId}`; Borrower tanpa baris aktif.
  - DU-098-88: Asset, Asset `Rock Breaker Furukawa {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang GM Nonaktif {runId}`, Status `Available`; aset di Group tanpa Approver dan tanpa Group Manager aktif.
  - DU-098-89: Asset, Asset `Mesin Gerinda Rusak Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Induk {runId}`, Status `Damaged`, Kondisi `Damaged`; aset berkondisi Damaged dengan override Allow Borrow Deny.
  - DU-098-90: Entitas, entitas khusus spec ini, tidak dipakai spec lain: Name `Entitas Approval Borrow {runId}`; Transaction timeout `1`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Approval Borrow {runId}` (DU-098-90) yang tidak dipakai spec lain, karena penugasan Role Transaksi `Approver` dan Transaction timeout adalah setting entitas; semua data di atas berada di entitas itu.
  - Level Feature Suite Borrowing bernilai `Full` dan Approval Workflow tersedia di plan entitas aktor.
  - Company default Borrow bernilai: Require approval `ON`, Auto-approve `ON`, Auto-approve when duration ≤ `3`, Approval type `Any one approver`, Max duration `14`, Max extensions `1`, Duration unit `Days`, Self service `OFF`, Transaction timeout `1`, Allow Borrow `Allow`.
  - Role Transaksi `Approver` untuk Borrow ditugaskan pada Group `Gudang Induk {runId}` beserta descendant kepada Rudi Hartono {runId}, Rani Kusuma {runId}, Ina Sulastri {runId}, Rio Saputra {runId}, dan Lia Permata {runId}; pada Group `Gudang Wawan {runId}` kepada Wawan Setiawan {runId} dan Rani Kusuma {runId}; pada Group `Gudang Satu Approver {runId}` kepada Sari Handayani {runId}; pada Group `Gudang Satu Approver B {runId}` kepada Sinta Maharani {runId}; pada Group `Gudang Gani {runId}` kepada Gani Prakoso {runId}.
  - Group `Gudang Tanpa Approver {runId}`, `Gudang Dua Manager {runId}`, `Gudang Sub Dua Manager {runId}`, `Gudang Tanpa Manager {runId}`, dan `Gudang GM Nonaktif {runId}` tidak punya penugasan Role Transaksi `Approver` untuk Borrow.
  - Group Manager: Gani Prakoso {runId} menaungi Group `Gudang Induk {runId}` dan `Gudang Gani {runId}`; Gina Anggraeni {runId} menaungi Group `Gudang Tanpa Approver {runId}`; Gino Wibowo {runId} dan Gita Rahayu {runId} menaungi Group `Gudang Dua Manager {runId}`; Gerry Kusuma {runId} menaungi Group `Gudang Sub Dua Manager {runId}`; tidak ada Group Manager yang menaungi Group `Gudang Tanpa Manager {runId}`; Hasan Basri {runId} menaungi Group `Gudang GM Nonaktif {runId}` dengan status Inactive.
  - Override tingkat aset yang ada untuk aset `Mixer Truck Scania {runId}`, `Crane Tower Potain {runId}`, `Genset Perkins 100kVA {runId}`, `Wheel Loader Caterpillar {runId}`, `Excavator Sany SY215 {runId}`, `Roller Hamm {runId}`, dan `Welding Machine Lincoln {runId}` bernilai Approval type `All approvers (AND)`.
  - Override tingkat aset untuk `Scissor Lift Skyjack {runId}`, `Boom Lift Haulotte {runId}`, dan `Bor Pile Soilmec {runId}` bernilai Require approval `OFF`; untuk `Skid Loader New Holland {runId}` bernilai Allowed borrower `Same Group only`; untuk `Mesin Bubut Krisbow {runId}` dan `Mesin Frais Mini {runId}` bernilai Max extensions `2`.
  - Override tingkat aset untuk `Genset Portable Hours A {runId}` dan `Genset Portable Hours B {runId}` bernilai Duration unit `Hours`; untuk `Plate Compactor Bomag {runId}` bernilai Auto-approve `OFF`; untuk `Mesin Las Genset Honda {runId}` bernilai Self service `ON`; untuk `Jackhammer Makita {runId}` bernilai Allow Borrow `Deny`; untuk `Bulldozer Kobelco {runId}` bernilai Allow Borrow `Deny` dan Allowed borrower `Same Group only`; untuk `Mesin Gerinda Rusak Bosch {runId}` bernilai Allow Borrow `Deny`.
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`; waktu acuan `T0` adalah waktu saat spec dimulai dan waktu berlalu dinyatakan relatif terhadap `T0`.

## Test Steps


### Approval satu level dari Approver Role Transaksi dengan Approval type Any one approver
1. Hana mengajukan Borrow aset `Pompa Beton Schwing {runId}` untuk Borrower `Bima Nugraha {runId}` dengan Duration `5 hari`
2. Verifikasi baris `Pompa Beton Schwing {runId}` berstatus `Waiting for Approval` karena nilai efektif Require approval `ON` dan Approval type `Any one approver`
3. Verifikasi Approver baris adalah Rudi Hartono {runId} dan Rani Kusuma {runId} yang ditugaskan Role Transaksi `Approver` pada Group `Gudang Induk {runId}`
4. Rudi menyetujui baris `Pompa Beton Schwing {runId}`
5. Verifikasi baris `Pompa Beton Schwing {runId}` berstatus `Waiting for Handover` karena Any one approver memakai rule OR dan approver pertama yang approve menyelesaikan level
6. Verifikasi Rani berstatus `Not Involved` pada baris `Pompa Beton Schwing {runId}`
7. Verifikasi baris `Pompa Beton Schwing {runId}` tidak menunggu approval tingkat berikutnya karena approval hanya satu level

### Approval type All approvers menunggu semua Approver
8. Hana mengajukan Borrow aset `Mixer Truck Scania {runId}` untuk Borrower `Bima Nugraha {runId}` dengan Duration `5 hari`
9. Verifikasi baris `Mixer Truck Scania {runId}` berstatus `Waiting for Approval` dengan nilai efektif Approval type `All approvers (AND)` dari override tingkat aset
10. Rudi menyetujui baris `Mixer Truck Scania {runId}`
11. Verifikasi baris `Mixer Truck Scania {runId}` tetap `Waiting for Approval` karena rule AND menunggu Approver lain
12. Rani menyetujui baris `Mixer Truck Scania {runId}`
13. Verifikasi baris `Mixer Truck Scania {runId}` berstatus `Waiting for Handover` karena semua Approver menyetujui

### Satu Reject pada rule AND membuat baris Rejected
14. Hana mengajukan Borrow aset `Crane Tower Potain {runId}` untuk Borrower `Citra Dewi {runId}` dengan Duration `5 hari`
15. Rudi menolak baris `Crane Tower Potain {runId}`
16. Verifikasi baris `Crane Tower Potain {runId}` berstatus `Rejected` karena satu Approver yang reject menggagalkan level
17. Verifikasi Rani berstatus `Not Involved` pada baris `Crane Tower Potain {runId}`

### Keputusan hampir bersamaan pada Any one approver
18. Hana mengajukan Borrow aset `Hoist Konstruksi Alimak {runId}` untuk Borrower `Citra Dewi {runId}` dengan Duration `5 hari`
19. Rudi menyetujui dan Rani menolak baris `Hoist Konstruksi Alimak {runId}` hampir bersamaan
20. Verifikasi baris `Hoist Konstruksi Alimak {runId}` memiliki tepat satu hasil final dan Approver yang keputusannya tidak diterapkan berstatus `Not Involved`
21. Verifikasi hasil final baris `Hoist Konstruksi Alimak {runId}` sama dengan keputusan yang diterima server lebih dulu dan keputusan yang masuk kemudian tidak diterapkan
22. Verifikasi permintaan approval Approver yang keputusannya tidak diterapkan ditutup dan tidak lagi menunggu keputusannya pada baris `Hoist Konstruksi Alimak {runId}`

### Approver yang tidak eligible tidak dihitung
23. Hana mengajukan Borrow aset `Genset Perkins 100kVA {runId}` untuk Borrower `Dedi Kurniawan {runId}` dengan Duration `5 hari`
24. Verifikasi daftar Approver baris `Genset Perkins 100kVA {runId}` tidak memuat Ina Sulastri {runId} karena berstatus Inactive, Rio Saputra {runId} karena Read Only, dan Lia Permata {runId} karena tanpa lisensi addon
25. Rudi menyetujui baris `Genset Perkins 100kVA {runId}`
26. Rani menyetujui baris `Genset Perkins 100kVA {runId}`
27. Verifikasi baris `Genset Perkins 100kVA {runId}` berstatus `Waiting for Handover` setelah semua Approver eligible menyetujui

### Approver yang ditugaskan di Group induk mencakup Group turunan
28. Hana mengajukan Borrow aset `Bulldozer Komatsu D65 {runId}` untuk Borrower `Dedi Kurniawan {runId}` dengan Duration `5 hari`
29. Verifikasi Rudi Hartono {runId} adalah Approver baris `Bulldozer Komatsu D65 {runId}` di Group `Gudang Anak {runId}` karena penugasan mencakup node beserta seluruh descendant-nya
30. Rudi menyetujui baris `Bulldozer Komatsu D65 {runId}`
31. Verifikasi baris `Bulldozer Komatsu D65 {runId}` berstatus `Waiting for Handover` tanpa langkah eskalasi tersendiri ke Group induk

### Keputusan Group Manager tanpa penugasan tetap override final
32. Hana mengajukan Borrow aset `Wheel Loader Caterpillar {runId}` untuk Borrower `Eka Putri {runId}` dengan Duration `5 hari`
33. Gani menyetujui baris `Wheel Loader Caterpillar {runId}`
34. Verifikasi baris `Wheel Loader Caterpillar {runId}` berstatus `Waiting for Handover` karena keputusan Group Manager yang menaungi Group asal bersifat override final walau Approval type `All approvers (AND)`

### Group Manager tanpa penugasan tidak dihitung dalam rule AND
35. Hana mengajukan Borrow aset `Excavator Sany SY215 {runId}` untuk Borrower `Eka Putri {runId}` dengan Duration `5 hari`
36. Rudi menyetujui baris `Excavator Sany SY215 {runId}`
37. Rani menyetujui baris `Excavator Sany SY215 {runId}`
38. Verifikasi baris `Excavator Sany SY215 {runId}` berstatus `Waiting for Handover` tanpa menunggu Gani karena Group Manager tanpa penugasan tidak dihitung dalam rule AND

### Tidak ada Approver eligible jatuh ke Group Manager yang menaungi
39. Hana mengajukan Borrow aset `Compactor Dynapac {runId}` untuk Borrower `Fitri Amelia {runId}` dengan Duration `5 hari`
40. Verifikasi Approver baris `Compactor Dynapac {runId}` adalah Gina Anggraeni {runId} sebagai Group Manager yang menaungi Group `Gudang Tanpa Approver {runId}`
41. Verifikasi kondisi tidak ada Approver eligible tercatat di log transaksi baris `Compactor Dynapac {runId}` dengan Modified By `System`
42. Verifikasi entri log itu tanpa Note enum
43. Verifikasi satu notifikasi `approver_required` dikirim untuk baris `Compactor Dynapac {runId}`
44. Gina menyetujui baris `Compactor Dynapac {runId}`
45. Verifikasi baris `Compactor Dynapac {runId}` berstatus `Waiting for Handover` karena Any one approver pada himpunan fallback cukup satu Approver

### Transaksi lain yang juga tanpa Approver mengirim notifikasinya sendiri
46. Hana mencatat jumlah notifikasi `approver_required` untuk Group `Gudang Tanpa Approver {runId}`
47. Hana mengajukan Borrow aset `Backhoe Loader Case {runId}` untuk Borrower `Fitri Amelia {runId}` dengan Duration `5 hari`
48. Verifikasi jumlah notifikasi `approver_required` untuk Group `Gudang Tanpa Approver {runId}` bertambah satu untuk baris `Backhoe Loader Case {runId}`

### Notifikasi approver_required saat konfigurasi Approval disimpan
49. Hana mencatat jumlah notifikasi `approver_required` untuk Group `Gudang Tanpa Approver {runId}`
50. Rina menambah override Group untuk `Gudang Tanpa Approver {runId}` dengan Require approval bernilai `ON`
51. Verifikasi jumlah notifikasi `approver_required` untuk Group `Gudang Tanpa Approver {runId}` tidak bertambah karena kondisi tidak ada Role Transaksi `Approver` di Group mana pun tidak timbul: Approver Borrow ditugaskan di Group lain
52. Rina menambah override tingkat aset untuk `Compactor Dynapac {runId}` dengan Max duration bernilai `10` tanpa mengubah konfigurasi Approval
53. Verifikasi jumlah notifikasi `approver_required` untuk Group `Gudang Tanpa Approver {runId}` tidak bertambah selama konfigurasi Approval tidak diubah

### Tanpa Approver dan tanpa Group Manager jatuh ke Total Control
54. Hana mengajukan Borrow aset `Motor Grader Volvo {runId}` untuk Borrower `Gilang Ramadhan {runId}` dengan Duration `5 hari`
55. Verifikasi Rina Wulandari {runId} sebagai Total Control termasuk Approver baris `Motor Grader Volvo {runId}` karena tidak ada Group Manager aktif
56. Verifikasi Tomi Arsyad {runId} sebagai Total Control kedua juga termasuk Approver baris `Motor Grader Volvo {runId}` karena approver fallback adalah semua user Total Control
57. Rina menyetujui baris `Motor Grader Volvo {runId}`
58. Verifikasi baris `Motor Grader Volvo {runId}` berstatus `Waiting for Handover`

### Approval type berlaku pada himpunan Group Manager fallback
59. Hana mengajukan Borrow aset `Roller Hamm {runId}` untuk Borrower `Gilang Ramadhan {runId}` dengan Duration `5 hari`
60. Gino menyetujui baris `Roller Hamm {runId}`
61. Verifikasi baris `Roller Hamm {runId}` tetap `Waiting for Approval` karena rule AND pada himpunan fallback menunggu Gita
62. Gita menyetujui baris `Roller Hamm {runId}`
63. Verifikasi baris `Roller Hamm {runId}` berstatus `Waiting for Handover` karena semua Group Manager fallback menyetujui

### Pengaju Total Control melewati seluruh langkah approval
64. Rina mengajukan Borrow aset `Dump Truck Mitsubishi {runId}` untuk Borrower `Hendra Gunawan {runId}` dengan Duration `3 hari`
65. Verifikasi baris `Dump Truck Mitsubishi {runId}` langsung berstatus `Waiting for Handover` sebagai hasil approval `Approved` dengan seluruh langkah approval dilewati walau Group asal punya Approver
66. Verifikasi log transaksi baris `Dump Truck Mitsubishi {runId}` memuat `Approved by [Nama] (Total Control — requester)` dengan [Nama] `Rina Wulandari {runId}` walau Duration `3 hari` juga memenuhi Auto-approve when duration ≤ `3`
67. Verifikasi Modified By baris `Dump Truck Mitsubishi {runId}` adalah pengaju Rina Wulandari, bukan `System`
68. Verifikasi Rina Wulandari {runId} tidak tercatat sebagai approver baris `Dump Truck Mitsubishi {runId}` karena bypass Kondisi A bukan pengaju menjadi approver transaksinya sendiri

### Pengaju Group Manager melewati seluruh langkah approval
69. Gani mengajukan Borrow aset `Forklift Komatsu {runId}` yang Group asalnya `Gudang Anak {runId}` untuk Borrower `Hendra Gunawan {runId}` dengan Duration `3 hari`
70. Verifikasi baris `Forklift Komatsu {runId}` langsung berstatus `Waiting for Handover` sebagai hasil approval `Approved` karena pengaju menaungi Group asal lewat ancestor-nya
71. Verifikasi log transaksi baris `Forklift Komatsu {runId}` memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] `Gani Prakoso {runId}` walau Duration `3 hari` juga memenuhi Auto-approve when duration ≤ `3`
72. Verifikasi Gani Prakoso {runId} tidak tercatat sebagai approver baris `Forklift Komatsu {runId}` karena bypass Kondisi A bukan pengaju menjadi approver transaksinya sendiri

### Kondisi A dievaluasi sebelum self-approval guard
73. Gani mengajukan Borrow aset `Concrete Vibrator Wacker {runId}` untuk Borrower `Indah Permatasari {runId}` dengan Duration `3 hari`
74. Verifikasi log transaksi baris `Concrete Vibrator Wacker {runId}` memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] `Gani Prakoso {runId}` dan bukan `Approved by system (no independent approver)` walau Gani satu-satunya Approver walau Duration `3 hari` juga memenuhi Auto-approve when duration ≤ `3`

### Kondisi A tidak berlaku bila Require approval efektif OFF
75. Rina mengajukan Borrow aset `Scissor Lift Skyjack {runId}` untuk Borrower `Indah Permatasari {runId}`
76. Verifikasi log transaksi baris `Scissor Lift Skyjack {runId}` tidak memuat `Approved by [Nama] (Total Control — requester)` dengan [Nama] `Rina Wulandari {runId}` karena Require approval efektif `OFF`

### Require approval efektif OFF melewati langkah approval
77. Hana mengajukan Borrow aset `Boom Lift Haulotte {runId}` untuk Borrower `Joko Widodo {runId}`
78. Verifikasi baris `Boom Lift Haulotte {runId}` langsung lanjut ke tahap eksekusi dengan status `Waiting for Handover` tanpa langkah approval
79. Verifikasi tidak ada rute Group Manager atau Total Control dan tidak ada notifikasi `approver_required` untuk baris `Boom Lift Haulotte {runId}`
80. Verifikasi Rudi Hartono {runId} dan Rani Kusuma {runId} tidak menerima permintaan approval untuk baris `Boom Lift Haulotte {runId}`

### Pengaju satu-satunya Approver eligible
81. Sari mengajukan Borrow aset `Telehandler JLG {runId}` untuk Borrower `Joko Widodo {runId}` dengan Duration `3 hari`
82. Verifikasi baris `Telehandler JLG {runId}` langsung berstatus `Waiting for Handover` sebagai hasil approval `Approved` karena langkah approval dilewati
83. Verifikasi log transaksi baris `Telehandler JLG {runId}` memuat `Approved by system (no independent approver)` walau Duration `3 hari` juga memenuhi Auto-approve when duration ≤ `3`
84. Verifikasi Modified By baris `Telehandler JLG {runId}` adalah `System`
85. Verifikasi Sari dikecualikan dari daftar Approver baris `Telehandler JLG {runId}` dan tidak menjadi approver transaksinya sendiri

### Pengaju salah satu dari beberapa Approver dikecualikan
86. Rudi mengajukan Borrow aset `Skid Steer Bobcat {runId}` untuk Borrower `Kirana Larasati {runId}` dengan Duration `5 hari`
87. Verifikasi baris `Skid Steer Bobcat {runId}` berstatus `Waiting for Approval` dengan Rani sebagai Approver dan tanpa Rudi
88. Rudi mencoba menyetujui baris `Skid Steer Bobcat {runId}` miliknya sendiri
89. Verifikasi keputusan Rudi ditolak karena pengaju tidak pernah menjadi approver transaksinya sendiri
90. Rani menyetujui baris `Skid Steer Bobcat {runId}`
91. Verifikasi baris `Skid Steer Bobcat {runId}` berstatus `Waiting for Handover` setelah Approver yang bukan pengaju menyetujui

### Borrower yang juga Approver dikecualikan dari baris miliknya
92. Hana mengajukan Borrow aset `Tower Light Generac {runId}` untuk Borrower `Wawan Setiawan {runId}` dengan Duration `5 hari`
93. Verifikasi Wawan tidak ada dalam daftar Approver baris `Tower Light Generac {runId}` miliknya dan Rani menjadi Approver

### Approval type tidak berpengaruh pada satu Approver
94. Hana mengajukan Borrow aset `Welding Machine Lincoln {runId}` untuk Borrower `Kirana Larasati {runId}` dengan Duration `5 hari`
95. Sinta menyetujui baris `Welding Machine Lincoln {runId}`
96. Verifikasi baris `Welding Machine Lincoln {runId}` berstatus `Waiting for Handover` setelah satu-satunya Approver menyetujui walau Approval type `All approvers (AND)`

### Pengajuan yang melanggar Deny atau Limits ditolak sebelum approval
97. Hana mencatat jumlah permintaan approval yang diterima Rudi
98. Hana mengajukan Borrow aset `Jackhammer Makita {runId}` untuk Borrower `Lukman Hakim {runId}`
99. Verifikasi pengajuan ditolak karena Deny pada override tingkat aset dievaluasi sebelum approval
100. Hana mengajukan Borrow aset `Boring Machine Bosch {runId}` untuk Borrower `Lukman Hakim {runId}` dengan Duration `15 hari`
101. Verifikasi pengajuan ditolak karena Max duration `14` dievaluasi sebelum approval
102. Verifikasi jumlah permintaan approval yang diterima Rudi sama dengan catatan

### Auto-approve meloloskan durasi sama dengan batas
103. Hana mengajukan Borrow aset `Paver Vogele {runId}` untuk Borrower `Mira Oktaviani {runId}` dengan Duration `3 hari`
104. Verifikasi baris `Paver Vogele {runId}` langsung berstatus `Waiting for Handover` tanpa menunggu approval karena durasi sama dengan batas Auto-approve when duration ≤

### Auto-approve tidak meloloskan durasi di atas batas
105. Hana mengajukan Borrow aset `Asphalt Cutter Husqvarna {runId}` untuk Borrower `Mira Oktaviani {runId}` dengan Duration `4 hari`
106. Verifikasi baris `Asphalt Cutter Husqvarna {runId}` berstatus `Waiting for Approval` karena durasi melebihi batas Auto-approve when duration ≤

### Auto-approve berlaku untuk Extension dan menghitung perpanjangan sebelumnya
107. Hana mengajukan Extension `1 hari` pada baris `Cutting Torch Harris {runId}`
108. Verifikasi Extension langsung berlaku tanpa menunggu approval karena durasi total sejak handover `3 hari` sama dengan batas Auto-approve when duration ≤
109. Hana mengajukan Extension `1 hari` kedua pada baris `Cutting Torch Harris {runId}`
110. Verifikasi Extension kedua ditolak karena Extension yang langsung berlaku dihitung terhadap Max extensions `1`

### Extension yang Approved dihitung terhadap Max extensions
111. Hana mengajukan Extension `2 hari` pada baris `Pemotong Pipa Ridgid {runId}`
112. Verifikasi Extension berstatus `Waiting for Approval` karena durasi total sejak handover `4 hari` melebihi batas Auto-approve when duration ≤
113. Rudi menyetujui Extension baris `Pemotong Pipa Ridgid {runId}`
114. Hana mengajukan Extension `1 hari` kedua pada baris `Pemotong Pipa Ridgid {runId}`
115. Verifikasi Extension kedua ditolak karena Extension yang Approved dihitung terhadap Max extensions `1`

### Auto-approve membandingkan dalam satuan Duration unit efektif aset
116. Hana mengajukan Borrow aset `Genset Portable Hours A {runId}` untuk Borrower `Bima Nugraha {runId}` dengan Duration `3 jam`
117. Verifikasi baris `Genset Portable Hours A {runId}` langsung berstatus `Waiting for Handover` karena `3` dalam satuan Duration unit `Hours` aset sama dengan batas Auto-approve when duration ≤
118. Hana mengajukan Borrow aset `Genset Portable Hours B {runId}` untuk Borrower `Lukman Hakim {runId}` dengan Duration `4 jam`
119. Verifikasi baris `Genset Portable Hours B {runId}` berstatus `Waiting for Approval` karena `4` dalam satuan Duration unit `Hours` aset melebihi batas

### Auto-approve dinilai per baris dalam satu pengajuan
120. Hana mengajukan satu Borrow dengan Duration `3 hari` yang memuat aset `Tamping Rammer Wacker {runId}` dan `Plate Compactor Bomag {runId}` untuk Borrower `Citra Dewi {runId}`
121. Verifikasi baris `Tamping Rammer Wacker {runId}` langsung berstatus `Waiting for Handover` karena Auto-approve dinilai per baris
122. Verifikasi baris `Plate Compactor Bomag {runId}` berstatus `Waiting for Approval` karena baris lain tetap mengikuti aturan efektifnya sendiri dengan override Auto-approve `OFF`

### Self service meminjam tanpa approval
123. Borrower `Nanda Pratiwi {runId}` melakukan Borrow Now aset `Mesin Las Genset Honda {runId}` dengan Duration `5 hari` tanpa bantuan Aktor Borrow
124. Verifikasi baris `Mesin Las Genset Honda {runId}` berstatus `Borrowed` tanpa langkah approval

### Aturan tetap dan Eligibility dievaluasi sebelum approval
125. Hana mencatat jumlah permintaan approval yang diterima Rudi
126. Hana mengajukan Borrow aset `Pompa Beton Schwing {runId}` untuk Borrower `Mira Oktaviani {runId}` dengan Duration `5 hari`
127. Verifikasi pengajuan ditolak karena aset sudah punya transaksi aktif, aturan tetap yang dievaluasi sebelum approval
128. Hana mengajukan Borrow aset `Skid Loader New Holland {runId}` untuk Borrower `Joko Widodo {runId}` dengan Duration `5 hari`
129. Verifikasi pengajuan ditolak karena Allowed borrower `Same Group only` pada Eligibility dievaluasi sebelum approval
130. Verifikasi jumlah permintaan approval yang diterima Rudi sama dengan catatan

### Auto-approve menghitung perpanjangan sebelumnya
131. Hana mengajukan Extension `1 hari` pada baris `Mesin Bubut Krisbow {runId}`
132. Verifikasi Extension langsung berlaku tanpa menunggu approval karena durasi total sejak handover `3` hari termasuk perpanjangan sebelumnya sama dengan batas Auto-approve when duration ≤
133. Hana mengajukan Extension `1 hari` pada baris `Mesin Frais Mini {runId}`
134. Verifikasi Extension berstatus `Waiting for Approval` karena durasi total `4` hari termasuk perpanjangan sebelumnya melebihi batas Auto-approve when duration ≤, walau Extension ini sendiri `1` hari

### Timeout menutup pengajuan dan Extension yang menunggu
135. Hana mengajukan Borrow aset `Chain Hoist Kito {runId}` untuk Borrower `Dedi Kurniawan {runId}` dengan Duration `5 hari`
136. Hana mengajukan Extension `1 hari` pada baris `Pompa Lumpur Grundfos {runId}`
137. Waktu berlalu sampai batas Transaction timeout `1` hari sejak masing-masing baris masuk statusnya terlewati
138. Job timeout transaksi berjalan
139. Verifikasi baris `Chain Hoist Kito {runId}` ditutup `Canceled` di BRW asal dengan alasan `Timed out (Waiting for Approval)`, dan asetnya dikembalikan ke Draft baru tanpa nomor BRW
140. Verifikasi log transaksi baris `Chain Hoist Kito {runId}` memuat node `Canceled` di BRW asal dan log aset dengan Modified By `System`
141. Verifikasi Extension baris `Pompa Lumpur Grundfos {runId}` berstatus Canceled dengan alasan `Timed out (Waiting for Approval)` dan baris tetap `Borrowed`
142. Verifikasi Extension baris `Bor Pile Soilmec {runId}` yang menunggu review Aktor Borrow berstatus Canceled dengan alasan `Timed out (Waiting for Review)` dan baris tetap `Borrowed`

### Any one approver: Reject pertama menggagalkan level
143. Hana mengajukan Borrow aset `Pompa Submersible Tsurumi {runId}` untuk Borrower `Lukman Hakim {runId}` dengan Duration `5 hari`
144. Rudi menolak baris `Pompa Submersible Tsurumi {runId}`
145. Verifikasi baris `Pompa Submersible Tsurumi {runId}` berstatus `Rejected` karena Approver pertama yang reject menggagalkan level pada Approval type `Any one approver`
146. Verifikasi Rani berstatus `Not Involved` pada baris `Pompa Submersible Tsurumi {runId}`

### Group Manager yang menaungi lewat ancestor memutuskan baris di Group turunan
147. Hana mengajukan Borrow aset `Skid Loader Gehl {runId}` yang Group asalnya `Gudang Anak {runId}` untuk Borrower `Kirana Larasati {runId}` dengan Duration `5 hari`
148. Gani menyetujui baris `Skid Loader Gehl {runId}`
149. Verifikasi baris `Skid Loader Gehl {runId}` berstatus `Waiting for Handover` karena keputusan Group Manager yang menaungi Group `Gudang Induk {runId}` sebagai ancestor Group asal bersifat override final tanpa penugasan Approver

### Himpunan fallback memuat Group Manager node dan ancestor-nya
150. Hana mengajukan Borrow aset `Mesin Press Hidrolik {runId}` yang Group asalnya `Gudang Sub Dua Manager {runId}` untuk Borrower `Gilang Ramadhan {runId}` dengan Duration `5 hari`
151. Verifikasi approver fallback baris `Mesin Press Hidrolik {runId}` adalah Gerry Kusuma {runId} sebagai Group Manager node serta Gino Wibowo {runId} dan Gita Rahayu {runId} sebagai Group Manager ancestor

### Any one approver pada himpunan fallback dengan dua Group Manager cukup satu
152. Hana mengajukan Borrow aset `Hydraulic Press Enerpac {runId}` untuk Borrower `Indah Permatasari {runId}` dengan Duration `5 hari`
153. Gino menyetujui baris `Hydraulic Press Enerpac {runId}`
154. Verifikasi baris `Hydraulic Press Enerpac {runId}` berstatus `Waiting for Handover` karena Any one approver pada himpunan fallback cukup satu Group Manager
155. Verifikasi Gita berstatus `Not Involved` pada baris `Hydraulic Press Enerpac {runId}`

### Deny pada override mengalahkan Eligibility dan Limits
156. Hana mencatat jumlah baris Borrow untuk aset `Bulldozer Kobelco {runId}`
157. Hana mengajukan Borrow aset `Bulldozer Kobelco {runId}` untuk Borrower `Joko Widodo {runId}` dengan Duration `15 hari`
158. Verifikasi pengajuan ditolak karena Deny pada override tingkat aset dievaluasi lebih dulu daripada Eligibility Allowed borrower `Same Group only` dan Limits Max duration `14`, walau Group Borrower berbeda dari Group asal aset dan Duration `15` hari melebihi Max duration
159. Verifikasi jumlah baris Borrow untuk aset `Bulldozer Kobelco {runId}` sama dengan catatan

### Aturan tetap dievaluasi sebelum Deny pada override
160. Hana mencatat jumlah baris Borrow untuk aset `Mesin Gerinda Rusak Bosch {runId}`
161. Hana mengajukan Borrow aset `Mesin Gerinda Rusak Bosch {runId}` untuk Borrower `Joko Widodo {runId}` dengan Duration `5 hari`
162. Verifikasi pengajuan ditolak karena aset berkondisi rusak, aturan tetap yang dievaluasi lebih dulu daripada Deny pada override tingkat aset
163. Verifikasi jumlah baris Borrow untuk aset `Mesin Gerinda Rusak Bosch {runId}` sama dengan catatan

### Eligibility dievaluasi sebelum Limits
164. Hana mencatat jumlah baris Borrow untuk aset `Skid Loader New Holland {runId}`
165. Hana mengajukan Borrow aset `Skid Loader New Holland {runId}` untuk Borrower `Joko Widodo {runId}` dengan Duration `15 hari`
166. Verifikasi pengajuan ditolak karena Allowed borrower `Same Group only` pada Eligibility dievaluasi lebih dulu daripada Limits Max duration `14`, walau Duration `15` hari melebihi Max duration
167. Verifikasi jumlah baris Borrow untuk aset `Skid Loader New Holland {runId}` sama dengan catatan

### Group Manager nonaktif tidak dihitung sehingga rute jatuh ke Total Control
168. Hana mengajukan Borrow aset `Rock Breaker Furukawa {runId}` untuk Borrower `Putra Wijaya {runId}` dengan Duration `5 hari`
169. Verifikasi Rina Wulandari {runId} dan Tomi Arsyad {runId} sebagai Total Control termasuk Approver baris `Rock Breaker Furukawa {runId}` karena Group Manager Hasan Basri {runId} berstatus Inactive sehingga tidak ada Group Manager aktif
170. Verifikasi Hasan Basri {runId} tidak termasuk Approver baris `Rock Breaker Furukawa {runId}` karena berstatus Inactive
