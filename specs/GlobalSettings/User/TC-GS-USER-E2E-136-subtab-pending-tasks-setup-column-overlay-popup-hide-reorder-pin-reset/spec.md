---
id: TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Sub-tab Pending Tasks: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-855
  - TC-GS-USER-856
  - TC-GS-USER-857
  - TC-GS-USER-858
  - TC-GS-USER-859
  - TC-GS-USER-860
  - TC-GS-USER-861
  - TC-GS-USER-862
  - TC-GS-USER-863
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data User; yang di-seed hanya task pending FAMS milik spec (Population PT-22), dipakai sebagai isi tabel pada preview Setup Column.
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat tepat 22 baris saat spec mulai). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC memakai Group dan user FAMS yang disediakan tim FE/BE. Bila Ahmad Fauzi sudah memiliki task pending Pre-setup, task itu dihitung ke dalam komposisi di bawah. Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A}` lebih kecil dari `{pic-B}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (kata pertama `{group-A}`) dan `{kw-pic}` (nama depan `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan: Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris dan `{group-B}` 12 baris; PIC `{pic-A}` 8 baris dan `{pic-B}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; page size 10 menghasilkan 3 halaman (10, 10, 2 baris).
- Data uji: delapan kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated` (semua Hideable, default visible, tanpa pin; tabel Pending Tasks tidak memiliki kolom Curated). Asersi spec ini menyangkut kolom tabel; komposisi kelompok Population PT-22 tidak diasersi, yang dipakai hanya jumlah baris lebih dari satu halaman.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (PRD `prd-conventions.md` §9.3, cache `localStorage`); "muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- State yang diubah dan dipulihkan: preferensi kolom tabel Pending Tasks dikembalikan ke default lewat `[Reset to Default]` dan `[Save]` di langkah 147 (setelah itu TC-GS-USER-861 sampai 863 tidak menyimpan perubahan); viewport dikembalikan di langkah 139. Hook `after` (tetap jalan walau spec gagal di tengah) menghapus preferensi kolom tabel Pending Tasks di browser dan mengembalikan viewport; nama key dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE/BE.
- Kemampuan teknis: drag and drop baris kolom pada popup Setup Column; mengarahkan kursor ke checkbox dan icon Pin disabled untuk membaca tooltip; mengatur ukuran viewport dan scroll horizontal tabel; membaca atau menghapus preferensi kolom di penyimpanan browser; seeding task pending FAMS dan pembersihannya (di atas).
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-855: Screening Overlay Column Visibility

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Tasks`
4. Klik header kolom Actions (⋯)
5. Verifikasi overlay menampilkan daftar kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`
6. Verifikasi seluruh kolom Hideable tercentang dan enabled
7. Verifikasi tiap kolom memiliki drag handle
8. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-856: Screening Popup Setup Column

9. Klik item `Setup Column...`
10. Verifikasi Header: Title `Setup Column`
11. Verifikasi Header: deskripsi panduan `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
12. Verifikasi Header: icon `[✕]`
13. Verifikasi Body: daftar kolom dengan checkbox
14. Verifikasi Body: drag handle pada tiap kolom
15. Verifikasi Body: icon Pin pada tiap kolom
16. Verifikasi Body: preview tabel
17. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
18. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-857: Setup Column hide dan unhide kelas Hideable

19. Hilangkan centang kolom `Transaction ID`
20. Verifikasi preview tabel tidak memuat kolom `Transaction ID`
21. Centang kembali kolom `Transaction ID`
22. Verifikasi preview tabel memuat kembali kolom `Transaction ID`
23. Hilangkan centang kolom `Transaction`
24. Verifikasi preview tabel tidak memuat kolom `Transaction`
25. Centang kembali kolom `Transaction`
26. Verifikasi preview tabel memuat kembali kolom `Transaction`
27. Hilangkan centang kolom `Status`
28. Verifikasi preview tabel tidak memuat kolom `Status`
29. Centang kembali kolom `Status`
30. Verifikasi preview tabel memuat kembali kolom `Status`
31. Hilangkan centang kolom `Group`
32. Verifikasi preview tabel tidak memuat kolom `Group`
33. Centang kembali kolom `Group`
34. Verifikasi preview tabel memuat kembali kolom `Group`
35. Hilangkan centang kolom `PIC`
36. Verifikasi preview tabel tidak memuat kolom `PIC`
37. Centang kembali kolom `PIC`
38. Verifikasi preview tabel memuat kembali kolom `PIC`
39. Hilangkan centang kolom `Total Asset`
40. Verifikasi preview tabel tidak memuat kolom `Total Asset`
41. Centang kembali kolom `Total Asset`
42. Verifikasi preview tabel memuat kembali kolom `Total Asset`
43. Hilangkan centang kolom `Request Date`
44. Verifikasi preview tabel tidak memuat kolom `Request Date`
45. Centang kembali kolom `Request Date`
46. Verifikasi preview tabel memuat kembali kolom `Request Date`
47. Hilangkan centang kolom `Last Updated`
48. Verifikasi preview tabel tidak memuat kolom `Last Updated`
49. Centang kembali kolom `Last Updated`
50. Verifikasi preview tabel memuat kembali kolom `Last Updated`
51. Klik `[Save]`
52. Verifikasi tabel menampilkan kedelapan kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated` setelah `[Save]`
53. Muat ulang halaman (F5)
54. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
55. Verifikasi kedelapan kolom tetap tampil setelah F5

### TC-GS-USER-858: Setup Column drag reorder kelas Hideable

56. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
57. Seret kolom `Transaction ID` ke posisi pertama
58. Verifikasi preview tabel menampilkan kolom `Transaction ID` di posisi pertama
59. Seret kolom `Transaction` ke posisi pertama
60. Verifikasi preview tabel menampilkan kolom `Transaction` di posisi pertama
61. Seret kolom `Status` ke posisi pertama
62. Verifikasi preview tabel menampilkan kolom `Status` di posisi pertama
63. Seret kolom `Group` ke posisi pertama
64. Verifikasi preview tabel menampilkan kolom `Group` di posisi pertama
65. Seret kolom `PIC` ke posisi pertama
66. Verifikasi preview tabel menampilkan kolom `PIC` di posisi pertama
67. Seret kolom `Total Asset` ke posisi pertama
68. Verifikasi preview tabel menampilkan kolom `Total Asset` di posisi pertama
69. Seret kolom `Request Date` ke posisi pertama
70. Verifikasi preview tabel menampilkan kolom `Request Date` di posisi pertama
71. Seret kolom `Last Updated` ke posisi pertama
72. Verifikasi preview tabel menampilkan kolom `Last Updated` di posisi pertama
73. Klik `[Save]`
74. Verifikasi tabel menampilkan urutan kolom `Last Updated`, `Request Date`, `Total Asset`, `PIC`, `Group`, `Status`, `Transaction`, `Transaction ID` setelah `[Save]`
75. Muat ulang halaman (F5)
76. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
77. Verifikasi urutan kolom `Last Updated`, `Request Date`, `Total Asset`, `PIC`, `Group`, `Status`, `Transaction`, `Transaction ID` tetap setelah F5

### TC-GS-USER-859: Setup Column pin dan unpin kelas Hideable

78. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
79. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
80. Klik icon Pin pada kolom `Transaction ID`
81. Verifikasi preview tabel menampilkan kolom `Transaction ID` ter-pin
82. Klik icon Pin pada kolom `Transaction`
83. Verifikasi preview tabel menampilkan kolom `Transaction` ter-pin
84. Klik icon Pin pada kolom `Status`
85. Verifikasi preview tabel menampilkan kolom `Status` ter-pin
86. Klik `[Save]`
87. Scroll tabel secara horizontal
88. Verifikasi kolom `Transaction ID` beku (sticky) saat scroll horizontal setelah `[Save]`
89. Verifikasi kolom `Transaction` beku (sticky) saat scroll horizontal setelah `[Save]`
90. Verifikasi kolom `Status` beku (sticky) saat scroll horizontal setelah `[Save]`
91. Muat ulang halaman (F5)
92. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
93. Scroll tabel secara horizontal
94. Verifikasi kolom `Transaction ID` tetap beku saat scroll horizontal setelah F5
95. Verifikasi kolom `Transaction` tetap beku saat scroll horizontal setelah F5
96. Verifikasi kolom `Status` tetap beku saat scroll horizontal setelah F5
97. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
98. Klik icon Pin pada kolom `Transaction ID` untuk unpin
99. Klik icon Pin pada kolom `Transaction` untuk unpin
100. Klik icon Pin pada kolom `Status` untuk unpin
101. Klik icon Pin pada kolom `Group`
102. Verifikasi preview tabel menampilkan kolom `Group` ter-pin
103. Klik icon Pin pada kolom `PIC`
104. Verifikasi preview tabel menampilkan kolom `PIC` ter-pin
105. Klik icon Pin pada kolom `Total Asset`
106. Verifikasi preview tabel menampilkan kolom `Total Asset` ter-pin
107. Klik `[Save]`
108. Scroll tabel secara horizontal
109. Verifikasi kolom `Group` beku (sticky) saat scroll horizontal setelah `[Save]`
110. Verifikasi kolom `PIC` beku (sticky) saat scroll horizontal setelah `[Save]`
111. Verifikasi kolom `Total Asset` beku (sticky) saat scroll horizontal setelah `[Save]`
112. Muat ulang halaman (F5)
113. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
114. Scroll tabel secara horizontal
115. Verifikasi kolom `Group` tetap beku saat scroll horizontal setelah F5
116. Verifikasi kolom `PIC` tetap beku saat scroll horizontal setelah F5
117. Verifikasi kolom `Total Asset` tetap beku saat scroll horizontal setelah F5
118. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
119. Klik icon Pin pada kolom `Group` untuk unpin
120. Klik icon Pin pada kolom `PIC` untuk unpin
121. Klik icon Pin pada kolom `Total Asset` untuk unpin
122. Klik icon Pin pada kolom `Request Date`
123. Verifikasi preview tabel menampilkan kolom `Request Date` ter-pin
124. Klik icon Pin pada kolom `Last Updated`
125. Verifikasi preview tabel menampilkan kolom `Last Updated` ter-pin
126. Klik `[Save]`
127. Scroll tabel secara horizontal
128. Verifikasi kolom `Request Date` beku (sticky) saat scroll horizontal setelah `[Save]`
129. Verifikasi kolom `Last Updated` beku (sticky) saat scroll horizontal setelah `[Save]`
130. Muat ulang halaman (F5)
131. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
132. Scroll tabel secara horizontal
133. Verifikasi kolom `Request Date` tetap beku saat scroll horizontal setelah F5
134. Verifikasi kolom `Last Updated` tetap beku saat scroll horizontal setelah F5
135. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
136. Klik icon Pin pada kolom `Request Date` untuk unpin
137. Klik icon Pin pada kolom `Last Updated` untuk unpin
138. Klik `[Save]`
139. Kembalikan viewport ke ukuran awal

### TC-GS-USER-860: Setup Column Reset to Default

140. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
141. Hilangkan centang kolom `PIC`
142. Seret kolom `Total Asset` ke posisi pertama
143. Klik `[Save]`
144. Verifikasi konfigurasi tersimpan berbeda dari default: kolom `PIC` tidak tampil dan kolom `Total Asset` berada di posisi pertama
145. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
146. Klik `[Reset to Default]`
147. Klik `[Save]`
148. Verifikasi susunan kolom kembali default: `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated` tampil berurutan tanpa pin
149. Muat ulang halaman (F5)
150. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
151. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-861: Tutup Setup Column via [✕] membuang perubahan

152. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
153. Hilangkan centang kolom `Group`
154. Klik `[✕]`
155. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kedelapan kolom tampil berurutan default, termasuk kolom `Group`

### TC-GS-USER-862: Guard satu kolom tersisa tidak bisa di-uncheck

156. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
157. Hilangkan centang kolom `Transaction ID`
158. Hilangkan centang kolom `Transaction`
159. Hilangkan centang kolom `Status`
160. Hilangkan centang kolom `Group`
161. Hilangkan centang kolom `PIC`
162. Hilangkan centang kolom `Total Asset`
163. Hilangkan centang kolom `Request Date`
164. Arahkan kursor ke checkbox kolom `Last Updated`
165. Verifikasi checkbox kolom `Last Updated` tetap tampil namun disabled
166. Verifikasi tooltip `At least one column must remain visible.` tampil
167. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-863: Maksimal 3 kolom di-pin

168. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
169. Klik icon Pin pada kolom `Transaction ID`
170. Klik icon Pin pada kolom `Transaction`
171. Klik icon Pin pada kolom `Status`
172. Arahkan kursor ke icon Pin kolom `Group`
173. Verifikasi icon Pin kolom `Group` disabled
174. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
175. Klik `[✕]` untuk menutup popup tanpa menyimpan

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (855 sampai 863) dipertahankan; dua TC screening (855, 856) di awal sebelum aksi yang mengubah konfigurasi kolom.
- Langkah 1 sampai 3 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Popup Setup Column yang terbuka pada TC-GS-USER-856 dipakai langkah 19 (TC-GS-USER-857), sehingga "Klik header (⋯) → `Setup Column...`" TC-GS-USER-857 dipenuhi langkah 9.
- Pemadatan langkah per kolom: TC-GS-USER-857, 858, dan 859 menuliskan siklus Save dan F5 untuk tiap kolom (delapan kali). Spec memakai satu sesi popup per TC dan satu siklus Save dan F5 untuk seluruh kolom pada TC-GS-USER-857 dan 858, serta tiga siklus (tiga, tiga, dan dua kolom) pada TC-GS-USER-859 karena batas pin 3 kolom (TC-GS-USER-863); preview tiap kolom, kolom beku tiap kolom, dan persistensi tiap kolom tetap diasersi satu per satu. Alasan: hasil Save dan F5 pada TC-GS-USER-857 tidak berbeda per kolom karena uncheck lalu check mengembalikan kolom ke keadaan semula, dan pada TC-GS-USER-858 sesi tunggal menyimpan urutan akhir seluruh seretan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 78 dan 139 (menyempitkan dan mengembalikan viewport untuk TC-GS-USER-859), unpin kolom di awal sesi popup berikutnya dan langkah 135 sampai 139 (unpin kolom terakhir dari TC-GS-USER-859 sebagai bagian "lalu Unpin"), langkah 167 dan 175 (menutup popup tanpa Save agar uncheck dan pin tidak tersimpan; hook `after` sebagai cadangan), serta langkah muat ulang dan buka kembali Tab dan sub-tab sesudah F5. Langkah membuka popup yang berulang ("Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`") merupakan prefix berulang.
- Urutan konfigurasi: TC-GS-USER-858 menyimpan urutan terbalik, TC-GS-USER-859 mem-pin dan meng-unpin pada urutan itu, dan TC-GS-USER-860 mengubah lalu mereset ke default; TC-GS-USER-861 sampai 863 berjalan sesudahnya pada konfigurasi default tersimpan. Langkah 144 adalah asersi tambahan (S-03) agar Reset to Default berangkat dari konfigurasi yang berbeda dari default (S-14).
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 ada di spec 132 (Search terhadap kolom hidden: TC-GS-USER-835); TC-GS-USER-837 sampai 846 ada di spec 133; TC-GS-USER-847 sampai 851 (Filter terhadap kolom hidden: TC-GS-USER-850) ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 ada di spec 135; TC-GS-USER-398 dan 864 sampai 868 (Download terhadap kolom hidden: TC-GS-USER-867) ada di spec 137. TC Setup Column sub-tab Pending Approvals ada di spec 130.
- Spec melewati sekitar 35 langkah (175 langkah) karena sembilan TC Setup Column menguji delapan kolom dengan blok identik (hide, reorder, pin) pada satu popup, satu layar, satu dataset, dan satu kelas harness (fungsional). Tiap blok TC berdiri sendiri: konfigurasi dikembalikan ke default oleh langkah akhir blok atau oleh TC-GS-USER-860, sehingga satu kegagalan tidak membuat blok lain kehilangan makna. Langkah muat ulang dan pembukaan kembali sub-tab sesudah F5 serta pembukaan popup adalah prefix berulang.
- Temuan untuk QA:
  - TC-GS-USER-855 Expected b: "kolom Curated unchecked & enabled" tidak punya objek karena tabel Pending Tasks hanya memiliki delapan kolom Hideable (PRD `user.md` §4.1.3); butir itu tidak diasersi.
  - TC-GS-USER-856 Expected a: "deskripsi panduan" tidak ditulis literal di TC; spec memakai teks PRD `prd-conventions.md` §9.3 (`Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`). Spec Division 047 mengasersi teks lain (`Manage column visibility, reorder, and freeze columns.`) untuk komponen yang sama.
  - TC-GS-USER-857: "uncheck lalu check, Save, refresh F5" mengembalikan kolom ke keadaan semula, sehingga F5 tidak membedakan konfigurasi tersimpan dari default; spec mengasersi preview saat kolom tidak tercentang dan saat tercentang kembali, lalu kolom tampil setelah Save dan F5.
  - TC-GS-USER-858: urutan default sudah menempatkan `Transaction ID` di posisi pertama, sehingga seret `Transaction ID` ke posisi pertama tidak mengubah urutan.
  - TC-GS-USER-859: TC tidak menyebut cara membuat tabel dapat di-scroll horizontal; spec menyempitkan viewport. Expected "bertahan setelah F5" untuk pin ditulis dengan scroll horizontal setelah F5.
  - TC-GS-USER-860 dan 861: "Ubah urutan dan visibility kolom" dan "ubah konfigurasi" tidak konkret; spec memakai hide `PIC` dengan seret `Total Asset` (860) dan hide `Group` (861).
  - Nama key preferensi kolom di browser dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE. Seeding task pending FAMS tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE.
