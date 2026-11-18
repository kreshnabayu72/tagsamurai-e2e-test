---
id: TC-FA-BORROW-E2E-020-approval-review-mode-all-dua-approver
title: "Approval mode Any one dan All antar dua approver menentukan hasil aset dan tampilan Review approver lain"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["EC-BRW-105", "EC-BRW-106", "EC-BRW-11", "EC-BRW-115", "EC-BRW-12", "F-BORROW-04.k6", "F-BORROW-04.k7", "FI-BRW-207", "FI-BRW-208", "FI-BRW-209", "FI-BRW-210"]
smoke: []
dependsOn: []
trace:
  "EC-BRW-105": 48
  "EC-BRW-106": [87, 96]
  "EC-BRW-11": [15, 20, 38]
  "EC-BRW-115": [64, 67, 70, 79]
  "EC-BRW-12": [125, 134]
  "F-BORROW-04.k6": [15, 20, 38, 48]
  "F-BORROW-04.k7": [64, 70, 79, 96, 125, 134]
  "FI-BRW-207": [37, 46]
  "FI-BRW-208": [94, 104, 111]
  "FI-BRW-209": [63, 77]
  "FI-BRW-210": [32, 33]
anchor: []
coverage:
  web: automated
---

# Approval mode Any one dan All antar dua approver menentukan hasil aset dan tampilan Review approver lain

## Prerequisites
- Aktor: Rina W, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`; dan `Wawan Setiawan {runId}`, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`. Keduanya bekerja bersamaan pada pengajuan yang sama.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-020-11: user `Wawan Setiawan {runId}`, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`.
  - DU-020-1: pengajuan `Borrow` Group `Head Office`, Borrower `Citra Lestari {runId}`, Requested By `Agus Pratama {runId}`, Total Asset `1`, menunggu approval Rina W dan `Wawan Setiawan {runId}`. Asetnya DU-020-2: `Laptop Lenovo ThinkPad {runId}`, Duration `3 / 5 days`, mode Any one approver (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-020-3: pengajuan `Borrow` Group `Head Office`, Borrower `Dimas Prakoso {runId}`, Requested By `Agus Pratama {runId}`, Total Asset `1`. Asetnya DU-020-4: `Printer Canon {runId}`, Duration `2 / 5 days`, mode Any one approver (Rina W dan `Wawan Setiawan {runId}`).
  - DU-020-5: pengajuan `Borrow` Group `Head Office`, Borrower `Eka Wijaya {runId}`, Requested By `Agus Pratama {runId}`, Total Asset `1`. Asetnya DU-020-6: `Scanner Epson {runId}`, Duration `3 / 7 days`, mode All approvers (Rina W dan `Wawan Setiawan {runId}`), belum ada keputusan.
  - DU-020-7: pengajuan `Borrow` Group `Head Office`, Borrower `Fajar Nugroho {runId}`, Requested By `Agus Pratama {runId}`, Total Asset `1`. Asetnya DU-020-8: `Monitor LG {runId}`, Duration `2 / 7 days`, mode All approvers (Rina W dan `Wawan Setiawan {runId}`), belum ada keputusan.
  - DU-020-9: pengajuan `Borrow` Group `Head Office`, Borrower `Gita Ramadhani {runId}`, Requested By `Agus Pratama {runId}`, Total Asset `1`. Asetnya DU-020-10: `Tablet Samsung {runId}`, Duration `3 / 7 days`, mode All approvers (Rina W dan `Wawan Setiawan {runId}`), belum ada keputusan, dan batas Transaction timeout baris itu sudah terlewati saat job Transaction timeout berjalan.

## Test Steps

### Dua approver mengirim keputusan Any one bersamaan: satu keputusan final
1. Rina W: Klik `Approvals` pada sidebar
2. Rina W: Klik `Borrow`
3. Rina W: Ketik Search `Citra Lestari {runId}`, tekan Enter
4. Rina W: Klik menu ⋯ pada baris DU-020-1
5. Rina W: Klik `Review`
6. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
7. Wawan Setiawan {runId}: Klik `Borrow`
8. Wawan Setiawan {runId}: Ketik Search `Citra Lestari {runId}`, tekan Enter
9. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-1
10. Wawan Setiawan {runId}: Klik `Review`
11. Rina W: Klik `[Submit]`
12. Wawan Setiawan {runId}: Klik `[Submit]`
13. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
14. Wawan Setiawan {runId}: Klik `[Submit]` pada dialog `Submit Approval`
15. Verifikasi tepat satu dari Rina W dan Wawan Setiawan {runId} menerima dialog `Approval cannot be made` dengan teks `You can no longer approve this request because it has already been done by another approver.`
16. Rina W: Klik tab `History`
17. Rina W: Ketik Search `Citra Lestari {runId}`, tekan Enter
18. Wawan Setiawan {runId}: Klik tab `History`
19. Wawan Setiawan {runId}: Ketik Search `Citra Lestari {runId}`, tekan Enter
20. Verifikasi baris DU-020-1 tampil di tab `History` tepat satu dari Rina W dan Wawan Setiawan {runId}, sehingga aset DU-020-2 hanya memiliki satu keputusan final

### Rina W memutuskan aset Any one lebih dulu saat Review Wawan terbuka
21. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
22. Wawan Setiawan {runId}: Klik `Borrow`
23. Wawan Setiawan {runId}: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
24. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-3
25. Wawan Setiawan {runId}: Klik `Review`
26. Rina W: Klik `Approvals` pada sidebar
27. Rina W: Klik `Borrow`
28. Rina W: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
29. Rina W: Klik menu ⋯ pada baris DU-020-3
30. Rina W: Klik `Review`
31. Rina W: Isi Approve Duration baris DU-020-4 dengan `3`
32. Verifikasi caption `Max. 2 days` tampil di bawah input Approve Duration baris DU-020-4 sehingga durasi tidak dapat ditambah
33. Verifikasi baris DU-020-4 tidak memiliki kontrol untuk mengganti aset
34. Rina W: Isi Approve Duration baris DU-020-4 dengan `1`
35. Rina W: Klik `[Submit]`
36. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
37. Verifikasi Rina W menerima toast `Success, borrow has been approved.`
38. Verifikasi Wawan Setiawan {runId} menerima dialog `Approval cannot be made` dengan teks `You can no longer approve this request because it has already been done by another approver.` tanpa menunggu `[Submit]`
39. Wawan Setiawan {runId}: Klik `[OK]`
40. Rina W: Klik `Approvals` pada sidebar
41. Rina W: Klik `Borrow`
42. Rina W: Klik tab `History`
43. Rina W: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
44. Rina W: Klik menu ⋯ pada baris DU-020-3
45. Rina W: Klik `Detail`
46. Verifikasi keputusan aset DU-020-4 `Approved` pada halaman Detail read-only tanpa kontrol keputusan yang dapat diubah
47. Rina W: Klik sel `Approval Rule` aset DU-020-4
48. Verifikasi dialog `Approval Progress` menampilkan Rina W `Approved` dan Wawan Setiawan {runId} `Not Involved`

### Rina W me-Reject aset All saat Review Wawan terbuka dan sudah diisi Approve
49. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
50. Wawan Setiawan {runId}: Klik `Borrow`
51. Wawan Setiawan {runId}: Ketik Search `Eka Wijaya {runId}`, tekan Enter
52. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-5
53. Wawan Setiawan {runId}: Klik `Review`
54. Rina W: Klik `Approvals` pada sidebar
55. Rina W: Klik `Borrow`
56. Rina W: Ketik Search `Eka Wijaya {runId}`, tekan Enter
57. Rina W: Klik menu ⋯ pada baris DU-020-5
58. Rina W: Klik `Review`
59. Rina W: Ubah toggle Approval baris DU-020-6 menjadi `Reject`
60. Rina W: Isi Approval Note baris DU-020-6 dengan `Scanner dipakai kegiatan lain`
61. Rina W: Klik `[Submit]`
62. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
63. Verifikasi Rina W menerima toast `Success, borrow has been rejected.`
64. Verifikasi Wawan Setiawan {runId} menerima dialog `Approval cannot be made` dengan teks `You can no longer approve this request because it has already been done by another approver.` tanpa menunggu `[Submit]`
65. Wawan Setiawan {runId}: Klik `[OK]`
66. Wawan Setiawan {runId}: Ketik Search `Eka Wijaya {runId}`, tekan Enter
67. Verifikasi tabel Active Wawan Setiawan {runId} menampilkan `No results found`
68. Wawan Setiawan {runId}: Klik tab `History`
69. Wawan Setiawan {runId}: Ketik Search `Eka Wijaya {runId}`, tekan Enter
70. Verifikasi tabel History Wawan Setiawan {runId} menampilkan `No results found` sehingga keputusan yang belum dikirim tidak tersimpan
71. Rina W: Klik `Approvals` pada sidebar
72. Rina W: Klik `Borrow`
73. Rina W: Klik tab `History`
74. Rina W: Ketik Search `Eka Wijaya {runId}`, tekan Enter
75. Rina W: Klik menu ⋯ pada baris DU-020-5
76. Rina W: Klik `Detail`
77. Verifikasi keputusan aset DU-020-6 `Rejected` karena satu penolakan
78. Rina W: Klik sel `Approval Rule` aset DU-020-6
79. Verifikasi dialog `Approval Progress` menampilkan Rina W `Rejected` dan Wawan Setiawan {runId} `Not Involved`

### Aset All menjadi Approved hanya bila kedua approver menyetujui
80. Rina W: Klik `Approvals` pada sidebar
81. Rina W: Klik `Borrow`
82. Rina W: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
83. Rina W: Klik menu ⋯ pada baris DU-020-7
84. Rina W: Klik `Review`
85. Rina W: Klik `[Submit]`
86. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
87. Verifikasi Rina W menerima toast `Success, your approval has been recorded. Waiting for the other approvers.`
88. Rina W: Klik `Approvals` pada sidebar
89. Rina W: Klik `Borrow`
90. Rina W: Klik tab `History`
91. Rina W: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
92. Rina W: Klik menu ⋯ pada baris DU-020-7
93. Rina W: Klik `Detail`
94. Verifikasi kolom Approval Rule aset DU-020-8 `All approvers · 1 of 2 approved` dan keputusannya `Waiting`, bukan `Approved`
95. Rina W: Klik sel `Approval Rule` aset DU-020-8
96. Verifikasi dialog `Approval Progress` menampilkan Rina W `Approved` dan Wawan Setiawan {runId} `Waiting for Approval`
97. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
98. Wawan Setiawan {runId}: Klik `Borrow`
99. Wawan Setiawan {runId}: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
100. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-7
101. Wawan Setiawan {runId}: Klik `Review`
102. Wawan Setiawan {runId}: Klik `[Submit]`
103. Wawan Setiawan {runId}: Klik `[Submit]` pada dialog `Submit Approval`
104. Verifikasi Wawan Setiawan {runId} menerima toast `Success, borrow has been approved.`
105. Rina W: Klik `Approvals` pada sidebar
106. Rina W: Klik `Borrow`
107. Rina W: Klik tab `History`
108. Rina W: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
109. Rina W: Klik menu ⋯ pada baris DU-020-7
110. Rina W: Klik `Detail`
111. Verifikasi keputusan aset DU-020-8 `Approved` karena semua approver menyetujui

### Aset All yang tidak diputuskan salah satu approver ditutup oleh timeout
112. Rina W: Klik `Approvals` pada sidebar
113. Rina W: Klik `Borrow`
114. Rina W: Ketik Search `Gita Ramadhani {runId}`, tekan Enter
115. Rina W: Klik menu ⋯ pada baris DU-020-9
116. Rina W: Klik `Review`
117. Rina W: Klik `[Submit]`
118. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
119. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
120. Wawan Setiawan {runId}: Klik `Borrow`
121. Wawan Setiawan {runId}: Ketik Search `Gita Ramadhani {runId}`, tekan Enter
122. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-9
123. Wawan Setiawan {runId}: Klik `Review`
124. Job Transaction timeout berjalan sesudah batas Transaction timeout baris DU-020-10 terlewati
125. Verifikasi Wawan Setiawan {runId} menerima dialog `Borrow Canceled` dengan teks `This borrow was canceled automatically (Timed out (Waiting for Approval)).`
126. Wawan Setiawan {runId}: Klik `[OK]`
127. Rina W: Klik `Approvals` pada sidebar
128. Rina W: Klik `Borrow`
129. Rina W: Klik tab `History`
130. Rina W: Ketik Search `Gita Ramadhani {runId}`, tekan Enter
131. Rina W: Klik menu ⋯ pada baris DU-020-9
132. Rina W: Klik `Detail`
133. Rina W: Klik sel `Approval Rule` aset DU-020-10
134. Verifikasi dialog `Approval Progress` menampilkan Rina W `Approved` dengan waktu keputusannya dan Wawan Setiawan {runId} `Not Involved` dengan keterangan `Canceled by system`
