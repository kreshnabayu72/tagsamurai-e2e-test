---
id: TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log
title: "Pencatatan Create, Edit Position, Edit Photo, Edit Represented By, dan Delete User di Modal Changelog User, Tab Changelog Detail, Tab System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-873
  - TC-GS-USER-874
  - TC-GS-USER-875
  - TC-GS-USER-876
  - TC-GS-USER-877
coverage:
  web: automated
---

# Pencatatan Create, Edit Position, Edit Photo, Edit Represented By, dan Delete User di Modal Changelog User, Tab Changelog Detail, Tab System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Siti Nurhaliza (No. 2) sebagai pelaku dan pemilik Tab System Log; Position `Staff` dan `Supervisor` (No. 22), Division `Finance` (No. 23), dan TAG `TAG-USR-0001` (No. 25, user, aktif, bebas). Data target Pre-setup No. 10 sampai 21 tidak dipakai sebagai target aksi dan tidak diubah (S-06).
- Data Dinamis (suffix `{runId}-138`; menggantikan Dewi Lestari No. 12, John Doe No. 18, Ahmad Fauzi No. 13, Agus Prasetyo No. 21, dan Rudi Hakim Tabel Dinamis No. 2):
  - `Budi Santoso {runId}-138` (First Name `Budi`, Last Name `Santoso {runId}-138`, Email `budisantoso+{runId}-138@qwertysystem.net`): dibuat spec lewat UI pada TC-GS-USER-873 dengan Division `Finance`, Access `Fixed Asset`, Position `Staff`, Temporary Until +30 hari, TAG `TAG-USR-0001`, dan foto `budi-{runId}-138.png`.
  - `Dewi Lestari {runId}-138` (Email `dewilestari+{runId}-138@qwertysystem.net`): di-seed lewat API di hook `before`; Activated, Division `Finance`, Access `Fixed Asset`, Position `Staff` (TC-GS-USER-874).
  - `John Doe {runId}-138` (Email `johndoe+{runId}-138@qwertysystem.net`): di-seed lewat API; Activated, Division `Finance`, Access `Fixed Asset`, dengan foto awal `john-{runId}-138.png` (TC-GS-USER-875).
  - `Ahmad Fauzi {runId}-138` (Email `ahmadfauzi+{runId}-138@qwertysystem.net`): di-seed lewat API; Activated, Division `Finance`, Access `Fixed Asset`; Non-Login User `Agus Prasetyo {runId}-138` di-seed dengan Represented By `Ahmad Fauzi {runId}-138` (TC-GS-USER-876).
  - `Rudi Hakim {runId}-138` (Email `rudihakim+{runId}-138@qwertysystem.net`): di-seed lewat API; Activated, Division `Finance`, Access `Fixed Asset`, dengan 2 foto (satu foto aktif dan satu foto lama di Recycle Bin) (TC-GS-USER-877).
  - Berkas foto uji (fixture belum ada, disediakan tim FE): `budi-{runId}-138.png`, `john-{runId}-138.png`, `john2-{runId}-138.png`, dan dua berkas foto `Rudi Hakim`.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD): seeding user, Non-Login User (dengan Represented By), dan foto lewat API; simulasi scan TAG pada Popup Create (perangkat RFID reader dianggap tersambung dan ID TAG disuntikkan seolah-olah dipindai); memilih berkas pada input unggah foto dari fixture; mengisi date picker Temporary Until dengan tanggal hari ini + 30 hari; membaca waktu server untuk penanda waktu T138.
- Hook `before` membebaskan `TAG-USR-0001` dari sisa run lama (melepas pairing dari user mana pun) sebelum TC-GS-USER-873.
- State global yang diubah: pairing `TAG-USR-0001` (dipakai `Budi Santoso {runId}-138` sampai cleanup). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Budi Santoso {runId}-138` (melepas `TAG-USR-0001`), `Dewi Lestari {runId}-138`, `John Doe {runId}-138`, `Ahmad Fauzi {runId}-138` (bila belum terhapus), `Agus Prasetyo {runId}-138`, dan `Rudi Hakim {runId}-138` (bila belum terhapus), beserta foto di File Manager dan Recycle Bin milik user seed. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan penanda waktu

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Catat penanda waktu T138 (waktu server) sebelum aksi pemicu pertama (langkah 3)

### TC-GS-USER-873: Log Create field Name

3. Klik `[+ User]` di Table Tools
4. Isi First Name `Budi`, Last Name `Santoso {runId}-138`, Division `Finance`, Email `budisantoso+{runId}-138@qwertysystem.net`, centang Access `Fixed Asset`, dan pilih Position `Staff`
5. Centang `Set as Temporary User`, lalu pilih Temporary Until +30 hari
6. Klik `Scan TAG`
7. Scan `TAG-USR-0001`
8. Pilih berkas foto `budi-{runId}-138.png` pada Avatar Popup Create
9. Klik `[Submit]`
10. Tunggu aksi selesai (Popup Create tertutup)
11. Buka Modal Changelog User, klik icon Search, ketik `Budi Santoso {runId}-138`, tekan Enter
12. Verifikasi Modal Changelog User: baris dengan Action `Create`, Name `Budi Santoso {runId}-138`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`, Modified By `Siti N`, bertanggal pada atau sesudah T138
13. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Create` untuk `Budi Santoso {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
14. Verifikasi Modal Changelog User: seluruh baris hasil Search `Budi Santoso {runId}-138` bertanggal pada atau sesudah T138 berjumlah tepat 1 dan Action-nya `Create` (bukan Add Access, Pair TAG, Set Temporary User, atau Edit Photo)
15. Buka Detail `Budi Santoso {runId}-138` > Tab `Changelog`
16. Verifikasi Tab Changelog Detail `Budi Santoso {runId}-138`: baris dengan Action `Create`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`, Modified By `Siti N`, bertanggal pada atau sesudah T138
17. Verifikasi Tab Changelog Detail `Budi Santoso {runId}-138`: tepat 1 baris dengan Action `Create` bertanggal pada atau sesudah T138 (tidak duplikat)
18. Verifikasi Tab Changelog Detail `Budi Santoso {runId}-138`: seluruh baris bertanggal pada atau sesudah T138 berjumlah tepat 1 dan Action-nya `Create` (bukan Add Access, Pair TAG, Set Temporary User, atau Edit Photo)
19. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Budi Santoso {runId}-138`, tekan Enter
20. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Create`, Object `User`, Name `Budi Santoso {runId}-138`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`, bertanggal pada atau sesudah T138
21. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Create` untuk `Budi Santoso {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
22. Buka Global Settings > Activity Log, klik icon Search, ketik `Budi Santoso {runId}-138`, tekan Enter
23. Verifikasi Activity Log: baris dengan Action `Create`, Object `User`, Name `Budi Santoso {runId}-138`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`, Modified By `Siti N`, bertanggal pada atau sesudah T138
24. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Create` untuk `Budi Santoso {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)

### TC-GS-USER-874: Log Edit field Position

25. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
26. Klik (⋯) baris `Dewi Lestari {runId}-138` → `Edit`
27. Ubah Position `Staff` menjadi `Supervisor`
28. Klik `[Save]`
29. Tunggu aksi selesai (Popup Edit tertutup)
30. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
31. Verifikasi Modal Changelog User: baris dengan Action `Edit`, Name `Dewi Lestari {runId}-138`, Field `Position`, Old Value `Staff`, New Value `Supervisor`, Modified By `Siti N`, bertanggal pada atau sesudah T138
32. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Dewi Lestari {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
33. Buka Detail `Dewi Lestari {runId}-138` > Tab `Changelog`
34. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-138`: baris dengan Action `Edit`, Field `Position`, Old Value `Staff`, New Value `Supervisor`, Modified By `Siti N`, bertanggal pada atau sesudah T138
35. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-138`: tepat 1 baris dengan Action `Edit` bertanggal pada atau sesudah T138 (tidak duplikat)
36. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
37. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Edit`, Object `User`, Name `Dewi Lestari {runId}-138`, Field `Position`, Old Value `Staff`, New Value `Supervisor`, bertanggal pada atau sesudah T138
38. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Dewi Lestari {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
39. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
40. Verifikasi Activity Log: baris dengan Action `Edit`, Object `User`, Name `Dewi Lestari {runId}-138`, Field `Position`, Old Value `Staff`, New Value `Supervisor`, Modified By `Siti N`, bertanggal pada atau sesudah T138
41. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Dewi Lestari {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)

### TC-GS-USER-875: Log Edit field Photo

42. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
43. Klik (⋯) baris `John Doe {runId}-138` → `Edit`
44. Pilih berkas foto `john2-{runId}-138.png` untuk mengganti foto pada Avatar Popup Edit
45. Klik `[Save]`
46. Tunggu aksi selesai (Popup Edit tertutup)
47. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
48. Verifikasi Modal Changelog User: baris dengan Action `Edit`, Name `John Doe {runId}-138`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
49. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `John Doe {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
50. Verifikasi Modal Changelog User: Old Value dan New Value baris `Edit` Field `Photo` untuk `John Doe {runId}-138` keduanya `—`
51. Buka Detail `John Doe {runId}-138` > Tab `Changelog`
52. Verifikasi Tab Changelog Detail `John Doe {runId}-138`: baris dengan Action `Edit`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
53. Verifikasi Tab Changelog Detail `John Doe {runId}-138`: tepat 1 baris dengan Action `Edit` bertanggal pada atau sesudah T138 (tidak duplikat)
54. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
55. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Edit`, Object `User`, Name `John Doe {runId}-138`, Field `Photo`, Old Value `—`, New Value `—`, bertanggal pada atau sesudah T138
56. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `John Doe {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
57. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
58. Verifikasi Activity Log: baris dengan Action `Edit`, Object `User`, Name `John Doe {runId}-138`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
59. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `John Doe {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)

### TC-GS-USER-876: Log Edit field Represented By

60. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Ahmad Fauzi {runId}-138`, tekan Enter
61. Klik (⋯) baris `Ahmad Fauzi {runId}-138` lalu `Delete`
62. Klik `[Delete]`
63. Tunggu aksi selesai (baris `Ahmad Fauzi {runId}-138` hilang dari User List)
64. Buka Modal Changelog User, klik icon Search, ketik `Agus Prasetyo {runId}-138`, tekan Enter
65. Verifikasi Modal Changelog User: baris dengan Action `Edit`, Name `Agus Prasetyo {runId}-138`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
66. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Agus Prasetyo {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
67. Buka Detail `Agus Prasetyo {runId}-138` > Tab `Changelog` (dari sub-tab Non-Login User)
68. Verifikasi Tab Changelog Detail `Agus Prasetyo {runId}-138`: baris dengan Action `Edit`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
69. Verifikasi Tab Changelog Detail `Agus Prasetyo {runId}-138`: tepat 1 baris dengan Action `Edit` bertanggal pada atau sesudah T138 (tidak duplikat)
70. Verifikasi Detail `Agus Prasetyo {runId}-138` yang dibuka dari sub-tab Non-Login User: Name pada baris log adalah Non-Login User `Agus Prasetyo {runId}-138`
71. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Agus Prasetyo {runId}-138`, tekan Enter
72. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Edit`, Object `User`, Name `Agus Prasetyo {runId}-138`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`, bertanggal pada atau sesudah T138
73. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Agus Prasetyo {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
74. Buka Global Settings > Activity Log, klik icon Search, ketik `Agus Prasetyo {runId}-138`, tekan Enter
75. Verifikasi Activity Log: baris dengan Action `Edit`, Object `User`, Name `Agus Prasetyo {runId}-138`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
76. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Agus Prasetyo {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)

### TC-GS-USER-877: Log Delete field Name

77. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
78. Klik (⋯) baris `Rudi Hakim {runId}-138` lalu `Delete`
79. Klik `[Delete]`
80. Tunggu aksi selesai (baris `Rudi Hakim {runId}-138` hilang dari User List)
81. Buka Modal Changelog User, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
82. Verifikasi Modal Changelog User: baris dengan Action `Delete`, Name `Rudi Hakim {runId}-138`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
83. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Delete` untuk `Rudi Hakim {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
84. Verifikasi Modal Changelog User: seluruh baris hasil Search `Rudi Hakim {runId}-138` bertanggal pada atau sesudah T138 berjumlah tepat 1 (baris `Delete`; jumlah foto tidak dicatat dan tidak ada baris per file)
85. Buka Detail `Rudi Hakim {runId}-138` > Tab `Changelog`
86. Verifikasi Tab Changelog Detail `Rudi Hakim {runId}-138`: baris dengan Action `Delete`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
87. Verifikasi Tab Changelog Detail `Rudi Hakim {runId}-138`: tepat 1 baris dengan Action `Delete` bertanggal pada atau sesudah T138 (tidak duplikat)
88. Verifikasi Tab Changelog Detail `Rudi Hakim {runId}-138`: seluruh baris bertanggal pada atau sesudah T138 berjumlah tepat 1 (baris `Delete`; jumlah foto tidak dicatat dan tidak ada baris per file)
89. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
90. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Delete`, Object `User`, Name `Rudi Hakim {runId}-138`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`, bertanggal pada atau sesudah T138
91. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Delete` untuk `Rudi Hakim {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)
92. Buka Global Settings > Activity Log, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
93. Verifikasi Activity Log: baris dengan Action `Delete`, Object `User`, Name `Rudi Hakim {runId}-138`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T138
94. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Delete` untuk `Rudi Hakim {runId}-138` bertanggal pada atau sesudah T138 (tidak duplikat)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penanda waktu T138 dicatat di langkah 2, sebelum aksi pemicu pertama yang diasersi (langkah 3, S-12). Tiap TC memakai user seed sendiri dengan nama bersuffix `{runId}-138`, sehingga satu penanda untuk seluruh spec cukup; baris log dikenali lewat Search nama bersuffix dan tanggal pada atau sesudah T138, bukan posisi teratas.
- Surface disebut satu per satu pada tiap TC: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai `Verifikasi` jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Pembagian TC lintas spec: TC-GS-USER-873 butir f ("Hanya 1 baris `Create`, tanpa baris tambahan") diasersi di spec ini sebagai jumlah baris (tepat 1, Action `Create`) pada Modal Changelog User dan Tab Changelog Detail dengan baseline T138; asersi absence kelas g untuk Pair TAG dari Popup Create (TC-GS-USER-923) diverifikasi di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`.
- Urutan TC di spec: 873, 874, 875, 876, 877 sesuai urutan TC; dua TC yang menghapus user (876, 877) berada paling akhir (bagian 3 prinsip 5), dan tiap TC memakai user seed berbeda.
- Spec melewati sekitar 35 langkah (94 langkah). Alasan: seluruh blok satu kelas (pencatatan log) dan satu dataset seed milik spec, tiap TC berdiri sendiri pada user sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan, menurut bagian 3 konvensi, tidak dihitung ke batas ukuran.
- Langkah penghubung (bukan dari TC sumber atau aksi tanpa `Verifikasi`): 1 sampai 11, 15, 19, 22, 25 sampai 30, 33, 36, 39, 42 sampai 47, 51, 54, 57, 60 sampai 64, 67, 71, 74, 77 sampai 81, 85, 89, 92. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama.
- Temuan untuk QA:
  - TC-GS-USER-873 Langkah Uji 1 menyebut "TAG", "Temporary", dan "Photo" tanpa nilai: spec memakai `TAG-USR-0001` (satu-satunya TAG user bebas di Tabel Pre-setup No. 25), Temporary Until +30 hari, dan foto `budi-{runId}-138.png`. Langkah scan TAG pada Popup Create membutuhkan simulasi scan (HK7).
  - TC-GS-USER-873 sampai 877 memakai nama Pre-setup (Dewi Lestari, John Doe, Ahmad Fauzi, Agus Prasetyo) dan Tabel Dinamis (Rudi Hakim dibuat di TC-GS-USER-138) sebagai target tulis atau hapus; spec memakai padanan seed bersuffix agar data bersama tidak berubah (S-06).
  - TC-GS-USER-874 tidak menyebut arah `Staff` dan `Supervisor` terhadap dropdown Position selain nilai Pre-setup No. 22; spec memilih nilai itu apa adanya.
  - TC-GS-USER-875: Expected c sampai f menyebut Old Value dan New Value `—` tanpa menyebut berkas foto yang diganti; Langkah Uji 1 tidak menyebut berkas pengganti, sehingga spec memakai `john2-{runId}-138.png`.
  - TC-GS-USER-876: Langkah Uji 1 ("Delete user Ahmad Fauzi") menghasilkan baris `Edit` Represented By pada Agus Prasetyo tanpa menjelaskan mekanismenya; Detail Non-Login User tidak disebut lokasinya (spec membukanya dari sub-tab Non-Login User). Expected f ("Name = Non-Login User Agus Prasetyo") tidak menyebut cara teramati selain kolom Name.
  - TC-GS-USER-877: "Rudi Hakim yang punya 2 foto" tidak merinci arti 2 foto (aktif dan lama, atau dua foto aktif); spec men-seed satu foto aktif dan satu foto lama. Langkah Uji 3 membuka Detail user yang sudah dihapus tanpa menyebut jalur aksesnya (baris User List sudah hilang); spec mengikuti TC apa adanya.
  - Kolom per surface mengikuti Expected tiap TC: Tab Changelog Detail tanpa kolom Name dan Object, Tab System Log tanpa kolom Modified By.
