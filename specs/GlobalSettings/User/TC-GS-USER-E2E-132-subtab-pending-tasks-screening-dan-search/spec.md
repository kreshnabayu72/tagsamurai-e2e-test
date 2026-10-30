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
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil) dan Dewi Lestari (No. 12; Client FAMS aktif dan tanpa data Pending Tasks).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat tepat 22 baris saat spec mulai). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC memakai Group dan user FAMS yang disediakan tim FE/BE. Bila Ahmad Fauzi sudah memiliki task pending Pre-setup, task itu dihitung ke dalam komposisi di bawah. Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A}` lebih kecil dari `{pic-B}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (kata pertama `{group-A}`) dan `{kw-pic}` (nama depan `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan: Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris dan `{group-B}` 12 baris; PIC `{pic-A}` 8 baris dan `{pic-B}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; page size 10 menghasilkan 3 halaman (10, 10, 2 baris).
- Data uji per TC: TC-GS-USER-396 baris contoh Transaction `Assignment`, Status `Waiting for Acceptance`, Total Asset `1`, dan keyword `Assignment`; TC-GS-USER-830 keyword `Assignment`; TC-GS-USER-831 keyword `  ASSIGNMENT  ` (spasi di kedua ujung); TC-GS-USER-832 keyword `ASG` (Transaction ID), `Assignment` (Transaction), `Acceptance` (Status), `{kw-group}` (Group), `{kw-pic}` (PIC); TC-GS-USER-833 keyword `1`; TC-GS-USER-834 keyword `{rd-1}` (Request Date) dan `{lu-1}` (Last Updated); TC-GS-USER-835 keyword `{kw-pic}` dan kolom `PIC` di-hide lalu di-unhide; TC-GS-USER-836 keyword `zzzqqq`.
- Kemampuan teknis: mengarahkan fokus dan membaca posisi kursor pada input Search; membaca teks sel tabel; seeding task pending FAMS dan pembersihannya (di atas).
- Preferensi kolom tabel Pending Tasks (visibilitas, urutan, pin) tersimpan per user di browser (cache `localStorage`, PRD `prd-conventions.md` §9.3); hook `after` menghapus preferensi itu sebagai cadangan. Nama key dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
- State yang diubah dan dipulihkan: kolom `PIC` dicentang kembali di langkah 92; kotak Search ditutup dan dikosongkan di langkah 99; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-396: Screening sub-tab Pending Tasks

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Tasks`
4. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`
5. Verifikasi kolom tabel berurutan `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`, lalu kolom Actions dengan `Column Visibility (⋯)`
6. Verifikasi tabel memakai urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)
7. Verifikasi baris contoh: Transaction `Assignment`, Status `Waiting for Acceptance`, Total Asset `1`
8. Verifikasi baris tabel tidak memiliki row action
9. Verifikasi kolom Actions hanya memuat pemicu Column Visibility (⋯)
10. Verifikasi kontrol pagination tampil pada 22 baris (pembanding untuk kontrol pagination yang hilang pada 10 baris atau kurang)
11. Klik icon Search, ketik `Assignment`, tekan Enter (membentuk hasil 10 baris atau kurang)
12. Verifikasi tabel menampilkan 8 baris Transaction `Assignment`
13. Verifikasi kontrol pagination tidak tampil
14. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-397: Empty state sub-tab Pending Tasks

15. Kembali ke Global Settings > User > User List (sub-tab Login User)
16. Klik Name `Dewi Lestari` di User List
17. Klik Tab `Responsibilities`
18. Klik sub-tab `Pending Tasks`
19. Verifikasi ilustrasi empty state tampil
20. Verifikasi teks `No pending tasks` tampil
21. Verifikasi teks `This user has no pending confirmation tasks.` tampil

### TC-GS-USER-830: Siklus Search (reveal, Enter, clear ×, collapse ←)

22. Kembali ke Global Settings > User > User List (sub-tab Login User)
23. Klik Name `Ahmad Fauzi` di User List
24. Klik Tab `Responsibilities`
25. Klik sub-tab `Pending Tasks`
26. Klik icon Search
27. Verifikasi Search bar melebar
28. Verifikasi kursor auto-focus di input Search
29. Ketik `Assignment` pada kotak Search
30. Verifikasi icon `×` muncul di dalam input
31. Verifikasi tabel belum tersaring (seluruh 22 baris (halaman 1 berisi 10 baris, footer pagination menampilkan 3 halaman))
32. Tekan Enter
33. Verifikasi tabel tersaring dan hanya menampilkan 8 baris Transaction `Assignment`
34. Klik icon `×`
35. Verifikasi input Search kosong
36. Verifikasi tabel tetap menampilkan hasil search terakhir (8 baris Transaction `Assignment`)
37. Tekan Enter pada input kosong
38. Verifikasi tabel kembali menampilkan seluruh data (seluruh 22 baris (halaman 1 berisi 10 baris, footer pagination menampilkan 3 halaman))
39. Isi Search dengan `Assignment`, tekan Enter
40. Klik icon panah `(←)`
41. Verifikasi Search collapse menjadi icon Search biasa
42. Verifikasi tabel langsung kembali menampilkan seluruh data tanpa menekan Enter (seluruh 22 baris (halaman 1 berisi 10 baris, footer pagination menampilkan 3 halaman))
43. Klik icon Search
44. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-USER-831: Query Search di-trim dan tidak case-sensitive

45. Isi Search dengan `  ASSIGNMENT  ` (spasi di kedua ujung), tekan Enter
46. Verifikasi tabel menampilkan 8 baris Transaction `Assignment` (spasi diabaikan, huruf besar atau kecil tidak dibedakan)
47. Verifikasi isi kotak Search tetap `  ASSIGNMENT  ` apa adanya

### TC-GS-USER-832: Search menemukan substring pada kolom kelas teks

48. Klik icon `×` untuk mengosongkan kotak Search
49. Isi Search dengan `ASG`, tekan Enter (potongan Transaction ID)
50. Verifikasi tabel menampilkan 8 baris dengan Transaction ID berawalan `ASG-`
51. Verifikasi baris dengan Transaction ID berawalan `BRW-` tidak tampil
52. Klik icon `×` untuk mengosongkan kotak Search
53. Isi Search dengan `Assignment`, tekan Enter (potongan Transaction)
54. Verifikasi tabel menampilkan 8 baris Transaction `Assignment`
55. Verifikasi baris Transaction `Borrowing` tidak tampil
56. Klik icon `×` untuk mengosongkan kotak Search
57. Isi Search dengan `Acceptance`, tekan Enter (potongan Status)
58. Verifikasi tabel menampilkan 8 baris Status `Waiting for Acceptance`
59. Verifikasi baris Status `Waiting for Confirmation` tidak tampil
60. Klik icon `×` untuk mengosongkan kotak Search
61. Isi Search dengan `{kw-group}`, tekan Enter (potongan Group)
62. Verifikasi tabel menampilkan 10 baris Group `{group-A}`
63. Verifikasi baris Group `{group-B}` tidak tampil
64. Klik icon `×` untuk mengosongkan kotak Search
65. Isi Search dengan `{kw-pic}`, tekan Enter (potongan PIC)
66. Verifikasi tabel menampilkan 8 baris PIC `{pic-A}`
67. Verifikasi baris PIC `{pic-B}` tidak tampil
68. Klik icon `×` untuk mengosongkan kotak Search
69. Tekan Enter pada input kosong untuk mereset tabel

### TC-GS-USER-833: Search menemukan substring pada kolom kelas numerik

70. Isi Search dengan `1`, tekan Enter (potongan Total Asset)
71. Verifikasi tabel menampilkan baris dengan Total Asset `1`
72. Verifikasi tabel menampilkan baris dengan Total Asset `10` (nilai yang memuat potongan `1`)
73. Klik icon `×` untuk mengosongkan kotak Search
74. Tekan Enter pada input kosong untuk mereset tabel

### TC-GS-USER-834: Kolom non-searchable tidak tercakup Search

75. Verifikasi baris pertama tabel menampilkan Request Date `{rd-1}` (pembanding untuk keyword Request Date)
76. Isi Search dengan `{rd-1}`, tekan Enter (nilai kolom Request Date)
77. Verifikasi tabel menampilkan no result state (`No results found`) untuk keyword Request Date
78. Klik icon `×` untuk mengosongkan kotak Search
79. Tekan Enter pada input kosong untuk mereset tabel
80. Verifikasi baris pertama tabel menampilkan Last Updated `{lu-1}` (pembanding untuk keyword Last Updated)
81. Isi Search dengan `{lu-1}`, tekan Enter (nilai kolom Last Updated)
82. Verifikasi tabel menampilkan no result state (`No results found`) untuk keyword Last Updated

### TC-GS-USER-835: Search tidak mencocokkan kolom yang di-hide, cocok kembali setelah unhide

83. Klik icon `×` untuk mengosongkan kotak Search
84. Tekan Enter pada input kosong untuk mereset tabel
85. Verifikasi baris PIC `{pic-A}` tampil di tabel (pembanding, kolom PIC masih visible)
86. Klik header kolom Column Visibility (⋯)
87. Hilangkan centang kolom `PIC` pada Overlay Column Visibility
88. Verifikasi kolom `PIC` tidak tampil di tabel
89. Isi Search dengan `{kw-pic}`, tekan Enter (nilai yang hanya ada di kolom PIC)
90. Verifikasi tabel menampilkan no result state (`No results found`) saat kolom PIC hidden
91. Klik header kolom Column Visibility (⋯)
92. Centang kembali kolom `PIC` pada Overlay Column Visibility
93. Tekan Enter pada input Search (keyword `{kw-pic}` masih terisi)
94. Verifikasi tabel menampilkan kembali 8 baris PIC `{pic-A}` setelah kolom PIC di-unhide

### TC-GS-USER-836: Empty filtered state

95. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
96. Verifikasi ilustrasi empty filtered state tampil
97. Verifikasi teks `No results found` tampil
98. Verifikasi teks `Try adjusting your search or filter.` tampil
99. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (396, 397, 830, 831, 832, 833, 834, 835, 836) dipertahankan; screening (396) dan empty state (397) berada di awal.
- Langkah 1 sampai 3 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Langkah 15 dan 22 kembali ke User List karena TC-GS-USER-397 memakai Detail Dewi Lestari.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 dan 14 (membentuk dan melepas hasil 10 baris atau kurang untuk butir pagination TC-GS-USER-396), langkah 15 dan 22 (kembali ke User List), langkah 48 sampai 69, 74, 79, serta 84 (mengosongkan kotak Search dan mereset tabel antar kasus), langkah 87 dan 92 (hide dan unhide `PIC` untuk TC-GS-USER-835), dan langkah 99 (menutup Search di akhir spec). Langkah 1 TC-GS-USER-832 sampai 836 memakai Search bar yang sudah terbuka (bagian 8b butir 9).
- Asersi tambahan (S-03, dengan alasan): langkah 10 (kontrol pagination tampil pada 22 baris) adalah pembanding sebelum asersi ketiadaan kontrol pagination; langkah 88 memastikan kolom `PIC` benar-benar hidden sebelum Search (S-14); pasangan `Verifikasi` "baris nilai lain tidak tampil" pada TC-GS-USER-832 memenuhi S-11 (dua nilai distinct pada kolom yang dicari) dan didahului `Verifikasi` baris yang tampil sebagai anchor (bagian 8b butir 2); `Verifikasi` baris pertama menampilkan Request Date dan Last Updated pada TC-GS-USER-834 menjadi anchor positif sebelum asersi no result. Pada TC-GS-USER-833 hanya baris yang tampil yang diasersi, karena Transaction ID dapat memuat digit `1` sehingga baris dengan Total Asset lain belum tentu hilang.
- Anchor TC-GS-USER-836: `Verifikasi` baris PIC `{pic-A}` kembali tampil pada TC-GS-USER-835 mendahului asersi empty filtered state di surface tabel yang sama.
- Pembagian TC lintas spec: TC-GS-USER-837 sampai 846 (Filter Panel) ada di spec 133; TC-GS-USER-847 sampai 851 (kombinasi Search dan Filter, Clear, filter kolom hidden) ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 (Sort, Pagination, kombinasi) ada di spec 135; TC-GS-USER-855 sampai 863 (Setup Column) ada di spec 136; TC-GS-USER-398 dan 864 sampai 868 (Download) ada di spec 137. TC sub-tab Pending Approvals ada di spec 126 sampai 131.
- Spec melewati sekitar 35 langkah (99 langkah) karena sembilan TC sub-tab Pending Tasks berbagi satu layar, satu dataset (PT-22), dan satu kelas harness (fungsional, tabel baca); tiap blok TC berdiri sendiri dan state dikembalikan lewat langkah penghubung, sehingga satu kegagalan tidak membuat blok lain kehilangan makna. Langkah pembuka Detail yang berulang (langkah 15 sampai 18 dan 22 sampai 25) adalah prefix berulang. TC-GS-USER-832 menguji lima kolom dengan blok identik (isi Search, `Verifikasi` baris tampil, `Verifikasi` baris lain tidak tampil, kosongkan).
- Temuan untuk QA:
  - TC-GS-USER-396 Expected e ("≤10 baris: kontrol pagination tidak tampil") bersyarat jumlah baris, sedangkan Population PT-22 memuat 22 baris (TC-GS-USER-869 mensyaratkan ≥21 baris). Spec membentuk hasil 8 baris lewat Search `Assignment` untuk mengasersi butir itu; TC tidak menyebut cara membentuk kondisi tersebut.
  - TC-GS-USER-396 dan 397: seeding task pending FAMS (Borrowing dan Assignment) beserta nilai Request Date, Last Updated, Group, dan PIC tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE. Ahmad Fauzi (Pre-setup No. 13) mungkin sudah memiliki task pending; TC tidak menyebut jumlahnya.
  - TC-GS-USER-397: sub-tab `Pending Tasks` Dewi Lestari dibuka lewat switcher sub-tab. NC-12 menetapkan empty state global menggantikan switcher bila dua sub-tab applicable atau lebih semuanya kosong; TC tidak menyebut apakah sub-tab Borrowed Assets, Assigned Assets, dan Pending Approvals Dewi Lestari terisi.
  - TC-GS-USER-830 langkah 5 ("amati tabel") tidak menyebut keyword konkret; spec memakai `Assignment`.
  - TC-GS-USER-832 dan 833: "potongan nilai kolom" dan keyword per kolom tidak konkret di TC; spec memakai keyword dari Population PT-22. Search kolom PIC mencocokkan nama lengkap, bukan teks tampil yang disingkat (PRD `user.md` §4.1.3), sehingga keyword PIC memakai nama depan.
  - TC-GS-USER-834 dan 835: "no result state" tidak diberi teks di TC; spec memakai `No results found` dari Expected TC-GS-USER-836 (teks sub-judul `Try adjusting your search or filter.` hanya diasersi di TC-GS-USER-836). TC-GS-USER-834 tidak menyebut format tanggal keyword; spec memakai teks sel apa adanya (format Date Format General Settings).
  - TC-GS-USER-835: TC tidak menyebut bahwa Search bar tetap terbuka dan keyword tetap terisi saat kolom di-unhide; spec menekan Enter pada input Search yang masih berisi keyword.
  - Nama key preferensi kolom di browser dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
