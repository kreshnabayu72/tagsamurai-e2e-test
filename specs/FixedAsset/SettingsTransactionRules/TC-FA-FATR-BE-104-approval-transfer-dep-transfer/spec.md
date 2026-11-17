---
id: TC-FA-FATR-BE-104-approval-transfer-dep-transfer
title: "Approval dan penentuan approver pada transaksi Transfer"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r83", "§4.1#p24", "§4.1#r202", "§4.1#r203", "§4.1#r204", "§4.1#r205", "§4.1#r207", "§9.2#b379", "§9.2#b380", "§9.2#b381", "§9.2#b440", "§9.2#b442", "§9.2#b443", "§9.2#b445", "§9.2#b447", "§9.2#b448", "§9.2#b449", "§9.2#b450", "§9.2#b452", "§9.2#b454", "§9.2#b455", "§9.2#b456", "§9.2#b457", "§9.2#b459", "§9.2#b460", "§9.2#b463", "§9.2#b464", "§9.2#b465", "§9.2#b467", "§9.2#b468", "§9.2#b469", "§9.2#b470", "§9.2#b471", "§9.2#b474", "§9.2#b475", "§9.2#b476", "§9.2#b487", "§9.2#b488", "§9.2#b489", "§9.2#b490", "§9.2#b491", "§9.2#b492", "§9.2#b493", "§9.2#b462", "§9.2#b441", "§9.2#b451", "§9.2#b461", "§9.2#b478", "§9.2#b479", "§9.2#b482", "§9.2#b480", "§9.2#b481", "§9.2#b499", "§9.2#b500", "§9.2#b502", "§9.2#b501", "§9.2#b503", "§9.2#b505", "§9.2#b506", "§9.2#b507", "§9.2#b508", "§9.2#b509", "§9.2#b510", "§9.2#b511", "§9.2#b512", "§9.2#b513", "§9.2#b514", "§9.2#b515", "§9.2#b516", "§9.2#b517", "§9.2#b518", "§9.2#b519", "§9.2#b520", "§9.2#b521", "§9.2#p26", "§9.2#p27", "§9.2#p28", "§9.2#p29", "§9.2#b533", "§9.2#b534", "§9.2#b536", "§9.2#b537", "§9.2#b539", "§9.2#b540", "§9.2#b548", "§9.2#b549", "§9.2#b550", "§9.2#b551", "§9.2#b552", "§9.2#b554", "§9.2#b542", "§9.2#b543", "§9.2#b544", "§9.2#b545", "§9.2#b553", "§9.4.1#r20", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r42", "§9.4.2#r62", "§9.4.2#r138", "§9.4.2#r139", "§9.4.2#r141", "§9.4.2#r142", "§9.4.2#r143", "§9.4.2#r156", "§9.4.2#r157", "§9.4.2#r158", "§9.4.2#r159", "§9.4.2#r160", "§9.4.3#b4", "§9.4.4#r11", "§9.4.4#r48", "§9.4.4#r49", "§9.4.4#r50", "§9.4.4#r51", "§9.4.4#r53", "§9.8#r10", "§9.8#r11", "§9.8#r12", "§10#b1", "§11#r5", "§4.1#r135", "§4.1#r191", "§4.1#r193"]
smoke: []
dependsOn:
  - "Transfer: pengajuan, Send, dan Receive"
trace:
  "§Aturan Logika Modul#r83": [129, 163, 165, 166]
  "§4.1#p24": [80, 86, 137, 139, 141]
  "§4.1#r202": 3
  "§4.1#r203": 5
  "§4.1#r204": [17, 19]
  "§4.1#r205": [5, 10, 22]
  "§4.1#r207": [93, 97]
  "§9.2#b379": [131, 139, 143, 157, 159, 161, 183, 184, 186, 187, 189, 190]
  "§9.2#b380": [2, 93]
  "§9.2#b381": 24
  "§9.2#b440": 7
  "§9.2#b442": [3, 24]
  "§9.2#b443": [2, 3, 101]
  "§9.2#b445": [2, 128]
  "§9.2#b447": [24, 27]
  "§9.2#b448": 24
  "§9.2#b449": 24
  "§9.2#b450": 25
  "§9.2#b452": [60, 145, 147]
  "§9.2#b454": [3, 17]
  "§9.2#b455": 5
  "§9.2#b456": [17, 19]
  "§9.2#b457": [5, 6, 10, 19, 22]
  "§9.2#b459": 29
  "§9.2#b460": [29, 34, 38, 149]
  "§9.2#b463": [38, 44, 46]
  "§9.2#b464": 40
  "§9.2#b465": 32
  "§9.2#b467": [44, 47, 49, 102]
  "§9.2#b468": 47
  "§9.2#b469": 42
  "§9.2#b470": 43
  "§9.2#b471": 46
  "§9.2#b474": [52, 60, 124, 174]
  "§9.2#b475": 53
  "§9.2#b476": 54
  "§9.2#b487": [60, 145]
  "§9.2#b488": 52
  "§9.2#b489": [58, 62, 65]
  "§9.2#b490": [58, 62]
  "§9.2#b491": [65, 67]
  "§9.2#b492": 70
  "§9.2#b493": 73
  "§9.2#b462": 30
  "§9.2#b441": 110
  "§9.2#b451": [93, 97]
  "§9.2#b461": 112
  "§9.2#b478": [54, 76]
  "§9.2#b479": 76
  "§9.2#b482": 78
  "§9.2#b480": 54
  "§9.2#b481": 56
  "§9.2#b499": [80, 82]
  "§9.2#b500": 84
  "§9.2#b502": [80, 86]
  "§9.2#b501": [88, 89, 91, 133, 135]
  "§9.2#b503": 89
  "§9.2#b505": [93, 101]
  "§9.2#b506": [93, 95]
  "§9.2#b507": [97, 99]
  "§9.2#b508": [101, 106]
  "§9.2#b509": [104, 108]
  "§9.2#b510": 101
  "§9.2#b511": 101
  "§9.2#b512": [101, 112, 117]
  "§9.2#b513": 112
  "§9.2#b514": 117
  "§9.2#b515": [112, 117]
  "§9.2#b516": [115, 119, 121, 126]
  "§9.2#b517": 121
  "§9.2#b518": [113, 122]
  "§9.2#b519": [112, 117, 124, 151, 153, 155, 168, 169, 171, 172, 174, 175]
  "§9.2#b520": [128, 129]
  "§9.2#b521": [106, 110, 181]
  "§9.2#p26": 101
  "§9.2#p27": 106
  "§9.2#p28": [104, 108]
  "§9.2#p29": [102, 106]
  "§9.2#b533": [5, 19]
  "§9.2#b534": [5, 6, 10, 22]
  "§9.2#b536": 42
  "§9.2#b537": 42
  "§9.2#b539": [52, 60]
  "§9.2#b540": 54
  "§9.2#b548": [29, 34]
  "§9.2#b549": [29, 34]
  "§9.2#b550": 30
  "§9.2#b551": 35
  "§9.2#b552": [31, 36]
  "§9.2#b554": 40
  "§9.2#b542": [101, 104]
  "§9.2#b543": [101, 108]
  "§9.2#b544": 112
  "§9.2#b545": 121
  "§9.2#b553": [113, 122]
  "§9.4.1#r20": 49
  "§9.4.2#r37": 128
  "§9.4.2#r40": [42, 43, 44]
  "§9.4.2#r42": [13, 14]
  "§9.4.2#r62": [80, 82, 88, 133, 135]
  "§9.4.2#r138": [52, 60]
  "§9.4.2#r139": 53
  "§9.4.2#r141": [101, 106]
  "§9.4.2#r142": [104, 108]
  "§9.4.2#r143": 112
  "§9.4.2#r156": [29, 34, 121]
  "§9.4.2#r157": [30, 35]
  "§9.4.2#r158": [31, 36]
  "§9.4.2#r159": [113, 122]
  "§9.4.2#r160": 40
  "§9.4.3#b4": 49
  "§9.4.4#r11": [52, 53, 177, 179]
  "§9.4.4#r48": [6, 13, 14]
  "§9.4.4#r49": [42, 43]
  "§9.4.4#r50": [52, 53, 54, 60, 177, 179]
  "§9.4.4#r51": [101, 108]
  "§9.4.4#r53": [29, 30, 34]
  "§9.8#r10": 43
  "§9.8#r11": [30, 31, 35, 36, 113, 122]
  "§9.8#r12": [53, 176, 177, 178, 179]
  "§10#b1": 7
  "§11#r5": 101
  "§4.1#r135": [137, 139, 141]
  "§4.1#r191": [80, 82, 84, 86]
  "§4.1#r193": [93, 97, 101]
anchor: []
---

# Approval dan penentuan approver pada transaksi Transfer

## Prerequisites
- Aktor: Rina (DU-104-1), pengaju Transfer; Ali (DU-104-2) dan Anto (DU-104-3), Approver Group asal; Dewi (DU-104-4) dan Dian (DU-104-5), Approver Group tujuan; Putri (DU-104-6), Approver Group induk; Nono (DU-104-7), Rudi (DU-104-8), dan Lena (DU-104-9), Approver yang tidak eligible; Gita (DU-104-10), Gani (DU-104-11), Gema (DU-104-13), Gina (DU-104-14), Gino (DU-104-15), dan Hana (DU-104-17), Group Manager; Hadi (DU-104-16), Approver Group Hybrid; Tomi (DU-104-12), Total Control; Wulan (DU-104-18), admin Transaction Settings; Gara (DU-104-83), Group Manager Group induk; Bayu (DU-104-93), Approver Group Toggle Off.
- Data:
  - DU-104-1: User: Name `Rina Pengaju {runId}`, Role `Aktor Transfer`, Cakupan Transfer `Group Gudang Asal {runId}, Gudang Anak {runId}, Gudang Sendiri {runId}, Gudang Tanpa Approver {runId}, Gudang Manager Saja {runId}, Gudang Hybrid {runId}, Gudang Asal Kosong {runId}, Kantor Pusat {runId}, Gudang Cabang Manajer {runId}, Gudang Toggle Off {runId}`, Role Transaksi `Approver pada Group Gudang Asal {runId}, Gudang Sendiri {runId}, dan Gudang Tujuan Sendiri {runId}`.
  - DU-104-2: User: Name `Ali Approver Asal {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Asal {runId}`, Status `Active`.
  - DU-104-3: User: Name `Anto Approver Asal {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Asal {runId}`, Status `Active`.
  - DU-104-4: User: Name `Dewi Approver Tujuan {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Tujuan {runId}`, Status `Active`.
  - DU-104-5: User: Name `Dian Approver Tujuan {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Tujuan {runId}`, Status `Active`.
  - DU-104-6: User: Name `Putri Approver Induk {runId}`, Role Transaksi `Approver Transfer pada Group Divisi Induk {runId}`, Status `Active`.
  - DU-104-7: User: Name `Nono Nonaktif {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Anak {runId}`, Status `Inactive`.
  - DU-104-8: User: Name `Rudi Baca {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Anak {runId}`, Access Level `Read Only`.
  - DU-104-9: User: Name `Lena Tanpa Lisensi {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Anak {runId}`, Lisensi addon `tidak ada`.
  - DU-104-10: User: Name `Gita Manajer Asal {runId}`, Role `Group Manager`, Cakupan `Group Gudang Asal {runId}`, Cakupan Transfer `Group Gudang Asal {runId}`.
  - DU-104-11: User: Name `Gani Manajer Tujuan {runId}`, Role `Group Manager`, Cakupan `Group Gudang Tujuan {runId}`, Cakupan Transfer `Group Gudang Asal {runId}`.
  - DU-104-12: User: Name `Tomi Kontrol {runId}`, Access Level `Total Control`, Cakupan `seluruh client`.
  - DU-104-13: User: Name `Gema Manajer Sendiri {runId}`, Role `Group Manager`, Cakupan `Group Gudang Peran Ganda {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Peran Ganda {runId}`, Cakupan Transfer `Group Gudang Peran Ganda {runId}`.
  - DU-104-14: User: Name `Gina Manajer Satu {runId}`, Role `Group Manager`, Cakupan `Group Gudang Manager Saja {runId}`.
  - DU-104-15: User: Name `Gino Manajer Dua {runId}`, Role `Group Manager`, Cakupan `Group Gudang Manager Saja {runId}`.
  - DU-104-16: User: Name `Hadi Approver Hybrid {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Hybrid {runId}`, Status `Active`.
  - DU-104-17: User: Name `Hana Manajer Hybrid {runId}`, Role `Group Manager`, Cakupan `Group Gudang Hybrid {runId}`.
  - DU-104-18: User: Name `Wulan Pengelola {runId}`, Access Level `Total Control`, Cakupan `seluruh client`.
  - DU-104-19: Group: Name `Regional Jawa {runId}`, Group induk `root client`.
  - DU-104-20: Group: Name `Gudang Asal {runId}`, Group induk `Regional Jawa {runId}`, Override Group `Approval type All approvers (AND), Approval scope Both, Require approval ON, Auto-approve OFF`.
  - DU-104-21: Group: Name `Gudang Tujuan {runId}`, Group induk `Regional Jawa {runId}`, Override Group `Approval type Any one approver, Approval scope Origin only, Require approval OFF, Auto-approve ON, Auto-approve when destination in same parent Group ON`, Sisa kuota `500`.
  - DU-104-22: Group: Name `Regional Sumatra {runId}`, Group induk `root client`.
  - DU-104-23: Group: Name `Gudang Luar {runId}`, Group induk `Regional Sumatra {runId}`, Sisa kuota `500`.
  - DU-104-24: Group: Name `Divisi Induk {runId}`, Group induk `root client`.
  - DU-104-25: Group: Name `Gudang Anak {runId}`, Group induk `Divisi Induk {runId}`.
  - DU-104-26: Group: Name `Gudang Peran Ganda {runId}`, Group induk `root client`.
  - DU-104-27: Group: Name `Gudang Sendiri {runId}`, Group induk `root client`.
  - DU-104-28: Group: Name `Gudang Tanpa Approver {runId}`, Group induk `root client`.
  - DU-104-29: Group: Name `Gudang Manager Saja {runId}`, Group induk `root client`.
  - DU-104-30: Group: Name `Gudang Hybrid {runId}`, Group induk `root client`.
  - DU-104-31: Group: Name `Gudang Asal Kosong {runId}`, Group induk `root client`.
  - DU-104-32: Group: Name `Kantor Pusat {runId}`, Group induk `root client`.
  - DU-104-33: Group: Name `Kantor Wilayah {runId}`, Group induk `root client`, Sisa kuota `500`.
  - DU-104-34: Asset: Name `Pallet Besi OR 1 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-35: Asset: Name `Pallet Besi OR 2 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-36: Asset: Name `Pallet Besi OR 3 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-37: Asset: Name `Pallet Besi AND 1 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type All approvers (AND), Approval scope Origin only`.
  - DU-104-38: Asset: Name `Pallet Besi AND 2 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type All approvers (AND), Approval scope Origin only`.
  - DU-104-39: Asset: Name `Pallet Besi Guard {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-40: Asset: Name `Rak Gudang Anak {runId}`, Group `Gudang Anak {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-41: Asset: Name `Troli Kondisi A 1 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-42: Asset: Name `Troli Kondisi A 2 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-43: Asset: Name `Troli Kondisi A 4 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval OFF, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-44: Asset: Name `Meja Peran Ganda {runId}`, Group `Gudang Peran Ganda {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-45: Asset: Name `Meja Gudang Sendiri {runId}`, Group `Gudang Sendiri {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-46: Asset: Name `Meja Tanpa Approver 1 {runId}`, Group `Gudang Tanpa Approver {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-47: Asset: Name `Meja Tanpa Approver 2 {runId}`, Group `Gudang Tanpa Approver {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-48: Asset: Name `Meja Manajer 1 {runId}`, Group `Gudang Manager Saja {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-49: Asset: Name `Meja Manajer 2 {runId}`, Group `Gudang Manager Saja {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type All approvers (AND), Approval scope Origin only`.
  - DU-104-50: Asset: Name `Meja Hybrid 1 {runId}`, Group `Gudang Hybrid {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type All approvers (AND), Approval scope Origin only`.
  - DU-104-51: Asset: Name `Meja Hybrid 2 {runId}`, Group `Gudang Hybrid {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type All approvers (AND), Approval scope Origin only`.
  - DU-104-52: Asset: Name `Meja Save 1 {runId}`, Group `Gudang Tanpa Approver {runId}`, Status `Active`.
  - DU-104-53: Asset: Name `Meja Save 2 {runId}`, Group `Gudang Tanpa Approver {runId}`, Status `Active`.
  - DU-104-54: Asset: Name `Gerobak Auto 1 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Both`.
  - DU-104-55: Asset: Name `Gerobak Auto 2 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Both`.
  - DU-104-56: Asset: Name `Gerobak Auto 3 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-57: Asset: Name `Gerobak Auto 4 {runId}`, Group `Kantor Pusat {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Both`.
  - DU-104-58: Asset: Name `Gerobak Auto 5 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Both`.
  - DU-104-59: Asset: Name `Gerobak Auto 6 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Both`.
  - DU-104-60: Asset: Name `Gerobak Auto 7 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Both`.
  - DU-104-61: Asset: Name `Mesin Scope Asal {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-62: Asset: Name `Mesin Scope Tujuan {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Destination only`.
  - DU-104-63: Asset: Name `Mesin Scope Both 1 {runId}`, Group `Gudang Asal {runId}`, Status `Active`.
  - DU-104-64: Asset: Name `Mesin Baris Asal {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-65: Asset: Name `Mesin Baris Tujuan {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Destination only`.
  - DU-104-66: Asset: Name `Mesin Scope Both 2 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-67: Asset: Name `Mesin Scope Both 3 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-68: Asset: Name `Mesin Scope Both 4 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-69: Asset: Name `Mesin Scope Both 5 {runId}`, Group `Gudang Asal Kosong {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-70: Asset: Name `Mesin Approval Off {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval OFF, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-71: Asset: Name `Mesin Deny Approval {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Allow Transfer Deny`.
  - DU-104-75: Asset: Name `Gerobak Auto 8 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-76: Asset: Name `Gerobak Auto 9 {runId}`, Group `Gudang Sendiri {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve ON, Auto-approve when destination in same parent Group ON, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-77: Asset: Name `Mesin Scope Induk 1 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Destination scope Within same parent Group`.
  - DU-104-78: Asset: Name `Mesin Scope Induk 2 {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Destination scope Within same parent Group`.
  - DU-104-79: Asset: Name `Mesin Scope Induk 3 {runId}`, Group `Kantor Pusat {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Destination scope Within same parent Group`.
  - DU-104-80: Asset: Name `Genset Hilang Approval {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Condition `Missing`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-81: Group: Name `Wilayah Manajer {runId}`, Group induk `root client`.
  - DU-104-82: Group: Name `Gudang Cabang Manajer {runId}`, Group induk `Wilayah Manajer {runId}`.
  - DU-104-83: User: Name `Gara Manajer Wilayah {runId}`, Role `Group Manager`, Cakupan `Group Wilayah Manajer {runId}`, Cakupan Transfer `Group Gudang Cabang Manajer {runId}`.
  - DU-104-84: Asset: Name `Meja Cabang Manajer 1 {runId}`, Group `Gudang Cabang Manajer {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-85: Asset: Name `Meja Cabang Manajer 2 {runId}`, Group `Gudang Cabang Manajer {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-86: Asset: Name `Meja Manajer Both {runId}`, Group `Gudang Manager Saja {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-88: Group: Name `Gudang Kuota Penuh {runId}`, Group induk `Regional Sumatra {runId}`, Sisa kuota `0`.
  - DU-104-89: Asset: Name `Mesin Kuota Pembanding {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-90: Asset: Name `Mesin Kuota Terlampaui {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-91: Asset: Name `Genset Hilang Ganda {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Condition `Missing`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Allow Transfer Deny, Destination scope Within same parent Group`.
  - DU-104-92: Group: Name `Gudang Toggle Off {runId}`, Group induk `root client`, Override Group `Require approval OFF, Auto-approve OFF`.
  - DU-104-93: User: Name `Bayu Approver Toggle {runId}`, Role Transaksi `Approver Transfer pada Group Gudang Toggle Off {runId}`, Status `Active`.
  - DU-104-94: Asset: Name `Mesin Toggle Pembanding {runId}`, Group `Gudang Toggle Off {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only`.
  - DU-104-95: Asset: Name `Mesin Toggle Off {runId}`, Group `Gudang Toggle Off {runId}`, Status `Active`.
  - DU-104-96: Group: Name `Gudang Tujuan Sendiri {runId}`, Group induk `root client`, Sisa kuota `500`.
  - DU-104-97: Group: Name `Gudang Tujuan Kosong {runId}`, Group induk `root client`, Sisa kuota `500`.
  - DU-104-98: Asset: Name `Meja Both Asal Sendiri {runId}`, Group `Gudang Sendiri {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-99: Asset: Name `Meja Both Tujuan Sendiri {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-100: Asset: Name `Meja Both Tujuan Kosong {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Both`.
  - DU-104-101: Asset: Name `Mesin Auto Asal Off {runId}`, Group `Gudang Asal {runId}`, Status `Active`.
  - DU-104-103: Asset: Name `Genset Hilang Deny {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Condition `Missing`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Allow Transfer Deny`.
  - DU-104-104: Asset: Name `Mesin Deny Scope {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Allow Transfer Deny, Destination scope Within same parent Group`.
  - DU-104-105: Asset: Name `Mesin Scope Kuota {runId}`, Group `Gudang Asal {runId}`, Status `Active`, Override aset `Require approval ON, Auto-approve OFF, Approval type Any one approver, Approval scope Origin only, Destination scope Within same parent Group`.
  - DU-104-102: Entitas, entitas khusus spec ini, tidak dipakai spec lain: Name `Entitas Approval Transfer {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Approval Transfer {runId}` (DU-104-102) yang tidak dipakai spec lain, karena penugasan Role Transaksi `Approver` adalah setting entitas; semua data di atas berada di entitas itu.
  - Setiap aset dengan override aset memakai nilai efektif dari override itu, dan aset tanpa override aset memakai nilai efektif dari override Group atau Company default.
  - Semua user di atas memiliki akun aktif, kecuali yang tertulis Status `Inactive`, dan kredensialnya disediakan fase 2.
  - Approval Workflow tersedia di plan client.
  - Alokasi kuota per Group aktif di client dan Destination quota check bernilai `ON` pada All categories; setiap Group tujuan selain `Gudang Kuota Penuh {runId}` memiliki Sisa kuota `500`.

## Test Steps

### Any one approver: keputusan Approve pertama menyelesaikan approval dan approver lain menjadi Not Involved
1. Rina mengajukan Transfer aset `Pallet Besi OR 1 {runId}` ke Group `Gudang Tujuan {runId}`
2. Verifikasi baris Transfer aset `Pallet Besi OR 1 {runId}` berstatus `Waiting for Approval`, karena nilai efektif Require approval `ON` dan Auto-approve `OFF` dari setting aset itu
3. Verifikasi Ali dan Anto, Approver Role Transaksi pada Group asal, masing-masing menerima permintaan approval, dan Approval type berlaku karena ada beberapa approver
4. Ali menyetujui permintaan approval atas baris Transfer aset `Pallet Besi OR 1 {runId}`
5. Verifikasi baris Transfer aset `Pallet Besi OR 1 {runId}` berstatus `Waiting for Send`, yaitu status disetujui yang belum dikirim, setelah satu Approver menyetujui, karena Approval type `Any one approver` memakai rule OR
6. Verifikasi permintaan Anto atas baris itu berstatus `Not Involved`
7. Verifikasi baris itu tidak menunggu level approval lanjutan, karena approval hanya satu level

### Any one approver: keputusan Reject pertama menolak transaksi
8. Rina mengajukan Transfer aset `Pallet Besi OR 2 {runId}` ke Group `Gudang Tujuan {runId}`
9. Ali menolak permintaan approval atas baris Transfer aset `Pallet Besi OR 2 {runId}`
10. Verifikasi baris Transfer aset `Pallet Besi OR 2 {runId}` berstatus `Rejected` dan permintaan Anto berstatus `Not Involved`

### Any one approver: keputusan yang masuk hampir bersamaan, yang pertama menentukan
11. Rina mengajukan Transfer aset `Pallet Besi OR 3 {runId}` ke Group `Gudang Tujuan {runId}`
12. Ali menyetujui dan Anto menolak permintaan approval atas baris Transfer aset `Pallet Besi OR 3 {runId}` pada saat hampir bersamaan
13. Verifikasi baris Transfer aset `Pallet Besi OR 3 {runId}` memiliki tepat satu status final, `Waiting for Send` atau `Rejected`, yang berasal dari keputusan pertama yang masuk
14. Verifikasi approver yang keputusannya masuk belakangan berstatus `Not Involved` dan permintaannya ditutup

### All approvers (AND): semua approver harus menyetujui
15. Rina mengajukan Transfer aset `Pallet Besi AND 1 {runId}` ke Group `Gudang Tujuan {runId}`
16. Ali menyetujui permintaan approval atas baris Transfer aset `Pallet Besi AND 1 {runId}`
17. Verifikasi baris Transfer aset `Pallet Besi AND 1 {runId}` masih berstatus `Waiting for Approval`, menunggu approver lain
18. Anto menyetujui permintaan approval atas baris Transfer aset `Pallet Besi AND 1 {runId}`
19. Verifikasi baris Transfer aset `Pallet Besi AND 1 {runId}` berstatus `Waiting for Send` setelah semua Approver menyetujui, karena Approval type `All approvers (AND)` memakai rule AND

### All approvers (AND): satu Reject langsung menolak transaksi
20. Rina mengajukan Transfer aset `Pallet Besi AND 2 {runId}` ke Group `Gudang Tujuan {runId}`
21. Ali menolak permintaan approval atas baris Transfer aset `Pallet Besi AND 2 {runId}`
22. Verifikasi baris Transfer aset `Pallet Besi AND 2 {runId}` berstatus `Rejected` dan permintaan Anto berstatus `Not Involved`

### Approver ditentukan dari Role Transaksi pada Group aset atau ancestor-nya, hanya user yang eligible
23. Rina mengajukan Transfer aset `Rak Gudang Anak {runId}` ke Group `Gudang Tujuan {runId}`
24. Verifikasi Putri, yang ditugaskan Role Transaksi `Approver` pada Group induk `Divisi Induk {runId}`, menerima permintaan approval atas baris Transfer aset `Rak Gudang Anak {runId}`, karena penugasan mencakup Group turunan dan tanpa langkah eskalasi tersendiri
25. Verifikasi Nono, Rudi, dan Lena, yang ditugaskan Approver pada Group `Gudang Anak {runId}` tetapi tidak eligible, tidak menerima permintaan approval
26. Putri menyetujui permintaan approval atas baris Transfer aset `Rak Gudang Anak {runId}`
27. Verifikasi baris Transfer aset `Rak Gudang Anak {runId}` berstatus `Waiting for Send`

### Pengaju Group Manager yang menaungi Group aset: seluruh langkah approval dilewati
28. Gita mengajukan Transfer aset `Troli Kondisi A 1 {runId}` ke Group `Gudang Tujuan {runId}`
29. Verifikasi langkah approval dilewati dan baris Transfer aset `Troli Kondisi A 1 {runId}` langsung berstatus `Waiting for Send`, walau Ali dan Anto adalah Approver pada Group asal
30. Verifikasi log transaksi baris itu memuat `Approved by Gita Manajer Asal {runId} (Group Manager — requester)`
31. Verifikasi Modified By log itu adalah `Gita Manajer Asal {runId}`, bukan `System`
32. Verifikasi `Gita Manajer Asal {runId}` tidak tercatat sebagai approver baris itu, karena bypass bukan pengaju menjadi approver transaksinya sendiri

### Pengaju Total Control: seluruh langkah approval dilewati
33. Tomi mengajukan Transfer aset `Troli Kondisi A 2 {runId}` ke Group `Gudang Tujuan {runId}`
34. Verifikasi langkah approval dilewati dan baris Transfer aset `Troli Kondisi A 2 {runId}` langsung berstatus `Waiting for Send`
35. Verifikasi log transaksi baris itu memuat `Approved by Tomi Kontrol {runId} (Total Control — requester)`
36. Verifikasi Modified By log itu adalah `Tomi Kontrol {runId}`, bukan `System`

### Kondisi A dievaluasi lebih dulu daripada self-approval guard
37. Gema mengajukan Transfer aset `Meja Peran Ganda {runId}` ke Group `Gudang Tujuan {runId}`
38. Verifikasi baris Transfer aset `Meja Peran Ganda {runId}` langsung berstatus `Waiting for Send` dengan log `Approved by Gema Manajer Sendiri {runId} (Group Manager — requester)`, bukan `Approved by system (no independent approver)`, walau Gema juga satu-satunya Approver pada Group asal

### Kondisi A tidak berlaku bila Require approval efektif OFF
39. Gita mengajukan Transfer aset `Troli Kondisi A 4 {runId}` ke Group `Gudang Tujuan {runId}`
40. Verifikasi baris Transfer aset `Troli Kondisi A 4 {runId}` berstatus `Waiting for Send`, dan tidak ada log `Approved by Gita Manajer Asal {runId} (Group Manager — requester)` untuk baris itu

### Pengaju satu-satunya Approver eligible: approval dilewati dan transaksi Approved oleh sistem
41. Rina mengajukan Transfer aset `Meja Gudang Sendiri {runId}` ke Group `Gudang Tujuan {runId}`
42. Verifikasi langkah approval dilewati dan baris Transfer aset `Meja Gudang Sendiri {runId}` langsung berstatus `Waiting for Send`
43. Verifikasi log transaksi baris itu memuat `Approved by system (no independent approver)` dengan Modified By `System`
44. Verifikasi Rina tidak menjadi approver transaksinya sendiri pada baris itu

### Pengaju dikecualikan dari daftar approver dan tidak dapat menyetujui transaksinya sendiri
45. Rina mengajukan Transfer aset `Pallet Besi Guard {runId}` ke Group `Gudang Tujuan {runId}`
46. Verifikasi baris Transfer aset `Pallet Besi Guard {runId}` berstatus `Waiting for Approval` dan permintaan approval diterima Ali dan Anto, sebagian Approver eligible yang bukan pengaju
47. Verifikasi Rina tidak ada dalam daftar approver baris itu, walau ia ditugaskan Role Transaksi `Approver` pada Group asal
48. Rina menyetujui permintaan approval atas baris Transfer aset `Pallet Besi Guard {runId}`, yang ia ajukan sendiri
49. Verifikasi persetujuan Rina ditolak dan baris Transfer aset `Pallet Besi Guard {runId}` tetap berstatus `Waiting for Approval`

### Tidak ada Approver eligible dan tidak ada Group Manager: rute jatuh ke Total Control
50. Tomi mencatat jumlah notifikasi `approver_required` yang terkait Group `Gudang Tanpa Approver {runId}`
51. Rina mengajukan Transfer aset `Meja Tanpa Approver 1 {runId}` ke Group `Gudang Tujuan {runId}`
52. Verifikasi baris Transfer aset `Meja Tanpa Approver 1 {runId}` berstatus `Waiting for Approval` dan permintaan approval diterima Tomi dan Wulan, masing-masing user Total Control, karena tidak ada Approver eligible dan tidak ada Group Manager aktif yang menaungi Group asal
53. Verifikasi pencatatan rute itu ada di log transaksi baris tersebut dengan Modified By `System`
54. Verifikasi satu notifikasi `approver_required` baru terkirim untuk pengajuan itu
55. Rina mengajukan Transfer aset `Meja Tanpa Approver 2 {runId}` ke Group `Gudang Tujuan {runId}`
56. Verifikasi pengajuan kedua itu mengirim notifikasi `approver_required` tambahan miliknya sendiri, sehingga jumlahnya bertambah dua sejak dicatat
57. Tomi menyetujui permintaan approval atas baris Transfer aset `Meja Tanpa Approver 1 {runId}`
58. Verifikasi baris Transfer aset `Meja Tanpa Approver 1 {runId}` berstatus `Waiting for Send`, karena Approval type berlaku pada himpunan fallback dan persetujuan satu approver cukup

### Tidak ada Approver eligible: Group Manager yang menaungi menjadi approver fallback
59. Rina mengajukan Transfer aset `Meja Manajer 1 {runId}` ke Group `Gudang Tujuan {runId}`
60. Verifikasi Gina dan Gino, Group Manager yang menaungi Group asal tanpa penugasan Approver, masing-masing menerima permintaan approval atas baris Transfer aset `Meja Manajer 1 {runId}`
61. Gina menyetujui permintaan approval atas baris Transfer aset `Meja Manajer 1 {runId}`
62. Verifikasi baris Transfer aset `Meja Manajer 1 {runId}` berstatus `Waiting for Send` dan permintaan Gino berstatus `Not Involved`, karena Any one approver pada himpunan fallback cukup satu
63. Rina mengajukan Transfer aset `Meja Manajer 2 {runId}` ke Group `Gudang Tujuan {runId}`
64. Gina menyetujui permintaan approval atas baris Transfer aset `Meja Manajer 2 {runId}`
65. Verifikasi baris Transfer aset `Meja Manajer 2 {runId}` masih berstatus `Waiting for Approval`, karena All approvers (AND) pada himpunan fallback menuntut semua Group Manager menyetujui
66. Gino menyetujui permintaan approval atas baris Transfer aset `Meja Manajer 2 {runId}`
67. Verifikasi baris Transfer aset `Meja Manajer 2 {runId}` berstatus `Waiting for Send`

### Ada Approver terdaftar: Group Manager tanpa penugasan tidak dihitung dalam AND tetapi keputusannya override final
68. Rina mengajukan Transfer aset `Meja Hybrid 1 {runId}` ke Group `Gudang Tujuan {runId}`
69. Hadi, Approver terdaftar pada Group asal, menyetujui permintaan approval atas baris Transfer aset `Meja Hybrid 1 {runId}`
70. Verifikasi baris Transfer aset `Meja Hybrid 1 {runId}` berstatus `Waiting for Send` walau Hana, Group Manager tanpa penugasan, belum memutuskan, karena Hana tidak dihitung dalam rule AND
71. Rina mengajukan Transfer aset `Meja Hybrid 2 {runId}` ke Group `Gudang Tujuan {runId}`
72. Hana menolak permintaan approval atas baris Transfer aset `Meja Hybrid 2 {runId}`
73. Verifikasi baris Transfer aset `Meja Hybrid 2 {runId}` berstatus `Rejected` dan permintaan Hadi berstatus `Not Involved`, karena keputusan Group Manager tetap bersifat override final

### Save konfigurasi Approval tidak mengirim approver_required bila ada Role Transaksi Approver di Group lain
74. Wulan mencatat jumlah notifikasi `approver_required` yang terkait Group `Gudang Tanpa Approver {runId}`
75. Wulan menambah override aset untuk aset `Meja Save 1 {runId}` di All categories dengan Require approval `ON` dan Auto-approve `OFF`
76. Verifikasi tidak ada notifikasi `approver_required` baru yang terkait Group `Gudang Tanpa Approver {runId}`, karena Role Transaksi `Approver` Transfer ditugaskan di Group lain sehingga kondisi tidak ada Role Transaksi `Approver` yang ditugaskan tidak timbul akibat Save itu
77. Wulan menambah override aset untuk aset `Meja Save 2 {runId}` di All categories dengan Photo at end `OFF`
78. Verifikasi jumlah notifikasi `approver_required` tidak bertambah, karena konfigurasi Approval tidak diubah

### Auto-approve ON: baris lolos bila Group tujuan berinduk langsung sama dengan Group asal
79. Rina mengajukan Transfer aset `Gerobak Auto 1 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, yang berinduk langsung sama
80. Verifikasi baris Transfer aset `Gerobak Auto 1 {runId}` langsung berstatus `Waiting for Send` dan melewati approval di kedua sisi pada Approval scope `Both`
81. Rina mengajukan Transfer aset `Gerobak Auto 2 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Luar {runId}`, yang berinduk berbeda
82. Verifikasi baris Transfer aset `Gerobak Auto 2 {runId}` berstatus `Waiting for Approval`, karena Group tujuan tidak berinduk langsung sama dengan Group asal
83. Rina mengajukan Transfer aset `Gerobak Auto 3 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, dengan Auto-approve when destination in same parent Group `OFF` pada aset itu
84. Verifikasi baris Transfer aset `Gerobak Auto 3 {runId}` berstatus `Waiting for Approval` dan mengikuti approval normal
85. Rina mengajukan Transfer aset `Gerobak Auto 4 {runId}` dari Group `Kantor Pusat {runId}` ke Group `Kantor Wilayah {runId}`, keduanya Group tingkat atas
86. Verifikasi baris Transfer aset `Gerobak Auto 4 {runId}` langsung berstatus `Waiting for Send`, karena Group tingkat atas dianggap berinduk root client sehingga antar Group tingkat atas memenuhi kondisi

### Auto-approve dinilai per baris dan sesudah Kondisi A
87. Rina mengajukan satu Transfer berisi aset `Gerobak Auto 5 {runId}` dan `Gerobak Auto 6 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
88. Verifikasi baris Transfer aset `Gerobak Auto 5 {runId}`, yang Auto-approve-nya `ON`, langsung berstatus `Waiting for Send`
89. Verifikasi baris Transfer aset `Gerobak Auto 6 {runId}`, yang Auto-approve-nya `OFF`, berstatus `Waiting for Approval` dan mengikuti aturan efektifnya sendiri walau berada pada pengajuan yang sama
90. Gita mengajukan Transfer aset `Gerobak Auto 7 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Luar {runId}`, yang tidak memenuhi Auto-approve
91. Verifikasi sisi Group asal dilewati karena Kondisi A, dan sisi Group tujuan `Gudang Luar {runId}` tetap menunggu approval, sehingga baris Transfer aset `Gerobak Auto 7 {runId}` berstatus `Waiting for Approval`, karena Approval scope `Both` dan Group tujuan tidak memenuhi Auto-approve

### Approval scope Origin only: hanya Approver yang mencakup Group asal
92. Rina mengajukan Transfer aset `Mesin Scope Asal {runId}` ke Group `Gudang Tujuan {runId}`
93. Verifikasi Ali dan Anto, Approver yang mencakup Group asal, menerima permintaan approval, dan Dewi serta Dian, Approver Group tujuan, tidak menerimanya
94. Ali menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Asal {runId}`
95. Verifikasi baris Transfer aset `Mesin Scope Asal {runId}` berstatus `Waiting for Send` tanpa persetujuan sisi Group tujuan

### Approval scope Destination only: hanya Approver yang mencakup Group tujuan
96. Rina mengajukan Transfer aset `Mesin Scope Tujuan {runId}` ke Group `Gudang Tujuan {runId}`
97. Verifikasi Dewi dan Dian, Approver yang mencakup Group tujuan, menerima permintaan approval, dan Ali serta Anto tidak menerimanya
98. Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Tujuan {runId}`
99. Verifikasi baris Transfer aset `Mesin Scope Tujuan {runId}` berstatus `Waiting for Send` tanpa persetujuan sisi Group asal

### Approval scope Both: kedua sisi menyetujui, nilai efektif diselesaikan dari aset dan Group asal
100. Rina mengajukan Transfer aset `Mesin Scope Both 1 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
101. Verifikasi Ali dan Anto menerima permintaan approval sebagai sisi Group asal, dan Dewi serta Dian menerima permintaan approval sebagai sisi Group tujuan, masing-masing sisi dengan daftar Approver-nya sendiri, dan nilai efektif Require approval `ON` diselesaikan dari Group asal, bukan dari Group tujuan `Gudang Tujuan {runId}` yang ber-Require approval `OFF`
102. Verifikasi Rina tidak menjadi approver Transfer-nya sendiri walau ia ditugaskan Role Transaksi `Approver` pada Group asal
103. Ali dan Anto menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 1 {runId}`
104. Verifikasi baris Transfer aset `Mesin Scope Both 1 {runId}` masih berstatus `Waiting for Approval`, karena sisi Group tujuan belum menyetujui
105. Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 1 {runId}`
106. Verifikasi baris Transfer aset `Mesin Scope Both 1 {runId}` masih berstatus `Waiting for Approval`, karena Approval type `All approvers (AND)` dari Group asal menuntut Dian menyetujui dan Group tujuan, yang Approval type-nya `Any one approver`, tidak ikut menentukan nilai efektif
107. Dian menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 1 {runId}`
108. Verifikasi baris Transfer aset `Mesin Scope Both 1 {runId}` berstatus `Waiting for Send`, karena kedua sisi telah menyetujui

### Approval scope Both: nilai efektif diselesaikan per baris dari aset masing-masing
109. Rina mengajukan satu Transfer berisi aset `Mesin Baris Asal {runId}` dan `Mesin Baris Tujuan {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
110. Verifikasi baris Transfer aset `Mesin Baris Asal {runId}`, yang Approval scope-nya `Origin only`, hanya menunggu Ali dan Anto, dan baris Transfer aset `Mesin Baris Tujuan {runId}`, yang Approval scope-nya `Destination only`, hanya menunggu Dewi dan Dian

### Approval scope Both: Group Manager yang menaungi Group asal hanya melewati sisi Group asal
111. Gita mengajukan Transfer aset `Mesin Scope Both 2 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
112. Verifikasi sisi Group asal dilewati dan sisi Group tujuan masih menunggu Dewi dan Dian, sehingga baris Transfer aset `Mesin Scope Both 2 {runId}` berstatus `Waiting for Approval`
113. Verifikasi log transaksi baris itu mencatat Kondisi A untuk sisi Group asal yang dilewati
114. Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 2 {runId}`
115. Verifikasi baris Transfer aset `Mesin Scope Both 2 {runId}` berstatus `Waiting for Send`, karena kedua sisi telah dilewati atau disetujui

### Approval scope Both: Group Manager yang menaungi Group tujuan hanya melewati sisi Group tujuan
116. Gani mengajukan Transfer aset `Mesin Scope Both 3 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
117. Verifikasi sisi Group tujuan dilewati dan sisi Group asal masih menunggu Ali dan Anto, sehingga baris Transfer aset `Mesin Scope Both 3 {runId}` berstatus `Waiting for Approval`
118. Ali menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 3 {runId}`
119. Verifikasi baris Transfer aset `Mesin Scope Both 3 {runId}` berstatus `Waiting for Send`

### Approval scope Both: Total Control melewati kedua sisi
120. Tomi mengajukan Transfer aset `Mesin Scope Both 4 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
121. Verifikasi baris Transfer aset `Mesin Scope Both 4 {runId}` langsung berstatus `Waiting for Send`, karena Total Control melewati kedua sisi
122. Verifikasi log transaksi baris itu mencatat Kondisi A untuk sisi Group asal dan sisi Group tujuan yang dilewati

### Approval scope Both: aturan tidak-ada-Approver berlaku per sisi
123. Rina mengajukan Transfer aset `Mesin Scope Both 5 {runId}` dari Group `Gudang Asal Kosong {runId}` ke Group `Gudang Tujuan {runId}`
124. Verifikasi sisi Group asal, yang tidak punya Approver eligible, jatuh ke Tomi dan Wulan sebagai Total Control, dan sisi Group tujuan menunggu Dewi dan Dian
125. Tomi dan Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 5 {runId}`
126. Verifikasi baris Transfer aset `Mesin Scope Both 5 {runId}` berstatus `Waiting for Send`

### Require approval efektif OFF: langkah approval dilewati walau ada Approver dan Approval scope
127. Rina mengajukan Transfer aset `Mesin Approval Off {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
128. Verifikasi baris Transfer aset `Mesin Approval Off {runId}` langsung berstatus `Waiting for Send`, karena nilai efektif Require approval `OFF` sehingga langkah approval dilewati dan pengajuan lanjut ke tahap eksekusi transaksinya
129. Verifikasi Ali, Anto, Dewi, dan Dian tidak menerima permintaan approval atas baris itu, karena penugasan Role Transaksi `Approver` tidak dipakai

### Pengajuan yang ditolak aturan Deny tidak sampai ke evaluasi approval
130. Rina mengajukan Transfer aset `Mesin Deny Approval {runId}` ke Group `Gudang Tujuan {runId}`
131. Verifikasi pengajuan ditolak oleh Deny pada override aset, tidak ada baris Transfer untuk aset `Mesin Deny Approval {runId}`, dan Ali serta Anto tidak menerima permintaan approval, karena Deny pada override dievaluasi sebelum Approval

### Baris yang lolos Auto-approve tetap dinilai sesudah Kondisi A dan self-approval guard
132. Gita mengajukan Transfer aset `Gerobak Auto 8 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, yang berinduk langsung sama sehingga baris memenuhi Auto-approve
133. Verifikasi baris Transfer aset `Gerobak Auto 8 {runId}` berstatus `Waiting for Send` dengan log `Approved by Gita Manajer Asal {runId} (Group Manager — requester)`, karena Kondisi A dinilai lebih dulu daripada Auto-approve
134. Rina mengajukan Transfer aset `Gerobak Auto 9 {runId}` dari Group `Gudang Sendiri {runId}` ke Group `Kantor Wilayah {runId}`, keduanya Group tingkat atas sehingga baris memenuhi Auto-approve
135. Verifikasi baris Transfer aset `Gerobak Auto 9 {runId}` berstatus `Waiting for Send` dengan log `Approved by system (no independent approver)` dan Modified By `System`, karena self-approval guard dinilai lebih dulu daripada Auto-approve

### Destination scope Within same parent Group dan aturan tetap dievaluasi sebelum Approval
136. Rina mengajukan Transfer aset `Mesin Scope Induk 1 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, yang berinduk langsung sama
137. Verifikasi pengajuan diterima dan baris Transfer aset `Mesin Scope Induk 1 {runId}` berstatus `Waiting for Approval`, karena Group tujuan memenuhi Destination scope `Within same parent Group`
138. Rina mengajukan Transfer aset `Mesin Scope Induk 2 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Luar {runId}`, yang berinduk berbeda
139. Verifikasi pengajuan ditolak, tidak ada baris Transfer untuk aset `Mesin Scope Induk 2 {runId}`, dan Ali serta Anto tidak menerima permintaan approval, karena Eligibility (Destination scope) dievaluasi sebelum Approval
140. Rina mengajukan Transfer aset `Mesin Scope Induk 3 {runId}` dari Group `Kantor Pusat {runId}` ke Group `Kantor Wilayah {runId}`, keduanya Group tingkat atas
141. Verifikasi pengajuan diterima dan baris Transfer aset `Mesin Scope Induk 3 {runId}` berstatus `Waiting for Approval`, karena Group tingkat atas dianggap berinduk root client sehingga memenuhi Destination scope `Within same parent Group`
142. Rina mengajukan Transfer aset `Genset Hilang Approval {runId}`, berkondisi `Missing`, ke Group `Gudang Tujuan {runId}`
143. Verifikasi pengajuan ditolak, tidak ada baris Transfer untuk aset `Genset Hilang Approval {runId}`, dan Ali serta Anto tidak menerima permintaan approval, karena aturan tetap kondisi `Missing` dievaluasi sebelum Approval

### Group Manager pada ancestor Group aset menjadi approver dan dapat melewati approval
144. Rina mengajukan Transfer aset `Meja Cabang Manajer 1 {runId}` ke Group `Gudang Tujuan {runId}`
145. Verifikasi Gara, Group Manager yang menaungi `Wilayah Manajer {runId}` sebagai ancestor Group aset, menerima permintaan approval atas baris Transfer aset `Meja Cabang Manajer 1 {runId}`, karena tidak ada Approver eligible pada Group aset dan Group Manager pada ancestor-nya menjadi approver fallback
146. Gara menyetujui permintaan approval atas baris Transfer aset `Meja Cabang Manajer 1 {runId}`
147. Verifikasi baris Transfer aset `Meja Cabang Manajer 1 {runId}` berstatus `Waiting for Send`
148. Gara mengajukan Transfer aset `Meja Cabang Manajer 2 {runId}` ke Group `Gudang Tujuan {runId}`
149. Verifikasi langkah approval dilewati dan baris Transfer aset `Meja Cabang Manajer 2 {runId}` berstatus `Waiting for Send` dengan log `Approved by Gara Manajer Wilayah {runId} (Group Manager — requester)`, karena Gara menaungi ancestor Group aset

### Approval scope Both: Group Manager pada sisi tanpa Approver menerima permintaan untuk sisinya saja
150. Rina mengajukan Transfer aset `Meja Manajer Both {runId}` dari Group `Gudang Manager Saja {runId}` ke Group `Gudang Tujuan {runId}`
151. Verifikasi Gina dan Gino, Group Manager Group asal tanpa penugasan Approver, menerima permintaan approval untuk sisi Group asal saja, dan Dewi serta Dian menerima permintaan approval untuk sisi Group tujuan
152. Gina menyetujui permintaan approval sisi Group asal atas baris Transfer aset `Meja Manajer Both {runId}`
153. Verifikasi baris Transfer aset `Meja Manajer Both {runId}` masih berstatus `Waiting for Approval`, karena sisi Group tujuan tetap menunggu approval dari Approver-nya sendiri
154. Dewi menyetujui permintaan approval sisi Group tujuan atas baris Transfer aset `Meja Manajer Both {runId}`
155. Verifikasi baris Transfer aset `Meja Manajer Both {runId}` berstatus `Waiting for Send`, karena kedua sisi telah menyetujui

### Pengajuan yang melanggar Limits ditolak sebelum Approval
156. Rina mengajukan Transfer aset `Mesin Kuota Pembanding {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
157. Verifikasi baris Transfer aset `Mesin Kuota Pembanding {runId}` berstatus `Waiting for Approval` dan Ali serta Anto menerima permintaan approval atas baris itu, sehingga pengajuan dari Group asal yang sama memang memicu permintaan approval bila tidak melanggar aturan sebelum Approval
158. Rina mengajukan Transfer aset `Mesin Kuota Terlampaui {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Kuota Penuh {runId}`, yang sisa kuotanya `0`
159. Verifikasi pengajuan ditolak karena kuota Group tujuan terlampaui, tidak ada baris Transfer untuk aset `Mesin Kuota Terlampaui {runId}`, dan Ali serta Anto tidak menerima permintaan approval atas aset itu, karena Limits dievaluasi sebelum Approval

### Pelanggaran aturan tetap, Deny, Eligibility, dan Limits sekaligus tidak sampai ke Approval
160. Rina mengajukan Transfer aset `Genset Hilang Ganda {runId}`, berkondisi `Missing`, ber-Deny pada override aset, dan ber-Destination scope `Within same parent Group`, dari Group `Gudang Asal {runId}` ke Group `Gudang Kuota Penuh {runId}`, yang berinduk berbeda dan sisa kuotanya `0`
161. Verifikasi pengajuan ditolak dengan alasan aturan tetap kondisi `Missing`, bukan Deny pada override, Destination scope, atau kuota, tidak ada baris Transfer untuk aset `Genset Hilang Ganda {runId}`, dan Ali serta Anto tidak menerima permintaan approval atas aset itu, karena aturan tetap dievaluasi lebih dulu daripada Deny pada override, Eligibility, dan Limits sebelum Approval

### Require approval OFF dari override Group: penugasan Approver tidak dipakai
162. Rina mengajukan Transfer aset `Mesin Toggle Pembanding {runId}`, yang ber-Require approval `ON` pada override aset, dari Group `Gudang Toggle Off {runId}` ke Group `Gudang Tujuan {runId}`
163. Verifikasi baris Transfer aset `Mesin Toggle Pembanding {runId}` berstatus `Waiting for Approval` dan Bayu, Approver pada Group `Gudang Toggle Off {runId}`, menerima permintaan approval atas baris itu
164. Rina mengajukan Transfer aset `Mesin Toggle Off {runId}`, yang tanpa override aset sehingga Require approval `OFF` berasal dari override Group, dari Group `Gudang Toggle Off {runId}` ke Group `Gudang Tujuan {runId}`
165. Verifikasi baris Transfer aset `Mesin Toggle Off {runId}` langsung berstatus `Waiting for Send`
166. Verifikasi Bayu tidak menerima permintaan approval atas baris Transfer aset `Mesin Toggle Off {runId}`, karena penugasan Role Transaksi `Approver` tidak dipakai selama Require approval `OFF`

### Self-approval guard dan tidak-ada-Approver berlaku per sisi pada Approval scope Both
167. Rina mengajukan Transfer aset `Meja Both Asal Sendiri {runId}` dari Group `Gudang Sendiri {runId}`, yang hanya memiliki Rina sebagai Approver eligible, ke Group `Gudang Tujuan {runId}`
168. Verifikasi sisi Group asal dilewati dengan log `Approved by system (no independent approver)` dan Modified By `System`
169. Verifikasi sisi Group tujuan masih menunggu Dewi dan Dian, sehingga baris Transfer aset `Meja Both Asal Sendiri {runId}` berstatus `Waiting for Approval`
170. Rina mengajukan Transfer aset `Meja Both Tujuan Sendiri {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan Sendiri {runId}`, yang hanya memiliki Rina sebagai Approver eligible
171. Verifikasi sisi Group tujuan dilewati dengan log `Approved by system (no independent approver)` dan Modified By `System`
172. Verifikasi sisi Group asal masih menunggu Ali dan Anto, sehingga baris Transfer aset `Meja Both Tujuan Sendiri {runId}` berstatus `Waiting for Approval`
173. Rina mengajukan Transfer aset `Meja Both Tujuan Kosong {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan Kosong {runId}`, yang tidak punya Approver eligible dan tidak punya Group Manager
174. Verifikasi sisi Group tujuan jatuh ke Tomi dan Wulan, masing-masing user Total Control, yang menerima permintaan approval untuk sisi itu
175. Verifikasi sisi Group asal masih menunggu Ali dan Anto, sehingga baris Transfer aset `Meja Both Tujuan Kosong {runId}` berstatus `Waiting for Approval`

### Entri log rute tidak ada Approver eligible tanpa Note enum
176. Verifikasi log transaksi baris Transfer aset `Meja Tanpa Approver 1 {runId}` memuat entri rute ke Total Control dengan Modified By `System`
177. Verifikasi entri log rute ke Total Control itu tanpa Note enum
178. Verifikasi log transaksi baris Transfer aset `Meja Manajer 1 {runId}` memuat entri rute ke Group Manager dengan Modified By `System`
179. Verifikasi entri log rute ke Group Manager itu tanpa Note enum

### Auto-approve diselesaikan dari Group asal, bukan dari Group tujuan
180. Rina mengajukan Transfer aset `Mesin Auto Asal Off {runId}` dari Group `Gudang Asal {runId}`, yang Auto-approve-nya `OFF`, ke Group `Gudang Tujuan {runId}`, yang Auto-approve-nya `ON` dan berinduk langsung sama
181. Verifikasi baris Transfer aset `Mesin Auto Asal Off {runId}` berstatus `Waiting for Approval` dan tidak lolos Auto-approve, karena Auto-approve diselesaikan dari Group asal dan bukan dari Group tujuan

### Urutan evaluasi berpasangan: aturan tetap sebelum Deny, Deny sebelum Eligibility, Eligibility sebelum Limits
182. Rina mengajukan Transfer aset `Genset Hilang Deny {runId}`, berkondisi `Missing` dan ber-Deny pada override aset, ke Group `Gudang Tujuan {runId}`
183. Verifikasi pengajuan ditolak dengan alasan aturan tetap kondisi `Missing`, bukan Deny pada override aset, karena aturan tetap dievaluasi lebih dulu daripada Deny pada override
184. Verifikasi tidak ada baris Transfer untuk aset `Genset Hilang Deny {runId}` dan Ali serta Anto tidak menerima permintaan approval atas aset itu
185. Rina mengajukan Transfer aset `Mesin Deny Scope {runId}`, ber-Deny pada override aset dan ber-Destination scope `Within same parent Group`, dari Group `Gudang Asal {runId}` ke Group `Gudang Luar {runId}`, yang berinduk berbeda
186. Verifikasi pengajuan ditolak dengan alasan Deny pada override aset, bukan Eligibility Destination scope `Within same parent Group`, karena Deny pada override dievaluasi lebih dulu daripada Eligibility
187. Verifikasi tidak ada baris Transfer untuk aset `Mesin Deny Scope {runId}` dan Ali serta Anto tidak menerima permintaan approval atas aset itu
188. Rina mengajukan Transfer aset `Mesin Scope Kuota {runId}`, ber-Destination scope `Within same parent Group`, dari Group `Gudang Asal {runId}` ke Group `Gudang Kuota Penuh {runId}`, yang berinduk berbeda dan sisa kuotanya `0`
189. Verifikasi pengajuan ditolak dengan alasan Eligibility Destination scope `Within same parent Group`, bukan kuota Group tujuan yang terlampaui, karena Eligibility dievaluasi lebih dulu daripada Limits
190. Verifikasi tidak ada baris Transfer untuk aset `Mesin Scope Kuota {runId}` dan Ali serta Anto tidak menerima permintaan approval atas aset itu
