---
id: TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus
title: "Edit Custom Field Dropdown: Tambah, Rename, dan Hapus Value, Dialog Remove Value, Cascade ke Nilai User, Tukar Label, dan Minimal Satu Value"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-114
  - TC-GS-UCF-115
  - TC-GS-UCF-113
  - TC-GS-UCF-366
  - TC-GS-UCF-117
  - TC-GS-UCF-118
  - TC-GS-UCF-120
  - TC-GS-UCF-336
  - TC-GS-UCF-111
  - TC-GS-UCF-112
  - TC-GS-UCF-370
  - TC-GS-UCF-376
  - TC-GS-UCF-377
  - TC-GS-UCF-337
  - TC-GS-UCF-116
  - TC-GS-UCF-119
coverage:
  web: automated
---

# Edit Custom Field Dropdown: Tambah, Rename, dan Hapus Value, Dialog Remove Value, Cascade ke Nilai User, Tukar Label, dan Minimal Satu Value

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (login di hook `before`; password hanya lewat env var): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`.
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`; langkah yang berpindah ke Detail User atau form `[+ User]` kembali ke tab Custom Field lewat langkah eksplisit.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup tidak dipakai kecuali akun Login User Client A `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Rahmat Hidayat) dan `intanPermata_automated_qaTeam1@qwertysystem.net` (Intan Permata), pemilik nilai Custom Field yang dibaca pada Detail User (tidak dipakai login).
- Data Dinamis milik spec (seeding lewat API di hook `before`, bersuffix `{runId}-037`; fixture baru `Fixture.customFieldUser.edit037`; Dropdown, Active, Required No, Placeholder kosong; nilai User di-seed lewat mekanisme yang disediakan tim FE/BE):
  - `Rename DD {runId}-037`: `Red`, `Green`, `Blue`; Rahmat Hidayat = `Green`, Intan Permata = `Green` (TC-GS-UCF-111, 112, 113, 114, 115).
  - `Remove DD {runId}-037`: `Low`, `Mid`, `High`; Rahmat Hidayat = `Mid`, Intan Permata = `Mid` (TC-GS-UCF-116 dan 119).
  - `Remove DD Cancel {runId}-037`: `Low`, `Mid`, `High`; Rahmat Hidayat = `Mid` (TC-GS-UCF-117).
  - `Remove DD Leave {runId}-037`: `Low`, `Mid`, `High`; Rahmat Hidayat = `Mid` (TC-GS-UCF-118).
  - `Last Value DD {runId}-037`: `Solo`, belum dipakai (TC-GS-UCF-120).
  - `Used Last DD {runId}-037`: `Only`; Rahmat Hidayat = `Only` (TC-GS-UCF-336).
  - `Swap All DD {runId}-037`: `Old1`, `Old2`; Rahmat Hidayat = `Old1` (TC-GS-UCF-337).
  - `Swap DD {runId}-037`: `Alpha`, `Beta`, bebas nilai User (TC-GS-UCF-370).
  - `Swap Users DD {runId}-037`: `Alpha`, `Beta`; Rahmat Hidayat = `Alpha`, Intan Permata = `Beta` (TC-GS-UCF-376).
  - `Readd DD {runId}-037`: `Alpha`, `Beta`; Rahmat Hidayat = `Alpha` (TC-GS-UCF-377).
  - `Rename Edge {runId}-037`: `Alpha`, `Beta` (TC-GS-UCF-366).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-037` (menghapus pula nilai User terkait); tutup form `[+ User]` bila masih terbuka tanpa menyimpan.
- Kemampuan teknis: membaca daftar request jaringan yang terekam sejak popup dibuka (asersi "tidak memuat request tulis ke server"); membaca opsi dropdown field Custom Field pada form `[+ User]` (Global Settings > User > User List, sub-tab Login User).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-UCF-114 dan TC-GS-UCF-115: Rename dan tambah value ke nama yang sudah ada ditolak

1. Ketik Search `Rename DD {runId}-037`, tekan Enter
2. Klik `⋯` pada baris `Rename DD {runId}-037`, pilih `Edit`
3. Klik teks badge `Blue`, ubah menjadi `red`, tekan Enter
4. Verifikasi error inline `Option name already exists` (tanpa membedakan huruf besar kecil)
5. Verifikasi perubahan dibatalkan dan badge kembali `Blue`
6. Ketik `RED` di Dropdown Values, tekan Enter
7. Verifikasi error inline `Option name already exists`
8. Verifikasi badge `RED` tidak ditambahkan
9. Klik `[✕]`

### TC-GS-UCF-113: Rename value hanya berlaku di form sampai Save dan dibuang saat Leave

10. Klik `⋯` pada baris `Rename DD {runId}-037`, pilih `Edit`
11. Ubah badge `Red` menjadi `Crimson`, tekan Enter
12. Verifikasi badge berubah di form setelah Enter
13. Periksa daftar request jaringan yang terekam sejak popup dibuka
14. Verifikasi daftar request tidak memuat request tulis ke server
15. Klik `[✕]`
16. Verifikasi dialog `Unsaved Changes` tampil
17. Klik `[Leave]`
18. Klik `⋯` pada baris `Rename DD {runId}-037`, pilih `Edit`
19. Verifikasi badge `Red` ditampilkan (bukan `Crimson`)
20. Klik `[✕]`

### TC-GS-UCF-366: Rename value Dropdown, Esc membatalkan, klik di luar menerapkan, nilai kosong ditolak

21. Ganti isi kotak search dengan `Rename Edge {runId}-037`, tekan Enter
22. Klik `⋯` pada baris `Rename Edge {runId}-037`, pilih `Edit`
23. Klik teks badge `Alpha`, ubah menjadi `Zeta`, tekan Esc
24. Verifikasi badge kembali `Alpha`
25. Klik teks badge `Alpha`, ubah menjadi `Zeta`, klik area kosong di luar badge
26. Verifikasi badge `Zeta` diterapkan di form tanpa dialog
27. Klik teks badge `Beta`, hapus seluruh teks, tekan Enter
28. Verifikasi error inline `Option name must not be empty`
29. Verifikasi badge `Beta` kembali ke teks lama
30. Klik teks badge `Beta`, ketik 3 spasi, klik area kosong di luar badge
31. Verifikasi error inline `Option name must not be empty`
32. Verifikasi badge `Beta` kembali ke teks lama
33. Klik `[✕]`
34. Verifikasi dialog `Unsaved Changes` tampil
35. Klik `[Leave]`
36. Verifikasi `Rename Edge {runId}-037` tidak berubah

### TC-GS-UCF-117: Cancel dialog Remove Value mempertahankan badge

37. Ganti isi kotak search dengan `Remove DD Cancel {runId}-037`, tekan Enter
38. Klik `⋯` pada baris `Remove DD Cancel {runId}-037`, pilih `Edit`
39. Klik `×` pada badge `Mid`
40. Klik `[Cancel]`
41. Verifikasi dialog `Remove Value` tertutup
42. Verifikasi badge `Mid` tetap ada di form
43. Klik `[✕]`
44. Verifikasi popup tertutup tanpa dialog `Unsaved Changes` (form tidak dirty karena perubahan)

### TC-GS-UCF-118: Hapus value lalu Leave popup membuang penghapusan

45. Ganti isi kotak search dengan `Remove DD Leave {runId}-037`, tekan Enter
46. Klik `⋯` pada baris `Remove DD Leave {runId}-037`, pilih `Edit`
47. Klik `×` pada `Mid`, klik `[Remove]`
48. Klik `[✕]`
49. Verifikasi dialog `Unsaved Changes` tampil
50. Klik `[Leave]`
51. Verifikasi popup tertutup
52. Verifikasi definisi field `Remove DD Leave {runId}-037` tetap `Low`, `Mid`, `High`
53. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
54. Verifikasi Detail User Rahmat Hidayat tetap menampilkan `Mid` pada `Remove DD Leave {runId}-037`
55. Kembali ke Global Settings > User > Custom Field

### TC-GS-UCF-120: Value terakhir dapat dihapus tanpa dialog blok lalu Save ditolak

56. Ketik Search `Last Value DD {runId}-037`, tekan Enter
57. Klik `⋯` pada baris `Last Value DD {runId}-037`, pilih `Edit`
58. Perhatikan kontrol `×` pada badge `Solo`
59. Verifikasi kontrol `×` Enabled pada value terakhir
60. Klik `×`
61. Verifikasi badge hilang tanpa dialog blok
62. Klik `[Save]`
63. Verifikasi error inline `Dropdown values must not be empty`
64. Periksa daftar request jaringan yang terekam sejak popup dibuka
65. Verifikasi daftar request tidak memuat request tulis ke server
66. Klik `[✕]`
67. Verifikasi dialog `Unsaved Changes` tampil
68. Klik `[Leave]`

### TC-GS-UCF-336: Menghapus value terakhir yang dipakai user, konfirmasi lalu Save ditolak karena nilai Dropdown kosong dan nilai User utuh

69. Ganti isi kotak search dengan `Used Last DD {runId}-037`, tekan Enter
70. Klik `⋯` pada baris `Used Last DD {runId}-037`, pilih `Edit`
71. Klik `×` pada badge `Only`
72. Verifikasi dialog `Remove Value` dengan bullet `Only`
73. Verifikasi body dialog `Used by 1 user(s). Removing it will clear this value from their profile — they'll need to select a new one. This will take effect when you save.`
74. Verifikasi pertanyaan dialog `Are you sure you want to remove it?`
75. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`
76. Klik `[Remove]`
77. Verifikasi badge `Only` hilang dari form
78. Verifikasi tidak ada toast
79. Klik `[Save]`
80. Verifikasi error inline `Dropdown values must not be empty`
81. Periksa daftar request jaringan yang terekam sejak popup dibuka
82. Verifikasi daftar request tidak memuat request tulis ke server (setelah `[Remove]` maupun setelah `[Save]`)
83. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
84. Verifikasi Detail User Rahmat Hidayat tetap menampilkan `Only` pada `Used Last DD {runId}-037`
85. Kembali ke Global Settings > User > Custom Field

### TC-GS-UCF-111: Menambah value Dropdown pada Edit non-destruktif tanpa konfirmasi

86. Ketik Search `Rename DD {runId}-037`, tekan Enter
87. Klik `⋯` pada baris `Rename DD {runId}-037`, pilih `Edit`
88. Ketik `Yellow`, tekan Enter
89. Klik `[Save]`
90. Verifikasi tidak ada dialog konfirmasi
91. Verifikasi toast sukses: "Success, custom field has been updated."
92. Verifikasi Value Setting baris `Rename DD {runId}-037` menampilkan `Red`, `Green`, lalu `+2 more` (Blue, Yellow)
93. Verifikasi `Yellow` berada di akhir urutan
94. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
95. Verifikasi nilai `Green` tidak berubah
96. Buka Global Settings > User > User List (sub-tab Login User), klik `[+ User]`
97. Buka dropdown field `Rename DD {runId}-037`
98. Verifikasi dropdown memuat opsi `Red`, `Green`, `Blue`, `Yellow` berurutan sesuai urutan penambahan
99. Tutup form `[+ User]`
100. Buka Global Settings > User > Custom Field, ketik Search `Rename DD {runId}-037`, tekan Enter

### TC-GS-UCF-112: Rename value Dropdown yang dipakai user di-cascade tanpa dialog

101. Klik `⋯` pada baris `Rename DD {runId}-037`, pilih `Edit`
102. Klik teks badge `Green`, ubah menjadi `Emerald`, tekan Enter
103. Verifikasi tidak ada dialog konfirmasi saat rename
104. Klik `[Save]`
105. Verifikasi tidak ada dialog konfirmasi saat Save
106. Verifikasi toast sukses: "Success, custom field has been updated."
107. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
108. Verifikasi Detail User Rahmat Hidayat menampilkan `Emerald` tanpa memilih ulang
109. Buka Detail User Intan Permata
110. Verifikasi Detail User Intan Permata menampilkan `Emerald` tanpa memilih ulang
111. Buka Global Settings > User > User List (sub-tab Login User), klik `[+ User]`
112. Buka dropdown field `Rename DD {runId}-037`
113. Verifikasi dropdown memuat opsi `Red`, `Emerald`, `Blue`, `Yellow` berurutan
114. Verifikasi dropdown tidak memuat opsi `Green`
115. Tutup form `[+ User]`
116. Buka Global Settings > User > Custom Field

### TC-GS-UCF-370: Menukar label dua value Dropdown lewat nama sementara dalam satu Save diterima

117. Ketik Search `Swap DD {runId}-037`, tekan Enter
118. Klik `⋯` pada baris `Swap DD {runId}-037`, pilih `Edit`
119. Klik teks badge `Alpha`, ubah menjadi `Beta`, tekan Enter
120. Verifikasi error inline `Option name already exists`
121. Verifikasi badge kembali `Alpha`
122. Klik teks badge `Alpha`, ubah menjadi `Tmp`, tekan Enter
123. Verifikasi tidak ada error
124. Klik teks badge `Beta`, ubah menjadi `Alpha`, tekan Enter
125. Verifikasi tidak ada error
126. Klik teks badge `Tmp`, ubah menjadi `Beta`, tekan Enter
127. Verifikasi tidak ada error
128. Klik `[Save]`
129. Verifikasi toast sukses: "Success, custom field has been updated."
130. Klik `⋯` pada baris `Swap DD {runId}-037`, pilih `Edit`
131. Verifikasi Edit menampilkan badge berurutan `Beta`, `Alpha`
132. Klik `[✕]`

### TC-GS-UCF-376: Menukar label dua value Dropdown memindahkan label sedangkan nilai User tetap terikat pada opsinya

133. Ganti isi kotak search dengan `Swap Users DD {runId}-037`, tekan Enter
134. Klik `⋯` pada baris `Swap Users DD {runId}-037`, pilih `Edit`
135. Ubah badge `Alpha` menjadi `Tmp`, tekan Enter
136. Verifikasi tidak ada dialog `Remove Value`
137. Verifikasi tidak ada error
138. Ubah badge `Beta` menjadi `Alpha`, tekan Enter
139. Verifikasi tidak ada error
140. Ubah badge `Tmp` menjadi `Beta`, tekan Enter
141. Verifikasi tidak ada error
142. Klik `[Save]`
143. Verifikasi toast sukses: "Success, custom field has been updated."
144. Verifikasi Value Setting baris `Swap Users DD {runId}-037` menampilkan badge `Beta`, `Alpha` berurutan
145. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
146. Verifikasi Rahmat Hidayat menampilkan `Beta` pada `Swap Users DD {runId}-037`
147. Buka Detail User Intan Permata, section Custom Fields
148. Verifikasi Intan Permata menampilkan `Alpha` pada `Swap Users DD {runId}-037` (nilai mengikuti opsi, label berpindah)
149. Buka Global Settings > User > Custom Field, klik icon Changelog, Search `Swap Users DD {runId}-037`
150. Verifikasi Changelog memuat satu entri Edit `Swap Users DD {runId}-037 — Value Setting` dengan Old Value `Alpha, Beta` dan New Value `Beta, Alpha`
151. Tutup Modal Changelog

### TC-GS-UCF-377: Menghapus lalu menambah kembali value dengan label sama menjadi opsi baru dan mengosongkan nilai User

152. Ganti isi kotak search dengan `Readd DD {runId}-037`, tekan Enter
153. Klik `⋯` pada baris `Readd DD {runId}-037`, pilih `Edit`
154. Klik `×` pada badge `Alpha`
155. Verifikasi dialog `Remove Value` dengan bullet `Alpha`
156. Verifikasi body dialog `Used by 1 user(s). Removing it will clear this value from their profile — they'll need to select a new one. This will take effect when you save.`
157. Klik `[Remove]`
158. Ketik `Alpha`, tekan Enter
159. Verifikasi badge baru `Alpha` berada di akhir: `Beta`, `Alpha`
160. Klik `[Save]`
161. Verifikasi toast sukses: "Success, custom field has been updated."
162. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
163. Verifikasi nilai `Readd DD {runId}-037` pada Detail User Rahmat Hidayat kosong
164. Buka Global Settings > User > Custom Field

### TC-GS-UCF-337: Mengganti seluruh value Dropdown dalam satu Save mengosongkan nilai User yang memakai value lama

165. Ketik Search `Swap All DD {runId}-037`, tekan Enter
166. Klik `⋯` pada baris `Swap All DD {runId}-037`, pilih `Edit`
167. Klik `×` pada `Old1`
168. Verifikasi dialog `Remove Value` tampil untuk penghapusan `Old1`
169. Klik `[Remove]`
170. Klik `×` pada `Old2`
171. Verifikasi `Old2` (belum dipakai) langsung hilang tanpa dialog
172. Ketik `New1` di Dropdown Values, tekan Enter, ketik `New2`, tekan Enter
173. Klik `[Save]`
174. Verifikasi toast sukses: "Success, custom field has been updated."
175. Verifikasi Value Setting baris `Swap All DD {runId}-037` menampilkan `New1`, `New2`
176. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
177. Verifikasi nilai `Swap All DD {runId}-037` pada Detail User Rahmat Hidayat kosong
178. Verifikasi `Old1` tidak ada
179. Buka Global Settings > User > Custom Field

### TC-GS-UCF-116: Hapus value yang dipakai user memunculkan konfirmasi dan baru berlaku saat Save

180. Ketik Search `Remove DD {runId}-037`, tekan Enter
181. Klik `⋯` pada baris `Remove DD {runId}-037`, pilih `Edit`
182. Klik `×` pada badge `Mid`
183. Verifikasi dialog `Remove Value` dengan bullet `Mid`
184. Verifikasi body dialog `Used by 2 user(s). Removing it will clear this value from their profile — they'll need to select a new one. This will take effect when you save.`
185. Verifikasi pertanyaan dialog `Are you sure you want to remove it?`
186. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`
187. Klik `[Remove]`
188. Verifikasi badge `Mid` hilang dari form
189. Verifikasi tidak ada toast
190. Periksa daftar request jaringan dan tabel di belakang popup
191. Verifikasi tidak ada request tulis ke server
192. Klik `[Save]`
193. Verifikasi toast sukses: "Success, custom field has been updated."
194. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
195. Verifikasi nilai `Remove DD {runId}-037` pada Detail User Rahmat Hidayat kosong
196. Buka Detail User Intan Permata, section Custom Fields
197. Verifikasi nilai `Remove DD {runId}-037` pada Detail User Intan Permata kosong
198. Buka Global Settings > User > Custom Field

### TC-GS-UCF-119: Hapus value yang belum dipakai tanpa dialog dan berlaku saat Save

199. Ketik Search `Remove DD {runId}-037`, tekan Enter
200. Klik `⋯` pada baris `Remove DD {runId}-037`, pilih `Edit`
201. Klik `×` pada badge `High`
202. Verifikasi tidak ada dialog
203. Verifikasi badge `High` hilang dari form
204. Klik `[Save]`
205. Verifikasi toast sukses: "Success, custom field has been updated."
206. Verifikasi Value Setting baris `Remove DD {runId}-037` menampilkan `Low`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 208 langkah (di atas smell sekitar 35 langkah): seluruhnya satu kelas (fungsional, pengelolaan value Dropdown pada popup Edit), satu akun, dan tiap blok memakai field seed bersuffix sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; pengecualian TC-GS-UCF-111 dan 112 serta TC-GS-UCF-116 dan 119 yang berurutan pada field yang sama sesuai dependensi TC (`Rename DD`, `Remove DD`). Jumlah langkah muncul dari satu baris per aksi, perpindahan ke Detail User dan form `[+ User]`, dan satu `Verifikasi` per klausa Expected.
- Urutan TC: validasi yang diblokir dan perubahan yang dibuang (TC-GS-UCF-114, 115, 113, 366, 117, 118, 120, 336) lebih dulu, lalu aksi yang menyimpan (TC-GS-UCF-111, 112, 370, 376, 377, 337, 116, 119). TC-GS-UCF-114 dan 115 digabung dalam satu pembukaan form `Rename DD` karena keduanya blokir yang tidak mengubah state dan memakai field yang sama. TC-GS-UCF-113 mendahului TC-GS-UCF-111 supaya badge `Red` masih ada; hasilnya sama dengan urutan TC sumber karena TC-GS-UCF-113 tidak menyimpan.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target atau mengganti target; kembali ke tab Custom Field dari Detail User atau form `[+ User]`; menutup form `[+ User]`; membuka dan menutup Modal Changelog; menutup popup lewat `✕` (pada form dirty ditulis `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]`, S-08). `✕` tanpa dialog dilakukan pada form yang bersih (TC-GS-UCF-114/115 setelah error, TC-GS-UCF-113 setelah Edit ulang, TC-GS-UCF-117, TC-GS-UCF-370).
- Pada blok TC-GS-UCF-114 dan 115 form tidak dirty saat `✕` karena perubahan dibatalkan (badge kembali `Blue`) dan badge `RED` tidak ditambahkan.
- Pembagian TC lintas spec: TC-GS-UCF-388 (dialog Remove Value pada form stale), 368 (Save ditolak saat value dihapus admin lain), dan 381 (rename value oleh dua admin) ada di spec 038; Changelog pencatatan rename dan remove value (TC-GS-UCF-276 dan sejenisnya) ada di spec 067.
- Temuan untuk QA:
  - TC-GS-UCF-111, 112, 116, 119 memuat dependensi pada TC sebelumnya (field `Rename DD`, `Remove DD`); spec mengurutkan blok sesuai dependensi pada field seed yang sama dan menyalin langkah (S-04).
  - TC-GS-UCF-116: langkah 4 TC ("Perhatikan jaringan dan tabel di belakang popup") tidak menyebut apa yang diperhatikan pada tabel; spec mengasersi tidak ada request tulis (sesuai Expected b) dan tidak menambah asersi tabel.
  - TC-GS-UCF-111, 112: Expected "Value Setting menampilkan `Red`, `Green`, lalu `+2 more`" bergantung pada lebar kolom; asersi mengikuti teks TC.
  - TC-GS-UCF-117: Expected b menyatakan "form tidak dirty karena perubahan"; diasersi lewat penutupan popup tanpa dialog `Unsaved Changes` (langkah 43 klik `✕`, langkah 44 `Verifikasi`).
  - TC-GS-UCF-366: Expected "form dirty" tidak punya langkah `Verifikasi` tersendiri; diamati lewat dialog `Unsaved Changes` saat `✕` diklik (langkah 33 dan 34).
  - TC-GS-UCF-116: Expected "form dirty" sesudah `[Remove]` tidak diasersi karena TC tidak memberi cara melihat form dirty sebelum `[Save]` (tidak ada penutupan popup di antara `[Remove]` dan `[Save]`).
  - TC-GS-UCF-113, 117, 118, 120, 366, 114, 115: tidak ada Post Condition yang punya langkah observasi di luar Expected.
  - Keputusan NC-04 (value Dropdown kosong atau hanya spasi: `Option name must not be empty`) dan NC-03 (emoji diblok) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan.
