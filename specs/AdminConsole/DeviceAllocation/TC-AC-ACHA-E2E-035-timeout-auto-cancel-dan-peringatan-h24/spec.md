---
id: TC-AC-ACHA-E2E-035-timeout-auto-cancel-dan-peringatan-h24
title: "Timeout Auto-Cancel, Peringatan H-24, dan Recalculate Approval Timeout dengan Manipulasi Jam Server"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-266
  - TC-AC-ACHA-267
  - TC-AC-ACHA-268
  - TC-AC-ACHA-269
  - TC-AC-ACHA-270
  - TC-AC-ACHA-271
  - TC-AC-ACHA-272
  - TC-AC-ACHA-273
  - TC-AC-ACHA-274
  - TC-AC-ACHA-275
  - TC-AC-ACHA-276
  - TC-AC-ACHA-277
  - TC-AC-ACHA-280
  - TC-AC-ACHA-281
coverage:
  web: automated
---

# Timeout Auto-Cancel, Peringatan H-24, dan Recalculate Approval Timeout dengan Manipulasi Jam Server

## Prerequisites

- Mode: FE+BE.
- Akun (password lewat env, nama baru didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login MB_ON di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Akun lain dipakai lewat Step ganti akun eksplisit.

| Alias | Pre-setup | Email | Env password | Dipakai di |
|---|---|---|---|---|
| MB_ON | #32 Group Member Distributor toggle ON (pembuat) | `memberOnDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_ON_PASSWORD` | semua blok kecuali TC-281 |
| TC_DIST | #27 Total Control Distributor (approver aktif) | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` | TC-266, 269 sampai 272, 275, 276, 281 |
| GM_DIST | #29 Group Manager Group Jakarta (approver aktif) | `groupManagerDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_GM_DIST_PASSWORD` | TC-270 |
| TC_PRIN | #21 Total Control Principal (penyimpan Approval Timeout) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_PRIN_PASSWORD` | TC-272, 274, 275, 276, 277 lewat sesi API |

- Data Pre-setup yang dibaca: Distributor PT Global Distribusi (#3), Client PT Sejahtera Logistik (#7), harga (#14), kantong PT Global Distribusi $20,000.00 (#16), Approval Timeout platform-wide 3 day(s) (#63).
- Data seed milik spec (seeding API di langkah penyiapan tiap blok, mekanisme disediakan tim FE/BE; Allocation ID ditangkap saat runtime). Timeout Auto-Cancel mengubah status permanen sehingga tiap blok memakai transaksi sendiri:
  - Transaksi W: transaksi Waiting for Approval milik MB_ON dengan atribut Pre-setup #49 (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00), dibuat pada waktu T1 (T1 dibaca dari waktu pembuatan oleh seeding, bagian 8b butir 3), Approval Timeout 3 day(s), kantong PT Global Distribusi saldo $20,000.00 dengan Reserved $250.00, untuk TC-266 sampai 276.
  - Untuk TC-277: transaksi Canceled manual milik MB_ON dengan atribut #52 (BLE Gateway, Quantity 50, Pay From `PT ABC (Principal)`, Notes `Batch lama`, Total Cost $100.00).
  - Untuk TC-280: transaksi milik MB_ON berstatus Completed (atribut #55), Rejected (atribut #54), dan Canceled (atribut #52).
  - Untuk TC-281: transaksi Completed jalur langsung milik TC_DIST (Pre-setup #59; atribut kategori, Quantity, dan Cost tidak dirinci TC).
  - Untuk TC-272: Approval Timeout `1` day(s) disimpan TC_PRIN lewat sesi API (Pre-setup #20, langkah 124) dan dipulihkan ke `3` day(s) pada langkah 139; kantong PT Global Distribusi saldo $20,000.00 (Pre-setup #16). Data Dinamis: satu transaksi Waiting for Approval dibuat spec lewat form (BLE Gateway, Quantity `5`, Client `PT Sejahtera Logistik`, Pay From default form) pada langkah 127 sampai 131. Efek: Reserve pada kantong PT Global Distribusi; modul tanpa Delete sehingga transaksi tidak dihapus dan dibatalkan fixture Pre-setup #20 di hook `after` (Lampiran A butir A-6).
  - Nilai literal `Batch uji` dan `Batch lama` diasersi TC (pengecualian S-12 nama literal, Lampiran A butir A-6).
- Kemampuan teknis (disediakan tim FE/BE, kontrak fixture tidak tertulis di TC): fixture API Pre-setup #20 untuk (a) mengatur jam server absolut, membekukan jam server pada waktu tertentu, dan memulihkannya, (b) menyetel saldo dan Reserved kantong, (c) membaca status transaksi, jumlah entri Allocation Log, dan status job; kueri status job fixture dipakai sebagai langkah "Tunggu satu siklus job pengecekan selesai" (bagian 6: di atas 30 detik hanya lewat kueri status job); (d) sesi API TC_PRIN untuk menyimpan Approval Timeout dan memulihkannya ke 3 day(s) (TC menyebut penyimpanan lewat Plans & Licensing > Lifecycle Settings > Approval Settings; objek uji TC-274 sampai 277 adalah efek recalculation, bukan halaman pengaturan); (e) pembacaan jumlah notifikasi berjudul tertentu per akun lewat sesi API aktor (baseline); (f) sesi login UI dan sesi API tetap valid selama jam server digeser.
- Jam yang diatur: jam server dan jam browser diatur bersama, absolut dari T1 (bukan relatif), dan dipulihkan ke waktu nyata sebelum akun membuka halaman List, Wallet Balance, Allocation Log, atau Notification Center (S-09). Pengecualian: pada blok TC-273 jam server tetap bergeser selama Edit karena Edit harus terjadi pada T1 + 2 hari. Margin terhadap batas 1 menit (kurang dari 5 menit): T1 dihitung dari waktu terbit transaksi sehingga batas T1 + 3 hari + 1 menit tidak bergantung pada waktu hook. TC-268 (tepat di deadline) memakai jam server dibekukan pada tepat T1 + 3 hari selama job berjalan.
- State global yang diubah dan pemulihannya: jam server dan jam browser, Approval Timeout platform-wide (3 day(s)), saldo dan Reserved kantong; dipulihkan di akhir tiap blok dan di hook `after`. Suite berjalan serial (`parallel: false`).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Device Allocation true untuk akun aktor, sesi API aktor, fixture API Pre-setup #20.

## Test Steps

### Timeout Auto-Cancel setelah deadline (TC-AC-ACHA-266)

1. Siapkan transaksi W (T1 = waktu pembuatan) dan catat Last Updated transaksi (LU0)
2. Ketik Search Allocation ID transaksi W, tekan Enter
3. Atur jam server dan jam browser ke T1 + 3 hari + 1 menit
4. Tunggu satu siklus job pengecekan selesai
5. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
6. Verifikasi Status transaksi `Canceled` (Timeout Auto-Cancel)
7. Buka Wallet Balance kantong PT Global Distribusi
8. Verifikasi Reserved $0.00 (Release)
9. Verifikasi saldo tetap $20,000.00
10. Buka modal Allocation Log transaksi
11. Verifikasi entri `Allocation auto-canceled` tanpa nama user
12. Verifikasi Description `Reason: Approval timeout` pada entri tersebut
13. Tutup modal, lalu buka menu row action `⋯` transaksi
14. Verifikasi menu memuat `Allocation Log` dan `Resubmit`
15. Tutup menu dengan Esc
16. Ganti akun ke TC_DIST: Logout, login dengan `Spectra.env.AC_DA_TC_DIST_PASSWORD`, buka Approvals > Device Allocation > Active Tab
17. Ketik Search Allocation ID transaksi W, tekan Enter
18. Verifikasi Tab Active tampil
19. Verifikasi subject transaksi tidak ada pada Active Tab milik TC_DIST
20. Ganti akun ke MB_ON: Logout, login dengan `Spectra.env.AC_DA_MB_ON_PASSWORD`, buka Allocation > Device Allocation
21. Ketik Search Allocation ID transaksi W, tekan Enter
22. Verifikasi Last Updated transaksi berubah dari LU0 dan sama dengan Date entri `Allocation auto-canceled` terbaru

### Sebelum deadline belum dibatalkan (TC-AC-ACHA-267)

23. Siapkan transaksi W
24. Ganti isi kotak search dengan Allocation ID transaksi W, tekan Enter
25. Atur jam server dan jam browser ke T1 + 2 hari 23 jam 59 menit
26. Tunggu satu siklus job pengecekan selesai
27. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
28. Verifikasi Status transaksi tetap `Waiting for Approval`
29. Buka Wallet Balance kantong PT Global Distribusi
30. Verifikasi Reserved tetap $250.00

### Tepat di titik deadline belum dibatalkan (TC-AC-ACHA-268)

31. Siapkan transaksi W
32. Ganti isi kotak search dengan Allocation ID transaksi W, tekan Enter
33. Bekukan jam server pada tepat T1 + 3 hari dan atur jam browser ke waktu yang sama
34. Tunggu satu siklus job pengecekan selesai
35. Lepas pembekuan, pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
36. Verifikasi Status transaksi tetap `Waiting for Approval` (pembatalan hanya bila batas waktu terlampaui)

### Edit tidak me-reset batas waktu (TC-AC-ACHA-273)

37. Siapkan transaksi W
38. Ganti isi kotak search dengan Allocation ID transaksi W, tekan Enter
39. Atur jam server dan jam browser ke T1 + 2 hari
40. Tunggu satu siklus job pengecekan selesai
41. Buka menu row action `⋯` transaksi, klik `Edit`, ubah Quantity menjadi `120`, lalu klik `[Save]`
42. Tunggu aksi selesai (modal Edit tertutup)
43. Atur jam server dan jam browser ke T1 + 3 hari + 1 menit
44. Tunggu satu siklus job pengecekan selesai
45. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
46. Verifikasi Status transaksi `Canceled` (dibatalkan pada T1 + 3 hari, bukan 3 hari setelah Edit)
47. Buka Wallet Balance kantong PT Global Distribusi
48. Verifikasi Reserved $0.00

### Perubahan Approval Timeout menghitung ulang batas waktu (TC-AC-ACHA-274)

49. Siapkan transaksi W
50. Ganti isi kotak search dengan Allocation ID transaksi W, tekan Enter
51. TC_PRIN (sesi API) menyimpan Approval Timeout `5` day(s) hingga tersimpan
52. Atur jam server dan jam browser ke T1 + 3 hari + 1 menit
53. Tunggu satu siklus job pengecekan selesai
54. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
55. Verifikasi Status transaksi tetap `Waiting for Approval` (batas waktu dihitung ulang menjadi T1 + 5 hari)
56. Atur jam server dan jam browser ke T1 + 5 hari + 1 menit
57. Tunggu satu siklus job pengecekan selesai
58. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
59. Verifikasi Status transaksi `Canceled`
60. Pulihkan Approval Timeout menjadi `3` day(s) lewat sesi API TC_PRIN

### Resubmit memakai Approval Timeout saat Submit (TC-AC-ACHA-277)

61. Siapkan transaksi Canceled milik MB_ON (atribut #52); TC_PRIN (sesi API) menyimpan Approval Timeout `5` day(s) hingga tersimpan
62. Ganti isi kotak search dengan Allocation ID transaksi Canceled milik MB_ON (atribut #52), tekan Enter
63. Klik `Resubmit` pada transaksi Canceled, lalu klik `[Submit]`
64. Tunggu aksi selesai (form Resubmit tertutup), lalu catat T1 baru (waktu pembuatan transaksi baru) dan Allocation ID-nya lewat fixture
65. Ganti isi kotak search dengan Allocation ID transaksi baru hasil Resubmit, tekan Enter
66. Atur jam server dan jam browser ke T1 baru + 3 hari + 1 menit
67. Tunggu satu siklus job pengecekan selesai
68. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
69. Verifikasi Status transaksi baru tetap `Waiting for Approval`
70. Atur jam server dan jam browser ke T1 baru + 5 hari + 1 menit
71. Tunggu satu siklus job pengecekan selesai
72. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
73. Verifikasi Status transaksi baru `Canceled`
74. Pulihkan Approval Timeout menjadi `3` day(s) lewat sesi API TC_PRIN

### Timeout tidak mengubah transaksi berstatus akhir (TC-AC-ACHA-280)

75. Siapkan transaksi Completed (atribut #55), Rejected (atribut #54), dan Canceled (atribut #52) milik MB_ON; catat jumlah entri Allocation Log tiap transaksi (C1, C2, C3) lewat fixture
76. Atur jam server dan jam browser ke 30 hari setelah transaksi yang paling akhir dibuat
77. Tunggu satu siklus job pengecekan selesai
78. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
79. Ganti isi kotak search dengan Allocation ID transaksi Completed (atribut #55), tekan Enter
80. Verifikasi Status transaksi Completed tetap `Completed`
81. Buka modal Allocation Log transaksi Completed
82. Verifikasi jumlah entri log transaksi Completed sama dengan C1 (tidak ada entri log baru)
83. Tutup modal
84. Ganti isi kotak search dengan Allocation ID transaksi Rejected (atribut #54), tekan Enter
85. Verifikasi Status transaksi Rejected tetap `Rejected`
86. Buka modal Allocation Log transaksi Rejected
87. Verifikasi jumlah entri log transaksi Rejected sama dengan C2 (tidak ada entri log baru)
88. Tutup modal
89. Ganti isi kotak search dengan Allocation ID transaksi Canceled (atribut #52), tekan Enter
90. Verifikasi Status transaksi Canceled tetap `Canceled`
91. Buka modal Allocation Log transaksi Canceled
92. Verifikasi jumlah entri log transaksi Canceled sama dengan C3 (tidak ada entri log baru)
93. Tutup modal

### Belum ada peringatan H-24 sebelum 24 jam menjelang deadline (TC-AC-ACHA-269)

94. Siapkan transaksi W; catat jumlah notifikasi berjudul "Please finish this approval — expiring soon" milik TC_DIST (P0) dan "Your request is expiring soon" milik MB_ON (F0) lewat sesi API
95. Atur jam server dan jam browser ke T1 + 1 hari 23 jam 59 menit
96. Tunggu satu siklus job pengecekan selesai
97. Pulihkan jam server dan jam browser ke waktu nyata, lalu buka Notification Center MB_ON
98. Verifikasi jumlah notifikasi "Your request is expiring soon" sama dengan F0 (belum ada notifikasi peringatan untuk pembuat)
99. Ganti akun ke TC_DIST: Logout, login dengan `Spectra.env.AC_DA_TC_DIST_PASSWORD`, buka Notification Center
100. Verifikasi jumlah notifikasi "Please finish this approval — expiring soon" sama dengan P0 (belum ada notifikasi peringatan untuk approver)

### Peringatan H-24 ke approver aktif dan FYI ke pembuat (TC-AC-ACHA-270)

101. Siapkan transaksi W (approver aktif: TC_DIST dan GM_DIST); catat jumlah notifikasi "Please finish this approval — expiring soon" milik TC_DIST (P0) dan GM_DIST (G0) serta "Your request is expiring soon" milik MB_ON (F0) lewat sesi API
102. Atur jam server dan jam browser ke T1 + 2 hari
103. Tunggu satu siklus job pengecekan selesai
104. Pulihkan jam server dan jam browser ke waktu nyata, lalu buka Notification Center TC_DIST
105. Verifikasi jumlah notifikasi `actionable` "Please finish this approval — expiring soon" milik TC_DIST sama dengan P0 + 1
106. Verifikasi notifikasi tersebut memuat tombol aksi menuju antrean Approvals
107. Ganti akun ke GM_DIST: Logout, login dengan `Spectra.env.AC_DA_GM_DIST_PASSWORD`, buka Notification Center
108. Verifikasi jumlah notifikasi `actionable` "Please finish this approval — expiring soon" milik GM_DIST sama dengan G0 + 1
109. Verifikasi notifikasi tersebut memuat tombol aksi menuju antrean Approvals
110. Ganti akun ke MB_ON: Logout, login dengan `Spectra.env.AC_DA_MB_ON_PASSWORD`, buka Notification Center
111. Verifikasi jumlah notifikasi FYI `view-only` "Your request is expiring soon" milik MB_ON sama dengan F0 + 1
112. Buka Allocation > Device Allocation
113. Ketik Search Allocation ID transaksi W, tekan Enter
114. Verifikasi Status transaksi tetap `Waiting for Approval`

### Peringatan H-24 idempoten (TC-AC-ACHA-271)

115. Siapkan transaksi W; catat jumlah notifikasi "Please finish this approval — expiring soon" milik TC_DIST (P0) dan "Your request is expiring soon" milik MB_ON (F0) lewat sesi API
116. Atur jam server dan jam browser ke T1 + 2 hari 6 jam
117. Tunggu satu siklus job pengecekan selesai
118. Atur jam server dan jam browser ke T1 + 2 hari 12 jam
119. Tunggu satu siklus job pengecekan selesai
120. Pulihkan jam server dan jam browser ke waktu nyata, lalu buka Notification Center MB_ON
121. Verifikasi jumlah notifikasi "Your request is expiring soon" sama dengan F0 + 1 (tidak berulang tiap siklus job)
122. Ganti akun ke TC_DIST: Logout, login dengan `Spectra.env.AC_DA_TC_DIST_PASSWORD`, buka Notification Center
123. Verifikasi jumlah notifikasi "Please finish this approval — expiring soon" sama dengan P0 + 1 (tidak berulang tiap siklus job)

### Approval Timeout minimum 1 hari: peringatan terkirim segera (TC-AC-ACHA-272)

124. TC_PRIN (sesi API) menyimpan Approval Timeout `1` day(s) hingga tersimpan; catat jumlah notifikasi "Please finish this approval — expiring soon" milik TC_DIST (P0) dan "Your request is expiring soon" milik MB_ON (F0) lewat sesi API
125. Ganti akun ke MB_ON: Logout, login dengan `Spectra.env.AC_DA_MB_ON_PASSWORD`, buka Allocation > Device Allocation
126. Catat total baris transaksi pada List (B)
127. Klik `[+ Allocation]`
128. Pilih Category `Hardware - BLE Gateway`
129. Pilih Client `PT Sejahtera Logistik`
130. Isi Quantity `5`
131. Klik `[Submit]`
132. Verifikasi total baris pada List bertambah satu dari B (langkah 126)
133. Verifikasi transaksi baru pada baris teratas List berstatus `Waiting for Approval`
134. Tunggu satu siklus job pengecekan selesai
135. Buka Notification Center MB_ON
136. Verifikasi jumlah notifikasi FYI "Your request is expiring soon" sama dengan F0 + 1
137. Ganti akun ke TC_DIST: Logout, login dengan `Spectra.env.AC_DA_TC_DIST_PASSWORD`, buka Notification Center
138. Verifikasi jumlah notifikasi `actionable` "Please finish this approval — expiring soon" sama dengan P0 + 1
139. Pulihkan Approval Timeout menjadi `3` day(s) lewat sesi API TC_PRIN

### Recalculate dengan deadline yang sudah lewat memakai grace 24 jam (TC-AC-ACHA-275)

140. Siapkan transaksi W
141. Atur jam server dan jam browser ke T1 + 2 hari
142. Tunggu satu siklus job pengecekan selesai (peringatan H-24 awal terkirim)
143. Catat jumlah notifikasi "Please finish this approval — expiring soon" milik TC_DIST (P0) dan "Your request is expiring soon" milik MB_ON (F0) lewat sesi API
144. TC_PRIN (sesi API) menyimpan Approval Timeout `1` day(s) pada T1 + 2 hari hingga tersimpan
145. Tunggu satu siklus job pengecekan selesai
146. Pulihkan jam server dan jam browser ke waktu nyata, lalu ganti akun ke MB_ON: Logout, login dengan `Spectra.env.AC_DA_MB_ON_PASSWORD`, muat ulang List
147. Ketik Search Allocation ID transaksi W, tekan Enter
148. Verifikasi Status transaksi tetap `Waiting for Approval` (tidak ada pembatalan instan; deadline efektif Save + 24 jam)
149. Buka Notification Center MB_ON
150. Verifikasi jumlah notifikasi "Your request is expiring soon" sama dengan F0 + 1 (peringatan H-24 dikirim ulang ke pembuat)
151. Ganti akun ke TC_DIST: Logout, login dengan `Spectra.env.AC_DA_TC_DIST_PASSWORD`, buka Notification Center
152. Verifikasi jumlah notifikasi "Please finish this approval — expiring soon" sama dengan P0 + 1 (peringatan H-24 dikirim ulang ke approver aktif)
153. Atur jam server dan jam browser ke T1 + 3 hari + 1 menit (Save + 24 jam + 1 menit)
154. Tunggu satu siklus job pengecekan selesai
155. Pulihkan jam server dan jam browser ke waktu nyata, lalu buka Allocation > Device Allocation
156. Ketik Search Allocation ID transaksi W, tekan Enter
157. Verifikasi Status transaksi `Canceled`
158. Pulihkan Approval Timeout menjadi `3` day(s) lewat sesi API TC_PRIN

### Recalculate yang mendekatkan deadline mengirim ulang peringatan H-24 (TC-AC-ACHA-276)

159. Siapkan transaksi W
160. Atur jam server dan jam browser ke T1 + 2 hari
161. Tunggu satu siklus job pengecekan selesai (peringatan H-24 untuk deadline lama terkirim)
162. Catat jumlah notifikasi "Please finish this approval — expiring soon" milik TC_DIST (P0) dan "Your request is expiring soon" milik MB_ON (F0) lewat sesi API
163. Atur jam server dan jam browser ke T1 + 2 hari 12 jam
164. TC_PRIN (sesi API) menyimpan Approval Timeout `1` day(s) hingga tersimpan
165. Tunggu satu siklus job pengecekan selesai
166. Pulihkan jam server dan jam browser ke waktu nyata, lalu buka Notification Center TC_DIST
167. Verifikasi jumlah notifikasi "Please finish this approval — expiring soon" sama dengan P0 + 1 (dikirim ulang segera ke approver aktif)
168. Ganti akun ke MB_ON: Logout, login dengan `Spectra.env.AC_DA_MB_ON_PASSWORD`, buka Notification Center
169. Verifikasi jumlah notifikasi "Your request is expiring soon" sama dengan F0 + 1 (dikirim ulang segera ke pembuat)
170. Pulihkan Approval Timeout menjadi `3` day(s) lewat sesi API TC_PRIN

### Jalur langsung tidak memiliki batas waktu persetujuan (TC-AC-ACHA-281)

171. Ganti akun ke TC_DIST: Logout, login dengan `Spectra.env.AC_DA_TC_DIST_PASSWORD`, buka Allocation > Device Allocation
172. Siapkan transaksi Completed (jalur langsung) milik TC_DIST (T1 = waktu pembuatan); catat jumlah notifikasi "Please finish this approval — expiring soon" milik TC_DIST (P0) lewat sesi API
173. Ketik Search Allocation ID transaksi Completed jalur langsung milik TC_DIST, tekan Enter
174. Atur jam server dan jam browser ke T1 + 5 hari
175. Tunggu satu siklus job pengecekan selesai
176. Pulihkan jam server dan jam browser ke waktu nyata, lalu muat ulang List
177. Verifikasi Status transaksi tetap `Completed`
178. Buka Notification Center TC_DIST
179. Verifikasi jumlah notifikasi "Please finish this approval — expiring soon" sama dengan P0 (tidak ada peringatan H-24)

## Notes

- Langkah penghubung (S-03, R-16): Search Allocation ID transaksi blok sebelum langkah yang membaca List ("Ganti isi kotak search dengan" bila kotak Search masih berisi, 8b butir 9), mencatat baseline total baris (B), menyiapkan seed dan state lewat fixture, mencatat baseline (LU0, C1 sampai C3, P0, G0, F0), mengatur dan memulihkan jam, menunggu job, memulihkan Approval Timeout, menutup modal dan menu, serta Step ganti akun (Logout, login) tidak punya `Verifikasi`.
- Anchor absence (bagian 8b butir 2): "subject hilang dari Approvals Active Tab" (TC-266) didahului `Verifikasi` Tab Active tampil dan diamati oleh TC_DIST (approver aktif, langkah uji ketiga TC) lewat ganti akun pada langkah 16 dan kembali ke MB_ON pada langkah 20 (S-07), karena pembuat MB_ON tidak melihat transaksinya sendiri di tab itu (TC-263); "belum ada notifikasi" dan "tidak berulang" diasersi sebagai selisih jumlah terhadap baseline (S-12), bukan absence tanpa anchor; "tidak ada entri log baru" (TC-280) diasersi sebagai jumlah entri sama dengan baseline karena aksinya (siklus job) ada di alur spec. Spec ini tidak berisi asersi kelas g. `Verifikasi` transaksi baru berstatus `Waiting for Approval` pada TC-272 adalah anchor positif bahwa Submit selesai sebelum notifikasi dibaca (S-03).
- Urutan blok geser jam (S-10): seluruh blok kecuali TC-272 dan TC-281 menggeser jam server karena objek ujinya job latar dan jam server (kelas d), sehingga tidak ada blok geser jam yang dapat dipindah ke akhir spec. Pergeseran jam satu blok dapat mengenai transaksi Waiting for Approval sisa blok sebelumnya (batas Timeout dan peringatan H-24 dihitung server untuk semua transaksi Waiting); asersi karena itu memakai Allocation ID transaksi W blok masing-masing (Search) dan baseline notifikasi per blok (P0, G0, F0). TC tidak menyatakan isolasi transaksi Waiting sisa terhadap pergeseran jam; kontrak fixture untuk itu tidak tertulis dan dicatat sebagai temuan.
- Kelas d (prinsip 13): seluruh blok berobjek uji job latar dan jam server; manipulasi jam bersama server dan browser (bagian 6). Penggeseran jam diatur absolut dari T1 dan dipulihkan sebelum UI dibuka kecuali Edit pada TC-273 yang wajib terjadi pada T1 + 2 hari. Pelaku TC_PRIN adalah sesi API pemicu state (bagian 3 P-2: pelaku kedua lewat sesi API tidak butuh butir Notes) dan Approval Timeout dipulihkan di akhir tiap blok yang mengubahnya.
- Urutan TC tidak mengikuti nomor TC: blok tanpa pembacaan notifikasi (TC-266 sampai 268, 273, 274, 277, 280) dikerjakan lebih dulu sebagai MB_ON, lalu blok notifikasi (TC-269 sampai 272, 275, 276) dan TC-281 dengan ganti akun yang diatur berurutan agar jumlah ganti akun minimal. TC-272 (Submit lewat form) dikerjakan sebagai MB_ON setelah Approval Timeout 1 day(s) disimpan.
- Alasan di atas 35 langkah: seluruh blok satu kelas harness (d, job latar dan jam server), satu topik besar (siklus hidup batas waktu persetujuan), masing-masing memakai transaksi seed sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah Pulihkan jam dan Tunggu siklus job berulang di setiap blok (sama untuk semua blok). Ganti akun ditulis eksplisit karena pembacaan Notification Center per akun tidak dapat dilakukan dari satu sesi.
- Penggabungan akun: pembacaan List/status pada TC-275 langkah akhir dilakukan oleh TC_DIST (akun aktif saat itu); TC mengasumsikan pembuat, tetapi Total Control Distributor melihat List entitasnya.
- Temuan untuk QA:
  - TC-276 Expected tidak menyebut nilai Approval Timeout yang menghasilkan "sisa waktu kurang dari 24 jam" dan dengan aturan grace TL-09 (TC-275) sisa waktu setelah recalculate adalah tepat 24 jam, bukan kurang; spec memakai Approval Timeout `1` day(s) pada T1 + 2 hari 12 jam. Precondition d TC-276 ("peringatan H-24 untuk deadline lama sudah terkirim") hanya dapat dipenuhi dengan jam digeser lewat T1 + 2 hari.
  - TC-266 sampai 276 menulis "langkah tunggu satu siklus job pengecekan (kelas timing eventual)" tanpa durasi siklus; spec membaca selesainya siklus lewat kueri status job fixture (disediakan tim BE).
  - TC-274, 275, 276, 277 menyebut Principal menyimpan Approval Timeout lewat UI; spec memakai sesi API TC_PRIN sebagai pemicu karena objek uji adalah efek recalculation. Kontrak fixture dan sesi API tidak ada di TC, PRD, atau LLD (S-13).
  - TC-272 langkah 1 "Submit alokasi BLE Gateway Quantity 5" tidak menyebut Pay From; spec mengikuti default form.
  - Isolasi transaksi Waiting for Approval sisa blok sebelumnya terhadap pergeseran jam (notifikasi H-24 dan Timeout ikut berlaku untuk transaksi sisa) tidak dinyatakan TC; hitungan notifikasi per blok memakai baseline (P0, G0, F0) dan hanya valid bila fixture mengisolasi atau membatalkan transaksi sisa.
  - TC-281: atribut seed Pre-setup #59 tidak dirinci; TC tidak menyebut notifikasi yang dicek selain "tidak ada peringatan H-24", sehingga spec membaca Title approver milik TC_DIST.
  - TC-270 butir a menyebut "approver aktif: Total Control Distributor dan Group Manager Group Jakarta" tetapi tombol aksi tidak dirinci labelnya; spec hanya mengasersi keberadaan tombol aksi menuju antrean Approvals.
  - Post Condition TC-273, 274, 275, 277, dan 280 (Wallet, Approvals Active Tab, Dashboard, notifikasi) yang tidak punya langkah observasi di TC tidak diasersi, kecuali yang punya Expected padanan.
  - TC-266 butir d "Last Updated berubah ke waktu kejadian Timeout" tidak menyatakan toleransi; spec membandingkan dengan Date entri `Allocation auto-canceled` terbaru (kolom Date log berketelitian menit).
