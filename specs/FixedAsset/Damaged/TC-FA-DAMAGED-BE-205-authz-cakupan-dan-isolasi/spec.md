---
id: TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi
title: "Server menegakkan hak per role dan cakupan Group, menolak aksi tulis tanpa capability, menolak Damage Log di luar cakupan dengan 403, membatasi nilai finansial, dan memblokir aksi tulis pada entitas Suspended/Expired atau plan Disposal None"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§2#b1", "§2#b2", "§2#b3", "§2#b5", "§2.1#b2", "§2.1#b5", "§2.1#b6", "§2.1#b8", "§9.3#b1", "§9.3#b2", "§9.11#r1", "§9.11#r2", "§9.11#b1", "§7.1#p1", "§4.2.2#p2", "§9.10#p1", "S-DMG-09", "§9.4.2#r19", "§9.4.2#r26", "§9.4.2#r32", "§9.4.4#r15", "§9.4.4#r14", "§9.4.4#r29", "§9.4.1#r1", "§9.4.1#r2", "§9.4.1#r4", "EB-AKS-7", "EB-AKS-3@report-damaged", "EB-AKS-3@confirm", "EB-AKS-3@reject", "EB-AKS-3@cancel-report", "EB-AKS-3@mark-as-repaired", "EB-AKS-3@cancel-disposal-report", "§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§2#b1": [20, 86]
  "§2#b2": [8, 12]
  "§2#b3": [10, 30]
  "§2#b5": 2
  "§2.1#b2": [62, 64, 66, 70, 72, 126, 128, 130, 132]
  "§2.1#b5": [46, 48, 50, 112, 114]
  "§2.1#b6": [6, 20, 40, 146, 148, 150, 152, 154]
  "§2.1#b8": [8, 10, 14]
  "§9.3#b1": [62, 64, 116, 118, 120, 122, 124, 134, 136]
  "§9.3#b2": [14, 42, 74, 82]
  "§9.11#r1": [58, 66, 70]
  "§9.11#r2": [84, 86, 88, 92]
  "§9.11#b1": [84, 88, 90]
  "§7.1#p1": [14, 60, 74]
  "§4.2.2#p2": [58, 60]
  "§9.10#p1": [104, 106]
  "S-DMG-09": [88, 90, 92]
  "§9.4.2#r19": [60, 66, 68, 70, 74, 76, 78, 80]
  "§9.4.2#r26": [94, 96, 98, 100]
  "§9.4.2#r32": [106, 108, 110]
  "§9.4.4#r15": [68, 74]
  "§9.4.4#r14": [94, 96, 100]
  "§9.4.4#r29": [106, 108, 110]
  "§9.4.1#r1": [94, 102]
  "§9.4.1#r2": [106, 110]
  "§9.4.1#r4": [6, 80]
  "EB-AKS-7": [94, 98, 100]
  "EB-AKS-3@report-damaged": 24
  "EB-AKS-3@confirm": [10, 26]
  "EB-AKS-3@reject": 28
  "EB-AKS-3@cancel-report": [44, 134, 136]
  "EB-AKS-3@mark-as-repaired": [14, 30, 64, 148]
  "EB-AKS-3@cancel-disposal-report": [46, 112, 114, 138, 140, 142, 144]
  "§2.1#r1": [2, 4, 16, 18, 22]
  "§2.1#r2": [24, 54, 154]
  "§2.1#r3": [54, 56]
  "§2.1#r4": [10, 26, 28, 146]
  "§2.1#r5": [44, 134, 136]
  "§2.1#r6": [12, 30, 148]
  "§2.1#r7": [32, 150]
  "§2.1#r8": [34, 36, 152]
  "§2.1#r9": [46, 48, 50, 52, 112, 114, 138, 140, 142, 144]
  "§2.1#r10": [38, 40]
  "§2.1#r11": [2, 4, 6, 8, 18, 22]
---

# Server menegakkan hak per role dan cakupan Group, menolak aksi tulis tanpa capability, menolak Damage Log di luar cakupan dengan 403, membatasi nilai finansial, dan memblokir aksi tulis pada entitas Suspended/Expired atau plan Disposal None

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`.
  - Group Manager `Gunawan Hartono {runId}`, binaan Group `Head Office {runId}` beserta sub-group.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, juga Read pada Group `Warehouse {runId}`.
  - Read Only `Rosa Maharani {runId}`; pemegang Manage asset & TAG (Read) `Reza Pratama {runId}`; pemegang View asset value `Vina Kusuma {runId}`.
  - Pelapor umum `Budi Santoso {runId}` tanpa role Damaged; pengguna tanpa akses modul `Nani Setiawan {runId}`.
  - Aktor transaksi peminjaman `Yoga Tanuwijaya {runId}` dan pemilik sesi opname `Sinta Marlina {runId}`, tanpa hak Update Manage asset & TAG.
  - Aktor penugasan `Dewi Anggraini {runId}` dan Aktor pemindahan aset `Tono Riyadi {runId}`, tanpa hak Update dan tanpa Read Only.
  - Aktor dari entitas lain yang sudah Suspended, Expired, atau ber-level Feature Suite Disposal `None`, masing-masing ber-role Total Control di entitasnya.
- Data:
  - DU-205-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-205-2: User `Gunawan Hartono {runId}`, Group Manager, cakupan Group `Head Office {runId}` beserta sub-group.
  - DU-205-3: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), cakupan Update pada Group `Head Office {runId}` beserta descendant, Read pada Group `Warehouse {runId}`.
  - DU-205-4: User `Rosa Maharani {runId}`, Read Only, cakupan seluruh client.
  - DU-205-5: User `Reza Pratama {runId}`, Manage asset & TAG (Read), cakupan Read pada Group `Head Office {runId}` beserta descendant.
  - DU-205-6: User `Vina Kusuma {runId}`, View asset value, cakupan Group `Warehouse {runId}` beserta descendant.
  - DU-205-7: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-205-8: User `Nani Setiawan {runId}`, Manage accounting tanpa Manage asset & TAG maupun Read Only, cakupan tanpa akses modul.
  - DU-205-9: User `Tari Aminah {runId}`, Read Only dan Manage accounting, cakupan seluruh client.
  - DU-205-10: User `Cici Rahayu {runId}`, Manage asset & TAG dengan Create dan Delete tanpa Update, cakupan Group `Head Office {runId}` beserta descendant.
  - DU-205-11: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-205-12: User `Sinta Marlina {runId}`, pemilik sesi opname, cakupan Group `Head Office {runId}`.
  - DU-205-13: User `Maya Puspita {runId}`, Manage asset & TAG (Update) dan Asset Admin sub-tab Disposal, cakupan Group `Head Office {runId}` beserta descendant.
  - DU-205-14: User `Anton Wijaya {runId}`, Total Control di entitas `Mitra Suspended {runId}` yang berstatus Suspended, cakupan entitas `Mitra Suspended {runId}`.
  - DU-205-15: User `Erika Hasan {runId}`, Total Control di entitas `Mitra Expired {runId}` yang berstatus Expired, cakupan entitas `Mitra Expired {runId}`.
  - DU-205-16: User `Dian Susanto {runId}`, Total Control di entitas `Mitra Tanpa Disposal {runId}` ber-level Feature Suite Disposal `None`, cakupan entitas `Mitra Tanpa Disposal {runId}`.
  - DU-205-17: User `Dedi Kurniawan {runId}`, pelapor umum, pemindai TAG, cakupan aset yang ia pindai.
  - DU-205-18: Entitas `Mitra Lain {runId}`, Active, terpisah dari entitas suite.
  - DU-205-19: Entitas `Mitra Suspended {runId}`, berstatus Suspended.
  - DU-205-20: Entitas `Mitra Expired {runId}`, berstatus Expired.
  - DU-205-21: Entitas `Mitra Tanpa Disposal {runId}`, level Feature Suite Disposal `None`.
  - DU-205-22: Group `Head Office {runId}`.
  - DU-205-23: Group `Finance Division {runId}`, sub-group dari `Head Office {runId}`.
  - DU-205-24: Group `Warehouse {runId}`.
  - DU-205-25: Aset `Laptop Dell Latitude 5420 - 31 {runId}`, Group `Head Office {runId}`, record `Damaged`.
  - DU-205-26: Aset `Printer HP LaserJet M404 - 32 {runId}`, Group `Finance Division {runId}`, record `Damaged`.
  - DU-205-27: Aset `Drill Bosch GSB - 33 {runId}`, Group `Warehouse {runId}`, record `Damaged`.
  - DU-205-28: Aset `Monitor Dell P2422H - 34 {runId}`, Group `Head Office {runId}`, record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-205-29: Aset `Camera Canon EOS - 35 {runId}`, Group `Head Office {runId}`, record `Reported Disposal` yang dilaporkan `Maya Puspita {runId}`.
  - DU-205-30: Aset `Tablet Samsung Tab A8 - 36 {runId}`, Group `Head Office {runId}`, record `Reported Disposal` yang dilaporkan `Agus Pratama {runId}`.
  - DU-205-31: Aset `Projector Epson EB-X06 - 37 {runId}`, Group `Head Office {runId}`, record `Damaged` dengan penanda `Missing`.
  - DU-205-32: Aset `Scanner Fujitsu fi-7160 - 38 {runId}`, Group `Head Office {runId}`, record `Damaged` dari laporan `Yoga Tanuwijaya {runId}`.
  - DU-205-33: Aset `Forklift Toyota 8FD - 39 {runId}`, Group `Head Office {runId}`, record `Damaged` dari laporan `Sinta Marlina {runId}`.
  - DU-205-34: Aset `Office Chair Ergo - 40 {runId}`, Group `Head Office {runId}`, record `Rejected` dari laporan `Budi Santoso {runId}` dengan Reason `Foto tidak jelas {runId}`, Damaged Photo `kursi-patah.jpg`, diputuskan `Rina Wulandari {runId}`.
  - DU-205-35: Aset `Handheld Scanner Zebra TC21 - 41 {runId}`, Group `Head Office {runId}`, record `Waiting for Confirmation` dari laporan `Dedi Kurniawan {runId}`.
  - DU-205-36: Aset `Toyota Avanza - 42 {runId}`, Group `Warehouse {runId}`, record `Damaged`.
  - DU-205-37: Aset `Laptop Dell Latitude 5420 - 43 {runId}`, Group `Head Office {runId}`, record tanpa record berjalan, dipegang `Rosa Maharani {runId}`.
  - DU-205-38: Aset `Laptop Dell Latitude 5420 - 44 {runId}`, Group `Warehouse {runId}`, record tanpa record berjalan, dipegang `Gunawan Hartono {runId}`.
  - DU-205-39: Aset `Laptop Dell Latitude 5420 - 52 {runId}`, Group `Head Office {runId}`, record tanpa record berjalan, `Borrowed` oleh `Budi Santoso {runId}`.
  - DU-205-40: Aset `Monitor Dell P2422H - 53 {runId}`, Group `Head Office {runId}`, record `Reported Disposal` yang dilaporkan `Maya Puspita {runId}`.
  - DU-205-41: Aset `Printer HP LaserJet M404 - 45 {runId}`, Group `Mitra Lain {runId}`, record `Damaged` milik entitas lain `Mitra Lain {runId}`.
  - DU-205-42: Aset `Monitor Dell P2422H - 46 {runId}`, Group `Mitra Suspended {runId}`, record `Damaged` di entitas `Mitra Suspended {runId}`.
  - DU-205-43: Aset `Camera Canon EOS - 47 {runId}`, Group `Mitra Suspended {runId}`, record `In Disposal Process` dengan baris Disposal yang kedaluwarsa oleh `System`.
  - DU-205-44: Aset `Scanner Fujitsu fi-7160 - 48 {runId}`, Group `Mitra Expired {runId}`, record `Damaged` di entitas `Mitra Expired {runId}`.
  - DU-205-45: Aset `Drill Bosch GSB - 49 {runId}`, Group `Mitra Tanpa Disposal {runId}`, record `Damaged` di entitas `Mitra Tanpa Disposal {runId}`.
  - DU-205-46: Aset `Forklift Toyota 8FD - 50 {runId}`, Group `Mitra Tanpa Disposal {runId}`, record `Reported Disposal` di entitas `Mitra Tanpa Disposal {runId}`.
  - DU-205-47: Aset `Tablet Samsung Tab A8 - 51 {runId}`, Group `Mitra Tanpa Disposal {runId}`, record `Normal`, tanpa record berjalan.
  - DU-205-48: Id record `00000000-0000-0000-0000-000000000000`, tidak ada di entitas mana pun.
  - DU-205-49: Permintaan Report Damaged `tanpa token`.
  - DU-205-50: What happened `Casing retak setelah terbentur {runId}`, Damaged Photo `casing-retak.jpg`.
  - DU-205-51: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-205-52: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-205-53: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`, tanpa Update dan tanpa Read Only.
  - DU-205-54: User `Tono Riyadi {runId}`, Aktor Transfer, cakupan Group `Head Office {runId}`, tanpa Update dan tanpa Read Only.
  - DU-205-55: Aset `Monitor Dell P2422H - 54 {runId}`, Group `Head Office {runId}`, record `Reported Disposal` yang dilaporkan `Agus Pratama {runId}`.
  - DU-205-56: Aset `Drill Bosch GSB - 55 {runId}`, Group `Warehouse {runId}`, record `Reported Disposal` yang dilaporkan `Agus Pratama {runId}`.
  - DU-205-57: Aset `Handheld Scanner Zebra TC21 - 56 {runId}`, Group `Head Office {runId}`, record `Damaged` dari laporan `Dewi Anggraini {runId}`.
  - DU-205-58: Aset `Forklift Toyota 8FD - 57 {runId}`, Group `Head Office {runId}`, record `Damaged` dari laporan `Tono Riyadi {runId}`.
  - DU-205-59: Aset `Toyota Avanza - 59 {runId}`, Group `Warehouse {runId}`, record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-205-60: Aset `Printer HP LaserJet M404 - 58 {runId}`, Group `Warehouse {runId}`, tanpa record berjalan.
  - DU-205-61: Aset `Camera Canon EOS - 61 {runId}`, Group `Mitra Suspended {runId}`, tanpa record berjalan di entitas `Mitra Suspended {runId}`.

## Test Steps

### Hak baca dan cakupan Group per role
1. Total Control `Agus Pratama {runId}` membaca daftar record Active
2. Verifikasi `Laptop Dell Latitude 5420 - 31 {runId}`, `Printer HP LaserJet M404 - 32 {runId}`, dan `Drill Bosch GSB - 33 {runId}` ikut terkembalikan karena cakupannya seluruh client
3. Group Manager `Gunawan Hartono {runId}` membaca daftar record Active
4. Verifikasi `Laptop Dell Latitude 5420 - 31 {runId}` di Group binaan dan `Printer HP LaserJet M404 - 32 {runId}` di sub-group ikut terkembalikan, sedangkan `Drill Bosch GSB - 33 {runId}` di Group `Warehouse {runId}` tidak
5. Pemegang View asset value `Vina Kusuma {runId}` membaca daftar record Active
6. Verifikasi `Drill Bosch GSB - 33 {runId}` dan `Toyota Avanza - 42 {runId}` di Group `Warehouse {runId}` terkembalikan, sedangkan record di Group `Head Office {runId}` tidak, sehingga dua aktor yang melihat pohon Group yang sama memperoleh cakupan berbeda
7. Pemegang Update `Rina Wulandari {runId}` membaca daftar record Active
8. Verifikasi record di Group `Head Office {runId}` dan sub-group `Finance Division {runId}` terkembalikan sebagai cakupan Update, dan `Drill Bosch GSB - 33 {runId}` di Group `Warehouse {runId}` terkembalikan hanya sebagai cakupan Read
9. Pemegang Update `Rina Wulandari {runId}` menjalankan Confirm atas laporan `Monitor Dell P2422H - 34 {runId}` di Group `Head Office {runId}`
10. Verifikasi Confirm diterima dan record menjadi `Damaged`, karena cakupan Update berlaku pada Group penugasan
11. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 32 {runId}` di sub-group `Finance Division {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
12. Verifikasi Mark as Repaired diterima dan record menjadi `Repaired`, karena sub-group termasuk descendant Group penugasan
13. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Drill Bosch GSB - 33 {runId}` di Group `Warehouse {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
14. Verifikasi Mark as Repaired ditolak karena aset di luar Group Update dan record tetap `Damaged`
15. Pemegang Read `Reza Pratama {runId}` membaca daftar record Active
16. Verifikasi hanya record di Group `Head Office {runId}` dan descendant yang terkembalikan, dan `Drill Bosch GSB - 33 {runId}` tidak
17. Read Only `Rosa Maharani {runId}` membaca daftar record Active
18. Verifikasi seluruh record client terkembalikan secara read-only
19. Pengguna `Nani Setiawan {runId}`, pemegang Manage accounting tanpa Manage asset & TAG maupun Read Only, membaca daftar record Active
20. Verifikasi permintaan ditolak karena Manage accounting tidak memberi akses modul dan modul tidak digate Global Role
21. Pelapor umum `Budi Santoso {runId}` membaca daftar record Active
22. Verifikasi permintaan ditolak karena pelapor umum hanya memperoleh hak karena memegang atau memindai aset

### Aksi tulis tanpa capability ditolak walau UI dilewati dan data tidak berubah
23. Read Only `Rosa Maharani {runId}` mengirim Report Damaged sebagai Pelapor admin dari Asset List atas `Laptop Dell Latitude 5420 - 43 {runId}` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
24. Verifikasi permintaan ditolak dan tidak ada Damage record untuk aset itu
25. Pemegang Read `Reza Pratama {runId}` menjalankan Confirm atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}`
26. Verifikasi Confirm ditolak dan record tetap `Waiting for Confirmation`
27. Read Only `Rosa Maharani {runId}` menjalankan Reject atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
28. Verifikasi Reject ditolak dan record tetap `Waiting for Confirmation`
29. Pemegang Manage asset & TAG `Cici Rahayu {runId}` yang hanya memegang Create dan Delete menjalankan Mark as Repaired atas `Scanner Fujitsu fi-7160 - 38 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
30. Verifikasi Mark as Repaired ditolak karena Create dan Delete tidak berlaku dan seluruh aksi tulis memakai Update, dan record tetap `Damaged`
31. Pemegang Read `Reza Pratama {runId}` menjalankan Report Missing atas `Laptop Dell Latitude 5420 - 31 {runId}` yang berstatus `Damaged` tanpa penanda `Missing`
32. Verifikasi permintaan ditolak karena tidak memegang Update dan record tetap `Damaged`
33. Read Only `Rosa Maharani {runId}` menjalankan Report Disposal atas `Scanner Fujitsu fi-7160 - 38 {runId}`
34. Verifikasi Report Disposal ditolak dan record tetap `Damaged`
35. Read Only `Rosa Maharani {runId}` mengirim Bulk Report Disposal atas `Scanner Fujitsu fi-7160 - 38 {runId}` dan `Forklift Toyota 8FD - 39 {runId}`
36. Verifikasi Bulk Report Disposal ditolak dan kedua record tetap `Damaged`
37. Pelapor umum `Budi Santoso {runId}` mengunduh Download atas record Active
38. Verifikasi permintaan Download pelapor umum ditolak
39. Read Only `Rosa Maharani {runId}` mengunduh Download atas record Active
40. Verifikasi permintaan Download diterima dan berkas terkirim
41. Permintaan Report Damaged atas `Laptop Dell Latitude 5420 - 43 {runId}` dikirim tanpa token
42. Verifikasi permintaan ditolak karena tanpa sesi dan tidak ada Damage record untuk aset itu

### Cancel Report hanya milik pelapor, dan Cancel Disposal Report menurut hak Disposal
43. Read Only `Rosa Maharani {runId}` menjalankan Cancel Report atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` milik `Dedi Kurniawan {runId}` yang masih `Waiting for Confirmation`
44. Verifikasi Cancel Report ditolak karena bukan laporannya sendiri dan record tetap `Waiting for Confirmation`
45. Pemegang Update `Rina Wulandari {runId}` menjalankan Cancel Disposal Report atas `Tablet Samsung Tab A8 - 36 {runId}`
46. Verifikasi Cancel Disposal Report ditolak karena tidak memegang Asset Admin sub-tab pelepasan aset dan record tetap `Reported Disposal`
47. Group Manager `Gunawan Hartono {runId}` menjalankan Cancel Disposal Report atas `Tablet Samsung Tab A8 - 36 {runId}` di Group binaan
48. Verifikasi Cancel Disposal Report diterima dan record kembali `Damaged`
49. Pemegang `Maya Puspita {runId}` yang juga Asset Admin sub-tab pelepasan aset menjalankan Cancel Disposal Report atas `Camera Canon EOS - 35 {runId}` yang ia laporkan sendiri
50. Verifikasi Cancel Disposal Report atas laporan miliknya diterima dan record kembali `Damaged`
51. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 53 {runId}` yang dilaporkan `Maya Puspita {runId}`
52. Verifikasi Cancel Disposal Report oleh Total Control atas semua laporan diterima

### Pelapor umum dan aktor transaksi: hak dan akses Damage Log
53. Group Manager `Gunawan Hartono {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 44 {runId}` di Group `Warehouse {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
54. Verifikasi server membuat record `Waiting for Confirmation` karena aset di luar Group binaan, sehingga Group Manager bertindak sebagai pelapor umum
55. Read Only `Rosa Maharani {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 43 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
56. Verifikasi server membuat record `Waiting for Confirmation` karena Read Only dapat melapor sebagai pelapor umum
57. Pelapor umum `Budi Santoso {runId}` membuka Damage Log record `Office Chair Ergo - 40 {runId}` yang ia laporkan dan sudah `Rejected`
58. Verifikasi Damage Log terkirim lengkap dengan Reason `Foto tidak jelas {runId}`, Damaged Photo `kursi-patah.jpg`, dan nama admin yang memutuskan, tanpa kolom nilai finansial
59. Pelapor umum `Budi Santoso {runId}` membuka Damage Log record `Handheld Scanner Zebra TC21 - 41 {runId}` milik laporan orang lain
60. Verifikasi permintaan ditolak dengan `403`
61. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 52 {runId}` dari halaman transaksi peminjaman tanpa hak Update dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
62. Verifikasi server menerima dan membuat record `Damaged`, karena hak melapor dari halaman transaksi mengikuti hak aksi transaksi, bukan hak Update
63. Aktor peminjaman `Yoga Tanuwijaya {runId}` menjalankan Mark as Repaired atas `Scanner Fujitsu fi-7160 - 38 {runId}` yang ia laporkan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
64. Verifikasi Mark as Repaired ditolak karena Aktor peminjaman tidak memegang Update pada Group aset dan record tetap `Damaged`
65. Aktor peminjaman `Yoga Tanuwijaya {runId}` membuka Damage Log record `Scanner Fujitsu fi-7160 - 38 {runId}` yang ia laporkan
66. Verifikasi Damage Log terkirim karena record itu laporannya sendiri
67. Aktor peminjaman `Yoga Tanuwijaya {runId}` membuka Damage Log record `Printer HP LaserJet M404 - 32 {runId}` yang bukan laporannya
68. Verifikasi permintaan ditolak dengan `403`
69. Pemilik sesi opname `Sinta Marlina {runId}` membuka Damage Log record `Forklift Toyota 8FD - 39 {runId}` yang ia laporkan dari sesinya
70. Verifikasi Damage Log terkirim karena record itu laporannya sendiri tanpa hak aksi lain
71. Pemilik sesi opname `Sinta Marlina {runId}` menjalankan Report Missing atas `Forklift Toyota 8FD - 39 {runId}`
72. Verifikasi permintaan ditolak karena tidak memegang Update pada Group aset

### Damage Log di luar cakupan atau tanpa hak baca ditolak dengan 403 tanpa mengubah log
73. Pemegang Read `Reza Pratama {runId}` membuka Damage Log record `Drill Bosch GSB - 33 {runId}` di Group `Warehouse {runId}`
74. Verifikasi permintaan ditolak dengan `403` dan tidak ada entri log baru
75. Pengguna `Nani Setiawan {runId}` tanpa akses modul membuka Damage Log record `Laptop Dell Latitude 5420 - 31 {runId}`
76. Verifikasi permintaan ditolak dengan `403`
77. Total Control `Agus Pratama {runId}` membuka Damage Log record dengan id `00000000-0000-0000-0000-000000000000`
78. Verifikasi permintaan ditolak karena record tidak ada
79. Total Control `Agus Pratama {runId}` membuka Damage Log record `Printer HP LaserJet M404 - 45 {runId}` milik entitas `Mitra Lain {runId}`
80. Verifikasi permintaan ditolak dan tidak ada data entitas lain yang terkirim
81. Group Manager `Gunawan Hartono {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 37 {runId}` yang berpenanda `Missing` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
82. Verifikasi Mark as Repaired ditolak oleh server karena record berpenanda `Missing`, walau aksinya disembunyikan di UI

### Nilai finansial hanya bagi yang berhak
83. Total Control `Agus Pratama {runId}` membaca record `Laptop Dell Latitude 5420 - 31 {runId}`
84. Verifikasi Purchase Cost `12500000`, Asset Value (Commercial) `10000000`, dan Asset Value (Fiscal) `9000000` ikut terkirim
85. Pemegang `Tari Aminah {runId}` yang Read Only dan Manage accounting membaca record `Laptop Dell Latitude 5420 - 31 {runId}`
86. Verifikasi kolom nilai finansial ikut terkirim karena Manage accounting berlaku di seluruh client
87. Read Only `Rosa Maharani {runId}` membaca record `Laptop Dell Latitude 5420 - 31 {runId}`
88. Verifikasi Purchase Cost, Asset Value (Commercial), dan Asset Value (Fiscal) tidak ikut terkirim sama sekali
89. Pemegang Read `Reza Pratama {runId}` membaca record `Laptop Dell Latitude 5420 - 31 {runId}`
90. Verifikasi nilai finansial tidak ikut terkirim
91. Pemegang View asset value `Vina Kusuma {runId}` membaca record `Drill Bosch GSB - 33 {runId}`
92. Verifikasi Purchase Cost `4500000`, Asset Value (Commercial) `3500000`, dan Asset Value (Fiscal) `3000000` ikut terkirim karena aset berada di Group assign

### Entitas Suspended atau Expired menolak aksi tulis, aksi sistem tetap berjalan
93. Total Control `Anton Wijaya {runId}` dari entitas `Mitra Suspended {runId}` yang Suspended mengirim Report Damaged atas aset `Camera Canon EOS - 61 {runId}` yang tidak punya record berjalan
94. Verifikasi server menolak dengan `403` dan tidak ada record atau node baru
95. Total Control `Anton Wijaya {runId}` menjalankan Mark as Repaired atas record `Monitor Dell P2422H - 46 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
96. Verifikasi server menolak dengan `403` dan record tetap `Damaged`
97. Total Control `Anton Wijaya {runId}` membaca daftar record Active, daftar History, dan Damage Log `Monitor Dell P2422H - 46 {runId}`
98. Verifikasi aksi baca tetap berjalan pada entitas Suspended
99. Total Control `Erika Hasan {runId}` dari entitas `Mitra Expired {runId}` yang Expired menjalankan Mark as Repaired atas `Scanner Fujitsu fi-7160 - 48 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
100. Verifikasi server menolak dengan `403` dan record tetap `Damaged`
101. Baris pelepasan aset `Camera Canon EOS - 47 {runId}` di entitas `Mitra Suspended {runId}` kedaluwarsa oleh `System`
102. Verifikasi record kembali `Damaged` karena aksi sistem tanpa user aktor tidak diblokir

### Level Feature Suite Disposal None menolak aksi Disposal tetapi tidak menggate inti Damaged
103. Total Control `Dian Susanto {runId}` dari entitas `Mitra Tanpa Disposal {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 51 {runId}` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
104. Verifikasi Report Damaged diterima karena inti Damaged tidak plan-gated
105. Total Control `Dian Susanto {runId}` menjalankan Report Disposal atas `Drill Bosch GSB - 49 {runId}`
106. Verifikasi Report Disposal ditolak server dan record tetap `Damaged`
107. Total Control `Dian Susanto {runId}` mengirim Bulk Report Disposal atas `Drill Bosch GSB - 49 {runId}`
108. Verifikasi Bulk Report Disposal ditolak server dan record tetap `Damaged`
109. Total Control `Dian Susanto {runId}` menjalankan Cancel Disposal Report atas `Forklift Toyota 8FD - 50 {runId}`
110. Verifikasi Cancel Disposal Report ditolak server, record tetap `Reported Disposal`, dan tidak ada node Damage Log baru

### Cancel Disposal Report atas laporan orang lain dan di luar Group binaan ditolak
111. Pemegang `Maya Puspita {runId}` yang juga Asset Admin sub-tab pelepasan aset menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}` yang dilaporkan `Agus Pratama {runId}`
112. Verifikasi Cancel Disposal Report ditolak karena bukan laporan miliknya dan record tetap `Reported Disposal`
113. Group Manager `Gunawan Hartono {runId}` menjalankan Cancel Disposal Report atas `Drill Bosch GSB - 55 {runId}` di Group `Warehouse {runId}` yang di luar Group binaan
114. Verifikasi Cancel Disposal Report ditolak karena di luar Group binaan dan record tetap `Reported Disposal`

### Pelapor umum murni tidak dapat menjalankan aksi Aktor Damaged
115. Pelapor umum `Budi Santoso {runId}` menjalankan Confirm atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}`
116. Verifikasi Confirm ditolak dan record tetap `Waiting for Confirmation`
117. Pelapor umum `Budi Santoso {runId}` menjalankan Reject atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
118. Verifikasi Reject ditolak dan record tetap `Waiting for Confirmation`
119. Pelapor umum `Budi Santoso {runId}` menjalankan Mark as Repaired atas `Scanner Fujitsu fi-7160 - 38 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
120. Verifikasi Mark as Repaired ditolak dan record tetap `Damaged`
121. Pelapor umum `Budi Santoso {runId}` menjalankan Report Missing atas `Scanner Fujitsu fi-7160 - 38 {runId}`
122. Verifikasi Report Missing ditolak dan record tidak berubah
123. Pelapor umum `Budi Santoso {runId}` menjalankan Report Disposal atas `Scanner Fujitsu fi-7160 - 38 {runId}`
124. Verifikasi Report Disposal ditolak dan record tetap `Damaged`

### Aktor penugasan dan Aktor pemindahan tanpa Update hanya membuka Damage Log laporannya sendiri
125. Aktor penugasan `Dewi Anggraini {runId}` membuka Damage Log record `Handheld Scanner Zebra TC21 - 56 {runId}` yang ia laporkan
126. Verifikasi Damage Log terkirim karena record itu laporannya sendiri tanpa hak Update maupun Read Only
127. Aktor penugasan `Dewi Anggraini {runId}` membuka Damage Log record `Laptop Dell Latitude 5420 - 31 {runId}` yang bukan laporannya
128. Verifikasi permintaan ditolak dengan `403`
129. Aktor pemindahan aset `Tono Riyadi {runId}` membuka Damage Log record `Forklift Toyota 8FD - 57 {runId}` yang ia laporkan
130. Verifikasi Damage Log terkirim karena record itu laporannya sendiri tanpa hak Update maupun Read Only
131. Aktor pemindahan aset `Tono Riyadi {runId}` membuka Damage Log record `Laptop Dell Latitude 5420 - 31 {runId}` yang bukan laporannya
132. Verifikasi permintaan ditolak dengan `403`

### Cancel Report atas laporan orang lain ditolak walau pelakunya berhak tulis
133. Pemegang Update `Rina Wulandari {runId}` menjalankan Cancel Report atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` milik `Dedi Kurniawan {runId}` yang masih `Waiting for Confirmation`
134. Verifikasi Cancel Report ditolak karena bukan laporannya sendiri dan record tetap `Waiting for Confirmation`
135. Pelapor umum `Budi Santoso {runId}` menjalankan Cancel Report atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` milik `Dedi Kurniawan {runId}` yang masih `Waiting for Confirmation`
136. Verifikasi Cancel Report ditolak karena bukan laporannya sendiri dan record tetap `Waiting for Confirmation`

### Cancel Disposal Report ditolak bagi Read Only, Manage asset & TAG (Read), View asset value, dan pelapor umum
137. Read Only `Rosa Maharani {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}`
138. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`
139. Pemegang Read `Reza Pratama {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}`
140. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`
141. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Cancel Disposal Report atas `Drill Bosch GSB - 55 {runId}` di Group `Warehouse {runId}`
142. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`
143. Pelapor umum `Budi Santoso {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}`
144. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`

### Pemegang View asset value tidak dapat menjalankan aksi tulis apa pun
145. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Confirm atas laporan `Toyota Avanza - 59 {runId}` di Group `Warehouse {runId}`
146. Verifikasi Confirm ditolak dan record tetap `Waiting for Confirmation`
147. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Mark as Repaired atas `Drill Bosch GSB - 33 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
148. Verifikasi Mark as Repaired ditolak dan record tetap `Damaged`
149. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Report Missing atas `Toyota Avanza - 42 {runId}`
150. Verifikasi Report Missing ditolak dan record tetap `Damaged`
151. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Report Disposal atas `Toyota Avanza - 42 {runId}`
152. Verifikasi Report Disposal ditolak dan record tetap `Damaged`
153. Pemegang View asset value `Vina Kusuma {runId}` mengirim Report Damaged sebagai Pelapor admin dari Asset List atas `Printer HP LaserJet M404 - 58 {runId}` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
154. Verifikasi permintaan ditolak dan tidak ada Damage record untuk aset itu
