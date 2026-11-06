---
id: TC-GS-IMPORT-E2E-128-create-missing-satu-entri-create-per-record-di-changelog-modul-system
title: "Create Missing: satu entri Create per record di Changelog modul, System Log, dan Activity Log (Division, Position, Custom Field Option)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-340
  - TC-GS-IMPORT-341
  - TC-GS-IMPORT-342
  - TC-GS-IMPORT-922
coverage:
  web: automated
---

# Create Missing: satu entri Create per record di Changelog modul, System Log, dan Activity Log (Division, Position, Custom Field Option)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Akun yang sama dipakai membuka Detail user (System Log) dan Activity Log.
- Layar awal: hook `beforeEach` suite membuka Import > User Login (Client C); TC-GS-IMPORT-340, 341, 342, dan 922 berawal di Global Settings sehingga langkah pertamanya berpindah ke sana.
- Data Pre-setup Client C (tidak diubah): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 baris); Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor` (5 baris); Custom Field Shift (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`. Client C tanpa draft Tab User Login pada awal spec (Kontrak Fixture R1).
- Data Dinamis (fixture baru `Fixture.import.berkas`, disediakan tim QA; berkas User Login standar D-45): `user-login-logistik-4.csv` (4 baris Division `Logistik`, Position kosong), `user-login-store-supervisor-1.csv` (1 baris: Siti Rahmawati, Division `Engineering`, Position `Store Supervisor`), `user-login-division-skip.csv` (2 baris: Division `Logistik` pada baris #1 dan 121 karakter pada baris #2), `user-login-shift-bulk.csv` (D-81: Shift `Lembur`, `lembur `, `Piket`, `Siang`).
- Nama master data `Logistik`, `Store Supervisor`, dan opsi `Lembur` dan `Piket` literal tanpa suffix karena isi berkas CSV menentukan hasil "not found" dan "Invalid option" (pengecualian S-12 nama literal). Hook `before` menghapus sisa nama itu lewat API; langkah penghubung menghapusnya di antara TC; hook `after` menghapusnya lagi, mengembalikan Value Setting Shift ke `Pagi, Siang, Malam` (Kontrak Fixture R2), dan melakukan Discard Draft Tab User Login Client C.
- Baseline log (S-12, D-14): nama literal sudah dibuat berkali-kali oleh spec 123 sampai 127, sehingga jumlah entri dibaca sebagai angka total Pagination dengan Filter Action dan Search Name (Changelog modul, System Log Rudi Hartanto, Activity Log tab User Action), dicatat sebelum aksi pemicu pada tiap surface dan dibandingkan sebagai selisih sesudahnya; tidak ada asersi angka absolut karena audit trail permanen. Spec tidak memajukan jam; jam server dan jam browser tidak diatur.
- Layanan AI mock mode normal (D-40, tabel D-41 dan D-42): disetel di hook `before`, dikembalikan di hook `after`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis disediakan tim FE/BE: reset draft Tab User Login Client C (R1), hapus Division atau Position lewat API, dan pulihkan opsi Custom Field Shift (R2).
- State global: master data dan Custom Field Client C serta log; suite berjalan serial (`parallel: false`).
- Env var: `GS_CLIENTC_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-340: Create Missing Divisions menulis satu entri Create per record

1. Buka Global Settings > User > Division
2. Klik icon `[Changelog]`
3. Terapkan Filter Action `Create` dan Search Name `Logistik` pada Changelog Division, lalu catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
4. Tutup modal Changelog Division
5. Buka Global Settings > User > User List > Login User
6. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
7. Buka Tab System Log
8. Terapkan Filter Action `Create` dan Search Name `Logistik` pada System Log (entri Object `Division`), lalu catat angka total pada teks Pagination
9. Buka Global Settings > Activity Log > tab User Action
10. Terapkan Filter Action `Create` dan Search Name `Logistik` pada Activity Log (entri Object `Division`), lalu catat angka total pada teks Pagination
11. Buka Import > User Login
12. Klik [Upload File] di Dropzone dan pilih berkas `user-login-logistik-4.csv`
13. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
14. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
15. Tunggu aksi selesai (permintaan mendapat respons)
16. Buka Global Settings > User > Division
17. Klik icon `[Changelog]`
18. Terapkan Filter Action `Create` dan Search Name `Logistik` pada Changelog Division, lalu baca angka total pada teks Pagination dan perhatikan entri teratas
19. Verifikasi angka total Pagination Changelog Division terfilter bertambah tepat 1 dari catatan langkah 3
20. Verifikasi entri teratas Changelog Division memuat Field `Division Name`, Old Value `—`, New Value `Logistik`, Modified By `Rudi H`
21. Tutup modal Changelog Division
22. Buka Global Settings > User > User List > Login User
23. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
24. Buka Tab System Log
25. Terapkan Filter Action `Create` dan Search Name `Logistik` pada System Log (entri Object `Division`), lalu baca angka total pada teks Pagination dan perhatikan entri teratas
26. Verifikasi angka total Pagination System Log Rudi Hartanto terfilter bertambah tepat 1 dari catatan langkah 8
27. Verifikasi entri teratas System Log memuat Field `Division Name`, Old Value `—`, New Value `Logistik`
28. Buka Global Settings > Activity Log > tab User Action
29. Terapkan Filter Action `Create` dan Search Name `Logistik` pada Activity Log (entri Object `Division`), lalu baca angka total pada teks Pagination dan perhatikan entri teratas
30. Verifikasi angka total Pagination Activity Log tab User Action terfilter bertambah tepat 1 dari catatan langkah 10
31. Verifikasi entri teratas Activity Log memuat Field `Division Name`, Old Value `—`, New Value `Logistik`, Modified By `Rudi H`
32. Verifikasi angka total Pagination Changelog Division (langkah 18 dibanding langkah 3), System Log Rudi Hartanto (langkah 25 dibanding langkah 8), dan Activity Log tab User Action (langkah 29 dibanding langkah 10) masing-masing bertambah tepat 1, sama dengan pertambahan entri Action `Create`, sehingga tidak ada entri baru dengan Action `Create (Import)` maupun `Import User Login`

### TC-GS-IMPORT-341: Create Missing Positions menulis satu entri Create per record

33. Hapus Division `Logistik` lewat API dan reset draft Tab User Login Client C ke tanpa draft
34. Buka Global Settings > User > Position
35. Klik icon `[Changelog]`
36. Terapkan Filter Action `Create` dan Search Name `Store Supervisor` pada Changelog Position, lalu catat angka total pada teks Pagination
37. Tutup modal Changelog Position
38. Buka Global Settings > User > User List > Login User
39. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
40. Buka Tab System Log
41. Terapkan Filter Action `Create` dan Search Name `Store Supervisor` pada System Log (entri Object `Position`), lalu catat angka total pada teks Pagination
42. Buka Global Settings > Activity Log > tab User Action
43. Terapkan Filter Action `Create` dan Search Name `Store Supervisor` pada Activity Log (entri Object `Position`), lalu catat angka total pada teks Pagination
44. Buka Import > User Login
45. Klik [Upload File] di Dropzone dan pilih berkas `user-login-store-supervisor-1.csv`
46. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
47. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
48. Tunggu aksi selesai (permintaan mendapat respons)
49. Buka Global Settings > User > Position
50. Klik icon `[Changelog]`
51. Terapkan Filter Action `Create` dan Search Name `Store Supervisor` pada Changelog Position, lalu baca angka total pada teks Pagination dan perhatikan entri teratas
52. Verifikasi angka total Pagination Changelog Position terfilter bertambah tepat 1 dari catatan langkah 36
53. Verifikasi entri teratas Changelog Position memuat Field `Position Name`, Old Value `—`, New Value `Store Supervisor`, Modified By `Rudi H`
54. Tutup modal Changelog Position
55. Buka Global Settings > User > User List > Login User
56. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
57. Buka Tab System Log
58. Terapkan Filter Action `Create` dan Search Name `Store Supervisor` pada System Log (entri Object `Position`), lalu baca angka total pada teks Pagination dan perhatikan entri teratas
59. Verifikasi angka total Pagination System Log Rudi Hartanto terfilter bertambah tepat 1 dari catatan langkah 41
60. Verifikasi entri teratas System Log memuat Field `Position Name`, Old Value `—`, New Value `Store Supervisor`
61. Buka Global Settings > Activity Log > tab User Action
62. Terapkan Filter Action `Create` dan Search Name `Store Supervisor` pada Activity Log (entri Object `Position`), lalu baca angka total pada teks Pagination dan perhatikan entri teratas
63. Verifikasi angka total Pagination Activity Log tab User Action terfilter bertambah tepat 1 dari catatan langkah 43
64. Verifikasi entri teratas Activity Log memuat Field `Position Name`, Old Value `—`, New Value `Store Supervisor`, Modified By `Rudi H`
65. Verifikasi angka total Pagination Changelog Position (langkah 51 dibanding langkah 36), System Log Rudi Hartanto (langkah 58 dibanding langkah 41), dan Activity Log tab User Action (langkah 62 dibanding langkah 43) masing-masing bertambah tepat 1, sama dengan pertambahan entri Action `Create`, sehingga tidak ada entri baru dengan Action `Create (Import)` maupun `Import User Login`

### TC-GS-IMPORT-342: Record Division bernama tidak valid yang dilewati tidak menulis entri log

66. Hapus Position `Store Supervisor` lewat API, hapus Division `Logistik` lewat API, dan reset draft Tab User Login Client C ke tanpa draft
67. Buka Global Settings > User > Division
68. Klik icon `[Changelog]`
69. Terapkan Filter Action `Create` dan Search Name `Logistik` pada Changelog Division, lalu catat angka total pada teks Pagination
70. Tutup modal Changelog Division
71. Buka Import > User Login
72. Klik [Upload File] di Dropzone dan pilih berkas `user-login-division-skip.csv`
73. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
74. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
75. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
76. Muat ulang halaman Import > User Login
77. Verifikasi baris #1 berstatus `pending`
78. Verifikasi baris #2 berstatus `error`
79. Buka Global Settings > User > Division
80. Klik icon `[Changelog]`
81. Terapkan Filter Action `Create` dan Search Name `Logistik` pada Changelog Division, lalu baca angka total pada teks Pagination dan perhatikan entri teratas
82. Verifikasi angka total Pagination Changelog Division terfilter bertambah tepat 1 dari catatan langkah 69
83. Ketik Search Name dengan nama 121 karakter baris #2 berkas `user-login-division-skip.csv` pada Changelog Division
84. Verifikasi Changelog Division tidak memuat entri untuk nama 121 karakter
85. Tutup modal Changelog Division

### TC-GS-IMPORT-922: Create Missing Options menulis satu entri Edit per Custom Field

86. Hapus Division `Logistik` lewat API dan reset draft Tab User Login Client C ke tanpa draft
87. Buka Global Settings > User > Custom Field lalu klik icon `[Changelog]`
88. Terapkan Filter Action `Edit` dan Search Name `Shift` pada Changelog Custom Field, lalu catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
89. Tutup modal Changelog Custom Field
90. Buka Global Settings > User > User List > Login User, cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, buka Detail user, lalu buka Tab System Log
91. Terapkan Filter Action `Edit` dan Search Name `Shift` pada System Log (entri Object `Custom Field`), lalu catat angka total pada teks Pagination
92. Buka Global Settings > Activity Log > tab User Action
93. Terapkan Filter Action `Edit` dan Search Name `Shift` pada Activity Log (entri Object `Custom Field`), lalu catat angka total pada teks Pagination
94. Buka Import > User Login
95. Klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-bulk.csv`
96. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
97. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
98. Tunggu aksi selesai (permintaan mendapat respons)
99. Buka Global Settings > User > Custom Field, klik icon `[Changelog]`, terapkan Filter Action `Edit` dan Search Name `Shift`, baca angka total pada teks Pagination, dan perhatikan entri teratas
100. Verifikasi angka total Pagination Changelog Custom Field terfilter bertambah tepat 1 dari catatan langkah 88 (satu entri untuk dua value yang bertambah)
101. Verifikasi entri teratas Changelog Custom Field memuat Action `Edit`, Field `Shift — Value Setting`, Old Value `Pagi, Siang, Malam`, New Value `Pagi, Siang, Malam, Lembur, Piket`, Modified By `Rudi H`
102. Tutup modal Changelog Custom Field
103. Buka Detail user Rudi Hartanto Tab System Log, terapkan Filter Action `Edit` dan Search Name `Shift`, baca angka total pada teks Pagination, dan perhatikan entri teratas
104. Verifikasi angka total Pagination System Log Rudi Hartanto terfilter bertambah tepat 1 dari catatan langkah 91
105. Verifikasi entri teratas System Log memuat Action `Edit`, Object `Custom Field`, Name `Shift`, Old Value `Pagi, Siang, Malam`, dan New Value `Pagi, Siang, Malam, Lembur, Piket`
106. Buka Global Settings > Activity Log > tab User Action, terapkan Filter Action `Edit` dan Search Name `Shift`, baca angka total pada teks Pagination, dan perhatikan entri teratas
107. Verifikasi angka total Pagination Activity Log tab User Action terfilter bertambah tepat 1 dari catatan langkah 93
108. Verifikasi entri teratas Activity Log memuat Action `Edit`, Object `Custom Field`, Name `Shift`, Old Value `Pagi, Siang, Malam`, New Value `Pagi, Siang, Malam, Lembur, Piket`, dan Modified By `Rudi H`
109. Verifikasi pertambahan tepat 1 pada ketiga surface (langkah 100, 104, dan 107)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-340, 341, 342, 922).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (340, 341, 342, 922) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 33, 66, dan 86 (hapus master data buatan TC sebelumnya dan reset draft sebagai precondition TC berikutnya, Kontrak Fixture R1 dan R2); langkah 15, 48, dan 98 (Tunggu aksi selesai sebelum berpindah surface, 8b butir 8); langkah 4, 21, 37, 54, 70, 85, 89, dan 102 (menutup modal Changelog sebelum berpindah surface); langkah 83 (Search Name nama 121 karakter agar asersi absence tidak terhalang Filter Search sebelumnya); Search user Rudi Hartanto dengan email untuk menemukan Detail user (langkah 6, 23, 39, 56, 90). Langkah baseline dan pembacaan (Filter Action + Search Name lalu catat atau baca total Pagination) adalah pembacaan tanpa `Verifikasi`; hasilnya diasersi pada langkah berikutnya.
- Spec berisi 109 langkah, di atas sekitar 35 langkah. Alasan: empat blok TC masing-masing berdiri sendiri (satu entitas per blok) dan sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) pada tiga surface sehingga tidak dihitung ke estimasi; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Asersi jumlah entri dengan baseline (bukan kelas g): Expected "tidak ada entri `Create (Import)` atau `Import User Login`" ditulis sebagai pertambahan tepat 1 terhadap baseline sebelum aksi (langkah 32, 65, 109), bukan sebagai spec absence; tidak ada TC spec ini yang dirujuk ke spec kelas g.
- Pengecualian S-12 nama literal: `Logistik`, `Store Supervisor`, `Lembur`, dan `Piket` literal tanpa suffix karena ditentukan isi berkas CSV; entri log dicari lewat baseline total Pagination terfilter (Action + Name), bukan posisi baris seed.
- Temuan untuk QA:
  - TC-GS-IMPORT-340, 341, 342, dan 922 tidak menyebut cara menemukan Detail user "Rudi Hartanto" pada User List; spec mencari lewat Search email akun aktor.
  - TC-GS-IMPORT-340 dan 341 memakai nama tampil `Rudi H` pada kolom Modified By; spec mengasersi format `[First Name] [Last Initial]` sesuai TC.
  - Post Condition "Entri `Create` ... tercatat" dan "Division `Logistik` tersimpan permanen" pada TC-GS-IMPORT-340, 341, 342 diamati lewat Changelog; Post Condition penyimpanan permanen tidak punya langkah observasi di daftar master data pada TC-GS-IMPORT-340 dan 341 sehingga tidak diasersi terpisah.
  - TC-GS-IMPORT-922 memuat Precondition tanpa "User berada di" layar awal dan Langkah Uji 1 membuka Custom Field; spec berawal dari layar awal suite lalu berpindah ke Custom Field.
  - Cara mencari entri di Changelog, System Log, dan Activity Log (Search atau Filter berdasarkan Name) tidak dijelaskan TC; spec memakai Filter Action dan Search Name lalu angka total Pagination terfilter sebagai baseline (D-14), dan ketersediaan Search Name pada ketiga surface perlu dikonfirmasi tim FE.
  - Penanda "Tunggu aksi selesai" sesudah `[Create Missing ...]` (langkah 15, 48, 98) memakai "permintaan mendapat respons"; TC-GS-IMPORT-340, 341, dan 922 serta PRD belum menetapkan penanda yang teramati (toast sukses atau hilangnya Error Summary Callout tidak ditulis).
