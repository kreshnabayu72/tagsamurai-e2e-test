---
id: TC-FA-MYASSET-UI-121-dialog-confirm-handover-reaksi-respons
title: "Dialog Confirm Handover: toast sukses dan gagal, dialog Handover No Longer Available per penyebab"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-03", "§1.2#r54", "§4.2.1#b5", "§4.2.5#p10", "§4.2.5#p11", "§4.2.5#p12", "§4.2.5#r5", "§4.2.5#r6", "§4.4#r40", "§4.4#r41", "§7.2#r2", "§7.3#r1", "§7.3#r11", "§7.3#r15", "§9.2#r3", "§9.4.2#r40", "§9.4.2#r41", "§9.4.2#r44", "§9.4.2#r56", "§9.4.2#r60", "§9.4.2#r93", "§9.6#r1", "§9.6#r10", "§9.6#p1", "EB-FB-1@confirm-handover", "EB-FB-1@confirm-handover-assignment", "EB-FB-2@confirm-handover", "EB-FB-4", "EB-ERR-1@confirm-handover", "EB-ERR-1@confirm-handover-assignment"]
smoke: []
dependsOn: []
trace:
  "V-03": [33, 34, 45, 46, 52, 53]
  "§1.2#r54": [108, 109]
  "§4.2.1#b5": 12
  "§4.2.5#p10": [34, 46, 53, 61, 68, 75]
  "§4.2.5#p11": [33, 34, 35, 45, 46, 52, 53, 60, 61, 67, 68, 74, 75]
  "§4.2.5#p12": [38, 39, 40]
  "§4.2.5#r5": [33, 34, 45, 46, 52, 53]
  "§4.2.5#r6": [60, 61, 67, 68, 74, 75, 76]
  "§4.4#r40": [33, 45, 52, 60, 67, 74]
  "§4.4#r41": [38, 39, 40]
  "§7.2#r2": [33, 34, 35, 46, 53, 75]
  "§7.3#r1": [11, 20]
  "§7.3#r11": 26
  "§7.3#r15": [82, 115, 138]
  "§9.2#r3": 53
  "§9.4.2#r40": [33, 45]
  "§9.4.2#r41": [38, 39, 40]
  "§9.4.2#r44": 53
  "§9.4.2#r56": [60, 67]
  "§9.4.2#r60": [67, 74]
  "§9.4.2#r93": [33, 34]
  "§9.6#r1": [11, 13, 82, 88, 103, 144]
  "§9.6#r10": [26, 27, 28, 115, 117, 118]
  "§9.6#p1": [82, 84, 85, 87, 98, 99, 100, 102, 138, 140, 141, 142, 143, 151, 153, 154, 155, 156]
  "EB-FB-1@confirm-handover": [11, 20, 82]
  "EB-FB-1@confirm-handover-assignment": [26, 115, 121]
  "EB-FB-2@confirm-handover": [6, 36, 47, 54]
  "EB-FB-4": [15, 90]
  "EB-ERR-1@confirm-handover": [82, 83, 84, 85, 86, 92, 98, 99, 100, 101, 138, 139, 140, 141, 142, 143, 151, 152, 153, 154, 155, 156]
  "EB-ERR-1@confirm-handover-assignment": [115, 116, 117, 118, 119, 121, 127, 128, 129, 130, 131]
anchor: [5]
coverage:
  web: automated
---

# Dialog Confirm Handover: toast sukses dan gagal, dialog Handover No Longer Available per penyebab

## Prerequisites
- Aktor: Borrower `Budi Santoso` pada kondisi K1 sampai K5 dan K10 sampai K12, Assignee Employee `Budi Santoso` pada kondisi K6 sampai K9, K13, dan K14, dan PIC Borrower, yaitu PIC dari Borrower tanpa akun `Dewi Lestari`, pada kondisi K15 dan K16.
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
  - DU-121-19: hasil Confirm ulang Assignment dua aset dicentang dijawab sukses dengan toast sukses.
  - DU-121-20: Task Confirm Handover (Borrow) atas nama Borrower tanpa akun dengan Transaction ID `BRW-2026-0165`, Task `Confirm Handover`, Group `Head Office`, Total Asset `2`, Handed Over By `Rina W`, Expires At `09/11/26, 20:55`, Borrower `Dewi Lestari`.
  - DU-121-21: aset sesi Handover dengan Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 52`, Asset ID `LPT-2026-0052`, Brand `Dell`, Model/Type `Latitude 5420`, Return by `13/11/26`.
  - DU-121-22: aset sesi Handover dengan Photo `meeting-mic-set.jpg`, Name `Meeting Mic Set - 11`, Asset ID `MIC-2026-0011`, Brand `Jabra`, Model/Type `Speak 510`, Return by `14/11/26`.
  - DU-121-23: pernyataan PIC `I confirm that Dewi Lestari has received the checked assets.` yang belum dicentang.
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
  - K10: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, Confirm pertama dijawab error server, dan pemuatan ulang tabel sesudahnya mengembalikan Task DU-121-1 tanpa perubahan, dan Confirm berikutnya dijawab sukses (DU-121-12).
  - K11: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, Confirm tidak mendapat respons karena koneksi terputus, dan pemuatan ulang tabel sesudahnya mengembalikan Task DU-121-1 tanpa perubahan.
  - K12: Task DU-121-1 dengan aset DU-121-2 sampai DU-121-4, dan Confirm ditolak karena Borrower bukan pemegang baris itu lagi.
  - K13: Task DU-121-7 dengan aset DU-121-8 dan DU-121-9, Confirm pertama dijawab error server, dan Confirm berikutnya dijawab sukses (DU-121-19).
  - K14: Task DU-121-7 dengan aset DU-121-8 dan DU-121-9, dan Confirm tidak mendapat respons karena koneksi terputus.
  - K15: Task DU-121-20 dengan aset DU-121-21 dan DU-121-22 tampil di tab Task, pernyataan PIC DU-121-23 belum dicentang, Confirm dijawab error server, dan pemuatan ulang tabel sesudahnya mengembalikan Task DU-121-20 tanpa perubahan.
  - K16: Task DU-121-20 dengan aset DU-121-21 dan DU-121-22 tampil di tab Task, pernyataan PIC DU-121-23 belum dicentang, dan Confirm tidak mendapat respons karena koneksi terputus.

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
47. Verifikasi toast tidak tampil

### Sudah dikonfirmasi lewat cara lain pada Borrow
48. Tampilkan Dialog Confirm Handover dengan kondisi K5
49. Klik `⋯` pada baris Task `BRW-2026-0152`
50. Klik `Confirm Handover`
51. Klik `[Confirm]`
52. Verifikasi dialog `Handover No Longer Available` tampil
53. Verifikasi pesan `This handover has already been confirmed.` tampil
54. Verifikasi toast tidak tampil

### Jendela konfirmasi habis pada Assignment
55. Tampilkan Dialog Confirm Handover dengan kondisi K7
56. Klik `⋯` pada baris Task `ASG-2026-0071`
57. Klik `Confirm Handover`
58. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
59. Klik `[Confirm]`
60. Verifikasi dialog `Handover No Longer Available` tampil
61. Verifikasi pesan `This handover has expired. Ask Rina W to start again.` tampil

### Sesi Handover Assignment dibatalkan Aktor
62. Tampilkan Dialog Confirm Handover dengan kondisi K8
63. Klik `⋯` pada baris Task `ASG-2026-0071`
64. Klik `Confirm Handover`
65. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
66. Klik `[Confirm]`
67. Verifikasi dialog `Handover No Longer Available` tampil
68. Verifikasi pesan `Rina W canceled this handover request. Ask them to start again if you still need the assets.` tampil

### Transaksi Assignment tidak aktif lagi
69. Tampilkan Dialog Confirm Handover dengan kondisi K9
70. Klik `⋯` pada baris Task `ASG-2026-0071`
71. Klik `Confirm Handover`
72. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
73. Klik `[Confirm]`
74. Verifikasi dialog `Handover No Longer Available` tampil
75. Verifikasi pesan `This assignment is no longer active.` tampil
76. Verifikasi dialog memuat tombol `[OK]`

### Gagal server pada Confirm Borrow lalu dicoba ulang
77. Tampilkan Dialog Confirm Handover dengan kondisi K10
78. Klik `⋯` pada baris Task `BRW-2026-0152`
79. Klik `Confirm Handover`
80. Hapus centang baris `Meeting Mic Set - 5`
81. Klik `[Confirm]`
82. Verifikasi toast `Error, failed to hand over assets.` tampil
83. Verifikasi toast tidak memuat tombol aksi
84. Verifikasi dialog `Confirm Handover` tetap terbuka
85. Verifikasi baris `Meeting Mic Set - 5` tetap tidak tercentang, sedangkan baris `Projector Epson EB-X06 - 12` dan `Laptop Dell Latitude 5420 - 21` tetap tercentang
86. Verifikasi tombol `[Confirm]` aktif lagi
87. Verifikasi tabel My Asset dimuat ulang
88. Verifikasi baris Task `BRW-2026-0152` dengan Task `Confirm Handover` tetap tampil di tab Task
89. Waktu berlalu 10 detik sejak toast tampil
90. Verifikasi toast `Error, failed to hand over assets.` masih tampil
91. Klik `[Confirm]`
92. Verifikasi toast `Success, 2 assets have been handed over.` tampil

### Koneksi terputus pada Confirm Borrow
93. Tampilkan Dialog Confirm Handover dengan kondisi K11
94. Klik `⋯` pada baris Task `BRW-2026-0152`
95. Klik `Confirm Handover`
96. Hapus centang baris `Meeting Mic Set - 5`
97. Klik `[Confirm]`
98. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
99. Verifikasi dialog `Confirm Handover` tetap terbuka
100. Verifikasi baris `Meeting Mic Set - 5` tetap tidak tercentang, sedangkan baris `Projector Epson EB-X06 - 12` dan `Laptop Dell Latitude 5420 - 21` tetap tercentang
101. Verifikasi tombol `[Confirm]` aktif lagi
102. Verifikasi tabel My Asset dimuat ulang
103. Verifikasi baris Task `BRW-2026-0152` dengan Task `Confirm Handover` tetap tampil di tab Task

### Confirm ditolak 403 karena bukan pemegang baris lagi
104. Tampilkan Dialog Confirm Handover dengan kondisi K12
105. Klik `⋯` pada baris Task `BRW-2026-0152`
106. Klik `Confirm Handover`
107. Klik `[Confirm]`
108. Verifikasi toast `You don't have permission to do this.` tampil
109. Verifikasi tabel My Asset dimuat ulang

### Gagal server pada Confirm Assignment
110. Tampilkan Dialog Confirm Handover dengan kondisi K13
111. Klik `⋯` pada baris Task `ASG-2026-0071`
112. Klik `Confirm Handover`
113. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
114. Klik `[Confirm]`
115. Verifikasi toast `Error, failed to hand over assets.` tampil
116. Verifikasi toast tidak memuat tombol aksi
117. Verifikasi dialog `Confirm Handover` tetap terbuka
118. Verifikasi pernyataan `I acknowledge receipt of these assets and accept responsibility for them.` dan kedua aset tetap tercentang
119. Verifikasi tombol `[Confirm]` aktif lagi
120. Klik `[Confirm]`
121. Verifikasi toast sukses tampil

### Koneksi terputus pada Confirm Assignment
122. Tampilkan Dialog Confirm Handover dengan kondisi K14
123. Klik `⋯` pada baris Task `ASG-2026-0071`
124. Klik `Confirm Handover`
125. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
126. Klik `[Confirm]`
127. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
128. Verifikasi toast tidak memuat tombol aksi
129. Verifikasi dialog `Confirm Handover` tetap terbuka
130. Verifikasi pernyataan `I acknowledge receipt of these assets and accept responsibility for them.` dan kedua aset tetap tercentang
131. Verifikasi tombol `[Confirm]` aktif lagi

### PIC Borrower: gagal server pada Confirm
132. Tampilkan Dialog Confirm Handover dengan kondisi K15
133. Klik `⋯` pada baris Task `BRW-2026-0165`
134. Klik `Confirm Handover`
135. Centang checkbox pernyataan `I confirm that Dewi Lestari has received the checked assets.`
136. Hapus centang baris `Meeting Mic Set - 11`
137. Klik `[Confirm]`
138. Verifikasi toast `Error, failed to hand over assets.` tampil
139. Verifikasi toast tidak memuat tombol aksi
140. Verifikasi dialog `Confirm Handover` tetap terbuka
141. Verifikasi pernyataan `I confirm that Dewi Lestari has received the checked assets.` dan baris `Laptop Dell Latitude 5420 - 52` tetap tercentang, sedangkan baris `Meeting Mic Set - 11` tetap tidak tercentang
142. Verifikasi tombol `[Confirm]` aktif lagi
143. Verifikasi tabel My Asset dimuat ulang
144. Verifikasi baris Task `BRW-2026-0165` dengan Task `Confirm Handover` tetap tampil di tab Task

### PIC Borrower: koneksi terputus pada Confirm
145. Tampilkan Dialog Confirm Handover dengan kondisi K16
146. Klik `⋯` pada baris Task `BRW-2026-0165`
147. Klik `Confirm Handover`
148. Centang checkbox pernyataan `I confirm that Dewi Lestari has received the checked assets.`
149. Hapus centang baris `Meeting Mic Set - 11`
150. Klik `[Confirm]`
151. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
152. Verifikasi toast tidak memuat tombol aksi
153. Verifikasi dialog `Confirm Handover` tetap terbuka
154. Verifikasi pernyataan `I confirm that Dewi Lestari has received the checked assets.` dan baris `Laptop Dell Latitude 5420 - 52` tetap tercentang, sedangkan baris `Meeting Mic Set - 11` tetap tidak tercentang
155. Verifikasi tombol `[Confirm]` aktif lagi
156. Verifikasi tabel My Asset dimuat ulang

[^drift-1]: Drift PRD vs foundation. PRD §9.6 Action Resilience Spec: gagal server (5xx atau timeout) pada Confirm Handover (Borrow dan Assignment) memunculkan toast `T-BRW-26` (`Error, failed to hand over assets.`). foundation `error-handling-convention.md` §2: Timeout / Network memunculkan `Connection problem. Please try again.` tanpa tombol aksi. Diasersi: foundation untuk koneksi terputus, karena toast kegagalan adalah pola bersama (SB-4); kegagalan server 5xx tetap memakai `T-BRW-26` dari PRD.
