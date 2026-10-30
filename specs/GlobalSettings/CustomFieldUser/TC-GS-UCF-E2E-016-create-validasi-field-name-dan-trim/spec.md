---
id: TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim
title: "Create Custom Field: Validasi Field Name, Trim, Keunikan, Karakter Khusus, dan Data Type Wajib"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-52
  - TC-GS-UCF-53
  - TC-GS-UCF-54
  - TC-GS-UCF-55
  - TC-GS-UCF-442
  - TC-GS-UCF-56
  - TC-GS-UCF-57
  - TC-GS-UCF-443
  - TC-GS-UCF-58
  - TC-GS-UCF-59
  - TC-GS-UCF-541
  - TC-GS-UCF-542
  - TC-GS-UCF-60
coverage:
  web: automated
---

# Create Custom Field: Validasi Field Name, Trim, Keunikan, Karakter Khusus, dan Data Type Wajib

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi, Modified By `Sari D`). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > tab Custom Field, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.preset14` (fixture baru, belum ada; lihat coverage); hanya dibaca, tidak diedit atau dihapus): 14 Custom Field Client A (6 Pre-setup: `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date` [Inactive]; 8 Population D-01: `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`). Hanya `Cost Center` (TC-GS-UCF-56, 443) dan `Joining Date` Inactive (TC-GS-UCF-57) yang dipakai langkah; sisanya dipakai sebagai precondition TC (jumlah 14 field dan keunikan nama), tidak diasersi. Total baris tabel (Pagination) Client A saat spec mulai adalah 14 dan dibaca sebagai baseline TC-GS-UCF-52, 53, dan 56.
- Data Pre-setup Client B: field `Client B Field` (D-85, dibuat Lina Kusuma, tipe Text) ada di Client B; disediakan tim FE/BE sebagai precondition TC-GS-UCF-443; spec ini tidak login ke Client B dan tidak mengubahnya.
- Data dinamis (dibuat lewat UI oleh spec ini; `{runId}` terdiri atas digit):
  - D-07: input `  Pay  Grade {runId}-016  ` (2 spasi depan, 2 spasi internal, 2 spasi belakang); tersimpan `Pay  Grade {runId}-016`.
  - D-180: input = 2 spasi + karakter `T` diulang + ` {runId}-016` + 2 spasi; jumlah `T` disesuaikan sehingga panjang setelah trim tepat 120 termasuk suffix.
  - D-181: `Client B Field` (nama literal, pengecualian S-12 butir (ii): harus sama dengan field Client B untuk menguji keunikan per entitas; dibuat di Client A; hook `before` menghapus lewat API sisa field `Client B Field` di Client A bila ada; hook `after` menghapusnya).
  - D-08: `Nomor Induk (NIP) – Ünit/Tim #1 {runId}-016`.
  - D-243: input tempel `Pay` + LF + `Roll {runId}-016` (tersimpan `PayRoll {runId}-016`); Data Type Dropdown, value tempel `Day` + LF + `Shift`, Placeholder tempel `Type` + LF + `here`.
  - D-244: input tempel `Cost` + TAB + `Code {runId}-016` (tersimpan `CostCode {runId}-016`); Data Type Dropdown, value tempel `Gam` + TAB + `ma`, Placeholder tempel `Hint` + TAB + `text`.
  - Nama yang hanya diketik dan tidak pernah tersimpan: `Grade Level {runId}-016` (TC-GS-UCF-60), 120 dan 121 karakter `A` (TC-GS-UCF-54), 3 spasi (TC-GS-UCF-53), `cost center` dan ` COST CENTER ` (TC-GS-UCF-56), `😊`, `Bonus 😊`, `Red 🔥`, `Hint 🌟` (TC-GS-UCF-59).
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Client A D-07, D-180, D-181, D-08, D-243, D-244 yang bernama memuat `{runId}-016` (D-181: nama literal `Client B Field` di Client A).
- Kemampuan teknis: tempel (paste) dari clipboard termasuk emoji, karakter LF, dan karakter TAB; jeda ±500 ms untuk debounce keunikan; pembacaan teks sel tabel termasuk spasi internal; pembacaan jumlah total baris tabel dari label Pagination (TC-GS-UCF-52, 53, 56; belum terbukti label menampilkan total, lihat Temuan untuk QA); Search pada tabel.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Validasi diblokir (tidak membuat data)

#### TC-GS-UCF-52: Submit dengan Field Name kosong ditolak

1. Catat jumlah total baris tabel Custom Field (dari Pagination) sebagai baseline
2. Klik [+ Custom Field]
3. Pilih Data Type `Text`
4. Klik [Submit]
5. Verifikasi error inline `Field name must not be empty` di bawah Field Name
6. Verifikasi border field Field Name berwarna danger
7. Verifikasi Data Type tetap `Text` (field lain tidak berubah)
8. Verifikasi popup tetap terbuka
9. Verifikasi jumlah total baris tabel Custom Field sama dengan baseline (langkah 1), record tidak dibuat

#### TC-GS-UCF-53: Field Name hanya berisi spasi dianggap kosong

10. Ketik 3 spasi di Field Name
11. Klik [Submit]
12. Verifikasi error inline `Field name must not be empty`
13. Verifikasi popup tetap terbuka
14. Verifikasi tidak ada toast sukses
15. Verifikasi jumlah total baris tabel Custom Field sama dengan baseline (langkah 1), record tidak dibuat

#### TC-GS-UCF-54: Field Name 120 karakter diterima dan 121 karakter menampilkan error

16. Ganti isi Field Name dengan 120 karakter `A`
17. Verifikasi tidak ada error pada Field Name
18. Tambahkan 1 karakter `A` (total 121 karakter)
19. Verifikasi error inline `Max. 120 characters` langsung muncul saat karakter ke-121 diketik (real-time)
20. Klik [Submit]
21. Verifikasi [Submit] diblokir: popup tetap terbuka
22. Verifikasi error tetap tampil
23. Verifikasi tidak ada toast sukses

#### TC-GS-UCF-56: Field Name duplikat ditolak real-time tanpa membedakan huruf besar kecil dan setelah trim

24. Ganti isi Field Name dengan `cost center` (huruf kecil), tunggu ±500 ms
25. Verifikasi error inline `Field name already exists` muncul otomatis setelah jeda ketik tanpa menunggu kursor keluar field
26. Ganti isi Field Name dengan ` COST CENTER ` (spasi tepi)
27. Verifikasi error inline `Field name already exists`
28. Klik [Submit]
29. Verifikasi [Submit] diblokir: popup tetap terbuka
30. Verifikasi tidak ada toast sukses
31. Verifikasi jumlah total baris tabel Custom Field sama dengan baseline (langkah 1), record tidak dibuat

#### TC-GS-UCF-57: Field Name sama dengan field Inactive ditolak

32. Ganti isi Field Name dengan `Joining Date`, tunggu ±500 ms
33. Verifikasi error inline `Field name already exists` (field Inactive ikut dibandingkan)
34. Klik [Submit]
35. Verifikasi error inline `Field name already exists` tetap tampil
36. Verifikasi popup tetap terbuka
37. Verifikasi tidak ada toast sukses

#### TC-GS-UCF-59: Emoji pada Field Name, value Dropdown, dan Placeholder diblok saat keystroke dan paste

38. Klik [Clear Field]
39. Ketik `😊` di Field Name
40. Tempel `Bonus 😊` di Field Name
41. Verifikasi Field Name tidak memuat emoji dan teks non-emoji `Bonus ` tetap masuk
42. Pilih Data Type `Dropdown`
43. Ketik `😊` di Dropdown Values
44. Tempel `Red 🔥` di Dropdown Values
45. Verifikasi Dropdown Values tidak memuat emoji dan teks non-emoji `Red ` tetap masuk
46. Ketik `😊` di Placeholder
47. Tempel `Hint 🌟` di Placeholder
48. Verifikasi Placeholder tidak memuat emoji dan teks non-emoji `Hint ` tetap masuk
49. Verifikasi tidak ada pesan error pada Field Name, Dropdown Values, dan Placeholder

#### TC-GS-UCF-60: Submit tanpa memilih Data Type ditolak

50. Klik [Clear Field]
51. Isi Field Name `Grade Level {runId}-016`
52. Klik [Submit] dengan Data Type belum dipilih
53. Verifikasi error inline `Data type must not be empty`
54. Verifikasi popup tetap terbuka
55. Verifikasi tidak ada toast sukses

### Create berhasil (membuat data)

56. Klik [Clear Field]
57. Centang checkbox `Stay on this form after submitting` agar beberapa Create terjadi dalam satu sesi popup

#### TC-GS-UCF-55: Spasi di tepi Field Name tidak dihitung dan disimpan ter-trim; spasi di tengah dipertahankan

58. Ketik `  Pay  Grade {runId}-016  ` di Field Name (D-07)
59. Verifikasi tidak ada error pada Field Name
60. Verifikasi nilai di field Field Name sama dengan yang diketik (tidak berubah saat mengetik)
61. Pilih Data Type `Text`
62. Klik [Submit]
63. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-442: Field Name 120 karakter dengan spasi di tepi diterima dan disimpan ter-trim

64. Ketik input D-180 di Field Name (2 spasi, `T` diulang + ` {runId}-016` sehingga 120 karakter setelah trim, 2 spasi)
65. Verifikasi tidak ada error `Max. 120 characters`
66. Pilih Data Type `Text`
67. Klik [Submit]
68. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-443: Field Name yang sama dengan field milik client lain diterima

69. Ketik `Cost Center` di Field Name, tunggu ±500 ms
70. Verifikasi error inline `Field name already exists`
71. Ganti isi Field Name dengan `Client B Field`, tunggu ±500 ms
72. Verifikasi tidak ada error (keunikan hanya dalam satu entitas)
73. Pilih Data Type `Text`
74. Klik [Submit]
75. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-58: Field Name menerima huruf beraksen, non-Latin, dan tanda baca

76. Isi Field Name `Nomor Induk (NIP) – Ünit/Tim #1 {runId}-016` (D-08)
77. Verifikasi tidak ada error karakter
78. Pilih Data Type `Text`
79. Klik [Submit]
80. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-541: Newline yang di-paste ke Field Name, Dropdown Values, dan Placeholder dibuang diam-diam

81. Tempel `Pay` + LF + `Roll {runId}-016` ke input Field Name (D-243)
82. Verifikasi Field Name berisi `PayRoll {runId}-016` (LF dibuang)
83. Verifikasi tidak ada pesan error pada Field Name
84. Pilih Data Type `Dropdown`
85. Tempel `Day` + LF + `Shift` ke input Dropdown Values, tekan Enter
86. Verifikasi Dropdown Values memuat satu badge `DayShift`
87. Verifikasi tidak ada pesan error pada Dropdown Values
88. Tempel `Type` + LF + `here` ke input Placeholder
89. Verifikasi Placeholder berisi `Typehere`
90. Verifikasi tidak ada pesan error pada Placeholder
91. Klik [Submit]
92. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-542: Karakter tab yang di-paste ke Field Name, Dropdown Values, dan Placeholder dibuang diam-diam

93. Tempel `Cost` + TAB + `Code {runId}-016` ke input Field Name (D-244)
94. Verifikasi Field Name berisi `CostCode {runId}-016` (TAB dibuang)
95. Verifikasi tidak ada pesan error pada Field Name
96. Pilih Data Type `Dropdown`
97. Tempel `Gam` + TAB + `ma` ke input Dropdown Values, tekan Enter
98. Verifikasi Dropdown Values memuat satu badge `Gamma`
99. Verifikasi tidak ada pesan error pada Dropdown Values
100. Tempel `Hint` + TAB + `text` ke input Placeholder
101. Verifikasi Placeholder berisi `Hinttext`
102. Verifikasi tidak ada pesan error pada Placeholder
103. Klik [Submit]
104. Verifikasi toast sukses: "Success, custom field has been created."

### Verifikasi tabel setelah popup ditutup

105. Klik `[✕]`
106. Ketik Search `Pay  Grade {runId}-016`, tekan Enter
107. Verifikasi tabel menampilkan `Pay  Grade {runId}-016` (spasi tepi dibuang, spasi ganda di tengah tidak digabung) (TC-GS-UCF-55)
108. Ganti isi kotak search dengan 10 karakter `T`, tekan Enter
109. Verifikasi baris tampil dengan Field Name 120 karakter (D-180) tanpa spasi tepi (TC-GS-UCF-442)
110. Ganti isi kotak search dengan `Client B Field`, tekan Enter
111. Verifikasi baris `Client B Field` tampil di tabel Client A (TC-GS-UCF-443)
112. Ganti isi kotak search dengan `Nomor Induk`, tekan Enter
113. Verifikasi baris tampil dengan nama persis `Nomor Induk (NIP) – Ünit/Tim #1 {runId}-016` (TC-GS-UCF-58)
114. Ganti isi kotak search dengan `PayRoll {runId}-016`, tekan Enter
115. Verifikasi Data Type baris `PayRoll {runId}-016` adalah `Dropdown` (TC-GS-UCF-541)
116. Verifikasi Value Setting baris `PayRoll {runId}-016` menampilkan badge `DayShift`
117. Verifikasi Placeholder baris `PayRoll {runId}-016` adalah `Typehere`
118. Ganti isi kotak search dengan `CostCode {runId}-016`, tekan Enter
119. Verifikasi Data Type baris `CostCode {runId}-016` adalah `Dropdown` (TC-GS-UCF-542)
120. Verifikasi Value Setting baris `CostCode {runId}-016` menampilkan badge `Gamma`
121. Verifikasi Placeholder baris `CostCode {runId}-016` adalah `Hinttext`
122. Ganti isi kotak search dengan `Grade Level {runId}-016`, tekan Enter
123. Verifikasi empty state `No results found` tampil (record `Grade Level {runId}-016` tidak dibuat) (TC-GS-UCF-60)
124. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 52, 53, 54, 56, 57, 59, 60 (validasi diblokir, tidak membuat data), lalu 55, 442, 443, 58, 541, 542 (Create berhasil), sesuai bagian 3 prinsip 3 dan 7 konvensi; urutan sumber (52 sampai 60, 442, 443, 541, 542) berubah demi satu sesi popup. Semua kasus memakai satu pembukaan popup dengan [Clear Field] di antara kasus (halaman yang sama dipakai berulang, prinsip 13). TC yang tidak membuat form bersih menyambung dari state sebelumnya dengan [Clear Field], dan satu-satunya kejadian menutup form adalah langkah 105 (form bersih setelah Stay mereset isian).
- Asersi "record tidak dibuat" untuk TC-GS-UCF-52, 53, dan 56 tidak dapat dicari lewat nama (nama kosong, 3 spasi, atau nama yang sudah ada); diasersi lewat surface agregat (bagian 8b butir 2): langkah 1 mencatat jumlah total baris tabel (Pagination) sebagai baseline, lalu satu `Verifikasi` jumlah sama dengan baseline sesudah tiap TC (langkah 9, 15, dan 31). Satu baseline dipakai tiga TC karena TC-GS-UCF-52, 53, 54, dan 56 tidak membuat data sebelum langkah itu. `Verifikasi` popup tetap terbuka dan tanpa toast sukses pada TC itu dipertahankan sebagai asersi Expected TC (tidak dicatat sebagai pengganti). Langkah 1 adalah langkah penghubung (pencatatan baseline mengikuti langkah 1 TC-GS-UCF-52, 53, dan 56). TC-GS-UCF-54 tidak memuat klausa "record tidak dibuat". Untuk TC-GS-UCF-60 asersi absence di tabel memakai Search nama unik dengan empty state `No results found` sebagai anchor (langkah 122 sampai 123). TC-GS-UCF-57 hanya menguji penolakan; nama `Joining Date` sudah ada sebagai Pre-setup sehingga absence record baru tidak diasersi terpisah selain toast sukses yang tidak muncul. TC-GS-UCF-56 dan 57 hanya menguji penolakan; nama `cost center` dan `Joining Date` sudah ada sebagai Pre-setup sehingga absence record baru tidak diasersi terpisah selain toast sukses yang tidak muncul.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3, 10, 16, 18, 24, 26, 32, 34, 38 sampai 40, 42 sampai 44, 46 sampai 47, 50 sampai 52, 56 sampai 58, 61 sampai 62, 64, 66 sampai 67, 69, 71, 73 sampai 74, 76, 78 sampai 79, 81, 84 sampai 85, 88, 91, 93, 96 sampai 97, 100, 103 (aksi yang dimaksud TC), langkah 105 (menutup popup agar tabel terlihat), langkah 106, 108, 110, 112, 114, 118, 122 (Search agar baris target tampil), dan langkah 124 (mereset Search). Langkah 57 (centang Stay) mengatur mode sesi popup, bukan asersi TC.
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 13 TC satu topik (validasi dan penyimpanan Field Name) dengan satu akun, satu dataset, dan satu pembukaan popup; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01). Blok Create berhasil tetap bermakna bila blok validasi gagal karena tiap Create memakai nama sendiri; kegagalan keras (popup tidak terbuka) menghentikan keduanya.
- Nama D-07, D-180, D-08, D-243, dan D-244 bersuffix `{runId}-016` (S-12); panjang 120 karakter TC-GS-UCF-442 sudah termasuk suffix sehingga batas yang diuji tidak berubah. Nama `Client B Field` (D-181) literal karena objek ujinya adalah kesamaan dengan field Client B; hook `before` menghapus sisa field itu di Client A dan hook `after` menghapus yang dibuat spec ini.
- Temuan untuk QA:
  - TC-GS-UCF-52, 53, dan 56 meminta jumlah total baris dicatat dan diperiksa dari Pagination; belum terbukti label Pagination menampilkan jumlah total, dan TC tidak menyebut apakah Pagination terbaca saat popup Create terbuka (spec membaca total saat popup terbuka mengikuti urutan langkah TC). Bila tidak terbaca, asersi "record tidak dibuat" perlu cara amati lain dari QA.
  - Plan menyebut 14 field Pre-setup, sedangkan tabel Pre-setup TC memuat 6 field; 8 sisanya berasal dari Population TC-GS-UCF-1 (D-01). Spec ini men-seed keempat belas lewat API (bukan menumpang hasil spec lain).
  - TC-GS-UCF-443 bergantung pada field `Client B Field` di Client B (D-85, "Disiapkan sebelum TC pemakai"); mekanisme penyiapannya tidak ditulis di TC (disediakan tim FE/BE).
  - Teks empty state `No results found` pada hasil Search tanpa hasil tidak ditulis di TC ini; mengikuti konvensi bagian 8b butir 2.
