---
id: TC-FA-DAMAGED-E2E-030-report-damaged-satu-aset-dep-asset
title: "Report Damaged satu aset dari Asset List / Asset Detail oleh Pelapor admin membuat record Damaged, banner Asset Detail, dan status global Damaged"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-01, §4.1#r5, §4.1#r10, §4.2.3#p1, §4.2.3#p2, §4.2.3#b2, §4.4#r3, TS-DMG-01, S-DMG-18, S-DMG-19, §4.2.2#p1, §8.2#b1, §Aturan Logika Modul#r14, §Aturan Logika Modul#r15, §Aturan Logika Modul#r46, §Aturan Logika Modul#r48, §Aturan Logika Modul#r52, §Aturan Logika Modul#r26, §9.7#r1, §3#p2, EC-DMG-04, §9.4.4#r2, F-DMG-01, §4.8#r2, §2.1#r2, §9.6#r1, T-DMG-01, §8.2#p4, §8.2#p5, §8.2#p6, §8.2#p7, §8.2#p10, §Aturan Logika Modul#r18, §8.1#p1, §4.2.4#p13, EB-FB-1@report-damaged, EB-FRM-1@report-damaged]
smoke: [EB-FB-1@report-damaged, EB-FRM-1@report-damaged]
dependsOn:
  - "Asset: Asset List dan Asset Detail (tombol Report Damaged, banner Damaged)"
trace:
  D-DMG-01: [13, 46]
  §4.1#r5: [10, 13]
  §4.1#r10: [23, 26, 46]
  §4.2.3#p1: [10, 45]
  §4.2.3#p2: [4, 5, 6, 41]
  §4.2.3#b2: [54, 57]
  §4.4#r3: [10, 45]
  TS-DMG-01: [10, 45]
  S-DMG-18: [61, 62]
  S-DMG-19: [23, 24, 46, 70, 71, 72, 80, 87]
  §4.2.2#p1: 26
  §8.2#b1: [31, 32, 33, 34, 116, 118, 119]
  §Aturan Logika Modul#r14: 51
  §Aturan Logika Modul#r15: [51, 63, 73, 127, 130]
  §Aturan Logika Modul#r46: 14
  §Aturan Logika Modul#r48: [27, 28]
  §Aturan Logika Modul#r52: 15
  §Aturan Logika Modul#r26: [21, 47]
  §9.7#r1: [21, 47]
  §3#p2: [14, 21]
  EC-DMG-04: [54, 57]
  §9.4.4#r2: [54, 57]
  F-DMG-01: [10, 45]
  §4.8#r2: [2, 39]
  §2.1#r2: [2, 39]
  §9.6#r1: [10, 31]
  T-DMG-01: [14, 15, 16, 17, 18]
  §8.2#p4: [31, 35]
  §8.2#p5: [65, 66]
  §8.2#p6: [75, 76]
  §8.2#p7: [92, 93]
  §8.2#p10: [83, 111]
  §Aturan Logika Modul#r18: [98, 99, 104, 105]
  §8.1#p1: 122
  §4.2.4#p13: [136, 141, 143, 144, 146, 148, 150, 152, 153]
  EB-FB-1@report-damaged: 10
  EB-FRM-1@report-damaged: [13, 31]
anchor: [50, 53, 56, 82, 110, 126, 129, 134]
coverage:
  web: automated
---

# Report Damaged satu aset dari Asset List / Asset Detail oleh Pelapor admin membuat record Damaged, banner Asset Detail, dan status global Damaged

## Prerequisites
- Aktor: Total Control (Pelapor admin).
- Layar awal: halaman Assets, tab Assets (Asset List).
- Data:
  - DU-030-1: aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, status global `Normal`, tanpa record Damage, ada di entitas aktor (dilaporkan dari Asset List).
  - DU-030-2: aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, status global `Normal`, tanpa record Damage, ada di entitas aktor (dilaporkan dari Asset Detail).
  - DU-030-5: aset `Monitor Dell P2422H {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `Damaged` yang dilaporkan pemegang pada `T0 − 5 hari, pukul 09:10` (Reported Date), di-Confirm pada `T0 − 2 hari, pukul 10:30`, dan node terbarunya tercatat pada `T0 − 1 hari, pukul 16:40`, ada di entitas aktor.
  - DU-030-8: aset `Headset Logitech H390 {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `Waiting for Confirmation` yang dilaporkan pemegang pada `T0 − 3 hari, pukul 09:15`, ada di entitas aktor.
  - DU-030-9: aset `Laptop Lenovo ThinkPad E14 {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `Reported Disposal`, ada di entitas aktor.
  - DU-030-10: aset `Keyboard Logitech K380 {runId}`, Group `Head Office`, status global `Damaged`, sudah punya record Damage berjalan berstatus `In Disposal Process`, ada di entitas aktor.
  - DU-030-6: aset `Scanner Fujitsu fi-7160 {runId}`, Group `Head Office`, status `Disposed`, ada di entitas aktor.
  - DU-030-7: aset `Drill Bosch GSB {runId}`, Group `Head Office`, status `Missing`, tanpa record Damage, ada di entitas aktor.
  - DU-030-11: aset `Tablet Samsung Galaxy Tab A8 {runId}`, Group `Head Office`, status global `Normal`, sudah punya record Damage berstatus `Rejected` yang dilaporkan pemegang dan ditolak Aktor Damaged, ada di entitas aktor.
  - DU-030-12: aset `Kamera Canon EOS 200D {runId}`, Group `Head Office`, status global `Normal`, sudah punya record Damage berstatus `Repaired` yang dilaporkan pemegang, di-Confirm, lalu di-Mark as Repaired oleh Aktor Damaged, ada di entitas aktor.
  - DU-030-13: aset `Mesin Fotokopi Ricoh MP 2014 {runId}`, Group `Head Office`, status `Disposed`, sudah punya record Damage berstatus `Disposed` yang dilaporkan pemegang dan di-Confirm, ada di entitas aktor.
  - DU-030-14: aset `Router Mikrotik RB4011 {runId}`, Group `Head Office`, status global `Normal`, sudah punya record Damage berstatus `Canceled` yang dilaporkan pemegang lalu dibatalkan pemegang itu, ada di entitas aktor.
  - DU-030-15: aset `Webcam Logitech C920 {runId}`, Group `Head Office`, status global `Normal`, tanpa record Damage, ada di entitas aktor (dialog Report Damaged dibuka lalu ditinggalkan tanpa dikirim; aset tidak berubah), isian What happened `Kamera web tidak terdeteksi oleh komputer`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.
  - Kemampuan teknis: mengonfirmasi atau menolak dialog `beforeunload` bawaan browser pada F5 dan mengklik menu sidebar.

## Test Steps

### Report Damaged satu aset dari Asset List
1. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
2. Verifikasi aksi `Report Damaged` tersedia untuk baris `Projector Epson EB-X06 {runId}`
3. Klik `[Report Damaged]` pada baris `Projector Epson EB-X06 {runId}`
4. Verifikasi dialog berjudul `Report Damaged` tampil dengan blok aset `Projector Epson EB-X06 {runId}`
5. Verifikasi field `What happened` tampil pada dialog
6. Verifikasi field `Damaged Photo` tampil pada dialog
7. Isi `What happened` dengan `Layar proyektor retak dan tidak menampilkan gambar`
8. Unggah foto `proyektor-retak.jpg` pada `Damaged Photo`
9. Klik `[Report Damaged]` pada footer dialog
10. Verifikasi toast `Success, asset has been reported damaged.` tampil

### Record Damaged tercatat di sub-tab Active tab Damaged
11. Buka tab `Damaged` pada halaman Assets
12. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
13. Verifikasi tepat satu baris `Projector Epson EB-X06 {runId}` tampil di sub-tab `Active`
14. Verifikasi Status baris itu `Damaged`
15. Verifikasi Source baris itu `Manual`
16. Verifikasi Days Damaged baris itu `0 days`
17. Verifikasi Last Holder baris itu `—`
18. Verifikasi Reported Date baris itu tampil dalam Date Format `dd/MM/yy` dan Time Format `24h`

### Status global aset menjadi Damaged di Asset List
19. Buka tab `Assets` pada halaman Assets
20. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
21. Verifikasi status global aset `Damaged` pada baris `Projector Epson EB-X06 {runId}`

### Banner, Damage Log, dan Transaction log di Asset Detail
22. Klik nama aset `Projector Epson EB-X06 {runId}` untuk membuka Asset Detail
23. Verifikasi banner `Damaged since [Date].` tampil
24. Verifikasi `[Date]` pada banner adalah tanggal Reported Date record dalam Date Format `dd/MM/yy`
25. Klik `[View]` pada banner
26. Verifikasi dialog `Damage Log` record aset itu tampil
27. Verifikasi `What happened` `Layar proyektor retak dan tidak menampilkan gambar` tampil pada node `Reported damaged by`
28. Verifikasi `Damaged Photo` tampil pada node `Reported damaged by`
29. Klik `✕` pada dialog Damage Log
30. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
31. Verifikasi tepat satu entri `Reported damaged by [Reporter Name]` tampil
32. Verifikasi kolom `Date`, `Status`, dan `User` tampil pada Transaction log
33. Verifikasi kolom `Transaction ID`, `Reader name`, `Group`, dan `Requested by` tidak tampil pada Transaction log
34. Verifikasi kolom `Date` entri itu tampil dalam Date Format `dd/MM/yy` dan Time Format `24h`
35. Verifikasi kolom `Status` entri itu `Damaged`

### Report Damaged satu aset dari Asset Detail
36. Buka tab `Assets` pada halaman Assets
37. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
38. Klik nama aset `Printer HP LaserJet M404 {runId}` untuk membuka Asset Detail
39. Verifikasi aksi `Report Damaged` tersedia pada Asset Detail
40. Klik `[Report Damaged]` pada Asset Detail
41. Verifikasi dialog berjudul `Report Damaged` tampil dengan blok aset `Printer HP LaserJet M404 {runId}`
42. Isi `What happened` dengan `Kertas macet dan roller printer patah`
43. Unggah foto `printer-roller-patah.jpg` pada `Damaged Photo`
44. Klik `[Report Damaged]` pada footer dialog
45. Verifikasi toast `Success, asset has been reported damaged.` tampil
46. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail aset itu
47. Verifikasi status global aset `Damaged` tampil pada Asset Detail

### Aksi Report Damaged tidak ditawarkan untuk aset yang sudah punya record berjalan
48. Buka tab `Assets` pada halaman Assets
49. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
50. Verifikasi baris `Monitor Dell P2422H {runId}` tampil
51. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Monitor Dell P2422H {runId}`

### Aksi Report Damaged tidak ditawarkan untuk aset Disposed
52. Ganti isi kotak search dengan `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
53. Verifikasi baris `Scanner Fujitsu fi-7160 {runId}` tampil
54. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Scanner Fujitsu fi-7160 {runId}`

### Aksi Report Damaged tidak ditawarkan untuk aset Missing
55. Ganti isi kotak search dengan `Drill Bosch GSB {runId}`, tekan Enter
56. Verifikasi baris `Drill Bosch GSB {runId}` tampil
57. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Drill Bosch GSB {runId}`

### Banner dan Transaction log Waiting for Confirmation di Asset Detail
58. Buka tab `Assets` pada halaman Assets
59. Ganti isi kotak search dengan `Headset Logitech H390 {runId}`, tekan Enter
60. Klik nama aset `Headset Logitech H390 {runId}` untuk membuka Asset Detail
61. Verifikasi banner `Damage reported on [Date]. Waiting for review.` tampil
62. Verifikasi `[Date]` pada banner adalah tanggal Reported Date record, yaitu `T0 − 3 hari`, dalam Date Format `dd/MM/yy`
63. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) pada Asset Detail aset itu
64. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
65. Verifikasi entri `Reported damaged by [Reporter Name]` tampil
66. Verifikasi kolom `Status` entri itu `Waiting for Confirmation`

### Tanggal banner Damaged mengikuti Reported Date dan peristiwa Confirm di Transaction log
67. Buka tab `Assets` pada halaman Assets
68. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
69. Klik nama aset `Monitor Dell P2422H {runId}` untuk membuka Asset Detail
70. Verifikasi banner `Damaged since [Date].` tampil
71. Verifikasi `[Date]` pada banner adalah tanggal Reported Date record, yaitu `T0 − 5 hari`, dalam Date Format `dd/MM/yy`
72. Verifikasi `[Date]` pada banner bukan tanggal Confirm `T0 − 2 hari` dan bukan tanggal node terbaru `T0 − 1 hari`
73. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) pada Asset Detail aset itu
74. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
75. Verifikasi entri `Report confirmed by [Admin Name]` tampil
76. Verifikasi kolom `Status` entri itu `Damaged`

### Banner Damaged dan peristiwa Disposal di Transaction log untuk record Reported Disposal dan In Disposal Process
77. Buka tab `Assets` pada halaman Assets
78. Ganti isi kotak search dengan `Laptop Lenovo ThinkPad E14 {runId}`, tekan Enter
79. Klik nama aset `Laptop Lenovo ThinkPad E14 {runId}` untuk membuka Asset Detail
80. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail aset ber-record `Reported Disposal`
81. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
82. Verifikasi entri `Reported damaged by [Reporter Name]` tampil
83. Verifikasi entri `Disposal reported by` tidak tampil pada Transaction log
84. Buka tab `Assets` pada halaman Assets
85. Ganti isi kotak search dengan `Keyboard Logitech K380 {runId}`, tekan Enter
86. Klik nama aset `Keyboard Logitech K380 {runId}` untuk membuka Asset Detail
87. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail aset ber-record `In Disposal Process`

### Peristiwa Report rejected di Transaction log
88. Buka tab `Assets` pada halaman Assets
89. Ganti isi kotak search dengan `Tablet Samsung Galaxy Tab A8 {runId}`, tekan Enter
90. Klik nama aset `Tablet Samsung Galaxy Tab A8 {runId}` untuk membuka Asset Detail
91. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
92. Verifikasi entri `Report rejected by [Admin Name]` tampil
93. Verifikasi kolom `Status` entri itu `Rejected`

### Peristiwa Marked as repaired di Transaction log
94. Buka tab `Assets` pada halaman Assets
95. Ganti isi kotak search dengan `Kamera Canon EOS 200D {runId}`, tekan Enter
96. Klik nama aset `Kamera Canon EOS 200D {runId}` untuk membuka Asset Detail
97. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
98. Verifikasi entri `Marked as repaired by [Admin Name]` tampil
99. Verifikasi kolom `Status` entri itu `Repaired`

### Peristiwa Disposed di Transaction log
100. Buka tab `Assets` pada halaman Assets
101. Ganti isi kotak search dengan `Mesin Fotokopi Ricoh MP 2014 {runId}`, tekan Enter
102. Klik nama aset `Mesin Fotokopi Ricoh MP 2014 {runId}` untuk membuka Asset Detail
103. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
104. Verifikasi entri `Disposed` tampil
105. Verifikasi kolom `Status` entri `Disposed` itu `Disposed`

### Report canceled tidak membentuk baris di Transaction log
106. Buka tab `Assets` pada halaman Assets
107. Ganti isi kotak search dengan `Router Mikrotik RB4011 {runId}`, tekan Enter
108. Klik nama aset `Router Mikrotik RB4011 {runId}` untuk membuka Asset Detail
109. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
110. Verifikasi entri `Reported damaged by [Reporter Name]` tampil
111. Verifikasi entri `Report canceled by [Reporter Name]` tidak tampil pada Transaction log

### Isi kolom User dan urutan kolom Transaction log
112. Buka tab `Assets` pada halaman Assets
113. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
114. Klik nama aset `Projector Epson EB-X06 {runId}` untuk membuka Asset Detail
115. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
116. Verifikasi kolom `User` entri `Reported damaged by [Reporter Name]` berisi pelapor record itu, yaitu Aktor
117. Arahkan kursor ke kolom `User` entri `Reported damaged by [Reporter Name]`
118. Verifikasi nama lengkap Aktor tampil
119. Verifikasi urutan kolom Transaction log adalah `Date`, `Status`, `User`

### Dialog Damage Log dibuka dari aksi baris Transaction log
120. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
121. Klik aksi baris `[Transaction] Log` pada entri `Reported damaged by [Reporter Name]`
122. Verifikasi dialog `Damage Log` record aset `Projector Epson EB-X06 {runId}` tampil
123. Klik `✕` pada dialog Damage Log

### Aksi Report Damaged tidak ditawarkan untuk aset ber-record Reported Disposal dan In Disposal Process
124. Buka tab `Assets` pada halaman Assets
125. Ganti isi kotak search dengan `Laptop Lenovo ThinkPad E14 {runId}`, tekan Enter
126. Verifikasi baris `Laptop Lenovo ThinkPad E14 {runId}` tampil
127. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Laptop Lenovo ThinkPad E14 {runId}`
128. Ganti isi kotak search dengan `Keyboard Logitech K380 {runId}`, tekan Enter
129. Verifikasi baris `Keyboard Logitech K380 {runId}` tampil
130. Verifikasi aksi `Report Damaged` tidak tampil (Hidden) untuk baris `Keyboard Logitech K380 {runId}`

### Form Report Damaged kotor: reload dan navigasi in-app
131. Buka tab `Assets` pada halaman Assets
132. Ganti isi kotak search dengan `Webcam Logitech C920 {runId}`, tekan Enter
133. Klik `[Report Damaged]` pada baris `Webcam Logitech C920 {runId}`
134. Verifikasi dialog berjudul `Report Damaged` tampil dengan blok aset `Webcam Logitech C920 {runId}`, form belum diubah
135. Tekan F5
136. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
137. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
138. Klik `[Report Damaged]` pada baris `Webcam Logitech C920 {runId}`
139. Isi `What happened` dengan `Kamera web tidak terdeteksi oleh komputer`
140. Tekan F5
141. Verifikasi konfirmasi bawaan browser muncul (teks dan tombol ditentukan browser)
142. Pilih tetap berada di halaman pada konfirmasi bawaan browser
143. Verifikasi dialog berjudul `Report Damaged` tetap terbuka dengan blok aset `Webcam Logitech C920 {runId}`
144. Verifikasi `What happened` masih `Kamera web tidak terdeteksi oleh komputer`
145. Klik menu `Dashboard` pada sidebar
146. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]` tampil
147. Klik `[Cancel]`
148. Verifikasi dialog berjudul `Report Damaged` tetap terbuka dengan `What happened` masih `Kamera web tidak terdeteksi oleh komputer`
149. Klik menu `Dashboard` pada sidebar
150. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]` tampil
151. Klik `[Leave]`
152. Verifikasi halaman Dashboard tampil
153. Verifikasi dialog berjudul `Report Damaged` tidak tampil
