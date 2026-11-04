---
id: TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Sub-tab Pending Tasks: Filter Panel (Opsi, Multi-select, OR, Dropdown Search, Chip, Rentang, AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-837
  - TC-GS-USER-838
  - TC-GS-USER-839
  - TC-GS-USER-840
  - TC-GS-USER-841
  - TC-GS-USER-842
  - TC-GS-USER-843
  - TC-GS-USER-844
  - TC-GS-USER-845
  - TC-GS-USER-846
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Filter Panel (Opsi, Multi-select, OR, Dropdown Search, Chip, Rentang, AND)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data User; yang di-seed hanya task pending FAMS milik spec (Population PT-22).
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List (sub-tab Login User) dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat `B0` + 22 baris sesudah seeding, dengan `B0` = jumlah task pending Pre-setup Ahmad Fauzi yang dibaca lewat kemampuan baca BE tepat sebelum seeding; kemampuan itu disediakan tim FE/BE). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC task seed memakai Group dan user FAMS yang disediakan tim FE/BE dan bernama bersuffix `{runId}-133` (`{group-A}` = `Alfa {runId}-133`, `{group-B}` = `Beta {runId}-133`; PIC `{pic-A}` nama lengkap `Rina Pica {runId}-133`, `{pic-B}` nama lengkap `Sari Picb {runId}-133`; teks tampil sel PIC `[First Name] [Last Initial]`: `{pic-A-tampil}` = `Rina P`, `{pic-B-tampil}` = `Sari P`, dua nilai berbeda; asersi sel dan sort kolom PIC memakai nilai tampil, nama lengkap hanya untuk Search dan hover), sehingga tidak bentrok dengan task Pre-setup. Task Pre-setup Ahmad Fauzi (`B0` baris) tidak diubah dan isinya tidak diasumsikan: asersi jumlah per nilai Group atau PIC memakai nama bersuffix itu, sedangkan asersi per nilai Transaction, Status, Total Asset, Request Date, atau Last Updated menyebut baris seed (task milik spec ini). Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A-tampil}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1a | 6 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B-tampil}` | `3` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q1b | 6 | `Borrowing` | `Waiting for Confirmation` | `{group-C}` | `{pic-B-tampil}` | `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B-tampil}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}`, `{group-B}` lebih kecil dari `{group-C}` (`Gamma {runId}-133`), dan `{pic-A-tampil}` lebih kecil dari `{pic-B-tampil}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (`lfa {runId}-133`, potongan `{group-A}`) dan `{kw-pic}` (`Pica {runId}-133`, potongan nama lengkap `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan (baris seed): Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris, `{group-B}` 6 baris, dan `{group-C}` 6 baris (tiga nilai Group distinct untuk TC-GS-USER-840); PIC `{pic-A-tampil}` 8 baris dan `{pic-B-tampil}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; total tabel `B0` + 22 baris sehingga page size 10 menghasilkan sedikitnya 3 halaman.
- Data uji per TC: TC-GS-USER-838 dropdown `Transaction`, `Status`, `Group`, `PIC`; TC-GS-USER-839 opsi `Assignment` (Transaction), `Waiting for Confirmation` (Status), `{group-A}` (Group), `{pic-A}` (PIC); TC-GS-USER-840 opsi `{group-A}` dan `{group-B}` pada Group; TC-GS-USER-841 keyword dropdown `borrow` lalu `zzz`; TC-GS-USER-842 dan 843 opsi `Assignment` dan `Borrowing` pada Transaction; TC-GS-USER-844 rentang `{rd-1}` sampai `{rd-1}` (Request Date) dan `{lu-1}` sampai `{lu-1}` (Last Updated); TC-GS-USER-845 Min `1` Max `2`; TC-GS-USER-846 Transaction `Borrowing` dan Group `{group-A}`.
- Date Format General Settings tidak diubah spec (nilai default environment); `{rd-1}` dan `{lu-1}` ditulis dalam format itu.
- Kemampuan teknis: memilih opsi dan menghapus chip di dropdown multi-select searchable; memilih rentang tanggal pada date range picker; mengisi field Min dan Max; membaca teks tanggal pada input date range; seeding task pending FAMS dan pembersihannya (di atas).
- State yang diubah dan dipulihkan: kriteria Filter dikosongkan lewat `[Clear Field]` dan `[Apply]` di akhir tiap blok dan di langkah 126; hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-837: Screening Filter Panel

1. Klik icon Search di User List, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Tasks`
5. Klik icon Filter
6. Verifikasi Filter Panel terbuka
7. Verifikasi field `Transaction` bertipe multi-select searchable dengan placeholder `All transactions`
8. Verifikasi field `Status` bertipe multi-select searchable dengan placeholder `All statuses`
9. Verifikasi field `Group` bertipe multi-select searchable dengan placeholder `All groups`
10. Verifikasi field `PIC` bertipe multi-select searchable dengan placeholder `All PICs`
11. Verifikasi field `Request Date` bertipe date range picker dengan placeholder `Select date`
12. Verifikasi field `Last Updated` bertipe date range picker dengan placeholder `Select date`
13. Verifikasi field `Total Asset` bertipe number range dengan placeholder `Min` dan `Max`
14. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-838: Opsi dropdown filter diambil dari nilai yang ada di tabel

15. Buka dropdown `Transaction`
16. Verifikasi dropdown `Transaction` hanya memuat opsi `Assignment` dan `Borrowing` (nilai yang ada di baris tabel; tidak ada opsi lain)
17. Tutup dropdown `Transaction`
18. Buka dropdown `Status`
19. Verifikasi dropdown `Status` hanya memuat opsi `Waiting for Acceptance` dan `Waiting for Confirmation` (tidak ada opsi lain)
20. Tutup dropdown `Status`
21. Buka dropdown `Group`
22. Verifikasi dropdown `Group` memuat opsi `{group-A}`, `{group-B}`, dan `{group-C}` (nilai baris seed)
23. Tutup dropdown `Group`
24. Buka dropdown `PIC`
25. Verifikasi dropdown `PIC` memuat opsi `{pic-A}` dan `{pic-B}` (nilai baris seed)
26. Tutup dropdown `PIC`

### TC-GS-USER-839: Filter multi-select per field menyaring baris

27. Pilih opsi `Assignment` pada dropdown `Transaction`
28. Klik `[Apply]`
29. Verifikasi tabel hanya menampilkan baris Transaction `Assignment` (termasuk 8 baris seed)
30. Verifikasi badge titik tampil pada icon Filter (filter ter-Apply)
31. Klik icon Filter
32. Verifikasi icon Filter gelap (panel terbuka)
33. Klik `[Clear Field]`
34. Klik `[Apply]`
35. Klik icon Filter
36. Pilih opsi `Waiting for Confirmation` pada dropdown `Status`
37. Klik `[Apply]`
38. Verifikasi tabel hanya menampilkan baris Status `Waiting for Confirmation` (termasuk 14 baris seed)
39. Verifikasi badge titik tampil pada icon Filter (filter ter-Apply)
40. Klik icon Filter
41. Verifikasi icon Filter gelap (panel terbuka)
42. Klik `[Clear Field]`
43. Klik `[Apply]`
44. Klik icon Filter
45. Pilih opsi `{group-A}` pada dropdown `Group`
46. Klik `[Apply]`
47. Verifikasi tabel hanya menampilkan 10 baris Group `{group-A}`
48. Verifikasi badge titik tampil pada icon Filter (filter ter-Apply)
49. Klik icon Filter
50. Verifikasi icon Filter gelap (panel terbuka)
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Klik icon Filter
54. Pilih opsi `{pic-A}` pada dropdown `PIC`
55. Klik `[Apply]`
56. Verifikasi tabel hanya menampilkan 8 baris PIC `{pic-A-tampil}`
57. Verifikasi badge titik tampil pada icon Filter (filter ter-Apply)
58. Klik icon Filter
59. Verifikasi icon Filter gelap (panel terbuka)
60. Klik `[Clear Field]`
61. Klik `[Apply]`

### TC-GS-USER-840: Dua opsi dalam satu field filter digabung OR

62. Klik icon Filter
63. Pilih opsi `{group-A}` pada dropdown `Group`
64. Pilih opsi `{group-B}` pada dropdown `Group`
65. Klik `[Apply]`
66. Verifikasi tabel menampilkan baris Group `{group-A}` (opsi 1)
67. Verifikasi tabel menampilkan baris Group `{group-B}` (opsi 2)
68. Verifikasi baris Group `{group-C}` tidak tampil (opsi ketiga)
69. Klik icon Filter
70. Klik `[Clear Field]`
71. Klik `[Apply]`

### TC-GS-USER-841: Search di dalam dropdown filter mempersempit opsi

72. Klik icon Filter
73. Buka dropdown `Transaction`
74. Ketik `borrow` pada kotak cari di dalam dropdown
75. Verifikasi dropdown hanya menampilkan opsi `Borrowing` (tersaring substring, tidak membedakan huruf besar kecil)
76. Ganti isi kotak cari di dalam dropdown dengan `zzz`
77. Verifikasi dropdown tidak menampilkan opsi yang cocok
78. Kosongkan kotak cari di dalam dropdown dan tutup dropdown `Transaction`

### TC-GS-USER-842: Hapus chip filter via (X) meng-uncheck opsi

79. Pilih opsi `Assignment` pada dropdown `Transaction`
80. Pilih opsi `Borrowing` pada dropdown `Transaction`
81. Tutup dropdown `Transaction`
82. Klik (X) pada chip pertama (`Assignment`)
83. Verifikasi chip `Assignment` hilang
84. Verifikasi chip `Borrowing` tetap tampil
85. Buka dropdown `Transaction`
86. Verifikasi checkbox opsi `Assignment` di dropdown ter-uncheck

### TC-GS-USER-843: Uncheck opsi di dropdown menghapus chip

87. Pilih opsi `Assignment` pada dropdown `Transaction` (opsi kedua setelah `Borrowing`)
88. Hilangkan centang opsi `Assignment` di dropdown `Transaction`
89. Verifikasi chip `Assignment` hilang
90. Verifikasi chip `Borrowing` tetap tampil
91. Tutup dropdown `Transaction`
92. Klik `[Clear Field]`

### TC-GS-USER-844: Filter date range per field

93. Pilih rentang tanggal `{rd-1}` sampai `{rd-1}` pada field `Request Date`
94. Verifikasi teks tanggal pada input `Request Date` mengikuti Date Format General Settings
95. Klik `[Apply]`
96. Verifikasi tabel hanya menampilkan baris dengan Request Date `{rd-1}` (termasuk 8 baris seed)
97. Klik icon Filter
98. Klik `[Clear Field]`
99. Klik `[Apply]`
100. Klik icon Filter
101. Pilih rentang tanggal `{lu-1}` sampai `{lu-1}` pada field `Last Updated`
102. Verifikasi teks tanggal pada input `Last Updated` mengikuti Date Format General Settings
103. Klik `[Apply]`
104. Verifikasi tabel hanya menampilkan baris dengan Last Updated `{lu-1}` (termasuk 10 baris seed)
105. Klik icon Filter
106. Klik `[Clear Field]`
107. Klik `[Apply]`

### TC-GS-USER-845: Filter number range Min/Max

108. Klik icon Filter
109. Isi `Total Asset` Min dengan `1`
110. Isi `Total Asset` Max dengan `2`
111. Klik `[Apply]`
112. Verifikasi tabel hanya menampilkan baris bernilai Total Asset `1` dan `2` (termasuk 6 baris seed bernilai `1` dan 4 baris seed bernilai `2`)
113. Verifikasi baris dengan Total Asset `3` dan `10` tidak tampil
114. Klik icon Filter
115. Klik `[Clear Field]`
116. Klik `[Apply]`

### TC-GS-USER-846: Kombinasi 2 field filter digabung AND

117. Klik icon Filter
118. Pilih opsi `Borrowing` pada dropdown `Transaction`
119. Pilih opsi `{group-A}` pada dropdown `Group`
120. Klik `[Apply]`
121. Verifikasi tabel hanya menampilkan 2 baris Transaction `Borrowing` dengan Group `{group-A}`
122. Verifikasi baris Transaction `Assignment` dengan Group `{group-A}` tidak tampil
123. Verifikasi baris Transaction `Borrowing` dengan Group `{group-B}` tidak tampil
124. Klik icon Filter
125. Klik `[Clear Field]`
126. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (837 sampai 846) dipertahankan; TC-GS-USER-837 (screening) di awal.
- Langkah 1 sampai 4 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Filter Panel yang terbuka pada TC-GS-USER-837 dipakai TC-GS-USER-838 dan blok pertama TC-GS-USER-839; TC-GS-USER-842 dan 843 memakai panel yang dibuka pada TC-GS-USER-841, dan TC-GS-USER-844 memakai panel dari TC-GS-USER-843 (langkah "Klik icon Filter" masing-masing TC sumber dipenuhi panel yang masih terbuka).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List agar Name dapat diklik, bagian 8b butir 12), langkah 17 sampai 26 (menutup dropdown setelah dibaca), langkah 78 (mengosongkan kotak cari dan menutup dropdown), langkah 92 (`[Clear Field]` tanpa `[Apply]` sehingga Filter Panel tetap terbuka dan tidak ada kriteria tersisa), serta rangkaian "Klik icon Filter, `[Clear Field]`, `[Apply]`" di akhir tiap blok TC-GS-USER-839, 840, 844, 845, dan 846 (mengosongkan Filter sebelum TC berikutnya, S-09). Klik icon Filter sebelum pemilihan opsi pada TC-GS-USER-839 sampai 846 membuka kembali Filter Panel yang tertutup setelah `[Apply]`.
- TC-GS-USER-838, 841, 842, dan 843 tidak menekan `[Apply]`; kriteria yang dipilih TC-GS-USER-842 dan 843 dibuang lewat `[Clear Field]` (langkah 86) dan tidak pernah di-Apply, sehingga tabel tidak berubah.
- Asersi tambahan (S-03, dengan alasan): pasangan `Verifikasi` "baris nilai lain tidak tampil" pada TC-GS-USER-845 dan 846 memenuhi S-11 (dua nilai distinct pada kolom yang difilter) dan didahului `Verifikasi` baris yang tampil sebagai anchor (bagian 8b butir 2); jumlah baris seed pada Expected TC-GS-USER-839, 844, 845, dan 846 adalah konkretisasi "hanya baris dengan nilai terpilih/dalam rentang tampil" dari Population PT-22; baris Pre-setup (`B0`) tidak dihitung. `Verifikasi` badge titik dan icon Filter gelap pada TC-GS-USER-839 mengikuti Expected TC (icon gelap saat panel terbuka, badge titik selama filter ter-Apply).
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 (screening dan Search) ada di spec 132; TC-GS-USER-847 sampai 851 (kombinasi Search dan Filter, Clear, filter kolom hidden) ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 ada di spec 135; TC-GS-USER-855 sampai 863 ada di spec 136; TC-GS-USER-398 dan 864 sampai 868 ada di spec 137. TC filter sub-tab Pending Approvals ada di spec 127.
- Spec melewati sekitar 35 langkah (126 langkah) karena sepuluh TC Filter Panel berbagi satu layar, satu dataset (PT-22), dan satu kelas harness (fungsional); tiap blok TC berdiri sendiri dan Filter dikosongkan di antara blok, sehingga satu kegagalan tidak membuat blok lain kehilangan makna. TC-GS-USER-839 menguji empat field dengan blok identik (pilih opsi, `[Apply]`, dua `Verifikasi`, kosongkan Filter) dan rangkaian "Klik icon Filter, `[Clear Field]`, `[Apply]`" merupakan prefix berulang.
- Temuan untuk QA:
  - Sel PIC menampilkan `[First Name] [Last Initial]` (PRD `user.md` §4.1.3); asersi sel tabel langkah 56 memakai `{pic-A-tampil}`. Opsi dropdown PIC (langkah 25 dan 54) tetap memakai nama lengkap `{pic-A}`/`{pic-B}`; format opsi menunggu PRD §4.1.3.
  - TC-GS-USER-840: "2 dari ≥3 Group berbeda" dipenuhi Population PT-22 dengan tiga Group (`{group-A}`, `{group-B}`, `{group-C}`); opsi pertama dan kedua dipilih, opsi ketiga tidak tampil.
  - TC-GS-USER-846: "Isi 2 field filter berbeda" tidak menyebut field; spec memakai Transaction `Borrowing` dan Group `{group-A}`. TC-GS-USER-845 mengasersi rentang 1 sampai 2 dengan batas inklusif (PRD `prd-conventions.md` §9.8).
  - TC dan PRD tidak menyatakan apakah Filter Panel menutup setelah `[Apply]`; spec membuka kembali panel dengan klik icon Filter sebelum memakainya lagi.
  - TC-GS-USER-841: teks `No results found` pada dropdown tanpa kecocokan (PRD `prd-conventions.md` §9.8) tidak disebut di TC; spec hanya mengasersi tidak ada opsi yang cocok. Cara menutup dropdown tidak didefinisikan di TC.
  - TC-GS-USER-842 dan 843: "Pilih 2 opsi" tidak menyebut opsi; spec memakai `Assignment` dan `Borrowing`. Di TC-GS-USER-843 opsi pertama `Borrowing` masih terpilih dari TC-GS-USER-842 dan `Assignment` dipilih kembali sebagai opsi kedua.
  - TC-GS-USER-844: nilai tanggal rentang tidak konkret; spec memakai `{rd-1}` dan `{lu-1}` dari Population PT-22. Seeding task pending FAMS dengan Request Date dan Last Updated tertentu tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE.
