---
id: TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Sub-tab Pending Approvals: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-814
  - TC-GS-USER-815
  - TC-GS-USER-816
  - TC-GS-USER-817
  - TC-GS-USER-818
  - TC-GS-USER-819
  - TC-GS-USER-820
  - TC-GS-USER-821
  - TC-GS-USER-822
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard)

## Prerequisites

- Mode: FE+BE. Spec hanya membaca sub-tab Pending Approvals Ahmad Fauzi (read-only, tanpa row action) dan tidak mengubah data Pre-setup User. Spec mengubah preferensi Setup Column dan memulihkannya.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Ahmad Fauzi (No. 13, data Responsibilities FAMS).
- Data Dinamis (HK8, seeding minimal S-11; seeding user dan approval FAMS lewat API di hook `before` adalah kemampuan yang disediakan tim FE/BE, endpoint tidak disebut di TC, PRD, dan LLD):
  - Requester seed (user biasa, Access `Fixed Asset`, Division `Finance`): R1 First Name `Budi`, Last Name `Santoso {runId}-130`, email `budisantoso+{runId}-130@qwertysystem.net`, tampil di tabel `Budi S`; R2 First Name `Citra`, Last Name `Anggraini {runId}-130`, email `citraanggraini+{runId}-130@qwertysystem.net`, tampil `Citra A`; R3 First Name `Dedi`, Last Name `Kurniawan {runId}-130`, email `dedikurniawan+{runId}-130@qwertysystem.net`, tampil `Dedi K`.
  - 30 request approval in-flight (status Waiting for Approval) dengan Approver Ahmad Fauzi (Pre-setup No. 13), sehingga tabel Pending Approvals Ahmad Fauzi memuat lebih dari satu halaman (page size 10). Transaction ID dibuat FAMS saat seeding dan dikembalikan ke spec; nilainya tidak ditulis di spec. Submission Date `D1` = hari uji dikurangi 14 hari dan `D2` = hari uji dikurangi 7 hari (kemampuan menetapkan Submission Date seed disediakan tim FE/BE), teks tanggal dibaca dari sel tabel dalam Date Format General Settings.
  - Transaction `Transfer`, `{transaksi-B}`, dan `{transaksi-C}`: `Transfer` dan dua nilai Transaction FAAP lain yang namanya tidak memuat `ransf`, dipilih tim FE/BE saat seeding (TC dan PRD tidak menyebut nilai selain `Transfer`). `{transaksi-D}` = satu nilai Transaction FAAP lain yang tidak di-seed (tidak punya baris).

    | Kelompok | Transaction | Requester | Submission Date | Jumlah baris |
    |---|---|---|---|---|
    | S1 | `Transfer` | R1 `Budi S` | D1 | 6 |
    | S2 | `Transfer` | R2 `Citra A` | D2 | 4 |
    | S3 | `{transaksi-B}` | R2 `Citra A` | D1 | 6 |
    | S4 | `{transaksi-B}` | R3 `Dedi K` | D2 | 6 |
    | S5 | `{transaksi-C}` | R3 `Dedi K` | D1 | 4 |
    | S6 | `{transaksi-C}` | R1 `Budi S` | D2 | 4 |

  - Hasil per dimensi: Transaction `Transfer` 10 baris, `{transaksi-B}` 12 baris, `{transaksi-C}` 8 baris; Requester R1, R2, R3 masing-masing 10 baris; Submission Date D1 16 baris, D2 14 baris. Tiap kolom yang diuji (Transaction, Requester, Submission Date) memuat tiga, tiga, dan dua nilai distinct.
  - Baris contoh = satu baris kelompok S1 (Transfer, R1 `Budi S`, D1); Transaction ID-nya `{trxId-contoh}` dikembalikan oleh seeding.
  - Keyword unik Requester (hanya cocok dengan Requester seed spec ini karena memuat suffix): `ntoso {runId}-130` (R1), `raini {runId}-130` (R2), `{runId}-130` (R1, R2, R3).
  - Baris Pre-setup Pending Approvals Ahmad Fauzi (bila ada) tidak diubah dan jumlahnya tidak diasumsikan: asersi jumlah baris memakai keyword atau filter yang hanya cocok dengan baris seed, dan asersi urutan atau isi umum tidak bergantung pada baris Pre-setup.
  - Cleanup di hook `after` (tanpa berasumsi seeding berhasil penuh): hapus 30 request approval seed dan user Requester seed lewat API.
- Data uji: kolom `Transaction ID`, `Transaction`, `Requester`, `Submission Date` (semua Hideable, default visible, tanpa pin; tidak ada kolom Curated). Asersi spec ini menyangkut kolom tabel, bukan isi baris; seed tetap dipasang supaya tabel terisi dan preview Setup Column memuat baris.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]`; Overlay Column Visibility langsung berlaku (prd-conventions.md §9.3). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- Lebar konten tabel harus melebihi lebar viewport (overflow horizontal) supaya scroll horizontal pada TC-GS-USER-818 teramati. Viewport disempitkan di langkah 81 dan dikembalikan ke ukuran awal di langkah 125; ukuran viewport dipilih tim FE karena TC tidak menyebutnya.
- State yang diubah dan dipulihkan: preferensi Setup Column sub-tab Pending Approvals dikembalikan ke default (`Transaction ID`, `Transaction`, `Requester`, `Submission Date` tampil berurutan, tanpa pin) oleh TC-GS-USER-819 (`[Reset to Default]` lalu `[Save]`); hook `after` (tetap jalan walau spec gagal di tengah) memulihkan lewat `[Reset to Default]` atau penghapusan preferensi kolom Pending Approvals di penyimpanan browser, serta mengembalikan viewport ke ukuran awal.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`): tabel Pending Approvals Ahmad Fauzi hanya boleh memuat baris Pre-setup dan seed spec ini saat spec berjalan.
- Kemampuan teknis: drag and drop item kolom pada Popup Setup Column; hover checkbox dan icon Pin yang disabled untuk membaca tooltip; mengatur viewport; scroll horizontal tabel; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-USER-814: Screening Overlay Column Visibility

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Approvals`
4. Klik header kolom Actions (⋯)
5. Verifikasi Overlay daftar kolom berurutan `Transaction ID`, `Transaction`, `Requester`, `Submission Date`
6. Verifikasi setiap kolom berstatus Hideable: tercentang dan enabled
7. Verifikasi setiap kolom memiliki drag handle
8. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-815: Screening Popup Setup Column

9. Klik item `Setup Column...`
10. Verifikasi Header: Title `Setup Column`
11. Verifikasi Header: deskripsi panduan tampil
12. Verifikasi Header: icon `[✕]`
13. Verifikasi Body: daftar kolom `Transaction ID`, `Transaction`, `Requester`, `Submission Date` masing-masing dengan checkbox
14. Verifikasi Body: drag handle pada tiap kolom
15. Verifikasi Body: icon Pin pada tiap kolom
16. Verifikasi Body: preview tabel tampil
17. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]` tampil
18. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-816: Setup Column hide dan unhide kelas Hideable

19. Hilangkan centang `Transaction ID`
20. Verifikasi preview tabel tidak menampilkan kolom `Transaction ID`
21. Klik `[Save]`
22. Verifikasi kolom `Transaction ID` tidak tampil di tabel (tersimpan setelah Save)
23. Muat ulang halaman (F5)
24. Verifikasi kolom `Transaction ID` tetap tidak tampil setelah F5
25. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
26. Centang kembali `Transaction ID`
27. Hilangkan centang `Transaction`
28. Verifikasi preview tabel tidak menampilkan kolom `Transaction`
29. Klik `[Save]`
30. Verifikasi kolom `Transaction` tidak tampil di tabel (tersimpan setelah Save)
31. Muat ulang halaman (F5)
32. Verifikasi kolom `Transaction` tetap tidak tampil setelah F5
33. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
34. Centang kembali `Transaction`
35. Hilangkan centang `Requester`
36. Verifikasi preview tabel tidak menampilkan kolom `Requester`
37. Klik `[Save]`
38. Verifikasi kolom `Requester` tidak tampil di tabel (tersimpan setelah Save)
39. Muat ulang halaman (F5)
40. Verifikasi kolom `Requester` tetap tidak tampil setelah F5
41. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
42. Centang kembali `Requester`
43. Hilangkan centang `Submission Date`
44. Verifikasi preview tabel tidak menampilkan kolom `Submission Date`
45. Klik `[Save]`
46. Verifikasi kolom `Submission Date` tidak tampil di tabel (tersimpan setelah Save)
47. Muat ulang halaman (F5)
48. Verifikasi kolom `Submission Date` tetap tidak tampil setelah F5
49. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
50. Centang kembali `Submission Date`
51. Klik `[Save]`
52. Tunggu aksi selesai (popup tertutup)

### TC-GS-USER-817: Setup Column drag reorder kelas Hideable

53. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
54. Seret `Transaction ID` ke posisi pertama
55. Verifikasi preview tabel menampilkan kolom `Transaction ID` di posisi pertama
56. Klik `[Save]`
57. Verifikasi kolom `Transaction ID` berada di posisi pertama tabel (tersimpan setelah Save)
58. Muat ulang halaman (F5)
59. Verifikasi kolom `Transaction ID` tetap di posisi pertama tabel setelah F5
60. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
61. Seret `Transaction` ke posisi pertama
62. Verifikasi preview tabel menampilkan kolom `Transaction` di posisi pertama
63. Klik `[Save]`
64. Verifikasi kolom `Transaction` berada di posisi pertama tabel (tersimpan setelah Save)
65. Muat ulang halaman (F5)
66. Verifikasi kolom `Transaction` tetap di posisi pertama tabel setelah F5
67. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
68. Seret `Requester` ke posisi pertama
69. Verifikasi preview tabel menampilkan kolom `Requester` di posisi pertama
70. Klik `[Save]`
71. Verifikasi kolom `Requester` berada di posisi pertama tabel (tersimpan setelah Save)
72. Muat ulang halaman (F5)
73. Verifikasi kolom `Requester` tetap di posisi pertama tabel setelah F5
74. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
75. Seret `Submission Date` ke posisi pertama
76. Verifikasi preview tabel menampilkan kolom `Submission Date` di posisi pertama
77. Klik `[Save]`
78. Verifikasi kolom `Submission Date` berada di posisi pertama tabel (tersimpan setelah Save)
79. Muat ulang halaman (F5)
80. Verifikasi kolom `Submission Date` tetap di posisi pertama tabel setelah F5

### TC-GS-USER-818: Setup Column pin dan unpin kelas Hideable

81. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
82. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
83. Klik icon Pin `Transaction ID`
84. Verifikasi preview tabel menampilkan kolom `Transaction ID` ter-pin
85. Klik `[Save]`
86. Scroll tabel secara horizontal
87. Verifikasi kolom `Transaction ID` beku saat scroll horizontal (tersimpan setelah Save)
88. Muat ulang halaman (F5)
89. Scroll tabel secara horizontal
90. Verifikasi kolom `Transaction ID` tetap beku saat scroll horizontal setelah F5
91. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
92. Klik icon Pin `Transaction ID` untuk unpin
93. Klik icon Pin `Transaction`
94. Verifikasi preview tabel menampilkan kolom `Transaction` ter-pin
95. Klik `[Save]`
96. Scroll tabel secara horizontal
97. Verifikasi kolom `Transaction` beku saat scroll horizontal (tersimpan setelah Save)
98. Muat ulang halaman (F5)
99. Scroll tabel secara horizontal
100. Verifikasi kolom `Transaction` tetap beku saat scroll horizontal setelah F5
101. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
102. Klik icon Pin `Transaction` untuk unpin
103. Klik icon Pin `Requester`
104. Verifikasi preview tabel menampilkan kolom `Requester` ter-pin
105. Klik `[Save]`
106. Scroll tabel secara horizontal
107. Verifikasi kolom `Requester` beku saat scroll horizontal (tersimpan setelah Save)
108. Muat ulang halaman (F5)
109. Scroll tabel secara horizontal
110. Verifikasi kolom `Requester` tetap beku saat scroll horizontal setelah F5
111. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
112. Klik icon Pin `Requester` untuk unpin
113. Klik icon Pin `Submission Date`
114. Verifikasi preview tabel menampilkan kolom `Submission Date` ter-pin
115. Klik `[Save]`
116. Scroll tabel secara horizontal
117. Verifikasi kolom `Submission Date` beku saat scroll horizontal (tersimpan setelah Save)
118. Muat ulang halaman (F5)
119. Scroll tabel secara horizontal
120. Verifikasi kolom `Submission Date` tetap beku saat scroll horizontal setelah F5
121. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
122. Klik icon Pin `Submission Date` untuk unpin
123. Klik `[Save]`
124. Tunggu aksi selesai (popup tertutup)
125. Kembalikan viewport ke ukuran awal

### TC-GS-USER-819: Setup Column Reset to Default

126. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
127. Seret `Requester` ke posisi pertama
128. Hilangkan centang `Transaction`
129. Klik `[Save]`
130. Verifikasi tabel menampilkan kolom `Requester` di posisi pertama dan tanpa kolom `Transaction` (susunan bukan default)
131. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
132. Klik `[Reset to Default]`
133. Klik `[Save]`
134. Verifikasi susunan kolom kembali default: `Transaction ID`, `Transaction`, `Requester`, `Submission Date` tampil berurutan
135. Muat ulang halaman (F5)
136. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-820: Tutup Setup Column via [✕] membuang perubahan

137. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
138. Hilangkan centang `Requester`
139. Klik `[✕]`
140. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom `Requester` tampil dan susunan default

### TC-GS-USER-821: Guard satu kolom tersisa tidak bisa di-uncheck

141. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
142. Hilangkan centang `Transaction`
143. Hilangkan centang `Requester`
144. Hilangkan centang `Submission Date`
145. Arahkan kursor ke checkbox `Transaction ID` (kolom terakhir)
146. Verifikasi checkbox `Transaction ID` tetap tampil namun disabled
147. Verifikasi tooltip `At least one column must remain visible.`
148. Klik `[✕]`

### TC-GS-USER-822: Maksimal 3 kolom di-pin

149. Buka Popup Setup Column lewat header kolom Actions (⋯) lalu `Setup Column...`
150. Klik icon Pin `Transaction ID`
151. Klik icon Pin `Transaction`
152. Klik icon Pin `Requester`
153. Arahkan kursor ke icon Pin `Submission Date` (kolom keempat)
154. Verifikasi icon Pin `Submission Date` disabled
155. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
156. Klik `[✕]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata). Dependensi data Pending Approvals Ahmad Fauzi dipenuhi spec ini lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (814 sampai 822) dipertahankan; dua TC screening (814, 815) di awal sebelum aksi yang mengubah konfigurasi kolom, dan TC-GS-USER-819 (Reset to Default) berada sesudah TC-GS-USER-816 sampai 818 sehingga menjadi pemulihan preferensi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 52 (menunggu popup tertutup sesudah `[Save]`), 81 dan 125 (menyempitkan dan mengembalikan viewport), serta 148 dan 156 (menutup popup lewat `[✕]` sehingga perubahan checkbox dan pin pada TC-GS-USER-821 dan 822 tidak tersimpan; hook `after` sebagai cadangan). Popup yang masih terbuka dari TC-GS-USER-815 dipakai ulang oleh TC-GS-USER-816; popup dibuka kembali sesudah tiap `[Save]` karena menutup, dan langkah pembuka berulang itu adalah prefix.
- TC-GS-USER-816: tiap kolom menjalankan "uncheck" lalu `[Save]` lalu F5, kemudian kolom dicentang kembali pada pembukaan popup berikutnya (digabung dengan uncheck kolom berikutnya) dan terakhir pada langkah sebelum 52. TC-GS-USER-817 menggeser tiap kolom ke posisi pertama berurutan tanpa pemulihan antar-kolom. TC-GS-USER-818 menjalankan Pin lalu `[Save]`, scroll, F5, scroll; unpin kolom sebelumnya digabung dengan pembukaan popup untuk kolom berikutnya (batas 3 kolom pin tidak tercapai) dan unpin terakhir sebelum langkah 125.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` tabel pada TC-GS-USER-819 sesudah `[Save]` pertama (susunan bukan default) berfungsi sebagai pembanding bagi susunan default sesudah Reset. Asersi "tersimpan setelah Save" pada TC-GS-USER-816 sampai 818 diamati di tabel sebelum F5.
- Pembagian TC lintas spec: TC-GS-USER-393, 394, 792 sampai 797 ada di spec 126; TC-GS-USER-798 sampai 806 ada di spec 127; TC-GS-USER-807 sampai 811 ada di spec 128; TC-GS-USER-812, 813, 828, 829 ada di spec 129; TC-GS-USER-395 dan 823 sampai 827 (Download terhadap kolom hidden) ada di spec 131.
- Spec melewati sekitar 35 langkah (156 langkah) karena sembilan TC Setup Column berada di satu kelas harness (fungsional), satu popup, dan satu tabel; TC-GS-USER-816, 817, dan 818 masing-masing menguji empat kolom dengan blok identik yang berdiri sendiri, dan langkah pembuka popup yang berulang adalah prefix. Memisahkannya mengulang login, seeding 30 request approval, dan pembukaan sub-tab yang sama.
- Temuan untuk QA:
  - TC-GS-USER-816: kalimat "uncheck lalu check, Save, refresh F5" secara literal tidak mengubah konfigurasi (hasil bersih sama dengan default). Spec mengasersi perubahan di preview, tersimpan setelah Save, dan bertahan setelah F5 dengan menjalankan uncheck, `[Save]`, F5, lalu centang kembali.
  - TC-GS-USER-817: `Transaction ID` sudah berada di posisi pertama pada susunan default, sehingga "geser ke posisi pertama" untuk kolom itu tidak mengubah susunan.
  - TC-GS-USER-818: TC tidak menyebut apakah Unpin perlu `[Save]`; spec menyimpannya pada pembukaan popup berikutnya dan di akhir blok.
  - TC-GS-USER-814 Expected b menyebut kolom Curated, tetapi sub-tab Pending Approvals tidak memiliki kolom Curated (semua Hideable); spec mengasersi Hideable saja.
  - TC-GS-USER-815 Expected a: teks deskripsi panduan tidak disebut TC maupun PRD; spec hanya mengasersi deskripsi tampil.
  - TC-GS-USER-819 langkah 4: TC tidak menyebut perubahan urutan dan visibilitas konkret; spec menggeser `Requester` ke posisi pertama dan menyembunyikan `Transaction`.
  - Mekanisme seeding user Requester dan request approval FAMS (jenis Transaction, Requester, Submission Date, Approver) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan. TC tidak menyebut nilai Transaction selain `Transfer`; dua nilai FAAP lain dipilih tim FE/BE.
  - Mekanisme menghapus preferensi kolom di penyimpanan browser tidak didefinisikan di TC, PRD, atau LLD; hook `after` memakai `[Reset to Default]` atau kemampuan yang disediakan tim FE/BE.
  - Mekanisme menyetel flag Guided Tooltip `gs-user` tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (hook suite).
