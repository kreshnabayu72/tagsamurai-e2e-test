---
id: TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name
title: "Edit Custom Field: Screening Popup Edit, Aksesibilitas, dan Validasi Field Name (Kosong, Hanya Spasi, Batas Panjang, Trim, Duplikat, Karakter Non-Latin, Data Type Kosong)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-91
  - TC-GS-UCF-92
  - TC-GS-UCF-406
  - TC-GS-UCF-93
  - TC-GS-UCF-331
  - TC-GS-UCF-94
  - TC-GS-UCF-95
  - TC-GS-UCF-96
  - TC-GS-UCF-456
  - TC-GS-UCF-457
  - TC-GS-UCF-465
  - TC-GS-UCF-466
coverage:
  web: automated
---

# Edit Custom Field: Screening Popup Edit, Aksesibilitas, dan Validasi Field Name (Kosong, Hanya Spasi, Batas Panjang, Trim, Duplikat, Karakter Non-Latin, Data Type Kosong)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (login di hook `before`; password hanya lewat env var, tidak ditulis di spec atau fixture): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`.
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup (hanya dibaca, tidak disimpan, tidak diedit; Last Updated dan Modified By barisnya tidak berubah; 14 field Client A di-seed hook `before` lewat API dengan `Fixture.customFieldUser.preset14`): `Cost Center` (Dropdown: Finance, Operations, Marketing; Placeholder `Select cost center`; Required Yes) untuk TC-GS-UCF-91 dan sebagai nama bentrok pada TC-GS-UCF-96; `Bonus` (Numeric, Decimal Places 2, nilai User Rahmat Hidayat = `1500.50`) untuk TC-GS-UCF-92; `Employee Grade` (Text) untuk TC-GS-UCF-406; `Joining Date` (Inactive) sebagai nama bentrok pada TC-GS-UCF-457. Pada semua target Pre-setup popup ditutup lewat `✕` tanpa Save.
- Data Dinamis milik spec (seeding lewat API di hook `before`, bersuffix `{runId}-031`; fixture baru `Fixture.customFieldUser.edit031`; seluruhnya Text, Placeholder kosong, Required No, Active, tanpa nilai User):
  - `Edit Meta {runId}-031` (TC-GS-UCF-93, 94, 95; menjadi `Edit Meta Renamed {runId}-031` pada TC-GS-UCF-95 dan dipakai TC-GS-UCF-96).
  - `Edit Blank Name {runId}-031` (TC-GS-UCF-331).
  - `Edit Unique Probe {runId}-031` (TC-GS-UCF-456 dan 457; tidak pernah tersimpan dengan nama lain).
  - `Edit Type Req {runId}-031` (TC-GS-UCF-466).
  - `Edit Script Probe {runId}-031` (TC-GS-UCF-465; menjadi `Kode Ünit – 部門 #2 {runId}-031`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-031` (termasuk nama hasil perubahan); tidak ada perubahan pada data Pre-setup.
- Kemampuan teknis: membaca atribut ARIA (`aria-required`, `aria-describedby`) dan urutan fokus keyboard pada popup; menghitung karakter string uji (120 dan 121 karakter `A`); menunggu jeda ±500 ms (debounce validasi unik) setelah mengetik Field Name pada langkah 83, 89, dan 104, sesuai TC-GS-UCF-456, 457, dan 96.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Persiapan tabel

1. Ketik Search `{runId}-031`, tekan Enter

### TC-GS-UCF-91: Screening Popup Edit Custom Field Dropdown pre-filled

2. Ganti isi kotak search dengan `Cost Center`, tekan Enter
3. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
4. Verifikasi judul popup `Edit Custom Field`
5. Verifikasi icon close `[✕]` tampil di header
6. Verifikasi `Field Name *` terisi `Cost Center`
7. Verifikasi `Data Type *` terisi `Dropdown` dengan icon `[ℹ]`
8. Verifikasi `Dropdown Values` memuat badge `Finance`, `Operations`, `Marketing` masing-masing dengan kontrol `×`
9. Verifikasi helper `Press enter to add new value or click the badge to edit` tampil pada `Dropdown Values`
10. Verifikasi `Placeholder` terisi `Select cost center`
11. Verifikasi switch `Required Field` pada Yes
12. Verifikasi `Decimal Places` tidak tampil
13. Verifikasi footer tidak memuat checkbox `Stay on this form after submitting`
14. Verifikasi footer memuat `[Clear Field]` (text, primary) dan `[Save]` (filled, success)
15. Verifikasi footer tidak memuat `[Cancel]`
16. Klik `[✕]`

### TC-GS-UCF-92: Popup Edit Numeric yang sudah memiliki nilai User

17. Ganti isi kotak search dengan `Bonus`, tekan Enter
18. Klik `⋯` pada baris `Bonus`, pilih `Edit`
19. Verifikasi field `Decimal Places` tampil dengan nilai `2`
20. Verifikasi field `Decimal Places` Enabled
21. Verifikasi Field Name, Placeholder, dan Required Field dapat diedit
22. Klik `[✕]`

### TC-GS-UCF-406: Aksesibilitas Popup Edit, aria-required, aria-describedby, dan focus trap

23. Ganti isi kotak search dengan `Employee Grade`, tekan Enter
24. Klik `⋯` pada baris `Employee Grade`, pilih `Edit`
25. Periksa atribut input Field Name dan Data Type
26. Verifikasi input `Field Name *` dan `Data Type *` memiliki `aria-required="true"`
27. Klik `[Clear Field]`
28. Klik `[Save]`
29. Verifikasi pesan `Field name must not be empty` tampil di bawah Field Name
30. Verifikasi pesan `Data type must not be empty` tampil di bawah Data Type
31. Verifikasi input Field Name memiliki `aria-describedby` yang merujuk elemen pesan `Field name must not be empty`
32. Verifikasi input Data Type memiliki `aria-describedby` yang merujuk elemen pesan `Data type must not be empty`
33. Tekan Tab berulang melewati elemen terakhir
34. Verifikasi fokus keyboard berputar di dalam popup Edit
35. Klik `[✕]`
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`
38. Verifikasi popup tertutup
39. Verifikasi `Employee Grade` tidak berubah

### TC-GS-UCF-93: Save dengan Field Name dikosongkan ditolak

40. Ganti isi kotak search dengan `{runId}-031`, tekan Enter
41. Klik `⋯` pada baris `Edit Meta {runId}-031`, pilih `Edit`
42. Hapus seluruh isi Field Name
43. Klik `[Save]`
44. Verifikasi error inline `Field name must not be empty`
45. Verifikasi popup tetap terbuka
46. Verifikasi perubahan tidak tersimpan (tidak ada toast sukses)

### TC-GS-UCF-331: Field Name hanya berisi spasi dianggap kosong

47. Klik `[✕]`
48. Verifikasi dialog `Unsaved Changes` tampil
49. Klik `[Leave]`
50. Klik `⋯` pada baris `Edit Blank Name {runId}-031`, pilih `Edit`
51. Ganti Field Name dengan 3 spasi
52. Klik `[Save]`
53. Verifikasi error inline `Field name must not be empty`
54. Verifikasi popup tetap terbuka
55. Verifikasi perubahan tidak tersimpan (tidak ada toast sukses)

### TC-GS-UCF-94: Field Name 120 karakter diterima dan 121 karakter menampilkan error

56. Klik `[✕]`
57. Verifikasi dialog `Unsaved Changes` tampil
58. Klik `[Leave]`
59. Klik `⋯` pada baris `Edit Meta {runId}-031`, pilih `Edit`
60. Ganti Field Name dengan 120 karakter `A`
61. Verifikasi tidak ada error pada Field Name
62. Tambahkan 1 karakter `A` pada Field Name
63. Verifikasi error inline `Max. 120 characters` tampil real-time
64. Klik `[Save]`
65. Verifikasi error inline `Max. 120 characters` tetap tampil
66. Verifikasi popup tetap terbuka
67. Verifikasi tidak ada toast sukses

### TC-GS-UCF-466: Save Edit dengan Data Type dikosongkan ditolak

68. Klik `[✕]`
69. Verifikasi dialog `Unsaved Changes` tampil
70. Klik `[Leave]`
71. Klik `⋯` pada baris `Edit Type Req {runId}-031`, pilih `Edit`
72. Klik `[Clear Field]`
73. Ketik `Edit Type Req Renamed {runId}-031` di Field Name
74. Klik `[Save]`
75. Verifikasi error inline `Data type must not be empty` pada Data Type
76. Verifikasi Field Name tidak menampilkan error
77. Verifikasi popup tetap terbuka
78. Verifikasi tidak ada toast sukses

### TC-GS-UCF-456: Field Name ke nama field lain dengan huruf besar dan spasi tepi ditolak

79. Klik `[✕]`
80. Verifikasi dialog `Unsaved Changes` tampil
81. Klik `[Leave]`
82. Klik `⋯` pada baris `Edit Unique Probe {runId}-031`, pilih `Edit`
83. Ganti Field Name menjadi ` COST CENTER ` (spasi di kedua tepi), tunggu ±500 ms
84. Verifikasi error inline `Field name already exists` tampil otomatis setelah jeda ketik (±500 ms)
85. Klik `[Save]`
86. Verifikasi error inline `Field name already exists` tetap tampil
87. Verifikasi popup tetap terbuka
88. Verifikasi tidak ada toast sukses

### TC-GS-UCF-457: Field Name ke nama field Inactive ditolak

89. Ganti Field Name menjadi `Joining Date`, tunggu ±500 ms
90. Verifikasi error inline `Field name already exists` tampil (field Inactive ikut dibandingkan)
91. Klik `[Save]`
92. Verifikasi error inline `Field name already exists` tetap tampil
93. Verifikasi popup tetap terbuka
94. Verifikasi tidak ada toast sukses

### TC-GS-UCF-95: Field Name dengan spasi tepi disimpan ter-trim

95. Klik `[✕]`
96. Verifikasi dialog `Unsaved Changes` tampil
97. Klik `[Leave]`
98. Klik `⋯` pada baris `Edit Meta {runId}-031`, pilih `Edit`
99. Ganti Field Name menjadi `  Edit Meta Renamed {runId}-031  `
100. Klik `[Save]`
101. Verifikasi toast sukses: "Success, custom field has been updated."
102. Verifikasi tabel menampilkan `Edit Meta Renamed {runId}-031` tanpa spasi tepi

### TC-GS-UCF-96: Field Name ke nama field lain ditolak dan nama sendiri tidak dianggap duplikat

103. Klik `⋯` pada baris `Edit Meta Renamed {runId}-031`, pilih `Edit`
104. Ganti Field Name menjadi `Cost Center`, tunggu ±500 ms
105. Verifikasi error inline `Field name already exists` tampil otomatis setelah jeda ketik
106. Ganti kembali Field Name menjadi `Edit Meta Renamed {runId}-031`
107. Verifikasi error `Field name already exists` hilang (record sendiri dikecualikan)
108. Klik `[✕]`

### TC-GS-UCF-465: Field Name menerima huruf beraksen, aksara non-Latin, dan tanda baca

109. Klik `⋯` pada baris `Edit Script Probe {runId}-031`, pilih `Edit`
110. Ganti Field Name menjadi `Kode Ünit – 部門 #2 {runId}-031`
111. Klik `[Save]`
112. Verifikasi tidak ada error karakter
113. Verifikasi toast sukses: "Success, custom field has been updated."
114. Verifikasi baris tampil dengan Field Name `Kode Ünit – 部門 #2 {runId}-031` persis

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (114 langkah). Seluruhnya satu kelas (fungsional, popup Edit dan validasi Field Name), satu akun, dan satu dataset; tiap blok memakai seed bersuffix sendiri atau target Pre-setup yang hanya dibaca, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Urutan TC: screening dulu (TC-GS-UCF-91, 92, 406), validasi yang diblokir (TC-GS-UCF-93, 331, 94, 466, 456, 457), baru aksi yang menyimpan (TC-GS-UCF-95, 96, 465). Urutan ini berbeda dari urutan TC sumber (TC-GS-UCF-96 menyusul TC-GS-UCF-95 karena memakai nama hasil rename; TC-GS-UCF-406 dipindah ke screening).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target atau mengganti target (`{runId}-031`, `Cost Center`, `Bonus`, `Employee Grade`); `✕` dan `[Leave]` yang menutup popup (pada form dirty ditulis `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]`, S-08; `Verifikasi` itu tidak dicatat lagi di sini); `✕` yang menutup popup bersih. Pada TC-GS-UCF-457 form dan field TC-GS-UCF-456 yang masih dirty dilanjutkan karena kedua TC memakai field dan form yang sama. Langkah mengikuti TC-GS-UCF-406 butir d dan e: Tab berulang, `Verifikasi` fokus berputar, lalu popup ditutup dan `Employee Grade` diperiksa.
- Target Pre-setup (`Cost Center`, `Bonus`, `Employee Grade`) hanya dibuka dan ditutup tanpa Save; `Cost Center` dan `Joining Date` pada TC-GS-UCF-96 dan 457 hanya sebagai nama bentrok yang diketik di field milik spec (S-06). Pengecualian S-06 itu dinyatakan di Prerequisites.
- Nama field uji di TC (`Edit Meta`, `Edit Meta Renamed`, `Edit Blank Name`, `Edit Unique Probe`, `Edit Type Req`, `Edit Script Probe`, `Kode Ünit – 部門 #2`) ditulis bersuffix `{runId}-031` (S-12). Panjang 120 karakter `A` pada TC-GS-UCF-94 mengganti seluruh isi field sehingga tidak memuat suffix.
- Pembagian TC lintas spec: TC-GS-UCF-97 (Placeholder 120 karakter, memakai `Edit Meta Renamed`) ada di spec 032; TC-GS-UCF-99 (rename `Edit Meta Final`) ada di spec 033.
- Temuan untuk QA:
  - TC-GS-UCF-95: Post Condition "Edit Meta menjadi Edit Meta Renamed" tanpa langkah observasi tambahan di TC; teramati lewat Expected b. TC-GS-UCF-465: Post Condition sama dengan Expected c.
  - TC-GS-UCF-93, 331, 94, 456, 457, 466: tidak ada Post Condition; "perubahan tidak tersimpan" ditulis sebagai `Verifikasi` tidak ada toast sukses (observasi sebatas UI; state backend tidak dibaca, TC tidak memberi langkah observasi).
  - TC-GS-UCF-406: butir e "Employee Grade tidak berubah" diasersi lewat tabel setelah popup ditutup; TC tidak menyebut kolom yang diperiksa.
  - TC-GS-UCF-96 menyebut dependensi TC-GS-UCF-95 (nama `Edit Meta Renamed`); spec menyalin langkah rename (blok TC-GS-UCF-95) sebagai prasyarat (S-04).
  - TC-GS-UCF-406, 91, 92 memakai data Pre-setup "14 field" (6 Pre-setup + 8 Population dari TC-GS-UCF-1); spec memakai 14 field yang di-seed hook `before` tanpa bergantung pada hasil TC-GS-UCF-1 (S-06).
