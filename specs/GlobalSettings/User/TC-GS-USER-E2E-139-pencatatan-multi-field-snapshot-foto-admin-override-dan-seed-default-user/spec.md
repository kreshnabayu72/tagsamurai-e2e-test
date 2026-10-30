---
id: TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user
title: "Pencatatan Changelog User: Seed Default User, Edit Multi-Field Menjadi Dua Baris, Edit Position dengan Remove Access, Inline Edit Custom Field, Set Temporary User pada Perubahan Temporary Until, Snapshot Beku dan Rename Position, Hapus Foto dari Avatar dan File Manager, serta Delete User dengan TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-909
  - TC-GS-USER-910
  - TC-GS-USER-911
  - TC-GS-USER-916
  - TC-GS-USER-917
  - TC-GS-USER-918
  - TC-GS-USER-921
  - TC-GS-USER-922
  - TC-GS-USER-1044
  - TC-GS-USER-1076
coverage:
  web: automated
---

# Pencatatan Changelog User: Seed Default User, Edit Multi-Field Menjadi Dua Baris, Edit Position dengan Remove Access, Inline Edit Custom Field, Set Temporary User pada Perubahan Temporary Until, Snapshot Beku dan Rename Position, Hapus Foto dari Avatar dan File Manager, serta Delete User dengan TAG

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Default User Hendra Gunawan (No. 1) untuk TC-GS-USER-1044; Siti Nurhaliza (No. 2) sebagai pelaku; Position `Staff`, `HR Business Partner`, dan `Finance Manager` (No. 22); Division `Finance` (No. 23); Custom Field Blood Type opsi `A` dan `O` (No. 24); TAG `TAG-USR-0001` (No. 25). Data target Pre-setup No. 10 sampai 21 tidak dipakai sebagai target aksi dan tidak diubah (S-06).
- Default User `Hendra Gunawan` belum pernah diedit saat TC-GS-USER-1044 berjalan (Precondition TC): spec ini hanya membaca Tab Changelog Hendra Gunawan, tidak mengedit Default User, dan dijalankan sebelum spec yang mengedit Default User (`suite.md`, suite serial). Entitas dalam keadaan seed registrasi customer disediakan tim FE.
- Data Dinamis (suffix `{runId}-139`; semua user Activated, Division `Finance`; menggantikan Dewi Lestari No. 12 dan John Doe No. 18; di-seed lewat API di hook `before` sebelum penanda waktu T139):
  - `Dewi Lestari {runId}-139` (First Name `Dewi`, Last Name `Lestari {runId}-139`, Email `dewilestari+{runId}-139@qwertysystem.net`), Access `Fixed Asset`; menjadi `Dewiana Putri {runId}-139` setelah TC-GS-USER-909.
  - `Dewi Lestari Akses {runId}-139` (Email `dewilestariakses+{runId}-139@qwertysystem.net`), Position `Staff`, Access `Fixed Asset` dan `Global Settings` (TC-GS-USER-910).
  - `Dewi Lestari Blood {runId}-139` (Email `dewilestariblood+{runId}-139@qwertysystem.net`), Access `Fixed Asset`, Blood Type `A` (TC-GS-USER-916).
  - `Dewi Lestari Temp {runId}-139` (Email `dewilestaritemp+{runId}-139@qwertysystem.net`), Access `Fixed Asset`, Temporary User aktif dengan Temporary Until hari seeding + 30 hari (TC-GS-USER-1076). `{tglAwal}` = nilai Temporary Until awal yang dibaca di Popup Edit; `{tglBaru}` = hari uji + 45 hari; keduanya dalam Date Format General Settings client.
  - `Dewi Lestari Posisi {runId}-139` (Email `dewilestariposisi+{runId}-139@qwertysystem.net`), Access `Fixed Asset`, Position `Staff` (TC-GS-USER-921 dan 922); Position `Supervisor {runId}-139` di-seed lewat API (menggantikan Position `Supervisor` Pre-setup yang di-rename pada TC-GS-USER-922).
  - `John Doe Foto {runId}-139` (Email `johndoefoto+{runId}-139@qwertysystem.net`), Access `Fixed Asset`, foto aktif `john-foto-{runId}-139.png` (TC-GS-USER-917).
  - `John Doe Admin {runId}-139` (Email `johndoeadmin+{runId}-139@qwertysystem.net`), Access `Fixed Asset`, foto aktif `john-admin-{runId}-139.png` (TC-GS-USER-918).
  - `John Doe Tag {runId}-139` (Email `johndoetag+{runId}-139@qwertysystem.net`), Access `Fixed Asset`, TAG `TAG-USR-0001` terpasang lewat seeding (TC-GS-USER-911).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD): seeding user, Position, foto, Temporary Until, dan pairing TAG lewat API (pairing diseed langsung, tanpa scan); memilih nilai dropdown Custom Field inline; membuka File Manager sebagai admin dan menghapus foto profil aktif; membaca waktu server untuk penanda waktu T139. Berkas foto uji (fixture belum ada): `john-foto-{runId}-139.png`, `john-admin-{runId}-139.png`.
- Hook `before` membebaskan `TAG-USR-0001` dari sisa run lama sebelum seeding `John Doe Tag {runId}-139`.
- State global yang diubah: pairing `TAG-USR-0001` (dilepas saat `John Doe Tag {runId}-139` dihapus pada TC-GS-USER-911); nama Position seed. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketujuh user seed (nama awal dan `Dewiana Putri {runId}-139`), Position `Supervisor {runId}-139` dan `Team Supervisor {runId}-139`, serta foto milik user seed di File Manager dan Recycle Bin. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### TC-GS-USER-1044: Tab Changelog Default User seed, baris paling awal Create oleh System

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
3. Klik Name `Hendra Gunawan` di User List
4. Klik Tab `Changelog`
5. Urutkan Oldest First
6. Verifikasi baris paling awal (Oldest First): Action `Create`, Name `Hendra Gunawan`, Field `Name`, Old Value `—`, New Value `Hendra Gunawan`, Modified By `System`

### TC-GS-USER-909: Edit First Name dan Last Name sekaligus menghasilkan 2 baris log

7. Klik menu User di sidebar Global Settings
8. Catat penanda waktu T139 (waktu server) sebelum aksi pemicu pertama (klik `[Save]` pada TC-GS-USER-909)
9. Klik icon Search, ketik `Dewi Lestari {runId}-139`, tekan Enter
10. Klik (⋯) baris `Dewi Lestari {runId}-139` → `Edit`
11. Ubah First Name `Dewi` menjadi `Dewiana`
12. Ubah Last Name `Lestari {runId}-139` menjadi `Putri {runId}-139`
13. Klik `[Save]`
14. Tunggu aksi selesai (Popup Edit tertutup dan baris `Dewiana Putri {runId}-139` tampil di User List)
15. Buka Detail `Dewiana Putri {runId}-139` > Tab `Changelog`
16. Verifikasi Tab Changelog Detail `Dewiana Putri {runId}-139`: baris dengan Action `Edit`, Field `First Name`, Old Value `Dewi`, New Value `Dewiana`, bertanggal pada atau sesudah T139
17. Verifikasi Tab Changelog Detail `Dewiana Putri {runId}-139`: baris dengan Action `Edit`, Field `Last Name`, Old Value `Lestari {runId}-139`, New Value `Putri {runId}-139`, bertanggal pada atau sesudah T139
18. Verifikasi Tab Changelog Detail `Dewiana Putri {runId}-139`: seluruh baris bertanggal pada atau sesudah T139 berjumlah tepat 2 (hanya Field `First Name` dan `Last Name`; tidak ada baris untuk field yang tidak berubah)

### TC-GS-USER-910: Edit Position dan Remove Access Fixed Asset menghasilkan baris Edit dan Remove Access terpisah

19. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Akses {runId}-139`, tekan Enter
20. Klik (⋯) baris `Dewi Lestari Akses {runId}-139` → `Edit`
21. Ubah Position `Staff` menjadi `HR Business Partner`
22. Uncheck Access `Fixed Asset`
23. Klik `[Save]`
24. Tunggu aksi selesai (Popup Edit tertutup)
25. Buka Detail `Dewi Lestari Akses {runId}-139` > Tab `Changelog`
26. Verifikasi Tab Changelog Detail `Dewi Lestari Akses {runId}-139`: tepat 1 baris dengan Action `Edit` dan Field `Position` bertanggal pada atau sesudah T139
27. Verifikasi Tab Changelog Detail `Dewi Lestari Akses {runId}-139`: tepat 1 baris dengan Action `Remove Access`, Field `App Access`, Old Value `Fixed Asset`, New Value `—`, bertanggal pada atau sesudah T139
28. Verifikasi Tab Changelog Detail `Dewi Lestari Akses {runId}-139`: seluruh baris bertanggal pada atau sesudah T139 berjumlah tepat 2 (tidak ada baris lain)

### TC-GS-USER-916: Inline edit Custom Field Blood Type tercatat sama dengan edit via Popup

29. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Blood {runId}-139`, tekan Enter
30. Klik Name `Dewi Lestari Blood {runId}-139` di User List
31. Hover baris Blood Type, klik icon Edit2Line
32. Pilih nilai Blood Type `O`, klik `[✓ Save]`
33. Tunggu aksi selesai (baris Blood Type kembali Display `Blood Type: O`)
34. Klik Tab `Changelog`
35. Verifikasi Tab Changelog Detail `Dewi Lestari Blood {runId}-139`: baris dengan Action `Edit`, Field `Blood Type`, Old Value `A`, New Value `O`, Modified By `Siti N`, bertanggal pada atau sesudah T139
36. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Blood {runId}-139`, tekan Enter
37. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Edit`, Object `User`, Name `Dewi Lestari Blood {runId}-139`, Field `Blood Type`, Old Value `A`, New Value `O`, bertanggal pada atau sesudah T139
38. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Blood {runId}-139`, tekan Enter
39. Verifikasi Activity Log: baris dengan Action `Edit`, Object `User`, Name `Dewi Lestari Blood {runId}-139`, Field `Blood Type`, Old Value `A`, New Value `O`, Modified By `Siti N`, bertanggal pada atau sesudah T139

### TC-GS-USER-1076: Edit Temporary Until pada user Temporary menulis Set Temporary User

40. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Temp {runId}-139`, tekan Enter
41. Klik (⋯) baris `Dewi Lestari Temp {runId}-139` → `Edit`
42. Catat Temporary Until awal (+30 hari) sebagai `{tglAwal}`
43. Ubah Temporary Until menjadi hari ini + 45 hari (`{tglBaru}`), `Set as Temporary User` tetap tercentang
44. Klik `[Save]`
45. Tunggu aksi selesai (Popup Edit tertutup)
46. Buka Detail `Dewi Lestari Temp {runId}-139` > Tab `Changelog`
47. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-139`: baris dengan Action `Set Temporary User`, Field `Temporary Until`, Old Value `{tglAwal}`, New Value `{tglBaru}`, Modified By `Siti N`, bertanggal pada atau sesudah T139
48. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-139`: tepat 1 baris dengan Action `Set Temporary User` bertanggal pada atau sesudah T139 (tidak duplikat)
49. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-139`: seluruh baris bertanggal pada atau sesudah T139 berjumlah tepat 1, sehingga tidak ada baris `Edit` dengan Field `Temporary Until`
50. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-139`: seluruh baris bertanggal pada atau sesudah T139 berjumlah tepat 1, sehingga tidak ada baris `Remove Temporary User`
51. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Temp {runId}-139`, tekan Enter
52. Verifikasi Modal Changelog User: baris dengan Action `Set Temporary User`, Name `Dewi Lestari Temp {runId}-139`, Field `Temporary Until`, Old Value `{tglAwal}`, New Value `{tglBaru}`, Modified By `Siti N`, bertanggal pada atau sesudah T139
53. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Set Temporary User` untuk `Dewi Lestari Temp {runId}-139` bertanggal pada atau sesudah T139 (tidak duplikat)
54. Verifikasi Modal Changelog User: seluruh baris hasil Search `Dewi Lestari Temp {runId}-139` bertanggal pada atau sesudah T139 berjumlah tepat 1, sehingga tidak ada baris `Edit` dengan Field `Temporary Until`
55. Verifikasi Modal Changelog User: seluruh baris hasil Search `Dewi Lestari Temp {runId}-139` bertanggal pada atau sesudah T139 berjumlah tepat 1, sehingga tidak ada baris `Remove Temporary User`

### TC-GS-USER-921: Entri log lama tetap snapshot setelah Edit kedua

56. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Posisi {runId}-139`, tekan Enter
57. Klik (⋯) baris `Dewi Lestari Posisi {runId}-139` → `Edit`
58. Ubah Position `Staff` menjadi `Supervisor {runId}-139`
59. Klik `[Save]`
60. Tunggu aksi selesai (Popup Edit tertutup)
61. Klik (⋯) baris `Dewi Lestari Posisi {runId}-139` → `Edit`
62. Ubah Position `Supervisor {runId}-139` menjadi `Finance Manager`
63. Klik `[Save]`
64. Tunggu aksi selesai (Popup Edit tertutup)
65. Buka Detail `Dewi Lestari Posisi {runId}-139` > Tab `Changelog`, urutkan Oldest First
66. Verifikasi Tab Changelog Detail `Dewi Lestari Posisi {runId}-139`: baris pertama tetap Action `Edit`, Field `Position`, Old Value `Staff`, New Value `Supervisor {runId}-139`
67. Verifikasi Tab Changelog Detail `Dewi Lestari Posisi {runId}-139`: baris kedua Action `Edit`, Field `Position`, Old Value `Supervisor {runId}-139`, New Value `Finance Manager`

### TC-GS-USER-922: Rename Position tidak mengubah entri Changelog User lama

68. Buka Global Settings > User > tab Position, klik icon Search, ketik `Supervisor {runId}-139`, tekan Enter
69. Klik (⋯) baris `Supervisor {runId}-139` → `Edit`
70. Ubah nama Position menjadi `Team Supervisor {runId}-139`
71. Klik `[Save]`
72. Tunggu aksi selesai (Popup Edit tertutup dan baris Position `Team Supervisor {runId}-139` tampil)
73. Buka Detail `Dewi Lestari Posisi {runId}-139` > Tab `Changelog`, urutkan Oldest First
74. Verifikasi Tab Changelog Detail `Dewi Lestari Posisi {runId}-139`: baris lama Field `Position` tetap menampilkan New Value `Supervisor {runId}-139` (bukan `Team Supervisor {runId}-139`)

### TC-GS-USER-917: Hapus foto dari Avatar Detail tercatat Edit Photo

75. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe Foto {runId}-139`, tekan Enter
76. Klik Name `John Doe Foto {runId}-139` di User List
77. Hover Avatar header → klik `[Delete]` → klik `[Remove]`
78. Tunggu aksi selesai (Avatar header kembali menampilkan inisial)
79. Klik Tab `Changelog`
80. Verifikasi Tab Changelog Detail `John Doe Foto {runId}-139`: baris dengan Action `Edit`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T139

### TC-GS-USER-918: Foto aktif dicabut lewat admin override di File Manager tercatat Edit Photo

81. Buka Global Settings > File Manager, Delete foto profil aktif `john-admin-{runId}-139.png` milik `John Doe Admin {runId}-139`
82. Tunggu aksi selesai (foto tidak lagi tampil di File Manager)
83. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe Admin {runId}-139`, tekan Enter
84. Buka Detail `John Doe Admin {runId}-139` > Tab `Changelog`
85. Verifikasi Tab Changelog Detail `John Doe Admin {runId}-139`: baris dengan Action `Edit`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N` (admin pelaku), bertanggal pada atau sesudah T139

### TC-GS-USER-911: Delete user dengan TAG menulis baris Unpair TAG oleh pelaku Delete

86. Klik menu User di sidebar Global Settings, klik icon Search, ketik `John Doe Tag {runId}-139`, tekan Enter
87. Klik (⋯) baris `John Doe Tag {runId}-139` lalu `Delete`
88. Klik `[Delete]`
89. Tunggu aksi selesai (baris `John Doe Tag {runId}-139` hilang dari User List)
90. Buka Modal Changelog User, klik icon Search, ketik `John Doe Tag {runId}-139`, tekan Enter
91. Verifikasi Modal Changelog User: baris dengan Action `Delete`, Name `John Doe Tag {runId}-139`, Field `Name`, Old Value `John Doe Tag {runId}-139`, New Value `—`, bertanggal pada atau sesudah T139
92. Verifikasi Modal Changelog User: baris dengan Action `Unpair TAG`, Name `John Doe Tag {runId}-139`, Field `TAG`, Old Value `TAG-USR-0001`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T139

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 1044, 909, 910, 916, 1076, 921, 922, 917, 918, 911. TC-GS-USER-1044 (tanpa aksi) paling awal karena Default User harus belum pernah diedit (Dependensi TC: dijalankan sebelum TC-GS-USER-82 dan TC lain yang mengedit Default User; `suite.md` menempatkan spec pencatatan log sebelum spec yang mengedit Default User). TC-GS-USER-922 mengikuti TC-GS-USER-921 pada user yang sama. Dua TC yang mencabut foto (917, 918) dan TC yang menghapus user (911) berada paling akhir (bagian 3 prinsip 5).
- Penanda waktu T139 dicatat di langkah 8, sebelum aksi pemicu pertama yang diasersi (TC-GS-USER-909, S-12). Tiap TC memakai user seed sendiri (nama bersuffix `{runId}-139` berbeda), sehingga satu penanda untuk seluruh spec cukup; baris log dikenali lewat nama bersuffix dan tanggal pada atau sesudah T139, bukan posisi teratas. TC-GS-USER-1044 tidak memakai penanda karena mengasersi baris paling awal Default User (Oldest First).
- Klausa "tidak ada baris untuk field yang tidak berubah" (909 b), "tidak ada baris lain" (910 c), serta "tidak ada baris `Edit` Temporary Until" dan "tidak ada baris `Remove Temporary User`" (1076 b, c) diasersi sebagai jumlah seluruh baris bertanggal pada atau sesudah T139 untuk user seed itu, bukan asersi absence kelas g (aksi berhasil dan baris yang diharapkan terasersi pada hasil yang sama). Asersi absence kelas g untuk Edit No-Op (TC-GS-USER-919) dan lintas user (TC-GS-USER-920) ada di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`.
- Surface TC-GS-USER-916 disebut satu per satu: Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. Baris di System Log dan Activity Log diturunkan dari format TC-GS-USER-873 sampai 877 (Action, Object `User`, Name, Field, Old Value, New Value, dan Modified By hanya di Activity Log), karena Expected b TC-GS-USER-916 hanya menyebut "baris yang sama".
- Spec melewati sekitar 35 langkah (92 langkah). Alasan: seluruh blok satu kelas (pencatatan log) dengan user seed sendiri per TC sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) tidak dihitung ke batas ukuran (bagian 3 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 5, 7 sampai 15, 19 sampai 25, 29 sampai 34, 36, 38, 40 sampai 46, 51, 56 sampai 65, 68 sampai 73, 75 sampai 79, 81 sampai 84, 86 sampai 90. Frasa "Buka Detail ... > Tab ..." mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau Back), Search nama pada User List, dan klik Name; "Buka Modal Changelog User" mencakup klik icon Changelog pada Table Tools dan menutup modal sebelumnya.
- Temuan untuk QA:
  - TC-GS-USER-911: Expected b menyebut `TAG-4F7K2XQ9` yang terpasang pada John Doe Pre-setup (No. 18) dan tidak dapat dipasang ke user seed; spec memakai `TAG-USR-0001` pada user seed milik spec. Modified By baris `Delete` tidak disebut TC dan tidak diasersi.
  - TC-GS-USER-909: Expected hanya menyebut Old Value dan New Value `Dewi`→`Dewiana` dan `Lestari`→`Putri` tanpa Modified By; spec memberi suffix pada Last Name (`Lestari {runId}-139` → `Putri {runId}-139`). TC-GS-USER-910 tidak menyebut Position baru; spec memakai `HR Business Partner`, dan tidak mengasersi Old Value dan New Value baris Position karena Expected hanya menyebut `Edit | Position`.
  - TC-GS-USER-1044: Expected menyebut kolom Name pada Tab Changelog Detail, sedangkan Expected TC-GS-USER-873 butir b tidak menyebut kolom Name pada Tab Changelog Detail; spec mengikuti Expected tiap TC. Precondition "Entitas baru diregistrasi" tidak bisa dibuktikan oleh spec; spec mengandalkan urutan eksekusi dan keadaan seed, dan Dependensi TC menyebut `TC-GS-USER-82`.
  - TC-GS-USER-916: Langkah Uji 2 ("Buka Tab Changelog, System Log aktor, Activity Log") tidak menyebut nama Detail dan format baris System Log dan Activity Log; spec memakai Detail user seed dan format TC-GS-USER-873 sampai 877.
  - TC-GS-USER-917: judul menyebut "Edit/Delete foto dari Detail" sedangkan Langkah Uji hanya menghapus foto lewat hover Avatar; spec hanya menghapus.
  - TC-GS-USER-918: Langkah Uji tidak menyebut cara memilih foto aktif di File Manager dan dialog konfirmasi hapus bila ada; spec menulis aksi Delete apa adanya tanpa langkah konfirmasi. "Modified By = admin pelaku" ditulis `Siti N`.
  - TC-GS-USER-921: "Baris pertama" dan "Baris kedua" tidak menyebut urutan sort; spec memakai Oldest First. TC-GS-USER-922: cara rename Position di tab Position tidak disebut (spec memakai Edit pada baris Position), dan Position `Supervisor` Pre-setup (No. 22) adalah data bersama sehingga spec memakai Position seed bersuffix (S-06).
  - TC-GS-USER-1076: format tanggal `[tanggal +30 hari]` dan `[tanggal +45 hari]` tidak disebut; spec memakai Date Format General Settings client.
