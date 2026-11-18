---
id: TC-FA-ASSIGN-UI-114-halaman-review-approval-keputusan-dan-note
title: "Halaman Review Approval: keputusan per aset, Approval Note, dan notice"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.9#b1", "§4.2.9#b2", "§4.2.9#b3", "§4.2.9#b4", "§4.2.9#b5", "§4.2.9#b6", "§4.2.9#b7", "§4.2.9#b8", "§4.2.9#b9", "§4.2.9#b10", "§4.2.9#b11", "§4.2.9#p1", "§4.2.9#p2", "§4.2.9#p4", "§4.2.9#r23", "§4.2.9#r24", "§4.2.9#r25", "§4.2.9#r26", "§4.2.9#r27", "§4.2.9#r28", FLD-ASG-06, FLD-ASG-07, FLD-ASG-08, V-ASG-16, EC-ASG-82, "EB-FRM-1@review-approval", "EB-FRM-4@approval-note"]
smoke: []
dependsOn: []
trace:
  "§4.2.9#b1": [11, 13, 140, 142]
  "§4.2.9#b2": [19, 23, 24, 26, 28, 29, 31, 32, 34]
  "§4.2.9#b3": [21, 37]
  "§4.2.9#b4": 37
  "§4.2.9#b5": 95
  "§4.2.9#b6": 128
  "§4.2.9#b7": [95, 96, 97, 98]
  "§4.2.9#b8": [100, 101, 104]
  "§4.2.9#b9": [107, 108, 110, 111]
  "§4.2.9#b10": [113, 114, 115, 117]
  "§4.2.9#b11": [119, 120, 121, 122, 123, 125]
  "§4.2.9#p1": [2, 3, 4, 5, 6, 7, 8, 9, 15, 17, 21, 22, 145, 148, 150, 151, 152, 155]
  "§4.2.9#p2": 37
  "§4.2.9#p4": [113, 117]
  "§4.2.9#r23": 37
  "§4.2.9#r24": [95, 96]
  "§4.2.9#r25": [100, 104]
  "§4.2.9#r26": [107, 110]
  "§4.2.9#r27": [113, 114, 117]
  "§4.2.9#r28": 37
  FLD-ASG-06: [19, 20, 34]
  FLD-ASG-07: [42, 48, 53, 65]
  FLD-ASG-08: [23, 87, 132, 133, 136, 138]
  V-ASG-16: [42, 43, 48, 53, 54, 59, 60, 65]
  EC-ASG-82: [42, 43, 48, 65, 66]
  "EB-FRM-1@review-approval": [90, 91, 93]
  "EB-FRM-4@approval-note": [59, 60, 65, 66, 71, 72, 77, 78, 83, 84]
anchor: [103]
coverage:
  web: automated
---
# Halaman Review Approval: keputusan per aset, Approval Note, dan notice

## Prerequisites
- Aktor: Approver `Agus Pratama` pada Group `Head Office` (DU-114-7); approver lain `Rina Wulandari` (DU-114-8).
- Layar awal: halaman Review Approval, dibuka dari `Approvals > Assignment` tab Active.
- Komponen: Halaman Review Approval
- Data:
  - DU-114-1: ASG Transaction ID `ASG-2026-0070`, Status header `Waiting for Approval`, Requested By `Dewi Lestari`, Assignee `Budi Santoso`, Active assets `3 / 5 active assets`, Group `Head Office`, Note `Penugasan alat berat proyek`.
  - DU-114-2: ASG Transaction ID `ASG-2026-0072`, Status header `Waiting for Approval`, Requested By `Dewi Lestari`, Assignee `Finance`, PIC `Sari Dewi`, Group `Head Office`.
  - DU-114-3: ASG Transaction ID `ASG-2026-0074`, Assignee `Budi Santoso`, Active assets `6 / 5 active assets`, Group `Head Office`.
  - DU-114-4: Baris aset Review Name `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Approval Rule `Any one approver · Waiting for Approval`, Purpose `Proyek tambang`, Approval `Approve`.
  - DU-114-5: Baris aset Review Name `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Approval Rule `Any one approver · Waiting for Approval`, Purpose `Kunjungan klien`, Approval `Approve`.
  - DU-114-6: Baris aset Review Name `Camera Sony A7 - 9`, Asset ID `CAM-2026-0009`, Approval Rule `Any one approver · Waiting for Approval`, Purpose `Dokumentasi proyek`, Keterangan `Not your approval`.
  - DU-114-7: User Name `Agus Pratama`, Role `Approver`, Cakupan `Group Head Office`.
  - DU-114-8: User Name `Rina Wulandari`, Role `Approver`, Cakupan `Group Head Office`.
  - DU-114-9: Approval Note Approval Note kosong.
  - DU-114-10: Approval Note Approval Note `   `.
  - DU-114-11: Approval Note Approval Note `Y`.
  - DU-114-12: Approval Note Approval Note `MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujui`.
  - DU-114-13: Approval Note Approval Note `MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuix`.
  - DU-114-14: Approval Note Approval Note ` MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujui `.
  - DU-114-15: Approval Note Approval Note `Aset layak untuk ditugaskan. Aset layak untuk ditugaskan. Aset layak untuk ditugaskan. Aset layak untuk ditugaskan. Aset`.
  - DU-114-16: Approval Note Approval Note `MenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiSetuju𝒜ya!`.
  - DU-114-17: Pengaju `Maria Magdalena Christina Kusumawardhani Wijayakusuma` dengan nama panjang, sebagai Requested By pengajuan DU-114-1.
- Kondisi:
  - K1: Review untuk DU-114-1 (Assignee yang diharapkan `Budi S (3 / 5 active assets)`, dari nama depan dan huruf pertama nama belakang Assignee serta Active assets) dengan baris DU-114-4 dan DU-114-5 milik Aktor, dan baris DU-114-6 milik approver lain; semua keputusan masih default.
  - K2: Review untuk DU-114-2 (Assignee Division) dengan baris DU-114-4.
  - K3: Review untuk DU-114-3 dengan baris DU-114-4; Assignee melewati Max efektif; Assignee yang diharapkan `Budi S (6 / 5 active assets)`, dari nama depan dan huruf pertama nama belakang Assignee serta Active assets.
  - K4: seperti K1; baris DU-114-4 diubah ke Reject.
  - K5: seperti K1; keputusan Approve atas DU-114-4 dan DU-114-5 dikirim lewat dialog Submit Approval; respons simpan lambat.
  - K6: seperti K1 dengan Approval type Any one approver; Rina Wulandari memutuskan DU-114-4 lebih dulu saat halaman terbuka; teks yang diharapkan `You can no longer approve this request because it has already been done by another approver.`, dari approver lain.
  - K7: seperti K1 dengan Approval type All approvers (AND); Rina Wulandari me-Reject DU-114-4 saat halaman terbuka.
  - K8: seperti K7; Rina Wulandari hanya meng-Approve DU-114-4.
  - K9: seperti K1; saat Submit konflik pada DU-114-4 menolak seluruh Submit.
  - K10: seperti K9; sesudah `[Close]` halaman Review dimuat ulang; DU-114-4 sudah diputuskan pihak lain; DU-114-5 sudah diisi Reject dengan Approval Note DU-114-12.
  - K11: seperti K1; pengajuan dibatalkan oleh `Dewi Lestari` saat halaman terbuka; teks yang diharapkan `This assignment was canceled by Dewi Lestari.`, dari Name.
  - K12: seperti K1; pengajuan dibatalkan otomatis oleh sistem karena `Assignee deactivated` saat halaman terbuka; teks yang diharapkan `This assignment was canceled automatically (Assignee deactivated).`, dari Reason.
  - K13: halaman dibuka dari `Detail` di tab History untuk DU-114-1; breadcrumb yang diharapkan `Approvals > Assignment > History > Detail`; DU-114-4 `Approved`, DU-114-5 `Rejected`, DU-114-6 `Waiting for Approval`.
  - K14: seperti K1 dengan dua baris milik Aktor, DU-114-4 Approve dan DU-114-5 Reject dengan Approval Note DU-114-12; Submit berhasil sebagian; toast yang diharapkan `Success, assignment has been partially approved.`.
  - K15: seperti K1; baris DU-114-5 Reject; Approval Note diisi sesuai langkah; Submit ditekan.
  - K17: halaman Review untuk DU-114-1 diakses oleh pengaju `Dewi Lestari`, yang bukan approver pada pengajuan itu; akses ditolak server.
  - K18: seperti K1; semua keputusan baris milik Aktor tetap `Approve`; Approval Note diisi sesuai langkah; Submit ditekan sesuai langkah.
  - K19: halaman Review untuk DU-114-1 diakses oleh Assignee `Budi Santoso`, yang bukan approver pada pengajuan itu; akses ditolak server.
  - K20: halaman Review untuk DU-114-2 diakses oleh PIC `Sari Dewi`, yang bukan approver pada pengajuan itu; akses ditolak server.
  - K21: seperti K1; Requested By adalah DU-114-17.

## Test Steps

### Header halaman Review dan info transaksi
1. Tampilkan Halaman Review Approval dengan kondisi K1
2. Verifikasi breadcrumb `Approvals > Assignment > Active > Review`
3. Verifikasi judul memuat Transaction ID `ASG-2026-0070` dengan ikon copy dan badge status header `Waiting for Approval`
4. Verifikasi ujung kanan memuat Requested By `Dewi Lestari` dan Request Date
5. Verifikasi info memuat Assignee `Budi S (3 / 5 active assets)` dan Group `Head Office`
6. Verifikasi info memuat Note `Penugasan alat berat proyek`
7. Verifikasi info tidak memuat PIC karena Assignee adalah karyawan
8. Verifikasi tabel memuat kolom `Approval Rule`, `Approval`, dan `Approval Note`
9. Verifikasi footer halaman Review memuat `[Cancel]` dan `[Submit]`

### Halaman Review dibuka dari Approvals Assignment oleh approver
10. Tampilkan Halaman Review Approval dengan kondisi K1
11. Verifikasi halaman Review untuk `ASG-2026-0070` tampil bagi approver `Agus Pratama` yang membukanya dari `Approvals > Assignment`

### Akses halaman Review ditolak untuk pengaju
12. Tampilkan Halaman Review Approval dengan kondisi K17
13. Verifikasi isi pengajuan `ASG-2026-0070` tidak ditampilkan kepada `Dewi Lestari` karena akses ditolak

### Info Assignee Division memuat PIC
14. Tampilkan Halaman Review Approval dengan kondisi K2
15. Verifikasi info memuat Assignee `Finance` dan PIC `Sari Dewi`

### Assignee yang melewati Max efektif ditandai danger
16. Tampilkan Halaman Review Approval dengan kondisi K3
17. Verifikasi info Assignee `Budi S (6 / 5 active assets)` memakai penanda `danger`

### Keputusan per aset: default Approve dan baris approver lain read-only
18. Tampilkan Halaman Review Approval dengan kondisi K1
19. Verifikasi toggle `Approval` baris `Excavator PC200 - 4` bernilai `Approve`
20. Verifikasi toggle `Approval` baris `Toyota Avanza - 6` bernilai `Approve`
21. Verifikasi baris `Camera Sony A7 - 9` read-only dengan keterangan `Not your approval`
22. Verifikasi kolom `Approval Rule` baris `Excavator PC200 - 4` menampilkan `Any one approver · Waiting for Approval`
23. Verifikasi placeholder `Approval Note` baris `Excavator PC200 - 4` adalah `Enter approval note`
24. Verifikasi halaman tidak memuat isian Approve Duration

### Bulk action hanya untuk baris milik approver
25. Tampilkan Halaman Review Approval dengan kondisi K1
26. Verifikasi toolbar bulk belum tampil karena belum ada baris tercentang
27. Centang baris `Excavator PC200 - 4`
28. Verifikasi toolbar bulk tampil
29. Verifikasi baris `Camera Sony A7 - 9` tidak dapat dicentang
30. Klik bulk action `Reject`
31. Verifikasi toggle `Approval` baris `Excavator PC200 - 4` bernilai `Reject`
32. Verifikasi toggle `Approval` baris `Toyota Avanza - 6` tetap `Approve`

### Reject mengubah toggle ke danger
33. Tampilkan Halaman Review Approval dengan kondisi K4
34. Verifikasi toggle `Approval` baris `Excavator PC200 - 4` bernilai `Reject` dengan penanda `danger`

### Submit mengirim seluruh keputusan aset milik approver sekaligus
35. Tampilkan Halaman Review Approval dengan kondisi K1
36. Klik `[Submit]`
37. Verifikasi dialog konfirmasi `Submit Approval` dibuka oleh `[Submit]` pada halaman Review dan memuat keputusan untuk 2 aset

### Approval Note wajib saat Reject: kosong
38. Tampilkan Halaman Review Approval dengan kondisi K15
39. Pilih `Reject` pada baris `Toyota Avanza - 6`
40. Kosongkan Approval Note baris `Toyota Avanza - 6`
41. Klik `[Submit]`
42. Verifikasi error `Approval note must not be empty` tampil di bawah field Approval Note baris `Toyota Avanza - 6`
43. Verifikasi Submit diblokir dan dialog Submit Approval tidak tampil

### Approval Note hanya spasi saat Reject ditolak
44. Tampilkan Halaman Review Approval dengan kondisi K15
45. Pilih `Reject` pada baris `Toyota Avanza - 6`
46. Isi Approval Note `   `
47. Klik `[Submit]`
48. Verifikasi error `Approval note must not be empty` tampil di bawah field Approval Note baris `Toyota Avanza - 6`

### Approval Note satu karakter diterima
49. Tampilkan Halaman Review Approval dengan kondisi K15
50. Pilih `Reject` pada baris `Toyota Avanza - 6`
51. Isi Approval Note `Y`
52. Klik `[Submit]`
53. Verifikasi dialog `Submit Approval` tampil karena Approval Note memenuhi batas minimum
54. Verifikasi error Approval Note tidak tampil

### Approval Note tepat di batas maksimum diterima
55. Tampilkan Halaman Review Approval dengan kondisi K15
56. Pilih `Reject` pada baris `Toyota Avanza - 6`
57. Isi Approval Note `MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujui` (120 karakter)
58. Klik `[Submit]`
59. Verifikasi dialog `Submit Approval` tampil karena Approval Note tepat 120 karakter
60. Verifikasi pesan `Max. 120 characters` tidak tampil

### Approval Note satu karakter melewati batas ditolak
61. Tampilkan Halaman Review Approval dengan kondisi K15
62. Pilih `Reject` pada baris `Toyota Avanza - 6`
63. Isi Approval Note `MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuix` (121 karakter)
64. Klik `[Submit]`
65. Verifikasi pesan `Max. 120 characters` tampil di bawah field Approval Note
66. Verifikasi Submit diblokir karena Approval Note melebihi batas

### Approval Note tepat di batas dengan spasi tepi diterima
67. Tampilkan Halaman Review Approval dengan kondisi K15
68. Pilih `Reject` pada baris `Toyota Avanza - 6`
69. Isi Approval Note ` MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujui `
70. Klik `[Submit]`
71. Verifikasi dialog `Submit Approval` tampil karena spasi tepi tidak dihitung
72. Verifikasi pesan `Max. 120 characters` tidak tampil

### Approval Note tepat di batas dengan spasi tengah diterima
73. Tampilkan Halaman Review Approval dengan kondisi K15
74. Pilih `Reject` pada baris `Toyota Avanza - 6`
75. Isi Approval Note `Aset layak untuk ditugaskan. Aset layak untuk ditugaskan. Aset layak untuk ditugaskan. Aset layak untuk ditugaskan. Aset` (120 karakter)
76. Klik `[Submit]`
77. Verifikasi dialog `Submit Approval` tampil karena spasi tengah dihitung penuh
78. Verifikasi pesan `Max. 120 characters` tidak tampil

### Approval Note tepat di batas dengan huruf beraksen dan karakter non-BMP diterima
79. Tampilkan Halaman Review Approval dengan kondisi K15
80. Pilih `Reject` pada baris `Toyota Avanza - 6`
81. Isi Approval Note `MenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiMenyétujuiSetuju𝒜ya!` (120 karakter)
82. Klik `[Submit]`
83. Verifikasi dialog `Submit Approval` tampil karena Approval Note tepat 120 karakter
84. Verifikasi pesan `Max. 120 characters` tidak tampil

### Approval Note saat Approve bersifat opsional
85. Tampilkan Halaman Review Approval dengan kondisi K1
86. Klik `[Submit]`
87. Verifikasi dialog `Submit Approval` tampil dengan Approval Note baris Approve dibiarkan opsional

### Saving: tombol Submit masuk loading dan klik kedua tidak mengirim request kedua
88. Tampilkan Halaman Review Approval dengan kondisi K5
89. Klik `[Submit]` pada dialog Submit Approval
90. Verifikasi `[Submit]` pada dialog masuk saving state dan disabled
91. Verifikasi seluruh kontrol form termasuk ikon penutup disabled selama menunggu respons
92. Klik `[Submit]` pada dialog Submit Approval sekali lagi
93. Verifikasi permintaan Submit terkirim satu kali

### Konflik Any one: dialog Approval cannot be made terbuka real-time
94. Tampilkan Halaman Review Approval dengan kondisi K6
95. Verifikasi dialog `Approval cannot be made` tampil tanpa menunggu `[Submit]`
96. Verifikasi dialog memuat teks `You can no longer approve this request because it has already been done by another approver.`
97. Verifikasi dialog memuat tombol `[Close]`
98. Verifikasi keputusan yang belum dikirim pada baris `Excavator PC200 - 4` tidak tersimpan

### All: Reject dari approver lain membuka dialog, Approve tidak
99. Tampilkan Halaman Review Approval dengan kondisi K7
100. Verifikasi dialog `Approval cannot be made` tampil tanpa menunggu `[Submit]`
101. Verifikasi keputusan yang belum dikirim pada baris `Excavator PC200 - 4` tidak tersimpan

### All: Approve dari approver lain tidak membuka dialog
102. Tampilkan Halaman Review Approval dengan kondisi K8
103. Verifikasi halaman Review tetap tampil
104. Verifikasi dialog `Approval cannot be made` tidak tampil karena aset masih menunggu approver ini

### Konflik saat Submit menolak seluruh Submit
105. Tampilkan Halaman Review Approval dengan kondisi K9
106. Klik `[Submit]` pada dialog Submit Approval
107. Verifikasi dialog `Approval cannot be made` tampil
108. Verifikasi keputusan atas baris `Toyota Avanza - 6` tidak tersimpan

### Setelah Close, halaman dimuat ulang dengan hasil aset yang sudah diputuskan
109. Tampilkan Halaman Review Approval dengan kondisi K10
110. Verifikasi baris `Excavator PC200 - 4` read-only dengan hasil keputusan pihak lain
111. Verifikasi baris `Toyota Avanza - 6` tetap `Reject` dengan Approval Note yang sudah diisi

### Pengajuan dibatalkan oleh pengaju saat halaman terbuka
112. Tampilkan Halaman Review Approval dengan kondisi K11
113. Verifikasi dialog `Assignment Canceled` tampil
114. Verifikasi dialog memuat teks `This assignment was canceled by Dewi Lestari.`
115. Verifikasi dialog memuat tombol `[Back to Approvals]`

### Pengajuan dibatalkan otomatis oleh sistem saat halaman terbuka
116. Tampilkan Halaman Review Approval dengan kondisi K12
117. Verifikasi dialog `Assignment Canceled` tampil dengan teks `This assignment was canceled automatically (Assignee deactivated).`

### Mode read-only dari Detail di tab History
118. Tampilkan Halaman Review Approval dengan kondisi K13
119. Verifikasi breadcrumb `Approvals > Assignment > History > Detail`
120. Verifikasi halaman tidak memuat toggle `Approval`, Approval Note yang dapat diisi, toolbar bulk, dan footer
121. Verifikasi baris `Excavator PC200 - 4` menampilkan hasil `Approved`
122. Verifikasi baris `Toyota Avanza - 6` menampilkan hasil `Rejected`
123. Verifikasi baris `Camera Sony A7 - 9` menampilkan `Waiting for Approval`
124. Klik sel `Approval Rule` baris `Camera Sony A7 - 9`
125. Verifikasi dialog `Approval Progress` tampil

### Hasil pengajuan campuran
126. Tampilkan Halaman Review Approval dengan kondisi K14
127. Klik `[Submit]` pada dialog Submit Approval
128. Verifikasi toast `Success, assignment has been partially approved.` tampil


### Approval Note pada keputusan Approve: tepat di batas maksimum diterima
129. Tampilkan Halaman Review Approval dengan kondisi K18
130. Isi Approval Note baris `Toyota Avanza - 6` `MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujui` (120 karakter)
131. Klik `[Submit]`
132. Verifikasi dialog `Submit Approval` tampil karena Approval Note keputusan Approve tepat 120 karakter
133. Verifikasi pesan `Max. 120 characters` tidak tampil

### Approval Note pada keputusan Approve: satu karakter melewati batas ditolak
134. Tampilkan Halaman Review Approval dengan kondisi K18
135. Isi Approval Note baris `Toyota Avanza - 6` `MenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuiMenyetujuix` (121 karakter)
136. Verifikasi pesan `Max. 120 characters` tampil di bawah field Approval Note baris `Toyota Avanza - 6`
137. Klik `[Submit]`
138. Verifikasi dialog `Submit Approval` tidak tampil karena Approval Note melebihi batas

### Akses halaman Review ditolak untuk Assignee
139. Tampilkan Halaman Review Approval dengan kondisi K19
140. Verifikasi isi pengajuan `ASG-2026-0070` tidak ditampilkan kepada `Budi Santoso` karena akses ditolak

### Akses halaman Review ditolak untuk PIC
141. Tampilkan Halaman Review Approval dengan kondisi K20
142. Verifikasi isi pengajuan `ASG-2026-0072` tidak ditampilkan kepada `Sari Dewi` karena akses ditolak

### Ikon copy pada judul menyalin Transaction ID
143. Tampilkan Halaman Review Approval dengan kondisi K1
144. Klik ikon copy pada judul
145. Verifikasi toast `Success, Transaction ID has been copied.` tampil

### Nama Requested By yang panjang disertai tooltip nama lengkap
146. Tampilkan Halaman Review Approval dengan kondisi K21
147. Arahkan kursor ke nama Requested By
148. Verifikasi tooltip pada Requested By menyampaikan nama lengkap `Maria Magdalena Christina Kusumawardhani Wijayakusuma`

### Kolom Purpose per aset
149. Tampilkan Halaman Review Approval dengan kondisi K1
150. Verifikasi tabel memuat kolom `Purpose`
151. Verifikasi baris `Excavator PC200 - 4` menampilkan Purpose `Proyek tambang`
152. Verifikasi baris `Toyota Avanza - 6` menampilkan Purpose `Kunjungan klien`

### Klik sel Approval Rule membuka dialog Approval Progress
153. Tampilkan Halaman Review Approval dengan kondisi K1
154. Klik sel `Approval Rule` baris `Excavator PC200 - 4`
155. Verifikasi dialog `Approval Progress` tampil
