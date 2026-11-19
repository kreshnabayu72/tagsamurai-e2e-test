---
id: TC-FA-BORROW-BE-082-self-service-dan-borrower-tanpa-akun
title: "Self-service Borrow Now, Borrower tanpa akun login dengan PIC, dan aturan Return self-service"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["BORROW-LOGIC-13aa", "BORROW-LOGIC-13b", "BORROW-LOGIC-13c", "BORROW-LOGIC-13d", "BORROW-LOGIC-13e", "BORROW-LOGIC-13f", "BORROW-LOGIC-13g", "BORROW-LOGIC-13h", "BORROW-LOGIC-13i", "BORROW-LOGIC-13j", "BORROW-LOGIC-13k", "BORROW-LOGIC-13l", "BORROW-LOGIC-13m", "BORROW-LOGIC-13n", "BORROW-LOGIC-13o", "BORROW-LOGIC-13p", "BORROW-LOGIC-13q", "BORROW-LOGIC-13r", "BORROW-LOGIC-13s", "BORROW-LOGIC-13t", "BORROW-LOGIC-13u", "BORROW-LOGIC-13v", "BORROW-LOGIC-13w", "BORROW-LOGIC-13x", "BORROW-LOGIC-13y", "BORROW-LOGIC-13z", "BORROW-LOGIC-20aa", "BORROW-LOGIC-20b", "BORROW-LOGIC-20c", "BORROW-LOGIC-20d", "BORROW-LOGIC-20e", "BORROW-LOGIC-20f", "BORROW-LOGIC-20g", "BORROW-LOGIC-20h", "BORROW-LOGIC-20i", "BORROW-LOGIC-20j", "BORROW-LOGIC-20k", "BORROW-LOGIC-20l", "BORROW-LOGIC-20m", "BORROW-LOGIC-20n", "BORROW-LOGIC-20o", "BORROW-LOGIC-20p", "BORROW-LOGIC-20q", "BORROW-LOGIC-20r", "BORROW-LOGIC-20s", "BORROW-LOGIC-20t", "BORROW-LOGIC-20u", "BORROW-LOGIC-20v", "BORROW-LOGIC-20w", "BORROW-LOGIC-20x", "BORROW-LOGIC-20y", "BORROW-LOGIC-20z", "EC-BRW-121", "EC-BRW-122", "EC-BRW-123", "EC-BRW-124", "EC-BRW-125", "EC-BRW-135", "EC-BRW-136", "EC-BRW-141", "EC-BRW-142", "EC-BRW-143", "EC-BRW-144", "EC-BRW-34", "EC-BRW-85", "EC-BRW-86", "EC-BRW-87", "EC-BRW-88", "F-BORROW-11.k1", "F-BORROW-11.k2", "F-BORROW-11.k3", "F-BORROW-11.k4", "§10#r4"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-13aa": [67]
  "BORROW-LOGIC-13b": [63, 164, 165]
  "BORROW-LOGIC-13c": [57, 71]
  "BORROW-LOGIC-13d": [58, 76]
  "BORROW-LOGIC-13e": [78]
  "BORROW-LOGIC-13f": [61]
  "BORROW-LOGIC-13g": [69, 89]
  "BORROW-LOGIC-13h": [80]
  "BORROW-LOGIC-13i": [71]
  "BORROW-LOGIC-13j": [82, 84, 167]
  "BORROW-LOGIC-13k": [89, 91]
  "BORROW-LOGIC-13l": [89, 91]
  "BORROW-LOGIC-13m": [100, 111]
  "BORROW-LOGIC-13n": [109, 111]
  "BORROW-LOGIC-13o": [112]
  "BORROW-LOGIC-13p": [105, 107, 175, 177]
  "BORROW-LOGIC-13q": [142]
  "BORROW-LOGIC-13r": [86, 87]
  "BORROW-LOGIC-13s": [33, 35, 39, 74, 169, 173, 175, 179]
  "BORROW-LOGIC-13t": [59]
  "BORROW-LOGIC-13u": [60]
  "BORROW-LOGIC-13v": [62]
  "BORROW-LOGIC-13w": [72]
  "BORROW-LOGIC-13x": [69]
  "BORROW-LOGIC-13y": [64]
  "BORROW-LOGIC-13z": [65]
  "BORROW-LOGIC-20aa": [111]
  "BORROW-LOGIC-20b": [114]
  "BORROW-LOGIC-20c": [5, 6]
  "BORROW-LOGIC-20d": [120, 124]
  "BORROW-LOGIC-20e": [124]
  "BORROW-LOGIC-20f": [118, 120]
  "BORROW-LOGIC-20g": [121]
  "BORROW-LOGIC-20h": [116]
  "BORROW-LOGIC-20i": [125, 192, 194, 196, 198]
  "BORROW-LOGIC-20j": [126]
  "BORROW-LOGIC-20k": [120]
  "BORROW-LOGIC-20l": [121, 122]
  "BORROW-LOGIC-20m": [105, 175, 177]
  "BORROW-LOGIC-20n": [111]
  "BORROW-LOGIC-20o": [105, 107, 175, 177]
  "BORROW-LOGIC-20p": [145, 201]
  "BORROW-LOGIC-20q": [147]
  "BORROW-LOGIC-20r": [151]
  "BORROW-LOGIC-20s": [158, 162]
  "BORROW-LOGIC-20t": [128]
  "BORROW-LOGIC-20u": [130]
  "BORROW-LOGIC-20v": [132]
  "BORROW-LOGIC-20w": [134]
  "BORROW-LOGIC-20x": [138]
  "BORROW-LOGIC-20y": [136, 140]
  "BORROW-LOGIC-20z": [142]
  "EC-BRW-121": [2, 3, 11]
  "EC-BRW-122": [25, 35]
  "EC-BRW-123": [27, 28, 29, 171]
  "EC-BRW-124": [13, 14, 15, 181, 182]
  "EC-BRW-125": [17, 19, 21, 23]
  "EC-BRW-135": [100, 112, 113]
  "EC-BRW-136": [101, 103, 184, 186]
  "EC-BRW-141": [43, 44, 46, 47]
  "EC-BRW-142": [49, 50, 51]
  "EC-BRW-143": [54, 55]
  "EC-BRW-144": [31, 33, 35, 37, 39, 41, 173, 188, 190]
  "EC-BRW-34": [95]
  "EC-BRW-85": [97, 98]
  "EC-BRW-86": [144, 145, 147, 149, 200, 201, 203, 206]
  "EC-BRW-87": [151, 152, 154, 155, 156]
  "EC-BRW-88": [158, 159, 161]
  "F-BORROW-11.k1": [31, 57, 95]
  "F-BORROW-11.k2": [25, 27, 28, 29, 31, 33, 35, 37, 39, 171, 173, 188, 190]
  "F-BORROW-11.k3": [57, 58, 101]
  "F-BORROW-11.k4": [91, 97, 98]
  "§10#r4": [4, 8, 114]
---

# Self-service Borrow Now, Borrower tanpa akun login dengan PIC, dan aturan Return self-service

## Prerequisites
- Aktor: `Dewi Lestari {runId}` (Borrower ber-akun, bukan Aktor Borrow); `Bagus Santoso {runId}` (Borrower ber-akun); `Agus Pratama {runId}` (Aktor Borrow, Asset Admin pada Group `Head Office {runId}`); `Siti Aminah {runId}` (Group Manager Group `Head Office {runId}`); `Rina Kusuma {runId}` (PIC); `Nanda Pratiwi {runId}` (PIC); `Hendra Wijaya {runId}` (Borrower ber-akun).
- Data:
  - DU-082-1: Group asal aset: Name `Head Office {runId}`
  - DU-082-2: Group di luar cakupan Aktor Borrow: Name `Branch Surabaya {runId}`
  - DU-082-3: User akun login: Name `Dewi Lestari {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-082-4: User akun login: Name `Agus Pratama {runId}`, Status `Active`, Activation Status `Activated`, Role `Asset Admin`, Group penugasan `Head Office {runId}`, Division `Operations`
  - DU-082-5: User akun login: Name `Siti Aminah {runId}`, Status `Active`, Activation Status `Activated`, Role `Group Manager`, Group binaan `Head Office {runId}`, Division `Operations`
  - DU-082-6: User akun login: Name `Bagus Santoso {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-082-7: User akun login: Name `Rina Kusuma {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-082-8: User akun login: Name `Maya Putri {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-082-9: User akun login: Name `Eko Prasetyo {runId}`, Status `Inactive`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Marketing`
  - DU-082-10: Karyawan tanpa akun login: Name `Gita Anggraini {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-082-11: Karyawan tanpa akun login: Name `Budi Santoso {runId}`, Status `Active`, Division `Finance`, PIC `Maya Putri {runId}`
  - DU-082-12: Karyawan tanpa akun login: Name `Lia Wulandari {runId}`, Status `Active`, Division `Finance`, PIC `(kosong)`
  - DU-082-13: Karyawan tanpa akun login: Name `Tono Hartono {runId}`, Status `Active`, Division `Finance`, PIC `Eko Prasetyo {runId}`
  - DU-082-14: User akun login: Name `Fajar Nugroho {runId}`, Status `Active`, Activation Status `Pending Activation`, Role `Karyawan biasa bukan Aktor Borrow`
  - DU-082-15: User akun login: Name `Hana Permata {runId}`, Status `Active`, Activation Status `Pending Email Confirmation`, Role `Karyawan biasa bukan Aktor Borrow`
  - DU-082-16: User akun login: Name `Irfan Hakim {runId}`, Status `Inactive`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`
  - DU-082-17: Karyawan tanpa akun login: Name `Citra Dewanti {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-082-18: Karyawan tanpa akun login: Name `Dian Sastro {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-082-19: Karyawan tanpa akun login: Name `Ratna Sari {runId}`, Status `Active`, Division `Finance`, PIC `Rina Kusuma {runId}`
  - DU-082-20: Aset tersedia: Asset Name `Laptop Dell Latitude 5440 {runId}`, Group `Head Office {runId}`, Category `Laptop`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Require approval `ON`, Approval type `All`, Max duration `7`, Max assets per borrower `10`
  - DU-082-21: Aset tersedia: Asset Name `Kamera Canon EOS 90D {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max duration `7`, Max assets per borrower `10`
  - DU-082-22: Aset tersedia: Asset Name `Proyektor Epson EB-X49 {runId}`, Group `Head Office {runId}`, Category `Projector`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Hours`, Max duration `8`, Max assets per borrower `10`
  - DU-082-23: Aset tersedia: Asset Name `Tripod Manfrotto MT055 {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max duration `7`
  - DU-082-24: Aset tersedia: Asset Name `Mikrofon Shure SM58 {runId}`, Group `Head Office {runId}`, Category `Audio`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Allowed borrower `Division Marketing`, Max duration `7`
  - DU-082-25: Aset tersedia: Asset Name `Printer Epson L3250 {runId}`, Group `Head Office {runId}`, Category `Printer`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`
  - DU-082-26: Aset tersedia: Asset Name `Scanner Fujitsu fi-8170 {runId}`, Group `Head Office {runId}`, Category `Scanner`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Allow Borrow `Deny pada override aset`
  - DU-082-27: Aset tersedia: Asset Name `Drone DJI Mavic 3 {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Activity Lock `In Audit`
  - DU-082-28: Aset tersedia: Asset Name `Kompor Induksi Philips {runId}`, Group `Head Office {runId}`, Category `Appliance`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Activity Lock `Under Maintenance`
  - DU-082-29: Aset tersedia: Asset Name `Headset Logitech H390 {runId}`, Group `Head Office {runId}`, Category `Audio`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max assets per borrower `1`
  - DU-082-30: Aset tersedia: Asset Name `Meja Rapat Kayu Jati {runId}`, Group `Head Office {runId}`, Category `Furniture`, TAG `Non TAG`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Allowed borrower `Division Marketing`
  - DU-082-31: Aset tersedia: Asset Name `Kursi Ergonomis Ergotec {runId}`, Group `Head Office {runId}`, Category `Furniture`, TAG `Non TAG`, Custody `In Borrow Process`, Condition `Normal`, Self service `ON`, Satuan `Days`
  - DU-082-32: Aset tersedia: Asset Name `Papan Tulis Magnetik {runId}`, Group `Head Office {runId}`, Category `Furniture`, TAG `Non TAG`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max assets per borrower `1`
  - DU-082-33: Aset tersedia: Asset Name `Bor Listrik Bosch GSB 13 {runId}`, Group `Head Office {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max duration `7`, Max assets per borrower `10`
  - DU-082-34: Aset tersedia: Asset Name `Handycam Sony FDR-AX43 {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max duration `7`, Max assets per borrower `10`
  - DU-082-35: Aset di Group lain: Asset Name `Mesin Bor Pasir Makita {runId}`, Group `Branch Surabaya {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`
  - DU-082-36: Aset tersedia: Asset Name `Pengeras Suara Yamaha {runId}`, Group `Head Office {runId}`, Category `Audio`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Require approval `OFF`, Max duration `7`
  - DU-082-37: Aset tersedia: Asset Name `Genset Honda EU22i {runId}`, Group `Head Office {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `OFF`, Satuan `Days`, Require approval `ON`, Approval type `Any one`, Approver `Siti Aminah {runId}`, Max duration `7`
  - DU-082-38: Aset tersedia: Asset Name `Lensa Canon RF 24-70 {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Require approval `OFF`, Max duration `7`
  - DU-082-39: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Tablet Samsung Galaxy Tab S9 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`
  - DU-082-40: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Speaker JBL PartyBox 310 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`
  - DU-082-41: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Monitor LG UltraFine 27 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Max extensions `2`, Max duration `7`
  - DU-082-42: Pinjaman berjalan: Borrower `Bagus Santoso {runId}`, Aset `Kamera Sony A7 III {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, TAG `Non TAG`, Max assets per borrower `1`
  - DU-082-43: Pinjaman berjalan: Borrower `Rina Kusuma {runId}`, Aset `Charger Anker 737 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Source `Admin`, Self service pada snapshot baris `ON`, Max extensions `2`
  - DU-082-44: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Lampu Studio Godox SL60 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Source `Admin`, PIC `Rina Kusuma {runId}`
  - DU-082-45: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Kamera Fujifilm X-T30 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Source `Admin`, PIC `Rina Kusuma {runId}`
  - DU-082-46: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Mixer Yamaha MG10 {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Source `Admin`, PIC `Rina Kusuma {runId}`
  - DU-082-47: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Rina Kusuma {runId}`, Self service `OFF`, Max extensions `2`, Max duration `7`, Duration berjalan `3 Days sejak handover`, Extension terpakai `0`
  - DU-082-48: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Tablet Apple iPad Air {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Rina Kusuma {runId}`
  - DU-082-49: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Laptop HP EliteBook 840 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Rina Kusuma {runId}`
  - DU-082-50: Pinjaman berjalan: Borrower `Gita Anggraini {runId}`, Aset `Kamera DJI Osmo Pocket 3 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, PIC `Rina Kusuma {runId}`
  - DU-082-51: Pinjaman berjalan: Borrower `Citra Dewanti {runId}`, Aset `Bor Makita HP1630 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Rina Kusuma {runId}`, Due date `T0 + 1 hari`
  - DU-082-52: Pinjaman berjalan: Borrower `Dian Sastro {runId}`, Aset `Gerinda Bosch GWS 060 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Rina Kusuma {runId}`, Due date `T0 + 1 hari`, Dikonfirmasi handover oleh `Rina Kusuma {runId}`, Notifikasi terkirim sebelum penggantian PIC `Pengingat Due date D-1 ke Rina Kusuma {runId}`, Pengingat Due date berikutnya `D-day pada tanggal Due date`
  - DU-082-53: Pinjaman berjalan: Borrower `Ratna Sari {runId}`, Aset `Obeng Set Tekiro {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Source `Admin`, PIC `Rina Kusuma {runId}`
  - DU-082-57: User akun login: Name `Nanda Pratiwi {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-082-58: User akun login: Name `Bayu Saputra {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow, PIC`, Division `Marketing`
  - DU-082-59: User akun login: Name `Joko Susilo {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`, Temporary Until `T0 - 1 hari`
  - DU-082-60: User akun login: Name `Hendra Wijaya {runId}`, Status `Active`, Activation Status `Activated`, Role `Karyawan biasa bukan Aktor Borrow`, Division `Finance`
  - DU-082-61: Karyawan tanpa akun login: Name `Wulan Safitri {runId}`, Status `Active`, Division `Finance`, PIC `Nanda Pratiwi {runId}`
  - DU-082-62: Karyawan tanpa akun login: Name `Yoga Pratama {runId}`, Status `Active`, Division `Finance`, PIC `Nanda Pratiwi {runId}`
  - DU-082-63: Karyawan tanpa akun login: Name `Tari Utami {runId}`, Status `Active`, Division `Finance`, PIC `Nanda Pratiwi {runId}`
  - DU-082-64: Karyawan tanpa akun login: Name `Fani Lestari {runId}`, Status `Active`, Division `Finance`, PIC `Bayu Saputra {runId}`
  - DU-082-65: Aset tersedia: Asset Name `Mesin Label Brother PT-P710 {runId}`, Group `Head Office {runId}`, Category `Office`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Require approval `ON`, Auto-approve `Auto (≤ 3 days)`, Approval type `Any one`, Max duration `7`, Max assets per borrower `10`
  - DU-082-66: Aset tersedia: Asset Name `Gimbal DJI RS 3 {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Photo at start `ON`, Max duration `7`, Max assets per borrower `10`
  - DU-082-67: Aset tersedia: Asset Name `Power Bank Anker 20K {runId}`, Group `Head Office {runId}`, Category `Electronics`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max duration `7`, Max assets per borrower `1`
  - DU-082-68: Aset tersedia: Asset Name `Kipas Angin Cosmos {runId}`, Group `Head Office {runId}`, Category `Appliance`, TAG `Non TAG`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Block new borrow when overdue `ON`, Max assets per borrower `10`
  - DU-082-69: Aset tersedia: Asset Name `Dispenser Miyako {runId}`, Group `Head Office {runId}`, Category `Appliance`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Block new borrow when overdue `ON`, Max assets per borrower `10`
  - DU-082-70: Aset tersedia: Asset Name `Rice Cooker Philips {runId}`, Group `Head Office {runId}`, Category `Appliance`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Block new borrow when overdue `ON`, Max assets per borrower `10`
  - DU-082-71: Aset tersedia: Asset Name `Lampu Ring Neewer 18 {runId}`, Group `Head Office {runId}`, Category `Camera`, TAG `Ber-tag`, Custody `Available`, Condition `Normal`, Self service `ON`, Satuan `Days`, Max duration `7`, Max assets per borrower `10`
  - DU-082-72: Aset tersedia: Asset Name `Heat Gun Bosch GHG 20 {runId}`, Group `Head Office {runId}`, Category `Tools`, TAG `Ber-tag`, Custody `Borrowed`, Condition `Normal`, Self service `ON`, Satuan `Days`
  - DU-082-73: Aset tersedia: Asset Name `Oven Listrik Maspion {runId}`, Group `Head Office {runId}`, Category `Appliance`, TAG `Ber-tag`, Custody `In Borrow Process`, Condition `Normal`, Self service `ON`, Satuan `Days`, Activity Lock `In Audit`
  - DU-082-74: Pinjaman berjalan: Borrower `Wulan Safitri {runId}`, Aset `Charger Laptop Baseus {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Nanda Pratiwi {runId}`
  - DU-082-75: Pinjaman berjalan: Borrower `Yoga Pratama {runId}`, Aset `Setrika Philips {runId}`, Group `Head Office {runId}`, Status baris `Overdue`, Source `Admin`, PIC `Nanda Pratiwi {runId}`, Due date `T0 - 2 hari`
  - DU-082-76: Pinjaman berjalan: Borrower `Hendra Wijaya {runId}`, Aset `Kabel Roll Eterna {runId}`, Group `Head Office {runId}`, Status baris `Overdue`, Source `Admin`, Due date `T0 - 2 hari`
  - DU-082-77: Pinjaman berjalan: Borrower `Siti Aminah {runId}`, Aset `Heat Gun Bosch GHG 20 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`
  - DU-082-78: Pinjaman berjalan: Borrower `Siti Aminah {runId}`, Aset `Oven Listrik Maspion {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Handover`, Source `Admin`
  - DU-082-79: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Webcam Logitech C920 {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Max extensions `2`, Max duration `7`, Duration berjalan `2 Days sejak handover`, Extension terpakai `0`
  - DU-082-80: Pinjaman berjalan: Borrower `Dewi Lestari {runId}`, Aset `Lampu Belajar Philips {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Self-service`, Max extensions `1`, Max duration `7`, Duration berjalan `2 Days sejak handover`, Extension terpakai `1`
  - DU-082-81: Pinjaman berjalan: Borrower `Tari Utami {runId}`, Aset `Mesin Las Krisbow {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Approval`, Source `Admin`, PIC `Nanda Pratiwi {runId}`, Require approval `ON`, Approval type `Any one`, Approver `Siti Aminah {runId}`, Self service `OFF`
  - DU-082-82: Pinjaman berjalan: Borrower `Tari Utami {runId}`, Aset `Gerinda Tangan Makita {runId}`, Group `Head Office {runId}`, Status baris `Waiting for Approval`, Source `Admin`, PIC `Nanda Pratiwi {runId}`, Require approval `ON`, Approval type `Any one`, Approver `Siti Aminah {runId}`, Self service `OFF`
  - DU-082-83: Pinjaman berjalan: Borrower `Tari Utami {runId}`, Aset `Troli Barang Lakoni {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Nanda Pratiwi {runId}`, Self service `OFF`, Max extensions `2`, Max duration `7`, Extension Request `menunggu review Aktor Borrow, Extend by 1, Reason Proyek belum selesai`
  - DU-082-84: Pinjaman berjalan: Borrower `Tari Utami {runId}`, Aset `Mic Wireless Sennheiser {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Nanda Pratiwi {runId}`, Due date `T0 + 1 hari`
  - DU-082-85: Pinjaman berjalan: Borrower `Fani Lestari {runId}`, Aset `Gergaji Mesin Stihl {runId}`, Group `Head Office {runId}`, Status baris `Borrowed`, Source `Admin`, PIC `Bayu Saputra {runId}`, Due date `T0 + 1 hari`
- Kondisi:
  - T0 adalah waktu permintaan Borrow Now dikirim; semua Due date dihitung relatif terhadap T0 menurut Time Zone General Settings penyewa.
  - Aset yang disebut self-service memakai Self service efektif `ON` pada override asetnya sendiri, kecuali disebut `OFF`; setiap aset punya Max assets per borrower yang dicatat di entri datanya.
  - Akun Dewi, Bagus, Rina, Maya, Agus, Siti, Nanda, dan Hendra aktif dan kredensialnya tersedia untuk fase 2.
  - Akun login yang dibuat untuk `Ratna Sari {runId}` berstatus `Active` dengan Activation Status `Activated`, dan kredensialnya tersedia untuk fase 2.
  - Aset yang memuat Block new borrow when overdue `ON`, Photo at start `ON`, Auto-approve, atau Max extensions memakainya pada override asetnya sendiri.

## Test Steps

### Select Borrower tidak menilai Allowed borrower dan memblokir karyawan tanpa PIC
1. Agus membuka pilihan Borrower pada form Borrow yang belum berisi aset
2. Verifikasi `Dewi Lestari {runId}` tidak `Blocked` walau Allowed borrower `Mikrofon Shure SM58 {runId}` tidak terpenuhi olehnya, karena Allowed borrower tidak dinilai di Select Borrower
3. Verifikasi `Lia Wulandari {runId}` tampil `Blocked` oleh status peminjamannya, yaitu tanpa PIC
4. Verifikasi setiap Borrower yang ditawarkan di Select Borrower adalah karyawan, ber-akun maupun tanpa akun, misalnya `Dewi Lestari {runId}` dan `Lia Wulandari {runId}`, karena peminjam eksternal yang bukan karyawan tidak didukung
5. Verifikasi karyawan tanpa akun `Lia Wulandari {runId}` yang PIC-nya kosong tampil di Select Borrower tetapi tidak bisa dipilih, dengan alasan `No login account and no PIC. Set a PIC in Users first.`
6. Verifikasi karyawan tanpa akun `Tono Hartono {runId}` yang PIC-nya nonaktif tampil di Select Borrower tetapi tidak bisa dipilih, dengan alasan `No login account and no PIC. Set a PIC in Users first.`
7. Agus mengirim Submit dengan Borrower `Lia Wulandari {runId}` atas `Laptop Dell Latitude 5440 {runId}`
8. Verifikasi Submit ditolak dengan pesan `Lia Wulandari {runId} has no login account and no PIC. Set a PIC in Users first.` dan tidak ada BRW yang dibuat
9. Agus memilih `Dewi Lestari {runId}` sebagai Borrower
10. Agus membuka daftar aset di Select Asset
11. Verifikasi daftar aset hanya menawarkan aset yang lolos untuk `Dewi Lestari {runId}`: `Laptop Dell Latitude 5440 {runId}` ada dan `Mikrofon Shure SM58 {runId}` tidak ada

### Karyawan ber-akun yang belum aktif tidak muncul di Select Borrower
12. Agus mencari Borrower di Select Borrower dengan Search `{runId}`
13. Verifikasi `Fajar Nugroho {runId}` dengan Activation Status `Pending Activation` tidak muncul di Select Borrower
14. Verifikasi `Hana Permata {runId}` dengan Activation Status `Pending Email Confirmation` tidak muncul di Select Borrower
15. Verifikasi `Irfan Hakim {runId}` yang Status-nya bukan `Active` tidak muncul di Select Borrower

### Aktor Borrow memilih dirinya sendiri sebagai Borrower
16. Agus mengirim Submit dengan Borrower dirinya sendiri, `Agus Pratama {runId}`, atas `Pengeras Suara Yamaha {runId}` dengan Duration `1` Days dan Purpose `Acara gathering tahunan`
17. Verifikasi pengajuan atas nama `Agus Pratama {runId}` sendiri diterima dan barisnya `Waiting for Handover`
18. Agus menyelesaikan Handover atas `Pengeras Suara Yamaha {runId}` dengan scan TAG
19. Verifikasi Handover yang diproses Agus sendiri diterima dan barisnya `Borrowed`
20. Agus menyelesaikan Return atas `Pengeras Suara Yamaha {runId}` dengan scan TAG
21. Verifikasi Return yang diproses Agus sendiri diterima dan barisnya `Returned`
22. Agus mengirim Submit dengan Borrower dirinya sendiri atas `Genset Honda EU22i {runId}` dengan Duration `3` Days dan Purpose `Cadangan listrik pameran`
23. Verifikasi `Agus Pratama {runId}` tidak ada di daftar approver eligible untuk pengajuan itu, sedangkan `Siti Aminah {runId}` ada

### Aset yang tidak memenuhi syarat self-service tidak dimuat atau ditandai Not ready
24. Dewi membuka daftar aset yang dapat dipinjam sendiri
25. Verifikasi `Meja Rapat Kayu Jati {runId}` yang Non TAG dan ber-Self service `ON` tetapi Allowed borrower-nya tidak dipenuhi `Dewi Lestari {runId}` tidak tampil di daftar
26. Bagus membuka daftar aset yang dapat dipinjam sendiri
27. Verifikasi `Kursi Ergonomis Ergotec {runId}` dengan Custody `In Borrow Process` tidak dimuat
28. Verifikasi `Kamera Sony A7 III {runId}` yang sedang dipinjam `Bagus Santoso {runId}` sendiri tidak dimuat
29. Verifikasi `Papan Tulis Magnetik {runId}` tampil `Not ready` dengan alasan `Bagus Santoso {runId} can borrow up to 1 assets at a time.` dan tidak bisa dicentang

### Scan TAG aset yang tidak dapat dipinjam sendiri ditolak
30. Dewi memindai TAG `Printer Epson L3250 {runId}` pada Borrow an Asset
31. Verifikasi aset tidak ditambahkan dan ditolak dengan pesan `Error, this asset can't be borrowed on your own.` karena Self service-nya `OFF`
32. Dewi memindai TAG `Scanner Fujitsu fi-8170 {runId}` pada Borrow an Asset
33. Verifikasi aset tidak ditambahkan dan ditolak dengan pesan `Error, this asset can't be borrowed on your own.` karena Allow Borrow-nya Deny
34. Dewi memindai TAG `Mikrofon Shure SM58 {runId}` pada Borrow an Asset
35. Verifikasi aset tidak ditambahkan dan ditolak dengan pesan `Error, this asset can't be borrowed on your own.` karena Allowed borrower tidak terpenuhi
36. Dewi memindai TAG `Drone DJI Mavic 3 {runId}` pada Borrow an Asset
37. Verifikasi aset tidak ditambahkan dan ditolak dengan alasan berprioritas tertinggi `This asset is In Audit and can't be borrowed.`
38. Bagus memindai TAG `Headset Logitech H390 {runId}` pada Borrow an Asset
39. Verifikasi aset tidak ditambahkan dan ditolak dengan pesan Borrower `Bagus Santoso {runId} can borrow up to 1 assets at a time.`
40. Dewi memindai TAG `Laptop Dell Latitude 5440 {runId}` pada Borrow an Asset
41. Verifikasi scan berikutnya tetap dapat dilakukan sesudah penolakan: `Laptop Dell Latitude 5440 {runId}` ditambahkan

### Mobile Scan Borrow oleh Aktor Borrow menolak aset tidak layak dan aset di luar cakupan Group
42. Agus memindai TAG `Kompor Induksi Philips {runId}` pada Scan > Borrow
43. Verifikasi `[Borrow]` tidak tersedia untuk aset itu dengan alasan `This asset is Under Maintenance and can't be borrowed.`
44. Verifikasi wizard Borrow tidak terbuka untuk aset yang tidak layak itu
45. Agus memindai TAG `Mesin Bor Pasir Makita {runId}` yang berada di Group `Branch Surabaya {runId}`
46. Verifikasi pesan scan `This asset belongs to Branch Surabaya {runId}.` diberikan
47. Verifikasi identitas, foto, dan atribut aset itu tidak diberikan dan `[Borrow]` tidak tersedia

### Submit memblokir aset yang tidak lolos Borrower dan aset yang diambil BRW lain
48. Agus mengirim Submit dengan Borrower `Dewi Lestari {runId}` atas `Laptop Dell Latitude 5440 {runId}` dan `Mikrofon Shure SM58 {runId}`
49. Verifikasi hanya `Mikrofon Shure SM58 {runId}` ditandai `This asset can no longer be borrowed.`, sedangkan `Laptop Dell Latitude 5440 {runId}` tidak ditandai
50. Verifikasi alasan tunggal untuk `Mikrofon Shure SM58 {runId}` adalah `Dewi Lestari {runId} can't borrow assets from Head Office {runId}.`
51. Verifikasi Submit ditolak dan tidak ada BRW yang dibuat selama `Mikrofon Shure SM58 {runId}` masih ada di pengajuan
52. Siti mengirim Submit dengan Borrower `Rina Kusuma {runId}` atas `Lensa Canon RF 24-70 {runId}`
53. Agus mengirim Submit dengan Borrower `Dewi Lestari {runId}` atas `Lensa Canon RF 24-70 {runId}`
54. Verifikasi alasan penolakan aset yang diambil BRW lain adalah `This asset is already in another transaction.`
55. Verifikasi Submit Agus ditolak dan tidak ada BRW yang dibuat sampai aset itu dikeluarkan dari pengajuan

### Borrow Now self-service atas aset Days langsung Borrowed
56. Dewi mengirim Borrow Now atas `Laptop Dell Latitude 5440 {runId}` dengan scan TAG, Duration `3` Days, dan Purpose `Presentasi klien` pada T0, yaitu waktu Borrow Now dikirim
57. Verifikasi baris pinjaman langsung `Borrowed` begitu Borrow Now diterima, setelah scan TAG, Duration, dan Purpose dipenuhi
58. Verifikasi Due date baris adalah tanggal T0 ditambah 2 hari pukul 23:59:59 menurut Time Zone General Settings penyewa, yaitu tanggal Borrow Now ditambah (Duration − 1) hari
59. Verifikasi Handed Over At baris sama dengan waktu T0 Borrow Now, bukan waktu handover
60. Verifikasi hasil Borrow Now memuat Due date yang sama dengan Due date baris tersimpan untuk `Return by [Date]`
61. Verifikasi riwayat status baris tidak memuat `Waiting for Handover`
62. Verifikasi pemberi pada baris tercatat `Self-service`
63. Verifikasi baris tidak melalui pengajuan approval walau Require approval aset `ON` dengan Approval type `All`
64. Verifikasi tidak ada task `Pick up` bagi `Dewi Lestari {runId}` atas baris itu
65. Verifikasi tidak ada permintaan konfirmasi Borrower atas baris itu
66. Job Transaction timeout berjalan setelah Transaction timeout sejak T0 terlewati
67. Verifikasi baris tetap `Borrowed` dan tidak ditutup dengan alasan `Not picked up`
68. Dewi mengirim Cancel Borrow atas baris `Laptop Dell Latitude 5440 {runId}`
69. Verifikasi Cancel Borrow ditolak dan baris tetap `Borrowed`, karena pinjaman yang sudah `Borrowed` hanya diakhiri lewat Return

### Borrow Now tanpa scan TAG dan melebihi Max duration ditolak, Duration 1 hari jatuh di hari yang sama
70. Dewi mengirim Borrow Now atas `Kamera Canon EOS 90D {runId}` tanpa scan TAG dengan Duration `2` Days dan Purpose `Liputan seminar`
71. Verifikasi permintaan ditolak karena aset ber-tag wajib scan TAG, yaitu bukti bahwa Borrower memegang asetnya
72. Verifikasi tidak ada baris pinjaman atau reservasi atas `Kamera Canon EOS 90D {runId}` dan Custody tetap `Available`
73. Dewi mengirim Borrow Now atas `Kamera Canon EOS 90D {runId}` dengan scan TAG, Duration `10` Days, dan Purpose `Dokumentasi acara`
74. Verifikasi permintaan ditolak dengan pesan `Max. 7 Days for Camera`
75. Dewi mengirim Borrow Now atas `Kamera Canon EOS 90D {runId}` dengan scan TAG, Duration `1` Days, dan Purpose `Dokumentasi acara` pada T0
76. Verifikasi Due date baris jatuh pada tanggal T0 yang sama pukul 23:59:59, karena `1 day` berarti kembali hari yang sama

### Borrow Now atas aset Hours
77. Dewi mengirim Borrow Now atas `Proyektor Epson EB-X49 {runId}` dengan scan TAG, Duration `4` Hours, dan Purpose `Rapat divisi` pada jam T0
78. Verifikasi Due date baris adalah jam T0 ditambah 4 jam

### Memulai self-service dari web ditolak server
79. Dewi mengirim Borrow Now atas `Tripod Manfrotto MT055 {runId}` dari web dengan Duration `2` Days dan Purpose `Survei lapangan`
80. Verifikasi permintaan ditolak dan tidak ada baris pinjaman atas `Tripod Manfrotto MT055 {runId}`

### Pinjaman self-service terbaca, dapat di-Extend, dan ditandai Source
81. Dewi membaca daftar Borrowed miliknya dari web dan dari mobile
82. Verifikasi pinjaman self-service atas `Monitor LG UltraFine 27 {runId}` terbaca `Dewi Lestari {runId}` di web dan di mobile
83. Dewi mengajukan Extend atas `Monitor LG UltraFine 27 {runId}` dari web dengan Extend by `1` dan Reason `Perlu dipakai satu hari lagi`
84. Verifikasi permintaan Extend atas pinjaman self-service diterima
85. Agus menyaring daftar transaksi Borrow dengan Source `Self-service`
86. Verifikasi baris pinjaman `Dewi Lestari {runId}` atas `Monitor LG UltraFine 27 {runId}` memuat Source `Self-service` pada kolom dan lolos filter itu
87. Verifikasi pinjaman yang sama ditandai Source `Self-service` di daftar pinjaman `Dewi Lestari {runId}`

### Return pinjaman self-service oleh Borrower atau diterima Aktor Borrow Group asal
88. Dewi menjalankan Return atas `Tablet Samsung Galaxy Tab S9 {runId}` dari web dengan scan TAG lewat reader
89. Verifikasi baris `Tablet Samsung Galaxy Tab S9 {runId}` menjadi `Returned`
90. Agus menerima Return atas `Speaker JBL PartyBox 310 {runId}` yang dititipkan Dewi di Group asal
91. Verifikasi baris `Speaker JBL PartyBox 310 {runId}` menjadi `Returned` setelah diterima Aktor Borrow Group asal

### Self service dimatikan sesudah baris Waiting for Handover
92. Self service pada `Charger Anker 737 {runId}` dimatikan sesudah baris `Rina Kusuma {runId}` berstatus `Waiting for Handover`
93. Agus menyelesaikan Handover atas `Charger Anker 737 {runId}` dengan konfirmasi `Rina Kusuma {runId}`
94. Rina mengajukan Extend atas `Charger Anker 737 {runId}` dengan Extend by `1` dan Reason `Dipakai sampai akhir pekan`
95. Verifikasi Extend langsung berlaku tanpa review Aktor Borrow, karena baris tetap memakai snapshot Self service `ON`

### Dua pengguna memindai aset yang sama hampir bersamaan
96. Dewi dan Rina mengirim Borrow Now atas `Bor Listrik Bosch GSB 13 {runId}` hampir bersamaan dengan Duration `2` Days dan Purpose `Perbaikan rak gudang`
97. Verifikasi tepat satu dari dua permintaan menghasilkan baris `Borrowed` atas `Bor Listrik Bosch GSB 13 {runId}`
98. Verifikasi permintaan yang lain ditolak dengan pesan `This asset was just borrowed by someone else.` dan tidak menghasilkan baris

### PIC memilih Borrow for karyawan tanpa akun dan batas dihitung untuk Borrower
99. Rina membuka pilihan `Borrow for`
100. Verifikasi `Gita Anggraini {runId}` yang PIC-nya `Rina Kusuma {runId}` tampil di pilihan `Borrow for`
101. Verifikasi `Budi Santoso {runId}`, `Lia Wulandari {runId}`, dan `Tono Hartono {runId}` tidak muncul di pilihan `Borrow for`
102. Rina mengirim Borrow Now atas nama `Budi Santoso {runId}` atas `Handycam Sony FDR-AX43 {runId}`
103. Verifikasi permintaan atas nama karyawan yang PIC-nya orang lain ditolak server
104. Rina mengirim Borrow Now atas nama `Gita Anggraini {runId}` atas `Mikrofon Shure SM58 {runId}` dengan scan TAG, Duration `2` Days, dan Purpose `Rekaman podcast`
105. Verifikasi permintaan ditolak karena Allowed borrower dinilai untuk `Gita Anggraini {runId}`, bukan untuk PIC `Rina Kusuma {runId}` yang memenuhinya
106. Rina mengirim Borrow Now atas nama `Gita Anggraini {runId}` atas `Handycam Sony FDR-AX43 {runId}` dengan scan TAG, Duration `10` Days, dan Purpose `Liputan peresmian kantor`
107. Verifikasi permintaan ditolak dengan pesan `Max. 7 Days for Camera` karena Max duration dinilai untuk Borrower
108. Rina mengirim Borrow Now atas nama `Gita Anggraini {runId}` atas `Handycam Sony FDR-AX43 {runId}` dengan scan TAG, Duration `2` Days, dan Purpose `Dokumentasi kunjungan` tanpa pernyataan Confirm Receipt
109. Verifikasi permintaan tanpa pernyataan Confirm Receipt oleh PIC ditolak
110. Rina mengirim Borrow Now atas nama `Gita Anggraini {runId}` atas `Handycam Sony FDR-AX43 {runId}` dengan scan TAG, Duration `2` Days, dan Purpose `Liputan peresmian kantor`, disertai pernyataan Confirm Receipt bahwa Gita hadir dan menerima aset
111. Verifikasi PIC dapat meminjam self-service untuk karyawan tanpa akun yang PIC-nya dirinya, dan permintaan yang disertai pernyataan Confirm Receipt diterima
112. Verifikasi Borrower pada baris adalah `Gita Anggraini {runId}`, bukan `Rina Kusuma {runId}`, dengan Source `Self-service`
113. Verifikasi baris tampil di daftar pinjaman `Rina Kusuma {runId}` sebagai PIC dengan penanda `On behalf of Gita Anggraini {runId}`
114. Verifikasi PIC pada baris adalah `Rina Kusuma {runId}` menurut master data Users dan tidak dipilih per transaksi

### Konfirmasi handover Borrower tanpa akun oleh PIC dan oleh admin
115. Rina mengirim permintaan Accept atas handover `Kamera Fujifilm X-T30 {runId}` dengan mengklaim sebagai Borrower `Gita Anggraini {runId}`, yang tidak punya akun login
116. Verifikasi Accept ditolak karena Borrower tanpa akun, dan baris tetap `Waiting for Handover`
117. Rina mengirim Confirm Handover atas `Kamera Fujifilm X-T30 {runId}` dari daftar pinjaman Borrower tanpa pernyataan
118. Verifikasi Confirm Handover tanpa pernyataan `I confirm that Gita Anggraini {runId} has received the checked assets.` ditolak dan baris tetap `Waiting for Handover`
119. Rina mengirim Confirm Handover atas `Kamera Fujifilm X-T30 {runId}` dari daftar pinjaman Borrower dengan checklist aset dan pernyataan `I confirm that Gita Anggraini {runId} has received the checked assets.`
120. Verifikasi PIC dapat mengonfirmasi handover dari daftar pinjaman Borrower: baris `Kamera Fujifilm X-T30 {runId}` menjadi `Borrowed`
121. Verifikasi konfirmasi dicatat `Confirmed by Rina Kusuma {runId} on behalf of Gita Anggraini {runId}`
122. Verifikasi pencatatan dari daftar pinjaman Borrower memuat `by Rina Kusuma {runId} on behalf of Gita Anggraini {runId}`
123. Agus menyelesaikan Handover atas `Lampu Studio Godox SL60 {runId}` dengan `Confirm on This Device` atas pernyataan admin bahwa `Gita Anggraini {runId}` menerima aset
124. Verifikasi konfirmasi lewat `Confirm on This Device` diterima dan baris `Lampu Studio Godox SL60 {runId}` menjadi `Borrowed`
125. Verifikasi notifikasi handover selesai yang ditujukan ke Borrower dikirim ke PIC `Rina Kusuma {runId}`
126. Verifikasi notifikasi itu memuat penanda atas nama `Gita Anggraini {runId}` yang diwakili PIC

### PIC bertindak atas nama Borrower dari daftar pinjaman Borrower
127. Rina mengirim Cancel Borrow atas `Mixer Yamaha MG10 {runId}` dari daftar pinjaman Borrower
128. Verifikasi baris `Mixer Yamaha MG10 {runId}` menjadi `Canceled`
129. Rina mengajukan Extend atas `Laptop Lenovo ThinkPad T14 {runId}` dari daftar pinjaman Borrower dengan Extend by `1` dan Reason `Proyek belum selesai`
130. Verifikasi permintaan Extend dari PIC atas nama Borrower diterima dan pengajuan Extension menunggu
131. Rina mengirim Cancel Extension atas `Laptop Lenovo ThinkPad T14 {runId}` dari daftar pinjaman Borrower
132. Verifikasi Cancel Extension dari PIC diterima dan Due date tidak berubah
133. Rina mengirim Report Damaged atas `Tablet Apple iPad Air {runId}` dari daftar pinjaman Borrower dengan satu foto dan What happened `Layar retak sesudah terjatuh`
134. Verifikasi laporan kerusakan dari PIC diterima dan record laporan berstatus `Waiting for Confirmation`
135. Rina mengirim Cancel Damage Report atas laporan yang ia ajukan atas nama `Gita Anggraini {runId}` untuk `Tablet Apple iPad Air {runId}`
136. Verifikasi Cancel Damage Report oleh PIC atas laporan yang ia ajukan diterima
137. Rina mengirim Report Missing atas `Laptop HP EliteBook 840 {runId}` dari daftar pinjaman Borrower dengan What happened `Aset tidak ditemukan di meja kerja`
138. Verifikasi laporan kehilangan dari PIC diterima dan record laporan berstatus `Waiting for Confirmation`
139. Rina mengirim Cancel Missing Report atas laporan yang ia ajukan atas nama `Gita Anggraini {runId}` untuk `Laptop HP EliteBook 840 {runId}`
140. Verifikasi Cancel Missing Report oleh PIC atas laporan yang ia ajukan diterima
141. Rina menjalankan Return self-service atas `Kamera DJI Osmo Pocket 3 {runId}` dari daftar pinjaman Borrower dengan scan TAG
142. Verifikasi baris `Kamera DJI Osmo Pocket 3 {runId}` menjadi `Returned` lewat Return self-service oleh PIC atas nama Borrower

### PIC dikosongkan saat pinjaman berjalan
143. PIC `Citra Dewanti {runId}` dikosongkan di Users saat pinjaman `Bor Makita HP1630 {runId}` berjalan
144. Verifikasi pinjaman tetap berjalan dengan status baris `Borrowed`
145. Verifikasi baris diberi penanda `No PIC`
146. Agus mengirim permintaan menunjuk PIC bagi `Citra Dewanti {runId}` dari Borrow
147. Verifikasi permintaan itu ditolak karena Borrow tidak memiliki aksi atau tugas menunjuk PIC
148. Job pengingat Due date harian berjalan
149. Verifikasi notifikasi untuk Borrower `Citra Dewanti {runId}` dialihkan ke Aktor Borrow Group asal `Agus Pratama {runId}` sampai PIC diisi

### PIC diganti di Users saat pinjaman berjalan
150. PIC `Dian Sastro {runId}` diganti dari `Rina Kusuma {runId}` menjadi `Maya Putri {runId}` di Users
151. Verifikasi pinjaman `Gerinda Bosch GWS 060 {runId}` pindah ke daftar pinjaman `Maya Putri {runId}`
152. Verifikasi `Rina Kusuma {runId}` tidak lagi melihat pinjaman itu
153. Job pengingat Due date harian berjalan pada tanggal Due date pinjaman `Gerinda Bosch GWS 060 {runId}`, saat pengingat D-day terbit
154. Verifikasi notifikasi berikutnya dikirim ke `Maya Putri {runId}`
155. Verifikasi notifikasi yang sudah terkirim ke `Rina Kusuma {runId}` sebelum penggantian tidak dipindahkan
156. Verifikasi Borrow Log tetap mencatat PIC saat aksi terjadi, `by Rina Kusuma {runId} on behalf of Dian Sastro {runId}`

### Borrower tanpa akun dibuatkan akun login saat pinjaman berjalan
157. `Ratna Sari {runId}` dibuatkan akun login di Users saat pinjaman `Obeng Set Tekiro {runId}` berstatus `Waiting for Handover`
158. Verifikasi pinjaman pindah ke daftar pinjaman `Ratna Sari {runId}`
159. Verifikasi `Rina Kusuma {runId}` tidak lagi melihat pinjaman itu
160. Ratna mengirim Accept atas handover `Obeng Set Tekiro {runId}`
161. Verifikasi Accept oleh `Ratna Sari {runId}` diterima karena konfirmasi handover berikutnya memakai semua cara
162. Verifikasi notifikasi berikutnya ditujukan ke `Ratna Sari {runId}`, bukan ke PIC

### Borrow Now self-service tidak menilai Auto-approve dan Approval type
163. Dewi mengirim Borrow Now atas `Mesin Label Brother PT-P710 {runId}` dengan scan TAG, Duration `2` Days, dan Purpose `Pelabelan arsip`
164. Verifikasi baris pinjaman langsung `Borrowed` walau Require approval aset `ON` dengan Approval type `Any one` dan Auto-approve terpenuhi oleh Duration `2` Days
165. Verifikasi baris tidak dicatat `Auto-approved` dan tidak melalui pengajuan approval, karena Source-nya `Self-service`

### Extend pinjaman self-service dari mobile dan batas Max extensions tetap berlaku
166. Dewi mengajukan Extend atas `Webcam Logitech C920 {runId}` dari mobile dengan Extend by `1` dan Reason `Dipakai untuk rapat daring`
167. Verifikasi permintaan Extend atas pinjaman self-service dari mobile diterima
168. Dewi mengajukan Extend atas `Lampu Belajar Philips {runId}` dari web dengan Extend by `1` dan Reason `Dipakai sampai ujian selesai`
169. Verifikasi permintaan Extend ditolak karena Max extensions aset itu sudah tercapai, dan Due date tidak berubah

### Batas Block when overdue dan Max assets dihitung untuk Borrower pada self-service
170. Hendra membuka daftar aset yang dapat dipinjam sendiri
171. Verifikasi `Kipas Angin Cosmos {runId}` yang Non TAG tampil `Not ready` untuk `Hendra Wijaya {runId}` dengan alasan `[Name] has an overdue borrow: [Asset Code], due [Date]. Return it first.` atas pinjaman `Kabel Roll Eterna {runId}`, dan tidak bisa dicentang
172. Hendra memindai TAG `Dispenser Miyako {runId}` pada Borrow an Asset
173. Verifikasi aset tidak ditambahkan dan ditolak dengan pesan Borrower `[Name] has an overdue borrow: [Asset Code], due [Date]. Return it first.` atas pinjaman `Kabel Roll Eterna {runId}`
174. Nanda mengirim Borrow Now atas nama `Wulan Safitri {runId}` atas `Power Bank Anker 20K {runId}` dengan scan TAG, Duration `1` Days, dan Purpose `Dokumentasi lapangan`, disertai pernyataan Confirm Receipt bahwa `Wulan Safitri {runId}` hadir dan menerima aset
175. Verifikasi permintaan ditolak dengan pesan `Wulan Safitri {runId} can borrow up to 1 assets at a time.`, karena Max assets per borrower dihitung untuk Borrower walau PIC `Nanda Pratiwi {runId}` belum memegang pinjaman
176. Nanda mengirim Borrow Now atas nama `Yoga Pratama {runId}` atas `Rice Cooker Philips {runId}` dengan scan TAG, Duration `1` Days, dan Purpose `Acara pantry kantor`, disertai pernyataan Confirm Receipt bahwa `Yoga Pratama {runId}` hadir dan menerima aset
177. Verifikasi permintaan ditolak dengan pesan `[Name] has an overdue borrow: [Asset Code], due [Date]. Return it first.` atas pinjaman `Setrika Philips {runId}`, karena Block new borrow when overdue dihitung untuk Borrower walau PIC `Nanda Pratiwi {runId}` tidak punya baris Overdue

### Evidence foto tetap berlaku pada Borrow Now self-service
178. Dewi mengirim Borrow Now atas `Gimbal DJI RS 3 {runId}` dengan scan TAG, Duration `2` Days, dan Purpose `Liputan acara` tanpa foto
179. Verifikasi permintaan ditolak dengan pesan `1 asset needs a handover photo.` dan tidak ada baris pinjaman atas `Gimbal DJI RS 3 {runId}`

### Akun sementara yang sudah lewat batas tidak muncul di Select Borrower
180. Agus mencari Borrower di Select Borrower dengan Search `{runId}`
181. Verifikasi `Bagus Santoso {runId}` yang akunnya `Active` dan `Activated` tampil di Select Borrower
182. Verifikasi `Joko Susilo {runId}` yang akun sementaranya sudah melewati Temporary Until tidak muncul di Select Borrower

### Server menolak Borrow Now atas nama karyawan dengan PIC kosong atau nonaktif
183. Rina mengirim Borrow Now atas nama `Lia Wulandari {runId}` atas `Lampu Ring Neewer 18 {runId}` dengan scan TAG, Duration `1` Days, dan Purpose `Foto produk`
184. Verifikasi permintaan atas nama karyawan yang PIC-nya kosong ditolak server dan tidak ada baris pinjaman atas `Lampu Ring Neewer 18 {runId}`
185. Rina mengirim Borrow Now atas nama `Tono Hartono {runId}` atas `Lampu Ring Neewer 18 {runId}` dengan scan TAG, Duration `1` Days, dan Purpose `Foto produk`
186. Verifikasi permintaan atas nama karyawan yang PIC-nya nonaktif ditolak server dan tidak ada baris pinjaman atas `Lampu Ring Neewer 18 {runId}`

### Scan aset yang sedang dalam transaksi atau berstatus tidak layak menampilkan alasan berprioritas tertinggi
187. Dewi memindai TAG `Heat Gun Bosch GHG 20 {runId}` pada Borrow an Asset
188. Verifikasi aset tidak ditambahkan dan ditolak dengan alasan `This asset is already in another transaction.` karena Custody-nya bukan `Available`
189. Dewi memindai TAG `Oven Listrik Maspion {runId}` pada Borrow an Asset
190. Verifikasi aset tidak ditambahkan dan ditolak dengan alasan berprioritas tertinggi `This asset is In Audit and can't be borrowed.`, bukan `This asset is already in another transaction.` walau aset itu juga ada di transaksi lain

### Notifikasi Borrower tanpa akun atas keputusan, Extension, dan Overdue dikirim ke PIC
191. Siti menyetujui pengajuan approval atas `Mesin Las Krisbow {runId}` milik `Tari Utami {runId}`
192. Verifikasi notifikasi keputusan Approve yang ditujukan ke Borrower diterima PIC `Nanda Pratiwi {runId}` sebagai notifikasi baru dengan penanda atas nama `Tari Utami {runId}`
193. Siti menolak pengajuan approval atas `Gerinda Tangan Makita {runId}` milik `Tari Utami {runId}`
194. Verifikasi notifikasi keputusan Reject yang ditujukan ke Borrower diterima PIC `Nanda Pratiwi {runId}` sebagai notifikasi baru dengan penanda atas nama `Tari Utami {runId}`
195. Agus menolak Extension Request atas `Troli Barang Lakoni {runId}` milik `Tari Utami {runId}`
196. Verifikasi notifikasi Extension yang ditujukan ke Borrower diterima PIC `Nanda Pratiwi {runId}` sebagai notifikasi baru dengan penanda atas nama `Tari Utami {runId}`
197. Job Overdue berjalan setelah Due date pinjaman `Mic Wireless Sennheiser {runId}` milik `Tari Utami {runId}` terlewati
198. Verifikasi notifikasi Overdue yang ditujukan ke Borrower diterima PIC `Nanda Pratiwi {runId}` sebagai notifikasi baru dengan penanda atas nama `Tari Utami {runId}`

### PIC dinonaktifkan saat pinjaman berjalan lalu PIC diisi kembali
199. PIC `Bayu Saputra {runId}` dinonaktifkan di Users saat pinjaman `Gergaji Mesin Stihl {runId}` milik `Fani Lestari {runId}` berjalan
200. Verifikasi pinjaman tetap berjalan dengan status baris `Borrowed`
201. Verifikasi baris `Gergaji Mesin Stihl {runId}` milik `Fani Lestari {runId}` diberi penanda `No PIC`
202. Job pengingat Due date harian berjalan
203. Verifikasi notifikasi untuk Borrower `Fani Lestari {runId}` dialihkan ke Aktor Borrow Group asal `Agus Pratama {runId}` sampai PIC diisi
204. PIC `Fani Lestari {runId}` diisi kembali di Users dengan `Maya Putri {runId}`
205. Job pengingat Due date harian berjalan pada tanggal Due date pinjaman `Gergaji Mesin Stihl {runId}`, saat pengingat D-day terbit
206. Verifikasi notifikasi berikutnya untuk Borrower `Fani Lestari {runId}` dikirim ke PIC `Maya Putri {runId}`, bukan lagi ke `Agus Pratama {runId}`
