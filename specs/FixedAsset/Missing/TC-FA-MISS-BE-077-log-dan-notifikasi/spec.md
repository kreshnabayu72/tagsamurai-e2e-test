---
id: TC-FA-MISS-BE-077-log-dan-notifikasi
title: "Server: satu node dan satu entri log per item, aktor System tanpa System Log, Cancel Report tanpa Transaction admin log, dan event per aksi"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§8#r1", "§8#r2", "§8#r3", "§8#r4", "§8#r5", "§8#r6", "§8#r7", "§8#r8", "§8#r9", "§8#r10", "§8#r11", "§8#p2", "§8.1#p2", "§8.2#b1", "§8.2#b2", "§8.2#b3", "§9.2#b21", "§9.4.4#r16", "§9.4.4#r18", "§9.4.4#r19", "§9.8#p1", "§9.8#r1", "§9.8#r2", "§9.8#r3", "§9.8#r4", "§9.8#r5", "§9.8#r6", "§9.8#r7", "§9.8#p2", "§9.8#p3", "§9.6#r1", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r5", "§9.6#r7", "§9.6#r8", "§9.6#r9", "§9.6#r10", "§9.6#r11", "§9.5#r7", "§9.7#p1", "§9.7#r1", "§9.7#r2", "§9.7#r3", "§9.7#r4", "§9.7#r5", "§9.7#r6", "§9.7#r7", "§9.7#r8", "§9.7#r9", "§9.7#r10", "EB-LOG-1", "§4.1a#r27", "§4.1a#r28", "§9.4.1#r8", "§9.4.1#r10", "§9.4.1#r9", "§9.4.1#r2", "§1.2#r115", "§9.4.4#r23", "§1.2#r72", "§9.2#b38", "§9.4.2#r39", "§9.4.4#r24", "§8.2#p4", "§8.2#p5", "§8.2#p6", "§8.2#p7", "§8.2#p8", "§8.2#p9", "§8.2#p10", "§8.2#p14", "§8.2#p15", "§8.2#p16", "§8.2#p17", "§8.2#p18", "§8.2#p21", "§8.2#p22", "§8.2#p23", "§8.2#p24", "§8.2#p25", "§8.2#p26", "§8.2#p27", "§8.1#r12", "§3#p4", "§1.2#r61", "§3#p8", "§9.4.2#r11", "§8.1#r15", "§8.1#r16", "§8.1#r17"]
smoke: []
dependsOn: []
trace:
  "§8#r1": 4
  "§8#r2": 4
  "§8#r3": 3
  "§8#r4": [4, 44]
  "§8#r5": [69, 95, 106, 122]
  "§8#r6": [12, 136, 137]
  "§8#r7": [9, 65]
  "§8#r8": [105, 106]
  "§8#r9": [113, 115]
  "§8#r10": [122, 132]
  "§8#r11": [69, 77, 83, 88, 95]
  "§8#p2": [4, 106]
  "§8.1#p2": [26, 81, 88, 90, 92, 94, 98, 102]
  "§8.2#b1": [5, 85]
  "§8.2#b2": [15, 59]
  "§8.2#b3": [9, 65, 141]
  "§9.2#b21": [13, 14, 137, 138]
  "§9.4.4#r16": [70, 72, 84]
  "§9.4.4#r18": [98, 99]
  "§9.4.4#r19": [101, 102]
  "§9.8#p1": 7
  "§9.8#r1": 7
  "§9.8#r2": [22, 48]
  "§9.8#r3": [29, 37]
  "§9.8#r4": [105, 108]
  "§9.8#r5": [123, 127, 130]
  "§9.8#r6": 114
  "§9.8#r7": [63, 84]
  "§9.8#p2": [57, 70, 73, 78, 81, 84, 88, 90, 92, 94]
  "§9.8#p3": [29, 37]
  "§9.6#r1": 4
  "§9.6#r2": 26
  "§9.6#r3": 34
  "§9.6#r4": 61
  "§9.6#r5": [56, 59]
  "§9.6#r7": [41, 52]
  "§9.6#r8": [121, 125]
  "§9.6#r9": [68, 76]
  "§9.6#r10": 136
  "§9.6#r11": [113, 118]
  "§9.5#r7": [125, 130]
  "§9.7#p1": 16
  "§9.7#r1": [3, 27]
  "§9.7#r2": [20, 22, 47]
  "§9.7#r3": 35
  "§9.7#r4": [61, 62]
  "§9.7#r5": [68, 84]
  "§9.7#r6": [105, 108]
  "§9.7#r7": 113
  "§9.7#r8": [41, 42]
  "§9.7#r9": 56
  "§9.7#r10": [121, 123, 133]
  "EB-LOG-1": [14, 17, 138, 143]
  "§4.1a#r27": [8, 30, 64, 77, 107, 115]
  "§4.1a#r28": [8, 30, 64, 107, 115]
  "§9.4.1#r8": [23, 27, 94]
  "§9.4.1#r10": 16
  "§9.4.1#r9": 12
  "§9.4.1#r2": 142
  "§1.2#r115": 114
  "§9.4.4#r23": 52
  "§1.2#r72": 48
  "§9.2#b38": 48
  "§9.4.2#r39": 48
  "§9.4.4#r24": 48
  "§8.2#p4": 3
  "§8.2#p5": [20, 21, 47, 50]
  "§8.2#p6": [26, 28]
  "§8.2#p7": [34, 36]
  "§8.2#p8": [61, 62]
  "§8.2#p9": [83, 85]
  "§8.2#p10": [43, 53, 57, 70, 73, 78, 109, 116, 133]
  "§8.2#p14": 5
  "§8.2#p15": [6, 28]
  "§8.2#p16": 6
  "§8.2#p17": 6
  "§8.2#p18": 6
  "§8.2#p21": [6, 49]
  "§8.2#p22": 53
  "§8.2#p23": 28
  "§8.2#p24": 36
  "§8.2#p25": 56
  "§8.2#p26": 62
  "§8.2#p27": [24, 43, 49, 70]
  "§8.1#r12": [121, 127]
  "§3#p4": [3, 35]
  "§1.2#r61": [34, 35]
  "§3#p8": 68
  "§9.4.2#r11": [72, 88]
  "§8.1#r15": [68, 136]
  "§8.1#r16": 72
  "§8.1#r17": [76, 146]
---

# Server: satu node dan satu entri log per item, aktor System tanpa System Log, Cancel Report tanpa Transaction admin log, dan event per aksi

## Prerequisites
- Aktor:
  - Aktor Missing A: Total Control, cakupan seluruh client, juga Aktor Disposal dan Pelapor admin.
  - Aktor Missing B: Total Control lain, cakupan seluruh client.
  - Approver Disposal dan Pembuat Request Disposal: Total Control dengan hak memutuskan dan membuat Request Disposal.
  - Pemegang: Borrower atau Assignee aset tanpa hak Aktor Missing pada Group aset; pemegang yang sama melapor dan membatalkan laporannya sendiri.
  - Pelapor sesi: Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group aset.
  - Penemu A dan Penemu B: pengguna terautentikasi tanpa hak Aktor Missing yang memindai TAG aset dari perangkat mobile.
  - Pelapor Disposal: Manage asset & TAG dengan Update pada Group `Head Office` beserta descendant, bukan Group Manager dan bukan Total Control.
- Data:
  - DU-077-1: aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office`, belum punya record berjalan, dilaporkan Aktor Missing A sebagai Pelapor admin.
  - DU-077-2: aset `Monitor LG 27UL500 {runId}` di Group `Head Office`, belum punya record berjalan, ikut laporan banyak aset.
  - DU-077-3: aset `Hand Pallet Truck {runId}` di Group `Head Office`, belum punya record berjalan, ikut laporan banyak aset.
  - DU-077-4: Missing record berstatus `Missing`, Source `Manual`, aset `Projector Epson EB-X06 {runId}` di Group `Head Office`, ikut terpilih dalam laporan banyak aset sehingga dilewati.
  - DU-077-5: Missing record berstatus `Missing`, Source `Manual`, aset `Scanner Zebra DS2208 {runId}` di Group `Head Office`, tidak terlibat aksi apa pun di spec ini.
  - DU-077-6: aset `Camera Canon EOS {runId}` di Group `Head Office`, dipegang Borrower lewat baris Borrow terbuka, belum punya record berjalan.
  - DU-077-7: aset `Drill Bosch GSB {runId}` di Group `Head Office`, dipegang Assignee lewat baris Assignment terbuka, belum punya record berjalan.
  - DU-077-8: aset `Forklift Toyota 8FD {runId}` di Group `Head Office`, dipegang Borrower lewat baris Borrow terbuka, belum punya record berjalan.
  - DU-077-9: aset `Router Cisco ISR {runId}` di Group `Head Office`, belum punya record berjalan, dilaporkan Pelapor sesi dari Task Detail sesi pemeriksaan.
  - DU-077-10: Missing record berstatus `Missing`, Source `Manual`, aset `Mixer Audio Yamaha MG10 {runId}` di Group `Head Office`, tanpa TAG, dilaporkan Aktor Missing A.
  - DU-077-11: Missing record berstatus `Missing`, Source `Manual`, aset `Lemari Arsip Brother {runId}` di Group `Head Office`.
  - DU-077-12: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Handheld Zebra TC21 {runId}` di Group `Head Office`, Disposal Report berstatus `Reported` dilaporkan Aktor Missing A.
  - DU-077-13: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Monitor Dell P2422H {runId}` di Group `Head Office`, Disposal Report berstatus `Reported`.
  - DU-077-14: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Generator Honda EU20 {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Execution`.
  - DU-077-15: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Kursi Ergonomis Ergotec {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-077-16: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Meja Rapat Informa {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-077-17: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `AC Daikin FTV35 {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`.
  - DU-077-18: Missing record berstatus `In Disposal Process`, Source `Manual`, aset `Kompresor Swan 2HP {runId}` di Group `Head Office`, baris Disposal Write-off `Waiting for Approval`, ditutup habis waktu tanpa user aktor.
  - DU-077-19: aset `Server Dell PowerEdge R450 {runId}` di Group `Head Office`, belum punya record Missing berjalan, dengan Disposal Report berstatus `Reported` Source `Manual`.
  - DU-077-20: aset `Barcode Printer Zebra ZD230 {runId}` di Group `Head Office`, belum punya record Missing berjalan, dengan satu baris Disposal berjenis Sell `Waiting for Approval` dan satu baris Disposal `Draft`.
  - DU-077-21: Missing record berstatus `Missing`, Source `Manual`, aset `Timbangan Digital Ohaus {runId}` di Group `Head Office`, TAG terpasang `QR-077-0001`.
  - DU-077-22: Reader Name `Gate A reader`, reader tetap tanpa pengguna.
  - DU-077-23: Missing record berstatus `Missing`, Source `Manual`, aset `Trolley Besi Gudang {runId}` di Group `Head Office`, dilaporkan 31 hari sebelum job harian berjalan.
  - DU-077-24: Missing record berstatus `Missing`, Source `Manual`, aset `Telepon IP Yealink T46 {runId}` di Group `Head Office`, TAG terpasang `QR-077-0002`.
  - DU-077-25: Missing record berstatus `Missing`, Source `Manual`, aset `Keyboard Logitech MX {runId}` di Group `Head Office`, ikut Bulk Report Disposal.
  - DU-077-26: Missing record berstatus `Missing`, Source `Manual`, aset `Tablet Samsung Galaxy Tab A8 {runId}` di Group `Head Office`, ikut Bulk Report Disposal.
  - DU-077-27: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Proyektor BenQ MW550 {runId}` di Group `Head Office`, ikut terpilih dalam Bulk Report Disposal sehingga dilewati.
  - DU-077-28: What happened `Aset tidak ada di rak penyimpanan saat inventaris`, dipakai Aktor Missing A.
  - DU-077-29: What happened `Beberapa aset tidak ditemukan saat inventaris bulanan`, dipakai Aktor Missing A.
  - DU-077-30: What happened `Aset hilang dari tas saat perjalanan dinas`, dipakai Pemegang.
  - DU-077-31: What happened `Aset tidak ada di lokasi saat pemeriksaan berlangsung`, dipakai Pelapor sesi.
  - DU-077-32: Reason Reject `Laporan belum disertai bukti yang cukup`, dipakai Aktor Missing B.
  - DU-077-33: Update `Tim keamanan sudah memeriksa rekaman kamera lantai dua`.
  - DU-077-34: Update `Pemeriksaan ruang arsip belum menemukan aset`.
  - DU-077-35: Reason Report Disposal `Aset sudah dicari berbulan-bulan tanpa hasil`.
  - DU-077-36: Reason Report Disposal Bulk `Aset dinyatakan hilang permanen setelah pencarian ulang`.
  - DU-077-37: Reason Decline Report `Pencarian lanjutan masih akan dilakukan bulan ini`.
  - DU-077-38: Location `-6.2088, 106.8456`, dipakai Penemu A.
  - DU-077-39: Location `-6.9175, 107.6191`, dipakai Aktor Missing B sebagai penemu.
  - DU-077-40: Missing record berstatus `Reported Disposal`, Source `Manual`, aset `Rak Server Panduit {runId}` di Group `Head Office`, Disposal Report berstatus `Reported` dilaporkan Pelapor Disposal.
- Kondisi:
  - Long missing after bernilai `30`.
  - Date Format bernilai `DD/MM/YY`, Time Format bernilai `HH:mm`, dan Time Zone bernilai `UTC`.
  - Plan client adalah `Basic`.
  - Jumlah notifikasi `missing_*`, jumlah node Missing Log, jumlah entri Activity Log, System Log, dan Transaction admin log, serta jumlah baris Transaction log aset dicatat sebelum aksi pertama atas record terkait.
  - Cakupan Group Aktor Missing A dan B meliputi `Head Office`.

## Test Steps

### Report Missing oleh Pelapor admin menulis node, log, baris Transaction log aset, Transaction admin log, dan event
1. Catat jumlah entri Activity Log dan System Log Aktor Missing A, jumlah entri Transaction admin log Aktor Missing A, jumlah baris Transaction log aset aset DU-077-1, jumlah notifikasi `missing_reported`, dan jumlah node serta entri log record DU-077-5 sebelum aksi pertama
2. Aktor Missing A melakukan Report Missing atas aset DU-077-1 sebagai Pelapor admin dengan What happened `Aset tidak ada di rak penyimpanan saat inventaris`
3. Verifikasi aset DU-077-1 mendapat record berstatus `Missing` yang memuat satu node `Reported missing by` dengan pelapor Aktor Missing A, dan status global aset menjadi `Missing`
4. Verifikasi Activity Log Aktor Missing A bertambah satu entri dengan entity `Missing record` dan object path `Missing`, dan System Log Aktor Missing A bertambah satu entri atas aksi pengguna itu
5. Verifikasi Transaction log aset aset DU-077-1 bertambah satu baris untuk `Reported missing by` dengan Status `Missing` dan User Aktor Missing A, memuat hanya kolom Date, Status, dan User tanpa Transaction ID, Reader name, Group, dan Requested by, dengan Date mengikuti Date Format `DD/MM/YY` dan Time Format `HH:mm`
6. Verifikasi Transaction admin log Aktor Missing A bertambah satu entri dengan Activity `Reported missing` tanpa akhiran `by [Pelaku]` dan tanpa badge, Name berupa nama aset DU-077-1 diikuti increment, Source sama dengan Source record DU-077-1, Group `Head Office` sebagai grup aset saat aksi dieksekusi, dan aktor entri berperan Pelapor
7. Verifikasi satu notifikasi `missing_reported` dikirim untuk record DU-077-1 dan tidak ada notifikasi `missing_holder_reported` untuk record itu
8. Verifikasi Modified By record DU-077-1 menampilkan Aktor Missing A dan Last Updated record DU-077-1 berisi waktu aksi tersebut
9. Verifikasi aksi atas record DU-077-1 tidak membuat entri Changelog dan riwayat record hanya terbaca di Missing Log

### Report Missing banyak aset menulis satu record, satu node, dan satu entri log per aset yang diproses
10. Catat jumlah entri Activity Log dan System Log Aktor Missing A, jumlah entri Transaction admin log Aktor Missing A, jumlah node record DU-077-4, jumlah baris Transaction log aset aset DU-077-4, dan jumlah entri log serta node record DU-077-5 sebelum aksi
11. Aktor Missing A melakukan Report Missing banyak aset sekaligus atas aset DU-077-2, DU-077-3, dan DU-077-4 dengan What happened `Beberapa aset tidak ditemukan saat inventaris bulanan`
12. Verifikasi aset DU-077-2 dan DU-077-3 masing-masing mendapat satu record berstatus `Missing` dengan satu node `Reported missing by`, sehingga laporan banyak aset menghasilkan satu record dan satu node per aset
13. Verifikasi aset DU-077-4 dilewati karena sudah punya record berjalan: tidak ada record baru, tidak ada node baru pada record DU-077-4, dan tidak ada baris baru di Transaction log aset aset DU-077-4
14. Verifikasi Activity Log dan System Log Aktor Missing A masing-masing bertambah dua entri, satu per aset DU-077-2 dan DU-077-3, tanpa entri untuk aset DU-077-4 yang dilewati
15. Verifikasi Transaction admin log Aktor Missing A bertambah dua entri, satu baris per aset DU-077-2 dan DU-077-3, tanpa baris untuk aset DU-077-4
16. Verifikasi status global aset DU-077-2 dan DU-077-3 menjadi `Missing` bersama record masing-masing dalam satu penulisan atomik per aset, sedangkan aset DU-077-4 tidak berubah
17. Verifikasi record DU-077-5 tidak mendapat node, entri log, baris Transaction log aset, maupun notifikasi baru dibanding sebelum aksi

### Laporan pemegang yang di-Confirm menulis log, event, dan sinyal task selesai
18. Catat jumlah notifikasi `missing_holder_reported` dan `missing_holder_resolved`, jumlah baris Transaction log aset aset DU-077-6, jumlah entri Transaction admin log Pemegang dan Aktor Missing A, serta jumlah entri Activity Log dan System Log Pemegang sebelum aksi
19. Pemegang melakukan Report Missing atas aset DU-077-6 dengan What happened `Aset hilang dari tas saat perjalanan dinas`
20. Verifikasi aset DU-077-6 mendapat record berstatus `Waiting for Confirmation` dengan satu node `Reported missing by` dan status global aset `Missing`
21. Verifikasi Transaction log aset aset DU-077-6 bertambah satu baris `Reported missing by` dengan Status `Waiting for Confirmation`
22. Verifikasi satu notifikasi `missing_holder_reported` dikirim ke Aktor Missing pada Group aset DU-077-6 dan tidak ada notifikasi `missing_reported` untuk record itu
23. Verifikasi baris transaksi aset DU-077-6 menampilkan badge `Reported Missing`
24. Verifikasi laporan pemegang itu tidak dicatat di Transaction admin log Pemegang maupun Aktor Missing A, sedangkan Activity Log dan System Log Pemegang masing-masing bertambah satu entri
25. Aktor Missing A melakukan Confirm atas record aset DU-077-6
26. Verifikasi status record aset DU-077-6 menjadi `Missing` dengan satu node `Report confirmed by` yang memuat Closed lines berupa nomor transaksi dan jenis baris yang ditutup
27. Verifikasi baris transaksi aset DU-077-6 ditutup bersama perubahan status record dalam satu penulisan atomik dan status global aset tetap `Missing`
28. Verifikasi Transaction log aset aset DU-077-6 bertambah satu baris `Report confirmed` dengan Status `Missing`, dan Transaction admin log Aktor Missing A bertambah satu entri `Report confirmed` dengan aktor berperan Aktor Missing
29. Verifikasi satu notifikasi `missing_holder_resolved` dikirim untuk record aset DU-077-6 dan sinyal task selesai dikirim untuk laporan itu
30. Verifikasi Modified By record aset DU-077-6 menampilkan Aktor Missing A, bukan Pemegang yang melapor, dan Activity Log serta System Log Aktor Missing A masing-masing bertambah satu entri

### Laporan pemegang yang di-Reject menulis log, event, dan sinyal task selesai
31. Pemegang melakukan Report Missing atas aset DU-077-7 dengan What happened `Aset hilang dari tas saat perjalanan dinas`
32. Catat jumlah notifikasi `missing_holder_resolved`, jumlah baris Transaction log aset aset DU-077-7, dan jumlah entri Transaction admin log Aktor Missing B sebelum Reject
33. Aktor Missing B melakukan Reject atas record aset DU-077-7 dengan Reason `Laporan belum disertai bukti yang cukup`
34. Verifikasi status record aset DU-077-7 menjadi `Rejected` dengan satu node `Report rejected by` yang memuat Reason `Laporan belum disertai bukti yang cukup`
35. Verifikasi status global aset DU-077-7 dihitung ulang dari state aset terkini menjadi `Assigned` bersama status record dalam satu penulisan atomik, dan badge `Reported Missing` pada baris transaksi aset DU-077-7 hilang
36. Verifikasi Transaction log aset aset DU-077-7 bertambah satu baris `Report rejected` dengan Status `Rejected`, dan Transaction admin log Aktor Missing B bertambah satu entri `Report rejected` dengan aktor berperan Aktor Missing
37. Verifikasi satu notifikasi `missing_holder_resolved` dikirim untuk record aset DU-077-7 dan sinyal task selesai dikirim untuk laporan itu

### Cancel Report oleh pemegang menulis node tanpa baris Transaction log aset, tanpa Transaction admin log, dan tanpa notifikasi baru
38. Pemegang melakukan Report Missing atas aset DU-077-8 dengan What happened `Aset hilang dari tas saat perjalanan dinas`
39. Catat jumlah notifikasi `missing_*`, jumlah baris Transaction log aset aset DU-077-8, jumlah entri Transaction admin log Pemegang, serta jumlah entri Activity Log dan System Log Pemegang sebelum Cancel Report
40. Pemegang melakukan Cancel Report atas laporannya sendiri pada aset DU-077-8
41. Verifikasi status record aset DU-077-8 menjadi `Canceled` dengan satu node `Report canceled by`, dan status global aset dihitung ulang menjadi `Borrowed` karena aset masih dipegang
42. Verifikasi pengingat baris transaksi aset DU-077-8 berjalan lagi
43. Verifikasi Cancel Report atas aset DU-077-8 tidak menambah baris Transaction log aset, tidak menambah entri Transaction admin log Pemegang, dan tidak memicu notifikasi `missing_*` baru dibanding sebelum aksi
44. Verifikasi Activity Log dan System Log Pemegang masing-masing bertambah satu entri atas aksi Cancel Report

### Laporan dari Task Detail sesi pemeriksaan oleh pelapor tanpa hak Aktor Missing
45. Catat jumlah notifikasi `missing_holder_reported` dan `missing_*` lainnya, jumlah baris Transaction log aset aset DU-077-9, serta jumlah entri Transaction admin log Pelapor sesi sebelum aksi
46. Pelapor sesi melakukan Report Missing atas aset DU-077-9 dari Task Detail sesi pemeriksaan dengan What happened `Aset tidak ada di lokasi saat pemeriksaan berlangsung`
47. Verifikasi aset DU-077-9 mendapat record berstatus `Waiting for Confirmation` dengan Source `Audit` dan satu node `Reported missing by`, dan status global aset langsung `Missing`
48. Verifikasi satu notifikasi `missing_holder_reported` dikirim ke Aktor Missing pada Group aset DU-077-9, penerima sama dengan laporan pemegang, dan tidak ada notifikasi `missing_reported` untuk record itu
49. Verifikasi Transaction admin log Pelapor sesi bertambah satu entri `Reported missing` dengan Source `Audit` dan aktor berperan Pelapor, dicatat hanya di sub-tab Missing dan tidak di sub-tab transaksi asal laporan
50. Verifikasi Transaction log aset aset DU-077-9 bertambah satu baris `Reported missing by` dengan Status `Waiting for Confirmation`
51. Pelapor sesi melakukan Cancel my report atas record aset DU-077-9 dari Task Detail sesi pemeriksaan
52. Verifikasi status record aset DU-077-9 menjadi `Canceled` dengan satu node `Report canceled by`, dan tidak ada notifikasi tambahan dibanding sesudah laporan
53. Verifikasi Transaction admin log Pelapor sesi bertambah satu entri `Report canceled` dengan aktor berperan Pelapor, tanpa baris baru di Transaction log aset aset DU-077-9

### Add Update tidak idempotent dan Mark as Found oleh aktor lain menulis log serta event
54. Catat jumlah node record DU-077-10, jumlah notifikasi `missing_*`, jumlah baris Transaction log aset aset DU-077-10, jumlah entri Transaction admin log Aktor Missing A dan Aktor Missing B, serta jumlah entri TAG Log aset DU-077-10 sebelum aksi
55. Aktor Missing A melakukan Add Update atas record DU-077-10 dengan Update `Tim keamanan sudah memeriksa rekaman kamera lantai dua`
56. Verifikasi record DU-077-10 memuat satu node `Update added by` baru, dan Transaction admin log Aktor Missing A bertambah satu entri `Update added` dengan aktor berperan Aktor Missing
57. Verifikasi Add Update tidak menambah baris Transaction log aset aset DU-077-10 dan tidak memicu notifikasi `missing_*` baru dibanding sebelum aksi
58. Aktor Missing A melakukan Add Update atas record DU-077-10 sekali lagi dengan Update `Pemeriksaan ruang arsip belum menemukan aset`
59. Verifikasi record DU-077-10 memuat dua node `Update added by` karena tiap Submit membuat node baru, dan Transaction admin log Aktor Missing A bertambah satu entri lagi
60. Aktor Missing B melakukan Mark as Found atas record DU-077-10 dengan Found at `Head Office` dan Asset Status `Normal`
61. Verifikasi status record DU-077-10 menjadi `Found` dengan satu node `Marked as found by`, dan status global aset berubah bersama status record dalam satu penulisan atomik tanpa Damage Report baru karena Asset Status `Normal`
62. Verifikasi Transaction log aset aset DU-077-10 bertambah satu baris `Marked as found` dengan Status `Found`, dan Transaction admin log Aktor Missing B bertambah satu entri `Marked as found` dengan aktor berperan Aktor Missing
63. Verifikasi satu notifikasi `missing_resolved` dikirim untuk record DU-077-10
64. Verifikasi Modified By record DU-077-10 menampilkan Aktor Missing B sebagai pelaku aksi terakhir dan bukan Aktor Missing A yang melaporkan, dan Activity Log serta System Log Aktor Missing B masing-masing bertambah satu entri
65. Verifikasi Mark as Found atas record DU-077-10 tidak menambah entri TAG Log aset DU-077-10 dan tidak membuat entri Changelog

### Report Disposal oleh Aktor Disposal ditulis sebagai node tanpa event Missing, lalu Decline mengembalikan ke Missing
66. Catat jumlah notifikasi `missing_*`, jumlah baris Transaction log aset aset DU-077-11, jumlah entri Transaction admin log Aktor Missing A sub-tab Missing, serta jumlah entri Activity Log dan System Log Aktor Missing A sebelum aksi
67. Aktor Missing A melakukan Report Disposal atas record DU-077-11 dengan Reason `Aset sudah dicari berbulan-bulan tanpa hasil`
68. Verifikasi status record DU-077-11 menjadi `Reported Disposal` dengan satu node `Disposal reported by` yang memuat Reason `Aset sudah dicari berbulan-bulan tanpa hasil` dan tanpa Report ID
69. Verifikasi Activity Log Aktor Missing A bertambah satu entri atas Report Disposal dan System Log Aktor Missing A bertambah satu entri karena ada user aktor
70. Verifikasi Report Disposal atas record DU-077-11 tidak memicu notifikasi `missing_*` baru, tidak menambah baris Transaction log aset, dan tidak menambah entri Transaction admin log sub-tab Missing karena dicatat di sub-tab Disposal
71. Aktor Missing A melakukan Decline atas Disposal Report record DU-077-11 sebagai Aktor Disposal dengan Reason `Pencarian lanjutan masih akan dilakukan bulan ini`
72. Verifikasi status record DU-077-11 kembali `Missing` dengan satu node `Disposal report declined by` yang memuat Reason `Pencarian lanjutan masih akan dilakukan bulan ini` dan Back to Missing `Yes`, tanpa Report ID
73. Verifikasi Decline atas record DU-077-11 tidak memicu notifikasi `missing_*` baru dan tidak menambah baris Transaction log aset

### Cancel Disposal Report oleh aktor lain menulis node dengan Back to Missing
74. Catat jumlah notifikasi `missing_*`, jumlah baris Transaction log aset aset DU-077-12, serta jumlah entri Activity Log dan System Log Aktor Missing B sebelum aksi
75. Aktor Missing B melakukan Cancel Disposal Report atas record DU-077-12 yang Report-nya dibuat Aktor Missing A
76. Verifikasi status record DU-077-12 kembali `Missing` dengan satu node `Disposal report canceled by` yang memuat Back to Missing `Yes` dan tanpa Report ID
77. Verifikasi Activity Log Aktor Missing B bertambah satu entri atas Cancel Disposal Report dan Modified By record DU-077-12 menampilkan Aktor Missing B, bukan Aktor Missing A yang membuat Report
78. Verifikasi Cancel Disposal Report atas record DU-077-12 tidak memicu notifikasi `missing_*` baru dan tidak menambah baris Transaction log aset

### Dispose dengan Submit Request dan eksekusi Disposal
79. Catat jumlah notifikasi `missing_*` untuk record DU-077-13 dan DU-077-14 sebelum aksi
80. Aktor Disposal melakukan Dispose atas Report record DU-077-13 dengan Submit Request jenis Write-off
81. Verifikasi status record DU-077-13 menjadi `In Disposal Process` tanpa notifikasi `missing_*` baru dibanding sebelum aksi
82. Aktor Disposal melakukan Execute atas baris Disposal Write-off record DU-077-14
83. Verifikasi status record DU-077-14 menjadi `Disposed` dengan satu node `Disposed`
84. Verifikasi satu notifikasi `missing_resolved` dikirim untuk record DU-077-14 saat Disposal dieksekusi
85. Verifikasi Transaction log aset aset DU-077-14 bertambah satu baris `Disposed` dengan Status `Disposed`

### Reject, Cancel, Remove, dan timeout atas baris Disposal mengembalikan ke Reported Disposal tanpa event Missing
86. Catat jumlah notifikasi `missing_*` untuk record DU-077-15, DU-077-16, DU-077-17, dan DU-077-18, serta jumlah entri Activity Log dan System Log pelaku aksi sebelum aksi
87. Approver Disposal melakukan Reject atas baris Disposal Write-off record DU-077-15
88. Verifikasi status record DU-077-15 menjadi `Reported Disposal` dan Disposal Report kembali `Reported`, tanpa notifikasi `missing_*` baru, dan Activity Log approver bertambah satu entri atas peristiwa itu
89. Pembuat Request Disposal melakukan Cancel atas baris Disposal Write-off record DU-077-16
90. Verifikasi status record DU-077-16 menjadi `Reported Disposal` dan Disposal Report kembali `Reported`, tanpa notifikasi `missing_*` baru
91. Aktor Disposal melakukan Remove atas baris Disposal Write-off record DU-077-17
92. Verifikasi status record DU-077-17 menjadi `Reported Disposal` dan Disposal Report kembali `Reported`, tanpa notifikasi `missing_*` baru
93. Waktu berlalu sampai baris Disposal Write-off record DU-077-18 habis waktu tanpa keputusan
94. Verifikasi status record DU-077-18 menjadi `Reported Disposal` dan Disposal Report kembali `Reported`, tanpa notifikasi `missing_*` baru
95. Verifikasi peristiwa habis waktu itu dicatat di Activity Log dengan Modified By `System` dan tanpa entri System Log aktor

### Report Missing menutup Report atau baris Disposal dari modul Disposal oleh System tanpa node Missing Log
96. Catat jumlah entri Activity Log dan System Log Aktor Missing A serta jumlah notifikasi `missing_reported` sebelum aksi
97. Aktor Missing A melakukan Report Missing atas aset DU-077-19 dengan What happened `Aset tidak ada di rak penyimpanan saat inventaris`
98. Verifikasi aset DU-077-19 mendapat record Missing baru yang Missing Log-nya dimulai dari node `Reported missing by` dan tidak memuat node apa pun dari penutupan Report
99. Verifikasi Disposal Report aset DU-077-19 berstatus `Canceled` oleh `System` dengan alasan `Asset reported missing`, tanpa notifikasi `missing_*` selain satu `missing_reported` dari Report Missing
100. Aktor Missing A melakukan Report Missing atas aset DU-077-20 dengan What happened `Aset tidak ada di rak penyimpanan saat inventaris`
101. Verifikasi baris Disposal berjenis Sell `Waiting for Approval` aset DU-077-20 menjadi `Canceled` oleh `System` dengan alasan `Asset reported missing`, baris `Draft` tidak diubah, dan aset ditandai ⚠
102. Verifikasi record Missing aset DU-077-20 dimulai dari node `Reported missing by` tanpa node dari penutupan baris Disposal, dan tidak ada notifikasi `missing_*` baru dari penutupan itu selain satu `missing_reported`

### Deteksi scan ditulis oleh System tanpa System Log
103. Catat jumlah entri Activity Log dan System Log, jumlah baris Transaction log aset aset DU-077-21, jumlah notifikasi `missing_detected`, serta nilai Modified By dan Last Updated record DU-077-21 sebelum scan
104. Reader DU-077-22 membaca TAG `QR-077-0001` milik aset DU-077-21
105. Verifikasi record DU-077-21 memuat satu node `Detected by scan` dengan pemindai `Gate A reader`
106. Verifikasi Activity Log mencatat deteksi itu dengan Modified By `System` dan System Log tidak mendapat entri aktor
107. Verifikasi Modified By record DU-077-21 menjadi `System` dan Last Updated record DU-077-21 diperbarui ke waktu deteksi
108. Verifikasi satu notifikasi `missing_detected` dikirim untuk node itu dan Last seen record DU-077-21 diperbarui bersama node tanpa menunggu job terjadwal
109. Verifikasi deteksi scan tidak menambah baris Transaction log aset aset DU-077-21

### Job Long missing ditulis oleh System tanpa System Log dan tidak mengirim ulang notifikasi
110. Catat jumlah entri Activity Log dan System Log, jumlah baris Transaction log aset aset DU-077-23, dan jumlah notifikasi `missing_long` sebelum job berjalan
111. Waktu berlalu sampai 31 hari sejak laporan record DU-077-23 dibuat
112. Job Long missing harian berjalan
113. Verifikasi record DU-077-23 memuat satu node `Long missing` dengan Days missing sesuai selisih hari sejak laporan dan tetap berstatus `Missing`
114. Verifikasi satu notifikasi `missing_long` dikirim untuk record DU-077-23
115. Verifikasi Activity Log mencatat penanda itu dengan Modified By `System`, System Log tidak mendapat entri aktor, dan Modified By serta Last Updated record DU-077-23 menampilkan `System` dan waktu job
116. Verifikasi job tidak menambah baris Transaction log aset aset DU-077-23
117. Job Long missing harian berjalan pada hari berikutnya
118. Verifikasi notifikasi `missing_long` untuk record DU-077-23 tidak bertambah dan record tidak mendapat node `Long missing` kedua

### I found it menulis node di log pengguna dengan notifikasi paling banyak sekali per jam per pengguna
119. Catat jumlah notifikasi `missing_found_reported` untuk record DU-077-24 dan jumlah entri Activity Log dan System Log Penemu A dan Penemu B sebelum aksi
120. Penemu A melakukan I found it atas record DU-077-24 dengan Location `-6.2088, 106.8456`
121. Verifikasi record DU-077-24 memuat satu node `Reported found by` dengan Location `-6.2088, 106.8456`, sedangkan status record tetap `Missing` dan status global aset tidak berubah
122. Verifikasi Activity Log dan System Log Penemu A masing-masing bertambah satu entri atas aksi pengguna itu
123. Verifikasi satu notifikasi `missing_found_reported` dikirim ke Aktor Missing untuk record DU-077-24
124. Penemu A melakukan I found it atas record DU-077-24 sekali lagi dalam jendela 1 jam
125. Verifikasi record DU-077-24 memuat dua node `Reported found by` dari Penemu A tanpa notifikasi `missing_found_reported` baru
126. Penemu B melakukan I found it atas record DU-077-24 tanpa Location
127. Verifikasi record DU-077-24 memuat node `Reported found by` dari Penemu B dengan Location `—` dan satu notifikasi `missing_found_reported` baru karena pengguna berbeda
128. Waktu berlalu sampai lebih dari 1 jam sejak I found it pertama Penemu A
129. Penemu A melakukan I found it atas record DU-077-24 dengan Location `-6.9175, 107.6191`
130. Verifikasi satu notifikasi `missing_found_reported` baru dikirim untuk Penemu A karena jendela 1 jam sudah lewat
131. Aktor Missing B melakukan I found it atas record DU-077-24 sebagai pengguna terautentikasi
132. Verifikasi Aktor Missing B tercatat sebagai penemu pada node `Reported found by` baru dan Activity Log serta System Log Aktor Missing B bertambah satu entri atas aksi itu
133. Verifikasi I found it tidak menambah baris Transaction log aset record DU-077-24, tidak menambah entri Transaction admin log, dan tidak mengubah status record maupun status global aset

### Bulk Report Disposal menulis satu node per record yang diproses dan tidak menulis untuk record yang dilewati
134. Catat jumlah node record DU-077-25, DU-077-26, dan DU-077-27 serta jumlah entri Activity Log dan System Log Aktor Missing A sebelum aksi
135. Aktor Missing A melakukan Bulk Report Disposal atas record DU-077-25, DU-077-26, dan DU-077-27 dengan Reason `Aset dinyatakan hilang permanen setelah pencarian ulang`
136. Verifikasi record DU-077-25 dan DU-077-26 masing-masing menjadi `Reported Disposal` dengan satu node `Disposal reported by` yang memuat Reason `Aset dinyatakan hilang permanen setelah pencarian ulang`
137. Verifikasi record DU-077-27 dilewati karena sudah bukan `Missing`: tidak ada node baru dan tidak ada entri log baru untuk record itu
138. Verifikasi Activity Log dan System Log Aktor Missing A masing-masing bertambah dua entri, satu per record yang diproses

### Unduh tidak dicatat dan aksi tidak plan-gated
139. Catat jumlah entri Activity Log, System Log, dan Transaction admin log Aktor Missing A sebelum unduh
140. Aktor Missing A mengunduh daftar record tab Active
141. Verifikasi unduh tidak menambah entri Activity Log, System Log, maupun Transaction admin log Aktor Missing A
142. Verifikasi aksi Report Missing, Confirm, Reject, Mark as Found, dan Add Update di spec ini tetap menulis node, entri log, dan event pada client berplan `Basic` karena tidak plan-gated
143. Verifikasi record DU-077-5 tidak mendapat node, entri log, baris Transaction log aset, atau notifikasi apa pun sepanjang spec ini dan Modified By serta Last Updated-nya tidak berubah

### Pelapor Disposal Manage asset & TAG dengan Update membatalkan laporannya sendiri menulis node atas namanya
144. Catat jumlah node record DU-077-40 sebelum aksi
145. Pelapor Disposal melakukan Cancel Disposal Report atas laporannya sendiri pada record DU-077-40
146. Verifikasi status record DU-077-40 kembali `Missing` dengan satu node `Disposal report canceled by` baru yang memuat Pelapor Disposal sebagai aktor dan Back to Missing `Yes`, tanpa Report ID
