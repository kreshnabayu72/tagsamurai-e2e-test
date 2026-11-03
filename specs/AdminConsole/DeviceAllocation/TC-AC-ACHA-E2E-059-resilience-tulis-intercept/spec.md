---
id: TC-AC-ACHA-E2E-059-resilience-tulis-intercept
title: "Resilience Tulis (Intercept): Kegagalan Server 500 dan Timeout pada Submit, Save Edit, Cancel, Resubmit, Approve, dan Reject"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-150
  - TC-AC-ACHA-151
  - TC-AC-ACHA-152
  - TC-AC-ACHA-209
  - TC-AC-ACHA-210
  - TC-AC-ACHA-228
  - TC-AC-ACHA-229
  - TC-AC-ACHA-252
  - TC-AC-ACHA-253
  - TC-AC-ACHA-462
  - TC-AC-ACHA-463
  - TC-AC-ACHA-464
  - TC-AC-ACHA-465
coverage:
  web: automated
---

# Resilience Tulis (Intercept): Kegagalan Server 500 dan Timeout pada Submit, Save Edit, Cancel, Resubmit, Approve, dan Reject

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; sebagian respons dipaksa lewat `Spectra.intercept()` dan state server nyata diasersi lewat fixture baca).
- Kelas harness b (fault injection / resilience tulis). Semua kegagalan dipaksa di sisi browser (respons 500 atau pemutusan koneksi) sehingga kegagalan yang tidak bisa di-intercept (rollback database) ada di spec 060.
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Dipakai di | Env var password |
|---|---|---|---|---|
| `totalControlDistributor` | #27 | Hendra Wibowo (aktor hook `before`) | TC-AC-ACHA-150, 152, 462, 463, 464, 465 | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | TC-AC-ACHA-151, 209, 210, 228, 229, 252, 253 | `Spectra.env.AC_DA_MB_ON_PASSWORD` |

- Login akun pertama (Hendra Wibowo) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan melepas semua intercept.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #7 Client PT Sejahtera Logistik, #14 harga produk (BLE Gateway $2.00), #16 kantong PT Global Distribusi saldo $20,000.00 (Reserved awal $0.00, dipulihkan fixture di hook `before`).
- Data seeding milik spec (fixture API disediakan tim FE/BE; salinan milik spec dari Pre-setup #49 dan #52): satu transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00) dipakai berurutan oleh TC-AC-ACHA-462 sampai 465 (Hendra), 209, 210, 228, 229 (Budi); satu transaksi Canceled milik MB_ON (BLE Gateway, Quantity 50, Pay From `PT ABC (Principal)`, Notes `Batch lama`) dipakai oleh TC-AC-ACHA-252 dan 253. Semua TC kegagalan membiarkan state transaksi tidak berubah sehingga transaksi yang sama sah dipakai berulang.
- Kebutuhan intercept (`Spectra.intercept()`; tiap intercept dilepas segera sesudah pemicu selesai, S-09):
  - respons Submit dipaksa 500 (TC-AC-ACHA-150, 151, 252), respons Save Edit 500 (TC-AC-ACHA-209), respons Cancel 500 (TC-AC-ACHA-228), respons Approve 500 (TC-AC-ACHA-462), respons Reject 500 (TC-AC-ACHA-463);
  - koneksi diputus (abort jaringan) pada Submit (TC-AC-ACHA-152, 253), Save Edit (TC-AC-ACHA-210), Cancel (TC-AC-ACHA-229), Approve (TC-AC-ACHA-464), dan Reject (TC-AC-ACHA-465).
- Kemampuan teknis: fixture baca (disediakan tim FE/BE) untuk jumlah transaksi entitas pengirim, status, Quantity, Reserved, dan saldo kantong PT Global Distribusi.
- Baseline (S-12): sebelum tiap TC dicatat lewat fixture baca jumlah transaksi, status, Quantity, Reserved, dan saldo; asersi "tidak berubah" membandingkan dengan catatan itu.
- Aksi Approve dan Reject dilakukan di Approvals > Device Allocation (modul Approvals; mekanik halaman Approvals diuji di `tc-approvals.md`); spec ini hanya mengasersi toast kegagalan dan state transaksi.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACHA-150: Kegagalan server pada Submit jalur langsung

1. Catat jumlah transaksi entitas pengirim dan saldo kantong PT Global Distribusi lewat fixture baca sebagai baseline
2. Klik `[+ Allocation]`
3. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, dan isi Quantity `5`
4. Atur intercept agar respons Submit dipaksa server error 500
5. Klik `[Submit]`
6. Lepas intercept respons Submit
7. Verifikasi toast error "Error, failed to create device allocation."
8. Verifikasi form tetap terbuka
9. Verifikasi input dipertahankan
10. Verifikasi tombol `[Submit]` kembali enabled
11. Baca jumlah transaksi dan saldo kantong lewat fixture baca
12. Verifikasi tidak ada baris baru pada List dibanding baseline langkah 1
13. Verifikasi saldo kantong tidak berubah dibanding baseline langkah 1
14. Klik `[×]` pada form
15. Verifikasi dialog `Unsaved Changes` tampil
16. Klik `[Leave]`

### TC-AC-ACHA-152: Timeout atau tanpa respons pada Submit

17. Klik `[+ Allocation]`
18. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, dan isi Quantity `5`
19. Atur intercept agar koneksi diputus pada permintaan Submit sebelum respons
20. Klik `[Submit]`
21. Lepas intercept permintaan Submit
22. Verifikasi toast error "Unable to connect to server. Please check your connection."
23. Verifikasi copy toast memakai teks PRD ini dan bukan copy kanonik "Connection problem. Please try again." (Deviasi T-15)
24. Verifikasi form tetap terbuka
25. Verifikasi form masih terisi
26. Verifikasi tombol `[Submit]` kembali enabled untuk dicoba ulang
27. Verifikasi toast tidak memiliki tombol aksi apa pun, termasuk `[Try Again]`
28. Klik `[×]` pada form
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`

### TC-AC-ACHA-462: Kegagalan server pada Approve

31. Catat status dan Reserved transaksi Waiting for Approval milik MB_ON (target blok ini) lewat fixture baca sebagai baseline
32. Buka Approvals > Device Allocation
33. Atur intercept agar respons Approve dipaksa server error 500
34. Klik `[Approve]` pada transaksi itu, lalu konfirmasi
35. Lepas intercept respons Approve
36. Verifikasi toast error "Error, failed to approve transaction."
37. Baca status dan Reserved transaksi lewat fixture baca
38. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 31
39. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 31
40. Verifikasi tidak ada Capture

### TC-AC-ACHA-463: Kegagalan server pada Reject

41. Atur intercept agar respons Reject dipaksa server error 500
42. Isi Rejection Reason `Stok belum siap`, klik `[Reject]`, lalu konfirmasi
43. Lepas intercept respons Reject
44. Verifikasi toast error "Error, failed to reject transaction."
45. Baca status dan Reserved transaksi lewat fixture baca
46. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 31
47. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 31 (tidak ada Release)

### TC-AC-ACHA-464: Timeout atau tanpa respons pada Approve

48. Atur intercept agar koneksi diputus pada permintaan Approve
49. Klik `[Approve]` pada transaksi itu, lalu konfirmasi
50. Lepas intercept permintaan Approve
51. Verifikasi toast error "Unable to connect to server. Please check your connection."
52. Baca status dan Reserved transaksi lewat fixture baca
53. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 31
54. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 31
55. Verifikasi keputusan dapat diulang: tombol `[Approve]` pada transaksi itu tetap tersedia

### TC-AC-ACHA-465: Timeout atau tanpa respons pada Reject

56. Atur intercept agar koneksi diputus pada permintaan Reject
57. Isi Rejection Reason `Stok belum siap`, klik `[Reject]`, lalu konfirmasi
58. Lepas intercept permintaan Reject
59. Verifikasi toast error "Unable to connect to server. Please check your connection."
60. Baca status dan Reserved transaksi lewat fixture baca
61. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 31
62. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 31
63. Verifikasi keputusan dapat diulang: tombol `[Reject]` pada transaksi itu tetap tersedia

### Ganti akun ke Budi Santoso (MB_ON)

64. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-151: Kegagalan server pada Submit jalur persetujuan

65. Catat jumlah transaksi entitas pengirim dan Reserved kantong PT Global Distribusi lewat fixture baca sebagai baseline
66. Klik `[+ Allocation]`
67. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, dan isi Quantity `5`
68. Atur intercept agar respons Submit dipaksa server error 500
69. Klik `[Submit]`
70. Lepas intercept respons Submit
71. Verifikasi toast error "Error, failed to submit device allocation."
72. Verifikasi form tetap terbuka
73. Verifikasi input dipertahankan
74. Verifikasi tombol `[Submit]` kembali enabled
75. Baca jumlah transaksi dan Reserved kantong lewat fixture baca
76. Verifikasi tidak ada baris baru dibanding baseline langkah 65
77. Verifikasi Reserved tidak bertambah dibanding baseline langkah 65
78. Klik `[×]` pada form
79. Verifikasi dialog `Unsaved Changes` tampil
80. Klik `[Leave]`

### TC-AC-ACHA-209: Kegagalan server pada Save Edit

81. Catat Quantity dan Reserved transaksi Waiting for Approval milik MB_ON lewat fixture baca sebagai baseline
82. Klik `Edit` pada transaksi itu
83. Ubah Quantity menjadi `120`
84. Atur intercept agar respons Save dipaksa server error 500
85. Klik `[Save]`
86. Lepas intercept respons Save
87. Verifikasi toast error "Error, failed to update device allocation."
88. Verifikasi form tetap terbuka
89. Verifikasi input dipertahankan
90. Verifikasi tombol `[Save]` enabled kembali
91. Baca Quantity dan Reserved transaksi lewat fixture baca
92. Verifikasi Quantity tersimpan tetap 100 sesuai baseline langkah 81
93. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 81
94. Klik `[×]` pada form
95. Verifikasi dialog `Unsaved Changes` tampil
96. Klik `[Leave]`

### TC-AC-ACHA-210: Timeout atau tanpa respons pada Save Edit

97. Klik `Edit` pada transaksi itu
98. Ubah Quantity menjadi `120`
99. Atur intercept agar koneksi diputus pada permintaan Save
100. Klik `[Save]`
101. Lepas intercept permintaan Save
102. Verifikasi toast error "Unable to connect to server. Please check your connection."
103. Verifikasi form tetap terbuka
104. Verifikasi input dipertahankan
105. Verifikasi tombol `[Save]` kembali enabled untuk dicoba ulang
106. Verifikasi toast tidak memiliki tombol aksi apa pun, termasuk `[Try Again]`
107. Klik `[×]` pada form
108. Verifikasi dialog `Unsaved Changes` tampil
109. Klik `[Leave]`

### TC-AC-ACHA-228: Kegagalan server pada Cancel

110. Catat status dan Reserved transaksi Waiting for Approval milik MB_ON lewat fixture baca sebagai baseline
111. Klik `Cancel Allocation` pada transaksi itu
112. Atur intercept agar respons Cancel dipaksa server error 500
113. Klik `[Cancel Allocation]` pada dialog
114. Lepas intercept respons Cancel
115. Verifikasi toast error "Error, failed to cancel device allocation."
116. Baca status dan Reserved transaksi lewat fixture baca
117. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 110
118. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 110

### TC-AC-ACHA-229: Timeout atau tanpa respons pada Cancel

119. Klik `Cancel Allocation` pada transaksi itu
120. Atur intercept agar koneksi diputus pada permintaan Cancel
121. Klik `[Cancel Allocation]` pada dialog
122. Lepas intercept permintaan Cancel
123. Verifikasi toast error "Unable to connect to server. Please check your connection."
124. Baca status transaksi lewat fixture baca
125. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 110
126. Verifikasi dialog `Cancel Allocation` masih terbuka dan dapat dicoba ulang
127. Verifikasi toast tidak memiliki tombol aksi apa pun, termasuk `[Try Again]`
128. Klik `[Go Back]` pada dialog `Cancel Allocation` sehingga dialog tertutup tanpa membatalkan transaksi

### TC-AC-ACHA-252: Kegagalan server pada Resubmit

129. Catat jumlah transaksi milik MB_ON lewat fixture baca sebagai baseline
130. Klik `Resubmit` pada transaksi Canceled milik MB_ON
131. Atur intercept agar respons Submit dipaksa server error 500
132. Klik `[Submit]`
133. Lepas intercept respons Submit
134. Verifikasi toast error "Error, failed to resubmit device allocation."
135. Verifikasi form tetap terbuka
136. Verifikasi input dipertahankan
137. Baca jumlah transaksi lewat fixture baca
138. Verifikasi tidak ada transaksi baru dibanding baseline langkah 129
139. Klik `[×]` pada form
140. Verifikasi dialog `Unsaved Changes` tampil
141. Klik `[Leave]`

### TC-AC-ACHA-253: Timeout atau tanpa respons pada Resubmit

142. Klik `Resubmit` pada transaksi Canceled milik MB_ON
143. Atur intercept agar koneksi diputus pada permintaan Submit
144. Klik `[Submit]`
145. Lepas intercept permintaan Submit
146. Verifikasi toast error "Unable to connect to server. Please check your connection."
147. Verifikasi form tetap terbuka
148. Verifikasi form masih terisi
149. Baca jumlah transaksi lewat fixture baca
150. Verifikasi tidak ada transaksi baru dibanding baseline langkah 129
151. Verifikasi toast tidak memiliki tombol aksi apa pun, termasuk `[Try Again]`
152. Klik `[×]` pada form
153. Verifikasi dialog `Unsaved Changes` tampil
154. Klik `[Leave]`

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 3a-5, 3b, 3c, 3d, 9c). Subjudul `###` memetakan langkah ke id TC granular. Spec ini FE+BE (bukan mock) karena asersi mencakup state server (jumlah transaksi, status, Quantity, Reserved); TC baca tanpa asersi state server ada di spec 058 (`Mode: mock`).
- Penyimpangan urutan (S-10): TC dikelompokkan per akun (Hendra Wibowo: 150, 152, 462, 463, 464, 465; Budi Santoso: 151, 209, 210, 228, 229, 252, 253) dengan ganti akun eksplisit (S-07); dalam akun, Submit ditaruh sebelum aksi lain dan Edit, Cancel, lalu Resubmit mengikuti nomor TC.
- Baris target (R-16): transaksi di List (Edit, Cancel Allocation, Resubmit) ditemukan lewat Search Allocation ID yang dicatat saat fixture sebagai langkah penghubung tanpa `Verifikasi`; langkah ini tidak diberi nomor sendiri.
- Penggunaan ulang transaksi (S-04, S-06): tiap TC kegagalan membiarkan state transaksi tidak berubah (diasersi per blok), sehingga satu transaksi Waiting for Approval dipakai berurutan oleh blok 462 sampai 465 dan oleh blok 209, 210, 228, 229, dan satu transaksi Canceled oleh blok 252 dan 253; baseline dicatat sekali per kelompok transaksi (langkah 31, 110, 129) dan dibandingkan dengan state setelah tiap kegagalan.
- Intercept dilepas segera sesudah pemicu (S-09); form yang tersisa dirty sesudah kegagalan ditutup deterministik dengan `[×]`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]` (S-08, tidak perlu dicatat lagi); dialog `Cancel Allocation` pada TC-AC-ACHA-229 ditutup tanpa membatalkan.
- Langkah penghubung (S-03): langkah baseline (1, 31, 65, 81, 110, 129), langkah baca state lewat fixture baca ("disediakan tim FE/BE", S-11, S-13), langkah memasang dan melepas intercept, langkah ganti akun (S-07), dan langkah menutup dialog `Cancel Allocation` lewat `[Go Back]` pada TC-AC-ACHA-229.
- Asersi tambahan di luar Expected TC: tidak ada selain pembacaan state lewat fixture baca untuk Expected yang menyebut status, Quantity, Reserved, atau jumlah baris.
- Pengecualian S-12 nama literal (Lampiran A butir A-6): Notes `Batch uji` dan `Batch lama`, serta Rejection Reason `Stok belum siap`, ditulis persis seperti TC.
- Ukuran spec: 154 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (b, resilience tulis) dan tiap blok berdiri sendiri dengan state tidak berubah sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah baseline, baca ulang state, dan penutupan form dirty menambah langkah tanpa interaksi baru.
- Temuan untuk QA:
  - TC-AC-ACHA-150 sampai 152, 252, 253 memakai Category `Hardware - BLE Gateway` sedangkan TC lain memakai `TAG - BLE`; spec mengikuti TC.
  - TC-AC-ACHA-464 b dan 465 b ("keputusan dapat diulang") tidak memberi cara mengamati; spec mengasersi tombol `[Approve]` atau `[Reject]` tetap tersedia pada transaksi itu.
  - TC-AC-ACHA-229 b ("dialog dapat dicoba ulang") tidak menyebut cara mengamati; spec mengasersi dialog `Cancel Allocation` masih terbuka.
  - TC-AC-ACHA-152 b menyebut copy toast Deviasi T-15 sebagai asersi; tidak ada penyimpangan lain.
  - TC-AC-ACHA-462 sampai 465 tidak menyebut apakah modal Review Approvals tetap terbuka sesudah toast; spec tidak mengasersinya.
  - TC-AC-ACHA-209 dan 210 tidak menyebut apakah Reserved dibaca lewat Wallet Balance atau fixture; spec memakai fixture baca.
  - Post Condition TC-AC-ACHA-150 sampai 152, 209, 210, 228, 229, 252, 253, 462 sampai 465 ("-") tidak ada.
