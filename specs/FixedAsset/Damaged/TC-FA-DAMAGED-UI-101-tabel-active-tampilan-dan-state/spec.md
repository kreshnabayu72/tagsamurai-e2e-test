---
id: TC-FA-DAMAGED-UI-101-tabel-active-tampilan-dan-state
title: "Tabel sub-tab Active: kolom awal, format sel, nilai kosong, nama singkat, badge status dan penanda, toolbar, serta state kosong, tersaring, gagal muat, dan loading"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§4.1#r1", "§4.1#p3", "§4.1#p4", "§4.4#r11", "§5#r1", S-DMG-11, S-DMG-12, S-DMG-16, S-DMG-02, S-DMG-10, "§4.5#p1", "§4#p1", EB-TBL-1@tabel-active, EB-TBL-3@kolom-labels, EB-TBL-4@kolom-last-holder, EB-TBL-4@kolom-reported-by, EB-TBL-4@kolom-modified-by, EB-TBL-8@tabel-active, EB-XM-1, EB-TBL-2@kolom-photo, EB-TBL-2@kolom-brand, EB-TBL-2@kolom-model-type, EB-TBL-2@kolom-tag, EB-TBL-2@kolom-last-holder, EB-TBL-2@kolom-alias-name, EB-TBL-2@kolom-measurement, EB-TBL-2@kolom-division, EB-TBL-2@kolom-labels, EB-TBL-2@kolom-asset-class, EB-TBL-2@kolom-purchase-date, EB-TBL-2@kolom-warranty-expiry, EB-TBL-2@kolom-purchase-cost, EB-TBL-2@kolom-asset-value-commercial, EB-TBL-2@kolom-asset-value-fiscal, "§Aturan Logika Modul#r96"]
smoke: []
dependsOn: []
trace:
  T-DMG-01: [2, 3, 4, 5, 6, 7, 8, 11, 48, 49, 52, 53, 55, 56, 57, 58, 60, 61, 63, 64, 65, 66, 67, 71, 72, 73, 97, 98, 99, 100, 102, 103, 105, 139, 140, 142, 143, 145, 146, 147, 148, 151, 152, 168, 171, 172, 174, 176, 177, 154, 155, 179, 181]
  "§4.1#r1": [133]
  "§4.1#p3": [19, 20, 21, 22, 24, 25]
  "§4.1#p4": [46, 51]
  "§4.4#r11": [15]
  "§5#r1": [130, 131, 132]
  S-DMG-11: [108, 109, 111]
  S-DMG-12: [114, 115]
  S-DMG-16: [118, 119, 122]
  S-DMG-02: [24, 25]
  S-DMG-10: [124, 125, 127, 128]
  "§4.5#p1": [17, 19, 136, 154, 155, 159, 162]
  "§4#p1": [19]
  EB-TBL-1@tabel-active: [108, 109, 114, 115, 116, 118, 119, 120]
  EB-TBL-3@kolom-labels: [78, 79, 80, 81, 82]
  EB-TBL-4@kolom-last-holder: [30, 32, 36, 38, 39, 44, 142, 145]
  EB-TBL-4@kolom-reported-by: [33, 35, 37, 40, 42, 143, 171, 172]
  EB-TBL-4@kolom-modified-by: [74, 76]
  EB-TBL-8@tabel-active: [106]
  EB-XM-1: [46, 47, 51, 68, 69, 70]
  EB-TBL-2@kolom-photo: [28, 168]
  EB-TBL-2@kolom-brand: [84]
  EB-TBL-2@kolom-model-type: [85]
  EB-TBL-2@kolom-tag: [86]
  EB-TBL-2@kolom-last-holder: [27]
  EB-TBL-2@kolom-alias-name: [87]
  EB-TBL-2@kolom-measurement: [88]
  EB-TBL-2@kolom-division: [89]
  EB-TBL-2@kolom-labels: [82]
  EB-TBL-2@kolom-asset-class: [90]
  EB-TBL-2@kolom-purchase-date: [91]
  EB-TBL-2@kolom-warranty-expiry: [92, 174]
  EB-TBL-2@kolom-purchase-cost: [93]
  EB-TBL-2@kolom-asset-value-commercial: [94]
  EB-TBL-2@kolom-asset-value-fiscal: [95, 97]
  "§Aturan Logika Modul#r96": [164, 165]
anchor: []
coverage:
  web: automated
---

# Tabel sub-tab Active: kolom awal, format sel, nilai kosong, nama singkat, badge status dan penanda, toolbar, serta state kosong, tersaring, gagal muat, dan loading

## Prerequisites
- Aktor: Total Control (Aktor Damaged, berhak melihat kolom nilai finansial).
- Layar awal: halaman Assets, tab `Damaged`, sub-tab `Active`.
- Komponen: Tabel T-DMG-01 (sub-tab Active)
- Data:
  - DU-101-1: Record `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, Status `Damaged`, Source `Borrow return`, Photo `projector-epson-eb-x06-2.jpg`, Last Holder `Sari Dewi` (tampil `Sari D`, dari `Sari Dewi`; Division `Operations`, Employee ID `EMP-0145`), Reported By `Rina Wijaya` (tampil `Rina W`, dari `Rina Wijaya`), Reported Date `04/11/26, 17:10` dari `2026-11-04T10:10:00Z`, Days Damaged `7 days` dari 7 hari kalender sampai hari ini `11/11/26`, Last Updated `06/11/26, 09:45` dari `2026-11-06T02:45:00Z`.
  - DU-101-2: Record `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Budi`, Reported By `Budi`, Reported Date `10/11/26, 08:15` dari `2026-11-10T01:15:00Z`, Days Damaged `1 day` dari 1 hari kalender, Last Updated `10/11/26, 08:15` dari `2026-11-10T01:15:00Z`.
  - DU-101-3: Record `Office Chair Ergo - 31`, Asset ID `CHR-2026-0031`, Group `Branch Surabaya`, Status `Damaged`, Source `Reported by scan`, tanpa Photo, Last Holder kosong (tampil `—`), Reported By `Dedi Kurniawan` (tampil `Dedi K`, dari `Dedi Kurniawan`), Reported Date `06/11/26, 13:00` dari `2026-11-06T06:00:00Z`, Days Damaged `5 days` dari 5 hari kalender.
  - DU-101-4: Record `Printer HP LaserJet M404 - 8`, Asset ID `PRN-2026-0008`, Group `Head Office`, Status `Reported Disposal`, Source `Audit`, Last Holder `Buzzlightyear Sumardi` (tampil `Buzzlightyear S`, dari `Buzzlightyear Sumardi`), Reported By `Alexander Graham Bell` (tampil `Alexander G`, dari `Alexander Graham Bell`), Reported Date `15/10/26, 10:00` dari `2026-10-15T03:00:00Z`, Days Damaged `27 days` dari 27 hari kalender.
  - DU-101-5: Record `Monitor Dell P2422H - 6`, Asset ID `MON-2026-0006`, Group `Head Office`, Status `In Disposal Process`, Source `Manual`, Last Holder `Dewi Anggraini` (tampil `Dewi A`, dari `Dewi Anggraini`), Reported By `Dewi Anggreni` (tampil `Dewi A`, dari `Dewi Anggreni`), Reported Date `20/09/26, 14:20` dari `2026-09-20T07:20:00Z`, Days Damaged `52 days` dari 52 hari kalender.
  - DU-101-6: Record `Camera Canon EOS - 3`, Asset ID `CAM-2026-0003`, Group `Head Office`, Status `Damaged` dengan penanda `Missing`, Source `Manual`, Reported By `Agus Prasetyo`, Reported Date `03/11/26, 11:00` dari `2026-11-03T04:00:00Z`.
  - DU-101-7: Record `Drill Bosch GSB - 6`, Asset ID `DRL-2026-0006`, Group `Warehouse`, Status `Damaged` dengan penanda `Reported Missing`, Source `Manual`, Last Holder `Sari Dewi`, Reported By `Agus Prasetyo`, Reported Date `28/10/26, 10:00` dari `2026-10-28T03:00:00Z`.
  - DU-101-8: Record `Laptop Dell Latitude 5420 - 6`, Asset ID `LPT-2026-0006`, Group `Head Office`, Status `Damaged`, Source `Missing asset`, Reported By `Rina Wijaya`, Reported Date `11/11/26, 15:20` dari `2026-11-11T08:20:00Z`, Days Damaged `0 days` karena dilaporkan pada hari ini `11/11/26`.
  - DU-101-9: Record `Generator Set Cummins C100 - 1`, Asset ID `GEN-2026-0001`, Group `Warehouse`, Status `Damaged`, Source `Audit`, Reported By `Agus Prasetyo`, Reported Date `25/03/26, 06:30` dari `2026-03-24T23:30:00Z` pada zona waktu company, Days Damaged `231 days` dari 231 hari kalender.
  - DU-101-10: Record `Tablet Samsung Tab A8 - 3`, Asset ID `TAB-2026-0003`, Brand `Samsung`, Model/Type `Galaxy Tab A8`, TAG `RFID` dan `QR`, Category `Tablet` (hierarki `IT Equipment > Tablet`), Group `Server Room` (hierarki `Head Office > Floor 2 > Server Room`), Status `Damaged`, Source `Manual`, Last Holder `Dewi Anggraini`, Reported By `Agus Prasetyo`, Alias Name `Tab Gudang`, Measurement `Unit`, Division `Operations`, Labels `Warehouse`, `Fragile`, `Priority` (tampil `Fragile`, `Priority`, dan `+1 more`, dari urutan A-Z), Asset Class `Electronic`, Register Date `15/01/26` dari `2026-01-15`, Purchase Date `10/01/26` dari `2026-01-10`, Warranty Expiry `10/01/28` dari `2028-01-10`, Purchase Cost `12500000`, Asset Value (Commercial) `9800000`, Asset Value (Fiscal) `10200000`, Modified By `Rina Wijaya` (tampil `Rina W`, dari `Rina Wijaya`), Reported Date `07/11/26, 10:30` dari `2026-11-07T03:30:00Z`, Last Updated `10/11/26, 09:30` dari `2026-11-10T02:30:00Z`.
  - DU-101-11: Record `Forklift Toyota 8FD - 1`, Asset ID `FLT-2026-0001`, Group `Warehouse`, Status `Damaged`, Source `Manual`, Reported By `Agus Prasetyo`; Brand, Model/Type, Alias Name, Measurement, Division, Asset Class, Purchase Date, Warranty Expiry, Purchase Cost, Asset Value (Commercial), dan Asset Value (Fiscal) tidak pernah diisi; TAG dan Labels tanpa isi (tampil `—`).
  - DU-101-12: Record `Handheld RFID Scanner Zebra TC21 Warehouse Receiving Dock Unit - 14`, Asset ID `HSC-2026-0014`, Brand `Zebra Technologies International Holdings` (tampil `Zebra Techno..nal Holdings`, dari 12 huruf pertama, `..`, dan 12 huruf terakhir), Group `Jakarta Selatan Distribution Center` (tampil `Jakarta Sela..ution Center`, hierarki `Region Jawa > Jakarta Selatan Distribution Center`), Status `Damaged`, Source `Manual`, Division `Regional Procurement and Vendor Management Office Jakarta`, Labels `Warehouse` lalu `Priority` (tampil `Priority` lalu `Warehouse`, dari urutan A-Z), Reported By `Rina Wijaya`.
  - DU-101-13: Record `Folding Chair Ergo - 4`, Asset ID `CHR-2026-0004`, Group `Head Office`, Status `Damaged`, Source `Manual`, Label `Fragile`, Asset Value (Fiscal) `0`, Reported By `Rina Wijaya`.
  - DU-101-14: Record `<b>Meeting</b> Table - 2`, Asset ID `TBL-2026-0002`, Group `Head Office`, Status `Damaged`, Source `Manual`, Reported By `Rina Wijaya`.
  - DU-101-15: Daftar record berjalan kosong untuk entitas yang belum pernah menerima laporan (jumlah record `0`).
  - DU-101-16: Record `Toyota Avanza - 2` di Group `Branch Surabaya`, ada di entitas tetapi di luar cakupan Group aktor `Head Office`.
  - DU-101-19: Record `Welding Machine Lincoln - 2`, Asset ID `WLD-2026-0002`, Group `Warehouse`, Status `Damaged`, Source `Manual`, Reported By `Rina Wijaya`; aset punya foto aset `welding-machine-lincoln-2.jpg`, sedangkan Damaged Photo record sudah dihapus lewat File Manager sehingga tidak ada.
  - DU-101-20: Record `Pressure Washer Karcher - 5`, Asset ID `PWR-2026-0005`, Group `Warehouse`, Status `Damaged`, Source `Manual`, Reported By `Rina Wijaya`; aset belum punya foto aset, dan Damaged Photo record sudah dihapus lewat File Manager sehingga tidak ada.
  - DU-101-18: Record `Handheld Scanner Zebra TC21 - 2`, Asset ID `HSC-2026-0002`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Tono Rahmat` tanpa akun (tampil `Tono R`, dari `Tono Rahmat`; Division `Finance`, PIC `Sinta Maharani` sehingga hover memuat `PIC: Sinta Maharani`, Employee ID `EMP-0217`), Reported By laporan PIC `Sinta Maharani` atas nama `Tono Rahmat` (tampil `Sinta M on behalf of Tono R`, dari `Sinta Maharani` dan `Tono Rahmat`).
  - DU-101-21: Record `Air Conditioner Daikin FTV - 5`, Asset ID `ACN-2026-0005`, Group `Head Office`, Status `Damaged`, Source `Manual`, Reported By `Rina Wijaya`, dua garansi aset: `Manufacturer Warranty` berakhir `15/03/27` dari `2027-03-15` dan `Extended Warranty` berakhir `10/01/28` dari `2028-01-10`; Warranty Expiry tampil `15/03/27`, dari garansi terdekat (hari ini `11/11/26`).
  - DU-101-22: Record `Rugged Laptop Dell - 7`, Asset ID `RLP-2026-0007`, Group `Head Office`, Status `Damaged`, Source `Manual`, Model/Type `Latitude Rugged Extreme Series 14` (33 karakter; tampil `Latitude Rug..me Series 14`, dari 12 huruf pertama, `..`, dan 12 huruf terakhir), Reported By `Rina Wijaya`.
- Kondisi:
  - K1: daftar memuat DU-101-1 sampai DU-101-5 dengan kolom bawaan Setup Column; hari ini `11/11/26`; Date Format bernilai `dd/MM/yy`; Time Format bernilai `24h`; Time Zone bernilai `Asia/Jakarta`.
  - K2: daftar memuat DU-101-6 dan DU-101-7 dengan kolom bawaan Setup Column.
  - K3: daftar memuat DU-101-8 dan DU-101-9 dengan kolom bawaan Setup Column; hari ini `11/11/26`.
  - K4: daftar memuat DU-101-10 sampai DU-101-14; Setup Column menampilkan seluruh kolom, termasuk kolom nilai finansial.
  - K5: daftar kosong sesuai DU-101-15.
  - K6: daftar memuat DU-101-1; pencarian `Printer Hilang` tidak cocok dengan record mana pun sehingga jawaban daftar kosong.
  - K7: daftar kosong untuk aktor karena satu-satunya record, DU-101-16, di luar cakupan Group aktor.
  - K8: memuat daftar gagal karena error server; pemuatan ulang berhasil dengan DU-101-1.
  - K9: jawaban daftar belum tiba saat tabel ditampilkan; begitu jawaban tiba, daftar memuat DU-101-1.
  - K10: lebar tampilan sempit; daftar memuat DU-101-1.
  - K11: daftar memuat DU-101-18.
  - K12: daftar memuat DU-101-19 dan DU-101-20 dengan kolom bawaan Setup Column.
  - K13: daftar memuat DU-101-21; Setup Column menampilkan seluruh kolom, termasuk kolom `Warranty Expiry`; hari ini `11/11/26`; Date Format bernilai `dd/MM/yy`.
  - K14: daftar memuat DU-101-22; Setup Column menampilkan seluruh kolom, termasuk kolom `Model/Type`.

## Test Steps

### Kolom awal dan isi sel baris Damaged
1. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
2. Verifikasi kolom tampil berurutan dari kiri ke kanan: `Checkbox`, `Photo`, `Name`, `Asset ID`, `Group`, `Status`, `Source`, `Last Holder`, `Reported By`, `Reported Date`, `Days Damaged`, `Last Updated`, dan `Actions`
3. Verifikasi header kolom `Brand`, `Model/Type`, `TAG`, `Category`, `Alias Name`, `Measurement`, `Division`, `Labels`, `Asset Class`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Modified By` tidak dirender
4. Verifikasi `Projector Epson EB-X06 - 2` tampil sebagai tautan pada kolom `Name`
5. Verifikasi Asset ID `PRJ-2026-0002` tampil pada baris `Projector Epson EB-X06 - 2`
6. Verifikasi Group `Head Office` tampil pada baris `Projector Epson EB-X06 - 2`
7. Verifikasi Source `Borrow return` tampil pada baris `Projector Epson EB-X06 - 2`
8. Verifikasi foto `projector-epson-eb-x06-2.jpg` tampil pada kolom `Photo` baris `Projector Epson EB-X06 - 2`

### Pratinjau foto dibuka dari kolom Photo
9. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
10. Klik foto pada kolom `Photo` baris `Projector Epson EB-X06 - 2`
11. Verifikasi pratinjau besar foto `projector-epson-eb-x06-2.jpg` tampil
12. Tekan `Esc`

### Nama aset membuka dialog Damage Log
13. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
14. Klik `Projector Epson EB-X06 - 2` pada kolom `Name`
15. Verifikasi dialog `Damage Log` terbuka
16. Klik `✕` pada dialog `Damage Log`
17. Verifikasi fokus kembali ke tautan `Projector Epson EB-X06 - 2` pada kolom `Name`

### Badge status record per nilai
18. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
19. Verifikasi badge status `Damaged` tampil pada baris `Projector Epson EB-X06 - 2`
20. Verifikasi badge status `Waiting for Confirmation` tampil pada baris `Laptop Dell Latitude 5420 - 4`
21. Verifikasi badge status `Reported Disposal` tampil pada baris `Printer HP LaserJet M404 - 8`
22. Verifikasi badge status `In Disposal Process` tampil pada baris `Monitor Dell P2422H - 6`

### Penanda Missing di samping badge status
23. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K2
24. Verifikasi penanda `Missing` tampil di samping badge status `Damaged` pada baris `Camera Canon EOS - 3`
25. Verifikasi penanda `Reported Missing` tampil di samping badge status `Damaged` pada baris `Drill Bosch GSB - 6`

### Nilai kosong pada kolom awal
26. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
27. Verifikasi kolom `Last Holder` baris `Office Chair Ergo - 31` menampilkan `—`
28. Verifikasi avatar inisial tampil pada kolom `Photo` baris `Office Chair Ergo - 31`

### Nama user singkat dan nama lengkap saat hover
29. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
30. Verifikasi kolom `Last Holder` baris `Projector Epson EB-X06 - 2` menampilkan `Sari D`
31. Arahkan pointer ke `Sari D` pada kolom `Last Holder` baris `Projector Epson EB-X06 - 2`
32. Verifikasi nama lengkap `Sari Dewi` tampil
33. Verifikasi kolom `Reported By` baris `Projector Epson EB-X06 - 2` menampilkan `Rina W`
34. Arahkan pointer ke `Rina W` pada kolom `Reported By` baris `Projector Epson EB-X06 - 2`
35. Verifikasi nama lengkap `Rina Wijaya` tampil
36. Verifikasi kolom `Last Holder` baris `Laptop Dell Latitude 5420 - 4` menampilkan `Budi` utuh
37. Verifikasi kolom `Reported By` baris `Printer HP LaserJet M404 - 8` menampilkan `Alexander G`
38. Verifikasi kolom `Last Holder` baris `Printer HP LaserJet M404 - 8` menampilkan `Buzzlightyear S`
39. Verifikasi kolom `Last Holder` baris `Monitor Dell P2422H - 6` menampilkan `Dewi A`
40. Verifikasi kolom `Reported By` baris `Monitor Dell P2422H - 6` menampilkan `Dewi A`
41. Arahkan pointer ke `Dewi A` pada kolom `Reported By` baris `Monitor Dell P2422H - 6`
42. Verifikasi nama lengkap `Dewi Anggreni` tampil
43. Arahkan pointer ke `Dewi A` pada kolom `Last Holder` baris `Monitor Dell P2422H - 6`
44. Verifikasi nama lengkap `Dewi Anggraini` tampil

### Format tanggal dan Days Damaged pada baris bawaan
45. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
46. Verifikasi kolom `Reported Date` baris `Projector Epson EB-X06 - 2` menampilkan `04/11/26, 17:10`
47. Verifikasi kolom `Last Updated` baris `Projector Epson EB-X06 - 2` menampilkan `06/11/26, 09:45`
48. Verifikasi kolom `Days Damaged` baris `Projector Epson EB-X06 - 2` menampilkan `7 days`
49. Verifikasi kolom `Days Damaged` baris `Laptop Dell Latitude 5420 - 4` menampilkan `1 day`

### Tanggal dekat tengah malam dan laporan pada hari ini
50. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K3
51. Verifikasi kolom `Reported Date` baris `Generator Set Cummins C100 - 1` menampilkan `25/03/26, 06:30`
52. Verifikasi kolom `Days Damaged` baris `Generator Set Cummins C100 - 1` menampilkan `231 days`
53. Verifikasi kolom `Days Damaged` baris `Laptop Dell Latitude 5420 - 6` menampilkan `0 days`

### Isi kolom tersembunyi saat ditampilkan
54. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
55. Verifikasi kolom `Brand` baris `Tablet Samsung Tab A8 - 3` menampilkan `Samsung`
56. Verifikasi kolom `Model/Type` baris `Tablet Samsung Tab A8 - 3` menampilkan `Galaxy Tab A8`
57. Verifikasi kolom `TAG` baris `Tablet Samsung Tab A8 - 3` menampilkan satu badge per tipe TAG, yaitu `RFID` dan `QR`
58. Verifikasi kolom `Category` baris `Tablet Samsung Tab A8 - 3` menampilkan `Tablet`
59. Arahkan pointer ke `Tablet` pada kolom `Category` baris `Tablet Samsung Tab A8 - 3`
60. Verifikasi hierarki lengkap `IT Equipment > Tablet` tampil
61. Verifikasi kolom `Group` baris `Tablet Samsung Tab A8 - 3` menampilkan `Server Room`
62. Arahkan pointer ke `Server Room` pada kolom `Group` baris `Tablet Samsung Tab A8 - 3`
63. Verifikasi hierarki lengkap `Head Office > Floor 2 > Server Room` tampil
64. Verifikasi kolom `Alias Name` baris `Tablet Samsung Tab A8 - 3` menampilkan `Tab Gudang`
65. Verifikasi kolom `Measurement` baris `Tablet Samsung Tab A8 - 3` menampilkan `Unit`
66. Verifikasi kolom `Division` baris `Tablet Samsung Tab A8 - 3` menampilkan `Operations`
67. Verifikasi kolom `Asset Class` baris `Tablet Samsung Tab A8 - 3` menampilkan `Electronic`
68. Verifikasi kolom `Register Date` baris `Tablet Samsung Tab A8 - 3` menampilkan `15/01/26`
69. Verifikasi kolom `Purchase Date` baris `Tablet Samsung Tab A8 - 3` menampilkan `10/01/26`
70. Verifikasi kolom `Warranty Expiry` baris `Tablet Samsung Tab A8 - 3` menampilkan `10/01/28`
71. Verifikasi kolom `Purchase Cost` baris `Tablet Samsung Tab A8 - 3` menampilkan `12500000` dalam mata uang Company dengan pemisah ribuan
72. Verifikasi kolom `Asset Value (Commercial)` baris `Tablet Samsung Tab A8 - 3` menampilkan `9800000` dalam mata uang Company dengan pemisah ribuan
73. Verifikasi kolom `Asset Value (Fiscal)` baris `Tablet Samsung Tab A8 - 3` menampilkan `10200000` dalam mata uang Company dengan pemisah ribuan
74. Verifikasi kolom `Modified By` baris `Tablet Samsung Tab A8 - 3` menampilkan `Rina W`
75. Arahkan pointer ke `Rina W` pada kolom `Modified By` baris `Tablet Samsung Tab A8 - 3`
76. Verifikasi nama lengkap `Rina Wijaya` tampil

### Kolom Labels per jumlah label
77. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
78. Verifikasi kolom `Labels` baris `Tablet Samsung Tab A8 - 3` menampilkan dua badge `Fragile` lalu `Priority`
79. Verifikasi kolom `Labels` baris `Tablet Samsung Tab A8 - 3` menampilkan `+1 more`
80. Verifikasi kolom `Labels` baris `Handheld RFID Scanner Zebra TC21 Warehouse Receiving Dock Unit - 14` menampilkan dua badge `Priority` lalu `Warehouse`
81. Verifikasi kolom `Labels` baris `Folding Chair Ergo - 4` menampilkan satu badge `Fragile`
82. Verifikasi kolom `Labels` baris `Forklift Toyota 8FD - 1` menampilkan `—`

### Nilai kosong pada kolom tersembunyi
83. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
84. Verifikasi kolom `Brand` baris `Forklift Toyota 8FD - 1` menampilkan `—`
85. Verifikasi kolom `Model/Type` baris `Forklift Toyota 8FD - 1` menampilkan `—`
86. Verifikasi kolom `TAG` baris `Forklift Toyota 8FD - 1` menampilkan `—`
87. Verifikasi kolom `Alias Name` baris `Forklift Toyota 8FD - 1` menampilkan `—`
88. Verifikasi kolom `Measurement` baris `Forklift Toyota 8FD - 1` menampilkan `—`
89. Verifikasi kolom `Division` baris `Forklift Toyota 8FD - 1` menampilkan `—`
90. Verifikasi kolom `Asset Class` baris `Forklift Toyota 8FD - 1` menampilkan `—`
91. Verifikasi kolom `Purchase Date` baris `Forklift Toyota 8FD - 1` menampilkan `—`
92. Verifikasi kolom `Warranty Expiry` baris `Forklift Toyota 8FD - 1` menampilkan `—`
93. Verifikasi kolom `Purchase Cost` baris `Forklift Toyota 8FD - 1` menampilkan `—`
94. Verifikasi kolom `Asset Value (Commercial)` baris `Forklift Toyota 8FD - 1` menampilkan `—`
95. Verifikasi kolom `Asset Value (Fiscal)` baris `Forklift Toyota 8FD - 1` menampilkan `—`

### Nilai nol, teks panjang, dan markup tampil apa adanya
96. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
97. Verifikasi kolom `Asset Value (Fiscal)` baris `Folding Chair Ergo - 4` menampilkan nilai `0`, bukan `—`
98. Verifikasi `Handheld RFID Scanner Zebra TC21 Warehouse Receiving Dock Unit - 14` tampil utuh pada kolom `Name`
99. Verifikasi `Regional Procurement and Vendor Management Office Jakarta` tampil utuh pada kolom `Division` baris `Handheld RFID Scanner Zebra TC21 Warehouse Receiving Dock Unit - 14`
100. Verifikasi kolom `Brand` baris `Handheld RFID Scanner Zebra TC21 Warehouse Receiving Dock Unit - 14` menampilkan badge `Zebra Techno..nal Holdings`
101. Arahkan pointer ke badge `Zebra Techno..nal Holdings`
102. Verifikasi nama penuh `Zebra Technologies International Holdings` tampil
103. Verifikasi kolom `Group` baris `Handheld RFID Scanner Zebra TC21 Warehouse Receiving Dock Unit - 14` menampilkan badge `Jakarta Sela..ution Center`
104. Arahkan pointer ke badge `Jakarta Sela..ution Center`
105. Verifikasi hierarki lengkap `Region Jawa > Jakarta Selatan Distribution Center` tampil
106. Verifikasi `<b>Meeting</b> Table - 2` tampil apa adanya sebagai teks pada kolom `Name`

### State kosong alami
107. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K5
108. Verifikasi judul `No damaged assets` tampil
109. Verifikasi deskripsi `Assets reported damaged will appear here until they're resolved.` tampil

### State kosong untuk aktor ini
110. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K7
111. Verifikasi judul `No damaged assets` tampil

### State kosong tersaring
112. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K6
113. Ketik Search `Printer Hilang`, tekan Enter
114. Verifikasi judul `No results found` tampil
115. Verifikasi deskripsi `Try adjusting your search or filter.` tampil
116. Verifikasi judul `No damaged assets` tidak tampil

### Gagal muat bukan state kosong
117. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K8
118. Verifikasi pesan `Unable to load this data.` tampil
119. Verifikasi tombol `[Try Again]` tampil
120. Verifikasi judul `No damaged assets` tidak tampil
121. Klik `[Try Again]`
122. Verifikasi baris `Projector Epson EB-X06 - 2` tampil

### Loading saat daftar dimuat
123. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K9
124. Verifikasi header kolom `Name` tetap tampil selama daftar dimuat
125. Verifikasi tabel ditandai sedang memuat dan baris `Projector Epson EB-X06 - 2` belum tampil
126. Jawaban daftar tiba dengan DU-101-1
127. Verifikasi baris `Projector Epson EB-X06 - 2` tampil
128. Verifikasi tabel tidak lagi ditandai sedang memuat

### Toolbar sub-tab Active
129. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
130. Verifikasi kotak Search tampil dengan placeholder `Search asset name or ID...`
131. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search
132. Verifikasi kontrol Filter dan Download tampil di toolbar
133. Verifikasi toolbar dan tabel T-DMG-01 tampil bersama pada sub-tab `Active`

### Alasan checkbox Disabled tersampaikan lewat hover
134. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
135. Arahkan pointer ke checkbox pada baris `Laptop Dell Latitude 5420 - 4`
136. Verifikasi alasan checkbox Disabled tersampaikan lewat hover[^drift-1]

### Hover Last Holder memuat Division dan Employee ID pemegang
137. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
138. Arahkan pointer ke `Sari D` pada kolom `Last Holder` baris `Projector Epson EB-X06 - 2`
139. Verifikasi Division `Operations` tampil
140. Verifikasi Employee ID `EMP-0145` tampil

### Pemegang tanpa akun dan laporan PIC
141. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K11
142. Verifikasi kolom `Last Holder` baris `Handheld Scanner Zebra TC21 - 2` menampilkan `Tono R`
143. Verifikasi kolom `Reported By` baris `Handheld Scanner Zebra TC21 - 2` menampilkan `Sinta M on behalf of Tono R`
144. Arahkan pointer ke `Tono R` pada kolom `Last Holder` baris `Handheld Scanner Zebra TC21 - 2`
145. Verifikasi nama lengkap `Tono Rahmat` tampil
146. Verifikasi Division `Finance` tampil
147. Verifikasi `PIC: Sinta Maharani` tampil
148. Verifikasi Employee ID `EMP-0217` tampil

### Klik label membuka popover Labels
149. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
150. Klik `+1 more` pada kolom `Labels` baris `Tablet Samsung Tab A8 - 3`
151. Verifikasi popover `Labels` tampil
152. Verifikasi popover `Labels` memuat seluruh label `Fragile`, `Priority`, dan `Warehouse`

### Lebar tampilan sempit
153. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K10
154. Verifikasi tabel T-DMG-01 dapat digulir horizontal
155. Verifikasi toolbar membungkus ke baris berikutnya

### Ikon Filter dan menu kolom dapat dioperasikan dengan keyboard
156. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
157. Fokuskan ikon Filter dengan keyboard
158. Tekan Enter
159. Verifikasi Filter Panel tampil
160. Fokuskan header kolom Actions (`⋯`) dengan keyboard
161. Tekan Enter
162. Verifikasi daftar kolom dengan checkbox tampil

### Kolom Photo jatuh ke nilai kosong sesudah Damaged Photo dihapus
163. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K12
164. Verifikasi foto aset `welding-machine-lincoln-2.jpg` tampil pada kolom `Photo` baris `Welding Machine Lincoln - 2`
165. Verifikasi avatar inisial tampil pada kolom `Photo` baris `Pressure Washer Karcher - 5`

### Hover foto pada kolom Photo menampilkan pratinjau besar
166. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
167. Arahkan pointer ke foto pada kolom `Photo` baris `Projector Epson EB-X06 - 2`
168. Verifikasi pratinjau besar foto `projector-epson-eb-x06-2.jpg` tampil

### Hover Reported By pada laporan PIC atas nama pemegang
169. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K11
170. Arahkan pointer ke `Sinta M on behalf of Tono R` pada kolom `Reported By` baris `Handheld Scanner Zebra TC21 - 2`
171. Verifikasi nama lengkap pelapor `Sinta Maharani` tampil
172. Verifikasi nama lengkap pemegang yang diwakili `Tono Rahmat` tampil

### Warranty Expiry memuat garansi terdekat dan daftar seluruh garansi saat hover
173. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K13
174. Verifikasi kolom `Warranty Expiry` baris `Air Conditioner Daikin FTV - 5` menampilkan `15/03/27`
175. Arahkan pointer ke `15/03/27` pada kolom `Warranty Expiry` baris `Air Conditioner Daikin FTV - 5`
176. Verifikasi garansi `Manufacturer Warranty — 15/03/27` tampil pada daftar garansi
177. Verifikasi garansi `Extended Warranty — 10/01/28` tampil pada daftar garansi

### Hover Model/Type menampilkan nama penuh
178. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K14
179. Verifikasi kolom `Model/Type` baris `Rugged Laptop Dell - 7` menampilkan badge `Latitude Rug..me Series 14`
180. Arahkan pointer ke badge `Latitude Rug..me Series 14`
181. Verifikasi nama penuh `Latitude Rugged Extreme Series 14` tampil

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.5: `Tooltip Disabled 🔖 dapat diakses lewat fokus`. Kontrak `Tooltip#38`: `A disabled control cannot be focused, so its tooltip opens on hover only`. Diasersi: kontrak (SB-7), sehingga alasan pada kontrol Disabled diasersi lewat hover dan klausa fokus PRD tidak diasersi.
