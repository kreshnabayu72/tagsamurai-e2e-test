---
id: TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Tab Non-Login User Detail: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-678
  - TC-GS-USER-679
  - TC-GS-USER-680
  - TC-GS-USER-681
  - TC-GS-USER-682
  - TC-GS-USER-683
  - TC-GS-USER-684
  - TC-GS-USER-685
  - TC-GS-USER-686
coverage:
  web: automated
---

# Tab Non-Login User Detail: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup dan tidak menyimpan preferensi kolom.
- Akun: Total Control, `Siti Nurhaliza`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Master Data Position (`Finance Manager`, `HR Business Partner`, `Staff`, `Supervisor`, `Internal Auditor`) dan Division (`Finance`, `General Affairs`, `Logistics`, `Legal`) Pre-setup No. 22 dan 23. `HR Business Partner` dan `Logistics` tidak dipakai Non-Login User mana pun di spec ini sehingga tidak boleh muncul sebagai opsi filter (TC-GS-USER-679).
- Data Dinamis, holder: Login User milik spec `Ahmad Fauzi {runId}-109` (email `ahmadfauzi+{runId}-109@qwertysystem.net`, status Activated, Access Global Settings) sebagai Represented By seluruh Non-Login User di bawah. Holder milik spec dipakai, bukan `Ahmad Fauzi` Pre-setup (Tabel Data Uji Pre-setup No. 13) beserta `Agus Prasetyo` dan `Lina Marlina` Pre-setup (No. 21), karena S-06 melarang mengubah data Pre-setup bersama dan S-11 menuntut data dengan lebih dari satu halaman serta sedikitnya dua nilai distinct pada kolom yang diuji.
- Data Dinamis, 12 Non-Login User milik spec (Represented By = `Ahmad Fauzi {runId}-109`), di-seed di hook `before`. Tabel memuat 12 baris: halaman 1 berisi 10 baris dan total 2 halaman. Nilai Name, Email, dan Employee ID bersuffix `{runId}-109`. `{U1}` dan `{U2}` pada kolom Temporary Until adalah tanggal hari uji + 30 hari dan hari uji + 60 hari; `{L1}` = tanggal 7 hari sebelum hari uji dan `{L2}` = tanggal hari uji (Last Update); semua tanggal ditampilkan dalam Date Format General Settings.
  | Name | Email | Employee ID | Position | Division | Active | Temporary User | Temporary Until | Last Update |
  |---|---|---|---|---|---|---|---|---|
  | `Agus Prasetyo {runId}-109` | `nlu01+{runId}-109@qwertysystem.net` | `EMP-AGS-{runId}-109` | Finance Manager | Finance | Active | No | kosong | `{L1}` |
  | `Bagas Santoso {runId}-109` | `nlu02+{runId}-109@qwertysystem.net` | `EMP-BGS-{runId}-109` | Staff | General Affairs | Active | No | kosong | `{L1}` |
  | `Citra Dewanti {runId}-109` | `nlu03+{runId}-109@qwertysystem.net` | `EMP-CTR-{runId}-109` | Supervisor | Finance | Active | Yes | `{U1}` (hari uji + 30 hari) | `{L1}` |
  | `Dimas Pranoto {runId}-109` | `nlu04+{runId}-109@qwertysystem.net` | `EMP-DMS-{runId}-109` | Staff | General Affairs | Active | No | kosong | `{L1}` |
  | `Eka Wulandari {runId}-109` | `nlu05+{runId}-109@qwertysystem.net` | `EMP-EKA-{runId}-109` | Finance Manager | Legal | Active | No | kosong | `{L1}` |
  | `Fitri Handayani {runId}-109` | `nlu06+{runId}-109@qwertysystem.net` | `EMP-FTR-{runId}-109` | Internal Auditor | Finance | Active | Yes | `{U2}` (hari uji + 60 hari) | `{L1}` |
  | `Galih Permadi {runId}-109` | `nlu07+{runId}-109@qwertysystem.net` | `EMP-GLH-{runId}-109` | Staff | Legal | Active | No | kosong | `{L2}` |
  | `Hana Kusuma {runId}-109` | `nlu08+{runId}-109@qwertysystem.net` | `EMP-HNA-{runId}-109` | Supervisor | General Affairs | Active | No | kosong | `{L2}` |
  | `Lina Marlina {runId}-109` | `nlu09+{runId}-109@qwertysystem.net` | kosong | kosong | Legal | Inactive | No | kosong | `{L2}` |
  | `Nadia Rahma {runId}-109` | `nlu10+{runId}-109@qwertysystem.net` | `EMP-NDR-{runId}-109` | Staff | Finance | Active | No | kosong | `{L2}` |
  | `Rizky Fadillah {runId}-109` | `nlu11+{runId}-109@qwertysystem.net` | `EMP-RZK-{runId}-109` | Finance Manager | General Affairs | Inactive | No | kosong | `{L2}` |
  | `Wahyu Hidayat {runId}-109` | `nlu12+{runId}-109@qwertysystem.net` | `EMP-WHY-{runId}-109` | Supervisor | Legal | Active | No | kosong | `{L2}` |

  Position dan Division di atas hanya memuat 4 dari 5 nilai Position dan 3 dari 4 nilai Division Master Data Pre-setup, sehingga dropdown filter yang diisi dari data tabel tidak memuat nilai sisanya. Dua baris berstatus `Inactive` (`Lina Marlina`, `Rizky Fadillah`) dan dua baris `Temporary User` = `Yes` (`Citra Dewanti`, `Fitri Handayani`) memberi dua nilai distinct pada kolom Status dan Temporary User.
- Kemampuan teknis (disediakan tim FE/BE; endpoint ditentukan tim FE di tahap script): seeding Login User holder dan Non-Login User dengan Represented By = holder lewat API di hook `before`; cleanup di hook `after` menghapus Non-Login User lalu holder lewat API tanpa berasumsi seeding berhasil penuh. Seeding menambah 13 user pada hitungan Master Data Count Limit gabungan Login + Non-Login User; nilai limit environment cukup besar untuk itu.
- Kemampuan teknis tambahan (disediakan tim FE/BE; TC tidak memberi cara): mengatur Last Update Non-Login User seed menjadi `{L1}` untuk enam baris pertama pada tabel di atas dan `{L2}` untuk enam baris lainnya. Last Update diturunkan dari waktu entri Changelog terbaru user itu (PRD user.md §4.1.4), sehingga nilainya tidak dapat diatur lewat edit biasa.
- Data uji per TC: TC-GS-USER-680 satu opsi per field (`Internal Auditor`, `Legal`, `Inactive`, `Yes`); TC-GS-USER-681 `Internal Auditor` dan `Supervisor`; TC-GS-USER-682 keyword dropdown `PERVIS` dan `zzz`; TC-GS-USER-683 dan 684 `Finance Manager` dan `Staff`; TC-GS-USER-685 rentang `{L1}` sampai `{L1}` dan `{U1}` sampai `{U1}`; TC-GS-USER-686 Position `Staff` dan Division `Finance`.
- Date Format General Settings default environment (`DD/MM/YY`); spec tidak mengubahnya.
- State yang diubah dan dipulihkan: Filter Panel dikosongkan lewat `[Clear Field]` dan `[Apply]` di akhir tiap TC yang menerapkan filter; hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data Pre-setup bersama (S-06).
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel; mengetik di kotak pencarian dalam dropdown; membaca warna icon Filter (gelap saat panel terbuka) dan badge titik pada icon Filter.

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-109`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-109` di User List
3. Klik Tab `Non-Login User`

### TC-GS-USER-678: Screening Filter Panel

4. Klik icon Filter
5. Verifikasi Filter Panel terbuka
6. Verifikasi field `Position` bertipe multi-select searchable dengan placeholder `All positions`
7. Verifikasi field `Division` bertipe multi-select searchable dengan placeholder `All divisions`
8. Verifikasi field `Status` bertipe multi-select searchable dengan placeholder `All statuses`
9. Verifikasi field `Temporary User` bertipe multi-select searchable dengan placeholder `All options`
10. Verifikasi field `Last Update` bertipe date range picker dengan placeholder `Select date`
11. Verifikasi field `Temporary Until` bertipe date range picker dengan placeholder `Select date`
12. Verifikasi tombol `[Clear Field]`
13. Verifikasi tombol `[Apply]`

### TC-GS-USER-679: Opsi dropdown filter diambil dari nilai yang ada di tabel

14. Buka dropdown Position
15. Verifikasi dropdown Position memuat opsi `Finance Manager`, `Internal Auditor`, `Staff`, dan `Supervisor`
16. Verifikasi dropdown Position tidak memuat opsi `HR Business Partner` (nilai Master Data tanpa baris)
17. Buka dropdown Division
18. Verifikasi dropdown Division memuat opsi `Finance`, `General Affairs`, dan `Legal`
19. Verifikasi dropdown Division tidak memuat opsi `Logistics` (nilai Master Data tanpa baris)
20. Buka dropdown Status
21. Verifikasi dropdown Status memuat opsi `Active` dan `Inactive`
22. Buka dropdown Temporary User
23. Verifikasi dropdown Temporary User memuat opsi `Yes` dan `No`

### TC-GS-USER-680: Filter multi-select per field menyaring baris

24. Pilih opsi `Internal Auditor` pada dropdown Position
25. Klik `[Apply]`
26. Verifikasi field Position: tabel hanya menampilkan baris `Fitri Handayani {runId}-109`
27. Verifikasi field Position: badge titik tampil pada icon Filter
28. Klik icon Filter
29. Verifikasi field Position: icon Filter gelap (panel terbuka)
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Klik icon Filter
33. Pilih opsi `Legal` pada dropdown Division
34. Klik `[Apply]`
35. Verifikasi field Division: tabel hanya menampilkan 4 baris dengan Division `Legal`: `Eka Wulandari {runId}-109`, `Galih Permadi {runId}-109`, `Lina Marlina {runId}-109`, `Wahyu Hidayat {runId}-109`
36. Verifikasi field Division: badge titik tampil pada icon Filter
37. Klik icon Filter
38. Verifikasi field Division: icon Filter gelap (panel terbuka)
39. Klik `[Clear Field]`
40. Klik `[Apply]`
41. Klik icon Filter
42. Pilih opsi `Inactive` pada dropdown Status
43. Klik `[Apply]`
44. Verifikasi field Status: tabel hanya menampilkan 2 baris berstatus `Inactive`: `Lina Marlina {runId}-109`, `Rizky Fadillah {runId}-109`
45. Verifikasi field Status: badge titik tampil pada icon Filter
46. Klik icon Filter
47. Verifikasi field Status: icon Filter gelap (panel terbuka)
48. Klik `[Clear Field]`
49. Klik `[Apply]`
50. Klik icon Filter
51. Pilih opsi `Yes` pada dropdown Temporary User
52. Klik `[Apply]`
53. Verifikasi field Temporary User: tabel hanya menampilkan 2 baris dengan Temporary User `Yes`: `Citra Dewanti {runId}-109`, `Fitri Handayani {runId}-109`
54. Verifikasi field Temporary User: badge titik tampil pada icon Filter
55. Klik icon Filter
56. Verifikasi field Temporary User: icon Filter gelap (panel terbuka)
57. Klik `[Clear Field]`
58. Klik `[Apply]`

### TC-GS-USER-681: Dua opsi dalam satu field digabung OR

59. Klik icon Filter
60. Pilih opsi `Internal Auditor` pada dropdown Position
61. Pilih opsi `Supervisor` pada dropdown Position
62. Klik `[Apply]`
63. Verifikasi tabel menampilkan baris dengan Position `Internal Auditor` ATAU `Supervisor`: 4 baris `Citra Dewanti {runId}-109`, `Fitri Handayani {runId}-109`, `Hana Kusuma {runId}-109`, `Wahyu Hidayat {runId}-109`
64. Verifikasi baris dengan Position lain, mis. `Agus Prasetyo {runId}-109` dan `Bagas Santoso {runId}-109`, tidak tampil
65. Klik icon Filter
66. Klik `[Clear Field]`
67. Klik `[Apply]`

### TC-GS-USER-682: Search di dalam dropdown filter mempersempit opsi

68. Klik icon Filter
69. Buka dropdown Position
70. Ketik `PERVIS` pada kotak pencarian dropdown Position
71. Verifikasi opsi tersaring substring tanpa membedakan huruf besar kecil: hanya opsi `Supervisor` tampil
72. Ganti isi kotak pencarian dropdown Position dengan `zzz`
73. Verifikasi tidak ada opsi yang cocok dengan `zzz` (dropdown menampilkan `No results found`)
74. Hapus isi kotak pencarian dropdown Position

### TC-GS-USER-683: Hapus chip filter via (X) meng-uncheck opsi

75. Pilih opsi `Finance Manager` pada dropdown Position
76. Pilih opsi `Staff` pada dropdown Position
77. Verifikasi chip `Finance Manager` dan chip `Staff` tampil di field Position
78. Klik (X) pada chip `Finance Manager`
79. Verifikasi chip `Finance Manager` hilang
80. Verifikasi chip `Staff` tetap tampil
81. Buka dropdown Position
82. Verifikasi checkbox opsi `Finance Manager` di dropdown Position ter-uncheck

### TC-GS-USER-684: Uncheck opsi di dropdown menghapus chip

83. Klik `[Clear Field]`
84. Pilih opsi `Finance Manager` pada dropdown Position
85. Pilih opsi `Staff` pada dropdown Position
86. Buka dropdown Position, hilangkan centang opsi kedua `Staff`
87. Verifikasi chip `Staff` hilang
88. Verifikasi chip `Finance Manager` tetap tampil

### TC-GS-USER-685: Filter date range per field

89. Klik `[Clear Field]`
90. Pilih rentang tanggal `{L1}` sampai `{L1}` pada field `Last Update`
91. Verifikasi input field `Last Update` menampilkan tanggal dalam Date Format General Settings (`DD/MM/YY`)
92. Klik `[Apply]`
93. Verifikasi field Last Update: tabel hanya menampilkan 6 baris dalam rentang: `Agus Prasetyo {runId}-109`, `Bagas Santoso {runId}-109`, `Citra Dewanti {runId}-109`, `Dimas Pranoto {runId}-109`, `Eka Wulandari {runId}-109`, `Fitri Handayani {runId}-109`
94. Klik icon Filter
95. Klik `[Clear Field]`
96. Klik `[Apply]`
97. Klik icon Filter
98. Pilih rentang tanggal `{U1}` sampai `{U1}` pada field `Temporary Until`
99. Verifikasi input field `Temporary Until` menampilkan tanggal dalam Date Format General Settings (`DD/MM/YY`)
100. Klik `[Apply]`
101. Verifikasi field Temporary Until: tabel hanya menampilkan baris dalam rentang: `Citra Dewanti {runId}-109`
102. Klik icon Filter
103. Klik `[Clear Field]`
104. Klik `[Apply]`

### TC-GS-USER-686: Kombinasi 2 field filter digabung AND

105. Klik icon Filter
106. Pilih opsi `Staff` pada dropdown Position
107. Pilih opsi `Finance` pada dropdown Division
108. Klik `[Apply]`
109. Verifikasi tabel hanya menampilkan baris yang memenuhi Position `Staff` DAN Division `Finance`: `Nadia Rahma {runId}-109`
110. Verifikasi baris yang hanya memenuhi satu kriteria, mis. `Bagas Santoso {runId}-109` (Staff, General Affairs) dan `Agus Prasetyo {runId}-109` (Finance Manager, Finance), tidak tampil
111. Klik icon Filter
112. Klik `[Clear Field]`
113. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Holder dan 12 Non-Login User dipenuhi spec ini lewat seeding di hook `before`; spec tidak menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (678 sampai 686) dipertahankan; screening 678 dan 679 di awal sebelum TC yang menerapkan filter.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan Tab (langkah 1 sampai 3); `Klik icon Filter`, `[Clear Field]`, dan `[Apply]` di akhir tiap TC yang menerapkan filter (langkah 28 sampai 31 dan blok sejenis sesudah tiap kasus) supaya TC berikutnya mulai tanpa filter aktif; `Hapus isi kotak pencarian dropdown Position` sebelum TC-GS-USER-683; `[Clear Field]` sebelum TC-GS-USER-684 dan 685 (mengosongkan pilihan yang belum di-Apply).
- Langkah `Klik icon Filter` dituliskan sebelum `[Clear Field]` sesudah tiap `[Apply]`: panel Filter ditutup oleh `[Apply]` dan icon Filter dipakai untuk membukanya kembali.
- Anchor positif (S-03, bagian 8b butir 2): TC-GS-USER-679 memverifikasi opsi yang ada sebelum ketiadaan `HR Business Partner` dan `Logistics`; TC-GS-USER-681 dan 686 memverifikasi baris yang cocok sebelum ketiadaan baris lain; TC-GS-USER-682 memverifikasi opsi `Supervisor` tampil sebelum `zzz`.
- Nilai dan cakupan: TC-GS-USER-682 memakai `PERVIS` untuk membuktikan substring dan tidak case-sensitive sekaligus (cocok dengan `Supervisor`). TC-GS-USER-683 dan 684 memilih `Finance Manager` lalu `Staff`; chip pertama dan kedua mengikuti urutan pemilihan.
- Pembagian TC lintas spec: TC-GS-USER-400 sampai 403 (screening Tab, state kosong, navigasi) ada di spec 108 dan TC-GS-USER-404 (Download) ada di spec 113; TC-GS-USER-671 sampai 677 (Search) ada di spec 108; TC-GS-USER-687 sampai 691 (kombinasi Search dan Filter) ada di spec 110; TC-GS-USER-692 sampai 696, 714, dan 715 (Sort dan Pagination) ada di spec 111; TC-GS-USER-697 sampai 708 (Setup Column) ada di spec 112; TC-GS-USER-709 sampai 713 (Download) ada di spec 113.
- Spec melewati sekitar 35 langkah (113 langkah) karena sembilan TC berbagi satu layar (Filter Panel Tab Non-Login User), satu dataset (12 Non-Login User milik spec), dan satu kelas harness (fungsional). TC-GS-USER-680 menguji empat field dengan pola identik (pilih opsi, `[Apply]`, tiga `Verifikasi`, kosongkan filter), TC-GS-USER-685 dua field tanggal. Blok 678 dan 679 (screening) serta 680 sampai 686 berdiri sendiri dan memakai Tab yang sama; memisahkannya mengulang login, seeding 13 user, dan pembukaan Tab.
- Temuan untuk QA:
  - TC-GS-USER-678 sampai 686 menyebut tabel dan Name tanpa suffix; spec memakai holder dan Non-Login User milik spec bersuffix (S-06, S-11).
  - TC-GS-USER-678: PRD user.md §4.1.4 menyebut filter Custom Field aktif (curated) di Filter Panel tab ini; spec hanya mengasersi enam field yang disebut Expected TC dan tidak mengasersi ketiadaan field lain.
  - TC-GS-USER-679: TC tidak menyebut apakah dropdown yang terbuka tertutup saat dropdown berikutnya dibuka; spec membuka dropdown berurutan tanpa menutup.
  - TC-GS-USER-679: dropdown Status dan Temporary User hanya memuat dua nilai (Active/Inactive dan Yes/No) yang semuanya muncul di tabel, sehingga ketiadaan nilai tanpa baris tidak teramati pada kedua dropdown itu.
  - TC-GS-USER-680 dan 685: TC tidak menyatakan apakah Filter Panel menutup sesudah `[Apply]`; spec membuka kembali lewat icon Filter sebelum `[Clear Field]`.
  - TC-GS-USER-682: teks `No results found` di dalam dropdown diambil dari prd-conventions.md §9.8 (No Match); TC hanya menyebut "tidak ada opsi cocok".
  - TC-GS-USER-683 dan 684: TC tidak menyebut urutan chip; spec mengikuti urutan pemilihan opsi.
  - TC-GS-USER-685: Last Update diturunkan dari waktu entri Changelog terbaru, sehingga mengatur dua tanggal berbeda pada seed tidak punya cara yang disebut TC, PRD, atau LLD; disediakan tim FE/BE. Kolom Temporary Until memakai tanggal Temporary Until seed, tanpa kemampuan tambahan.
  - Mekanisme seeding Login User dan Non-Login User (Represented By, Employee ID, Position, Division, Temporary Until) dan penghapusan sisa tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
