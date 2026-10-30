---
id: TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options
title: "Import User Login: Kolom Custom Field di Staging Table, Kolom Tak Dikenal, Create Missing Options (Log Tiga Surface, Urutan Value, Nama Sudah Ditambahkan Admin Lain, Field Dinonaktifkan Admin Lain, Pemegang Import data Create)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-300
  - TC-GS-UCF-536
  - TC-GS-UCF-560
  - TC-GS-UCF-561
  - TC-GS-UCF-564
  - TC-GS-UCF-565
  - TC-GS-UCF-562
coverage:
  web: automated
---

# Import User Login: Kolom Custom Field di Staging Table, Kolom Tak Dikenal, Create Missing Options (Log Tiga Surface, Urutan Value, Nama Sudah Ditambahkan Admin Lain, Field Dinonaktifkan Admin Lain, Pemegang Import data Create)

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas d (harness eksternal Import): objek uji adalah draft Import User Login dan dampaknya pada definisi Custom Field.
- Suite serial (`parallel: false`): draft Import User Login hanya boleh satu yang aktif per entitas (`IMP-LOGIC-02`), sehingga spec ini tidak boleh dijalankan paralel dengan spec lain yang memakai Import User Login di Client A.
- Akun aktor:
  - Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Import data: Create dan Read Rina Marlina (Modified By `Rina M`) `importCreate_automated_qaTeam1@qwertysystem.net` (Pre-setup TC; hanya capability Import data C dan R, tanpa Manage user and role dan bukan Total Control atau Read Only) untuk TC-GS-UCF-562, login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_IMPORTCREATE_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Pelaku kedua pada TC-GS-UCF-564 dan 565: Total Control Client A Admin kedua Nadia Pratama (Modified By `Nadia P`) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), hanya memicu perubahan lewat sesi API (P-2) dengan `Spectra.env.GS_TC2_PASSWORD`; mekanisme sesi API disediakan tim FE/BE. Spec tidak membuka sesi UI kedua.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah yang berpindah ke Import atau Staging Table ditulis eksplisit.
- Data Pre-setup (baca-saja): 6 Custom Field Pre-setup Client A dan Changelog Pre-setup tidak diubah; Login User Rahmat Hidayat `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Pre-setup TC; nilai `Import Sync Probe` milik spec).
- Data Dinamis (nama bersuffix `{runId}-074`; fixture baru `Fixture.customFieldUser.import074`), di-seed lewat API oleh Sari Dewi di hook `before` (seeding menghasilkan satu entri Create per field di Changelog, System Log, dan Activity Log; entri ini menjadi baseline):
  - `Consumer Probe {runId}-074` (Text, Active; nilai User Rahmat Hidayat = `Probe Value`; D-89) untuk TC-GS-UCF-300.
  - `Import Log Probe {runId}-074` (Dropdown `Pagi`, `Siang`; Active; Required No; bebas nilai User; D-255) untuk TC-GS-UCF-560.
  - `Import Sync Probe {runId}-074` (Dropdown `Red`, `Green`; Active; nilai User Rahmat Hidayat = `Green`; D-257) untuk TC-GS-UCF-561.
  - `Import Dup Probe {runId}-074` (Dropdown `Pagi`, `Siang`; Active; bebas nilai User; D-260) untuk TC-GS-UCF-564.
  - `Import Skip Probe {runId}-074` (Dropdown `Pagi`, `Siang`; Active; bebas nilai User; D-261) untuk TC-GS-UCF-565.
  - `Import Cap Probe {runId}-074` (Dropdown `Pagi`, `Siang`; Active; bebas nilai User; D-259) untuk TC-GS-UCF-562.
  - Berkas Import: `Fixture.customFieldUser.importUnknownCsv074` (D-241): CSV dari template Import User Login dengan satu baris data valid ditambah kolom `Unknown Field` bernilai `Value X` (disediakan tim FE).
  - Draft Import User Login per TC (D-256 untuk TC-GS-UCF-560, D-258 untuk 561, D-259 untuk 562, D-260 untuk 564, D-261 untuk 565, dan draft 1 baris untuk TC-GS-UCF-300): satu-satunya draft aktif, 1 baris valid dengan nilai kategori Dropdown terkait = `Malam` (561: `Blue`) berstatus `error`. Penyiapan draft tiap TC ditulis sebagai langkah eksplisit; mekanisme penyiapannya (draft dari berkas CSV via Import atau fixture BE) disediakan tim FE/BE. Draft dibuang di akhir tiap TC.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-074` yang masih ada; buang draft Import User Login aktif Client A; kembalikan sesi ke Sari Dewi. Entri Changelog, System Log, dan Activity Log bersifat audit trail permanen dan tidak dibersihkan; asersi hitungan memakai nama bersuffix unik per run (S-12).
- Kemampuan teknis: upload berkas CSV lewat file picker Import; penyiapan draft Import (di atas); sesi API Nadia Pratama; ganti akun (logout lalu login); pemantauan jaringan untuk status respons permintaan `[Create Missing Options]` (TC-GS-UCF-562); Search pada Modal Changelog, tab System Log di Detail User, dan Activity Log tab User Action (kolom pencarian tidak dijelaskan di TC; lihat Temuan untuk QA).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (Sari Dewi dan Rina Marlina) dan hook `after` memulihkannya; lihat `suite.md`.
- State global: tidak ada yang diubah selain flag Guided Tooltip, sesi akun, dan draft Import (dibuang seperti di atas).

## Test Steps

### TC-GS-UCF-536: Import User Login dengan kolom tak dikenal tidak membuat atau mengubah definisi Custom Field

1. Buka Global Settings > Import > User Login (tanpa draft aktif)
2. Unggah berkas CSV `Fixture.customFieldUser.importUnknownCsv074` (D-241) lewat `[Upload File]` dan file picker
3. Verifikasi Modal Column Mapping memuat Target Attribute `Email` (pembanding: daftar sudah termuat)
4. Verifikasi daftar Target Attribute pada Modal Column Mapping tidak memuat atribut target `Unknown Field`
5. Klik `[Confirm Mapping]`
6. Verifikasi Modal Column Mapping tertutup
7. Verifikasi baris tampil pada Staging Table
8. Buka Global Settings > User > Custom Field
9. Ketik Search `Unknown Field`, tekan Enter
10. Verifikasi empty state `No results found` (tidak ada field `Unknown Field`)
11. Klik icon Changelog
12. Ketik Search `{runId}-074`, tekan Enter
13. Verifikasi anchor Changelog: entri Create seeding `Consumer Probe {runId}-074` tampil
14. Ganti isi kotak search Changelog dengan `Unknown Field`, tekan Enter
15. Verifikasi Changelog tidak memuat entri `Unknown Field` (empty state `No results found`)
16. Klik `[✕]`
17. Buka Global Settings > Import > User Login
18. Klik `[Discard]` pada Unsaved Banner
19. Klik `[Discard Draft]`
20. Verifikasi toast sukses: "Success, draft has been discarded."
21. Verifikasi draft Import dibuang

### TC-GS-UCF-300: Kolom Custom Field aktif ditambahkan dinamis di Staging Table Import User Login

22. Siapkan draft Import User Login sebagai satu-satunya draft aktif dengan 1 baris (disediakan tim FE/BE)
23. Buka Global Settings > Import > User Login
24. Muat ulang halaman (F5)
25. Verifikasi Staging Table memuat kolom `Consumer Probe {runId}-074` pada kolom Custom Fields (User) setelah pemuatan berikutnya (read-time, tanpa push)
26. Klik `[Discard]` pada Unsaved Banner
27. Klik `[Discard Draft]`

### TC-GS-UCF-560: Value Dropdown yang ditambahkan lewat Import tercatat satu entri Edit Value Setting di tiga surface

28. Buka Global Settings > User > Custom Field
29. Klik icon Changelog
30. Ketik Search `Import Log Probe {runId}-074`, tekan Enter
31. Catat jumlah entri Create untuk `Import Log Probe {runId}-074` (baseline BCreate560)
32. Klik `[✕]`
33. Siapkan draft Import User Login (D-256): 1 baris valid dengan `Import Log Probe {runId}-074` = `Malam` berstatus `error` (satu-satunya draft aktif, disediakan tim FE/BE)
34. Buka Global Settings > Import > User Login
35. Pada Error Summary Callout, klik `[Create Missing Options]` untuk kategori `Import Log Probe {runId}-074`
36. Tunggu aksi selesai
37. Buka Global Settings > User > Custom Field
38. Ketik Search `Import Log Probe {runId}-074`, tekan Enter
39. Verifikasi kolom Value Setting baris `Import Log Probe {runId}-074` menampilkan `Pagi`, `Siang`, `Malam`
40. Klik icon Changelog
41. Ketik Search `Import Log Probe {runId}-074`, tekan Enter
42. Verifikasi Changelog: tepat satu entri Action `Edit`
43. Verifikasi entri Edit: Field `Import Log Probe {runId}-074 — Value Setting`, Old Value `Pagi, Siang`, New Value `Pagi, Siang, Malam`, Modified By `Sari D`
44. Verifikasi jumlah entri Create untuk `Import Log Probe {runId}-074` sama dengan BCreate560 (tidak ada entri Create baru)
45. Klik `[✕]`
46. Buka Global Settings > User > Detail Sari Dewi > tab System Log
47. Ketik Search `Import Log Probe {runId}-074`, tekan Enter
48. Verifikasi System Log Sari Dewi: entri Edit yang sama tampil tepat 1 kali dengan Object `Custom Field`, Name `Import Log Probe {runId}-074`
49. Buka Global Settings > Activity Log > tab User Action
50. Ketik Search `Import Log Probe {runId}-074`, tekan Enter
51. Verifikasi Activity Log: entri Edit yang sama tampil tepat 1 kali dengan Modified By `Sari D`
52. Buka Global Settings > Import > User Login
53. Klik `[Discard]` pada Unsaved Banner
54. Klik `[Discard Draft]`

### TC-GS-UCF-561: Value Dropdown dari Import tampil di akhir daftar field dan form User tanpa mengubah nilai User yang ada

55. Siapkan draft Import User Login (D-258): 1 baris valid dengan `Import Sync Probe {runId}-074` = `Blue` berstatus `error` (satu-satunya draft aktif, disediakan tim FE/BE)
56. Buka Global Settings > Import > User Login
57. Pada Error Summary Callout, klik `[Create Missing Options]` untuk kategori `Import Sync Probe {runId}-074`
58. Tunggu aksi selesai
59. Buka Global Settings > User > Custom Field
60. Ketik Search `Import Sync Probe {runId}-074`, tekan Enter
61. Klik `⋯` pada baris `Import Sync Probe {runId}-074`, pilih `Edit`
62. Verifikasi popup Edit menampilkan badge Dropdown Values `Red`, `Green`, `Blue`
63. Verifikasi badge `Blue` berada di akhir
64. Klik `[✕]` pada popup
65. Buka Global Settings > User > Detail Rahmat Hidayat
66. Verifikasi Detail Rahmat Hidayat menampilkan `Import Sync Probe {runId}-074: Green` (nilai User tidak berubah)
67. Buka Global Settings > User > User List (sub-tab Login User)
68. Klik `[+ User]`
69. Buka dropdown `Import Sync Probe {runId}-074`
70. Verifikasi popup Create User menawarkan opsi `Red`, `Green`, dan `Blue`
71. Tutup popup lewat `✕`
72. Buka Global Settings > Import > User Login
73. Klik `[Discard]` pada Unsaved Banner
74. Klik `[Discard Draft]`

### TC-GS-UCF-564: Create Missing Options untuk nama yang sudah ditambahkan admin lain tidak menduplikasi value dan tidak menulis entri log

75. Siapkan draft Import User Login (D-260): 1 baris valid dengan `Import Dup Probe {runId}-074` = `Malam` berstatus `error` (satu-satunya draft aktif, disediakan tim FE/BE)
76. Buka Global Settings > Import > User Login (halaman Admin A; draft terlihat)
77. Admin kedua (Nadia Pratama, sesi API) mengedit `Import Dup Probe {runId}-074` dengan menambah value `malam` (huruf kecil) hingga tersimpan
78. Admin A klik `[Create Missing Options]` untuk kategori `Import Dup Probe {runId}-074` pada halaman yang belum dimuat ulang
79. Tunggu aksi selesai
80. Buka Global Settings > User > Custom Field
81. Ketik Search `Import Dup Probe {runId}-074`, tekan Enter
82. Verifikasi kolom Value Setting baris `Import Dup Probe {runId}-074` menampilkan `Pagi`, `Siang`, `malam`
83. Verifikasi kolom Value Setting tidak memuat duplikat `Malam`
84. Klik icon Changelog
85. Ketik Search `Import Dup Probe {runId}-074`, tekan Enter
86. Verifikasi Changelog: tepat satu entri Edit `Import Dup Probe {runId}-074 — Value Setting` (Old Value `Pagi, Siang`; New Value `Pagi, Siang, malam`) dengan Modified By `Nadia P`
87. Klik `[✕]`
88. Buka Global Settings > Import > User Login (pembacaan Staging Table berikutnya)
89. Verifikasi baris draft pulih ke `pending` karena nilai `Malam` cocok dengan opsi `malam` tanpa beda huruf besar-kecil
90. Klik `[Discard]` pada Unsaved Banner
91. Klik `[Discard Draft]`

### TC-GS-UCF-565: Create Missing Options untuk field yang dinonaktifkan admin lain dilewati tanpa menulis value atau entri log

92. Siapkan draft Import User Login (D-261): 1 baris valid dengan `Import Skip Probe {runId}-074` = `Malam` berstatus `error` (satu-satunya draft aktif, disediakan tim FE/BE)
93. Buka Global Settings > Import > User Login (halaman Admin A; draft terlihat)
94. Admin kedua (Nadia Pratama, sesi API) menonaktifkan `Import Skip Probe {runId}-074` hingga tersimpan
95. Admin A klik `[Create Missing Options]` untuk kategori `Import Skip Probe {runId}-074` pada halaman yang belum dimuat ulang
96. Tunggu aksi selesai
97. Buka Global Settings > User > Custom Field
98. Ketik Search `Import Skip Probe {runId}-074`, tekan Enter
99. Verifikasi baris `Import Skip Probe {runId}-074` berstatus Inactive
100. Verifikasi kolom Value Setting baris `Import Skip Probe {runId}-074` tetap menampilkan `Pagi`, `Siang` tanpa `Malam`
101. Klik icon Changelog
102. Ketik Search `Import Skip Probe {runId}-074`, tekan Enter
103. Verifikasi Changelog: tepat satu entri Deactivate `Import Skip Probe {runId}-074 — Status` dengan Modified By `Nadia P`
104. Verifikasi Changelog: tidak ada entri Edit `Value Setting` untuk `Import Skip Probe {runId}-074`
105. Klik `[✕]`
106. Buka Global Settings > Import > User Login
107. Klik `[Discard]` pada Unsaved Banner
108. Klik `[Discard Draft]`

### TC-GS-UCF-562 bagian pertama: Pemegang Import data Create menambah value lewat Import, tab Custom Field Hidden

109. Ganti akun: logout dari Total Control Client A Sari Dewi
110. Login sebagai Import data: Create dan Read Rina Marlina (`importCreate_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_IMPORTCREATE_PASSWORD`)
111. Siapkan draft Import User Login (D-259): 1 baris valid dengan `Import Cap Probe {runId}-074` = `Malam` berstatus `error` (satu-satunya draft aktif, disediakan tim FE/BE)
112. Buka Global Settings > User
113. Verifikasi halaman Global Settings > User termuat (pembanding)
114. Verifikasi tab `Custom Field` tidak tampil bagi Rina Marlina
115. Buka Global Settings > Import > User Login
116. Pada Error Summary Callout, klik `[Create Missing Options]` untuk kategori `Import Cap Probe {runId}-074`
117. Verifikasi permintaan `[Create Missing Options]` sukses (tanpa penolakan `403`)
118. Buka Global Settings > Import > User Login (pembacaan Staging Table berikutnya)
119. Verifikasi baris draft pulih ke `pending`
120. Klik `[Discard]` pada Unsaved Banner
121. Klik `[Discard Draft]`

### TC-GS-UCF-562 bagian kedua: pengamatan Total Control

122. Ganti akun: logout dari Import data: Create dan Read Rina Marlina
123. Login sebagai Total Control Client A Sari Dewi (`Spectra.env.GS_TC_PASSWORD`)
124. Buka Global Settings > User > Custom Field
125. Ketik Search `Import Cap Probe {runId}-074`, tekan Enter
126. Verifikasi kolom Value Setting baris `Import Cap Probe {runId}-074` menampilkan `Pagi`, `Siang`, `Malam`
127. Verifikasi `Malam` berada di akhir
128. Klik icon Changelog
129. Ketik Search `Import Cap Probe {runId}-074`, tekan Enter
130. Verifikasi Changelog: tepat satu entri Edit `Import Cap Probe {runId}-074 — Value Setting` (Old Value `Pagi, Siang`; New Value `Pagi, Siang, Malam`) dengan Modified By `Rina M`
131. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-GS-UCF-562 dibagi dua subjudul: bagian pertama sebagai Rina Marlina, bagian kedua (pengamatan) sebagai Total Control sesudah ganti akun.
- Urutan TC dalam spec: 536, 300, 560, 561, 564, 565, 562 (bagian pertama), lalu pengamatan Total Control. Urutan menyimpang dari urutan TC sumber: TC-GS-UCF-536 lebih dulu karena mensyaratkan tidak ada draft aktif; TC-GS-UCF-300 dan TC-GS-UCF-560 sampai 565 berikutnya menyiapkan draft masing-masing dan membuangnya di akhir; akun Rina Marlina (TC-GS-UCF-562) di akhir karena ganti akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): pindah halaman, pengisian Search, pencatatan BCreate560, penyiapan draft Import (disediakan tim FE/BE), membuang draft Import lewat `[Discard]` dan `[Discard Draft]`, penutupan Modal Changelog dan popup Edit lewat `[✕]` (popup tidak dirty sehingga tanpa dialog), penutupan popup Create User lewat `✕`, ganti akun, dan "Tunggu aksi selesai" sesudah `[Create Missing Options]` yang hasilnya tidak diasersi langsung dan langkah berikutnya berpindah surface (bagian 8b butir 8). Pada TC-GS-UCF-536 langkah buang draft diasersi (Expected e) sehingga tanpa langkah penghubung. Langkah 3 dan 13 bukan Expected TC: pembanding/anchor sebelum asersi universal atau absence (bagian 8b butir 2, S-03); langkah 13 adalah anchor positif sebelum langkah 15.
- TC-GS-UCF-564 dan 565 berstatus Manual Only di TC (dua sesi paralel); admin kedua memakai sesi API karena hanya memicu (P-2); langkahnya ditulis "hingga ... tersimpan". TC-GS-UCF-563 (defense-in-depth kelas a) dipindah ke spec 012 (keputusan K-8 A, 2026-10-29) dan tidak lagi ada di spec ini; seluruh TC di spec ini kelas d (Import).
- Spec melewati sekitar 35 langkah (131 langkah). Seluruhnya satu kelas d (draft Import User Login dan dampaknya pada definisi Custom Field); tiap blok TC menyiapkan draft dan fieldnya sendiri sehingga tetap bermakna bila blok lain gagal. Ganti akun memakai langkah eksplisit dan bagian sesudahnya (pengamatan Total Control) tetap bermakna.
- Draft Import hanya boleh satu aktif (`IMP-LOGIC-02`); karena itu tiap TC membuang draft di akhirnya dan hook `after` membuang sisa draft.
- Pembagian TC lintas spec: konsumen Staging Table Import untuk TC lain ada di `tc-import.md` (modul Import); pemicu `[Create Missing Options]` dan tampilan halaman Import dimiliki `global-settings/import/TestCases/tc-import.md`, sedangkan spec ini hanya mengasersi sisi pemilik definisi (value, log, permission).
- P-1 (state berat): asersi absence pada langkah 15 (TC-GS-UCF-536: tidak ada entri `Unknown Field`) dan langkah 104 (TC-GS-UCF-565: tidak ada entri Edit `Value Setting`) berada di spec ini karena bergantung pada draft Import yang menjadi satu-satunya draft aktif dan, untuk TC-GS-UCF-565, pada perubahan sesi API Admin kedua di antara dua langkah Admin A yang tidak dapat diulang murah di spec absence 070. Keduanya punya baseline dan anchor positif di surface yang sama (langkah 13 untuk Changelog `Unknown Field`; langkah 103 untuk Changelog `Import Skip Probe`). Absence "tidak ada entri Edit dengan Modified By `Sari D`" TC-GS-UCF-564 tidak diasersi terpisah: langkah 86 sudah mengasersi tepat satu entri Edit (Modified By `Nadia P`), yang mencakup klausa itu (asersi jumlah, S-12). Keputusan K-7 A.
- Temuan untuk QA:
  - TC-GS-UCF-560 sampai 565 mensyaratkan draft Import User Login (D-256, D-258, sampai D-261) tanpa menyebut cara membentuknya; spec menyatakannya sebagai disediakan tim FE/BE.
  - TC-GS-UCF-560 Expected b menyatakan "tidak ada entri Create"; seeding field Dropdown lewat API menghasilkan entri Create yang sama di Changelog. Spec mengasersi bahwa jumlah entri Create tidak bertambah dibanding baseline (BCreate560), bukan nol. Bila fixture D-255 dibuat langsung di backend tanpa entri Create, baseline bernilai nol dan asersi tetap sah.
  - TC-GS-UCF-562 Expected a menyebut "tab `Custom Field` tidak tampil" tanpa menyebut sub-tab lain yang tampil bagi Rina Marlina; spec memakai halaman Global Settings > User yang termuat sebagai pembanding. Expected b menyebut "permintaan sukses (tanpa penolakan `403`)" tanpa menyebut pemantauan jaringan; spec menyatakan kemampuan itu di Prerequisites.
  - TC-GS-UCF-562 Expected b dan TC-GS-UCF-564 Expected d menyebut "pembacaan Staging Table berikutnya" tanpa langkah yang membukanya; spec menambahkan langkah membuka ulang Import > User Login sebagai langkah observasi.
  - Pre-setup TC memuat dua akun bernama tampil Rina Marlina (Manage user and role: Create dan Read, dan Import data: Create dan Read); spec membedakannya lewat email.
  - TC-GS-UCF-536 Expected c dan d menyebut "jumlah baris" dan "jumlah entri" sama dengan langkah 1. Tabel dan Changelog dipaginasi (ukuran halaman bawaan 10; Client A sedikitnya 14 field dan 16 entri), sehingga hitungan dari satu halaman tidak mendeteksi field atau entri baru. Spec mengganti pembanding jumlah dengan Search berbaseline: Search `Unknown Field` pada tabel (empty state) dan pada Changelog (anchor positif lewat Search `{runId}-074`, lalu empty state `Unknown Field`). Ini hanya membuktikan tidak ada field atau entri bernama `Unknown Field`; field lain dengan nama berbeda tidak terdeteksi. Bila UI menampilkan total pada label Pagination (belum terbukti), QA dapat memulihkan perbandingan jumlah.
  - TC-GS-UCF-536 menyebut atribut target `Unknown Field` tanpa menyebut atribut lain yang menjadi pembanding; spec memakai `Email` sebagai pembanding.
  - Post Condition tiap TC ("draft Import dibuang") tidak punya langkah observasi di TC selain TC-GS-UCF-536; spec membuang draft sebagai langkah penghubung tanpa `Verifikasi`.
