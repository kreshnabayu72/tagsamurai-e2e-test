---
id: TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi
title: "Server menegakkan hak per role dan cakupan Group, menolak aksi tulis tanpa capability, menolak Damage Log di luar cakupan dengan 403, membatasi nilai finansial, dan memblokir aksi tulis pada entitas Suspended/Expired atau plan Disposal None"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§2#b1", "§2#b2", "§2#b3", "§2#b5", "§2.1#b2", "§2.1#b6", "§2.1#b7", "§2.1#b9", "§9.3#b1", "§9.3#b2", "§9.11#r1", "§9.11#r2", "§9.11#b1", S-DMG-17, "§4.2.2#p2", "§9.10#p1", S-DMG-09, EC-DMG-22, EC-DMG-30, EC-DMG-36, "§9.4.4#r16", "§9.4.4#r15", "§9.4.4#r31", "§9.4.1#r1", "§9.4.1#r2", "§9.4.1#r4", EB-AKS-7, EB-AKS-3@report-damaged, EB-AKS-3@confirm, EB-AKS-3@reject, EB-AKS-3@cancel-report, EB-AKS-3@mark-as-repaired, EB-AKS-3@cancel-disposal-report, "§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#b4", "§2.1#b5", "§4.8#r8", "§4.8#r9", "§4.8#r12", "§4.8#r13", "§9.4.3#b6"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§2#b1": [20, 86]
  "§2#b2": [8, 12]
  "§2#b3": [10, 30]
  "§2#b5": 2
  "§2.1#b2": [62, 64, 66, 70, 72, 131, 133, 135, 137, 161, 163, 165, 167, 171]
  "§2.1#b6": [46, 48, 50, 117, 119]
  "§2.1#b7": [6, 20, 40, 151, 153, 155, 157, 159]
  "§2.1#b9": [8, 10, 14]
  "§9.3#b1": [62, 64, 121, 123, 125, 127, 129, 139, 141, 167, 169]
  "§9.3#b2": [14, 42, 74, 82]
  "§9.11#r1": [58, 66, 70, 167, 169]
  "§9.11#r2": [84, 86, 88, 92]
  "§9.11#b1": [84, 88, 90]
  S-DMG-17: [14, 58, 60, 74]
  "§4.2.2#p2": [58, 60]
  "§9.10#p1": [104, 106]
  S-DMG-09: [88, 90, 92]
  EC-DMG-22: [60, 66, 68, 70, 74, 76, 78, 80, 167, 169]
  EC-DMG-30: [94, 96, 98, 100]
  EC-DMG-36: [106, 110, 114]
  "§9.4.4#r16": [68, 74]
  "§9.4.4#r15": [94, 96, 100]
  "§9.4.4#r31": [106, 107, 108, 110, 111, 112, 114, 115]
  "§9.4.1#r1": [94, 102]
  "§9.4.1#r2": [106, 114]
  "§9.4.1#r4": [6, 80]
  EB-AKS-7: [94, 98, 100]
  EB-AKS-3@report-damaged: 24
  EB-AKS-3@confirm: [10, 26]
  EB-AKS-3@reject: 28
  EB-AKS-3@cancel-report: [44, 139, 141]
  EB-AKS-3@mark-as-repaired: [14, 30, 64, 153]
  EB-AKS-3@cancel-disposal-report: [46, 117, 119, 143, 145, 147, 149]
  "§2.1#r1": [2, 4, 16, 18, 22]
  "§2.1#r2": [24, 54, 159]
  "§2.1#r3": [54, 56]
  "§2.1#r4": [10, 26, 28, 151]
  "§2.1#r5": [44, 139, 141, 173, 175, 177, 179, 181, 183, 185, 187]
  "§2.1#r6": [12, 30, 153]
  "§2.1#r7": [32, 155]
  "§2.1#r8": [34, 36, 157]
  "§2.1#r9": [46, 48, 50, 52, 117, 119, 143, 145, 147, 149]
  "§2.1#r10": [38, 40]
  "§2.1#r11": [2, 4, 6, 8, 18, 22]
  "§2.1#b4": [173, 175, 177, 179]
  "§2.1#b5": [181, 183, 185, 187]
  "§4.8#r8": [173, 175, 177, 179]
  "§4.8#r9": [181, 183, 185, 187]
  "§4.8#r12": [84, 86, 88, 90, 92]
  "§4.8#r13": [38, 40]
  "§9.4.3#b6": [189, 191, 193]
---

# Server menegakkan hak per role dan cakupan Group, menolak aksi tulis tanpa capability, menolak Damage Log di luar cakupan dengan 403, membatasi nilai finansial, dan memblokir aksi tulis pada entitas Suspended/Expired atau plan Disposal None

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`.
  - Group Manager `Gunawan Hartono {runId}`, binaan Group `Head Office {runId}` beserta sub-group.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, juga Read pada Group `Warehouse {runId}`.
  - Read Only `Rosa Maharani {runId}`; pemegang Manage asset & TAG (Read) `Reza Pratama {runId}`; pemegang View asset value `Vina Kusuma {runId}`.
  - Pelapor umum `Budi Santoso {runId}` tanpa role Damaged; pengguna tanpa akses modul `Nani Setiawan {runId}`.
  - Aktor transaksi peminjaman `Yoga Tanuwijaya {runId}`, Staff Auditor `Sinta Marlina {runId}` (pelapor dari Task Detail Audit), dan Staff Executor Maintenance Routine `Joko Prasetyo {runId}` (pelapor dari Task Maintenance), tanpa hak Update Manage asset & TAG dan tanpa hak Aktor Damaged.
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
  - DU-205-12: User `Sinta Marlina {runId}`, Staff Auditor, pelapor dari Task Detail Audit, tanpa hak Update dan tanpa hak Aktor Damaged, cakupan Group `Head Office {runId}`.
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
  - DU-205-32: Aset `Scanner Fujitsu fi-7160 - 38 {runId}`, Group `Head Office {runId}`, record `Damaged` dari laporan `Yoga Tanuwijaya {runId}` yang sudah di-Confirm Aktor Damaged.
  - DU-205-33: Aset `Forklift Toyota 8FD - 39 {runId}`, Group `Head Office {runId}`, record `Damaged` dari laporan `Agus Pratama {runId}` lewat Task Detail Audit.
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
  - DU-205-63: User `Joko Prasetyo {runId}`, Staff Executor Maintenance Routine, pelapor dari Task Maintenance, tanpa hak Update dan tanpa hak Aktor Damaged, cakupan Group `Head Office {runId}`.
  - DU-205-64: Aset `Rack Server Dell R740 - 54 {runId}`, Group `Head Office {runId}`, record `Waiting for Confirmation` Source `Audit` dari laporan `Sinta Marlina {runId}` lewat Task Detail Audit.
  - DU-205-65: Aset `Rack Server Dell R740 - 55 {runId}`, Group `Head Office {runId}`, record `Damaged` Source `Audit` dari laporan `Rina Wulandari {runId}` lewat Task Detail Audit.
  - DU-205-66: Aset `Rack Server Dell R740 - 58 {runId}`, Group `Head Office {runId}`, Condition `Normal`, item sesi Audit berjalan milik `Sinta Marlina {runId}`, tanpa record berjalan.
  - DU-205-67: Aset `Generator Honda EU22i - 56 {runId}`, Group `Head Office {runId}`, record `Waiting for Confirmation` Source `Maintenance` dari laporan `Joko Prasetyo {runId}` lewat Task Maintenance.
  - DU-205-68: Aset `Generator Honda EU22i - 57 {runId}`, Group `Head Office {runId}`, TAG milik aset, record `Damaged` Source `Maintenance` dari laporan `Rina Wulandari {runId}` lewat Task Maintenance.
  - DU-205-69: Aset `Generator Honda EU22i - 59 {runId}`, Group `Head Office {runId}`, Condition `Normal`, punya Task Maintenance berjalan yang dikerjakan `Joko Prasetyo {runId}`, tanpa record berjalan.
  - DU-205-50: What happened `Casing retak setelah terbentur {runId}`, Damaged Photo `casing-retak.jpg`.
  - DU-205-51: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-205-52: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-205-53: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`, tanpa Update dan tanpa Read Only.
  - DU-205-54: User `Tono Riyadi {runId}`, Aktor Transfer, cakupan Group `Head Office {runId}`, tanpa Update dan tanpa Read Only.
  - DU-205-55: Aset `Monitor Dell P2422H - 54 {runId}`, Group `Head Office {runId}`, record `Reported Disposal` yang dilaporkan `Agus Pratama {runId}`.
  - DU-205-56: Aset `Drill Bosch GSB - 55 {runId}`, Group `Warehouse {runId}`, record `Reported Disposal` yang dilaporkan `Agus Pratama {runId}`.
  - DU-205-57: Aset `Handheld Scanner Zebra TC21 - 56 {runId}`, Group `Head Office {runId}`, record `Waiting for Confirmation` dari laporan `Dewi Anggraini {runId}`.
  - DU-205-58: Aset `Forklift Toyota 8FD - 57 {runId}`, Group `Head Office {runId}`, record `Damaged` dari laporan `Tono Riyadi {runId}`.
  - DU-205-59: Aset `Toyota Avanza - 59 {runId}`, Group `Warehouse {runId}`, record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-205-60: Aset `Printer HP LaserJet M404 - 58 {runId}`, Group `Warehouse {runId}`, tanpa record berjalan.
  - DU-205-61: Aset `Camera Canon EOS - 61 {runId}`, Group `Mitra Suspended {runId}`, tanpa record berjalan di entitas `Mitra Suspended {runId}`.
  - DU-205-62: Aset `Tablet Samsung Tab A8 - 60 {runId}`, Group `Head Office {runId}`, tanpa record berjalan.

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
30. Verifikasi Mark as Repaired ditolak karena Create dan Delete tidak berlaku dan aksi tulis Damaged (Report Damaged, Confirm, Reject, Mark as Repaired, Report Missing) memakai Update, dan record tetap `Damaged`
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
60. Verifikasi permintaan ditolak karena record itu laporan orang lain dan di luar hak lihat `Budi Santoso {runId}`
61. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 52 {runId}` dari halaman transaksi peminjaman tanpa hak Update dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
62. Verifikasi server menerima laporan karena hak melapor dari halaman transaksi mengikuti hak aksi transaksi, bukan hak Update, dan membuat record `Waiting for Confirmation`, bukan `Damaged`, karena Aktor Borrow tanpa hak Aktor Damaged adalah pelapor umum
63. Aktor peminjaman `Yoga Tanuwijaya {runId}` menjalankan Mark as Repaired atas `Scanner Fujitsu fi-7160 - 38 {runId}` yang ia laporkan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
64. Verifikasi Mark as Repaired ditolak karena Aktor peminjaman tidak memegang Update pada Group aset dan record tetap `Damaged`
65. Aktor peminjaman `Yoga Tanuwijaya {runId}` membuka Damage Log record `Scanner Fujitsu fi-7160 - 38 {runId}` yang ia laporkan
66. Verifikasi Damage Log terkirim karena record itu laporannya sendiri
67. Aktor peminjaman `Yoga Tanuwijaya {runId}` membuka Damage Log record `Printer HP LaserJet M404 - 32 {runId}` yang bukan laporannya
68. Verifikasi permintaan ditolak karena record itu bukan laporannya dan di luar hak lihat `Yoga Tanuwijaya {runId}`
69. Staff Auditor `Sinta Marlina {runId}` membuka Damage Log record `Rack Server Dell R740 - 54 {runId}` yang ia laporkan dari Task Detail Audit dan masih `Waiting for Confirmation`
70. Verifikasi Damage Log terkirim karena record itu laporannya sendiri tanpa hak aksi lain
71. Staff Auditor `Sinta Marlina {runId}` menjalankan Report Missing atas `Rack Server Dell R740 - 54 {runId}`
72. Verifikasi permintaan ditolak karena tidak memegang Update pada Group aset

### Damage Log di luar cakupan atau tanpa hak baca ditolak tanpa mengubah log
73. Pemegang Read `Reza Pratama {runId}` membuka Damage Log record `Drill Bosch GSB - 33 {runId}` di Group `Warehouse {runId}`
74. Verifikasi permintaan ditolak karena record di luar cakupan `Reza Pratama {runId}` dan tidak ada entri log baru
75. Pengguna `Nani Setiawan {runId}` tanpa akses modul membuka Damage Log record `Laptop Dell Latitude 5420 - 31 {runId}`
76. Verifikasi permintaan ditolak karena `Nani Setiawan {runId}` tidak punya hak lihat atas modul ini
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
94. Verifikasi server menolak karena entitas Suspended dan tidak ada record atau node baru
95. Total Control `Anton Wijaya {runId}` menjalankan Mark as Repaired atas record `Monitor Dell P2422H - 46 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
96. Verifikasi server menolak karena entitas Suspended dan record tetap `Damaged`
97. Total Control `Anton Wijaya {runId}` membaca daftar record Active, daftar History, dan Damage Log `Monitor Dell P2422H - 46 {runId}`
98. Verifikasi aksi baca tetap berjalan pada entitas Suspended
99. Total Control `Erika Hasan {runId}` dari entitas `Mitra Expired {runId}` yang Expired menjalankan Mark as Repaired atas `Scanner Fujitsu fi-7160 - 48 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
100. Verifikasi server menolak karena entitas Expired dan record tetap `Damaged`
101. Baris pelepasan aset `Camera Canon EOS - 47 {runId}` di entitas `Mitra Suspended {runId}` kedaluwarsa oleh `System`
102. Verifikasi record kembali `Damaged` karena aksi sistem tanpa user aktor tidak diblokir

### Level Feature Suite Disposal None menolak aksi Disposal tetapi tidak menggate inti Damaged
103. Total Control `Dian Susanto {runId}` dari entitas `Mitra Tanpa Disposal {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 51 {runId}` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
104. Verifikasi Report Damaged diterima karena inti Damaged tidak plan-gated
105. Total Control `Dian Susanto {runId}` menjalankan Report Disposal atas `Drill Bosch GSB - 49 {runId}`
106. Verifikasi Report Disposal ditolak server dan record tetap `Damaged`
107. Verifikasi penolakan Report Disposal itu tidak menambah node Damage Log di record
108. Verifikasi penolakan Report Disposal itu tidak memicu event `damaged_*`
109. Total Control `Dian Susanto {runId}` mengirim Bulk Report Disposal atas `Drill Bosch GSB - 49 {runId}`
110. Verifikasi Bulk Report Disposal ditolak server dan record tetap `Damaged`
111. Verifikasi penolakan Bulk Report Disposal itu tidak menambah node Damage Log di record
112. Verifikasi penolakan Bulk Report Disposal itu tidak memicu event `damaged_*`
113. Total Control `Dian Susanto {runId}` menjalankan Cancel Disposal Report atas `Forklift Toyota 8FD - 50 {runId}`
114. Verifikasi Cancel Disposal Report ditolak server, record tetap `Reported Disposal`, dan tidak ada node Damage Log baru
115. Verifikasi penolakan Cancel Disposal Report itu tidak memicu event `damaged_*`

### Cancel Disposal Report atas laporan orang lain dan di luar Group binaan ditolak
116. Pemegang `Maya Puspita {runId}` yang juga Asset Admin sub-tab pelepasan aset menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}` yang dilaporkan `Agus Pratama {runId}`
117. Verifikasi Cancel Disposal Report ditolak karena bukan laporan miliknya dan record tetap `Reported Disposal`
118. Group Manager `Gunawan Hartono {runId}` menjalankan Cancel Disposal Report atas `Drill Bosch GSB - 55 {runId}` di Group `Warehouse {runId}` yang di luar Group binaan
119. Verifikasi Cancel Disposal Report ditolak karena di luar Group binaan dan record tetap `Reported Disposal`

### Pelapor umum murni tidak dapat menjalankan aksi Aktor Damaged
120. Pelapor umum `Budi Santoso {runId}` menjalankan Confirm atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}`
121. Verifikasi Confirm ditolak dan record tetap `Waiting for Confirmation`
122. Pelapor umum `Budi Santoso {runId}` menjalankan Reject atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
123. Verifikasi Reject ditolak dan record tetap `Waiting for Confirmation`
124. Pelapor umum `Budi Santoso {runId}` menjalankan Mark as Repaired atas `Scanner Fujitsu fi-7160 - 38 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
125. Verifikasi Mark as Repaired ditolak dan record tetap `Damaged`
126. Pelapor umum `Budi Santoso {runId}` menjalankan Report Missing atas `Scanner Fujitsu fi-7160 - 38 {runId}`
127. Verifikasi Report Missing ditolak dan record tidak berubah
128. Pelapor umum `Budi Santoso {runId}` menjalankan Report Disposal atas `Scanner Fujitsu fi-7160 - 38 {runId}`
129. Verifikasi Report Disposal ditolak dan record tetap `Damaged`

### Aktor penugasan dan Aktor pemindahan tanpa Update hanya membuka Damage Log laporannya sendiri
130. Aktor penugasan `Dewi Anggraini {runId}` membuka Damage Log record `Handheld Scanner Zebra TC21 - 56 {runId}` yang ia laporkan
131. Verifikasi Damage Log terkirim karena record itu laporannya sendiri tanpa hak Update maupun Read Only
132. Aktor penugasan `Dewi Anggraini {runId}` membuka Damage Log record `Laptop Dell Latitude 5420 - 31 {runId}` yang bukan laporannya
133. Verifikasi permintaan ditolak karena record itu bukan laporannya dan di luar hak lihat `Dewi Anggraini {runId}`
134. Aktor pemindahan aset `Tono Riyadi {runId}` membuka Damage Log record `Forklift Toyota 8FD - 57 {runId}` yang ia laporkan
135. Verifikasi Damage Log terkirim karena record itu laporannya sendiri tanpa hak Update maupun Read Only
136. Aktor pemindahan aset `Tono Riyadi {runId}` membuka Damage Log record `Laptop Dell Latitude 5420 - 31 {runId}` yang bukan laporannya
137. Verifikasi permintaan ditolak karena record itu bukan laporannya dan di luar hak lihat `Tono Riyadi {runId}`

### Cancel Report atas laporan orang lain ditolak walau pelakunya berhak tulis
138. Pemegang Update `Rina Wulandari {runId}` menjalankan Cancel Report atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` milik `Dedi Kurniawan {runId}` yang masih `Waiting for Confirmation`
139. Verifikasi Cancel Report ditolak karena bukan laporannya sendiri dan record tetap `Waiting for Confirmation`
140. Pelapor umum `Budi Santoso {runId}` menjalankan Cancel Report atas laporan `Handheld Scanner Zebra TC21 - 41 {runId}` milik `Dedi Kurniawan {runId}` yang masih `Waiting for Confirmation`
141. Verifikasi Cancel Report ditolak karena bukan laporannya sendiri dan record tetap `Waiting for Confirmation`

### Cancel Disposal Report ditolak bagi Read Only, Manage asset & TAG (Read), View asset value, dan pelapor umum
142. Read Only `Rosa Maharani {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}`
143. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`
144. Pemegang Read `Reza Pratama {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}`
145. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`
146. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Cancel Disposal Report atas `Drill Bosch GSB - 55 {runId}` di Group `Warehouse {runId}`
147. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`
148. Pelapor umum `Budi Santoso {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 54 {runId}`
149. Verifikasi Cancel Disposal Report ditolak dan record tetap `Reported Disposal`

### Pemegang View asset value tidak dapat menjalankan aksi tulis apa pun
150. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Confirm atas laporan `Toyota Avanza - 59 {runId}` di Group `Warehouse {runId}`
151. Verifikasi Confirm ditolak dan record tetap `Waiting for Confirmation`
152. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Mark as Repaired atas `Drill Bosch GSB - 33 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
153. Verifikasi Mark as Repaired ditolak dan record tetap `Damaged`
154. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Report Missing atas `Toyota Avanza - 42 {runId}`
155. Verifikasi Report Missing ditolak dan record tetap `Damaged`
156. Pemegang View asset value `Vina Kusuma {runId}` menjalankan Report Disposal atas `Toyota Avanza - 42 {runId}`
157. Verifikasi Report Disposal ditolak dan record tetap `Damaged`
158. Pemegang View asset value `Vina Kusuma {runId}` mengirim Report Damaged sebagai Pelapor admin dari Asset List atas `Printer HP LaserJet M404 - 58 {runId}` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
159. Verifikasi permintaan ditolak dan tidak ada Damage record untuk aset itu

### Aktor Assignment tanpa hak Aktor Damaged melapor sebagai pelapor umum
160. Aktor penugasan `Dewi Anggraini {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 60 {runId}` dari halaman transaksi penugasan tanpa hak Update dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
161. Verifikasi server menerima laporan dan membuat record `Waiting for Confirmation`, bukan `Damaged`, karena Aktor Assignment tanpa hak Aktor Damaged adalah pelapor umum

### Pelapor dari Task Detail Audit dan Task Maintenance tanpa hak Update: hak melapor mengikuti hak task dan laporan Waiting for Confirmation
162. Staff Auditor `Sinta Marlina {runId}` mengirim Report Damaged atas `Rack Server Dell R740 - 58 {runId}` dari Task Detail Audit tanpa hak Update dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
163. Verifikasi server menerima laporan karena hak melapor dari Task Detail Audit mengikuti hak aksi sesi, bukan hak Update, dan membuat record `Waiting for Confirmation`, bukan `Damaged`, karena Staff Auditor tanpa hak Aktor Damaged adalah pelapor umum
164. Staff Executor `Joko Prasetyo {runId}` mengirim Report Damaged atas `Generator Honda EU22i - 59 {runId}` dari Task Maintenance tanpa hak Update dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
165. Verifikasi server menerima laporan karena hak melapor dari Task Maintenance mengikuti hak aksi task, bukan hak Update, dan membuat record `Waiting for Confirmation`, bukan `Damaged`, karena Staff Executor tanpa hak Aktor Damaged adalah pelapor umum

### Pelapor dari Task Maintenance membuka Damage Log laporannya sendiri, sedangkan laporan orang lain ditolak
166. Staff Executor `Joko Prasetyo {runId}` membuka Damage Log record `Generator Honda EU22i - 56 {runId}` yang ia laporkan dari Task Maintenance dan masih `Waiting for Confirmation`
167. Verifikasi Damage Log terkirim karena record itu laporannya sendiri tanpa hak aksi lain
168. Staff Executor `Joko Prasetyo {runId}` membuka Damage Log record `Printer HP LaserJet M404 - 32 {runId}` yang bukan laporannya
169. Verifikasi permintaan ditolak karena record itu bukan laporannya dan di luar hak lihat `Joko Prasetyo {runId}`
170. Staff Executor `Joko Prasetyo {runId}` menjalankan Mark as Repaired atas `Generator Honda EU22i - 57 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
171. Verifikasi Mark as Repaired ditolak karena Staff Executor tidak memegang Update pada Group aset dan record tetap `Damaged`

### Cancel my report dari Task Detail Audit hanya milik pelapor Source Audit tanpa hak Aktor Damaged
172. Read Only `Rosa Maharani {runId}` menjalankan `Cancel my report` di Task Detail Audit atas laporan `Rack Server Dell R740 - 54 {runId}` milik `Sinta Marlina {runId}`
173. Verifikasi `Cancel my report` ditolak karena bukan laporannya sendiri dan record tetap `Waiting for Confirmation`
174. Total Control `Agus Pratama {runId}` menjalankan `Cancel my report` di Task Detail Audit atas laporan `Rack Server Dell R740 - 54 {runId}` milik `Sinta Marlina {runId}`
175. Verifikasi `Cancel my report` ditolak karena aksi itu hanya milik pelapor dan record tetap `Waiting for Confirmation`
176. Pemegang Update `Rina Wulandari {runId}` menjalankan `Cancel my report` di Task Detail Audit atas laporannya sendiri `Rack Server Dell R740 - 55 {runId}` yang langsung berstatus `Damaged`
177. Verifikasi `Cancel my report` ditolak karena laporan yang langsung `Damaged` tidak memiliki aksi itu dan record tetap `Damaged`
178. Staff Auditor `Sinta Marlina {runId}` menjalankan `Cancel my report` di Task Detail Audit atas laporannya sendiri `Rack Server Dell R740 - 54 {runId}`
179. Verifikasi `Cancel my report` diterima dan record `Rack Server Dell R740 - 54 {runId}` menjadi `Canceled`

### Cancel my report dari Task Maintenance hanya milik pelapor Source Maintenance tanpa hak Aktor Damaged
180. Read Only `Rosa Maharani {runId}` menjalankan `Cancel my report` di Task Maintenance atas laporan `Generator Honda EU22i - 56 {runId}` milik `Joko Prasetyo {runId}`
181. Verifikasi `Cancel my report` ditolak karena bukan laporannya sendiri dan record tetap `Waiting for Confirmation`
182. Total Control `Agus Pratama {runId}` menjalankan `Cancel my report` di Task Maintenance atas laporan `Generator Honda EU22i - 56 {runId}` milik `Joko Prasetyo {runId}`
183. Verifikasi `Cancel my report` ditolak karena aksi itu hanya milik pelapor dan record tetap `Waiting for Confirmation`
184. Pemegang Update `Rina Wulandari {runId}` menjalankan `Cancel my report` di Task Maintenance atas laporannya sendiri `Generator Honda EU22i - 57 {runId}` yang langsung berstatus `Damaged`
185. Verifikasi `Cancel my report` ditolak karena laporan yang langsung `Damaged` tidak memiliki aksi itu dan record tetap `Damaged`
186. Staff Executor `Joko Prasetyo {runId}` menjalankan `Cancel my report` di Task Maintenance atas laporannya sendiri `Generator Honda EU22i - 56 {runId}`
187. Verifikasi `Cancel my report` diterima dan record `Generator Honda EU22i - 56 {runId}` menjadi `Canceled`

### Confirm dan Reject oleh pengguna tanpa hak Aktor Damaged ditolak, termasuk atas laporannya sendiri
188. Staff Auditor `Sinta Marlina {runId}`, pelapor tanpa hak Aktor Damaged pada Group aset, menjalankan Confirm atas laporannya sendiri `Rack Server Dell R740 - 58 {runId}` yang masih `Waiting for Confirmation`
189. Verifikasi Confirm ditolak karena pelapor tidak memegang hak Aktor Damaged pada Group aset dan record tetap `Waiting for Confirmation`
190. Staff Executor `Joko Prasetyo {runId}`, pelapor tanpa hak Aktor Damaged pada Group aset, menjalankan Reject atas laporannya sendiri `Generator Honda EU22i - 59 {runId}` yang masih `Waiting for Confirmation` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
191. Verifikasi Reject ditolak karena pelapor tidak memegang hak Aktor Damaged pada Group aset dan record tetap `Waiting for Confirmation`
192. Pengguna `Nani Setiawan {runId}`, pemegang Manage accounting tanpa hak Aktor Damaged, menjalankan Confirm atas laporan `Rack Server Dell R740 - 58 {runId}`
193. Verifikasi Confirm ditolak karena pengguna tanpa hak Aktor Damaged pada Group aset tidak dapat memutuskan laporan dan record tetap `Waiting for Confirmation`
