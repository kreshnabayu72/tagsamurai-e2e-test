---
id: TC-FA-FATR-BE-104-approval-transfer-dep-transfer
title: "Approval dan penentuan approver pada transaksi Transfer"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
owner: BE
sourceRules: ["§Aturan Logika Modul#r74", "§Aturan Logika Modul#r81", "§4.1#p24", "§4.1#r193", "§4.1#r194", "§4.1#r195", "§4.1#r196", "§4.1#r198", "§9.2#b379", "§9.2#b380", "§9.2#b381", "§9.2#b382", "§9.2#b441", "§9.2#b443", "§9.2#b444", "§9.2#b445", "§9.2#b446", "§9.2#b448", "§9.2#b449", "§9.2#b450", "§9.2#b451", "§9.2#b453", "§9.2#b455", "§9.2#b456", "§9.2#b457", "§9.2#b458", "§9.2#b460", "§9.2#b461", "§9.2#b464", "§9.2#b465", "§9.2#b466", "§9.2#b468", "§9.2#b469", "§9.2#b470", "§9.2#b471", "§9.2#b472", "§9.2#b475", "§9.2#b476", "§9.2#b477", "§9.2#b488", "§9.2#b489", "§9.2#b490", "§9.2#b491", "§9.2#b492", "§9.2#b493", "§9.2#b494", "§9.2#b463", "§9.2#b442", "§9.2#b452", "§9.2#b462", "§9.2#b479", "§9.2#b480", "§9.2#b483", "§9.2#b481", "§9.2#b482", "§9.2#b500", "§9.2#b501", "§9.2#b503", "§9.2#b502", "§9.2#b504", "§9.2#b506", "§9.2#b507", "§9.2#b508", "§9.2#b509", "§9.2#b510", "§9.2#b511", "§9.2#b512", "§9.2#b513", "§9.2#b514", "§9.2#b515", "§9.2#b516", "§9.2#b517", "§9.2#b518", "§9.2#b519", "§9.2#b520", "§9.2#b521", "§9.2#b522", "§9.2#p26", "§9.2#p27", "§9.2#p28", "§9.2#p29", "§9.2#b534", "§9.2#b535", "§9.2#b537", "§9.2#b538", "§9.2#b540", "§9.2#b541", "§9.2#b549", "§9.2#b550", "§9.2#b551", "§9.2#b552", "§9.2#b553", "§9.2#b555", "§9.2#b543", "§9.2#b544", "§9.2#b545", "§9.2#b546", "§9.2#b554", "§9.4.1#r20", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r42", "§9.4.2#r62", "§9.4.2#r130", "§9.4.2#r131", "§9.4.2#r133", "§9.4.2#r134", "§9.4.2#r135", "§9.4.2#r148", "§9.4.2#r149", "§9.4.2#r150", "§9.4.2#r151", "§9.4.2#r152", "§9.4.3#b4", "§9.4.4#r11", "§9.4.4#r48", "§9.4.4#r49", "§9.4.4#r50", "§9.4.4#r51", "§9.4.4#r53", "§9.8#r12", "§9.8#r13", "§9.8#r14", "§9.10.1#r11", "§10#b1", "§11#r5"]
smoke: []
dependsOn:
  - Transfer: pengajuan, Send, dan Receive
trace:
  "§Aturan Logika Modul#r74": 129
  "§Aturan Logika Modul#r81": 130
  "§4.1#p24": [81, 87, 138, 140, 142]
  "§4.1#r193": 3
  "§4.1#r194": 6
  "§4.1#r195": [18, 20]
  "§4.1#r196": [6, 11, 23]
  "§4.1#r198": [94, 98]
  "§9.2#b379": [132, 140, 144]
  "§9.2#b380": [2, 94]
  "§9.2#b381": 25
  "§9.2#b382": 129
  "§9.2#b441": 8
  "§9.2#b443": [3, 25]
  "§9.2#b444": [2, 3, 102]
  "§9.2#b445": 4
  "§9.2#b446": [2, 129]
  "§9.2#b448": [25, 28]
  "§9.2#b449": 25
  "§9.2#b450": 25
  "§9.2#b451": 26
  "§9.2#b453": [61, 146, 148]
  "§9.2#b455": [3, 18]
  "§9.2#b456": 6
  "§9.2#b457": [18, 20]
  "§9.2#b458": [6, 7, 11, 20, 23]
  "§9.2#b460": 30
  "§9.2#b461": [30, 35, 39, 150]
  "§9.2#b464": [39, 45, 47]
  "§9.2#b465": 41
  "§9.2#b466": 33
  "§9.2#b468": [45, 48, 50, 103]
  "§9.2#b469": 48
  "§9.2#b470": 43
  "§9.2#b471": 44
  "§9.2#b472": 47
  "§9.2#b475": [53, 61, 125]
  "§9.2#b476": 54
  "§9.2#b477": 55
  "§9.2#b488": [61, 146]
  "§9.2#b489": 53
  "§9.2#b490": [59, 63, 66]
  "§9.2#b491": [59, 63]
  "§9.2#b492": [66, 68]
  "§9.2#b493": 71
  "§9.2#b494": 74
  "§9.2#b463": 31
  "§9.2#b442": 111
  "§9.2#b452": [94, 98]
  "§9.2#b462": 113
  "§9.2#b479": [55, 77]
  "§9.2#b480": 77
  "§9.2#b483": 79
  "§9.2#b481": 55
  "§9.2#b482": 57
  "§9.2#b500": [81, 83]
  "§9.2#b501": 85
  "§9.2#b503": [81, 87]
  "§9.2#b502": [89, 90, 92, 134, 136]
  "§9.2#b504": 90
  "§9.2#b506": [94, 102]
  "§9.2#b507": [94, 96]
  "§9.2#b508": [98, 100]
  "§9.2#b509": [102, 107]
  "§9.2#b510": [105, 109]
  "§9.2#b511": 102
  "§9.2#b512": 102
  "§9.2#b513": [102, 113, 118]
  "§9.2#b514": 113
  "§9.2#b515": 118
  "§9.2#b516": [113, 118]
  "§9.2#b517": [116, 120, 122, 127]
  "§9.2#b518": 122
  "§9.2#b519": [114, 123]
  "§9.2#b520": [113, 118, 125, 152, 154, 156]
  "§9.2#b521": [129, 130]
  "§9.2#b522": [107, 111]
  "§9.2#p26": 102
  "§9.2#p27": 107
  "§9.2#p28": [105, 109]
  "§9.2#p29": [103, 107]
  "§9.2#b534": [6, 20]
  "§9.2#b535": [6, 7, 11, 23]
  "§9.2#b537": 43
  "§9.2#b538": 43
  "§9.2#b540": [53, 61]
  "§9.2#b541": 55
  "§9.2#b549": [30, 35]
  "§9.2#b550": [30, 35]
  "§9.2#b551": 31
  "§9.2#b552": 36
  "§9.2#b553": [32, 37]
  "§9.2#b555": 41
  "§9.2#b543": [102, 105]
  "§9.2#b544": [102, 109]
  "§9.2#b545": 113
  "§9.2#b546": 122
  "§9.2#b554": [114, 123]
  "§9.4.1#r20": 50
  "§9.4.2#r37": 129
  "§9.4.2#r40": [43, 44, 45]
  "§9.4.2#r42": [14, 15]
  "§9.4.2#r62": [81, 83, 89, 134, 136]
  "§9.4.2#r130": [53, 61]
  "§9.4.2#r131": 54
  "§9.4.2#r133": [102, 107]
  "§9.4.2#r134": [105, 109]
  "§9.4.2#r135": 113
  "§9.4.2#r148": [30, 35, 122]
  "§9.4.2#r149": [31, 36]
  "§9.4.2#r150": [32, 37]
  "§9.4.2#r151": [114, 123]
  "§9.4.2#r152": 41
  "§9.4.3#b4": 50
  "§9.4.4#r11": [53, 54]
  "§9.4.4#r48": [7, 14, 15]
  "§9.4.4#r49": [43, 44]
  "§9.4.4#r50": [53, 54, 55, 61]
  "§9.4.4#r51": [102, 109]
  "§9.4.4#r53": [30, 31, 35]
  "§9.8#r12": 44
  "§9.8#r13": [31, 32, 36, 37]
  "§9.8#r14": 54
  "§9.10.1#r11": 129
  "§10#b1": 8
  "§11#r5": 102
anchor: []
---

# Approval dan penentuan approver pada transaksi Transfer

## Prerequisites
- Aktor: Rina (DU-104-1), pengaju Transfer; Ali (DU-104-2) dan Anto (DU-104-3), Approver Group asal; Dewi (DU-104-4) dan Dian (DU-104-5), Approver Group tujuan; Putri (DU-104-6), Approver Group induk; Nono (DU-104-7), Rudi (DU-104-8), dan Lena (DU-104-9), Approver yang tidak eligible; Gita (DU-104-10), Gani (DU-104-11), Gema (DU-104-13), Gina (DU-104-14), Gino (DU-104-15), dan Hana (DU-104-17), Group Manager; Hadi (DU-104-16), Approver Group Hybrid; Tomi (DU-104-12), Total Control; Wulan (DU-104-18), admin Transaction Settings; Gara (DU-104-83), Group Manager Group induk.
- Data:
  - DU-104-1: User: Name `Rina Pengaju {runId}`, Role `Aktor Transfer`, Cakupan Transfer `Group Gudang Asal {runId}, Gudang Anak {runId}, Gudang Sendiri {runId}, Gudang Tanpa Approver {runId}, Gudang Manager Saja {runId}, Gudang Hybrid {runId}, Gudang Asal Kosong {runId}, Kantor Pusat {runId}, Gudang Cabang Manajer {runId}`, Role Transaksi `Approver pada Group Gudang Asal {runId} dan Gudang Sendiri {runId}`.
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
  - DU-104-21: Group: Name `Gudang Tujuan {runId}`, Group induk `Regional Jawa {runId}`, Override Group `Approval type Any one approver, Approval scope Origin only, Require approval OFF`.
  - DU-104-22: Group: Name `Regional Sumatra {runId}`, Group induk `root client`.
  - DU-104-23: Group: Name `Gudang Luar {runId}`, Group induk `Regional Sumatra {runId}`.
  - DU-104-24: Group: Name `Divisi Induk {runId}`, Group induk `root client`.
  - DU-104-25: Group: Name `Gudang Anak {runId}`, Group induk `Divisi Induk {runId}`.
  - DU-104-26: Group: Name `Gudang Peran Ganda {runId}`, Group induk `root client`.
  - DU-104-27: Group: Name `Gudang Sendiri {runId}`, Group induk `root client`.
  - DU-104-28: Group: Name `Gudang Tanpa Approver {runId}`, Group induk `root client`.
  - DU-104-29: Group: Name `Gudang Manager Saja {runId}`, Group induk `root client`.
  - DU-104-30: Group: Name `Gudang Hybrid {runId}`, Group induk `root client`.
  - DU-104-31: Group: Name `Gudang Asal Kosong {runId}`, Group induk `root client`.
  - DU-104-32: Group: Name `Kantor Pusat {runId}`, Group induk `root client`.
  - DU-104-33: Group: Name `Kantor Wilayah {runId}`, Group induk `root client`.
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
- Kondisi:
  - Setiap aset dengan override aset memakai nilai efektif dari override itu, dan aset tanpa override aset memakai nilai efektif dari override Group atau Company default.
  - Semua user di atas memiliki akun aktif, kecuali yang tertulis Status `Inactive`, dan kredensialnya disediakan fase 2.
  - Approval Workflow tersedia di plan client.

## Test Steps

### Any one approver: keputusan Approve pertama menyelesaikan approval dan approver lain menjadi Not Involved
1. Rina mengajukan Transfer aset `Pallet Besi OR 1 {runId}` ke Group `Gudang Tujuan {runId}`
2. Verifikasi baris Transfer aset `Pallet Besi OR 1 {runId}` berstatus `Waiting for Approval`, karena nilai efektif Require approval `ON` dan Auto-approve `OFF` dari setting aset itu
3. Verifikasi Ali dan Anto, Approver Role Transaksi pada Group asal, masing-masing menerima permintaan approval, dan Approval type berlaku karena ada beberapa approver
4. Verifikasi baris itu belum ditutup oleh Transaction timeout, yaitu masih berstatus `Waiting for Approval` dengan permintaan approval Ali dan Anto masih terbuka, karena hitungan Transaction timeout dimulai sejak baris masuk status itu
5. Ali menyetujui permintaan approval atas baris Transfer aset `Pallet Besi OR 1 {runId}`
6. Verifikasi baris Transfer aset `Pallet Besi OR 1 {runId}` berstatus `Waiting for Send`, yaitu status disetujui yang belum dikirim, setelah satu Approver menyetujui, karena Approval type `Any one approver` memakai rule OR
7. Verifikasi permintaan Anto atas baris itu berstatus `Not Involved`
8. Verifikasi baris itu tidak menunggu level approval lanjutan, karena approval hanya satu level

### Any one approver: keputusan Reject pertama menolak transaksi
9. Rina mengajukan Transfer aset `Pallet Besi OR 2 {runId}` ke Group `Gudang Tujuan {runId}`
10. Ali menolak permintaan approval atas baris Transfer aset `Pallet Besi OR 2 {runId}`
11. Verifikasi baris Transfer aset `Pallet Besi OR 2 {runId}` berstatus `Rejected` dan permintaan Anto berstatus `Not Involved`

### Any one approver: keputusan yang masuk hampir bersamaan, yang pertama menentukan
12. Rina mengajukan Transfer aset `Pallet Besi OR 3 {runId}` ke Group `Gudang Tujuan {runId}`
13. Ali menyetujui dan Anto menolak permintaan approval atas baris Transfer aset `Pallet Besi OR 3 {runId}` pada saat hampir bersamaan
14. Verifikasi baris Transfer aset `Pallet Besi OR 3 {runId}` memiliki tepat satu status final, `Waiting for Send` atau `Rejected`, yang berasal dari keputusan pertama yang masuk
15. Verifikasi approver yang keputusannya masuk belakangan berstatus `Not Involved` dan permintaannya ditutup

### All approvers (AND): semua approver harus menyetujui
16. Rina mengajukan Transfer aset `Pallet Besi AND 1 {runId}` ke Group `Gudang Tujuan {runId}`
17. Ali menyetujui permintaan approval atas baris Transfer aset `Pallet Besi AND 1 {runId}`
18. Verifikasi baris Transfer aset `Pallet Besi AND 1 {runId}` masih berstatus `Waiting for Approval`, menunggu approver lain
19. Anto menyetujui permintaan approval atas baris Transfer aset `Pallet Besi AND 1 {runId}`
20. Verifikasi baris Transfer aset `Pallet Besi AND 1 {runId}` berstatus `Waiting for Send` setelah semua Approver menyetujui, karena Approval type `All approvers (AND)` memakai rule AND

### All approvers (AND): satu Reject langsung menolak transaksi
21. Rina mengajukan Transfer aset `Pallet Besi AND 2 {runId}` ke Group `Gudang Tujuan {runId}`
22. Ali menolak permintaan approval atas baris Transfer aset `Pallet Besi AND 2 {runId}`
23. Verifikasi baris Transfer aset `Pallet Besi AND 2 {runId}` berstatus `Rejected` dan permintaan Anto berstatus `Not Involved`

### Approver ditentukan dari Role Transaksi pada Group aset atau ancestor-nya, hanya user yang eligible
24. Rina mengajukan Transfer aset `Rak Gudang Anak {runId}` ke Group `Gudang Tujuan {runId}`
25. Verifikasi Putri, yang ditugaskan Role Transaksi `Approver` pada Group induk `Divisi Induk {runId}`, menerima permintaan approval atas baris Transfer aset `Rak Gudang Anak {runId}`, karena penugasan mencakup Group turunan dan tanpa langkah eskalasi tersendiri
26. Verifikasi Nono, Rudi, dan Lena, yang ditugaskan Approver pada Group `Gudang Anak {runId}` tetapi tidak eligible, tidak menerima permintaan approval
27. Putri menyetujui permintaan approval atas baris Transfer aset `Rak Gudang Anak {runId}`
28. Verifikasi baris Transfer aset `Rak Gudang Anak {runId}` berstatus `Waiting for Send`

### Pengaju Group Manager yang menaungi Group aset: seluruh langkah approval dilewati
29. Gita mengajukan Transfer aset `Troli Kondisi A 1 {runId}` ke Group `Gudang Tujuan {runId}`
30. Verifikasi langkah approval dilewati dan baris Transfer aset `Troli Kondisi A 1 {runId}` langsung berstatus `Waiting for Send`, walau Ali dan Anto adalah Approver pada Group asal
31. Verifikasi log transaksi baris itu memuat `Approved by Gita Manajer Asal {runId} (Group Manager — requester)`
32. Verifikasi Modified By log itu adalah `Gita Manajer Asal {runId}`, bukan `System`
33. Verifikasi `Gita Manajer Asal {runId}` tidak tercatat sebagai approver baris itu, karena bypass bukan pengaju menjadi approver transaksinya sendiri

### Pengaju Total Control: seluruh langkah approval dilewati
34. Tomi mengajukan Transfer aset `Troli Kondisi A 2 {runId}` ke Group `Gudang Tujuan {runId}`
35. Verifikasi langkah approval dilewati dan baris Transfer aset `Troli Kondisi A 2 {runId}` langsung berstatus `Waiting for Send`
36. Verifikasi log transaksi baris itu memuat `Approved by Tomi Kontrol {runId} (Total Control — requester)`
37. Verifikasi Modified By log itu adalah `Tomi Kontrol {runId}`, bukan `System`

### Kondisi A dievaluasi lebih dulu daripada self-approval guard
38. Gema mengajukan Transfer aset `Meja Peran Ganda {runId}` ke Group `Gudang Tujuan {runId}`
39. Verifikasi baris Transfer aset `Meja Peran Ganda {runId}` langsung berstatus `Waiting for Send` dengan log `Approved by Gema Manajer Sendiri {runId} (Group Manager — requester)`, bukan `Approved by system (no independent approver)`, walau Gema juga satu-satunya Approver pada Group asal

### Kondisi A tidak berlaku bila Require approval efektif OFF
40. Gita mengajukan Transfer aset `Troli Kondisi A 4 {runId}` ke Group `Gudang Tujuan {runId}`
41. Verifikasi baris Transfer aset `Troli Kondisi A 4 {runId}` berstatus `Waiting for Send`, dan tidak ada log `Approved by Gita Manajer Asal {runId} (Group Manager — requester)` untuk baris itu

### Pengaju satu-satunya Approver eligible: approval dilewati dan transaksi Approved oleh sistem
42. Rina mengajukan Transfer aset `Meja Gudang Sendiri {runId}` ke Group `Gudang Tujuan {runId}`
43. Verifikasi langkah approval dilewati dan baris Transfer aset `Meja Gudang Sendiri {runId}` langsung berstatus `Waiting for Send`
44. Verifikasi log transaksi baris itu memuat `Approved by system (no independent approver)` dengan Modified By `System`
45. Verifikasi Rina tidak menjadi approver transaksinya sendiri pada baris itu

### Pengaju dikecualikan dari daftar approver dan tidak dapat menyetujui transaksinya sendiri
46. Rina mengajukan Transfer aset `Pallet Besi Guard {runId}` ke Group `Gudang Tujuan {runId}`
47. Verifikasi baris Transfer aset `Pallet Besi Guard {runId}` berstatus `Waiting for Approval` dan permintaan approval diterima Ali dan Anto, sebagian Approver eligible yang bukan pengaju
48. Verifikasi Rina tidak ada dalam daftar approver baris itu, walau ia ditugaskan Role Transaksi `Approver` pada Group asal
49. Rina menyetujui permintaan approval atas baris Transfer aset `Pallet Besi Guard {runId}`, yang ia ajukan sendiri
50. Verifikasi persetujuan Rina ditolak dan baris Transfer aset `Pallet Besi Guard {runId}` tetap berstatus `Waiting for Approval`

### Tidak ada Approver eligible dan tidak ada Group Manager: rute jatuh ke Total Control
51. Tomi mencatat jumlah notifikasi `approver_required` yang terkait Group `Gudang Tanpa Approver {runId}`
52. Rina mengajukan Transfer aset `Meja Tanpa Approver 1 {runId}` ke Group `Gudang Tujuan {runId}`
53. Verifikasi baris Transfer aset `Meja Tanpa Approver 1 {runId}` berstatus `Waiting for Approval` dan permintaan approval diterima Tomi dan Wulan, semua user Total Control, karena tidak ada Approver eligible dan tidak ada Group Manager aktif yang menaungi Group asal
54. Verifikasi pencatatan rute itu ada di log transaksi baris tersebut dengan Modified By `System`
55. Verifikasi satu notifikasi `approver_required` baru terkirim untuk pengajuan itu
56. Rina mengajukan Transfer aset `Meja Tanpa Approver 2 {runId}` ke Group `Gudang Tujuan {runId}`
57. Verifikasi pengajuan kedua itu mengirim notifikasi `approver_required` tambahan miliknya sendiri, sehingga jumlahnya bertambah dua sejak dicatat
58. Tomi menyetujui permintaan approval atas baris Transfer aset `Meja Tanpa Approver 1 {runId}`
59. Verifikasi baris Transfer aset `Meja Tanpa Approver 1 {runId}` berstatus `Waiting for Send`, karena Approval type berlaku pada himpunan fallback dan persetujuan satu approver cukup

### Tidak ada Approver eligible: Group Manager yang menaungi menjadi approver fallback
60. Rina mengajukan Transfer aset `Meja Manajer 1 {runId}` ke Group `Gudang Tujuan {runId}`
61. Verifikasi Gina dan Gino, Group Manager yang menaungi Group asal tanpa penugasan Approver, masing-masing menerima permintaan approval atas baris Transfer aset `Meja Manajer 1 {runId}`
62. Gina menyetujui permintaan approval atas baris Transfer aset `Meja Manajer 1 {runId}`
63. Verifikasi baris Transfer aset `Meja Manajer 1 {runId}` berstatus `Waiting for Send` dan permintaan Gino berstatus `Not Involved`, karena Any one approver pada himpunan fallback cukup satu
64. Rina mengajukan Transfer aset `Meja Manajer 2 {runId}` ke Group `Gudang Tujuan {runId}`
65. Gina menyetujui permintaan approval atas baris Transfer aset `Meja Manajer 2 {runId}`
66. Verifikasi baris Transfer aset `Meja Manajer 2 {runId}` masih berstatus `Waiting for Approval`, karena All approvers (AND) pada himpunan fallback menuntut semua Group Manager menyetujui
67. Gino menyetujui permintaan approval atas baris Transfer aset `Meja Manajer 2 {runId}`
68. Verifikasi baris Transfer aset `Meja Manajer 2 {runId}` berstatus `Waiting for Send`

### Ada Approver terdaftar: Group Manager tanpa penugasan tidak dihitung dalam AND tetapi keputusannya override final
69. Rina mengajukan Transfer aset `Meja Hybrid 1 {runId}` ke Group `Gudang Tujuan {runId}`
70. Hadi, Approver terdaftar pada Group asal, menyetujui permintaan approval atas baris Transfer aset `Meja Hybrid 1 {runId}`
71. Verifikasi baris Transfer aset `Meja Hybrid 1 {runId}` berstatus `Waiting for Send` walau Hana, Group Manager tanpa penugasan, belum memutuskan, karena Hana tidak dihitung dalam rule AND
72. Rina mengajukan Transfer aset `Meja Hybrid 2 {runId}` ke Group `Gudang Tujuan {runId}`
73. Hana menolak permintaan approval atas baris Transfer aset `Meja Hybrid 2 {runId}`
74. Verifikasi baris Transfer aset `Meja Hybrid 2 {runId}` berstatus `Rejected` dan permintaan Hadi berstatus `Not Involved`, karena keputusan Group Manager tetap bersifat override final

### Notifikasi approver_required saat Save konfigurasi Approval menimbulkan kondisi tanpa Approver
75. Wulan mencatat jumlah notifikasi `approver_required` yang terkait Group `Gudang Tanpa Approver {runId}`
76. Wulan menambah override aset untuk aset `Meja Save 1 {runId}` di All categories dengan Require approval `ON` dan Auto-approve `OFF`
77. Verifikasi satu notifikasi `approver_required` baru terkirim karena Save konfigurasi Approval menimbulkan kondisi tidak ada Approver untuk Transfer aset itu
78. Wulan menambah override aset untuk aset `Meja Save 2 {runId}` di All categories dengan Photo at end `OFF`
79. Verifikasi jumlah notifikasi `approver_required` tidak bertambah, karena konfigurasi Approval tidak diubah

### Auto-approve ON: baris lolos bila Group tujuan berinduk langsung sama dengan Group asal
80. Rina mengajukan Transfer aset `Gerobak Auto 1 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, yang berinduk langsung sama
81. Verifikasi baris Transfer aset `Gerobak Auto 1 {runId}` langsung berstatus `Waiting for Send` dan melewati approval di kedua sisi pada Approval scope `Both`
82. Rina mengajukan Transfer aset `Gerobak Auto 2 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Luar {runId}`, yang berinduk berbeda
83. Verifikasi baris Transfer aset `Gerobak Auto 2 {runId}` berstatus `Waiting for Approval`, karena Group tujuan tidak berinduk langsung sama dengan Group asal
84. Rina mengajukan Transfer aset `Gerobak Auto 3 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, dengan Auto-approve when destination in same parent Group `OFF` pada aset itu
85. Verifikasi baris Transfer aset `Gerobak Auto 3 {runId}` berstatus `Waiting for Approval` dan mengikuti approval normal
86. Rina mengajukan Transfer aset `Gerobak Auto 4 {runId}` dari Group `Kantor Pusat {runId}` ke Group `Kantor Wilayah {runId}`, keduanya Group tingkat atas
87. Verifikasi baris Transfer aset `Gerobak Auto 4 {runId}` langsung berstatus `Waiting for Send`, karena Group tingkat atas dianggap berinduk root client sehingga antar Group tingkat atas memenuhi kondisi

### Auto-approve dinilai per baris dan sesudah Kondisi A
88. Rina mengajukan satu Transfer berisi aset `Gerobak Auto 5 {runId}` dan `Gerobak Auto 6 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
89. Verifikasi baris Transfer aset `Gerobak Auto 5 {runId}`, yang Auto-approve-nya `ON`, langsung berstatus `Waiting for Send`
90. Verifikasi baris Transfer aset `Gerobak Auto 6 {runId}`, yang Auto-approve-nya `OFF`, berstatus `Waiting for Approval` dan mengikuti aturan efektifnya sendiri walau berada pada pengajuan yang sama
91. Gita mengajukan Transfer aset `Gerobak Auto 7 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Luar {runId}`, yang tidak memenuhi Auto-approve
92. Verifikasi sisi Group asal dilewati karena Kondisi A, dan sisi Group tujuan `Gudang Luar {runId}` tetap menunggu approval, sehingga baris Transfer aset `Gerobak Auto 7 {runId}` berstatus `Waiting for Approval`, karena Approval scope `Both` dan Group tujuan tidak memenuhi Auto-approve

### Approval scope Origin only: hanya Approver yang mencakup Group asal
93. Rina mengajukan Transfer aset `Mesin Scope Asal {runId}` ke Group `Gudang Tujuan {runId}`
94. Verifikasi Ali dan Anto, Approver yang mencakup Group asal, menerima permintaan approval, dan Dewi serta Dian, Approver Group tujuan, tidak menerimanya
95. Ali menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Asal {runId}`
96. Verifikasi baris Transfer aset `Mesin Scope Asal {runId}` berstatus `Waiting for Send` tanpa persetujuan sisi Group tujuan

### Approval scope Destination only: hanya Approver yang mencakup Group tujuan
97. Rina mengajukan Transfer aset `Mesin Scope Tujuan {runId}` ke Group `Gudang Tujuan {runId}`
98. Verifikasi Dewi dan Dian, Approver yang mencakup Group tujuan, menerima permintaan approval, dan Ali serta Anto tidak menerimanya
99. Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Tujuan {runId}`
100. Verifikasi baris Transfer aset `Mesin Scope Tujuan {runId}` berstatus `Waiting for Send` tanpa persetujuan sisi Group asal

### Approval scope Both: kedua sisi menyetujui, nilai efektif diselesaikan dari aset dan Group asal
101. Rina mengajukan Transfer aset `Mesin Scope Both 1 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
102. Verifikasi Ali dan Anto menerima permintaan approval sebagai sisi Group asal, dan Dewi serta Dian menerima permintaan approval sebagai sisi Group tujuan, masing-masing sisi dengan daftar Approver-nya sendiri, dan nilai efektif Require approval `ON` diselesaikan dari Group asal, bukan dari Group tujuan `Gudang Tujuan {runId}` yang ber-Require approval `OFF`
103. Verifikasi Rina tidak menjadi approver Transfer-nya sendiri walau ia ditugaskan Role Transaksi `Approver` pada Group asal
104. Ali dan Anto menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 1 {runId}`
105. Verifikasi baris Transfer aset `Mesin Scope Both 1 {runId}` masih berstatus `Waiting for Approval`, karena sisi Group tujuan belum menyetujui
106. Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 1 {runId}`
107. Verifikasi baris Transfer aset `Mesin Scope Both 1 {runId}` masih berstatus `Waiting for Approval`, karena Approval type `All approvers (AND)` dari Group asal menuntut Dian menyetujui dan Group tujuan, yang Approval type-nya `Any one approver`, tidak ikut menentukan nilai efektif
108. Dian menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 1 {runId}`
109. Verifikasi baris Transfer aset `Mesin Scope Both 1 {runId}` berstatus `Waiting for Send`, karena kedua sisi telah menyetujui

### Approval scope Both: nilai efektif diselesaikan per baris dari aset masing-masing
110. Rina mengajukan satu Transfer berisi aset `Mesin Baris Asal {runId}` dan `Mesin Baris Tujuan {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
111. Verifikasi baris Transfer aset `Mesin Baris Asal {runId}`, yang Approval scope-nya `Origin only`, hanya menunggu Ali dan Anto, dan baris Transfer aset `Mesin Baris Tujuan {runId}`, yang Approval scope-nya `Destination only`, hanya menunggu Dewi dan Dian

### Approval scope Both: Group Manager yang menaungi Group asal hanya melewati sisi Group asal
112. Gita mengajukan Transfer aset `Mesin Scope Both 2 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
113. Verifikasi sisi Group asal dilewati dan sisi Group tujuan masih menunggu Dewi dan Dian, sehingga baris Transfer aset `Mesin Scope Both 2 {runId}` berstatus `Waiting for Approval`
114. Verifikasi log transaksi baris itu mencatat Kondisi A untuk sisi Group asal yang dilewati
115. Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 2 {runId}`
116. Verifikasi baris Transfer aset `Mesin Scope Both 2 {runId}` berstatus `Waiting for Send`, karena kedua sisi telah dilewati atau disetujui

### Approval scope Both: Group Manager yang menaungi Group tujuan hanya melewati sisi Group tujuan
117. Gani mengajukan Transfer aset `Mesin Scope Both 3 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
118. Verifikasi sisi Group tujuan dilewati dan sisi Group asal masih menunggu Ali dan Anto, sehingga baris Transfer aset `Mesin Scope Both 3 {runId}` berstatus `Waiting for Approval`
119. Ali menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 3 {runId}`
120. Verifikasi baris Transfer aset `Mesin Scope Both 3 {runId}` berstatus `Waiting for Send`

### Approval scope Both: Total Control melewati kedua sisi
121. Tomi mengajukan Transfer aset `Mesin Scope Both 4 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
122. Verifikasi baris Transfer aset `Mesin Scope Both 4 {runId}` langsung berstatus `Waiting for Send`, karena Total Control melewati kedua sisi
123. Verifikasi log transaksi baris itu mencatat Kondisi A untuk sisi Group asal dan sisi Group tujuan yang dilewati

### Approval scope Both: aturan tidak-ada-Approver berlaku per sisi
124. Rina mengajukan Transfer aset `Mesin Scope Both 5 {runId}` dari Group `Gudang Asal Kosong {runId}` ke Group `Gudang Tujuan {runId}`
125. Verifikasi sisi Group asal, yang tidak punya Approver eligible, jatuh ke Tomi dan Wulan sebagai Total Control, dan sisi Group tujuan menunggu Dewi dan Dian
126. Tomi dan Dewi menyetujui permintaan approval atas baris Transfer aset `Mesin Scope Both 5 {runId}`
127. Verifikasi baris Transfer aset `Mesin Scope Both 5 {runId}` berstatus `Waiting for Send`

### Require approval efektif OFF: langkah approval dilewati walau ada Approver dan Approval scope
128. Rina mengajukan Transfer aset `Mesin Approval Off {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`
129. Verifikasi baris Transfer aset `Mesin Approval Off {runId}` langsung berstatus `Waiting for Send`, karena nilai efektif Require approval `OFF` sehingga langkah approval dilewati dan pengajuan lanjut ke tahap eksekusi transaksinya
130. Verifikasi Ali, Anto, Dewi, dan Dian tidak menerima permintaan approval atas baris itu, karena penugasan Role Transaksi `Approver` tidak dipakai

### Pengajuan yang ditolak aturan Deny tidak sampai ke evaluasi approval
131. Rina mengajukan Transfer aset `Mesin Deny Approval {runId}` ke Group `Gudang Tujuan {runId}`
132. Verifikasi pengajuan ditolak oleh Deny pada override aset, tidak ada baris Transfer untuk aset `Mesin Deny Approval {runId}`, dan Ali serta Anto tidak menerima permintaan approval, karena Deny pada override dievaluasi sebelum Approval

### Baris yang lolos Auto-approve tetap dinilai sesudah Kondisi A dan self-approval guard
133. Gita mengajukan Transfer aset `Gerobak Auto 8 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, yang berinduk langsung sama sehingga baris memenuhi Auto-approve
134. Verifikasi baris Transfer aset `Gerobak Auto 8 {runId}` berstatus `Waiting for Send` dengan log `Approved by Gita Manajer Asal {runId} (Group Manager — requester)`, karena Kondisi A dinilai lebih dulu daripada Auto-approve
135. Rina mengajukan Transfer aset `Gerobak Auto 9 {runId}` dari Group `Gudang Sendiri {runId}` ke Group `Kantor Wilayah {runId}`, keduanya Group tingkat atas sehingga baris memenuhi Auto-approve
136. Verifikasi baris Transfer aset `Gerobak Auto 9 {runId}` berstatus `Waiting for Send` dengan log `Approved by system (no independent approver)` dan Modified By `System`, karena self-approval guard dinilai lebih dulu daripada Auto-approve

### Destination scope Within same parent Group dan aturan tetap dievaluasi sebelum Approval
137. Rina mengajukan Transfer aset `Mesin Scope Induk 1 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Tujuan {runId}`, yang berinduk langsung sama
138. Verifikasi pengajuan diterima dan baris Transfer aset `Mesin Scope Induk 1 {runId}` berstatus `Waiting for Approval`, karena Group tujuan memenuhi Destination scope `Within same parent Group`
139. Rina mengajukan Transfer aset `Mesin Scope Induk 2 {runId}` dari Group `Gudang Asal {runId}` ke Group `Gudang Luar {runId}`, yang berinduk berbeda
140. Verifikasi pengajuan ditolak, tidak ada baris Transfer untuk aset `Mesin Scope Induk 2 {runId}`, dan Ali serta Anto tidak menerima permintaan approval, karena Eligibility (Destination scope) dievaluasi sebelum Approval
141. Rina mengajukan Transfer aset `Mesin Scope Induk 3 {runId}` dari Group `Kantor Pusat {runId}` ke Group `Kantor Wilayah {runId}`, keduanya Group tingkat atas
142. Verifikasi pengajuan diterima dan baris Transfer aset `Mesin Scope Induk 3 {runId}` berstatus `Waiting for Approval`, karena Group tingkat atas dianggap berinduk root client sehingga memenuhi Destination scope `Within same parent Group`
143. Rina mengajukan Transfer aset `Genset Hilang Approval {runId}`, berkondisi `Missing`, ke Group `Gudang Tujuan {runId}`
144. Verifikasi pengajuan ditolak, tidak ada baris Transfer untuk aset `Genset Hilang Approval {runId}`, dan Ali serta Anto tidak menerima permintaan approval, karena aturan tetap kondisi `Missing` dievaluasi sebelum Approval

### Group Manager pada ancestor Group aset menjadi approver dan dapat melewati approval
145. Rina mengajukan Transfer aset `Meja Cabang Manajer 1 {runId}` ke Group `Gudang Tujuan {runId}`
146. Verifikasi Gara, Group Manager yang menaungi `Wilayah Manajer {runId}` sebagai ancestor Group aset, menerima permintaan approval atas baris Transfer aset `Meja Cabang Manajer 1 {runId}`, karena tidak ada Approver eligible pada Group aset dan Group Manager pada ancestor-nya menjadi approver fallback
147. Gara menyetujui permintaan approval atas baris Transfer aset `Meja Cabang Manajer 1 {runId}`
148. Verifikasi baris Transfer aset `Meja Cabang Manajer 1 {runId}` berstatus `Waiting for Send`
149. Gara mengajukan Transfer aset `Meja Cabang Manajer 2 {runId}` ke Group `Gudang Tujuan {runId}`
150. Verifikasi langkah approval dilewati dan baris Transfer aset `Meja Cabang Manajer 2 {runId}` berstatus `Waiting for Send` dengan log `Approved by Gara Manajer Wilayah {runId} (Group Manager — requester)`, karena Gara menaungi ancestor Group aset

### Approval scope Both: Group Manager pada sisi tanpa Approver menerima permintaan untuk sisinya saja
151. Rina mengajukan Transfer aset `Meja Manajer Both {runId}` dari Group `Gudang Manager Saja {runId}` ke Group `Gudang Tujuan {runId}`
152. Verifikasi Gina dan Gino, Group Manager Group asal tanpa penugasan Approver, menerima permintaan approval untuk sisi Group asal saja, dan Dewi serta Dian menerima permintaan approval untuk sisi Group tujuan
153. Gina menyetujui permintaan approval sisi Group asal atas baris Transfer aset `Meja Manajer Both {runId}`
154. Verifikasi baris Transfer aset `Meja Manajer Both {runId}` masih berstatus `Waiting for Approval`, karena sisi Group tujuan tetap menunggu approval dari Approver-nya sendiri
155. Dewi menyetujui permintaan approval sisi Group tujuan atas baris Transfer aset `Meja Manajer Both {runId}`
156. Verifikasi baris Transfer aset `Meja Manajer Both {runId}` berstatus `Waiting for Send`, karena kedua sisi telah menyetujui
