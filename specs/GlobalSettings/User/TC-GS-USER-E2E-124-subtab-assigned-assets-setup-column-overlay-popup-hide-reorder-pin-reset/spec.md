---
id: TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Sub-tab Assigned Assets: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin, Reset to Default, dan Guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-776
  - TC-GS-USER-777
  - TC-GS-USER-778
  - TC-GS-USER-779
  - TC-GS-USER-780
  - TC-GS-USER-781
  - TC-GS-USER-782
  - TC-GS-USER-783
  - TC-GS-USER-784
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin, Reset to Default, dan Guard)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup user; hanya dataset Assigned Assets milik spec yang ditambahkan lalu dibersihkan.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Ahmad Fauzi (No. 13; Assigned Assets berisi K1).
- Data Dinamis, dataset Assigned Assets milik Ahmad Fauzi (27 baris; dengan page size 10 menjadi tiga halaman: 10, 10, 7 baris). K1 adalah data Pre-setup (hanya dibaca, tidak dihapus); K2 sampai K27 di-seed milik spec lewat kemampuan seeding data Responsibilities/FAMS (HK8) di hook `before` (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Saat spec mulai, Assigned Assets Ahmad Fauzi hanya berisi K1 sampai K27. Transaction ID `ASG-{runId}-124-kk` dan Asset ID `AST-{runId}-124-kk` dengan kk = nomor K dua digit:
  - K1 (Pre-setup, literal dari TC-GS-USER-390): Transaction ID `ASG-20260505-0001`, Name `Company Vehicle B1234XY`, Asset ID `AST-0001`, Brand `Toyota`, Model / Type `Hilux`, PIC `Citra Wulandari`.
  - K2 sampai K4: Name `Company Vehicle V1 {runId}-124` sampai `Company Vehicle V3 {runId}-124`, Brand `Toyota`, Model / Type `Hilux`, PIC `Rudi Hartanto {runId}-124`.
  - K5 sampai K7: Name `Company Vehicle V4 {runId}-124` sampai `Company Vehicle V6 {runId}-124`, Brand `Honda`, Model / Type `Civic`, PIC `Sinta Dewi {runId}-124`.
  - K8 sampai K12: Name `Laptop L1 {runId}-124` sampai `Laptop L5 {runId}-124`, Brand `Dell`, Model / Type `Latitude 5440`, PIC `Bambang Susanto {runId}-124`.
  - K13 sampai K17: Name `Laptop L6 {runId}-124` sampai `Laptop L10 {runId}-124`, Brand `Lenovo`, Model / Type `ThinkPad T14`, PIC `Rudi Hartanto {runId}-124`.
  - K18 sampai K22: Name `Printer P1 {runId}-124` sampai `Printer P5 {runId}-124`, Brand `Canon`, Model / Type `PIXMA G3010`, PIC `Sinta Dewi {runId}-124`.
  - K23 sampai K27: Name `Printer P6 {runId}-124` sampai `Printer P10 {runId}-124`, Brand `Epson`, Model / Type `EcoTank L3250`, PIC `Bambang Susanto {runId}-124`.
  - Ringkasan: Name 27 nilai distinct; Brand 6 nilai (Toyota 4 baris, Honda 3, Dell 5, Lenovo 5, Canon 5, Epson 5); PIC 4 nilai (Citra Wulandari 1 baris, Rudi Hartanto 8, Sinta Dewi 8, Bambang Susanto 10); baris ber-Name memuat `Vehicle`: 7 (K1 sampai K7). Nilai distinct pada kolom yang di-sort, di-search, dan di-filter dipenuhi (S-11).
  - Nama literal tanpa suffix hanya K1 (Pre-setup); seluruh nilai Name, Transaction ID, Asset ID, dan PIC milik spec bersuffix `{runId}-124`. Nama Brand dan Model / Type adalah nilai master tanpa suffix.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus aset seed K2 sampai K27 lewat kemampuan seeding yang sama; data Pre-setup (K1 dan record user) tidak diubah. Seeding aset tidak mengubah record user Ahmad Fauzi.
- Data uji: tujuh kolom `Photo`, `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `PIC` (semua Hideable, default tampil); TC-GS-USER-778 dikelompokkan menjadi dua siklus (`Photo`, `Transaction ID`, `Asset ID`, `Brand` lalu `Name`, `Model / Type`, `PIC`) supaya selalu ada kolom yang tampil; TC-GS-USER-780 dikelompokkan menjadi tiga siklus pin (`Photo`, `Transaction ID`, `Name`; `Asset ID`, `Brand`, `Model / Type`; `PIC`) karena maksimal 3 kolom ter-pin sekaligus.
- Preferensi kolom (visibilitas, urutan, pin) sub-tab Assigned Assets tersimpan per user dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3); "muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan tetap ada. Overlay Column Visibility langsung berlaku.
- Lebar konten tabel harus melebihi lebar viewport (overflow horizontal) supaya scroll horizontal pada TC-GS-USER-780 teramati. Viewport disempitkan pada langkah 95 dan dikembalikan pada langkah 140; ukuran viewport dipilih tim FE karena TC tidak menyebutnya.
- Kemampuan teknis: seeding Assigned Assets (HK8) (disediakan tim FE/BE); drag and drop item kolom pada Popup Setup Column; mengatur viewport; scroll horizontal tabel; mengarahkan kursor ke checkbox dan icon Pin disabled untuk membaca tooltip; membaca dan menghapus preferensi kolom di penyimpanan browser; setelah F5 sub-tab Assigned Assets user yang sama tetap terbuka.
- State yang diubah dan dipulihkan: preferensi Setup Column sub-tab Assigned Assets dikembalikan ke default (susunan `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`, semua tampil, tanpa pin) oleh blok TC-GS-USER-781 di akhir spec (langkah 141 sampai 150); hook `after` (tetap jalan walau spec gagal di tengah) mengembalikannya lewat `[Reset to Default]` atau penghapusan preferensi kolom sub-tab Assigned Assets di browser, serta mengembalikan viewport ke ukuran awal. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Assigned Assets`

### TC-GS-USER-776: Screening Overlay Column Visibility

5. Klik header kolom Actions (⋯)
6. Verifikasi Overlay daftar kolom: `Photo` | `Name` | `Asset ID` | `Transaction ID` | `Brand` | `Model / Type` | `PIC`
7. Verifikasi ketujuh kolom (Hideable) tercentang dan enabled
8. Verifikasi drag handle tersedia pada tiap kolom
9. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-777: Screening Popup Setup Column

10. Klik `Setup Column...`
11. Verifikasi Header: Title `Setup Column`
12. Verifikasi Header: deskripsi panduan tampil
13. Verifikasi Header: icon `[✕]` tampil
14. Verifikasi Body: daftar kolom dengan checkbox
15. Verifikasi Body: drag handle pada tiap kolom
16. Verifikasi Body: icon Pin pada tiap kolom
17. Verifikasi Body: preview tabel tampil
18. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
19. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-782: Tutup Setup Column via [✕] membuang perubahan

20. Hilangkan centang `Brand`
21. Verifikasi preview tidak memuat kolom `Brand`
22. Klik `[✕]`
23. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom `Brand` tampil

### TC-GS-USER-783: Guard satu kolom tersisa tidak bisa di-uncheck

24. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
25. Hilangkan centang `Photo`
26. Hilangkan centang `Transaction ID`
27. Hilangkan centang `Name`
28. Hilangkan centang `Asset ID`
29. Hilangkan centang `Brand`
30. Hilangkan centang `Model / Type`
31. Arahkan kursor ke checkbox kolom terakhir `PIC`
32. Verifikasi checkbox `PIC` tetap tampil namun disabled
33. Verifikasi tooltip `At least one column must remain visible.`
34. Klik `[✕]`

### TC-GS-USER-784: Maksimal 3 kolom di-pin

35. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
36. Klik icon Pin pada `Photo`
37. Klik icon Pin pada `Transaction ID`
38. Klik icon Pin pada `Name`
39. Verifikasi preview menampilkan kolom `Photo`, `Transaction ID`, dan `Name` ter-pin
40. Arahkan kursor ke icon Pin kolom keempat `Brand`
41. Verifikasi icon Pin `Brand` disabled
42. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
43. Klik `[✕]`

### TC-GS-USER-778: Setup Column hide/unhide kelas Hideable

44. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
45. Hilangkan centang `Photo`
46. Hilangkan centang `Transaction ID`
47. Hilangkan centang `Asset ID`
48. Hilangkan centang `Brand`
49. Verifikasi preview tidak memuat kolom `Photo`, `Transaction ID`, `Asset ID`, `Brand`
50. Klik `[Save]`
51. Verifikasi tabel tidak memuat kolom `Photo`, `Transaction ID`, `Asset ID`, `Brand`
52. Muat ulang halaman (F5)
53. Verifikasi kolom `Photo`, `Transaction ID`, `Asset ID`, `Brand` tetap tidak tampil setelah F5
54. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
55. Centang kembali `Photo`
56. Centang kembali `Transaction ID`
57. Centang kembali `Asset ID`
58. Centang kembali `Brand`
59. Klik `[Save]`
60. Verifikasi tabel memuat kembali kolom `Photo`, `Transaction ID`, `Asset ID`, `Brand`
61. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
62. Hilangkan centang `Name`
63. Hilangkan centang `Model / Type`
64. Hilangkan centang `PIC`
65. Verifikasi preview tidak memuat kolom `Name`, `Model / Type`, `PIC`
66. Klik `[Save]`
67. Verifikasi tabel tidak memuat kolom `Name`, `Model / Type`, `PIC`
68. Muat ulang halaman (F5)
69. Verifikasi kolom `Name`, `Model / Type`, `PIC` tetap tidak tampil setelah F5
70. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
71. Centang kembali `Name`
72. Centang kembali `Model / Type`
73. Centang kembali `PIC`
74. Klik `[Save]`
75. Verifikasi tabel memuat kembali kolom `Name`, `Model / Type`, `PIC`

### TC-GS-USER-779: Setup Column drag reorder kelas Hideable

76. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
77. Seret `Photo` ke posisi pertama
78. Verifikasi preview menempatkan `Photo` di posisi pertama
79. Seret `Transaction ID` ke posisi pertama
80. Verifikasi preview menempatkan `Transaction ID` di posisi pertama
81. Seret `Name` ke posisi pertama
82. Verifikasi preview menempatkan `Name` di posisi pertama
83. Seret `Asset ID` ke posisi pertama
84. Verifikasi preview menempatkan `Asset ID` di posisi pertama
85. Seret `Brand` ke posisi pertama
86. Verifikasi preview menempatkan `Brand` di posisi pertama
87. Seret `Model / Type` ke posisi pertama
88. Verifikasi preview menempatkan `Model / Type` di posisi pertama
89. Seret `PIC` ke posisi pertama
90. Verifikasi preview menempatkan `PIC` di posisi pertama
91. Klik `[Save]`
92. Verifikasi tabel berurutan `PIC | Model / Type | Brand | Asset ID | Name | Transaction ID | Photo`
93. Muat ulang halaman (F5)
94. Verifikasi urutan tabel tetap `PIC | Model / Type | Brand | Asset ID | Name | Transaction ID | Photo` setelah F5

### TC-GS-USER-780: Setup Column pin/unpin kelas Hideable

95. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
96. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
97. Klik icon Pin pada `Photo`
98. Klik icon Pin pada `Transaction ID`
99. Klik icon Pin pada `Name`
100. Verifikasi preview menampilkan kolom `Photo`, `Transaction ID`, `Name` ter-pin
101. Klik `[Save]`
102. Scroll tabel secara horizontal
103. Verifikasi kolom `Photo`, `Transaction ID`, `Name` membeku (sticky) saat scroll horizontal
104. Muat ulang halaman (F5)
105. Scroll tabel secara horizontal
106. Verifikasi kolom `Photo`, `Transaction ID`, `Name` tetap membeku setelah F5
107. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
108. Klik icon Pin pada `Photo` untuk unpin
109. Klik icon Pin pada `Transaction ID` untuk unpin
110. Klik icon Pin pada `Name` untuk unpin
111. Klik `[Save]`
112. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
113. Klik icon Pin pada `Asset ID`
114. Klik icon Pin pada `Brand`
115. Klik icon Pin pada `Model / Type`
116. Verifikasi preview menampilkan kolom `Asset ID`, `Brand`, `Model / Type` ter-pin
117. Klik `[Save]`
118. Scroll tabel secara horizontal
119. Verifikasi kolom `Asset ID`, `Brand`, `Model / Type` membeku (sticky) saat scroll horizontal
120. Muat ulang halaman (F5)
121. Scroll tabel secara horizontal
122. Verifikasi kolom `Asset ID`, `Brand`, `Model / Type` tetap membeku setelah F5
123. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
124. Klik icon Pin pada `Asset ID` untuk unpin
125. Klik icon Pin pada `Brand` untuk unpin
126. Klik icon Pin pada `Model / Type` untuk unpin
127. Klik `[Save]`
128. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
129. Klik icon Pin pada `PIC`
130. Verifikasi preview menampilkan kolom `PIC` ter-pin
131. Klik `[Save]`
132. Scroll tabel secara horizontal
133. Verifikasi kolom `PIC` membeku (sticky) saat scroll horizontal
134. Muat ulang halaman (F5)
135. Scroll tabel secara horizontal
136. Verifikasi kolom `PIC` tetap membeku setelah F5
137. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
138. Klik icon Pin pada `PIC` untuk unpin
139. Klik `[Save]`
140. Kembalikan viewport ke ukuran awal

### TC-GS-USER-781: Setup Column Reset to Default

141. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
142. Hilangkan centang `Brand`
143. Klik `[Save]`
144. Verifikasi tabel tanpa kolom `Brand` dengan urutan hasil perubahan `PIC | Model / Type | Asset ID | Name | Transaction ID | Photo`
145. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
146. Klik `[Reset to Default]`
147. Klik `[Save]`
148. Verifikasi susunan kolom kembali default: `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`
149. Muat ulang halaman (F5)
150. Verifikasi susunan default tetap bertahan setelah F5: `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata). Dataset 27 baris (lebih dari satu halaman) dipenuhi spec lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 776, 777 (screening), 782, 783, 784 (batal dan guard tanpa Save), 778, 779, 780 (perubahan yang disimpan), lalu 781 (Reset to Default) di akhir. TC-GS-USER-782, 783, dan 784 tidak menyimpan perubahan sehingga ditaruh sebelum TC yang menyimpan; TC-GS-USER-781 ditaruh terakhir karena sekaligus memulihkan preferensi kolom ke default. Urutan di `tc-user.md`: 776 sampai 784 berurutan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (pembukaan layar bersama untuk Ahmad Fauzi), langkah 34 dan 43 (menutup popup tanpa Save supaya perubahan checkbox dan pin tidak tersimpan; hook `after` sebagai cadangan), langkah 95 dan 140 (menyempitkan dan mengembalikan viewport), serta unpin dan centang kembali yang memulihkan state pada TC-GS-USER-778 dan 780. Langkah pembuka popup yang berulang merupakan prefix berulang. TC-GS-USER-782 memakai popup yang masih terbuka dari TC-GS-USER-777 sehingga langkah Uji 4 TC-GS-USER-782 (`Buka Setup Column`) dipenuhi langkah pembuka TC-GS-USER-777.
- Pengelompokan kolom (diizinkan karena ketujuh kolom berkelas Hideable dengan perilaku identik): TC-GS-USER-778, 779, dan 780 pada TC sumber memuat siklus Save dan F5 per kolom. Spec menjalankan siklus Save dan F5 per kelompok kolom (778: dua kelompok; 780: tiga kelompok, batas 3 kolom ter-pin; 779: satu sesi tujuh seretan kumulatif dengan satu Save dan satu F5). Setiap kolom tetap punya `Verifikasi` sendiri (daftar kolom yang disebut utuh pada satu `Verifikasi`, S-01; di TC-GS-USER-779 satu `Verifikasi` preview per kolom).
- Langkah Uji TC-GS-USER-778 `uncheck lalu check, Save, refresh F5` dibaca sebagai hide, Save, F5, lalu unhide, Save: uncheck yang langsung dibatalkan sebelum Save tidak mengubah konfigurasi tersimpan.
- Urutan seretan TC-GS-USER-779 mengikuti urutan kolom TC (`Photo`, `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `PIC`), sehingga urutan akhir adalah kebalikannya. Seret `Photo` ke posisi pertama tidak mengubah susunan bila `Photo` sudah berada di posisi pertama.
- Anchor positif dan state: verifikasi preview tidak memuat `Brand` (TC-GS-USER-782) dan verifikasi tiga kolom ter-pin (TC-GS-USER-784) mendahului asersi yang bergantung pada state itu (S-14); verifikasi footer `[Reset to Default]` dan `[Save]` mendahului asersi ketiadaan `[Cancel]`.
- Spec melewati sekitar 35 langkah (150 langkah) karena sembilan TC berbagi satu popup Setup Column, satu layar, satu dataset 27 baris, dan satu kelas harness (fungsional). Blok 778, 779, dan 780 menguji tujuh kolom dengan blok identik (buka popup, ubah, Save, cek, F5) dan tiap blok berdiri sendiri; blok 781 memakai susunan hasil 779 dan 780 (Reset to Default). Langkah pembuka popup yang berulang dan pasangan klik per kolom merupakan prefix berulang.
- Pembagian TC lintas spec: TC-GS-USER-390, 391, 755 sampai 760 (termasuk Search terhadap kolom hidden) ada di spec 120; TC-GS-USER-761 sampai 768 ada di spec 121; TC-GS-USER-769 sampai 773 ada di spec 122; TC-GS-USER-774, 775, 790, 791 ada di spec 123; TC-GS-USER-392 dan 785 sampai 789 (Download terhadap kolom hidden) ada di spec 125.
- Temuan untuk QA:
  - TC-GS-USER-776 butir a vs TC-GS-USER-390 butir b: urutan kolom berbeda. Overlay: `Photo | Name | Asset ID | Transaction ID | Brand | Model / Type | PIC`; tabel: `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`. Spec mengikuti masing-masing TC (overlay di langkah verifikasi overlay, tabel di langkah verifikasi urutan default TC-GS-USER-781).
  - TC-GS-USER-776 butir b: `kolom Curated unchecked & enabled`, tetapi daftar kolom TC tidak memuat kolom Curated apa pun (ketujuh kolom Hideable dan default tampil); butir Curated tidak diasersi.
  - TC-GS-USER-777: `deskripsi panduan` tidak disebut teksnya; spec hanya mengasersi deskripsi tampil.
  - TC-GS-USER-778, 779, 780: siklus Save dan F5 per kolom dipadatkan per kelompok (lihat butir Pengelompokan kolom); `uncheck lalu check` ambigu (lihat butir pembacaan langkah). TC-GS-USER-780 tidak menyebut ukuran viewport dan perilaku `kolom beku` untuk tabel yang tidak overflow; disediakan tim FE.
  - TC-GS-USER-781: Langkah Uji 4 (`Ubah urutan dan visibility kolom, Save`) tidak menyebut kolom dan urutan; spec memakai susunan hasil TC-GS-USER-779 dan menyembunyikan `Brand`.
  - TC-GS-USER-784: `kolom keempat` ambigu (urutan daftar popup vs urutan tabel); spec memakai `Brand` sebagai kolom yang belum ter-pin sesudah tiga kolom ter-pin.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat, menyiapkan data FAMS, dan menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE. TC tidak menyatakan apakah F5 mempertahankan Tab dan sub-tab yang terbuka; spec mengasumsikan sub-tab Assigned Assets user yang sama tetap terbuka.
