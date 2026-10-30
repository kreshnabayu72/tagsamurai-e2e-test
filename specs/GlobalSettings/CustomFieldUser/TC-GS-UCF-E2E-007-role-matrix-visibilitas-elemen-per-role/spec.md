---
id: TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Tab Custom Field per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-30
  - TC-GS-UCF-31
  - TC-GS-UCF-32
  - TC-GS-UCF-33
  - TC-GS-UCF-34
  - TC-GS-UCF-35
  - TC-GS-UCF-36
  - TC-GS-UCF-391
  - TC-GS-UCF-513
  - TC-GS-UCF-514
  - TC-GS-UCF-39
  - TC-GS-UCF-392
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tab Custom Field per Role

## Prerequisites

- Mode: FE+BE (backend nyata).
- Langkah mengikuti TC masing-masing; akun login dan hasil yang diharapkan berbeda per role. Password tidak ditulis di spec atau fixture.
- Layar awal: pembukaan Global Settings > User > Custom Field per role adalah bagian dari objek uji (visibilitas), sehingga ditulis di `## Test Steps`, bukan di hook `beforeEach`.

Role yang diuji (Tabel Data Uji Pre-setup; semua Client A):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-GS-UCF-30 | Total Control (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-UCF-391 | Default User (Teguh Santoso) | `defaultUser_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DEFAULT_PASSWORD` |
| TC-GS-UCF-36 | Manage user and role: Full CRUD (Bayu Saputra) | `manageUserFullCrud_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FULLCRUD_PASSWORD` |
| TC-GS-UCF-34 | Manage user and role: Update dan Read (Agus Wijaya) | `manageUserUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-UCF-35, 39 | Manage user and role: Delete dan Read (Dewi Lestari) | `manageUserDelete_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-UCF-33, 39 | Manage user and role: Create dan Read (Rina Marlina) | `manageUserCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-UCF-32, 514, 39 | Manage user and role: Read saja (Tono Hartono) | `manageUserRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
| TC-GS-UCF-31, 513, 39, 392 | Read Only (Maya Putri) | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |

- Akun aktor pertama (Total Control) login di hook `before`; akun berikutnya login lewat langkah ganti akun eksplisit di awal tiap blok. Karena spec berakhir di akun Read Only, hook `after` mengembalikan sesi ke akun Total Control default suite (`GS_TC_PASSWORD`).
- Data Pre-setup Client A (6 field, tetap di environment, hanya dibaca, tanpa suffix): `Cost Center` (Active) dan `Joining Date` (Inactive) dipakai langsung oleh langkah; field lain hanya membentuk isi tabel dan dipakai sebagai precondition TC (14 field), tidak diasersi.
- Population D-01 (8 field: `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`): di-seed lewat API di hook `before` (idempotent, dilewati bila sudah ada) sehingga tabel berisi tepat 14 field (precondition TC-GS-UCF-30 sampai 36, 391, 513, 514, 39, dan 392). Nama literal tanpa suffix (pengecualian S-12 butir (i)); fixture baru `Fixture.customFieldUser.population`. Hook `after` hanya menghapus field Population yang dibuat hook `before` spec ini.
- Spec tidak membuat, mengubah, atau menghapus data. Aksi Create, Edit, Delete, Activate, dan Deactivate tidak dijalankan; hanya visibilitas dan state kontrolnya yang diperiksa. Klik pada switch Active yang Disabled (TC-GS-UCF-39) tidak mengubah status. Tidak ada Data Dinamis.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk semua akun role di atas dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover; fokus keyboard (Tab); pembacaan state Enabled atau Disabled switch; pembacaan tooltip; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`) dan sesi akun (dipulihkan hook `after`). Capability tiap akun adalah data Pre-setup dan tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-30: Visibilitas elemen tab Custom Field untuk Total Control

1. Buka Global Settings > User > Custom Field
2. Verifikasi tab `Custom Field` tampil
3. Verifikasi baris tabel termuat
4. Verifikasi `[+ Custom Field]` tampil
5. Klik `⋯` pada baris `Cost Center`
6. Verifikasi row action `Edit` tampil
7. Verifikasi row action `Delete` tampil
8. Tutup menu `⋯` dengan Esc
9. Arahkan kursor ke switch Active baris `Cost Center`
10. Verifikasi switch Active baris `Cost Center` Enabled
11. Centang baris `Cost Center` (Active) dan baris `Joining Date` (Inactive)
12. Klik `Bulk Action`
13. Verifikasi kolom Checkbox tampil
14. Verifikasi Bulk Action Bar tampil dengan `Activate`, `Deactivate`, dan `Delete` (seleksi campuran)
15. Tutup overlay `Bulk Action` dengan Esc, lalu hapus centang baris `Cost Center` dan `Joining Date`
16. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
17. Verifikasi header kolom Column Visibility (⋯) tampil
18. Verifikasi header kolom yang dapat diurutkan tampil
19. Verifikasi Pagination tampil

### TC-GS-UCF-391: Visibilitas elemen tab Custom Field untuk Default User

20. Ganti akun: logout, lalu login sebagai Default User
21. Buka Global Settings > User > Custom Field
22. Verifikasi tab `Custom Field` tampil
23. Verifikasi baris tabel termuat
24. Verifikasi `[+ Custom Field]` tampil
25. Klik `⋯` pada baris `Cost Center`
26. Verifikasi row action `Edit` tampil
27. Verifikasi row action `Delete` tampil
28. Tutup menu `⋯` dengan Esc
29. Arahkan kursor ke switch Active baris `Cost Center`
30. Verifikasi switch Active baris `Cost Center` Enabled
31. Centang baris `Cost Center` (Active) dan baris `Joining Date` (Inactive)
32. Klik `Bulk Action`
33. Verifikasi kolom Checkbox tampil
34. Verifikasi Bulk Action Bar tampil dengan `Activate`, `Deactivate`, dan `Delete` (seleksi campuran)
35. Tutup overlay `Bulk Action` dengan Esc, lalu hapus centang baris `Cost Center` dan `Joining Date`
36. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
37. Verifikasi header kolom Column Visibility (⋯) tampil
38. Verifikasi header kolom yang dapat diurutkan tampil
39. Verifikasi Pagination tampil

### TC-GS-UCF-36: Visibilitas elemen tab Custom Field untuk Manage user and role: Full CRUD

40. Ganti akun: logout, lalu login sebagai Manage user and role: Full CRUD
41. Buka Global Settings > User > Custom Field
42. Verifikasi tab `Custom Field` tampil
43. Verifikasi baris tabel termuat
44. Verifikasi `[+ Custom Field]` tampil
45. Klik `⋯` pada baris `Cost Center`
46. Verifikasi row action `Edit` tampil
47. Verifikasi row action `Delete` tampil
48. Tutup menu `⋯` dengan Esc
49. Arahkan kursor ke switch Active baris `Cost Center`
50. Verifikasi switch Active baris `Cost Center` Enabled
51. Centang baris `Cost Center` (Active) dan baris `Joining Date` (Inactive)
52. Klik `Bulk Action`
53. Verifikasi kolom Checkbox tampil
54. Verifikasi Bulk Action Bar tampil dengan `Activate`, `Deactivate`, dan `Delete`
55. Tutup overlay `Bulk Action` dengan Esc, lalu hapus centang baris `Cost Center` dan `Joining Date`
56. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
57. Verifikasi header kolom Column Visibility (⋯) tampil
58. Verifikasi header kolom yang dapat diurutkan tampil
59. Verifikasi Pagination tampil

### TC-GS-UCF-34: Visibilitas elemen tab Custom Field untuk Manage user and role: Update dan Read

60. Ganti akun: logout, lalu login sebagai Manage user and role: Update dan Read
61. Buka Global Settings > User > Custom Field
62. Verifikasi tab `Custom Field` tampil
63. Verifikasi baris tabel termuat
64. Verifikasi `[+ Custom Field]` Hidden
65. Klik `⋯` pada baris `Cost Center`
66. Verifikasi row action `Edit` tampil
67. Verifikasi row action `Delete` Hidden
68. Tutup menu `⋯` dengan Esc
69. Arahkan kursor ke switch Active baris `Cost Center`
70. Verifikasi switch Active baris `Cost Center` Enabled
71. Centang baris `Cost Center` (Active) dan baris `Joining Date` (Inactive)
72. Klik `Bulk Action`
73. Verifikasi kolom Checkbox tampil
74. Verifikasi Bulk Action Bar tampil hanya dengan `Activate` dan `Deactivate`
75. Verifikasi `Delete` tidak tampil pada `Bulk Action`
76. Tutup overlay `Bulk Action` dengan Esc, lalu hapus centang baris `Cost Center` dan `Joining Date`
77. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
78. Verifikasi header kolom Column Visibility (⋯) tampil
79. Verifikasi header kolom yang dapat diurutkan tampil
80. Verifikasi Pagination tampil

### TC-GS-UCF-35: Visibilitas elemen tab Custom Field untuk Manage user and role: Delete dan Read

81. Ganti akun: logout, lalu login sebagai Manage user and role: Delete dan Read
82. Buka Global Settings > User > Custom Field
83. Verifikasi tab `Custom Field` tampil
84. Verifikasi baris tabel termuat
85. Verifikasi `[+ Custom Field]` Hidden
86. Klik `⋯` pada baris `Cost Center`
87. Verifikasi row action `Edit` Hidden
88. Verifikasi row action `Delete` tampil
89. Tutup menu `⋯` dengan Esc
90. Arahkan kursor ke switch Active baris `Cost Center`
91. Verifikasi switch Active baris `Cost Center` tampil Disabled
92. Verifikasi tooltip `You don't have permission to edit.`
93. Centang baris `Cost Center` (Active) dan baris `Joining Date` (Inactive)
94. Klik `Bulk Action`
95. Verifikasi kolom Checkbox tampil
96. Verifikasi Bulk Action Bar tampil hanya dengan `Delete`
97. Verifikasi `Activate` dan `Deactivate` tidak tampil pada `Bulk Action`
98. Tutup overlay `Bulk Action` dengan Esc, lalu hapus centang baris `Cost Center` dan `Joining Date`
99. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
100. Verifikasi header kolom Column Visibility (⋯) tampil
101. Verifikasi header kolom yang dapat diurutkan tampil
102. Verifikasi Pagination tampil

### TC-GS-UCF-39: Hover switch Active yang Disabled menampilkan alasan permission (aktor Delete dan Read)

103. Arahkan kursor ke switch Active baris `Cost Center`
104. Verifikasi tooltip `You don't have permission to edit.` tampil
105. Klik switch Active baris `Cost Center`
106. Verifikasi klik tidak membuka dialog `Deactivate Custom Field`
107. Verifikasi switch Active baris `Cost Center` tetap On

### TC-GS-UCF-33: Visibilitas elemen tab Custom Field untuk Manage user and role: Create dan Read

108. Ganti akun: logout, lalu login sebagai Manage user and role: Create dan Read
109. Buka Global Settings > User > Custom Field
110. Verifikasi tab `Custom Field` tampil
111. Verifikasi baris tabel termuat
112. Verifikasi `[+ Custom Field]` tampil
113. Perhatikan kolom Actions pada baris `Cost Center`
114. Verifikasi row action `Edit` dan `Delete` Hidden (menu `⋯` per baris tidak tampil)
115. Arahkan kursor ke switch Active baris `Cost Center`
116. Verifikasi switch Active baris `Cost Center` tampil Disabled
117. Verifikasi tooltip `You don't have permission to edit.`
118. Perhatikan kolom paling kiri tabel
119. Verifikasi kolom Checkbox Hidden
120. Verifikasi Bulk Action Bar Hidden
121. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
122. Verifikasi header kolom Column Visibility (⋯) tampil
123. Verifikasi header kolom yang dapat diurutkan tampil
124. Verifikasi Pagination tampil

### TC-GS-UCF-39: Hover switch Active yang Disabled menampilkan alasan permission (aktor Create dan Read)

125. Arahkan kursor ke switch Active baris `Cost Center`
126. Verifikasi tooltip `You don't have permission to edit.` tampil
127. Klik switch Active baris `Cost Center`
128. Verifikasi klik tidak membuka dialog `Deactivate Custom Field`
129. Verifikasi switch Active baris `Cost Center` tetap On

### TC-GS-UCF-32: Visibilitas elemen tab Custom Field untuk Manage user and role: Read saja

130. Ganti akun: logout, lalu login sebagai Manage user and role: Read saja
131. Buka Global Settings > User > Custom Field
132. Verifikasi tab `Custom Field` tampil
133. Verifikasi baris tabel termuat
134. Verifikasi `[+ Custom Field]` Hidden
135. Perhatikan kolom Actions pada baris `Cost Center`
136. Verifikasi row action `Edit` dan `Delete` Hidden (menu `⋯` per baris tidak tampil)
137. Arahkan kursor ke switch Active baris `Cost Center`
138. Verifikasi switch Active baris `Cost Center` tampil Disabled
139. Verifikasi tooltip `You don't have permission to edit.`
140. Perhatikan kolom paling kiri tabel
141. Verifikasi kolom Checkbox Hidden
142. Verifikasi Bulk Action Bar Hidden
143. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
144. Verifikasi header kolom Column Visibility (⋯) tampil
145. Verifikasi header kolom yang dapat diurutkan tampil
146. Verifikasi Pagination tampil

### TC-GS-UCF-514: Manage user and role: Read saja melihat field Inactive dengan switch Active Off dan Disabled

147. Perhatikan baris `Joining Date`
148. Verifikasi baris `Joining Date` tampil di tabel dengan switch Active Off
149. Arahkan kursor ke switch Active baris `Joining Date`
150. Verifikasi switch Active baris `Joining Date` tampil Disabled
151. Verifikasi tooltip `You don't have permission to edit.`

### TC-GS-UCF-39: Hover switch Active yang Disabled menampilkan alasan permission (aktor Read saja)

152. Arahkan kursor ke switch Active baris `Cost Center`
153. Verifikasi tooltip `You don't have permission to edit.` tampil
154. Klik switch Active baris `Cost Center`
155. Verifikasi klik tidak membuka dialog `Deactivate Custom Field`
156. Verifikasi switch Active baris `Cost Center` tetap On

### TC-GS-UCF-31: Visibilitas elemen tab Custom Field untuk Read Only

157. Ganti akun: logout, lalu login sebagai Read Only
158. Buka Global Settings > User > Custom Field
159. Verifikasi tab `Custom Field` tampil
160. Verifikasi baris tabel termuat
161. Verifikasi `[+ Custom Field]` Hidden
162. Perhatikan kolom Actions pada baris `Cost Center`
163. Verifikasi row action `Edit` dan `Delete` Hidden (menu `⋯` per baris tidak tampil)
164. Arahkan kursor ke switch Active baris `Cost Center`
165. Verifikasi switch Active baris `Cost Center` tampil Disabled
166. Verifikasi tooltip `You don't have permission to edit.`
167. Perhatikan kolom paling kiri tabel
168. Verifikasi kolom Checkbox Hidden
169. Verifikasi Bulk Action Bar Hidden
170. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
171. Verifikasi header kolom Column Visibility (⋯) tampil
172. Verifikasi header kolom yang dapat diurutkan tampil
173. Verifikasi Pagination tampil

### TC-GS-UCF-513: Read Only melihat field Inactive dengan switch Active Off dan Disabled

174. Perhatikan baris `Joining Date`
175. Verifikasi baris `Joining Date` tampil di tabel dengan switch Active Off
176. Arahkan kursor ke switch Active baris `Joining Date`
177. Verifikasi switch Active baris `Joining Date` tampil Disabled
178. Verifikasi tooltip `You don't have permission to edit.`

### TC-GS-UCF-39: Hover switch Active yang Disabled menampilkan alasan permission (aktor Read Only)

179. Arahkan kursor ke switch Active baris `Cost Center`
180. Verifikasi tooltip `You don't have permission to edit.` tampil
181. Klik switch Active baris `Cost Center`
182. Verifikasi klik tidak membuka dialog `Deactivate Custom Field`
183. Verifikasi switch Active baris `Cost Center` tetap On

### TC-GS-UCF-392: Tooltip switch Active yang Disabled dapat diakses lewat fokus keyboard

184. Pindahkan kursor keluar dari tabel (kursor tidak digerakkan lagi sesudahnya)
185. Tekan Tab berulang sampai fokus berada di switch Active baris `Cost Center`
186. Verifikasi tooltip `You don't have permission to edit.` tampil saat switch menerima fokus keyboard (bukan hanya saat hover)
187. Verifikasi switch Active baris `Cost Center` tetap Disabled
188. Verifikasi switch Active baris `Cost Center` berstatus On

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi): matriks visibilitas elemen per role yang memuat polaritas tampil dan Hidden/Disabled; `caseType` Positive mengikuti alur dominan (bagian 8). Jumlah langkah (188) di atas smell sekitar 35 langkah karena delapan role dijalankan berurutan, bukan karena beberapa kelas harness; satu kelas (baca visibilitas), tiap blok role berdiri sendiri dengan langkah ganti akun eksplisit, dan kegagalan satu blok tidak menghilangkan makna blok lain. Langkah tiap role berbeda (Expected berbeda per role) sehingga spec ditulis per blok role, bukan perulangan atas tabel "Role yang diuji".
- Urutan blok role: Total Control (30), Default User (391), Full CRUD (36), Update dan Read (34), Delete dan Read (35), Create dan Read (33), Read saja (32), Read Only (31). Urutan ini menyimpang dari daftar sumber supaya ganti akun satu kali per role. TC-GS-UCF-39 (empat aktor: Read Only, Read saja, Create dan Read, Delete dan Read) dijalankan di dalam blok keempat role itu, bukan sebagai blok sendiri dengan empat ganti akun tambahan; TC-GS-UCF-513 menyatu dengan blok Read Only dan TC-GS-UCF-514 dengan blok Read saja; TC-GS-UCF-392 (Read Only) ditaruh terakhir karena hanya valid bila kursor tidak digerakkan sesudah Tab.
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti akun (langkah 20 dan awal tiap blok role berikutnya), membuka Global Settings > User > Custom Field, menutup menu `⋯` dengan Esc, mencentang baris lalu menutup overlay `Bulk Action` dan menghapus centang (seleksi dipakai hanya untuk memunculkan Bulk Action Bar), mengarahkan kursor ke elemen sebagai pemicu hover, dan memindahkan kursor keluar tabel sebelum Tab pada TC-GS-UCF-392. Aksi Activate, Deactivate, dan Delete tidak dijalankan.
- Asersi `Hidden` (mis. `[+ Custom Field]`, kolom Checkbox, Bulk Action Bar, row action) beranchor tab `Custom Field` tampil dan baris tabel termuat pada tiga langkah pembuka tiap blok, serta Table Tools dan Pagination yang diverifikasi tampil di akhir blok (bagian 8b butir 2). Asersi "Bulk Action Bar Hidden" pada role tanpa kolom Checkbox diamati tanpa seleksi karena kolom Checkbox sendiri Hidden.
- Expected f tiap TC menyebut Search, Filter, Download, Changelog, header Column Visibility, header kolom yang dapat diurutkan, dan Pagination "tampil"; spec mengasersi tiap kelompok tampil tanpa menjalankan fungsinya (fungsi diuji di spec tabel utama).
- Temuan untuk QA:
  - Email Pre-setup TC (`manageUserRead_automated_qaTeam1@...`, `manageUserCreate_...`, `manageUserUpdate_...`, `manageUserDelete_...`) berbeda dari email di komentar `.env.example` untuk `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, dan `GS_DELETE_PASSWORD` (`readCapability_...`, `createOnly_...`, `updateOnly_...`, `deleteOnly_...`), dan `GS_DEFAULT_PASSWORD` serta `GS_FULLCRUD_PASSWORD` memakai pola `{namaCompany}`. Spec memakai email TC dan nama env yang sudah terdaftar; tim FE perlu memastikan satu env var untuk satu akun yang sama.
  - TC-GS-UCF-30, 34, 35, 36, dan 391 menyebut `⋯` pada baris `Cost Center` dan mencentang `Cost Center` dan `Joining Date` tanpa menyebut halaman; spec mengasumsikan keduanya di halaman 1 (urutan default dengan 14 field).
  - TC-GS-UCF-39 tidak menyebut efek klik pada switch Disabled selain dialog; spec mengasersi dialog `Deactivate Custom Field` tidak terbuka dan switch tetap On sesuai Expected b.
  - TC-GS-UCF-30 Expected f memuat "header kolom yang dapat diurutkan" tanpa menyebut kolom; spec mengasersi header kolom sortable pada TC-GS-UCF-2 tampil.
