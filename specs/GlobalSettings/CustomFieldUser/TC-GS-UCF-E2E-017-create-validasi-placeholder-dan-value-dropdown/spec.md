---
id: TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown
title: "Create Custom Field: Validasi Placeholder, Placeholder Default, dan Value Dropdown"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-61
  - TC-GS-UCF-444
  - TC-GS-UCF-62
  - TC-GS-UCF-445
  - TC-GS-UCF-446
  - TC-GS-UCF-63
  - TC-GS-UCF-64
  - TC-GS-UCF-447
  - TC-GS-UCF-65
  - TC-GS-UCF-66
  - TC-GS-UCF-67
  - TC-GS-UCF-448
  - TC-GS-UCF-68
  - TC-GS-UCF-449
coverage:
  web: automated
---

# Create Custom Field: Validasi Placeholder, Placeholder Default, dan Value Dropdown

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi, Modified By `Sari D`). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > tab Custom Field, dibuka di hook `beforeEach`.
- Data Pre-setup: tidak ada yang dibaca atau diubah. Spec membuat datanya sendiri (S-06).
- Data dinamis (dibuat lewat UI oleh spec ini; `{runId}` terdiri atas digit):
  - D-182: Field Name `Trim Placeholder Field {runId}-017`, Data Type Text, Placeholder = 2 spasi + 120 karakter `A` + 2 spasi.
  - D-09: Field Name `Spacey {runId}-017`, Data Type Text, Placeholder 3 spasi (tersimpan kosong; nilai efektif `Enter spacey {runId}-017`).
  - D-183: Field Name `Employee ID {runId}-017`, Data Type Text, Placeholder kosong (nilai efektif `Enter employee id {runId}-017`).
  - D-184: Field Name = karakter `K` diulang + ` {runId}-017` sehingga panjang tepat 120 karakter; Data Type Text; Placeholder kosong (nilai efektif `Enter ` + nama huruf kecil, 126 karakter).
  - D-185: Field Name `Probe Chip {runId}-017`, Data Type Dropdown; value yang diketik `Alpha`, `Beta`, lalu `Alpha` diubah menjadi `Gamma` dan `Beta` dihapus; tersimpan hanya `Gamma`.
  - D-186: Field Name `Many Values DD {runId}-017`, Data Type Dropdown, 101 value (parameter langkah 102; satu baris pola mewakili 101 baris):

    | No | Value |
    |---|---|
    | 001 sampai 101 | `V` + nomor urut tiga digit (`V001` sampai `V101`) |

  - Nilai yang hanya diketik dan tidak pernah tersimpan: Field Name `Probe Placeholder Max`, `Empty Options`, `Probe Enter`; value `Alpha`, `ALPHA`, `  Alpha  `, ` ALPHA `; 120 dan 121 karakter `A`; 3 spasi.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Client A yang namanya memuat `{runId}-017`.
- Kemampuan teknis: pembacaan daftar request jaringan yang terekam sejak langkah tertentu (TC-GS-UCF-63 dan 68); klik pada badge value untuk rename dan klik `×` untuk hapus; hover sel tabel; Search pada tabel dan Changelog.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Validasi diblokir (tidak membuat data)

#### TC-GS-UCF-61: Placeholder 120 karakter diterima dan 121 karakter menampilkan error

1. Klik [+ Custom Field]
2. Pilih Data Type `Text`
3. Ketik 120 karakter `A` di Placeholder
4. Verifikasi tidak ada error pada Placeholder
5. Tambahkan 1 karakter `A` (total 121 karakter)
6. Verifikasi error inline `Max. 120 characters` pada Placeholder
7. Isi Field Name `Probe Placeholder Max`
8. Klik [Submit]
9. Verifikasi error inline `Max. 120 characters` tetap tampil
10. Verifikasi popup tetap terbuka
11. Verifikasi tidak ada toast sukses

#### TC-GS-UCF-63: Submit Dropdown tanpa value ditolak

12. Klik [Clear Field]
13. Isi Field Name `Empty Options`
14. Pilih Data Type `Dropdown`
15. Klik [Submit]
16. Verifikasi error inline `Dropdown values must not be empty` pada Dropdown Values
17. Verifikasi daftar request jaringan yang terekam sejak langkah 1 tidak memuat request tulis ke server
18. Verifikasi popup tetap terbuka

#### TC-GS-UCF-64: Value Dropdown kosong atau hanya spasi ditolak saat Enter

19. Klik [Clear Field]
20. Pilih Data Type `Dropdown`
21. Tekan Enter pada input Dropdown Values yang kosong
22. Verifikasi error inline `Option name must not be empty` (input kosong)
23. Ketik 3 spasi di input Dropdown Values, tekan Enter
24. Verifikasi error inline `Option name must not be empty` (3 spasi)
25. Verifikasi tidak ada badge yang ditambahkan

#### TC-GS-UCF-447: Value Dropdown hanya spasi ditolak saat fokus meninggalkan input

26. Klik [Clear Field]
27. Pilih Data Type `Dropdown`
28. Ketik 3 spasi di input Dropdown Values tanpa menekan Enter
29. Klik area kosong di luar input
30. Verifikasi error inline `Option name must not be empty` muncul saat fokus meninggalkan input
31. Verifikasi tidak ada badge yang ditambahkan

#### TC-GS-UCF-65: Value Dropdown ditambahkan hanya saat Enter dan tampil sebagai badge

32. Klik [Clear Field]
33. Isi Field Name `Probe Enter`
34. Pilih Data Type `Dropdown`
35. Ketik `Alpha` di Dropdown Values tanpa menekan Enter
36. Klik [Submit]
37. Verifikasi tidak ada badge
38. Verifikasi [Submit] menampilkan error `Dropdown values must not be empty`
39. Tekan Enter pada teks `Alpha` yang masih ada di input
40. Verifikasi `Alpha` menjadi badge
41. Verifikasi input Dropdown Values kosong kembali
42. Ketik `Beta`, tekan Enter
43. Verifikasi urutan badge `Alpha`, `Beta` (`Beta` ditambahkan di akhir)

#### TC-GS-UCF-66: Value Dropdown duplikat ditolak tanpa membedakan huruf besar kecil

44. Klik [Clear Field]
45. Pilih Data Type `Dropdown`
46. Ketik `Alpha`, tekan Enter
47. Ketik `ALPHA`
48. Verifikasi error inline `Option name already exists` tampil langsung saat mengetik (tanpa debounce)
49. Tekan Enter
50. Verifikasi value `ALPHA` tidak ditambahkan dan hanya ada satu badge `Alpha`

#### TC-GS-UCF-67: Value Dropdown 120 karakter diterima dan 121 karakter menampilkan error

51. Klik [Clear Field]
52. Pilih Data Type `Dropdown`
53. Ketik 120 karakter `A`, tekan Enter
54. Verifikasi 120 karakter menjadi badge
55. Ketik 121 karakter `A`
56. Verifikasi error inline `Max. 120 characters`
57. Tekan Enter
58. Verifikasi Enter tidak menambah badge

#### TC-GS-UCF-448: Value Dropdown dengan spasi di tepi di-trim sebelum pengecekan keunikan

59. Klik [Clear Field]
60. Pilih Data Type `Dropdown`
61. Ketik `  Alpha  ` (spasi di kedua tepi) di Dropdown Values, tekan Enter
62. Verifikasi badge `Alpha` ditambahkan tanpa spasi tepi
63. Ketik ` ALPHA ` (spasi di kedua tepi)
64. Verifikasi error inline `Option name already exists` (perbandingan setelah trim, tanpa membedakan huruf besar kecil)
65. Tekan Enter
66. Verifikasi tidak ada badge baru dan hanya ada satu badge `Alpha`

### Create berhasil (membuat data)

67. Klik [Clear Field]
68. Centang checkbox `Stay on this form after submitting` agar beberapa Create terjadi dalam satu sesi popup

#### TC-GS-UCF-444: Placeholder 120 karakter dengan spasi di tepi diterima dan disimpan ter-trim

69. Isi Field Name `Trim Placeholder Field {runId}-017` (D-182)
70. Pilih Data Type `Text`
71. Ketik 2 spasi, lalu 120 karakter `A`, lalu 2 spasi di Placeholder
72. Verifikasi tidak ada error `Max. 120 characters` (panjang dihitung setelah trim: 120 karakter)
73. Klik [Submit]
74. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-62: Placeholder hanya berisi spasi disimpan kosong

75. Isi Field Name `Spacey {runId}-017` (D-09)
76. Pilih Data Type `Text`
77. Ketik 3 spasi di Placeholder
78. Klik [Submit]
79. Verifikasi tidak ada error
80. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-445: Placeholder default memakai Field Name huruf kecil tanpa mempertahankan akronim

81. Isi Field Name `Employee ID {runId}-017` (D-183)
82. Pilih Data Type `Text`, Placeholder dibiarkan kosong
83. Klik [Submit]
84. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-446: Placeholder default untuk Field Name 120 karakter tampil utuh tanpa dipotong

85. Ketik Field Name D-184 (karakter `K` diulang + ` {runId}-017`, total 120 karakter)
86. Pilih Data Type `Text`, Placeholder dibiarkan kosong
87. Klik [Submit]
88. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-68: Badge Dropdown di-rename dan dihapus tanpa dialog, hasilnya tersimpan saat Submit

89. Pilih Data Type `Dropdown`
90. Ketik `Alpha`, tekan Enter; ketik `Beta`, tekan Enter
91. Klik teks badge `Alpha`, ubah menjadi `Gamma`, tekan Enter
92. Verifikasi badge `Alpha` menjadi input edit lalu menjadi badge `Gamma`
93. Klik `×` pada badge `Beta`
94. Verifikasi badge `Beta` hilang tanpa dialog `Remove Value`
95. Verifikasi helper `Press enter to add new value or click the badge to edit` tampil
96. Verifikasi daftar request jaringan yang terekam sejak langkah 89 tidak memuat request tulis ke server
97. Isi Field Name `Probe Chip {runId}-017` (D-185)
98. Klik [Submit]
99. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-GS-UCF-449: Jumlah value Dropdown tidak dibatasi: 101 value diterima

100. Isi Field Name `Many Values DD {runId}-017` (D-186)
101. Pilih Data Type `Dropdown`
102. Untuk setiap baris tabel D-186 pada Prerequisites (langkah 102; 101 nilai `V001` sampai `V101`): ketik nilai di Dropdown Values, tekan Enter
103. Verifikasi Dropdown Values memuat 101 badge tanpa pesan batas jumlah
104. Klik [Submit]
105. Verifikasi toast sukses: "Success, custom field has been created."

### Verifikasi tabel dan Changelog setelah popup ditutup

106. Klik `[✕]`
107. Ketik Search `Trim Placeholder Field {runId}-017`, tekan Enter
108. Verifikasi kolom Placeholder baris tersebut menampilkan 120 karakter `A` tanpa spasi tepi (TC-GS-UCF-444)
109. Ganti isi kotak search dengan `Spacey {runId}-017`, tekan Enter
110. Verifikasi kolom Placeholder baris `Spacey {runId}-017` menampilkan nilai efektif default `Enter spacey {runId}-017` (TC-GS-UCF-62)
111. Klik `⋯` pada baris `Spacey {runId}-017` > Edit
112. Verifikasi popup Edit menampilkan Placeholder kosong
113. Klik `[✕]`
114. Ganti isi kotak search dengan `Employee ID {runId}-017`, tekan Enter
115. Verifikasi kolom Placeholder menampilkan nilai efektif `Enter employee id {runId}-017` (seluruhnya huruf kecil; akronim `ID` tidak dipertahankan) (TC-GS-UCF-445)
116. Ganti isi kotak search dengan 10 karakter `K`, tekan Enter
117. Verifikasi sel Placeholder baris D-184 menampilkan `Enter ` diikuti nama huruf kecil (126 karakter) utuh tanpa pemotongan `..` (TC-GS-UCF-446)
118. Hover sel Placeholder baris D-184
119. Verifikasi hover tidak menampilkan tooltip
120. Ganti isi kotak search dengan `Probe Chip {runId}-017`, tekan Enter
121. Verifikasi Data Type baris `Probe Chip {runId}-017` adalah `Dropdown` (TC-GS-UCF-68)
122. Verifikasi Value Setting baris `Probe Chip {runId}-017` hanya badge `Gamma` (tanpa `Alpha` dan `Beta`)
123. Klik icon Changelog
124. Ketik Search `Probe Chip {runId}-017` di Changelog, tekan Enter
125. Verifikasi Changelog memuat entri Create (tepat 1) untuk `Probe Chip {runId}-017`
126. Verifikasi tidak ada entri `Probe Chip {runId}-017 — Value Setting` di Changelog
127. Tutup modal Changelog
128. Ganti isi kotak search dengan `Many Values DD {runId}-017`, tekan Enter
129. Verifikasi kolom Value Setting menampilkan badge `V001`, `V002`, lalu `+99 more` (TC-GS-UCF-449)
130. Klik `+99 more` pada baris `Many Values DD {runId}-017`
131. Verifikasi popup `All Values` dengan baris identitas `Many Values DD {runId}-017 (101)` memuat 101 badge `V001` sampai `V101`
132. Tutup popup `All Values` dengan Esc
133. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 61, 63, 64, 447, 65, 66, 67, 448 (validasi diblokir), lalu 444, 62, 445, 446, 68, 449 (Create berhasil). Urutan sumber (61, 444, 62, ...) berubah demi satu sesi popup dan validasi diblokir sebelum aksi yang membuat data (bagian 3 prinsip 3 dan 7). [Clear Field] dipakai di antara kasus karena TC ini hanya mengetik tanpa submit (halaman yang sama dipakai berulang, prinsip 13); satu-satunya kejadian menutup popup adalah langkah 106.
- Langkah penghubung (aksi tanpa `Verifikasi`): [Clear Field] (langkah 12, 19, 26, 32, 44, 51, 59, 67), langkah 68 (centang Stay; mengatur mode sesi popup), pemilihan Data Type dan pengisian nama sebagai bagian langkah TC, langkah 106 (menutup popup agar tabel terlihat), langkah 107, 109, 114, 116, 120, 128 (Search agar baris target tampil), langkah 111 dan 113 (membuka dan menutup Edit untuk TC-GS-UCF-62), langkah 123, 124, 127 (membuka, mencari, dan menutup Changelog), langkah 130 dan 132, serta langkah 133 (mereset Search).
- Langkah 102 diulang 101 kali (nilai `V001` sampai `V101`); parameter di tabel Prerequisites D-186 ditulis sebagai satu baris pola (`V` + nomor urut tiga digit) yang menggantikan 101 baris tabel; dihitung dengan ekspansi, spec melewati sekitar 35 langkah. Alasan (bagian 3 prinsip 13): 14 TC satu topik (validasi Placeholder dan value Dropdown pada popup Create) dengan satu akun dan satu dataset; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01). Blok Create berhasil tetap bermakna bila blok validasi gagal, karena tiap Create memakai nama sendiri.
- Nama D-182, D-09, D-183, D-184, D-185, dan D-186 bersuffix `{runId}-017` (S-12). Panjang 120 karakter pada D-184 sudah termasuk suffix sehingga batas yang diuji tidak berubah; nilai efektif Placeholder default mengikuti nama bersuffix.
- TC-GS-UCF-68 mencatat Changelog tepat 1 entri Create dan tidak ada entri Value Setting: asersi jumlah dengan nama unik (baseline nol), bukan kelas g.
- Temuan untuk QA:
  - TC-GS-UCF-68 Expected c "Form dirty" tidak memiliki indikator yang teramati langsung tanpa menutup popup; spec hanya mengasersi bagian yang dapat diamati (tidak ada request tulis). Perilaku dirty ditutup di spec Create unsaved changes.
  - TC-GS-UCF-63 dan 68 mensyaratkan pembacaan daftar request jaringan; endpoint yang dihitung sebagai "request tulis" (Create Custom Field) tidak disebut di TC, sehingga cakupannya ditulis sebagai kemampuan teknis tanpa mengarang endpoint.
  - Teks tombol dan judul modal Changelog tidak disebut di TC ini; langkah menutup Changelog ditulis tanpa label.
