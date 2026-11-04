---
id: TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search
title: "Sub-tab Pending Tasks: Screening, State Kosong, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-396
  - TC-GS-USER-397
  - TC-GS-USER-830
  - TC-GS-USER-831
  - TC-GS-USER-832
  - TC-GS-USER-833
  - TC-GS-USER-834
  - TC-GS-USER-835
  - TC-GS-USER-836
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Screening, State Kosong, dan Search

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data User; yang di-seed hanya task pending FAMS milik spec (Population PT-22).
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List (sub-tab Login User) dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil) dan Rina Kartika (No. 30; data hanya di sub-tab Responsibilities Borrowed Assets, sedangkan Assigned Assets, Pending Approvals, dan Pending Tasks kosong; Client FAMS aktif).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat `B0` + 22 baris sesudah seeding, dengan `B0` = jumlah task pending Pre-setup Ahmad Fauzi yang dibaca lewat kemampuan baca BE tepat sebelum seeding; kemampuan itu disediakan tim FE/BE). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC task seed memakai Group dan user FAMS yang disediakan tim FE/BE dan bernama bersuffix `{runId}-132` (`{group-A}` = `Alfa {runId}-132`, `{group-B}` = `Beta {runId}-132`; PIC `{pic-A}` nama lengkap `Rina Pica {runId}-132`, `{pic-B}` nama lengkap `Sari Picb {runId}-132`; teks tampil sel PIC `[First Name] [Last Initial]`: `{pic-A-tampil}` = `Rina P`, `{pic-B-tampil}` = `Sari P`, dua nilai berbeda; asersi sel dan sort kolom PIC memakai nilai tampil, nama lengkap hanya untuk Search dan hover), sehingga tidak bentrok dengan task Pre-setup. Task Pre-setup Ahmad Fauzi (`B0` baris) tidak diubah dan isinya tidak diasumsikan: asersi jumlah per nilai Group atau PIC memakai nama bersuffix itu, sedangkan asersi per nilai Transaction, Status, Total Asset, Request Date, atau Last Updated menyebut baris seed (task milik spec ini). Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A-tampil}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B-tampil}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B-tampil}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A-tampil}` lebih kecil dari `{pic-B-tampil}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (`lfa {runId}-132`, potongan `{group-A}`) dan `{kw-pic}` (`Pica {runId}-132`, potongan nama lengkap `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan (baris seed): Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris dan `{group-B}` 12 baris; PIC `{pic-A-tampil}` 8 baris dan `{pic-B-tampil}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; total tabel `B0` + 22 baris sehingga page size 10 menghasilkan sedikitnya 3 halaman.
- Data uji per TC: TC-GS-USER-396 baris contoh Transaction `Assignment`, Status `Waiting for Acceptance`, Total Asset `1`, dan keyword `Assignment`; TC-GS-USER-830 keyword `Assignment`; TC-GS-USER-831 keyword `  ASSIGNMENT  ` (spasi di kedua ujung); TC-GS-USER-832 keyword `ASG` (Transaction ID), `Assignment` (Transaction), `Acceptance` (Status), `{kw-group}` (Group), `{kw-pic}` (PIC); TC-GS-USER-833 keyword `1`; TC-GS-USER-834 keyword `{rd-1}` (Request Date) dan `{lu-1}` (Last Updated); TC-GS-USER-835 keyword `{kw-pic}` dan kolom `PIC` di-hide lalu di-unhide; TC-GS-USER-836 keyword `zzzqqq`.
- Kemampuan teknis: mengarahkan fokus dan membaca posisi kursor pada input Search; membaca teks sel tabel; seeding task pending FAMS dan pembersihannya (di atas).
- Preferensi kolom tabel Pending Tasks (visibilitas, urutan, pin) tersimpan per user di browser (cache `localStorage`, PRD `prd-conventions.md` §9.3); hook `after` menghapus preferensi itu sebagai cadangan. Nama key dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
- State yang diubah dan dipulihkan: kolom `PIC` dicentang kembali di langkah 96; kotak Search ditutup dan dikosongkan di langkah 101; hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-396: Screening sub-tab Pending Tasks

1. Klik icon Search di User List, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Tasks`
5. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`
6. Klik icon Search
7. Verifikasi input Search kosong dengan placeholder `Search transaction ID, status, or group...`
8. Klik icon panah `(←)`
9. Verifikasi kolom tabel berurutan `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`, lalu kolom Actions dengan `Column Visibility (⋯)`
10. Verifikasi tabel memakai urutan default Request Date Oldest First (baris seed Transaction `Assignment` dengan Request Date `{rd-1}` tampil sebelum baris seed Transaction `Borrowing` dengan Request Date `{rd-2}`)
11. Verifikasi baris contoh: Transaction `Assignment`, Status `Waiting for Acceptance`, Total Asset `1`
12. Verifikasi baris tabel tidak memiliki row action
13. Verifikasi kolom Actions hanya memuat pemicu Column Visibility (⋯)
14. Verifikasi kontrol pagination tampil pada `B0` + 22 baris (pembanding untuk kontrol pagination yang hilang pada 10 baris atau kurang)
15. Klik icon Search, ketik `{kw-group}`, tekan Enter (membentuk hasil 10 baris atau kurang)
16. Verifikasi tabel menampilkan 10 baris Group `{group-A}`
17. Verifikasi kontrol pagination tidak tampil
18. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-397: Empty state sub-tab Pending Tasks

19. Kembali ke Global Settings > User > User List (sub-tab Login User)
20. Klik icon Search di User List, ketik `Rina Kartika`, tekan Enter
21. Klik Name `Rina Kartika` di User List
22. Klik Tab `Responsibilities`
23. Klik sub-tab `Pending Tasks`
24. Verifikasi ilustrasi empty state dengan judul `No pending tasks` dan deskripsi `This user has no pending confirmation tasks.`

### TC-GS-USER-830: Siklus Search (reveal, Enter, clear (✕), collapse ←)

25. Kembali ke Global Settings > User > User List (sub-tab Login User)
26. Klik icon Search di User List, ketik `Ahmad Fauzi`, tekan Enter
27. Klik Name `Ahmad Fauzi` di User List
28. Klik Tab `Responsibilities`
29. Klik sub-tab `Pending Tasks`
30. Klik icon Search
31. Verifikasi Search bar melebar
32. Verifikasi kursor auto-focus di input Search
33. Ketik `Assignment` pada kotak Search
34. Verifikasi icon `(✕)` muncul di dalam input
35. Verifikasi tabel belum tersaring (seluruh `B0` + 22 baris (halaman 1 berisi 10 baris, footer pagination menampilkan sedikitnya 3 halaman))
36. Tekan Enter
37. Verifikasi tabel tersaring dan hanya menampilkan baris Transaction `Assignment` (termasuk 8 baris seed)
38. Klik icon `(✕)`
39. Verifikasi input Search kosong
40. Verifikasi tabel tetap menampilkan hasil search terakhir (baris Transaction `Assignment`, termasuk 8 baris seed)
41. Tekan Enter pada input kosong
42. Verifikasi tabel kembali menampilkan seluruh data (seluruh `B0` + 22 baris (halaman 1 berisi 10 baris, footer pagination menampilkan sedikitnya 3 halaman))
43. Isi Search dengan `Assignment`, tekan Enter
44. Klik icon panah `(←)`
45. Verifikasi Search collapse menjadi icon Search biasa
46. Verifikasi tabel langsung kembali menampilkan seluruh data tanpa menekan Enter (seluruh `B0` + 22 baris (halaman 1 berisi 10 baris, footer pagination menampilkan sedikitnya 3 halaman))
47. Klik icon Search
48. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-USER-831: Query Search di-trim dan tidak case-sensitive

49. Isi Search dengan `  ASSIGNMENT  ` (spasi di kedua ujung), tekan Enter
50. Verifikasi tabel menampilkan baris Transaction `Assignment`, termasuk 8 baris seed (spasi diabaikan, huruf besar atau kecil tidak dibedakan)
51. Verifikasi isi kotak Search tetap `  ASSIGNMENT  ` apa adanya

### TC-GS-USER-832: Search menemukan substring pada kolom kelas teks

52. Klik icon `×` untuk mengosongkan kotak Search
53. Isi Search dengan `ASG`, tekan Enter (potongan Transaction ID)
54. Verifikasi tabel menampilkan baris dengan Transaction ID berawalan `ASG-`, termasuk 8 baris seed
55. Verifikasi baris dengan Transaction ID berawalan `BRW-` tidak tampil
56. Klik icon `×` untuk mengosongkan kotak Search
57. Isi Search dengan `Assignment`, tekan Enter (potongan Transaction)
58. Verifikasi tabel menampilkan baris Transaction `Assignment`, termasuk 8 baris seed
59. Verifikasi baris Transaction `Borrowing` tidak tampil
60. Klik icon `×` untuk mengosongkan kotak Search
61. Isi Search dengan `Acceptance`, tekan Enter (potongan Status)
62. Verifikasi tabel menampilkan baris Status `Waiting for Acceptance`, termasuk 8 baris seed
63. Verifikasi baris Status `Waiting for Confirmation` tidak tampil
64. Klik icon `×` untuk mengosongkan kotak Search
65. Isi Search dengan `{kw-group}`, tekan Enter (potongan Group)
66. Verifikasi tabel menampilkan 10 baris Group `{group-A}`
67. Verifikasi baris Group `{group-B}` tidak tampil
68. Klik icon `×` untuk mengosongkan kotak Search
69. Isi Search dengan `{kw-pic}`, tekan Enter (potongan PIC)
70. Verifikasi tabel menampilkan 8 baris PIC `{pic-A-tampil}`
71. Verifikasi baris PIC `{pic-B-tampil}` tidak tampil
72. Klik icon `×` untuk mengosongkan kotak Search
73. Tekan Enter pada input kosong untuk mereset tabel

### TC-GS-USER-833: Search menemukan substring pada kolom kelas numerik

74. Isi Search dengan `1`, tekan Enter (potongan Total Asset)
75. Verifikasi tabel menampilkan baris dengan Total Asset `1`
76. Verifikasi tabel menampilkan baris dengan Total Asset `10` (nilai yang memuat potongan `1`)
77. Klik icon `×` untuk mengosongkan kotak Search
78. Tekan Enter pada input kosong untuk mereset tabel

### TC-GS-USER-834: Kolom non-searchable tidak tercakup Search

79. Verifikasi baris seed dengan Request Date `{rd-1}` tampil di tabel (pembanding untuk keyword Request Date)
80. Isi Search dengan `{rd-1}`, tekan Enter (nilai kolom Request Date)
81. Verifikasi tabel menampilkan no result state (`No results found`) untuk keyword Request Date
82. Klik icon `×` untuk mengosongkan kotak Search
83. Tekan Enter pada input kosong untuk mereset tabel
84. Verifikasi baris seed dengan Last Updated `{lu-1}` tampil di tabel (pembanding untuk keyword Last Updated)
85. Isi Search dengan `{lu-1}`, tekan Enter (nilai kolom Last Updated)
86. Verifikasi tabel menampilkan no result state (`No results found`) untuk keyword Last Updated

### TC-GS-USER-835: Search tidak mencocokkan kolom yang di-hide, cocok kembali setelah unhide

87. Klik icon `×` untuk mengosongkan kotak Search
88. Tekan Enter pada input kosong untuk mereset tabel
89. Verifikasi baris PIC `{pic-A-tampil}` tampil di tabel (pembanding, kolom PIC masih visible)
90. Klik header kolom Column Visibility (⋯)
91. Hilangkan centang kolom `PIC` pada Overlay Column Visibility
92. Verifikasi kolom `PIC` tidak tampil di tabel
93. Isi Search dengan `{kw-pic}`, tekan Enter (nilai yang hanya ada di kolom PIC)
94. Verifikasi tabel menampilkan no result state (`No results found`) saat kolom PIC hidden
95. Klik header kolom Column Visibility (⋯)
96. Centang kembali kolom `PIC` pada Overlay Column Visibility
97. Tekan Enter pada input Search (keyword `{kw-pic}` masih terisi)
98. Verifikasi tabel menampilkan kembali 8 baris PIC `{pic-A-tampil}` setelah kolom PIC di-unhide

### TC-GS-USER-836: Empty filtered state

99. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
100. Verifikasi ilustrasi empty filtered state dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
101. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (396, 397, 830, 831, 832, 833, 834, 835, 836) dipertahankan; screening (396) dan empty state (397) berada di awal.
- Langkah 1 sampai 4 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Langkah 19 dan 25 kembali ke User List karena TC-GS-USER-397 memakai Detail Rina Kartika; langkah 1, 20, dan 26 mencari user target di User List agar Name dapat diklik (bagian 8b butir 12).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 dan 18 (membentuk dan melepas hasil 10 baris atau kurang untuk butir pagination TC-GS-USER-396), langkah 6 sampai 8 (membuka Search hanya untuk mengamati placeholder lalu menutupnya), langkah 19 dan 25 (kembali ke User List), langkah 52 sampai 73, 78, 83, serta 88 (mengosongkan kotak Search dan mereset tabel antar kasus), langkah 91 dan 96 (hide dan unhide `PIC` untuk TC-GS-USER-835), dan langkah 101 (menutup Search di akhir spec). Langkah 1 TC-GS-USER-832 sampai 836 memakai Search bar yang sudah terbuka (bagian 8b butir 9).
- Asersi tambahan (S-03, dengan alasan): langkah 14 (kontrol pagination tampil pada `B0` + 22 baris) adalah pembanding sebelum asersi ketiadaan kontrol pagination; langkah 92 memastikan kolom `PIC` benar-benar hidden sebelum Search (S-14); pasangan `Verifikasi` "baris nilai lain tidak tampil" pada TC-GS-USER-832 memenuhi S-11 (dua nilai distinct pada kolom yang dicari) dan didahului `Verifikasi` baris yang tampil sebagai anchor (bagian 8b butir 2); `Verifikasi` baris seed dengan Request Date dan Last Updated pada TC-GS-USER-834 menjadi anchor positif sebelum asersi no result. Pada TC-GS-USER-833 hanya baris yang tampil yang diasersi, karena Transaction ID dapat memuat digit `1` sehingga baris dengan Total Asset lain belum tentu hilang.
- Anchor TC-GS-USER-836: `Verifikasi` baris PIC `{pic-A-tampil}` kembali tampil pada TC-GS-USER-835 mendahului asersi empty filtered state di surface tabel yang sama.
- Pembagian TC lintas spec: TC-GS-USER-837 sampai 846 (Filter Panel) ada di spec 133; TC-GS-USER-847 sampai 851 (kombinasi Search dan Filter, Clear, filter kolom hidden) ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 (Sort, Pagination, kombinasi) ada di spec 135; TC-GS-USER-855 sampai 863 (Setup Column) ada di spec 136; TC-GS-USER-398 dan 864 sampai 868 (Download) ada di spec 137. TC sub-tab Pending Approvals ada di spec 126 sampai 131.
- Spec melewati sekitar 35 langkah (101 langkah) karena sembilan TC sub-tab Pending Tasks berbagi satu layar, satu dataset (PT-22), dan satu kelas harness (fungsional, tabel baca); tiap blok TC berdiri sendiri dan state dikembalikan lewat langkah penghubung, sehingga satu kegagalan tidak membuat blok lain kehilangan makna. Langkah pembuka Detail yang berulang (langkah 19 sampai 23 dan 25 sampai 29) adalah prefix berulang. TC-GS-USER-832 menguji lima kolom dengan blok identik (isi Search, `Verifikasi` baris tampil, `Verifikasi` baris lain tidak tampil, kosongkan).
- Temuan untuk QA:
  - TC-GS-USER-396 Expected e ("≤10 baris: kontrol pagination tidak tampil") bersyarat jumlah baris, sedangkan Population PT-22 memuat `B0` + 22 baris. Spec membentuk hasil 10 baris lewat Search `{kw-group}` untuk mengasersi butir itu; TC tidak menyebut cara membentuk kondisi tersebut.
  - TC-GS-USER-396 dan 397: seeding task pending FAMS (Borrowing dan Assignment) beserta nilai Request Date, Last Updated, Group, dan PIC tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE. Ahmad Fauzi (Pre-setup No. 13) mungkin sudah memiliki task pending; TC tidak menyebut jumlahnya.
  - TC-GS-USER-397: sub-tab `Pending Tasks` Rina Kartika (No. 30, data Pre-setup dari TC) dibuka lewat switcher sub-tab; data hanya ada di sub-tab Borrowed Assets.
  - TC-GS-USER-830 langkah 5 ("amati tabel") tidak menyebut keyword konkret; spec memakai `Assignment`.
  - TC-GS-USER-832 dan 833: "potongan nilai kolom" dan keyword per kolom tidak konkret di TC; spec memakai keyword dari Population PT-22. Search kolom PIC mencocokkan nama lengkap, bukan teks tampil yang disingkat (PRD `user.md` §4.1.3), sehingga keyword PIC memakai nama depan.
  - TC-GS-USER-834 dan 835: "no result state" tidak diberi teks di TC; spec memakai `No results found` dari Expected TC-GS-USER-836 (teks sub-judul `Try adjusting your search or filter.` hanya diasersi di TC-GS-USER-836). TC-GS-USER-834 tidak menyebut format tanggal keyword; spec memakai teks sel apa adanya (format Date Format General Settings).
  - TC-GS-USER-835: TC tidak menyebut bahwa Search bar tetap terbuka dan keyword tetap terisi saat kolom di-unhide; spec menekan Enter pada input Search yang masih berisi keyword.
  - Sel PIC menampilkan `[First Name] [Last Initial]` (PRD `user.md` §4.1.3); asersi sel memakai `{pic-A-tampil}`/`{pic-B-tampil}`. Format opsi dropdown PIC menunggu PRD §4.1.3.
  - Nama key preferensi kolom di browser dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
