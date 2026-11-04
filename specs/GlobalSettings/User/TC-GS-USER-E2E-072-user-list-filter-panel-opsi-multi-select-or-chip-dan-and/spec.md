---
id: TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and
title: "User List: Filter Panel (Screening Field, Opsi dari Tabel, Multi-Select, OR, Pencarian Dropdown, Chip, Rentang Tanggal, dan AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-421
  - TC-GS-USER-422
  - TC-GS-USER-423
  - TC-GS-USER-424
  - TC-GS-USER-425
  - TC-GS-USER-426
  - TC-GS-USER-427
  - TC-GS-USER-428
  - TC-GS-USER-429
coverage:
  web: automated
---

# User List: Filter Panel (Screening Field, Opsi dari Tabel, Multi-Select, OR, Pencarian Dropdown, Chip, Rentang Tanggal, dan AND)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (admin kedua; hanya sesi API untuk membuat U-2 agar Modified By berbeda dari U-1). Keduanya didaftarkan di `executionConfig.environmentVariables`.
- Admin kedua: akun Total Control kedua yang disediakan tim FE (tidak ada di Tabel Pre-setup TC). Nama tampil admin kedua tidak memuat `Siti N`. Sesi UI kedua tidak dipakai.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan Custom Field aktif No. 24, hanya dibaca): `Dewi Lestari` (Active), `Jane Smith` (Inactive), `John Doe` (Activated), serta user Pre-setup lain di tabel Login User. Last Update baris Pre-setup lebih lama dari hari uji, dan Temporary Until baris Pre-setup tidak jatuh pada hari uji + 45 hari (kondisi disediakan tim FE; spec tidak mengubah Pre-setup).
- Data Dinamis, di-seed lewat API di hook `before`. Kemampuan seeding user lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD). Field wajib yang bukan objek uji: Access sesuai tabel, Division sesuai tabel, dan Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) dengan Country Code `🇮🇩 +62` dan Number `81234567890`. Tanggal diformat mengikuti Date Format General Settings client (default environment `DD/MM/YY`).
  - U-1 (dibuat lewat sesi API Total Control, sehingga Modified By `Siti N`): Name `Gandhi Pranoto {runId}-072`, Email `gandhipranoto+{runId}-072@qwertysystem.net`, Position `Supervisor`, Division `Logistics`, Access `Fixed Asset`, Temporary User dengan Temporary Until hari uji + 45 hari. Status awal `Pending Activation`.
  - U-2 (dibuat lewat sesi API admin kedua, sehingga Modified By berbeda dari U-1): Name `Hesti Maharani {runId}-072`, Email `hestimaharani+{runId}-072@qwertysystem.net`, Position `Internal Auditor`, Division `Legal`, Access `Supply Asset`, bukan Temporary User.
  - U-3: Name `Indra Wibowo {runId}-072`, Email `indrawibowo+{runId}-072@qwertysystem.net`, Position `Supervisor`, Division `Legal`, Access `Fixed Asset`.
  - U-4: Name `Kartika Ayu {runId}-072`, Email `kartikaayu+{runId}-072@qwertysystem.net`, Position `Internal Auditor`, Division `Logistics`, Access `Fixed Asset`.
  - Master Data tanpa user (dibuat lewat API di hook `before`, kemampuan disediakan tim FE/BE): Position `Posisi Kosong {runId}-072` dan Division `Divisi Kosong {runId}-072`, tidak dipakai user mana pun, dipakai untuk asersi bahwa nilai master tanpa baris tidak menjadi opsi dropdown (TC-GS-USER-422).
  - Seeding minimal (S-11): U-1 dan U-2 membawa nilai berbeda pada kolom yang difilter; U-3 dan U-4 hanya untuk asersi AND (TC-GS-USER-429).
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 sampai U-4 lewat API, lalu hapus Position `Posisi Kosong {runId}-072` dan Division `Divisi Kosong {runId}-072`.
- Data uji: Status `Active` dan `Inactive`; Position `Supervisor`; Division `Logistics`; Access `Fixed Asset`; Modified By `Siti N`; Activation Status `Pending Activation`; Temporary User `Yes`; rentang tanggal `{tanggal hari uji}` (bagian tanggal sel Last Update U-1) dan `{tanggal TU}` (bagian tanggal sel Temporary Until U-1), keduanya dibaca dari tabel pada langkah 7.
- State yang diubah dan dipulihkan: ukuran halaman 100 (langkah 1) dikembalikan ke 10 (langkah 180); kolom `Activation Status`, `Temporary User`, `Temporary Until` ditampilkan (langkah 2 sampai 6) dan disembunyikan lagi (langkah 175 sampai 179); Filter dikosongkan di akhir tiap blok dan di langkah 172. Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (Setup Column > `[Reset to Default]`, `[Save]`, atau penghapusan preferensi kolom User List di browser; mekanisme disediakan tim FE/BE).
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel; membaca teks sel tabel dan teks input date range; mengetik pada pencarian di dalam dropdown filter.

## Test Steps

### Persiapan tampilan

1. Pilih 100 baris per halaman pada Pagination
2. Klik header kolom Column Visibility (⋯)
3. Centang `Activation Status`
4. Centang `Temporary User`
5. Centang `Temporary Until`
6. Tekan Esc untuk menutup Overlay Column Visibility
7. Baca bagian tanggal sel Last Update baris `Gandhi Pranoto {runId}-072` sebagai `{tanggal hari uji}` dan sel Temporary Until baris `Gandhi Pranoto {runId}-072` sebagai `{tanggal TU}`
8. Baca kumpulan nilai distinct kolom Active, Position, Division, Access, Modified By, Activation Status, dan Temporary User dari seluruh baris tabel (nilai `—` tidak dihitung)

### TC-GS-USER-421: Screening Filter Panel

9. Klik icon Filter
10. Verifikasi Filter Panel terbuka
11. Verifikasi field `Status` bertipe multi-select searchable dengan placeholder `All statuses`
12. Verifikasi field `Position` bertipe multi-select searchable dengan placeholder `All positions`
13. Verifikasi field `Division` bertipe multi-select searchable dengan placeholder `All divisions`
14. Verifikasi field `Access` bertipe multi-select searchable dengan placeholder `All products`
15. Verifikasi field `Modified By` bertipe multi-select searchable dengan placeholder `All users`
16. Verifikasi field `Activation Status` bertipe multi-select searchable dengan placeholder `All statuses`
17. Verifikasi field `Temporary User` bertipe multi-select searchable dengan placeholder `All options`
18. Verifikasi field `Last Update` bertipe date range picker dengan placeholder `Select date`
19. Verifikasi field `Temporary Until` bertipe date range picker dengan placeholder `Select date`
20. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-422: Opsi dropdown filter diambil dari nilai yang ada di tabel

21. Buka dropdown Status
22. Verifikasi dropdown Status: opsi sama dengan kumpulan nilai kolom Active yang tampil di baris tabel (langkah 8), tanpa nilai lain
23. Tutup dropdown Status
24. Buka dropdown Position
25. Verifikasi dropdown Position: opsi sama dengan kumpulan nilai kolom Position yang tampil di baris tabel (langkah 8), tanpa nilai lain
26. Verifikasi dropdown Position: opsi `Posisi Kosong {runId}-072` (nilai master tanpa baris) tidak tampil
27. Tutup dropdown Position
28. Buka dropdown Division
29. Verifikasi dropdown Division: opsi sama dengan kumpulan nilai kolom Division yang tampil di baris tabel (langkah 8), tanpa nilai lain
30. Verifikasi dropdown Division: opsi `Divisi Kosong {runId}-072` (nilai master tanpa baris) tidak tampil
31. Tutup dropdown Division
32. Buka dropdown Access
33. Verifikasi dropdown Access: opsi sama dengan kumpulan nilai kolom Access yang tampil di baris tabel (langkah 8), tanpa nilai lain
34. Tutup dropdown Access
35. Buka dropdown Modified By
36. Verifikasi dropdown Modified By: opsi sama dengan kumpulan nilai kolom Modified By yang tampil di baris tabel (langkah 8), tanpa nilai lain
37. Tutup dropdown Modified By
38. Buka dropdown Activation Status
39. Verifikasi dropdown Activation Status: opsi sama dengan kumpulan nilai kolom Activation Status yang tampil di baris tabel (langkah 8), tanpa nilai lain
40. Tutup dropdown Activation Status
41. Buka dropdown Temporary User
42. Verifikasi dropdown Temporary User: opsi sama dengan kumpulan nilai kolom Temporary User yang tampil di baris tabel (langkah 8), tanpa nilai lain
43. Tutup dropdown Temporary User

### TC-GS-USER-423: Filter multi-select per field menyaring baris

44. Pilih opsi `Inactive` pada Status
45. Klik `[Apply]`
46. Verifikasi field Status: badge titik tampil pada icon Filter
47. Verifikasi field Status: baris `Jane Smith` (nilai terpilih) tampil
48. Verifikasi field Status: baris `Dewi Lestari` (nilai lain) tidak tampil
49. Klik icon Filter
50. Verifikasi field Status: icon Filter berubah gelap
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Klik icon Filter
54. Pilih opsi `Supervisor` pada Position
55. Klik `[Apply]`
56. Verifikasi field Position: badge titik tampil pada icon Filter
57. Verifikasi field Position: baris `Gandhi Pranoto {runId}-072` (nilai terpilih) tampil
58. Verifikasi field Position: baris `Hesti Maharani {runId}-072` (nilai lain) tidak tampil
59. Klik icon Filter
60. Verifikasi field Position: icon Filter berubah gelap
61. Klik `[Clear Field]`
62. Klik `[Apply]`
63. Klik icon Filter
64. Pilih opsi `Logistics` pada Division
65. Klik `[Apply]`
66. Verifikasi field Division: badge titik tampil pada icon Filter
67. Verifikasi field Division: baris `Gandhi Pranoto {runId}-072` (nilai terpilih) tampil
68. Verifikasi field Division: baris `Hesti Maharani {runId}-072` (nilai lain) tidak tampil
69. Klik icon Filter
70. Verifikasi field Division: icon Filter berubah gelap
71. Klik `[Clear Field]`
72. Klik `[Apply]`
73. Klik icon Filter
74. Pilih opsi `Fixed Asset` pada Access
75. Klik `[Apply]`
76. Verifikasi field Access: badge titik tampil pada icon Filter
77. Verifikasi field Access: baris `Gandhi Pranoto {runId}-072` (nilai terpilih) tampil
78. Verifikasi field Access: baris `Hesti Maharani {runId}-072` (nilai lain) tidak tampil
79. Klik icon Filter
80. Verifikasi field Access: icon Filter berubah gelap
81. Klik `[Clear Field]`
82. Klik `[Apply]`
83. Klik icon Filter
84. Pilih opsi `Siti N` pada Modified By
85. Klik `[Apply]`
86. Verifikasi field Modified By: badge titik tampil pada icon Filter
87. Verifikasi field Modified By: baris `Gandhi Pranoto {runId}-072` (nilai terpilih) tampil
88. Verifikasi field Modified By: baris `Hesti Maharani {runId}-072` (nilai lain) tidak tampil
89. Klik icon Filter
90. Verifikasi field Modified By: icon Filter berubah gelap
91. Klik `[Clear Field]`
92. Klik `[Apply]`
93. Klik icon Filter
94. Pilih opsi `Pending Activation` pada Activation Status
95. Klik `[Apply]`
96. Verifikasi field Activation Status: badge titik tampil pada icon Filter
97. Verifikasi field Activation Status: baris `Gandhi Pranoto {runId}-072` (nilai terpilih) tampil
98. Verifikasi field Activation Status: baris `John Doe` (nilai lain) tidak tampil
99. Klik icon Filter
100. Verifikasi field Activation Status: icon Filter berubah gelap
101. Klik `[Clear Field]`
102. Klik `[Apply]`
103. Klik icon Filter
104. Pilih opsi `Yes` pada Temporary User
105. Klik `[Apply]`
106. Verifikasi field Temporary User: badge titik tampil pada icon Filter
107. Verifikasi field Temporary User: baris `Gandhi Pranoto {runId}-072` (nilai terpilih) tampil
108. Verifikasi field Temporary User: baris `Hesti Maharani {runId}-072` (nilai lain) tidak tampil
109. Klik icon Filter
110. Verifikasi field Temporary User: icon Filter berubah gelap
111. Klik `[Clear Field]`
112. Klik `[Apply]`

### TC-GS-USER-424: 2 opsi dalam satu field filter digabung OR

113. Klik icon Filter
114. Pilih opsi `Active` pada Status
115. Pilih opsi `Inactive` pada Status
116. Klik `[Apply]`
117. Verifikasi baris dengan Status `Active` (`Dewi Lestari`) tampil
118. Verifikasi baris dengan Status `Inactive` (`Jane Smith`) tampil
119. Klik icon Filter
120. Klik `[Clear Field]`
121. Klik `[Apply]`

### TC-GS-USER-425: Search di dalam dropdown filter mempersempit opsi

122. Klik icon Filter
123. Buka dropdown Status
124. Verifikasi dropdown Status menampilkan opsi `Active` dan `Inactive` sebelum diketik
125. Ketik `NACT` pada pencarian di dalam dropdown Status
126. Verifikasi opsi `Inactive` tampil (substring, tanpa membedakan huruf besar/kecil)
127. Verifikasi opsi `Active` tidak tampil
128. Ganti isi pencarian di dalam dropdown Status dengan `zzz`
129. Verifikasi tidak ada opsi yang cocok di dropdown Status
130. Kosongkan pencarian di dalam dropdown Status, lalu tutup dropdown Status

### TC-GS-USER-426: Hapus chip filter via (X) meng-uncheck opsi

131. Pilih opsi `Active` pada Status
132. Pilih opsi `Inactive` pada Status
133. Klik (X) pada chip pertama (`Active`)
134. Verifikasi chip `Active` hilang
135. Verifikasi chip `Inactive` tetap tampil
136. Buka dropdown Status
137. Verifikasi checkbox opsi `Active` di dropdown Status tidak tercentang
138. Tutup dropdown Status
139. Klik `[Clear Field]`

### TC-GS-USER-427: Uncheck opsi di dropdown menghapus chip

140. Pilih opsi `Active` pada Status
141. Pilih opsi `Inactive` pada Status
142. Buka dropdown Status
143. Hilangkan centang opsi kedua (`Inactive`) di dropdown Status
144. Verifikasi chip `Inactive` hilang
145. Verifikasi chip `Active` tetap tampil
146. Tutup dropdown Status
147. Klik `[Clear Field]`

### TC-GS-USER-428: Filter date range per field

148. Pilih rentang tanggal `{tanggal hari uji}` sampai `{tanggal hari uji}` pada Last Update
149. Verifikasi input Last Update menampilkan rentang tanggal berformat Date Format General Settings (`DD/MM/YY`)
150. Klik `[Apply]`
151. Verifikasi field Last Update: baris `Gandhi Pranoto {runId}-072` dan baris `Hesti Maharani {runId}-072` (Last Update dalam rentang) tampil
152. Verifikasi field Last Update: baris `Dewi Lestari` (Last Update di luar rentang) tidak tampil
153. Klik icon Filter
154. Klik `[Clear Field]`
155. Klik `[Apply]`
156. Klik icon Filter
157. Pilih rentang tanggal `{tanggal TU}` sampai `{tanggal TU}` pada Temporary Until
158. Verifikasi input Temporary Until menampilkan rentang tanggal berformat Date Format General Settings (`DD/MM/YY`)
159. Klik `[Apply]`
160. Verifikasi field Temporary Until: baris `Gandhi Pranoto {runId}-072` (Temporary Until dalam rentang) tampil
161. Verifikasi field Temporary Until: baris `Hesti Maharani {runId}-072` dan baris `Dewi Lestari` (Temporary Until di luar rentang atau kosong) tidak tampil
162. Klik icon Filter
163. Klik `[Clear Field]`
164. Klik `[Apply]`

### TC-GS-USER-429: Kombinasi 2 field filter digabung AND

165. Klik icon Filter
166. Pilih opsi `Supervisor` pada Position
167. Pilih opsi `Logistics` pada Division
168. Klik `[Apply]`
169. Verifikasi baris `Gandhi Pranoto {runId}-072` (Position `Supervisor`, Division `Logistics`) tampil
170. Verifikasi baris `Indra Wibowo {runId}-072` (hanya Position `Supervisor`) tidak tampil
171. Verifikasi baris `Kartika Ayu {runId}-072` (hanya Division `Logistics`) tidak tampil

### Pemulihan state

172. Klik icon Filter
173. Klik `[Clear Field]`
174. Klik `[Apply]`
175. Klik header kolom Column Visibility (⋯)
176. Hilangkan centang `Activation Status`
177. Hilangkan centang `Temporary User`
178. Hilangkan centang `Temporary Until`
179. Tekan Esc untuk menutup Overlay Column Visibility
180. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Urutan TC sumber (421 sampai 429) dipertahankan; TC-GS-USER-421 (screening tanpa aksi) berada di awal.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 agar seluruh baris seed dan Pre-setup berada di halaman yang sama), langkah 2 sampai 6 (menampilkan kolom curated lewat Overlay Column Visibility agar nilai Activation Status, Temporary User, dan Temporary Until terbaca), langkah 7 dan 8 (membaca tanggal dan kumpulan nilai kolom dari tabel), `Klik icon Filter`, `Klik [Clear Field]`, `Klik [Apply]` di akhir tiap blok (mengosongkan Filter, S-09), `Tutup dropdown`, `Klik [Clear Field]` di antara TC-GS-USER-425 sampai 427 (mengembalikan Filter Panel ke keadaan kosong), serta langkah 172 sampai 180 (memulihkan Filter, kolom, dan ukuran halaman).
- Panel Filter menutup sesudah `[Apply]`; karena itu tiap pengosongan Filter diawali `Klik icon Filter`. Filter Panel yang masih terbuka dari TC-GS-USER-421 dipakai TC-GS-USER-422 dan field pertama TC-GS-USER-423.
- Asersi pembanding (S-03, bagian 8b butir 2): tiap `Verifikasi` ketiadaan baris didahului `Verifikasi` baris yang tampil pada tabel yang sama; `Verifikasi` ketiadaan opsi dropdown (Position dan Division) didahului `Verifikasi` kesamaan opsi dengan nilai tabel.
- TC-GS-USER-422: asersi "hanya nilai yang genuinely muncul di baris tabel" ditulis sebagai kesamaan opsi dropdown dengan kumpulan nilai kolom yang dibaca dari tabel (langkah 8); untuk Position dan Division ditambah `Verifikasi` bahwa nilai master tanpa baris (`Posisi Kosong {runId}-072`, `Divisi Kosong {runId}-072`) tidak menjadi opsi.
- Spec melewati sekitar 35 langkah karena sembilan TC Filter Panel berbagi satu layar, satu panel, dan satu dataset (U-1 sampai U-4 dan Pre-setup), dan semuanya satu kelas harness (fungsional, baca saja). TC-GS-USER-423 menguji tujuh field dengan blok identik (pilih opsi, Apply, dua asersi baris, asersi icon, kosongkan Filter); tiap blok berdiri sendiri. Memisahkannya mengulang login, seeding, dan pembukaan layar yang sama.
- Pembagian TC lintas spec: TC-GS-USER-430 sampai 434, 463, 464 (kombinasi Search dan Filter, filter kolom hidden, Custom Field) diverifikasi di spec 073; Search di spec 071; Sort dan Pagination di spec 074.
- Temuan untuk QA:
  - TC-GS-USER-424: field Status hanya memiliki dua opsi (`Active`, `Inactive`), sehingga gabungan OR mencakup semua baris dan tidak membedakan OR dari tanpa filter. Spec mengasersi dua baris (satu per opsi) sesuai TC; TC perlu field dengan lebih dari dua opsi bila OR harus teramati.
  - TC-GS-USER-428: format tanggal pada input tidak disebut konkret di TC (hanya "mengikuti Date Format General Settings"); spec mengasersi `DD/MM/YY` (default environment). TC juga tidak menyebut tanggal yang dipakai; spec memakai bagian tanggal sel Last Update dan Temporary Until U-1.
  - TC-GS-USER-423 dan 422: label opsi Activation Status (`Pending Activation`, `Activated`) dan Temporary User (`Yes`, `No`) mengikuti Tabel Pre-setup dan TC-GS-USER-1061; TC tidak menyebut label opsi dropdown secara literal.
  - TC-GS-USER-425: TC tidak menyebut teks keadaan "tidak ada opsi cocok"; spec hanya mengasersi tidak ada opsi yang tampil.
  - TC-GS-USER-429: TC hanya menyebut "Isi 2 field filter berbeda"; spec memakai Position `Supervisor` dan Division `Logistics` dengan U-3 dan U-4 sebagai baris yang hanya memenuhi satu kriteria.
  - TC-GS-USER-421 dan 463: daftar field Filter Panel tidak memuat field Custom Field aktif (`Blood Type`, `Skills`, `Emergency Phone`), sedangkan TC-GS-USER-463 menyatakan Custom Field aktif muncul sebagai filter sesudah kolomnya dicentang. Spec 072 mengasersi sembilan field TC-GS-USER-421 (Custom Field belum dicentang di Setup Column).
