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
  - Entri 1 dan 2 dibuat dengan jam server diatur ke dua hari sebelum hari ini (D-2), lalu jam dipulihkan sebelum entri 3 sampai 6 (hari ini, D0), agar kolom Date punya dua nilai distinct untuk TC-GS-USER-525. Kemampuan mengatur jam server saat seeding disediakan tim FE/BE; TC tidak memberi caranya. Log yang dibuat saat jam digeser bercap waktu hasil geseran, jadi asersi memakai pola baris (S-12).
  - Nilai distinct (S-11): Action 3 (`Assign`, `Edit`, `Remove`), Role 3 (`Manage TAG`, `Manage files`, `Manage hardware`), Field 2 (`Access`, `Update`), Modified By 2 (`Siti N`, `Fajar N`), Date 2 hari (D-2 dan D0).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan jam server dan jam browser bila masih digeser; hapus user seed lewat API. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: memilih rentang tanggal pada date range picker; membaca Date Format General Settings yang berlaku (disediakan tim FE); mengetik di kolom search dropdown filter; membaca warna icon Filter (aktif gelap).
- Precondition TC-GS-USER-518 sampai 526: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data pre-setup User tersedia; riwayat Changelog Role user seed terisi.
- Suite serial (`parallel: false`), lihat `suite.md`.
- State global yang dipulihkan: jam server dan jam browser (hanya bila digeser saat seeding).

## Test Steps

### TC-GS-USER-518: Screening Filter Panel

1. Klik Name `Ahmad Fauzi {runId}-085` di User List
2. Klik Tab `Role`
3. Klik icon Changelog di toolbar Tab Role
4. Klik icon Filter
5. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `All actions`
6. Verifikasi field `Role` berupa multi-select searchable dengan placeholder `All roles`
7. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `All fields`
8. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder `All users`
9. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
10. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-519: Opsi dropdown filter bersumber dari nilai yang ada di tabel

11. Buka dropdown Action
12. Verifikasi opsi Action memuat `Assign`, `Edit`, dan `Remove`
13. Verifikasi opsi Action tidak memuat `Delete`
14. Buka dropdown Role
15. Verifikasi opsi Role memuat `Manage TAG`, `Manage files`, dan `Manage hardware`
16. Verifikasi opsi Role tidak memuat `Import data`
17. Buka dropdown Field
18. Verifikasi opsi Field memuat `Access` dan `Update`
19. Verifikasi opsi Field tidak memuat `Delete`
20. Buka dropdown Modified By
21. Verifikasi opsi Modified By memuat `Siti N` dan `Fajar N`
22. Verifikasi opsi Modified By tidak memuat `Yudi P`

### TC-GS-USER-522: Search di dalam dropdown filter mempersempit opsi

23. Buka dropdown Action
24. Verifikasi opsi `Assign`, `Edit`, dan `Remove` tampil (pembanding sebelum mengetik)
25. Ketik `ASS` pada search dropdown Action
26. Verifikasi opsi `Assign` tampil
27. Verifikasi opsi `Edit` tidak tampil
28. Ganti isi search dropdown Action dengan `zzz`
29. Verifikasi tidak ada opsi cocok
30. Kosongkan search dropdown Action

### TC-GS-USER-523: Hapus chip filter via (X) meng-uncheck opsi

31. Pilih opsi `Assign` dan `Edit` pada dropdown Action
32. Klik (X) pada chip pertama (`Assign`)
33. Verifikasi chip `Assign` hilang
34. Verifikasi chip `Edit` tetap tampil
35. Buka dropdown Action
36. Verifikasi checkbox opsi `Assign` ter-uncheck

### TC-GS-USER-524: Uncheck opsi di dropdown menghapus chip

37. Pilih opsi `Assign` pada dropdown Action (chip `Edit` lalu `Assign`)
38. Buka dropdown Action, uncheck opsi kedua (`Assign`)
39. Verifikasi chip `Assign` hilang
40. Verifikasi chip `Edit` tetap tampil

### TC-GS-USER-520: Filter multi-select per field menyaring baris

41. Klik `[Clear Field]`, lalu klik `[Apply]`
42. Klik icon Filter, pilih opsi Action `Remove`, klik `[Apply]`
43. Verifikasi Action: baris Action `Remove` tampil
44. Verifikasi Action: baris Action `Assign` tidak tampil
45. Verifikasi icon Filter berubah gelap
46. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
47. Klik icon Filter, pilih opsi Role `Manage files`, klik `[Apply]`
48. Verifikasi Role: baris Role `Manage files` tampil
49. Verifikasi Role: baris Role `Manage TAG` tidak tampil
50. Verifikasi icon Filter berubah gelap
51. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
52. Klik icon Filter, pilih opsi Field `Update`, klik `[Apply]`
53. Verifikasi Field: baris Field `Update` tampil
54. Verifikasi Field: baris Field `Access` tidak tampil
55. Verifikasi icon Filter berubah gelap
56. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
57. Klik icon Filter, pilih opsi Modified By `Fajar N`, klik `[Apply]`
58. Verifikasi Modified By: baris Modified By `Fajar N` tampil
59. Verifikasi Modified By: baris Modified By `Siti N` tidak tampil
60. Verifikasi icon Filter berubah gelap
61. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-521: Dua opsi dalam satu field filter digabung OR

62. Klik icon Filter, pilih opsi Action `Assign` dan `Remove`, klik `[Apply]`
63. Verifikasi baris Action `Assign` tampil
64. Verifikasi baris Action `Remove` tampil
65. Verifikasi baris Action `Edit` tidak tampil
66. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-525: Filter date range

67. Verifikasi baris Action `Edit` Role `Manage hardware` tampil (pembanding hari ini sebelum Filter Date)
68. Klik icon Filter, pilih rentang tanggal pada Date dari D-2 sampai D-2, klik `[Apply]`
69. Verifikasi Date: baris Action `Assign` Role `Manage TAG` tampil
70. Verifikasi Date: baris Action `Edit` Role `Manage TAG` tampil
71. Verifikasi Date: baris Action `Remove` Role `Manage files` tidak tampil
72. Klik icon Filter
73. Verifikasi tanggal di input Date mengikuti Date Format General Settings
74. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-526: Kombinasi dua field filter digabung AND

75. Klik icon Filter, pilih opsi Action `Assign` dan Modified By `Fajar N`, klik `[Apply]`
76. Verifikasi baris Action `Assign` Role `Manage files` Modified By `Fajar N` tampil
77. Verifikasi baris Action `Assign` Role `Manage TAG` Modified By `Siti N` tidak tampil
78. Verifikasi baris Action `Edit` Role `Manage hardware` Modified By `Fajar N` tidak tampil
79. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka sekali di langkah 1 sampai 3 untuk semua TC; Filter Panel dibuka di langkah 4.
- Urutan TC dalam spec: TC-GS-USER-518, 519, 522, 523, 524, 520, 521, 525, 526. Alasan: screening (518) di awal, TC-GS-USER-519, 522, 523, dan 524 hanya mengamati dropdown dan chip tanpa `[Apply]` sehingga mendahului TC yang menerapkan filter (bagian 3 konvensi); TC-GS-USER-520, 521, 525, 526 menerapkan filter dan masing-masing diakhiri `[Clear Field]` + `[Apply]`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 30 (mengosongkan search dropdown), 41 (membuang chip `Edit` sisa TC-GS-USER-524), 46, 51, 56, 61, 66, 74, dan 79 (`[Clear Field]` + `[Apply]` sesudah asersi; di TC-GS-USER-520 dan 525 langkah ini tertulis "lalu clear" / `[Clear Field]` + `[Apply]`).
- Langkah 24, 43, 48, 53, 58, 63, 67, 69, 70, dan 76 adalah anchor positif untuk asersi ketiadaan (opsi atau baris tidak tampil; S-03, bagian 8b butir 2). Pada TC-GS-USER-519 asersi "tidak memuat" (langkah 13, 16, 19, 22) mewujudkan Expected "nilai tanpa baris tidak tampil" dan didahului `Verifikasi` opsi yang ada pada dropdown yang sama.
- Pada TC-GS-USER-523 dan 524 opsi Action yang dipilih ditetapkan `Assign` dan `Edit` (TC hanya menyebut "2 opsi"); pada TC-GS-USER-524 opsi kedua adalah `Assign` yang dipilih ulang di langkah 37.
- Spec melewati sekitar 35 langkah (79 langkah) karena TC-GS-USER-520 menguji empat field masing-masing dengan pilih, `[Apply]`, tiga `Verifikasi` (S-01), dan `[Clear Field]` + `[Apply]`, dan tiap field dropdown pada TC-GS-USER-519 memerlukan `Verifikasi` sendiri. Semua blok satu kelas harness (Filter Panel satu Modal Changelog Role), satu akun, satu dataset, dan tiap blok berdiri sendiri karena filter dilepas di akhir blok; modal dibuka sekali.
- TC terbagi lintas spec: pemakaian Filter dalam kombinasi dengan Search dan Clear (TC-GS-USER-527 sampai 531) diverifikasi di spec 086; Filter pada kombinasi dengan Sort dan Pagination (TC-GS-USER-550) di spec 087.
- Temuan untuk QA: (1) TC-GS-USER-525 membutuhkan entri Changelog Role pada dua tanggal berbeda, tetapi TC tidak memberi cara; spec meminta pengaturan jam server saat seeding (disediakan tim FE/BE). (2) TC-GS-USER-520 Expected "icon Filter berubah gelap saat aktif" tidak menyebut cara mengamati warna; spec memakai kemampuan membaca state icon. (3) TC-GS-USER-523 dan 524 menyebut "2 opsi" tanpa nama; spec menetapkan `Assign` dan `Edit`. (4) TC-GS-USER-519 tidak menyebut apakah label opsi Modified By nama singkat atau nama lengkap; spec memakai nama singkat seperti di tabel. (5) TC-GS-USER-525 tidak menyebut format tanggal konkret; spec mengasersi kesesuaian dengan Date Format General Settings yang berlaku. (6) TC-GS-USER-518 sampai 526 menyebut `Ahmad Fauzi` tanpa suffix; spec memakai user seed bersuffix.
