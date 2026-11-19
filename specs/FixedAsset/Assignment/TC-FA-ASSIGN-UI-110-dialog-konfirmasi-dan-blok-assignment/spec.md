---
id: TC-FA-ASSIGN-UI-110-dialog-konfirmasi-dan-blok-assignment
title: "Dialog konfirmasi dan blok: Cancel, Delete Draft, Submit, dan batas baris"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-01, D-ASG-02, D-ASG-03, D-ASG-06, D-ASG-20, D-ASG-24, DO-ASG-09, DO-ASG-10, EC-ASG-40, EC-ASG-41, "§4.2.8#p1", "§4.2.8#p2", "§4.2.8#p3", "§4.2.8#b1", "§4.2.8#b2", "§4.2.8#b3", "§4.2.8#b4", "§4.2.8#b5", "§4.2.8#b6", "§4.2.8#b7", "§4.2.8#b8", "§4.2.8#b9", "§4.2.8#b10", "§4.2.8#b11", "§4.2.8#b12", "§4.2.8#b13", "§7.2#r11", "§7.2#r12", "§7.2#r24", "§4.1#r11", "§9.5#r16", "§4.4#r3", "EB-ERR-2@delete-draft"]
smoke: []
dependsOn: []
trace:
  D-ASG-01: [2, 3, 4, 5, 7, 8, 9, 10, 12, 14, 15, 17, 19, 20, 22, 23, 26, 196, 197, 199, 200]
  D-ASG-02: [28, 29, 30, 31, 33, 34, 36]
  D-ASG-03: [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82]
  D-ASG-06: [84, 85, 86, 88, 90]
  D-ASG-20: [96, 100]
  D-ASG-24: [51, 52, 53, 54, 55, 57, 58, 59, 60, 62, 63, 64]
  DO-ASG-09: [96, 98]
  DO-ASG-10: 93
  EC-ASG-40: [96, 97, 98, 103, 104]
  EC-ASG-41: [107, 108, 109]
  "§4.2.8#p1": [114, 115, 118, 120]
  "§4.2.8#p2": [112, 113, 116, 117, 125, 126, 182, 185, 202, 203]
  "§4.2.8#p3": [113, 122]
  "§4.2.8#b1": [128, 131, 136]
  "§4.2.8#b2": [127, 130, 132]
  "§4.2.8#b3": [134, 135, 137]
  "§4.2.8#b4": [139, 140, 141, 143, 144]
  "§4.2.8#b5": [146, 147, 158]
  "§4.2.8#b6": [148, 149, 150]
  "§4.2.8#b7": 151
  "§4.2.8#b8": [152, 153, 156, 157]
  "§4.2.8#b9": 154
  "§4.2.8#b10": [161, 162, 165, 166]
  "§4.2.8#b11": [169, 172, 173]
  "§4.2.8#b12": [175, 176]
  "§4.2.8#b13": [178, 179]
  "§7.2#r11": 188
  "§7.2#r12": 194
  "§7.2#r24": 191
  "§4.1#r11": [188, 191, 194]
  "§9.5#r16": [76, 77]
  "§4.4#r3": [66, 67]
  "EB-ERR-2@delete-draft": [39, 40, 43, 44, 47, 49]
anchor: []
coverage:
  web: automated
---
# Dialog konfirmasi dan blok: Cancel, Delete Draft, Submit, dan batas baris

## Prerequisites
- Aktor: Asset Admin dengan cakupan Group `Head Office`, `Branch Surabaya`, dan `Gudang Medan`; pada K33 aktornya karyawan pengaju yang tidak berperan Aktor Assignment.
- Layar awal: halaman Assignment (daftar Transactions, tab Drafts, dan Assignment Detail), form Assignment Request, halaman Review Approval, atau halaman Unassign menurut kondisi.
- Komponen: Dialog Konfirmasi Assignment
- Data:
  - DU-110-1: ASG Transaction ID `ASG-2026-0071`, Group `Head Office`, Jumlah aset `3 assets`.
  - DU-110-2: Baris ASG Name `Laptop Dell Latitude 5420 - 10`, Transaction ID `ASG-2026-0071`.
  - DU-110-3: Baris ASG Name `Toyota Avanza - 6`, Transaction ID `ASG-2026-0071`.
  - DU-110-4: Draft Assignee `Budi Santoso`, Group `Head Office`.
  - DU-110-5: Draft Assignee `No assignee yet`, Group `Head Office`.
  - DU-110-6: Draft Assignee `Sari Dewi`, Group `Head Office`.
  - DU-110-7: Draft Assignee `Rina Wulandari`, Group `Cabang Bandung`, di luar cakupan Group Aktor.
  - DU-110-8: Baris aset form Name `Laptop Dell Latitude 5420 - 10`, Group `Head Office`, Purpose `Kerja dari rumah`, Approval Rule `No approval`.
  - DU-110-9: Baris aset form Name `Excavator PC200 - 4`, Group `Head Office`, Purpose `Proyek tambang`, Approval Rule `Needs approval`.
  - DU-110-10: Baris aset form Name `Toyota Avanza - 6`, Group `Branch Surabaya`, Purpose `Kunjungan klien`, Approval Rule `Needs approval`.
  - DU-110-25: Baris aset form Name `Genset Perkins 20kVA - 2`, Group `Gudang Medan`, Purpose `Cadangan listrik gudang`, Approval Rule `No approval`.
  - DU-110-11: Baris Transaction Rules Asset `Excavator PC200 - 4`, Approval `Needs approval`, Approval type `Any one approver`, Approver 1 `Agus Pratama`, Approver 2 `Rina Wulandari`, Approver 3 `Sari Dewi`, Status `Waiting for Approval`.
  - DU-110-12: Baris Transaction Rules Asset `Toyota Avanza - 6`, Approval `Needs approval`, Approval type `Any one approver`, Approver 1 `Agus Pratama`, Approver 2 `Rina Wulandari`, Approver 3 `Sari Dewi`, Keputusan `Rina Wulandari Approved pada T0 − 2 jam`.
  - DU-110-13: Baris Transaction Rules Asset `Printer HP M404 - 3`, Approval `Needs approval`, Approval type `All approvers`, Approver 1 `Agus Pratama`, Approver 2 `Rina Wulandari`, Approver 3 `Sari Dewi`, Keputusan `Agus Pratama Rejected pada T0 − 1 jam`.
  - DU-110-14: Baris Transaction Rules Asset `Camera Sony A7 - 9`, Approval `Needs approval`, Approval type `All approvers`, Approver 1 `Agus Pratama`, Approver 2 `Rina Wulandari`, Approver 3 `Sari Dewi`, Keputusan `Rina Wulandari Approved pada T0 − 3 jam`, Keterangan `Canceled by Dewi Lestari`.
  - DU-110-15: Baris Transaction Rules Asset `Tablet Samsung Tab S8 - 2`, Approval `Needs approval`, Approval type `Any one approver`, Approver 1 `Agus Pratama`, Approver 2 `Sari Dewi`, Keterangan `Canceled by system (approval timeout`.
  - DU-110-16: Baris Transaction Rules Asset `Laptop Dell Latitude 5420 - 10`, Putaran 3 (terbaru) `Needs approval, Any one approver, Agus Pratama dan Rina Wulandari Waiting for Approval`, Putaran 2 `Not required`, Putaran 1 `Needs approval, All approvers, Sari Dewi Rejected dan Agus Pratama Not Involved`, Submitted putaran 3 `T0 − 1 hari`, putaran 2 `T0 − 3 hari`, putaran 1 `T0 − 5 hari`, Approval Note Agus Pratama `Setuju setelah cek lapangan`.
  - DU-110-17: Baris Transaction Rules Asset `Printer HP M404 - 3`, Approval `Needs approval`, Approval type `All approvers`, Approver 1 `Agus Pratama`, Approver 2 `Rina Wulandari`, Override `Dewi Lestari Approved dengan keterangan Group Manager override`.
  - DU-110-18: Baris Transaction Rules Asset `Camera Sony A7 - 9`, Approval `Needs approval`, Approval type `Any one approver`, Approver 1 `Agus Pratama`, Approver 2 `Sari Dewi`, Override `Hendra Gunawan Rejected dengan keterangan Total Control override`.
  - DU-110-19: Baris Transaction Rules Asset `Excavator PC200 - 5`, Approval `Needs approval`, Penerima `Dewi Lestari`, Keterangan `Routed to Group Manager`.
  - DU-110-20: Baris Transaction Rules Asset `Excavator PC200 - 6`, Approval `Needs approval`, Penerima `Hendra Gunawan`, Keterangan `Routed to Total Control`.
  - DU-110-21: Baris Transaction Rules Asset `Forklift Toyota 8FD - 1`, Approval `Needs approval`, Approval type `Any one approver`, Approver 1 `Agus Pratama`, Approver 2 `Bambang Hartono`, Approver 3 `Citra Lestari`, Approver 4 `Dewi Anggraini`, Approver 5 `Eko Prasetyo`, Approver 6 `Fajar Nugroho`, Approver 7 `Gita Permata`, Approver 8 `Hendra Gunawan`.
  - DU-110-22: Baris Transaction Rules Asset `Laptop Dell Latitude 5420 - 12`, Approval `Needs approval`.
  - DU-110-23: Baris Transaction Rules Asset `Tablet Samsung Tab S8 - 3`, Approval `Needs approval`, Approval type `—`, Approver 1 `Agus Pratama`.
  - DU-110-24: Baris Transaction Rules Asset `Printer HP M404 - 4`, Approval `Not required`.
- Kondisi:
  - K1: dialog Cancel Assignment dibuka untuk satu ASG DU-110-1; bullet yang diharapkan `ASG-2026-0071 · Head Office · 3 assets`, dari Transaction ID, Group, dan Jumlah aset DU-110-1.
  - K2: dialog Cancel Assignment dibuka dari baris DU-110-2 (level Full, Aktor Assignment, belum ada baris Assigned pada ASG); bullet yang diharapkan `Laptop Dell Latitude 5420 - 10 · ASG-2026-0071`, dari Name dan Transaction ID DU-110-2.
  - K3: dialog Cancel Assignment dibuka dari dua baris, DU-110-2 dan DU-110-3, dengan syarat checkbox sama seperti K2; bullet yang diharapkan `Laptop Dell Latitude 5420 - 10 · ASG-2026-0071` dan `Toyota Avanza - 6 · ASG-2026-0071`.
  - K4: dialog Cancel Assignment dibuka dari baris DU-110-2 pada level Basic.
  - K5: dialog Cancel Assignment dibuka dari baris DU-110-2 pada ASG yang sudah memuat baris Assigned.
  - K6: dialog Delete Draft dibuka untuk DU-110-4; bullet yang diharapkan `Budi Santoso · Head Office`, dari Assignee dan Group DU-110-4.
  - K7: dialog Delete Draft dibuka untuk DU-110-5; bullet yang diharapkan `No assignee yet · Head Office`, dari Assignee dan Group DU-110-5.
  - K8: dialog Delete Drafts dibuka untuk DU-110-4 dan DU-110-6, keduanya dalam cakupan Aktor; bullet yang diharapkan `Budi Santoso · Head Office` dan `Sari Dewi · Head Office`.
  - K9: dialog Delete Drafts dibuka untuk DU-110-4, DU-110-6, dan DU-110-7, dengan DU-110-7 memuat aset di luar Group Aktor; bullet dilewati yang diharapkan `Rina Wulandari · Cabang Bandung`.
  - K10: dialog Delete Drafts dibuka untuk satu Draft, yaitu DU-110-4, lewat Bulk Action.
  - K11: dialog Submit Assignment dibuka dari form dengan urutan baris DU-110-9, DU-110-8, DU-110-10 yang terpecah ke dua Group; kalimat pemecahan yang diharapkan `This will create 2 assignments (Head Office, Branch Surabaya).`, dari 2 Group; blok Approval yang diharapkan `No approval needed: Laptop Dell Latitude 5420 - 10.` dan `Needs approval: Excavator PC200 - 4.`, dari Asset Name; jumlah aset kartu `Head Office` yang diharapkan `2` dan kartu `Branch Surabaya` yang diharapkan `1`.
  - K12: dialog Submit Assignment dibuka dari form dengan baris DU-110-9 dan DU-110-8 yang hanya terdiri dari satu Group `Head Office`.
  - K13: form Assignment Request memuat DU-110-8, DU-110-9, DU-110-10, dan DU-110-25 dari tiga Group; alert pemecahan yang diharapkan `This will create 3 assignments (Head Office, Branch Surabaya, Gudang Medan).`, dari 3 Group.
  - K14: dialog Submit Approval dibuka dari halaman Review Approval dengan keputusan atas 1 aset.
  - K15: dialog Submit Approval dibuka dari halaman Review Approval dengan keputusan atas 3 aset.
  - K16: form Assignment Request memuat aset sebanyak Bulk Transaction Row Limit ditambah 1; isian dan pilihan aset form sudah terisi.
  - K17: form Assignment Request memuat aset sebanyak tepat Bulk Transaction Row Limit.
  - K18: halaman Unassign memuat aset sebanyak Bulk Transaction Row Limit ditambah 1; Verification sudah diisi dan Photo sudah diunggah.
  - K19: daftar baris memuat DU-110-11 dan DU-110-13; dialog Transaction Rules dibuka dari baris masing-masing; level Full; identitas yang diharapkan `Asset : Excavator PC200 - 4` dan `Asset : Printer HP M404 - 3`, dari Asset.
  - K20: dialog Transaction Rules dibuka untuk DU-110-12 (Any one approver; satu approver sudah memutuskan).
  - K21: dialog Transaction Rules dibuka untuk DU-110-13 (All approvers; satu Rejected).
  - K22: dialog Transaction Rules dibuka untuk DU-110-14 (baris di-Cancel oleh Aktor sebelum diputuskan penuh).
  - K23: dialog Transaction Rules dibuka untuk DU-110-15 (baris ditutup sistem karena approval timeout).
  - K24: dialog Transaction Rules dibuka untuk DU-110-16 (tiga putaran) dari baris di daftar.
  - K25: dialog Approval Progress dibuka dari halaman Review pengajuan putaran 1 untuk DU-110-16.
  - K26: dialog Transaction Rules dibuka untuk DU-110-17 (override Group Manager) dan DU-110-18 (override Total Control).
  - K27: dialog Transaction Rules dibuka untuk DU-110-19 (dirutekan ke Group Manager) dan DU-110-20 (dirutekan ke Total Control).
  - K28: dialog Transaction Rules dibuka untuk DU-110-21 (delapan approver).
  - K29: dialog Transaction Rules dibuka untuk baris Draft DU-110-22.
  - K30: dialog Transaction Rules dibuka untuk DU-110-23 (satu approver) dan DU-110-24 (Approval tidak diwajibkan).
  - K31: Assignment Detail memuat baris Assigned `Laptop Dell Latitude 5420 - 10` yang belum dilaporkan; Aktor Assignment membuka dialog laporan.
  - K33: dialog Cancel Assignment dibuka dari baris DU-110-2 pada level Full, belum ada baris Assigned pada ASG, oleh karyawan pengaju yang tidak lagi berperan Aktor Assignment.
  - K34: dialog Cancel Assignment dibuka dari dua baris, DU-110-2 dan DU-110-3, pada level Basic.
  - K35: halaman Review Approval dengan keputusan atas 3 aset; dialog Submit Approval belum dibuka.
  - K32: Assignment Detail memuat baris Assigned `Toyota Avanza - 6` yang laporan Damaged-nya milik Aktor dan masih `Waiting for Confirmation`.

## Test Steps

### Cancel Assignment per ASG
1. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K1
2. Verifikasi judul dialog `Cancel Assignment`
3. Verifikasi body memuat bullet `ASG-2026-0071 · Head Office · 3 assets`
4. Verifikasi body memuat pertanyaan `Are you sure you want to cancel it?`
5. Verifikasi dialog memuat tombol `[Go Back]` dan `[Cancel Assignment]`

### Cancel per baris: satu aset, checkbox, dan teks bantu
6. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K2
7. Verifikasi body memuat bullet `Laptop Dell Latitude 5420 - 10 · ASG-2026-0071`
8. Verifikasi dialog tidak memuat field Reason
9. Verifikasi checkbox `Save as Draft to edit` tampil dan tidak tercentang
10. Verifikasi teks bantu `The asset becomes available again and the assignee and approvers are notified.` tampil
11. Centang `Save as Draft to edit`
12. Verifikasi teks bantu `The asset becomes available again and a new draft with the same details is created so you can fix and resubmit it.` tampil

### Cancel per baris: dua aset
13. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K3
14. Verifikasi body memuat bullet `Laptop Dell Latitude 5420 - 10 · ASG-2026-0071` dan `Toyota Avanza - 6 · ASG-2026-0071`
15. Verifikasi teks bantu `The assets become available again and the assignee and approvers are notified.` tampil
16. Centang `Save as Draft to edit`
17. Verifikasi teks bantu `The assets become available again and a new draft with the same details is created so you can fix and resubmit it.` tampil

### Checkbox Save as Draft to edit tidak tampil pada level Basic
18. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K4
19. Verifikasi teks bantu `The asset becomes available again and the assignee and approvers are notified.` tampil
20. Verifikasi checkbox `Save as Draft to edit` tidak tampil

### Checkbox Save as Draft to edit tidak tampil bila sudah ada baris Assigned
21. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K5
22. Verifikasi teks bantu `The asset becomes available again and the assignee and approvers are notified.` tampil
23. Verifikasi checkbox `Save as Draft to edit` tidak tampil

### Go Back menutup dialog Cancel Assignment
24. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K1
25. Klik `[Go Back]`
26. Verifikasi dialog Cancel Assignment tertutup

### Delete Draft dengan Assignee: judul, bullet, pertanyaan, tombol, dan toast
27. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K6
28. Verifikasi judul dialog `Delete Draft`
29. Verifikasi body memuat bullet `Budi Santoso · Head Office`
30. Verifikasi body memuat `This draft will be removed. Are you sure you want to delete it?`
31. Verifikasi dialog memuat tombol `[Go Back]` dan `[Delete]`
32. Klik `[Delete]`
33. Verifikasi toast `Success, draft has been deleted.` tampil setelah Delete Draft dikonfirmasi
34. Verifikasi dialog Delete Draft tertutup

### Delete Draft tanpa Assignee
35. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K7
36. Verifikasi body memuat bullet `No assignee yet · Head Office`

### Klik ganda Delete menghapus sekali dengan satu toast
37. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K6
38. Klik ganda `[Delete]`
39. Verifikasi Draft dihapus satu kali
40. Verifikasi toast `Success, draft has been deleted.` tampil satu kali

### Esc menutup dialog Delete Draft tanpa menghapus
41. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K6
42. Tekan Esc
43. Verifikasi dialog Delete Draft tertutup
44. Verifikasi Draft `Budi Santoso · Head Office` tidak dihapus

### Fokus terkunci di dialog Delete Draft dan kembali ke pemicu
45. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K6
46. Tekan Tab sebanyak jumlah kontrol di dialog ditambah satu
47. Verifikasi fokus tetap berada di dalam dialog Delete Draft
48. Klik `[Go Back]`
49. Verifikasi fokus kembali ke pemicu dialog

### Delete Drafts: semua Draft dapat dihapus
50. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K8
51. Verifikasi judul dialog `Delete Drafts`
52. Verifikasi daftar bullet memuat `Budi Santoso · Head Office` dan `Sari Dewi · Head Office`
53. Verifikasi daftar bullet berada dalam container yang dapat di-scroll
54. Verifikasi body memuat `These drafts will be removed. Are you sure you want to delete them?`
55. Verifikasi dialog memuat tombol `[Go Back]` dan `[Delete]`

### Delete Drafts: sebagian dilewati
56. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K9
57. Verifikasi label `The following will be deleted:` tampil dengan bullet `Budi Santoso · Head Office` dan `Sari Dewi · Head Office`
58. Verifikasi label `The following will be skipped because they include assets outside your groups:` tampil dengan bullet `Rina Wulandari · Cabang Bandung`
59. Verifikasi body memuat penutup `Are you sure you want to continue?`
60. Verifikasi dialog memuat tombol `[Go Back]` dan `[Continue]`

### Delete Drafts dengan hasil akhir satu Draft memakai dialog Delete Draft
61. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K10
62. Verifikasi judul dialog `Delete Draft`
63. Verifikasi body memuat bullet `Budi Santoso · Head Office`
64. Verifikasi body memuat `This draft will be removed. Are you sure you want to delete it?`

### Alert pemecahan di form saat aset berasal dari Group berbeda
65. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K13
66. Verifikasi alert `This will create 3 assignments (Head Office, Branch Surabaya, Gudang Medan).` tampil di form
67. Verifikasi alert menyebut ketiga Group aset di form: `Head Office`, `Branch Surabaya`, dan `Gudang Medan`

### Submit Assignment dengan dua ASG
68. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K11
69. Verifikasi judul dialog `Submit Assignment`
70. Verifikasi dialog memuat kalimat `This will create 2 assignments (Head Office, Branch Surabaya).`
71. Verifikasi kartu `Head Office` memuat jumlah aset `2`
72. Verifikasi kartu `Head Office` memuat aset `Laptop Dell Latitude 5420 - 10` dengan Purpose `Kerja dari rumah`
73. Verifikasi kartu `Head Office` memuat aset `Excavator PC200 - 4` dengan Purpose `Proyek tambang`
74. Verifikasi kartu `Branch Surabaya` memuat jumlah aset `1`
75. Verifikasi kartu `Branch Surabaya` memuat aset `Toyota Avanza - 6` dengan Purpose `Kunjungan klien`
76. Verifikasi kartu `Head Office` memuat blok Approval `No approval needed: Laptop Dell Latitude 5420 - 10.`
77. Verifikasi kartu `Head Office` memuat blok Approval `Needs approval: Excavator PC200 - 4.`
78. Verifikasi dialog memuat penutup `Are you sure you want to submit it?`
79. Verifikasi dialog memuat tombol `[Cancel]` dan `[Submit]`

### Submit Assignment dengan satu ASG tanpa kalimat pemecahan
80. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K12
81. Verifikasi kartu `Head Office` memuat aset `Excavator PC200 - 4` dengan Purpose `Proyek tambang`
82. Verifikasi dialog tidak memuat kalimat `This will create`

### Submit Approval untuk satu aset
83. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K14
84. Verifikasi judul dialog `Submit Approval`
85. Verifikasi body memuat `You will submit your decision for 1 asset. Are you sure you want to submit it?`
86. Verifikasi dialog memuat tombol `[Cancel]` dan `[Submit]`

### Submit Approval untuk beberapa aset
87. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K15
88. Verifikasi body memuat `You will submit your decision for 3 assets. Are you sure you want to submit it?`
89. Klik `[Cancel]`
90. Verifikasi dialog Submit Approval tertutup

### Submit pada halaman Review membuka dialog Submit Approval
91. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K35
92. Klik `[Submit]` pada halaman Review
93. Verifikasi dialog `Submit Approval` tampil

### Submit melebihi Bulk Transaction Row Limit pada form Assignment Request
94. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K16
95. Klik `[Submit]`
96. Verifikasi dialog blok `Bulk Transaction Row Limit` tampil dengan tombol `[OK]` karena jumlah aset melebihi batas
97. Verifikasi tidak ada pengajuan yang dibuat
98. Verifikasi isian dan pilihan aset di form tidak direset
99. Klik `[OK]`
100. Verifikasi dialog Bulk Transaction Row Limit tertutup

### Submit dengan jumlah aset tepat sama dengan batas lolos
101. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K17
102. Klik `[Submit]`
103. Verifikasi dialog konfirmasi `Submit Assignment` tampil karena jumlah aset sama dengan batas
104. Verifikasi dialog `Bulk Transaction Row Limit` tidak tampil

### Submit melebihi Bulk Transaction Row Limit pada halaman Unassign
105. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K18
106. Klik `[Submit]`
107. Verifikasi dialog `Bulk Transaction Row Limit` tampil
108. Verifikasi tidak ada baris yang berubah
109. Verifikasi Verification dan Photo pada halaman Unassign tetap terisi

### Transaction Rules: judul, identitas, batas, Approval, dan ikon silang
110. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K19
111. Klik `Transaction Rules` pada baris `Excavator PC200 - 4`
112. Verifikasi judul dialog `Transaction Rules`
113. Verifikasi identitas `Asset : Excavator PC200 - 4` tampil di bawah judul
114. Verifikasi dialog memuat batas `Allowed assignee`, `Need recipient confirmation`, `Photo at start`, dan `Photo at end`
115. Verifikasi dialog tidak memuat versi setting
116. Verifikasi dialog memuat Approval `Needs approval`
117. Verifikasi bagian `Approval Progress` tampil karena baris punya satu putaran approval
118. Verifikasi dialog tidak memuat tombol `Close`
119. Klik ikon silang
120. Verifikasi dialog Transaction Rules tertutup
121. Klik `Transaction Rules` pada baris `Printer HP M404 - 3`
122. Verifikasi identitas `Asset : Printer HP M404 - 3` tampil di bawah judul

### Any one approver sebelum ada keputusan
123. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K19
124. Klik `Transaction Rules` pada baris `Excavator PC200 - 4`
125. Verifikasi blok putaran memuat Approval type `Any one approver`
126. Verifikasi approver tampil satu per baris urut A–Z: `Agus Pratama`, `Rina Wulandari`, `Sari Dewi`
127. Verifikasi `Agus Pratama`, `Rina Wulandari`, dan `Sari Dewi` berstatus `Waiting for Approval`
128. Verifikasi status approver memakai salah satu dari `Waiting for Approval`, `Approved`, `Rejected`, atau `Not Involved`

### Any one approver: satu approver memutuskan
129. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K20
130. Verifikasi `Rina Wulandari` berstatus `Approved`
131. Verifikasi status `Approved` pada `Rina Wulandari` disertai waktu keputusannya
132. Verifikasi `Agus Pratama` dan `Sari Dewi` berstatus `Not Involved`

### All approvers: satu Rejected menolak aset
133. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K21
134. Verifikasi blok putaran memuat Approval type `All approvers`
135. Verifikasi `Agus Pratama` berstatus `Rejected`
136. Verifikasi status `Rejected` pada `Agus Pratama` disertai waktu keputusannya
137. Verifikasi `Rina Wulandari` dan `Sari Dewi` berstatus `Not Involved`

### Baris di-Cancel sebelum diputuskan
138. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K22
139. Verifikasi `Rina Wulandari` tetap `Approved` disertai waktunya
140. Verifikasi `Agus Pratama` dan `Sari Dewi` berstatus `Not Involved`
141. Verifikasi dialog memuat keterangan `Canceled by Dewi Lestari` disertai waktunya

### Baris ditutup sistem karena approval timeout
142. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K23
143. Verifikasi `Agus Pratama` dan `Sari Dewi` berstatus `Not Involved`
144. Verifikasi dialog memuat keterangan `Canceled by system (approval timeout` disertai waktunya

### Blok per putaran: terbaru di atas, snapshot sendiri, dan putaran Not required
145. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K24
146. Verifikasi bagian `Approval Progress` memuat tiga blok putaran
147. Verifikasi blok putaran terbaru tampil paling atas
148. Verifikasi blok putaran terbaru memuat `Agus Pratama` dan `Rina Wulandari` sebagai approver
149. Verifikasi blok putaran terlama memuat `Sari Dewi` dan `Agus Pratama` sebagai approver
150. Verifikasi blok putaran dengan Approval `Not required` tampil tanpa daftar approver
151. Verifikasi blok putaran terlama yang di-Reject tetap tampil dengan `Sari Dewi` berstatus `Rejected` dan `Agus Pratama` berstatus `Not Involved`
152. Verifikasi blok putaran terbaru terbuka
153. Verifikasi blok putaran lain terlipat
154. Verifikasi Approval Note `Setuju setelah cek lapangan` dari `Agus Pratama` tidak ditampilkan

### Dialog dari halaman Review menaruh blok pengajuan itu paling atas dan terbuka
155. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K25
156. Verifikasi blok putaran 1 tampil paling atas
157. Verifikasi blok putaran 1 terbuka
158. Verifikasi bagian `Approval Progress` hanya memuat format blok yang sama dengan Transaction Rules

### Override Group Manager dan Total Control
159. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K26
160. Klik `Transaction Rules` pada baris `Printer HP M404 - 3`
161. Verifikasi `Dewi Lestari` tampil sebagai baris tambahan berstatus `Approved` dengan keterangan `Group Manager override`
162. Verifikasi `Agus Pratama` dan `Rina Wulandari` berstatus `Not Involved`
163. Klik ikon silang
164. Klik `Transaction Rules` pada baris `Camera Sony A7 - 9`
165. Verifikasi `Hendra Gunawan` tampil sebagai baris tambahan berstatus `Rejected` dengan keterangan `Total Control override`
166. Verifikasi `Agus Pratama` dan `Sari Dewi` berstatus `Not Involved`

### Daftar snapshot kosong dirutekan ke Group Manager atau Total Control
167. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K27
168. Klik `Transaction Rules` pada baris `Excavator PC200 - 5`
169. Verifikasi `Dewi Lestari` tampil sebagai penerima dengan keterangan `Routed to Group Manager`
170. Klik ikon silang
171. Klik `Transaction Rules` pada baris `Excavator PC200 - 6`
172. Verifikasi `Hendra Gunawan` tampil sebagai penerima dengan keterangan `Routed to Total Control`
173. Verifikasi dialog tidak memuat `Approval rerouted`

### Banyak approver tampil semua tanpa dipotong dan dapat di-scroll
174. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K28
175. Verifikasi delapan approver tampil dengan nama lengkap: `Agus Pratama`, `Bambang Hartono`, `Citra Lestari`, `Dewi Anggraini`, `Eko Prasetyo`, `Fajar Nugroho`, `Gita Permata`, `Hendra Gunawan`
176. Verifikasi area daftar approver dapat di-scroll dengan tinggi maksimal 5 baris

### Baris Draft belum punya progres approval
177. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K29
178. Verifikasi dialog memuat keterangan `Final rules are fixed when you submit`
179. Verifikasi bagian `Approval Progress` tidak tampil

### Satu approver dan Approval tidak diwajibkan
180. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K30
181. Klik `Transaction Rules` pada baris `Tablet Samsung Tab S8 - 3`
182. Verifikasi blok putaran memuat Approval type `—` karena approver hanya satu
183. Klik ikon silang
184. Klik `Transaction Rules` pada baris `Printer HP M404 - 4`
185. Verifikasi dialog memuat Approval `Not required`

### Dialog Report Damaged dan Report Missing dibuka dari Assignment Detail
186. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K31
187. Klik `Report Damaged` pada baris `Laptop Dell Latitude 5420 - 10`
188. Verifikasi dialog `Report Damaged` tampil
189. Klik ikon silang
190. Klik `Report Missing` pada baris `Laptop Dell Latitude 5420 - 10`
191. Verifikasi dialog `Report Missing` tampil

### Dialog Cancel Report dibuka dari Assignment Detail
192. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K32
193. Klik `Cancel Report` pada baris `Toyota Avanza - 6`
194. Verifikasi dialog `Cancel Report` tampil

### Checkbox Save as Draft to edit tidak tampil bagi aktor yang bukan Aktor Assignment
195. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K33
196. Verifikasi teks bantu `The asset becomes available again and the assignee and approvers are notified.` tampil
197. Verifikasi checkbox `Save as Draft to edit` tidak tampil

### Teks bantu bentuk jamak bila checkbox tidak tampil
198. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K34
199. Verifikasi teks bantu `The assets become available again and the assignee and approvers are notified.` tampil
200. Verifikasi checkbox `Save as Draft to edit` tidak tampil

### Blok putaran memuat Submitted dan Approval mengikuti putaran terakhir
201. Tampilkan Dialog Konfirmasi Assignment dengan kondisi K24
202. Verifikasi ketiga blok putaran masing-masing memuat `Submitted` beserta tanggal dan waktu pengajuan putaran itu
203. Verifikasi baris Approval dialog menampilkan `Needs approval`, nilai putaran terakhir, walau putaran tengah `Not required`
