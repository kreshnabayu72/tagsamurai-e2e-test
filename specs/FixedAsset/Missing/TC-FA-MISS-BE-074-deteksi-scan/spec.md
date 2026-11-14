---
id: TC-FA-MISS-BE-074-deteksi-scan
title: "Server: setiap scan TAG aset berjalan dicatat sebagai deteksi, penggabungan per jendela 1 jam per sumber, Last seen, pengecualian di luar cakupan, dan scan tidak menemukan aset"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [§1.2#r103, §1.2#r104, §1.2#r105, §1.2#r106, §1.2#r107, §1.2#r108, §1.2#r109, §9.2#b35, §9.2#b36, §9.2#b37, §9.2#b38, §9.2#b39, §9.2#b40, §9.2#b41, §9.2#b42, §9.2#b43, §9.2#b44, §9.2#b45, §9.2#b46, §9.2#b47, §9.2#p21, §9.4.2#r13, §9.4.2#r14, §9.4.2#r15, §9.4.2#r25, §9.4.2#r29, §9.4.3#b1, §9.4.4#r21, §9.4.4#r22, §9.4.1#r12, §9.4.1#r15, §9.4.1#r5, §9.5#r6, §9.6#r6, §9.7#r6, §9.8#r4, §8#r8, §8.1#r11, §6#r9, §4.1a#r12, §9.9#p3, §10#r3, §3#p6, §9.1#r7, §4.7#r3, §1.2#r65]
smoke: []
dependsOn: []
trace:
  §1.2#r103: 8
  §1.2#r104: [3, 18]
  §1.2#r105: 4
  §1.2#r106: 6
  §1.2#r107: 11
  §1.2#r108: 32
  §1.2#r109: 33
  §9.2#b35: [3, 22]
  §9.2#b36: [3, 32]
  §9.2#b37: 32
  §9.2#b38: [35, 37]
  §9.2#b39: [32, 48, 50]
  §9.2#b40: [39, 40]
  §9.2#b41: 42
  §9.2#b42: 22
  §9.2#b43: [14, 18, 19]
  §9.2#b44: [11, 14, 15]
  §9.2#b45: [22, 23]
  §9.2#b46: [5, 16, 24]
  §9.2#b47: [32, 47, 50]
  §9.2#p21: 33
  §9.4.2#r13: [4, 11]
  §9.4.2#r14: [47, 48]
  §9.4.2#r15: 50
  §9.4.2#r25: [39, 40]
  §9.4.2#r29: [1, 51]
  §9.4.3#b1: [8, 33]
  §9.4.4#r21: [3, 4, 6]
  §9.4.4#r22: [47, 48]
  §9.4.1#r12: 3
  §9.4.1#r15: 3
  §9.4.1#r5: [1, 51]
  §9.5#r6: 14
  §9.6#r6: [11, 15]
  §9.7#r6: [6, 16, 57, 58]
  §9.8#r4: [6, 15, 19]
  §8#r8: 7
  §8.1#r11: 5
  §6#r9: 47
  §4.1a#r12: 5
  §9.9#p3: 14
  §10#r3: [8, 33]
  §3#p6: [4, 6]
  §9.1#r7: 3
  §4.7#r3: 5
  §1.2#r65: [53, 55]
---

# Server: setiap scan TAG aset berjalan dicatat sebagai deteksi, penggabungan per jendela 1 jam per sumber, Last seen, pengecualian di luar cakupan, dan scan tidak menemukan aset

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client dan penerima `missing_detected`; `Maya Anggraini {runId}` (DU-074-1), Group Manager dengan Group binaan Head Office beserta sub-group, penerima `missing_detected`, dan pemindai Aktor Missing dalam cakupan Group aset; `Fajar Nugroho {runId}` (DU-074-2), Read Only dengan cakupan seluruh client; `Agus Pratama {runId}` (DU-074-3), pengguna terautentikasi tanpa hak Aktor Missing dengan akses ke layar pemindai Handover, Return, Send Transfer, Receive Transfer, Disposal, Damage, Work Order, Report TAG, dan Stock Opname, sebagai pemindai; `Dedi Kurnia {runId}` (DU-074-4), Group Manager dengan Group binaan Head Office sebagai Last holder; `Joko Susilo {runId}` (DU-074-5), pemegang tanpa hak Aktor Missing.
- Data:
  - DU-074-1: User Name `Maya Anggraini {runId}`, Peran `Group Manager`, Cakupan `Group Head Office beserta sub-group`.
  - DU-074-2: User Name `Fajar Nugroho {runId}`, Peran `Read Only`, Cakupan `seluruh client`.
  - DU-074-3: User Name `Agus Pratama {runId}`, Peran `pengguna terautentikasi tanpa hak Aktor Missing dengan akses ke layar pemindai Handover, Return, Send Transfer, Receive Transfer, Disposal, Damage, Work Order, Report TAG, dan Stock Opname`, Cakupan `tanpa cakupan Group Missing`.
  - DU-074-4: User Name `Dedi Kurnia {runId}`, Peran `Group Manager`, Cakupan `Group Head Office beserta sub-group`.
  - DU-074-5: User Name `Joko Susilo {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`.
  - DU-074-6: Reader Name `Gate A reader`, Jenis `reader tetap tanpa pengguna`.
  - DU-074-7: Setting Jendela penggabungan `1 jam per sumber pemindai`.
  - DU-074-8: Asset Name `Laptop Dell Latitude 5420 {runId}`, Asset ID `FA074-001`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-074-0001 dan RFID-074-0001`, Scan terakhir `belum pernah terpindai`.
  - DU-074-9: Asset Name `Projector Epson EB-X06 {runId}`, Asset ID `FA074-002`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-074-0002`, Scan terakhir `Gate B reader pada T0 − 3 hari, pukul 08:00`.
  - DU-074-10: Asset Name `Toyota Innova {runId}`, Asset ID `FA074-003`, Group aset `Finance Room`, Record berjalan `Reported Disposal, dilaporkan Rina W`, TAG terpasang `QR-074-0003`.
  - DU-074-11: Asset Name `Genset Honda EU22 {runId}`, Asset ID `FA074-004`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Dedi Kurnia {runId}`, TAG terpasang `QR-074-0004`, Last holder `Dedi Kurnia {runId}`.
  - DU-074-12: Asset Name `Hand Truck Gudang {runId}`, Asset ID `FA074-005`, Group aset `Warehouse`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-074-0005`.
  - DU-074-13: Asset Name `Monitor LG 27UL500 {runId}`, Asset ID `FA074-006`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-074-0006`.
  - DU-074-14: Asset Name `Printer HP LaserJet M404 {runId}`, Asset ID `FA074-007`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `QR-074-0007`.
  - DU-074-15: Asset Name `Hand Pallet Truck {runId}`, Asset ID `FA074-008`, Group aset `Finance Room`, Record berjalan `Missing, dilaporkan Rina W`, TAG terpasang `tidak ada`.
  - DU-074-16: Asset Name `Meja Kerja Kayu {runId}`, Asset ID `FA074-009`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Tagging `Tag Reported`, Activity Lock `In Audit`, Custody `dipegang Joko Susilo {runId}`.
  - DU-074-19: Sesi Stock Opname Sesi sebelumnya `Monitor LG 27UL500 {runId} berstatus Not found`, Sesi berikutnya `berjalan dengan pemindai Agus Pratama {runId}`.
  - DU-074-17: Asset Name `Kursi Ergonomis {runId}`, Asset ID `FA074-010`, Group aset `Finance Room`, Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}`, Pemegang `Joko Susilo {runId}`, Tagging `Tag Reported`, Activity Lock `In Audit`, Custody `dipegang Joko Susilo {runId}`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`
  - Jendela penggabungan deteksi scan bernilai `1 jam` per sumber pemindai

## Test Steps
### Scan reader dicatat sebagai deteksi dan tidak menemukan aset
1. Verifikasi Last Seen record `Laptop Dell Latitude 5420 {runId}` bernilai `Unknown` karena aset belum pernah terpindai
2. Reader `Gate A reader` membaca TAG `QR-074-0001` milik `Laptop Dell Latitude 5420 {runId}` pada waktu T0
3. Verifikasi record `Laptop Dell Latitude 5420 {runId}` memuat satu node `Detected by scan` dengan pemindai `Gate A reader` dan Count `1`
4. Verifikasi Last seen record `Laptop Dell Latitude 5420 {runId}` bernilai sama dengan Last seen pada node `Detected by scan` itu
5. Verifikasi Last seen itu memuat waktu deteksi menurut Date Format dan Time Format yang berlaku serta pemindai `Gate A reader`
6. Verifikasi Rina W dan `Maya Anggraini {runId}` masing-masing menerima satu notifikasi `missing_detected`, dan `Fajar Nugroho {runId}` tidak menerimanya
7. Verifikasi Activity Log mencatat deteksi dengan Modified By `System` dan System Log tidak mendapat entri aktor
8. Verifikasi record `Laptop Dell Latitude 5420 {runId}` tetap `Missing` dan status global aset tidak berubah menjadi Found walau TAG-nya terbaca
9. Waktu berlalu sampai 20 menit sejak deteksi pertama
10. Reader `Gate A reader` membaca lagi TAG `QR-074-0001` milik `Laptop Dell Latitude 5420 {runId}`
11. Verifikasi record `Laptop Dell Latitude 5420 {runId}` tetap memuat satu node `Detected by scan` dengan pemindai `Gate A reader` yang Count-nya menjadi `2`, tanpa node baru
12. Waktu berlalu sampai 40 menit sejak deteksi pertama
13. Reader `Gate A reader` membaca TAG `RFID-074-0001` milik `Laptop Dell Latitude 5420 {runId}`
14. Verifikasi node `Detected by scan` dengan pemindai `Gate A reader` memiliki Count `3`, karena deteksi dicatat untuk setiap TAG terpasang aset dan digabung per sumber pemindai
15. Verifikasi `Maya Anggraini {runId}` tidak menerima notifikasi `missing_detected` tambahan dari penggabungan itu
16. Verifikasi Last seen record `Laptop Dell Latitude 5420 {runId}` menampilkan waktu deteksi terbaru

### Sumber pemindai berbeda dan jendela tetap menghasilkan node baru
17. `Agus Pratama {runId}` memindai TAG `QR-074-0001` milik `Laptop Dell Latitude 5420 {runId}` dari layar pemindai pengguna
18. Verifikasi record `Laptop Dell Latitude 5420 {runId}` memuat node `Detected by scan` kedua dengan pemindai `Agus Pratama {runId}`, terpisah dari node milik `Gate A reader`, karena kunci gabung adalah sumber pemindai
19. Verifikasi Rina W dan `Maya Anggraini {runId}` masing-masing menerima satu notifikasi `missing_detected` tambahan untuk node baru itu
20. Waktu berlalu sampai 80 menit sejak deteksi pertama
21. Reader `Gate A reader` membaca TAG `QR-074-0001` milik `Laptop Dell Latitude 5420 {runId}`
22. Verifikasi record `Laptop Dell Latitude 5420 {runId}` memuat node `Detected by scan` baru dengan pemindai `Gate A reader` dan Count `1`, sedangkan node `Gate A reader` pertama tetap Count `3`, karena jendela 1 jam dihitung tetap dari deteksi pertama
23. Verifikasi Rina W dan `Maya Anggraini {runId}` masing-masing menerima satu notifikasi `missing_detected` tambahan untuk node baru itu
24. Verifikasi Last seen record `Laptop Dell Latitude 5420 {runId}` menampilkan waktu deteksi terbaru dengan pemindai `Gate A reader`

### Scan dari berbagai layar pemindai dicatat sebagai deteksi
25. `Maya Anggraini {runId}` memindai TAG `QR-074-0002` milik `Projector Epson EB-X06 {runId}` lewat Scan Found Asset
26. `Maya Anggraini {runId}` memindai TAG `QR-074-0002` milik `Projector Epson EB-X06 {runId}` pada Scan TAG di Mark as Found
27. `Maya Anggraini {runId}` memindai TAG `QR-074-0002` milik `Projector Epson EB-X06 {runId}` lewat Search by Scan
28. `Agus Pratama {runId}` memindai TAG `QR-074-0002` milik `Projector Epson EB-X06 {runId}` pada layar pemindai Disposal
29. `Agus Pratama {runId}` memindai TAG `QR-074-0002` milik `Projector Epson EB-X06 {runId}` pada layar pemindai Damage
30. `Agus Pratama {runId}` memindai TAG `QR-074-0002` milik `Projector Epson EB-X06 {runId}` pada layar pemindai Work Order
31. `Agus Pratama {runId}` memindai TAG `QR-074-0002` milik `Projector Epson EB-X06 {runId}` pada layar pemindai Report TAG
32. Verifikasi record `Projector Epson EB-X06 {runId}` memuat dua node `Detected by scan` terpisah per sumber pemindai, `Maya Anggraini {runId}` dengan Count `3` dari Scan Found Asset, Scan TAG di Mark as Found, dan Search by Scan, serta `Agus Pratama {runId}` dengan Count `4` dari layar pemindai Disposal, Damage, Work Order, dan Report TAG, sehingga setiap layar pemindai mencatat deteksi
33. Verifikasi record `Projector Epson EB-X06 {runId}` tetap `Missing` dan hanya Mark as Found oleh Aktor Missing yang dapat menandainya Found

### Scan yang diblok tetap dicatat sebagai deteksi
34. `Maya Anggraini {runId}` menjalankan Scan Found Asset dengan TAG `QR-074-0003` milik `Toyota Innova {runId}` yang berstatus `Reported Disposal`
35. Verifikasi scan itu diblok dengan pesan `[Asset Name] is in disposal. Mark as Found is not available.` dan record `Toyota Innova {runId}` memuat node `Detected by scan` baru dengan pemindai `Maya Anggraini {runId}`
36. `Dedi Kurnia {runId}` menjalankan Scan Found Asset dengan TAG `QR-074-0004` milik `Genset Honda EU22 {runId}` yang ia pegang
37. Verifikasi scan itu diblok dengan pesan `You were holding this asset. Ask another admin.` dan record `Genset Honda EU22 {runId}` memuat node `Detected by scan` baru dengan pemindai `Dedi Kurnia {runId}`

### Scan di luar cakupan Group tidak dicatat dan tidak mengungkap data aset
38. `Maya Anggraini {runId}` menjalankan Scan Found Asset dengan TAG `QR-074-0005` milik `Hand Truck Gudang {runId}` yang berada di Group `Warehouse`
39. Verifikasi scan itu ditolak dengan pesan `You don't have access to this asset.` tanpa nama aset dan tanpa data aset
40. Verifikasi record `Hand Truck Gudang {runId}` tidak memuat node `Detected by scan` baru dan Last seen-nya tidak berubah
41. `Maya Anggraini {runId}` memindai TAG `QR-074-0005` milik `Hand Truck Gudang {runId}` lewat Search by Scan
42. Verifikasi hasil pemindaian itu hanya menawarkan `[I found it]` tanpa `[Mark as Found]`, dan record `Hand Truck Gudang {runId}` tidak memuat node `Detected by scan` baru

### Scan di layar transaksi dan Stock Opname hanya mencatat deteksi
43. `Agus Pratama {runId}` memindai TAG `QR-074-0007` milik `Printer HP LaserJet M404 {runId}` pada layar Handover aset lain
44. `Agus Pratama {runId}` memindai TAG `QR-074-0007` milik `Printer HP LaserJet M404 {runId}` pada layar Return
45. `Agus Pratama {runId}` memindai TAG `QR-074-0007` milik `Printer HP LaserJet M404 {runId}` pada layar Send Transfer
46. `Agus Pratama {runId}` memindai TAG `QR-074-0007` milik `Printer HP LaserJet M404 {runId}` pada layar Receive Transfer
47. Verifikasi keempat scan itu ditolak dengan pesan `[Asset Name] is reported missing.` dan status record `Printer HP LaserJet M404 {runId}` tidak berubah
48. Verifikasi record `Printer HP LaserJet M404 {runId}` memuat satu node `Detected by scan` dengan pemindai `Agus Pratama {runId}` yang Count-nya `4`
49. `Agus Pratama {runId}` memindai TAG `QR-074-0006` milik `Monitor LG 27UL500 {runId}` pada sesi Stock Opname berikutnya setelah aset itu berstatus Not found
50. Verifikasi record `Monitor LG 27UL500 {runId}` memuat node `Detected by scan` baru dan tetap `Missing`, tanpa aksi apa pun dari layar Stock Opname

### Aset tanpa TAG menampilkan Last Seen tanpa nilai
51. Verifikasi Last Seen record `Hand Pallet Truck {runId}` bernilai `—` karena aset tidak punya TAG

### Reject dan Cancel Report tidak memulihkan Custody, Tagging, dan Activity Lock
52. Rina W mengirim Reject atas record `Meja Kerja Kayu {runId}` dengan Reason `Aset masih tercatat di ruang rapat`
53. Verifikasi record `Meja Kerja Kayu {runId}` berstatus `Rejected`, sedangkan Tagging `Tag Reported`, Activity Lock `In Audit`, dan Custody aset tidak berubah
54. `Joko Susilo {runId}` mengirim Cancel Report atas record `Kursi Ergonomis {runId}`
55. Verifikasi record `Kursi Ergonomis {runId}` berstatus `Canceled`, sedangkan Tagging `Tag Reported`, Activity Lock `In Audit`, dan Custody aset tidak berubah

### Last seen diperbarui pada saat scan dicatat
56. Reader `Gate A reader` membaca TAG `QR-074-0004` milik `Genset Honda EU22 {runId}`
57. Verifikasi record `Genset Honda EU22 {runId}` memuat node `Detected by scan` dengan pemindai `Gate A reader` dan Count `1`
58. Verifikasi Last seen record `Genset Honda EU22 {runId}` langsung berisi waktu deteksi itu dan pemindai `Gate A reader`, tanpa menunggu job terjadwal
