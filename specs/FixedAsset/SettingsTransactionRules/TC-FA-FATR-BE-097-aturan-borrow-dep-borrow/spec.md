---
id: TC-FA-FATR-BE-097-aturan-borrow-dep-borrow
title: "Evaluasi dan penegakan aturan pada transaksi Borrow"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["§Aturan Logika Modul#r6", "§Aturan Logika Modul#r26", "§Aturan Logika Modul#r36", "§Aturan Logika Modul#r89", "§4.1#r62", "§4.1#r63", "§4.1#r64", "§4.1#r65", "§4.1#r66", "§4.1#r67", "§4.1#r68", "§4.1#r69", "§4.1#r70", "§4.1#r71", "§4.1#r72", "§4.1#r73", "§4.1#r74", "§4.1#r75", "§4.1#r79", "§4.1#r80", "§4.1#r81", "§4.1#r83", "§4.1#r85", "§4.1#r93", "§4.1#r94", "§4.1#r95", "§4.1#r96", "§4.1#r97", "§4.1#r98", "§4.1#r164", "§4.1#r165", "§4.1#r175", "§4.1#r190", "§4.1#r206", "§4.1#r207", "§4.1#r208", "§4.1#r209", "§4.1#r210", "§4.1#r211", "§9.2#b92", "§9.2#b427", "§9.2#b428", "§9.2#b429", "§9.2#b434", "§9.2#b435", "§9.2#b438", "§9.2#b384", "§9.2#b386", "§9.2#b387", "§9.2#b388", "§9.2#b389", "§9.2#b390", "§9.2#b392", "§9.2#b393", "§9.2#b394", "§9.2#b401", "§9.2#b402", "§9.2#b404", "§9.2#b406", "§9.2#b407", "§9.2#b408", "§9.2#b409", "§9.2#b410", "§9.2#b411", "§9.2#b424", "§9.2#b430", "§9.2#b431", "§9.2#b432", "§9.4.2#r35", "§9.4.2#r60", "§9.4.2#r82", "§9.4.2#r122", "§9.4.2#r128", "§9.4.2#r145", "§9.4.2#r146", "§9.4.2#r147", "§9.4.3#b9", "§9.4.4#r54", "§9.7#r6", "§9.7#r15", "§9.8#r2", "§9.8#r3", "§9.8#r4", "§9.10.2#r5", "§9.10.2#b7", "§9.10.2#r12", "§11#r3", "§11#r19"]
smoke: []
dependsOn:
  - Borrow: pengajuan, Extension, dan Return
trace:
  "§Aturan Logika Modul#r6": [4, 6, 49]
  "§Aturan Logika Modul#r26": [4]
  "§Aturan Logika Modul#r36": [203, 208]
  "§Aturan Logika Modul#r89": [238]
  "§4.1#r62": [84]
  "§4.1#r63": [214, 216]
  "§4.1#r64": [84]
  "§4.1#r65": [91]
  "§4.1#r66": [84]
  "§4.1#r67": [96, 99]
  "§4.1#r68": [37, 107, 108]
  "§4.1#r69": [40, 112, 114]
  "§4.1#r70": [54, 56]
  "§4.1#r71": [45, 59, 118, 121]
  "§4.1#r72": [45]
  "§4.1#r73": [47]
  "§4.1#r74": [49]
  "§4.1#r75": [51]
  "§4.1#r79": [84, 87, 124]
  "§4.1#r80": [84]
  "§4.1#r81": [87, 89]
  "§4.1#r83": [91, 93]
  "§4.1#r85": [93, 127]
  "§4.1#r93": [66, 68]
  "§4.1#r94": [62, 64]
  "§4.1#r95": [71, 73]
  "§4.1#r96": [77, 79]
  "§4.1#r97": [75]
  "§4.1#r98": [82]
  "§4.1#r164": [135]
  "§4.1#r165": [211]
  "§4.1#r175": [140]
  "§4.1#r190": [212]
  "§4.1#r206": [168]
  "§4.1#r207": [156, 164]
  "§4.1#r208": [156, 168]
  "§4.1#r209": [151]
  "§4.1#r210": [182]
  "§4.1#r211": [188, 191]
  "§9.2#b92": [10, 11, 12]
  "§9.2#b427": [129]
  "§9.2#b428": [131]
  "§9.2#b429": [138]
  "§9.2#b434": [4, 6]
  "§9.2#b435": [5]
  "§9.2#b438": [202]
  "§9.2#b384": [5]
  "§9.2#b386": [20, 21]
  "§9.2#b387": [162, 173]
  "§9.2#b388": [163, 174]
  "§9.2#b389": [176]
  "§9.2#b390": [142]
  "§9.2#b392": [162, 173]
  "§9.2#b393": [171, 173]
  "§9.2#b394": [159, 162]
  "§9.2#b401": [168]
  "§9.2#b402": [156, 164]
  "§9.2#b404": [23, 25, 27, 28, 30, 31, 103, 104]
  "§9.2#b406": [33]
  "§9.2#b407": [40, 42]
  "§9.2#b408": [37, 107, 108]
  "§9.2#b409": [40, 42, 112, 114]
  "§9.2#b410": [25, 27]
  "§9.2#b411": [35]
  "§9.2#b424": [133, 140]
  "§9.2#b430": [144]
  "§9.2#b431": [145, 146, 147, 148]
  "§9.2#b432": [136]
  "§9.4.2#r35": [4]
  "§9.4.2#r60": [47, 51, 59]
  "§9.4.2#r82": [205, 207]
  "§9.4.2#r122": [16, 18]
  "§9.4.2#r128": [202]
  "§9.4.2#r145": [84]
  "§9.4.2#r146": [87, 88]
  "§9.4.2#r147": [93, 127]
  "§9.4.3#b9": [198]
  "§9.4.4#r54": [235]
  "§9.7#r6": [205, 207]
  "§9.7#r15": [10, 14]
  "§9.8#r2": [194, 195, 196]
  "§9.8#r3": [231]
  "§9.8#r4": [232]
  "§9.10.2#r5": [220, 222]
  "§9.10.2#b7": [225]
  "§9.10.2#r12": [220, 224]
  "§11#r3": [40, 194]
  "§11#r19": [194, 197, 231, 232]
owner: BE
---

# Evaluasi dan penegakan aturan pada transaksi Borrow

## Prerequisites
- Aktor: Rina Wulandari {runId} (Total Control) mengubah setting; Hana Pertiwi {runId} (Aktor Borrow) mengajukan, menyerahterimakan, dan mengembalikan; Rudi Hartono {runId} (Approver Borrow) menyetujui Extension dan pengajuan; Borrower sesuai entri data; Principal (operator Admin Console) mengubah level plan dan toggle Approval Workflow.
- Data:
  - DU-097-1: Entitas, Nama `Entitas Aturan Borrow {runId}`; entitas khusus spec ini.
  - DU-097-2: Group, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Group dengan Division.
  - DU-097-3: Group, Group `Gudang Pusat Unit 2 {runId}`, Group induk `Gudang Pusat {runId}`, Division `Operasional {runId}`; Group turunan dari Gudang Pusat.
  - DU-097-4: Group, Group `Gudang Cabang {runId}`, Division `Operasional {runId}`; Group lain dengan Division yang sama.
  - DU-097-5: Group, Group `Gudang Mitra {runId}`, Division `Logistik {runId}`; Group dengan Division berbeda.
  - DU-097-6: Group, Group `Gudang Tanpa Divisi {runId}`; Group tanpa Division.
  - DU-097-7: Category, Category `Alat Berat {runId}`, TAG Type `RFID`; Category bertag.
  - DU-097-8: Category, Category `Kendaraan {runId}`, TAG Type `RFID`; Category bertag.
  - DU-097-9: Category, Category `Perkakas {runId}`, TAG Type `RFID`; Category bertag.
  - DU-097-10: Category, Category `Perlengkapan Lapangan {runId}`, TAG Type `Non TAG`; Category bertanda Non TAG.
  - DU-097-11: Category, Category `Alat Ringan {runId}`, TAG Type `RFID`; Category bertag.
  - DU-097-12: User, Nama `Rina Wulandari {runId}`, Akses `Total Control`; Total Control yang mengubah setting.
  - DU-097-13: User, Nama `Hana Pertiwi {runId}`, Peran `Aktor Borrow`, Group `Gudang Pusat {runId} beserta descendant, Gudang Cabang {runId}, dan Gudang Tanpa Divisi {runId}`; Aktor Borrow yang mengajukan, menyerahterimakan, dan mengembalikan.
  - DU-097-14: User, Nama `Rudi Hartono {runId}`, Peran `Approver Borrow`, Group `Gudang Pusat {runId} beserta descendant`; Approver Borrow.
  - DU-097-15: User, Nama `Budi Santoso {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan dua baris aktif.
  - DU-097-16: User, Nama `Citra Lestari {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan tiga baris aktif.
  - DU-097-17: User, Nama `Dewi Anggraini {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan satu baris aktif.
  - DU-097-18: User, Nama `Eko Prasetyo {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan dua baris aktif dan satu Draft.
  - DU-097-19: User, Nama `Fajar Nugroho {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan baris aktif di dua Category.
  - DU-097-20: User, Nama `Gita Purnama {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan baris Overdue.
  - DU-097-21: User, Nama `Intan Maharani {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower satu Group dengan Group asal aset.
  - DU-097-22: User, Nama `Joko Susilo {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat Unit 2 {runId}`, Division `Operasional {runId}`; Borrower di Group turunan.
  - DU-097-23: User, Nama `Kiki Amalia {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Cabang {runId}`, Division `Operasional {runId}`; Borrower di Group lain berDivision sama.
  - DU-097-24: User, Nama `Lina Marlina {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Mitra {runId}`, Division `Logistik {runId}`; Borrower berDivision berbeda.
  - DU-097-25: User, Nama `Maya Safitri {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`; Borrower tanpa Division.
  - DU-097-26: User, Nama `Nanda Wijaya {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Tanpa Divisi {runId}`; Borrower tanpa Division di Group tanpa Division.
  - DU-097-27: User, Nama `Tono Hidayat {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan tiga baris Borrowed.
  - DU-097-28: User, Nama `Tari Wulandari {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan satu baris Borrowed.
  - DU-097-29: User, Nama `Umar Faruq {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower Self service.
  - DU-097-30: User, Nama `Vina Oktaviani {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower tanpa baris aktif.
  - DU-097-31: User, Nama `Wati Rahmawati {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan baris Days dan Hours.
  - DU-097-32: User, Nama `Winda Kusuma {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan baris pengingat.
  - DU-097-33: User, Nama `Yuda Pratama {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan baris yang menunggu batas timeout.
  - DU-097-34: User, Nama `Zaki Ramadhan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Cabang {runId}`, Division `Operasional {runId}`; Borrower dengan baris serah terima dan pengembalian.
  - DU-097-35: User, Nama `Bagas Setiawan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower pada level Basic.
  - DU-097-36: Asset, Asset `Bor Listrik Bosch GSB {runId}`, Category `Perkakas {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-37: Asset, Asset `Excavator PC200 {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-38: Asset, Asset `Bulldozer D85 {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-39: Asset, Asset `Gerinda Tangan Makita {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-40: Asset, Asset `Mesin Las Inverter {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-41: Asset, Asset `Kompresor Atlas Copco {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-42: Asset, Asset `Bor Beton Hilti {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-43: Asset, Asset `Tangga Aluminium 6m {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-44: Asset, Asset `Genset Honda 5kVA {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-45: Asset, Asset `Pickup Hilux {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-46: Asset, Asset `Wheel Loader L60 {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-47: Asset, Asset `Backhoe JCB 3CX {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-48: Asset, Asset `Dump Truck Hino {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Cabang {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-49: Asset, Asset `Excavator Mini Kubota {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-50: Asset, Asset `Bor Tangan Dewalt {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-51: Asset, Asset `Gergaji Mesin Stihl {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-52: Asset, Asset `Pompa Air Honda {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-53: Asset, Asset `Mesin Potong Keramik {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-54: Asset, Asset `Bor Tangan Bosch GBH {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Cabang {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-55: Asset, Asset `Trafo Las Lincoln {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Mitra {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-56: Asset, Asset `Genset Portable Yamaha {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Tanpa Divisi {runId}`, Status `Available`; aset di Group asal tanpa Division.
  - DU-097-57: Asset, Asset `Genset Cummins 20kVA {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset untuk Borrow Now.
  - DU-097-58: Asset, Asset `Mesin Gergaji Rusak {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Damaged`, Kondisi `Damaged`; aset berkondisi Damaged.
  - DU-097-59: Asset, Asset `Mesin Gerinda Hilang {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Missing`, Kondisi `Missing`; aset berkondisi Missing.
  - DU-097-60: Asset, Asset `Theodolite Topcon {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-61: Asset, Asset `Pemadat Tanah Wacker {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-62: Asset, Asset `Concrete Cutter Husqvarna {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-63: Asset, Asset `Water Pump Mitsubishi {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-64: Asset, Asset `Scaffolding Set Lengkap {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-65: Asset, Asset `Hydraulic Jack 20T {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berstatus Available.
  - DU-097-66: Borrow, Borrower `Budi Santoso {runId}`, Asset `Pemecah Beton Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Waiting for Approval`; baris aktif pertama Budi.
  - DU-097-67: Borrow, Borrower `Budi Santoso {runId}`, Asset `Penggiling Beton Fiori {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`; baris aktif kedua Budi.
  - DU-097-68: Borrow, Borrower `Citra Lestari {runId}`, Asset `Pemotong Besi Makita {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Waiting for Approval`; baris aktif pertama Citra.
  - DU-097-69: Borrow, Borrower `Citra Lestari {runId}`, Asset `Troli Material Heavy Duty {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Waiting for Handover`; baris aktif kedua Citra.
  - DU-097-70: Borrow, Borrower `Citra Lestari {runId}`, Asset `Vibrator Beton Wacker {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `5 hari`, Due date `T0 + 5 hari`; baris aktif ketiga Citra, Borrowed.
  - DU-097-71: Borrow, Borrower `Dewi Anggraini {runId}`, Asset `Gerinda Meja Krisbow {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`; satu baris aktif Dewi.
  - DU-097-72: Borrow, Borrower `Eko Prasetyo {runId}`, Asset `Palu Hidrolik Breaker {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Waiting for Approval`; baris aktif pertama Eko.
  - DU-097-73: Borrow, Borrower `Eko Prasetyo {runId}`, Asset `Alat Ukur Laser Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`; baris aktif kedua Eko.
  - DU-097-74: Borrow, Borrower `Eko Prasetyo {runId}`, Asset `Tiang Penyangga Baja {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Draft`; baris Draft Eko yang tidak dihitung kuota.
  - DU-097-75: Borrow, Borrower `Fajar Nugroho {runId}`, Asset `Roller Compactor Bomag {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`; baris aktif Fajar di Category Alat Berat.
  - DU-097-76: Borrow, Borrower `Fajar Nugroho {runId}`, Asset `Truk Fuso Fighter {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`; baris aktif Fajar di Category Kendaraan.
  - DU-097-77: Borrow, Borrower `Fajar Nugroho {runId}`, Asset `Van Gran Max {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`; baris aktif kedua Fajar di Category Kendaraan.
  - DU-097-78: Borrow, Borrower `Gita Purnama {runId}`, Asset `Mesin Pemadat Tanah Mikasa {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Overdue`, Due date `T0 - 2 hari`; baris Overdue Gita.
  - DU-097-79: Borrow, Borrower `Gita Purnama {runId}`, Asset `Concrete Mixer Molen {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `5 hari`, Due date `T0 + 5 hari`; baris Borrowed Gita untuk Extension.
  - DU-097-80: Borrow, Borrower `Tono Hidayat {runId}`, Asset `Crane Mobil Tadano {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `10 hari`, Handover `T0`; baris Borrowed total 10 hari sejak Handover.
  - DU-097-81: Borrow, Borrower `Tono Hidayat {runId}`, Asset `Vibro Roller Sakai {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `10 hari`, Handover `T0`; baris Borrowed total 10 hari sejak Handover.
  - DU-097-82: Borrow, Borrower `Tono Hidayat {runId}`, Asset `Concrete Pump Putzmeister {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `3 hari`, Handover `T0`, Extension `satu Extension Approved sebesar 2 hari`; baris dengan satu Extension Approved.
  - DU-097-83: Borrow, Borrower `Tari Wulandari {runId}`, Asset `Scissor Lift Genie {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `3 hari`, Handover `T0`, Extension `satu Extension Rejected dan satu Extension Canceled`; baris dengan Extension Rejected dan Canceled.
  - DU-097-85: Borrow, Borrower `Zaki Ramadhan {runId}`, Asset `Mesin Bor Magnet Jancy {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Waiting for Handover`, TAG `RFID E280-1100-0097-0001`, TAG Type `RFID`; baris Waiting for Handover untuk aset ber-TAG.
  - DU-097-86: Borrow, Borrower `Zaki Ramadhan {runId}`, Asset `Rompi Safety Set {runId}`, Category `Perlengkapan Lapangan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Waiting for Handover`, TAG Type `Non TAG`; baris Waiting for Handover untuk aset Non TAG.
  - DU-097-87: Borrow, Borrower `Zaki Ramadhan {runId}`, Asset `Alat Ukur Jarak Leica {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, TAG `RFID E280-1100-0097-0003`, TAG Type `RFID`, Kondisi TAG `rusak`; baris Borrowed dengan TAG rusak.
  - DU-097-88: Borrow, Borrower `Wati Rahmawati {runId}`, Asset `Tangki Air Portabel {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration unit `Days`, Due date `T0 + 1 hari`; baris Days dengan Due date T0 + 1 hari.
  - DU-097-89: Borrow, Borrower `Wati Rahmawati {runId}`, Asset `Lampu Sorot LED {runId}`, Category `Alat Ringan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration unit `Hours`, Due date `T0 + 2 jam`; baris Hours dengan Due date T0 + 2 jam.
  - DU-097-90: Borrow, Borrower `Winda Kusuma {runId}`, Asset `Troli Dorong Besi {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration unit `Days`, Due date `T0 + 2 hari`; baris Days yang titik D-3 sudah lewat saat Due date ditetapkan.
  - DU-097-91: Borrow, Borrower `Winda Kusuma {runId}`, Asset `Mesin Amplas Bosch {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration unit `Days`, Due date `T0 + 5 hari`, Duration `5 hari`; baris Days untuk Extension dan ambang dihitung ulang.
  - DU-097-92: Borrow, Borrower `Winda Kusuma {runId}`, Asset `Kabel Roll 50m {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration unit `Days`, Due date `T0 + 4 hari`, Duration `4 hari`; baris Days untuk Extension yang titik D-3 barunya sudah lewat.
  - DU-097-93: Borrow, Borrower `Winda Kusuma {runId}`, Asset `Lampu Kerja Portabel {runId}`, Category `Alat Ringan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration unit `Hours`, Due date `T0 + 3 jam`; baris Hours untuk pengingat per jam.
  - DU-097-94: Borrow, Borrower `Yuda Pratama {runId}`, Asset `Pompa Submersible Grundfos {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Waiting for Handover`, Masuk status `T0`; baris Waiting for Handover yang melewati batas.
  - DU-097-95: Borrow, Borrower `Yuda Pratama {runId}`, Asset `Kunci Torsi Digital {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Draft`; baris Draft.
  - DU-097-96: Borrow, Borrower `Yuda Pratama {runId}`, Asset `Pengebor Tanah Manual {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Due date `T0 + 30 hari`; baris Borrowed yang di luar cakupan timeout.
  - DU-097-97: Asset, Asset `Senter Kerja Industrial {runId}`, Category `Alat Ringan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset berCategory Hours untuk level Basic.
  - DU-097-98: Asset, Asset `Tenda Lapangan Komando {runId}`, Category `Perlengkapan Lapangan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset Non TAG untuk Borrow sesudah Max extensions bernilai 0.
  - DU-097-99: Asset, Asset `Mobil Operasional Avanza {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset Category Kendaraan untuk pengajuan di batas kuota.
  - DU-097-100: User, Nama `Hendra Gunawan {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan satu baris Overdue dan dua baris Borrowed.
  - DU-097-101: Borrow, Borrower `Hendra Gunawan {runId}`, Asset `Pompa Lumpur Tsurumi {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Overdue`, Due date `T0 - 2 hari`; baris Overdue Hendra yang ikut dihitung kuota.
  - DU-097-102: Borrow, Borrower `Hendra Gunawan {runId}`, Asset `Mesin Gerinda Duduk Krisbow {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Due date `T0 + 30 hari`; baris Borrowed pertama Hendra.
  - DU-097-103: Borrow, Borrower `Hendra Gunawan {runId}`, Asset `Kompaktor Plat Bomag {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Due date `T0 + 30 hari`; baris Borrowed kedua Hendra.
  - DU-097-104: User, Nama `Indra Kusuma {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan satu baris Alat Berat dan satu baris Kendaraan.
  - DU-097-105: Borrow, Borrower `Indra Kusuma {runId}`, Asset `Dongkrak Hidrolik 50T {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Due date `T0 + 30 hari`; baris Borrowed Indra di Category Alat Berat.
  - DU-097-106: Borrow, Borrower `Indra Kusuma {runId}`, Asset `Pickup Mitsubishi L300 {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Due date `T0 + 30 hari`; baris Borrowed Indra di Category Kendaraan.
  - DU-097-107: Asset, Asset `Forklift Toyota 8FD {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Cabang {runId}`, Status `Available`; aset Kendaraan di Gudang Cabang untuk kuota override All categories.
  - DU-097-108: User, Nama `Kartika Sari {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan satu baris Kendaraan dan satu baris Alat Berat.
  - DU-097-109: Borrow, Borrower `Kartika Sari {runId}`, Asset `Van Pengangkut Daihatsu {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Due date `T0 + 30 hari`; baris Borrowed Kartika di Category Kendaraan.
  - DU-097-110: Borrow, Borrower `Kartika Sari {runId}`, Asset `Mesin Bubut Mini {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Due date `T0 + 30 hari`; baris Borrowed Kartika di Category Alat Berat.
  - DU-097-111: Asset, Asset `Mini Bus Toyota HiAce {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Cabang {runId}`, Status `Available`; aset Kendaraan di Gudang Cabang yang diterima oleh kuota per Category.
  - DU-097-112: Asset, Asset `Truk Boks Isuzu {runId}`, Category `Kendaraan {runId}`, Group asal `Gudang Cabang {runId}`, Status `Available`; aset Kendaraan di Gudang Cabang yang ditolak oleh kuota per Category.
  - DU-097-113: User, Nama `Lukman Hakim {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan dua baris Overdue.
  - DU-097-114: Borrow, Borrower `Lukman Hakim {runId}`, Asset `Generator Set Perkins {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Overdue`, Due date `T0 - 2 hari`; baris Overdue pertama Lukman.
  - DU-097-115: Borrow, Borrower `Lukman Hakim {runId}`, Asset `Blower Industri Kipor {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Overdue`, Due date `T0 - 3 hari`; baris Overdue kedua Lukman.
  - DU-097-116: Asset, Asset `Ekskavator Mini Yanmar {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Available`; aset Alat Berat yang nilai efektif Block new borrow when overdue-nya ON.
  - DU-097-117: User, Nama `Mulyadi Pranoto {runId}`, Peran `Borrower (Employee aktif)`, Group `Gudang Pusat {runId}`, Division `Operasional {runId}`; Borrower dengan baris ber-Extension Approved dan baris ber-Extension Waiting for Approval.
  - DU-097-118: Borrow, Borrower `Mulyadi Pranoto {runId}`, Asset `Pompa Beton Schwing {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `10 hari`, Handover `T0`, Extension `satu Extension Approved sebesar 2 hari`; baris dengan Duration 10 hari dan satu Extension Approved.
  - DU-097-119: Borrow, Borrower `Mulyadi Pranoto {runId}`, Asset `Pompa Celup Ebara {runId}`, Category `Alat Berat {runId}`, Group asal `Gudang Pusat {runId}`, Status `Borrowed`, Duration `3 hari`, Handover `T0`, Extension `satu Extension Waiting for Approval sebesar 1 hari`; baris dengan satu Extension Waiting for Approval.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Aturan Borrow {runId}` yang tidak dipakai spec lain, sehingga perubahan setting dan plan tidak menyentuh spec lain.
  - Level Feature Suite Borrowing bernilai `Full` dan toggle Approval Workflow ON pada plan entitas, kecuali diubah langkah.
  - Company default Borrow bernilai: Max duration `14`, Max extensions `1`, Max assets per borrower (concurrent) `3`, Allowed borrower `Employee in any Group`, Block new borrow when overdue `ON`, Self service `OFF`, Duration unit `Days`, Photo at start `ON`, Photo at end `ON`, Due date reminders `D-3, D-1, D-day`, Transaction timeout `7`, Require approval `ON`, Allow Borrow `Allow`.
  - Category `Alat Ringan {runId}` bernilai sendiri Duration unit `Hours` dan Due date reminders `D-day only`.
  - Waktu acuan `T0` adalah waktu saat spec dimulai; waktu berlalu dinyatakan relatif terhadap `T0` menurut zona waktu client.

## Test Steps
### Pengajuan yang melanggar Deny pada Category ditolak server tanpa memandang keadaan tampilan
1. Rina menyimpan Allow Borrow bernilai `Deny` pada Category `Perkakas {runId}`
2. Hana mencatat jumlah baris Borrow untuk aset `Bor Listrik Bosch GSB {runId}`
3. Hana mengirim pengajuan Borrow aset `Bor Listrik Bosch GSB {runId}` untuk Borrower `Intan Maharani {runId}` tanpa melalui tampilan
4. Verifikasi pengajuan ditolak server karena Deny pada Category tetap dievaluasi di server
5. Verifikasi pesan blokir menyebut pihak yang dapat dihubungi
6. Verifikasi jumlah baris Borrow untuk aset `Bor Listrik Bosch GSB {runId}` sama dengan catatan sehingga tidak ada baris yang tercipta

### Deny pada override tingkat aset mengalahkan nilai lain
7. Rina menambah override tingkat aset untuk `Excavator PC200 {runId}` pada Category `Alat Berat {runId}` dengan Allow Borrow bernilai `Deny`
8. Hana mencatat jumlah baris Borrow untuk aset `Excavator PC200 {runId}`
9. Hana mengajukan Borrow aset `Excavator PC200 {runId}` untuk Borrower `Intan Maharani {runId}`
10. Verifikasi pengajuan ditolak karena Deny pada override tingkat aset mengalahkan nilai Allow di Category dan Company default
11. Verifikasi pesan blokir menyebut pihak yang dapat dihubungi
12. Verifikasi jumlah baris Borrow untuk aset `Excavator PC200 {runId}` sama dengan catatan
13. Hana mengajukan Borrow aset `Bulldozer D85 {runId}` yang sama Category-nya tanpa override Deny untuk Borrower `Intan Maharani {runId}`
14. Verifikasi pengajuan diterima karena override Deny hanya mengevaluasi aset targetnya

### Aset rusak atau hilang tidak dapat di-Borrow
15. Hana mengajukan Borrow aset `Mesin Gergaji Rusak {runId}` untuk Borrower `Intan Maharani {runId}`
16. Verifikasi pengajuan ditolak karena aset berkondisi rusak tidak bisa di-Borrow
17. Hana mengajukan Borrow aset `Mesin Gerinda Hilang {runId}` untuk Borrower `Intan Maharani {runId}`
18. Verifikasi pengajuan ditolak karena aset berkondisi hilang tidak bisa di-Borrow

### Batas yang berlaku diterima Borrower sebelum mengisi form
19. Hana membaca batas aturan Borrow untuk aset `Gerinda Tangan Makita {runId}` bagi Borrower `Budi Santoso {runId}`
20. Verifikasi batas yang diterima memuat Max duration `14` dan Max assets per borrower (concurrent) `3`
21. Verifikasi jumlah baris aktif Borrower `Budi Santoso {runId}` yang diterima adalah `2`

### Kuota di bawah batas diterima
22. Hana mengajukan Borrow aset `Tangga Aluminium 6m {runId}` untuk Borrower `Dewi Anggraini {runId}`
23. Verifikasi pengajuan diterima karena baris aktif ditambah baris baru adalah `2`, satu di bawah Max assets per borrower (concurrent)

### Kuota tepat di batas diterima
24. Hana mengajukan Borrow aset `Bor Beton Hilti {runId}` untuk Borrower `Budi Santoso {runId}`
25. Verifikasi pengajuan diterima karena baris aktif ditambah baris baru adalah `3`, sama dengan Max assets per borrower (concurrent)

### Kuota melebihi batas ditolak
26. Hana mengajukan Borrow aset `Genset Honda 5kVA {runId}` untuk Borrower `Citra Lestari {runId}`
27. Verifikasi pengajuan ditolak karena baris Waiting for Approval, Waiting for Handover, dan Borrowed ditambah baris baru melebihi Max assets per borrower (concurrent)
28. Verifikasi jumlah baris aktif Borrower `Citra Lestari {runId}` tetap `3`

### Seluruh baris dalam satu pengajuan dihitung terhadap kuota
29. Hana mengajukan satu Borrow yang memuat aset `Mesin Las Inverter {runId}` dan `Kompresor Atlas Copco {runId}` untuk Borrower `Dewi Anggraini {runId}`
30. Verifikasi seluruh pengajuan ditolak karena baris aktif ditambah semua baris baru adalah `4`
31. Verifikasi jumlah baris aktif Borrower `Dewi Anggraini {runId}` tetap `2`

### Draft tidak dihitung terhadap kuota
32. Hana mengajukan Borrow aset `Pemadat Tanah Wacker {runId}` untuk Borrower `Eko Prasetyo {runId}`
33. Verifikasi pengajuan diterima karena baris Draft tidak dihitung

### Extension tidak menambah hitungan kuota
34. Hana mengajukan Extension `1 hari` pada baris `Vibrator Beton Wacker {runId}` milik Borrower `Citra Lestari {runId}`
35. Verifikasi Extension diterima walau Borrower sudah berada di batas Max assets per borrower (concurrent)

### Kuota dihitung lintas Category atau per Category menurut sumber nilai efektif
36. Hana mengajukan Borrow aset `Pickup Hilux {runId}` di Category `Kendaraan {runId}` untuk Borrower `Fajar Nugroho {runId}`
37. Verifikasi pengajuan ditolak karena nilai efektif bersumber dari Company default sehingga kuota dihitung lintas Category
38. Rina menyimpan Max assets per borrower (concurrent) bernilai `2` pada Category `Alat Berat {runId}`
39. Hana mengajukan Borrow aset `Wheel Loader L60 {runId}` di Category `Alat Berat {runId}` untuk Borrower `Fajar Nugroho {runId}`
40. Verifikasi pengajuan diterima karena kuota dihitung di Category `Alat Berat {runId}` dan nilai efektif aset adalah `2`
41. Hana mengajukan Borrow aset `Backhoe JCB 3CX {runId}` di Category `Alat Berat {runId}` untuk Borrower `Fajar Nugroho {runId}`
42. Verifikasi pengajuan ditolak karena kuota di Category `Alat Berat {runId}` melebihi nilai efektif aset yang diajukan
43. Rina mengembalikan Max assets per borrower (concurrent) pada Category `Alat Berat {runId}` menjadi Inherit

### Block new borrow when overdue menolak pengajuan lintas Category dan Group
44. Hana memilih Borrower `Gita Purnama {runId}` pada pengajuan Borrow aset `Dump Truck Hino {runId}`
45. Verifikasi pemilihan Borrower ditolak karena Borrower punya baris Overdue di Category dan Group yang berbeda
46. Hana mengirim Submit pengajuan Borrow aset `Dump Truck Hino {runId}` untuk Borrower `Gita Purnama {runId}`
47. Verifikasi Submit ditolak karena Borrower punya baris Overdue
48. Hana mengirim pengajuan Borrow aset `Dump Truck Hino {runId}` untuk Borrower `Gita Purnama {runId}` tanpa melalui tampilan
49. Verifikasi pengajuan ditolak oleh server

### Block new borrow when overdue tidak berlaku untuk Extension
50. Hana mengajukan Extension `1 hari` pada baris `Concrete Mixer Molen {runId}` milik Borrower `Gita Purnama {runId}`
51. Verifikasi Extension diterima walau Borrower punya baris Overdue

### Block new borrow when overdue memakai nilai efektif aset yang dimohon
52. Rina menyimpan Block new borrow when overdue bernilai `OFF` pada Category `Kendaraan {runId}`
53. Hana mengajukan Borrow aset `Excavator Mini Kubota {runId}` di Category `Alat Berat {runId}` untuk Borrower `Gita Purnama {runId}`
54. Verifikasi pengajuan ditolak karena nilai efektif Block new borrow when overdue untuk aset ini adalah `ON`
55. Hana mengajukan Borrow aset `Dump Truck Hino {runId}` di Category `Kendaraan {runId}` untuk Borrower `Gita Purnama {runId}`
56. Verifikasi pengajuan diterima karena nilai efektif Block new borrow when overdue untuk aset ini adalah `OFF`

### Pengajuan Borrow baru diterima setelah semua baris Overdue Returned
57. Hana menyelesaikan Return baris `Mesin Pemadat Tanah Mikasa {runId}` milik Borrower `Gita Purnama {runId}` dengan 1 foto
58. Hana mengajukan Borrow aset `Excavator Mini Kubota {runId}` di Category `Alat Berat {runId}` untuk Borrower `Gita Purnama {runId}`
59. Verifikasi pengajuan diterima karena semua baris Overdue Borrower sudah Returned

### Allowed borrower Same Group only
60. Rina menyimpan Allowed borrower bernilai `Same Group only`
61. Hana mengajukan Borrow aset `Bor Tangan Dewalt {runId}` untuk Borrower `Intan Maharani {runId}`
62. Verifikasi pengajuan diterima karena Group Borrower sama persis dengan Group asal aset
63. Hana mengajukan Borrow aset `Gergaji Mesin Stihl {runId}` untuk Borrower `Joko Susilo {runId}`
64. Verifikasi pengajuan ditolak karena Group turunan tidak dihitung sebagai Group yang sama
65. Hana mengajukan Borrow aset `Bor Tangan Bosch GBH {runId}` yang Group asalnya `Gudang Cabang {runId}` untuk Borrower `Kiki Amalia {runId}`
66. Verifikasi pengajuan diterima karena Allowed borrower dievaluasi terhadap Group asal aset
67. Hana mengajukan Borrow aset `Pompa Air Honda {runId}` yang Group asalnya `Gudang Pusat {runId}` untuk Borrower `Kiki Amalia {runId}`
68. Verifikasi pengajuan ditolak karena Group Borrower berbeda dari Group asal aset

### Allowed borrower Same Division only
69. Rina menyimpan Allowed borrower bernilai `Same Division only`
70. Hana mengajukan Borrow aset `Pompa Air Honda {runId}` yang Group asalnya `Gudang Pusat {runId}` untuk Borrower `Kiki Amalia {runId}`
71. Verifikasi pengajuan diterima karena Division Borrower sama dengan Division yang melekat pada Group asal aset
72. Hana mengajukan Borrow aset `Mesin Potong Keramik {runId}` untuk Borrower `Lina Marlina {runId}`
73. Verifikasi pengajuan ditolak karena Division Borrower berbeda dari Division Group asal aset
74. Hana mengajukan Borrow aset `Mesin Potong Keramik {runId}` untuk Borrower `Maya Safitri {runId}`
75. Verifikasi pengajuan ditolak karena Borrower tidak punya Division
76. Hana mengajukan Borrow aset `Genset Portable Yamaha {runId}` yang Group asalnya `Gudang Tanpa Divisi {runId}` untuk Borrower `Nanda Wijaya {runId}`
77. Verifikasi pengajuan ditolak karena Group asal aset dan Borrower sama-sama tidak punya Division
78. Hana mengajukan Borrow aset `Genset Portable Yamaha {runId}` yang Group asalnya `Gudang Tanpa Divisi {runId}` untuk Borrower `Kiki Amalia {runId}`
79. Verifikasi pengajuan ditolak karena Group asal aset tidak punya Division

### Allowed borrower Employee in any Group
80. Rina menyimpan Allowed borrower bernilai `Employee in any Group`
81. Hana mengajukan Borrow aset `Mesin Potong Keramik {runId}` untuk Borrower `Lina Marlina {runId}`
82. Verifikasi pengajuan diterima untuk karyawan aktif mana pun

### Extension diizinkan sampai total sama dengan Max duration
83. Hana mengajukan Extension `4 hari` pada baris `Crane Mobil Tadano {runId}` milik Borrower `Tono Hidayat {runId}`
84. Verifikasi Extension diterima karena total `14` hari sejak Handover termasuk perpanjangan sama dengan Max duration

### Extension yang melebihi Max duration ditolak dan tidak dipotong
85. Hana mencatat Due date baris `Vibro Roller Sakai {runId}`
86. Hana mengajukan Extension `5 hari` pada baris `Vibro Roller Sakai {runId}` milik Borrower `Tono Hidayat {runId}`
87. Verifikasi Extension ditolak karena total `15` hari melebihi Max duration
88. Verifikasi pesan blokir menyebut pihak yang dapat dihubungi
89. Verifikasi Due date baris `Vibro Roller Sakai {runId}` sama dengan catatan sehingga Extension tidak dipotong

### Extension melebihi Max extensions ditolak
90. Hana mengajukan Extension `1 hari` pada baris `Concrete Pump Putzmeister {runId}` yang sudah punya satu Extension Approved
91. Verifikasi Extension ditolak karena jumlah perpanjangan sesudahnya melebihi Max extensions `1`

### Extension Rejected dan Canceled tidak dihitung terhadap Max extensions
92. Hana mengajukan Extension `1 hari` pada baris `Scissor Lift Genie {runId}` yang punya Extension Rejected dan Extension Canceled
93. Verifikasi Extension diterima karena Extension Rejected dan Canceled tidak dihitung terhadap Max extensions

### Max extensions bernilai 0 melarang Due date dimundurkan
94. Rina menyimpan Max extensions bernilai `0`
95. Hana mengajukan Borrow aset `Tenda Lapangan Komando {runId}` dengan Duration `2 hari` untuk Borrower `Tari Wulandari {runId}`
96. Verifikasi baris `Tenda Lapangan Komando {runId}` berstatus `Waiting for Handover` karena Duration `2` hari tidak melebihi Auto-approve when duration ≤ `3`
97. Hana melakukan Handover baris `Tenda Lapangan Komando {runId}` tanpa scan TAG dengan 1 foto
98. Hana mengajukan Extension `1 hari` pada baris `Tenda Lapangan Komando {runId}` milik Borrower `Tari Wulandari {runId}`
99. Verifikasi Extension ditolak karena Max extensions bernilai `0` pada pengajuan Borrow yang diajukan sesudah Save sehingga Due date tidak boleh dimundurkan
100. Rina menyimpan Max extensions bernilai `1`

### Baris Overdue dihitung terhadap kuota Max assets per borrower
101. Rina menyimpan Block new borrow when overdue bernilai `OFF` pada Category `Kendaraan {runId}`
102. Hana mengajukan Borrow aset `Mobil Operasional Avanza {runId}` untuk Borrower `Hendra Gunawan {runId}`
103. Verifikasi pengajuan ditolak karena baris Overdue ikut dihitung sehingga baris aktif ditambah baris baru adalah `4`, melebihi Max assets per borrower (concurrent) `3`, sedangkan Block new borrow when overdue bernilai `OFF` untuk aset ini
104. Verifikasi jumlah baris aktif Borrower `Hendra Gunawan {runId}` tetap `3`

### Kuota dihitung lintas Category untuk nilai efektif dari override All categories
105. Rina menambahkan override Group `Gudang Cabang {runId}` untuk All categories pada transaksi peminjaman dengan Max assets per borrower (concurrent) `2`
106. Hana mengajukan Borrow aset `Forklift Toyota 8FD {runId}` untuk Borrower `Indra Kusuma {runId}`
107. Verifikasi pengajuan ditolak karena nilai efektif bersumber dari override All categories sebesar `2` sehingga kuota dihitung lintas Category: `2` baris aktif di dua Category ditambah baris baru adalah `3`
108. Verifikasi jumlah baris aktif Borrower `Indra Kusuma {runId}` tetap `2`
109. Rina menghapus override Group `Gudang Cabang {runId}` untuk All categories pada transaksi peminjaman

### Kuota dihitung per Category untuk nilai efektif dari override Category leaf
110. Rina menambahkan override Group `Gudang Cabang {runId}` untuk Category `Kendaraan {runId}` pada transaksi peminjaman dengan Max assets per borrower (concurrent) `2`
111. Hana mengajukan Borrow aset `Mini Bus Toyota HiAce {runId}` untuk Borrower `Kartika Sari {runId}`
112. Verifikasi pengajuan diterima karena kuota dihitung di Category `Kendaraan {runId}`: `1` baris aktif ditambah baris baru adalah `2`, sama dengan nilai efektif `2` dari override Category leaf, walau seluruh baris aktif lintas Category ditambah baris baru adalah `3`
113. Hana mengajukan Borrow aset `Truk Boks Isuzu {runId}` untuk Borrower `Kartika Sari {runId}`
114. Verifikasi pengajuan ditolak karena kuota di Category `Kendaraan {runId}`: `2` baris aktif ditambah baris baru adalah `3`, melebihi nilai efektif `2`
115. Rina menghapus override Group `Gudang Cabang {runId}` untuk Category `Kendaraan {runId}` pada transaksi peminjaman

### Pengajuan Borrow baru ditolak sampai semua baris Overdue Borrower Returned
116. Hana menyelesaikan Return baris `Generator Set Perkins {runId}` milik Borrower `Lukman Hakim {runId}` dengan 1 foto
117. Hana mengajukan Borrow aset `Ekskavator Mini Yanmar {runId}` di Category `Alat Berat {runId}` untuk Borrower `Lukman Hakim {runId}`
118. Verifikasi pengajuan ditolak karena Borrower masih punya satu baris Overdue, yaitu `Blower Industri Kipor {runId}`
119. Hana menyelesaikan Return baris `Blower Industri Kipor {runId}` milik Borrower `Lukman Hakim {runId}` dengan 1 foto
120. Hana mengajukan Borrow aset `Ekskavator Mini Yanmar {runId}` di Category `Alat Berat {runId}` untuk Borrower `Lukman Hakim {runId}`
121. Verifikasi pengajuan diterima karena semua baris Overdue Borrower sudah Returned

### Extension dihitung terhadap Max duration bersama perpanjangan yang sudah ada
122. Rina menyimpan Max extensions bernilai `2`
123. Hana mengajukan Extension `3 hari` pada baris `Pompa Beton Schwing {runId}` milik Borrower `Mulyadi Pranoto {runId}`
124. Verifikasi Extension ditolak karena total `15` hari sejak Handover termasuk Extension Approved `2` hari yang sudah ada melebihi Max duration `14`, walau Extension ini sendiri `3` hari dan total tanpa perpanjangan lama `13` hari
125. Rina menyimpan Max extensions bernilai `1`

### Extension Waiting for Approval tidak dihitung terhadap Max extensions
126. Hana mengajukan Extension `1 hari` pada baris `Pompa Celup Ebara {runId}` milik Borrower `Mulyadi Pranoto {runId}`
127. Verifikasi Extension diterima karena Extension Waiting for Approval pada baris itu tidak dihitung terhadap Max extensions `1`

### Langkah mulai Borrow mewajibkan scan TAG dan 1 foto
128. Hana mencoba Handover baris `Mesin Bor Magnet Jancy {runId}` tanpa scan TAG
129. Verifikasi Handover ditolak karena scan TAG wajib saat mulai transaksi untuk aset ber-TAG
130. Hana mencoba menyelesaikan langkah mulai baris `Mesin Bor Magnet Jancy {runId}` dengan identifikasi manual
131. Verifikasi langkah mulai ditolak karena tidak ada identifikasi manual untuk langkah mulai
132. Hana mencoba Handover baris `Mesin Bor Magnet Jancy {runId}` dengan scan TAG tanpa foto
133. Verifikasi Handover ditolak karena Photo at start `ON` mewajibkan 1 foto
134. Hana melakukan Handover baris `Mesin Bor Magnet Jancy {runId}` dengan scan TAG dan 1 foto
135. Verifikasi baris `Mesin Bor Magnet Jancy {runId}` berstatus `Borrowed` setelah Handover sebagai langkah awal Borrow
136. Verifikasi Handover Note PDF dibuat untuk serah terima fisik itu

### Aset Non TAG dikecualikan dari scan TAG saat mulai
137. Hana melakukan Handover baris `Rompi Safety Set {runId}` tanpa scan TAG dengan 1 foto
138. Verifikasi Handover diterima karena Category bertanda Non TAG dikecualikan dari scan TAG wajib

### Return mewajibkan 1 foto dan aset kembali ke Group asal
139. Hana mencoba Return baris `Mesin Bor Magnet Jancy {runId}` tanpa foto
140. Verifikasi Return ditolak karena Photo at end `ON` mewajibkan 1 foto
141. Hana melakukan Return baris `Mesin Bor Magnet Jancy {runId}` dengan 1 foto
142. Verifikasi aset `Mesin Bor Magnet Jancy {runId}` berada di Group asal `Gudang Pusat {runId}` walau Borrower berada di Group `Gudang Cabang {runId}`

### Return lewat I can't scan the TAG
143. Hana melakukan Return baris `Alat Ukur Jarak Leica {runId}` lewat "I can't scan the TAG" dengan 1 foto
144. Verifikasi Return diterima karena tag rusak boleh melewati scan pada langkah selesai
145. Verifikasi foto tercatat pada Return
146. Verifikasi pengecekan radius dilakukan pada Return
147. Verifikasi Return diberi flag
148. Verifikasi Report TAG dibuat otomatis

### Titik pengingat yang sudah lewat saat Due date ditetapkan dilewati
149. Winda mencatat jumlah notifikasi `borrow_due_soon` untuk baris `Troli Dorong Besi {runId}`
150. Job harian pengingat Due date berjalan pada `T0`
151. Verifikasi jumlah notifikasi `borrow_due_soon` untuk baris `Troli Dorong Besi {runId}` sama dengan catatan karena titik D-3 sudah lewat dan tidak dikirim terlambat

### Pengingat per jam untuk Duration unit Hours tidak mengikuti pilihan Due date reminders
152. Winda mencatat jumlah notifikasi `borrow_due_soon` untuk baris `Lampu Kerja Portabel {runId}`
153. Wati mencatat jumlah notifikasi `borrow_overdue` untuk baris `Lampu Sorot LED {runId}`
154. Waktu berlalu sampai `T0 + 2 jam`
155. Pengecekan per jam berjalan
156. Verifikasi jumlah notifikasi `borrow_due_soon` untuk baris `Lampu Kerja Portabel {runId}` bertambah satu pada 1 jam sebelum Due date walau Due date reminders bernilai `D-day only`
157. Waktu berlalu sampai 59 menit sesudah Due date baris `Lampu Sorot LED {runId}`
158. Pengecekan per jam berjalan
159. Verifikasi baris `Lampu Sorot LED {runId}` masih `Borrowed`
160. Waktu berlalu sampai `T0 + 3 jam`
161. Pengecekan per jam berjalan
162. Verifikasi baris `Lampu Sorot LED {runId}` berstatus `Overdue` 1 jam setelah Due date menurut zona waktu client
163. Verifikasi Wati menerima satu notifikasi `borrow_overdue` untuk baris `Lampu Sorot LED {runId}`
164. Verifikasi jumlah notifikasi `borrow_due_soon` untuk baris `Lampu Kerja Portabel {runId}` bertambah satu lagi pada saat Due date

### Pengingat D-1 dikirim oleh job harian
165. Winda mencatat jumlah notifikasi `borrow_due_soon` untuk baris `Troli Dorong Besi {runId}`
166. Waktu berlalu sampai `T0 + 1 hari`
167. Job harian pengingat Due date berjalan
168. Verifikasi jumlah notifikasi `borrow_due_soon` untuk baris `Troli Dorong Besi {runId}` bertambah satu sebagai pengingat D-1 untuk aset ber-Duration unit Days

### Overdue Days mulai awal hari kalender setelah Due date
169. Wati mencatat jumlah notifikasi `borrow_overdue` untuk baris `Tangki Air Portabel {runId}`
170. Waktu berlalu sampai akhir hari Due date `T0 + 1 hari` menurut zona waktu client
171. Verifikasi baris `Tangki Air Portabel {runId}` masih `Borrowed`
172. Waktu berlalu sampai awal hari kalender `T0 + 2 hari` menurut zona waktu client
173. Verifikasi baris `Tangki Air Portabel {runId}` berstatus `Overdue` mulai awal hari kalender setelah Due date
174. Verifikasi jumlah notifikasi `borrow_overdue` untuk baris `Tangki Air Portabel {runId}` bertambah satu
175. Waktu berlalu sampai `T0 + 3 hari`
176. Verifikasi jumlah notifikasi `borrow_overdue` untuk baris `Tangki Air Portabel {runId}` sama dengan setelah Overdue pertama sehingga tidak ada notifikasi atau eskalasi lanjutan

### Titik pengingat baru yang sudah lewat saat Due date diubah dilewati
177. Job harian pengingat Due date berjalan pada `T0 + 3 hari`
178. Winda mencatat jumlah notifikasi `borrow_due_soon` untuk baris `Kabel Roll 50m {runId}`
179. Hana mengajukan Extension `1 hari` pada baris `Kabel Roll 50m {runId}` milik Borrower `Winda Kusuma {runId}`
180. Rudi menyetujui Extension baris `Kabel Roll 50m {runId}`
181. Job harian pengingat Due date berjalan kembali
182. Verifikasi jumlah notifikasi `borrow_due_soon` untuk baris `Kabel Roll 50m {runId}` sama dengan catatan karena titik D-3 terhadap Due date baru sudah lewat dan tidak dikirim terlambat

### Extension menghitung ulang ambang pengingat terhadap Due date baru
183. Winda mencatat jumlah notifikasi `borrow_due_soon` untuk baris `Mesin Amplas Bosch {runId}`
184. Hana mengajukan Extension `4 hari` pada baris `Mesin Amplas Bosch {runId}` milik Borrower `Winda Kusuma {runId}`
185. Rudi menyetujui Extension baris `Mesin Amplas Bosch {runId}`
186. Waktu berlalu sampai `T0 + 4 hari`
187. Job harian pengingat Due date berjalan
188. Verifikasi jumlah notifikasi `borrow_due_soon` untuk baris `Mesin Amplas Bosch {runId}` sama dengan catatan karena ambang terhadap Due date lama tidak berlaku lagi
189. Waktu berlalu sampai `T0 + 6 hari`
190. Job harian pengingat Due date berjalan
191. Verifikasi jumlah notifikasi `borrow_due_soon` untuk baris `Mesin Amplas Bosch {runId}` bertambah satu sebagai pengingat D-3 terhadap Due date baru

### Timeout Waiting for Handover mengembalikan baris ke Draft baru
192. Waktu berlalu sampai batas Transaction timeout `7` hari sejak `T0` terlewati
193. Job timeout transaksi berjalan
194. Verifikasi baris `Pompa Submersible Grundfos {runId}` kembali ke Draft baru tanpa nomor BRW dan bukan `Canceled` atau Expired
195. Verifikasi log transaksi memuat node `Returned to Draft` pada BRW asal, Draft baru, dan log aset
196. Verifikasi alasan tercatat `Not picked up` dan Modified By `System`
197. Verifikasi aturan no-show Borrow tidak berlaku: baris `Pompa Submersible Grundfos {runId}` tidak berstatus no-show
198. Verifikasi Draft `Kunci Torsi Digital {runId}` dan baris Borrowed `Pengebor Tanah Manual {runId}` tidak ditutup otomatis

### Settings berubah saat Borrow berjalan
199. Hana mengajukan Borrow aset `Theodolite Topcon {runId}` dengan Duration `10 hari` untuk Borrower `Vina Oktaviani {runId}`
200. Hana mencatat Versi setting yang tercatat pada baris `Theodolite Topcon {runId}`
201. Rina menyimpan Max duration bernilai `5`
202. Verifikasi baris `Theodolite Topcon {runId}` tetap `Waiting for Approval` dan tidak dibatalkan otomatis
203. Verifikasi Versi setting yang tercatat pada baris `Theodolite Topcon {runId}` sama dengan catatan

### Perubahan Settings berlaku untuk Borrow baru
204. Hana mengajukan Borrow aset `Pemadat Tanah Wacker {runId}` dengan Duration `6 hari` untuk Borrower `Vina Oktaviani {runId}`
205. Verifikasi pengajuan ditolak karena Duration melebihi Max duration `5` yang baru
206. Hana mengajukan Borrow aset `Pemadat Tanah Wacker {runId}` dengan Duration `5 hari` untuk Borrower `Vina Oktaviani {runId}`
207. Verifikasi pengajuan diterima menurut Max duration `5`
208. Verifikasi Versi setting yang tercatat pada baris `Pemadat Tanah Wacker {runId}` satu lebih besar daripada pada baris `Theodolite Topcon {runId}`

### Self service dan Max duration dihitung sejak Borrow Now
209. Rina menyimpan Self service bernilai `ON`
210. Umar melakukan Borrow Now aset `Genset Cummins 20kVA {runId}` dengan Duration `4 hari` tanpa bantuan Aktor Borrow
211. Verifikasi baris `Genset Cummins 20kVA {runId}` berstatus `Borrowed` tanpa langkah Handover
212. Verifikasi Borrower meminjam sendiri tanpa admin
213. Umar mengajukan Extension `2 hari` pada baris `Genset Cummins 20kVA {runId}`
214. Verifikasi Extension ditolak karena total `6` hari sejak Borrow Now melebihi Max duration `5`
215. Umar mengajukan Extension `1 hari` pada baris `Genset Cummins 20kVA {runId}`
216. Verifikasi Extension diterima karena total `5` hari sejak Borrow Now sama dengan Max duration

### Level Basic memakai nilai efektif apa pun nilai tersimpan
217. Hana mencatat Versi setting yang berlaku
218. Principal mengubah level Feature Suite Borrowing plan entitas menjadi `Basic`
219. Umar mencoba Borrow Now aset `Concrete Cutter Husqvarna {runId}`
220. Verifikasi Borrow Now ditolak karena Self service tidak tersedia pada level Basic walau nilai tersimpan `ON`
221. Hana mengajukan Borrow aset `Senter Kerja Industrial {runId}` dengan Duration `3 jam` untuk Borrower `Bagas Setiawan {runId}`
222. Verifikasi pengajuan ditolak karena Duration unit Hours tidak tersedia pada level Basic
223. Hana mengajukan Borrow aset `Senter Kerja Industrial {runId}` dengan Duration `3 hari` untuk Borrower `Bagas Setiawan {runId}`
224. Verifikasi transaksi tercatat memakai Duration unit `Days` walau nilai tersimpan Category `Hours`
225. Verifikasi Versi setting yang berlaku sama dengan catatan karena perubahan level plan bukan perubahan Settings

### Timeout Borrow pada level Basic membatalkan baris
226. Hana mengajukan Borrow aset `Water Pump Mitsubishi {runId}` dengan Duration `4 hari` untuk Borrower `Bagas Setiawan {runId}`
227. Hana mengajukan Borrow aset `Scaffolding Set Lengkap {runId}` dengan Duration `4 hari` untuk Borrower `Bagas Setiawan {runId}`
228. Rudi menyetujui pengajuan Borrow aset `Scaffolding Set Lengkap {runId}`
229. Waktu berlalu sampai batas Transaction timeout `7` hari sejak masing-masing baris masuk statusnya terlewati
230. Job timeout transaksi berjalan
231. Verifikasi baris `Water Pump Mitsubishi {runId}` berstatus `Canceled` dan bukan Draft, dengan alasan `Timed out (Waiting for Approval)` dan Modified By `System`
232. Verifikasi baris `Scaffolding Set Lengkap {runId}` berstatus `Canceled` dan bukan Draft, dengan alasan `Not picked up` dan Modified By `System`

### Approval Workflow tidak tersedia melewati langkah approval
233. Principal mematikan toggle Approval Workflow pada plan entitas
234. Hana mengajukan Borrow aset `Hydraulic Jack 20T {runId}` untuk Borrower `Intan Maharani {runId}`
235. Verifikasi nilai efektif Require approval adalah `OFF` dan baris `Hydraulic Jack 20T {runId}` langsung `Waiting for Handover` tanpa langkah approval

### Borrow tidak tersedia pada level None
236. Principal mengubah level Feature Suite Borrowing plan entitas menjadi `None`
237. Hana mengajukan Borrow aset `Gerinda Tangan Makita {runId}` untuk Borrower `Intan Maharani {runId}`
238. Verifikasi Borrow tidak tersedia dan pengajuan ditolak server
