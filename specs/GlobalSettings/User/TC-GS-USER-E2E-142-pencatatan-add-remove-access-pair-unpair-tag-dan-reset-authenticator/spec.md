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
- Data Dinamis (suffix `{runId}-142`; di-seed lewat API di hook `before` sebelum penanda waktu T142; semua user Activated, Division `Finance`; menggantikan Dewi Lestari No. 12, Doni Pratama No. 11, dan John Doe No. 18):
  - `Dewi Lestari Add {runId}-142` (Email `dewilestariadd+{runId}-142@qwertysystem.net`): Access `Fixed Asset` dan `Global Settings`, tanpa Access `Supply Asset` (TC-GS-USER-884).
  - `Dewi Lestari Remove {runId}-142` (Email `dewilestariremove+{runId}-142@qwertysystem.net`): Access `Fixed Asset` dan `Global Settings`, tanpa borrowed asset dan tanpa approval sehingga tidak ada dialog Remove Access produk (TC-GS-USER-885).
  - `Doni Pratama {runId}-142` (Email `donipratama+{runId}-142@qwertysystem.net`): tier Read Only di Role & Permission, Access `Fixed Asset` dan `Global Settings` (TC-GS-USER-924).
  - `Dewi Lestari Pair {runId}-142` (Email `dewilestaripair+{runId}-142@qwertysystem.net`): Access `Fixed Asset`, tanpa TAG (TC-GS-USER-886).
  - `John Doe {runId}-142` (Email `johndoe+{runId}-142@qwertysystem.net`): Access `Fixed Asset`, TAG `TAG-USR-0001` terpasang lewat seeding (TC-GS-USER-887).
  - `John Doe Auth {runId}-142` (Email `johndoeauth+{runId}-142@qwertysystem.net`): Access `Fixed Asset`, Authenticator Enrolled (MFA Enrolled) (TC-GS-USER-897).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD): seeding user, tier Read Only, pairing TAG, dan Authenticator Enrolled lewat API; simulasi scan TAG pada Detail (perangkat RFID reader dianggap tersambung dan ID TAG disuntikkan seolah-olah dipindai); membaca waktu server untuk penanda waktu T142.
- Hook `before` membebaskan `TAG-USR-0001` dari sisa run lama sebelum seeding `John Doe {runId}-142`. `TAG-USR-0001` dipakai bergantian oleh `John Doe {runId}-142` (dilepas pada TC-GS-USER-887) lalu `Dewi Lestari Pair {runId}-142` (dipasang pada TC-GS-USER-886).
- State global yang diubah: pairing `TAG-USR-0001`; akses Global Settings dan tier Read Only milik `Doni Pratama {runId}-142`. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API keenam user seed di atas (melepas `TAG-USR-0001`). Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan penanda waktu

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Catat penanda waktu T142 (waktu server) sebelum aksi pemicu pertama (klik `[Save]` pada TC-GS-USER-884)

### TC-GS-USER-884: Log Add Access field App Access

3. Klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
4. Klik (⋯) baris `Dewi Lestari Add {runId}-142` → `Edit`
5. Centang Access `Supply Asset`
6. Klik `[Save]`
7. Tunggu aksi selesai (Popup Edit tertutup)
8. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
9. Verifikasi Modal Changelog User: baris dengan Action `Add Access`, Name `Dewi Lestari Add {runId}-142`, Field `App Access`, Old Value `—`, New Value `Supply Asset`, Modified By `Siti N`, bertanggal pada atau sesudah T142
10. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Add Access` untuk `Dewi Lestari Add {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
11. Verifikasi Modal Changelog User: Action baris untuk `Dewi Lestari Add {runId}-142` adalah `Add Access` dan seluruh baris hasil Search bertanggal pada atau sesudah T142 berjumlah tepat 1 (bukan `Edit`)
12. Buka Detail `Dewi Lestari Add {runId}-142` > Tab `Changelog`
13. Verifikasi Tab Changelog Detail `Dewi Lestari Add {runId}-142`: baris dengan Action `Add Access`, Field `App Access`, Old Value `—`, New Value `Supply Asset`, Modified By `Siti N`, bertanggal pada atau sesudah T142
14. Verifikasi Tab Changelog Detail `Dewi Lestari Add {runId}-142`: tepat 1 baris dengan Action `Add Access` bertanggal pada atau sesudah T142 (tidak duplikat)
15. Verifikasi Tab Changelog Detail `Dewi Lestari Add {runId}-142`: Action baris adalah `Add Access` dan seluruh baris bertanggal pada atau sesudah T142 berjumlah tepat 1 (bukan `Edit`)
16. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
17. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Add Access`, Object `User`, Name `Dewi Lestari Add {runId}-142`, Field `App Access`, Old Value `—`, New Value `Supply Asset`, bertanggal pada atau sesudah T142
18. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Add Access` untuk `Dewi Lestari Add {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
19. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Add {runId}-142`, tekan Enter
20. Verifikasi Activity Log: baris dengan Action `Add Access`, Object `User`, Name `Dewi Lestari Add {runId}-142`, Field `App Access`, Old Value `—`, New Value `Supply Asset`, Modified By `Siti N`, bertanggal pada atau sesudah T142
21. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Add Access` untuk `Dewi Lestari Add {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)

### TC-GS-USER-887: Log Unpair TAG field TAG

22. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
23. Klik Name `John Doe {runId}-142` di User List
24. Klik `Unpair`
25. Klik `[Unpair]` pada dialog `Unpair TAG`
26. Tunggu aksi selesai (Button `Scan TAG` tampil kembali di sub-section User TAG)
27. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
28. Verifikasi Modal Changelog User: baris dengan Action `Unpair TAG`, Name `John Doe {runId}-142`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T142
29. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Unpair TAG` untuk `John Doe {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
30. Buka Detail `John Doe {runId}-142` > Tab `Changelog`
31. Verifikasi Tab Changelog Detail `John Doe {runId}-142`: baris dengan Action `Unpair TAG`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T142
32. Verifikasi Tab Changelog Detail `John Doe {runId}-142`: tepat 1 baris dengan Action `Unpair TAG` bertanggal pada atau sesudah T142 (tidak duplikat)
33. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
34. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Unpair TAG`, Object `User`, Name `John Doe {runId}-142`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, bertanggal pada atau sesudah T142
35. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Unpair TAG` untuk `John Doe {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
36. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-142`, tekan Enter
37. Verifikasi Activity Log: baris dengan Action `Unpair TAG`, Object `User`, Name `John Doe {runId}-142`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T142
38. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Unpair TAG` untuk `John Doe {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)

### TC-GS-USER-886: Log Pair TAG field TAG

39. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
40. Klik Name `Dewi Lestari Pair {runId}-142` di User List
41. Klik `Scan TAG`
42. Scan `TAG-USR-0001`
43. Tunggu aksi selesai (Badge `Verified` dan Button `Unpair` tampil di sub-section User TAG)
44. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
45. Verifikasi Modal Changelog User: baris dengan Action `Pair TAG`, Name `Dewi Lestari Pair {runId}-142`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`, Modified By `Siti N`, bertanggal pada atau sesudah T142
46. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Pair TAG` untuk `Dewi Lestari Pair {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
47. Buka Detail `Dewi Lestari Pair {runId}-142` > Tab `Changelog`
48. Verifikasi Tab Changelog Detail `Dewi Lestari Pair {runId}-142`: baris dengan Action `Pair TAG`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`, Modified By `Siti N`, bertanggal pada atau sesudah T142
49. Verifikasi Tab Changelog Detail `Dewi Lestari Pair {runId}-142`: tepat 1 baris dengan Action `Pair TAG` bertanggal pada atau sesudah T142 (tidak duplikat)
50. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
51. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Pair TAG`, Object `User`, Name `Dewi Lestari Pair {runId}-142`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`, bertanggal pada atau sesudah T142
52. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Pair TAG` untuk `Dewi Lestari Pair {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
53. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Pair {runId}-142`, tekan Enter
54. Verifikasi Activity Log: baris dengan Action `Pair TAG`, Object `User`, Name `Dewi Lestari Pair {runId}-142`, Field `TAG`, Old Value `—`, New Value `TAG-USR-0001`, Modified By `Siti N`, bertanggal pada atau sesudah T142
55. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Pair TAG` untuk `Dewi Lestari Pair {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)

### TC-GS-USER-897: Log Reset Authenticator field Authenticator Enrollment

56. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
57. Klik Name `John Doe Auth {runId}-142` di User List
58. Klik `Reset Authenticator` → `[Reset]`
59. Tunggu aksi selesai (Badge Authenticator berubah `Not Enrolled`)
60. Buka Modal Changelog User, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
61. Verifikasi Modal Changelog User: baris dengan Action `Reset Authenticator`, Name `John Doe Auth {runId}-142`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`, Modified By `Siti N`, bertanggal pada atau sesudah T142
62. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Reset Authenticator` untuk `John Doe Auth {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
63. Buka Detail `John Doe Auth {runId}-142` > Tab `Changelog`
64. Verifikasi Tab Changelog Detail `John Doe Auth {runId}-142`: baris dengan Action `Reset Authenticator`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`, Modified By `Siti N`, bertanggal pada atau sesudah T142
65. Verifikasi Tab Changelog Detail `John Doe Auth {runId}-142`: tepat 1 baris dengan Action `Reset Authenticator` bertanggal pada atau sesudah T142 (tidak duplikat)
66. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
67. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Reset Authenticator`, Object `User`, Name `John Doe Auth {runId}-142`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`, bertanggal pada atau sesudah T142
68. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Reset Authenticator` untuk `John Doe Auth {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
69. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe Auth {runId}-142`, tekan Enter
70. Verifikasi Activity Log: baris dengan Action `Reset Authenticator`, Object `User`, Name `John Doe Auth {runId}-142`, Field `Authenticator Enrollment`, Old Value `Enrolled`, New Value `Not Enrolled`, Modified By `Siti N`, bertanggal pada atau sesudah T142
71. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Reset Authenticator` untuk `John Doe Auth {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)

### TC-GS-USER-885: Log Remove Access field App Access

72. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
73. Klik (⋯) baris `Dewi Lestari Remove {runId}-142` → `Edit`
74. Uncheck Access `Fixed Asset`
75. Klik `[Save]`
76. Tunggu aksi selesai (Popup Edit tertutup)
77. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
78. Verifikasi Modal Changelog User: baris dengan Action `Remove Access`, Name `Dewi Lestari Remove {runId}-142`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T142
79. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Remove Access` untuk `Dewi Lestari Remove {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
80. Verifikasi Modal Changelog User: Action baris untuk `Dewi Lestari Remove {runId}-142` adalah `Remove Access` (bukan `Edit`) dan seluruh baris hasil Search bertanggal pada atau sesudah T142 berjumlah tepat 1 (1 baris per produk yang dicabut)
81. Buka Detail `Dewi Lestari Remove {runId}-142` > Tab `Changelog`
82. Verifikasi Tab Changelog Detail `Dewi Lestari Remove {runId}-142`: baris dengan Action `Remove Access`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T142
83. Verifikasi Tab Changelog Detail `Dewi Lestari Remove {runId}-142`: tepat 1 baris dengan Action `Remove Access` bertanggal pada atau sesudah T142 (tidak duplikat)
84. Verifikasi Tab Changelog Detail `Dewi Lestari Remove {runId}-142`: Action baris adalah `Remove Access` (bukan `Edit`) dan seluruh baris bertanggal pada atau sesudah T142 berjumlah tepat 1 (1 baris per produk yang dicabut)
85. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
86. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Remove Access`, Object `User`, Name `Dewi Lestari Remove {runId}-142`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, bertanggal pada atau sesudah T142
87. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Remove Access` untuk `Dewi Lestari Remove {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)
88. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Remove {runId}-142`, tekan Enter
89. Verifikasi Activity Log: baris dengan Action `Remove Access`, Object `User`, Name `Dewi Lestari Remove {runId}-142`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T142
90. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Remove Access` untuk `Dewi Lestari Remove {runId}-142` bertanggal pada atau sesudah T142 (tidak duplikat)

### TC-GS-USER-924: Remove Access Global Settings menulis satu baris Remove Access di log User

91. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Doni Pratama {runId}-142`, tekan Enter
92. Klik (⋯) baris `Doni Pratama {runId}-142` → `Edit`
93. Uncheck Access `Global Settings`
94. Klik `[Save]`
95. Klik `[Remove]` pada dialog `Remove Access`
96. Tunggu aksi selesai (Popup Edit tertutup)
97. Buka Modal Changelog User, klik icon Search, ketik `Doni Pratama {runId}-142`, tekan Enter
98. Verifikasi Modal Changelog User: tepat 1 baris dengan Action `Remove Access`, Name `Doni Pratama {runId}-142`, Field `App Access`, Old Value `Global Settings`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T142
99. Verifikasi Modal Changelog User: seluruh baris hasil Search `Doni Pratama {runId}-142` bertanggal pada atau sesudah T142 berjumlah tepat 1 (detail per role tidak ditulis di log User)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penanda waktu T142 dicatat di langkah 2, sebelum aksi pemicu pertama yang diasersi (S-12). Tiap TC memakai user seed sendiri, sehingga satu penanda untuk seluruh spec cukup; baris log dikenali lewat nama bersuffix, Action, dan tanggal pada atau sesudah T142, bukan posisi teratas.
- Surface disebut satu per satu pada TC-GS-USER-884, 887, 886, 897, dan 885: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. TC-GS-USER-924 hanya memuat Modal Changelog User sesuai Langkah Uji. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Urutan TC di spec: 884, 887, 886, 897, 885, 924. TC-GS-USER-887 dijalankan sebelum TC-GS-USER-886 karena `TAG-USR-0001` harus bebas sebelum dipasang ke `Dewi Lestari Pair {runId}-142` (satu-satunya TAG user bebas di Tabel Pre-setup No. 25). Dua TC yang mencabut akses (885, 924) berada paling akhir (bagian 3 prinsip 5).
- Pembagian TC lintas spec: Expected f TC-GS-USER-897 ("Tidak tercatat di Tab User Log") adalah asersi absence kelas g dan diverifikasi di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role` lewat TC-GS-USER-942 (aksi Reset Authenticator dengan baseline sendiri); spec ini tidak mengasersinya. Absence Product Selector (TC-GS-USER-925) juga ada di spec 147. Klausa Expected f TC-GS-USER-884 dan 885 ("Action `Add Access`/`Remove Access`, bukan `Edit`") serta Expected b TC-GS-USER-924 ("Detail per role tidak ditulis di log User") diasersi di spec ini sebagai jumlah seluruh baris bertanggal pada atau sesudah T142 untuk user seed itu (tepat 1), bukan asersi absence kelas g. Changelog Role & Permission (tempat detail per role) tidak diasersi karena tidak ada di Langkah Uji TC-GS-USER-924.
- Spec melewati sekitar 35 langkah (99 langkah). Alasan: seluruh blok satu kelas (pencatatan log) dengan user seed sendiri per TC sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan tidak dihitung ke batas ukuran (bagian 3 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 8, 12, 16, 19, 22 sampai 27, 30, 33, 36, 39 sampai 44, 47, 50, 53, 56 sampai 60, 63, 66, 69, 72 sampai 77, 81, 85, 88, 91 sampai 97. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama.
- Temuan untuk QA:
  - TC-GS-USER-887: Expected menyebut `TAG-4F7K2XQ9` yang terpasang pada John Doe Pre-setup (No. 18) dan tidak dapat dipasang ke user seed; spec memakai `TAG-USR-0001` pada user seed milik spec.
  - TC-GS-USER-886 memakai simulasi scan TAG (HK7); TC-GS-USER-887 memakai TAG hasil seeding; TC-GS-USER-884, 885, dan 924 hanya memakai UI Popup Edit.
  - TC-GS-USER-897: Precondition tidak menyebut John Doe Enrolled; spec men-seed Authenticator Enrolled (disediakan tim FE/BE). Tanda Enrolled atau Not Enrolled dibaca dari Badge Authenticator di Detail; nama elemen itu mengikuti TC Detail Reset Authenticator.
  - TC-GS-USER-924: Langkah Uji "Remove Access GS Doni Pratama (konfirmasi)" tidak menyebut Edit dan `[Save]`; spec memakai alur Popup Edit yang sama dengan TC Remove Access Global Settings. Expected b memuat penjelasan dalam tanda kurung ("ada di Changelog Role & Permission") yang tidak diasersi.
  - TC-GS-USER-884, 885, 886, 887, 897 memakai nama Pre-setup (Dewi Lestari, John Doe) dan TC-GS-USER-924 memakai Doni Pratama Pre-setup sebagai target tulis; spec memakai padanan seed bersuffix (S-06).
