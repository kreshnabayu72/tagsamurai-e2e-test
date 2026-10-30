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
- Baseline log (S-12): jumlah entri dan angka total Pagination dicatat sebelum aksi pemicu pada tiap surface (Changelog modul, System Log Rudi Hartanto, Activity Log tab User Action); tidak ada asersi angka absolut karena audit trail permanen. Spec tidak memajukan jam; jam server dan jam browser tidak diatur.
- Layanan AI mock mode normal (D-40, tabel D-41 dan D-42): disetel di hook `before`, dikembalikan di hook `after`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis disediakan tim FE/BE: reset draft Tab User Login Client C (R1), hapus Division atau Position lewat API, dan pulihkan opsi Custom Field Shift (R2).
- State global: master data dan Custom Field Client C serta log; suite berjalan serial (`parallel: false`).
- Env var: `GS_CLIENTC_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-340: Create Missing Divisions menulis satu entri Create per record

1. Buka Global Settings > User > Division
2. Klik icon `[Changelog]`
3. Catat jumlah entri Action `Create` dengan Division Name `Logistik` pada Changelog Division dan angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
4. Buka Global Settings > User > User List > Login User
5. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
6. Buka Tab System Log
7. Catat jumlah entri Action `Create` dengan Object `Division` dan Name `Logistik` pada System Log dan angka total pada teks Pagination
8. Buka Global Settings > Activity Log > tab User Action
9. Catat jumlah entri Action `Create` dengan Object `Division` dan Name `Logistik` pada Activity Log dan angka total pada teks Pagination
10. Buka Import > User Login
11. Klik [Upload File] di toolbar dan pilih berkas `user-login-logistik-4.csv`
12. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
13. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
14. Tunggu aksi selesai (toast sukses tampil dan Error Summary Callout hilang)
15. Buka Global Settings > User > Division
16. Klik icon `[Changelog]`
17. Hitung jumlah entri Action `Create` dengan Division Name `Logistik` pada Changelog Division, perhatikan entri terbarunya, dan baca angka total pada teks Pagination
18. Verifikasi jumlah entri Action `Create` dengan Division Name `Logistik` pada Changelog Division bertambah tepat 1 dari catatan langkah 3
19. Verifikasi entri baru Changelog Division memuat Field `Division Name`, Old Value `—`, New Value `Logistik`, Modified By `Rudi H`
20. Buka Global Settings > User > User List > Login User
21. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
22. Buka Tab System Log
23. Hitung jumlah entri Action `Create` dengan Object `Division` dan Name `Logistik` pada System Log, perhatikan entri terbarunya, dan baca angka total pada teks Pagination
24. Verifikasi jumlah entri Action `Create` dengan Object `Division` dan Name `Logistik` pada System Log Rudi Hartanto bertambah tepat 1 dari catatan langkah 7
25. Verifikasi entri baru System Log memuat Field `Division Name`, Old Value `—`, New Value `Logistik`
26. Buka Global Settings > Activity Log > tab User Action
27. Hitung jumlah entri Action `Create` dengan Object `Division` dan Name `Logistik` pada Activity Log, perhatikan entri terbarunya, dan baca angka total pada teks Pagination
28. Verifikasi jumlah entri Action `Create` dengan Object `Division` dan Name `Logistik` pada Activity Log tab User Action bertambah tepat 1 dari catatan langkah 9
29. Verifikasi entri baru Activity Log memuat Field `Division Name`, Old Value `—`, New Value `Logistik`, Modified By `Rudi H`
30. Verifikasi angka total Pagination Changelog Division (langkah 17 dibanding langkah 3), System Log Rudi Hartanto (langkah 23 dibanding langkah 7), dan Activity Log tab User Action (langkah 27 dibanding langkah 9) masing-masing bertambah tepat 1, sama dengan pertambahan entri Action `Create`, sehingga tidak ada entri baru dengan Action `Create (Import)` maupun `Import User Login`

### TC-GS-IMPORT-341: Create Missing Positions menulis satu entri Create per record

31. Hapus Division `Logistik` lewat API dan reset draft Tab User Login Client C ke tanpa draft
32. Buka Global Settings > User > Position
33. Klik icon `[Changelog]`
34. Catat jumlah entri Action `Create` dengan Position Name `Store Supervisor` pada Changelog Position dan angka total pada teks Pagination
35. Buka Global Settings > User > User List > Login User
36. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
37. Buka Tab System Log
38. Catat jumlah entri Action `Create` dengan Object `Position` dan Name `Store Supervisor` pada System Log dan angka total pada teks Pagination
39. Buka Global Settings > Activity Log > tab User Action
40. Catat jumlah entri Action `Create` dengan Object `Position` dan Name `Store Supervisor` pada Activity Log dan angka total pada teks Pagination
41. Buka Import > User Login
42. Klik [Upload File] di toolbar dan pilih berkas `user-login-store-supervisor-1.csv`
43. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
44. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
45. Tunggu aksi selesai (toast sukses tampil dan Error Summary Callout hilang)
46. Buka Global Settings > User > Position
47. Klik icon `[Changelog]`
48. Hitung jumlah entri Action `Create` dengan Position Name `Store Supervisor` pada Changelog Position, perhatikan entri terbarunya, dan baca angka total pada teks Pagination
49. Verifikasi jumlah entri Action `Create` dengan Position Name `Store Supervisor` pada Changelog Position bertambah tepat 1 dari catatan langkah 34
50. Verifikasi entri baru Changelog Position memuat Field `Position Name`, Old Value `—`, New Value `Store Supervisor`, Modified By `Rudi H`
51. Buka Global Settings > User > User List > Login User
52. Cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, lalu buka Detail user
53. Buka Tab System Log
54. Hitung jumlah entri Action `Create` dengan Object `Position` dan Name `Store Supervisor` pada System Log, perhatikan entri terbarunya, dan baca angka total pada teks Pagination
55. Verifikasi jumlah entri Action `Create` dengan Object `Position` dan Name `Store Supervisor` pada System Log Rudi Hartanto bertambah tepat 1 dari catatan langkah 38
56. Verifikasi entri baru System Log memuat Field `Position Name`, Old Value `—`, New Value `Store Supervisor`
57. Buka Global Settings > Activity Log > tab User Action
58. Hitung jumlah entri Action `Create` dengan Object `Position` dan Name `Store Supervisor` pada Activity Log, perhatikan entri terbarunya, dan baca angka total pada teks Pagination
59. Verifikasi jumlah entri Action `Create` dengan Object `Position` dan Name `Store Supervisor` pada Activity Log tab User Action bertambah tepat 1 dari catatan langkah 40
60. Verifikasi entri baru Activity Log memuat Field `Position Name`, Old Value `—`, New Value `Store Supervisor`, Modified By `Rudi H`
61. Verifikasi angka total Pagination Changelog Position (langkah 48 dibanding langkah 34), System Log Rudi Hartanto (langkah 54 dibanding langkah 38), dan Activity Log tab User Action (langkah 58 dibanding langkah 40) masing-masing bertambah tepat 1, sama dengan pertambahan entri Action `Create`, sehingga tidak ada entri baru dengan Action `Create (Import)` maupun `Import User Login`

### TC-GS-IMPORT-342: Record Division bernama tidak valid yang dilewati tidak menulis entri log

62. Hapus Position `Store Supervisor` lewat API, hapus Division `Logistik` lewat API, dan reset draft Tab User Login Client C ke tanpa draft
63. Buka Global Settings > User > Division
64. Klik icon `[Changelog]`
65. Catat jumlah entri Action `Create` dengan Division Name `Logistik` pada Changelog Division
66. Buka Import > User Login
67. Klik [Upload File] di toolbar dan pilih berkas `user-login-division-skip.csv`
68. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
69. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
70. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
71. Muat ulang halaman Import > User Login
72. Verifikasi baris #1 berstatus `pending`
73. Verifikasi baris #2 berstatus `error`
74. Buka Global Settings > User > Division
75. Klik icon `[Changelog]`
76. Hitung jumlah entri Action `Create` dengan Division Name `Logistik` dan perhatikan entri terbarunya
77. Verifikasi jumlah entri Action `Create` dengan Division Name `Logistik` pada Changelog Division bertambah tepat 1 dari catatan langkah 65
78. Verifikasi Changelog Division tidak memuat entri untuk nama 121 karakter

### TC-GS-IMPORT-922: Create Missing Options menulis satu entri Edit per Custom Field

79. Hapus Division `Logistik` lewat API dan reset draft Tab User Login Client C ke tanpa draft
80. Buka Global Settings > User > Custom Field lalu klik icon `[Changelog]`
81. Catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
82. Buka Global Settings > User > User List > Login User, cari user Rudi Hartanto dengan Ketik Search `totalControl_automated_qaTeam3@qwertysystem.net`, tekan Enter, buka Detail user, lalu buka Tab System Log
83. Catat angka total pada teks Pagination System Log
84. Buka Global Settings > Activity Log > tab User Action
85. Catat angka total pada teks Pagination Activity Log
86. Buka Import > User Login
87. Klik [Upload File] di toolbar dan pilih berkas `user-login-shift-bulk.csv`
88. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
89. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
90. Tunggu aksi selesai (toast sukses tampil dan Error Summary Callout hilang)
91. Buka Global Settings > User > Custom Field, klik icon `[Changelog]`, baca angka total pada teks Pagination, dan perhatikan entri teratas
92. Verifikasi angka total Pagination Changelog Custom Field bertambah tepat 1 dari catatan langkah 81 (satu entri untuk dua value yang bertambah)
93. Verifikasi entri teratas Changelog Custom Field memuat Action `Edit`, Field `Shift — Value Setting`, Old Value `Pagi, Siang, Malam`, New Value `Pagi, Siang, Malam, Lembur, Piket`, Modified By `Rudi H`
94. Buka Detail user Rudi Hartanto Tab System Log, baca angka total pada teks Pagination, dan perhatikan entri teratas
95. Verifikasi angka total Pagination System Log Rudi Hartanto bertambah tepat 1 dari catatan langkah 83
96. Verifikasi entri teratas System Log memuat Action `Edit`, Object `Custom Field`, Name `Shift`, Old Value `Pagi, Siang, Malam`, dan New Value `Pagi, Siang, Malam, Lembur, Piket`
97. Buka Global Settings > Activity Log > tab User Action, baca angka total pada teks Pagination, dan perhatikan entri teratas
98. Verifikasi angka total Pagination Activity Log tab User Action bertambah tepat 1 dari catatan langkah 85
99. Verifikasi entri teratas Activity Log memuat Action `Edit`, Object `Custom Field`, Name `Shift`, Old Value `Pagi, Siang, Malam`, New Value `Pagi, Siang, Malam, Lembur, Piket`, dan Modified By `Rudi H`
100. Verifikasi pertambahan tepat 1 pada ketiga surface (langkah 92, 95, dan 98) sehingga tidak ada entri baru dengan Action `Create (Import)` maupun `Import User Login`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-340, 341, 342, 922).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (340, 341, 342, 922) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 31, 62, dan 79 (hapus master data buatan TC sebelumnya dan reset draft sebagai precondition TC berikutnya, Kontrak Fixture R1 dan R2); langkah 14, 45, dan 90 (Tunggu aksi selesai sebelum berpindah surface, 8b butir 8); Search user Rudi Hartanto dengan email untuk menemukan Detail user (langkah 5, 21, 36, 52, 82).
- Spec berisi 100 langkah, di atas sekitar 35 langkah. Alasan: empat blok TC masing-masing berdiri sendiri (satu entitas per blok) dan sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) pada tiga surface sehingga tidak dihitung ke estimasi; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Asersi jumlah entri dengan baseline (bukan kelas g): Expected "tidak ada entri `Create (Import)` atau `Import User Login`" ditulis sebagai pertambahan tepat 1 terhadap baseline sebelum aksi (langkah 30, 61, 100), bukan sebagai spec absence; tidak ada TC spec ini yang dirujuk ke spec kelas g.
- Pengecualian S-12 nama literal: `Logistik`, `Store Supervisor`, `Lembur`, dan `Piket` literal tanpa suffix karena ditentukan isi berkas CSV; entri log dicari lewat baseline jumlah, bukan posisi baris seed.
- Temuan untuk QA:
  - TC-GS-IMPORT-340, 341, 342, dan 922 tidak menyebut cara menemukan Detail user "Rudi Hartanto" pada User List; spec mencari lewat Search email akun aktor.
  - TC-GS-IMPORT-340 dan 341 memakai nama tampil `Rudi H` pada kolom Modified By; spec mengasersi format `[First Name] [Last Initial]` sesuai TC.
  - Post Condition "Entri `Create` ... tercatat" dan "Division `Logistik` tersimpan permanen" pada TC-GS-IMPORT-340, 341, 342 diamati lewat Changelog; Post Condition penyimpanan permanen tidak punya langkah observasi di daftar master data pada TC-GS-IMPORT-340 dan 341 sehingga tidak diasersi terpisah.
  - TC-GS-IMPORT-922 memuat Precondition tanpa "User berada di" layar awal dan Langkah Uji 1 membuka Custom Field; spec berawal dari layar awal suite lalu berpindah ke Custom Field.
  - Cara mencari entri di Changelog, System Log, dan Activity Log (Search atau Filter berdasarkan Name) tidak dijelaskan TC; spec menghitung entri pada daftar yang tampil dan memakai angka total Pagination sebagai baseline.
