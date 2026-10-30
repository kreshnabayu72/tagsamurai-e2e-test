---
id: TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log
title: "Pencatatan Create, Edit, Delete, Bulk Delete Campuran, Snapshot Rename, Kapitalisasi, Create Missing Positions, Field, dan Position Name pada Changelog dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-242
  - TC-GS-POS-243
  - TC-GS-POS-244
  - TC-GS-POS-245
  - TC-GS-POS-247
  - TC-GS-POS-248
  - TC-GS-POS-250
  - TC-GS-POS-252
  - TC-GS-POS-253
coverage:
  web: automated
---

# Pencatatan Create, Edit, Delete, Bulk Delete Campuran, Snapshot Rename, Kapitalisasi, Create Missing Positions, Field, dan Position Name pada Changelog dan Activity Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Langkah yang membuka ulang halaman itu (17, 32, 38, 54, 72, 91, 105) berfungsi sebagai pemulihan state: sesudah Activity Log atau Import, atau untuk mereset Search tabel (klik sidebar mereset Search, Sort, dan Filter).
- Data Pre-setup: tidak ada yang dipakai (seluruh target aksi tulis dan hapus adalah data milik spec).
- Data Dinamis (nama bersuffix per run):
  - Di-seed lewat API di hook `before` oleh Budi Santoso pada entitas Total Control (fixture baru `Fixture.position.logSeed044`): Position `Office Administrator {runId}-044` (TC-GS-POS-247), `Data Engineer {runId}-044` (TC-GS-POS-248), `Compliance Officer {runId}-044` dan `Tax Specialist {runId}-044` (bebas relasi, TC-GS-POS-245), serta `Warehouse Supervisor {runId}-044` yang dipakai user Login aktif milik spec `inuse+{runId}-044@qwertysystem.net` (fixture baru `Fixture.position.userInUse044`; mekanisme seeding user disediakan tim FE/BE) sebagai Position in-use pada TC-GS-POS-245.
  - Dibuat dan diubah lewat UI oleh spec: `Risk Manager {runId}-044` (Create, TC-GS-POS-242), diubah menjadi `Risk Director {runId}-044` (TC-GS-POS-243), lalu dihapus (TC-GS-POS-244); `Office Administrator {runId}-044` diubah menjadi `Office Coordinator {runId}-044` lalu `Office Manager {runId}-044` (TC-GS-POS-247); `Data Engineer {runId}-044` diubah menjadi `Data engineer {runId}-044` (TC-GS-POS-248).
  - Dibuat lewat Import: `Site Engineer {runId}-044` dari tombol `[Create Missing Positions]` pada Import Type "User Login" (TC-GS-POS-250); berkas CSV User Login satu baris data dengan Position `Site Engineer {runId}-044` disediakan sebagai fixture berkas baru `Fixture.position.createMissingCsv044` oleh tim FE (pola berkas User Login standar pada `tc-import.md`).
  - Entri Changelog dan Activity Log bersifat audit trail permanen dan tidak dibersihkan.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user `inuse+{runId}-044@qwertysystem.net`, lalu hapus lewat API semua Position bersuffix `{runId}-044` yang masih ada (`Office Manager`, `Data engineer`, `Site Engineer`, `Warehouse Supervisor`, dan sisa lainnya); reset draft Import User Login pada entitas Total Control (hapus semua baris draft hasil TC-GS-POS-250).
- Kondisi awal Import: hook `before` juga mereset draft Import User Login pada entitas Total Control (tanpa baris draft sebelum langkah 65), karena TC-GS-POS-250 meminjam kondisi fixture direset dari `tc-import.md` (TC-GS-IMPORT-328); hook `after` mengulang reset yang sama sebagai cadangan.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: seeding Position dan user lewat API; pencatatan penanda waktu T1 (jam browser) sesudah Submit pada TC-GS-POS-242 dan perbandingannya dengan kolom Date entri log (berketelitian menit) dalam format General Settings (Pre-setup 22); jam server dan jam browser sinkron; upload berkas lewat file picker pada Import; pencarian entri di Popup Changelog (Search) dan di Activity Log.
- State global: tidak ada yang diubah selain flag Guided Tooltip dan draft Import User Login (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-242: Entri Create Position pada Changelog dan Activity Log

1. Klik `[+ Position]`
2. Ketik `Risk Manager {runId}-044` pada Position Name
3. Klik `[Submit]`
4. Tunggu aksi selesai (modal tertutup)
5. Catat penanda waktu T1 (jam browser) sesudah Submit
6. Klik ikon Changelog
7. Ketik `Risk Manager {runId}-044` pada Search Popup Changelog, tekan Enter
8. Verifikasi tepat 1 entri untuk Position `Risk Manager {runId}-044`
9. Verifikasi Date entri sesuai waktu Submit (T1) dengan toleransi satu menit
10. Verifikasi Action `Create` ditampilkan sebagai teks polos
11. Verifikasi entri: Position Name `Risk Manager {runId}-044`, Old Value `—`, New Value `Risk Manager {runId}-044`, Modified By `Budi S`, Field `Position Name`
12. Tutup Popup Changelog dengan klik `✕` di header
13. Buka Global Settings > Activity Log
14. Cari entri Object `Position` Name `Risk Manager {runId}-044`
15. Verifikasi tepat 1 entri untuk Position `Risk Manager {runId}-044`
16. Verifikasi entri: Action `Create`, Object `Position`, Name `Risk Manager {runId}-044`, Old Value `—`, New Value `Risk Manager {runId}-044`, Modified By `Budi S`

### TC-GS-POS-243: Entri Edit Position pada Changelog dan Activity Log

17. Buka Global Settings > User > Position
18. Ketik `{runId}-044` pada Search tabel, tekan Enter
19. Klik `⋯` pada baris `Risk Manager {runId}-044`, pilih `Edit`
20. Ganti nilai Position Name menjadi `Risk Director {runId}-044`
21. Klik `[Save]`
22. Tunggu aksi selesai (modal tertutup)
23. Klik ikon Changelog
24. Ketik `Risk Director {runId}-044` pada Search Popup Changelog, tekan Enter
25. Verifikasi tepat 1 entri dengan Action `Edit`
26. Verifikasi entri Edit: Old Value `Risk Manager {runId}-044`, New Value `Risk Director {runId}-044`, Modified By `Budi S`, Position Name `Risk Director {runId}-044`, Field `Position Name`
27. Tutup Popup Changelog dengan klik `✕` di header
28. Buka Global Settings > Activity Log
29. Cari entri Object `Position` Name `Risk Director {runId}-044`
30. Verifikasi tepat 1 entri dengan Action `Edit`
31. Verifikasi entri Edit: Object `Position`, Old Value `Risk Manager {runId}-044`, New Value `Risk Director {runId}-044`

### TC-GS-POS-253: Isi kolom Position Name pada entri Edit

32. Buka Global Settings > User > Position
33. Klik ikon Changelog
34. Ketik `Risk Director {runId}-044` pada Search Popup Changelog, tekan Enter
35. Verifikasi kolom Position Name entri Edit menampilkan nama sesudah perubahan `Risk Director {runId}-044`
36. Verifikasi nama lama `Risk Manager {runId}-044` hanya tampil di Old Value entri Edit, tidak di kolom Position Name
37. Tutup Popup Changelog dengan klik `✕` di header

### TC-GS-POS-247: Snapshot entri Changelog tidak berubah setelah rename kedua

38. Buka Global Settings > User > Position
39. Ketik `{runId}-044` pada Search tabel, tekan Enter
40. Klik `⋯` pada baris `Office Administrator {runId}-044`, pilih `Edit`
41. Ganti nilai Position Name menjadi `Office Coordinator {runId}-044`
42. Klik `[Save]`
43. Klik `⋯` pada baris `Office Coordinator {runId}-044`, pilih `Edit`
44. Ganti nilai Position Name menjadi `Office Manager {runId}-044`
45. Klik `[Save]`
46. Tunggu aksi selesai (modal tertutup)
47. Klik ikon Changelog
48. Ketik `Office Administrator {runId}-044` pada Search Popup Changelog, tekan Enter
49. Verifikasi entri Edit pertama tetap Old Value `Office Administrator {runId}-044` dan New Value `Office Coordinator {runId}-044`
50. Verifikasi entri Create awal tetap New Value `Office Administrator {runId}-044`
51. Ganti isi kotak search Popup Changelog dengan `Office Coordinator {runId}-044`, tekan Enter
52. Verifikasi entri Edit kedua Old Value `Office Coordinator {runId}-044` dan New Value `Office Manager {runId}-044`
53. Tutup Popup Changelog dengan klik `✕` di header

### TC-GS-POS-248: Perubahan kapitalisasi tercatat sebagai Edit

54. Buka Global Settings > User > Position
55. Ketik `{runId}-044` pada Search tabel, tekan Enter
56. Klik `⋯` pada baris `Data Engineer {runId}-044`, pilih `Edit`
57. Ganti nilai Position Name menjadi `Data engineer {runId}-044`
58. Klik `[Save]`
59. Tunggu aksi selesai (modal tertutup)
60. Klik ikon Changelog
61. Ketik `Data engineer {runId}-044` pada Search Popup Changelog, tekan Enter
62. Verifikasi tepat 1 entri dengan Action `Edit`
63. Verifikasi entri Edit: Old Value `Data Engineer {runId}-044` dan New Value `Data engineer {runId}-044`
64. Tutup Popup Changelog dengan klik `✕` di header

### TC-GS-POS-250: Position dari Create Missing Positions tercatat sebagai Create biasa

65. Buka Import dari sidebar
66. Buka Import > User Login
67. Klik `[Upload File]`
68. Pilih berkas CSV User Login (`Fixture.position.createMissingCsv044`) di file picker
69. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
70. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
71. Tunggu aksi selesai
72. Buka Global Settings > User > Position
73. Klik ikon Changelog
74. Ketik `Site Engineer {runId}-044` pada Search Popup Changelog, tekan Enter
75. Verifikasi tepat 1 entri dengan Action `Create`
76. Verifikasi entri: Position Name `Site Engineer {runId}-044`, Old Value `—`, New Value `Site Engineer {runId}-044`, Modified By `Budi S`
77. Tutup Popup Changelog dengan klik `✕` di header

### TC-GS-POS-244: Entri Delete Position pada Changelog dan Activity Log

78. Ketik `{runId}-044` pada Search tabel, tekan Enter
79. Klik `⋯` pada baris `Risk Director {runId}-044`, pilih `Delete`
80. Klik `[Delete]` pada dialog konfirmasi
81. Tunggu aksi selesai (dialog tertutup)
82. Klik ikon Changelog
83. Ketik `Risk Director {runId}-044` pada Search Popup Changelog, tekan Enter
84. Verifikasi tepat 1 entri dengan Action `Delete`
85. Verifikasi entri Delete: Position Name `Risk Director {runId}-044`, Old Value `Risk Director {runId}-044`, New Value `—`, Field `Position Name`
86. Tutup Popup Changelog dengan klik `✕` di header
87. Buka Global Settings > Activity Log
88. Cari entri Object `Position` Name `Risk Director {runId}-044`
89. Verifikasi tepat 1 entri dengan Action `Delete`
90. Verifikasi entri Delete: Object `Position`, Name `Risk Director {runId}-044`

### TC-GS-POS-252: Nilai kolom Field pada entri log Position

91. Buka Global Settings > User > Position
92. Klik ikon Changelog
93. Ketik `Risk Manager {runId}-044` pada Search Popup Changelog, tekan Enter
94. Verifikasi kolom Field entri Create `Risk Manager {runId}-044` di Changelog = `Position Name`
95. Ganti isi kotak search Popup Changelog dengan `Risk Director {runId}-044`, tekan Enter
96. Verifikasi kolom Field entri Edit `Risk Director {runId}-044` di Changelog = `Position Name`
97. Verifikasi kolom Field entri Delete `Risk Director {runId}-044` di Changelog = `Position Name`
98. Tutup Popup Changelog dengan klik `✕` di header
99. Buka Global Settings > Activity Log
100. Cari entri Object `Position` Name `Risk Manager {runId}-044`
101. Verifikasi kolom Field entri Create di Activity Log = `Position Name`
102. Cari entri Object `Position` Name `Risk Director {runId}-044`
103. Verifikasi kolom Field entri Edit di Activity Log = `Position Name`
104. Verifikasi kolom Field entri Delete di Activity Log = `Position Name`

### TC-GS-POS-245: Bulk Delete campuran mencatat hanya item yang terhapus

105. Buka Global Settings > User > Position
106. Ketik `{runId}-044` pada Search tabel, tekan Enter
107. Centang baris `Compliance Officer {runId}-044`
108. Centang baris `Tax Specialist {runId}-044`
109. Centang baris `Warehouse Supervisor {runId}-044`
110. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
111. Klik `[Continue]`
112. Tunggu aksi selesai (dialog tertutup)
113. Klik ikon Changelog
114. Klik ikon Filter
115. Pilih `Delete` pada dropdown `Action`
116. Klik `[Apply]`
117. Ketik `Compliance Officer {runId}-044` pada Search Popup Changelog, tekan Enter
118. Verifikasi anchor Changelog: tepat 1 entri Delete untuk `Compliance Officer {runId}-044`
119. Ganti isi kotak search Popup Changelog dengan `Tax Specialist {runId}-044`, tekan Enter
120. Verifikasi anchor Changelog: tepat 1 entri Delete untuk `Tax Specialist {runId}-044`
121. Ganti isi kotak search Popup Changelog dengan `Warehouse Supervisor {runId}-044`, tekan Enter
122. Verifikasi tidak ada entri Delete untuk `Warehouse Supervisor {runId}-044`
123. Tutup Popup Changelog dengan klik `✕` di header
124. Buka Global Settings > Activity Log
125. Cari entri Object `Position` Name `Compliance Officer {runId}-044`
126. Verifikasi anchor Activity Log: tepat 1 entri dengan Action `Delete`
127. Cari entri Object `Position` Name `Tax Specialist {runId}-044`
128. Verifikasi anchor Activity Log: tepat 1 entri dengan Action `Delete`
129. Cari entri Object `Position` Name `Warehouse Supervisor {runId}-044`
130. Verifikasi tidak ada entri dengan Action `Delete` untuk `Warehouse Supervisor {runId}-044`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 242, 243, 253, 247, 248, 250, 244, 252, 245. Urutan ini menyimpang dari urutan TC sumber: TC-GS-POS-242, 243, dan 244 membentuk satu rantai (Create, Edit, Delete `Risk Manager`) dengan TC-GS-POS-253 sesudah Edit dan TC-GS-POS-252 sesudah Delete (karena butuh entri Create, Edit, dan Delete); TC-GS-POS-245 menghapus data sehingga ditaruh paling akhir (prinsip 5). Form Create dibuka sekali (langkah 1) dan ditutup oleh Submit sukses; form Edit dibuka empat kali (langkah 19, 40, 43, 56) dan masing-masing ditutup oleh Save sukses.
- Layar awal Global Settings > User > Position dibuka hook `beforeEach` dan dipakai TC-GS-POS-242; TC lain membuka ulang halaman (langkah 17, 32, 38, 54, 72, 91, 105) karena langkah sebelum itu berada di Activity Log atau Import atau untuk mereset Search tabel.
- Langkah "Tunggu aksi selesai" (langkah 4, 22, 46, 59, 71, 81, 112) ditulis tanpa `Verifikasi` sesudah `[Submit]`, `[Save]`, `[Create Missing Positions]`, `[Delete]`, atau `[Continue]` yang hasilnya tidak diasersi langsung (TC tanpa toast) dan langkah berikutnya pindah surface (konvensi bagian 8b butir 8): langkah 4, 22, 46, dan 59 mendahului pembukaan Popup Changelog; langkah 71 mendahului pembukaan Global Settings > User > Position sesudah `[Create Missing Positions]`; langkah 81 dan 112 mendahului pembukaan Popup Changelog sesudah `[Delete]` dan `[Continue]`. Langkah 4 sekaligus menjamin T1 dicatat sesudah aksi selesai. `[Save]` pada langkah 42 tidak diikuti langkah ini karena langkah berikutnya bekerja di tabel yang sama; `[Confirm Mapping]` pada langkah 69 tidak diikuti langkah ini karena langkah berikutnya bekerja di Error Summary Callout pada halaman yang sama. Langkah ini juga dihitung sebagai langkah penghubung.
- Langkah penghubung (aksi tanpa `Verifikasi`): pengisian Search tabel (langkah 18, 39, 55, 78, 106) untuk mempersempit tabel ke Position milik spec, pencatatan penanda waktu T1 (langkah 5), penutupan Popup Changelog (langkah 12, 27, 37, 53, 64, 77, 86, 98, 123), pemilihan Filter `Delete` pada Popup Changelog (langkah 114 sampai 116), pencarian di Popup Changelog serta Activity Log, dan langkah "Tunggu aksi selesai" (langkah 4, 22, 46, 59, 71, 81, 112).
- Asersi "tepat N entri" memakai nama Position bersuffix `-044` yang unik per run sebagai baseline nol (S-12), bukan anchor baris seed dan bukan penanda waktu; TC menyebut baseline jumlah entri sebelum aksi, dan nama unik per run membuat hitungan entri untuk nama itu bernilai nol sebelum aksi. Search `Risk Manager`, `Risk Director`, `Office Administrator`, dan `Office Coordinator` dapat menampilkan beberapa entri (Create, Edit, Delete) untuk nama yang sama, sehingga asersi "tepat 1" menyebut Action-nya. Penanda waktu hanya T1 (langkah 5, diambil sesudah Submit) untuk "Date sesuai waktu Submit" dengan toleransi satu menit karena kolom Date log berketelitian menit.
- TC-GS-POS-245 Expected "tidak ada entri `Warehouse Supervisor`" diasersi di spec ini (P-1: konteks campuran terhapus dan terblokir dibangun oleh bulk delete pada langkah 110 sampai 111 dan tidak dapat diulang tanpa biaya besar). Asersi memakai nama bersuffix unik (baseline nol) dan anchor positif (kedua entri Delete yang terhapus, langkah 118 dan 120 di Changelog serta 126 dan 128 di Activity Log, pada surface yang sama dengan asersi absence). Asersi absence log untuk TC-GS-POS-246 dan 308 (Edit No-Op) ada di spec 046; TC-GS-POS-249 (Position hasil Import tidak tercatat di Changelog) hanya di spec 046; System Log aktor (TC-GS-POS-251, 305, 306, 307) ada di spec 045.
- Spec melewati sekitar 35 langkah (130 langkah, sebagian besar blok baca-log berpola: buka surface, cari entri, lalu `Verifikasi` kolom log). Seluruhnya satu kelas (pencatatan Changelog dan Activity Log, satu akun), tiap blok TC memakai Position bersuffix sendiri dan tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - Mekanisme pencarian entri di Activity Log ("cari entri Object `Position` Name ...") dan kolom yang dicakup Search Popup Changelog tidak dijelaskan di TC; spec memakai Search Popup Changelog dan pencarian Activity Log berdasarkan nama.
  - TC-GS-POS-242 sampai 244 tidak menyebut toast hasil aksi (Create, Edit, Delete); spec tidak mengasersi toast di spec ini. TC-GS-POS-245 tidak menyebut toast hasil Bulk Delete campuran (NC-07 menetapkan "Success, position has been deleted. Some items were skipped."); spec tidak mengasersinya di sini.
  - TC-GS-POS-245 precondition memakai `Warehouse Supervisor` Pre-setup 12 yang dipakai user `Rina Wulandari`; spec memakai Position `Warehouse Supervisor {runId}-044` milik spec dan user Login aktif milik spec agar tidak menyentuh data Pre-setup bersama (S-06). TC tidak mendefinisikan field user yang di-seed. TC-GS-POS-245 juga mengacu TC-GS-POS-65 dan 66 sebagai pembuatan `Compliance Officer` dan `Tax Specialist`; spec men-seed keduanya lewat API.
  - TC-GS-POS-245 menyebut `[Continue]` tanpa menyebut dialog yang memuatnya; spec mengikuti TC. TC-GS-POS-242 sampai 245 tidak menyebut apakah Search dan Filter Popup Changelog kosong dan bersih saat Popup dibuka ulang sesudah ditutup; spec menganggap keduanya bersih pada setiap pembukaan baru.
  - TC-GS-POS-247 mengharuskan entri Create awal `Office Administrator` ada; spec men-seed Position lewat API dan mengasumsikan seeding API menulis entri Create ke Changelog yang sama dengan Create lewat UI.
  - TC-GS-POS-248 bergantung pada TC-GS-POS-90 (edit kapitalisasi); langkah Edit disalin ke spec. Pencarian `Data engineer` bersifat case-insensitive sehingga entri Create `Data Engineer` ikut tampil; spec mengasersi tepat 1 entri dengan Action `Edit`.
  - TC-GS-POS-250 berstatus Manual Only di TC tetapi tetap ditulis (konvensi bagian 2). Langkah impor disalin dari pola `tc-import.md` (TC-GS-IMPORT-324 dan 328); berkas CSV dan Division yang valid untuk entitas Total Control tidak ditentukan oleh TC-GS-POS-250.
  - TC-GS-POS-252 precondition merujuk "TC Section 5" tanpa menyebut entri mana; spec memakai entri Create, Edit, dan Delete `Risk Manager`/`Risk Director` milik spec ini.
  - TC-GS-POS-253 precondition bergantung pada TC-GS-POS-243; langkah Edit disalin ke spec.
