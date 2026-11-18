---
id: TC-FA-BORROW-E2E-019-approval-review-keputusan-per-aset
title: "Halaman Review Approval memutuskan setiap aset dengan Approve atau Reject, Approve Duration, dan Approval Note"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["F-BORROW-05", "FI-BRW-206", "FI-BRW-211", "FI-BRW-212", "§4.1g#p1", "§4.1g#r1", "§4.1g#r2", "§4.1g#r3", "§4.1g#r4", "§4.1g#r5", "§4.1g#r6", "§4.1g#r7", "§4.1g#r8", "§4.1g#r9", "§4.1g#r10", "§4.1g#r11", "§4.1g#r12", "§4.1g#r13", "§4.1g#r14", "§4.1g#r15", "§4.1g#r16", "§4.1g#r17", "§4.1g#r18", "§4.2.9#p1", "§4.3#r4", "§4.4#r7", "§4.4#r8", "§4.4#r9"]
smoke: []
dependsOn: []
trace:
  "F-BORROW-05": [79, 86]
  "FI-BRW-206": 77
  "FI-BRW-211": 83
  "FI-BRW-212": 83
  "§4.1g#p1": [7, 64, 65]
  "§4.1g#r1": 9
  "§4.1g#r2": [10, 21, 27, 28]
  "§4.1g#r3": 11
  "§4.1g#r4": [12, 25, 30, 47, 48]
  "§4.1g#r5": [13, 32]
  "§4.1g#r6": [16, 53, 54]
  "§4.1g#r7": [17, 59, 60]
  "§4.1g#r8": [18, 23, 99]
  "§4.1g#r9": [19, 34]
  "§4.1g#r10": [100, 113]
  "§4.1g#r11": [101, 108]
  "§4.1g#r12": 102
  "§4.1g#r13": 103
  "§4.1g#r14": 104
  "§4.1g#r15": [20, 36, 41, 42]
  "§4.1g#r16": [64, 66]
  "§4.1g#r17": [64, 66, 68]
  "§4.1g#r18": [64, 73]
  "§4.2.9#p1": 8
  "§4.3#r4": 8
  "§4.4#r7": 91
  "§4.4#r8": 93
  "§4.4#r9": [73, 92]
anchor: [6, 116]
coverage:
  web: automated
---

# Halaman Review Approval memutuskan setiap aset dengan Approve atau Reject, Approve Duration, dan Approval Note

## Prerequisites
- Aktor: Rina W, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-019-1: pengajuan approval tipe `Borrow` di antrean Active Rina W, Group `Head Office`, Borrower `Nadia Putri {runId}`, Requested By `Agus Pratama {runId}`, Total Asset `5`, dengan aset DU-019-2 sampai DU-019-6.
  - DU-019-2: aset `Laptop Dell Latitude {runId}`, Brand `Dell`, Model/Type `Latitude 5420`, TAG `RFID`, Category `Laptop`, tanpa foto, Duration `3 / 3 days`, Purpose `Presentasi klien`, Approval Rule `Any one approver · Waiting` (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-019-3: aset `Proyektor Epson {runId}`, Brand `Epson`, Model/Type `EB-X49`, TAG `QR`, Category `Proyektor`, Duration `2 / 7 days`, Purpose `Rapat divisi`, Approval Rule `Rina W (You) · Waiting` (satu approver, Rina W).
  - DU-019-4: aset `Kamera Sony Alpha {runId}`, Brand `Sony`, Model/Type `A7 III`, TAG `NFC`, Category `Kamera`, Duration `4 / 7 days`, Purpose `Dokumentasi acara`, Approval Rule `All approvers · 0 of 2 approved` (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-019-5: aset `Tripod Manfrotto {runId}`, Brand `Manfrotto`, Model/Type `MT055`, TAG `Non TAG`, Category `Aksesori Kamera`, Duration `1 / 3 days`, Purpose `Dokumentasi acara`, Approval Rule `Wawan Setiawan {runId} · Waiting` (satu approver, bukan Rina W).
  - DU-019-6: aset `Mikrofon Rode {runId}`, Brand `Rode`, Model/Type `VideoMic Pro`, TAG `RFID`, Category `Audio`, Duration `5 / 5 days`, Purpose `Wawancara lapangan`, Approval Rule `Rina W (You) · Waiting` (satu approver, Rina W).
  - Asset ID tiap aset dibentuk sistem dan menjadi milik entri aset itu.
  - DU-019-7: pengajuan approval tipe `Extension` di antrean Active Rina W, Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Requested By `Lina Setiawati {runId}`, Total Asset `1`, dengan aset DU-019-8.
  - DU-019-8: aset `Toyota Avanza {runId}`, Brand `Toyota`, Model/Type `Avanza 1.5 G`, TAG `RFID`, Category `Kendaraan`, Current Due Date T0 + 1 hari, Extensions `0 / 1`, Extend By `2 days`, New Due Date T0 + 3 hari (dari Current Due Date T0 + 1 hari ditambah Extend By 2 hari), Reason `Perjalanan dinas diperpanjang`, Approval Rule `Any one approver · Waiting` (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-019-9: user `Wawan Setiawan {runId}`, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`.

## Test Steps

### Membuka halaman Review dari antrean Active
1. Klik `Approvals` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Nadia Putri {runId}`, tekan Enter
4. Klik menu ⋯ pada baris DU-019-1
5. Klik `Review`
6. Verifikasi halaman Review pengajuan DU-019-1 terbuka dengan breadcrumb `Approvals > Borrow > Active > Review`
7. Verifikasi tabel aset memuat seluruh aset pengajuan DU-019-1, yaitu aset DU-019-2, DU-019-3, DU-019-4, DU-019-5, dan DU-019-6, termasuk aset milik approver lain
8. Verifikasi notice `You cannot decide a borrow you requested or borrow for.` tidak tampil dan tombol `[Submit]` tampil karena Rina W bukan pengaju, Borrower, maupun PIC Borrower

### Isi kolom tabel aset pada pengajuan Borrow
9. Verifikasi kolom Photo baris DU-019-5 menampilkan placeholder gambar standar
10. Verifikasi kolom Name baris DU-019-2 menampilkan `Laptop Dell Latitude {runId}` diikuti Increment
11. Verifikasi kolom Asset ID baris DU-019-2 menampilkan Asset ID milik DU-019-2
12. Verifikasi kolom Brand baris DU-019-2 `Dell` dan baris DU-019-3 `Epson`
13. Verifikasi kolom Model/Type baris DU-019-2 `Latitude 5420` dan baris DU-019-3 `EB-X49`
14. Buka Setup Column
15. Tampilkan kolom `TAG` dan `Category`
16. Verifikasi kolom TAG baris DU-019-2 menampilkan TAG `RFID` dan baris DU-019-5 menampilkan `—`
17. Verifikasi kolom Category baris DU-019-2 `Laptop` dan baris DU-019-4 `Kamera`
18. Verifikasi kolom Duration baris DU-019-2 `3 / 3 days` dan baris DU-019-3 `2 / 7 days`
19. Verifikasi kolom Purpose baris DU-019-2 `Presentasi klien` dan baris DU-019-3 `Rapat divisi`
20. Verifikasi kolom Approval Rule baris DU-019-2 `Any one approver · Waiting`, baris DU-019-3 `Rina W (You) · Waiting`, baris DU-019-4 `All approvers · 0 of 2 approved`, dan baris DU-019-5 `Wawan Setiawan {runId} · Waiting`

### Sort, search, dan filter tabel aset
21. Verifikasi urutan awal baris dari atas ke bawah adalah DU-019-4, DU-019-2, DU-019-6, DU-019-3, DU-019-5 (Name A–Z)
22. Urutkan kolom `Duration` dengan `Shortest First`
23. Verifikasi urutan dari atas ke bawah adalah DU-019-5, DU-019-3, DU-019-2, DU-019-4, DU-019-6
24. Urutkan kolom `Brand` secara Alphabetical (A–Z)
25. Verifikasi urutan dari atas ke bawah adalah DU-019-2, DU-019-3, DU-019-5, DU-019-6, DU-019-4
26. Ketik Search `Kamera Sony Alpha {runId}`, tekan Enter
27. Verifikasi baris DU-019-4 tampil
28. Verifikasi baris DU-019-2, DU-019-3, DU-019-5, dan DU-019-6 tidak tampil
29. Ganti isi kotak search dengan `Manfrotto`, tekan Enter
30. Verifikasi baris DU-019-5 tampil
31. Ganti isi kotak search dengan `Latitude 5420`, tekan Enter
32. Verifikasi baris DU-019-2 tampil
33. Ganti isi kotak search dengan `Presentasi klien`, tekan Enter
34. Verifikasi baris DU-019-2 tampil
35. Ganti isi kotak search dengan `All approvers`, tekan Enter
36. Verifikasi baris DU-019-4 tampil
37. Klik `(←)` pada kotak Search
38. Klik ikon Filter
39. Pada field `Approval Type` pilih `All approvers`
40. Klik `[Apply]`
41. Verifikasi baris DU-019-4 tampil
42. Verifikasi baris DU-019-2, DU-019-3, DU-019-5, dan DU-019-6 tidak tampil
43. Klik `[Clear Field]`
44. Klik `[Apply]`
45. Pada field `Brand` pilih `Dell` dan `Epson`
46. Klik `[Apply]`
47. Verifikasi baris DU-019-2 dan DU-019-3 tampil
48. Verifikasi baris DU-019-4, DU-019-5, dan DU-019-6 tidak tampil
49. Klik `[Clear Field]`
50. Klik `[Apply]`
51. Pada field `TAG` pilih `RFID`
52. Klik `[Apply]`
53. Verifikasi baris DU-019-2 dan DU-019-6 tampil
54. Verifikasi baris DU-019-3, DU-019-4, dan DU-019-5 tidak tampil
55. Klik `[Clear Field]`
56. Klik `[Apply]`
57. Pada field `Category` pilih `Audio`
58. Klik `[Apply]`
59. Verifikasi baris DU-019-6 tampil
60. Verifikasi baris DU-019-2, DU-019-3, DU-019-4, dan DU-019-5 tidak tampil
61. Klik `[Clear Field]`
62. Klik `[Apply]`
63. Klik ikon Filter

### Aset milik approver lain tampil read-only
64. Verifikasi baris DU-019-5 menampilkan keterangan `Not your approval` pada kontrol Approval, Approve Duration, dan Approval Note
65. Verifikasi checkbox baris DU-019-5 tidak dapat dicentang

### Keputusan per aset: Approve Duration, Reject, dan Approval Note
66. Verifikasi toggle Approval baris DU-019-2 `Approve` dan Approve Duration baris DU-019-2 `3` sesuai Duration yang diminta
67. Isi Approve Duration baris DU-019-2 dengan `4`
68. Verifikasi caption `Max. 3 days` tampil di bawah input Approve Duration baris DU-019-2
69. Isi Approve Duration baris DU-019-2 dengan `2`
70. Ubah toggle Approval baris DU-019-3 menjadi `Reject`
71. Isi Approve Duration baris DU-019-6 dengan `0`
72. Klik `[Submit]`
73. Verifikasi caption `Approval note must not be empty` tampil pada baris DU-019-3 dan baris DU-019-6
74. Isi Approval Note baris DU-019-3 dengan `Proyektor dipakai kegiatan lain`
75. Isi Approval Note baris DU-019-6 dengan `Durasi terlalu panjang untuk kegiatan ini`
76. Klik `[Submit]`
77. Verifikasi dialog `Submit Approval` tampil dengan teks `You will submit this transaction approval. Asset with 0 approved duration will be rejected and will not appear in the next step of transaction. Are you sure you want to submit it?`
78. Klik `[Submit]` pada dialog `Submit Approval`
79. Verifikasi toast `Success, your approval has been recorded. Waiting for the other approvers.` tampil

### Hasil keputusan tercatat di History dan Detail
80. Klik `Borrow` pada sidebar
81. Klik tab `History`
82. Ketik Search `Nadia Putri {runId}`, tekan Enter
83. Verifikasi baris DU-019-1 tampil di tab `History` dengan Status `Partially Approved`
84. Klik tab `Active`
85. Ketik Search `Nadia Putri {runId}`, tekan Enter
86. Verifikasi tabel Active menampilkan `No results found`
87. Klik tab `History`
88. Ketik Search `Nadia Putri {runId}`, tekan Enter
89. Klik menu ⋯ pada baris DU-019-1
90. Klik `Detail`
91. Verifikasi keputusan aset DU-019-2 `Approved` sebagai keputusan pertama pada mode Any one approver
92. Verifikasi keputusan aset DU-019-3 `Rejected` dan aset DU-019-6 `Rejected`
93. Verifikasi kolom Approval Rule aset DU-019-4 `All approvers · 1 of 2 approved` dan keputusannya `Waiting`

### Kolom khusus pengajuan Extension pada halaman Review
94. Klik `Borrow` pada sidebar
95. Klik tab `Active`
96. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
97. Klik menu ⋯ pada baris DU-019-7
98. Klik `Review`
99. Verifikasi kolom Duration baris DU-019-8 menampilkan `—`
100. Verifikasi kolom Current Due Date baris DU-019-8 menampilkan tanggal Current Due Date milik DU-019-8 menurut format General Settings
101. Verifikasi kolom Extensions baris DU-019-8 `0 / 1`
102. Verifikasi kolom Extend By baris DU-019-8 `2 days`
103. Verifikasi kolom New Due Date baris DU-019-8 menampilkan tanggal New Due Date milik DU-019-8 menurut format General Settings
104. Verifikasi kolom Reason baris DU-019-8 `Perjalanan dinas diperpanjang`
105. Klik ikon Filter
106. Isi field `Extensions` dengan Min `1` dan Max `1`
107. Klik `[Apply]`
108. Verifikasi tabel aset menampilkan `No results found`
109. Klik `[Clear Field]`
110. Klik `[Apply]`
111. Pada field `Current Due Date` pilih rentang dari T0 + 2 hari sampai T0 + 4 hari
112. Klik `[Apply]`
113. Verifikasi tabel aset menampilkan `No results found`
114. Klik `[Clear Field]`
115. Klik `[Apply]`
116. Verifikasi baris DU-019-8 tampil kembali setelah filter dibersihkan
