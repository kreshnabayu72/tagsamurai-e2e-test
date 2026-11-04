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
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD): seeding user, Non-Login User (dengan Represented By), dan foto lewat API; simulasi scan TAG pada Popup Create (perangkat RFID reader dianggap tersambung dan ID TAG disuntikkan seolah-olah dipindai); memilih berkas pada input unggah foto dari fixture; mengisi date picker Temporary Until dengan tanggal hari ini + 30 hari.
- Hook `before` membebaskan `TAG-USR-0001` dari sisa run lama (melepas pairing dari user mana pun) sebelum TC-GS-USER-873.
- State global yang diubah: pairing `TAG-USR-0001` (dipakai `Budi Santoso {runId}-138` sampai cleanup). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Budi Santoso {runId}-138` (melepas `TAG-USR-0001`), `Dewi Lestari {runId}-138`, `John Doe {runId}-138`, `Ahmad Fauzi {runId}-138` (bila belum terhapus), `Agus Prasetyo {runId}-138`, dan `Rudi Hakim {runId}-138` (bila belum terhapus), beserta foto di File Manager dan Recycle Bin milik user seed. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-874: Log Edit field Position

2. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
3. Klik (⋯) baris `Dewi Lestari {runId}-138` → `Edit`
4. Ubah Position `Staff` menjadi `Supervisor`
5. Klik `[Save]`
6. Tunggu aksi selesai (Popup Edit tertutup)
7. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
8. Verifikasi Modal Changelog User: baris dengan Action `Edit`, Name `Dewi Lestari {runId}-138`, Field `Position`, Old Value `Staff`, New Value `Supervisor`, Modified By `Siti N`
9. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Dewi Lestari {runId}-138` (tidak duplikat)
10. Buka Detail `Dewi Lestari {runId}-138` > Tab `Changelog`
11. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-138`: baris dengan Action `Edit`, Field `Position`, Old Value `Staff`, New Value `Supervisor`, Modified By `Siti N`
12. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-138`: tepat 1 baris dengan Action `Edit` (tidak duplikat)
13. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
14. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Edit`, Object `User`, Name `Dewi Lestari {runId}-138`, Field `Position`, Old Value `Staff`, New Value `Supervisor`
15. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Dewi Lestari {runId}-138` (tidak duplikat)
16. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari {runId}-138`, tekan Enter
17. Verifikasi Activity Log: baris dengan Action `Edit`, Object `User`, Name `Dewi Lestari {runId}-138`, Field `Position`, Old Value `Staff`, New Value `Supervisor`, Modified By `Siti N`
18. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Dewi Lestari {runId}-138` (tidak duplikat)

### TC-GS-USER-875: Log Edit field Photo

19. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
20. Klik (⋯) baris `John Doe {runId}-138` → `Edit`
21. Pilih berkas foto `john2-{runId}-138.png` untuk mengganti foto pada Avatar Popup Edit
22. Klik `[Save]`
23. Tunggu aksi selesai (Popup Edit tertutup)
24. Buka Modal Changelog User, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
25. Verifikasi Modal Changelog User: baris dengan Action `Edit`, Name `John Doe {runId}-138`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`
26. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `John Doe {runId}-138` (tidak duplikat)
27. Verifikasi Modal Changelog User: Old Value dan New Value baris `Edit` Field `Photo` untuk `John Doe {runId}-138` keduanya `—`
28. Buka Detail `John Doe {runId}-138` > Tab `Changelog`
29. Verifikasi Tab Changelog Detail `John Doe {runId}-138`: baris dengan Action `Edit`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`
30. Verifikasi Tab Changelog Detail `John Doe {runId}-138`: tepat 1 baris dengan Action `Edit` (tidak duplikat)
31. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
32. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Edit`, Object `User`, Name `John Doe {runId}-138`, Field `Photo`, Old Value `—`, New Value `—`
33. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `John Doe {runId}-138` (tidak duplikat)
34. Buka Global Settings > Activity Log, klik icon Search, ketik `John Doe {runId}-138`, tekan Enter
35. Verifikasi Activity Log: baris dengan Action `Edit`, Object `User`, Name `John Doe {runId}-138`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`
36. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `John Doe {runId}-138` (tidak duplikat)

### TC-GS-USER-876: Log Edit field Represented By

37. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Ahmad Fauzi {runId}-138`, tekan Enter
38. Klik (⋯) baris `Ahmad Fauzi {runId}-138` lalu `Delete`
39. Klik `[Delete]`
40. Tunggu aksi selesai (baris `Ahmad Fauzi {runId}-138` hilang dari User List)
41. Buka Modal Changelog User, klik icon Search, ketik `Agus Prasetyo {runId}-138`, tekan Enter
42. Verifikasi Modal Changelog User: baris dengan Action `Edit`, Name `Agus Prasetyo {runId}-138`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`, Modified By `Siti N`
43. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Agus Prasetyo {runId}-138` (tidak duplikat)
44. Buka Detail `Agus Prasetyo {runId}-138` > Tab `Changelog` (dari sub-tab Non-Login User)
45. Verifikasi Tab Changelog Detail `Agus Prasetyo {runId}-138`: baris dengan Action `Edit`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`, Modified By `Siti N`
46. Verifikasi Tab Changelog Detail `Agus Prasetyo {runId}-138`: tepat 1 baris dengan Action `Edit` (tidak duplikat)
47. Verifikasi Detail `Agus Prasetyo {runId}-138` yang dibuka dari sub-tab Non-Login User: Name pada baris log adalah Non-Login User `Agus Prasetyo {runId}-138`
48. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Agus Prasetyo {runId}-138`, tekan Enter
49. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Edit`, Object `User`, Name `Agus Prasetyo {runId}-138`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`
50. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Agus Prasetyo {runId}-138` (tidak duplikat)
51. Buka Global Settings > Activity Log, klik icon Search, ketik `Agus Prasetyo {runId}-138`, tekan Enter
52. Verifikasi Activity Log: baris dengan Action `Edit`, Object `User`, Name `Agus Prasetyo {runId}-138`, Field `Represented By`, Old Value `Ahmad Fauzi {runId}-138`, New Value `—`, Modified By `Siti N`
53. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Edit` untuk `Agus Prasetyo {runId}-138` (tidak duplikat)

### TC-GS-USER-877: Log Delete field Name

54. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
55. Klik (⋯) baris `Rudi Hakim {runId}-138` lalu `Delete`
56. Klik `[Delete]`
57. Tunggu aksi selesai (baris `Rudi Hakim {runId}-138` hilang dari User List)
58. Buka Modal Changelog User, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
59. Verifikasi Modal Changelog User: baris dengan Action `Delete`, Name `Rudi Hakim {runId}-138`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`, Modified By `Siti N`
60. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Delete` untuk `Rudi Hakim {runId}-138` (tidak duplikat)
61. Verifikasi Modal Changelog User: baris dengan Action `Delete` pada hasil Search `Rudi Hakim {runId}-138` berjumlah tepat 1 (jumlah foto tidak dicatat dan tidak ada baris `Delete` per file)
62. Buka Detail `Rudi Hakim {runId}-138` > Tab `Changelog`
63. Verifikasi Tab Changelog Detail `Rudi Hakim {runId}-138`: baris dengan Action `Delete`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`, Modified By `Siti N`
64. Verifikasi Tab Changelog Detail `Rudi Hakim {runId}-138`: tepat 1 baris dengan Action `Delete` (tidak duplikat)
65. Verifikasi Tab Changelog Detail `Rudi Hakim {runId}-138`: baris dengan Action `Delete` berjumlah tepat 1 (jumlah foto tidak dicatat dan tidak ada baris `Delete` per file)
66. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
67. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Delete`, Object `User`, Name `Rudi Hakim {runId}-138`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`
68. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Delete` untuk `Rudi Hakim {runId}-138` (tidak duplikat)
69. Buka Global Settings > Activity Log, klik icon Search, ketik `Rudi Hakim {runId}-138`, tekan Enter
70. Verifikasi Activity Log: baris dengan Action `Delete`, Object `User`, Name `Rudi Hakim {runId}-138`, Field `Name`, Old Value `Rudi Hakim {runId}-138`, New Value `—`, Modified By `Siti N`
71. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Delete` untuk `Rudi Hakim {runId}-138` (tidak duplikat)

### TC-GS-USER-873: Log Create field Name

72. Klik menu User di sidebar Global Settings, lalu klik `[+ User]` di Table Tools
73. Isi First Name `Budi`, Last Name `Santoso {runId}-138`, Division `Finance`, Email `budisantoso+{runId}-138@qwertysystem.net`, centang Access `Fixed Asset`, dan pilih Position `Staff`
74. Centang `Set as Temporary User`, lalu pilih Temporary Until +30 hari
75. Klik `Scan TAG`
76. Scan `TAG-USR-0001`
77. Pilih berkas foto `budi-{runId}-138.png` pada Avatar Popup Create
78. Klik `[Submit]`
79. Tunggu aksi selesai (Popup Create tertutup)
80. Buka Modal Changelog User, klik icon Search, ketik `Budi Santoso {runId}-138`, tekan Enter
81. Verifikasi Modal Changelog User: baris dengan Action `Create`, Name `Budi Santoso {runId}-138`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`, Modified By `Siti N`
82. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Create` untuk `Budi Santoso {runId}-138` (tidak duplikat)
83. Verifikasi Modal Changelog User: seluruh baris hasil Search `Budi Santoso {runId}-138` berjumlah tepat 1 dan Action-nya `Create` (bukan Add Access, Pair TAG, Set Temporary User, atau Edit Photo)
84. Buka Detail `Budi Santoso {runId}-138` > Tab `Changelog`
85. Verifikasi Tab Changelog Detail `Budi Santoso {runId}-138`: baris dengan Action `Create`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`, Modified By `Siti N`
86. Verifikasi Tab Changelog Detail `Budi Santoso {runId}-138`: tepat 1 baris dengan Action `Create` (tidak duplikat)
87. Verifikasi Tab Changelog Detail `Budi Santoso {runId}-138`: seluruh baris berjumlah tepat 1 dan Action-nya `Create` (bukan Add Access, Pair TAG, Set Temporary User, atau Edit Photo)
88. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Budi Santoso {runId}-138`, tekan Enter
89. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Create`, Object `User`, Name `Budi Santoso {runId}-138`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`
90. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Create` untuk `Budi Santoso {runId}-138` (tidak duplikat)
91. Buka Global Settings > Activity Log, klik icon Search, ketik `Budi Santoso {runId}-138`, tekan Enter
92. Verifikasi Activity Log: baris dengan Action `Create`, Object `User`, Name `Budi Santoso {runId}-138`, Field `Name`, Old Value `—`, New Value `Budi Santoso {runId}-138`, Modified By `Siti N`
93. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Create` untuk `Budi Santoso {runId}-138` (tidak duplikat)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Baris log dikenali lewat Search nama bersuffix `{runId}-138` yang unik per run (baseline nol), Action, dan Field, bukan posisi teratas dan bukan penanda waktu (S-12). Tiap TC memakai user seed sendiri dengan nama bersuffix berbeda. Entri seed (Create dari seeding) tidak dihitung karena asersi jumlah dibatasi pada Action yang dipicu aksi spec ini.
- Surface disebut satu per satu pada tiap TC: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai `Verifikasi` jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Pembagian TC lintas spec: TC-GS-USER-873 butir f ("Hanya 1 baris `Create`, tanpa baris tambahan") diasersi di spec ini sebagai jumlah baris (tepat 1, Action `Create`) pada Modal Changelog User dan Tab Changelog Detail dengan nama bersuffix unik per run (baseline nol, S-12); asersi absence kelas g untuk Pair TAG dari Popup Create (TC-GS-USER-923) diverifikasi di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`.
- Urutan TC di spec: 874, 875, 876, 877, 873. TC-GS-USER-873 (Create dengan simulator scan `TAG-USR-0001`, langkah 75 dan 76) dipindah ke akhir spec supaya kegagalan simulator tidak menutupi blok lain (konvensi bagian 3, pemisah nyata hardware berisiko); dua TC yang menghapus user (876, 877) tetap mendahuluinya dan tiap TC memakai user seed berbeda, sehingga blok 873 tidak bergantung pada hasil blok lain. Pemisahan blok simulator scan (konvensi bagian 3, pemisah nyata hardware berisiko): objek uji TC-GS-USER-873 adalah pencatatan log Create, bukan perangkat scan; scan hanya membentuk user ber-TAG pada Popup Create. Langkah 72 memulihkan layar User List.
- Spec melewati sekitar 35 langkah (93 langkah). Alasan: seluruh blok satu kelas (pencatatan log) dan satu dataset seed milik spec, tiap TC berdiri sendiri pada user sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan, menurut bagian 3 konvensi, tidak dihitung ke batas ukuran.
- Langkah penghubung (bukan dari TC sumber atau aksi tanpa `Verifikasi`): 1 sampai 7, 10, 13, 16, 19 sampai 24, 28, 31, 34, 37 sampai 41, 44, 48, 51, 54 sampai 58, 62, 66, 69, 72 sampai 80, 84, 88, 91. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama.
- Temuan untuk QA:
  - TC-GS-USER-873 Langkah Uji 1 menyebut "TAG", "Temporary", dan "Photo" tanpa nilai: spec memakai `TAG-USR-0001` (satu-satunya TAG user bebas di Tabel Pre-setup No. 25), Temporary Until +30 hari, dan foto `budi-{runId}-138.png`. Langkah scan TAG pada Popup Create membutuhkan simulasi scan (HK7).
  - TC-GS-USER-873 sampai 877 memakai nama Pre-setup (Dewi Lestari, John Doe, Ahmad Fauzi, Agus Prasetyo) dan Tabel Dinamis (Rudi Hakim dibuat di TC-GS-USER-138) sebagai target tulis atau hapus; spec memakai padanan seed bersuffix agar data bersama tidak berubah (S-06).
  - TC-GS-USER-874 tidak menyebut arah `Staff` dan `Supervisor` terhadap dropdown Position selain nilai Pre-setup No. 22; spec memilih nilai itu apa adanya.
  - TC-GS-USER-875: Expected c sampai f menyebut Old Value dan New Value `—` tanpa menyebut berkas foto yang diganti; Langkah Uji 1 tidak menyebut berkas pengganti, sehingga spec memakai `john2-{runId}-138.png`.
  - TC-GS-USER-876: Langkah Uji 1 ("Delete user Ahmad Fauzi") menghasilkan baris `Edit` Represented By pada Agus Prasetyo tanpa menjelaskan mekanismenya; Detail Non-Login User tidak disebut lokasinya (spec membukanya dari sub-tab Non-Login User). Expected f ("Name = Non-Login User Agus Prasetyo") tidak menyebut cara teramati selain kolom Name.
  - TC-GS-USER-877: "Rudi Hakim yang punya 2 foto" tidak merinci arti 2 foto (aktif dan lama, atau dua foto aktif); spec men-seed satu foto aktif dan satu foto lama. Langkah Uji 3 membuka Detail user yang sudah dihapus tanpa menyebut jalur aksesnya (baris User List sudah hilang); spec mengikuti TC apa adanya.
  - Kolom per surface mengikuti Expected tiap TC: Tab Changelog Detail tanpa kolom Name dan Object, Tab System Log tanpa kolom Modified By.
