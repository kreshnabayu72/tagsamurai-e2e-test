---
id: TC-FA-BORROW-UI-064-dialog-katalog-blok-dan-konfirmasi
title: "Katalog dialog blok dan konfirmasi Borrow: judul, copy, tombol, dan blok Approval di D-BRW-03"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-BRW-03", "D-BRW-06", "D-BRW-09", "D-BRW-13", "D-BRW-14", "D-BRW-16", "D-BRW-17", "D-BRW-18", "D-BRW-22", "D-BRW-23", "D-BRW-24", "DM-BRW-04", "DM-BRW-05", "DM-BRW-06", "DM-BRW-07", "DM-BRW-08", "DM-BRW-09", "DM-BRW-10", "DM-BRW-12", "DM-BRW-17", "DO-BRW-11", "DO-BRW-12", "DO-BRW-13", "DO-BRW-14", "DO-BRW-15", "DO-BRW-16", "FLD-BRW-18", "FLD-BRW-19", "§4.2.3#p2", "§4.2.3#b1", "§4.2.3#b2", "§7.2#p1", "§7.2#p2", "§9.5#r19"]
smoke: []
dependsOn: []
trace:
  "D-BRW-03": [2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 114, 115, 116, 152, 153, 154, 155, 156]
  "D-BRW-06": [25, 26, 27]
  "D-BRW-09": [35, 36, 37, 39, 119]
  "D-BRW-13": [41, 42, 43]
  "D-BRW-14": [47, 48, 49, 50]
  "D-BRW-16": [54, 55, 56, 58, 121, 123, 126]
  "D-BRW-17": [69, 70, 71, 72]
  "D-BRW-18": [88, 89]
  "D-BRW-22": [93, 94, 95, 96, 98, 129]
  "D-BRW-23": [102, 103, 104, 131, 132, 134, 135, 137, 138, 140, 141, 143, 144, 146, 147, 150]
  "D-BRW-24": [106, 107, 108]
  "DM-BRW-04": [47, 52]
  "DM-BRW-05": [2, 17, 20, 23]
  "DM-BRW-06": [88, 91]
  "DM-BRW-07": [25, 29, 31, 33]
  "DM-BRW-08": 60
  "DM-BRW-09": 35
  "DM-BRW-10": [93, 98, 100]
  "DM-BRW-12": [69, 86]
  "DM-BRW-17": [41, 45]
  "DO-BRW-11": 60
  "DO-BRW-12": 61
  "DO-BRW-13": 63
  "DO-BRW-14": 64
  "DO-BRW-15": 67
  "DO-BRW-16": 39
  "FLD-BRW-18": [75, 77, 79]
  "FLD-BRW-19": [74, 83]
  "§4.2.3#p2": [7, 8]
  "§4.2.3#b1": [7, 152, 153]
  "§4.2.3#b2": [8, 154, 155, 156]
  "§7.2#p1": [39, 60, 63, 110]
  "§7.2#p2": 112
  "§9.5#r19": 9
anchor: [66, 131, 134, 137, 140, 143, 146]
coverage:
  web: automated
---

# Katalog dialog blok dan konfirmasi Borrow: judul, copy, tombol, dan blok Approval di D-BRW-03

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Halaman yang memuat pemicu dialog
- Komponen: Dialog konfirmasi dan blok Borrow
- Data:
  - DU-064-1: BRW untuk Group `Finance` dengan dua aset: `Printer Epson L3110 - 1` (Duration `2 days`, Purpose `Presentasi klien`, tanpa approval) dan `Laptop Dell Latitude 5420 - 8` (Duration `3 days`, Purpose `Demo aplikasi ke klien`, perlu approval).
  - DU-064-2: BRW untuk Group `Gudang Pusat` dengan satu aset: `Forklift Toyota 8FD - 1` (Duration `1 day`, Purpose `Bongkar muat gudang`, perlu approval).
  - DU-064-3: pengguna `Rina W` (approver dan Aktor Borrow), `Budi Santoso` (Borrower), dan `Agus P` (PIC Borrower tanpa akun).
  - DU-064-4: perubahan Draft oleh `Budi Santoso` pukul `14:30`.
  - DU-064-5: aset pengajuan Extend `Laptop Dell Latitude 5420 - 8` dengan Current Due Date `10/12/2026`.
  - DU-064-6: alasan pembatalan otomatis `Timed out (Waiting for Approval)`.
  - DU-064-7: aset di daftar Return `Tablet Samsung Galaxy Tab A8`, tanpa laporan Damaged.
  - DU-064-8: BRW `BRW-2026-0153`, Group `Finance`.
  - DU-064-9: Draft `Draft Peminjaman Gudang 03` di luar cakupan Aktor.
  - DU-064-14: isian Borrow Request tersimpan: Borrower `Budi Santoso`, aset `Printer Epson L3110 - 1`, Duration `2 days`, Purpose `Presentasi klien`, Note `Dipakai untuk presentasi di kantor klien`.
  - DU-064-15: BRW untuk Group `Finance` dengan satu aset `Printer Epson L3110 - 1` (Duration `2 days`, Purpose `Presentasi klien`, tanpa approval).
  - DU-064-16: BRW untuk Group `Gudang Pusat` dengan satu aset `Hand Pallet Yale MP20 - 1` (Duration `1 day`, Purpose `Bongkar muat gudang`, tanpa approval).
  - DU-064-17: BRW untuk Group `Finance` dengan lima aset menurut aturan approval: `Printer Epson L3110 - 1` (Auto-approve terpenuhi), `Proyektor BenQ MW550 - 2` (Self service aktif), `Laptop Dell Latitude 5420 - 8` (perlu approval, satu approver), `Laptop HP ProBook 440 - 3` (perlu approval, beberapa approver), dan `Meja Rapat Kayu Jati - 4` (perlu approval, tanpa approver di Group sehingga dirutekan ke Group Manager atau Total Control).
- Kondisi:
  - K1: Date Format bernilai `DD/MM/YYYY`; dialog Submit Borrow dibuka dari `[Submit]` form Borrow Request dengan DU-064-1 dan DU-064-2.
  - K2: dialog Submit Borrow dibuka dari `[Submit]` form Borrow Request dengan DU-064-1 saja.
  - K3: dialog Submit Borrow dengan DU-064-15 dan DU-064-16 dikonfirmasi, semua BRW langsung Waiting for Handover.
  - K4: dialog Submit Borrow dengan DU-064-2 dikonfirmasi, satu BRW yang seluruh asetnya menunggu approval.
  - K5: dialog Submit Borrow dengan DU-064-1 dan DU-064-2 dikonfirmasi, dua BRW dengan total 3 aset, sebagian aset langsung disetujui dan sebagian menunggu approval (1 dari 3 aset disetujui, 2 menunggu approval).
  - K6: dialog Submit Approval dibuka dari `[Submit]` halaman Review Approval, lalu dikonfirmasi dan berhasil.
  - K7: dialog Submit Approval dibuka dari `[Submit]` halaman Review Extension Request, lalu dikonfirmasi dan berhasil.
  - K8: dialog Borrow Canceled dibuka saat halaman Review Approval terbuka karena pengajuan dibatalkan oleh `Budi Santoso`.
  - K9: dialog Borrow Canceled dibuka saat halaman Review Approval terbuka karena pengajuan dibatalkan otomatis dengan alasan DU-064-6.
  - K10: Time Format bernilai `24h`, dialog Draft Changed dibuka dari `[Save Draft]` pada Draft yang diubah oleh DU-064-4.
  - K11: Time Format bernilai `24h`, dialog Draft Changed dibuka dari `[Submit]` pada Draft yang diubah oleh DU-064-4.
  - K12: dialog Cancel Extension dibuka dari row action `Cancel Extension` untuk DU-064-5, Date Format bernilai `DD/MM/YYYY`, lalu dikonfirmasi dan berhasil.
  - K13: dialog Approval cannot be made dibuka karena approver lain sudah memutuskan pengajuan Borrow.
  - K14: dialog Approval cannot be made dibuka karena Aktor Borrow lain sudah mengirim review Extension Request.
  - K15: halaman Review Approval terbuka dan approver lain lebih dulu memutuskan aset mode Any one approver yang sama.
  - K16: halaman Review Approval terbuka dan salah satu approver me-Reject aset mode All approvers.
  - K17: halaman Review Approval terbuka dan satu approver meng-Approve aset mode All approvers yang masih menunggu approver lain.
  - K18: dialog Report Damaged dibuka dari row action `Report Damaged` pada halaman Return untuk DU-064-7.
  - K19: dialog Report Damaged dibuka untuk DU-064-7, dan Report dikonfirmasi dengan isian lengkap lalu berhasil.
  - K20: dialog Bulk Transaction Row Limit dibuka dari `[Submit]` form Borrow Request yang jumlah barisnya melebihi Bulk Transaction Row Limit.
  - K21: dialog Bulk Transaction Row Limit dibuka dari `[Borrow Now]` yang jumlah asetnya melebihi Bulk Transaction Row Limit.
  - K22: dialog Borrow Already Canceled dibuka saat Aktor Borrow menjalankan Cancel Borrow pada baris yang sudah dibatalkan DU-064-3 `Budi Santoso`.
  - K23: dialog Borrow Already Canceled dibuka saat Aktor Borrow menjalankan Hand Over pada baris yang sudah dibatalkan PIC DU-064-3 `Agus P` atas nama `Budi Santoso`.
  - K24: dialog Borrow Already Canceled dibuka saat Aktor Borrow menjalankan Remind Borrower pada baris yang sudah dibatalkan DU-064-3 `Budi Santoso`.
  - K25: dialog Restore Unsent Borrow dibuka saat Borrow Request dibuka di perangkat yang sama oleh pengguna yang sama dan ada isian tersimpan.
  - K26: dialog Cannot Delete Drafts dibuka dari Bulk Delete Draft untuk DU-064-9 saja.
  - K27: dialog Approval cannot be made dibuka karena approver lain sudah memutuskan pengajuan Extension approval.
  - K28: dialog Approval cannot be made dibuka karena keputusan override Group Manager atau Total Control sudah masuk lebih dulu.
  - K29: dialog Borrow Already Canceled dibuka saat Aktor Borrow menjalankan Cancel Borrow pada DU-064-8 yang sudah dibatalkan `Budi Santoso`.
  - K30: Borrow Request dibuka di perangkat yang sama oleh pengguna yang sama, tanpa isian tersimpan.
  - K31: Borrow Request dibuka di perangkat yang sama oleh pengguna lain, sedangkan isian tersimpan milik pengguna sebelumnya.
  - K32: Borrow Request dibuka di perangkat lain oleh pengguna yang sama, sedangkan isian tersimpan hanya ada di perangkat sebelumnya.
  - K33: Borrow Request dibuka lagi sesudah `[Submit]` berhasil pada isian yang sebelumnya tersimpan.
  - K34: Borrow Request dibuka lagi sesudah `[Discard]` diklik pada dialog Restore Unsent Borrow.
  - K35: Borrow Request dibuka lagi sesudah pengguna yang sama logout, padahal isian sebelumnya tersimpan.
  - K36: dialog Restore Unsent Borrow dibuka, isian tersimpan diperbarui tiap perubahan: pertama dengan Duration `1 day`, lalu dengan seluruh isian DU-064-14.
  - K37: dialog Submit Borrow dibuka dari `[Submit]` form Borrow Request dengan DU-064-17.

## Test Steps

### Dialog Submit Borrow untuk lebih dari satu BRW
1. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K1
2. Verifikasi judul dialog `Submit Borrow` tampil
3. Verifikasi teks `This will create 2 borrows (Finance, Gudang Pusat).` tampil
4. Verifikasi kartu BRW `Finance` menampilkan daftar aset `Printer Epson L3110 - 1` dengan `2 days · Presentasi klien`
5. Verifikasi kartu BRW `Finance` menampilkan daftar aset `Laptop Dell Latitude 5420 - 8` dengan `3 days · Demo aplikasi ke klien`
6. Verifikasi kartu BRW `Gudang Pusat` menampilkan daftar aset `Forklift Toyota 8FD - 1` dengan `1 day · Bongkar muat gudang`
7. Verifikasi kartu BRW `Finance` menampilkan baris approval `No approval needed: Printer Epson L3110 - 1.`
8. Verifikasi kartu BRW `Finance` menampilkan baris approval `Needs approval: Laptop Dell Latitude 5420 - 8.`
9. Verifikasi baris `No approval needed: Printer Epson L3110 - 1.` berada sebelum baris `Needs approval: Laptop Dell Latitude 5420 - 8.` pada kartu BRW `Finance`
10. Verifikasi teks `Are you sure you want to submit it?` tampil
11. Verifikasi tombol `[Cancel]` dan `[Submit]` tampil pada dialog Submit Borrow

### Dialog Submit Borrow untuk satu BRW
12. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K2
13. Verifikasi kartu BRW `Finance` tampil pada dialog Submit Borrow
14. Verifikasi dialog Submit Borrow tidak menampilkan teks `This will create 2 borrows (Finance, Gudang Pusat).`

### Hasil konfirmasi Submit Borrow, semua langsung Waiting for Handover
15. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K3
16. Klik `[Submit]` pada dialog Submit Borrow
17. Verifikasi toast `Success, 2 borrows are ready for handover.` tampil

### Hasil konfirmasi Submit Borrow, semua menunggu approval
18. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K4
19. Klik `[Submit]` pada dialog Submit Borrow
20. Verifikasi toast `Success, borrow has been submitted for approval.` tampil

### Hasil konfirmasi Submit Borrow, hasil campuran
21. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K5
22. Klik `[Submit]` pada dialog Submit Borrow
23. Verifikasi toast `Success, 1 of 3 assets have been approved. 2 submitted for approval.` tampil

### Dialog Submit Approval dari halaman Review Approval
24. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K6
25. Verifikasi judul dialog `Submit Approval` tampil
26. Verifikasi teks `You will submit this transaction approval. Asset with 0 approved duration will be rejected and will not appear in the next step of transaction. Are you sure you want to submit it?` tampil
27. Verifikasi tombol `[Cancel]` dan `[Submit]` tampil pada dialog Submit Approval
28. Klik `[Submit]` pada dialog Submit Approval
29. Verifikasi toast `Success, borrow has been approved.` tampil

### Dialog Submit Approval dari halaman Review Extension Request
30. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K7
31. Verifikasi dialog `Submit Approval` tampil dari halaman Review Extension Request
32. Klik `[Submit]` pada dialog Submit Approval
33. Verifikasi toast `Success, extension request has been reviewed.` tampil

### Dialog Borrow Canceled dibatalkan oleh pengguna
34. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K8
35. Verifikasi judul dialog `Borrow Canceled` tampil
36. Verifikasi teks `This borrow was canceled by Budi Santoso.` tampil
37. Verifikasi tombol `[OK]` tampil pada dialog Borrow Canceled

### Dialog Borrow Canceled dibatalkan otomatis
38. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K9
39. Verifikasi teks `This borrow was canceled automatically (Timed out (Waiting for Approval)).` tampil

### Dialog Draft Changed dari Save Draft
40. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K10
41. Verifikasi judul dialog `Draft Changed` tampil dari `[Save Draft]`
42. Verifikasi teks `This draft was changed by Budi Santoso at 14:30. Reload to see the latest version; your unsaved changes will be lost.` tampil
43. Verifikasi tombol `[Cancel]` dan `[Reload]` tampil

### Dialog Draft Changed dari Submit
44. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K11
45. Verifikasi dialog `Draft Changed` tampil dari `[Submit]` pada Draft yang diubah orang lain

### Dialog Cancel Extension
46. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K12
47. Verifikasi judul dialog `Cancel Extension` tampil
48. Verifikasi bullet `Laptop Dell Latitude 5420 - 8` tampil di body dialog
49. Verifikasi teks `The approval request will be withdrawn and the current due date stays 10/12/2026. Are you sure you want to cancel it?` tampil
50. Verifikasi tombol `[Go Back]` dan `[Cancel Extension]` tampil
51. Klik `[Cancel Extension]`
52. Verifikasi toast `Success, extension request has been canceled.` tampil

### Dialog Approval cannot be made
53. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K13
54. Verifikasi judul dialog `Approval cannot be made` tampil
55. Verifikasi teks `You can no longer approve this request because it has already been done by another approver.` tampil
56. Verifikasi tombol `[OK]` tampil pada dialog Approval cannot be made
57. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K14
58. Verifikasi teks `You can no longer approve this request because it has already been done by another Asset Admin.` tampil

### Dialog terbuka real-time saat approver lain memutuskan lebih dulu
59. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K15
60. Verifikasi dialog `Approval cannot be made` terbuka tanpa menunggu `[Submit]` diklik
61. Verifikasi keputusan yang belum dikirim tidak disimpan, tidak ada toast `Success, borrow has been approved.` sesudah dialog terbuka

### Dialog terbuka real-time saat approver lain me-Reject aset mode All
62. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K16
63. Verifikasi dialog `Approval cannot be made` terbuka tanpa menunggu `[Submit]` diklik bagi approver lain yang membuka Review aset itu
64. Verifikasi Approve atau Reject yang belum dikirim tidak disimpan, tidak ada toast `Success, borrow has been rejected.` sesudah dialog terbuka

### Approve dari satu approver tidak memicu dialog bagi approver lain
65. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K17
66. Verifikasi toggle Approval aset mode All approvers tetap tampil pada halaman Review Approval
67. Verifikasi dialog `Approval cannot be made` tidak terbuka bagi approver lain

### Dialog Report Damaged dari halaman Return
68. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K18
69. Verifikasi judul dialog `Report Damaged` tampil dari row action pada halaman Return
70. Verifikasi field `Photo` tampil sebagai ImagePicker tunggal
71. Verifikasi placeholder `Enter what happened` tampil pada field `What happened`
72. Verifikasi tombol `[Cancel]` dan `[Report]` tampil
73. Klik `[Report]`
74. Verifikasi pesan `Photo must not be empty` tampil
75. Verifikasi pesan `What happened must not be empty` tampil
76. Isi field `What happened` dengan `Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk.` (360 karakter)
77. Verifikasi pesan `Max. 360 characters` tidak tampil di bawah field `What happened`
78. Ganti isi field `What happened` dengan `Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk..` (361 karakter)
79. Verifikasi pesan `Max. 360 characters` tampil di bawah field `What happened`

### Report Damaged berhasil dengan isian lengkap
80. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K19
81. Pilih berkas `kerusakan-layar.jpg` pada field `Photo`
82. Klik `[Apply]` pada dialog `Adjust photo`
83. Verifikasi thumbnail foto tampil pada field `Photo`
84. Isi field `What happened` dengan `Layar retak setelah terjatuh saat dipindahkan`
85. Klik `[Report]`
86. Verifikasi dialog `Report Damaged` tertutup dan baris `Tablet Samsung Galaxy Tab A8` menampilkan badge `Reported Damaged`

### Dialog Bulk Transaction Row Limit dari Submit
87. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K20
88. Verifikasi judul dialog `Bulk Transaction Row Limit` tampil dari `[Submit]`
89. Verifikasi tombol `[OK]` tampil pada dialog Bulk Transaction Row Limit

### Dialog Bulk Transaction Row Limit dari Borrow Now
90. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K21
91. Verifikasi dialog `Bulk Transaction Row Limit` tampil dari `[Borrow Now]`

### Dialog Borrow Already Canceled dari Cancel Borrow
92. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K22
93. Verifikasi judul dialog `Borrow Already Canceled` tampil
94. Verifikasi teks `Budi Santoso already canceled this borrow.` tampil
95. Verifikasi teks `Your action was not saved.` tampil
96. Verifikasi tombol `[OK]` tampil pada dialog Borrow Already Canceled

### Dialog Borrow Already Canceled atas nama PIC dari Hand Over
97. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K23
98. Verifikasi teks `Agus P already canceled this borrow on behalf of Budi Santoso.` tampil dari aksi Hand Over

### Dialog Borrow Already Canceled dari Remind Borrower
99. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K24
100. Verifikasi dialog `Borrow Already Canceled` tampil dari aksi Remind Borrower

### Dialog Restore Unsent Borrow
101. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K25
102. Verifikasi judul dialog `Restore Unsent Borrow` tampil
103. Verifikasi teks `Restore your unsent borrow?` tampil
104. Verifikasi tombol `[Discard]` dan `[Restore]` tampil

### Dialog blok Cannot Delete Drafts
105. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K26
106. Verifikasi judul dialog `Cannot Delete Drafts` tampil pada Bulk Delete Draft
107. Verifikasi teks `None of the selected drafts can be deleted because they have groups outside your access.` tampil
108. Verifikasi tombol `[OK]` tampil pada dialog Cannot Delete Drafts

### Aturan dialog dan matriks skenario
109. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K15
110. Verifikasi urutan dialog real-time mengikuti Aturan Urutan Dialog: `Approval cannot be made` terbuka tanpa menunggu `[Submit]`
111. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K26
112. Verifikasi dialog `Cannot Delete Drafts` tampil sebagai hasil skenario Bulk Delete Draft menurut Matriks Skenario, Dialog, dan Hasil

### Jumlah aset dan baris approval kartu BRW Gudang Pusat
113. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K1
114. Verifikasi kartu BRW `Finance` menampilkan jumlah aset `2`
115. Verifikasi kartu BRW `Gudang Pusat` menampilkan jumlah aset `1`
116. Verifikasi kartu BRW `Gudang Pusat` menampilkan baris approval `Needs approval: Forklift Toyota 8FD - 1.`

### Dialog Borrow Canceled ditutup lewat OK
117. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K8
118. Klik `[OK]` pada dialog Borrow Canceled
119. Verifikasi dialog `Borrow Canceled` tertutup

### Dialog Approval cannot be made untuk Extension approval dan keputusan override
120. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K27
121. Verifikasi teks `You can no longer approve this request because it has already been done by another approver.` tampil untuk pengajuan Extension approval
122. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K28
123. Verifikasi teks `You can no longer approve this request because it has already been done by another approver.` tampil untuk keputusan override Group Manager atau Total Control

### Dialog Approval cannot be made ditutup lewat OK
124. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K13
125. Klik `[OK]` pada dialog Approval cannot be made
126. Verifikasi dialog `Approval cannot be made` tertutup

### Dialog Borrow Already Canceled ditutup lewat OK
127. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K29
128. Klik `[OK]` pada dialog Borrow Already Canceled
129. Verifikasi dialog `Borrow Already Canceled` tertutup

### Dialog Restore Unsent Borrow tidak muncul tanpa isian tersimpan
130. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K30
131. Verifikasi form Borrow Request tampil
132. Verifikasi dialog `Restore Unsent Borrow` tidak tampil karena tidak ada isian tersimpan

### Dialog Restore Unsent Borrow tidak muncul bagi pengguna lain di perangkat yang sama
133. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K31
134. Verifikasi form Borrow Request tampil
135. Verifikasi dialog `Restore Unsent Borrow` tidak tampil karena isian tersimpan bukan milik pengguna ini

### Dialog Restore Unsent Borrow tidak muncul di perangkat lain
136. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K32
137. Verifikasi form Borrow Request tampil
138. Verifikasi dialog `Restore Unsent Borrow` tidak tampil karena isian tersimpan hanya ada di perangkat lain

### Dialog Restore Unsent Borrow tidak muncul sesudah Submit berhasil
139. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K33
140. Verifikasi form Borrow Request tampil
141. Verifikasi dialog `Restore Unsent Borrow` tidak tampil karena isian sudah dihapus sesudah Submit berhasil

### Dialog Restore Unsent Borrow tidak muncul sesudah Discard
142. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K34
143. Verifikasi form Borrow Request tampil
144. Verifikasi dialog `Restore Unsent Borrow` tidak tampil karena isian sudah dihapus sesudah Discard

### Dialog Restore Unsent Borrow tidak muncul sesudah logout
145. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K35
146. Verifikasi form Borrow Request tampil
147. Verifikasi dialog `Restore Unsent Borrow` tidak tampil karena isian tersimpan sudah dihapus

### Restore memuat isian tersimpan terakhir
148. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K36
149. Klik `[Restore]`
150. Verifikasi form Borrow Request memuat Borrower `Budi Santoso`, aset `Printer Epson L3110 - 1`, Duration `2 days`, Purpose `Presentasi klien`, dan Note `Dipakai untuk presentasi di kantor klien`

### Baris approval kartu BRW menurut aturan approval aset
151. Tampilkan Dialog konfirmasi dan blok Borrow dengan kondisi K37
152. Verifikasi kartu BRW `Finance` menampilkan baris approval `No approval needed: Printer Epson L3110 - 1.` untuk aset Auto-approve
153. Verifikasi kartu BRW `Finance` menampilkan baris approval `No approval needed: Proyektor BenQ MW550 - 2.` untuk aset Self service
154. Verifikasi kartu BRW `Finance` menampilkan baris approval `Needs approval: Laptop Dell Latitude 5420 - 8.` untuk aset dengan satu approver
155. Verifikasi kartu BRW `Finance` menampilkan baris approval `Needs approval: Laptop HP ProBook 440 - 3.` untuk aset dengan beberapa approver
156. Verifikasi kartu BRW `Finance` menampilkan baris approval `Needs approval: Meja Rapat Kayu Jati - 4.` untuk aset tanpa approver di Group
