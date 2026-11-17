---
id: TC-FA-MYASSET-UI-113-tabel-borrowed-reaksi-respons-aksi-laporan
title: "Tabel Borrowed: toast dan dialog atas respons Report Damaged, Report Missing, dan pembatalannya"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.1b#r43", "§4.1b#r45", "§4.1b#r51", "§4.1b#r52", "§4.1b#r66", "§4.1b#r74", "§7.2#r6", "§7.2#r7", "§7.2#r8", "§7.2#r9", "§7.3#r6", "§7.3#r7", "§7.3#r9", "§7.3#r15", "§9.6#r5", "§9.6#r8", "§9.6#r9", "§9.6#p1", "EB-FB-1@report-damaged", "EB-FB-1@report-missing", "EB-FB-1@cancel-damage-report", "EB-FB-1@cancel-missing-report", "EB-ERR-1@report-damaged", "EB-ERR-1@report-missing", "EB-ERR-1@cancel-damage-report", "EB-ERR-1@cancel-missing-report"]
smoke: []
dependsOn: []
trace:
  "§4.1b#r43": [4, 5]
  "§4.1b#r45": 20
  "§4.1b#r51": [38, 39]
  "§4.1b#r52": 50
  "§4.1b#r66": 75
  "§4.1b#r74": 98
  "§7.2#r6": 4
  "§7.2#r7": 66
  "§7.2#r8": 38
  "§7.2#r9": 89
  "§7.3#r6": 20
  "§7.3#r7": 50
  "§7.3#r9": [75, 98]
  "§7.3#r15": [9, 15, 41, 68, 91]
  "§9.6#r5": [41, 47, 48, 50, 51, 61, 62]
  "§9.6#r8": [9, 17, 18, 20, 21, 33, 34]
  "§9.6#r9": [68, 73, 75, 76, 85, 91, 96, 98, 99, 108]
  "§9.6#p1": [10, 11, 16, 32, 42, 43, 46, 58, 60, 69, 72, 84, 92, 95, 107]
  "EB-FB-1@report-damaged": [9, 20]
  "EB-FB-1@report-missing": [41, 50]
  "EB-FB-1@cancel-damage-report": [68, 75]
  "EB-FB-1@cancel-missing-report": [91, 98]
  "EB-ERR-1@report-damaged": [10, 11, 12, 13, 20, 28, 29, 30, 31]
  "EB-ERR-1@report-missing": [42, 43, 44, 45, 50, 56, 57, 58, 59]
  "EB-ERR-1@cancel-damage-report": [69, 70, 71, 75, 81, 82, 83]
  "EB-ERR-1@cancel-missing-report": [92, 93, 94, 98, 104, 105, 106]
anchor: []
coverage:
  web: automated
---

# Tabel Borrowed: toast dan dialog atas respons Report Damaged, Report Missing, dan pembatalannya

## Prerequisites
- Aktor: Borrower.
- Layar awal: My Asset > tab Borrowed.
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-113-1: baris pinjaman tanpa laporan dengan Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0147`, Source `Self-service`, Duration `4 days`, Handed Over At `07/11/26, 09:10`.
  - DU-113-2: baris pinjaman dengan Damage Report yang menunggu konfirmasi: Name `Laptop Dell Latitude 5420 - 54`, Asset ID `LPT-2026-0054`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed` dengan badge `Reported Damaged`, Due Date `12/11/26`, Remaining `Due in 3 days`, Borrower `Me`, Transaction ID `BRW-2026-0164`, Source `Admin`, Duration `6 days`, Handed Over At `07/11/26, 09:00`.
  - DU-113-3: baris pinjaman dengan laporan Missing yang menunggu konfirmasi: Name `Laptop Dell Latitude 5420 - 11`, Asset ID `LPT-2026-0011`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed` dengan badge `Reported Missing`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0150`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-113-4: isian dialog `Report Damaged`: Damaged Photo `layar-retak.jpg` dan What happened `Layar retak setelah terjatuh dari meja rapat`.
  - DU-113-5: baris pinjaman yang baru muncul saat daftar dimuat ulang: Name `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `09/11/26, 21:50`, Remaining `Due in 1 hour`, Borrower `Me`, Transaction ID `BRW-2026-0156`, Source `Self-service`, Duration `3 hours`, Handed Over At `09/11/26, 18:50`.
- Kondisi:
  - K1: daftar berisi DU-113-1; kirim Report Damaged yang pertama gagal karena error server dan yang kedua berhasil; memuat ulang daftar sesudah kegagalan dijawab dengan DU-113-1 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K2: daftar berisi DU-113-1; kirim Report Damaged tidak mendapat jawaban (timeout atau koneksi putus); memuat ulang daftar sesudahnya dijawab dengan DU-113-1 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K3: daftar berisi DU-113-1; kirim Report Missing yang pertama gagal karena error server dan yang kedua berhasil; memuat ulang daftar sesudah kegagalan dijawab dengan DU-113-1 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K4: daftar berisi DU-113-1; kirim Report Missing tidak mendapat jawaban (timeout atau koneksi putus); memuat ulang daftar sesudahnya dijawab dengan DU-113-1 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K5: daftar berisi DU-113-2; Cancel Damage Report yang pertama gagal karena error server dan yang kedua berhasil; memuat ulang daftar sesudah kegagalan dijawab dengan DU-113-2 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K6: daftar berisi DU-113-2; Cancel Damage Report tidak mendapat jawaban (timeout atau koneksi putus); memuat ulang daftar sesudahnya dijawab dengan DU-113-2 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K7: daftar berisi DU-113-3; Cancel Missing Report yang pertama gagal karena error server dan yang kedua berhasil; memuat ulang daftar sesudah kegagalan dijawab dengan DU-113-3 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K8: daftar berisi DU-113-3; Cancel Missing Report tidak mendapat jawaban (timeout atau koneksi putus); memuat ulang daftar sesudahnya dijawab dengan DU-113-3 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.

## Test Steps

### Report Damaged: dialog, gagal server, lalu berhasil dikirim ulang
1. Tampilkan Tabel Borrowed dengan kondisi K1
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
3. Klik `Report Damaged`
4. Verifikasi judul dialog `Report Damaged` tampil
5. Verifikasi dialog `Report Damaged` tidak memiliki kotak dampak
6. Isi Damaged Photo dengan `layar-retak.jpg`
7. Isi What happened dengan `Layar retak setelah terjatuh dari meja rapat`
8. Klik `[Report Damaged]`
9. Verifikasi `Error, failed to send report.` tampil untuk Report Damaged
10. Verifikasi dialog `Report Damaged` tetap terbuka sesudah gagal server
11. Verifikasi isian Damaged Photo `layar-retak.jpg` dan What happened `Layar retak setelah terjatuh dari meja rapat` dipertahankan sesudah gagal server
12. Verifikasi tombol `[Report Damaged]` aktif kembali sesudah gagal server
13. Verifikasi toast kegagalan Report Damaged tidak memiliki tombol aksi seperti `[Try Again]`
14. Waktu berlalu 5 detik sejak toast kegagalan tampil
15. Verifikasi `Error, failed to send report.` masih tampil sesudah 5 detik untuk Report Damaged
16. Verifikasi tabel dimuat ulang sesudah kegagalan Report Damaged: `Meeting Mic Set - 2` tampil
17. Verifikasi baris `Laptop Dell Latitude 5420 - 2` tampil dengan Status `Borrowed` sesudah kegagalan Report Damaged
18. Verifikasi badge `Reported Damaged` tidak tampil pada baris `Laptop Dell Latitude 5420 - 2`
19. Klik `[Report Damaged]`
20. Verifikasi `Success, damage report has been sent to the Asset Admin.` tampil
21. Verifikasi dialog `Report Damaged` tertutup sesudah laporan terkirim

### Report Damaged: timeout atau koneksi putus
22. Tampilkan Tabel Borrowed dengan kondisi K2
23. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
24. Klik `Report Damaged`
25. Isi Damaged Photo dengan `layar-retak.jpg`
26. Isi What happened dengan `Layar retak setelah terjatuh dari meja rapat`
27. Klik `[Report Damaged]`
28. Verifikasi `Connection problem. Please try again.` tampil untuk Report Damaged
29. Verifikasi dialog `Report Damaged` tetap terbuka sesudah timeout
30. Verifikasi isian Damaged Photo `layar-retak.jpg` dan What happened `Layar retak setelah terjatuh dari meja rapat` dipertahankan sesudah timeout
31. Verifikasi tombol `[Report Damaged]` aktif kembali sesudah timeout
32. Verifikasi tabel dimuat ulang sesudah timeout Report Damaged: `Meeting Mic Set - 2` tampil
33. Verifikasi baris `Laptop Dell Latitude 5420 - 2` tampil dengan Status `Borrowed` sesudah timeout Report Damaged
34. Verifikasi badge `Reported Damaged` tidak tampil pada baris `Laptop Dell Latitude 5420 - 2` sesudah timeout

### Report Missing: dialog, gagal server, lalu berhasil dikirim ulang
35. Tampilkan Tabel Borrowed dengan kondisi K3
36. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
37. Klik `Report Missing`
38. Verifikasi judul dialog `Report Missing` tampil
39. Verifikasi dialog `Report Missing` tidak memiliki kotak dampak
40. Klik `[Report Missing]`
41. Verifikasi `Error, failed to send report.` tampil untuk Report Missing
42. Verifikasi dialog `Report Missing` tetap terbuka sesudah gagal server
43. Verifikasi isian dialog `Report Missing` dipertahankan sesudah gagal server
44. Verifikasi tombol `[Report Missing]` aktif kembali sesudah gagal server
45. Verifikasi toast kegagalan Report Missing tidak memiliki tombol aksi seperti `[Try Again]`
46. Verifikasi tabel dimuat ulang sesudah kegagalan Report Missing: `Meeting Mic Set - 2` tampil
47. Verifikasi baris `Laptop Dell Latitude 5420 - 2` tampil dengan Status `Borrowed` sesudah kegagalan Report Missing
48. Verifikasi badge `Reported Missing` tidak tampil pada baris `Laptop Dell Latitude 5420 - 2`
49. Klik `[Report Missing]`
50. Verifikasi `Success, your report has been sent to the asset admins.` tampil
51. Verifikasi dialog `Report Missing` tertutup sesudah laporan terkirim

### Report Missing: timeout atau koneksi putus
52. Tampilkan Tabel Borrowed dengan kondisi K4
53. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
54. Klik `Report Missing`
55. Klik `[Report Missing]`
56. Verifikasi `Connection problem. Please try again.` tampil untuk Report Missing
57. Verifikasi dialog `Report Missing` tetap terbuka sesudah timeout
58. Verifikasi isian dialog `Report Missing` dipertahankan sesudah timeout
59. Verifikasi tombol `[Report Missing]` aktif kembali sesudah timeout
60. Verifikasi tabel dimuat ulang sesudah timeout Report Missing: `Meeting Mic Set - 2` tampil
61. Verifikasi baris `Laptop Dell Latitude 5420 - 2` tampil dengan Status `Borrowed` sesudah timeout Report Missing
62. Verifikasi badge `Reported Missing` tidak tampil pada baris `Laptop Dell Latitude 5420 - 2` sesudah timeout

### Cancel Damage Report: gagal server, lalu berhasil dikirim ulang
63. Tampilkan Tabel Borrowed dengan kondisi K5
64. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 54`
65. Klik `Cancel Damage Report`
66. Verifikasi judul dialog `Cancel Report` tampil untuk Cancel Damage Report
67. Klik tombol konfirmasi pada dialog `Cancel Report`
68. Verifikasi `Error, failed to cancel report.` tampil untuk Cancel Damage Report
69. Verifikasi dialog `Cancel Report` tetap terbuka sesudah gagal server pada Cancel Damage Report
70. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah gagal server pada Cancel Damage Report
71. Verifikasi toast kegagalan Cancel Damage Report tidak memiliki tombol aksi seperti `[Try Again]`
72. Verifikasi tabel dimuat ulang sesudah kegagalan Cancel Damage Report: `Meeting Mic Set - 2` tampil
73. Verifikasi baris `Laptop Dell Latitude 5420 - 54` tampil dengan badge `Reported Damaged` sesudah kegagalan Cancel Damage Report
74. Klik tombol konfirmasi pada dialog `Cancel Report`
75. Verifikasi `Success, report has been canceled.` tampil untuk Cancel Damage Report
76. Verifikasi dialog `Cancel Report` tertutup sesudah Cancel Damage Report berhasil

### Cancel Damage Report: timeout atau koneksi putus
77. Tampilkan Tabel Borrowed dengan kondisi K6
78. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 54`
79. Klik `Cancel Damage Report`
80. Klik tombol konfirmasi pada dialog `Cancel Report`
81. Verifikasi `Connection problem. Please try again.` tampil untuk Cancel Damage Report
82. Verifikasi dialog `Cancel Report` tetap terbuka sesudah timeout pada Cancel Damage Report
83. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah timeout pada Cancel Damage Report
84. Verifikasi tabel dimuat ulang sesudah timeout Cancel Damage Report: `Meeting Mic Set - 2` tampil
85. Verifikasi baris `Laptop Dell Latitude 5420 - 54` tampil dengan badge `Reported Damaged` sesudah timeout Cancel Damage Report

### Cancel Missing Report: gagal server, lalu berhasil dikirim ulang
86. Tampilkan Tabel Borrowed dengan kondisi K7
87. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 11`
88. Klik `Cancel Missing Report`
89. Verifikasi judul dialog `Cancel Report` tampil untuk Cancel Missing Report
90. Klik tombol konfirmasi pada dialog `Cancel Report`
91. Verifikasi `Error, failed to cancel report.` tampil untuk Cancel Missing Report
92. Verifikasi dialog `Cancel Report` tetap terbuka sesudah gagal server pada Cancel Missing Report
93. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah gagal server pada Cancel Missing Report
94. Verifikasi toast kegagalan Cancel Missing Report tidak memiliki tombol aksi seperti `[Try Again]`
95. Verifikasi tabel dimuat ulang sesudah kegagalan Cancel Missing Report: `Meeting Mic Set - 2` tampil
96. Verifikasi baris `Laptop Dell Latitude 5420 - 11` tampil dengan badge `Reported Missing` sesudah kegagalan Cancel Missing Report
97. Klik tombol konfirmasi pada dialog `Cancel Report`
98. Verifikasi `Success, report has been canceled.` tampil untuk Cancel Missing Report
99. Verifikasi dialog `Cancel Report` tertutup sesudah Cancel Missing Report berhasil

### Cancel Missing Report: timeout atau koneksi putus
100. Tampilkan Tabel Borrowed dengan kondisi K8
101. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 11`
102. Klik `Cancel Missing Report`
103. Klik tombol konfirmasi pada dialog `Cancel Report`
104. Verifikasi `Connection problem. Please try again.` tampil untuk Cancel Missing Report
105. Verifikasi dialog `Cancel Report` tetap terbuka sesudah timeout pada Cancel Missing Report
106. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah timeout pada Cancel Missing Report
107. Verifikasi tabel dimuat ulang sesudah timeout Cancel Missing Report: `Meeting Mic Set - 2` tampil
108. Verifikasi baris `Laptop Dell Latitude 5420 - 11` tampil dengan badge `Reported Missing` sesudah timeout Cancel Missing Report
