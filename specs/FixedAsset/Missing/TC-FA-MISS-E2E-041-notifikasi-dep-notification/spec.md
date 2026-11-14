---
id: TC-FA-MISS-E2E-041-notifikasi-dep-notification
title: "Event notifikasi Missing: tiap aksi memicu event yang dinyatakan dan transisi Disposal tidak memicu event missing_*"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.8#p1", "§9.8#r1", "§9.8#r2", "§9.8#r3", "§9.8#r4", "§9.8#r5", "§9.8#r6", "§9.8#r7", "§9.8#p2", "§9.8#p3", "§11#r16", "§11#r17", "§1.2#r62", "§1.2#r106", "§1.2#r111", "§9.4.4#r2", "§9.4.4#r18", "§9.4.4#r19", "§9.2#b33", "§9.7#r1", "§9.7#r2", "§9.7#r3", "§9.7#r4", "§9.7#r5", "§9.7#r7", "§9.7#r10", "§9.4.2#r7", "§3#p2", "§4.2.3#p2", "§4.2.4#r15", "§4.2.4#r16", "§9.2#b15"]
smoke: []
dependsOn: ["Notification: daftar notifikasi in-app"]
trace:
  "§9.8#p1": [17]
  "§9.8#r1": [17, 18]
  "§9.8#r2": [22]
  "§9.8#r3": [29, 30]
  "§9.8#r4": [42]
  "§9.8#r5": [44]
  "§9.8#r6": [43]
  "§9.8#r7": [34, 38]
  "§9.8#p2": [41]
  "§9.8#p3": [35]
  "§11#r16": [17, 22, 29, 34, 42, 43, 44]
  "§11#r17": [23, 24]
  "§1.2#r62": [45]
  "§1.2#r106": [42]
  "§1.2#r111": [43]
  "§9.4.4#r2": [17, 18, 22]
  "§9.4.4#r18": [23, 24]
  "§9.4.4#r19": [29, 30]
  "§9.2#b33": [29, 30]
  "§9.7#r1": [17]
  "§9.7#r2": [22]
  "§9.7#r3": [30]
  "§9.7#r4": [34]
  "§9.7#r5": [38]
  "§9.7#r7": [43]
  "§9.7#r10": [44]
  "§9.4.2#r7": [30]
  "§3#p2": [17, 18]
  "§4.2.3#p2": [6, 12]
  "§4.2.4#r15": [6]
  "§4.2.4#r16": [12]
  "§9.2#b15": [53, 56]
anchor: []
coverage:
  web: automated
---

# Event notifikasi Missing: tiap aksi memicu event yang dinyatakan dan transisi Disposal tidak memicu event missing_*

## Prerequisites
- Aktor: Total Control `Rina W` sebagai penerima notifikasi. Aktor lain yang memicu perubahan: Total Control `Dewi Anggraini {runId}`, pemegang `Joko Santoso {runId}` tanpa hak Aktor Missing, dan pemegang `Andi Pratama {runId}` dengan hak Manage asset & TAG (Update) pada Group asetnya.
- Layar awal: daftar notifikasi in-app.
- Data:
  - DU-041-1: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, dipegang `Sari Dewanti {runId}`, tanpa record Missing.
  - DU-041-2: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, tanpa pemegang, tanpa record Missing.
  - DU-041-3: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, dipegang `Joko Santoso {runId}`, tanpa record Missing.
  - DU-041-4: Asset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, dipegang `Andi Pratama {runId}`, tanpa record Missing.
  - DU-041-5: Asset `Camera Canon EOS {runId}`, Group `Head Office`, dipegang `Joko Santoso {runId}`, dengan record Missing `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
  - DU-041-6: Asset `Projector Epson EB-X06 {runId}`, Group `Head Office`, tanpa TAG, dengan record Missing berstatus `Missing` dan notifikasi `missing_reported` yang belum terbaca.
  - DU-041-7: Asset `Drill Bosch GSB {runId}`, Group `Warehouse`, dengan record Missing berstatus `In Disposal Process`.
  - DU-041-8: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing` yang tidak membawa notifikasi event `missing_*` apa pun sebelum spec mulai.
  - DU-041-9: Asset `Toyota Innova {runId}`, Group `Branch Surabaya`, dengan record Missing berstatus `Missing` yang punya node `Detected by scan` dan notifikasi `missing_detected` yang sudah terkirim.
  - DU-041-10: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, dengan record Missing berstatus `Missing` yang dilaporkan pada `T0 − 34 hari`, punya penanda `Long missing`, dan satu notifikasi `missing_long` yang sudah terkirim.
  - DU-041-11: Asset `Handheld Honeywell CT60 {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing` yang punya node `Reported found by` dan notifikasi `missing_found_reported` yang sudah terkirim.
  - DU-041-12: Asset `Server Dell PowerEdge {runId}`, Group `Head Office`, tanpa pemegang, tanpa record Missing.
  - DU-041-13: Asset `Meja Rapat Kayu {runId}`, Group `Head Office`, dengan record Missing `Waiting for Confirmation` yang dilaporkan pemegang pada `T0 − 40 hari` dan satu notifikasi `missing_holder_reported`.
  - DU-041-14: Pengguna `Dewi Anggraini {runId}`, Total Control.
  - DU-041-15: Pengguna `Joko Santoso {runId}`, pemegang tanpa hak Aktor Missing.
  - DU-041-16: Pengguna `Andi Pratama {runId}`, pemegang dengan hak Manage asset & TAG (Update).
  - DU-041-17: Pengguna `Sari Dewanti {runId}`, pemegang tanpa hak Aktor Missing.
  - DU-041-18: Pengguna `Rina W`, Total Control.
  - DU-041-19: What happened `Monitor tidak ada di meja kerja setelah pindah lantai`.
  - DU-041-20: What happened `Printer tidak ada di ruang cetak saat pengecekan`.
  - DU-041-21: What happened `Scanner tidak ada di loker setelah shift malam`.
  - DU-041-22: What happened `Laptop tidak ada di meja setelah perjalanan dinas`.
  - DU-041-23: Reason `Kamera masih dipakai di lapangan`.
  - DU-041-24: Note `Ditemukan di mobil operasional`.
  - DU-041-25: Reason `Aset tidak ditemukan setelah penelusuran`.
  - DU-041-26: What happened `Server tidak ditemukan di rak setelah pemindahan ruang server`.
  - DU-041-27: What happened `Server tidak ada di ruang server saat inventarisasi`.
- Kondisi:
  - Akun `Rina W`, `Dewi Anggraini {runId}`, `Joko Santoso {runId}`, dan `Andi Pratama {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Missing oleh Pelapor admin memicu missing_reported
1. Masuk sebagai `Dewi Anggraini {runId}`
2. Buka halaman `Assets`
3. Ketik Search `Monitor LG 27UL500 {runId}`, tekan Enter
4. Buka menu `⋯` pada baris `Monitor LG 27UL500 {runId}`
5. Klik `Report Missing`
6. Verifikasi kotak dampak memuat baris pemegang `Sari Dewanti {runId}` diikuti `and the asset admins will be notified.`
7. Isi What happened `Monitor tidak ada di meja kerja setelah pindah lantai`
8. Klik `[Report Missing]` pada dialog
9. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
10. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`
11. Klik `Report Missing`
12. Verifikasi kotak dampak memuat baris `The asset admins will be notified.`
13. Isi What happened `Printer tidak ada di ruang cetak saat pengecekan`
14. Klik `[Report Missing]` pada dialog
15. Masuk sebagai `Rina W`
16. Buka daftar notifikasi
17. Verifikasi notifikasi event `missing_reported` atas `Monitor LG 27UL500 {runId}` tampil di daftar notifikasi
18. Verifikasi notifikasi event `missing_reported` atas `Printer HP LaserJet M404 {runId}` tampil di daftar notifikasi

### Laporan pemegang memicu missing_holder_reported dan laporan pemegang berhak memicu missing_reported
19. `Joko Santoso {runId}` melaporkan `Scanner Zebra DS2208 {runId}` hilang lewat Report Missing sebagai pemegang dengan What happened `Scanner tidak ada di loker setelah shift malam`
20. `Andi Pratama {runId}` melaporkan `Laptop Lenovo ThinkPad T14 {runId}` hilang lewat Report Missing sebagai pemegang dengan What happened `Laptop tidak ada di meja setelah perjalanan dinas`
21. Muat ulang halaman
22. Verifikasi notifikasi event `missing_holder_reported` atas `Scanner Zebra DS2208 {runId}` tampil di daftar notifikasi
23. Verifikasi notifikasi event `missing_reported` atas `Laptop Lenovo ThinkPad T14 {runId}` tampil di daftar notifikasi
24. Verifikasi tidak ada notifikasi event `missing_holder_reported` atas `Laptop Lenovo ThinkPad T14 {runId}` di daftar notifikasi

### Confirm dan Reject laporan pemegang memicu missing_holder_resolved
25. Rina W melakukan Confirm atas laporan `Scanner Zebra DS2208 {runId}`
26. Rina W melakukan Reject atas laporan `Camera Canon EOS {runId}` dengan Reason `Kamera masih dipakai di lapangan`
27. Masuk sebagai `Joko Santoso {runId}`
28. Buka daftar notifikasi
29. Verifikasi notifikasi event `missing_holder_resolved` atas `Scanner Zebra DS2208 {runId}` tampil di daftar notifikasi
30. Verifikasi notifikasi event `missing_holder_resolved` atas `Camera Canon EOS {runId}` tampil di daftar notifikasi

### Mark as Found memicu missing_resolved dan menandai notifikasi tugas selesai
31. `Dewi Anggraini {runId}` melakukan Mark as Found atas `Projector Epson EB-X06 {runId}` dengan Note `Ditemukan di mobil operasional`
32. Masuk sebagai `Rina W`
33. Buka daftar notifikasi
34. Verifikasi notifikasi event `missing_resolved` atas `Projector Epson EB-X06 {runId}` tampil di daftar notifikasi
35. Verifikasi notifikasi event `missing_reported` atas `Projector Epson EB-X06 {runId}` berstatus terbaca

### Disposal Executed memicu missing_resolved dan transisi Disposal lain tidak memicu event missing_*
36. `Dewi Anggraini {runId}` melakukan Execute atas baris Disposal `Drill Bosch GSB {runId}`
37. Muat ulang halaman
38. Verifikasi notifikasi event `missing_resolved` atas `Drill Bosch GSB {runId}` tampil di daftar notifikasi
39. `Dewi Anggraini {runId}` melakukan Report Disposal atas `Hand Pallet Truck {runId}` dengan Reason `Aset tidak ditemukan setelah penelusuran`
40. Muat ulang halaman
41. Verifikasi tidak ada notifikasi event `missing_*` atas `Hand Pallet Truck {runId}` di daftar notifikasi

### Event dari job dan deteksi tampil sebagai notifikasi
42. Verifikasi notifikasi event `missing_detected` atas `Toyota Innova {runId}` tampil di daftar notifikasi
43. Verifikasi notifikasi event `missing_long` atas `Laptop Dell Latitude 5420 {runId}` tampil tepat satu di daftar notifikasi
44. Verifikasi notifikasi event `missing_found_reported` atas `Handheld Honeywell CT60 {runId}` tampil di daftar notifikasi

### Laporan pemegang yang menunggu lama tidak menambah notifikasi
45. Verifikasi daftar notifikasi atas `Meja Rapat Kayu {runId}` hanya memuat notifikasi event `missing_holder_reported` dan tidak ada notifikasi tambahan

### Laporan kedua pada aset yang sama tidak memicu notifikasi
46. Buka halaman `Assets`
47. Ketik Search `Server Dell PowerEdge {runId}`, tekan Enter
48. Buka menu `⋯` pada baris `Server Dell PowerEdge {runId}`
49. Klik `Report Missing`
50. `Dewi Anggraini {runId}` melaporkan `Server Dell PowerEdge {runId}` hilang lewat Report Missing dengan What happened `Server tidak ditemukan di rak setelah pemindahan ruang server`
51. Isi What happened `Server tidak ada di ruang server saat inventarisasi`
52. Klik `[Report Missing]` pada dialog
53. Verifikasi Alert pada dialog menyebut `Server Dell PowerEdge {runId}` dan `Dewi Anggraini {runId}` dengan teks `was just reported missing by`
54. Klik `[Cancel]` pada dialog
55. Buka daftar notifikasi
56. Verifikasi notifikasi event `missing_reported` atas `Server Dell PowerEdge {runId}` hanya satu di daftar notifikasi
