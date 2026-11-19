---
id: TC-FA-BORROW-E2E-020-approval-review-mode-all-dua-approver
title: "Approval mode Any one dan All antar dua approver menentukan hasil aset dan tampilan Review approver lain"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-BRW-105", "EC-BRW-106", "EC-BRW-11", "EC-BRW-115", "EC-BRW-12", "F-BORROW-04.k6", "F-BORROW-04.k7", "FI-BRW-207", "FI-BRW-208", "FI-BRW-209", "FI-BRW-210"]
smoke: []
dependsOn: []
trace:
  "EC-BRW-105": 51
  "EC-BRW-106": [93, 102]
  "EC-BRW-11": [14, 15, 17, 22, 40, 42]
  "EC-BRW-115": [69, 71, 73, 76, 85]
  "EC-BRW-12": [131, 140]
  "F-BORROW-04.k6": [14, 15, 17, 22, 40, 51]
  "F-BORROW-04.k7": [69, 76, 85, 102, 131, 140]
  "FI-BRW-207": [39, 49]
  "FI-BRW-208": [100, 110, 117]
  "FI-BRW-209": [68, 83]
  "FI-BRW-210": [34, 35]
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
14. Verifikasi Rina W menerima toast `Success, borrow has been approved.`
15. Verifikasi Wawan Setiawan {runId} menerima dialog `Approval cannot be made` dengan teks `You can no longer approve this request because it has already been done by another approver.` pada Review yang sedang terbuka, karena keputusan Rina W dikomit server lebih dulu
16. Wawan Setiawan {runId}: Klik `[OK]`
17. Verifikasi Wawan Setiawan {runId} kembali ke halaman `Approvals > Borrow` sesudah `[OK]`
18. Rina W: Klik tab `History`
19. Rina W: Ketik Search `Citra Lestari {runId}`, tekan Enter
20. Wawan Setiawan {runId}: Klik tab `History`
21. Wawan Setiawan {runId}: Ketik Search `Citra Lestari {runId}`, tekan Enter
22. Verifikasi baris DU-020-1 tampil di tab `History` Rina W dan tidak tampil di tab `History` Wawan Setiawan {runId}, sehingga aset DU-020-2 hanya memiliki satu keputusan final

### Rina W memutuskan aset Any one lebih dulu saat Review Wawan terbuka
23. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
24. Wawan Setiawan {runId}: Klik `Borrow`
25. Wawan Setiawan {runId}: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
26. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-3
27. Wawan Setiawan {runId}: Klik `Review`
28. Rina W: Klik `Approvals` pada sidebar
29. Rina W: Klik `Borrow`
30. Rina W: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
31. Rina W: Klik menu ⋯ pada baris DU-020-3
32. Rina W: Klik `Review`
33. Rina W: Isi Approve Duration baris DU-020-4 dengan `3`
34. Verifikasi Approve Duration baris DU-020-4 menjadi `2`, dijepit ke durasi yang diminta, tanpa pesan di bawah input, sehingga durasi tidak dapat ditambah[^drift-1]
35. Verifikasi baris DU-020-4 tidak memiliki kontrol untuk mengganti aset
36. Rina W: Isi Approve Duration baris DU-020-4 dengan `1`
37. Rina W: Klik `[Submit]`
38. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
39. Verifikasi Rina W menerima toast `Success, borrow has been approved.`
40. Verifikasi Wawan Setiawan {runId} menerima dialog `Approval cannot be made` dengan teks `You can no longer approve this request because it has already been done by another approver.` tanpa menunggu `[Submit]`
41. Wawan Setiawan {runId}: Klik `[OK]`
42. Verifikasi Wawan Setiawan {runId} kembali ke halaman `Approvals > Borrow` sesudah `[OK]`
43. Rina W: Klik `Approvals` pada sidebar
44. Rina W: Klik `Borrow`
45. Rina W: Klik tab `History`
46. Rina W: Ketik Search `Dimas Prakoso {runId}`, tekan Enter
47. Rina W: Klik menu ⋯ pada baris DU-020-3
48. Rina W: Klik `Detail`
49. Verifikasi keputusan aset DU-020-4 `Approved` pada halaman Detail read-only tanpa kontrol keputusan yang dapat diubah
50. Rina W: Klik sel `Approval Rule` aset DU-020-4
51. Verifikasi dialog `Approval Progress` berjudul `Approval Progress` dengan identitas berlabel `Asset` bernilai `Printer Canon {runId}` di bawah judul, hanya memuat bagian Approval Progress, dan menampilkan Rina W `Approved` dan Wawan Setiawan {runId} `Not Involved`

### Rina W me-Reject aset All saat Review Wawan terbuka dan sudah diisi Approve
52. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
53. Wawan Setiawan {runId}: Klik `Borrow`
54. Wawan Setiawan {runId}: Ketik Search `Eka Wijaya {runId}`, tekan Enter
55. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-5
56. Wawan Setiawan {runId}: Klik `Review`
57. Wawan Setiawan {runId}: Isi Approve Duration baris DU-020-6 dengan `2`
58. Wawan Setiawan {runId}: Isi Approval Note baris DU-020-6 dengan `Scanner siap dipakai`
59. Rina W: Klik `Approvals` pada sidebar
60. Rina W: Klik `Borrow`
61. Rina W: Ketik Search `Eka Wijaya {runId}`, tekan Enter
62. Rina W: Klik menu ⋯ pada baris DU-020-5
63. Rina W: Klik `Review`
64. Rina W: Ubah toggle Approval baris DU-020-6 menjadi `Reject`
65. Rina W: Isi Approval Note baris DU-020-6 dengan `Scanner dipakai kegiatan lain`
66. Rina W: Klik `[Submit]`
67. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
68. Verifikasi Rina W menerima toast `Success, borrow has been rejected.`
69. Verifikasi Wawan Setiawan {runId} menerima dialog `Approval cannot be made` dengan teks `You can no longer approve this request because it has already been done by another approver.` tanpa menunggu `[Submit]`
70. Wawan Setiawan {runId}: Klik `[OK]`
71. Verifikasi Wawan Setiawan {runId} kembali ke halaman `Approvals > Borrow` sesudah `[OK]`
72. Wawan Setiawan {runId}: Ketik Search `Eka Wijaya {runId}`, tekan Enter
73. Verifikasi tabel Active Wawan Setiawan {runId} menampilkan `No results found`
74. Wawan Setiawan {runId}: Klik tab `History`
75. Wawan Setiawan {runId}: Ketik Search `Eka Wijaya {runId}`, tekan Enter
76. Verifikasi tabel History Wawan Setiawan {runId} menampilkan `No results found` sehingga keputusan yang belum dikirim tidak tersimpan
77. Rina W: Klik `Approvals` pada sidebar
78. Rina W: Klik `Borrow`
79. Rina W: Klik tab `History`
80. Rina W: Ketik Search `Eka Wijaya {runId}`, tekan Enter
81. Rina W: Klik menu ⋯ pada baris DU-020-5
82. Rina W: Klik `Detail`
83. Verifikasi keputusan aset DU-020-6 `Rejected` karena satu penolakan
84. Rina W: Klik sel `Approval Rule` aset DU-020-6
85. Verifikasi dialog `Approval Progress` berjudul `Approval Progress` dengan identitas berlabel `Asset` bernilai `Scanner Epson {runId}` di bawah judul, hanya memuat bagian Approval Progress, dan menampilkan Rina W `Rejected` dan Wawan Setiawan {runId} `Not Involved`

### Aset All menjadi Approved hanya bila kedua approver menyetujui
86. Rina W: Klik `Approvals` pada sidebar
87. Rina W: Klik `Borrow`
88. Rina W: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
89. Rina W: Klik menu ⋯ pada baris DU-020-7
90. Rina W: Klik `Review`
91. Rina W: Klik `[Submit]`
92. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
93. Verifikasi Rina W menerima toast `Success, your approval has been recorded. Waiting for the other approvers.`
94. Rina W: Klik `Approvals` pada sidebar
95. Rina W: Klik `Borrow`
96. Rina W: Klik tab `History`
97. Rina W: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
98. Rina W: Klik menu ⋯ pada baris DU-020-7
99. Rina W: Klik `Detail`
100. Verifikasi kolom Approval Rule aset DU-020-8 `All approvers · 1 of 2 approved` dan keputusannya `Waiting`, bukan `Approved`
101. Rina W: Klik sel `Approval Rule` aset DU-020-8
102. Verifikasi dialog `Approval Progress` berjudul `Approval Progress` dengan identitas berlabel `Asset` bernilai `Monitor LG {runId}` di bawah judul, hanya memuat bagian Approval Progress, dan menampilkan Rina W `Approved` dan Wawan Setiawan {runId} `Waiting for Approval`
103. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
104. Wawan Setiawan {runId}: Klik `Borrow`
105. Wawan Setiawan {runId}: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
106. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-7
107. Wawan Setiawan {runId}: Klik `Review`
108. Wawan Setiawan {runId}: Klik `[Submit]`
109. Wawan Setiawan {runId}: Klik `[Submit]` pada dialog `Submit Approval`
110. Verifikasi Wawan Setiawan {runId} menerima toast `Success, borrow has been approved.`
111. Rina W: Klik `Approvals` pada sidebar
112. Rina W: Klik `Borrow`
113. Rina W: Klik tab `History`
114. Rina W: Ketik Search `Fajar Nugroho {runId}`, tekan Enter
115. Rina W: Klik menu ⋯ pada baris DU-020-7
116. Rina W: Klik `Detail`
117. Verifikasi keputusan aset DU-020-8 `Approved` karena semua approver menyetujui

### Aset All yang tidak diputuskan salah satu approver ditutup oleh timeout
118. Rina W: Klik `Approvals` pada sidebar
119. Rina W: Klik `Borrow`
120. Rina W: Ketik Search `Gita Ramadhani {runId}`, tekan Enter
121. Rina W: Klik menu ⋯ pada baris DU-020-9
122. Rina W: Klik `Review`
123. Rina W: Klik `[Submit]`
124. Rina W: Klik `[Submit]` pada dialog `Submit Approval`
125. Wawan Setiawan {runId}: Klik `Approvals` pada sidebar
126. Wawan Setiawan {runId}: Klik `Borrow`
127. Wawan Setiawan {runId}: Ketik Search `Gita Ramadhani {runId}`, tekan Enter
128. Wawan Setiawan {runId}: Klik menu ⋯ pada baris DU-020-9
129. Wawan Setiawan {runId}: Klik `Review`
130. Job Transaction timeout berjalan sesudah batas Transaction timeout baris DU-020-10 terlewati
131. Verifikasi Wawan Setiawan {runId} menerima dialog `Borrow Canceled` dengan teks `This borrow was canceled automatically (Timed out (Waiting for Approval)).`
132. Wawan Setiawan {runId}: Klik `[OK]`
133. Rina W: Klik `Approvals` pada sidebar
134. Rina W: Klik `Borrow`
135. Rina W: Klik tab `History`
136. Rina W: Ketik Search `Gita Ramadhani {runId}`, tekan Enter
137. Rina W: Klik menu ⋯ pada baris DU-020-9
138. Rina W: Klik `Detail`
139. Rina W: Klik sel `Approval Rule` aset DU-020-10
140. Verifikasi dialog `Approval Progress` berjudul `Approval Progress` dengan identitas berlabel `Asset` bernilai `Tablet Samsung {runId}` di bawah judul, hanya memuat bagian Approval Progress, dan menampilkan Rina W `Approved` dengan waktu keputusannya dan Wawan Setiawan {runId} `Not Involved` dengan keterangan `Canceled by system`

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.1g (kontrol keputusan T-BRW-08), V-BRW-27, dan FLD-BRW-17: Approve Duration yang melebihi durasi diminta ditolak dengan caption `Max. [Requested] [Unit]` di bawah input. Kontrak `NumberInput#1`: `min` dan `max` adalah rentang, bukan filter ketik; nilai di luar rentang dijepit ke batas terdekat saat blur atau Enter. Kontrak `NumberInput#15`: tidak ada pesan rentang dan tidak ada state invalid untuk nilai di luar `min`/`max`. Diasersi: kontrak, nilai dijepit ke durasi diminta tanpa caption (SB-7).
