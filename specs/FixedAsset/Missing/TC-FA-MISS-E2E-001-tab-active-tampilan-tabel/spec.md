---
id: TC-FA-MISS-E2E-001-tab-active-tampilan-tabel
title: "Tab Active: kolom default, format sel, badge status, penanda Long missing, dan tautan Missing Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1a#r1, §4.1a#r2, §4.1a#r3, §4.1a#r4, §4.1a#r5, §4.1a#r6, §4.1a#r7, §4.1a#r8, §4.1a#r9, §4.1a#r10, §4.1a#r11, §4.1a#r12, §4.1a#r13, §4.1a#r14, §4.1a#r15, §4.1a#r16, §4.1a#r17, §4.1a#r18, §4.1a#r19, §4.1a#r20, §4.1a#r21, §4.1a#r22, §4.1a#r23, §4.1a#r24, §4.1a#r25, §4.1a#r26, §4.1a#r27, §4.1a#r28, §4.1a#p1, §4.1a#p2, §4.1#p2, §4.1#p3, §4.1#p4, §4.2.1#p1, §4.2.1#b1, §4.2.1#b3, §4.3#r2, §4.3#r5, §4.4#r1, §4.4#r10, §5#r1, §5#r4, §5#r5, §5#r7, §5#r8, §5#r9, §9.5#r1, §9.5#r2, §9.5#r9, §9.4.2#r16, §9.4.2#r29, §9.2#b16, §4.1a#r29, §4.1a#p5, §4.1a#p6, §4.1a#p7, §4.3#r3, §4.3#r6, §4.1a#r34, §1.2#r112, EB-AKS-4, EB-TBL-12, §9.11#r2, §9.11#b1, §9.10#p1, §4.1#r1, §4.1#r2, §1#b2, §9.1#r2, EB-TBL-1@tabel-active]
smoke: [EB-TBL-1@tabel-active]
dependsOn: []
trace:
  §4.1a#r1: [15, 18]
  §4.1a#r2: [15, 19, 60]
  §4.1a#r3: [15, 20]
  §4.1a#r4: [17, 72]
  §4.1a#r5: [17, 72]
  §4.1a#r6: [17, 72, 75, 76]
  §4.1a#r7: 17
  §4.1a#r8: [15, 21]
  §4.1a#r9: [15, 22]
  §4.1a#r10: [15, 23]
  §4.1a#r11: [15, 24, 25]
  §4.1a#r12: [15, 26, 27, 28, 29]
  §4.1a#r13: [15, 30]
  §4.1a#r14: [15, 31]
  §4.1a#r15: [15, 32, 33]
  §4.1a#r16: [17, 72]
  §4.1a#r17: [17, 72]
  §4.1a#r18: [17, 72]
  §4.1a#r19: [17, 72]
  §4.1a#r20: [17, 72]
  §4.1a#r21: [17, 72]
  §4.1a#r22: [17, 72]
  §4.1a#r23: [17, 72]
  §4.1a#r24: [17, 71, 72]
  §4.1a#r25: [17, 71, 72]
  §4.1a#r26: [17, 71, 72]
  §4.1a#r27: [17, 72]
  §4.1a#r28: [15, 34]
  §4.1a#p1: 12
  §4.1a#p2: 16
  §4.1#p2: 22
  §4.1#p3: [15, 31]
  §4.1#p4: [26, 28]
  §4.2.1#p1: [2, 3, 6, 96]
  §4.2.1#b1: 7
  §4.2.1#b3: 4
  §4.3#r2: 33
  §4.3#r5: 71
  §4.4#r1: 82
  §4.4#r10: 60
  §5#r1: 6
  §5#r4: 14
  §5#r5: 67
  §5#r7: 8
  §5#r8: [71, 72]
  §5#r9: 15
  §9.5#r1: 5
  §9.5#r2: 14
  §9.5#r9: 9
  §9.4.2#r16: 35
  §9.4.2#r29: [28, 29]
  §9.2#b16: [12, 13, 84]
  §4.1a#r29: [37, 64]
  §4.1a#p5: [37, 38]
  §4.1a#p6: [37, 44, 48, 52, 56, 88]
  §4.1a#p7: [49, 53, 57]
  §4.3#r3: [49, 53]
  §4.3#r6: [38, 45, 53]
  §4.1a#r34: [38, 48]
  §1.2#r112: 41
  EB-AKS-4: 10
  EB-TBL-12: 26
  §9.11#r2: 71
  §9.11#b1: 71
  §9.10#p1: 75
  §4.1#r1: 6
  §4.1#r2: 5
  §1#b2: [2, 60]
  §9.1#r2: 6
  EB-TBL-1@tabel-active: 78
anchor: []
coverage:
  web: automated
---

# Tab Active: kolom default, format sel, badge status, penanda Long missing, dan tautan Missing Log

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-001-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini, tampil sebagai `Rina W`, dari `Rina Wijaya {runId}`.
  - DU-001-2: User `Andi Pratama {runId}`, role Group Manager pada Group `Head Office {runId}`; tampil sebagai `Andi P`, dari `Andi Pratama {runId}`.
  - DU-001-3: User `Joko Susilo {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing; tampil sebagai `Joko S`, dari `Joko Susilo {runId}`.
  - DU-001-4: User `Agus Prasetyo {runId}`, role Manage asset & TAG (Update) pada Group `Branch Surabaya {runId}`; tampil sebagai `Agus P`, dari `Agus Prasetyo {runId}`.
  - DU-001-5: User `Dewi Anggraini {runId}`, role Manage asset & TAG (Update) pada Group `Head Office {runId}`, dinonaktifkan sesudah menjadi Last holder record DU-001-11; tampil sebagai `Dewi A`, dari `Dewi Anggraini {runId}`.
  - DU-001-6: Record berstatus `Missing` untuk aset `Laptop Dell Latitude 5420 {runId}` (Group `Finance Room {runId}`, TAG `RFID`), Source `Borrow`, Last Holder `Andi Pratama {runId}`, pemindai terakhir reader `Lobby reader {runId}` pada T0 − 9 hari pukul `10:12`, Reported By `Andi Pratama {runId}`, Reported Date T0 − 8 hari pukul `09:30`, tanpa pembaruan sesudah dilaporkan. Days Missing `8 days`, dari selisih 8 hari kalender. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-001-7: Record berstatus `Waiting for Confirmation` untuk aset `Hand Pallet Truck {runId}` (Group `Warehouse {runId}`, TAG `NFC`), Source `Reported by holder`, Last Holder `Joko Susilo {runId}`, belum pernah terpindai, Reported By `Joko Susilo {runId}`, Reported Date T0 − 1 hari pukul `07:15`, tanpa pembaruan. Days Missing `1 day`, dari selisih 1 hari kalender.
  - DU-001-8: Record berstatus `Reported Disposal` untuk aset `Projector Epson EB-X06 {runId}` (Group `Branch Surabaya {runId}`, TAG `QR`), Source `Stock opname`, tanpa Last Holder, pemindai terakhir pengguna `Agus Prasetyo {runId}` pada T0 − 45 hari pukul `14:05`, Reported By `Agus Prasetyo {runId}`, Reported Date T0 − 41 hari pukul `08:00`. Days Missing `41 days`, dari selisih 41 hari kalender.
  - DU-001-9: Record berstatus `In Disposal Process` untuk aset `Printer HP LaserJet M404 {runId}` (Group `Head Office {runId}`, TAG `BLE`), Source `Manual`, tanpa Last Holder, pemindai terakhir reader `Lobby reader {runId}` pada T0 − 80 hari pukul `16:40`, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 78 hari pukul `10:00`. Days Missing `78 days`, dari selisih 78 hari kalender.
  - DU-001-10: Record berstatus `Missing` untuk aset `Toyota Innova {runId}` (Group `Branch Surabaya {runId}`, TAG `GPS`), Source `Transfer`, tanpa Last Holder, pemindai terakhir reader `Gate B reader {runId}` pada T0 − 11 hari pukul `16:20`, Reported By `Agus Prasetyo {runId}`, Reported Date T0 − 10 hari pukul `09:00`, tanpa pembaruan sesudah dilaporkan. Days Missing `10 days`, dari selisih 10 hari kalender.
  - DU-001-11: Record berstatus `Missing` untuk aset `Laptop Lenovo ThinkPad T14 {runId}` (Group `Head Office {runId}`, TAG `NFC` dan `QR`), Source `Manual`, Last Holder `Dewi Anggraini {runId}`, pemindai terakhir reader `Gate A reader {runId}` pada T0 − 37 hari pukul `11:10`, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 34 hari pukul `09:00`. Days Missing `34 days`, dari selisih 34 hari kalender, melewati Long missing after sehingga memuat penanda `Long missing`.
  - DU-001-12: Record berstatus `Missing` untuk aset `Monitor LG 27UL500 {runId}` (Group `Head Office {runId}`, tanpa TAG), Source `Borrow`, Last Holder `Rina Wijaya {runId}` (aktor spec ini), Reported By `Rina Wijaya {runId}`, Reported Date T0 − 3 hari pukul `08:00`, tanpa pembaruan sesudah dilaporkan. Days Missing `3 days`, dari selisih 3 hari kalender.
  - DU-001-13: Record berstatus `Found` untuk aset `Camera Canon EOS {runId}` (Group `Head Office {runId}`), Source `Manual`, Reported By `Rina Wijaya {runId}`, sudah selesai sehingga hanya ada di tab History.
  - DU-001-14: kata kunci Search `{runId} tidakada` yang tidak cocok dengan kolom mana pun.
  - DU-001-15: isian Report Disposal untuk DU-001-6: Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - Long missing after bernilai `30`.
  - T0 adalah waktu spec dijalankan; tanggal Reported Date dan pemindaian pada entri di atas dihitung relatif terhadap T0.
  - Level Feature Suite Disposal pada entitas aktor adalah Basic atau Full, dan `Rina Wijaya {runId}` sebagai Total Control memegang hak Report Disposal (Aktor Disposal).
  - Plan client membuka semua tipe TAG: `RFID`, `NFC`, `QR`, `BLE`, dan `GPS`.

## Test Steps

### Halaman Missing terbuka di sub-tab Active
1. Klik tab `Missing` pada halaman Assets
2. Verifikasi tab `Missing` tampil bersama tab `Assets` dan `Registration`, dan tab `Missing` memuat badge jumlah
3. Verifikasi Breadcrumb memuat `Assets`, `Missing`, dan `Active`
4. Verifikasi pada Breadcrumb hanya `Missing` yang dapat diklik, sedangkan `Assets` dan `Active` tampil sebagai label statis yang tidak bisa diklik[^drift-1]
5. Verifikasi sub-tab `Active` aktif sebagai sub-tab awal dan sub-tab `History` tersedia
6. Verifikasi toolbar tab Active memuat Search, Filter, Download, dan `[Scan Found Asset]`
7. Verifikasi tidak ada tombol `Report Missing` di halaman Missing
8. Verifikasi tidak ada tombol `Changelog` di toolbar

### Tanpa filter bawaan dan kontrol tabel aktif
9. Verifikasi ikon Filter tidak berbadge titik karena tidak ada filter yang ter-Apply
10. Verifikasi Search, Filter, ikon sort pada header kolom data, kontrol Pagination, dan header kolom Actions pembuka Setup Column tampil dan aktif untuk Total Control

### Baris data spec tampil di tab Active dengan kolom bawaan dan urutan default
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi tabel memuat baris untuk `Hand Pallet Truck {runId}`, `Printer HP LaserJet M404 {runId}`, `Projector Epson EB-X06 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Toyota Innova {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Monitor LG 27UL500 {runId}`
13. Verifikasi baris `Camera Canon EOS {runId}` tidak tampil di tab Active karena recordnya berstatus `Found`
14. Verifikasi urutan baris dari atas ke bawah: `Hand Pallet Truck {runId}`, `Printer HP LaserJet M404 {runId}`, `Projector Epson EB-X06 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Toyota Innova {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Monitor LG 27UL500 {runId}`, yaitu `Waiting for Confirmation` di atas lalu Days Missing terlama dulu
15. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Group`, `Status`, `Source`, `Last Holder`, `Last Seen`, `Reported By`, `Reported Date`, `Days Missing`, `Last Updated`, dengan `Status` tepat setelah `Group` dan `Last Updated` sebagai kolom data terakhir sebelum Actions
16. Verifikasi kolom Checkbox dan kolom Actions tampil pada tabel Active
17. Verifikasi kolom `Brand`, `Model/Type`, `TAG`, `Category`, `Alias Name`, `Measurement`, `Division`, `Labels`, `Asset Class`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Modified By` tidak tampil sebagai kolom bawaan

### Isi sel dari data awal
18. Verifikasi kolom Photo menampilkan foto aset atau avatar inisial pada setiap baris
19. Verifikasi kolom Name setiap baris berformat `[Asset Name] - [Increment]`, dengan nama aset `Hand Pallet Truck {runId}`, `Printer HP LaserJet M404 {runId}`, `Projector Epson EB-X06 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Toyota Innova {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Monitor LG 27UL500 {runId}` dan Increment milik entri datanya
20. Verifikasi kolom Asset ID setiap baris menampilkan Asset ID milik entri datanya, DU-001-6 sampai DU-001-12
21. Verifikasi kolom Group menampilkan `Finance Room {runId}` pada baris `Laptop Dell Latitude 5420 {runId}`, `Warehouse {runId}` pada baris `Hand Pallet Truck {runId}`, `Branch Surabaya {runId}` pada baris `Projector Epson EB-X06 {runId}` dan `Toyota Innova {runId}`, dan `Head Office {runId}` pada baris `Printer HP LaserJet M404 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, dan `Monitor LG 27UL500 {runId}`
22. Verifikasi kolom Status menampilkan `Waiting for Confirmation` pada baris `Hand Pallet Truck {runId}`, `Missing` pada baris `Laptop Dell Latitude 5420 {runId}`, `Toyota Innova {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, dan `Monitor LG 27UL500 {runId}`, `Reported Disposal` pada baris `Projector Epson EB-X06 {runId}`, dan `In Disposal Process` pada baris `Printer HP LaserJet M404 {runId}`
23. Verifikasi kolom Source menampilkan `Borrow` pada baris `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 27UL500 {runId}`, `Reported by holder` pada baris `Hand Pallet Truck {runId}`, `Stock opname` pada baris `Projector Epson EB-X06 {runId}`, `Manual` pada baris `Printer HP LaserJet M404 {runId}` dan `Laptop Lenovo ThinkPad T14 {runId}`, dan `Transfer` pada baris `Toyota Innova {runId}`, tanpa nomor transaksi
24. Verifikasi kolom Last Holder menampilkan `Andi P` pada baris `Laptop Dell Latitude 5420 {runId}`, `Joko S` pada baris `Hand Pallet Truck {runId}`, `Dewi A` pada baris `Laptop Lenovo ThinkPad T14 {runId}`, dan `Rina W` pada baris `Monitor LG 27UL500 {runId}`
25. Verifikasi kolom Last Holder menampilkan `—` pada baris `Projector Epson EB-X06 {runId}`, `Printer HP LaserJet M404 {runId}`, dan `Toyota Innova {runId}` karena asetnya tidak dipegang
26. Verifikasi kolom Last Seen baris `Laptop Dell Latitude 5420 {runId}` menampilkan tanggal dan jam pemindaian T0 − 9 hari dengan format `DD/MM/YY` dan `HH:mm`, diikuti tanda `·` dan nama pemindai `Lobby reader {runId}` persis seperti yang dibuat pengguna
27. Verifikasi kolom Last Seen baris `Projector Epson EB-X06 {runId}` menampilkan nama pemindai `Agus P`, dari `Agus Prasetyo {runId}`, dan baris `Laptop Lenovo ThinkPad T14 {runId}` menampilkan nama pemindai `Gate A reader {runId}`
28. Verifikasi kolom Last Seen baris `Hand Pallet Truck {runId}` menampilkan `Unknown` karena asetnya belum pernah terpindai
29. Verifikasi kolom Last Seen baris `Monitor LG 27UL500 {runId}` menampilkan `—` karena asetnya tanpa TAG
30. Verifikasi kolom Reported By menampilkan `Andi P` pada baris `Laptop Dell Latitude 5420 {runId}`, `Joko S` pada baris `Hand Pallet Truck {runId}`, `Agus P` pada baris `Projector Epson EB-X06 {runId}` dan `Toyota Innova {runId}`, dan `Rina W` pada baris `Printer HP LaserJet M404 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, dan `Monitor LG 27UL500 {runId}`
31. Verifikasi kolom Reported Date baris `Laptop Dell Latitude 5420 {runId}` menampilkan tanggal T0 − 8 hari dengan format `DD/MM/YY` dan jam `09:30`, dan baris `Hand Pallet Truck {runId}` menampilkan tanggal T0 − 1 hari dengan jam `07:15`
32. Verifikasi kolom Days Missing menampilkan `1 day` pada baris `Hand Pallet Truck {runId}`, `78 days` pada baris `Printer HP LaserJet M404 {runId}`, `41 days` pada baris `Projector Epson EB-X06 {runId}`, `34 days` pada baris `Laptop Lenovo ThinkPad T14 {runId}`, `10 days` pada baris `Toyota Innova {runId}`, `8 days` pada baris `Laptop Dell Latitude 5420 {runId}`, dan `3 days` pada baris `Monitor LG 27UL500 {runId}`
33. Verifikasi penanda `Long missing` tampil pada kolom Days Missing baris `Laptop Lenovo ThinkPad T14 {runId}` dan tidak tampil pada baris `Laptop Dell Latitude 5420 {runId}`, `Toyota Innova {runId}`, `Monitor LG 27UL500 {runId}`, `Projector Epson EB-X06 {runId}`, dan `Printer HP LaserJet M404 {runId}`, walau baris `Projector Epson EB-X06 {runId}` dan `Printer HP LaserJet M404 {runId}` sudah lewat `30` hari
34. Verifikasi kolom Last Updated baris `Laptop Dell Latitude 5420 {runId}`, `Hand Pallet Truck {runId}`, `Toyota Innova {runId}`, dan `Monitor LG 27UL500 {runId}` menampilkan waktu yang sama dengan Reported Date barisnya dalam format `DD/MM/YY` dan `HH:mm`
35. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId}` tetap tampil dengan Last Holder `Dewi A` walau Last holder-nya sudah dinonaktifkan

### Menu aksi baris per status
36. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
37. Verifikasi menu baris `Laptop Dell Latitude 5420 {runId}` memuat berurutan `Missing Log`, `Add Update`, `Mark as Found`, `Report Disposal`, dengan aksi bernama `Missing Log`
38. Verifikasi menu baris `Laptop Dell Latitude 5420 {runId}` tidak memuat `Review`, `Cancel Disposal Report`, dan `Detail`
39. Tekan Esc untuk menutup menu
40. Klik `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
41. Verifikasi menu baris `Laptop Lenovo ThinkPad T14 {runId}` memuat `Report Disposal` sebagai saran tindak lanjut bagi record `Missing` yang sudah melewati Long missing after
42. Tekan Esc untuk menutup menu
43. Klik `⋯` pada baris `Hand Pallet Truck {runId}`
44. Verifikasi menu baris `Hand Pallet Truck {runId}` memuat berurutan `Missing Log`, `Add Update`, `Review`, `Mark as Found`
45. Verifikasi menu baris `Hand Pallet Truck {runId}` tidak memuat `Report Disposal` dan `Cancel Disposal Report`
46. Tekan Esc untuk menutup menu
47. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
48. Verifikasi menu baris `Projector Epson EB-X06 {runId}` memuat berurutan `Missing Log`, `Add Update`, `Cancel Disposal Report`, dengan `Cancel Disposal Report` sebagai aksi terakhir
49. Verifikasi menu baris `Projector Epson EB-X06 {runId}` tidak memuat `Mark as Found`
50. Tekan Esc untuk menutup menu
51. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
52. Verifikasi menu baris `Printer HP LaserJet M404 {runId}` memuat `Missing Log`, `Add Update`
53. Verifikasi menu baris `Printer HP LaserJet M404 {runId}` tidak memuat `Mark as Found` dan `Cancel Disposal Report`
54. Tekan Esc untuk menutup menu

### Aksi yang terhalang pemisahan tugas Last holder
55. Klik `⋯` pada baris `Monitor LG 27UL500 {runId}`
56. Verifikasi menu baris `Monitor LG 27UL500 {runId}` memuat `Missing Log` dan `Add Update` yang aktif
57. Verifikasi `Mark as Found` dan `Report Disposal` pada baris `Monitor LG 27UL500 {runId}` Disabled, dan alasan `You were holding this asset. Ask another admin.` tersampaikan pada keduanya
58. Tekan Esc untuk menutup menu

### Missing Log terbuka dari kolom Name dan dari aksi baris
59. Klik nama aset pada kolom Name baris `Laptop Dell Latitude 5420 {runId}`
60. Verifikasi dialog `Missing Log` terbuka untuk record baris `Laptop Dell Latitude 5420 {runId}`
61. Tekan Esc untuk menutup dialog `Missing Log`
62. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
63. Klik `Missing Log` pada menu
64. Verifikasi dialog `Missing Log` terbuka untuk record baris `Laptop Dell Latitude 5420 {runId}`
65. Tekan Esc untuk menutup dialog `Missing Log`

### Bulk Report Disposal tersedia di tab Active
66. Centang baris `Laptop Dell Latitude 5420 {runId}`
67. Verifikasi bar aksi bulk memuat aksi `Report Disposal`
68. Hapus centang baris `Laptop Dell Latitude 5420 {runId}`

### Kolom lain tersedia lewat Setup Column
69. Klik header kolom Actions
70. Klik `Setup Column...`
71. Verifikasi modal `Setup Column` memuat kolom `Purchase Cost`, `Asset Value (Commercial)`, `Asset Value (Fiscal)` bagi Total Control
72. Verifikasi di modal `Setup Column` kolom `Photo`, `Name`, `Asset ID`, `Group`, `Status`, `Source`, `Last Holder`, `Last Seen`, `Reported By`, `Reported Date`, `Days Missing`, `Last Updated` tercentang dan kolom `Brand`, `Model/Type`, `TAG`, `Category`, `Alias Name`, `Measurement`, `Division`, `Labels`, `Asset Class`, `Register Date`, `Purchase Date`, `Warranty Expiry`, `Purchase Cost`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Modified By` tidak tercentang
73. Centang kolom `TAG`
74. Klik `[Save]`
75. Verifikasi kolom `TAG` tampil dan setiap tipe TAG yang terbuka tampil sebagai ikon ber-label: `RFID` pada baris `Laptop Dell Latitude 5420 {runId}`, `NFC` pada baris `Hand Pallet Truck {runId}`, `QR` pada baris `Projector Epson EB-X06 {runId}`, `BLE` pada baris `Printer HP LaserJet M404 {runId}`, `GPS` pada baris `Toyota Innova {runId}`, serta `NFC` dan `QR` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
76. Verifikasi kolom `TAG` baris `Monitor LG 27UL500 {runId}` menampilkan `—` karena asetnya tanpa TAG

### Tanpa hasil tersaring
77. Ketik Search `{runId} tidakada`, tekan Enter
78. Verifikasi `No results found` dan `Try adjusting your search or filter.` tampil
79. Klik `(←)` pada kotak Search

### Sub-tab tersimpan di URL
80. Klik sub-tab `History`
81. Muat ulang halaman
82. Verifikasi sub-tab `History` tetap aktif sesudah halaman dimuat ulang karena sub-tab tersimpan di URL
83. Ketik Search `{runId}`, tekan Enter
84. Verifikasi baris `Camera Canon EOS {runId}` tampil di tab History dengan Status `Found`

### Confirm dan Reject bukan item menu baris
85. Klik sub-tab `Active`
86. Ketik Search `{runId}`, tekan Enter
87. Klik `⋯` pada baris `Hand Pallet Truck {runId}`
88. Verifikasi menu baris `Hand Pallet Truck {runId}` yang berstatus `Waiting for Confirmation` tidak memuat `Confirm` dan `Reject`
89. Tekan Esc untuk menutup menu

### Badge tab Missing berkurang saat record Missing berpindah ke Reported Disposal
90. Catat jumlah pada badge tab `Missing` di halaman Assets
91. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
92. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
93. Klik `Report Disposal`
94. Isi Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`
95. Kirim dialog Report Disposal
96. Verifikasi jumlah pada badge tab `Missing` berkurang satu dari jumlah yang dicatat, karena record yang berpindah ke `Reported Disposal` tidak dihitung

[^drift-1]: Drift PRD vs foundation. PRD §4.2.1 butir 3: pada Breadcrumb `Assets > Missing > [Active | History]` hanya `Assets` yang dapat diklik; `Missing` dan sub-tab adalah halaman aktif. Foundation `prd-conventions.md` §27.0: segmen pertama dan terakhir tidak bisa diklik, hanya segmen di tengah yang bisa diklik pada breadcrumb dengan 3 segmen atau lebih. Diasersi: foundation, karena breadcrumb adalah pola bersama (SB-4).
