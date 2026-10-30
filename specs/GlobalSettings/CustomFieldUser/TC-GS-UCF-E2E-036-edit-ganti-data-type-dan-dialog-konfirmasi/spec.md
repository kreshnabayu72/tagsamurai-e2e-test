---
id: TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi
title: "Edit Custom Field: Ganti Data Type, Dialog Change Data Type, Pengosongan Nilai User, Pemulihan Data Type Tersimpan, Validasi Inline Sebelum Dialog, dan Backdrop Dialog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-473
  - TC-GS-UCF-474
  - TC-GS-UCF-475
  - TC-GS-UCF-110
  - TC-GS-UCF-372
  - TC-GS-UCF-408
  - TC-GS-UCF-108
  - TC-GS-UCF-103
  - TC-GS-UCF-104
  - TC-GS-UCF-460
  - TC-GS-UCF-373
  - TC-GS-UCF-105
  - TC-GS-UCF-106
  - TC-GS-UCF-107
coverage:
  web: automated
---

# Edit Custom Field: Ganti Data Type, Dialog Change Data Type, Pengosongan Nilai User, Pemulihan Data Type Tersimpan, Validasi Inline Sebelum Dialog, dan Backdrop Dialog

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (login di hook `before`; password hanya lewat env var): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`.
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`; langkah yang berpindah ke Detail User, Changelog User, atau Activity Log kembali ke tab Custom Field lewat langkah eksplisit.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup Client A (hanya dibuka, tidak pernah disimpan; Last Updated dan Modified By barisnya tidak berubah; 14 field di-seed hook `before` lewat API dengan `Fixture.customFieldUser.preset14`): `Cost Center` (Dropdown, nilai User Rahmat Hidayat = `Finance`) dan `Bonus` (Numeric, Decimal Places 2, nilai User Rahmat Hidayat = `1500.50`) untuk TC-GS-UCF-408 (S-06: dialog dibatalkan).
- Akun Login User Client A: `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Rahmat Hidayat) dan `intanPermata_automated_qaTeam1@qwertysystem.net` (Intan Permata), pemilik nilai Custom Field yang dibaca pada Detail User (tidak dipakai login).
- Data Dinamis milik spec (seeding lewat API di hook `before`, bersuffix `{runId}-036`; fixture baru `Fixture.customFieldUser.edit036`; Active, Required No, Placeholder kosong kecuali dinyatakan lain; nilai User di-seed lewat mekanisme yang disediakan tim FE/BE):
  - `Pre Dialog Probe {runId}-036`: Text, nilai User Rahmat Hidayat = `Keep` (TC-GS-UCF-473, 474, 475).
  - `Dt Probe ToDd {runId}-036`: Text, belum pernah bernilai (TC-GS-UCF-110).
  - `Order Chk Field {runId}-036`: Text, nilai User Rahmat Hidayat = `Alpha` (TC-GS-UCF-372).
  - `Dt Probe Cancel {runId}-036`: Dropdown `Up`, `Down`, nilai User Rahmat Hidayat = `Up` (TC-GS-UCF-108).
  - `Dt Probe Empty {runId}-036`: Text, belum pernah bernilai (TC-GS-UCF-103).
  - `Dt Probe Emptied {runId}-036`: Text; pernah bernilai lalu dikosongkan lewat ganti Data Type, kini tanpa nilai User (TC-GS-UCF-104; keadaan "pernah bernilai" di-seed lewat mekanisme yang disediakan tim FE/BE).
  - `Dt Log Probe {runId}-036`: Text, belum pernah bernilai (TC-GS-UCF-460).
  - `Round Trip DD {runId}-036`: Dropdown `Red`, `Blue`, nilai User Rahmat Hidayat = `Red` (TC-GS-UCF-373).
  - `Dt Probe Values {runId}-036`: Dropdown `One`, `Two`, nilai User Rahmat Hidayat = `One` dan Intan Permata = `Two` (TC-GS-UCF-105, 106, 107).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-036` (menghapus pula nilai User terkait).
- Kemampuan teknis: membaca daftar request jaringan yang terekam sejak popup dibuka (asersi "tidak memuat request tulis ke server"); membaca Changelog Custom Field, Changelog User (sub-tab Login User), System Log Detail User, dan Activity Log tab `User Action` dengan Search; jam server dan jam browser sinkron.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Persiapan tabel

1. Ketik Search `{runId}-036`, tekan Enter

### TC-GS-UCF-473: Field Name kosong dan Data Type diubah pada field bernilai menampilkan error Field Name tanpa dialog Change Data Type

2. Klik `⋯` pada baris `Pre Dialog Probe {runId}-036`, pilih `Edit`
3. Ubah Data Type menjadi `Numeric`
4. Hapus seluruh isi Field Name
5. Klik `[Save]`
6. Verifikasi error inline `Field name must not be empty`
7. Verifikasi dialog `Change Data Type` tidak tampil
8. Verifikasi popup tetap terbuka
9. Verifikasi tidak ada toast sukses
10. Klik `[✕]`
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`

### TC-GS-UCF-474: Field Name 121 karakter dan Data Type diubah pada field bernilai menampilkan error Field Name tanpa dialog Change Data Type

13. Klik `⋯` pada baris `Pre Dialog Probe {runId}-036`, pilih `Edit`
14. Ubah Data Type menjadi `Numeric`
15. Ganti Field Name dengan 121 karakter `A`
16. Klik `[Save]`
17. Verifikasi error inline `Max. 120 characters` pada Field Name
18. Verifikasi dialog `Change Data Type` tidak tampil
19. Verifikasi popup tetap terbuka
20. Verifikasi tidak ada toast sukses
21. Klik `[✕]`
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`

### TC-GS-UCF-475: Placeholder 121 karakter dan Data Type diubah pada field bernilai menampilkan error Placeholder tanpa dialog Change Data Type

24. Klik `⋯` pada baris `Pre Dialog Probe {runId}-036`, pilih `Edit`
25. Ubah Data Type menjadi `Numeric`
26. Ketik 121 karakter `A` di Placeholder
27. Klik `[Save]`
28. Verifikasi error inline `Max. 120 characters` pada Placeholder
29. Verifikasi dialog `Change Data Type` tidak tampil
30. Verifikasi popup tetap terbuka
31. Verifikasi tidak ada toast sukses
32. Klik `[✕]`
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`

### TC-GS-UCF-110: Ganti Data Type ke Dropdown tanpa value ditolak saat Save

35. Klik `⋯` pada baris `Dt Probe ToDd {runId}-036`, pilih `Edit`
36. Ubah Data Type menjadi `Dropdown`
37. Klik `[Save]`
38. Verifikasi error inline `Dropdown values must not be empty`
39. Periksa daftar request jaringan yang terekam sejak popup dibuka
40. Verifikasi daftar request tidak memuat request tulis ke server
41. Klik `[✕]`
42. Verifikasi dialog `Unsaved Changes` tampil
43. Klik `[Leave]`
44. Verifikasi kolom Data Type baris `Dt Probe ToDd {runId}-036` tetap `Text`

### TC-GS-UCF-372: Save Data Type menjadi Dropdown tanpa value pada field bernilai menampilkan error nilai Dropdown kosong sebelum dialog Change Data Type

45. Klik `⋯` pada baris `Order Chk Field {runId}-036`, pilih `Edit`
46. Ubah Data Type menjadi `Dropdown`, biarkan Dropdown Values kosong
47. Klik `[Save]`
48. Verifikasi error inline `Dropdown values must not be empty`
49. Verifikasi dialog `Change Data Type` tidak tampil
50. Periksa daftar request jaringan yang terekam sejak popup dibuka
51. Verifikasi daftar request tidak memuat request tulis ke server
52. Ketik value `Beta`, tekan Enter, klik `[Save]`
53. Verifikasi dialog `Change Data Type` tampil dengan bullet `Order Chk Field {runId}-036`
54. Klik `[Cancel]`
55. Verifikasi popup tetap terbuka dengan Data Type `Dropdown`
56. Verifikasi badge `Beta` tetap berada di form
57. Klik `[✕]`
58. Verifikasi dialog `Unsaved Changes` tampil
59. Klik `[Leave]`
60. Verifikasi kolom Data Type baris `Order Chk Field {runId}-036` tetap `Text`
61. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
62. Verifikasi nilai `Alpha` pada `Order Chk Field {runId}-036` tidak berubah
63. Kembali ke Global Settings > User > Custom Field, ketik Search `{runId}-036`, tekan Enter

### TC-GS-UCF-408: Klik backdrop tidak menutup dialog Change Data Type, Remove Value, dan Decimal Places Locked pada Edit

64. Ganti isi kotak search dengan `Cost Center`, tekan Enter
65. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
66. Ubah Data Type menjadi `Text`, klik `[Save]`
67. Klik backdrop di luar dialog
68. Verifikasi dialog `Change Data Type` tetap tampil
69. Klik `[Cancel]`
70. Verifikasi dialog tertutup
71. Verifikasi popup Edit tetap terbuka
72. Klik `[✕]`
73. Verifikasi dialog `Unsaved Changes` tampil
74. Klik `[Leave]`
75. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
76. Klik `×` pada badge `Finance`
77. Klik backdrop di luar dialog
78. Verifikasi dialog `Remove Value` dengan bullet `Finance` tetap tampil
79. Klik `[Cancel]`
80. Verifikasi dialog tertutup
81. Verifikasi badge `Finance` tetap berada di form
82. Klik `[✕]`
83. Ganti isi kotak search dengan `Bonus`, tekan Enter
84. Klik `⋯` pada baris `Bonus`, pilih `Edit`
85. Pilih Decimal Places `1`
86. Klik backdrop di luar dialog
87. Verifikasi dialog `Decimal Places Locked` tetap tampil
88. Klik `[OK]`
89. Verifikasi dialog tertutup
90. Verifikasi Decimal Places kembali `2`
91. Klik `[✕]`
92. Verifikasi `Cost Center` tidak berubah
93. Verifikasi `Bonus` tidak berubah
94. Ganti isi kotak search dengan `{runId}-036`, tekan Enter

### TC-GS-UCF-108: Cancel pada dialog Change Data Type tidak mengubah apa pun

95. Klik `⋯` pada baris `Dt Probe Cancel {runId}-036`, pilih `Edit`
96. Ubah Data Type menjadi `Date`, klik `[Save]`
97. Klik `[Cancel]` pada dialog
98. Verifikasi dialog tertutup
99. Verifikasi tidak ada toast
100. Klik `[✕]`
101. Verifikasi dialog `Unsaved Changes` tampil
102. Klik `[Leave]`
103. Verifikasi baris `Dt Probe Cancel {runId}-036` tetap `Dropdown`
104. Verifikasi Value Setting baris `Dt Probe Cancel {runId}-036` memuat value `Up`, `Down`
105. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
106. Verifikasi Detail User Rahmat Hidayat tetap menampilkan `Up` pada `Dt Probe Cancel {runId}-036`
107. Kembali ke Global Settings > User > Custom Field, ketik Search `{runId}-036`, tekan Enter

### TC-GS-UCF-103: Data Type diubah pada field tanpa nilai User tidak memunculkan dialog

108. Klik `⋯` pada baris `Dt Probe Empty {runId}-036`, pilih `Edit`
109. Ubah Data Type menjadi `Numeric`
110. Klik `[Save]`
111. Verifikasi dialog `Change Data Type` tidak tampil
112. Verifikasi toast sukses: "Success, custom field has been updated."
113. Verifikasi Data Type baris `Dt Probe Empty {runId}-036` berubah menjadi `Numeric`
114. Verifikasi Value Setting baris `Dt Probe Empty {runId}-036` menampilkan `0 Decimal Places` (Decimal Places awal `0`)

### TC-GS-UCF-104: Data Type diubah pada field yang nilainya sudah dikosongkan tidak memunculkan dialog

115. Klik `⋯` pada baris `Dt Probe Emptied {runId}-036`, pilih `Edit`
116. Ubah Data Type menjadi `Date`
117. Klik `[Save]`
118. Verifikasi dialog `Change Data Type` tidak tampil (tidak ada nilai saat ini untuk di-reset)
119. Verifikasi toast sukses: "Success, custom field has been updated."

### TC-GS-UCF-460: Ganti Data Type tanpa perubahan teks Value Setting hanya mencatat entri Data Type

120. Klik `⋯` pada baris `Dt Log Probe {runId}-036`, pilih `Edit`
121. Ubah Data Type menjadi `Date`, klik `[Save]`
122. Verifikasi dialog `Change Data Type` tidak tampil
123. Verifikasi toast sukses: "Success, custom field has been updated."
124. Buka Changelog Custom Field, Search `Dt Log Probe {runId}-036`
125. Verifikasi Changelog memuat 1 entri Edit: Field `Dt Log Probe {runId}-036 — Data Type`, Old Value `Text`, New Value `Date`
126. Verifikasi Changelog tidak memuat entri dengan Field `Dt Log Probe {runId}-036 — Value Setting` (anchor: entri Data Type di atas tampil pada Modal Changelog yang sama)
127. Tutup Modal Changelog

### TC-GS-UCF-373: Kembali memilih Data Type tersimpan dalam satu form Edit memulihkan value tersimpan tanpa dialog

128. Klik `⋯` pada baris `Round Trip DD {runId}-036`, pilih `Edit`
129. Ubah Data Type menjadi `Text`
130. Verifikasi Dropdown Values tidak tampil
131. Pilih kembali Data Type `Dropdown`
132. Verifikasi badge `Red` dan `Blue` pulih
133. Klik `[Save]`
134. Verifikasi toast netral (Info): "No changes to save."
135. Verifikasi dialog `Change Data Type` tidak tampil
136. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
137. Verifikasi nilai `Red` pada `Round Trip DD {runId}-036` tidak berubah
138. Kembali ke Global Settings > User > Custom Field, ketik Search `{runId}-036`, tekan Enter

### TC-GS-UCF-105: Data Type diubah pada field yang sudah memiliki nilai User memunculkan dialog konfirmasi

139. Klik `⋯` pada baris `Dt Probe Values {runId}-036`, pilih `Edit`
140. Ubah Data Type menjadi `Text`
141. Klik `[Save]`
142. Verifikasi dialog `Change Data Type` (warning) tampil dengan bullet `Dt Probe Values {runId}-036`
143. Verifikasi body dialog `Changing the data type will reset all existing values for this field. This action cannot be undone.`
144. Verifikasi pertanyaan dialog `Are you sure you want to change it?`
145. Verifikasi tombol dialog `[Cancel]` dan `[Change Data Type]`
146. Verifikasi belum ada perubahan tersimpan selama dialog tampil (baris `Dt Probe Values {runId}-036` di belakang dialog tetap `Dropdown`)

### TC-GS-UCF-106: Konfirmasi Change Data Type mengosongkan seluruh nilai User dan membuang Dropdown Values

147. Klik `[Change Data Type]`
148. Verifikasi toast sukses: "Success, custom field has been updated."
149. Verifikasi Data Type baris `Dt Probe Values {runId}-036` `Text`
150. Verifikasi Value Setting baris `Dt Probe Values {runId}-036` `—`
151. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
152. Verifikasi field `Dt Probe Values {runId}-036` tampil kosong
153. Verifikasi nilai `One` tidak ada
154. Buka Global Settings > User > Detail Intan Permata, section Custom Fields
155. Verifikasi field `Dt Probe Values {runId}-036` tampil kosong
156. Verifikasi nilai `Two` tidak ada
157. Buka Global Settings > User > Custom Field, klik icon Changelog, Search `Dt Probe Values {runId}-036`
158. Verifikasi Changelog Custom Field memuat entri Edit Field `Dt Probe Values {runId}-036 — Data Type` dengan Old Value `Dropdown` dan New Value `Text`
159. Verifikasi Changelog Custom Field memuat entri Edit Field `Dt Probe Values {runId}-036 — Value Setting` dengan Old Value `One, Two` dan New Value `-`
160. Tutup Modal Changelog
161. Buka Global Settings > User > User List (sub-tab Login User), klik icon Changelog
162. Verifikasi Modal Changelog User memuat sedikitnya satu entri (data pembanding)
163. Search `Dt Probe Values {runId}-036`
164. Verifikasi hasil Search menampilkan empty state "No results found" (tidak ada entri dengan Field `Dt Probe Values {runId}-036` untuk Rahmat Hidayat maupun Intan Permata)
165. Tutup Modal Changelog
166. Buka Global Settings > User > Detail Sari Dewi > tab System Log, Search `Dt Probe Values {runId}-036`
167. Verifikasi System Log memuat entri Object `Custom Field` dengan Name `Dt Probe Values {runId}-036`
168. Verifikasi System Log tidak memuat entri Object `User` dengan Field `Dt Probe Values {runId}-036` (anchor: entri Object `Custom Field` di atas tampil pada surface yang sama)
169. Buka Global Settings > Activity Log > tab `User Action`, Search `Dt Probe Values {runId}-036`
170. Verifikasi Activity Log tab `User Action` memuat entri Object `Custom Field` dengan Name `Dt Probe Values {runId}-036` dan Modified By `Sari D`
171. Verifikasi Activity Log tab `User Action` tidak memuat entri Object `User` dengan Field `Dt Probe Values {runId}-036` (anchor: entri Object `Custom Field` di atas tampil pada surface yang sama)
172. Kembali ke Global Settings > User > Custom Field, ketik Search `{runId}-036`, tekan Enter

### TC-GS-UCF-107: Ganti Data Type membuang Dropdown Values dan tipe baru mulai dari default

173. Klik `⋯` pada baris `Dt Probe Values {runId}-036`, pilih `Edit`
174. Ubah Data Type kembali menjadi `Dropdown`
175. Verifikasi Dropdown Values kosong (value lama `One`, `Two` tidak kembali)
176. Klik `[Save]` tanpa menambah value
177. Verifikasi error inline `Dropdown values must not be empty`
178. Periksa daftar request jaringan yang terekam sejak popup dibuka
179. Verifikasi daftar request tidak memuat request tulis ke server
180. Klik `[✕]`
181. Verifikasi dialog `Unsaved Changes` tampil
182. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 182 langkah (di atas smell sekitar 35 langkah): seluruhnya satu kelas (fungsional, ganti Data Type pada popup Edit), satu akun; tiap blok memakai field seed bersuffix sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, kecuali TC-GS-UCF-105, 106, dan 107 yang memakai `Dt Probe Values` berurutan sesuai dependensi TC (105 lalu 106 lalu 107). Jumlah langkah muncul dari satu baris per aksi, perpindahan ke Detail User, Changelog, System Log, dan Activity Log pada TC-GS-UCF-106, dan satu `Verifikasi` per klausa Expected.
- Urutan TC: validasi yang diblokir (TC-GS-UCF-473, 474, 475, 110, 372), dialog yang dibatalkan (TC-GS-UCF-408, 108), perubahan tanpa dialog (TC-GS-UCF-103, 104, 460), No-Op (TC-GS-UCF-373), lalu perubahan yang mengosongkan nilai User (TC-GS-UCF-105, 106, 107) di akhir (prinsip 5). Urutan berbeda dari TC sumber. TC-GS-UCF-105 berakhir pada dialog yang masih tampil dan TC-GS-UCF-106 melanjutkan dengan `[Change Data Type]` pada form dan dialog yang sama (langkah 1 sampai 3 TC-GS-UCF-106 identik dengan TC-GS-UCF-105; S-04).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target atau mengganti target; kembali ke tab Custom Field dari Detail User; membuka dan menutup Modal Changelog; menutup popup lewat `✕` (pada form dirty ditulis `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]`, S-08). Pada TC-GS-UCF-108 langkah 4 TC ("klik [Leave] bila dialog muncul") ditulis deterministik: form tetap dirty setelah `[Cancel]` karena Data Type `Date` berbeda dari nilai tersimpan, sehingga dialog `Unsaved Changes` diasersi. Pada TC-GS-UCF-373 dan 408 langkah `✕` tanpa dialog dilakukan pada form yang kembali bersih.
- Asersi tidak ada entri (TC-GS-UCF-106: Changelog User, System Log Detail User, Activity Log; TC-GS-UCF-460: entri Value Setting) memakai anchor positif pada surface yang sama atau empty state "No results found" setelah Search berbaseline nama bersuffix unik (S-12, butir 2 konvensi 8b). Aksi pemicunya (ganti Data Type yang mengosongkan nilai User) ada di spec ini (P-1: state berat bagian dari aksi yang sama); asersi absence kelas g lain ada di spec 070.
- Pembagian TC lintas spec: TC-GS-UCF-102, 540, 375 (form stale saat Decimal Places atau Data Type) ada di spec 038; TC-GS-UCF-109, 461, 367 (Decimal Places terkunci) ada di spec 035.
- Temuan untuk QA:
  - TC-GS-UCF-106 mensyaratkan Changelog User bernama sub-tab Login User, System Log tab di Detail Sari Dewi, dan Activity Log tab `User Action`; teks UI modul lain mengikuti TC (S-02) dan tidak dapat ditelusuri ulang oleh penulis slice.
  - TC-GS-UCF-106: Expected f ("Changelog: User tidak memuat entri ... Field `Dt Probe Values`") ditulis dengan Search berbaseline dan empty state; Post Condition "Dt Probe Values bertipe Text tanpa nilai User" tidak punya langkah observasi tambahan (sudah dicakup Expected c, d).
  - TC-GS-UCF-107: Post Condition tidak ada; Expected c dibaca melalui daftar request jaringan.
  - TC-GS-UCF-460: Post Condition "Dt Log Probe bertipe Date" diasersi lewat Expected b.
  - TC-GS-UCF-103: Expected c "Decimal Places awal `0`" diasersi lewat Value Setting `0 Decimal Places` pada tabel (Decimal Places tidak terlihat di tabel selain lewat teks Value Setting).
  - TC-GS-UCF-408: langkah 1 TC memakai `Cost Center` (Pre-setup) sebagai target dialog yang dibatalkan; spec tidak menyimpan apa pun pada `Cost Center` dan `Bonus` (S-06).
  - TC-GS-UCF-473, 474, 475, 110, 372: tidak ada Post Condition; "perubahan tidak tersimpan" diasersi sebatas UI.
  - Keputusan NC-21 (dialog `D-01` berdasarkan ada nilai saat ini) dan NC-23 (Data Type berubah dari Dropdown juga mencatat entri Value Setting) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan.
