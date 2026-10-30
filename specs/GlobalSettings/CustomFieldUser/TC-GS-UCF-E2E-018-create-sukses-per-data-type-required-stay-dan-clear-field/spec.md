---
id: TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field
title: "Create Custom Field Berhasil: Population, Per Data Type, Required, Stay on Form, Clear Field, dan Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-1
  - TC-GS-UCF-69
  - TC-GS-UCF-70
  - TC-GS-UCF-71
  - TC-GS-UCF-72
  - TC-GS-UCF-73
  - TC-GS-UCF-74
  - TC-GS-UCF-450
  - TC-GS-UCF-451
  - TC-GS-UCF-75
coverage:
  web: automated
---

# Create Custom Field Berhasil: Population, Per Data Type, Required, Stay on Form, Clear Field, dan Modified By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi, Modified By `Sari D`). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun tambahan (ganti akun eksplisit di langkah, dipakai TC-GS-UCF-450 dan 451): Total Control Client A nama satu kata `totalControlMono_automated_qaTeam1@qwertysystem.net` (Bagas) dengan `Spectra.env.GS_MONO_TC_PASSWORD`, dan Total Control Client A nama depan panjang `totalControlLongName_automated_qaTeam1@qwertysystem.net` (Buzzlightyear Sumardi) dengan `Spectra.env.GS_LONGNAME_TC_PASSWORD`. Kedua nama environment variable adalah nama baru (env baru; belum terdaftar di `spectra.config.ts` dan `.env.example`, tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`); nama mengikuti pola `<APP>_<ROLE>_PASSWORD` (konvensi bagian 5), dan kedua email tidak memiliki env var terdaftar lain. Nama env var password kedua akun tidak ada di TC (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun aktor utama.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > tab Custom Field, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.preset14` (fixture baru, belum ada; lihat coverage); hanya dibaca): 6 Custom Field Client A: `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date` [Inactive]. Keenam field dipakai sebagai precondition TC-GS-UCF-1, tidak diasersi satu per satu (hanya total 14 field yang diasersi). Populasi Client A sebelum TC-GS-UCF-1 tepat 6 field ini; hook `before` menghapus lewat API sisa field Population (D-01) bernama sama yang ada dari run lain, hook `before` suite menghapus field sisa lain (lihat `suite.md`, butir Field sisa Client A), dan field milik spec lain dibersihkan oleh hook `after` spec masing-masing (suite serial).
- Data Population TC-GS-UCF-1 (D-01), dibuat lewat UI; nama literal karena TC-GS-UCF-1 mendefinisikannya dan spec lain membaca nama ini (pengecualian S-12 butir (i)); hook `after` menghapus lewat API delapan field ini:

  | No | Field Name | Data Type | Isian lain |
  |---|---|---|---|
  | 1 | Blood Type | Dropdown | value `A`, `B`, `AB`, `O` |
  | 2 | Shirt Size | Dropdown | value `S`, `M`, `L`, `XL`; Placeholder `Choose shirt size` |
  | 3 | Emergency Phone | Phone | - |
  | 4 | Birth Date | Date | - |
  | 5 | Tax ID | Text | Placeholder `Enter tax ID number`; Required Field Yes |
  | 6 | Work Notes | Text Area | - |
  | 7 | Annual Target | Numeric | Decimal Places `1` |
  | 8 | badge number | Text | - |

- Data dinamis lain (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-018`):
  - D-10 sampai D-13 (parameter langkah 37 sampai 41; Placeholder dan Required dibiarkan default):

    | No | Field Name | Data Type |
    |---|---|---|
    | D-10 | Vehicle Plate {runId}-018 | Text |
    | D-11 | Remarks {runId}-018 | Text Area |
    | D-12 | Hire Date {runId}-018 | Date |
    | D-13 | Mobile Backup {runId}-018 | Phone |

  - D-14: `Work Location {runId}-018` (Dropdown `HQ`, `Branch`; Placeholder `Choose work location`; Required Yes).
  - D-15: `Overtime Hours {runId}-018` (Numeric, Decimal Places 2).
  - D-16 dan D-17: `Optional One {runId}-018` (Text, Required No) dan `Mandatory One {runId}-018` (Text, Required Yes).
  - D-18: `One Shot {runId}-018` (Text). D-19: `Stay A {runId}-018` (Numeric, Decimal Places 2, Required Yes, Placeholder `Enter value`).
  - D-187: `Single Name Probe {runId}-018` (Text, dibuat Bagas). D-188: `Long Name Probe {runId}-018` (Text, dibuat Buzzlightyear Sumardi).
  - Nilai yang hanya diketik dan tidak pernah tersimpan: `Temp`, value `One`, Placeholder `abc` (TC-GS-UCF-75).
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API delapan field Population dan semua field Client A yang namanya memuat `{runId}-018`.
- Kemampuan teknis: ganti akun login di tengah spec (TC-GS-UCF-450 dan 451); pembacaan teks sel tabel, hover tooltip sel Modified By, posisi baris, jumlah baris per halaman (10) dan pindah halaman; waktu hari uji untuk Last Updated (toleransi satu menit; jam server dan jam browser sinkron); Search pada tabel.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-1: Create 8 Custom Field berurutan dengan Stay on this form dicentang (Population)

1. Klik [+ Custom Field]
2. Centang checkbox `Stay on this form after submitting`
3. Untuk setiap baris tabel Population pada Prerequisites (langkah 3 sampai 9): isi Field Name dan pilih Data Type baris itu; untuk Dropdown ketik tiap value lalu tekan Enter; untuk Numeric pilih Decimal Places; isi Placeholder dan ubah Required Field hanya bila kolom "Isian lain" menyatakannya
4. Klik [Submit]
5. Verifikasi toast sukses: "Success, custom field has been created."
6. Verifikasi popup tetap terbuka
7. Verifikasi Field Name kosong dan Data Type belum dipilih
8. Verifikasi `Dropdown Values` dan `Decimal Places` tidak tampil
9. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
10. Klik `[✕]`
11. Verifikasi halaman 1 tabel menampilkan 10 baris
12. Pindah ke halaman 2
13. Verifikasi halaman 2 tabel menampilkan 4 baris (total 14 field: 6 Pre-setup dan 8 Population)
14. Ketik Search `Sari D`, tekan Enter
15. Verifikasi tabel menampilkan 8 baris Population
16. Verifikasi setiap baris berstatus Active (switch On)
17. Verifikasi Modified By setiap baris `Sari D`
18. Verifikasi Last Updated setiap baris adalah hari uji
19. Klik `(←)` pada kotak Search

### TC-GS-UCF-75: Clear Field mengosongkan seluruh isian tanpa dialog dan tanpa mengubah checkbox Stay

20. Klik [+ Custom Field]
21. Centang checkbox `Stay on this form after submitting`
22. Isi Field Name `Temp`, Data Type `Dropdown`, ketik value `One` lalu tekan Enter, isi Placeholder `abc`, ubah Required Field ke Yes
23. Kosongkan Field Name, klik [Submit] hingga error tampil
24. Klik [Clear Field]
25. Verifikasi Field Name kosong
26. Verifikasi Data Type belum dipilih
27. Verifikasi `Dropdown Values` tidak tampil
28. Verifikasi Placeholder kosong
29. Verifikasi Required Field kembali No
30. Verifikasi border dan pesan error hilang
31. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
32. Verifikasi dialog `Unsaved Changes` tidak muncul
33. Verifikasi popup tetap terbuka
34. Verifikasi kursor fokus berada di field Field Name (field input pertama)
35. Klik `[✕]`
36. Verifikasi popup tertutup langsung tanpa dialog `Unsaved Changes` (form tidak dirty walau checkbox Stay tercentang)

### TC-GS-UCF-69: Submit Create happy path Data Type Text, Text Area, Date, dan Phone

37. Untuk setiap baris tabel D-10 sampai D-13 pada Prerequisites (langkah 37 sampai 41): klik [+ Custom Field]
38. Isi Field Name dan pilih Data Type baris itu, Placeholder dan Required dibiarkan default
39. Klik [Submit]
40. Verifikasi toast sukses: "Success, custom field has been created."
41. Verifikasi popup tertutup
42. Ketik Search `{runId}-018`, tekan Enter
43. Verifikasi tabel menampilkan 4 baris (`Hire Date {runId}-018`, `Mobile Backup {runId}-018`, `Remarks {runId}-018`, `Vehicle Plate {runId}-018`)
44. Verifikasi switch Active setiap baris On
45. Verifikasi Required setiap baris `No`
46. Verifikasi Value Setting setiap baris `—`
47. Verifikasi Modified By setiap baris `Sari D`
48. Verifikasi Last Updated setiap baris adalah hari uji
49. Verifikasi Placeholder `Vehicle Plate {runId}-018` adalah `Enter vehicle plate {runId}-018`
50. Verifikasi Placeholder `Remarks {runId}-018` adalah `Enter remarks {runId}-018`
51. Verifikasi Placeholder `Hire Date {runId}-018` adalah `Select date`
52. Verifikasi Placeholder `Mobile Backup {runId}-018` adalah `Enter phone number`
53. Verifikasi posisi baris mengikuti urutan A-Z Field Name
54. Klik `(←)` pada kotak Search

### TC-GS-UCF-70: Submit Create happy path Dropdown dengan Required, Placeholder custom, dan value

55. Klik [+ Custom Field]
56. Isi Field Name `Work Location {runId}-018`
57. Pilih Data Type `Dropdown`, ketik `HQ` lalu Enter, ketik `Branch` lalu Enter
58. Isi Placeholder `Choose work location`
59. Ubah switch Required Field menjadi Yes
60. Klik [Submit]
61. Verifikasi toast sukses: "Success, custom field has been created."
62. Verifikasi popup tertutup
63. Ketik Search `Work Location {runId}-018`, tekan Enter
64. Verifikasi Data Type baris adalah `Dropdown`
65. Verifikasi Value Setting baris menampilkan badge `HQ`, `Branch`
66. Verifikasi Placeholder baris adalah `Choose work location`
67. Verifikasi Required baris adalah `Yes`
68. Verifikasi switch Active baris On

### TC-GS-UCF-71: Submit Create happy path Numeric dengan Decimal Places

69. Klik [+ Custom Field]
70. Isi Field Name `Overtime Hours {runId}-018`
71. Pilih Data Type `Numeric`, pilih Decimal Places `2`
72. Klik [Submit]
73. Verifikasi toast sukses: "Success, custom field has been created."
74. Ganti isi kotak search dengan `Overtime Hours {runId}-018`, tekan Enter
75. Verifikasi Data Type baris adalah `Numeric`
76. Verifikasi Value Setting baris adalah `2 Decimal Places`
77. Verifikasi Placeholder baris adalah `Enter overtime hours {runId}-018`

### TC-GS-UCF-72: Required Field default No dan tersimpan sesuai pilihan

78. Klik [+ Custom Field]
79. Verifikasi switch Required Field awal berada pada No
80. Isi Field Name `Optional One {runId}-018`, Data Type `Text`
81. Klik [Submit]
82. Klik [+ Custom Field]
83. Isi Field Name `Mandatory One {runId}-018`, Data Type `Text`, ubah Required Field ke Yes
84. Klik [Submit]
85. Tunggu aksi selesai (popup tertutup)
86. Ganti isi kotak search dengan `Optional One {runId}-018`, tekan Enter
87. Verifikasi kolom Required `Optional One {runId}-018` adalah `No`
88. Ganti isi kotak search dengan `Mandatory One {runId}-018`, tekan Enter
89. Verifikasi kolom Required `Mandatory One {runId}-018` adalah `Yes`

### TC-GS-UCF-73: Stay on this form after submitting tidak dicentang menutup popup setelah Submit

90. Klik [+ Custom Field]
91. Isi Field Name `One Shot {runId}-018`, Data Type `Text`
92. Klik [Submit]
93. Verifikasi toast sukses: "Success, custom field has been created."
94. Verifikasi popup tertutup
95. Ganti isi kotak search dengan `One Shot {runId}-018`, tekan Enter
96. Verifikasi `One Shot {runId}-018` muncul di tabel

### TC-GS-UCF-74: Stay on this form after submitting dicentang mereset seluruh isian termasuk Required Field dan field tambahan

97. Klik [+ Custom Field]
98. Centang checkbox `Stay on this form after submitting`
99. Isi Field Name `Stay A {runId}-018`, Data Type `Numeric`, Decimal Places `2`, Required Field Yes, Placeholder `Enter value`
100. Klik [Submit]
101. Verifikasi toast sukses: "Success, custom field has been created."
102. Verifikasi popup tetap terbuka
103. Verifikasi Field Name kosong
104. Verifikasi Data Type belum dipilih
105. Verifikasi `Decimal Places` tidak tampil
106. Verifikasi Placeholder kosong
107. Verifikasi Required Field kembali No
108. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
109. Klik `[✕]`
110. Ganti isi kotak search dengan `Stay A {runId}-018`, tekan Enter
111. Verifikasi `Stay A {runId}-018` muncul di tabel

### TC-GS-UCF-450: Modified By pelaku bernama satu kata tampil utuh dengan hover nama lengkap

112. Ganti akun: logout, lalu login sebagai Total Control Client A (nama satu kata) `totalControlMono_automated_qaTeam1@qwertysystem.net` (Bagas) dengan `Spectra.env.GS_MONO_TC_PASSWORD` dan buka Global Settings > User > tab Custom Field
113. Klik [+ Custom Field]
114. Isi Field Name `Single Name Probe {runId}-018`, Data Type `Text`
115. Klik [Submit]
116. Verifikasi toast sukses: "Success, custom field has been created."
117. Ketik Search `Single Name Probe {runId}-018`, tekan Enter
118. Verifikasi sel Modified By menampilkan `Bagas` sebagai plain text tanpa inisial tambahan
119. Verifikasi sel Modified By tidak menampilkan avatar
120. Hover sel Modified By tersebut
121. Verifikasi tooltip `Bagas`

### TC-GS-UCF-451: Modified By pelaku dengan nama depan panjang tampil utuh dengan inisial belakang

122. Ganti akun: logout, lalu login sebagai Total Control Client A (nama depan panjang) `totalControlLongName_automated_qaTeam1@qwertysystem.net` (Buzzlightyear Sumardi) dengan `Spectra.env.GS_LONGNAME_TC_PASSWORD` dan buka Global Settings > User > tab Custom Field
123. Klik [+ Custom Field]
124. Isi Field Name `Long Name Probe {runId}-018`, Data Type `Text`
125. Klik [Submit]
126. Verifikasi toast sukses: "Success, custom field has been created."
127. Ketik Search `Long Name Probe {runId}-018`, tekan Enter
128. Verifikasi sel Modified By menampilkan `Buzzlightyear S`
129. Verifikasi nama depan tampil utuh tanpa pemotongan `..`
130. Hover sel Modified By tersebut
131. Verifikasi tooltip `Buzzlightyear Sumardi`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 1, 75, 69, 70, 71, 72, 73, 74, 450, 451 (urutan sumber 1, 69 sampai 75, 450, 451). TC-GS-UCF-1 pertama karena mengasersi total tepat 14 field sebelum field spec lain ada; TC-GS-UCF-75 (tidak membuat data) mendahului Create lain; TC-GS-UCF-74 ditaruh setelah TC-GS-UCF-73 karena memakai checkbox Stay, dan TC-GS-UCF-450 dan 451 di akhir karena butuh ganti akun. TC-GS-UCF-75 dan TC-GS-UCF-1 sama-sama menutup popup lewat `[✕]` pada form bersih.
- Langkah 3 sampai 9 diulang untuk delapan baris tabel Population; langkah 37 sampai 41 diulang untuk empat field D-10 sampai D-13 (parameter di Prerequisites).
- Asersi tabel "muncul di tabel" untuk TC-GS-UCF-74 (`Stay A` di belakang popup) ditaruh sesudah popup ditutup (langkah 109 sampai 111) karena tabel berada di belakang modal.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 10, 12, 14, 19, 21, 35, 42, 54, 63, 74, 85 (menunggu popup tertutup), 86, 88, 95, 98, 109, 110, 112 dan 122 (ganti akun eksplisit), 117, 127 (Search), serta pengisian form dan klik tombol sebagai bagian langkah TC. Langkah 2, 21, dan 98 (centang Stay) mengatur mode sesi popup.
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 10 TC satu topik (Create berhasil) dengan satu dataset; kegagalan keras satu Create tidak menghilangkan makna Create lain karena tiap Create memakai nama sendiri. Pemecahan hanya menambah login, hook, dan pembukaan popup. Ganti akun di dua blok terakhir memenuhi bagian 3 pengecualian (b): bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah 15 dan 43 adalah pembanding sebelum asersi universal langkah 16 sampai 18 dan 44 sampai 48 (bagian 8b butir 2, S-03), bukan Expected TC.
- Nama Population TC-GS-UCF-1 literal (pengecualian S-12 butir (i)): hook `before` menghapus sisa dan hook `after` menghapus yang dibuat spec; nama lain bersuffix `{runId}-018`. Placeholder default field bersuffix mengikuti nama bersuffix (`Enter vehicle plate {runId}-018`).
- Asersi Last Updated memakai toleransi satu menit terhadap waktu aksi, jam server dan jam browser sinkron (S-12).
- Temuan untuk QA:
  - Plan menyebut 14 field Pre-setup; tabel Pre-setup TC memuat 6 field dan 8 sisanya adalah hasil TC-GS-UCF-1. Spec ini membangun Population sendiri; spec lain men-seed 14 field lewat API.
  - TC-GS-UCF-1 mengasersi total tepat 14 field (10 di halaman 1, 4 di halaman 2): bergantung pada tidak adanya field sisa lain di Client A (dijamin hook `before` suite, butir Field sisa Client A di `suite.md`, dan hook `before` spec ini untuk sisa Population).
  - Post Condition b TC-GS-UCF-1 ("Field baru tersedia pada form User Login dan Non-Login pada katalog berikutnya") tidak punya langkah observasi dan tidak diasersi.
  - TC-GS-UCF-71 Expected `2 Decimal Places` (PRD, NC-10) berbeda dari LLD (`2 decimal places`); asersi mengikuti TC dan bisa gagal pada backend nyata sampai LLD diselaraskan.
  - Asersi Search `Sari D` (langkah 14 sampai 18) bergantung pada Search mencocokkan kolom Modified By; NC-06 mencatat LLD hanya mencocokkan sebagian kolom. Bila Modified By tidak dicari, langkah itu dapat diganti pencarian per nama.
  - TC-GS-UCF-450 dan 451 memakai akun yang ada di Pre-setup TC tetapi tanpa nama environment variable password; spec memakai nama baru `GS_MONO_TC_PASSWORD` dan `GS_LONGNAME_TC_PASSWORD` yang didaftarkan tim FE.
  - TC-GS-UCF-72 tidak memuat Expected toast pada kedua Create; hanya kolom Required yang diasersi.
