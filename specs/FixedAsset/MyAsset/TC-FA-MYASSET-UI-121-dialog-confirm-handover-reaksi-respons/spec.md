---
id: TC-FA-MYASSET-UI-121-dialog-confirm-handover-reaksi-respons
title: "Dialog Confirm Handover: toast sukses dan gagal, dialog Handover No Longer Available per penyebab"
layer: ui-client
priority: Critical
caseType: Negative
status: draft
sourceRules: ["V-03", "§1.2#r53", "§4.2.1#b5", "§4.2.5#p10", "§4.2.5#p11", "§4.2.5#p12", "§4.2.5#r5", "§4.2.5#r6", "§4.4#r40", "§4.4#r41", "§7.2#r2", "§7.3#r1", "§7.3#r11", "§7.3#r15", "§9.2#r3", "§9.4.2#r36", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r52", "§9.4.2#r56", "§9.4.2#r88", "§9.6#r1", "§9.6#r10", "§9.6#p1", "EB-FB-1@confirm-handover", "EB-FB-1@confirm-handover-assignment", "EB-FB-2@confirm-handover", "EB-FB-4", "EB-ERR-1@confirm-handover", "EB-ERR-1@confirm-handover-assignment"]
smoke: []
dependsOn: []
trace:
  "V-03": [33, 34, 45, 46, 51, 52]
  "§1.2#r53": [104, 105]
  "§4.2.1#b5": 12
  "§4.2.5#p10": [34, 46, 52, 59, 66, 73]
  "§4.2.5#p11": [33, 34, 35, 45, 46, 51, 52, 58, 59, 65, 66, 72, 73]
  "§4.2.5#p12": [38, 39, 40]
  "§4.2.5#r5": [33, 34, 45, 46, 51, 52]
  "§4.2.5#r6": [58, 59, 65, 66, 72, 73, 74]
  "§4.4#r40": [33, 45, 51, 58, 65, 72]
  "§4.4#r41": [38, 39, 40]
  "§7.2#r2": [33, 34, 35, 46, 52, 73]
  "§7.3#r1": [11, 20]
  "§7.3#r11": 26
  "§7.3#r15": [80, 111]
  "§9.2#r3": 52
  "§9.4.2#r36": [33, 45]
  "§9.4.2#r37": [38, 39, 40]
  "§9.4.2#r40": 52
  "§9.4.2#r52": [58, 65]
  "§9.4.2#r56": [65, 72]
  "§9.4.2#r88": [33, 34]
  "§9.6#r1": [11, 13, 80]
  "§9.6#r10": [26, 27, 28, 111, 112, 113]
  "§9.6#p1": [80, 82, 83, 85, 95, 96, 97, 99]
  "EB-FB-1@confirm-handover": [11, 20, 80]
  "EB-FB-1@confirm-handover-assignment": [26, 111]
  "EB-FB-2@confirm-handover": [6, 36]
  "EB-FB-4": [15, 87]
  "EB-ERR-1@confirm-handover": [80, 81, 82, 83, 84, 89, 95, 96, 97, 98]
  "EB-ERR-1@confirm-handover-assignment": [111, 112, 113, 114]
anchor: [5]
coverage:
  web: automated
---

# Dialog Confirm Handover: toast sukses dan gagal, dialog Handover No Longer Available per penyebab

## Prerequisites
- Aktor: Borrower `Budi Santoso` pada kondisi K1 sampai K5 dan K10 sampai K12, dan Assignee Employee `Budi Santoso` pada kondisi K6 sampai K9 dan K13.
- Layar awal: My Asset > Task.
- Komponen: Dialog Confirm Handover (D-MYA-01)
- Data:
  - DU-121-1: Task Confirm Handover (Borrow) dengan Transaction ID `BRW-2026-0152`, Task `Confirm Handover`, Group `Head Office`, Total Asset `3`, Handed Over By `Rina W`, Expires At `09/11/26, 20:41`, Borrower `Budi Santoso`.
  - DU-121-2: aset sesi Handover dengan Photo `projector-epson-eb-x06.jpg`, Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Brand `Epson`, Model/Type `EB-X06`, Return by `12/11/26`.
  - DU-121-3: aset sesi Handover dengan Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 21`, Asset ID `LPT-2026-0021`, Brand `Dell`, Model/Type `Latitude 5420`, Return by `13/11/26`.
  - DU-121-4: aset sesi Handover dengan Photo `meeting-mic-set.jpg`, Name `Meeting Mic Set - 5`, Asset ID `MIC-2026-0005`, Brand `Jabra`, Model/Type `Speak 510`, Return by `14/11/26`.
  - DU-121-5: Task Confirm Handover (Borrow) satu aset dengan Transaction ID `BRW-2026-0163`, Task `Confirm Handover`, Group `Head Office`, Total Asset `1`, Handed Over By `Rina W`, Expires At `09/11/26, 21:05`, Borrower `Budi Santoso`.
  - DU-121-6: aset sesi Handover dengan Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 40`, Asset ID `LPT-2026-0040`, Brand `Dell`, Model/Type `Latitude 5420`, Return by `13/11/26`.
  - DU-121-7: Task Confirm Handover (Assignment) dengan Transaction ID `ASG-2026-0071`, Task `Confirm Handover`, Group `Head Office`, Total Asset `2`, Handed Over By `Rina W`, Expires At `09/11/26, 20:43`, Assignee `Budi Santoso`.
  - DU-121-8: aset sesi Handover Assignment dengan Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 44`, Asset ID `LPT-2026-0044`, Brand `Dell`, Model/Type `Latitude 5420`.
  - DU-121-9: aset sesi Handover Assignment dengan Photo `meeting-mic-set.jpg`, Name `Meeting Mic Set - 7`, Asset ID `MIC-2026-0007`, Brand `Jabra`, Model/Type `Speak 510`.
  - DU-121-10: hasil Confirm tiga aset dicentang dengan toast `Success, 3 assets have been handed over.`.
  - DU-121-11: hasil Confirm satu aset dicentang dengan toast `Success, 1 asset has been handed over.`.
  - DU-121-12: hasil Confirm ulang dua aset dicentang dengan toast `Success, 2 assets have been handed over.`.
  - DU-121-13: penolakan Borrow karena jendela konfirmasi habis dengan Admin `Rina W` dan pesan `This handover has expired. Ask Rina W to start again.`.
  - DU-121-14: penolakan Borrow karena admin menekan Cancel Request dengan Admin `Rina W` dan pesan `Rina W canceled this handover request. Ask them to start again if you still need the assets.`.
  - DU-121-15: penolakan Borrow karena sudah dikonfirmasi lewat cara lain dengan pesan `This handover has already been confirmed.`.
  - DU-121-16: penolakan Assignment karena jendela konfirmasi habis dengan Admin `Rina W` dan pesan `This handover has expired. Ask Rina W to start again.`.
  - DU-121-17: penolakan Assignment karena sesi Handover dibatalkan Aktor Assignment penyerah `Rina W` dengan pesan `Rina W canceled this handover request. Ask them to start again if you still need the assets.`.
  - DU-121-18: penolakan Assignment karena transaksi dibatalkan, ditolak, atau ditutup sistem dengan pesan `This assignment is no longer active.`.
- Kondisi:
  - K1: Task DU-121-1 tampil di tab Task, sesi Handover-nya memuat aset DU-121-2 sampai DU-121-4, dan Confirm dijawab sukses (DU-121-10).
  - K2: Task DU-121-5 tampil di tab Task, sesi Handover-nya memuat aset DU-121-6, dan Confirm dijawab sukses (DU-121-11).
  - K3: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, dan Confirm ditolak karena jendela konfirmasi habis (DU-121-13).
  - K4: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, dan Confirm ditolak karena admin menekan Cancel Request (DU-121-14).
  - K5: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, dan Confirm ditolak karena sudah dikonfirmasi lewat cara lain (DU-121-15).
  - K6: Task DU-121-7 dengan aset DU-121-8 dan DU-121-9, dan Confirm dijawab sukses.
  - K7: Task DU-121-7 dengan aset DU-121-8 dan DU-121-9, dan Confirm ditolak karena jendela konfirmasi habis (DU-121-16).
  - K8: Task DU-121-7 dengan aset DU-121-8 dan DU-121-9, dan Confirm ditolak karena sesi Handover dibatalkan Aktor (DU-121-17).
  - K9: Task DU-121-7 dengan aset DU-121-8 dan DU-121-9, dan Confirm ditolak karena transaksi tidak aktif lagi (DU-121-18).
  - K10: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, Confirm pertama dijawab error server, dan Confirm berikutnya dijawab sukses (DU-121-12).
  - K11: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, dan Confirm tidak mendapat respons karena koneksi terputus.
  - K12: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, dan Confirm ditolak karena Borrower bukan pemegang baris itu lagi.
  - K13: Task DU-121-7 dengan aset DU-121-8 dan DU-121-9, dan Confirm dijawab error server.

## Test Steps

### Cancel menutup dialog tanpa toast
1. Tampilkan Dialog Confirm Handover dengan kondisi K1
2. Klik `⋯` pada baris Task `BRW-2026-0152`
3. Klik `Confirm Handover`
4. Klik `[Cancel]`
5. Verifikasi dialog `Confirm Handover` tertutup
6. Verifikasi toast tidak tampil

### Confirm tiga aset berhasil dan toast sukses hilang sendiri
7. Tampilkan Dialog Confirm Handover dengan kondisi K1
8. Klik `⋯` pada baris Task `BRW-2026-0152`
9. Klik `Confirm Handover`
10. Klik `[Confirm]`
11. Verifikasi toast `Success, 3 assets have been handed over.` tampil
12. Verifikasi toast tampil di kanan bawah layar
13. Verifikasi dialog `Confirm Handover` tertutup
14. Waktu berlalu 5 detik sejak toast tampil
15. Verifikasi toast `Success, 3 assets have been handed over.` tidak tampil lagi

### Confirm satu aset berhasil
16. Tampilkan Dialog Confirm Handover dengan kondisi K2
17. Klik `⋯` pada baris Task `BRW-2026-0163`
18. Klik `Confirm Handover`
19. Klik `[Confirm]`
20. Verifikasi toast `Success, 1 asset has been handed over.` tampil

### Confirm Assignment berhasil
21. Tampilkan Dialog Confirm Handover dengan kondisi K6
22. Klik `⋯` pada baris Task `ASG-2026-0071`
23. Klik `Confirm Handover`
24. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
25. Klik `[Confirm]`
26. Verifikasi toast sukses tampil
27. Verifikasi dialog `Confirm Handover` tertutup
28. Verifikasi tab Task aktif

### Jendela konfirmasi habis pada Borrow
29. Tampilkan Dialog Confirm Handover dengan kondisi K3
30. Klik `⋯` pada baris Task `BRW-2026-0152`
31. Klik `Confirm Handover`
32. Klik `[Confirm]`
33. Verifikasi dialog `Handover No Longer Available` tampil
34. Verifikasi pesan `This handover has expired. Ask Rina W to start again.` tampil
35. Verifikasi dialog memuat tombol `[OK]`
36. Verifikasi toast tidak tampil
37. Klik `[OK]`
38. Verifikasi dialog `Handover No Longer Available` tertutup
39. Verifikasi baris Task `BRW-2026-0152` tidak tampil di tab Task
40. Verifikasi tabel My Asset dimuat ulang

### Admin menekan Cancel Request pada Borrow
41. Tampilkan Dialog Confirm Handover dengan kondisi K4
42. Klik `⋯` pada baris Task `BRW-2026-0152`
43. Klik `Confirm Handover`
44. Klik `[Confirm]`
45. Verifikasi dialog `Handover No Longer Available` tampil
46. Verifikasi pesan `Rina W canceled this handover request. Ask them to start again if you still need the assets.` tampil

### Sudah dikonfirmasi lewat cara lain pada Borrow
47. Tampilkan Dialog Confirm Handover dengan kondisi K5
48. Klik `⋯` pada baris Task `BRW-2026-0152`
49. Klik `Confirm Handover`
50. Klik `[Confirm]`
51. Verifikasi dialog `Handover No Longer Available` tampil
52. Verifikasi pesan `This handover has already been confirmed.` tampil

### Jendela konfirmasi habis pada Assignment
53. Tampilkan Dialog Confirm Handover dengan kondisi K7
54. Klik `⋯` pada baris Task `ASG-2026-0071`
55. Klik `Confirm Handover`
56. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
57. Klik `[Confirm]`
58. Verifikasi dialog `Handover No Longer Available` tampil
59. Verifikasi pesan `This handover has expired. Ask Rina W to start again.` tampil

### Sesi Handover Assignment dibatalkan Aktor
60. Tampilkan Dialog Confirm Handover dengan kondisi K8
61. Klik `⋯` pada baris Task `ASG-2026-0071`
62. Klik `Confirm Handover`
63. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
64. Klik `[Confirm]`
65. Verifikasi dialog `Handover No Longer Available` tampil
66. Verifikasi pesan `Rina W canceled this handover request. Ask them to start again if you still need the assets.` tampil

### Transaksi Assignment tidak aktif lagi
67. Tampilkan Dialog Confirm Handover dengan kondisi K9
68. Klik `⋯` pada baris Task `ASG-2026-0071`
69. Klik `Confirm Handover`
70. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
71. Klik `[Confirm]`
72. Verifikasi dialog `Handover No Longer Available` tampil
73. Verifikasi pesan `This assignment is no longer active.` tampil
74. Verifikasi dialog memuat tombol `[OK]`

### Gagal server pada Confirm Borrow lalu dicoba ulang
75. Tampilkan Dialog Confirm Handover dengan kondisi K10
76. Klik `⋯` pada baris Task `BRW-2026-0152`
77. Klik `Confirm Handover`
78. Hapus centang baris `Meeting Mic Set - 5`
79. Klik `[Confirm]`
80. Verifikasi toast `Error, failed to hand over assets.` tampil
81. Verifikasi toast tidak memuat tombol aksi
82. Verifikasi dialog `Confirm Handover` tetap terbuka
83. Verifikasi baris `Meeting Mic Set - 5` tetap tidak tercentang, sedangkan baris `Projector Epson EB-X06 - 12` dan `Laptop Dell Latitude 5420 - 21` tetap tercentang
84. Verifikasi tombol `[Confirm]` aktif lagi
85. Verifikasi tabel My Asset dimuat ulang
86. Waktu berlalu 10 detik sejak toast tampil
87. Verifikasi toast `Error, failed to hand over assets.` masih tampil
88. Klik `[Confirm]`
89. Verifikasi toast `Success, 2 assets have been handed over.` tampil

### Koneksi terputus pada Confirm Borrow
90. Tampilkan Dialog Confirm Handover dengan kondisi K11
91. Klik `⋯` pada baris Task `BRW-2026-0152`
92. Klik `Confirm Handover`
93. Hapus centang baris `Meeting Mic Set - 5`
94. Klik `[Confirm]`
95. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
96. Verifikasi dialog `Confirm Handover` tetap terbuka
97. Verifikasi baris `Meeting Mic Set - 5` tetap tidak tercentang, sedangkan baris `Projector Epson EB-X06 - 12` dan `Laptop Dell Latitude 5420 - 21` tetap tercentang
98. Verifikasi tombol `[Confirm]` aktif lagi
99. Verifikasi tabel My Asset dimuat ulang

### Confirm ditolak 403 karena bukan pemegang baris lagi
100. Tampilkan Dialog Confirm Handover dengan kondisi K12
101. Klik `⋯` pada baris Task `BRW-2026-0152`
102. Klik `Confirm Handover`
103. Klik `[Confirm]`
104. Verifikasi toast `You don't have permission to do this.` tampil
105. Verifikasi tabel My Asset dimuat ulang

### Gagal server pada Confirm Assignment
106. Tampilkan Dialog Confirm Handover dengan kondisi K13
107. Klik `⋯` pada baris Task `ASG-2026-0071`
108. Klik `Confirm Handover`
109. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
110. Klik `[Confirm]`
111. Verifikasi toast `Error, failed to hand over assets.` tampil
112. Verifikasi dialog `Confirm Handover` tetap terbuka
113. Verifikasi pernyataan `I acknowledge receipt of these assets and accept responsibility for them.` dan kedua aset tetap tercentang
114. Verifikasi tombol `[Confirm]` aktif lagi

[^drift-1]: Drift PRD vs foundation. PRD §9.6 Action Resilience Spec: gagal server (5xx atau timeout) pada Confirm Handover (Borrow) memunculkan toast `T-BRW-26` (`Error, failed to hand over assets.`). foundation `error-handling-convention.md` §2: Timeout / Network memunculkan `Connection problem. Please try again.` tanpa tombol aksi. Diasersi: foundation untuk koneksi terputus, karena toast kegagalan adalah pola bersama (SB-4); kegagalan server 5xx tetap memakai `T-BRW-26` dari PRD.
