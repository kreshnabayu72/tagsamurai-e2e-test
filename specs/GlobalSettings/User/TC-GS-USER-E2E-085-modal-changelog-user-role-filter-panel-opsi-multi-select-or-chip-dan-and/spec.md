---
id: TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Modal Changelog Role: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-518
  - TC-GS-USER-519
  - TC-GS-USER-520
  - TC-GS-USER-521
  - TC-GS-USER-522
  - TC-GS-USER-523
  - TC-GS-USER-524
  - TC-GS-USER-525
  - TC-GS-USER-526
coverage:
  web: automated
---

# Modal Changelog Role: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control Siti Nurhaliza (`Siti N`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), akun default suite. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User).
- Pelaku seeding lewat sesi API (tidak login UI): Manage user and role (Full CRUD) Fajar Nugroho (`Fajar N`), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 4), `Spectra.env.GS_FULLCRUD_PASSWORD`. Fajar menjadi nilai Modified By kedua selain `Siti N`.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak dipakai. TC menyebut `Ahmad Fauzi` (Tabel Data Uji Pre-setup baris 13); aksi tulis Role memakai user seed milik spec (S-06), jadi Pre-setup tidak diubah.
- Data Dinamis: user seed `Ahmad Fauzi {runId}-085`, email `ahmadfauzi+{runId}-085@qwertysystem.net`, Access `Global Settings`, bukan tier, field wajib lain diisi seadanya oleh seeding.
- Seeding minimal (S-11; lewat API di hook `before`, urutan sebagai berikut; setara TC-GS-USER-902, 903, 904, 1052). Entri yang diasersi:
  - 1. Siti N: Assign `Manage TAG` -> `Assign | Manage TAG | Access | — | Assigned | Siti N`.
  - 2. Siti N: centang Update `Manage TAG` -> `Edit | Manage TAG | Update | Inactive | Active | Siti N`.
  - 3. Fajar N: Assign `Manage files` -> `Assign | Manage files | Access | — | Assigned | Fajar N`.
  - 4. Siti N: Remove `Manage files` -> `Remove | Manage files | Access | Assigned | — | Siti N`.
  - 5. Siti N: centang Read `Manage hardware` -> `Assign | Manage hardware | Access | — | Assigned | Siti N`.
  - 6. Fajar N: centang Update `Manage hardware` -> `Edit | Manage hardware | Update | Inactive | Active | Fajar N`.
  - Entri 1 dan 2 dibuat dengan jam server diatur ke dua hari sebelum hari ini, lalu jam dipulihkan sebelum entri 3 sampai 6 (hari ini), agar kolom Date punya dua nilai distinct untuk TC-GS-USER-525. Kemampuan mengatur jam server saat seeding disediakan tim FE/BE; TC tidak memberi caranya. Log yang dibuat saat jam digeser bercap waktu hasil geseran, jadi asersi memakai pola baris (S-12).
  - Nilai distinct (S-11): Action 3 (`Assign`, `Edit`, `Remove`), Role 3 (`Manage TAG`, `Manage files`, `Manage hardware`), Field 2 (`Access`, `Update`), Modified By 2 (`Siti N`, `Fajar N`), Date 2 hari (dua hari sebelum hari ini dan hari ini).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan jam server dan jam browser bila masih digeser; hapus user seed lewat API. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: memilih rentang tanggal pada date range picker; membaca Date Format General Settings yang berlaku (disediakan tim FE); mengetik di kolom search dropdown filter; membaca warna icon Filter (gelap saat panel terbuka) dan badge titik pada icon Filter (tampil selama filter ter-Apply).
- Precondition TC-GS-USER-518 sampai 526: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data pre-setup User tersedia; riwayat Changelog Role user seed terisi.
- Suite serial (`parallel: false`), lihat `suite.md`.
- State global yang dipulihkan: jam server dan jam browser (hanya bila digeser saat seeding).

## Test Steps

### TC-GS-USER-518: Screening Filter Panel

1. Ketik Search `Ahmad Fauzi {runId}-085`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-085` di User List
3. Klik Tab `Role`
4. Klik icon Changelog di toolbar Tab Role
5. Klik icon Filter
6. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `All actions`
7. Verifikasi field `Role` berupa multi-select searchable dengan placeholder `All roles`
8. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `All fields`
9. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder `All users`
10. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
11. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-519: Opsi dropdown filter bersumber dari nilai yang ada di tabel

12. Buka dropdown Action
13. Verifikasi opsi Action memuat `Assign`, `Edit`, dan `Remove`
14. Verifikasi opsi Action tidak memuat `Delete`
15. Buka dropdown Role
16. Verifikasi opsi Role memuat `Manage TAG`, `Manage files`, dan `Manage hardware`
17. Verifikasi opsi Role tidak memuat `Import data`
18. Buka dropdown Field
19. Verifikasi opsi Field memuat `Access` dan `Update`
20. Verifikasi opsi Field tidak memuat `Delete`
21. Buka dropdown Modified By
22. Verifikasi opsi Modified By memuat `Siti N` dan `Fajar N`
23. Verifikasi opsi Modified By tidak memuat `Yudi P`

### TC-GS-USER-522: Search di dalam dropdown filter mempersempit opsi

24. Buka dropdown Action
25. Verifikasi opsi `Assign`, `Edit`, dan `Remove` tampil (pembanding sebelum mengetik)
26. Ketik `ASS` pada search dropdown Action
27. Verifikasi opsi `Assign` tampil
28. Verifikasi opsi `Edit` tidak tampil
29. Ganti isi search dropdown Action dengan `zzz`
30. Verifikasi tidak ada opsi cocok
31. Kosongkan search dropdown Action

### TC-GS-USER-523: Hapus chip filter via (X) meng-uncheck opsi

32. Pilih opsi `Assign` dan `Edit` pada dropdown Action
33. Klik (X) pada chip pertama (`Assign`)
34. Verifikasi chip `Assign` hilang
35. Verifikasi chip `Edit` tetap tampil
36. Buka dropdown Action
37. Verifikasi checkbox opsi `Assign` ter-uncheck

### TC-GS-USER-524: Uncheck opsi di dropdown menghapus chip

38. Pilih opsi `Assign` pada dropdown Action (chip `Edit` lalu `Assign`)
39. Buka dropdown Action, uncheck opsi kedua (`Assign`)
40. Verifikasi chip `Assign` hilang
41. Verifikasi chip `Edit` tetap tampil

### TC-GS-USER-520: Filter multi-select per field menyaring baris

42. Klik `[Clear Field]`, lalu klik `[Apply]`
43. Klik icon Filter, pilih opsi Action `Remove`, klik `[Apply]`
44. Verifikasi field Action: badge titik tampil pada icon Filter
45. Verifikasi Action: baris Action `Remove` tampil
46. Verifikasi Action: baris Action `Assign` tidak tampil
47. Klik icon Filter
48. Verifikasi icon Filter berubah gelap
49. Klik `[Clear Field]`, lalu klik `[Apply]`
50. Klik icon Filter, pilih opsi Role `Manage files`, klik `[Apply]`
51. Verifikasi field Role: badge titik tampil pada icon Filter
52. Verifikasi Role: baris Role `Manage files` tampil
53. Verifikasi Role: baris Role `Manage TAG` tidak tampil
54. Klik icon Filter
55. Verifikasi icon Filter berubah gelap
56. Klik `[Clear Field]`, lalu klik `[Apply]`
57. Klik icon Filter, pilih opsi Field `Update`, klik `[Apply]`
58. Verifikasi field Field: badge titik tampil pada icon Filter
59. Verifikasi Field: baris Field `Update` tampil
60. Verifikasi Field: baris Field `Access` tidak tampil
61. Klik icon Filter
62. Verifikasi icon Filter berubah gelap
63. Klik `[Clear Field]`, lalu klik `[Apply]`
64. Klik icon Filter, pilih opsi Modified By `Fajar N`, klik `[Apply]`
65. Verifikasi field Modified By: badge titik tampil pada icon Filter
66. Verifikasi Modified By: baris Modified By `Fajar N` tampil
67. Verifikasi Modified By: baris Modified By `Siti N` tidak tampil
68. Klik icon Filter
69. Verifikasi icon Filter berubah gelap
70. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-521: Dua opsi dalam satu field filter digabung OR

71. Klik icon Filter, pilih opsi Action `Assign` dan `Remove`, klik `[Apply]`
72. Verifikasi baris Action `Assign` tampil
73. Verifikasi baris Action `Remove` tampil
74. Verifikasi baris Action `Edit` tidak tampil
75. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-525: Filter date range

76. Verifikasi baris Action `Edit` Role `Manage hardware` tampil (pembanding hari ini sebelum Filter Date)
77. Klik icon Filter, pilih rentang tanggal pada Date dari dua hari sebelum hari ini sampai dua hari sebelum hari ini, klik `[Apply]`
78. Verifikasi Date: baris Action `Assign` Role `Manage TAG` tampil
79. Verifikasi Date: baris Action `Edit` Role `Manage TAG` tampil
80. Verifikasi Date: baris Action `Remove` Role `Manage files` tidak tampil
81. Klik icon Filter
82. Verifikasi tanggal di input Date mengikuti Date Format General Settings
83. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-526: Kombinasi dua field filter digabung AND

84. Klik icon Filter, pilih opsi Action `Assign` dan Modified By `Fajar N`, klik `[Apply]`
85. Verifikasi baris Action `Assign` Role `Manage files` Modified By `Fajar N` tampil
86. Verifikasi baris Action `Assign` Role `Manage TAG` Modified By `Siti N` tidak tampil
87. Verifikasi baris Action `Edit` Role `Manage hardware` Modified By `Fajar N` tidak tampil
88. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka sekali di langkah 2 sampai 4 untuk semua TC; Filter Panel dibuka di langkah 5.
- Urutan TC dalam spec: TC-GS-USER-518, 519, 522, 523, 524, 520, 521, 525, 526. Alasan: screening (518) di awal, TC-GS-USER-519, 522, 523, dan 524 hanya mengamati dropdown dan chip tanpa `[Apply]` sehingga mendahului TC yang menerapkan filter (bagian 3 konvensi); TC-GS-USER-520, 521, 525, 526 menerapkan filter dan masing-masing diakhiri `[Clear Field]` + `[Apply]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama baris persis sebelum Klik Name, karena User List bisa lebih dari satu halaman; akhiran runId saja tidak cukup), langkah 31 (mengosongkan search dropdown), 42 (membuang chip `Edit` sisa TC-GS-USER-524), 49, 56, 63, 70, 75, 83, dan 88 (`[Clear Field]` + `[Apply]` sesudah asersi; di TC-GS-USER-520 dan 525 langkah ini tertulis "lalu clear" / `[Clear Field]` + `[Apply]`); langkah 47, 54, 61, dan 68 (`Klik icon Filter`) membuka kembali Filter Panel sesudah `[Apply]` agar icon Filter diamati saat panel terbuka, sesuai Expected TC-GS-USER-520 ("icon Filter gelap saat panel terbuka").
- Langkah 25, 45, 52, 59, 66, 72, 76, 78, 79, dan 85 adalah anchor positif untuk asersi ketiadaan (opsi atau baris tidak tampil; S-03, bagian 8b butir 2). Pada TC-GS-USER-519 asersi "tidak memuat" (langkah 14, 17, 20, 23) mewujudkan Expected "nilai tanpa baris tidak tampil" dan didahului `Verifikasi` opsi yang ada pada dropdown yang sama.
- Tiap `[Apply]` pada TC-GS-USER-520 diikuti `Verifikasi` badge titik pada icon Filter (Expected TC-GS-USER-520 a-d: badge titik tampil selama filter ter-Apply); `Verifikasi` icon Filter gelap hanya sesudah `Klik icon Filter` (panel terbuka).
- Pada TC-GS-USER-523 dan 524 opsi Action yang dipilih ditetapkan `Assign` dan `Edit` (TC hanya menyebut "2 opsi"); pada TC-GS-USER-524 opsi kedua adalah `Assign` yang dipilih ulang di langkah 38.
- Spec melewati sekitar 35 langkah (88 langkah) karena TC-GS-USER-520 menguji empat field masing-masing dengan pilih, `[Apply]`, tiga `Verifikasi` dan satu `Verifikasi` badge titik (S-01), dan `[Clear Field]` + `[Apply]`, dan tiap field dropdown pada TC-GS-USER-519 memerlukan `Verifikasi` sendiri. Semua blok satu kelas harness (Filter Panel satu Modal Changelog Role), satu akun, satu dataset, dan tiap blok berdiri sendiri karena filter dilepas di akhir blok; modal dibuka sekali.
- TC terbagi lintas spec: pemakaian Filter dalam kombinasi dengan Search dan Clear (TC-GS-USER-527 sampai 531) diverifikasi di spec 086; Filter pada kombinasi dengan Sort dan Pagination (TC-GS-USER-550) di spec 087.
- Temuan untuk QA: (1) TC-GS-USER-525 membutuhkan entri Changelog Role pada dua tanggal berbeda, tetapi TC tidak memberi cara; spec meminta pengaturan jam server saat seeding (disediakan tim FE/BE). (2) TC-GS-USER-520 Expected "icon Filter berubah gelap saat aktif" tidak menyebut cara mengamati warna; spec memakai kemampuan membaca state icon. (3) TC-GS-USER-523 dan 524 menyebut "2 opsi" tanpa nama; spec menetapkan `Assign` dan `Edit`. (4) TC-GS-USER-519 tidak menyebut apakah label opsi Modified By nama singkat atau nama lengkap; spec memakai nama singkat seperti di tabel. (5) TC-GS-USER-525 tidak menyebut format tanggal konkret; spec mengasersi kesesuaian dengan Date Format General Settings yang berlaku. (6) TC-GS-USER-518 sampai 526 menyebut `Ahmad Fauzi` tanpa suffix; spec memakai user seed bersuffix.
