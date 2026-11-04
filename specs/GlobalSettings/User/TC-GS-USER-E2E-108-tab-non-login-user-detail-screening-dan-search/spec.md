---
id: TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search
title: "Tab Non-Login User Detail: screening, state kosong, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-400
  - TC-GS-USER-401
  - TC-GS-USER-402
  - TC-GS-USER-403
  - TC-GS-USER-671
  - TC-GS-USER-672
  - TC-GS-USER-673
  - TC-GS-USER-674
  - TC-GS-USER-675
  - TC-GS-USER-676
  - TC-GS-USER-677
coverage:
  web: automated
---

# Tab Non-Login User Detail: screening, state kosong, dan Search

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup; satu-satunya state yang diubah adalah visibilitas kolom curated (dipulihkan).
- Akun: Total Control, `Siti Nurhaliza`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): `Dewi Lestari` (Tabel Data Uji Pre-setup No. 12, tidak mewakili Non-Login User mana pun) untuk TC-GS-USER-402; Master Data Position (`Finance Manager`, `Staff`, `Supervisor`, `Internal Auditor`) dan Division (`Finance`, `General Affairs`, `Legal`) Pre-setup No. 22 dan 23 sebagai nilai seed.
- Data Dinamis, holder: Login User milik spec `Ahmad Fauzi {runId}-108` (email `ahmadfauzi+{runId}-108@qwertysystem.net`, status Activated, Access Global Settings) sebagai Represented By seluruh Non-Login User di bawah. Holder milik spec dipakai, bukan `Ahmad Fauzi` Pre-setup (Tabel Data Uji Pre-setup No. 13) beserta `Agus Prasetyo` dan `Lina Marlina` Pre-setup (No. 21), karena S-06 melarang mengubah data Pre-setup bersama dan S-11 menuntut data dengan lebih dari satu halaman serta sedikitnya dua nilai distinct pada kolom yang diuji.
- Data Dinamis, 12 Non-Login User milik spec (Represented By = `Ahmad Fauzi {runId}-108`), di-seed di hook `before`. Tabel memuat 12 baris: halaman 1 berisi 10 baris dan total 2 halaman. Nilai Name, Email, dan Employee ID bersuffix `{runId}-108`; Last Update seluruh baris = waktu seeding; `{U1}` dan `{U2}` pada kolom Temporary Until adalah tanggal hari uji + 30 hari dan hari uji + 60 hari, ditampilkan dalam Date Format General Settings.
  | Name | Email | Employee ID | Position | Division | Active | Temporary User | Temporary Until |
  |---|---|---|---|---|---|---|---|
  | `Agus Prasetyo {runId}-108` | `nlu01+{runId}-108@qwertysystem.net` | `EMP-AGS-{runId}-108` | Finance Manager | Finance | Active | No | kosong |
  | `Bagas Santoso {runId}-108` | `nlu02+{runId}-108@qwertysystem.net` | `EMP-BGS-{runId}-108` | Staff | General Affairs | Active | No | kosong |
  | `Citra Dewanti {runId}-108` | `nlu03+{runId}-108@qwertysystem.net` | `EMP-CTR-{runId}-108` | Supervisor | Finance | Active | Yes | `{U1}` (hari uji + 30 hari) |
  | `Dimas Pranoto {runId}-108` | `nlu04+{runId}-108@qwertysystem.net` | `EMP-DMS-{runId}-108` | Staff | General Affairs | Active | No | kosong |
  | `Eka Wulandari {runId}-108` | `nlu05+{runId}-108@qwertysystem.net` | `EMP-EKA-{runId}-108` | Finance Manager | Legal | Active | No | kosong |
  | `Fitri Handayani {runId}-108` | `nlu06+{runId}-108@qwertysystem.net` | `EMP-FTR-{runId}-108` | Internal Auditor | Finance | Active | Yes | `{U2}` (hari uji + 60 hari) |
  | `Galih Permadi {runId}-108` | `nlu07+{runId}-108@qwertysystem.net` | `EMP-GLH-{runId}-108` | Staff | Legal | Active | No | kosong |
  | `Hana Kusuma {runId}-108` | `nlu08+{runId}-108@qwertysystem.net` | `EMP-HNA-{runId}-108` | Supervisor | General Affairs | Active | No | kosong |
  | `Lina Marlina {runId}-108` | `nlu09+{runId}-108@qwertysystem.net` | kosong | kosong | Legal | Inactive | No | kosong |
  | `Nadia Rahma {runId}-108` | `nlu10+{runId}-108@qwertysystem.net` | `EMP-NDR-{runId}-108` | Staff | Finance | Active | No | kosong |
  | `Rizky Fadillah {runId}-108` | `nlu11+{runId}-108@qwertysystem.net` | `EMP-RZK-{runId}-108` | Finance Manager | General Affairs | Inactive | No | kosong |
  | `Wahyu Hidayat {runId}-108` | `nlu12+{runId}-108@qwertysystem.net` | `EMP-WHY-{runId}-108` | Supervisor | Legal | Active | No | kosong |

  Keyword Search ditulis dari sisi nama (`Prasetyo`), Email (`nlu03`), Employee ID (`EMP-DMS`), Position (`Auditor`), dan Division (`General`); tiap keyword mencocokkan satu kolom saja pada data di atas.
- Kemampuan teknis (disediakan tim FE/BE; endpoint ditentukan tim FE di tahap script): seeding Login User holder dan Non-Login User dengan Represented By = holder lewat API di hook `before`; cleanup di hook `after` menghapus Non-Login User lalu holder lewat API tanpa berasumsi seeding berhasil penuh. Seeding menambah 13 user pada hitungan Master Data Count Limit gabungan Login + Non-Login User; nilai limit environment cukup besar untuk itu.
- Data uji per TC: TC-GS-USER-671 keyword `Agus`; TC-GS-USER-672 `  AGUS  `; TC-GS-USER-673 `Prasetyo`, `nlu03`, `EMP-DMS`, `Auditor`, `General`; TC-GS-USER-674 `active`, `Inactive`, `Ye`; TC-GS-USER-675 teks Last Update dan Temporary Until baris `Citra Dewanti` yang dibaca dari tabel; TC-GS-USER-676 `General`; TC-GS-USER-677 `zzzqqq`.
- Date Format General Settings default environment (`DD/MM/YY`); spec tidak mengubahnya.
- Kolom `Temporary User` dan `Temporary Until` adalah Curated (default unchecked, PRD user.md §4.1.4) sehingga tidak tampil di awal spec; keduanya ditampilkan lewat Overlay Column Visibility pada TC-GS-USER-674 dan disembunyikan kembali sebelum TC-GS-USER-401. Preferensi kolom tersimpan di browser (PRD prd-conventions.md §9.3); hook `after` mengembalikan preferensi kolom Tab Non-Login User ke default.
- State yang diubah dan dipulihkan: visibilitas kolom Temporary User dan Temporary Until (dikembalikan tersembunyi di langkah 104 sampai 107), Search (ditutup dengan icon ←); hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data Pre-setup bersama (S-06).
- Kemampuan teknis: membaca teks sel tabel; menekan Esc untuk menutup Overlay Column Visibility; membaca jumlah baris dan jumlah halaman pada footer pagination.

## Test Steps

### TC-GS-USER-402: Empty state Tab Non-Login User

1. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
2. Klik Name `Dewi Lestari` di User List
3. Klik Tab `Non-Login User`
4. Verifikasi ilustrasi empty state tampil
5. Verifikasi judul empty state `No non-login users represented`
6. Verifikasi deskripsi empty state `This user does not represent any non-login users.`

### TC-GS-USER-400: Screening Tab Non-Login User di Detail

7. Buka Global Settings > User > User List (sub-tab Login User)
8. Klik icon Search, ketik `Ahmad Fauzi {runId}-108`, tekan Enter
9. Klik Name `Ahmad Fauzi {runId}-108` di User List
10. Klik Tab `Non-Login User`
11. Verifikasi label tab `Non-Login User` menampilkan badge count `12`
12. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`
13. Verifikasi toolbar tidak memuat Changelog dan tidak memuat Create
14. Verifikasi header kolom berurutan: `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`, `Column Visibility (⋯)`
15. Verifikasi header kolom `Name` sortable
16. Verifikasi tabel terurut default Name A-Z: halaman 1 berisi `Agus Prasetyo {runId}-108`, `Bagas Santoso {runId}-108`, `Citra Dewanti {runId}-108`, `Dimas Pranoto {runId}-108`, `Eka Wulandari {runId}-108`, `Fitri Handayani {runId}-108`, `Galih Permadi {runId}-108`, `Hana Kusuma {runId}-108`, `Lina Marlina {runId}-108`, `Nadia Rahma {runId}-108`
17. Verifikasi kolom `Active` menampilkan badge: baris `Agus Prasetyo {runId}-108` berbadge `Active`
18. Verifikasi baris `Lina Marlina {runId}-108` menampilkan Employee ID `—`
19. Verifikasi baris `Lina Marlina {runId}-108` menampilkan Position `—`
20. Verifikasi baris `Lina Marlina {runId}-108` berbadge `Inactive`
21. Klik icon Search
22. Verifikasi input Search kosong dengan placeholder `Search name, email, or employee ID...`
23. Klik icon (←)

### TC-GS-USER-671: Siklus Search: reveal, Enter, clear (✕), collapse ←

24. Klik icon Search
25. Verifikasi Search bar melebar
26. Verifikasi kursor auto-focus di input Search
27. Ketik `Agus` pada kotak Search
28. Verifikasi tabel belum tersaring (12 baris: halaman 1 berisi 10 baris, total 2 halaman)
29. Verifikasi icon (✕) muncul di dalam input
30. Tekan Enter
31. Verifikasi tabel hanya menampilkan baris `Agus Prasetyo {runId}-108`
32. Klik icon (✕)
33. Verifikasi input Search kosong
34. Verifikasi tabel tetap menampilkan hasil search terakhir (hanya baris `Agus Prasetyo {runId}-108`)
35. Tekan Enter pada input kosong
36. Verifikasi tabel kembali menampilkan seluruh data (12 baris, total 2 halaman)
37. Isi Search dengan `Agus`, tekan Enter
38. Klik icon ←
39. Verifikasi Search bar menutup menjadi icon Search biasa
40. Verifikasi tabel langsung kembali menampilkan seluruh data tanpa menekan Enter (12 baris, total 2 halaman)
41. Klik icon Search
42. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-USER-672: Query Search di-trim dan tidak case-sensitive

43. Isi Search dengan `  AGUS  `, tekan Enter
44. Verifikasi tabel hanya menampilkan baris `Agus Prasetyo {runId}-108` (spasi diabaikan, huruf besar/kecil tidak dibedakan)
45. Verifikasi isi kotak Search tetap `  AGUS  ` apa adanya

### TC-GS-USER-673: Search menemukan substring pada kolom kelas teks

46. Ganti isi kotak search dengan `Prasetyo`, tekan Enter
47. Verifikasi kolom Name: tabel hanya menampilkan baris `Agus Prasetyo {runId}-108` (Name memuat `Prasetyo`)
48. Klik icon (✕)
49. Isi Search dengan `nlu03`, tekan Enter
50. Verifikasi kolom Email: tabel hanya menampilkan baris `Citra Dewanti {runId}-108` (Email `nlu03+{runId}-108@qwertysystem.net` memuat `nlu03`)
51. Klik icon (✕)
52. Isi Search dengan `EMP-DMS`, tekan Enter
53. Verifikasi kolom Employee ID: tabel hanya menampilkan baris `Dimas Pranoto {runId}-108` (Employee ID memuat `EMP-DMS`)
54. Klik icon (✕)
55. Isi Search dengan `Auditor`, tekan Enter
56. Verifikasi kolom Position: tabel hanya menampilkan baris `Fitri Handayani {runId}-108` (Position `Internal Auditor` memuat `Auditor`)
57. Klik icon (✕)
58. Isi Search dengan `General`, tekan Enter
59. Verifikasi kolom Division: tabel hanya menampilkan 4 baris dengan Division `General Affairs`: `Bagas Santoso {runId}-108`, `Dimas Pranoto {runId}-108`, `Hana Kusuma {runId}-108`, `Rizky Fadillah {runId}-108`
60. Klik icon (✕)

### TC-GS-USER-674: Search kolom Active exact match dan kolom Temporary User substring

61. Isi Search dengan `active`, tekan Enter
62. Verifikasi kolom Active exact match tidak case-sensitive: tabel menampilkan 10 baris berstatus Active dalam satu halaman
63. Verifikasi baris Inactive `Lina Marlina {runId}-108` dan `Rizky Fadillah {runId}-108` tidak tampil
64. Klik icon (✕)
65. Isi Search dengan `Inactive`, tekan Enter
66. Verifikasi keyword `Inactive` hanya menampilkan baris Inactive: `Lina Marlina {runId}-108` dan `Rizky Fadillah {runId}-108`
67. Klik icon (✕)
68. Klik header kolom Column Visibility (⋯)
69. Centang kolom `Temporary User`
70. Centang kolom `Temporary Until`
71. Tutup Overlay Column Visibility dengan menekan Esc
72. Isi Search dengan `Ye`, tekan Enter
73. Verifikasi kolom Temporary User: tabel hanya menampilkan baris dengan Temporary User `Yes`: `Citra Dewanti {runId}-108` dan `Fitri Handayani {runId}-108`
74. Klik icon (✕)

### TC-GS-USER-675: Kolom non-searchable tidak tercakup Search

75. Verifikasi baris `Citra Dewanti {runId}-108` tampil di tabel
76. Baca teks Last Update dan teks Temporary Until pada baris `Citra Dewanti {runId}-108`
77. Isi Search dengan teks Last Update tersebut, tekan Enter
78. Verifikasi kolom Last Update: tabel menampilkan no result state `No results found`
79. Klik icon (✕)
80. Tekan Enter pada input kosong
81. Verifikasi tabel kembali menampilkan seluruh data (12 baris, total 2 halaman)
82. Isi Search dengan teks Temporary Until tersebut, tekan Enter
83. Verifikasi kolom Temporary Until: tabel menampilkan no result state `No results found`
84. Klik icon (✕)

### TC-GS-USER-676: Search tidak mencocokkan kolom yang di-hide, cocok kembali setelah unhide

85. Isi Search dengan `General`, tekan Enter
86. Verifikasi baris dengan Division `General Affairs` tampil: `Bagas Santoso {runId}-108`, `Dimas Pranoto {runId}-108`, `Hana Kusuma {runId}-108`, `Rizky Fadillah {runId}-108`
87. Klik header kolom Column Visibility (⋯)
88. Hilangkan centang kolom `Division`
89. Tutup Overlay Column Visibility dengan menekan Esc
90. Klik input Search, tekan Enter
91. Verifikasi saat Division hidden: tabel menampilkan no result state `No results found`
92. Klik header kolom Column Visibility (⋯)
93. Centang kolom `Division`
94. Tutup Overlay Column Visibility dengan menekan Esc
95. Klik input Search, tekan Enter
96. Verifikasi setelah Division di-unhide: 4 baris dengan Division `General Affairs` kembali cocok: `Bagas Santoso {runId}-108`, `Dimas Pranoto {runId}-108`, `Hana Kusuma {runId}-108`, `Rizky Fadillah {runId}-108`
97. Klik icon ←

### TC-GS-USER-677: Empty filtered state

98. Verifikasi tabel menampilkan seluruh data (12 baris, total 2 halaman) sebelum Search
99. Klik icon Search, ketik `zzzqqq`, tekan Enter
100. Verifikasi ilustrasi empty filtered state tampil
101. Verifikasi judul empty filtered state `No results found`
102. Verifikasi deskripsi empty filtered state `Try adjusting your search or filter.`
103. Klik icon ←
104. Klik header kolom Column Visibility (⋯)
105. Hilangkan centang kolom `Temporary User`
106. Hilangkan centang kolom `Temporary Until`
107. Tutup Overlay Column Visibility dengan menekan Esc

### TC-GS-USER-401: Klik Name di Tab Non-Login User membuka Detail Non-Login User

108. Klik Name `Agus Prasetyo {runId}-108`
109. Verifikasi navigasi ke Detail Non-Login User `Agus Prasetyo {runId}-108`

### TC-GS-USER-403: Tab Non-Login User tidak muncul di Detail Non-Login User

110. Buka Global Settings > User > User List (sub-tab Login User)
111. Klik sub-tab `Non-Login User`
112. Klik icon Search, ketik `Agus Prasetyo {runId}-108`, tekan Enter
113. Klik Name `Agus Prasetyo {runId}-108`
114. Verifikasi halaman Detail Non-Login User `Agus Prasetyo {runId}-108` tampil
115. Verifikasi Tab `Non-Login User` tidak dirender

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Holder dan 12 Non-Login User dipenuhi spec ini lewat seeding di hook `before`; spec tidak menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 402 (empty state, memakai user Pre-setup lain), 400 (screening), 671 sampai 677 (Search, satu pembukaan Tab), lalu 401 dan 403 di akhir karena keduanya berpindah ke Detail Non-Login User dan meninggalkan Tab. Urutan di `tc-user.md`: 400, 401, 402, 403, 671 sampai 677.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 110 (membuka ulang User List supaya Search User List dalam keadaan awal; retensi Search saat kembali ke list belum diputuskan PRD, Open Item Filter Persistence), pencarian holder di User List pada tiap pembukaan, langkah 68 sampai 71 dan 104 sampai 107 (menampilkan dan menyembunyikan kolom curated), langkah membaca teks Last Update dan Temporary Until, serta penutupan Search dengan icon (✕) dan ← di antara kasus, dan langkah 21 dan 23 (membuka dan menutup Search untuk memverifikasi placeholder TC-GS-USER-400).
- Anchor positif (S-03, bagian 8b butir 2): `Verifikasi` baris `Citra Dewanti {runId}-108` tampil mendahului asersi `No results found` pada TC-GS-USER-675; `Verifikasi` 12 baris kembali mendahului asersi Temporary Until pada TC-GS-USER-675 dan asersi `No results found` pada TC-GS-USER-677; `Verifikasi` baris Active mendahului asersi ketiadaan baris Inactive pada TC-GS-USER-674. Anchor ini tidak ada di Expected TC.
- Keyword dan nilai: kolom Temporary User dicari dengan `Ye` (potongan `Yes`); kolom Name dengan `Prasetyo`. Sel Last Update dan Temporary Until dibaca dari baris `Citra Dewanti`, satu-satunya baris yang memuat Temporary Until pada kumpulan baris hasil `Ye`.
- Pembagian TC lintas spec: TC-GS-USER-404 dan 709 sampai 713 (Download) ada di spec 113; TC-GS-USER-678 sampai 686 (Filter Panel) ada di spec 109; TC-GS-USER-687 sampai 691 (kombinasi Search dan Filter) ada di spec 110; TC-GS-USER-692 sampai 696, 714, dan 715 (Sort dan Pagination) ada di spec 111; TC-GS-USER-697 sampai 708 (Setup Column) ada di spec 112.
- Spec melewati sekitar 35 langkah (115 langkah) karena sebelas TC berbagi satu layar (Tab Non-Login User di Detail), satu dataset (12 Non-Login User milik spec), dan satu kelas harness (fungsional). Blok Search 671 sampai 677 berdiri sendiri (kegagalan satu blok tidak menghapus makna blok lain) dan memakai kotak Search yang sama, sehingga satu pembukaan Tab dipakai bersama; memisahkannya mengulang login, seeding 13 user, dan pembukaan Tab. Blok 673 menguji lima kolom dengan pola identik (keyword, `Verifikasi`, clear).
- Temuan untuk QA:
  - TC-GS-USER-400 Expected a: badge count `2` mengacu ke data Pre-setup (`Agus Prasetyo` Active dan `Lina Marlina` Inactive). Holder milik spec mewakili 12 Non-Login User (10 Active, 2 Inactive), sehingga spec mengasersi `12`.
  - TC-GS-USER-400, 401, 403 menyebut Name `Ahmad Fauzi` dan `Agus Prasetyo` tanpa suffix; spec memakai holder dan Non-Login User milik spec bersuffix (S-06, S-11).
  - TC-GS-USER-400 Expected c: PRD user.md §4.1.4 menyebut kolom Custom Field aktif (Pre-setup No. 24: `Blood Type`, `Skills`, `Emergency Phone`) sebagai curated pada tab ini; spec mengasersi daftar kolom default tanpa kolom curated.
  - TC-GS-USER-674 dan 675: kolom Temporary User dan Temporary Until bersifat Curated dan tersembunyi secara default, sedangkan Search tidak mencocokkan kolom hidden (TC-GS-USER-676). TC tidak menyebut langkah menampilkan kolom itu; spec menambahkannya sebagai langkah penghubung.
  - TC-GS-USER-675: TC tidak menyebut baris mana yang dibaca nilai Last Update dan Temporary Until-nya; spec membaca baris `Citra Dewanti`.
  - TC-GS-USER-676: TC tidak menyebut nilai yang hanya ada di kolom Division; spec memakai `General` (Division `General Affairs`). Setelah kolom di-hide atau di-unhide, spec menekan Enter lagi di input yang sama sesuai langkah 6 TC.
  - TC-GS-USER-403: TC tidak menyebut tab apa saja yang ada di Detail Non-Login User; spec mengasersi Detail tampil lalu ketiadaan Tab `Non-Login User`.
  - TC-GS-USER-402: `Dewi Lestari` Pre-setup dibaca tanpa diubah; TC tidak menyebut teks pada Tab selain empty state.
  - Cara menutup Overlay Column Visibility tidak didefinisikan di TC maupun PRD; spec memakai Esc.
  - Mekanisme seeding Login User dan Non-Login User (Represented By, Employee ID, Position, Division, Temporary Until) dan penghapusan sisa tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
