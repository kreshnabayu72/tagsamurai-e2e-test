---
id: TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Sub-tab Pending Approvals: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang, AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-798
  - TC-GS-USER-799
  - TC-GS-USER-800
  - TC-GS-USER-801
  - TC-GS-USER-802
  - TC-GS-USER-803
  - TC-GS-USER-804
  - TC-GS-USER-805
  - TC-GS-USER-806
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang, AND)

## Prerequisites

- Mode: FE+BE. Spec hanya membaca sub-tab Pending Approvals Ahmad Fauzi (read-only, tanpa row action) dan tidak mengubah data Pre-setup User.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Ahmad Fauzi (No. 13, data Responsibilities FAMS).
- Data Dinamis (HK8, seeding minimal S-11; seeding user dan approval FAMS lewat API di hook `before` adalah kemampuan yang disediakan tim FE/BE, endpoint tidak disebut di TC, PRD, dan LLD):
  - Requester seed (user biasa, Access `Fixed Asset`, Division `Finance`): R1 First Name `Budi`, Last Name `Santoso {runId}-127`, email `budisantoso+{runId}-127@qwertysystem.net`, tampil di tabel `Budi S`; R2 First Name `Citra`, Last Name `Anggraini {runId}-127`, email `citraanggraini+{runId}-127@qwertysystem.net`, tampil `Citra A`; R3 First Name `Dedi`, Last Name `Kurniawan {runId}-127`, email `dedikurniawan+{runId}-127@qwertysystem.net`, tampil `Dedi K`.
  - Requester R4 tanpa approval: First Name `Eka`, Last Name `Putri {runId}-127`, email `ekaputri+{runId}-127@qwertysystem.net`, tampil `Eka P`. R4 tidak punya request approval sehingga tidak boleh muncul di opsi dropdown Requester.
  - 30 request approval in-flight (status Waiting for Approval) dengan Approver Ahmad Fauzi (Pre-setup No. 13), sehingga tabel Pending Approvals Ahmad Fauzi memuat lebih dari satu halaman (page size 10). Transaction ID dibuat FAMS saat seeding dan dikembalikan ke spec; nilainya tidak ditulis di spec. Submission Date `D1` = hari uji dikurangi 14 hari dan `D2` = hari uji dikurangi 7 hari (kemampuan menetapkan Submission Date seed disediakan tim FE/BE), teks tanggal dibaca dari sel tabel dalam Date Format General Settings.
  - Transaction `Transfer`, `{transaksi-B}`, dan `{transaksi-C}`: `Transfer` dan dua nilai Transaction FAAP lain yang namanya tidak memuat `ransf`, dipilih tim FE/BE saat seeding (TC dan PRD tidak menyebut nilai selain `Transfer`). `{transaksi-D}` = satu nilai Transaction FAAP lain yang tidak di-seed (tidak punya baris).

    | Kelompok | Transaction | Requester | Submission Date | Jumlah baris |
    |---|---|---|---|---|
    | S1 | `Transfer` | R1 `Budi S` | D1 | 6 |
    | S2 | `Transfer` | R2 `Citra A` | D2 | 4 |
    | S3 | `{transaksi-B}` | R2 `Citra A` | D1 | 6 |
    | S4 | `{transaksi-B}` | R3 `Dedi K` | D2 | 6 |
    | S5 | `{transaksi-C}` | R3 `Dedi K` | D1 | 4 |
    | S6 | `{transaksi-C}` | R1 `Budi S` | D2 | 4 |

  - Hasil per dimensi: Transaction `Transfer` 10 baris, `{transaksi-B}` 12 baris, `{transaksi-C}` 8 baris; Requester R1, R2, R3 masing-masing 10 baris; Submission Date D1 16 baris, D2 14 baris. Tiap kolom yang diuji (Transaction, Requester, Submission Date) memuat tiga, tiga, dan dua nilai distinct.
  - Baris contoh = satu baris kelompok S1 (Transfer, R1 `Budi S`, D1); Transaction ID-nya `{trxId-contoh}` dikembalikan oleh seeding.
  - Keyword unik Requester (hanya cocok dengan Requester seed spec ini karena memuat suffix): `ntoso {runId}-127` (R1), `raini {runId}-127` (R2), `{runId}-127` (R1, R2, R3).
  - Baris Pre-setup Pending Approvals Ahmad Fauzi (bila ada) tidak diubah dan jumlahnya tidak diasumsikan: asersi jumlah baris memakai keyword atau filter yang hanya cocok dengan baris seed, dan asersi urutan atau isi umum tidak bergantung pada baris Pre-setup.
  - Cleanup di hook `after` (tanpa berasumsi seeding berhasil penuh): hapus 30 request approval seed dan user Requester seed lewat API.
- Data uji per TC: TC-GS-USER-799 opsi dropdown Transaction dan Requester; TC-GS-USER-800 Transaction `Transfer` dan Requester `Budi S`; TC-GS-USER-801 `Transfer` dan `{transaksi-B}`; TC-GS-USER-802 keyword dropdown `RANSF` dan `zzz`; TC-GS-USER-803 dan 804 `Transfer` dan `{transaksi-B}`; TC-GS-USER-805 rentang `{tanggal-D1}` sampai `{tanggal-D1}`; TC-GS-USER-806 Transaction `Transfer` dan Requester `Citra A`.
- State yang diubah dan dipulihkan: Filter dikosongkan (`[Clear Field]` lalu `[Apply]`) di akhir tiap TC yang menerapkannya; Filter Panel ditutup di akhir TC tanpa Apply; page size dikembalikan ke 10 oleh hook `after`; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`): tabel Pending Approvals Ahmad Fauzi hanya boleh memuat baris Pre-setup dan seed spec ini saat spec berjalan.
- Kemampuan teknis: memilih opsi dan menghapus chip pada multi-select; memilih rentang tanggal pada date range picker; membaca teks sel tabel dan menghitung baris.

## Test Steps

### TC-GS-USER-798: Screening Filter Panel

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Approvals`
4. Ubah page size ke 100 supaya seluruh baris seed tampil dalam satu halaman
5. Klik icon Filter
6. Verifikasi field `Transaction`: multi-select searchable dengan placeholder `All transactions`
7. Verifikasi field `Requester`: multi-select searchable dengan placeholder `All requesters`
8. Verifikasi field `Submission Date`: date range picker dengan placeholder `Select date`
9. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-799: Opsi dropdown filter diambil dari nilai yang ada di tabel

10. Buka dropdown Transaction
11. Verifikasi dropdown Transaction memuat opsi `Transfer`, `{transaksi-B}`, dan `{transaksi-C}`
12. Verifikasi dropdown Transaction tidak memuat opsi `{transaksi-D}` (nilai tanpa baris)
13. Tutup dropdown Transaction
14. Buka dropdown Requester
15. Verifikasi dropdown Requester memuat opsi `Budi S`, `Citra A`, dan `Dedi K`
16. Verifikasi dropdown Requester tidak memuat opsi `Eka P` (Requester tanpa baris)
17. Tutup dropdown Requester
18. Tutup Filter Panel dengan klik icon Filter

### TC-GS-USER-800: Filter multi-select per field menyaring baris

19. Klik icon Filter
20. Buka dropdown Transaction
21. Pilih opsi `Transfer` di dropdown Transaction
22. Klik `[Apply]`
23. Verifikasi hanya baris dengan Transaction `Transfer` yang tampil
24. Verifikasi icon Filter berubah gelap (filter aktif)
25. Klik icon Filter
26. Klik `[Clear Field]`
27. Klik `[Apply]`
28. Klik icon Filter
29. Buka dropdown Requester
30. Pilih opsi `Budi S` di dropdown Requester
31. Klik `[Apply]`
32. Verifikasi hanya baris dengan Requester `Budi S` yang tampil
33. Verifikasi icon Filter berubah gelap (filter aktif)
34. Klik icon Filter
35. Klik `[Clear Field]`
36. Klik `[Apply]`

### TC-GS-USER-801: 2 opsi dalam satu field filter digabung OR

37. Klik icon Filter
38. Buka dropdown Transaction
39. Pilih opsi `Transfer` di dropdown Transaction
40. Pilih opsi `{transaksi-B}` di dropdown Transaction
41. Klik `[Apply]`
42. Verifikasi baris dengan Transaction `Transfer` tampil
43. Verifikasi baris dengan Transaction `{transaksi-B}` tampil
44. Verifikasi baris dengan Transaction `{transaksi-C}` tidak tampil
45. Klik icon Filter
46. Klik `[Clear Field]`
47. Klik `[Apply]`

### TC-GS-USER-802: Search di dalam dropdown filter mempersempit opsi

48. Klik icon Filter
49. Buka dropdown Transaction
50. Ketik `RANSF` pada search dropdown Transaction
51. Verifikasi opsi `Transfer` tampil (substring, tidak membedakan huruf besar dan kecil)
52. Verifikasi opsi `{transaksi-B}` dan `{transaksi-C}` tidak tampil
53. Ganti isi search dropdown dengan `zzz`
54. Verifikasi tidak ada opsi yang cocok
55. Tutup dropdown Transaction
56. Tutup Filter Panel dengan klik icon Filter

### TC-GS-USER-803: Hapus chip filter via (X) meng-uncheck opsi

57. Klik icon Filter
58. Buka dropdown Transaction
59. Pilih opsi `Transfer` di dropdown Transaction
60. Pilih opsi `{transaksi-B}` di dropdown Transaction
61. Klik (X) pada chip `Transfer` (chip pertama)
62. Verifikasi chip `Transfer` hilang
63. Verifikasi chip `{transaksi-B}` tetap tampil
64. Buka dropdown Transaction
65. Verifikasi checkbox opsi `Transfer` tidak tercentang
66. Tutup dropdown Transaction
67. Klik `[Clear Field]`
68. Tutup Filter Panel dengan klik icon Filter

### TC-GS-USER-804: Uncheck opsi di dropdown menghapus chip

69. Klik icon Filter
70. Buka dropdown Transaction
71. Pilih opsi `Transfer` di dropdown Transaction
72. Pilih opsi `{transaksi-B}` di dropdown Transaction
73. Hilangkan centang opsi `{transaksi-B}` (opsi kedua) di dropdown Transaction
74. Verifikasi chip `{transaksi-B}` hilang
75. Verifikasi chip `Transfer` tetap tampil
76. Tutup dropdown Transaction
77. Klik `[Clear Field]`
78. Tutup Filter Panel dengan klik icon Filter

### TC-GS-USER-805: Filter date range per field

79. Klik icon Filter
80. Pilih rentang tanggal `{tanggal-D1}` sampai `{tanggal-D1}` pada field Submission Date
81. Verifikasi tanggal pada input Submission Date memakai Date Format General Settings (format sama dengan sel Submission Date)
82. Klik `[Apply]`
83. Verifikasi hanya baris dengan Submission Date `{tanggal-D1}` yang tampil
84. Verifikasi baris dengan Submission Date `{tanggal-D2}` tidak tampil
85. Klik icon Filter
86. Klik `[Clear Field]`
87. Klik `[Apply]`

### TC-GS-USER-806: Kombinasi 2 field filter digabung AND

88. Klik icon Filter
89. Buka dropdown Transaction
90. Pilih opsi `Transfer` di dropdown Transaction
91. Buka dropdown Requester
92. Pilih opsi `Citra A` di dropdown Requester
93. Klik `[Apply]`
94. Verifikasi seluruh baris yang tampil bernilai Transaction `Transfer` dan Requester `Citra A`
95. Verifikasi jumlah baris hasil adalah 4
96. Verifikasi baris dengan Requester `Budi S` tidak tampil
97. Klik icon Filter
98. Klik `[Clear Field]`
99. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dependensi data Pending Approvals Ahmad Fauzi dipenuhi spec ini lewat seeding di hook `before`, tanpa menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (798 sampai 806) dipertahankan; TC-GS-USER-798 (screening) di awal.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (page size 100 supaya seluruh baris seed tampil di satu halaman dan asersi isi hasil filter tidak bergantung pada pembagian halaman), 13, 17, 55, 66, dan 76 (menutup dropdown), 18, 56, 68, dan 78 (menutup Filter Panel tanpa Apply), 67 dan 77 (`[Clear Field]` agar pilihan tidak terbawa ke TC berikutnya), serta pasangan `[Clear Field]` dan `[Apply]` di akhir TC-GS-USER-800, 801, 805, dan 806 (melepas filter yang diterapkan). Filter Panel yang masih terbuka dari TC-GS-USER-798 dipakai ulang oleh TC-GS-USER-799.
- Filter Panel diasumsikan menutup setelah `[Apply]` dan dibuka kembali lewat icon Filter; asumsi ini tidak disebut TC maupun PRD.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` baris `{transaksi-C}` tidak tampil (TC-GS-USER-801) dan baris `Budi S` tidak tampil (TC-GS-USER-806) memperjelas OR dan AND; keduanya didahului `Verifikasi` baris yang tampil pada hasil yang sama (8b butir 2). `Verifikasi` baris `{tanggal-D2}` tidak tampil (TC-GS-USER-805) dengan pola yang sama. Jumlah baris 4 pada TC-GS-USER-806 berasal dari matriks seed (Transfer dengan R2).
- Pembagian TC lintas spec: TC-GS-USER-393, 394, 792 sampai 797 (screening, state kosong, Search) ada di spec 126; TC-GS-USER-807 sampai 811 ada di spec 128; TC-GS-USER-812, 813, 828, 829 ada di spec 129; TC-GS-USER-814 sampai 822 ada di spec 130; TC-GS-USER-395 dan 823 sampai 827 ada di spec 131.
- Spec melewati sekitar 35 langkah (99 langkah) karena sembilan TC Filter Panel berada di satu kelas harness (fungsional, baca saja), satu sub-tab, dan dataset seed yang sama; tiap blok berdiri sendiri dan melepas filternya sendiri, jadi kegagalan satu blok tidak membuat blok lain kehilangan makna. Memisahkannya mengulang login, seeding 30 request approval, dan pembukaan sub-tab yang sama.
- Temuan untuk QA:
  - TC-GS-USER-799: TC tidak menyebut format label opsi Requester; spec mengasersi opsi `Budi S`, `Citra A`, `Dedi K` mengikuti format kolom `[First Name] [Last Initial]`. Nilai Transaction `{transaksi-D}` yang tidak di-seed dipilih tim FE/BE dari enam nilai FAAP.
  - TC-GS-USER-805: TC tidak menyebut apakah rentang tanggal inklusif; spec memakai rentang satu hari dan mengasersi baris pada tanggal itu tampil.
  - TC-GS-USER-806: TC hanya menyebut "Isi 2 field filter berbeda"; spec memilih Transaction `Transfer` dan Requester `Citra A`.
  - TC-GS-USER-802 dan 803: TC tidak menyebut apakah dropdown menutup sendiri sesudah memilih opsi; spec menutupnya dengan langkah eksplisit.
  - Mekanisme seeding user Requester dan request approval FAMS (jenis Transaction, Requester, Submission Date, Approver) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan. TC tidak menyebut nilai Transaction selain `Transfer`; dua nilai FAAP lain dipilih tim FE/BE.
  - Mekanisme menyetel flag Guided Tooltip `gs-user` tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (hook suite).
