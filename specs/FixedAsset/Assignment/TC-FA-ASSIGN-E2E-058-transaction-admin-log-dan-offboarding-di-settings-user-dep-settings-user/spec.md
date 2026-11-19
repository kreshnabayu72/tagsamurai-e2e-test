---
id: TC-FA-ASSIGN-E2E-058-transaction-admin-log-dan-offboarding-di-settings-user-dep-settings-user
title: "Transaction admin log di User Detail dan Assignee dinonaktifkan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.2#p1", "§8.2#p2", "§8.2#r1", "§8.2#r2", "§8.2#r3", "§8.2#r4", "§8.2#r5", EC-ASG-01, EC-ASG-02, EC-ASG-31, EC-ASG-67, "§9.7#r17", "§9.7#r18", "§9.7#r21", ASSIGN-LOGIC-16ad, ASSIGN-LOGIC-16ae, ASSIGN-LOGIC-16ap, ASSIGN-LOGIC-16aq]
smoke: []
dependsOn: ["Settings User: User Detail > Transaction admin log, daftar Unassign offboarding"]
trace:
  "§8.2#p1": [4, 5]
  "§8.2#p2": 11
  "§8.2#r1": [10, 22, 25, 108, 112, 116, 117, 121, 125, 130]
  "§8.2#r2": 5
  "§8.2#r3": [16, 99]
  "§8.2#r4": [6, 7, 8, 90, 91, 92, 94]
  "§8.2#r5": [9, 93, 104]
  EC-ASG-01: [32, 36, 41, 44, 141, 149]
  EC-ASG-02: [62, 71, 76, 154, 163, 168]
  EC-ASG-31: [50, 53, 54, 58]
  EC-ASG-67: [82, 84]
  "§9.7#r17": [32, 44]
  "§9.7#r18": 50
  "§9.7#r21": [5, 6]
  ASSIGN-LOGIC-16ad: [32, 36]
  ASSIGN-LOGIC-16ae: [45, 149]
  ASSIGN-LOGIC-16ap: [41, 140, 141, 143, 147]
  ASSIGN-LOGIC-16aq: 44
anchor: [135]
coverage:
  web: automated
---
# Transaction admin log di User Detail dan Assignee dinonaktifkan

## Prerequisites
- Aktor: Admin pengguna (Total Control `Fajar Nugroho {runId}`, DU-058-3) yang membuka User Detail di Settings > User, menonaktifkan karyawan, dan mencabut akun login; Aktor Assignment (Asset Admin `Dewi Lestari {runId}`, DU-058-1, dan Asset Admin `Bayu Pratama {runId}`, DU-058-19) yang bekerja di Transactions > Assignment; Approver `Anton Pratama {runId}` (DU-058-2).
- Layar awal: Settings > User.
- Data:
  - DU-058-1: Karyawan `Dewi Lestari {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`.
  - DU-058-2: Karyawan `Anton Pratama {runId}`, role Approver, Group penugasan `Head Office`, Status `Active`.
  - DU-058-3: Karyawan `Fajar Nugroho {runId}`, role Total Control, Status `Active`.
  - DU-058-4: Karyawan `Rudi Hartono {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`, pembuat Draft DU-058-9.
  - DU-058-5: Karyawan `Tono Hartono {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee DU-058-12, DU-058-13, DU-058-14, dan DU-058-15.
  - DU-058-6: Karyawan `Gita Maharani {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, PIC Division `Finance {runId}`.
  - DU-058-7: Karyawan `Wulan Sari {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee DU-058-17.
  - DU-058-8: Draft Assignee `Wulan Sari {runId}` dengan aset `Kamera Mirrorless Sony A6400 {runId}` (Group `Head Office`), Purpose `Dokumentasi acara`, dibuat oleh `Dewi Lestari {runId}`; satu baris tindakan Draft create tercatat di Transaction admin log `Dewi Lestari {runId}`; Modified By Draft `Dewi Lestari {runId}`. Purpose baru yang diketik Aktor: `Dokumentasi seminar`.
  - DU-058-9: Draft Assignee `Budi Santoso {runId}` (DU-058-20) dengan aset `Mesin Label Brother PT-P700 {runId}` (Group `Head Office`, dalam cakupan Group `Head Office` Aktor Assignment `Dewi Lestari {runId}`), Purpose `Pelabelan aset`, dibuat oleh `Rudi Hartono {runId}`.
  - DU-058-10: Riwayat tindakan `Dewi Lestari {runId}` di Transaction admin log: `Assignment requested by [Actor]` untuk aset `Kursi Ergonomis Ergotec {runId}` (Purpose `Kerja harian`, Approval `Not required`); `Handed over by [Giver]` untuk aset `Meja Kerja Lipat {runId}`; `PIC changed by [Actor]` untuk aset `Lemari Arsip Besi {runId}`; `Damage reported by [Reporter]` untuk aset `Kipas Angin Berdiri {runId}`; `Canceled by [Actor]` untuk aset `Rak Buku Kayu {runId}`; `Unassigned by [Receiver]` untuk aset `Scanner Epson DS-530 {runId}`; `Reported missing by [Actor]` untuk aset `Router Mikrotik hAP ax2 {runId}`; `Damage report canceled by [Actor]` untuk aset `Proyektor Epson EB-X06 {runId}`; `Canceled by [Actor]` dengan Description `Saved as draft` untuk aset `Whiteboard Magnetik {runId}` (Cancel dengan Save as draft).
  - DU-058-11: Riwayat tindakan `Anton Pratama {runId}`: `Approved by [Approver]` untuk aset `Dispenser Air Galon {runId}`; `Rejected by [Approver]` untuk aset `Kulkas Mini Sharp {runId}`.
  - DU-058-12: ASG `Waiting for Approval` untuk Assignee `Tono Hartono {runId}`, diajukan oleh pengaju `Dewi Lestari {runId}`, berisi aset `Laptop Asus ExpertBook {runId}` (Group `Head Office`).
  - DU-058-13: ASG `Waiting for Handover` untuk Assignee `Tono Hartono {runId}`, diajukan oleh pengaju `Dewi Lestari {runId}`, berisi aset `Monitor Samsung S24 {runId}` (Group `Head Office`).
  - DU-058-14: ASG `Assigned` untuk Assignee `Tono Hartono {runId}` berisi aset `Proyektor Optoma HD146X {runId}`.
  - DU-058-15: Draft Assignee `Tono Hartono {runId}` berisi aset `Printer Brother HL-L2375 {runId}` (Group `Head Office`), Purpose `Cetak laporan`.
  - DU-058-16: ASG Assignee Division `Finance {runId}` dengan PIC `Gita Maharani {runId}`, satu baris `Waiting for Handover` untuk aset `Speaker Bluetooth Bose {runId}` dan satu baris `Assigned` untuk aset `Kamera Canon M50 {runId}`.
  - DU-058-17: ASG `Waiting for Handover` untuk Assignee `Wulan Sari {runId}`, Confirmation Rule `Yes`, berisi aset `Headset Jabra Evolve 40 {runId}`; Handover dikerjakan `Dewi Lestari {runId}` lewat Confirm on This Device, sehingga Description log Handed over adalah `Confirmation: Confirmed by Dewi Lestari {runId} on behalf of Wulan Sari {runId}`.
  - DU-058-18: ASG `Assigned` untuk Assignee `Dewi Lestari {runId}` berisi aset `Tablet Lenovo Tab M10 {runId}`, diserahkan oleh `Rudi Hartono {runId}` dan dikonfirmasi `Dewi Lestari {runId}` sebagai Assignee.
  - DU-058-19: Karyawan `Bayu Pratama {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`; Aktor Assignment Group aset selain pengaju.
  - DU-058-20: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee Draft DU-058-9.
  - DU-058-21: Karyawan `Sinta Wijaya {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login; Assignee pengganti untuk Draft DU-058-15.
  - DU-058-22: Karyawan `Hendra Saputra {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, PIC Division `Operations {runId}`.
  - DU-058-23: ASG Assignee Division `Operations {runId}` dengan PIC `Hendra Saputra {runId}`, satu baris `Waiting for Handover`, Confirmation Rule `Yes`, berisi aset `Genset Honda EU22i {runId}` (Group `Head Office`).
  - DU-058-24: Riwayat tindakan `Fajar Nugroho {runId}`: `Canceled by [Actor]` untuk aset `Kulkas Showcase {runId}`.
- Kondisi:
  - Akun semua karyawan aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Transaction admin log Aktor Assignment memuat kolom dan tindakan Aktor
1. Admin pengguna `Fajar Nugroho {runId}`: Ketik Search `Dewi Lestari {runId}`, tekan Enter
2. Buka User Detail `Dewi Lestari {runId}`
3. Buka tab `Transaction admin log`
4. Verifikasi kolom `Date`, `Activity`, `Transaction No.`, `Asset(s)`, dan `Description` tampil
5. Verifikasi baris Activity `Assignment requested by [Actor]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Kursi Ergonomis Ergotec {runId}` dengan Description `Purpose: Kerja harian · Approval: Not required`
6. Verifikasi baris Activity `Handed over by [Giver]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Meja Kerja Lipat {runId}`
7. Verifikasi baris Activity `PIC changed by [Actor]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Lemari Arsip Besi {runId}`
8. Verifikasi baris Activity `Damage reported by [Reporter]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Kipas Angin Berdiri {runId}`
9. Verifikasi baris Activity `Canceled by [Actor]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Rak Buku Kayu {runId}`
10. Verifikasi satu baris tindakan Draft create dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Kamera Mirrorless Sony A6400 {runId}`
11. Verifikasi tidak ada baris untuk aset `Tablet Lenovo Tab M10 {runId}` karena konfirmasi Assignee atas penugasannya sendiri tidak masuk log ini

### Transaction admin log Approver memuat keputusan Approve
12. Kembali ke daftar pengguna
13. Ketik Search `Anton Pratama {runId}`, tekan Enter
14. Buka User Detail `Anton Pratama {runId}`
15. Buka tab `Transaction admin log`
16. Verifikasi baris Activity `Approved by [Approver]` dengan pelaku `Anton Pratama {runId}` tampil untuk aset `Dispenser Air Galon {runId}`

### Save Draft tanpa perubahan tidak menambah baris log
17. Aktor Assignment `Dewi Lestari {runId}`: Buka halaman Transactions > Assignment
18. Buka tab Drafts
19. Ketik Search `Kamera Mirrorless Sony A6400 {runId}`, tekan Enter
20. Klik ikon `Edit` pada baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}`
21. Klik `[Save Draft]` tanpa mengubah isian
22. Verifikasi toast `No changes to save.`
23. Admin pengguna `Fajar Nugroho {runId}`: Buka User Detail `Dewi Lestari {runId}`
24. Buka tab `Transaction admin log`
25. Verifikasi tetap satu baris tindakan untuk aset `Kamera Mirrorless Sony A6400 {runId}`

### Assignee dinonaktifkan: baris menunggu dibatalkan otomatis
26. Admin pengguna `Fajar Nugroho {runId}`: Nonaktifkan karyawan `Tono Hartono {runId}`
27. Buka halaman Transactions > Assignment
28. Buka tab History
29. Buka sub-tab By Asset
30. Ketik Search `Laptop Asus ExpertBook {runId}`, tekan Enter
31. Klik aksi `Assignment Log` pada baris aset `Laptop Asus ExpertBook {runId}`
32. Verifikasi node `Canceled by [Actor]` dengan pelaku `System` dan Reason `Assignee deactivated` tampil untuk aset `Laptop Asus ExpertBook {runId}`
33. Tutup dialog `Assignment Log`
34. Ganti isi kotak search dengan `Monitor Samsung S24 {runId}`, tekan Enter
35. Klik aksi `Assignment Log` pada baris aset `Monitor Samsung S24 {runId}`
36. Verifikasi node `Canceled by [Actor]` dengan pelaku `System` dan Reason `Assignee deactivated` tampil untuk aset `Monitor Samsung S24 {runId}`
37. Tutup dialog `Assignment Log`

### Assignee dinonaktifkan: Draft tetap ada dan aset Assigned masuk daftar Unassign offboarding
38. Buka tab Drafts
39. Ketik Search `Tono Hartono {runId}`, tekan Enter
40. Klik ikon `Edit` pada baris Draft untuk Assignee `Tono Hartono {runId}`
41. Verifikasi pesan `[Name] is no longer active. Pick another assignee.` tampil dengan nama `Tono Hartono {runId}` pada Draft untuk aset `Printer Brother HL-L2375 {runId}`
42. Klik `[Cancel]` pada form Draft yang belum diubah
43. Buka daftar Unassign offboarding karyawan `Tono Hartono {runId}`
44. Verifikasi aset `Proyektor Optoma HD146X {runId}` tampil di daftar Unassign offboarding karyawan `Tono Hartono {runId}`
45. Verifikasi notifikasi pembatalan otomatis untuk ASG milik `Tono Hartono {runId}` diterima pengaju `Dewi Lestari {runId}` pada daftar notifikasinya

### PIC dinonaktifkan: baris aktif diberi No PIC dan Handover diblokir
46. Admin pengguna `Fajar Nugroho {runId}`: Nonaktifkan karyawan `Gita Maharani {runId}`
47. Buka halaman Transactions > Assignment
48. Buka tab Transactions
49. Ketik Search `Finance {runId}`, tekan Enter
50. Verifikasi baris ASG milik Assignee `Finance {runId}` memiliki penanda `No PIC`
51. Klik `⋯` pada baris ASG milik Assignee `Finance {runId}`
52. Klik `Hand Over`
53. Verifikasi pesan `Set a PIC for this division first.` tampil dan Handover tidak dapat dimulai
54. Verifikasi tombol `[Change PIC]` tampil
55. Buka halaman Transactions > Assignment
56. Buka tab Assigned Assets
57. Ketik Search `Kamera Canon M50 {runId}`, tekan Enter
58. Verifikasi baris aset `Kamera Canon M50 {runId}` tetap berstatus `Assigned`

### Akun login Assignee dicabut: Handover hanya lewat Confirm on This Device dan pengajuan baru ditolak
59. Admin pengguna `Fajar Nugroho {runId}`: Cabut akun login karyawan `Wulan Sari {runId}` tanpa menonaktifkan karyawannya
60. Aktor Assignment `Dewi Lestari {runId}`: Buka halaman Transactions > Assignment
61. Ketik Search `Wulan Sari {runId}`, tekan Enter
62. Verifikasi baris ASG milik Assignee `Wulan Sari {runId}` masih berstatus `Waiting for Handover`
63. Klik `⋯` pada baris ASG milik Assignee `Wulan Sari {runId}`
64. Klik `Hand Over`
65. Klik `[Verify Asset]`
66. Pindai TAG aset `Headset Jabra Evolve 40 {runId}`
67. Klik `[Request Confirmation]`
68. Klik `[Confirm on This Device]`
69. Centang pernyataan pada dialog `Confirm Receipt`
70. Klik `[Confirm]` pada dialog `Confirm Receipt`
71. Verifikasi baris aset `Headset Jabra Evolve 40 {runId}` berstatus `Assigned` setelah konfirmasi lewat `Confirm on This Device`
72. Klik `[+ Assign]`
73. Klik `Employee` pada overlay `Assign to`
74. Klik `[Select Assignee]`
75. Ketik Search `Wulan Sari {runId}`, tekan Enter
76. Verifikasi baris `Wulan Sari {runId}` berstatus `Blocked` dengan alasan `No login account. Only employees who can sign in can be assignees.`
77. Klik `[Cancel]` pada form yang belum diubah

### Pembuat Draft dinonaktifkan: Draft tetap ada dan dilanjutkan Aktor lain
78. Admin pengguna `Fajar Nugroho {runId}`: Nonaktifkan karyawan `Rudi Hartono {runId}`
79. Aktor Assignment `Dewi Lestari {runId}`: Buka halaman Transactions > Assignment
80. Buka tab Drafts
81. Ketik Search `Mesin Label Brother PT-P700 {runId}`, tekan Enter
82. Verifikasi baris Draft untuk aset `Mesin Label Brother PT-P700 {runId}` tetap tampil
83. Klik ikon `Edit` pada baris Draft untuk aset `Mesin Label Brother PT-P700 {runId}`
84. Verifikasi form Assignment Request mode edit terbuka dengan aset `Mesin Label Brother PT-P700 {runId}` dan Purpose `Pelabelan aset`
85. Klik `[Cancel]` pada form Draft yang belum diubah

### Transaction admin log Aktor Assignment memuat Unassign, Report Missing, Cancel Damage Report, Cancel dengan Save as draft, dan Confirm on This Device
86. Admin pengguna `Fajar Nugroho {runId}`: Buka halaman Settings > User
87. Ketik Search `Dewi Lestari {runId}`, tekan Enter
88. Buka User Detail `Dewi Lestari {runId}`
89. Buka tab `Transaction admin log`
90. Verifikasi baris Activity `Unassigned by [Receiver]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Scanner Epson DS-530 {runId}`
91. Verifikasi baris Activity `Reported missing by [Actor]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Router Mikrotik hAP ax2 {runId}`
92. Verifikasi baris Activity `Damage report canceled by [Actor]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Proyektor Epson EB-X06 {runId}`
93. Verifikasi baris Activity `Canceled by [Actor]` dengan pelaku `Dewi Lestari {runId}` dan Description `Saved as draft` tampil untuk aset `Whiteboard Magnetik {runId}`
94. Verifikasi baris Activity `Handed over by [Giver]` dengan pelaku `Dewi Lestari {runId}` tampil untuk aset `Headset Jabra Evolve 40 {runId}` dengan Description `Confirmation: Confirmed by Dewi Lestari {runId} on behalf of Wulan Sari {runId}`

### Transaction admin log Approver memuat keputusan Reject
95. Kembali ke daftar pengguna
96. Ketik Search `Anton Pratama {runId}`, tekan Enter
97. Buka User Detail `Anton Pratama {runId}`
98. Buka tab `Transaction admin log`
99. Verifikasi baris Activity `Rejected by [Approver]` dengan pelaku `Anton Pratama {runId}` tampil untuk aset `Kulkas Mini Sharp {runId}`

### Transaction admin log Total Control memuat Cancel sebagai pelaku
100. Kembali ke daftar pengguna
101. Ketik Search `Fajar Nugroho {runId}`, tekan Enter
102. Buka User Detail `Fajar Nugroho {runId}`
103. Buka tab `Transaction admin log`
104. Verifikasi baris Activity `Canceled by [Actor]` dengan pelaku `Fajar Nugroho {runId}` tampil untuk aset `Kulkas Showcase {runId}`

### Save Draft tanpa perubahan oleh Aktor lain tidak memperbarui Modified By dan Last Updated
105. Aktor Assignment `Bayu Pratama {runId}`: Buka halaman Transactions > Assignment
106. Buka tab Drafts
107. Ketik Search `Kamera Mirrorless Sony A6400 {runId}`, tekan Enter
108. Verifikasi Modified By baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}` adalah `Dewi Lestari {runId}`
109. Catat nilai Last Updated baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}`
110. Klik ikon `Edit` pada baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}`
111. Klik `[Save Draft]` tanpa mengubah isian
112. Verifikasi toast `No changes to save.`
113. Buka halaman Transactions > Assignment
114. Buka tab Drafts
115. Ketik Search `Kamera Mirrorless Sony A6400 {runId}`, tekan Enter
116. Verifikasi Modified By baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}` tetap `Dewi Lestari {runId}`
117. Verifikasi Last Updated baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}` sama dengan nilai yang dicatat

### Save Draft dengan perubahan nyata dicatat satu baris di log pelaku
118. Klik ikon `Edit` pada baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}`
119. Ganti Purpose menjadi `Dokumentasi seminar`
120. Klik `[Save Draft]`
121. Verifikasi toast `Success, assignment has been saved as draft.`
122. Buka halaman Transactions > Assignment
123. Buka tab Drafts
124. Ketik Search `Kamera Mirrorless Sony A6400 {runId}`, tekan Enter
125. Verifikasi Modified By baris Draft untuk aset `Kamera Mirrorless Sony A6400 {runId}` adalah `Bayu Pratama {runId}`
126. Admin pengguna `Fajar Nugroho {runId}`: Buka halaman Settings > User
127. Ketik Search `Bayu Pratama {runId}`, tekan Enter
128. Buka User Detail `Bayu Pratama {runId}`
129. Buka tab `Transaction admin log`
130. Verifikasi satu baris tindakan Draft edit dengan pelaku `Bayu Pratama {runId}` tampil untuk aset `Kamera Mirrorless Sony A6400 {runId}`

### Draft atas nama Assignee dinonaktifkan: pesan hilang setelah Assignee lain dipilih
131. Aktor Assignment `Dewi Lestari {runId}`: Buka halaman Transactions > Assignment
132. Buka tab Drafts
133. Ketik Search `Tono Hartono {runId}`, tekan Enter
134. Klik ikon `Edit` pada baris Draft untuk Assignee `Tono Hartono {runId}`
135. Verifikasi pesan `[Name] is no longer active. Pick another assignee.` masih tampil dengan nama `Tono Hartono {runId}`
136. Klik tombol Assignee `Tono Hartono {runId}` pada form
137. Ketik Search `Sinta Wijaya {runId}`, tekan Enter
138. Centang baris `Sinta Wijaya {runId}`
139. Klik `[Select]`
140. Verifikasi Assignee pada form adalah `Sinta Wijaya {runId}`
141. Verifikasi pesan `[Name] is no longer active. Pick another assignee.` tidak tampil
142. Klik `[Save Draft]`
143. Verifikasi toast `Success, assignment has been saved as draft.`
144. Buka halaman Transactions > Assignment
145. Buka tab Drafts
146. Ketik Search `Sinta Wijaya {runId}`, tekan Enter
147. Verifikasi baris Draft untuk aset `Printer Brother HL-L2375 {runId}` memiliki Assignee `Sinta Wijaya {runId}`

### Assignee dinonaktifkan: notifikasi dialihkan juga ke Aktor Assignment Group aset
148. Aktor Assignment `Bayu Pratama {runId}`: Buka daftar notifikasi
149. Verifikasi notifikasi pembatalan otomatis untuk ASG milik `Tono Hartono {runId}` diterima `Bayu Pratama {runId}` sebagai Aktor Assignment Group aset `Head Office`

### Akun login PIC Division dicabut: baris aktif tetap dan Handover hanya lewat Confirm on This Device
150. Admin pengguna `Fajar Nugroho {runId}`: Cabut akun login karyawan `Hendra Saputra {runId}` tanpa menonaktifkan karyawannya
151. Aktor Assignment `Dewi Lestari {runId}`: Buka halaman Transactions > Assignment
152. Buka tab Transactions
153. Ketik Search `Operations {runId}`, tekan Enter
154. Verifikasi baris ASG milik Assignee `Operations {runId}` masih berstatus `Waiting for Handover`
155. Klik `⋯` pada baris ASG milik Assignee `Operations {runId}`
156. Klik `Hand Over`
157. Klik `[Verify Asset]`
158. Pindai TAG aset `Genset Honda EU22i {runId}`
159. Klik `[Request Confirmation]`
160. Klik `[Confirm on This Device]`
161. Centang pernyataan pada dialog `Confirm Receipt`
162. Klik `[Confirm]` pada dialog `Confirm Receipt`
163. Verifikasi baris aset `Genset Honda EU22i {runId}` berstatus `Assigned` setelah konfirmasi lewat `Confirm on This Device`

### Pengajuan baru untuk PIC Division yang akunnya dicabut ditolak
164. Klik `[+ Assign]`
165. Klik `Employee` pada overlay `Assign to`
166. Klik `[Select Assignee]`
167. Ketik Search `Hendra Saputra {runId}`, tekan Enter
168. Verifikasi baris `Hendra Saputra {runId}` berstatus `Blocked` dengan alasan `No login account. Only employees who can sign in can be assignees.`
169. Klik `[Cancel]` pada form yang belum diubah
