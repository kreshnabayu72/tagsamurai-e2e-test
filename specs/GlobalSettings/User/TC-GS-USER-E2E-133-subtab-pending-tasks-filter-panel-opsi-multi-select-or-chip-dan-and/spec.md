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
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat tepat 22 baris saat spec mulai). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC memakai Group dan user FAMS yang disediakan tim FE/BE. Bila Ahmad Fauzi sudah memiliki task pending Pre-setup, task itu dihitung ke dalam komposisi di bawah. Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A}` lebih kecil dari `{pic-B}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (kata pertama `{group-A}`) dan `{kw-pic}` (nama depan `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan: Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris dan `{group-B}` 12 baris; PIC `{pic-A}` 8 baris dan `{pic-B}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; page size 10 menghasilkan 3 halaman (10, 10, 2 baris).
- Data uji per TC: TC-GS-USER-838 dropdown `Transaction`, `Status`, `Group`, `PIC`; TC-GS-USER-839 opsi `Assignment` (Transaction), `Waiting for Confirmation` (Status), `{group-A}` (Group), `{pic-A}` (PIC); TC-GS-USER-840 opsi `Assignment` dan `Borrowing`; TC-GS-USER-841 keyword dropdown `borrow` lalu `zzz`; TC-GS-USER-842 dan 843 opsi `Assignment` dan `Borrowing` pada Transaction; TC-GS-USER-844 rentang `{rd-1}` sampai `{rd-1}` (Request Date) dan `{lu-1}` sampai `{lu-1}` (Last Updated); TC-GS-USER-845 Min `1` Max `2`; TC-GS-USER-846 Transaction `Borrowing` dan Group `{group-A}`.
- Date Format General Settings tidak diubah spec (nilai default environment); `{rd-1}` dan `{lu-1}` ditulis dalam format itu.
- Kemampuan teknis: memilih opsi dan menghapus chip di dropdown multi-select searchable; memilih rentang tanggal pada date range picker; mengisi field Min dan Max; membaca teks tanggal pada input date range; seeding task pending FAMS dan pembersihannya (di atas).
- State yang diubah dan dipulihkan: kriteria Filter dikosongkan lewat `[Clear Field]` dan `[Apply]` di akhir tiap blok dan di langkah 120; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-837: Screening Filter Panel

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Tasks`
4. Klik icon Filter
5. Verifikasi Filter Panel terbuka
6. Verifikasi field `Transaction` bertipe multi-select searchable dengan placeholder `All transactions`
7. Verifikasi field `Status` bertipe multi-select searchable dengan placeholder `All statuses`
8. Verifikasi field `Group` bertipe multi-select searchable dengan placeholder `All groups`
9. Verifikasi field `PIC` bertipe multi-select searchable dengan placeholder `All PICs`
10. Verifikasi field `Request Date` bertipe date range picker dengan placeholder `Select date`
11. Verifikasi field `Last Updated` bertipe date range picker dengan placeholder `Select date`
12. Verifikasi field `Total Asset` bertipe number range dengan placeholder `Min` dan `Max`
13. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-838: Opsi dropdown filter diambil dari nilai yang ada di tabel

14. Buka dropdown `Transaction`
15. Verifikasi dropdown `Transaction` hanya memuat opsi `Assignment` dan `Borrowing` (nilai yang ada di 22 baris tabel; tidak ada opsi lain)
16. Tutup dropdown `Transaction`
17. Buka dropdown `Status`
18. Verifikasi dropdown `Status` hanya memuat opsi `Waiting for Acceptance` dan `Waiting for Confirmation` (tidak ada opsi lain)
19. Tutup dropdown `Status`
20. Buka dropdown `Group`
21. Verifikasi dropdown `Group` hanya memuat opsi `{group-A}` dan `{group-B}` (tidak ada opsi lain)
22. Tutup dropdown `Group`
23. Buka dropdown `PIC`
24. Verifikasi dropdown `PIC` hanya memuat opsi `{pic-A}` dan `{pic-B}` (tidak ada opsi lain)
25. Tutup dropdown `PIC`

### TC-GS-USER-839: Filter multi-select per field menyaring baris

26. Pilih opsi `Assignment` pada dropdown `Transaction`
27. Klik `[Apply]`
28. Verifikasi tabel hanya menampilkan 8 baris Transaction `Assignment`
29. Verifikasi icon Filter berubah gelap
30. Klik icon Filter
31. Klik `[Clear Field]`
32. Klik `[Apply]`
33. Klik icon Filter
34. Pilih opsi `Waiting for Confirmation` pada dropdown `Status`
35. Klik `[Apply]`
36. Verifikasi tabel hanya menampilkan baris Status `Waiting for Confirmation` (14 baris: halaman 1 berisi 10 baris, 2 halaman)
37. Verifikasi icon Filter berubah gelap
38. Klik icon Filter
39. Klik `[Clear Field]`
40. Klik `[Apply]`
41. Klik icon Filter
42. Pilih opsi `{group-A}` pada dropdown `Group`
43. Klik `[Apply]`
44. Verifikasi tabel hanya menampilkan 10 baris Group `{group-A}`
45. Verifikasi icon Filter berubah gelap
46. Klik icon Filter
47. Klik `[Clear Field]`
48. Klik `[Apply]`
49. Klik icon Filter
50. Pilih opsi `{pic-A}` pada dropdown `PIC`
51. Klik `[Apply]`
52. Verifikasi tabel hanya menampilkan 8 baris PIC `{pic-A}`
53. Verifikasi icon Filter berubah gelap
54. Klik icon Filter
55. Klik `[Clear Field]`
56. Klik `[Apply]`

### TC-GS-USER-840: Dua opsi dalam satu field filter digabung OR

57. Klik icon Filter
58. Pilih opsi `Assignment` pada dropdown `Transaction`
59. Pilih opsi `Borrowing` pada dropdown `Transaction`
60. Klik `[Apply]`
61. Verifikasi tabel menampilkan baris Transaction `Assignment` (opsi 1)
62. Verifikasi tabel menampilkan baris Transaction `Borrowing` (opsi 2)
63. Klik icon Filter
64. Klik `[Clear Field]`
65. Klik `[Apply]`

### TC-GS-USER-841: Search di dalam dropdown filter mempersempit opsi

66. Klik icon Filter
67. Buka dropdown `Transaction`
68. Ketik `borrow` pada kotak cari di dalam dropdown
69. Verifikasi dropdown hanya menampilkan opsi `Borrowing` (tersaring substring, tidak membedakan huruf besar kecil)
70. Ganti isi kotak cari di dalam dropdown dengan `zzz`
71. Verifikasi dropdown tidak menampilkan opsi yang cocok
72. Kosongkan kotak cari di dalam dropdown dan tutup dropdown `Transaction`

### TC-GS-USER-842: Hapus chip filter via (X) meng-uncheck opsi

73. Pilih opsi `Assignment` pada dropdown `Transaction`
74. Pilih opsi `Borrowing` pada dropdown `Transaction`
75. Tutup dropdown `Transaction`
76. Klik (X) pada chip pertama (`Assignment`)
77. Verifikasi chip `Assignment` hilang
78. Verifikasi chip `Borrowing` tetap tampil
79. Buka dropdown `Transaction`
80. Verifikasi checkbox opsi `Assignment` di dropdown ter-uncheck

### TC-GS-USER-843: Uncheck opsi di dropdown menghapus chip

81. Pilih opsi `Assignment` pada dropdown `Transaction` (opsi kedua setelah `Borrowing`)
82. Hilangkan centang opsi `Assignment` di dropdown `Transaction`
83. Verifikasi chip `Assignment` hilang
84. Verifikasi chip `Borrowing` tetap tampil
85. Tutup dropdown `Transaction`
86. Klik `[Clear Field]`

### TC-GS-USER-844: Filter date range per field

87. Pilih rentang tanggal `{rd-1}` sampai `{rd-1}` pada field `Request Date`
88. Verifikasi teks tanggal pada input `Request Date` mengikuti Date Format General Settings
89. Klik `[Apply]`
90. Verifikasi tabel hanya menampilkan 8 baris dengan Request Date `{rd-1}`
91. Klik icon Filter
92. Klik `[Clear Field]`
93. Klik `[Apply]`
94. Klik icon Filter
95. Pilih rentang tanggal `{lu-1}` sampai `{lu-1}` pada field `Last Updated`
96. Verifikasi teks tanggal pada input `Last Updated` mengikuti Date Format General Settings
97. Klik `[Apply]`
98. Verifikasi tabel hanya menampilkan 10 baris dengan Last Updated `{lu-1}`
99. Klik icon Filter
100. Klik `[Clear Field]`
101. Klik `[Apply]`

### TC-GS-USER-845: Filter number range Min/Max

102. Klik icon Filter
103. Isi `Total Asset` Min dengan `1`
104. Isi `Total Asset` Max dengan `2`
105. Klik `[Apply]`
106. Verifikasi tabel hanya menampilkan 10 baris bernilai Total Asset `1` (6 baris) dan `2` (4 baris)
107. Verifikasi baris dengan Total Asset `3` dan `10` tidak tampil
108. Klik icon Filter
109. Klik `[Clear Field]`
110. Klik `[Apply]`

### TC-GS-USER-846: Kombinasi 2 field filter digabung AND

111. Klik icon Filter
112. Pilih opsi `Borrowing` pada dropdown `Transaction`
113. Pilih opsi `{group-A}` pada dropdown `Group`
114. Klik `[Apply]`
115. Verifikasi tabel hanya menampilkan 2 baris Transaction `Borrowing` dengan Group `{group-A}`
116. Verifikasi baris Transaction `Assignment` dengan Group `{group-A}` tidak tampil
117. Verifikasi baris Transaction `Borrowing` dengan Group `{group-B}` tidak tampil
118. Klik icon Filter
119. Klik `[Clear Field]`
120. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (837 sampai 846) dipertahankan; TC-GS-USER-837 (screening) di awal.
- Langkah 1 sampai 3 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Filter Panel yang terbuka pada TC-GS-USER-837 dipakai TC-GS-USER-838 dan blok pertama TC-GS-USER-839; TC-GS-USER-842 dan 843 memakai panel yang dibuka pada TC-GS-USER-841, dan TC-GS-USER-844 memakai panel dari TC-GS-USER-843 (langkah "Klik icon Filter" masing-masing TC sumber dipenuhi panel yang masih terbuka).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 sampai 25 (menutup dropdown setelah dibaca), langkah 72 (mengosongkan kotak cari dan menutup dropdown), langkah 86 (`[Clear Field]` tanpa `[Apply]` sehingga Filter Panel tetap terbuka dan tidak ada kriteria tersisa), serta rangkaian "Klik icon Filter, `[Clear Field]`, `[Apply]`" di akhir tiap blok TC-GS-USER-839, 840, 844, 845, dan 846 (mengosongkan Filter sebelum TC berikutnya, S-09). Klik icon Filter sebelum pemilihan opsi pada TC-GS-USER-839 sampai 846 membuka kembali Filter Panel yang tertutup setelah `[Apply]`.
- TC-GS-USER-838, 841, 842, dan 843 tidak menekan `[Apply]`; kriteria yang dipilih TC-GS-USER-842 dan 843 dibuang lewat `[Clear Field]` (langkah 86) dan tidak pernah di-Apply, sehingga tabel tidak berubah.
- Asersi tambahan (S-03, dengan alasan): pasangan `Verifikasi` "baris nilai lain tidak tampil" pada TC-GS-USER-845 dan 846 memenuhi S-11 (dua nilai distinct pada kolom yang difilter) dan didahului `Verifikasi` baris yang tampil sebagai anchor (bagian 8b butir 2); jumlah baris pada Expected TC-GS-USER-839, 844, 845, dan 846 adalah konkretisasi "hanya baris dengan nilai terpilih/dalam rentang tampil" dari Population PT-22.
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 (screening dan Search) ada di spec 132; TC-GS-USER-847 sampai 851 (kombinasi Search dan Filter, Clear, filter kolom hidden) ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 ada di spec 135; TC-GS-USER-855 sampai 863 ada di spec 136; TC-GS-USER-398 dan 864 sampai 868 ada di spec 137. TC filter sub-tab Pending Approvals ada di spec 127.
- Spec melewati sekitar 35 langkah (120 langkah) karena sepuluh TC Filter Panel berbagi satu layar, satu dataset (PT-22), dan satu kelas harness (fungsional); tiap blok TC berdiri sendiri dan Filter dikosongkan di antara blok, sehingga satu kegagalan tidak membuat blok lain kehilangan makna. TC-GS-USER-839 menguji empat field dengan blok identik (pilih opsi, `[Apply]`, dua `Verifikasi`, kosongkan Filter) dan rangkaian "Klik icon Filter, `[Clear Field]`, `[Apply]`" merupakan prefix berulang.
- Temuan untuk QA:
  - TC-GS-USER-840: Transaction hanya memiliki dua nilai (`Assignment` dan `Borrowing`, PRD `user.md` §4.1.3), sehingga memilih dua opsi menghasilkan seluruh baris dan tidak dapat dibedakan dari Filter kosong; spec mengasersi baris kedua jenis tampil. Pembuktian OR yang membedakan membutuhkan field dengan tiga nilai atau lebih (mis. Group).
  - TC-GS-USER-846: "Isi 2 field filter berbeda" tidak menyebut field; spec memakai Transaction `Borrowing` dan Group `{group-A}`. TC-GS-USER-845 mengasersi rentang 1 sampai 2 dengan batas inklusif (PRD `prd-conventions.md` §9.8).
  - TC-GS-USER-839: "icon Filter berubah gelap saat aktif" berbeda dari PRD `prd-conventions.md` §9.8 ("gelap saat panel aktif/terbuka"); spec mengasersi icon gelap sesudah `[Apply]` mengikuti TC.
  - TC dan PRD tidak menyatakan apakah Filter Panel menutup setelah `[Apply]`; spec membuka kembali panel dengan klik icon Filter sebelum memakainya lagi.
  - TC-GS-USER-841: teks `No results found` pada dropdown tanpa kecocokan (PRD `prd-conventions.md` §9.8) tidak disebut di TC; spec hanya mengasersi tidak ada opsi yang cocok. Cara menutup dropdown tidak didefinisikan di TC.
  - TC-GS-USER-842 dan 843: "Pilih 2 opsi" tidak menyebut opsi; spec memakai `Assignment` dan `Borrowing`. Di TC-GS-USER-843 opsi pertama `Borrowing` masih terpilih dari TC-GS-USER-842 dan `Assignment` dipilih kembali sebagai opsi kedua.
  - TC-GS-USER-844: nilai tanggal rentang tidak konkret; spec memakai `{rd-1}` dan `{lu-1}` dari Population PT-22. Seeding task pending FAMS dengan Request Date dan Last Updated tertentu tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE.
