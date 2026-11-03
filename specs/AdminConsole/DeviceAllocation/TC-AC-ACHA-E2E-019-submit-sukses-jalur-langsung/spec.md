---
id: TC-AC-ACHA-E2E-019-submit-sukses-jalur-langsung
title: "Submit Allocate Device Sukses Jalur Langsung: Status Completed per Role dan Entitas, Stay on Form, dan Full-State Record"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-133
  - TC-AC-ACHA-134
  - TC-AC-ACHA-135
  - TC-AC-ACHA-136
  - TC-AC-ACHA-137
  - TC-AC-ACHA-138
  - TC-AC-ACHA-139
  - TC-AC-ACHA-140
  - TC-AC-ACHA-144
  - TC-AC-ACHA-145
  - TC-AC-ACHA-148
  - TC-AC-ACHA-149
coverage:
  web: automated
---

# Submit Allocate Device Sukses Jalur Langsung: Status Completed per Role dan Entitas, Stay on Form, dan Full-State Record

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (urutan pemakaian dalam spec):

| Kode | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| A-01 | Total Control Principal `PT ABC` (Admin Pratama) | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| A-02 | Total Control Distributor `PT Global Distribusi` (Hendra Wibowo) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| A-05 | Group Member Distributor toggle OFF (Citra Anggraini) | #33 | `memberOffDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_OFF_PASSWORD` |
| A-06 | Group Manager Distributor Group Jakarta (Agus Hartono) | #29 | `groupManagerDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_GM_DIST_PASSWORD` |
| A-07 | Group Manager Region Jawa, ancestor Group Jakarta | #31 | `groupManagerRegion_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_GM_REGION_PASSWORD` |
| A-03 | Total Control Partner `CV Mitra Solusi` (Maya Putri) | #43 | `totalControlPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P1_PASSWORD` |
| A-04 | Total Control Partner `CV Karya Mandiri` | #46 | `totalControlPartner2_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P2_PASSWORD` |

- Login A-01 di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (A-01, `AC_TC_PASSWORD`). Ganti akun dengan langkah logout dan login eksplisit. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan tahap script); password tidak ditulis di spec.
- Data Pre-setup: Client #7 `PT Sejahtera Logistik`, #8 `PT Retail Makmur`, #9 `PT Cipta Kreasi`, #10 `PT Manufaktur Unggul`; kantong #16 PT Global Distribusi saldo $20,000.00, #17 CV Mitra Solusi saldo $2,000.00, #18 kantong A CV Karya Mandiri saldo $1,000.00, #19 kantong B saldo $3,000.00; harga #14 dan #15; General Settings #1 (`dd/MM/yy`, 24 jam, Asia/Jakarta).
- Hook `before` menyetel saldo semua kantong ke nilai Pre-setup lewat fixture API Pre-setup #20 (disediakan tim FE/BE); hook `after` memulihkannya dan memulihkan seed lewat fixture Pre-setup #20 (Lampiran A butir A-11).
- Data Dinamis: tiga belas alokasi `Completed` dibuat spec ini. Nilai Notes bersuffix per run: `Batch uji prin+{runId}-019` (TC-133) dan `Uji full state+{runId}-019` (TC-148). Efek: kuota Client dan saldo kantong bertambah atau berkurang; modul tanpa Delete sehingga alokasi tidak dihapus. Allocation ID tiap alokasi ditangkap dari baris teratas List sebagai Dynamic Reference (Notes bersuffix hanya pada TC-133 dan TC-148 karena Notes TC lain tidak menjadi data uji).
- Kolom Notes, Payment, Paid From, dan Cost pada List ditampilkan lewat Setup Column pada langkah pertama (precondition TC-133) dan ditampilkan ulang lewat Setup Column sesudah ganti akun ke A-02, A-03, dan A-04 (akun yang asersinya memakai kolom itu), karena cakupan preferensi kolom lintas akun tidak diasumsikan; preferensi kolom dihapus di hook `after` (`suite.md`).
- Waktu aksi: waktu dicatat sesudah `[Submit]`; asersi Last Updated dengan toleransi satu menit (kolom Last Updated berketelitian menit); jam server dan jam browser sinkron dan tidak diubah.
- Kemampuan teknis: kemampuan baca Wallet Balance (saldo, Reserved, Wallet Transaction List) kantong PT Global Distribusi, CV Mitra Solusi, dan kedua kantong CV Karya Mandiri; kemampuan menangkap Allocation ID baris teratas List.
- Hook suite: flag Guided Tooltip, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column, dan seed 30 baris dinyatakan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### Akun A-01 Principal: Submit jalur langsung Principal (TC-AC-ACHA-133)

1. Buka Setup Column, tampilkan kolom Notes, Payment, Paid From, dan Cost, klik `[Save]`
2. Klik `[+ Allocation]`
3. Pilih Category `Hardware - BLE Gateway`, Client `PT Manufaktur Unggul`, isi Quantity `50`, isi Notes `Batch uji prin+{runId}-019`
4. Klik `[Submit]`, lalu catat waktu Submit
5. Verifikasi toast sukses: "Success, device allocation has been created."
6. Verifikasi form tertutup
7. Catat Allocation ID baris teratas List (transaksi TC-133)
8. Verifikasi baris teratas List: Category `BLE Gateway`
9. Verifikasi baris teratas List: Type `—`
10. Verifikasi baris teratas List: Quantity `50`
11. Verifikasi baris teratas List: From `PT ABC`
12. Verifikasi baris teratas List: Client `PT Manufaktur Unggul`
13. Verifikasi baris teratas List: Status `Completed`
14. Verifikasi baris teratas List: Last Updated sama dengan waktu Submit (toleransi satu menit)
15. Verifikasi kolom Notes `Batch uji prin+{runId}-019`
16. Verifikasi kolom Payment `Free`
17. Verifikasi kolom Paid From `—`
18. Verifikasi kolom Cost `—`
19. Buka modal Allocation Log transaksi baru
20. Verifikasi modal Allocation Log memuat satu entri `Allocation created by [PIC]`
21. Verifikasi modal Allocation Log tidak memuat entri `Allocation approved`
22. Tutup modal Allocation Log

### Akun A-01 Principal: Stay on this form (TC-AC-ACHA-144) dan tanpa Stay (TC-AC-ACHA-145)

23. Klik `[+ Allocation]`, centang "Stay on this form after submitting"
24. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `3`, klik `[Submit]`
25. Verifikasi toast "Success, device allocation has been created."
26. Verifikasi form tetap terbuka
27. Verifikasi semua field pada form kosong
28. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
29. Pilih Category `TAG - GPS`, Client `PT Manufaktur Unggul`, isi Quantity `4`, klik `[Submit]`
30. Verifikasi toast "Success, device allocation has been created."
31. Klik `[×]`
32. Verifikasi form tertutup tanpa dialog Unsaved Changes (checkbox bukan field data)
33. Catat Allocation ID baris pertama dan kedua List (transaksi TC-144: GPS dan NFC)
34. Verifikasi baris pertama List: `GPS` Quantity `4`
35. Verifikasi baris kedua List: `NFC` Quantity `3`
36. Verifikasi kedua baris adalah transaksi terpisah dengan Allocation ID berbeda
37. Klik `[+ Allocation]` tanpa mencentang checkbox
38. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `3`, klik `[Submit]`
39. Verifikasi toast sukses "Success, device allocation has been created."
40. Verifikasi form tertutup
41. Catat Allocation ID baris teratas List (transaksi TC-145)

### Akun A-02 Distributor: Capture tanpa Reserve (TC-AC-ACHA-134), Type Handheld Reader (TC-AC-ACHA-140), full-state (TC-AC-ACHA-148, TC-AC-ACHA-149)

42. Logout, lalu login sebagai A-02 (`PT Global Distribusi`), buka Allocation > Device Allocation
43. Buka Setup Column, tampilkan kolom Notes, Payment, Paid From, dan Cost, klik `[Save]`
44. Klik `[+ Allocation]`
45. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `50`
46. Klik `[Submit]`
47. Verifikasi toast sukses "Success, device allocation has been created."
48. Catat Allocation ID baris teratas List (transaksi TC-134)
49. Verifikasi baris baru berstatus `Completed`
50. Verifikasi baris baru: Payment `Wallet`
51. Verifikasi baris baru: Paid From `PT ABC (Principal)`
52. Verifikasi baris baru: Cost `$100.00`
53. Buka Wallet Balance kantong PT Global Distribusi
54. Verifikasi Wallet Balance: saldo $19,900.00
55. Verifikasi Wallet Balance: Reserved $0.00 (jalur langsung dipotong langsung tanpa Reserve)
56. Verifikasi Wallet Transaction List memuat debit $100.00
57. Buka Allocation > Device Allocation, lalu klik `[+ Allocation]`
58. Pilih Category `Hardware - Handheld Reader`, Client `PT Sejahtera Logistik`, isi Quantity `3`
59. Pilih Type `Short Range`
60. Klik `[Submit]`
61. Verifikasi toast sukses "Success, device allocation has been created."
62. Catat Allocation ID baris teratas List (transaksi TC-140)
63. Verifikasi baris baru: Category `Handheld Reader`
64. Verifikasi baris baru: Type `Short Range`
65. Verifikasi baris baru: Cost `$66.00`
66. Buka modal Allocation Log transaksi baru
67. Verifikasi modal Allocation Log memuat baris `Type: Short Range`
68. Tutup modal Allocation Log
69. Klik `[+ Allocation]`
70. Pilih Category `TAG - RFID`, Client `PT Sejahtera Logistik`, isi Quantity `20`, isi Notes `Uji full state+{runId}-019`
71. Pilih Type `Object TAG` (default)
72. Klik `[Submit]`, lalu catat waktu Submit
73. Catat Allocation ID baris teratas List (transaksi TC-148)
74. Verifikasi baris List: Allocation ID berformat `HALC-YYYYMMDD-XXXXX`
75. Verifikasi baris List: Category `RFID`
76. Verifikasi baris List: Type `Object TAG`
77. Verifikasi baris List: Quantity `20`
78. Verifikasi baris List: From `PT Global Distribusi`
79. Verifikasi baris List: Client `PT Sejahtera Logistik`
80. Verifikasi baris List: Allocated By `Hendra W`
81. Verifikasi baris List: Status `Completed`
82. Verifikasi baris List: Last Updated sama dengan waktu Submit sesuai General Settings (toleransi satu menit)
83. Verifikasi baris List: Notes `Uji full state+{runId}-019`
84. Verifikasi baris List: Payment `Wallet`
85. Verifikasi baris List: Paid From `PT ABC (Principal)`
86. Verifikasi baris List: Cost `$50.00`
87. Buka modal Allocation Log transaksi baru
88. Verifikasi header Allocation Log: Status `Completed`, Client `PT Sejahtera Logistik`, Paid From `PT ABC (Principal)`
89. Verifikasi entri `Allocation created by [PIC]` memuat `Category: RFID`, `Type: Object TAG`, `Quantity: 20`, `From: PT Global Distribusi`, `Notes: Uji full state+{runId}-019`, `Cost: $50.00`
90. Tutup modal Allocation Log
91. Klik `[+ Allocation]`
92. Pilih Category `TAG - NFC`, Client `PT Sejahtera Logistik`, isi Quantity `5`
93. Klik `[Submit]`
94. Catat Allocation ID baris teratas List (transaksi TC-149)
95. Verifikasi baris baru: Type `—`
96. Verifikasi baris baru: Notes `—`
97. Buka modal Allocation Log transaksi baru
98. Verifikasi entri `Allocation created by [PIC]` memuat `Category: NFC`, `Quantity: 5`, `From`, dan `Cost: $6.00`
99. Verifikasi entri `Allocation created by [PIC]` tidak memuat baris `Type` maupun `Notes`
100. Tutup modal Allocation Log

### Akun A-05 Group Member toggle OFF (TC-AC-ACHA-135)

101. Logout, lalu login sebagai A-05 (`Citra Anggraini`), buka Allocation > Device Allocation
102. Klik `[+ Allocation]`
103. Pilih Category `TAG - NFC`, Client `PT Sejahtera Logistik`, isi Quantity `10`
104. Klik `[Submit]`
105. Verifikasi toast sukses "Success, device allocation has been created." (toggle Require Approval for Allocation role OFF)
106. Catat Allocation ID baris teratas List (transaksi TC-135)
107. Verifikasi baris baru langsung berstatus `Completed` tanpa subject di Approvals (role lain dengan toggle ON di Group Surabaya tidak memengaruhi hasil)

### Akun A-06 Group Manager pada group target (TC-AC-ACHA-136)

108. Logout, lalu login sebagai A-06 (`Agus Hartono`), buka Allocation > Device Allocation
109. Klik `[+ Allocation]`
110. Pilih Category `TAG - NFC`, Client `PT Sejahtera Logistik`, isi Quantity `10`
111. Klik `[Submit]`
112. Verifikasi toast sukses "Success, device allocation has been created." (auto-bypass walau toggle role ON)
113. Catat Allocation ID baris teratas List (transaksi TC-136)
114. Verifikasi baris baru langsung berstatus `Completed`

### Akun A-07 Group Manager ancestor group target (TC-AC-ACHA-137)

115. Logout, lalu login sebagai A-07 (Group Manager Region Jawa), buka Allocation > Device Allocation
116. Klik `[+ Allocation]`
117. Pilih Category `TAG - NFC`, Client `PT Sejahtera Logistik`, isi Quantity `10`
118. Klik `[Submit]`
119. Verifikasi toast sukses "Success, device allocation has been created." (auto-bypass pada ancestor group target)
120. Catat Allocation ID baris teratas List (transaksi TC-137)
121. Verifikasi baris baru langsung berstatus `Completed`

### Akun A-03 Partner satu kantong (TC-AC-ACHA-138)

122. Logout, lalu login sebagai A-03 (`CV Mitra Solusi`), buka Allocation > Device Allocation
123. Buka Setup Column, tampilkan kolom Notes, Payment, Paid From, dan Cost, klik `[Save]`
124. Klik `[+ Allocation]`
125. Pilih Category `Hardware - BLE Gateway`, Client `PT Retail Makmur`, isi Quantity `50`
126. Klik `[Submit]`
127. Verifikasi toast sukses "Success, device allocation has been created."
128. Catat Allocation ID baris teratas List (transaksi TC-138)
129. Verifikasi baris baru berstatus `Completed`
130. Verifikasi baris baru: Paid From `PT Global Distribusi (Distributor)`
131. Verifikasi baris baru: Cost `$125.00`
132. Buka Wallet Balance kantong CV Mitra Solusi
133. Verifikasi saldo kantong CV Mitra Solusi $1,875.00
134. Verifikasi Reserved kantong CV Mitra Solusi $0.00

### Akun A-04 Partner dua kantong (TC-AC-ACHA-139)

135. Logout, lalu login sebagai A-04 (`CV Karya Mandiri`), buka Allocation > Device Allocation
136. Buka Setup Column, tampilkan kolom Notes, Payment, Paid From, dan Cost, klik `[Save]`
137. Klik `[+ Allocation]`
138. Pilih Category `TAG - NFC`, Client `PT Cipta Kreasi`, isi Quantity `10`
139. Pilih Pay From `PT ABC (Principal)`
140. Klik `[Submit]`
141. Verifikasi toast sukses "Success, device allocation has been created."
142. Catat Allocation ID baris teratas List (transaksi TC-139)
143. Verifikasi baris baru berstatus `Completed`
144. Verifikasi baris baru: Paid From `PT ABC (Principal)`
145. Verifikasi baris baru: Cost `$12.00`
146. Buka Wallet Balance kedua kantong
147. Verifikasi kantong B menjadi $2,988.00
148. Verifikasi kantong A tetap $1,000.00

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan spec di atas sekitar 35 langkah: semua blok satu topik (Submit jalur langsung yang berhasil) dan satu kelas; tiap blok akun berdiri sendiri dengan langkah ganti akun eksplisit (konvensi bagian 3, pemisah (b)) sehingga kegagalan satu blok tidak menghilangkan makna blok lain; jumlah langkah terutama dari S-01 pada asersi full-state TC-133 dan TC-148. Spec ini seluruhnya membuat data (semua aksi sukses) sehingga tidak ada pemisah antara pembuat dan bukan pembuat data.
- Penyimpangan urutan (S-10): blok akun dikelompokkan menurut akun untuk meminimalkan ganti akun: TC-134 mendahului TC-140, TC-148, dan TC-149 supaya saldo awal kantong PT Global Distribusi $20,000.00 sesuai Expected TC-134 (saldo $19,900.00); TC-135 sampai TC-137 mengikuti blok A-02 karena asersi saldo hanya pada TC-134. TC-144 menutup form dengan `[×]` sebelum membaca dua baris teratas List (Allocation ID pada baris, bukan pada form), sehingga butir c (tanpa dialog) mendahului butir b.
- Langkah penghubung (S-03): tampilkan kolom lewat Setup Column (juga sesudah ganti akun ke A-02, A-03, A-04, langkah 43, 123, dan 136), catat waktu Submit, buka dan tutup modal Allocation Log, pembukaan ulang halaman Device Allocation dari Wallet Balance, logout dan login ganti akun.
- Asersi gabungan sesuai S-03: "tanpa subject di Approvals" dan "role lain tidak memengaruhi hasil" (TC-135) serta "tidak ada Reserve atau potongan wallet" (TC-133 butir d) tidak punya langkah observasi sendiri di TC dan diasersi sebagai kesimpulan dari status `Completed` dan kolom Payment `Free`, Paid From `—`, Cost `—`.
- Pengecualian S-12 nama literal: nama entitas dan Client Pre-setup literal (sudah ada di environment); Notes dinamis bersuffix `{runId}-019`.
- Temuan untuk QA:
  - TC-133 dan TC-148 menulis `[PIC]` pada entri `Allocation created by [PIC]` tanpa format nama; spec mengasersi teks `Allocation created by [PIC]` seperti di TC.
  - TC-135 Expected b ("tanpa subject di Approvals") tidak punya langkah observasi di TC (Approvals tidak dibuka); tidak diasersi di Approvals.
  - TC-144 Expected b ("Allocation ID berbeda") tidak menyebut cara membandingkan ID; spec membaca dua baris teratas List sesudah form ditutup.
  - TC-148 Expected a menyebut Allocated By `[First Name] [Last Initial]`; spec mengasersi `Hendra W` dari nama pengguna Pre-setup #27 (Hendra Wibowo).
  - Post Condition semua TC (kuota Client, panel `Allocated quota`, Wallet Transaction List, Client Dashboard) tidak punya langkah observasi di TC dan tidak diasersi; pengecualian: saldo, Reserved, dan Wallet Transaction List yang tercantum pada Expected TC-134, TC-138, dan TC-139.
  - TC-133 Expected e ("satu entri") tidak menyebut jumlah entri dasar; Allocation Log transaksi baru memuat satu entri sehingga tidak butuh baseline.
