---
id: TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Tab Changelog Detail: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang, AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-558
  - TC-GS-USER-559
  - TC-GS-USER-562
  - TC-GS-USER-563
  - TC-GS-USER-564
  - TC-GS-USER-560
  - TC-GS-USER-561
  - TC-GS-USER-565
  - TC-GS-USER-566
coverage:
  web: automated
---

# Tab Changelog Detail: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang, AND)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, tampil `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` spec ini; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role Full CRUD (Fajar Nugroho, tampil `Fajar N`) `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4; kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`). Dipakai hanya untuk membuat entri Changelog dengan Modified By kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Data Pre-setup yang dipakai (hanya dibaca, tidak diubah; S-06): Position `Staff`, `Supervisor`, `Finance Manager`, dan `Internal Auditor` (Tabel Data Uji Pre-setup No. 22) dan Client PT Maju Bersama dengan subscription Fixed Asset + Supply Asset (No. 26). John Doe (No. 18) yang disebut TC tidak dipakai: riwayat Changelog-nya tidak dijamin memuat sedikitnya dua nilai distinct pada kolom yang diuji (S-11) dan data Pre-setup tidak diubah (S-06), sehingga spec memakai user uji milik spec.
- Data Dinamis (user uji milik spec, seeding lewat API di hook `before`; kemampuan seeding user lewat API disediakan tim FE/BE, endpoint tidak disebut di TC dan PRD):
  - User uji: Name `Log User {runId}-091`, Email `loguser+{runId}-091@qwertysystem.net`, Position `Staff`, Employee ID `{empId1}`, Access `Fixed Asset`, Active. `{empId1}`, `{empId2}`, `{empId3}` adalah tiga Employee ID numerik, naik berurutan (`{empId1}` < `{empId2}` < `{empId3}`), unik per run, diturunkan dari `{runId}` (hanya digit timestamp) dan memuat nomor spec (S-12): `{empId1}` = `{runId}0911`, `{empId2}` = `{runId}0912`, `{empId3}` = `{runId}0913`.
  - Entri Changelog base (12 entri, urutan seeding = urutan waktu, dari terlama ke terbaru; Modified By tampil `[First Name] [Last Initial]`):
    - a. `Create` | `Name` | `—` | `Log User {runId}-091` | `Siti N`
    - b. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - c. `Edit` | `Employee ID` | `{empId1}` | `{empId2}` | `Siti N`
    - d. `Deactivate` | `Status (Global)` | `Active` | `Inactive` | `Siti N`
    - e. `Activate` | `Status (Global)` | `Inactive` | `Active` | `Siti N`
    - f. `Add Access` | `App Access` | `—` | `Supply Asset` | `Siti N`
    - g. `Remove Access` | `App Access` | `Supply Asset` | `—` | `Siti N`
    - h. `Edit` | `Position` | `Supervisor` | `Finance Manager` | `Fajar N`
    - i. `Edit` | `Position` | `Finance Manager` | `Staff` | `Fajar N`
    - j. `Edit` | `Employee ID` | `{empId2}` | `{empId3}` | `Fajar N`
    - k. `Edit` | `Position` | `Staff` | `Internal Auditor` | `Fajar N`
    - l. `Edit` | `Position` | `Internal Auditor` | `Supervisor` | `Fajar N`
  - Pelaku entri: `Siti N` lewat sesi API Total Control, `Fajar N` lewat sesi API Fajar Nugroho. Dengan demikian kolom Modified By memuat dua nilai distinct (`Siti N`, `Fajar N`); kolom Action, Field, Old Value, dan New Value memuat sedikitnya dua nilai distinct (S-11).
- Kemampuan teknis yang disediakan tim FE/BE (TC, PRD, dan LLD tidak memberi cara): memberi cap waktu pada entri seed sehingga setiap entri berjarak sedikitnya 1 menit dari entri sebelumnya mengikuti urutan huruf di atas, dan entri a (`Create`) bercap tanggal hari uji dikurangi 2 hari (H-2) sedangkan entri lain bercap hari uji. Cap waktu ini membuat urutan Date deterministik (entri terbaru di atas) dan memberi dua nilai distinct pada kolom Date.
- Kemampuan teknis: klik header kolom dan icon di toolbar tabel; mengetik di kotak Search dan dropdown Filter; memilih rentang pada date range picker Date (H-2 sampai H-2); mengamati state icon Filter (gelap saat panel terbuka) dan badge titik; menyalin teks sel.
- Konfigurasi kolom Tab Changelog akun Total Control dalam keadaan default (6 kolom tampil, tanpa pin) saat spec dimulai; hook `before` mengosongkan konfigurasi kolom Tab Changelog bila perlu (mekanisme disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user uji `Log User {runId}-091` lewat API. Entri Changelog tidak bisa dihapus.
- Precondition TC-GS-USER-558, 559, 560, 561, 562, 563, 564, 565, 566: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tersedia; user uji punya riwayat Changelog.
- Suite serial (`parallel: false`) karena spec membaca dan mengubah konfigurasi kolom Tab Changelog di browser yang sama dengan spec lain.
- State global yang diubah dan dipulihkan: tidak ada yang bertahan; visibilitas kolom yang diubah di dalam spec dikembalikan lewat langkah, dan hook `after` memulihkan konfigurasi kolom Tab Changelog ke nilai awal sebagai cadangan.

## Test Steps

### TC-GS-USER-558: Screening Filter Panel

1. Klik icon Search di User List, ketik `Log User {runId}-091`, tekan Enter
2. Klik Name `Log User {runId}-091` di User List
3. Klik Tab `Changelog`
4. Klik icon Filter
5. Verifikasi field `Action`: multi-select searchable dengan placeholder `All actions`
6. Verifikasi field `Field`: multi-select searchable dengan placeholder `All fields`
7. Verifikasi field `Modified By`: multi-select searchable dengan placeholder `All users`
8. Verifikasi field `Date`: date range picker dengan placeholder `Select date`
9. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-559: Opsi dropdown filter diambil dari nilai yang ada di tabel

10. Buka dropdown Action
11. Verifikasi opsi dropdown Action: `Activate`, `Add Access`, `Create`, `Deactivate`, `Edit`, dan `Remove Access`
12. Verifikasi opsi `Delete` tidak ada di dropdown Action (tidak ada baris dengan nilai itu)
13. Tutup dropdown Action
14. Buka dropdown Field
15. Verifikasi opsi dropdown Field: `Name`, `Position`, `Employee ID`, `Status (Global)`, dan `App Access`
16. Verifikasi opsi `Photo` tidak ada di dropdown Field (tidak ada baris dengan nilai itu)
17. Tutup dropdown Field
18. Buka dropdown Modified By
19. Verifikasi opsi dropdown Modified By: `Siti N`, `Fajar N`, dan `System`
20. Tutup dropdown Modified By

### TC-GS-USER-562: Search di dalam dropdown filter mempersempit opsi

21. Buka dropdown Action
22. Ketik `ACTIV` pada search dropdown Action
23. Verifikasi opsi `Activate` tampil
24. Verifikasi opsi `Deactivate` tampil
25. Verifikasi opsi `Create` tidak tampil (opsi tersaring substring tanpa membedakan huruf besar kecil)
26. Ganti isi search dropdown Action dengan `zzz`
27. Verifikasi tidak ada opsi cocok pada dropdown Action
28. Kosongkan search dropdown Action, lalu tutup dropdown Action

### TC-GS-USER-563: Hapus chip filter lewat (X) meng-uncheck opsi

29. Pilih opsi `Create` dan `Edit` pada dropdown Action, lalu tutup dropdown Action
30. Verifikasi chip `Create` dan chip `Edit` tampil
31. Klik (X) pada chip pertama (`Create`)
32. Verifikasi chip `Create` hilang
33. Verifikasi chip `Edit` tetap tampil
34. Buka dropdown Action
35. Verifikasi checkbox opsi `Create` ter-uncheck
36. Tutup dropdown Action, lalu klik `[Clear Field]`

### TC-GS-USER-564: Uncheck opsi di dropdown menghapus chip

37. Pilih opsi `Create` dan `Edit` pada dropdown Action
38. Uncheck opsi kedua (`Edit`) di dropdown Action yang masih terbuka
39. Verifikasi chip `Edit` hilang
40. Verifikasi chip `Create` tetap tampil
41. Tutup dropdown Action, lalu klik `[Clear Field]`

### TC-GS-USER-560: Filter multi-select per field menyaring baris

42. Pilih opsi `Deactivate` pada Action, lalu klik `[Apply]`
43. Verifikasi sedikitnya satu baris tampil di tabel
44. Verifikasi tabel hanya memuat baris Action `Deactivate`
45. Verifikasi badge titik tampil pada icon Filter selama filter ter-Apply
46. Klik icon Filter
47. Verifikasi icon Filter gelap saat panel terbuka
48. Klik `[Clear Field]`, lalu klik `[Apply]`
49. Klik icon Filter, pilih opsi `Employee ID` pada Field, lalu klik `[Apply]`
50. Verifikasi sedikitnya satu baris tampil di tabel
51. Verifikasi tabel hanya memuat baris Field `Employee ID`
52. Verifikasi badge titik tampil pada icon Filter selama filter ter-Apply
53. Klik icon Filter
54. Verifikasi icon Filter gelap saat panel terbuka
55. Klik `[Clear Field]`, lalu klik `[Apply]`
56. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, lalu klik `[Apply]`
57. Verifikasi sedikitnya satu baris tampil di tabel
58. Verifikasi tabel hanya memuat baris Modified By `Fajar N`
59. Verifikasi badge titik tampil pada icon Filter selama filter ter-Apply
60. Klik icon Filter
61. Verifikasi icon Filter gelap saat panel terbuka
62. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-561: Dua opsi dalam satu field filter digabung OR

63. Klik icon Filter, pilih opsi `Create` dan `Activate` pada Action, lalu klik `[Apply]`
64. Verifikasi tabel memuat baris Action `Create`
65. Verifikasi tabel memuat baris Action `Activate`
66. Verifikasi tidak ada baris Action `Edit`
67. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-565: Filter date range per field

68. Klik icon Filter, pilih rentang tanggal pada Date dari H-2 sampai H-2 (tanggal entri `Create`), lalu klik `[Apply]`
69. Verifikasi sedikitnya satu baris tampil di tabel
70. Verifikasi tabel hanya memuat baris dalam rentang (baris Action `Create`, Field `Name`)
71. Verifikasi baris Action `Edit` tidak tampil
72. Klik icon Filter
73. Verifikasi tanggal pada input Date mengikuti Date Format General Settings
74. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-USER-566: Kombinasi dua field filter digabung AND

75. Klik icon Filter, pilih opsi `Edit` pada Action dan opsi `Siti N` pada Modified By, lalu klik `[Apply]`
76. Verifikasi sedikitnya satu baris tampil di tabel
77. Verifikasi tabel hanya memuat baris Action `Edit` dengan Modified By `Siti N`
78. Verifikasi baris Action `Edit` dengan Modified By `Fajar N` tidak tampil
79. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-558, 559, 562, 563, 564, 560, 561, 565, 566. Alasan: TC-GS-USER-558 dan 559 hanya mengamati (screening di awal, bagian 3 konvensi); TC-GS-USER-562, 563, dan 564 hanya memakai panel tanpa `[Apply]` sehingga tabel tetap utuh; TC-GS-USER-560, 561, 565, dan 566 menerapkan filter dan dibersihkan di akhir tiap blok. Detail user dan Tab `Changelog` dibuka sekali di langkah 1 sampai 3.
- Langkah 1 sampai 3 (mencari user uji lewat Search User List, lalu klik Name dan Tab `Changelog`) adalah langkah penghubung tanpa `Verifikasi`; TC menulis "Klik Name `John Doe`" tanpa cara menemukan baris, dan user uji milik spec menggantikan John Doe (lihat Prerequisites).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): menutup dropdown, mengosongkan search dropdown, `[Clear Field]` setelah TC-GS-USER-563 dan 564 (tanpa `[Apply]` karena filter belum diterapkan), serta "Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`" setelah tiap filter yang diterapkan pada TC-GS-USER-560, 561, dan 566. Pembersihan filter pada TC-GS-USER-560 dan 565 adalah langkah TC ("lalu clear"; `[Clear Field]` + `[Apply]`).
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` chip `Create` dan `Edit` tampil (TC-GS-USER-563) adalah anchor sebelum chip dihapus; `Verifikasi` ketiadaan baris `Edit` (TC-GS-USER-561 dan 565), baris Modified By `Fajar N` (TC-GS-USER-566), dan ketiadaan opsi `Delete` dan `Photo` (TC-GS-USER-559) membuktikan pembatasan, didahului `Verifikasi` pembanding pada surface yang sama (bagian 8b butir 2).
- Pada TC-GS-USER-560 tiap field: `Verifikasi sedikitnya satu baris tampil di tabel` adalah pembanding sebelum asersi "hanya" (S-03, bagian 8b butir 2); sesudah `Verifikasi` badge titik (filter ter-Apply, panel tertutup), `Klik icon Filter` membuka panel kembali untuk `Verifikasi icon Filter gelap saat panel terbuka`, lalu `[Clear Field]` dan `[Apply]` (langkah TC).
- Anchor positif (bagian 8b butir 2): `Verifikasi sedikitnya satu baris tampil di tabel` juga mendahului asersi "hanya" pada TC-GS-USER-565 dan 566.
- Rentang Date pada TC-GS-USER-565 memakai H-2 (tanggal entri `Create`); seluruh entri lain bertanggal hari uji sehingga rentang itu hanya mencocokkan entri `Create`.
- Pembagian TC Tab Changelog di User Detail: Filter Panel di spec 091; Search di spec 090; kombinasi Search dan Filter di spec 092.
- Spec melewati sekitar 35 langkah (79 langkah) karena sembilan TC memakai Filter Panel Tab Changelog pada dataset dan layar yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); semua blok satu kelas harness (Filter Panel Tab Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena filter dibersihkan di akhir tiap blok.
- Temuan untuk QA: (1) Cap waktu entri Changelog (entri `Create` H-2, jarak sedikitnya 1 menit antar entri) tidak punya cara di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE (S-13). (2) Label Field Changelog untuk perubahan Employee ID tidak disebut eksplisit (PRD user.md §8.3 hanya menulis `[Field]`); spec memakai `Employee ID`. (3) TC-GS-USER-559 Expected c menyebut dropdown Modified By memuat nilai yang muncul di tabel ditambah opsi `System`; spec mengasersi `Siti N`, `Fajar N`, dan `System` (user uji tidak punya entri bermodifier `System`, sehingga `System` berasal dari opsi tetap). (4) TC-GS-USER-560 Expected "icon Filter gelap saat panel terbuka; badge titik tampil selama filter ter-Apply" tidak menyebut cara mengamati warna dan badge; kemampuan membaca state icon Filter dan badge disediakan tim FE. (5) TC-GS-USER-561 dan 566 tidak menyebut opsi dan field yang dipilih; spec memilih `Create`/`Activate` (OR) dan `Edit`/`Siti N` (AND). (6) TC-GS-USER-565 Data Uji "rentang tanggal sesuai data" tidak menyebut rentang; spec memakai H-2. (7) TC-GS-USER-563 Expected b tidak menyebut apakah opsi kedua tetap ter-check; spec hanya mengasersi opsi pertama ter-uncheck.

