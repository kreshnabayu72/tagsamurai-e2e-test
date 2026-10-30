---
id: TC-GS-UCF-E2E-070-absence-log-no-op-gagal-dan-item-dilewati
title: "Tidak Ada Pencatatan Log untuk Edit No-Op, Kapitalisasi dan Spasi Tepi, Aksi Gagal atau Dibatalkan, dan Item yang Dilewati pada Bulk Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-284
  - TC-GS-UCF-533
  - TC-GS-UCF-291
  - TC-GS-UCF-288
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log untuk Edit No-Op, Kapitalisasi dan Spasi Tepi, Aksi Gagal atau Dibatalkan, dan Item yang Dilewati pada Bulk Delete

## Prerequisites

- Mode: FE+BE (backend nyata; intercept jaringan parsial di atas backend nyata untuk TC-GS-UCF-291 hanya sebagai pemicu kegagalan, P-5).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Seluruh aksi UI dan seeding Custom Field spec ini dilakukan Sari Dewi, sehingga entri System Log berada di Detail Sari Dewi. Password tidak ditulis di spec atau fixture.
- Pelaku kedua (TC-GS-UCF-288): Total Control Client A Admin kedua Nadia Pratama (Modified By `Nadia P`) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), hanya memicu penghapusan `Log Skip B {runId}-070` lewat sesi API (P-2) dengan `Spectra.env.GS_TC2_PASSWORD`; mekanisme sesi API disediakan tim FE/BE. Spec tidak membuka sesi UI kedua.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field. Langkah yang membuka ulang halaman itu berfungsi sebagai pemulihan state sesudah System Log atau Activity Log.
- Data Pre-setup (baca-saja): Custom Field `Employee Grade` (Text, Pre-setup Client A, Active, Required No, Placeholder kosong) menjadi target aksi No-Op pada TC-GS-UCF-284 dan 533; nilainya tidak diubah dan Last Updated-nya tidak berubah (S-06). Changelog Pre-setup memuat entri Activate `Employee Grade`.
- Data Dinamis (nama bersuffix `{runId}-070`; fixture baru `Fixture.customFieldUser.logAbsence070`): di-seed lewat API oleh Sari Dewi di hook `before` (seeding menghasilkan satu entri Create per field di tiga surface; entri ini menjadi baseline dan anchor positif): `Log Keep Probe {runId}-070` dan `Log Fail Del Probe {runId}-070` (Text, bebas nilai User; TC-GS-UCF-291), serta `Log Skip A {runId}-070`, `Log Skip B {runId}-070`, dan `Log Skip C {runId}-070` (Text; TC-GS-UCF-288). Dibuat lewat UI tetapi gagal: `Log Fail Probe {runId}-070` (TC-GS-UCF-291, tidak boleh tersimpan).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Custom Field bersuffix `{runId}-070` yang masih ada (`Log Keep Probe`, `Log Fail Del Probe`, `Log Fail Probe` bila tersimpan); lepas semua intercept.
- Kemampuan teknis: intercept jaringan memaksa respons 500 pada `POST /v2/iam/user-custom-fields` (Create) dan `DELETE /v2/iam/user-custom-fields` (Delete), keduanya dilepas segera sesudah pemicu selesai (S-09); sesi API Nadia Pratama; Search pada Modal Changelog, tab System Log di Detail User, dan Activity Log tab User Action (kolom pencarian tidak dijelaskan di TC; lihat Temuan untuk QA).
- Setup Column Modal Changelog: konfigurasi default; hook `beforeEach` membersihkan cache browser.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- State global: tidak ada yang diubah selain flag Guided Tooltip dan intercept (dilepas seperti di atas).

## Test Steps

### TC-GS-UCF-284: Edit No-Op tanpa perubahan tidak menghasilkan entri di tiga surface

1. Klik icon Changelog
2. Ketik Search `Employee Grade`, tekan Enter
3. Catat jumlah entri `Employee Grade` pada Changelog (baseline BC)
4. Klik `[✕]`
5. Buka Global Settings > User > Detail Sari Dewi > tab System Log
6. Ketik Search `Employee Grade`, tekan Enter
7. Catat jumlah entri `Employee Grade` pada System Log Sari Dewi (baseline BS)
8. Buka Global Settings > Activity Log > tab User Action
9. Ketik Search `Employee Grade`, tekan Enter
10. Catat jumlah entri `Employee Grade` pada Activity Log (baseline BA)
11. Buka Global Settings > User > Custom Field
12. Ketik Search `Employee Grade` pada tabel utama, tekan Enter
13. Klik `⋯` pada baris `Employee Grade`, pilih `Edit`
14. Klik `[Save]` tanpa mengubah apa pun
15. Verifikasi toast netral (Info): "No changes to save."
16. Verifikasi popup tertutup
17. Klik icon Changelog
18. Ketik Search `Employee Grade`, tekan Enter
19. Verifikasi anchor Changelog: entri Activate `Employee Grade — Status` Pre-setup tampil
20. Verifikasi jumlah entri `Employee Grade` pada Changelog sama dengan BC
21. Klik `[✕]`
22. Buka Global Settings > User > Detail Sari Dewi > tab System Log
23. Ketik Search `{runId}-070`, tekan Enter
24. Verifikasi anchor System Log Sari Dewi: entri Create seeding milik spec ini tampil
25. Ganti isi kotak search dengan `Employee Grade`, tekan Enter
26. Verifikasi jumlah entri `Employee Grade` pada System Log Sari Dewi sama dengan BS
27. Buka Global Settings > Activity Log > tab User Action
28. Ketik Search `{runId}-070`, tekan Enter
29. Verifikasi anchor Activity Log: entri Create seeding milik spec ini (Modified By `Sari D`) tampil
30. Ganti isi kotak search dengan `Employee Grade`, tekan Enter
31. Verifikasi jumlah entri `Employee Grade` pada Activity Log sama dengan BA
32. Buka Global Settings > User > Custom Field

### TC-GS-UCF-533: Edit No-Op yang hanya mengubah kapitalisasi atau spasi tepi Field Name

33. Catat baseline kedua jumlah entri `Employee Grade` pada ketiga surface: memakai hitungan BC, BS, dan BA yang diverifikasi pada blok TC-GS-UCF-284 (tidak ada aksi tulis ke `Employee Grade` di antara kedua blok)
34. Ketik Search `Employee Grade` pada tabel utama, tekan Enter
35. Klik `⋯` pada baris `Employee Grade`, pilih `Edit`
36. Ubah Field Name menjadi ` EMPLOYEE GRADE ` (huruf kapital semua dengan spasi di awal dan akhir)
37. Klik `[Save]`
38. Verifikasi toast netral (Info): "No changes to save."
39. Verifikasi popup tertutup
40. Verifikasi nama pada tabel tetap `Employee Grade`
41. Klik icon Changelog
42. Ketik Search `Employee Grade`, tekan Enter
43. Verifikasi anchor Changelog: entri Activate `Employee Grade — Status` Pre-setup tampil
44. Verifikasi jumlah entri `Employee Grade` pada Changelog sama dengan BC
45. Klik `[✕]`
46. Buka Global Settings > User > Detail Sari Dewi > tab System Log
47. Ketik Search `{runId}-070`, tekan Enter
48. Verifikasi anchor System Log Sari Dewi: entri Create seeding milik spec ini tampil
49. Ganti isi kotak search dengan `Employee Grade`, tekan Enter
50. Verifikasi jumlah entri `Employee Grade` pada System Log Sari Dewi sama dengan BS
51. Buka Global Settings > Activity Log > tab User Action
52. Ketik Search `{runId}-070`, tekan Enter
53. Verifikasi anchor Activity Log: entri Create seeding milik spec ini (Modified By `Sari D`) tampil
54. Ganti isi kotak search dengan `Employee Grade`, tekan Enter
55. Verifikasi jumlah entri `Employee Grade` pada Activity Log sama dengan BA
56. Buka Global Settings > User > Custom Field

### TC-GS-UCF-291: Aksi yang gagal atau dibatalkan tidak menulis log

57. Klik icon Changelog
58. Ketik Search `{runId}-070`, tekan Enter
59. Catat jumlah entri pada Changelog (baseline BC2)
60. Klik `[✕]`
61. Buka Global Settings > User > Detail Sari Dewi > tab System Log
62. Ketik Search `{runId}-070`, tekan Enter
63. Catat jumlah entri pada System Log Sari Dewi (baseline BS2)
64. Buka Global Settings > Activity Log > tab User Action
65. Ketik Search `{runId}-070`, tekan Enter
66. Catat jumlah entri pada Activity Log (baseline BA2)
67. Buka Global Settings > User > Custom Field
68. Klik `[+ Custom Field]`
69. Isi Field Name `Log Fail Probe {runId}-070`
70. Pilih Data Type `Text`
71. Paksa respons `POST /v2/iam/user-custom-fields` menjadi 500 (intercept)
72. Klik `[Submit]`
73. Lepas intercept POST
74. Klik `[✕]` pada popup
75. Verifikasi dialog `Unsaved Changes` tampil
76. Klik `[Leave]`
77. Ketik Search `{runId}-070` pada tabel utama, tekan Enter
78. Klik `⋯` pada baris `Log Keep Probe {runId}-070`, pilih `Delete`
79. Klik `[Cancel]`
80. Paksa respons `DELETE /v2/iam/user-custom-fields` menjadi 500 (intercept)
81. Klik `⋯` pada baris `Log Fail Del Probe {runId}-070`, pilih `Delete`
82. Klik `[Delete]`
83. Lepas intercept DELETE
84. Verifikasi `Log Keep Probe {runId}-070` tetap tampil pada tabel Custom Field
85. Verifikasi `Log Fail Del Probe {runId}-070` tetap tampil pada tabel Custom Field
86. Klik icon Changelog
87. Ketik Search `{runId}-070`, tekan Enter
88. Verifikasi anchor Changelog: entri Create seeding untuk `Log Keep Probe {runId}-070` dan `Log Fail Del Probe {runId}-070` tampil
89. Verifikasi tidak ada entri Create untuk `Log Fail Probe {runId}-070`
90. Verifikasi tidak ada entri Delete untuk `Log Keep Probe {runId}-070`
91. Verifikasi tidak ada entri Delete untuk `Log Fail Del Probe {runId}-070`
92. Verifikasi jumlah entri pada Changelog sama dengan BC2
93. Klik `[✕]`
94. Buka Global Settings > User > Detail Sari Dewi > tab System Log
95. Ketik Search `{runId}-070`, tekan Enter
96. Verifikasi anchor System Log Sari Dewi: entri Create seeding milik spec ini tampil
97. Verifikasi jumlah entri pada System Log Sari Dewi sama dengan BS2
98. Buka Global Settings > Activity Log > tab User Action
99. Ketik Search `{runId}-070`, tekan Enter
100. Verifikasi anchor Activity Log: entri Create seeding milik spec ini tampil
101. Verifikasi jumlah entri pada Activity Log sama dengan BA2
102. Buka Global Settings > User > Custom Field

### TC-GS-UCF-288: Item yang dilewati pada Bulk Delete tidak dicatat dan Delete idempotent tidak menulis entri kedua

103. Ketik Search `{runId}-070` pada tabel utama, tekan Enter
104. Centang `Log Skip A {runId}-070`, `Log Skip B {runId}-070`, dan `Log Skip C {runId}-070`
105. Admin kedua (Nadia Pratama, sesi API) menghapus `Log Skip B {runId}-070` hingga tersimpan
106. Klik `Bulk Action` > `Delete`
107. Klik `[Delete]`
108. Tunggu aksi selesai (dialog tertutup)
109. Klik icon Changelog
110. Ketik Search `Log Skip B {runId}-070`, tekan Enter
111. Verifikasi Changelog: entri Delete `Log Skip B {runId}-070` tampil dengan Modified By `Nadia P`
112. Verifikasi Changelog: entri Delete `Log Skip B {runId}-070` tepat 1 (tidak ada entri kedua dari bulk milik Sari D)
113. Ganti isi kotak search dengan `Log Skip A {runId}-070`, tekan Enter
114. Verifikasi Changelog: entri Delete `Log Skip A {runId}-070` tampil dengan Modified By `Sari D`
115. Ganti isi kotak search dengan `Log Skip C {runId}-070`, tekan Enter
116. Verifikasi Changelog: entri Delete `Log Skip C {runId}-070` tampil dengan Modified By `Sari D`
117. Klik `[✕]`
118. Buka Global Settings > User > Detail Sari Dewi > tab System Log
119. Ketik Search `Log Skip A {runId}-070`, tekan Enter
120. Verifikasi System Log Sari Dewi: entri Delete `Log Skip A {runId}-070` tampil tepat 1 kali
121. Ganti isi kotak search dengan `Log Skip C {runId}-070`, tekan Enter
122. Verifikasi System Log Sari Dewi: entri Delete `Log Skip C {runId}-070` tampil tepat 1 kali
123. Ganti isi kotak search dengan `Log Skip B {runId}-070`, tekan Enter
124. Verifikasi System Log Sari Dewi: entri Create seeding `Log Skip B {runId}-070` tampil
125. Verifikasi System Log Sari Dewi: tidak ada entri Delete `Log Skip B {runId}-070`
126. Buka Global Settings > Activity Log > tab User Action
127. Ketik Search `Log Skip A {runId}-070`, tekan Enter
128. Verifikasi Activity Log: entri Delete `Log Skip A {runId}-070` (Modified By `Sari D`) tampil tepat 1 kali
129. Ganti isi kotak search dengan `Log Skip C {runId}-070`, tekan Enter
130. Verifikasi Activity Log: entri Delete `Log Skip C {runId}-070` (Modified By `Sari D`) tampil tepat 1 kali
131. Ganti isi kotak search dengan `Log Skip B {runId}-070`, tekan Enter
132. Verifikasi Activity Log: entri Delete `Log Skip B {runId}-070` (Modified By `Nadia P`) tampil tepat 1 kali

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 284, 533, 291, 288. Urutan menyimpang dari urutan TC sumber: aksi yang menghapus data (Bulk Delete TC-GS-UCF-288) ditaruh paling akhir (bagian 3 prinsip 5), dan TC-GS-UCF-288 adalah satu-satunya TC dengan pelaku kedua.
- Pembagian TC: pencatatan presence untuk Create, Edit, Activate, Deactivate, Delete ada di spec 067, 068, dan 069; spec ini memuat aksi nyata untuk tiap TC absence, dengan baseline jumlah entri sendiri dan anchor positif pada surface yang sama (S-05, bagian 8b butir 2). Expected "tidak ada entri" TC-GS-UCF-287 (bulk Activate dan Deactivate yang melewati item) dibuktikan sebagai hitungan entri berbaseline di spec 068 (P-1).
- Langkah penghubung (aksi tanpa `Verifikasi`): pengisian Search tabel utama, Search pada Changelog, System Log, dan Activity Log, pencatatan baseline (BC, BS, BA, BC2, BS2, BA2), penutupan Modal Changelog lewat `[✕]` (tanpa dialog karena tidak ada form), pembukaan ulang Global Settings > User > Custom Field sebagai pemulihan state, memasang dan melepas intercept (S-09), `[Cancel]` pada dialog Delete, dan `[Leave]` pada dialog Unsaved Changes. Langkah "Tunggu aksi selesai (dialog tertutup)" sesudah `[Delete]` pada TC-GS-UCF-288 ditulis karena langkah berikutnya berpindah surface (bagian 8b butir 8).
- Intercept 5xx pada TC-GS-UCF-291 hanya berfungsi sebagai pemicu kegagalan (P-2/P-5); respons gagal itu sendiri tidak menjadi objek asersi, sehingga spec tetap `FE+BE`.
- Baseline TC-GS-UCF-291: TC menulis "jumlah entri dengan kata `Log`" (Search `Log`); spec memakai Search `{runId}-070` yang mencakup seluruh Custom Field milik spec ini (baseline dari entri Create seeding) supaya entri run lain tidak ikut terhitung (S-12).
- Spec melewati sekitar 35 langkah (132 langkah). Seluruhnya satu kelas g (absence log) dengan baca-log berpola yang tidak dihitung ke ambang (bagian 3 smell); pemicu kelas lain (intercept 5xx, sesi API kedua) hanya sebagai pemicu (P-5). Tiap blok TC berdiri sendiri dengan data bersuffix sendiri.
- Temuan untuk QA:
  - TC-GS-UCF-284 dan 533 menargetkan `Employee Grade` Pre-setup bersama; S-06 mengizinkan aksi No-Op pada baris Pre-setup karena nilai dan Last Updated tidak berubah, dengan syarat toast Info benar-benar tampil dan tidak ada penyimpanan. Bila Save No-Op ternyata menyimpan, Last Updated berubah dan baris Pre-setup ikut berubah.
  - TC-GS-UCF-533 mengasumsikan hitungan entri `Employee Grade` tidak berubah di antara TC-GS-UCF-284 dan 533; spec memakai hitungan yang sama sebagai baseline.
  - TC-GS-UCF-533 langkah 3 menulis Field Name ` EMPLOYEE GRADE ` dengan spasi tepi; spec menulis nilai itu verbatim.
  - TC-GS-UCF-291 langkah 5 menyebut "paksa respons DELETE 500" tanpa menyebut endpoint; spec memakai `POST /v2/iam/user-custom-fields` dan `DELETE /v2/iam/user-custom-fields` seperti ditulis di TC-GS-UCF-563 (TC yang sama menyebut path itu). TC-GS-UCF-291 tidak menyebut toast gagal; toast tidak diasersi.
  - TC-GS-UCF-288 berstatus Manual Only di TC (dua sesi paralel) tetapi tetap ditulis (konvensi bagian 2); pelaku kedua memakai sesi API (P-2). TC menyebut "admin kedua (Nadia Pratama) siap" tanpa menyebut hasil Bulk Delete pada baris yang sudah dihapus; spec tidak mengasersi toast bulk.
  - TC-GS-UCF-288 Expected c dan d menyebut System Log Sari Dewi dan Activity Log tanpa mekanisme pencarian; spec memakai Search atas nama bersuffix.
  - Post Condition TC kosong pada keempat TC.
