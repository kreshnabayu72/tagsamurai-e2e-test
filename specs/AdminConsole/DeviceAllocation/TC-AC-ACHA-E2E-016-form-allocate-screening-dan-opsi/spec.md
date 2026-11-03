---
id: TC-AC-ACHA-E2E-016-form-allocate-screening-dan-opsi
title: "Form Allocate Device: Screening per Entitas, Footer, Opsi Category dan Type, Dropdown Client, Pay From, dan Price Catalog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-89
  - TC-AC-ACHA-90
  - TC-AC-ACHA-91
  - TC-AC-ACHA-92
  - TC-AC-ACHA-93
  - TC-AC-ACHA-94
  - TC-AC-ACHA-100
  - TC-AC-ACHA-114
  - TC-AC-ACHA-115
  - TC-AC-ACHA-116
  - TC-AC-ACHA-117
  - TC-AC-ACHA-118
  - TC-AC-ACHA-119
  - TC-AC-ACHA-120
  - TC-AC-ACHA-421
coverage:
  web: automated
---

# Form Allocate Device: Screening per Entitas, Footer, Opsi Category dan Type, Dropdown Client, Pay From, dan Price Catalog

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (urutan pemakaian dalam spec):

| Kode | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| A-01 | Total Control Principal `PT ABC` (Admin Pratama) | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| A-02 | Total Control Distributor `PT Global Distribusi` (Hendra Wibowo) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| A-03 | Total Control Partner `CV Mitra Solusi` (Maya Putri) | #43 | `totalControlPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P1_PASSWORD` |
| A-04 | Total Control Partner `CV Karya Mandiri` | #46 | `totalControlPartner2_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P2_PASSWORD` |

- Login A-01 di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (A-01, `AC_TC_PASSWORD`). Ganti akun A-02, A-03, A-04 di tengah spec memakai langkah logout dan login eksplisit.
- Password tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script.
- Data Pre-setup: entitas #2 sampai #5; Client #7 (`PT Sejahtera Logistik`, Active), #10 (`PT Manufaktur Unggul`), #12 (`PT Agro Lestari`, Suspended), #13 (`Toko Lama Abadi`, Archived); Seed 30 alokasi #48 (dipakai sebagai precondition TC-116 dan TC-117, tidak diasersi); kantong #16, #18 (saldo $1,000.00), #19 (saldo $3,000.00); harga produk #14 dan #15; kategori #64. Tidak ada data yang dibuat spec ini (semua submit tidak dilakukan).
- Kondisi data TC-120: tidak ada transaksi alokasi dalam scope `CV Karya Mandiri`, disediakan lewat fixture API yang disediakan tim FE/BE di hook `before`, termasuk menyingkirkan transaksi seed Pre-setup #50 dan #70 milik MB_P2 dari scope `CV Karya Mandiri` lalu memulihkannya di hook `after` (mekanismenya tidak tertulis di TC, lihat Temuan untuk QA).
- Pilihan Category tanpa Type (TC-114), diulang pada langkah "Untuk setiap baris tabel":

| Category (label opsi) |
|---|
| `TAG - NFC` |
| `TAG - BLE` |
| `TAG - GPS` |
| `Hardware - Smart Fixed Reader` |
| `Hardware - BLE Gateway` |

- Kemampuan teknis: dismiss klik backdrop dan tekan Esc pada modal; fixture API Pre-setup #20 (penyetel penempatan group, saldo, kantong, harga) disediakan tim FE/BE.
- Hook suite (dinyatakan sekali di `suite.md`): flag Guided Tooltip halaman Device Allocation disetel true untuk akun aktor dan dipulihkan di `after`, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global. Kondisi data TC-120 dan penyetel fixture dipulihkan fixture Pre-setup #20 di hook `after` bersama seed 30 baris (Lampiran A butir A-11); tidak ada transaksi yang dibuat spec ini.

## Test Steps

### Akun A-01 Principal: TC-AC-ACHA-89 Screening form dan TC-AC-ACHA-93 Footer dan penutupan

1. Klik `[+ Allocation]`
2. Amati form dari atas ke bawah tanpa mengisi apa pun
3. Verifikasi Header: judul `Allocate Device`
4. Verifikasi Header: ikon close `[×]` di kanan atas
5. Verifikasi Body: From berupa label read-only `PT ABC (Principal)`
6. Verifikasi Body: field Category * berupa dropdown flat dengan placeholder "Select category"
7. Verifikasi Body: helper Category "Quota allocation is based on device category. Options come from the first-level nodes of Settings > Device > Category, a different source from the Category filter in the List."
8. Verifikasi Body: Type tidak tampil sebelum Category RFID atau Handheld Reader dipilih
9. Verifikasi Body: field Client * berupa searchable dropdown dengan placeholder "Select client recipient"
10. Verifikasi Body: field Quantity * berupa input angka dengan placeholder "Enter quantity"
11. Verifikasi Body: helper Quantity "Enter the number of units to allocate (>= 1)."
12. Verifikasi Body: Pay From tidak dirender
13. Verifikasi Body: field Notes berupa textarea dengan placeholder "Enter notes"
14. Verifikasi Body: Preview (Estimated Cost, Your Pocket Balance) tidak dirender
15. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" rata kanan tepat di atas tombol
16. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" default tidak tercentang
17. Verifikasi Footer baris 2: `[Clear Field]` (text, primary)
18. Verifikasi Footer baris 2: `[Submit]` (filled, success)
19. Verifikasi Footer: tidak ada tombol `[Cancel]`
20. Verifikasi footer hanya berisi dua tombol aksi `[Clear Field]` dan `[Submit]` ditambah checkbox "Stay on this form after submitting"
21. Verifikasi tombol `[Cancel]` tidak ada
22. Klik area backdrop di luar form
23. Verifikasi form tidak tertutup oleh klik backdrop
24. Klik `[×]`
25. Verifikasi form tertutup lewat `[×]`
26. Klik `[+ Allocation]`
27. Tekan Esc
28. Verifikasi form tertutup lewat Esc
29. Klik `[+ Allocation]`

### TC-AC-ACHA-94 Dropdown Category tujuh node first-level

30. Buka dropdown Category
31. Verifikasi dropdown flat tanpa group header dengan tujuh opsi berlabel pola "[Device Type] - [Category]" berurutan: `TAG - RFID` | `TAG - NFC` | `TAG - BLE` | `TAG - GPS` | `Hardware - Handheld Reader` | `Hardware - Smart Fixed Reader` | `Hardware - BLE Gateway`
32. Verifikasi nilai awal field Category kosong dengan placeholder "Select category"
33. Pilih opsi `TAG - NFC`
34. Verifikasi field Category menampilkan label opsi `TAG - NFC`

### TC-AC-ACHA-100 Type wajib dengan default terpilih pada RFID dan Handheld Reader

35. Pilih Category `TAG - RFID`
36. Verifikasi radio Type memunculkan `Object TAG` dan `User TAG`
37. Verifikasi `Object TAG` terpilih
38. Ubah Category menjadi `Hardware - Handheld Reader`
39. Verifikasi radio Type memunculkan `Long Range` dan `Short Range`
40. Verifikasi `Long Range` terpilih
41. Verifikasi radio Type tidak punya state kosong: selalu ada satu opsi terpilih

### TC-AC-ACHA-114 Type disembunyikan untuk lima Category tanpa Type

42. Untuk setiap baris tabel "Pilihan Category tanpa Type" lakukan langkah 43 sampai 44
43. Pilih Category pada baris itu lalu amati area Type
44. Verifikasi kontainer pilihan Type disembunyikan

### TC-AC-ACHA-115 Default Type kembali saat Category berganti

45. Pilih Category `TAG - RFID`, lalu pilih Type `User TAG`
46. Ubah Category menjadi `Hardware - Handheld Reader`
47. Verifikasi radio Type berganti menjadi `Long Range` dan `Short Range`
48. Pilih Type `Short Range`
49. Ubah Category menjadi `TAG - RFID` lagi
50. Verifikasi radio Type kembali `Object TAG` dan `User TAG`
51. Verifikasi `Object TAG` terpilih sebagai default

### TC-AC-ACHA-117 Dropdown Client searchable

52. Buka dropdown Client, ketik `sejah` (huruf kecil) pada kotak pencarian dropdown
53. Verifikasi hasil pencarian hanya `PT Sejahtera Logistik` (substring, tidak case-sensitive)
54. Pilih opsi `PT Sejahtera Logistik`
55. Verifikasi field Client berisi `PT Sejahtera Logistik`
56. Klik `[×]`
57. Verifikasi dialog Unsaved Changes tampil
58. Klik `[Leave]`

### Akun A-02 Distributor: TC-AC-ACHA-90 Screening, TC-AC-ACHA-116 Dropdown Client, TC-AC-ACHA-421 Push-only, TC-AC-ACHA-119 Price Catalog

59. Logout, lalu login sebagai A-02 (`PT Global Distribusi`), buka Allocation > Device Allocation
60. Klik `[+ Allocation]`
61. Amati form dari atas ke bawah tanpa mengisi apa pun
62. Verifikasi Header: judul `Allocate Device`
63. Verifikasi Header: ikon close `[×]` di kanan atas
64. Verifikasi Body: From berupa label read-only `PT Global Distribusi (Distributor)`
65. Verifikasi Body: field Category * berupa dropdown flat dengan placeholder "Select category"
66. Verifikasi Body: helper Category "Quota allocation is based on device category. Options come from the first-level nodes of Settings > Device > Category, a different source from the Category filter in the List."
67. Verifikasi Body: Type tidak tampil sebelum Category RFID atau Handheld Reader dipilih
68. Verifikasi Body: field Client * berupa searchable dropdown dengan placeholder "Select client recipient"
69. Verifikasi Body: field Quantity * berupa input angka dengan placeholder "Enter quantity"
70. Verifikasi Body: helper Quantity "Enter the number of units to allocate (>= 1)."
71. Verifikasi Body: Pay From * pre-filled `PT ABC (Principal)`
72. Verifikasi Body: Pay From * disabled
73. Verifikasi Body: tombol `[View Price Catalog]` tampil di samping Pay From
74. Verifikasi Body: field Notes berupa textarea dengan placeholder "Enter notes"
75. Verifikasi Body: Preview (Estimated Cost, Your Pocket Balance) belum dirender sampai Category, Pay From, harga, dan Quantity valid terisi
76. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" rata kanan tepat di atas tombol
77. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" default tidak tercentang
78. Verifikasi Footer baris 2: `[Clear Field]` (text, primary)
79. Verifikasi Footer baris 2: `[Submit]` (filled, success)
80. Verifikasi Footer: tidak ada tombol `[Cancel]`
81. Buka dropdown Client dan amati opsi
82. Verifikasi opsi dropdown Client hanya `PT Sejahtera Logistik` (Client Active dalam scope)
83. Verifikasi `PT Agro Lestari` (Suspended) dan `Toko Lama Abadi` (Archived) tidak muncul sebagai opsi
84. Verifikasi `PT Agro Lestari` dan `Toko Lama Abadi` tidak tampil sebagai opsi disabled
85. Ketik `Agro` pada kotak pencarian dropdown
86. Verifikasi `PT Agro Lestari` tidak muncul pada hasil pencarian
87. Ganti isi kotak pencarian dropdown dengan `Lama`
88. Verifikasi `Toko Lama Abadi` tidak muncul pada hasil pencarian
89. Ganti isi kotak pencarian dropdown dengan `Sejahtera`, lalu pilih opsi `PT Sejahtera Logistik`
90. Verifikasi form hanya memuat penerima berupa Client (field `Client *`)
91. Verifikasi tidak ada pilihan Recipient Type, Source Type, atau entitas Distributor/Partner sebagai penerima
92. Isi Quantity `5`
93. Klik `[View Price Catalog]`
94. Verifikasi modal Price Catalog (milik modul Wallet) terbuka
95. Verifikasi modal Price Catalog read-only tanpa aksi transaksional
96. Tutup modal Price Catalog
97. Verifikasi form Allocate Device tetap terbuka
98. Verifikasi Quantity `5` tetap terisi
99. Klik `[×]`
100. Verifikasi dialog Unsaved Changes tampil
101. Klik `[Leave]`
102. Amati Table Tools pada List
103. Verifikasi Table Tools tampil beserta `[+ Allocation]`
104. Verifikasi Table Tools tidak memuat aksi `Request Allocation` atau aksi tarik (pull) apa pun, alokasi hanya satu arah dari pengirim ke Client

### Akun A-03 Partner satu kantong: TC-AC-ACHA-91 Screening

105. Logout, lalu login sebagai A-03 (`CV Mitra Solusi`), buka Allocation > Device Allocation
106. Klik `[+ Allocation]`
107. Amati form dari atas ke bawah tanpa mengisi apa pun
108. Verifikasi Header: judul `Allocate Device`
109. Verifikasi Header: ikon close `[×]` di kanan atas
110. Verifikasi Body: From berupa label read-only `CV Mitra Solusi (Partner)`
111. Verifikasi Body: field Category * berupa dropdown flat dengan placeholder "Select category"
112. Verifikasi Body: helper Category "Quota allocation is based on device category. Options come from the first-level nodes of Settings > Device > Category, a different source from the Category filter in the List."
113. Verifikasi Body: Type tidak tampil sebelum Category RFID atau Handheld Reader dipilih
114. Verifikasi Body: field Client * berupa searchable dropdown dengan placeholder "Select client recipient"
115. Verifikasi Body: field Quantity * berupa input angka dengan placeholder "Enter quantity"
116. Verifikasi Body: helper Quantity "Enter the number of units to allocate (>= 1)."
117. Verifikasi Body: Pay From * pre-filled `PT Global Distribusi (Distributor)` (satu kantong sumber)
118. Verifikasi Body: Pay From * disabled
119. Verifikasi Body: tombol `[View Price Catalog]` tampil di samping Pay From
120. Verifikasi Body: field Notes berupa textarea dengan placeholder "Enter notes"
121. Verifikasi Body: Preview (Estimated Cost, Your Pocket Balance) belum dirender sampai Category, Pay From, harga, dan Quantity valid terisi
122. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" rata kanan tepat di atas tombol
123. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" default tidak tercentang
124. Verifikasi Footer baris 2: `[Clear Field]` (text, primary)
125. Verifikasi Footer baris 2: `[Submit]` (filled, success)
126. Verifikasi Footer: tidak ada tombol `[Cancel]`
127. Klik `[×]` untuk menutup form (form bersih, tanpa dialog)

### Akun A-04 Partner dua kantong: TC-AC-ACHA-120 Sumber opsi Category, TC-AC-ACHA-92 Screening, TC-AC-ACHA-118 Preview per kantong

128. Logout, lalu login sebagai A-04 (`CV Karya Mandiri`), buka Allocation > Device Allocation
129. Buka Filter Panel List, lalu buka dropdown filter Category
130. Verifikasi dropdown filter Category tidak memuat opsi apa pun dan menampilkan "No options available" (opsi filter berasal dari data tabel saat ini)
131. Tutup Filter Panel
132. Klik `[+ Allocation]`
133. Amati form dari atas ke bawah tanpa mengisi apa pun
134. Verifikasi Header: judul `Allocate Device`
135. Verifikasi Header: ikon close `[×]` di kanan atas
136. Verifikasi Body: From berupa label read-only `CV Karya Mandiri (Partner)`
137. Verifikasi Body: field Category * berupa dropdown flat dengan placeholder "Select category"
138. Verifikasi Body: helper Category "Quota allocation is based on device category. Options come from the first-level nodes of Settings > Device > Category, a different source from the Category filter in the List."
139. Verifikasi Body: Type tidak tampil sebelum Category RFID atau Handheld Reader dipilih
140. Verifikasi Body: field Client * berupa searchable dropdown dengan placeholder "Select client recipient"
141. Verifikasi Body: field Quantity * berupa input angka dengan placeholder "Enter quantity"
142. Verifikasi Body: helper Quantity "Enter the number of units to allocate (>= 1)."
143. Verifikasi Body: Pay From * berupa dropdown wajib dipilih dengan placeholder "Select source pocket"
144. Verifikasi Body: tombol `[View Price Catalog]` tampil di samping Pay From
145. Verifikasi Body: field Notes berupa textarea dengan placeholder "Enter notes"
146. Verifikasi Body: Preview (Estimated Cost, Your Pocket Balance) belum dirender sampai Pay From dipilih dan Category serta Quantity valid terisi
147. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" rata kanan tepat di atas tombol
148. Verifikasi Footer baris 1: checkbox "Stay on this form after submitting" default tidak tercentang
149. Verifikasi Footer baris 2: `[Clear Field]` (text, primary)
150. Verifikasi Footer baris 2: `[Submit]` (filled, success)
151. Verifikasi Footer: tidak ada tombol `[Cancel]`
152. Buka dropdown Category pada form
153. Verifikasi dropdown Category pada form memuat ketujuh node first-level (`TAG - RFID` | `TAG - NFC` | `TAG - BLE` | `TAG - GPS` | `Hardware - Handheld Reader` | `Hardware - Smart Fixed Reader` | `Hardware - BLE Gateway`) karena bersumber dari master data penuh
154. Pilih Category `TAG - NFC`, Client `PT Cipta Kreasi`, isi Quantity `10`
155. Pilih Pay From `PT Global Distribusi (Distributor)`
156. Verifikasi Preview: Estimated Cost `$15.00 (10 × $1.50/unit)`
157. Verifikasi Preview: Your Pocket Balance `$1,000.00`
158. Verifikasi field Pay From menampilkan label opsi terpilih `PT Global Distribusi (Distributor)` beserta tipe sumber
159. Ganti Pay From menjadi `PT ABC (Principal)`
160. Verifikasi Preview: Estimated Cost `$12.00 (10 × $1.20/unit)`
161. Verifikasi Preview: Your Pocket Balance `$3,000.00`
162. Klik `[×]`
163. Verifikasi dialog Unsaved Changes tampil
164. Klik `[Leave]`

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular. Semua TC di spec ini tidak melakukan Submit; tidak ada transaksi, saldo, atau kuota yang berubah.
- Alasan spec di atas sekitar 35 langkah: seluruh blok satu topik (screening dan opsi form Allocate Device), tidak ada kelas harness lain, dan tiap blok akun (A-01 sampai A-04) berdiri sendiri dengan langkah ganti akun eksplisit sehingga blok sesudahnya tetap bermakna walau blok sebelumnya gagal (konvensi bagian 3, pemisah (b)). Jumlah langkah terutama berasal dari S-01 yang menuntut satu `Verifikasi` per klausa Expected pada empat screening form.
- Penyimpangan urutan (S-10): TC-93 dijalankan tepat sesudah screening TC-89 pada form yang sama; klik backdrop didahulukan supaya form tidak tertutup sebelum langkah `[×]` dan Esc, dan form dibuka lagi sesudah tiap penutupan. Form dirty pada akhir blok A-01 dan A-02 ditutup lewat `[×]`, dialog Unsaved Changes, `[Leave]` (S-08).
- Langkah penghubung (S-03): pembukaan ulang form, tutup Filter Panel, tutup modal Price Catalog, penutupan form dirty (`[×]`, dialog Unsaved Changes, `[Leave]`), logout dan login ganti akun, serta pilihan Client `PT Sejahtera Logistik` sebagai prasyarat penutupan.
- TC-114 diulang per baris tabel "Pilihan Category tanpa Type" (langkah 43 sampai 44); parameter tiap iterasi ada di tabel Prerequisites.
- TC-421 dibelah antar permukaan: bagian form (butir a) diasersi di form yang terbuka bersama TC-116 dan TC-119, bagian Table Tools (butir b) diasersi sesudah form ditutup, dengan Table Tools dan `[+ Allocation]` yang tampil sebagai anchor positif sebelum asersi absence.
- TC-117: pembanding asersi "hanya" adalah opsi `PT Sejahtera Logistik` yang tampil pada hasil pencarian itu sendiri. TC-116: opsi `PT Sejahtera Logistik` pada daftar awal menjadi anchor absence untuk Client Suspended dan Archived.
- Pengecualian S-12 nama literal: nama entitas dan Client Pre-setup (`PT Sejahtera Logistik`, `PT Cipta Kreasi`, dan seterusnya) literal karena sudah ada di environment automation; tidak ada data dinamis yang dibuat spec ini.
- Temuan untuk QA:
  - TC-100 Expected c ("pesan Type wajib tidak dapat dipicu lewat UI") bukan observasi UI terpisah; spec mengasersinya sebagai "radio Type tidak punya state kosong" yang sudah tampak dari butir a dan b.
  - TC-116 menyebut seed #48 di Precondition tetapi Expected hanya membahas opsi Client; seed tidak diasersi.
  - TC-119 tidak menyebut cara menutup modal Price Catalog (milik modul Wallet); spec menulis "Tutup modal Price Catalog".
  - TC-120 Precondition ("belum ada transaksi dalam scope CV Karya Mandiri") bergantung pada fixture Pre-setup #20 yang tidak mendefinisikan penghapusan atau penyaringan transaksi; transaksi dari TC lain (mis. TC-139) menyebabkan scope tidak kosong pada run berikutnya. Mekanisme pemulihan disediakan tim FE/BE.
  - TC-118 mensyaratkan saldo kantong A $1,000.00 dan B $3,000.00; saldo itu dapat berubah karena TC-139 (spec lain) dan perlu dipulihkan fixture sebelum spec ini.
  - TC-421 Expected a tidak merinci cara memastikan opsi dropdown Client tidak memuat entitas Distributor/Partner; spec mengasersi lewat struktur form (hanya field `Client *`) dan opsi yang sudah diperiksa pada TC-116.
