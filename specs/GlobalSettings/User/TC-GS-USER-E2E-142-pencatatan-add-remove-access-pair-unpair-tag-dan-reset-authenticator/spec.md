---
id: TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator
title: "Pencatatan Add Access, Remove Access, Remove Access Global Settings, Pair TAG, Unpair TAG, dan Reset Authenticator di Changelog, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-884
  - TC-GS-USER-885
  - TC-GS-USER-924
  - TC-GS-USER-886
  - TC-GS-USER-887
  - TC-GS-USER-897
coverage:
  web: automated
---

# Pencatatan Add Access, Remove Access, Remove Access Global Settings, Pair TAG, Unpair TAG, dan Reset Authenticator di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Siti Nurhaliza (No. 2) sebagai pelaku dan pemilik Tab System Log; Division `Finance` (No. 23); TAG `TAG-USR-0001` (No. 25, user, aktif, bebas); Client subscribe Fixed Asset dan Supply Asset (No. 26). Data target Pre-setup No. 10 sampai 21 tidak dipakai sebagai target aksi dan tidak diubah (S-06).
- Data Dinamis (suffix `{runId}-142`; di-seed lewat API di hook `before`; semua user Activated, Division `Finance`; menggantikan Dewi Lestari No. 12, Doni Pratama No. 11, dan John Doe No. 18):
  - `Dewi Lestari Add {runId}-142` (Email `dewilestariadd+{runId}-142@qwertysystem.net`): Access `Fixed Asset` dan `Global Settings`, tanpa Access `Supply Asset` (TC-GS-USER-884).
  - `Dewi Lestari Remove {runId}-142` (Email `dewilestariremove+{runId}-142@qwertysystem.net`): Access `Fixed Asset` dan `Global Settings`, tanpa borrowed asset dan tanpa approval sehingga tidak ada dialog Remove Access produk (TC-GS-USER-885).
  - `Doni Pratama {runId}-142` (Email `donipratama+{runId}-142@qwertysystem.net`): tier Read Only di Role & Permission, Access `Fixed Asset` dan `Global Settings` (TC-GS-USER-924).
  - `Dewi Lestari Pair {runId}-142` (Email `dewilestaripair+{runId}-142@qwertysystem.net`): Access `Fixed Asset`, tanpa TAG (TC-GS-USER-886).
  - `John Doe {runId}-142` (Email `johndoe+{runId}-142@qwertysystem.net`): Access `Fixed Asset`, TAG `TAG-USR-0001` terpasang lewat seeding (TC-GS-USER-887).
  - `John Doe Auth {runId}-142` (Email `johndoeauth+{runId}-142@qwertysystem.net`): Access `Fixed Asset`, Authenticator Enrolled (MFA Enrolled) (TC-GS-USER-897).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD): seeding user, tier Read Only, pairing TAG, dan Authenticator Enrolled lewat API; simulasi scan TAG pada Detail (perangkat RFID reader dianggap tersambung dan ID TAG disuntikkan seolah-olah dipindai); membaca jumlah baris log per user sebagai baseline.
- Hook `before` membebaskan `TAG-USR-0001` dari sisa run lama sebelum seeding `John Doe {runId}-142`. `TAG-USR-0001` dipakai bergantian oleh `John Doe {runId}-142` (dilepas pada TC-GS-USER-887) lalu `Dewi Lestari Pair {runId}-142` (dipasang pada TC-GS-USER-886).
- State global yang diubah: pairing `TAG-USR-0001`; akses Global Settings dan tier Read Only milik `Doni Pratama {runId}-142`. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API keenam user seed di atas (melepas `TAG-USR-0001`). Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-884: Log Add Access field App Access

2. Catat baseline `{n0}` (lewat kemampuan baca BE) sebelum aksi pemicu: jumlah seluruh baris untuk `Dewi Lestari Add {runId}-142`
3. Klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
4. Klik (⋯) baris `Dewi Lestari Add {runId}-142` → `Edit`
5. Centang Access `Supply Asset`
6. Klik `[Save]`
7. Tunggu aksi selesai (Popup Edit tertutup)
8. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
9. Verifikasi Modal Changelog User: baris dengan Action `Add Access`, Name `Dewi Lestari Add {runId}-142`, Field `App Access`, Old Value `—`, New Value `Supply Asset`, Modified By `Siti N`
10. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Add Access` untuk `Dewi Lestari Add {runId}-142` (tidak duplikat)
11. Verifikasi Modal Changelog User: jumlah seluruh baris untuk `Dewi Lestari Add {runId}-142` bertambah tepat 1 dari baseline `{n0}` dan baris itu Action `Add Access` (bukan `Edit`)
12. Buka Detail `Dewi Lestari Add {runId}-142` > Tab `Changelog`
13. Verifikasi Tab Changelog Detail `Dewi Lestari Add {runId}-142`: baris dengan Action `Add Access`, Field `App Access`, Old Value `—`, New Value `Supply Asset`, Modified By `Siti N`
14. Verifikasi Tab Changelog Detail `Dewi Lestari Add {runId}-142`: tepat 1 baris dengan Action `Add Access` (tidak duplikat)
15. Verifikasi Tab Changelog Detail `Dewi Lestari Add {runId}-142`: jumlah seluruh baris bertambah tepat 1 dari baseline `{n0}` dan baris itu Action `Add Access` (bukan `Edit`)
16. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
17. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Add Access`, Object `User`, Name `Dewi Lestari Add {runId}-142`, Field `App Access`, Old Value `—`, New Value `Supply Asset`
18. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Add Access` untuk `Dewi Lestari Add {runId}-142` (tidak duplikat)
19. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
20. Verifikasi Activity Log: baris dengan Action `Add Access`, Object `User`, Name `Dewi Lestari Add {runId}-142`, Field `App Access`, Old Value `—`, New Value `Supply Asset`, Modified By `Siti N`
21. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Add Access` untuk `Dewi Lestari Add {runId}-142` (tidak duplikat)

### TC-GS-USER-887: Log Unpair TAG field TAG

22. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
23. Klik Name `John Doe {runId}-142` di User List
24. Klik `Unpair`
25. Klik `[Unpair]` pada dialog `Unpair TAG`
26. Tunggu aksi selesai (Button `Scan TAG` tampil kembali di sub-section User TAG)
27. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
28. Verifikasi Modal Changelog User: baris dengan Action `Unpair TAG`, Name `John Doe {runId}-142`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, Modified By `Siti N`
29. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Unpair TAG` untuk `John Doe {runId}-142` (tidak duplikat)
30. Buka Detail `John Doe {runId}-142` > Tab `Changelog`
31. Verifikasi Tab Changelog Detail `John Doe {runId}-142`: baris dengan Action `Unpair TAG`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, Modified By `Siti N`
32. Verifikasi Tab Changelog Detail `John Doe {runId}-142`: tepat 1 baris dengan Action `Unpair TAG` (tidak duplikat)
33. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
34. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Unpair TAG`, Object `User`, Name `John Doe {runId}-142`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`
35. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Unpair TAG` untuk `John Doe {runId}-142` (tidak duplikat)
36. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
37. Verifikasi Activity Log: baris dengan Action `Unpair TAG`, Object `User`, Name `John Doe {runId}-142`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, Modified By `Siti N`
38. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Unpair TAG` untuk `John Doe {runId}-142` (tidak duplikat)

### TC-GS-USER-897: Log Reset Authenticator field Authenticator Enrollment

39. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
40. Klik Name `John Doe Auth {runId}-142` di User List
41. Klik `Reset Authenticator` → `[Reset]`
42. Tunggu aksi selesai (Badge Authenticator berubah `Not enrolled yet`)
43. Buka Modal Changelog User, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
44. Verifikasi Modal Changelog User: baris dengan Action `Reset Authenticator`, Name `John Doe Auth {runId}-142`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`, Modified By `Siti N`
45. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Reset Authenticator` untuk `John Doe Auth {runId}-142` (tidak duplikat)
46. Buka Detail `John Doe Auth {runId}-142` > Tab `Changelog`
47. Verifikasi Tab Changelog Detail `John Doe Auth {runId}-142`: baris dengan Action `Reset Authenticator`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`, Modified By `Siti N`
48. Verifikasi Tab Changelog Detail `John Doe Auth {runId}-142`: tepat 1 baris dengan Action `Reset Authenticator` (tidak duplikat)
49. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
50. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Reset Authenticator`, Object `User`, Name `John Doe Auth {runId}-142`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`
51. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Reset Authenticator` untuk `John Doe Auth {runId}-142` (tidak duplikat)
52. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
53. Verifikasi Activity Log: baris dengan Action `Reset Authenticator`, Object `User`, Name `John Doe Auth {runId}-142`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`, Modified By `Siti N`
54. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Reset Authenticator` untuk `John Doe Auth {runId}-142` (tidak duplikat)

### TC-GS-USER-885: Log Remove Access field App Access

55. Catat baseline `{n0}` (lewat kemampuan baca BE) sebelum aksi pemicu: jumlah seluruh baris untuk `Dewi Lestari Remove {runId}-142`
56. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
57. Klik (⋯) baris `Dewi Lestari Remove {runId}-142` → `Edit`
58. Uncheck Access `Fixed Asset`
59. Klik `[Save]`
60. Tunggu aksi selesai (Popup Edit tertutup)
61. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
62. Verifikasi Modal Changelog User: baris dengan Action `Remove Access`, Name `Dewi Lestari Remove {runId}-142`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, Modified By `Siti N`
63. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Remove Access` untuk `Dewi Lestari Remove {runId}-142` (tidak duplikat)
64. Verifikasi Modal Changelog User: jumlah seluruh baris untuk `Dewi Lestari Remove {runId}-142` bertambah tepat 1 dari baseline `{n0}` dan baris itu Action `Remove Access` (bukan `Edit`; 1 baris per produk yang dicabut)
65. Buka Detail `Dewi Lestari Remove {runId}-142` > Tab `Changelog`
66. Verifikasi Tab Changelog Detail `Dewi Lestari Remove {runId}-142`: baris dengan Action `Remove Access`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, Modified By `Siti N`
67. Verifikasi Tab Changelog Detail `Dewi Lestari Remove {runId}-142`: tepat 1 baris dengan Action `Remove Access` (tidak duplikat)
68. Verifikasi Tab Changelog Detail `Dewi Lestari Remove {runId}-142`: jumlah seluruh baris bertambah tepat 1 dari baseline `{n0}` dan baris itu Action `Remove Access` (bukan `Edit`; 1 baris per produk yang dicabut)
69. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
70. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Remove Access`, Object `User`, Name `Dewi Lestari Remove {runId}-142`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`
71. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Remove Access` untuk `Dewi Lestari Remove {runId}-142` (tidak duplikat)
72. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
73. Verifikasi Activity Log: baris dengan Action `Remove Access`, Object `User`, Name `Dewi Lestari Remove {runId}-142`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, Modified By `Siti N`
74. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Remove Access` untuk `Dewi Lestari Remove {runId}-142` (tidak duplikat)

### TC-GS-USER-924: Remove Access Global Settings menulis satu baris Remove Access di log User

75. Catat baseline `{n0}` (lewat kemampuan baca BE) sebelum aksi pemicu: jumlah seluruh baris untuk `Doni Pratama {runId}-142`
76. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Doni Pratama {runId}-142`, tekan Enter
77. Klik (⋯) baris `Doni Pratama {runId}-142` → `Edit`
78. Uncheck Access `Global Settings`
79. Klik `[Save]`
80. Klik `[Remove]` pada dialog `Remove Access`
81. Tunggu aksi selesai (Popup Edit tertutup)
82. Buka Modal Changelog User, klik icon Search, ketik `Doni Pratama {runId}-142`, tekan Enter
83. Verifikasi Modal Changelog User: tepat 1 baris dengan Action `Remove Access`, Name `Doni Pratama {runId}-142`, Field `App Access`, Old Value `Global Settings`, New Value `—`, Modified By `Siti N`
84. Verifikasi Modal Changelog User: jumlah seluruh baris untuk `Doni Pratama {runId}-142` bertambah tepat 1 dari baseline `{n0}` (detail per role tidak ditulis di log User)

### TC-GS-USER-886: Log Pair TAG field TAG

85. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
86. Klik Name `Dewi Lestari Pair {runId}-142` di User List
87. Klik `Scan TAG`
88. Scan `TAG-USR-0001`
89. Tunggu aksi selesai (Badge `Verified` dan Button `Unpair` tampil di sub-section User TAG)
90. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
91. Verifikasi Modal Changelog User: baris dengan Action `Pair TAG`, Name `Dewi Lestari Pair {runId}-142`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`, Modified By `Siti N`
92. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Pair TAG` untuk `Dewi Lestari Pair {runId}-142` (tidak duplikat)
93. Buka Detail `Dewi Lestari Pair {runId}-142` > Tab `Changelog`
94. Verifikasi Tab Changelog Detail `Dewi Lestari Pair {runId}-142`: baris dengan Action `Pair TAG`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`, Modified By `Siti N`
95. Verifikasi Tab Changelog Detail `Dewi Lestari Pair {runId}-142`: tepat 1 baris dengan Action `Pair TAG` (tidak duplikat)
96. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
97. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Pair TAG`, Object `User`, Name `Dewi Lestari Pair {runId}-142`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`
98. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Pair TAG` untuk `Dewi Lestari Pair {runId}-142` (tidak duplikat)
99. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
100. Verifikasi Activity Log: baris dengan Action `Pair TAG`, Object `User`, Name `Dewi Lestari Pair {runId}-142`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`, Modified By `Siti N`
101. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Pair TAG` untuk `Dewi Lestari Pair {runId}-142` (tidak duplikat)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Baris log dikenali lewat nama bersuffix `{runId}-142` yang unik per run, Action, dan Field, bukan posisi teratas dan bukan penanda waktu (S-12). Tiap TC memakai user seed sendiri; TC-GS-USER-884, 885, dan 924 mencatat baseline jumlah seluruh baris user sebelum aksi pemicu (entri seed tidak diasumsikan nol) dan mengasersi selisih.
- Surface disebut satu per satu pada TC-GS-USER-884, 887, 886, 897, dan 885: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. TC-GS-USER-924 hanya memuat Modal Changelog User sesuai Langkah Uji. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Urutan TC di spec: 884, 887, 897, 885, 924, 886. TC-GS-USER-887 dijalankan sebelum TC-GS-USER-886 karena `TAG-USR-0001` harus bebas sebelum dipasang ke `Dewi Lestari Pair {runId}-142` (satu-satunya TAG user bebas di Tabel Pre-setup No. 25). TC-GS-USER-886 (simulator scan `TAG-USR-0001`, langkah 87 dan 88) dipindah ke akhir spec (langkah 85 sampai 101) supaya kegagalan simulator tidak menutupi blok lain (konvensi bagian 3, pemisah nyata hardware berisiko); dua TC yang mencabut akses (885, 924) tetap mendahuluinya dan tiap blok memakai user seed sendiri, sehingga tidak ada state yang perlu dipulihkan antar blok (langkah 85 membuka kembali User List).
- Pemisahan blok simulator scan (konvensi bagian 3, pemisah nyata hardware berisiko): TC-GS-USER-886 membutuhkan simulator scan TAG; objek ujinya adalah pencatatan log Pair TAG, bukan perangkat scan; scan hanya memicu aksi Pair.
- Pembagian TC lintas spec: Expected f TC-GS-USER-897 ("Tidak tercatat di Tab User Log") adalah asersi absence kelas g dan diverifikasi di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role` lewat TC-GS-USER-942 (aksi Reset Authenticator dengan baseline sendiri); spec ini tidak mengasersinya. Absence Product Selector (TC-GS-USER-925) juga ada di spec 147. Klausa Expected f TC-GS-USER-884 dan 885 ("Action `Add Access`/`Remove Access`, bukan `Edit`") serta Expected b TC-GS-USER-924 ("Detail per role tidak ditulis di log User") diasersi di spec ini sebagai selisih jumlah seluruh baris untuk user seed itu terhadap baseline `{n0}` (tepat 1), bukan asersi absence kelas g. Changelog Role & Permission (tempat detail per role) tidak diasersi karena tidak ada di Langkah Uji TC-GS-USER-924.
- Spec melewati sekitar 35 langkah (101 langkah). Alasan: seluruh blok satu kelas (pencatatan log) dengan user seed sendiri per TC sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan tidak dihitung ke batas ukuran (bagian 3 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 8, 12, 16, 19, 22 sampai 27, 30, 33, 36, 39 sampai 43, 46, 49, 52, 55 sampai 61, 65, 69, 72, 75 sampai 82, 85 sampai 90, 93, 96, 99. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama.
- Temuan untuk QA:
  - TC-GS-USER-887: Expected menyebut `TAG-4F7K2XQ9` yang terpasang pada John Doe Pre-setup (No. 18) dan tidak dapat dipasang ke user seed; spec memakai `TAG-USR-0001` pada user seed milik spec.
  - TC-GS-USER-886 memakai simulasi scan TAG (HK7); TC-GS-USER-887 memakai TAG hasil seeding; TC-GS-USER-884, 885, dan 924 hanya memakai UI Popup Edit.
  - TC-GS-USER-897: Precondition tidak menyebut John Doe Enrolled; spec men-seed Authenticator Enrolled (disediakan tim FE/BE). Tanda Enrolled atau Not enrolled yet dibaca dari Badge Authenticator di Detail; nama elemen itu mengikuti TC Detail Reset Authenticator.
  - TC-GS-USER-924: Langkah Uji "Remove Access GS Doni Pratama (konfirmasi)" tidak menyebut Edit dan `[Save]`; spec memakai alur Popup Edit yang sama dengan TC Remove Access Global Settings. Expected b memuat penjelasan dalam tanda kurung ("ada di Changelog Role & Permission") yang tidak diasersi.
  - TC-GS-USER-884, 885, 886, 887, 897 memakai nama Pre-setup (Dewi Lestari, John Doe) dan TC-GS-USER-924 memakai Doni Pratama Pre-setup sebagai target tulis; spec memakai padanan seed bersuffix (S-06).
  - Asumsi seeding: seeding user dan data pendukung lewat API hanya menghasilkan entri log aksi `Create`; spec tidak mengandalkan entri Update atau Delete dari seeding (diterima 2026-11-03).
