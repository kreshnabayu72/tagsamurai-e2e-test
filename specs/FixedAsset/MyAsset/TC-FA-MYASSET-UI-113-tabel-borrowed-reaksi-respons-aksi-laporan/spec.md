---
id: TC-FA-MYASSET-UI-113-tabel-borrowed-reaksi-respons-aksi-laporan
title: "Tabel Borrowed: toast dan dialog atas respons Report Damaged, Report Missing, dan pembatalannya"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§4.1b#r43", "§4.1b#r45", "§4.1b#r51", "§4.1b#r52", "§4.1b#r66", "§4.1b#r74", "§7.2#r6", "§7.2#r7", "§7.2#r8", "§7.2#r9", "§7.3#r6", "§7.3#r7", "§7.3#r9", "§7.3#r15", "§9.6#r5", "§9.6#r8", "§9.6#r9", "§9.6#p1", "EB-FB-1@report-damaged", "EB-FB-1@report-missing", "EB-FB-1@cancel-damage-report", "EB-FB-1@cancel-missing-report", "EB-ERR-1@report-damaged", "EB-ERR-1@report-missing", "EB-ERR-1@cancel-damage-report", "EB-ERR-1@cancel-missing-report"]
smoke: []
dependsOn: []
trace:
  "§4.1b#r43": [4, 5]
  "§4.1b#r45": 18
  "§4.1b#r51": [33, 34]
  "§4.1b#r52": 43
  "§4.1b#r66": 64
  "§4.1b#r74": 84
  "§7.2#r6": 4
  "§7.2#r7": 56
  "§7.2#r8": 33
  "§7.2#r9": 76
  "§7.3#r6": 18
  "§7.3#r7": 43
  "§7.3#r9": [64, 84]
  "§7.3#r15": [9, 15, 37, 58, 78]
  "§9.6#r5": [37, 43, 44]
  "§9.6#r8": [9, 18, 19]
  "§9.6#r9": [58, 64, 65, 78, 84, 85]
  "§9.6#p1": [10, 11, 16, 38, 41, 59, 62, 79, 82]
  "EB-FB-1@report-damaged": [9, 18]
  "EB-FB-1@report-missing": [37, 43]
  "EB-FB-1@cancel-damage-report": [58, 64]
  "EB-FB-1@cancel-missing-report": [78, 84]
  "EB-ERR-1@report-damaged": [10, 11, 12, 13, 18, 26, 27, 28, 29]
  "EB-ERR-1@report-missing": [38, 39, 40, 43, 50, 51, 52]
  "EB-ERR-1@cancel-damage-report": [59, 60, 61, 64, 70, 71, 72]
  "EB-ERR-1@cancel-missing-report": [79, 80, 81, 84, 90, 91, 92]
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
  - K2: daftar berisi DU-113-1; kirim Report Damaged tidak mendapat jawaban (timeout atau koneksi putus). Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K3: daftar berisi DU-113-1; kirim Report Missing yang pertama gagal karena error server dan yang kedua berhasil; memuat ulang daftar sesudah kegagalan dijawab dengan DU-113-1 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K4: daftar berisi DU-113-1; kirim Report Missing tidak mendapat jawaban (timeout atau koneksi putus). Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K5: daftar berisi DU-113-2; Cancel Damage Report yang pertama gagal karena error server dan yang kedua berhasil; memuat ulang daftar sesudah kegagalan dijawab dengan DU-113-2 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K6: daftar berisi DU-113-2; Cancel Damage Report tidak mendapat jawaban (timeout atau koneksi putus). Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K7: daftar berisi DU-113-3; Cancel Missing Report yang pertama gagal karena error server dan yang kedua berhasil; memuat ulang daftar sesudah kegagalan dijawab dengan DU-113-3 dan DU-113-5. Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.
  - K8: daftar berisi DU-113-3; Cancel Missing Report tidak mendapat jawaban (timeout atau koneksi putus). Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`.

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
17. Klik `[Report Damaged]`
18. Verifikasi `Success, damage report has been sent to the Asset Admin.` tampil
19. Verifikasi dialog `Report Damaged` tertutup sesudah laporan terkirim

### Report Damaged: timeout atau koneksi putus
20. Tampilkan Tabel Borrowed dengan kondisi K2
21. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
22. Klik `Report Damaged`
23. Isi Damaged Photo dengan `layar-retak.jpg`
24. Isi What happened dengan `Layar retak setelah terjatuh dari meja rapat`
25. Klik `[Report Damaged]`
26. Verifikasi `Connection problem. Please try again.` tampil untuk Report Damaged
27. Verifikasi dialog `Report Damaged` tetap terbuka sesudah timeout
28. Verifikasi isian Damaged Photo `layar-retak.jpg` dan What happened `Layar retak setelah terjatuh dari meja rapat` dipertahankan sesudah timeout
29. Verifikasi tombol `[Report Damaged]` aktif kembali sesudah timeout

### Report Missing: dialog, gagal server, lalu berhasil dikirim ulang
30. Tampilkan Tabel Borrowed dengan kondisi K3
31. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
32. Klik `Report Missing`
33. Verifikasi judul dialog `Report Missing` tampil
34. Verifikasi dialog `Report Missing` tidak memiliki kotak dampak
35. Isi seluruh field wajib pada dialog `Report Missing`
36. Klik `[Report Missing]`
37. Verifikasi `Error, failed to send report.` tampil untuk Report Missing
38. Verifikasi dialog `Report Missing` tetap terbuka sesudah gagal server
39. Verifikasi tombol `[Report Missing]` aktif kembali sesudah gagal server
40. Verifikasi toast kegagalan Report Missing tidak memiliki tombol aksi seperti `[Try Again]`
41. Verifikasi tabel dimuat ulang sesudah kegagalan Report Missing: `Meeting Mic Set - 2` tampil
42. Klik `[Report Missing]`
43. Verifikasi `Success, your report has been sent to the asset admins.` tampil
44. Verifikasi dialog `Report Missing` tertutup sesudah laporan terkirim

### Report Missing: timeout atau koneksi putus
45. Tampilkan Tabel Borrowed dengan kondisi K4
46. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
47. Klik `Report Missing`
48. Isi seluruh field wajib pada dialog `Report Missing`
49. Klik `[Report Missing]`
50. Verifikasi `Connection problem. Please try again.` tampil untuk Report Missing
51. Verifikasi dialog `Report Missing` tetap terbuka sesudah timeout
52. Verifikasi tombol `[Report Missing]` aktif kembali sesudah timeout

### Cancel Damage Report: gagal server, lalu berhasil dikirim ulang
53. Tampilkan Tabel Borrowed dengan kondisi K5
54. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 54`
55. Klik `Cancel Damage Report`
56. Verifikasi judul dialog `Cancel Report` tampil untuk Cancel Damage Report
57. Klik tombol konfirmasi pada dialog `Cancel Report`
58. Verifikasi `Error, failed to cancel report.` tampil untuk Cancel Damage Report
59. Verifikasi dialog `Cancel Report` tetap terbuka sesudah gagal server pada Cancel Damage Report
60. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah gagal server pada Cancel Damage Report
61. Verifikasi toast kegagalan Cancel Damage Report tidak memiliki tombol aksi seperti `[Try Again]`
62. Verifikasi tabel dimuat ulang sesudah kegagalan Cancel Damage Report: `Meeting Mic Set - 2` tampil
63. Klik tombol konfirmasi pada dialog `Cancel Report`
64. Verifikasi `Success, report has been canceled.` tampil untuk Cancel Damage Report
65. Verifikasi dialog `Cancel Report` tertutup sesudah Cancel Damage Report berhasil

### Cancel Damage Report: timeout atau koneksi putus
66. Tampilkan Tabel Borrowed dengan kondisi K6
67. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 54`
68. Klik `Cancel Damage Report`
69. Klik tombol konfirmasi pada dialog `Cancel Report`
70. Verifikasi `Connection problem. Please try again.` tampil untuk Cancel Damage Report
71. Verifikasi dialog `Cancel Report` tetap terbuka sesudah timeout pada Cancel Damage Report
72. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah timeout pada Cancel Damage Report

### Cancel Missing Report: gagal server, lalu berhasil dikirim ulang
73. Tampilkan Tabel Borrowed dengan kondisi K7
74. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 11`
75. Klik `Cancel Missing Report`
76. Verifikasi judul dialog `Cancel Report` tampil untuk Cancel Missing Report
77. Klik tombol konfirmasi pada dialog `Cancel Report`
78. Verifikasi `Error, failed to cancel report.` tampil untuk Cancel Missing Report
79. Verifikasi dialog `Cancel Report` tetap terbuka sesudah gagal server pada Cancel Missing Report
80. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah gagal server pada Cancel Missing Report
81. Verifikasi toast kegagalan Cancel Missing Report tidak memiliki tombol aksi seperti `[Try Again]`
82. Verifikasi tabel dimuat ulang sesudah kegagalan Cancel Missing Report: `Meeting Mic Set - 2` tampil
83. Klik tombol konfirmasi pada dialog `Cancel Report`
84. Verifikasi `Success, report has been canceled.` tampil untuk Cancel Missing Report
85. Verifikasi dialog `Cancel Report` tertutup sesudah Cancel Missing Report berhasil

### Cancel Missing Report: timeout atau koneksi putus
86. Tampilkan Tabel Borrowed dengan kondisi K8
87. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 11`
88. Klik `Cancel Missing Report`
89. Klik tombol konfirmasi pada dialog `Cancel Report`
90. Verifikasi `Connection problem. Please try again.` tampil untuk Cancel Missing Report
91. Verifikasi dialog `Cancel Report` tetap terbuka sesudah timeout pada Cancel Missing Report
92. Verifikasi tombol konfirmasi dialog `Cancel Report` aktif kembali sesudah timeout pada Cancel Missing Report
