---
id: TC-FA-FATR-BE-101-approval-assign-dep-assign
title: "Approval dan penentuan approver pada transaksi Assign"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r83", "§4.1#r202", "§4.1#r203", "§4.1#r204", "§4.1#r205", "§9.2#b379", "§9.2#b380", "§9.2#b381", "§9.2#b440", "§9.2#b442", "§9.2#b443", "§9.2#b445", "§9.2#b447", "§9.2#b448", "§9.2#b449", "§9.2#b450", "§9.2#b452", "§9.2#b454", "§9.2#b455", "§9.2#b456", "§9.2#b457", "§9.2#b459", "§9.2#b460", "§9.2#b463", "§9.2#b464", "§9.2#b465", "§9.2#b467", "§9.2#b468", "§9.2#b469", "§9.2#b470", "§9.2#b471", "§9.2#b474", "§9.2#b475", "§9.2#b476", "§9.2#b487", "§9.2#b488", "§9.2#b489", "§9.2#b490", "§9.2#b491", "§9.2#b492", "§9.2#b493", "§9.2#b462", "§9.2#b478", "§9.2#b479", "§9.2#b482", "§9.2#b480", "§9.2#b481", "§9.2#b533", "§9.2#b534", "§9.2#b536", "§9.2#b537", "§9.2#b539", "§9.2#b540", "§9.2#b548", "§9.2#b549", "§9.2#b550", "§9.2#b551", "§9.2#b552", "§9.2#b554", "§9.4.1#r20", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r42", "§9.4.2#r138", "§9.4.2#r139", "§9.4.2#r156", "§9.4.2#r157", "§9.4.2#r158", "§9.4.2#r160", "§9.4.3#b4", "§9.4.4#r11", "§9.4.4#r48", "§9.4.4#r49", "§9.4.4#r50", "§9.4.4#r53", "§9.8#r10", "§9.8#r11", "§9.8#r12", "§10#b1", "§9.2#r11"]
smoke: []
dependsOn:
  - "Assign: pengajuan, handover, Reassign, dan Unassign"
owner: BE
trace:
  "§Aturan Logika Modul#r83": [107, 135]
  "§4.1#r202": 6
  "§4.1#r203": [8, 13]
  "§4.1#r204": [22, 24]
  "§4.1#r205": [9, 27]
  "§9.2#b379": [98, 100, 109, 111, 126, 128, 130, 132]
  "§9.2#b380": 3
  "§9.2#b381": [4, 32]
  "§9.2#b440": 10
  "§9.2#b442": [8, 86]
  "§9.2#b443": 24
  "§9.2#b445": 3
  "§9.2#b447": [4, 6, 32]
  "§9.2#b448": 4
  "§9.2#b449": 5
  "§9.2#b450": [33, 34, 114, 115, 116]
  "§9.2#b452": 41
  "§9.2#b454": [8, 22]
  "§9.2#b455": [8, 13]
  "§9.2#b456": [22, 24]
  "§9.2#b457": [9, 14, 27, 28]
  "§9.2#b459": 69
  "§9.2#b460": [69, 75, 118]
  "§9.2#b463": [73, 94, 122, 123]
  "§9.2#b464": 79
  "§9.2#b465": 72
  "§9.2#b467": 84
  "§9.2#b468": [82, 87]
  "§9.2#b469": 90
  "§9.2#b470": 91
  "§9.2#b471": [82, 86]
  "§9.2#b474": [35, 44]
  "§9.2#b475": 36
  "§9.2#b476": 37
  "§9.2#b487": [35, 50]
  "§9.2#b488": 44
  "§9.2#b489": [46, 50]
  "§9.2#b490": [46, 57]
  "§9.2#b491": [52, 54]
  "§9.2#b492": 62
  "§9.2#b493": [65, 66]
  "§9.2#b462": [70, 76]
  "§9.2#b478": [37, 102]
  "§9.2#b479": 102
  "§9.2#b482": 104
  "§9.2#b480": 37
  "§9.2#b481": 39
  "§9.2#b533": 8
  "§9.2#b534": 9
  "§9.2#b536": 90
  "§9.2#b537": 90
  "§9.2#b539": [35, 44]
  "§9.2#b540": 37
  "§9.2#b548": [69, 75]
  "§9.2#b549": [69, 75, 118, 122]
  "§9.2#b550": [70, 119, 123]
  "§9.2#b551": 76
  "§9.2#b552": 71
  "§9.2#b554": 79
  "§9.4.1#r20": 82
  "§9.4.2#r37": 106
  "§9.4.2#r40": [91, 93]
  "§9.4.2#r42": [17, 18]
  "§9.4.2#r138": [35, 44]
  "§9.4.2#r139": 36
  "§9.4.2#r156": [69, 75]
  "§9.4.2#r157": [70, 76]
  "§9.4.2#r158": 71
  "§9.4.2#r160": 79
  "§9.4.3#b4": [84, 93]
  "§9.4.4#r11": 36
  "§9.4.4#r48": [17, 18]
  "§9.4.4#r49": 90
  "§9.4.4#r50": 35
  "§9.4.4#r53": [69, 75]
  "§9.8#r10": [91, 92]
  "§9.8#r11": [70, 76]
  "§9.8#r12": 36
  "§10#b1": 10
  "§9.2#r11": [35, 44]
---

# Approval dan penentuan approver pada transaksi Assign

## Prerequisites
- Aktor: Admin `Budi Santoso {runId}` (Total Control entitas; membuat override dan, pada blok Kondisi A, mengajukan transaksi sebagai Total Control); `Tia Anggraini {runId}` (pengaju Assign, bukan Group Manager dan bukan Total Control); Approver, Group Manager, dan Total Control sesuai data di bawah.
- Data:
  - DU-101-1: User: Name `Budi Santoso {runId}`, Status `Aktif`, Role `Total Control entitas`; user di entitas suite.
  - DU-101-2: User: Name `Tia Anggraini {runId}`, Status `Aktif`, Role `Pengaju Assign, bukan Group Manager dan bukan Total Control`; user di entitas suite.
  - DU-101-3: User: Name `Wawan Hidayat {runId}`, Status `Aktif`, Role `Pemegang peran Approver`; user di entitas suite.
  - DU-101-4: User: Name `Citra Lestari {runId}`, Status `Aktif`, Role `Pemegang peran Approver`; user di entitas suite.
  - DU-101-5: User: Name `Sinta Maharani {runId}`, Status `Aktif`, Role `Pemegang peran Approver`; user di entitas suite.
  - DU-101-6: User: Name `Hadi Kurniawan {runId}`, Status `Aktif`, Role `Group Manager`; user di entitas suite.
  - DU-101-7: User: Name `Indra Wijaya {runId}`, Status `Aktif`, Role `Group Manager`; user di entitas suite.
  - DU-101-8: User: Name `Farah Nabila {runId}`, Status `Nonaktif`, Role `Pemegang peran Approver`; user di entitas suite.
  - DU-101-9: User: Name `Gilang Ramadhan {runId}`, Status `Aktif`, Role `Pemegang peran Approver untuk jenis transaksi lain`; user di entitas suite.
  - DU-101-10: User: Name `Eko Prasetyo {runId}`, Status `Aktif`, Role `Pemegang peran Approver`; user di entitas suite.
  - DU-101-11: User: Name `Fitri Anggraini {runId}`, Status `Aktif`, Role `Pemegang peran Approver`; user di entitas suite.
  - DU-101-12: User: Name `Rizal Fauzi {runId}`, Status `Aktif`, Role `Pemegang peran Approver`; user di entitas suite.
  - DU-101-13: Employee: Name `Bayu Saputra {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-101-14: Employee: Name `Putri Handayani {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-101-15: Employee: Name `Ratna Dewi {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-101-16: Employee: Name `Surya Atmaja {runId}`, Status `Aktif`, Akun login `Ada`; Employee assignee yang aktif dan punya akun login.
  - DU-101-17: Group: Name `Operasional Jawa Barat {runId}`; Group milik spec ini.
  - DU-101-18: Group: Name `Gudang Cikarang {runId}`, Group induk `Operasional Jawa Barat {runId}`; Group milik spec ini.
  - DU-101-19: Group: Name `Gudang Karawang {runId}`, Group induk `Operasional Jawa Barat {runId}`; Group milik spec ini.
  - DU-101-20: Group: Name `Gudang Bandung {runId}`; Group milik spec ini.
  - DU-101-21: Group: Name `Kantor Pusat Jakarta {runId}`; Group milik spec ini.
  - DU-101-22: Group: Name `Gudang Jakarta Timur {runId}`, Group induk `Kantor Pusat Jakarta {runId}`; Group milik spec ini.
  - DU-101-23: Group: Name `Gudang Semarang {runId}`; Group milik spec ini.
  - DU-101-24: Group: Name `Gudang Denpasar {runId}`; Group milik spec ini.
  - DU-101-25: Group: Name `Gudang Makassar {runId}`; Group milik spec ini.
  - DU-101-26: Group: Name `Gudang Medan {runId}`; Group milik spec ini.
  - DU-101-27: Group: Name `Gudang Padang {runId}`; Group milik spec ini.
  - DU-101-28: Group: Name `Gudang Pontianak {runId}`; Group milik spec ini.
  - DU-101-29: Group: Name `Gudang Palembang {runId}`; Group milik spec ini.
  - DU-101-30: Group: Name `Gudang Manado {runId}`; Group milik spec ini.
  - DU-101-31: Penugasan Role Transaksi: User `Wawan Hidayat {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Operasional Jawa Barat {runId}`; penugasan Approver.
  - DU-101-32: Penugasan Role Transaksi: User `Citra Lestari {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Cikarang {runId}`; penugasan Approver.
  - DU-101-33: Penugasan Role Transaksi: User `Sinta Maharani {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Karawang {runId}`; penugasan Approver.
  - DU-101-34: Penugasan Role Transaksi: User `Farah Nabila {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Makassar {runId}`; penugasan Approver.
  - DU-101-35: Penugasan Role Transaksi: User `Gilang Ramadhan {runId}`, Role Transaksi `Approver`, Jenis transaksi `transaksi lain`, Group `Gudang Makassar {runId}`; penugasan Approver.
  - DU-101-36: Penugasan Role Transaksi: User `Eko Prasetyo {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Denpasar {runId}`; penugasan Approver.
  - DU-101-37: Penugasan Role Transaksi: User `Fitri Anggraini {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Denpasar {runId}`; penugasan Approver.
  - DU-101-38: Penugasan Role Transaksi: User `Tia Anggraini {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Medan {runId}`; penugasan Approver.
  - DU-101-39: Penugasan Role Transaksi: User `Rizal Fauzi {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Medan {runId}`; penugasan Approver.
  - DU-101-40: Penugasan Role Transaksi: User `Tia Anggraini {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Padang {runId}`; penugasan Approver.
  - DU-101-41: Penugasan Group Manager: User `Hadi Kurniawan {runId}`, Group Manager di `Gudang Bandung {runId}`; Group Manager yang menaungi Group.
  - DU-101-42: Penugasan Group Manager: User `Hadi Kurniawan {runId}`, Group Manager di `Gudang Jakarta Timur {runId}`; Group Manager yang menaungi Group.
  - DU-101-43: Penugasan Group Manager: User `Indra Wijaya {runId}`, Group Manager di `Kantor Pusat Jakarta {runId}`; Group Manager yang menaungi Group.
  - DU-101-44: Penugasan Group Manager: User `Hadi Kurniawan {runId}`, Group Manager di `Gudang Denpasar {runId}`; Group Manager yang menaungi Group.
  - DU-101-45: Penugasan Group Manager: User `Hadi Kurniawan {runId}`, Group Manager di `Gudang Makassar {runId}`; Group Manager yang menaungi Group.
  - DU-101-46: Asset: Name `Laptop Lenovo ThinkPad L14 {runId}`, Group `Gudang Cikarang {runId}`; aset milik spec ini.
  - DU-101-47: Asset: Name `Laptop HP EliteBook 840 {runId}`, Group `Gudang Cikarang {runId}`; aset milik spec ini.
  - DU-101-48: Asset: Name `Laptop Dell Latitude 7440 {runId}`, Group `Gudang Cikarang {runId}`; aset milik spec ini.
  - DU-101-49: Asset: Name `Laptop Asus Zenbook 14 {runId}`, Group `Gudang Cikarang {runId}`; aset milik spec ini.
  - DU-101-50: Asset: Name `Laptop Acer Swift 3 {runId}`, Group `Gudang Cikarang {runId}`; aset milik spec ini.
  - DU-101-51: Asset: Name `Printer Epson L5290 {runId}`, Group `Gudang Karawang {runId}`; aset milik spec ini.
  - DU-101-52: Asset: Name `Printer Canon G4010 {runId}`, Group `Gudang Karawang {runId}`; aset milik spec ini.
  - DU-101-53: Asset: Name `Proyektor Epson EB-X49 {runId}`, Group `Gudang Makassar {runId}`; aset milik spec ini.
  - DU-101-54: Asset: Name `Proyektor BenQ MW550 {runId}`, Group `Gudang Makassar {runId}`; aset milik spec ini.
  - DU-101-55: Asset: Name `Monitor LG 24MK600 {runId}`, Group `Gudang Semarang {runId}`; aset milik spec ini.
  - DU-101-56: Asset: Name `Scanner Fujitsu ScanSnap iX1600 {runId}`, Group `Gudang Jakarta Timur {runId}`; aset milik spec ini.
  - DU-101-57: Asset: Name `Scanner Brother ADS-2200 {runId}`, Group `Gudang Jakarta Timur {runId}`; aset milik spec ini.
  - DU-101-58: Asset: Name `Tablet Samsung Galaxy Tab S8 {runId}`, Group `Gudang Denpasar {runId}`; aset milik spec ini.
  - DU-101-59: Asset: Name `Tablet Apple iPad 10 {runId}`, Group `Gudang Denpasar {runId}`; aset milik spec ini.
  - DU-101-60: Asset: Name `Kamera Canon EOS M50 {runId}`, Group `Gudang Bandung {runId}`; aset milik spec ini.
  - DU-101-61: Asset: Name `Kamera Sony ZV-E10 {runId}`, Group `Gudang Bandung {runId}`; aset milik spec ini.
  - DU-101-62: Asset: Name `Router Mikrotik hAP ax2 {runId}`, Group `Gudang Palembang {runId}`; aset milik spec ini.
  - DU-101-63: Asset: Name `Switch Cisco CBS250 {runId}`, Group `Gudang Medan {runId}`; aset milik spec ini.
  - DU-101-64: Asset: Name `Access Point Ubiquiti U6 {runId}`, Group `Gudang Padang {runId}`; aset milik spec ini.
  - DU-101-65: Asset: Name `Handphone Samsung Galaxy A54 {runId}`, Group `Gudang Pontianak {runId}`, Status `Assigned`, Pemegang `Ratna Dewi {runId}`; aset milik spec ini.
  - DU-101-66: Asset: Name `Handphone Xiaomi Redmi Note 12 {runId}`, Group `Gudang Pontianak {runId}`; aset milik spec ini.
  - DU-101-67: Asset: Name `Handphone Oppo A78 {runId}`, Group `Gudang Pontianak {runId}`; aset milik spec ini.
  - DU-101-68: Asset: Name `Server Dell PowerEdge T150 {runId}`, Group `Gudang Manado {runId}`; aset milik spec ini.
  - DU-101-76: User: Name `Susanti Wijaya {runId}`, Status `Aktif`, Role `Total Control entitas`; user di entitas suite.
  - DU-101-77: User: Name `Lukman Hakim {runId}`, Status `Aktif`, Role `Pemegang peran Approver dengan akses Read Only`; user di entitas suite.
  - DU-101-78: User: Name `Nanda Pratiwi {runId}`, Status `Aktif`, Role `Pemegang peran Approver tanpa lisensi addon`; user di entitas suite.
  - DU-101-79: User: Name `Yusuf Hakim {runId}`, Status `Aktif`, Role `Group Manager dan pemegang peran Approver`; user di entitas suite.
  - DU-101-80: Employee: Name `Dian Pertiwi {runId}`, Status `Nonaktif`, Akun login `Ada`; Employee assignee yang Nonaktif.
  - DU-101-81: Group: Name `Gudang Malang {runId}`; Group milik spec ini.
  - DU-101-82: Group: Name `Gudang Tangerang {runId}`; Group milik spec ini.
  - DU-101-83: Penugasan Role Transaksi: User `Lukman Hakim {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Malang {runId}`; penugasan Approver.
  - DU-101-84: Penugasan Role Transaksi: User `Nanda Pratiwi {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Malang {runId}`; penugasan Approver.
  - DU-101-85: Penugasan Role Transaksi: User `Yusuf Hakim {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Tangerang {runId}`; penugasan Approver.
  - DU-101-86: Penugasan Group Manager: User `Yusuf Hakim {runId}`, Group Manager di `Gudang Tangerang {runId}`; Group Manager yang menaungi Group.
  - DU-101-87: Asset: Name `Laptop Lenovo Yoga Slim 7 {runId}`, Group `Gudang Cikarang {runId}`; aset milik spec ini.
  - DU-101-88: Asset: Name `Printer Epson L3210 {runId}`, Group `Gudang Malang {runId}`; aset milik spec ini.
  - DU-101-89: Asset: Name `Scanner Canon DR-C225 {runId}`, Group `Gudang Jakarta Timur {runId}`; aset milik spec ini.
  - DU-101-90: Asset: Name `Printer Brother HL-L5100 {runId}`, Group `Gudang Tangerang {runId}`; aset milik spec ini.
  - DU-101-91: Asset: Name `Handphone Realme C55 {runId}`, Group `Gudang Pontianak {runId}`, Status `Assigned`, Pemegang `Dian Pertiwi {runId}`; aset milik spec ini, dipegang Employee Nonaktif.
  - DU-101-92: Asset: Name `Handphone Vivo Y36 {runId}`, Group `Gudang Pontianak {runId}`; aset milik spec ini.
  - DU-101-93: Group: Name `Gudang Surabaya {runId}`; Group milik spec ini, tercakup dalam cakupan Group `Tia Anggraini {runId}`.
  - DU-101-94: Penugasan Role Transaksi: User `Rizal Fauzi {runId}`, Role Transaksi `Approver`, Jenis transaksi `Assign`, Group `Gudang Surabaya {runId}`; penugasan Approver.
  - DU-101-95: Asset: Name `Printer HP LaserJet Pro M404 {runId}`, Group `Gudang Surabaya {runId}`; aset milik spec ini.
- Kondisi:
  - Approval Workflow tersedia pada plan entitas dan Level Feature Suite Assignment bernilai `Full`
  - Setiap Group di atas hanya memuat penugasan Approver dan Group Manager yang tertulis di data; Group tanpa penugasan tidak mewarisi Approver atau Group Manager dari Group lain
  - Semua konfigurasi approval dibuat lewat override pada Group atau aset milik spec ini, sehingga Company default tidak diubah
  - Employee assignee `Ratna Dewi {runId}` memegang aset `Handphone Samsung Galaxy A54 {runId}` berstatus Assigned
  - Transaction timeout (Company default, tidak diubah spec ini) bernilai `7` hari

## Test Steps
### Any one approver: persetujuan pertama menentukan dan approval hanya satu level
1. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Cikarang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
2. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop HP EliteBook 840 {runId}` kepada `Bayu Saputra {runId}`
3. Verifikasi pengajuan berstatus `Waiting for Approval` karena nilai efektif Require approval `ON` dari override Group `Gudang Cikarang {runId}`, dan Approval type `Any one approver` dari override yang sama
4. Verifikasi `Wawan Hidayat {runId}`, Approver pada Group induk `Operasional Jawa Barat {runId}`, termasuk approver transaksi aset di Group `Gudang Cikarang {runId}`
5. Verifikasi permintaan approval untuk `Wawan Hidayat {runId}` tersedia sejak pengajuan, tanpa langkah eskalasi tersendiri
6. Verifikasi `Citra Lestari {runId}`, Approver pada Group `Gudang Cikarang {runId}`, juga termasuk approver transaksi yang sama
7. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Laptop HP EliteBook 840 {runId}`
8. Verifikasi transaksi berstatus `Waiting for Handover` karena satu persetujuan sudah cukup pada Approval type `Any one approver`, yang memakai rule OR
9. Verifikasi `Citra Lestari {runId}` berstatus `Not Involved` karena Approver lain di level itu sudah memutuskan
10. Verifikasi tidak ada level approval lanjutan: transaksi langsung `Waiting for Handover` setelah keputusan pada level yang sama, tanpa approval bertingkat

### Any one approver: Reject oleh satu Approver
11. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Dell Latitude 7440 {runId}` kepada `Bayu Saputra {runId}`
12. `Citra Lestari {runId}` menolak pengajuan Assign aset `Laptop Dell Latitude 7440 {runId}`
13. Verifikasi transaksi langsung `Rejected` setelah satu Approver menolak pada Approval type `Any one approver`
14. Verifikasi `Wawan Hidayat {runId}` berstatus `Not Involved` setelah transaksi `Rejected`

### Any one approver: keputusan hampir bersamaan
15. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Asus Zenbook 14 {runId}` kepada `Bayu Saputra {runId}`
16. `Wawan Hidayat {runId}` menyetujui dan `Citra Lestari {runId}` menolak pengajuan Assign aset `Laptop Asus Zenbook 14 {runId}` hampir bersamaan
17. Verifikasi transaksi mengikuti hanya satu keputusan, yaitu keputusan yang masuk lebih dulu, apa pun urutan tibanya
18. Verifikasi Approver yang keputusannya masuk kemudian berstatus `Not Involved` dan permintaannya ditutup

### All approvers (AND): semua Approver harus menyetujui
19. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Karawang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `All approvers (AND)`
20. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Epson L5290 {runId}` kepada `Bayu Saputra {runId}`
21. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Printer Epson L5290 {runId}`
22. Verifikasi transaksi tetap `Waiting for Approval` menunggu `Sinta Maharani {runId}`, karena Approval type `All approvers (AND)` memakai rule AND
23. `Sinta Maharani {runId}` menyetujui pengajuan Assign aset `Printer Epson L5290 {runId}`
24. Verifikasi transaksi `Waiting for Handover` setelah semua Approver menyetujui
25. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Canon G4010 {runId}` kepada `Bayu Saputra {runId}`
26. `Sinta Maharani {runId}` menolak pengajuan Assign aset `Printer Canon G4010 {runId}`
27. Verifikasi transaksi langsung `Rejected` tanpa menunggu approver lain pada Approval type `All approvers (AND)`
28. Verifikasi `Wawan Hidayat {runId}` berstatus `Not Involved` setelah transaksi `Rejected`

### Tidak ada Approver eligible: rute ke Group Manager, tercatat, dan notifikasi approver_required
29. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Makassar {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
30. `Tia Anggraini {runId}` mengajukan Assign aset `Proyektor Epson EB-X49 {runId}` kepada `Bayu Saputra {runId}`
31. `Gilang Ramadhan {runId}` mencoba menyetujui pengajuan Assign aset `Proyektor Epson EB-X49 {runId}`
32. Verifikasi percobaan itu ditolak karena `Gilang Ramadhan {runId}` hanya Approver untuk jenis transaksi lain, dan transaksi tetap `Waiting for Approval`
33. Verifikasi `Farah Nabila {runId}`, yang berstatus Nonaktif, tidak menerima permintaan approval untuk pengajuan aset `Proyektor Epson EB-X49 {runId}`
34. Verifikasi `Farah Nabila {runId}` tidak termasuk daftar approver transaksi itu karena berstatus Nonaktif sehingga tidak eligible, dan transaksi tetap `Waiting for Approval`
35. Verifikasi tidak ada Approver eligible yang mencakup Group `Gudang Makassar {runId}`, sehingga approver jatuh ke Group Manager yang menaungi, yaitu `Hadi Kurniawan {runId}`
36. Verifikasi kondisi itu tercatat di log transaksi tanpa Note enum, dengan Modified By `System`
37. Verifikasi satu notifikasi `approver_required` dikirim untuk pengajuan aset `Proyektor Epson EB-X49 {runId}`
38. `Tia Anggraini {runId}` mengajukan Assign aset `Proyektor BenQ MW550 {runId}` kepada `Bayu Saputra {runId}`
39. Verifikasi pengajuan aset `Proyektor BenQ MW550 {runId}` mengirim notifikasi `approver_required` sendiri, terpisah dari notifikasi pengajuan aset `Proyektor Epson EB-X49 {runId}`
40. `Hadi Kurniawan {runId}` menyetujui pengajuan Assign aset `Proyektor Epson EB-X49 {runId}`
41. Verifikasi transaksi `Waiting for Handover` karena Group Manager yang menaungi Group aset menjadi approver bila tidak ada Approver eligible

### Tidak ada Group Manager aktif: rute jatuh ke Total Control
42. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Semarang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
43. `Tia Anggraini {runId}` mengajukan Assign aset `Monitor LG 24MK600 {runId}` kepada `Bayu Saputra {runId}`
44. Verifikasi `Budi Santoso {runId}` dan `Susanti Wijaya {runId}`, termasuk user Total Control, dapat memutuskan pengajuan itu karena tidak ada Approver eligible dan tidak ada Group Manager aktif, sehingga himpunan approver fallback adalah user Total Control dan memuat keduanya
45. `Budi Santoso {runId}` menyetujui pengajuan Assign aset `Monitor LG 24MK600 {runId}`
46. Verifikasi transaksi `Waiting for Handover` karena pada himpunan fallback Approval type `Any one approver` cukup satu persetujuan

### Fallback Group Manager dengan All approvers (AND) dan Any one approver
47. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Jakarta Timur {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `All approvers (AND)`
48. Admin `Budi Santoso {runId}` membuat override pada aset `Scanner Brother ADS-2200 {runId}` untuk transaksi Assign dengan Approval type `Any one approver`
49. `Tia Anggraini {runId}` mengajukan Assign aset `Scanner Fujitsu ScanSnap iX1600 {runId}` kepada `Bayu Saputra {runId}`
50. Verifikasi approver fallback adalah semua Group Manager yang menaungi Group aset, yaitu `Hadi Kurniawan {runId}` di Group `Gudang Jakarta Timur {runId}` dan `Indra Wijaya {runId}` di Group induk `Kantor Pusat Jakarta {runId}`
51. `Hadi Kurniawan {runId}` menyetujui pengajuan Assign aset `Scanner Fujitsu ScanSnap iX1600 {runId}`
52. Verifikasi transaksi tetap `Waiting for Approval` menunggu `Indra Wijaya {runId}` pada himpunan fallback dengan All approvers (AND)
53. `Indra Wijaya {runId}` menyetujui pengajuan Assign aset `Scanner Fujitsu ScanSnap iX1600 {runId}`
54. Verifikasi transaksi `Waiting for Handover` setelah semua Group Manager pada himpunan fallback menyetujui
55. `Tia Anggraini {runId}` mengajukan Assign aset `Scanner Brother ADS-2200 {runId}` kepada `Bayu Saputra {runId}`
56. `Indra Wijaya {runId}` menyetujui pengajuan Assign aset `Scanner Brother ADS-2200 {runId}`
57. Verifikasi transaksi `Waiting for Handover` karena pada himpunan fallback dengan Any one approver salah satu cukup, dan `Hadi Kurniawan {runId}` berstatus `Not Involved`

### Group Manager tanpa penugasan tidak dihitung pada AND dan keputusannya override final
58. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Denpasar {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `All approvers (AND)`
59. `Tia Anggraini {runId}` mengajukan Assign aset `Tablet Samsung Galaxy Tab S8 {runId}` kepada `Bayu Saputra {runId}`
60. `Eko Prasetyo {runId}` menyetujui pengajuan Assign aset `Tablet Samsung Galaxy Tab S8 {runId}`
61. `Fitri Anggraini {runId}` menyetujui pengajuan Assign aset `Tablet Samsung Galaxy Tab S8 {runId}`
62. Verifikasi transaksi `Waiting for Handover` setelah `Eko Prasetyo {runId}` dan `Fitri Anggraini {runId}` menyetujui, tanpa menunggu Group Manager `Hadi Kurniawan {runId}` yang tidak punya penugasan Approver
63. `Tia Anggraini {runId}` mengajukan Assign aset `Tablet Apple iPad 10 {runId}` kepada `Bayu Saputra {runId}`
64. `Hadi Kurniawan {runId}` menyetujui pengajuan Assign aset `Tablet Apple iPad 10 {runId}`
65. Verifikasi transaksi langsung `Waiting for Handover` oleh keputusan Group Manager sebagai override final, walau Approver terdaftar belum bertindak
66. Verifikasi `Eko Prasetyo {runId}` dan `Fitri Anggraini {runId}` berstatus `Not Involved` setelah keputusan override

### Kondisi A: pengaju Group Manager atau Total Control melewati approval
67. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Bandung {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
68. `Hadi Kurniawan {runId}` mengajukan Assign aset `Kamera Canon EOS M50 {runId}` kepada `Putri Handayani {runId}`
69. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Group Manager yang menaungi Group aset
70. Verifikasi log transaksi memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] adalah `Hadi Kurniawan {runId}`
71. Verifikasi Modified By log itu adalah `Hadi Kurniawan {runId}`, bukan `System`
72. Verifikasi `Hadi Kurniawan {runId}` tidak tercatat sebagai approver transaksinya sendiri
73. Verifikasi Kondisi A dievaluasi lebih dulu daripada rute tidak ada Approver: transaksi di Group `Gudang Bandung {runId}` yang tidak punya Approver langsung `Waiting for Handover` atas nama pengaju
74. `Budi Santoso {runId}` mengajukan Assign aset `Kamera Sony ZV-E10 {runId}` kepada `Putri Handayani {runId}`
75. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Total Control
76. Verifikasi log transaksi memuat `Approved by [Nama] (Total Control — requester)` dengan [Nama] adalah `Budi Santoso {runId}`

### Kondisi A tidak berlaku bila Require approval efektif OFF
77. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Palembang {runId}` untuk transaksi Assign dengan Require approval `OFF`
78. `Budi Santoso {runId}` mengajukan Assign aset `Router Mikrotik hAP ax2 {runId}` kepada `Putri Handayani {runId}`
79. Verifikasi transaksi berstatus `Waiting for Handover` dan log transaksi tidak memuat `Approved by [Nama] (Total Control — requester)` dengan [Nama] adalah `Budi Santoso {runId}`, karena Kondisi A tidak berlaku bila Require approval efektif `OFF`

### Self-approval guard: pengaju dikecualikan dari daftar approver
80. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Medan {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
81. `Tia Anggraini {runId}` mengajukan Assign aset `Switch Cisco CBS250 {runId}` kepada `Bayu Saputra {runId}`
82. Verifikasi `Tia Anggraini {runId}`, yang juga Approver di Group `Gudang Medan {runId}`, dikecualikan dari daftar approver transaksinya sendiri, sedangkan `Rizal Fauzi {runId}` tetap menjadi approver
83. `Tia Anggraini {runId}` mencoba menyetujui pengajuan Assign aset `Switch Cisco CBS250 {runId}` miliknya sendiri
84. Verifikasi percobaan itu ditolak dan transaksi tetap `Waiting for Approval`, karena pengaju tidak pernah menjadi approver transaksinya sendiri
85. `Rizal Fauzi {runId}` menyetujui pengajuan Assign aset `Switch Cisco CBS250 {runId}`
86. Verifikasi transaksi `Waiting for Handover` karena approval tetap berjalan dengan Approver yang bukan pengaju, sesuai rule approval-foundation untuk requester yang juga approver
87. Verifikasi `Tia Anggraini {runId}` berstatus `Not Involved` pada transaksinya sendiri

### Pengaju satu-satunya Approver eligible: approval dilewati
88. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Padang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
89. `Tia Anggraini {runId}` mengajukan Assign aset `Access Point Ubiquiti U6 {runId}` kepada `Bayu Saputra {runId}`
90. Verifikasi langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena semua Approver eligible adalah pengaju
91. Verifikasi log transaksi memuat `Approved by system (no independent approver)`
92. Verifikasi log itu tercatat dengan Modified By `System`
93. Verifikasi `Tia Anggraini {runId}` tidak menjadi approver transaksinya sendiri
94. Verifikasi self-approval guard dievaluasi sebelum rute tidak ada Approver: transaksi `Waiting for Handover` oleh sistem, bukan menunggu approver fallback

### Urutan evaluasi: Deny dan Limits ditolak sebelum approval
95. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Pontianak {runId}` untuk transaksi Assign dengan Require approval `ON` dan Max assets per assignee (concurrent) `1`
96. Admin `Budi Santoso {runId}` membuat override pada aset `Handphone Xiaomi Redmi Note 12 {runId}` untuk transaksi Assign dengan Allow Assign `Deny`
97. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Xiaomi Redmi Note 12 {runId}` kepada `Surya Atmaja {runId}`
98. Verifikasi pengajuan aset `Handphone Xiaomi Redmi Note 12 {runId}` ditolak oleh Deny pada override sebelum approval, dan tidak ada permintaan approval yang terbentuk
99. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Oppo A78 {runId}` kepada `Ratna Dewi {runId}`
100. Verifikasi pengajuan aset `Handphone Oppo A78 {runId}` ditolak karena batas Max assets per assignee (concurrent) `1` terlampaui oleh `Ratna Dewi {runId}`, sebelum approval, dan tidak ada permintaan approval yang terbentuk

### Notifikasi approver_required saat Save konfigurasi Approval
101. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Manado {runId}` untuk transaksi Assign dengan Require approval `ON`, sedangkan Group itu tidak punya Approver dan tidak punya Group Manager
102. Verifikasi tidak ada notifikasi `approver_required` yang dikirim saat konfigurasi Approval itu disimpan, karena kondisi tidak ada Role Transaksi `Approver` untuk transaksi Assign di Group mana pun tidak timbul: Role Transaksi `Approver` Assign masih ditugaskan di Group lain
103. Admin `Budi Santoso {runId}` membuat override pada aset `Server Dell PowerEdge T150 {runId}` untuk transaksi Assign dengan Need recipient confirmation `No`
104. Verifikasi tidak ada notifikasi `approver_required` baru karena konfigurasi Approval tidak diubah

### Approval berlaku selama Approval Workflow tersedia di plan
105. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Acer Swift 3 {runId}` kepada `Bayu Saputra {runId}`
106. Verifikasi pengajuan aset `Laptop Acer Swift 3 {runId}` berstatus `Waiting for Approval` dan langkah approval tidak dilewati, karena Approval Workflow tersedia di plan entitas dan nilai efektif Require approval `ON` dari override Group `Gudang Cikarang {runId}`
107. Verifikasi permintaan approval terbentuk untuk `Wawan Hidayat {runId}` dan `Citra Lestari {runId}`, karena penugasan Role Transaksi `Approver` dipakai selama Approval Workflow tersedia di plan

### Urutan evaluasi: aturan tetap dan Eligibility ditolak sebelum approval
108. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop HP EliteBook 840 {runId}`, yang masih punya transaksi Assign aktif, kepada `Bayu Saputra {runId}`
109. Verifikasi pengajuan ditolak oleh aturan tetap satu transaksi aktif per aset, sebelum approval, dan tidak ada permintaan approval yang terbentuk
110. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Lenovo Yoga Slim 7 {runId}` kepada `Dian Pertiwi {runId}`
111. Verifikasi pengajuan ditolak oleh Eligibility karena assignee Employee `Dian Pertiwi {runId}` berstatus Nonaktif, sebelum approval, dan tidak ada permintaan approval yang terbentuk

### Approver berakses Read Only dan tanpa lisensi addon tidak eligible
112. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Malang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
113. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Epson L3210 {runId}` kepada `Bayu Saputra {runId}`
114. Verifikasi `Lukman Hakim {runId}`, Approver pada Group `Gudang Malang {runId}` yang berakses Read Only, tidak termasuk approver transaksi itu dan tidak menerima permintaan approval
115. Verifikasi `Nanda Pratiwi {runId}`, Approver pada Group `Gudang Malang {runId}` yang tanpa lisensi addon, tidak termasuk approver transaksi itu dan tidak menerima permintaan approval
116. Verifikasi tidak ada Approver eligible yang mencakup Group `Gudang Malang {runId}`, sehingga approver jatuh ke user Total Control karena tidak ada Group Manager yang menaungi

### Pengaju Group Manager di Group induk melewati approval
117. `Indra Wijaya {runId}` mengajukan Assign aset `Scanner Canon DR-C225 {runId}` kepada `Putri Handayani {runId}`
118. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Group Manager di Group induk `Kantor Pusat Jakarta {runId}` yang menaungi Group aset `Gudang Jakarta Timur {runId}` lewat ancestor-nya, walau Group aset ber-Require approval `ON` dengan Approval type `All approvers (AND)`
119. Verifikasi log transaksi memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] adalah `Indra Wijaya {runId}`

### Kondisi A dievaluasi sebelum self-approval guard
120. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Tangerang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
121. `Yusuf Hakim {runId}` mengajukan Assign aset `Printer Brother HL-L5100 {runId}` kepada `Putri Handayani {runId}`
122. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Group Manager yang menaungi Group aset, walau pengaju juga satu-satunya Approver eligible Group `Gudang Tangerang {runId}`
123. Verifikasi log transaksi memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] adalah `Yusuf Hakim {runId}`, dan bukan `Approved by system (no independent approver)`

### Urutan evaluasi: aturan tetap dan Deny pada override mendahului Eligibility dan Limits
124. Admin `Budi Santoso {runId}` membuat override pada aset `Laptop HP EliteBook 840 {runId}` untuk transaksi Assign dengan Allow Assign `Deny`
125. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop HP EliteBook 840 {runId}`, yang masih punya transaksi Assign aktif dan kini ber-Deny pada override, kepada `Bayu Saputra {runId}`
126. Verifikasi pengajuan ditolak oleh aturan tetap satu transaksi aktif per aset, bukan oleh Deny pada override, karena aturan tetap dievaluasi lebih dulu daripada Deny pada override
127. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Xiaomi Redmi Note 12 {runId}`, yang ber-Deny pada override, kepada `Ratna Dewi {runId}`, yang sudah memegang aset sebesar batas Max assets per assignee (concurrent) `1`
128. Verifikasi pengajuan ditolak oleh Deny pada override, bukan oleh batas Max assets per assignee (concurrent) `1`, karena Deny pada override dievaluasi lebih dulu daripada Limits
129. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Xiaomi Redmi Note 12 {runId}` kepada `Dian Pertiwi {runId}`, yang berstatus Nonaktif
130. Verifikasi pengajuan ditolak oleh Deny pada override, bukan oleh Eligibility karena assignee `Dian Pertiwi {runId}` berstatus Nonaktif, karena Deny pada override dievaluasi lebih dulu daripada Eligibility

### Urutan evaluasi: Eligibility ditolak sebelum Limits
131. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Vivo Y36 {runId}` kepada `Dian Pertiwi {runId}`, yang berstatus Nonaktif dan sudah memegang aset `Handphone Realme C55 {runId}` sebesar batas Max assets per assignee (concurrent) `1`
132. Verifikasi pengajuan ditolak oleh Eligibility karena assignee Employee `Dian Pertiwi {runId}` berstatus Nonaktif, bukan oleh batas Max assets per assignee (concurrent) `1`, karena Eligibility dievaluasi lebih dulu daripada Limits

### Penugasan Approver tidak dipakai selama Require approval OFF
133. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Surabaya {runId}` untuk transaksi Assign dengan Require approval `OFF`
134. `Tia Anggraini {runId}` mengajukan Assign aset `Printer HP LaserJet Pro M404 {runId}` kepada `Bayu Saputra {runId}`
135. Verifikasi pengajuan berstatus `Waiting for Handover` karena nilai efektif Require approval `OFF` dari override Group `Gudang Surabaya {runId}`, dan tidak ada permintaan approval untuk `Rizal Fauzi {runId}`, Approver yang ditugaskan pada Group itu, karena penugasan Role Transaksi `Approver` tidak dipakai selama Require approval `OFF`
