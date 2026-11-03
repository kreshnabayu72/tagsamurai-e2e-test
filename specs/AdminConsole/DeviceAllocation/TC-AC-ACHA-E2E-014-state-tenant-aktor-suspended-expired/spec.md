---
id: TC-AC-ACHA-E2E-014-state-tenant-aktor-suspended-expired
title: "State Tenant: Aksi Tulis Ditolak Saat Entitas Aktor Suspended atau Expired, Timeout Tetap Berjalan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-80
  - TC-AC-ACHA-81
  - TC-AC-ACHA-82
  - TC-AC-ACHA-83
  - TC-AC-ACHA-84
  - TC-AC-ACHA-85
  - TC-AC-ACHA-86
  - TC-AC-ACHA-87
  - TC-AC-ACHA-88
  - TC-AC-ACHA-278
  - TC-AC-ACHA-480
  - TC-AC-ACHA-481
  - TC-AC-ACHA-482
  - TC-AC-ACHA-483
  - TC-AC-ACHA-484
coverage:
  web: automated
---

# State Tenant: Aksi Tulis Ditolak Saat Entitas Aktor Suspended atau Expired, Timeout Tetap Berjalan

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

| TC | Akun | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-278, TC-484 | Total Control Principal PT ABC (pengguna entitas lain yang melihat transaksi) | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-80, TC-81, TC-85, TC-86, TC-87, TC-482, TC-483 | Total Control Distributor PT Global Distribusi (alias TC_DIST) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| TC-82, TC-83, TC-84, TC-88, TC-480, TC-481 | Group Member Distributor toggle ON (alias MB_ON, Budi Santoso) | #32 | `memberOnDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_ON_PASSWORD` |

- Login akun aktor pertama (Total Control Principal) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan status entitas PT Global Distribusi menjadi Active, memulihkan baseline transaksi dan jam server, serta mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite: sesi API aktor, flag Guided Tooltip, pemulihan preferensi Setup Column, seed 30 baris idempotent (Lampiran A butir A-6), dan fixture Pre-setup #20 dinyatakan di `suite.md` (endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Kelas harness: h (state tenant, write-lockdown entitas Suspended dan Expired). Spec ini kondisi data tersendiri (prinsip 12): tidak digabung dengan alur normal.
- Nilai literal: `Batch uji` (Notes transaksi #49) dan `Stok belum siap` (Rejection Reason) adalah nama batch dan nama stok seed yang sah sebagai literal menurut Lampiran A butir A-6; `Revisi catatan` adalah nilai input non-identitas (bukan Data Dinamis), sesuai Lampiran A butir A-6.
- Data Pre-setup yang dipakai: transaksi Waiting for Approval milik MB_ON (Pre-setup #49: RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi, Approval Timeout 3 day(s) per Pre-setup #63); transaksi Canceled milik MB_ON (Pre-setup #52, sumber Resubmit); kantong PT Global Distribusi saldo $20,000.00 (Pre-setup #16). Allocation ID Pre-setup #49 dan #52 serta waktu terbit T1 transaksi #49 dibaca lewat fixture seed (disediakan tim FE/BE), tidak di-hardcode.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak dikarang): fixture Pre-setup #20 untuk (a) mengatur status entitas PT Global Distribusi menjadi Active, Suspended, atau Expired setelah transaksi #49 dibuat, (b) memulihkan baseline transaksi #49 (Waiting for Approval, Quantity 100, Notes `Batch uji`) dan #52 (Canceled), serta kantong PT Global Distribusi (saldo $20,000.00, Reserved $250.00 untuk #49) dan membaca saldo dan Reserved kantong, (c) menggeser dan memulihkan jam server. Browser uji menangani dialog `beforeunload` secara otomatis pada muat ulang halaman (S-08). Penunggu job memakai idiom polling worker commit (muat ulang tiap 5 detik, batas 2 menit).
- Jam: hanya jam server yang digeser (Approval Timeout 3 hari dihitung murni di server dan tidak diamati lewat UI countdown). Jam server diset absolut ke T1 + 3 hari + 1 menit (T1 dibaca dari fixture seed; margin 1 menit di atas batas, bukan relatif terhadap waktu nyata) dan dipulihkan segera sesudah status Canceled terbaca dan di hook `after`.
- Kemampuan teknis (jam): sesi UI dan sesi API tetap valid selama jam server digeser (dinyatakan di `suite.md`).
- General Settings Pre-setup #1 tidak diubah.
- State global: status entitas PT Global Distribusi, jam server, baseline transaksi #49 dan #52, dan saldo kantong PT Global Distribusi diubah dan dipulihkan; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_DIST_PASSWORD` dan `AC_DA_MB_ON_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### Persiapan entitas Suspended

1. Pulihkan baseline lewat fixture Pre-setup #20: transaksi #49 Waiting for Approval (Quantity 100, Notes `Batch uji`), transaksi #52 Canceled, kantong PT Global Distribusi saldo $20,000.00 dan Reserved $250.00
2. Atur status entitas PT Global Distribusi menjadi Suspended lewat fixture Pre-setup #20

### TC-AC-ACHA-278: Timeout Auto-Cancel berjalan pada entitas Suspended (dilihat sebagai Total Control Principal)

3. Catat T1 (waktu terbit transaksi #49) dari fixture seed
4. Ketik Search `Allocation ID` transaksi #49, tekan Enter
5. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
6. Geser jam server ke T1 + 3 hari + 1 menit lewat fixture Pre-setup #20
7. Ulangi tiap 5 detik: muat ulang halaman, ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter, sampai baris transaksi #49 berstatus `Canceled` (batas tunggu 2 menit)
8. Pulihkan jam server ke waktu nyata lewat fixture Pre-setup #20
9. Verifikasi baris transaksi #49 berstatus `Canceled` (Timeout Auto-Cancel tetap berjalan pada entitas Suspended)
10. Verifikasi Reserved kantong PT Global Distribusi $0.00 (dibaca lewat fixture)
11. Klik `(←)` pada kotak Search

### Persiapan ulang entitas Suspended

12. Pulihkan baseline lewat fixture Pre-setup #20: transaksi #49 Waiting for Approval (Quantity 100, Notes `Batch uji`), transaksi #52 Canceled, kantong PT Global Distribusi saldo $20,000.00 dan Reserved $250.00
13. Atur status entitas PT Global Distribusi menjadi Suspended lewat fixture Pre-setup #20

### Ganti akun ke Total Control Distributor

14. Logout dari akun Total Control Principal
15. Login sebagai TC_DIST (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
16. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-80: Submit ditolak saat entitas aktor Suspended

17. Catat Allocation ID baris teratas List (baseline baris)
18. Klik `[+ Allocation]`
19. Pilih Category `TAG - BLE`
20. Pilih Client `PT Sejahtera Logistik`
21. Isi Quantity `5`
22. Klik `[Submit]`
23. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
24. Muat ulang halaman Allocation > Device Allocation (F5)
25. Verifikasi Allocation ID baris teratas List sama dengan baseline baris (tidak ada transaksi baru)
26. Verifikasi saldo kantong PT Global Distribusi $20,000.00 dan Reserved $250.00 tidak berubah (dibaca lewat fixture)

### TC-AC-ACHA-81: Tombol Allocation tidak dipengaruhi status entitas

27. Amati Table Tools
28. Verifikasi tombol `[+ Allocation]` tetap Show (tidak berubah oleh status entitas)

### TC-AC-ACHA-85: Approve ditolak saat entitas aktor Suspended

29. Buka Approvals > Device Allocation lewat sidebar
30. Buka transaksi #49
31. Klik `[Approve]`
32. Konfirmasi Approve pada dialog
33. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
34. Buka Allocation > Device Allocation lewat sidebar
35. Ketik Search `Allocation ID` transaksi #49, tekan Enter
36. Verifikasi transaksi #49 tetap `Waiting for Approval`
37. Verifikasi saldo yang di-Reserve tidak berubah: Reserved kantong PT Global Distribusi $250.00 (dibaca lewat fixture)
38. Klik `(←)` pada kotak Search

### TC-AC-ACHA-86: Reject ditolak saat entitas aktor Suspended

39. Buka Approvals > Device Allocation lewat sidebar
40. Tunggu toast error sebelumnya hilang
41. Buka transaksi #49
42. Isi Rejection Reason `Stok belum siap`
43. Klik `[Reject]`
44. Konfirmasi Reject pada dialog
45. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
46. Buka Allocation > Device Allocation lewat sidebar
47. Ketik Search `Allocation ID` transaksi #49, tekan Enter
48. Verifikasi transaksi #49 tetap `Waiting for Approval`
49. Verifikasi saldo yang di-Reserve tidak berubah: Reserved kantong PT Global Distribusi $250.00 (dibaca lewat fixture)
50. Klik `(←)` pada kotak Search

### Ganti akun ke Group Member Distributor (Suspended)

51. Logout dari akun TC_DIST
52. Login sebagai MB_ON (`memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_MB_ON_PASSWORD`)
53. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-82: Edit ditolak saat entitas aktor Suspended

54. Ketik Search `Allocation ID` transaksi #49, tekan Enter
55. Klik `[⋯]` pada baris hasil
56. Klik `Edit`
57. Ubah Quantity dari `100` menjadi `120`
58. Klik `[Save]`
59. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
60. Muat ulang halaman Allocation > Device Allocation (F5)
61. Ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter
62. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
63. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
64. Verifikasi Quantity baris transaksi #49 tetap `100`
65. Klik `(←)` pada kotak Search

### TC-AC-ACHA-83: Cancel ditolak saat entitas aktor Suspended

66. Ketik Search `Allocation ID` transaksi #49, tekan Enter
67. Klik `[⋯]` pada baris hasil
68. Klik `Cancel Allocation`
69. Klik `[Cancel Allocation]` pada dialog
70. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
71. Muat ulang halaman Allocation > Device Allocation (F5)
72. Ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter
73. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
74. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
75. Klik `(←)` pada kotak Search

### TC-AC-ACHA-84: Resubmit ditolak saat entitas aktor Suspended

76. Catat Allocation ID baris teratas List (baseline baris)
77. Ketik Search `Allocation ID` transaksi Canceled #52, tekan Enter
78. Klik `[⋯]` pada baris hasil
79. Klik `Resubmit`
80. Klik `[Submit]` tanpa mengubah isian
81. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
82. Klik `(←)` pada kotak Search, lalu muat ulang halaman Allocation > Device Allocation (F5)
83. Verifikasi Allocation ID baris teratas List sama dengan baseline baris (tidak ada transaksi baru)

### Persiapan entitas Expired

84. Pulihkan baseline lewat fixture Pre-setup #20: transaksi #49 Waiting for Approval (Quantity 100, Notes `Batch uji`), transaksi #52 Canceled, kantong PT Global Distribusi saldo $20,000.00 dan Reserved $250.00
85. Atur status entitas PT Global Distribusi menjadi Expired lewat fixture Pre-setup #20
86. Muat ulang halaman Allocation > Device Allocation (F5)
87. Klik header kolom `Column Visibility (⋯)`, klik `[Setup Column]`, tampilkan kolom Notes, lalu klik `[Save]`

### TC-AC-ACHA-88: Edit ditolak saat entitas aktor Expired

88. Ketik Search `Allocation ID` transaksi #49, tekan Enter
89. Klik `[⋯]` pada baris hasil
90. Klik `Edit`
91. Ubah Notes dari `Batch uji` menjadi `Revisi catatan`
92. Klik `[Save]`
93. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
94. Muat ulang halaman Allocation > Device Allocation (F5)
95. Ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter
96. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
97. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
98. Verifikasi Notes baris transaksi #49 tetap `Batch uji`
99. Klik `(←)` pada kotak Search

### TC-AC-ACHA-480: Cancel ditolak saat entitas aktor Expired

100. Ketik Search `Allocation ID` transaksi #49, tekan Enter
101. Klik `[⋯]` pada baris hasil
102. Klik `Cancel Allocation`
103. Klik `[Cancel Allocation]` pada dialog
104. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
105. Muat ulang halaman Allocation > Device Allocation (F5)
106. Ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter
107. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
108. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
109. Klik `(←)` pada kotak Search

### TC-AC-ACHA-481: Resubmit ditolak saat entitas aktor Expired

110. Catat Allocation ID baris teratas List (baseline baris)
111. Ketik Search `Allocation ID` transaksi Canceled #52, tekan Enter
112. Klik `[⋯]` pada baris hasil
113. Klik `Resubmit`
114. Klik `[Submit]` tanpa mengubah isian
115. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
116. Klik `(←)` pada kotak Search, lalu muat ulang halaman Allocation > Device Allocation (F5)
117. Verifikasi Allocation ID baris teratas List sama dengan baseline baris (tidak ada transaksi baru)

### Ganti akun ke Total Control Distributor (Expired)

118. Logout dari akun MB_ON
119. Login sebagai TC_DIST (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
120. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-87: Submit ditolak saat entitas aktor Expired

121. Catat Allocation ID baris teratas List (baseline baris)
122. Klik `[+ Allocation]`
123. Pilih Category `TAG - BLE`
124. Pilih Client `PT Sejahtera Logistik`
125. Isi Quantity `5`
126. Klik `[Submit]`
127. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." (satu copy untuk Suspended dan Expired)
128. Muat ulang halaman Allocation > Device Allocation (F5)
129. Verifikasi Allocation ID baris teratas List sama dengan baseline baris (tidak ada transaksi baru)

### TC-AC-ACHA-482: Approve ditolak saat entitas aktor Expired

130. Buka Approvals > Device Allocation lewat sidebar
131. Buka transaksi #49
132. Klik `[Approve]`
133. Konfirmasi Approve pada dialog
134. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
135. Buka Allocation > Device Allocation lewat sidebar
136. Ketik Search `Allocation ID` transaksi #49, tekan Enter
137. Verifikasi transaksi #49 tetap `Waiting for Approval`
138. Verifikasi saldo yang di-Reserve tidak berubah: Reserved kantong PT Global Distribusi $250.00 (dibaca lewat fixture)
139. Klik `(←)` pada kotak Search

### TC-AC-ACHA-483: Reject ditolak saat entitas aktor Expired

140. Buka Approvals > Device Allocation lewat sidebar
141. Tunggu toast error sebelumnya hilang
142. Buka transaksi #49
143. Isi Rejection Reason `Stok belum siap`
144. Klik `[Reject]`
145. Konfirmasi Reject pada dialog
146. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
147. Buka Allocation > Device Allocation lewat sidebar
148. Ketik Search `Allocation ID` transaksi #49, tekan Enter
149. Verifikasi transaksi #49 tetap `Waiting for Approval`
150. Verifikasi saldo yang di-Reserve tidak berubah: Reserved kantong PT Global Distribusi $250.00 (dibaca lewat fixture)
151. Klik `(←)` pada kotak Search

### Ganti akun ke Total Control Principal (Expired)

152. Logout dari akun TC_DIST
153. Login sebagai Total Control Principal (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
154. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-484: Timeout Auto-Cancel berjalan pada entitas Expired (dilihat sebagai Total Control Principal)

155. Catat T1 (waktu terbit transaksi #49) dari fixture seed
156. Ketik Search `Allocation ID` transaksi #49, tekan Enter
157. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
158. Geser jam server ke T1 + 3 hari + 1 menit lewat fixture Pre-setup #20
159. Ulangi tiap 5 detik: muat ulang halaman, ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter, sampai baris transaksi #49 berstatus `Canceled` (batas tunggu 2 menit)
160. Pulihkan jam server ke waktu nyata lewat fixture Pre-setup #20
161. Verifikasi baris transaksi #49 berstatus `Canceled` (Timeout Auto-Cancel tetap berjalan pada entitas Expired)
162. Verifikasi Reserved kantong PT Global Distribusi $0.00 (dibaca lewat fixture)
163. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec kelas h (state tenant): write-lockdown entitas aktor Suspended dan Expired; Timeout Auto-Cancel tetap berjalan. Serial; fixture status entitas.
- Urutan TC di spec: TC-278, 80, 81, 85, 86, 82, 83, 84 (blok Suspended), lalu 88, 480, 481, 87, 482, 483, 484 (blok Expired) (penyimpangan dari urutan nomor, S-05). Alasan: TC-278 dan TC-484 membatalkan transaksi #49 lewat Timeout sehingga TC-278 ditaruh pertama dengan baseline dipulihkan sesudahnya, dan TC-484 terakhir pada blok Expired. Blok geser jam TC-278 tidak berada di akhir spec (S-10): efek geser jam pada transaksi lain dinetralkan oleh pemulihan baseline dan status entitas langsung sesudahnya (langkah 12 dan 13); aksi lain dikelompokkan per akun agar ganti akun minimal (prinsip 5, aksi yang merusak data di akhir).
- P-2 (pemicu bukan objek uji, `[KEPUTUSAN 2026-10-21]`): job latar Timeout (TC-278, TC-484) dan jam server yang digeser hanya memicu kondisi yang diamati lewat List dan fixture; Approve dan Reject lewat UI Approvals (TC-85, TC-86, TC-482, TC-483) adalah objek uji penolakan, bukan pemicu.
- Langkah penghubung (S-03, R-12): langkah "Tunggu toast error sebelumnya hilang" sebelum `[Reject]` (toast error identik dengan toast Approve sebelumnya), langkah persiapan (pemulihan baseline dan status entitas lewat fixture), langkah ganti akun (subjudul "Ganti akun ..."), `(←)` yang mereset Search, buka halaman via sidebar, muat ulang halaman, pencarian transaksi target, pencatatan T1 dan baseline baris teratas, penampilan kolom Notes lewat Setup Column (preferensi dipulihkan hook `after` suite), langkah pemulihan jam server, dan polling muat ulang tiap 5 detik. Aksi yang ditolak server tidak dinyatakan TC meninggalkan form atau dialog dalam keadaan apa; setelah toast spec memuat ulang halaman (dialog `beforeunload` ditangani otomatis, S-08) lalu mengamati state dari List dan fixture.
- Asersi absence "tidak ada transaksi baru" (TC-80, TC-84, TC-87, TC-481): didahului `Verifikasi` toast error (respons server sudah diproses, bagian 8b butir 2) dan dibandingkan dengan baris teratas List yang dicatat sebagai baseline (S-12); bukan kelas g karena aksinya ada dalam alur fungsional spec ini. Klausa "tidak ada Capture" pada TC lain (TC-458, TC-461) ada di spec 015.
- Aksi Approve dan Reject dipecah per kontrol (S-01, S-03): buka transaksi #49, klik `[Approve]` atau isi Rejection Reason lalu klik `[Reject]`, lalu konfirmasi pada dialog sebagai langkah terpisah.
- Ukuran spec (jauh di atas sekitar 35 langkah): satu kelas harness (h) dengan satu dataset (transaksi #49 dan #52 pada entitas PT Global Distribusi), tiap Expected menjadi `Verifikasi` sendiri (S-01), tiap TC memuat langkah mengamati state sesudah penolakan, dan tiga ganti akun eksplisit di dua blok. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras karena baseline dan status entitas dipulihkan lewat fixture sebelum tiap blok (bagian 3, pemisah (b)).
- Pembagian TC lintas spec: write-lockdown akibat status Client penerima (TC-279, 456 sampai 461) ada di spec 015; TC-484 dan TC-278 juga menjadi rujukan spec 035 (Timeout Auto-Cancel umum).
- Temuan untuk QA:
  - TC-80 sampai TC-88 dan TC-480 sampai TC-483 tidak menyatakan keadaan form atau dialog sesudah toast penolakan (tetap terbuka atau tertutup); spec tidak mengasersinya dan memuat ulang halaman.
  - TC-85, TC-86, TC-482, TC-483 menulis "buka transaksi itu" di Approvals > Device Allocation tanpa menyebut nama kontrol; Page Object Approvals menentukan cara membukanya (modul Approvals).
  - TC-82 Data Uji "Quantity 100 menjadi 120" dan TC-88 Data Uji "Notes: Revisi catatan"; spec membaca nilai tetap lewat List (Quantity) dan kolom Notes yang ditampilkan Setup Column.
  - TC-278 dan TC-484 Langkah Uji 2 menyebut "pengguna entitas lain yang dapat melihat transaksi itu (Total Control Principal)" sedangkan Precondition a login sebagai MB_ON; spec memakai Principal sebagai aktor dan MB_ON hanya pembuat transaksi.
  - TC-278 dan TC-484 menyatakan Timeout berjalan "tanpa aktor"; Expected "Reserved $0.00" tidak punya cara baca selain Wallet Balance modul lain; spec membaca Reserved lewat fixture (disediakan tim FE/BE).
  - Post Condition TC-278 dan TC-484 (Wallet Balance dan Wallet Transaction List Release, Approvals Active Tab, Dashboard, notifikasi in-app ke pembuat dan approver) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-87 Expected a menyatakan "satu copy untuk Suspended dan Expired"; spec mengulang teks toast yang sama pada TC-88 dan TC-480 sampai TC-483.
  - TC-278 dan TC-484 dapat dibaca sebagai kelas d (background job sebagai objek uji "Timeout tetap berjalan") dan bukan hanya pemicu; spec ini menempatkannya di kelas h berdasarkan `[KEPUTUSAN 2026-10-21]` (proses sistem sebagai pemicu kondisi yang diuji); penempatan ini perlu dikonfirmasi.
