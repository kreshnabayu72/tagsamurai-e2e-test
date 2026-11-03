---
id: TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Tab System Log Detail: Filter Panel (Field, Opsi Dropdown, Multi-Select, OR, Search Dropdown, Chip, Rentang Date, dan AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-598
  - TC-GS-USER-599
  - TC-GS-USER-600
  - TC-GS-USER-601
  - TC-GS-USER-602
  - TC-GS-USER-603
  - TC-GS-USER-604
  - TC-GS-USER-605
  - TC-GS-USER-606
coverage:
  web: automated
---

# Tab System Log Detail: Filter Panel (Field, Opsi Dropdown, Multi-Select, OR, Search Dropdown, Chip, Rentang Date, dan AND)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor UI: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 23 dan 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). System Log memuat aksi yang dilakukan user sebagai aktor (PRD user.md §8.3). Tiap user diberi Division `Finance` dan Access `Fixed Asset`:
  - Pemilik log `Aktor Log {runId}-097`, email `aktorlog+{runId}-097@qwertysystem.net`, tier Total Control, status Activated, password `Spectra.env.USER_PASSWORD`. Aktivasi akun seed dan sesi API Aktor Log disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut mekanismenya). Seluruh aksi seed di bawah dijalankan lewat sesi API Aktor Log.
  - Target aksi `Target Alfa {runId}-097` (email `targetalfa+{runId}-097@qwertysystem.net`, Position `Staff`) dan `Target Beta {runId}-097` (email `targetbeta+{runId}-097@qwertysystem.net`).
  - Aksi seed oleh Aktor Log, berurutan (hanya data yang dipakai `Verifikasi`, S-11): (1) Create `Target Alfa` (Field `Name`, Old Value `—`); (2) Create `Target Beta`; (3) Edit Position `Target Alfa` dari `Staff` menjadi `Supervisor`; (4) Deactivate `Target Alfa` (Field `Status (Global)`, `Active` menjadi `Inactive`); (5) Activate `Target Alfa` (`Inactive` menjadi `Active`); (6) Delete `Target Beta` (Field `Name`, New Value `—`); (7) Assign Total Control ke `Target Alfa` (Object `Total Control`, Field `Access Level`, New Value `Total Control`). Hasil: kolom Action memuat `Activate`, `Assign`, `Create`, `Deactivate`, `Delete`, `Edit`; kolom Object memuat `Total Control` dan `User`; kolom Name memuat `Target Alfa` dan `Target Beta`; kolom Field memuat `Access Level`, `Name`, `Position`, `Status (Global)` (sedikitnya dua nilai distinct per kolom, S-11). Seluruh entri bertanggal hari uji.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa` (cabut tier Total Control lebih dulu bila diperlukan), `Target Beta` bila masih ada, dan `Aktor Log`; hapus sisa user bersuffix `-097` dari run lama. Entri log tidak bisa dihapus.
- Kemampuan teknis: kontrol date range picker (memilih rentang 1 Jan 2020 sampai 31 Jan 2020 dan rentang yang memuat hari uji); membaca format tanggal yang dikonfigurasi di General Settings (Date Format) sebagai pembanding teks di input Date; mengamati state icon Filter (gelap saat panel terbuka), badge titik selama filter ter-Apply, chip, dan checkbox opsi dropdown.
- State global yang diubah: tidak ada (filter hanya state tampilan tab; spec tidak mengubah General Settings). Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-598 sampai 606: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-598: Screening Filter Panel

1. Klik icon Search di User List, ketik `Aktor Log {runId}-097`, tekan Enter
2. Klik Name `Aktor Log {runId}-097`
3. Klik Tab `System Log`
4. Klik icon Filter
5. Verifikasi field `Action`: multi-select searchable dengan placeholder `All actions`
6. Verifikasi field `Object`: multi-select searchable dengan placeholder `All objects`
7. Verifikasi field `Name`: multi-select searchable dengan placeholder `All users`
8. Verifikasi field `Field`: multi-select searchable dengan placeholder `All fields`
9. Verifikasi field `Date`: date range picker dengan placeholder `Select date`
10. Verifikasi tombol `[Clear Field]` dan `[Apply]`

### TC-GS-USER-599: Opsi dropdown filter diambil dari nilai yang ada di tabel

11. Buka dropdown Action
12. Verifikasi opsi dropdown Action tepat `Activate`, `Assign`, `Create`, `Deactivate`, `Delete`, `Edit`
13. Verifikasi opsi `Pair TAG` (nilai tanpa baris di tabel) tidak tampil di dropdown Action
14. Buka dropdown Object
15. Verifikasi opsi dropdown Object tepat `Total Control` dan `User`
16. Verifikasi opsi `Non-Login User` (nilai tanpa baris di tabel) tidak tampil di dropdown Object
17. Buka dropdown Name
18. Verifikasi opsi dropdown Name tepat `Target Alfa {runId}-097` dan `Target Beta {runId}-097`
19. Verifikasi opsi `Aktor Log {runId}-097` (nilai tanpa baris di kolom Name) tidak tampil di dropdown Name
20. Buka dropdown Field
21. Verifikasi opsi dropdown Field tepat `Access Level`, `Name`, `Position`, `Status (Global)`
22. Verifikasi opsi `Photo` (nilai tanpa baris di tabel) tidak tampil di dropdown Field

### TC-GS-USER-602: Search di dalam dropdown filter mempersempit opsi

23. Buka dropdown Action
24. Ketik `REAT` pada kotak search dropdown
25. Verifikasi opsi `Create` tampil
26. Verifikasi opsi `Delete` tidak tampil
27. Ganti isi kotak search dropdown dengan `zzz`
28. Verifikasi tidak ada opsi yang cocok
29. Kosongkan kotak search dropdown

### TC-GS-USER-603: Hapus chip filter via (X) meng-uncheck opsi

30. Pilih opsi Action `Create`
31. Pilih opsi Action `Delete`
32. Klik (X) pada chip pertama (`Create`)
33. Verifikasi chip `Create` hilang
34. Verifikasi chip `Delete` tetap tampil
35. Buka dropdown Action
36. Verifikasi checkbox opsi `Create` ter-uncheck

### TC-GS-USER-604: Uncheck opsi di dropdown menghapus chip

37. Klik `[Clear Field]`
38. Pilih opsi Action `Create`
39. Pilih opsi Action `Delete`
40. Buka dropdown Action
41. Hilangkan centang opsi kedua (`Delete`)
42. Verifikasi chip `Delete` hilang
43. Verifikasi chip `Create` tetap tampil

### TC-GS-USER-600: Filter multi-select per field menyaring baris

44. Klik `[Clear Field]`
45. Pilih Action `Create`, klik `[Apply]`
46. Verifikasi sedikitnya satu baris tampil di tabel
47. Verifikasi tabel hanya memuat baris Action `Create`
48. Verifikasi badge titik tampil pada icon Filter selama filter ter-Apply
49. Klik icon Filter
50. Verifikasi icon Filter gelap saat panel terbuka
51. Klik `[Clear Field]`, lalu klik `[Apply]`
52. Klik icon Filter, pilih Object `Total Control`, klik `[Apply]`
53. Verifikasi sedikitnya satu baris tampil di tabel
54. Verifikasi tabel hanya memuat baris Object `Total Control`
55. Verifikasi badge titik tampil pada icon Filter selama filter ter-Apply
56. Klik icon Filter
57. Verifikasi icon Filter gelap saat panel terbuka
58. Klik `[Clear Field]`, lalu klik `[Apply]`
59. Klik icon Filter, pilih Name `Target Beta {runId}-097`, klik `[Apply]`
60. Verifikasi sedikitnya satu baris tampil di tabel
61. Verifikasi tabel hanya memuat baris Name `Target Beta {runId}-097`
62. Verifikasi badge titik tampil pada icon Filter selama filter ter-Apply
63. Klik icon Filter
64. Verifikasi icon Filter gelap saat panel terbuka
65. Klik `[Clear Field]`, lalu klik `[Apply]`
66. Klik icon Filter, pilih Field `Position`, klik `[Apply]`
67. Verifikasi sedikitnya satu baris tampil di tabel
68. Verifikasi tabel hanya memuat baris Field `Position`
69. Verifikasi badge titik tampil pada icon Filter selama filter ter-Apply
70. Klik icon Filter
71. Verifikasi icon Filter gelap saat panel terbuka
72. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-601: Dua opsi dalam satu field filter digabung OR

73. Klik icon Filter, pilih Action `Create` dan `Delete`, klik `[Apply]`
74. Verifikasi tabel memuat baris Action `Create`
75. Verifikasi tabel memuat baris Action `Delete`
76. Verifikasi baris Action `Edit` tidak tampil
77. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-605: Filter date range

78. Klik icon Filter, pilih rentang tanggal yang memuat hari uji pada Date
79. Verifikasi tanggal di input Date mengikuti Date Format General Settings
80. Klik `[Apply]`
81. Verifikasi baris Action `Create` Name `Target Alfa {runId}-097` (entri hari uji) tampil
82. Klik icon Filter, pilih rentang tanggal 1 Jan 2020 sampai 31 Jan 2020 pada Date
83. Klik `[Apply]`
84. Verifikasi pesan `No results found`
85. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-606: Kombinasi dua field filter digabung AND

86. Klik icon Filter, pilih Action `Create` dan Name `Target Beta {runId}-097`, klik `[Apply]`
87. Verifikasi baris Action `Create` Name `Target Beta {runId}-097` tampil
88. Verifikasi baris Action `Create` Name `Target Alfa {runId}-097` tidak tampil
89. Verifikasi baris Action `Delete` Name `Target Beta {runId}-097` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `Siti Nurhaliza` sebagai pemilik System Log; isi log user itu bergantung pada aksi spec lain. Spec memakai user milik spec (`Aktor Log`) dengan aksi seed yang diketahui (S-06, S-11).
- Urutan TC dalam spec: TC-GS-USER-598, 599, 602, 603, 604, 600, 601, 605, 606. Alasan: screening (598, 599) di awal; TC-GS-USER-602, 603, 604 tidak memakai `[Apply]` sehingga memakai satu pembukaan Filter Panel (langkah 4) dan hanya mengosongkan field di antara kasus; TC-GS-USER-600, 601, 605, 606 memakai `[Apply]` yang menutup panel dan membuka panel kembali sebelum tiap kasus.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 sampai 3 (membuka User Detail; Name dicari di User List), langkah 29 (mengosongkan kotak search dropdown), langkah 37 dan 44 (`[Clear Field]` sebelum kasus berikutnya), serta langkah 77 dan 85 (melepas filter sebelum kasus berikutnya). Langkah 51, 58, 65, 72 adalah langkah TC-GS-USER-600 (`[Clear Field]` + `[Apply]` tiap field).
- Langkah 13, 16, 19, 22 (nilai tanpa baris tidak tampil) didahului `Verifikasi` daftar opsi utuh pada dropdown yang sama sebagai anchor positif (bagian 8b butir 2). Langkah 26 didahului langkah 25 (opsi `Create` tampil) dan langkah 12 (opsi `Delete` ada sebelum disaring). Langkah 88 dan 89 didahului langkah 87 (baris yang memenuhi kedua kriteria tampil).
- Pada TC-GS-USER-600 tiap field: `Verifikasi sedikitnya satu baris tampil di tabel` adalah pembanding sebelum asersi "hanya" (S-03, bagian 8b butir 2); sesudah `Verifikasi` badge titik (filter ter-Apply, panel tertutup), `Klik icon Filter` membuka panel kembali untuk `Verifikasi icon Filter gelap saat panel terbuka`, lalu `[Clear Field]` dan `[Apply]` (langkah TC).
- Langkah 81 (baris entri hari uji tampil) adalah anchor positif untuk `Verifikasi` `No results found` pada langkah 84 (rentang Januari 2020), sehingga hasil kosong bukan karena tabel belum dimuat.
- Asersi memakai pola baris (bukan jumlah baris), sehingga entri log dari run atau spec lain tidak memengaruhi hasil.
- Spec melewati sekitar 35 langkah (89 langkah) karena sembilan TC memakai Filter Panel yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01), termasuk empat field pada TC-GS-USER-599 dan 600. Semua blok satu kelas (Filter Panel Tab System Log), satu akun, satu dataset, dan tiap blok berdiri sendiri karena filter dilepas di akhir tiap blok.
- Pembagian TC lintas spec: Search Tab System Log TC-GS-USER-591 sampai 597 diverifikasi di spec 096; kombinasi Search dan Filter TC-GS-USER-607 sampai 611 di spec 098.
- Temuan untuk QA: (1) TC-GS-USER-600 Expected "icon Filter gelap saat panel terbuka; badge titik tampil selama filter ter-Apply" tidak menyebut cara mengamati; cara membaca state icon Filter dan badge disediakan tim FE. (2) TC-GS-USER-602 Expected b "tidak ada opsi cocok" tidak menyebut teks empty state dropdown; spec hanya mengasersi tidak ada opsi tampil. (3) TC-GS-USER-603 "chip pertama" tidak mendefinisikan urutan; spec memakai opsi yang dipilih pertama (`Create`). (4) TC-GS-USER-605 Data Uji "Rentang tanggal sesuai data" dan judul "per field" tidak menyebut rentang; spec memakai rentang hari uji dan 1 Jan 2020 sampai 31 Jan 2020, dan hanya field Date yang bertipe rentang. (5) TC-GS-USER-606 "Isi 2 field filter berbeda" tidak menyebut field; spec memakai Action `Create` dan Name `Target Beta`. (6) TC-GS-USER-599 "nilai tanpa baris" tidak menyebut contoh; spec memakai `Pair TAG`, `Non-Login User`, dan `Photo`. (7) TC-GS-USER-598 memakai Date sebagai field filter; cara mengisi date range picker disediakan tim FE.
