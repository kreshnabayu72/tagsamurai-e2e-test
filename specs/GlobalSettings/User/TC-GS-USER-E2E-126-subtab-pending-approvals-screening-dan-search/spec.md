---
id: TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search
title: "Sub-tab Pending Approvals: Screening, State Kosong, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-393
  - TC-GS-USER-394
  - TC-GS-USER-792
  - TC-GS-USER-793
  - TC-GS-USER-794
  - TC-GS-USER-795
  - TC-GS-USER-796
  - TC-GS-USER-797
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Screening, State Kosong, dan Search

## Prerequisites

- Mode: FE+BE. Spec hanya membaca sub-tab Pending Approvals Ahmad Fauzi (read-only, tanpa row action) dan tidak mengubah data Pre-setup User.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Ahmad Fauzi (No. 13, data Responsibilities FAMS), Rina Kartika (No. 30; data hanya di sub-tab Responsibilities Borrowed Assets, sedangkan Assigned Assets, Pending Approvals, dan Pending Tasks kosong; tanpa data Pending Approvals), Client FAMS aktif (TC-GS-USER-394).
- Data Dinamis (HK8, seeding minimal S-11; seeding user dan approval FAMS lewat API di hook `before` adalah kemampuan yang disediakan tim FE/BE, endpoint tidak disebut di TC, PRD, dan LLD):
  - Requester seed (user biasa, Access `Fixed Asset`, Division `Finance`): R1 First Name `Budi`, Last Name `Santoso {runId}-126`, email `budisantoso+{runId}-126@qwertysystem.net`, tampil di tabel `Budi S`; R2 First Name `Citra`, Last Name `Anggraini {runId}-126`, email `citraanggraini+{runId}-126@qwertysystem.net`, tampil `Citra A`; R3 First Name `Dedi`, Last Name `Kurniawan {runId}-126`, email `dedikurniawan+{runId}-126@qwertysystem.net`, tampil `Dedi K`.
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
  - Keyword unik Requester (hanya cocok dengan Requester seed spec ini karena memuat suffix): `ntoso {runId}-126` (R1), `raini {runId}-126` (R2), `{runId}-126` (R1, R2, R3).
  - Baris Pre-setup Pending Approvals Ahmad Fauzi (bila ada) tidak diubah dan jumlahnya tidak diasumsikan: asersi jumlah baris memakai keyword atau filter yang hanya cocok dengan baris seed, dan asersi urutan atau isi umum tidak bergantung pada baris Pre-setup.
  - Cleanup di hook `after` (tanpa berasumsi seeding berhasil penuh): hapus 30 request approval seed dan user Requester seed lewat API.
- Data uji per TC: TC-GS-USER-393 Search `{trxId-contoh}`; TC-GS-USER-792 keyword `Transfer`; TC-GS-USER-793 keyword `  TRANSFER  `; TC-GS-USER-794 `{potongan-ID}`, `ransfe`, `ntoso {runId}-126`; TC-GS-USER-795 `{tanggal-D1}`; TC-GS-USER-796 `ntoso {runId}-126`; TC-GS-USER-797 `zzzqqq`. Data Rina Kartika (TC-GS-USER-394) tanpa request approval; spec tidak membuat approval untuk Rina Kartika.
- State yang diubah dan dipulihkan: Search dikosongkan dan ditutup di akhir tiap TC; page size dikembalikan ke 10 oleh hook `after`; visibilitas kolom `Requester` dikembalikan di langkah 86; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`): tabel Pending Approvals Ahmad Fauzi hanya boleh memuat baris Pre-setup dan seed spec ini saat spec berjalan.
- Kemampuan teknis: hover elemen; membaca teks sel tabel dan menghitung baris; mengubah page size lewat kontrol pagination.

## Test Steps

### TC-GS-USER-393: Screening sub-tab Pending Approvals

1. Ketik Search `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Approvals`
5. Verifikasi toolbar menampilkan `Search`, `Filter`, dan `Download`
6. Klik icon Search
7. Verifikasi input Search kosong dengan placeholder `Search transaction ID, transaction, or requester...`
8. Klik icon panah `(←)` di kiri toolbar
9. Verifikasi kolom tabel berurutan `Transaction ID`, `Transaction`, `Requester`, `Submission Date`, dan Column Visibility (⋯)
10. Verifikasi baris tabel terurut Submission Date Oldest First (default sort)
11. Verifikasi kontrol pagination tampil (total baris lebih dari 10)
12. Klik icon Search, ketik `{trxId-contoh}`, tekan Enter
13. Verifikasi tabel menampilkan baris contoh dengan Transaction ID `{trxId-contoh}`
14. Verifikasi Transaction ID baris contoh tampil sebagai teks biasa, bukan tautan
15. Verifikasi Transaction baris contoh `Transfer`
16. Verifikasi Requester baris contoh `Budi S` (format `[First Name] [Last Initial]`)
17. Arahkan kursor ke Requester `Budi S` pada baris contoh
18. Verifikasi hover menampilkan nama lengkap `Budi Santoso {runId}-126`
19. Verifikasi baris contoh tidak memiliki row action, dan kolom Actions hanya memuat pemicu Column Visibility (⋯)
20. Verifikasi kontrol pagination tidak tampil (hasil Search satu baris, kurang dari atau sama dengan 10 baris)
21. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-394: Empty state sub-tab Pending Approvals

22. Kembali ke User List (Global Settings > User > User List, sub-tab Login User)
23. Ganti isi kotak search dengan `Rina Kartika`, tekan Enter
24. Klik Name `Rina Kartika` di User List
25. Klik Tab `Responsibilities`
26. Klik sub-tab `Pending Approvals`
27. Verifikasi ilustrasi empty state tampil
28. Verifikasi judul empty state `No pending approvals`
29. Verifikasi deskripsi empty state `Pending approval requests will appear here.`

### TC-GS-USER-792: Siklus Search: reveal, Enter, clear (✕), collapse ←

30. Kembali ke User List (Global Settings > User > User List, sub-tab Login User)
31. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
32. Klik Name `Ahmad Fauzi` di User List
33. Klik Tab `Responsibilities`
34. Klik sub-tab `Pending Approvals`
35. Ubah page size ke 100 supaya seluruh baris seed tampil dalam satu halaman
36. Baca jumlah baris tabel sebagai `{baris-awal}`
37. Klik icon Search
38. Verifikasi input Search melebar
39. Verifikasi kursor auto-focus di input Search
40. Ketik `Transfer` pada kotak Search
41. Verifikasi icon `(✕)` muncul di dalam input
42. Verifikasi tabel belum tersaring (jumlah baris tetap `{baris-awal}`)
43. Tekan Enter
44. Verifikasi tabel tersaring: seluruh baris yang tampil bernilai Transaction `Transfer`
45. Baca jumlah baris tabel sebagai `{baris-transfer}`
46. Klik icon `(✕)`
47. Verifikasi input Search kosong
48. Verifikasi tabel tetap menampilkan hasil terakhir (jumlah baris `{baris-transfer}`)
49. Tekan Enter pada input Search yang kosong
50. Verifikasi tabel kembali menampilkan semua data (jumlah baris `{baris-awal}`)
51. Isi Search dengan `Transfer`, tekan Enter
52. Klik icon panah `(←)` di kiri toolbar
53. Verifikasi kotak pencarian menutup menjadi icon Search biasa
54. Verifikasi tabel langsung kembali menampilkan semua data tanpa menekan Enter (jumlah baris `{baris-awal}`)
55. Klik icon Search
56. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-USER-793: Query Search di-trim dan tidak case-sensitive

57. Isi Search dengan `  TRANSFER  `, tekan Enter
58. Verifikasi baris yang memuat `Transfer` tampil: seluruh baris bernilai Transaction `Transfer` dan jumlah baris `{baris-transfer}` (spasi diabaikan, huruf besar dan kecil tidak dibedakan)
59. Verifikasi isi kotak Search tetap `  TRANSFER  ` apa adanya
60. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-794: Search menemukan substring pada kolom kelas teks

61. Klik icon Search, ketik `{potongan-ID}` (Transaction ID `{trxId-contoh}` tanpa karakter terakhir), tekan Enter
62. Verifikasi baris contoh dengan Transaction ID `{trxId-contoh}` tampil
63. Klik icon `×`
64. Tekan Enter pada input Search yang kosong
65. Isi Search dengan `ransfe`, tekan Enter
66. Verifikasi baris contoh dengan Transaction `Transfer` tampil
67. Klik icon `×`
68. Tekan Enter pada input Search yang kosong
69. Isi Search dengan `ntoso {runId}-126`, tekan Enter
70. Verifikasi baris contoh dengan Requester `Budi S` tampil
71. Verifikasi baris dengan Requester `Citra A` tidak tampil
72. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-795: Kolom non-searchable tidak tercakup Search

73. Verifikasi baris contoh menampilkan Submission Date `{tanggal-D1}` (teks tanggal dalam Date Format General Settings)
74. Klik icon Search, ketik `{tanggal-D1}`, tekan Enter
75. Verifikasi no result state: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
76. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-796: Search tidak mencocokkan kolom yang di-hide, kembali cocok setelah unhide

77. Klik header kolom Actions (⋯)
78. Hilangkan centang kolom `Requester` pada Overlay Column Visibility
79. Tutup Overlay Column Visibility
80. Verifikasi kolom `Requester` tidak tampil di tabel
81. Verifikasi kolom `Transaction ID` tetap tampil dengan baris tabel (pembanding sebelum Search)
82. Klik icon Search, ketik `ntoso {runId}-126`, tekan Enter
83. Verifikasi no result state: ilustrasi, `No results found`, dan `Try adjusting your search or filter.` (saat kolom Requester hidden)
84. Klik header kolom Actions (⋯)
85. Centang kembali kolom `Requester` pada Overlay Column Visibility
86. Tutup Overlay Column Visibility
87. Klik kotak Search yang berisi `ntoso {runId}-126`, tekan Enter
88. Verifikasi baris dengan Requester `Budi S` kembali tampil
89. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-797: Empty filtered state

90. Klik icon Search, ketik `zzzqqq`, tekan Enter
91. Verifikasi empty filtered state: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
92. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dependensi data Pending Approvals Ahmad Fauzi dipenuhi spec ini lewat seeding di hook `before`, tanpa menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber (393, 394, 792, 793, 794, 795, 796, 797) dipertahankan; dua TC screening (393, 394) berada di awal.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 23, dan 31 (Search nama baris persis di User List sebelum Klik Name, karena User List bisa lebih dari satu halaman; langkah 23 dan 31 memakai "ganti isi kotak search" karena Search User List mungkin masih berisi nama sebelumnya), langkah 6 dan 8 (membuka dan menutup Search untuk mengamati placeholder, penghubung TC-GS-USER-393), langkah 12 (mencari baris contoh dengan Transaction ID-nya supaya asersi baris contoh tidak bergantung halaman), 21, 60, 72, 76, 89, dan 92 (menutup Search dan mereset tabel), 22 dan 30 (kembali ke User List sebelum membuka user lain), 35 (page size 100 supaya semua baris seed tampil di satu halaman), 36 dan 45 (membaca jumlah baris untuk pembanding), 55 (membuka kembali Search agar keyword dikosongkan teramati), 64 dan 68 (membersihkan Search di antara kolom pada TC-GS-USER-794), serta 79 dan 86 (menutup Overlay Column Visibility).
- Search bar yang masih terbuka dari langkah sebelumnya dipakai ulang dengan "Isi Search dengan" atau "ganti isi kotak search dengan" (bagian 8b butir 9).
- TC-GS-USER-393 Expected e ("≤10 baris: kontrol pagination tidak tampil") diasersi pada hasil Search satu baris, didahului `Verifikasi` bahwa kontrol pagination tampil pada tabel penuh sebagai pembanding (8b butir 2), karena seeding membuat tabel lebih dari satu halaman.
- Asersi tambahan di luar Expected TC (S-03): pembanding kolom `Transaction ID` tampil sebelum Search pada TC-GS-USER-796, dan `Verifikasi` baris dengan Requester `Citra A` tidak tampil pada TC-GS-USER-794 (didahului baris `Budi S` tampil pada hasil yang sama); keduanya anchor absence.
- Pembagian TC lintas spec: TC-GS-USER-798 sampai 806 (Filter Panel) ada di spec 127; TC-GS-USER-807 sampai 811 (kombinasi Search dan Filter) ada di spec 128; TC-GS-USER-812, 813, 828, 829 (Sort, Pagination, kombinasi) ada di spec 129; TC-GS-USER-814 sampai 822 (Setup Column) ada di spec 130; TC-GS-USER-395 dan 823 sampai 827 (Download) ada di spec 131.
- Spec melewati sekitar 35 langkah (92 langkah) karena delapan TC berada di satu kelas harness (fungsional, baca saja), satu sub-tab, dan dataset seed yang sama; tiap blok TC berdiri sendiri dan membersihkan state Search-nya sendiri, jadi kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan sub-tab Ahmad Fauzi dipakai bersama oleh enam TC (langkah pembuka tidak dihitung ke batas).
- Temuan untuk QA:
  - TC-GS-USER-393: Transaction ID `REQ-TRF-0089` dan Requester `Budi S` pada Expected c adalah contoh PRD; Transaction ID dibuat FAMS saat seeding sehingga spec memakai `{trxId-contoh}` dan Requester seed `Budi S`.
  - TC-GS-USER-393 Expected e (≤10 baris) bertentangan dengan kebutuhan data lebih dari satu halaman untuk spec ini; spec mengasersinya pada hasil Search yang menyisakan satu baris.
  - TC-GS-USER-393 Expected d: TC tidak menyebut cara mengamati "tanpa row action"; spec mengasersi tidak ada tombol aksi pada baris dan kolom Actions hanya berisi pemicu Column Visibility.
  - TC-GS-USER-792 Expected b: "tabel belum tersaring" diasersi lewat jumlah baris yang tidak berubah; TC tidak menyebut indikator lain.
  - TC-GS-USER-794: TC hanya memberi contoh `Transfer`; potongan nilai tiap kolom dipilih spec (`{potongan-ID}`, `ransfe`, `ntoso {runId}-126`).
  - TC-GS-USER-795: TC tidak menyebut teks no result state; spec memakai teks empty filtered state TC-GS-USER-797.
  - TC-GS-USER-796 langkah 8: TC tidak menyebut fokus untuk "Tekan Enter lagi"; spec mengklik kotak Search yang masih berisi keyword lalu menekan Enter.
  - TC-GS-USER-394: Precondition d ("Client FAMS aktif") bergantung pada subscription entitas uji; disediakan tim FE.
  - Mekanisme seeding user Requester dan request approval FAMS (jenis Transaction, Requester, Submission Date, Approver) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan. TC tidak menyebut nilai Transaction selain `Transfer`; dua nilai FAAP lain dipilih tim FE/BE.
  - Mekanisme menyetel flag Guided Tooltip `gs-user` tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (hook suite).
