---
id: TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Tab System Log Detail: Setup Column (Overlay, Popup, Guard Kolom Terakhir, Maksimal 3 Pin, Tutup dengan X, Hide/Unhide, Reorder, Pin/Unpin, dan Reset to Default)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-615
  - TC-GS-USER-616
  - TC-GS-USER-617
  - TC-GS-USER-618
  - TC-GS-USER-619
  - TC-GS-USER-620
  - TC-GS-USER-621
  - TC-GS-USER-622
  - TC-GS-USER-623
coverage:
  web: automated
---

# Tab System Log Detail: Setup Column (Overlay, Popup, Guard Kolom Terakhir, Maksimal 3 Pin, Tutup dengan X, Hide/Unhide, Reorder, Pin/Unpin, dan Reset to Default)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor UI: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 23 dan 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). System Log memuat aksi yang dilakukan user sebagai aktor (PRD user.md §8.3). Tiap user diberi Division `Finance` dan Access `Fixed Asset`:
  - Pemilik log `Aktor Log {runId}-100`, email `aktorlog+{runId}-100@qwertysystem.net`, tier Total Control, status Activated, password `Spectra.env.USER_PASSWORD`. Aktivasi akun seed dan sesi API Aktor Log disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut mekanismenya). Seluruh aksi seed di bawah dijalankan lewat sesi API Aktor Log.
  - Target aksi `Target Alfa {runId}-100` (email `targetalfa+{runId}-100@qwertysystem.net`, Position `Staff`) dan `Target Beta {runId}-100` (email `targetbeta+{runId}-100@qwertysystem.net`).
  - Aksi seed oleh Aktor Log, berurutan (hanya data yang dipakai `Verifikasi`, S-11): (1) Create `Target Alfa`; (2) Create `Target Beta`; (3) Edit Position `Target Alfa` dari `Staff` menjadi `Supervisor`; (4) Delete `Target Beta`. Spec mengamati kolom, bukan isi baris; riwayat terisi agar tabel menampilkan baris data dan dapat di-scroll horizontal.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa`, `Target Beta` bila masih ada, dan `Aktor Log`; hapus sisa user bersuffix `-100` dari run lama. Entri log tidak bisa dihapus. Pulihkan preferensi Setup Column tab System Log ke default lewat `[Reset to Default]` (akun Siti) dan kembalikan viewport ke bawaan.
- Preferensi Setup Column (urutan, visibilitas, pin) tersimpan lintas muat ulang halaman (TC-GS-USER-617 sampai 620). Tempat penyimpanan tidak disebut TC User; mekanisme membaca dan mengosongkannya disediakan tim FE. Hook `before` mengosongkan preferensi tab System Log sehingga spec mulai dari default (urutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, tujuh kolom tampil, tanpa pin). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya preferensi tetap ada.
- Kemampuan teknis: drag and drop elemen daftar kolom; hover checkbox dan icon Pin yang disabled untuk membaca tooltip; mengatur lebar viewport sehingga tabel System Log dapat di-scroll horizontal (TC tidak menyebut lebar viewport; viewport diperkecil sampai overflow horizontal) dan scroll horizontal tabel.
- State global yang diubah dan dipulihkan: preferensi Setup Column tab System Log (default dipulihkan lewat `[Reset to Default]` dan hook `after`) dan lebar viewport (dipulihkan pada langkah 172). Suite berjalan serial (`parallel: false`) karena preferensi Setup Column dipakai bersama spec lain pada akun dan browser yang sama.
- Precondition TC-GS-USER-615 sampai 623: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### Pembukaan tab

1. Klik icon Search di User List, ketik `Aktor Log {runId}-100`, tekan Enter
2. Klik Name `Aktor Log {runId}-100`
3. Klik Tab `System Log`

### TC-GS-USER-615: Screening Overlay Column Visibility

4. Klik header Column Visibility (⋯)
5. Verifikasi overlay memuat tujuh kolom berurutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`
6. Verifikasi ketujuh kolom pada overlay tercentang dan enabled (kolom Hideable)
7. Verifikasi ketujuh kolom pada overlay memiliki drag handle
8. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-616: Screening Popup Setup Column

9. Klik item `Setup Column...` pada overlay
10. Verifikasi bagian Header: Title `Setup Column`
11. Verifikasi bagian Header: deskripsi panduan tampil
12. Verifikasi bagian Header: icon `[✕]`
13. Verifikasi bagian Body: daftar tujuh kolom dengan checkbox
14. Verifikasi bagian Body: ketujuh kolom memiliki drag handle
15. Verifikasi bagian Body: ketujuh kolom memiliki icon Pin
16. Verifikasi bagian Body: preview tabel
17. Verifikasi bagian Footer: `[Reset to Default]` dan `[Save]`
18. Verifikasi bagian Footer: tidak ada `[Cancel]`

### TC-GS-USER-622: Guard satu kolom tersisa tidak bisa di-uncheck

19. Hilangkan centang enam kolom: `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value` (tersisa `Date`)
20. Hover checkbox `Date`
21. Verifikasi checkbox `Date` tetap tampil dan disabled
22. Verifikasi Tooltip `At least one column must remain visible.`
23. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-621: Tutup Setup Column via [✕] membuang perubahan

24. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Field`
25. Klik `[✕]`
26. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: tujuh kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value` tampil berurutan

### TC-GS-USER-623: Maksimal 3 kolom di-pin

27. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Date`
28. Klik icon Pin pada `Action`
29. Klik icon Pin pada `Object`
30. Hover icon Pin pada kolom keempat `Name`
31. Verifikasi icon Pin `Name` disabled
32. Verifikasi Tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
33. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-617: Setup Column hide/unhide kelas Hideable

34. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Date`
35. Verifikasi preview pada popup tidak memuat kolom `Date`
36. Klik `[Save]`
37. Verifikasi kolom `Date` tidak tampil di tabel
38. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Date`
39. Verifikasi preview pada popup memuat kolom `Date`
40. Klik `[Save]`
41. Verifikasi kolom `Date` tampil kembali di tabel
42. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Action`
43. Verifikasi preview pada popup tidak memuat kolom `Action`
44. Klik `[Save]`
45. Verifikasi kolom `Action` tidak tampil di tabel
46. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Action`
47. Verifikasi preview pada popup memuat kolom `Action`
48. Klik `[Save]`
49. Verifikasi kolom `Action` tampil kembali di tabel
50. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Object`
51. Verifikasi preview pada popup tidak memuat kolom `Object`
52. Klik `[Save]`
53. Verifikasi kolom `Object` tidak tampil di tabel
54. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Object`
55. Verifikasi preview pada popup memuat kolom `Object`
56. Klik `[Save]`
57. Verifikasi kolom `Object` tampil kembali di tabel
58. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Name`
59. Verifikasi preview pada popup tidak memuat kolom `Name`
60. Klik `[Save]`
61. Verifikasi kolom `Name` tidak tampil di tabel
62. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Name`
63. Verifikasi preview pada popup memuat kolom `Name`
64. Klik `[Save]`
65. Verifikasi kolom `Name` tampil kembali di tabel
66. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Field`
67. Verifikasi preview pada popup tidak memuat kolom `Field`
68. Klik `[Save]`
69. Verifikasi kolom `Field` tidak tampil di tabel
70. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Field`
71. Verifikasi preview pada popup memuat kolom `Field`
72. Klik `[Save]`
73. Verifikasi kolom `Field` tampil kembali di tabel
74. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Old Value`
75. Verifikasi preview pada popup tidak memuat kolom `Old Value`
76. Klik `[Save]`
77. Verifikasi kolom `Old Value` tidak tampil di tabel
78. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Old Value`
79. Verifikasi preview pada popup memuat kolom `Old Value`
80. Klik `[Save]`
81. Verifikasi kolom `Old Value` tampil kembali di tabel
82. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `New Value`
83. Verifikasi preview pada popup tidak memuat kolom `New Value`
84. Klik `[Save]`
85. Verifikasi kolom `New Value` tidak tampil di tabel
86. Muat ulang halaman (F5)
87. Klik Tab `System Log`
88. Verifikasi kolom `New Value` tetap tidak tampil setelah muat ulang halaman
89. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `New Value`
90. Verifikasi preview pada popup memuat kolom `New Value`
91. Klik `[Save]`
92. Verifikasi kolom `New Value` tampil kembali di tabel

### TC-GS-USER-618: Setup Column drag reorder kelas Hideable

93. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Date` ke posisi pertama
94. Verifikasi preview pada popup menempatkan `Date` di posisi pertama
95. Klik `[Save]`
96. Verifikasi kolom `Date` berada di posisi pertama tabel
97. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Action` ke posisi pertama
98. Verifikasi preview pada popup menempatkan `Action` di posisi pertama
99. Klik `[Save]`
100. Verifikasi kolom `Action` berada di posisi pertama tabel
101. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Object` ke posisi pertama
102. Verifikasi preview pada popup menempatkan `Object` di posisi pertama
103. Klik `[Save]`
104. Verifikasi kolom `Object` berada di posisi pertama tabel
105. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Name` ke posisi pertama
106. Verifikasi preview pada popup menempatkan `Name` di posisi pertama
107. Klik `[Save]`
108. Verifikasi kolom `Name` berada di posisi pertama tabel
109. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Field` ke posisi pertama
110. Verifikasi preview pada popup menempatkan `Field` di posisi pertama
111. Klik `[Save]`
112. Verifikasi kolom `Field` berada di posisi pertama tabel
113. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Old Value` ke posisi pertama
114. Verifikasi preview pada popup menempatkan `Old Value` di posisi pertama
115. Klik `[Save]`
116. Verifikasi kolom `Old Value` berada di posisi pertama tabel
117. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `New Value` ke posisi pertama
118. Verifikasi preview pada popup menempatkan `New Value` di posisi pertama
119. Klik `[Save]`
120. Verifikasi kolom `New Value` berada di posisi pertama tabel
121. Muat ulang halaman (F5)
122. Klik Tab `System Log`
123. Verifikasi urutan terakhir tetap tersimpan setelah muat ulang halaman: `New Value`, `Old Value`, `Field`, `Name`, `Object`, `Action`, `Date`

### TC-GS-USER-619: Setup Column pin/unpin kelas Hideable

124. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
125. Perkecil lebar viewport hingga tabel System Log dapat di-scroll horizontal
126. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Date`
127. Verifikasi preview pada popup menampilkan `Date` ter-pin
128. Klik `[Save]`
129. Scroll tabel System Log secara horizontal
130. Verifikasi kolom `Date` membeku (sticky) saat scroll horizontal
131. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Date`, lalu klik `[Save]`
132. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Action`
133. Verifikasi preview pada popup menampilkan `Action` ter-pin
134. Klik `[Save]`
135. Scroll tabel System Log secara horizontal
136. Verifikasi kolom `Action` membeku (sticky) saat scroll horizontal
137. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Action`, lalu klik `[Save]`
138. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Object`
139. Verifikasi preview pada popup menampilkan `Object` ter-pin
140. Klik `[Save]`
141. Scroll tabel System Log secara horizontal
142. Verifikasi kolom `Object` membeku (sticky) saat scroll horizontal
143. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Object`, lalu klik `[Save]`
144. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Name`
145. Verifikasi preview pada popup menampilkan `Name` ter-pin
146. Klik `[Save]`
147. Scroll tabel System Log secara horizontal
148. Verifikasi kolom `Name` membeku (sticky) saat scroll horizontal
149. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Name`, lalu klik `[Save]`
150. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Field`
151. Verifikasi preview pada popup menampilkan `Field` ter-pin
152. Klik `[Save]`
153. Scroll tabel System Log secara horizontal
154. Verifikasi kolom `Field` membeku (sticky) saat scroll horizontal
155. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Field`, lalu klik `[Save]`
156. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Old Value`
157. Verifikasi preview pada popup menampilkan `Old Value` ter-pin
158. Klik `[Save]`
159. Scroll tabel System Log secara horizontal
160. Verifikasi kolom `Old Value` membeku (sticky) saat scroll horizontal
161. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Old Value`, lalu klik `[Save]`
162. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `New Value`
163. Verifikasi preview pada popup menampilkan `New Value` ter-pin
164. Klik `[Save]`
165. Scroll tabel System Log secara horizontal
166. Verifikasi kolom `New Value` membeku (sticky) saat scroll horizontal
167. Muat ulang halaman (F5)
168. Klik Tab `System Log`
169. Scroll tabel System Log secara horizontal
170. Verifikasi kolom `New Value` tetap membeku setelah muat ulang halaman
171. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `New Value`, lalu klik `[Save]`
172. Pulihkan lebar viewport ke ukuran semula

### TC-GS-USER-620: Setup Column Reset to Default

173. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Old Value`, seret `Field` ke posisi pertama, lalu klik `[Save]`
174. Verifikasi kolom `Old Value` tidak tampil dan kolom `Field` berada di posisi pertama tabel
175. Klik header Column Visibility (⋯), lalu klik `Setup Column...`
176. Klik `[Reset to Default]`
177. Klik `[Save]`
178. Verifikasi susunan kolom kembali default: `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value` (tujuh kolom tampil)
179. Muat ulang halaman (F5)
180. Klik Tab `System Log`
181. Verifikasi susunan kolom default bertahan setelah muat ulang halaman

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `Siti Nurhaliza` sebagai pemilik System Log; Setup Column tidak bergantung pada isi baris, tetapi tabel perlu baris agar scroll horizontal dan pin teramati. Spec memakai user milik spec (`Aktor Log`) dengan riwayat yang diketahui (S-06, S-11).
- Urutan TC dalam spec: TC-GS-USER-615, 616, 622, 621, 623, 617, 618, 619, 620. Alasan: dua TC screening (615, 616) di awal; TC-GS-USER-622 (guard), 621 (`[✕]` membuang perubahan), dan 623 (batas pin) tidak menyimpan apa pun sehingga ditaruh sebelum TC yang menyimpan (bagian 3 konvensi: validasi diblokir sebelum aksi sukses); TC-GS-USER-617, 618, 619 menyimpan konfigurasi; TC-GS-USER-620 di akhir karena reset mengembalikan konfigurasi yang diubah TC sebelumnya.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 sampai 3 (membuka User Detail; Name dicari di User List), langkah 23, 25, dan 33 (menutup popup tanpa menyimpan sehingga perubahan dibuang), langkah 86 sampai 87, 121 sampai 122, 167 sampai 168, dan 179 sampai 180 (muat ulang halaman lalu membuka kembali Tab `System Log`, karena User Detail dibuka pada tab pertama), langkah 124 (reset ke default sebelum TC-GS-USER-619, S-09), langkah 125 (viewport diperkecil agar scroll horizontal teramati), langkah 171 (unpin `New Value` sebelum TC-GS-USER-620), dan langkah 172 (memulihkan viewport). Langkah unpin tiap kolom pada TC-GS-USER-619 adalah langkah TC. Langkah 174 (observasi perubahan sebelum reset) adalah asersi tambahan agar reset tidak lulus pada konfigurasi yang tidak berubah (S-03).
- Langkah membuka popup (klik header Column Visibility lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup tersebut, karena `[Save]` menutup popup dan tabel diamati sesudahnya.
- Persistensi sesudah muat ulang halaman (F5) diasersi sekali per TC pada konfigurasi akhir (langkah 88, 123, 170, 181), karena mekanisme penyimpanan sama untuk ketujuh kolom; penyimpanan tiap kolom setelah `[Save]` diasersi lewat tabel pada langkah `Verifikasi` setelahnya.
- Kolom Curated: tabel System Log tidak punya kolom Curated (semua kolom Hideable, PRD user.md §4.1.6), sehingga bagian Expected 615 b tentang kolom Curated unchecked tidak diasersi.
- Pembagian TC lintas spec: Search, Filter, Sort, Pagination Tab System Log di spec 096 sampai 099; Download di spec 101.
- Spec melewati sekitar 35 langkah (181 langkah) karena TC-GS-USER-617, 618, dan 619 masing-masing menguji tujuh kolom dengan `Verifikasi` per klausa Expected (S-01). Semua blok satu kelas (Setup Column Tab System Log), satu akun, satu dataset, dan tiap blok berdiri sendiri karena konfigurasi dikembalikan di tiap kolom (TC-GS-USER-617 dan 619) atau di-reset (TC-GS-USER-618 dan 620).
- Temuan untuk QA: (1) TC-GS-USER-616 Expected a menyebut "deskripsi panduan" tanpa teks; spec hanya mengasersi deskripsi tampil. (2) TC-GS-USER-617 sampai 619 langkah "uncheck lalu check, Save, refresh F5" bertentangan dengan hasil bersih (kolom kembali tampil) pada hide/unhide; spec memisahkan hide dan unhide dengan `[Save]` masing-masing. (3) TC-GS-USER-618 langkah menyeret `Date` ke posisi pertama padahal `Date` sudah pertama pada konfigurasi default; Expected tidak membedakannya dari kolom lain. (4) TC-GS-USER-619 tidak menyebut lebar viewport atau cara membuat tabel overflow agar scroll horizontal teramati. (5) TC-GS-USER-620 "Ubah urutan dan visibility kolom" tidak menyebut kolom; spec memakai sembunyikan `Old Value` dan seret `Field` ke posisi pertama. (6) TC-GS-USER-622 tidak menyebut kolom yang tersisa; spec menyisakan `Date`. (7) TC-GS-USER-623 tidak menyebut kolom yang di-pin; spec memakai `Date`, `Action`, `Object`, dengan `Name` sebagai kolom keempat. (8) TC-GS-USER-615 Expected b menyebut kolom Curated yang tidak ada di tabel ini. (9) Tempat penyimpanan preferensi Setup Column tab ini tidak disebut TC maupun PRD User.
