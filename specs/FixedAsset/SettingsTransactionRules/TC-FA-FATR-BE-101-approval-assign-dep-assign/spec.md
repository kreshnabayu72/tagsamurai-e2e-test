---
id: TC-FA-FATR-BE-101-approval-assign-dep-assign
title: "Approval dan penentuan approver pada transaksi Assign"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["§Aturan Logika Modul#r74", "§Aturan Logika Modul#r81", "§4.1#r193", "§4.1#r194", "§4.1#r195", "§4.1#r196", "§9.2#b379", "§9.2#b380", "§9.2#b381", "§9.2#b382", "§9.2#b441", "§9.2#b443", "§9.2#b444", "§9.2#b445", "§9.2#b446", "§9.2#b448", "§9.2#b449", "§9.2#b450", "§9.2#b451", "§9.2#b453", "§9.2#b455", "§9.2#b456", "§9.2#b457", "§9.2#b458", "§9.2#b460", "§9.2#b461", "§9.2#b464", "§9.2#b465", "§9.2#b466", "§9.2#b468", "§9.2#b469", "§9.2#b470", "§9.2#b471", "§9.2#b472", "§9.2#b475", "§9.2#b476", "§9.2#b477", "§9.2#b488", "§9.2#b489", "§9.2#b490", "§9.2#b491", "§9.2#b492", "§9.2#b493", "§9.2#b494", "§9.2#b463", "§9.2#b479", "§9.2#b480", "§9.2#b483", "§9.2#b481", "§9.2#b482", "§9.2#b534", "§9.2#b535", "§9.2#b537", "§9.2#b538", "§9.2#b540", "§9.2#b541", "§9.2#b549", "§9.2#b550", "§9.2#b551", "§9.2#b552", "§9.2#b553", "§9.2#b555", "§9.4.1#r20", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r42", "§9.4.2#r130", "§9.4.2#r131", "§9.4.2#r148", "§9.4.2#r149", "§9.4.2#r150", "§9.4.2#r152", "§9.4.3#b4", "§9.4.4#r11", "§9.4.4#r48", "§9.4.4#r49", "§9.4.4#r50", "§9.4.4#r53", "§9.8#r12", "§9.8#r13", "§9.8#r14", "§9.10.1#r11", "§10#b1"]
smoke: []
dependsOn:
  - "Assign: pengajuan, handover, Reassign, dan Unassign"
owner: BE
trace:
  "§Aturan Logika Modul#r74": 108
  "§Aturan Logika Modul#r81": 109
  "§4.1#r193": 6
  "§4.1#r194": [9, 14]
  "§4.1#r195": [23, 25]
  "§4.1#r196": [10, 28]
  "§9.2#b379": [99, 101, 112, 114]
  "§9.2#b380": 3
  "§9.2#b381": [4, 33]
  "§9.2#b382": 108
  "§9.2#b441": 11
  "§9.2#b443": [9, 87]
  "§9.2#b444": 25
  "§9.2#b445": 7
  "§9.2#b446": 3
  "§9.2#b448": [4, 6, 33]
  "§9.2#b449": 4
  "§9.2#b450": 5
  "§9.2#b451": [34, 35, 117, 118, 119]
  "§9.2#b453": 42
  "§9.2#b455": [9, 23]
  "§9.2#b456": [9, 14]
  "§9.2#b457": [23, 25]
  "§9.2#b458": [10, 15, 28, 29]
  "§9.2#b460": 70
  "§9.2#b461": [70, 76, 121]
  "§9.2#b464": [74, 95, 125, 126]
  "§9.2#b465": 80
  "§9.2#b466": 73
  "§9.2#b468": 85
  "§9.2#b469": [83, 88]
  "§9.2#b470": 91
  "§9.2#b471": 92
  "§9.2#b472": [83, 87]
  "§9.2#b475": [36, 45]
  "§9.2#b476": 37
  "§9.2#b477": 38
  "§9.2#b488": [36, 51]
  "§9.2#b489": 45
  "§9.2#b490": [47, 51]
  "§9.2#b491": [47, 58]
  "§9.2#b492": [53, 55]
  "§9.2#b493": 63
  "§9.2#b494": [66, 67]
  "§9.2#b463": [71, 77]
  "§9.2#b479": [38, 103]
  "§9.2#b480": 103
  "§9.2#b483": 105
  "§9.2#b481": 38
  "§9.2#b482": 40
  "§9.2#b534": 9
  "§9.2#b535": 10
  "§9.2#b537": 91
  "§9.2#b538": 91
  "§9.2#b540": [36, 45]
  "§9.2#b541": 38
  "§9.2#b549": [70, 76]
  "§9.2#b550": [70, 76, 121, 125]
  "§9.2#b551": [71, 122, 126]
  "§9.2#b552": 77
  "§9.2#b553": 72
  "§9.2#b555": 80
  "§9.4.1#r20": 83
  "§9.4.2#r37": 108
  "§9.4.2#r40": [92, 94]
  "§9.4.2#r42": [18, 19]
  "§9.4.2#r130": [36, 45]
  "§9.4.2#r131": 37
  "§9.4.2#r148": [70, 76]
  "§9.4.2#r149": [71, 77]
  "§9.4.2#r150": 72
  "§9.4.2#r152": 80
  "§9.4.3#b4": [85, 94]
  "§9.4.4#r11": 37
  "§9.4.4#r48": [18, 19]
  "§9.4.4#r49": 91
  "§9.4.4#r50": 36
  "§9.4.4#r53": [70, 76]
  "§9.8#r12": [92, 93]
  "§9.8#r13": [71, 77]
  "§9.8#r14": 37
  "§9.10.1#r11": 108
  "§10#b1": 11
---

# Approval dan penentuan approver pada transaksi Assign

## Prerequisites
- Aktor: Admin `Budi Santoso {runId}` (Total Control entitas; membuat override dan, pada blok Kondisi A, mengajukan transaksi sebagai Total Control); `Tia Anggraini {runId}` (pengaju Assign, bukan Group Manager dan bukan Total Control); Approver, Group Manager, dan Total Control sesuai data di bawah; Operator platform (hanya mengubah Approval Workflow pada plan entitas).
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
  - DU-101-69: Plan entitas: Approval Workflow `Tersedia`; keadaan plan entitas suite.
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
7. Verifikasi transaksi yang menunggu approval itu memiliki batas waktu menunggu `7` hari sejak masuk status `Waiting for Approval`, dari Transaction timeout per transaksi Assign
8. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Laptop HP EliteBook 840 {runId}`
9. Verifikasi transaksi berstatus `Waiting for Handover` karena satu persetujuan sudah cukup pada Approval type `Any one approver`, yang memakai rule OR
10. Verifikasi `Citra Lestari {runId}` berstatus `Not Involved` karena Approver lain di level itu sudah memutuskan
11. Verifikasi tidak ada level approval lanjutan: transaksi langsung `Waiting for Handover` setelah keputusan pada level yang sama, tanpa approval bertingkat

### Any one approver: Reject oleh satu Approver
12. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Dell Latitude 7440 {runId}` kepada `Bayu Saputra {runId}`
13. `Citra Lestari {runId}` menolak pengajuan Assign aset `Laptop Dell Latitude 7440 {runId}`
14. Verifikasi transaksi langsung `Rejected` setelah satu Approver menolak pada Approval type `Any one approver`
15. Verifikasi `Wawan Hidayat {runId}` berstatus `Not Involved` setelah transaksi `Rejected`

### Any one approver: keputusan hampir bersamaan
16. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Asus Zenbook 14 {runId}` kepada `Bayu Saputra {runId}`
17. `Wawan Hidayat {runId}` menyetujui dan `Citra Lestari {runId}` menolak pengajuan Assign aset `Laptop Asus Zenbook 14 {runId}` hampir bersamaan
18. Verifikasi transaksi mengikuti hanya satu keputusan, yaitu keputusan yang masuk lebih dulu, apa pun urutan tibanya
19. Verifikasi Approver yang keputusannya masuk kemudian berstatus `Not Involved` dan permintaannya ditutup

### All approvers (AND): semua Approver harus menyetujui
20. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Karawang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `All approvers (AND)`
21. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Epson L5290 {runId}` kepada `Bayu Saputra {runId}`
22. `Wawan Hidayat {runId}` menyetujui pengajuan Assign aset `Printer Epson L5290 {runId}`
23. Verifikasi transaksi tetap `Waiting for Approval` menunggu `Sinta Maharani {runId}`, karena Approval type `All approvers (AND)` memakai rule AND
24. `Sinta Maharani {runId}` menyetujui pengajuan Assign aset `Printer Epson L5290 {runId}`
25. Verifikasi transaksi `Waiting for Handover` setelah semua Approver menyetujui
26. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Canon G4010 {runId}` kepada `Bayu Saputra {runId}`
27. `Sinta Maharani {runId}` menolak pengajuan Assign aset `Printer Canon G4010 {runId}`
28. Verifikasi transaksi langsung `Rejected` tanpa menunggu approver lain pada Approval type `All approvers (AND)`
29. Verifikasi `Wawan Hidayat {runId}` berstatus `Not Involved` setelah transaksi `Rejected`

### Tidak ada Approver eligible: rute ke Group Manager, tercatat, dan notifikasi approver_required
30. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Makassar {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
31. `Tia Anggraini {runId}` mengajukan Assign aset `Proyektor Epson EB-X49 {runId}` kepada `Bayu Saputra {runId}`
32. `Gilang Ramadhan {runId}` mencoba menyetujui pengajuan Assign aset `Proyektor Epson EB-X49 {runId}`
33. Verifikasi percobaan itu ditolak karena `Gilang Ramadhan {runId}` hanya Approver untuk jenis transaksi lain, dan transaksi tetap `Waiting for Approval`
34. Verifikasi `Farah Nabila {runId}`, yang berstatus Nonaktif, tidak menerima permintaan approval untuk pengajuan aset `Proyektor Epson EB-X49 {runId}`
35. Verifikasi `Farah Nabila {runId}` tidak termasuk daftar approver transaksi itu karena berstatus Nonaktif sehingga tidak eligible, dan transaksi tetap `Waiting for Approval`
36. Verifikasi tidak ada Approver eligible yang mencakup Group `Gudang Makassar {runId}`, sehingga approver jatuh ke Group Manager yang menaungi, yaitu `Hadi Kurniawan {runId}`
37. Verifikasi kondisi itu tercatat di log transaksi tanpa Note enum, dengan Modified By `System`
38. Verifikasi satu notifikasi `approver_required` dikirim untuk pengajuan aset `Proyektor Epson EB-X49 {runId}`
39. `Tia Anggraini {runId}` mengajukan Assign aset `Proyektor BenQ MW550 {runId}` kepada `Bayu Saputra {runId}`
40. Verifikasi pengajuan aset `Proyektor BenQ MW550 {runId}` mengirim notifikasi `approver_required` sendiri, terpisah dari notifikasi pengajuan aset `Proyektor Epson EB-X49 {runId}`
41. `Hadi Kurniawan {runId}` menyetujui pengajuan Assign aset `Proyektor Epson EB-X49 {runId}`
42. Verifikasi transaksi `Waiting for Handover` karena Group Manager yang menaungi Group aset menjadi approver bila tidak ada Approver eligible

### Tidak ada Group Manager aktif: rute jatuh ke Total Control
43. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Semarang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
44. `Tia Anggraini {runId}` mengajukan Assign aset `Monitor LG 24MK600 {runId}` kepada `Bayu Saputra {runId}`
45. Verifikasi `Budi Santoso {runId}` dan `Susanti Wijaya {runId}`, semua user Total Control, dapat memutuskan pengajuan itu karena tidak ada Approver eligible dan tidak ada Group Manager aktif, sehingga approver fallback adalah semua user Total Control
46. `Budi Santoso {runId}` menyetujui pengajuan Assign aset `Monitor LG 24MK600 {runId}`
47. Verifikasi transaksi `Waiting for Handover` karena pada himpunan fallback Approval type `Any one approver` cukup satu persetujuan

### Fallback Group Manager dengan All approvers (AND) dan Any one approver
48. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Jakarta Timur {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `All approvers (AND)`
49. Admin `Budi Santoso {runId}` membuat override pada aset `Scanner Brother ADS-2200 {runId}` untuk transaksi Assign dengan Approval type `Any one approver`
50. `Tia Anggraini {runId}` mengajukan Assign aset `Scanner Fujitsu ScanSnap iX1600 {runId}` kepada `Bayu Saputra {runId}`
51. Verifikasi approver fallback adalah semua Group Manager yang menaungi Group aset, yaitu `Hadi Kurniawan {runId}` di Group `Gudang Jakarta Timur {runId}` dan `Indra Wijaya {runId}` di Group induk `Kantor Pusat Jakarta {runId}`
52. `Hadi Kurniawan {runId}` menyetujui pengajuan Assign aset `Scanner Fujitsu ScanSnap iX1600 {runId}`
53. Verifikasi transaksi tetap `Waiting for Approval` menunggu `Indra Wijaya {runId}` pada himpunan fallback dengan All approvers (AND)
54. `Indra Wijaya {runId}` menyetujui pengajuan Assign aset `Scanner Fujitsu ScanSnap iX1600 {runId}`
55. Verifikasi transaksi `Waiting for Handover` setelah semua Group Manager pada himpunan fallback menyetujui
56. `Tia Anggraini {runId}` mengajukan Assign aset `Scanner Brother ADS-2200 {runId}` kepada `Bayu Saputra {runId}`
57. `Indra Wijaya {runId}` menyetujui pengajuan Assign aset `Scanner Brother ADS-2200 {runId}`
58. Verifikasi transaksi `Waiting for Handover` karena pada himpunan fallback dengan Any one approver salah satu cukup, dan `Hadi Kurniawan {runId}` berstatus `Not Involved`

### Group Manager tanpa penugasan tidak dihitung pada AND dan keputusannya override final
59. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Denpasar {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `All approvers (AND)`
60. `Tia Anggraini {runId}` mengajukan Assign aset `Tablet Samsung Galaxy Tab S8 {runId}` kepada `Bayu Saputra {runId}`
61. `Eko Prasetyo {runId}` menyetujui pengajuan Assign aset `Tablet Samsung Galaxy Tab S8 {runId}`
62. `Fitri Anggraini {runId}` menyetujui pengajuan Assign aset `Tablet Samsung Galaxy Tab S8 {runId}`
63. Verifikasi transaksi `Waiting for Handover` setelah `Eko Prasetyo {runId}` dan `Fitri Anggraini {runId}` menyetujui, tanpa menunggu Group Manager `Hadi Kurniawan {runId}` yang tidak punya penugasan Approver
64. `Tia Anggraini {runId}` mengajukan Assign aset `Tablet Apple iPad 10 {runId}` kepada `Bayu Saputra {runId}`
65. `Hadi Kurniawan {runId}` menyetujui pengajuan Assign aset `Tablet Apple iPad 10 {runId}`
66. Verifikasi transaksi langsung `Waiting for Handover` oleh keputusan Group Manager sebagai override final, walau Approver terdaftar belum bertindak
67. Verifikasi `Eko Prasetyo {runId}` dan `Fitri Anggraini {runId}` berstatus `Not Involved` setelah keputusan override

### Kondisi A: pengaju Group Manager atau Total Control melewati approval
68. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Bandung {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
69. `Hadi Kurniawan {runId}` mengajukan Assign aset `Kamera Canon EOS M50 {runId}` kepada `Putri Handayani {runId}`
70. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Group Manager yang menaungi Group aset
71. Verifikasi log transaksi memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] adalah `Hadi Kurniawan {runId}`
72. Verifikasi Modified By log itu adalah `Hadi Kurniawan {runId}`, bukan `System`
73. Verifikasi `Hadi Kurniawan {runId}` tidak tercatat sebagai approver transaksinya sendiri
74. Verifikasi Kondisi A dievaluasi lebih dulu daripada rute tidak ada Approver: transaksi di Group `Gudang Bandung {runId}` yang tidak punya Approver langsung `Waiting for Handover` atas nama pengaju
75. `Budi Santoso {runId}` mengajukan Assign aset `Kamera Sony ZV-E10 {runId}` kepada `Putri Handayani {runId}`
76. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Total Control
77. Verifikasi log transaksi memuat `Approved by [Nama] (Total Control — requester)` dengan [Nama] adalah `Budi Santoso {runId}`

### Kondisi A tidak berlaku bila Require approval efektif OFF
78. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Palembang {runId}` untuk transaksi Assign dengan Require approval `OFF`
79. `Budi Santoso {runId}` mengajukan Assign aset `Router Mikrotik hAP ax2 {runId}` kepada `Putri Handayani {runId}`
80. Verifikasi transaksi berstatus `Waiting for Handover` dan log transaksi tidak memuat `Approved by [Nama] (Total Control — requester)` dengan [Nama] adalah `Budi Santoso {runId}`, karena Kondisi A tidak berlaku bila Require approval efektif `OFF`

### Self-approval guard: pengaju dikecualikan dari daftar approver
81. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Medan {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
82. `Tia Anggraini {runId}` mengajukan Assign aset `Switch Cisco CBS250 {runId}` kepada `Bayu Saputra {runId}`
83. Verifikasi `Tia Anggraini {runId}`, yang juga Approver di Group `Gudang Medan {runId}`, dikecualikan dari daftar approver transaksinya sendiri, sedangkan `Rizal Fauzi {runId}` tetap menjadi approver
84. `Tia Anggraini {runId}` mencoba menyetujui pengajuan Assign aset `Switch Cisco CBS250 {runId}` miliknya sendiri
85. Verifikasi percobaan itu ditolak dan transaksi tetap `Waiting for Approval`, karena pengaju tidak pernah menjadi approver transaksinya sendiri
86. `Rizal Fauzi {runId}` menyetujui pengajuan Assign aset `Switch Cisco CBS250 {runId}`
87. Verifikasi transaksi `Waiting for Handover` karena approval tetap berjalan dengan Approver yang bukan pengaju, sesuai rule approval-foundation untuk requester yang juga approver
88. Verifikasi `Tia Anggraini {runId}` berstatus `Not Involved` pada transaksinya sendiri

### Pengaju satu-satunya Approver eligible: approval dilewati
89. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Padang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
90. `Tia Anggraini {runId}` mengajukan Assign aset `Access Point Ubiquiti U6 {runId}` kepada `Bayu Saputra {runId}`
91. Verifikasi langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena semua Approver eligible adalah pengaju
92. Verifikasi log transaksi memuat `Approved by system (no independent approver)`
93. Verifikasi log itu tercatat dengan Modified By `System`
94. Verifikasi `Tia Anggraini {runId}` tidak menjadi approver transaksinya sendiri
95. Verifikasi self-approval guard dievaluasi sebelum rute tidak ada Approver: transaksi `Waiting for Handover` oleh sistem, bukan menunggu approver fallback

### Urutan evaluasi: Deny dan Limits ditolak sebelum approval
96. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Pontianak {runId}` untuk transaksi Assign dengan Require approval `ON` dan Max assets per assignee (concurrent) `1`
97. Admin `Budi Santoso {runId}` membuat override pada aset `Handphone Xiaomi Redmi Note 12 {runId}` untuk transaksi Assign dengan Allow Assign `Deny`
98. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Xiaomi Redmi Note 12 {runId}` kepada `Surya Atmaja {runId}`
99. Verifikasi pengajuan aset `Handphone Xiaomi Redmi Note 12 {runId}` ditolak oleh Deny pada override sebelum approval, dan tidak ada permintaan approval yang terbentuk
100. `Tia Anggraini {runId}` mengajukan Assign aset `Handphone Oppo A78 {runId}` kepada `Ratna Dewi {runId}`
101. Verifikasi pengajuan aset `Handphone Oppo A78 {runId}` ditolak karena batas Max assets per assignee (concurrent) `1` terlampaui oleh `Ratna Dewi {runId}`, sebelum approval, dan tidak ada permintaan approval yang terbentuk

### Notifikasi approver_required saat Save konfigurasi Approval
102. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Manado {runId}` untuk transaksi Assign dengan Require approval `ON`, sedangkan Group itu tidak punya Approver dan tidak punya Group Manager
103. Verifikasi tidak ada notifikasi `approver_required` yang dikirim saat konfigurasi Approval itu disimpan, karena kondisi tidak ada Role Transaksi `Approver` untuk transaksi Assign di Group mana pun tidak timbul: Role Transaksi `Approver` Assign masih ditugaskan di Group lain
104. Admin `Budi Santoso {runId}` membuat override pada aset `Server Dell PowerEdge T150 {runId}` untuk transaksi Assign dengan Recipient acceptance `Optional`
105. Verifikasi tidak ada notifikasi `approver_required` baru karena konfigurasi Approval tidak diubah

### Approval dilewati saat Approval Workflow tidak tersedia di plan
106. Operator platform mengubah Approval Workflow pada plan entitas menjadi tidak tersedia
107. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Acer Swift 3 {runId}` kepada `Bayu Saputra {runId}`
108. Verifikasi pengajuan tidak berstatus `Waiting for Approval` melainkan langsung `Waiting for Handover`, karena nilai efektif Require approval `OFF` saat Approval Workflow tidak tersedia
109. Verifikasi tidak ada permintaan approval untuk `Wawan Hidayat {runId}` dan `Citra Lestari {runId}` walau mereka Approver pada Group `Gudang Cikarang {runId}`, karena penugasan Role Transaksi `Approver` tidak dipakai selama Approval Workflow tidak tersedia
110. Operator platform mengubah Approval Workflow pada plan entitas menjadi tersedia

### Urutan evaluasi: aturan tetap dan Eligibility ditolak sebelum approval
111. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop HP EliteBook 840 {runId}`, yang masih punya transaksi Assign aktif, kepada `Bayu Saputra {runId}`
112. Verifikasi pengajuan ditolak oleh aturan tetap satu transaksi aktif per aset, sebelum approval, dan tidak ada permintaan approval yang terbentuk
113. `Tia Anggraini {runId}` mengajukan Assign aset `Laptop Lenovo Yoga Slim 7 {runId}` kepada `Dian Pertiwi {runId}`
114. Verifikasi pengajuan ditolak oleh Eligibility karena assignee Employee `Dian Pertiwi {runId}` berstatus Nonaktif, sebelum approval, dan tidak ada permintaan approval yang terbentuk

### Approver berakses Read Only dan tanpa lisensi addon tidak eligible
115. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Malang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
116. `Tia Anggraini {runId}` mengajukan Assign aset `Printer Epson L3210 {runId}` kepada `Bayu Saputra {runId}`
117. Verifikasi `Lukman Hakim {runId}`, Approver pada Group `Gudang Malang {runId}` yang berakses Read Only, tidak termasuk approver transaksi itu dan tidak menerima permintaan approval
118. Verifikasi `Nanda Pratiwi {runId}`, Approver pada Group `Gudang Malang {runId}` yang tanpa lisensi addon, tidak termasuk approver transaksi itu dan tidak menerima permintaan approval
119. Verifikasi tidak ada Approver eligible yang mencakup Group `Gudang Malang {runId}`, sehingga approver jatuh ke user Total Control karena tidak ada Group Manager yang menaungi

### Pengaju Group Manager di Group induk melewati approval
120. `Indra Wijaya {runId}` mengajukan Assign aset `Scanner Canon DR-C225 {runId}` kepada `Putri Handayani {runId}`
121. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Group Manager di Group induk `Kantor Pusat Jakarta {runId}` yang menaungi Group aset `Gudang Jakarta Timur {runId}` lewat ancestor-nya, walau Group aset ber-Require approval `ON` dengan Approval type `All approvers (AND)`
122. Verifikasi log transaksi memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] adalah `Indra Wijaya {runId}`

### Kondisi A dievaluasi sebelum self-approval guard
123. Admin `Budi Santoso {runId}` membuat override pada Group `Gudang Tangerang {runId}` untuk transaksi Assign dengan Require approval `ON` dan Approval type `Any one approver`
124. `Yusuf Hakim {runId}` mengajukan Assign aset `Printer Brother HL-L5100 {runId}` kepada `Putri Handayani {runId}`
125. Verifikasi seluruh langkah approval dilewati dan transaksi langsung `Waiting for Handover` karena pengaju adalah Group Manager yang menaungi Group aset, walau pengaju juga satu-satunya Approver eligible Group `Gudang Tangerang {runId}`
126. Verifikasi log transaksi memuat `Approved by [Nama] (Group Manager — requester)` dengan [Nama] adalah `Yusuf Hakim {runId}`, dan bukan `Approved by system (no independent approver)`

