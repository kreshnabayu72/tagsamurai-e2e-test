---
id: TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen
title: "Field Reflected ikut berubah saat pemilik berubah, field Snapshot membeku mengikuti node, Days Damaged dan Duration dihitung per zona waktu company, Group record ikut Transfer, pelapor nonaktif tidak mengubah record, dan Group ber-record berjalan tidak dapat dihapus"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.7#p1", "§9.7#b1", "§9.7#b2", "§9.7#b3", "§9.7#r17", V-DMG-11, EC-DMG-19, EC-DMG-20, EC-DMG-29, "§9.4.4#r14", "§9.4.4#r20", "§9.4.1#r13", "§9.4.1#r14", "§9.4.1#r10", T-DMG-01, T-DMG-02, "§9.7#r18"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§9.7#p1": [9, 35, 37, 38, 48, 50, 52, 58]
  "§9.7#b1": [2, 3, 5, 9, 23, 38, 40]
  "§9.7#b2": [11, 12, 14, 24, 56]
  "§9.7#b3": [2, 7, 12, 15, 17, 19, 21, 43, 44]
  "§9.7#r17": [23, 24, 66, 68, 69]
  V-DMG-11: [28, 30]
  EC-DMG-19: 26
  EC-DMG-20: [28, 30]
  EC-DMG-29: [23, 24]
  "§9.4.4#r14": [28, 30]
  "§9.4.4#r20": 26
  "§9.4.1#r13": 26
  "§9.4.1#r14": [28, 30, 64]
  "§9.4.1#r10": 33
  T-DMG-01: [2, 3, 5, 11, 17, 19, 60]
  T-DMG-02: [7, 14, 15, 21, 61]
  "§9.7#r18": [60, 61, 62, 63, 64, 65, 70, 71]
---

# Field Reflected ikut berubah saat pemilik berubah, field Snapshot membeku mengikuti node, Days Damaged dan Duration dihitung per zona waktu company, Group record ikut Transfer, pelapor nonaktif tidak mengubah record, dan Group ber-record berjalan tidak dapat dihapus

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, Aktor Damaged pada Group `Head Office {runId}`.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}` dan Aktor pemindahan aset `Tono Riyadi {runId}`.
  - Pelapor umum `Budi Santoso {runId}` dan `Hana Lestari {runId}`, pemegang aset, tanpa role Damaged.
- Data:
  - DU-210-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-210-2: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), cakupan Group `Head Office {runId}` beserta descendant, yang kemudian dicabut.
  - DU-210-3: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-210-4: User `Tono Riyadi {runId}`, Aktor Transfer, cakupan Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`.
  - DU-210-5: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-210-6: User `Hana Lestari {runId}`, pelapor umum, pemegang aset yang kemudian dinonaktifkan, cakupan aset yang ia pegang.
  - DU-210-7: Time Zone company `Asia/Jakarta`.
  - DU-210-8: Group `Head Office {runId}`.
  - DU-210-9: Group `Branch Surabaya {runId}`.
  - DU-210-10: Group `Divisi Gudang {runId}`, tanpa sub-group, punya record berjalan.
  - DU-210-11: Group `Divisi Pusat {runId}`, punya sub-group `Sub Pusat {runId}` yang punya record berjalan.
  - DU-210-12: Aset `Laptop Lenovo ThinkPad - 201 {runId}`, Group `Head Office {runId}`, punya record `Damaged` Source `Manual` dilaporkan `Agus P`, Last Holder `Budi S`, Asset ID `LPT-0201-{runId}`, Brand `Lenovo {runId}`, Model/Type `ThinkPad X1 {runId}`, Division `Keuangan {runId}`, Purchase Cost `12500000`, Asset Value (Commercial) `10000000`.
  - DU-210-13: Aset `Printer HP LaserJet M404 - 202 {runId}`, Group `Head Office {runId}`, punya record `Repaired` dengan Resolved Date `T0 − 2 hari, pukul 00:30`, Group saat selesai `Head Office {runId}`, Asset Value (Commercial) saat selesai `8000000`, Asset Value (Fiscal) saat selesai `6500000`, Category saat selesai `Elektronik {runId}`, Purchase Cost `3000000`, Alias Name `Printer Lobi {runId}`, Damaged Photo pertama `printer-rusak.jpg`, After photo `sesudah-perbaikan.jpg`.
  - DU-210-14: Aset `Tablet Samsung Tab A8 - 203 {runId}`, Group `Head Office {runId}`, punya record `Damaged` dengan Reported Date `T0, pukul 01:00` zona waktu `Asia/Jakarta`.
  - DU-210-15: Aset `Camera Canon EOS - 204 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dengan Reported Date `T0 − 2 hari, pukul 10:00`.
  - DU-210-16: Aset `Camera Canon EOS - 205 {runId}`, Group `Head Office {runId}`, punya record `Damaged` ditahan penanda `Missing` dengan Reported Date `T0 − 3 hari, pukul 10:00`.
  - DU-210-17: Aset `Forklift Toyota 8FD - 206 {runId}`, Group `Head Office {runId}`, punya record `Damaged` Source `Manual`, dalam pemindahan menuju `Branch Surabaya {runId}`.
  - DU-210-18: Aset `Drill Bosch GSB - 207 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Hana Lestari {runId}`.
  - DU-210-19: Aset `Monitor Dell P2422H - 208 {runId}`, Group `Divisi Gudang {runId}`, punya record `Damaged` di Group `Divisi Gudang {runId}`.
  - DU-210-20: Aset `Monitor Dell P2422H - 209 {runId}`, Group `Sub Pusat {runId}`, punya record `Damaged` di sub-group `Sub Pusat {runId}`.
  - DU-210-21: Aset `Scanner Fujitsu fi-7160 - 210 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-210-22: Aset `Office Chair Ergo - 211 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa record berjalan.
  - DU-210-23: Aset `Projector Epson EB-X06 - 212 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal` yang mencerminkan laporan pelepasan aset.
  - DU-210-24: Konsumen `asset-detail/` dengan surface halaman detail aset.
  - DU-210-25: Konsumen `my-asset/` dengan surface halaman aset yang dipegang pemegang.
  - DU-210-26: Konsumen `borrow/` dengan surface baris peminjaman.
  - DU-210-27: Konsumen `assignment/` dengan surface baris penugasan.
  - DU-210-28: Konsumen `missing/` dengan surface modul aset hilang.
  - DU-210-29: Konsumen `asset-registration/` dengan surface registrasi aset.
  - DU-210-30: Konsumen `audit/` dengan surface sesi Audit.
  - DU-210-31: Konsumen `disposal/` dengan surface laporan pelepasan aset.
  - DU-210-32: Konsumen `transfer/` dengan surface pemindahan aset.
  - DU-210-33: Konsumen `settings-groups/` dengan surface pengelolaan Group.
  - DU-210-34: What happened `Layar retak setelah terjatuh dari meja {runId}`, Damaged Photo `layar-retak.jpg`.
  - DU-210-35: Brand `Lenovo Baru {runId}`, Purchase Cost `13000000`, Asset Value (Commercial) `9500000`.
  - DU-210-36: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-210-37: Aset `Laptop Lenovo ThinkPad - 213 {runId}`, Group `Head Office {runId}`, punya record `Damaged` Source `Manual`, Asset ID `LPT-0213-{runId}`, Model/Type `ThinkPad T14 {runId}`, Division `Operasional {runId}`.
  - DU-210-38: Nilai baru dari pemilik aset: Name `Laptop Lenovo ThinkPad - 213 Baru {runId}`, Asset ID `LPT-0213B-{runId}`, Model/Type `ThinkPad T14s {runId}`, Division `Teknologi {runId}`.
  - DU-210-39: Aset `Laptop Lenovo ThinkPad - 214 {runId}`, Group `Head Office {runId}`, punya record `Damaged` Source `Manual` dengan Damaged Photo pertama `layar-retak.jpg`, TAG `RFID-L214 {runId}`, Labels `Prioritas {runId}`, Asset Class `Laptop {runId}`, Category `Elektronik {runId}`, Alias Name `Laptop Staf {runId}`, Measurement `14 inci`, Register Date `T0 − 400 hari`, Purchase Date `T0 − 420 hari`, Warranty Expiry `T0 + 300 hari`.
  - DU-210-40: Nilai baru dari pemilik aset: TAG `QR-L214 {runId}`, Labels `Garansi {runId}`, Asset Class `Perangkat Kerja {runId}`, Category `Peralatan Kantor {runId}`.
  - DU-210-41: Nilai baru dari pemilik aset: Alias Name `Laptop Direksi {runId}`, Measurement `15 inci`, Register Date `T0 − 380 hari`, Purchase Date `T0 − 400 hari`, Warranty Expiry `T0 + 320 hari`.
  - DU-210-42: Nilai baru dari pemilik aset: Purchase Cost `14000000`.
  - DU-210-43: Nilai baru dari pemilik aset: Alias Name `Printer Lantai Dua {runId}`, Purchase Cost `3500000`.
  - DU-210-44: Aset `Tablet Samsung Tab A8 - 215 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-210-45: Aset `Tablet Samsung Tab A8 - 216 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-210-46: User `Wawan Setiadi {runId}`, Total Control, cakupan seluruh client, yang kemudian diganti namanya menjadi `Wawan Hidayat {runId}`.
  - DU-210-47: User `Dimas Prakoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang, yang kemudian diganti namanya menjadi `Dimas Kusuma {runId}`.
  - DU-210-49: Konsumen `asset-list/` dengan surface daftar aset.
  - DU-210-50: Aset `Laptop Lenovo ThinkPad - 218 {runId}`, Group `Head Office {runId}`, dipegang `Budi Santoso {runId}`, punya record `Waiting for Confirmation` Source `Reported by holder` dari laporan `Budi Santoso {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`.
  - DU-210-48: Aset `Laptop Lenovo ThinkPad - 217 {runId}`, Group `Head Office {runId}`, punya record `Damaged` Source `Manual` dilaporkan `Wawan S`, Last Holder `Dimas P`.
  - DU-210-51: User `Lina Marlina {runId}`, Manage asset & TAG (Update), Aktor Damaged, cakupan hanya Group `Cabang Asal {runId}`.
  - DU-210-52: User `Bayu Santoso {runId}`, Manage asset & TAG (Update), Aktor Damaged, cakupan hanya Group `Cabang Tujuan {runId}`.
  - DU-210-53: User `Wahyu Hidayat {runId}`, Aktor Transfer, cakupan Group `Cabang Asal {runId}` dan Group `Cabang Tujuan {runId}`.
  - DU-210-54: Group `Cabang Asal {runId}`, tanpa sub-group, hanya berisi `Forklift Toyota 8FD - 219 {runId}` dan `Forklift Toyota 8FD - 220 {runId}`.
  - DU-210-55: Group `Cabang Tujuan {runId}`, tanpa sub-group, hanya berisi `Forklift Toyota 8FD - 221 {runId}` sebelum pemindahan diterima.
  - DU-210-56: Aset `Forklift Toyota 8FD - 219 {runId}`, Group `Cabang Asal {runId}`, punya record `Damaged` Source `Manual`, dalam pemindahan menuju `Cabang Tujuan {runId}`.
  - DU-210-57: Aset `Forklift Toyota 8FD - 220 {runId}`, Group `Cabang Asal {runId}`, punya record `Damaged` Source `Manual`.
  - DU-210-58: Aset `Forklift Toyota 8FD - 221 {runId}`, Group `Cabang Tujuan {runId}`, punya record `Damaged` Source `Manual`.
- Kondisi:
  - Time Zone company bernilai `Asia/Jakarta`.
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.

## Test Steps

### Field Reflected ikut berubah saat pemilik berubah
1. Pemilik aset mengubah `Laptop Lenovo ThinkPad - 201 {runId}`: Brand menjadi `Lenovo Baru {runId}`, Purchase Cost menjadi `13000000`, dan Asset Value (Commercial) menjadi `9500000`
2. Verifikasi record Active `Laptop Lenovo ThinkPad - 201 {runId}` menampilkan Brand `Lenovo Baru {runId}` dan Purchase Cost `13000000` dari pemilik aset
3. Verifikasi nilai finansial record Active mengikuti nilai buku saat ini, yaitu Asset Value (Commercial) `9500000`
4. Pemilik aset mengubah Name `Laptop Lenovo ThinkPad - 213 {runId}` menjadi `Laptop Lenovo ThinkPad - 213 Baru {runId}`, Asset ID `LPT-0213-{runId}` menjadi `LPT-0213B-{runId}`, Model/Type `ThinkPad T14 {runId}` menjadi `ThinkPad T14s {runId}`, dan Division `Operasional {runId}` menjadi `Teknologi {runId}`
5. Verifikasi record Active menampilkan Name `Laptop Lenovo ThinkPad - 213 Baru {runId}`, Asset ID `LPT-0213B-{runId}`, Model/Type `ThinkPad T14s {runId}`, dan Division `Teknologi {runId}`
6. Pemilik aset mengubah Alias Name `Printer Lobi {runId}` menjadi `Printer Lantai Dua {runId}` dan Purchase Cost `3000000` menjadi `3500000` pada `Printer HP LaserJet M404 - 202 {runId}` yang record-nya `Repaired`
7. Verifikasi record History menampilkan Alias Name `Printer Lantai Dua {runId}` dan Purchase Cost `3500000` dari pemilik aset
8. Total Control `Agus Pratama {runId}` meminta daftar record Active setelah status record `Reported Disposal` `Projector Epson EB-X06 - 212 {runId}` mengikuti laporan pelepasan aset
9. Verifikasi Status record `Projector Epson EB-X06 - 212 {runId}` mencerminkan laporan pelepasan aset yang menjadi sumbernya

### Field Snapshot membeku mengikuti kejadian
10. Pemilik aset mengubah Purchase Cost `Laptop Lenovo ThinkPad - 201 {runId}` menjadi `14000000`
11. Verifikasi record `Laptop Lenovo ThinkPad - 201 {runId}` tetap menampilkan Last Holder `Budi S`, Reported By `Agus P`, Source `Manual`, dan Reported Date semula
12. Verifikasi node Damage Log record itu tidak berubah oleh perubahan pemilik aset
13. Aset `Printer HP LaserJet M404 - 202 {runId}` dipindahkan ke Group `Branch Surabaya {runId}` dan nilai buku Commercial turun menjadi `7000000`, nilai buku Fiscal turun menjadi `5500000`, dan Category diganti menjadi `Peralatan Kantor {runId}` setelah record selesai
14. Verifikasi record History tetap menampilkan Group `Head Office {runId}`, Asset Value (Commercial) `8000000`, Asset Value (Fiscal) `6500000`, dan Category `Elektronik {runId}` saat record selesai
15. Verifikasi Resolved By, Resolved Date, dan Duration record History tetap sesuai node yang menyelesaikannya

### Days Damaged dan Duration dihitung per zona waktu company
16. Total Control `Agus Pratama {runId}` meminta daftar record Active yang memuat `Tablet Samsung Tab A8 - 203 {runId}` dilaporkan pada `T0, pukul 01:00` zona waktu `Asia/Jakarta`
17. Verifikasi Days Damaged `Tablet Samsung Tab A8 - 203 {runId}` adalah `0 days` karena laporan pada hari kalender yang sama menurut zona waktu company
18. Total Control `Agus Pratama {runId}` meminta daftar record Active yang memuat `Camera Canon EOS - 204 {runId}` dan `Camera Canon EOS - 205 {runId}`
19. Verifikasi Days Damaged `Camera Canon EOS - 204 {runId}` yang `Waiting for Confirmation` adalah `2 days` dan `Camera Canon EOS - 205 {runId}` yang ditahan penanda `Missing` adalah `3 days`, keduanya dihitung sejak laporan pertama
20. Total Control `Agus Pratama {runId}` meminta daftar record History yang memuat `Printer HP LaserJet M404 - 202 {runId}` dilaporkan pada `T0 − 3 hari, pukul 23:30` dan selesai pada `T0 − 2 hari, pukul 00:30`
21. Verifikasi Duration `Printer HP LaserJet M404 - 202 {runId}` adalah `1 day` karena selisih hari kalender menurut zona waktu company, walau selisih waktunya satu jam

### Group record ikut Group aset tujuan saat pemindahan aset diterima
22. Aktor pemindahan aset `Tono Riyadi {runId}` menerima pemindahan `Forklift Toyota 8FD - 206 {runId}` ke Group `Branch Surabaya {runId}`
23. Verifikasi Damage record aktif ikut berpindah ke Group `Branch Surabaya {runId}` pada sub-tab Active
24. Verifikasi Source `Manual` dan riwayat Damage Log record tidak berubah dan tidak ada node baru

### Pelapor yang dinonaktifkan tidak mengubah record
25. User `Hana Lestari {runId}`, pelapor `Drill Bosch GSB - 207 {runId}`, dinonaktifkan
26. Verifikasi record `Drill Bosch GSB - 207 {runId}` tetap `Waiting for Confirmation` dengan Reported By `Hana L` dan tanpa node baru

### Group yang punya record berjalan tidak dapat dihapus
27. Total Control `Agus Pratama {runId}` menghapus Group `Divisi Gudang {runId}` yang tidak punya sub-group dan punya record berjalan
28. Verifikasi penghapusan Group ditolak dan record `Monitor Dell P2422H - 208 {runId}` tetap berada di Group itu tanpa node baru
29. Total Control `Agus Pratama {runId}` menghapus sub-group `Sub Pusat {runId}` yang punya record berjalan
30. Verifikasi penghapusan Group ditolak karena Group punya record berjalan dan record `Monitor Dell P2422H - 209 {runId}` tetap berada di sub-group itu tanpa node baru

### Hak Update yang dicabut saat halaman masih terbuka menolak aksi tulis berikutnya
31. Hak Update `Rina Wulandari {runId}` dicabut saat ia masih membuka Mark as Repaired atas `Scanner Fujitsu fi-7160 - 210 {runId}`
32. Pemegang Update `Rina Wulandari {runId}` mengirim Mark as Repaired atas `Scanner Fujitsu fi-7160 - 210 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
33. Verifikasi permintaan ditolak karena hak Update sudah dicabut dan record tetap `Damaged`

### Status global aset dan surface turunan mengikuti record
34. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Office Chair Ergo - 211 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
35. Verifikasi status global aset `Office Chair Ergo - 211 {runId}` menjadi `Damaged` sebagai data tersimpan milik modul aset, dan jumlah pada badge tab Damaged bertambah satu sebagai tampilan turunan
36. Konsumen modul lain membaca surface turunan dari record `Office Chair Ergo - 211 {runId}`
37. Verifikasi halaman detail aset menampilkan banner `Damaged since [Date]` dengan tanggal Reported Date record
38. Verifikasi modul aset hilang, registrasi aset, sesi `Audit`, laporan pelepasan aset, pemindahan aset, dan pengelolaan Group membaca status atau Group record yang sama tanpa salinan sendiri

### Field Reflected TAG, Labels, Asset Class, dan Category ikut berubah saat pemilik berubah
39. Pemilik aset mengubah TAG `RFID-L214 {runId}` menjadi `QR-L214 {runId}`, Labels `Prioritas {runId}` menjadi `Garansi {runId}`, Asset Class `Laptop {runId}` menjadi `Perangkat Kerja {runId}`, dan Category `Elektronik {runId}` menjadi `Peralatan Kantor {runId}` pada `Laptop Lenovo ThinkPad - 214 {runId}`
40. Verifikasi record Active `Laptop Lenovo ThinkPad - 214 {runId}` menampilkan TAG `QR-L214 {runId}`, Labels `Garansi {runId}`, Asset Class `Perangkat Kerja {runId}`, dan Category `Peralatan Kantor {runId}` dari pemilik aset

### Field Reflected lain ikut berubah, sedangkan Photo, Modified By, dan Last Updated membeku
41. Catat Damaged Photo pertama, Modified By, dan Last Updated record `Laptop Lenovo ThinkPad - 214 {runId}`
42. Pemilik aset mengubah Alias Name `Laptop Staf {runId}` menjadi `Laptop Direksi {runId}`, Measurement `14 inci` menjadi `15 inci`, Register Date `T0 − 400 hari` menjadi `T0 − 380 hari`, Purchase Date `T0 − 420 hari` menjadi `T0 − 400 hari`, dan Warranty Expiry `T0 + 300 hari` menjadi `T0 + 320 hari` pada `Laptop Lenovo ThinkPad - 214 {runId}`
43. Verifikasi record Active menampilkan Alias Name `Laptop Direksi {runId}`, Measurement `15 inci`, Register Date `T0 − 380 hari`, Purchase Date `T0 − 400 hari`, dan Warranty Expiry `T0 + 320 hari` menurut Date Format dari pemilik aset
44. Verifikasi Damaged Photo pertama `layar-retak.jpg`, Modified By, dan Last Updated record itu tetap sama dengan yang dicatat

### Surface turunan memuat penanda dan status yang pasti dari record yang sama
45. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 215 {runId}` yang sedang dipinjam dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
46. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 216 {runId}` yang sedang ditugaskan dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
47. Konsumen `borrow/` membaca baris peminjaman `Tablet Samsung Tab A8 - 215 {runId}`
48. Verifikasi baris peminjaman itu menampilkan penanda `Damaged` dari record yang sama
49. Konsumen `assignment/` membaca baris penugasan `Tablet Samsung Tab A8 - 216 {runId}`
50. Verifikasi baris penugasan itu menampilkan penanda `Damaged` dari record yang sama
51. Konsumen `my-asset/` membaca halaman aset yang dipegang `Budi Santoso {runId}`
52. Verifikasi halaman itu menampilkan status `Damaged` untuk `Tablet Samsung Tab A8 - 215 {runId}`

### Last Holder dan Reported By membeku walau nama pemegang dan pelapor berubah
53. Nama User `Wawan Setiadi {runId}`, pelapor `Laptop Lenovo ThinkPad - 217 {runId}`, diganti menjadi `Wawan Hidayat {runId}`
54. Nama User `Dimas Prakoso {runId}`, pemegang `Laptop Lenovo ThinkPad - 217 {runId}` saat dilaporkan, diganti menjadi `Dimas Kusuma {runId}`
55. Total Control `Agus Pratama {runId}` meminta record Active `Laptop Lenovo ThinkPad - 217 {runId}`
56. Verifikasi record itu tetap menampilkan Last Holder `Dimas P` dan Reported By `Wawan S` seperti saat dilaporkan

### Konsumen daftar aset membaca status global yang sama dari record
57. Konsumen `asset-list/` membaca daftar aset yang memuat `Office Chair Ergo - 211 {runId}`
58. Verifikasi daftar aset itu menampilkan status `Damaged` untuk `Office Chair Ergo - 211 {runId}` dari record yang sama

### Delete File Manager atas Damaged Photo dan After photo mengosongkan rujukan foto tanpa mengubah status
59. Total Control `Agus Pratama {runId}` menghapus berkas Damaged Photo milik laporan `Laptop Lenovo ThinkPad - 218 {runId}` dan berkas After photo milik Mark as Repaired `Printer HP LaserJet M404 - 202 {runId}` dari `File Manager`
60. Verifikasi rujukan Damaged Photo pada node `Reported damaged by` record Active `Laptop Lenovo ThinkPad - 218 {runId}` dikosongkan di respons server
61. Verifikasi rujukan Damaged Photo pertama `printer-rusak.jpg` pada node `Reported damaged by` record History `Printer HP LaserJet M404 - 202 {runId}` tetap ada di respons server, karena yang dihapus hanya After photo
62. Verifikasi respons Damage Log `Laptop Lenovo ThinkPad - 218 {runId}` tidak memuat rujukan Damaged Photo pada node `Reported damaged by`, sedangkan What happened `Layar retak setelah terjatuh dari meja {runId}` tetap ada
63. Verifikasi respons Damage Log di `My Asset` pelapor `Budi Santoso {runId}` untuk `Laptop Lenovo ThinkPad - 218 {runId}` tidak memuat rujukan Damaged Photo
64. Verifikasi penghapusan berkas itu tidak diblokir, status record `Laptop Lenovo ThinkPad - 218 {runId}` tetap `Waiting for Confirmation`, status record `Printer HP LaserJet M404 - 202 {runId}` tetap `Repaired`, dan status global serta penanda kedua aset tidak berubah
65. Verifikasi respons Damage Log `Printer HP LaserJet M404 - 202 {runId}` tidak memuat rujukan After photo pada node `Marked as repaired by`

### Transfer Completed menyinkronkan badge jumlah tab Damaged menurut cakupan Group pengguna
66. Verifikasi badge jumlah tab Damaged yang dilihat `Lina Marlina {runId}` adalah `2` dan yang dilihat `Bayu Santoso {runId}` adalah `1`
67. Aktor pemindahan aset `Wahyu Hidayat {runId}` menerima pemindahan `Forklift Toyota 8FD - 219 {runId}` ke Group `Cabang Tujuan {runId}`
68. Verifikasi badge jumlah tab Damaged yang dilihat `Lina Marlina {runId}` menjadi `1` karena record `Forklift Toyota 8FD - 219 {runId}` keluar dari cakupan Group `Cabang Asal {runId}`
69. Verifikasi badge jumlah tab Damaged yang dilihat `Bayu Santoso {runId}` menjadi `2` karena record `Forklift Toyota 8FD - 219 {runId}` sekarang berada di Group `Cabang Tujuan {runId}`

### Kolom Photo hanya mengikuti Damaged Photo pertama, sedangkan After photo hanya memengaruhi node Marked as repaired by
70. Verifikasi respons daftar record Active untuk `Laptop Lenovo ThinkPad - 218 {runId}` tidak lagi memuat Damaged Photo pada kolom Photo, karena Damaged Photo pertamanya sudah dihapus
71. Verifikasi respons daftar record History untuk `Printer HP LaserJet M404 - 202 {runId}` tetap memuat Damaged Photo pertama `printer-rusak.jpg` pada kolom Photo, karena menghapus After photo tidak memengaruhi kolom Photo
