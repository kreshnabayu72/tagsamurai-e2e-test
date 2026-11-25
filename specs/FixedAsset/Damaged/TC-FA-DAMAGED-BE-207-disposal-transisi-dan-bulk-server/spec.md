---
id: TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server
title: "Server mengikuti Disposal Report dan baris Disposal untuk status record, memproses Bulk Report Disposal per record dengan pengecekan ganda, memblok lintas Group, dan membatasi Cancel Disposal Report pada Reported Disposal"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r20", "§Aturan Logika Modul#r21", "§Aturan Logika Modul#r22", "§Aturan Logika Modul#r63", "§Aturan Logika Modul#r64", "§Aturan Logika Modul#r65", "§9.2#r3", "§9.2#r4", "§9.2#r6", "§9.2#b13", "§9.2#b24", "§9.2#b25", "§9.2#b26", "§6#p2", "§8.1#p2", V-DMG-06, V-DMG-08, V-DMG-09, D-DMG-13, TS-DMG-09, TS-DISP-12, TS-DISP-15, "§9.6#r8", EC-DMG-17, EC-DMG-21, EC-DMG-35, "§9.4.4#r11", "§9.4.4#r12", "§9.4.4#r28", "§9.4.4#r29", "§9.4.4#r30", "§9.7#r10", "§9.7#r11", "§9.7#r12", "§9.7#r13", "§9.7#r14", "§9.4.1#r9", "§3#p7", F-DMG-06, "§9.2#b8", "§Aturan Logika Modul#r19", "§9.4.2#r32", "§4.2.4#r10", "§4.2.4#r11", T-DMG-01, "§8.1#r14", "§8.1#r15", "§9.2#r2"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r20": [2, 26, 59, 94, 96, 97]
  "§Aturan Logika Modul#r21": [32, 34]
  "§Aturan Logika Modul#r22": [36, 38, 40, 42]
  "§Aturan Logika Modul#r63": 2
  "§Aturan Logika Modul#r64": [2, 6]
  "§Aturan Logika Modul#r65": [26, 32, 34]
  "§9.2#r3": [2, 3, 12, 36, 38, 40, 42, 74, 76, 78, 80]
  "§9.2#r4": [26, 36, 82]
  "§9.2#r6": [20, 29, 84]
  "§9.2#b13": [51, 52]
  "§9.2#b24": [2, 3, 14, 16, 18, 20, 68, 70, 72, 74, 76, 78, 80, 84]
  "§9.2#b25": [44, 47]
  "§9.2#b26": [8, 10, 12, 54]
  "§6#p2": [22, 24, 59, 63, 88, 89, 91]
  "§8.1#p2": [4, 27, 32, 36, 38, 40, 42]
  V-DMG-06: [47, 49]
  V-DMG-08: 51
  V-DMG-09: [59, 60, 89]
  D-DMG-13: [63, 64, 91]
  TS-DMG-09: 60
  TS-DISP-12: [4, 6, 86]
  TS-DISP-15: [54, 55, 57, 63]
  "§9.6#r8": [44, 45, 66]
  EC-DMG-17: [32, 34, 36, 38]
  EC-DMG-21: 51
  EC-DMG-35: [59, 61]
  "§9.4.4#r11": 52
  "§9.4.4#r12": [55, 61, 64, 88, 92]
  "§9.4.4#r28": [32, 34, 36]
  "§9.4.4#r29": [47, 49]
  "§9.4.4#r30": [29, 30]
  "§9.7#r10": 2
  "§9.7#r11": [32, 34, 44]
  "§9.7#r12": 26
  "§9.7#r13": 29
  "§9.7#r14": [36, 38, 40, 42]
  "§9.4.1#r9": [51, 54, 59]
  "§3#p7": [2, 29, 36, 38, 40, 42]
  F-DMG-06: 2
  "§9.2#b8": 12
  "§Aturan Logika Modul#r19": [12, 14, 20, 29]
  "§9.4.2#r32": [88, 89, 91, 92]
  "§4.2.4#r10": [51, 52]
  "§4.2.4#r11": [63, 64, 91, 92]
  T-DMG-01: 105
  "§8.1#r14": 99
  "§8.1#r15": [101, 103]
  "§9.2#r2": [2, 32, 34, 44]
---

# Server mengikuti Disposal Report dan baris Disposal untuk status record, memproses Bulk Report Disposal per record dengan pengecekan ganda, memblok lintas Group, dan membatasi Cancel Disposal Report pada Reported Disposal

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged dengan hak Report Disposal dan Cancel Disposal Report.
  - Aktor pelepasan aset `Maya Puspita {runId}`, Asset Admin sub-tab Disposal, yang menjalankan Dispose, Decline, dan Cancel Report dari tab Reported.
- Data:
  - DU-207-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-207-2: User `Maya Puspita {runId}`, Asset Admin sub-tab Disposal, cakupan Group `Head Office {runId}` dan Group `Warehouse {runId}`.
  - DU-207-3: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-207-4: Group `Head Office {runId}`.
  - DU-207-5: Group `Warehouse {runId}`.
  - DU-207-6: Entitas `Mitra Tanpa Disposal {runId}`, level Feature Suite Disposal `None`.
  - DU-207-7: Aset `Scanner Fujitsu fi-7160 - 81 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-207-8: Aset `Laptop Dell Latitude 5420 - 82 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tanpa transaksi berjalan.
  - DU-207-9: Aset `Printer HP LaserJet M404 - 83 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-207-10: Aset `Printer HP LaserJet M404 - 84 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal` dari laporan `Maya Puspita {runId}`.
  - DU-207-11: Aset `Printer HP LaserJet M404 - 85 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal` yang dilaporkan `Agus Pratama {runId}`.
  - DU-207-12: Aset `Monitor Dell P2422H - 86 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tanpa transaksi berjalan.
  - DU-207-13: Aset `Camera Canon EOS - 87 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris Disposal `Waiting for Approval`.
  - DU-207-14: Aset `Camera Canon EOS - 88 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris Disposal `Waiting for Execution`.
  - DU-207-15: Aset `Camera Canon EOS - 89 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris Disposal yang akan di-Remove.
  - DU-207-16: Aset `Camera Canon EOS - 90 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris Disposal yang akan kedaluwarsa.
  - DU-207-17: Aset `Camera Canon EOS - 91 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan laporan pelepasan aset berstatus Report `In Disposal Process` di tab Reported.
  - DU-207-18: Aset `Drill Bosch GSB - 92 {runId}`, Group `Head Office {runId}`, punya record `Repaired`.
  - DU-207-19: Aset `Drill Bosch GSB - 93 {runId}`, Group `Head Office {runId}`, `Disposed`, punya record `Disposed`.
  - DU-207-20: Aset `Drill Bosch GSB - 94 {runId}`, Group `Head Office {runId}`, punya record `Rejected`.
  - DU-207-21: Aset `Drill Bosch GSB - 95 {runId}`, Group `Head Office {runId}`, punya record `Canceled`.
  - DU-207-22: Aset `Tablet Samsung Tab A8 - 96 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-207-23: Aset `Toyota Avanza - 97 {runId}`, Group `Head Office {runId}`, punya record `Damaged` dengan penanda `Reported Missing`.
  - DU-207-24: Aset `Toyota Avanza - 98 {runId}`, Group `Head Office {runId}`, punya record `Damaged` dengan penanda `Missing`.
  - DU-207-25: Aset `Forklift Toyota 8FD - 99 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-207-26: Aset `Forklift Toyota 8FD - 100 {runId}`, Group `Warehouse {runId}`, punya record `Damaged`.
  - DU-207-27: Aset `Office Chair Ergo - 101 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-207-28: Aset `Office Chair Ergo - 102 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-207-29: Aset `Handheld Scanner Zebra TC21 - 103 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-207-30: Aset `Handheld Scanner Zebra TC21 - 104 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang kemudian menjadi `Repaired` sebelum Submit.
  - DU-207-31: Aset `Handheld Scanner Zebra TC21 - 105 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang kemudian ditahan penanda `Missing` sebelum Submit.
  - DU-207-32: Aset `Projector Epson EB-X06 - 106 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang kemudian menjadi `Repaired` sebelum Submit.
  - DU-207-33: Aset `Projector Epson EB-X06 - 107 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang kemudian ditahan penanda `Missing` sebelum Submit.
  - DU-207-34: Aset `Monitor Dell P2422H - 108 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tanpa transaksi berjalan, dilaporkan dari Asset List.
  - DU-207-35: Aset `Printer HP LaserJet M404 - 109 {runId}`, Group `Head Office {runId}`, punya record `Damaged` di entitas `Mitra Tanpa Disposal {runId}`.
  - DU-207-36: Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`.
  - DU-207-37: Reason `Seluruh unit dihentikan penggunaannya {runId}`.
  - DU-207-38: Reason `Unit masih layak dipakai {runId}`.
  - DU-207-39: Aset `Barcode Printer Zebra ZD421 - 110 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-207-40: Aset `Barcode Printer Zebra ZD421 - 111 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang sudah `Repaired` sebelum bulk dipilih.
  - DU-207-41: Aset `Barcode Printer Zebra ZD421 - 112 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang sudah ditahan penanda `Missing` sebelum bulk dipilih.
  - DU-207-42: Aset `Label Printer Brother QL-820 - 113 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang sudah `Repaired` sebelum bulk dipilih.
  - DU-207-43: Aset `Label Printer Brother QL-820 - 114 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang sudah ditahan penanda `Missing` sebelum bulk dipilih.
  - DU-207-44: Aset `Scanner Fujitsu fi-7160 - 115 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal` dengan laporan pelepasan aset `Reported` di tab Reported, belum ada baris Disposal.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Full`.

## Test Steps

### Report Disposal dari baris record: record Damaged menjadi Reported Disposal
1. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Laptop Dell Latitude 5420 - 82 {runId}` dari tab Damaged dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
2. Verifikasi server membuat laporan pelepasan aset berstatus `Reported` di tab Reported dan record menjadi `Reported Disposal`
3. Verifikasi Condition aset menjadi `Reported Disposal` dan Custody `Available`
4. Verifikasi Damage Log record memuat node `Disposal reported by` dengan pelaku `Agus Pratama {runId}`, dan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
5. Total Control `Agus Pratama {runId}` mengirim ulang Report Disposal yang sama atas `Laptop Dell Latitude 5420 - 82 {runId}` dengan kunci idempotensi yang sama
6. Verifikasi tidak ada laporan pelepasan aset kedua dan tidak ada node `Disposal reported by` kedua, karena record sudah berada di state tujuan
7. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Monitor Dell P2422H - 108 {runId}` dari Asset List dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
8. Verifikasi record yang ada otomatis tertaut dan menjadi `Reported Disposal` tanpa record baru
9. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Tablet Samsung Tab A8 - 96 {runId}` yang sedang dipinjam dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
10. Verifikasi Report Disposal ditolak karena aset belum Available dan record tetap `Damaged`

### Report Disposal hanya untuk record Damaged: status lain ditolak
11. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Scanner Fujitsu fi-7160 - 81 {runId}` yang record-nya `Waiting for Confirmation` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
12. Verifikasi Report Disposal ditolak dan record tetap `Waiting for Confirmation`
13. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Drill Bosch GSB - 92 {runId}` yang record-nya `Repaired` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
14. Verifikasi Report Disposal ditolak dan record tetap `Repaired`
15. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Drill Bosch GSB - 94 {runId}` yang record-nya `Rejected` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
16. Verifikasi Report Disposal ditolak dan record tetap `Rejected`
17. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Drill Bosch GSB - 95 {runId}` yang record-nya `Canceled` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
18. Verifikasi Report Disposal ditolak dan record tetap `Canceled`
19. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Drill Bosch GSB - 93 {runId}` yang record-nya `Disposed` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
20. Verifikasi Report Disposal ditolak dan record `Disposed` tidak berubah karena tidak punya transisi keluar
21. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Toyota Avanza - 97 {runId}` yang berpenanda `Reported Missing` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
22. Verifikasi Report Disposal ditolak karena record berpenanda dan record tetap `Damaged`
23. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Toyota Avanza - 98 {runId}` yang berpenanda `Missing` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
24. Verifikasi Report Disposal ditolak karena record berpenanda dan record tetap `Damaged`

### Dispose lalu Submit Request menjadikan record In Disposal Process, lalu Disposed saat Executed
25. Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Dispose atas laporan `Laptop Dell Latitude 5420 - 82 {runId}` dari tab Reported dan men-Submit Request
26. Verifikasi record berubah menjadi `In Disposal Process` dan Condition aset menjadi `In Disposal Process`
27. Verifikasi Damage Log record memuat node `Disposal requested by` dengan pelaku `Maya Puspita {runId}`
28. Pelepasan aset `Laptop Dell Latitude 5420 - 82 {runId}` dieksekusi (Executed)
29. Verifikasi record menjadi `Disposed` dan pindah dari record berjalan ke History
30. Verifikasi pelepasan aset yang dieksekusi itu tercatat di Damage Log sebagai node `Disposed` yang pelakunya `System`

### Decline Report dan Cancel Report atas laporan pelepasan aset mengembalikan record ke Damaged
31. Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Decline atas laporan `Printer HP LaserJet M404 - 83 {runId}` dari tab Reported dengan Reason `Unit masih layak dipakai {runId}`
32. Verifikasi record kembali `Damaged` dan Damage Log memuat node `Disposal report declined by` dengan pelaku `Maya Puspita {runId}`
33. Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Cancel Report atas laporan `Printer HP LaserJet M404 - 84 {runId}` dari tab Reported
34. Verifikasi record kembali `Damaged` dan Damage Log memuat node `Disposal report canceled by` dengan pelaku `Maya Puspita {runId}`

### Baris pelepasan aset ditolak, dibatalkan, dihapus, atau kedaluwarsa mengembalikan record ke Reported Disposal dan laporan ke Reported
35. Baris pelepasan aset `Camera Canon EOS - 87 {runId}` ditolak (Reject) oleh approver
36. Verifikasi record kembali `Reported Disposal`, bukan `Damaged`, laporan pelepasan aset kembali `Reported`, dan Damage Log memuat node `Rejected by`
37. Baris pelepasan aset `Camera Canon EOS - 88 {runId}` dibatalkan (Cancel) oleh pembuatnya
38. Verifikasi record kembali `Reported Disposal`, bukan `Damaged`, laporan pelepasan aset kembali `Reported`, dan Damage Log memuat node `Canceled by`
39. Baris pelepasan aset `Camera Canon EOS - 89 {runId}` dihapus (Remove)
40. Verifikasi record kembali `Reported Disposal`, bukan `Damaged`, laporan pelepasan aset kembali `Reported`, dan Damage Log memuat node `Removed from disposal by`
41. Baris pelepasan aset `Camera Canon EOS - 90 {runId}` kedaluwarsa (timeout) tanpa user aktor
42. Verifikasi record kembali `Reported Disposal`, bukan `Damaged`, laporan pelepasan aset kembali `Reported`, dan node di Damage Log dicatat dengan PIC `System`

### Cancel Disposal Report hanya untuk record Reported Disposal
43. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Printer HP LaserJet M404 - 85 {runId}` yang berstatus `Reported Disposal`
44. Verifikasi Cancel Report atas laporan itu dijalankan dan record kembali `Damaged` dengan node `Disposal report canceled by` dari `Agus Pratama {runId}`
45. Verifikasi status record, Condition aset, dan laporan pelepasan aset berubah bersamaan sebagai satu kesatuan
46. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 86 {runId}` yang berstatus `Damaged`
47. Verifikasi permintaan ditolak karena status record bukan `Reported Disposal` dan tidak ada node baru
48. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Camera Canon EOS - 91 {runId}` yang berstatus `In Disposal Process`
49. Verifikasi permintaan ditolak karena status record bukan `Reported Disposal` dan record tetap `In Disposal Process`

### Bulk Report Disposal lintas Group diblok
50. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Forklift Toyota 8FD - 99 {runId}` di Group `Head Office {runId}` dan `Forklift Toyota 8FD - 100 {runId}` di Group `Warehouse {runId}` dengan satu Reason `Seluruh unit dihentikan penggunaannya {runId}`
51. Verifikasi permintaan ditolak karena aset berasal dari lebih dari satu Group
52. Verifikasi tidak ada laporan pelepasan aset dibuat, kedua record tetap `Damaged`, dan tidak ada node baru

### Bulk Report Disposal satu Group: satu Reason untuk semua dan satu node per record
53. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Office Chair Ergo - 101 {runId}` dan `Office Chair Ergo - 102 {runId}` di Group `Head Office {runId}` dengan satu Reason `Seluruh unit dihentikan penggunaannya {runId}`
54. Verifikasi kedua record menjadi `Reported Disposal` dengan Reason `Seluruh unit dihentikan penggunaannya {runId}` yang sama
55. Verifikasi Damage Log tiap record memuat satu node `Disposal reported by`
56. Total Control `Agus Pratama {runId}` mengirim ulang Bulk Report Disposal yang sama atas kedua record dengan kunci idempotensi yang sama
57. Verifikasi tidak ada laporan pelepasan aset atau node baru karena kedua record sudah berada di state tujuan

### Bulk Report Disposal melewati record yang tidak lagi layak saat Submit
58. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Handheld Scanner Zebra TC21 - 103 {runId}`, `Handheld Scanner Zebra TC21 - 104 {runId}`, dan `Handheld Scanner Zebra TC21 - 105 {runId}` dengan satu Reason `Seluruh unit dihentikan penggunaannya {runId}`, setelah `Handheld Scanner Zebra TC21 - 104 {runId}` menjadi `Repaired` dan `Handheld Scanner Zebra TC21 - 105 {runId}` ditahan penanda `Missing`
59. Verifikasi hanya `Handheld Scanner Zebra TC21 - 103 {runId}` yang menjadi `Reported Disposal`, sedangkan dua record lain dilewati
60. Verifikasi respons memuat pesan baku `Success, asset has been reported for disposal. Some items were skipped.`
61. Verifikasi node `Disposal reported by` hanya ada di record yang diproses
62. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Projector Epson EB-X06 - 106 {runId}` dan `Projector Epson EB-X06 - 107 {runId}` dengan satu Reason `Seluruh unit dihentikan penggunaannya {runId}`, setelah satu record menjadi `Repaired` dan yang lain ditahan penanda `Missing`
63. Verifikasi tidak ada laporan pelepasan aset yang dibuat dan respons menyatakan `None of the selected records can be reported for disposal.` tanpa pesan sukses
64. Verifikasi kedua record tidak berubah dan tidak ada node baru

### Cancel Disposal Report yang dikirim ulang tidak membuat node kedua
65. Total Control `Agus Pratama {runId}` mengirim ulang Cancel Disposal Report yang sama atas `Printer HP LaserJet M404 - 85 {runId}` dengan kunci idempotensi yang sama
66. Verifikasi tidak ada node `Disposal report canceled by` kedua dan record tetap `Damaged`

### Condition aset mengikuti status record saat keluar dari proses pelepasan aset: Damaged untuk Decline dan Cancel Report, Reported Disposal untuk penutupan baris
67. Total Control `Agus Pratama {runId}` membaca Condition aset `Printer HP LaserJet M404 - 83 {runId}` yang laporan pelepasan asetnya di-Decline
68. Verifikasi Condition aset kembali `Damaged`
69. Total Control `Agus Pratama {runId}` membaca Condition aset `Printer HP LaserJet M404 - 84 {runId}` yang laporan pelepasan asetnya dibatalkan lewat Cancel Report
70. Verifikasi Condition aset kembali `Damaged`
71. Total Control `Agus Pratama {runId}` membaca Condition aset `Printer HP LaserJet M404 - 85 {runId}` yang laporan pelepasan asetnya dibatalkan lewat Cancel Disposal Report
72. Verifikasi Condition aset kembali `Damaged`
73. Total Control `Agus Pratama {runId}` membaca Condition aset `Camera Canon EOS - 87 {runId}` yang baris pelepasan asetnya ditolak
74. Verifikasi Condition aset kembali `Reported Disposal`
75. Total Control `Agus Pratama {runId}` membaca Condition aset `Camera Canon EOS - 88 {runId}` yang baris pelepasan asetnya dibatalkan
76. Verifikasi Condition aset kembali `Reported Disposal`
77. Total Control `Agus Pratama {runId}` membaca Condition aset `Camera Canon EOS - 89 {runId}` yang baris pelepasan asetnya dihapus
78. Verifikasi Condition aset kembali `Reported Disposal`
79. Total Control `Agus Pratama {runId}` membaca Condition aset `Camera Canon EOS - 90 {runId}` yang baris pelepasan asetnya kedaluwarsa
80. Verifikasi Condition aset kembali `Reported Disposal`

### Custody aset In Disposal Process dan Lifecycle aset yang dieksekusi
81. Total Control `Agus Pratama {runId}` membaca Custody aset `Camera Canon EOS - 91 {runId}` yang record-nya `In Disposal Process`
82. Verifikasi Custody aset `Available`
83. Total Control `Agus Pratama {runId}` membaca Lifecycle aset `Laptop Dell Latitude 5420 - 82 {runId}` yang pelepasan asetnya sudah dieksekusi
84. Verifikasi Lifecycle aset `Disposed`

### Report Disposal satu aset atomik: laporan, Condition, dan status record berubah bersamaan
85. Total Control `Agus Pratama {runId}` membaca laporan pelepasan aset, status record, dan Condition aset `Monitor Dell P2422H - 108 {runId}` yang Report Disposal-nya sudah diproses
86. Verifikasi laporan pelepasan aset, status record `Reported Disposal`, dan Condition aset `Reported Disposal` terbentuk bersamaan sebagai satu kesatuan, tanpa laporan yang tersisa tanpa perubahan Condition dan status record

### Bulk Report Disposal atas seleksi yang sebagian tidak layak sejak sebelum Submit hanya memproses record yang layak
87. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Barcode Printer Zebra ZD421 - 110 {runId}`, `Barcode Printer Zebra ZD421 - 111 {runId}`, dan `Barcode Printer Zebra ZD421 - 112 {runId}` dengan satu Reason `Seluruh unit dihentikan penggunaannya {runId}`, setelah record `Barcode Printer Zebra ZD421 - 111 {runId}` sudah `Repaired` dan record `Barcode Printer Zebra ZD421 - 112 {runId}` sudah ditahan penanda `Missing`
88. Verifikasi hanya `Barcode Printer Zebra ZD421 - 110 {runId}` yang menjadi `Reported Disposal` dengan Reason `Seluruh unit dihentikan penggunaannya {runId}`, sedangkan dua record lain tidak diproses dan tidak ada node baru di keduanya
89. Verifikasi respons memuat pesan baku `Success, asset has been reported for disposal. Some items were skipped.`
90. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Label Printer Brother QL-820 - 113 {runId}` dan `Label Printer Brother QL-820 - 114 {runId}` dengan satu Reason `Seluruh unit dihentikan penggunaannya {runId}`, setelah record pertama sudah `Repaired` dan record kedua sudah ditahan penanda `Missing`
91. Verifikasi tidak ada laporan pelepasan aset yang dibuat dan respons menyatakan `None of the selected records can be reported for disposal.` tanpa pesan sukses
92. Verifikasi kedua record tidak berubah dan tidak ada node baru

### Laporan tetap di tab Reported selama baris Disposal berjalan, dan Draft Disposal tidak mengubah record
93. Total Control `Agus Pratama {runId}` membaca laporan pelepasan aset `Camera Canon EOS - 91 {runId}` yang record-nya `In Disposal Process`
94. Verifikasi laporan itu tetap di tab Reported dengan status Report `In Disposal Process`
95. Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Dispose atas laporan `Scanner Fujitsu fi-7160 - 115 {runId}` dari tab Reported dan menyimpannya sebagai Draft Disposal tanpa Submit Request
96. Verifikasi record `Scanner Fujitsu fi-7160 - 115 {runId}` tetap `Reported Disposal` dan tidak ada node baru di Damage Log
97. Verifikasi laporan pelepasan aset itu tidak mendapat penanda dari Draft Disposal dan tetap di tab Reported

### Node Disposal report declined by dan Disposal report canceled by memuat Reason dan Back to Damaged
98. Total Control `Agus Pratama {runId}` membaca Damage Log record `Printer HP LaserJet M404 - 83 {runId}` yang laporan pelepasan asetnya di-Decline oleh `Maya Puspita {runId}` dengan Reason `Unit masih layak dipakai {runId}`
99. Verifikasi node `Disposal report declined by` memuat Reason `Unit masih layak dipakai {runId}` dan `Back to Damaged`
100. Total Control `Agus Pratama {runId}` membaca Damage Log record `Printer HP LaserJet M404 - 84 {runId}` yang laporan pelepasan asetnya dibatalkan lewat Cancel Report oleh pelapor `Maya Puspita {runId}` dari tab Reported
101. Verifikasi node `Disposal report canceled by` atas nama `Maya Puspita {runId}` memuat `Back to Damaged`
102. Total Control `Agus Pratama {runId}` membaca Damage Log record `Printer HP LaserJet M404 - 85 {runId}` yang laporan pelepasan asetnya dibatalkan lewat Cancel Disposal Report
103. Verifikasi node `Disposal report canceled by` atas nama `Agus Pratama {runId}` memuat `Back to Damaged`

### Record yang menjadi berpenanda Missing setelah dipilih dilewati pada submit Bulk Report Disposal
104. Total Control `Agus Pratama {runId}` membaca record `Handheld Scanner Zebra TC21 - 105 {runId}` yang menjadi berpenanda `Missing` setelah dipilih untuk Bulk Report Disposal
105. Verifikasi record itu dilewati pada submit dan tetap `Damaged`
