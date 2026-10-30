---
id: TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow
title: "Modal Changelog: Chip Filter, Search di Dropdown, dan Overflow Chip"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-202
  - TC-GS-DIV-203
  - TC-GS-DIV-204
  - TC-GS-DIV-233
  - TC-GS-DIV-292
  - TC-GS-DIV-293
  - TC-GS-DIV-294
  - TC-GS-DIV-295
coverage:
  web: automated
---

# Modal Changelog: Chip Filter, Search di Dropdown, dan Overflow Chip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Akun aksi lewat API (tidak login UI): Create+Read, Rina Marlina (`Rina M`), `createOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_CREATE_PASSWORD`; Update+Read, Agus Wijaya (`Agus W`), `updateOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_UPDATE_PASSWORD`; Delete+Read, Dewi Lestari (`Dewi L`), `deleteOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_DELETE_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API di hook `before`, urutan sebagai berikut):
  - Sembilan Division dari Population D-02 oleh Sari Dewi (seeding Division lewat API, setara TC-GS-DIV-30) dengan nama dan Code literal Accounting (`ACC`), Administration (`ADM`), Audit (`AUD`), Business Development (`BD`), Corporate Communication (`CCM`), Customer Service (`CSV`), Data Analytics (`DA`), Engineering (`ENG`), Facilities (`FAC`). Hanya sembilan nama ini yang di-seed (S-11) karena itulah satu-satunya yang dipakai `Verifikasi`: delapan nama untuk TC-GS-DIV-233 dan `Accounting` untuk opsi hasil Search `account` di dropdown Division Name (langkah 28); sisa 17 nama Population tidak dipakai asersi. Seed idempotent: nama yang sudah ada dilewati; cleanup hanya menghapus yang dibuat spec ini. Tiap Create mencatat entri Changelog Action Create oleh `Sari D` (Old Value `—`). Delapan nama yang dipakai TC-GS-DIV-233 adalah `Administration`, `Audit`, `Business Development`, `Corporate Communication`, `Customer Service`, `Data Analytics`, `Engineering`, `Facilities`.
  - Division milik spec oleh Sari Dewi lewat API (setara TC-GS-DIV-101 dan TC-GS-DIV-102): `Accounting {runId}-058` (Code `ACC-058`) dibuat lalu Name-nya diubah menjadi `Accounting and Tax {runId}-058`, dan `Procurement {runId}-058` (Code `PRC-058`) dibuat lalu Code-nya diubah menjadi `PROC-058` (entri Action Create, lalu Edit Field `Division Name` dan `Code`, oleh `Sari D`). Population D-02 tidak diedit.
  - Division `Log Mixed Div {runId}-058` dibuat oleh Rina Marlina (entri Create oleh `Rina M`), diubah namanya oleh Agus Wijaya menjadi `Log Mixed Div Renamed {runId}-058` (entri Edit oleh `Agus W`), lalu dihapus oleh Dewi Lestari (entri Delete oleh `Dewi L`). Menyediakan keempat user Modified By untuk TC-GS-DIV-292 dan TC-GS-DIV-293.
- Cleanup (hook `before` dan `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division Population yang dibuat spec ini dan Division bersuffix `-058` (termasuk `Accounting and Tax {runId}-058`, `Procurement {runId}-058`; hook `before` juga menghapus sisa bersuffix `-058` dari run lama). Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6), Population (9), dan Division milik spec ini (`Accounting and Tax {runId}-058`, `Procurement {runId}-058`, `Log Mixed Div {runId}-058`; disediakan tim FE).
- Kemampuan teknis: viewport desktop lebar 1280 px (diatur di hook `before`, dipulihkan di hook `after`); klik `(X)` pada chip filter; mengetik di kotak search di dalam dropdown filter; mengamati chip yang tersembunyi di belakang field (tidak wrap, tanpa `+N more`).
- Precondition TC-GS-DIV-202, 203, 204, 233, 292, 293, 294, 295: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi (Modified By: `Sari D`, `Rina M`, `Agus W`, `Dewi L`). TC-GS-DIV-204, 292, 293, 294, 295: entri hasil TC-GS-DIV-101 (dan TC-GS-DIV-102 kecuali TC-GS-DIV-204) ada. TC-GS-DIV-233: lebih dari 8 nama Division berbeda di riwayat.
- Suite serial (`parallel: false`) karena Population D-02 bernama literal dan dipakai bersama spec lain.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: ukuran viewport dikembalikan ke bawaan di hook `after`.

## Test Steps

### TC-GS-DIV-233: Banyak opsi terpilih pada field filter Changelog menampilkan overflow chip

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di modal
3. Pilih 8 opsi Division Name: `Administration`, `Audit`, `Business Development`, `Corporate Communication`, `Customer Service`, `Data Analytics`, `Engineering`, `Facilities`
4. Amati field Division Name
5. Verifikasi chip yang melebihi lebar field Division Name tersembunyi di belakang field
6. Verifikasi chip tidak wrap ke baris baru
7. Verifikasi tidak ada ringkasan `+N more`
8. Klik `[Apply]`
9. Verifikasi tabel memuat sedikitnya satu baris dengan Division Name salah satu dari 8 opsi tersebut
10. Verifikasi tabel hanya memuat baris dengan Division Name dari 8 opsi tersebut
11. Klik Filter, lalu buka dropdown Division Name
12. Verifikasi 8 opsi tetap tercentang

### TC-GS-DIV-202: Hapus chip filter lewat X menghapus centang opsi

13. Klik `[Clear Field]`
14. Pilih Action `Create` dan `Edit`
15. Klik `(X)` pada chip `Create` (field Action) tanpa membuka dropdown
16. Verifikasi chip `Create` hilang
17. Verifikasi chip `Edit` tetap
18. Buka dropdown Action
19. Verifikasi checkbox `Create` ter-uncheck
20. Verifikasi checkbox `Edit` tetap tercentang

### TC-GS-DIV-203: Uncheck opsi di dalam dropdown menghapus chip

21. Klik `[Clear Field]`
22. Pilih Action `Create` dan `Edit`
23. Buka dropdown Action dan uncheck `Create`
24. Verifikasi chip `Create` hilang dari field Action
25. Verifikasi chip `Edit` tetap

### TC-GS-DIV-204: Search di dalam dropdown filter mempersempit opsi

26. Klik `[Clear Field]`
27. Buka dropdown Division Name, ketik `account` pada kotak search di dalam dropdown
28. Verifikasi daftar opsi memuat `Accounting`
29. Verifikasi daftar opsi memuat `Accounting and Tax {runId}-058`
30. Verifikasi daftar opsi hanya memuat opsi yang namanya memuat `account` (tanpa membedakan huruf besar kecil)
31. Ganti isi kotak search yang sama dengan `zzz`
32. Verifikasi daftar opsi kosong (keadaan tanpa opsi)
33. Kosongkan kotak search, tutup dropdown

### TC-GS-DIV-292: Search di dalam dropdown filter Changelog: Action, Field, dan Modified By

34. Buka dropdown Action, ketik `cre` pada kotak search
35. Verifikasi dropdown Action hanya memuat opsi `Create`
36. Buka dropdown Field, ketik `cod` pada kotak search
37. Verifikasi dropdown Field hanya memuat opsi `Code`
38. Buka dropdown Modified By, ketik `sar` pada kotak search
39. Verifikasi dropdown Modified By hanya memuat opsi `Sari D`
40. Buka dropdown Action, ganti isi kotak search dengan `zzz`
41. Verifikasi dropdown Action menampilkan keadaan tanpa opsi
42. Buka dropdown Field, ganti isi kotak search dengan `zzz`
43. Verifikasi dropdown Field menampilkan keadaan tanpa opsi
44. Buka dropdown Modified By, ganti isi kotak search dengan `zzz`
45. Verifikasi dropdown Modified By menampilkan keadaan tanpa opsi
46. Buka dropdown Action, kosongkan kotak search
47. Verifikasi dropdown Action memuat opsi `Create`, `Edit`, `Delete` secara penuh
48. Buka dropdown Field, kosongkan kotak search
49. Verifikasi dropdown Field memuat opsi `Division Name` dan `Code` secara penuh
50. Buka dropdown Modified By, kosongkan kotak search
51. Verifikasi dropdown Modified By memuat opsi `Sari D`, `Rina M`, `Agus W`, dan `Dewi L` secara penuh

### TC-GS-DIV-293: Dua opsi pada satu field filter digabung OR: Division Name, Field, dan Modified By

52. Klik `[Clear Field]`
53. Pilih Division Name `Accounting and Tax {runId}-058` dan `Procurement {runId}-058`, klik `[Apply]`
54. Verifikasi tabel memuat baris Division Name `Accounting and Tax {runId}-058`
55. Verifikasi tabel memuat baris Division Name `Procurement {runId}-058`
56. Verifikasi tidak ada baris Division Name selain `Accounting and Tax {runId}-058` dan `Procurement {runId}-058`
57. Klik Filter, klik `[Clear Field]`
58. Pilih Field `Division Name` dan `Code`, klik `[Apply]`
59. Verifikasi tabel memuat baris Field `Division Name`
60. Verifikasi tabel memuat baris Field `Code`
61. Klik Filter, klik `[Clear Field]`
62. Pilih Modified By `Sari D` dan `Rina M`, klik `[Apply]`
63. Verifikasi tabel memuat baris Modified By `Sari D`
64. Verifikasi tabel memuat baris Modified By `Rina M`
65. Verifikasi tidak ada baris Modified By `Agus W`
66. Verifikasi tidak ada baris Modified By `Dewi L`

### TC-GS-DIV-294: Hapus chip lewat X pada field filter Division Name, Field, dan Modified By

67. Klik Filter, klik `[Clear Field]`
68. Pada field Division Name centang `Accounting and Tax {runId}-058` dan `Procurement {runId}-058`
69. Klik `(X)` pada chip `Procurement {runId}-058` tanpa membuka dropdown
70. Pada field Field centang `Division Name` dan `Code`
71. Klik `(X)` pada chip `Code`
72. Pada field Modified By centang `Sari D` dan `Rina M`
73. Klik `(X)` pada chip `Rina M`
74. Verifikasi field Division Name: chip `Procurement {runId}-058` hilang
75. Verifikasi field Division Name: chip `Accounting and Tax {runId}-058` tetap
76. Verifikasi field Field: chip `Code` hilang
77. Verifikasi field Field: chip `Division Name` tetap
78. Verifikasi field Modified By: chip `Rina M` hilang
79. Verifikasi field Modified By: chip `Sari D` tetap
80. Buka dropdown Division Name
81. Verifikasi checkbox `Procurement {runId}-058` ter-uncheck
82. Verifikasi checkbox `Accounting and Tax {runId}-058` tetap tercentang
83. Buka dropdown Field
84. Verifikasi checkbox `Code` ter-uncheck
85. Verifikasi checkbox `Division Name` tetap tercentang
86. Buka dropdown Modified By
87. Verifikasi checkbox `Rina M` ter-uncheck
88. Verifikasi checkbox `Sari D` tetap tercentang

### TC-GS-DIV-295: Uncheck opsi di dalam dropdown menghapus chip pada Division Name, Field, dan Modified By

89. Klik `[Clear Field]`
90. Pada field Division Name centang `Accounting and Tax {runId}-058` dan `Procurement {runId}-058`, lalu uncheck `Procurement {runId}-058` dari dalam dropdown yang terbuka
91. Pada field Field centang `Division Name` dan `Code`, lalu uncheck `Code` dari dalam dropdown
92. Pada field Modified By centang `Sari D` dan `Rina M`, lalu uncheck `Rina M` dari dalam dropdown
93. Verifikasi field Division Name: chip `Procurement {runId}-058` hilang
94. Verifikasi field Division Name: chip `Accounting and Tax {runId}-058` tetap
95. Verifikasi field Field: chip `Code` hilang
96. Verifikasi field Field: chip `Division Name` tetap
97. Verifikasi field Modified By: chip `Rina M` hilang
98. Verifikasi field Modified By: chip `Sari D` tetap

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-233, 202, 203, 204, 292, 293, 294, 295. Alasan: TC-GS-DIV-233 mengamati field dan satu [Apply] di awal (screening lebih dulu, bagian 3 konvensi); TC yang hanya mengamati chip dan dropdown tanpa [Apply] (202, 203, 204, 292) sebelum TC yang meng-Apply filter (293); TC-GS-DIV-294 dan 295 terakhir karena memakai pilihan yang sama dengan 293. Modal Changelog dan Filter Panel dibuka sekali di awal dan dipakai berurutan.
- Langkah penghubung (aksi tanpa `Verifikasi`, membersihkan state filter dari TC sebelumnya, S-03 dan S-09): langkah 13, 21, 26, 33 (Clear Field dan menutup dropdown), langkah 52, 57, 61, 67, 89 (Clear Field, Filter dibuka ulang sesudah [Apply]), langkah 4 (mengamati field Division Name sebelum asersi chip langkah 5 sampai 7), dan langkah 11 (membuka kembali Filter dan dropdown Division Name sesudah [Apply]). Langkah 9 (Verifikasi baris pembanding tampil) adalah anchor positif sebelum asersi "hanya memuat" pada langkah 10 (bagian 8b butir 2).
- Langkah 5 sampai 7 TC-GS-DIV-233 (Expected a) diasersi sebelum [Apply] (langkah 8), karena chip hanya teramati saat opsi terpilih belum diterapkan atau setelah dibuka kembali (state sementara diasersi sebelum langkah yang mengubahnya, bagian 8b butir 5).
- Precondition TC menyebut Modified By `Sari D`, `Rina M`, `Agus W`, `Dewi L`; keempatnya di-seed karena TC-GS-DIV-292 dan 293 mengasersi ketersediaan dan ketiadaan baris ketiga user lain.
- Spec melewati sekitar 35 langkah karena delapan TC menguji chip dan dropdown Filter Panel yang sama pada tiga field berbeda dan tiap klausa Expected (chip hilang dan chip lain tetap, per field) menjadi satu `Verifikasi` (S-01); semua blok satu kelas harness (Filter Panel Changelog), satu akun aktor, satu dataset. Modal Changelog dan Filter Panel dibuka sekali di awal dan blok-blok melanjutkan state yang sama; state filter dari blok sebelumnya dibersihkan lewat `[Clear Field]` (langkah penghubung), dan blok TC-GS-DIV-294 dan 295 memakai pilihan yang sama dengan blok TC-GS-DIV-293.
- Temuan untuk QA: (1) TC-GS-DIV-233 Expected a (chip yang melebihi lebar field tersembunyi di belakang field, tanpa `+N more`) mengikuti NC-13 (Dikonfirmasi); cara mengasersi chip yang "tersembunyi" (secara visual) disediakan tim FE. (2) TC-GS-DIV-233 tidak menyebut lebar viewport; spec memakai 1280 px agar 8 chip melebihi lebar field. (3) TC-GS-DIV-293 Expected c bergantung pada ada atau tidaknya entri `Agus W` dan `Dewi L`; spec men-seed keduanya agar asersi ketiadaan bermakna. (4) TC-GS-DIV-233 menyebut 8 opsi tanpa menyebut namanya; spec memilih 8 nama Population (`Administration` ... `Facilities`). (5) TC-GS-DIV-293 sampai 295 menyebut `Accounting and Tax` dan `Procurement`; spec memakai Division milik spec bersuffix (`Accounting and Tax {runId}-058`, `Procurement {runId}-058`) karena Population tidak diedit.
