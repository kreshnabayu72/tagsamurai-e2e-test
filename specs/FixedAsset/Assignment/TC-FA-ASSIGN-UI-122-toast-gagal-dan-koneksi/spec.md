---
id: TC-FA-ASSIGN-UI-122-toast-gagal-dan-koneksi
title: "Toast gagal server, gangguan jaringan, dan reaksi atas respons gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["TS-ASG-26", "TS-ASG-27", "EB-ERR-1@submit-assignment", "EB-ERR-1@save-draft", "EB-ERR-1@cancel-assignment", "EB-ERR-1@handover", "EB-ERR-1@unassign", "EB-ERR-1@change-pic", "EB-ERR-1@keputusan-approval", "EB-FB-4", "EB-DL-5", "EB-DL-2@tabel-transactions"]
smoke: []
dependsOn: []
trace:
  "TS-ASG-26": [4, 21, 37, 52, 66, 83, 102, 151, 155]
  "TS-ASG-27": [13, 28, 45, 59, 73, 93, 111]
  "EB-ERR-1@submit-assignment": [4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 18]
  "EB-ERR-1@save-draft": [21, 22, 23, 24, 25, 28, 29, 30, 32]
  "EB-ERR-1@cancel-assignment": [37, 38, 39, 40, 45, 46, 47, 49]
  "EB-ERR-1@handover": [52, 53, 54, 55, 56, 59, 60, 61, 63]
  "EB-ERR-1@unassign": [66, 67, 68, 69, 70, 73, 74, 75, 77]
  "EB-ERR-1@change-pic": [83, 84, 85, 86, 87, 93, 94, 95, 98]
  "EB-ERR-1@keputusan-approval": [102, 103, 104, 105, 107, 111, 112, 113, 115, 118]
  "EB-FB-4": [121, 123, 126, 128, 130]
  "EB-DL-5": [134, 136, 137]
  "EB-DL-2@tabel-transactions": [141, 145]
coverage:
  web: automated
---

# Toast gagal server, gangguan jaringan, dan reaksi atas respons gagal

## Prerequisites
- Aktor: Aktor Assignment; Approver untuk K13, K14, dan K20 (halaman Review Approval).
- Layar awal: Transactions > Assignment, sesuai kondisi; Approvals > Assignment > Active > Review untuk K13, K14, dan K20.
- Komponen: Toast Assignment
- Data:
  - DU-122-1: Form Assignment Request Assignee Type `Employee`, Assignee `Budi S`, Note `Penugasan laptop untuk survei lapangan`, Asset Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Purpose `Survei lapangan`.
  - DU-122-2: Assignment Transaction ID `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-122-3: Handover Transaction ID `ASG-2026-0071`, Assignee `Budi S`, Asset Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Verification `Verified`, Confirmation `No`.
  - DU-122-4: Unassign Assignee `Budi S`, Asset Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Transaction ID `ASG-2026-0041`, Verification `Verified`, Unassign Photo `unassign-laptop-dell-5420-4.jpg`.
  - DU-122-5: Change PIC Transaction ID `ASG-2026-0072`, Status `Waiting for Handover + No PIC`, Group `Branch Surabaya`, Assignee `Field Survey`, Assignee Type `Division`, Total Asset `2`, Requested By `Agus P`, Request Date `2026-11-10 10:15 WIB`, Last Updated `2026-11-11 08:00 WIB`, PIC baru `Rina Wijaya`.
  - DU-122-6: Review Approval Transaction ID `ASG-2026-0070`, Assignee `Sari D`, Asset Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Decision `Approve`.
  - DU-122-7: Assignment (5001 baris dengan pola `{n}`) Transaction ID `ASG-2026-{n}`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `1`, Requested By `Rina W`, Request Date `2026-11-02 08:30 WIB`, Last Updated `2026-11-03 10:00 WIB`.
  - DU-122-8: Assignment Transaction ID `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-122-9: Review Approval Transaction ID `ASG-2026-0070`, Assignee `Sari D`, Asset Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Decision `Reject`, Approval Note `Aset belum dibutuhkan bulan ini`.
- Kondisi:
  - K1: form Assignment Request untuk DU-122-1 siap dipakai, dan Submit Assignment dijawab error server 5xx.
  - K2: form Assignment Request untuk DU-122-1 siap dipakai, Submit Assignment pertama tidak dijawab sampai batas waktu (timeout), dan Submit Assignment berikutnya dijawab sukses dengan seluruh aset menunggu approval dari lebih dari satu penerima approval.
  - K3: form Assignment Request untuk DU-122-1 siap dipakai, dan Save Draft dijawab error server 5xx.
  - K4: form Assignment Request untuk DU-122-1 siap dipakai, Save Draft pertama tidak dijawab sampai batas waktu (timeout), dan Save Draft berikutnya dijawab sukses.
  - K5: dialog Cancel Assignment untuk DU-122-2 siap dipakai, dan Cancel Assignment dijawab error server 5xx.
  - K6: dialog Cancel Assignment untuk DU-122-2 siap dipakai, Cancel Assignment pertama tidak dijawab sampai batas waktu (timeout), dan Cancel Assignment berikutnya dijawab sukses.
  - K7: halaman Handover untuk DU-122-3 siap dipakai dengan aset terverifikasi dan Confirmation `No`, sehingga `[Complete Handover]` tersedia, dan Handover dijawab error server 5xx.
  - K8: halaman Handover untuk DU-122-3 siap dipakai dengan aset terverifikasi dan Confirmation `No`, sehingga `[Complete Handover]` tersedia, Handover pertama tidak dijawab sampai batas waktu (timeout), dan Handover berikutnya dijawab sukses.
  - K9: halaman Unassign untuk DU-122-4 siap dipakai dengan aset terverifikasi dan Unassign Photo terisi, dan Unassign dijawab error server 5xx.
  - K10: halaman Unassign untuk DU-122-4 siap dipakai dengan aset terverifikasi dan Unassign Photo terisi, Unassign pertama tidak dijawab sampai batas waktu (timeout), dan Unassign berikutnya dijawab sukses.
  - K11: dialog Select User untuk DU-122-5 siap dipakai, dan Change PIC dijawab error server 5xx.
  - K12: dialog Select User untuk DU-122-5 siap dipakai, Change PIC pertama tidak dijawab sampai batas waktu (timeout), dan Change PIC berikutnya dijawab sukses.
  - K13: dialog Submit Approval untuk DU-122-6 siap dipakai, dan Submit Approval dijawab error server 5xx.
  - K14: dialog Submit Approval untuk DU-122-6 siap dipakai, Submit Approval pertama tidak dijawab sampai batas waktu (timeout), dan Submit Approval berikutnya dijawab sukses dengan keputusan ini menjadi keputusan terakhir yang dibutuhkan sehingga pengajuan disetujui seluruhnya.
  - K15: form Assignment Request untuk DU-122-1 siap dipakai, dan Save Draft dijawab sukses.
  - K16: form Assignment Request untuk DU-122-1 siap dipakai, dan Save Draft dijawab error server 5xx.
  - K17: daftar Tabel Transactions berisi DU-122-7, sehingga jumlah baris di atas ambang `5.000`, dan berkas Download belum siap.
  - K18: daftar Tabel Transactions berisi DU-122-8, dan Download dijawab error server 5xx.
  - K19: daftar Tabel Transactions berisi DU-122-8, dan Download tidak dijawab sampai batas waktu (timeout).
  - K20: halaman Review Approval untuk DU-122-9 siap dipakai, dan Submit Approval dijawab error server 5xx.
  - K21: daftar Tabel Transactions berisi DU-122-8, dan Remind Assignee dijawab error server 5xx.

## Test Steps

### Submit Assignment gagal dengan error server 5xx
1. Tampilkan Toast Assignment dengan kondisi K1
2. Klik `[Submit]`
3. Klik `[Submit]` pada dialog `Submit Assignment`
4. Verifikasi toast `Error, failed to submit assignment.` tampil
5. Verifikasi toast tidak memuat tombol `[Try Again]`
6. Verifikasi form Assignment Request tetap terbuka
7. Verifikasi dialog `Submit Assignment` tetap terbuka
8. Verifikasi Assignee `Budi S` tetap terisi pada form
9. Verifikasi tombol `[Submit]` pada dialog `Submit Assignment` aktif kembali

### Submit Assignment gagal karena timeout lalu diulang
10. Tampilkan Toast Assignment dengan kondisi K2
11. Klik `[Submit]`
12. Klik `[Submit]` pada dialog `Submit Assignment`
13. Verifikasi toast `Connection problem. Please try again.` tampil
14. Verifikasi form Assignment Request tetap terbuka
15. Verifikasi dialog `Submit Assignment` tetap terbuka
16. Verifikasi tombol `[Submit]` pada dialog `Submit Assignment` aktif kembali
17. Klik `[Submit]` pada dialog `Submit Assignment`
18. Verifikasi toast `Success, assignment has been submitted for approval.` tampil

### Save Draft gagal dengan error server 5xx
19. Tampilkan Toast Assignment dengan kondisi K3
20. Klik `[Save Draft]`
21. Verifikasi toast `Error, failed to save draft.` tampil
22. Verifikasi toast tidak memuat tombol `[Try Again]`
23. Verifikasi form Assignment Request tetap terbuka
24. Verifikasi Note `Penugasan laptop untuk survei lapangan` tetap terisi pada form
25. Verifikasi tombol `[Save Draft]` aktif kembali

### Save Draft gagal karena timeout lalu diulang
26. Tampilkan Toast Assignment dengan kondisi K4
27. Klik `[Save Draft]`
28. Verifikasi toast `Connection problem. Please try again.` tampil
29. Verifikasi form Assignment Request tetap terbuka
30. Verifikasi tombol `[Save Draft]` aktif kembali
31. Klik `[Save Draft]`
32. Verifikasi toast `Success, assignment has been saved as draft.` tampil

### Cancel Assignment gagal dengan error server 5xx
33. Tampilkan Toast Assignment dengan kondisi K5
34. Klik `⋯` pada baris `ASG-2026-0071`
35. Klik `Cancel Assignment`
36. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
37. Verifikasi toast `Error, failed to cancel assignment.` tampil
38. Verifikasi toast tidak memuat tombol `[Try Again]`
39. Verifikasi dialog `Cancel Assignment` tetap terbuka
40. Verifikasi tombol `[Cancel Assignment]` aktif kembali

### Cancel Assignment gagal karena timeout lalu diulang
41. Tampilkan Toast Assignment dengan kondisi K6
42. Klik `⋯` pada baris `ASG-2026-0071`
43. Klik `Cancel Assignment`
44. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
45. Verifikasi toast `Connection problem. Please try again.` tampil
46. Verifikasi dialog `Cancel Assignment` tetap terbuka
47. Verifikasi tombol `[Cancel Assignment]` aktif kembali
48. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
49. Verifikasi toast `Success, assignment has been canceled.` tampil

### Handover gagal dengan error server 5xx
50. Tampilkan Toast Assignment dengan kondisi K7
51. Klik `[Complete Handover]`
52. Verifikasi toast `Error, failed to hand over assets.` tampil
53. Verifikasi toast tidak memuat tombol `[Try Again]`
54. Verifikasi halaman Handover tetap terbuka
55. Verifikasi aset `Laptop Dell Latitude 5420 - 4` tetap tampil pada daftar aset Handover
56. Verifikasi tombol `[Complete Handover]` aktif kembali

### Handover gagal karena timeout lalu diulang
57. Tampilkan Toast Assignment dengan kondisi K8
58. Klik `[Complete Handover]`
59. Verifikasi toast `Connection problem. Please try again.` tampil
60. Verifikasi halaman Handover tetap terbuka
61. Verifikasi tombol `[Complete Handover]` aktif kembali
62. Klik `[Complete Handover]`
63. Verifikasi toast `Success, 1 asset has been assigned to Budi S.` tampil

### Unassign gagal dengan error server 5xx
64. Tampilkan Toast Assignment dengan kondisi K9
65. Klik `[Submit]`
66. Verifikasi toast `Error, failed to unassign assets.` tampil
67. Verifikasi toast tidak memuat tombol `[Try Again]`
68. Verifikasi halaman Unassign tetap terbuka
69. Verifikasi aset `Laptop Dell Latitude 5420 - 4` tetap tampil pada daftar aset Unassign
70. Verifikasi tombol `[Submit]` aktif kembali

### Unassign gagal karena timeout lalu diulang
71. Tampilkan Toast Assignment dengan kondisi K10
72. Klik `[Submit]`
73. Verifikasi toast `Connection problem. Please try again.` tampil
74. Verifikasi halaman Unassign tetap terbuka
75. Verifikasi tombol `[Submit]` aktif kembali
76. Klik `[Submit]`
77. Verifikasi toast `Success, 1 asset has been unassigned.` tampil

### Change PIC gagal dengan error server 5xx
78. Tampilkan Toast Assignment dengan kondisi K11
79. Klik `⋯` pada baris `ASG-2026-0072`
80. Klik `Change PIC`
81. Pilih user `Rina Wijaya`
82. Klik `[Select]`
83. Verifikasi toast `Error, failed to change PIC.` tampil
84. Verifikasi toast tidak memuat tombol `[Try Again]`
85. Verifikasi dialog `Select User` tetap terbuka
86. Verifikasi user `Rina Wijaya` tetap terpilih
87. Verifikasi tombol `[Select]` aktif kembali

### Change PIC gagal karena timeout lalu diulang
88. Tampilkan Toast Assignment dengan kondisi K12
89. Klik `⋯` pada baris `ASG-2026-0072`
90. Klik `Change PIC`
91. Pilih user `Rina Wijaya`
92. Klik `[Select]`
93. Verifikasi toast `Connection problem. Please try again.` tampil
94. Verifikasi dialog `Select User` tetap terbuka
95. Verifikasi tombol `[Select]` aktif kembali
96. Pilih user `Rina Wijaya`
97. Klik `[Select]`
98. Verifikasi toast `Success, PIC has been changed to Rina Wijaya.` tampil

### Submit Approval gagal dengan error server 5xx
99. Tampilkan Toast Assignment dengan kondisi K13
100. Klik `[Submit]`
101. Klik `[Submit]` pada dialog `Submit Approval`
102. Verifikasi toast `Error, failed to approve assignment.` tampil
103. Verifikasi toast tidak memuat tombol `[Try Again]`
104. Verifikasi dialog `Submit Approval` tetap terbuka
105. Verifikasi tombol `[Submit]` pada dialog `Submit Approval` aktif kembali
106. Klik `[Cancel]` pada dialog `Submit Approval`
107. Verifikasi keputusan `Approve` pada aset `Laptop Dell Latitude 5420 - 10` masih terpilih pada halaman Review

### Submit Approval gagal karena timeout lalu diulang
108. Tampilkan Toast Assignment dengan kondisi K14
109. Klik `[Submit]`
110. Klik `[Submit]` pada dialog `Submit Approval`
111. Verifikasi toast `Connection problem. Please try again.` tampil
112. Verifikasi dialog `Submit Approval` tetap terbuka
113. Verifikasi tombol `[Submit]` pada dialog `Submit Approval` aktif kembali
114. Klik `[Cancel]` pada dialog `Submit Approval`
115. Verifikasi keputusan `Approve` pada aset `Laptop Dell Latitude 5420 - 10` masih terpilih pada halaman Review
116. Klik `[Submit]`
117. Klik `[Submit]` pada dialog `Submit Approval`
118. Verifikasi toast `Success, assignment has been approved.` tampil

### Toast sukses hilang sendiri
119. Tampilkan Toast Assignment dengan kondisi K15
120. Klik `[Save Draft]`
121. Verifikasi toast `Success, assignment has been saved as draft.` tampil
122. Waktu berlalu sampai 5 detik sejak toast tampil
123. Verifikasi toast `Success, assignment has been saved as draft.` tidak tampil

### Toast error bertahan sampai ditutup
124. Tampilkan Toast Assignment dengan kondisi K16
125. Klik `[Save Draft]`
126. Verifikasi toast `Error, failed to save draft.` tampil
127. Waktu berlalu sampai 30 detik sejak toast tampil
128. Verifikasi toast `Error, failed to save draft.` masih tampil
129. Klik tombol tutup pada toast
130. Verifikasi toast `Error, failed to save draft.` tidak tampil

### Download di atas ambang memakai loading screen
131. Tampilkan Toast Assignment dengan kondisi K17
132. Klik `Download`
133. Klik `Download as CSV`
134. Verifikasi loading screen tampil
135. Berkas Download siap
136. Verifikasi berkas langsung terunduh
137. Verifikasi tidak ada toast informasional yang tampil

### Download gagal dengan error server 5xx
138. Tampilkan Toast Assignment dengan kondisi K18
139. Klik `Download`
140. Klik `Download as CSV`
141. Verifikasi toast `Error, failed to download Assignment-Transactions.` tampil

### Download gagal karena timeout
142. Tampilkan Toast Assignment dengan kondisi K19
143. Klik `Download`
144. Klik `Download as XLSX`
145. Verifikasi toast `Error, failed to download Assignment-Transactions.` tampil

### Reject keputusan gagal dengan error server 5xx
146. Tampilkan Toast Assignment dengan kondisi K20
147. Ubah keputusan pada aset `Laptop Dell Latitude 5420 - 10` menjadi `Reject`
148. Isi Approval Note `Aset belum dibutuhkan bulan ini`
149. Klik `[Submit]`
150. Klik `[Submit]` pada dialog `Submit Approval`
151. Verifikasi toast `Error, failed to reject assignment.` tampil

### Remind Assignee gagal dengan error server 5xx
152. Tampilkan Toast Assignment dengan kondisi K21
153. Klik `⋯` pada baris `ASG-2026-0071`
154. Klik `Remind Assignee`
155. Verifikasi toast error `Error, failed to remind [item].` tampil, dengan `[item]` nama entitas huruf kecil


