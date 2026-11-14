---
id: TC-FA-DAMAGED-UI-116-dialog-damage-log
title: "Dialog Damage Log: judul tanpa nomor, pihak, badge status dan penanda, footer Review hanya saat berhak dengan Confirm/Reject Disabled bagi pelapor, Confirm tanpa dialog kedua, reaksi sesudah Confirm, dan navigasi Prev/Next"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-11, "§4.1#r4", "§8.1#r1", "§8.1#r2", "§8.1#r3", "§8.1#r4", "§8.1#r5", "§8.1#r6", "§8.1#b1", "§4.4#r4", "§4.4#r5", "§4.4#p1", "§7.1#r3", TS-DMG-04, "§9.6#r2", EB-FB-1@confirm, EB-ERR-1@confirm, "§8.1#r7", "§8.1#r8", "§8.1#r9", "§8.1#r10", "§8.1#r11", "§8.1#r12", "§8.1#r13", "§8.1#r14", "§8.1#r15", "§8.1#r16"]
smoke: []
dependsOn: []
trace:
  D-DMG-11: [2, 5, 10, 11, 28]
  "§4.1#r4": [3, 9]
  "§8.1#r1": [2]
  "§8.1#r2": [4]
  "§8.1#r3": [13, 16, 17, 18, 21, 22]
  "§8.1#r4": [6, 7]
  "§8.1#r5": [8, 27, 30, 31, 34, 35]
  "§8.1#r6": [10, 11, 12, 24, 25, 28, 32, 48, 98, 99, 101, 102, 105]
  "§8.1#b1": [41, 42, 43, 51, 52, 53, 54, 55]
  "§4.4#r4": [10, 11]
  "§4.4#r5": [38, 39, 40]
  "§4.4#p1": [40, 41, 42, 43, 45, 52, 53, 54, 55, 108, 110, 112]
  "§7.1#r3": [9]
  TS-DMG-04: [38, 58]
  "§9.6#r2": [38, 58, 59]
  EB-FB-1@confirm: [38, 58]
  EB-ERR-1@confirm: [58, 59, 60, 62, 65, 66]
  "§8.1#r7": [68, 69, 70, 72, 74, 75]
  "§8.1#r8": [77, 78, 79]
  "§8.1#r9": [81]
  "§8.1#r10": [83, 84]
  "§8.1#r11": [85]
  "§8.1#r12": [87, 88]
  "§8.1#r13": [90]
  "§8.1#r14": [91]
  "§8.1#r15": [92, 94]
  "§8.1#r16": [96]
anchor: []
coverage:
  web: automated
---

# Dialog Damage Log: judul tanpa nomor, pihak, badge status dan penanda, footer Review hanya saat berhak dengan Confirm/Reject Disabled bagi pelapor, Confirm tanpa dialog kedua, reaksi sesudah Confirm, dan navigasi Prev/Next

## Prerequisites
- Aktor: Aktor Damaged pada Group aset yang membuka dialog Damage Log (`Rina W`); pada K2 pelapor yang juga Aktor Damaged; pada K19 dan K20 pengguna tanpa hak Aktor Damaged.
- Layar awal: Dialog Damage Log belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Damage Log (D-DMG-11)
- Data:
  - DU-116-1: record `Waiting for Confirmation` untuk aset `Laptop Dell Latitude 5420 - 4`, Holder `Budi S`, Reported By `Budi S`, node pertama `Reported damaged by Budi S` pada `10/11/26, 08:15` dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `kerusakan-layar.jpeg`.
  - DU-116-2: record `Damaged` untuk aset `Projector Epson EB-X06 - 2`, Holder `Sari D`, Reported By `Rina W`.
  - DU-116-3: record `Damaged` untuk aset `Tablet Samsung Tab A8 - 3`, Holder `Dewi A`, Reported By `Agus P`.
  - DU-116-4: pengguna `Rina W` sebagai Aktor Damaged yang bukan pelapor DU-116-1.
  - DU-116-5: pengguna `Budi S` sebagai pelapor DU-116-1 yang juga memegang hak Aktor Damaged.
  - DU-116-6: record `Waiting for Confirmation` untuk aset `Scanner Fujitsu fi-7160 - 2`, Holder `Dewi A`, Reported By `Dewi A`, berpenanda `Reported Missing`.
  - DU-116-7: record `Damaged` untuk aset `Camera Canon EOS - 3`, berpenanda `Missing`.
  - DU-116-8: Reason yang diketik `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`.
  - DU-116-9: record `Damaged` untuk aset `Toyota Avanza - 2` dengan node `Reported damaged by Agus P` (pelapor admin) berisi What happened `Rem tidak berfungsi saat dipakai` dan Damaged Photo `kerusakan-rem.jpeg`.
  - DU-116-10: record `Damaged` untuk aset `Handheld Scanner Zebra TC21 - 2` dengan node `Reported damaged by Sinta M on behalf of Tono R`.
  - DU-116-11: record `Damaged` untuk aset `Projector Epson EB-X06 - 5` Source `Registration` dengan node `Reported damaged by Agus P` berisi What happened `Layar bergaris sejak didaftarkan` tanpa Damaged Photo.
  - DU-116-12: record dengan node `Report confirmed by Yoga T` tanpa detail dan node `Report rejected by Rina W` berisi Reason `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`.
  - DU-116-13: record `Canceled` dengan node `Report canceled by Budi S` tanpa detail.
  - DU-116-14: record dengan node `Asset reported missing`, `Missing report closed`, dan `Asset found` oleh `System`.
  - DU-116-15: record `Repaired` dengan node `Marked as repaired by Rina W` berisi Repair note `Panel layar diganti dan diuji`, After photo `foto-sesudah.jpeg`, dan Manual identification `Identifikasi manual dicatat`.
  - DU-116-16: record dengan node `Disposal reported by Agus P`, `Disposal report declined by Dedi K`, dan `Disposal report canceled by Agus P`, masing-masing berisi Report ID `RPT-DSP-0001`, Reason `Aset tidak ekonomis diperbaiki`, dan pada dua node terakhir Back to Damaged.
  - DU-116-17: record dengan node `Disposal report canceled by System` berisi Report ID `RPT-DSP-0002` dan Back to Damaged.
  - DU-116-18: record `Disposed` dengan node `Disposed` oleh `System` berisi Disposal No. `DSP-2026-0007`.
  - DU-116-19: pengguna `Lia N` dengan role Read Only, cakupan seluruh client, tanpa hak Aktor Damaged.
  - DU-116-20: pengguna `Joko T` dengan role Manage asset & TAG (Read), cakupan Group `Head Office` beserta descendant, tanpa hak Update dan tanpa hak Aktor Damaged.
- Kondisi:
  - K1: DU-116-1 dibuka oleh DU-116-4; daftar record saat dialog dibuka berurutan DU-116-2, DU-116-1, DU-116-3; respons Confirm sukses.
  - K2: DU-116-1 dibuka oleh DU-116-5.
  - K3: DU-116-2 dibuka oleh DU-116-4.
  - K4: DU-116-6 dibuka oleh DU-116-4.
  - K5: DU-116-7 dibuka oleh DU-116-4.
  - K6: DU-116-1 dibuka oleh DU-116-4; respons Reject sukses.
  - K7: DU-116-1 dibuka oleh DU-116-4; respons Confirm pertama gagal karena error server, respons berikutnya sukses.
  - K8: DU-116-1 dibuka oleh DU-116-4; permintaan Confirm melewati batas waktu.
  - K9: DU-116-9.
  - K10: DU-116-10.
  - K11: DU-116-11.
  - K12: DU-116-12.
  - K13: DU-116-13.
  - K14: DU-116-14.
  - K15: DU-116-15.
  - K16: DU-116-16.
  - K17: DU-116-17.
  - K18: DU-116-18.
  - K19: DU-116-1 dibuka oleh DU-116-19.
  - K20: DU-116-1 dibuka oleh DU-116-20.
  - K21: DU-116-1 dibuka oleh DU-116-4; daftar record saat dialog dibuka berurutan DU-116-2, DU-116-1, DU-116-3; respons Reject sukses.

## Test Steps

### Isi dialog untuk laporan yang menunggu review
1. Tampilkan Dialog Damage Log dengan kondisi K1
2. Verifikasi judul dialog `Damage Log`
3. Verifikasi tab `Damage Log` tampil sebagai tab aktif
4. Verifikasi header dialog tidak memuat nomor transaksi dan tidak memuat tombol salin
5. Verifikasi header aset memuat `Laptop Dell Latitude 5420 - 4`
6. Verifikasi pihak `Holder` bernilai `Budi S`
7. Verifikasi pihak `Reported By` bernilai `Budi S`
8. Verifikasi badge status record `Waiting for Confirmation` tampil
9. Verifikasi timeline memuat node pertama `Reported damaged by Budi S` dengan tanggal `10/11/26, 08:15`
10. Verifikasi tombol `[Reject]` tampil pada footer
11. Verifikasi tombol `[Confirm]` tampil pada footer
12. Verifikasi tombol `[Reject]` dan `[Confirm]` aktif
13. Verifikasi tombol `Prev` dan `Next` aktif karena record berada di tengah daftar

### Navigasi Prev dan Next dalam daftar
14. Tampilkan Dialog Damage Log dengan kondisi K1
15. Klik `Next`
16. Verifikasi dialog Damage Log menampilkan record `Tablet Samsung Tab A8 - 3`
17. Verifikasi footer review tidak tampil untuk record `Tablet Samsung Tab A8 - 3` yang berstatus `Damaged`
18. Verifikasi `Next` Disabled karena record berada di ujung daftar
19. Klik `Prev`
20. Klik `Prev`
21. Verifikasi dialog Damage Log menampilkan record `Projector Epson EB-X06 - 2`
22. Verifikasi `Prev` Disabled karena record berada di ujung daftar

### Confirm dan Reject Disabled bagi pelapor sendiri
23. Tampilkan Dialog Damage Log dengan kondisi K2
24. Verifikasi tombol `[Reject]` dan `[Confirm]` Disabled bagi pelapor sendiri
25. Verifikasi alasan `You reported this. Ask another admin.` tersampaikan pada tombol `[Confirm]` yang Disabled

### Record Damaged tanpa footer review
26. Tampilkan Dialog Damage Log dengan kondisi K3
27. Verifikasi badge status record `Damaged` tampil pada record `Projector Epson EB-X06 - 2`
28. Verifikasi footer review tidak dirender untuk record yang berstatus `Damaged`

### Laporan menunggu review dengan penanda Reported Missing
29. Tampilkan Dialog Damage Log dengan kondisi K4
30. Verifikasi badge status record `Waiting for Confirmation` tampil
31. Verifikasi penanda `Reported Missing` tampil di samping badge status
32. Verifikasi footer review tidak dirender untuk record yang berpenanda `Reported Missing`

### Record Damaged dengan penanda Missing
33. Tampilkan Dialog Damage Log dengan kondisi K5
34. Verifikasi badge status record `Damaged` tampil pada record `Camera Canon EOS - 3`
35. Verifikasi penanda `Missing` tampil di samping badge status

### Confirm langsung tanpa dialog kedua dan dialog tetap terbuka
36. Tampilkan Dialog Damage Log dengan kondisi K1
37. Klik `[Confirm]`
38. Verifikasi toast `Success, report has been confirmed.` tampil
39. Verifikasi tidak ada dialog konfirmasi kedua yang tampil sesudah `[Confirm]` diklik
40. Verifikasi dialog Damage Log tetap terbuka
41. Verifikasi footer `[Reject]` dan `[Confirm]` hilang
42. Verifikasi badge status record berubah menjadi `Damaged`
43. Verifikasi node `Report confirmed by Rina W` ditambahkan pada timeline
44. Klik `Next`
45. Verifikasi dialog Damage Log menampilkan record `Tablet Samsung Tab A8 - 3` dari daftar saat dialog dibuka

### Reject membuka dialog alasan dan dialog Damage Log tetap terbuka
46. Tampilkan Dialog Damage Log dengan kondisi K6
47. Klik `[Reject]`
48. Verifikasi dialog `Reject Report` terbuka
49. Isi `Reason*` dengan `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
50. Klik `[Reject]` pada dialog `Reject Report`
51. Verifikasi dialog `Reject Report` tertutup
52. Verifikasi dialog Damage Log tetap terbuka sesudah Reject
53. Verifikasi footer `[Reject]` dan `[Confirm]` hilang sesudah Reject
54. Verifikasi badge status record berubah menjadi `Rejected`
55. Verifikasi node `Report rejected by Rina W` ditambahkan pada timeline dengan baris `Reason` berisi `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`

### Confirm gagal 5xx lalu berhasil sesudah pulih
56. Tampilkan Dialog Damage Log dengan kondisi K7
57. Klik `[Confirm]`
58. Verifikasi toast `Error, failed to confirm report.` tampil
59. Verifikasi dialog Damage Log tetap terbuka dengan badge status record `Waiting for Confirmation`
60. Verifikasi tombol `[Confirm]` aktif lagi sesudah simpan gagal
61. Klik `[Confirm]`
62. Verifikasi toast `Success, report has been confirmed.` tampil pada pengiriman ulang

### Confirm timeout
63. Tampilkan Dialog Damage Log dengan kondisi K8
64. Klik `[Confirm]`
65. Verifikasi toast `Connection problem. Please try again.` tampil untuk Confirm yang melewati batas waktu
66. Verifikasi dialog Damage Log tetap terbuka sesudah timeout dengan footer `[Confirm]` aktif

### Node laporan Pelapor admin
67. Tampilkan Dialog Damage Log dengan kondisi K9
68. Verifikasi node `Reported damaged by Agus P` tampil dengan nama pelaku sebagai tautan disertai ikon pengguna
69. Verifikasi node `Reported damaged by Agus P` memuat baris `What happened` dan baris `Damaged Photo`
70. Verifikasi baris `Damaged Photo` tampil sebagai gambar kecil dan bukan nama berkas

### Node laporan PIC atas nama karyawan
71. Tampilkan Dialog Damage Log dengan kondisi K10
72. Verifikasi node `Reported damaged by Sinta M on behalf of Tono R` tampil

### Node laporan Registration tanpa Damaged Photo
73. Tampilkan Dialog Damage Log dengan kondisi K11
74. Verifikasi node `Reported damaged by Agus P` tampil dengan baris `What happened`
75. Verifikasi node `Reported damaged by Agus P` tidak memuat baris `Damaged Photo`

### Node Confirm dan Reject
76. Tampilkan Dialog Damage Log dengan kondisi K12
77. Verifikasi node `Report confirmed by Yoga T` tampil pada timeline
78. Verifikasi node `Report confirmed by Yoga T` tidak memuat baris `Reason`
79. Verifikasi node `Report rejected by Rina W` tampil dengan baris `Reason` berisi `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`

### Node Cancel Report
80. Tampilkan Dialog Damage Log dengan kondisi K13
81. Verifikasi node `Report canceled by Budi S` tampil tanpa baris detail

### Node peristiwa Missing oleh System
82. Tampilkan Dialog Damage Log dengan kondisi K14
83. Verifikasi node `Asset reported missing` tampil dengan pelaku `System` tanpa ikon pengguna dan tanpa tautan
84. Verifikasi node `Asset found` tampil dengan pelaku `System`
85. Verifikasi node `Missing report closed` tampil dengan pelaku `System`

### Node Marked as repaired
86. Tampilkan Dialog Damage Log dengan kondisi K15
87. Verifikasi node `Marked as repaired by Rina W` tampil
88. Verifikasi node `Marked as repaired by Rina W` memuat baris `Repair note`, `After photo`, dan `Manual identification`

### Node peristiwa Disposal
89. Tampilkan Dialog Damage Log dengan kondisi K16
90. Verifikasi node `Disposal reported by Agus P` memuat baris `Report ID` dan `Reason`
91. Verifikasi node `Disposal report declined by Dedi K` memuat baris `Report ID`, `Reason`, dan `Back to Damaged`
92. Verifikasi node `Disposal report canceled by Agus P` memuat baris `Report ID`, `Reason`, dan `Back to Damaged`

### Node Disposal report canceled oleh System
93. Tampilkan Dialog Damage Log dengan kondisi K17
94. Verifikasi node `Disposal report canceled by System` tampil dengan pelaku `System` tanpa tautan

### Node Disposed oleh System
95. Tampilkan Dialog Damage Log dengan kondisi K18
96. Verifikasi node `Disposed` tampil dengan pelaku `System` dan baris `Disposal No.`

### Footer review tidak dirender bagi pengguna Read Only
97. Tampilkan Dialog Damage Log dengan kondisi K19
98. Verifikasi badge status record `Waiting for Confirmation` tampil
99. Verifikasi footer `[Reject]` dan `[Confirm]` tidak dirender bagi pengguna tanpa hak Aktor Damaged

### Footer review tidak dirender bagi pemegang Manage asset & TAG (Read)
100. Tampilkan Dialog Damage Log dengan kondisi K20
101. Verifikasi badge status record `Waiting for Confirmation` tampil
102. Verifikasi footer `[Reject]` dan `[Confirm]` tidak dirender bagi pengguna tanpa hak Aktor Damaged

### Record yang sudah Rejected tetap dapat dikunjungi lewat Prev dan Next
103. Tampilkan Dialog Damage Log dengan kondisi K21
104. Klik `[Reject]`
105. Verifikasi dialog `Reject Report` terbuka
106. Isi `Reason*` dengan `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan`
107. Klik `[Reject]` pada dialog `Reject Report`
108. Verifikasi badge status record berubah menjadi `Rejected`
109. Klik `Next`
110. Verifikasi dialog Damage Log menampilkan record `Tablet Samsung Tab A8 - 3` dari daftar saat dialog dibuka
111. Klik `Prev`
112. Verifikasi dialog Damage Log menampilkan record `Laptop Dell Latitude 5420 - 4` dengan badge status record `Rejected`
