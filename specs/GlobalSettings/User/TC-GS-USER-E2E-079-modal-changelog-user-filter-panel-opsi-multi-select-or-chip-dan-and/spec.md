---
id: TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Modal Changelog User: Filter Panel (Opsi Dropdown, Multi-Select per Field, Logika OR, Search Dropdown, Chip, Rentang Date, dan Logika AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-477
  - TC-GS-USER-478
  - TC-GS-USER-479
  - TC-GS-USER-480
  - TC-GS-USER-481
  - TC-GS-USER-482
  - TC-GS-USER-483
  - TC-GS-USER-484
  - TC-GS-USER-485
coverage:
  web: automated
---

# Modal Changelog User: Filter Panel (Opsi Dropdown, Multi-Select per Field, Logika OR, Search Dropdown, Chip, Rentang Date, dan Logika AND)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite: login di hook `before`, hook `after` mengembalikan sesi ke akun ini. Nama singkat di kolom Modified By: `Siti N` (tooltip `Siti Nurhaliza`). Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role, Full CRUD (Fajar Nugroho), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4); kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`. Dipakai hanya untuk memicu entri Changelog dengan Modified By kedua `Fajar N` (nama singkat dibentuk seperti `Siti N`; TC tidak menyebutnya), sehingga kolom Modified By punya sedikitnya dua nilai distinct (S-11). Tidak ada sesi UI kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Seeding minimal (S-11; lewat API di hook `before`, berurutan; kemampuan seeding user dan perubahan user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Tiap user seed diberi Position `Staff` (Tabel Data Uji Pre-setup No. 22), Division `Finance` (No. 23), dan Access `Fixed Asset` (No. 26), email `<nama>+{runId}-079@qwertysystem.net`. Kuota user plan cukup untuk user seed milik spec ini (disediakan tim FE). Hanya data yang dipakai `Verifikasi` yang di-seed; keempat kolom yang difilter punya sedikitnya dua nilai distinct):
  - U-1: Create `Alfa {runId}-079` oleh Siti Nurhaliza (Action Create, Field Name, Modified By `Siti N`), lalu Edit Position `Staff` menjadi `Supervisor` oleh Siti Nurhaliza (Action Edit, Field Position).
  - U-2: Create `Beta {runId}-079` oleh Fajar Nugroho (Action Create, Modified By `Fajar N`), lalu Deactivate oleh Siti Nurhaliza (Action Deactivate, Field Status (Global)).
  - Nilai distinct yang tersedia: Action `Create`, `Edit`, `Deactivate`; User Name `Alfa {runId}-079`, `Beta {runId}-079`; Field `Name`, `Position`, `Status (Global)`; Modified By `Siti N`, `Fajar N`. Seluruh entri seed hari uji dipakai TC-GS-USER-484.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1 dan U-2 bila masih ada; kembalikan sesi ke akun default suite. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: kontrol date range picker (memilih rentang hari uji dan rentang 1 Jan 2020 sampai 31 Jan 2020); mengetik di kolom pencarian dropdown filter; membaca seluruh entri Changelog Client (nilai distinct Action, User Name, Field, dan Modified By) sebagai pembanding opsi dropdown pada TC-GS-USER-478 (disediakan tim FE/BE; TC tidak menyebut cara); membaca indikator icon Filter aktif (gelap).
- Precondition TC-GS-USER-477 sampai 485: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); riwayat Changelog terisi.
- Suite serial (`parallel: false`). Changelog bersifat append-only dan dipakai bersama spec lain: asersi memakai pola baris (nilai bersuffix `{runId}-079`), bukan jumlah baris total, kecuali dinyatakan lain. Spec ini tidak mengubah atau menghapus data Pre-setup (S-06).
- State global yang diubah: tidak ada (Filter Panel hanya state tampilan modal).

## Test Steps

### TC-GS-USER-477: Screening Filter Panel
1. Klik icon Changelog di Table Tools
2. Klik icon Filter di modal
3. Verifikasi field `Action`: multi-select searchable dengan placeholder `All actions`
4. Verifikasi field `User Name`: multi-select searchable dengan placeholder `All users`
5. Verifikasi field `Field`: multi-select searchable dengan placeholder `All fields`
6. Verifikasi field `Modified By`: multi-select searchable dengan placeholder `All users`
7. Verifikasi field `Date`: date range picker dengan placeholder `Select date`
8. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
### TC-GS-USER-478: Opsi dropdown diambil dari nilai yang ada di tabel
9. Buka dropdown Action
10. Verifikasi opsi `Create`, `Edit`, dan `Deactivate` tersedia
11. Verifikasi dropdown Action hanya memuat nilai Action yang muncul pada baris Changelog (himpunan opsi sama dengan himpunan nilai Action pada seluruh entri Changelog)
12. Tutup dropdown Action
13. Buka dropdown User Name
14. Verifikasi opsi `Alfa {runId}-079` dan `Beta {runId}-079` tersedia
15. Verifikasi dropdown User Name hanya memuat nilai User Name yang muncul pada baris Changelog (himpunan opsi sama dengan himpunan nilai User Name pada seluruh entri Changelog)
16. Tutup dropdown User Name
17. Buka dropdown Field
18. Verifikasi opsi `Name`, `Position`, dan `Status (Global)` tersedia
19. Verifikasi dropdown Field hanya memuat nilai Field yang muncul pada baris Changelog (himpunan opsi sama dengan himpunan nilai Field pada seluruh entri Changelog)
20. Tutup dropdown Field
21. Buka dropdown Modified By
22. Verifikasi opsi `Siti N` dan `Fajar N` tersedia
23. Verifikasi dropdown Modified By hanya memuat nilai Modified By yang muncul pada baris Changelog (himpunan opsi sama dengan himpunan nilai Modified By pada seluruh entri Changelog)
24. Tutup dropdown Modified By dan Filter Panel
### TC-GS-USER-479: Filter multi-select per field menyaring baris
25. Klik icon Filter, pilih opsi `Edit` pada Action, klik `[Apply]`
26. Verifikasi field Action: semua baris tampil bernilai Action `Edit`
27. Verifikasi field Action: baris Edit `Alfa {runId}-079` tampil
28. Verifikasi field Action: icon Filter berubah gelap
29. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
30. Klik icon Filter, pilih opsi `Beta {runId}-079` pada User Name, klik `[Apply]`
31. Verifikasi field User Name: semua baris tampil bernilai User Name `Beta {runId}-079`
32. Verifikasi field User Name: baris Create `Beta {runId}-079` tampil
33. Verifikasi field User Name: icon Filter berubah gelap
34. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
35. Klik icon Filter, pilih opsi `Status (Global)` pada Field, klik `[Apply]`
36. Verifikasi field Field: semua baris tampil bernilai Field `Status (Global)`
37. Verifikasi field Field: baris Deactivate `Beta {runId}-079` tampil
38. Verifikasi field Field: icon Filter berubah gelap
39. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
40. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, klik `[Apply]`
41. Verifikasi field Modified By: semua baris tampil bernilai Modified By `Fajar N`
42. Verifikasi field Modified By: baris Create `Beta {runId}-079` tampil
43. Verifikasi field Modified By: icon Filter berubah gelap
44. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
### TC-GS-USER-480: Dua opsi dalam satu field digabung OR
45. Klik icon Filter, pilih opsi `Create` dan `Edit` pada Action, klik `[Apply]`
46. Verifikasi baris Action `Create` (`Alfa {runId}-079`) tampil
47. Verifikasi baris Action `Edit` (`Alfa {runId}-079`) tampil
48. Verifikasi semua baris tampil bernilai Action `Create` atau `Edit`
49. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
### TC-GS-USER-481: Search di dalam dropdown filter mempersempit opsi
50. Klik icon Filter, buka dropdown Action
51. Verifikasi opsi `Create` dan `Edit` tampil sebelum mengetik
52. Ketik `CREA` pada kolom pencarian dropdown Action
53. Verifikasi opsi `Create` tampil (tersaring substring tanpa membedakan huruf besar kecil)
54. Verifikasi opsi `Edit` tidak tampil
55. Ganti isi kolom pencarian dropdown dengan `zzz`
56. Verifikasi tidak ada opsi yang cocok
57. Tutup dropdown Action
### TC-GS-USER-482: Hapus chip via (X) meng-uncheck opsi
58. Pilih opsi `Create` lalu `Edit` pada Action
59. Verifikasi chip `Create` dan `Edit` tampil
60. Klik (X) pada chip pertama (`Create`)
61. Verifikasi chip `Create` hilang
62. Verifikasi chip `Edit` tetap tampil
63. Buka dropdown Action
64. Verifikasi checkbox opsi `Create` ter-uncheck
65. Tutup dropdown Action
### TC-GS-USER-483: Uncheck opsi di dropdown menghapus chip
66. Klik `[Clear Field]`, pilih opsi `Create` lalu `Edit` pada Action
67. Buka dropdown Action, hilangkan centang opsi kedua (`Edit`)
68. Verifikasi chip `Edit` hilang
69. Verifikasi chip `Create` tetap tampil
70. Tutup dropdown Action, klik `[Clear Field]`
### TC-GS-USER-484: Filter date range
71. Pilih rentang tanggal hari uji pada Date
72. Verifikasi tanggal di input Date mengikuti Date Format General Settings
73. Klik `[Apply]`
74. Verifikasi semua baris tampil bertanggal dalam rentang hari uji
75. Verifikasi baris Create `Alfa {runId}-079` tampil
76. Klik icon Filter, klik `[Clear Field]`, pilih rentang tanggal 1 Jan 2020 sampai 31 Jan 2020 pada Date, klik `[Apply]`
77. Verifikasi baris di luar rentang tidak tampil (pesan `No results found`)
78. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
### TC-GS-USER-485: Kombinasi dua field filter digabung AND
79. Klik icon Filter, pilih opsi `Create` pada Action dan opsi `Fajar N` pada Modified By, klik `[Apply]`
80. Verifikasi semua baris tampil bernilai Action `Create` dan Modified By `Fajar N`
81. Verifikasi baris Create `Beta {runId}-079` tampil
82. Verifikasi baris Create `Alfa {runId}-079` (Modified By `Siti N`) tidak tampil
83. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (477 sampai 485). Screening (477) dan TC yang hanya mengamati dropdown (478) di awal; TC tanpa penyaringan data (481 sampai 483) tidak mengubah hasil tabel. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): `Klik icon Filter, klik [Clear Field], klik [Apply]` di akhir tiap blok yang menyaring (melepas filter sebelum blok berikutnya), serta menutup dropdown dan Filter Panel. Langkah `[Clear Field]` + `[Apply]` pada TC-GS-USER-479 adalah langkah TC.
- Langkah tambahan atas TC (S-03): `Verifikasi` baris seed tampil pada TC-GS-USER-479, 480, 484, 485 adalah anchor positif untuk asersi "semua baris" dan ketiadaan baris (bagian 8b butir 2); `Verifikasi` opsi `Create`, `Edit` tampil dan chip tampil pada TC-GS-USER-481 dan 482 adalah pembanding sebelum penyaringan dan sebelum penghapusan chip. Rentang 1 Jan 2020 sampai 31 Jan 2020 pada TC-GS-USER-484 mengasersi bahwa baris di luar rentang tidak tampil.
- Asersi "semua baris" membaca baris yang tampil pada halaman 1 hasil penyaringan; baris seed bersuffix `{runId}-079` dipakai sebagai anchor sehingga entri dari run atau spec lain tidak memengaruhi hasil.
- Pembagian TC Modal Changelog User: screening dan Search ada di spec 078, kombinasi Search+Filter ada di spec 080, Sort dan Pagination ada di spec 081, Setup Column ada di spec 082, Download ada di spec 083.
- Spec melewati sekitar 35 langkah (83 langkah) karena tiap field filter pada TC-GS-USER-478 dan 479 memerlukan aksi dan `Verifikasi` sendiri (S-01); semua blok satu layar (Filter Panel Modal Changelog User), satu akun aktor, dan satu dataset seed, serta tiap blok melepas filter di akhirnya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: (1) TC-GS-USER-478 "hanya nilai yang genuinely muncul di baris tabel ini" tidak menyebut cara mengetahui himpunan nilai pada seluruh entri; spec membandingkan opsi dengan himpunan nilai yang dibaca tim FE/BE. (2) TC-GS-USER-479 "icon Filter berubah gelap" tidak menyebut cara membaca warna; kemampuan membaca indikator disediakan tim FE. (3) TC-GS-USER-484 Data Uji "rentang tanggal sesuai data" tidak menyebut rentang; spec memakai rentang hari uji (berisi baris seed) dan rentang 1 Jan 2020 sampai 31 Jan 2020. (4) TC-GS-USER-485 Data Uji "2 field" tidak menyebut field dan nilainya; spec memakai Action `Create` dan Modified By `Fajar N`. (5) TC-GS-USER-478 dan 485 tidak menyebut teks opsi Modified By; spec memakai nama singkat seperti di kolom tabel (`Siti N`, `Fajar N`). (6) TC-GS-USER-481 tidak menyebut teks yang ditampilkan saat tidak ada opsi cocok; spec hanya mengasersi tidak ada opsi.
