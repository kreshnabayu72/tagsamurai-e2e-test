---
id: TC-FA-MISS-BE-080-state-tenant-dan-plan
title: "Server: client Suspended dan Expired menolak aksi tulis aktor, aksi System tetap menulis, Missing tersedia di semua plan dengan Report Disposal mengikuti level Disposal"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [EB-AKS-7, EB-AKS-8, §9.2#b21, §9.4.1#r1, §9.4.1#r2, §9.4.2#r30, §9.4.2#r31, §9.4.4#r8, §9.10#p1, §8#r8, §8#r9]
smoke: []
dependsOn: []
trace:
  EB-AKS-7: [10, 26, 34]
  EB-AKS-8: [39, 43, 53, 55]
  §9.2#b21: [14, 15, 16, 30, 31, 32]
  §9.4.1#r1: [10, 12, 26, 28]
  §9.4.1#r2: 39
  §9.4.2#r30: [10, 12, 26, 28, 34]
  §9.4.2#r31: [39, 43, 58]
  §9.4.4#r8: [10, 12, 26, 28]
  §9.10#p1: [39, 43, 45, 47, 49, 53, 55]
  §8#r8: [15, 16, 31, 32]
  §8#r9: [14, 16, 30, 32]
---

# Server: client Suspended dan Expired menolak aksi tulis aktor, aksi System tetap menulis, Missing tersedia di semua plan dengan Report Disposal mengikuti level Disposal

## Prerequisites
- Aktor: Setiap pengguna pada entri data DU-080-6 sampai DU-080-12 dan DU-080-48 sebagai Total Control atau pemegang di client masing-masing, dengan peran dan client seperti tercatat di entri; job sistem hanya sebagai pemicu keadaan.
- Data:
  - DU-080-1: Client Name `Klien Aktif Uji {runId}`, Plan `Professional`, Status `Active`; entitas khusus yang tidak dipakai spec lain.
  - DU-080-2: Client Name `Klien Suspended Uji {runId}`, Plan `Professional`, Status `Suspended`; entitas khusus yang tidak dipakai spec lain.
  - DU-080-3: Client Name `Klien Expired Uji {runId}`, Plan `Professional`, Status `Expired`; entitas khusus yang tidak dipakai spec lain.
  - DU-080-4: Client Name `Klien Starter Uji {runId}`, Plan `Starter`, Status `Active`; entitas khusus yang tidak dipakai spec lain.
  - DU-080-5: Client Name `Klien Growth Uji {runId}`, Plan `Growth`, Status `Active`; entitas khusus yang tidak dipakai spec lain.
  - DU-080-6: User Name `Gunawan Setiadi {runId}`, Peran `Total Control`, Client `Klien Aktif Uji {runId}`.
  - DU-080-7: User Name `Maria Kusuma {runId}`, Peran `Total Control`, Client `Klien Suspended Uji {runId}`.
  - DU-080-8: User Name `Nugroho Aditya {runId}`, Peran `Total Control`, Client `Klien Expired Uji {runId}`.
  - DU-080-9: User Name `Putri Handayani {runId}`, Peran `Total Control`, Client `Klien Starter Uji {runId}`.
  - DU-080-10: User Name `Rahmat Hidayat {runId}`, Peran `Total Control`, Client `Klien Growth Uji {runId}`.
  - DU-080-11: User Name `Slamet Riyadi {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Client `Klien Suspended Uji {runId}`.
  - DU-080-12: User Name `Tono Wijaya {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Client `Klien Expired Uji {runId}`.
  - DU-080-13: Asset Name `Camera Canon EOS {runId}`, Asset ID `FA080-101`, Client `Klien Suspended Uji {runId}`, Record berjalan `tidak ada`.
  - DU-080-14: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA080-102`, Client `Klien Suspended Uji {runId}`, Record berjalan `Waiting for Confirmation, dilaporkan Slamet Riyadi {runId}`, Pemegang `Slamet Riyadi {runId}`.
  - DU-080-15: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA080-103`, Client `Klien Suspended Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, TAG terpasang `tidak ada`.
  - DU-080-16: Asset Name `Toyota Innova {runId}`, Asset ID `FA080-104`, Client `Klien Suspended Uji {runId}`, Record berjalan `Reported Disposal, dilaporkan admin client`.
  - DU-080-17: Asset Name `Drill Bosch GSB {runId}`, Asset ID `FA080-105`, Client `Klien Suspended Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-18: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA080-106`, Client `Klien Suspended Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, Reported Date `T0 − 30 hari, pukul 09:00`.
  - DU-080-19: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA080-107`, Client `Klien Suspended Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, TAG terpasang `QR-080-107`.
  - DU-080-20: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA080-201`, Client `Klien Expired Uji {runId}`, Record berjalan `tidak ada`.
  - DU-080-21: Asset Name `Scanner Zebra DS2208 {runId}`, Asset ID `FA080-202`, Client `Klien Expired Uji {runId}`, Record berjalan `Waiting for Confirmation, dilaporkan Tono Wijaya {runId}`, Pemegang `Tono Wijaya {runId}`.
  - DU-080-22: Asset Name `Mesin Fotokopi Ricoh {runId}`, Asset ID `FA080-203`, Client `Klien Expired Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, TAG terpasang `tidak ada`.
  - DU-080-23: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA080-204`, Client `Klien Expired Uji {runId}`, Record berjalan `Reported Disposal, dilaporkan admin client`.
  - DU-080-24: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA080-205`, Client `Klien Expired Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-25: Asset Name `Meja Kerja Kayu {runId}`, Asset ID `FA080-206`, Client `Klien Expired Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, Reported Date `T0 − 30 hari, pukul 09:00`.
  - DU-080-26: Asset Name `Rak Besi Gudang {runId}`, Asset ID `FA080-207`, Client `Klien Expired Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, TAG terpasang `QR-080-207`.
  - DU-080-27: Asset Name `Laptop Lenovo ThinkPad T14 {runId}`, Asset ID `FA080-301`, Client `Klien Aktif Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-28: Asset Name `Tablet Samsung Tab A8 {runId}`, Asset ID `FA080-302`, Client `Klien Aktif Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-29: Asset Name `Kamera Sony A7 {runId}`, Asset ID `FA080-401`, Client `Klien Starter Uji {runId}`, Record berjalan `tidak ada`.
  - DU-080-30: Asset Name `Brankas Besi {runId}`, Asset ID `FA080-402`, Client `Klien Starter Uji {runId}`, Record berjalan `Waiting for Confirmation, dilaporkan admin client`.
  - DU-080-31: Asset Name `Papan Tulis {runId}`, Asset ID `FA080-403`, Client `Klien Starter Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-32: Asset Name `Lemari Arsip Besi {runId}`, Asset ID `FA080-404`, Client `Klien Starter Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, TAG terpasang `tidak ada`.
  - DU-080-33: Asset Name `Kipas Angin Standing {runId}`, Asset ID `FA080-405`, Client `Klien Starter Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-34: Asset Name `Dispenser Air Galon {runId}`, Asset ID `FA080-406`, Client `Klien Starter Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-35: Asset Name `Genset Mini Yamaha {runId}`, Asset ID `FA080-407`, Client `Klien Starter Uji {runId}`, Record berjalan `Reported Disposal, dilaporkan admin client`.
  - DU-080-36: Asset Name `Router Mikrotik RB750 {runId}`, Asset ID `FA080-408`, Client `Klien Starter Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, TAG terpasang `QR-080-0408 dan RFID-080-0408`.
  - DU-080-37: Asset Name `Switch Cisco SG350 {runId}`, Asset ID `FA080-409`, Client `Klien Starter Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`, TAG terpasang `RFID-080-0409`.
  - DU-080-38: Asset Name `Stabilizer Lampu Studio {runId}`, Asset ID `FA080-501`, Client `Klien Growth Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-39: Asset Name `Lampu Sorot Panggung {runId}`, Asset ID `FA080-502`, Client `Klien Growth Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-40: Asset Name `Speaker Aktif Yamaha {runId}`, Asset ID `FA080-503`, Client `Klien Growth Uji {runId}`, Record berjalan `Missing, dilaporkan admin client`.
  - DU-080-46: Asset Name `Meja Lipat Aluminium {runId}`, Asset ID `FA080-410`, Client `Klien Starter Uji {runId}`, Record berjalan `Waiting for Confirmation, dilaporkan Wawan Setiawan {runId}`, Pemegang `Wawan Setiawan {runId}`.
  - DU-080-47: Asset Name `Kursi Lipat Besi {runId}`, Asset ID `FA080-411`, Client `Klien Starter Uji {runId}`, Record berjalan `Waiting for Confirmation, dilaporkan Wawan Setiawan {runId}`, Pemegang `Wawan Setiawan {runId}`.
  - DU-080-48: User Name `Wawan Setiawan {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Client `Klien Starter Uji {runId}`.
  - DU-080-41: Asset Name `Mixer Audio Behringer {runId}`, Asset ID `FA080-504`, Client `Klien Growth Uji {runId}`, Record berjalan `Reported Disposal, dilaporkan admin client`.
- Kondisi:
  - Long missing after bernilai `30`

## Test Steps
### Client Suspended menolak semua aksi tulis aktor tetapi tetap bisa dibaca dan ditulis oleh System
1. `Maria Kusuma {runId}` mengirim Report Missing atas `Camera Canon EOS {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
2. `Maria Kusuma {runId}` menjalankan Confirm atas record `Printer HP LaserJet M404 {runId}`
3. `Maria Kusuma {runId}` menjalankan Reject atas record `Printer HP LaserJet M404 {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
4. `Slamet Riyadi {runId}` menjalankan Cancel Report atas record `Printer HP LaserJet M404 {runId}`
5. `Maria Kusuma {runId}` mengirim Add Update atas record `Hand Pallet Truck {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
6. `Maria Kusuma {runId}` mengirim Mark as Found atas record `Hand Pallet Truck {runId}` dengan Found at default Group aset dan Asset Status `Normal`
7. `Maria Kusuma {runId}` mengirim Report Disposal atas record `Hand Pallet Truck {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
8. `Maria Kusuma {runId}` menjalankan Cancel Disposal Report atas record `Toyota Innova {runId}`
9. `Maria Kusuma {runId}` menjalankan Bulk Report Disposal atas `Hand Pallet Truck {runId}` dan `Drill Bosch GSB {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
10. Verifikasi semua permintaan tulis itu ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`, walau aktornya punya hak, dan tidak ada record, node, atau status yang berubah pada aset `Camera Canon EOS {runId}`, `Printer HP LaserJet M404 {runId}`, `Hand Pallet Truck {runId}`, `Toyota Innova {runId}`, dan `Drill Bosch GSB {runId}`
11. `Maria Kusuma {runId}` mengambil daftar sub-tab Active dengan Search `{runId}` dan membuka Missing Log record `Hand Pallet Truck {runId}`
12. Verifikasi daftar memuat record `Printer HP LaserJet M404 {runId}`, `Hand Pallet Truck {runId}`, dan `Toyota Innova {runId}`, dan Missing Log `Hand Pallet Truck {runId}` dapat dibaca, karena data tetap dapat dibaca pada client Suspended
13. Job Long missing harian berjalan dan `Slamet Riyadi {runId}` memindai TAG `QR-080-107` milik `Projector Epson EB-X06 {runId}` dari layar pemindai pengguna
14. Verifikasi record `Monitor LG 27UL500 {runId}` memuat node `Long missing` atas nama `System` walau client Suspended, karena aksi sistem tanpa aktor tidak diblokir
15. Verifikasi record `Projector Epson EB-X06 {runId}` memuat node `Detected by scan` walau client Suspended
16. Verifikasi Activity Log mencatat kedua peristiwa itu dengan Modified By `System` dan System Log tidak mendapat entri aktor

### Client Expired menolak semua aksi tulis aktor tetapi tetap bisa dibaca dan ditulis oleh System
17. `Nugroho Aditya {runId}` mengirim Report Missing atas `Laptop Dell Latitude 5420 {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
18. `Nugroho Aditya {runId}` menjalankan Confirm atas record `Scanner Zebra DS2208 {runId}`
19. `Nugroho Aditya {runId}` menjalankan Reject atas record `Scanner Zebra DS2208 {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
20. `Tono Wijaya {runId}` menjalankan Cancel Report atas record `Scanner Zebra DS2208 {runId}`
21. `Nugroho Aditya {runId}` mengirim Add Update atas record `Mesin Fotokopi Ricoh {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
22. `Nugroho Aditya {runId}` mengirim Mark as Found atas record `Mesin Fotokopi Ricoh {runId}` dengan Found at default Group aset dan Asset Status `Normal`
23. `Nugroho Aditya {runId}` mengirim Report Disposal atas record `Mesin Fotokopi Ricoh {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
24. `Nugroho Aditya {runId}` menjalankan Cancel Disposal Report atas record `Genset Honda EU22 {runId}`
25. `Nugroho Aditya {runId}` menjalankan Bulk Report Disposal atas `Mesin Fotokopi Ricoh {runId}` dan `Kursi Ergonomis {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
26. Verifikasi semua permintaan tulis itu ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`, walau aktornya punya hak, dan tidak ada record, node, atau status yang berubah pada aset `Laptop Dell Latitude 5420 {runId}`, `Scanner Zebra DS2208 {runId}`, `Mesin Fotokopi Ricoh {runId}`, `Genset Honda EU22 {runId}`, dan `Kursi Ergonomis {runId}`
27. `Nugroho Aditya {runId}` mengambil daftar sub-tab Active dengan Search `{runId}` dan membuka Missing Log record `Mesin Fotokopi Ricoh {runId}`
28. Verifikasi daftar memuat record `Scanner Zebra DS2208 {runId}`, `Mesin Fotokopi Ricoh {runId}`, dan `Genset Honda EU22 {runId}`, dan Missing Log `Mesin Fotokopi Ricoh {runId}` dapat dibaca, karena data tetap dapat dibaca pada client Expired
29. Job Long missing harian berjalan dan `Tono Wijaya {runId}` memindai TAG `QR-080-207` milik `Rak Besi Gudang {runId}` dari layar pemindai pengguna
30. Verifikasi record `Meja Kerja Kayu {runId}` memuat node `Long missing` atas nama `System` walau client Expired, karena aksi sistem tanpa aktor tidak diblokir
31. Verifikasi record `Rak Besi Gudang {runId}` memuat node `Detected by scan` walau client Expired
32. Verifikasi Activity Log mencatat kedua peristiwa itu dengan Modified By `System` dan System Log tidak mendapat entri aktor

### Client aktif menerima aksi tulis yang sama
33. `Gunawan Setiadi {runId}` mengirim Add Update atas record `Laptop Lenovo ThinkPad T14 {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
34. Verifikasi permintaan itu diterima dan record `Laptop Lenovo ThinkPad T14 {runId}` mendapat node `Update added by`, sehingga penolakan di client Suspended dan Expired disebabkan state client

### Plan Starter: Report Missing, Confirm, Reject, Mark as Found, dan Add Update tidak plan-gated
35. `Putri Handayani {runId}` mengirim Report Missing atas `Kamera Sony A7 {runId}` dengan What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip`
36. `Putri Handayani {runId}` menjalankan Confirm atas record `Brankas Besi {runId}`
37. `Putri Handayani {runId}` mengirim Add Update atas record `Papan Tulis {runId}` dengan Update `Pencarian di gudang lantai satu belum membuahkan hasil`
38. `Putri Handayani {runId}` mengirim Mark as Found atas record `Lemari Arsip Besi {runId}` dengan Found at default Group aset dan Asset Status `Normal`
39. Verifikasi keempat aksi itu diterima di plan Starter: `Kamera Sony A7 {runId}` mendapat record `Missing`, `Brankas Besi {runId}` berstatus `Missing`, `Papan Tulis {runId}` mendapat node `Update added by`, dan `Lemari Arsip Besi {runId}` berstatus `Found`

### Level Disposal None di Starter menolak Report Disposal, Bulk Report Disposal, dan Cancel Disposal Report
40. `Putri Handayani {runId}` mengirim Report Disposal atas record `Kipas Angin Standing {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
41. `Putri Handayani {runId}` menjalankan Bulk Report Disposal atas `Kipas Angin Standing {runId}` dan `Dispenser Air Galon {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
42. `Putri Handayani {runId}` menjalankan Cancel Disposal Report atas record `Genset Mini Yamaha {runId}`
43. Verifikasi ketiga permintaan itu ditolak karena level Disposal `None` di Starter, record `Kipas Angin Standing {runId}` dan `Dispenser Air Galon {runId}` tetap `Missing`, dan record `Genset Mini Yamaha {runId}` tetap `Reported Disposal`

### Plan Starter hanya membuka tipe TAG QR
44. `Putri Handayani {runId}` mengambil daftar sub-tab Active dengan Search `{runId}` dan opsi filter TAG
45. Verifikasi baris `Router Mikrotik RB750 {runId}` hanya mengembalikan TAG `QR`, baris `Switch Cisco SG350 {runId}` yang hanya ber-TAG `RFID` memuat `—` pada kolom TAG, dan opsi filter TAG hanya memuat `QR`
46. `Putri Handayani {runId}` meminta Download as CSV dari sub-tab Active dengan Search `{runId}`
47. Verifikasi kolom TAG pada berkas tidak menulis `RFID` untuk baris `Router Mikrotik RB750 {runId}` dan `Switch Cisco SG350 {runId}`
48. `Putri Handayani {runId}` menjalankan Scan Found Asset dengan TAG `RFID-080-0409` milik `Switch Cisco SG350 {runId}`
49. Verifikasi scan itu ditolak karena tipe TAG `RFID` terkunci di Starter, dan hanya jalur `QR` atau `I Can't Scan the TAG` yang tersisa

### Level Disposal Full di Growth menerima Report Disposal, Bulk Report Disposal, dan Cancel Disposal Report
50. `Rahmat Hidayat {runId}` mengirim Report Disposal atas record `Stabilizer Lampu Studio {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
51. `Rahmat Hidayat {runId}` menjalankan Bulk Report Disposal atas `Lampu Sorot Panggung {runId}` dan `Speaker Aktif Yamaha {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
52. `Rahmat Hidayat {runId}` menjalankan Cancel Disposal Report atas record `Mixer Audio Behringer {runId}`
53. Verifikasi ketiga permintaan itu diterima di Growth: `Stabilizer Lampu Studio {runId}`, `Lampu Sorot Panggung {runId}`, dan `Speaker Aktif Yamaha {runId}` berstatus `Reported Disposal`, dan `Mixer Audio Behringer {runId}` kembali `Missing`

### Level Disposal Full di Professional menerima Report Disposal
54. `Gunawan Setiadi {runId}` mengirim Report Disposal atas record `Tablet Samsung Tab A8 {runId}` dengan Reason `Aset tidak ditemukan setelah pencarian dua pekan`
55. Verifikasi permintaan itu diterima dan record `Tablet Samsung Tab A8 {runId}` berstatus `Reported Disposal`

### Plan Starter: Reject dan Cancel Report tidak plan-gated
56. `Putri Handayani {runId}` menjalankan Reject atas record `Meja Lipat Aluminium {runId}` dengan Reason `Aset masih dipakai di meja pemegang`
57. `Wawan Setiawan {runId}` menjalankan Cancel Report atas record `Kursi Lipat Besi {runId}`
58. Verifikasi kedua aksi itu diterima di plan Starter: `Meja Lipat Aluminium {runId}` berstatus `Rejected` dan `Kursi Lipat Besi {runId}` berstatus `Canceled`
