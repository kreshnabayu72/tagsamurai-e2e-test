---
id: TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list
title: "User Detail: Header, Badge Status, User Type, Info Temporary, Pending Email Change, Tab Role Aktif Default, Edit Profile, serta Retensi State User List lewat Back Browser dan F5"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-356
  - TC-GS-USER-357
  - TC-GS-USER-358
  - TC-GS-USER-359
  - TC-GS-USER-360
  - TC-GS-USER-361
  - TC-GS-USER-362
  - TC-GS-USER-363
  - TC-GS-USER-364
  - TC-GS-USER-1018
  - TC-GS-USER-1054
  - TC-GS-USER-365
  - TC-GS-USER-366
  - TC-GS-USER-273
coverage:
  web: automated
---

# User Detail: Header, Badge Status, User Type, Info Temporary, Pending Email Change, Tab Role Aktif Default, Edit Profile, serta Retensi State User List lewat Back Browser dan F5

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (dibaca, tidak diubah; Tabel Data Uji Pre-setup): John Doe (No. 18; Activated, Position Staff, Employee ID `EMP-0001`), Mike Tan (No. 14; Pending Activation), Rina Putri (No. 15; email pending `rinaputri.new@qwertysystem.net`), Jane Smith (No. 17; Inactive manual), Andi Wijaya (No. 10; Total Control), Doni Pratama (No. 11; Read Only), Ahmad Fauzi (No. 13; User Type Admin), Dewi Lestari (No. 12; Basic, Temporary aktif +30 hari, Position Staff), Division `Finance` (No. 23).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after` (untuk TC-GS-USER-365 dan TC-GS-USER-366 agar halaman 2 ada setelah Search `a` + filter Division `Finance`): sebelas user Activated, Division `Finance`, nama `Aria Uji 01 {runId}-061` sampai `Aria Uji 11 {runId}-061`, email `ariauji01+{runId}-061@qwertysystem.net` sampai `ariauji11+{runId}-061@qwertysystem.net` (email berbeda-beda sehingga sort Email punya nilai distinct). Field wajib lain diisi seadanya oleh seeding.
- Kemampuan teknis (disediakan tim FE/BE): seeding user lewat API (nama endpoint ditentukan tim FE di tahap script); membaca tanggal Temporary Until Dewi Lestari lewat API untuk asersi TC-GS-USER-364 (Tabel Pre-setup hanya menyebut "+30 hari" tanpa tanggal mutlak); tombol Back browser dan F5 dikendalikan skrip.
- State global yang diubah: tidak ada. State UI (Search, Filter, Sort, halaman, ukuran halaman) User List dikosongkan dan dikembalikan ke default di hook `after`; sebelas user seed dihapus di hook `after` tanpa mengandalkan seeding berhasil penuh.

## Test Steps

### Persiapan

1. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-356: Screening halaman User Detail

2. Klik Name `John Doe` di User List
3. Verifikasi Header: breadcrumb `User > Detail` tampil
4. Verifikasi Header: breadcrumb `User > Detail` berupa label statis yang tidak dapat diklik
5. Verifikasi Header Baris 1: Avatar + `John Doe` (kiri) dan switch Active (kanan atas)
6. Verifikasi Header Baris 2: badge `Active` dan menu `[⋯]`
7. Verifikasi Header Baris 2: Button Resend tidak tampil (kondisional; tidak tampil untuk John Doe)
8. Verifikasi Header Baris 3: Employee ID `EMP-0001` (muted)
9. Verifikasi Header Baris 4: `Viewing: [Global Settings ▾]`
10. Verifikasi Body: SectionCard General Information grid 4 kolom: Identity (Position, Division, Email) | Access & Status (User Type badge, daftar product access) | User TAG | Authenticator (MFA)
11. Verifikasi Body: SectionCard Custom Fields (collapsible)
12. Verifikasi Body: Tab `Role | Responsibilities | Non-Login User | Changelog | System Log | User Log`
13. Verifikasi Full Name dan Photo tidak diulang di General Information

### TC-GS-USER-1054: Detail User dibuka dengan tab Role aktif secara default

14. Verifikasi Tab `Role` aktif pada Detail `John Doe` yang sama (langkah 1 TC-GS-USER-1054 dipenuhi langkah 2)
15. Verifikasi konten Tab `Role` tampil
16. Verifikasi Tab `Responsibilities`, `Non-Login User`, `Changelog`, `System Log`, dan `User Log` tidak aktif

### TC-GS-USER-357: Header Detail menampilkan badge Pending Activation bila pending

17. Klik menu User di sidebar Global Settings
18. Klik icon Search, ketik `Mike Tan`, tekan Enter
19. Klik Name `Mike Tan` di User List
20. Verifikasi badge `Active` tampil di Header
21. Verifikasi badge `Pending Activation` tampil di Header

### TC-GS-USER-358: Header Detail menampilkan badge Pending Email Confirmation

22. Klik menu User di sidebar Global Settings
23. Klik icon Search, ketik `Rina Putri`, tekan Enter
24. Klik Name `Rina Putri` di User List
25. Verifikasi badge `Active` tampil di Header
26. Verifikasi badge `Pending Email Confirmation` tampil di Header

### TC-GS-USER-1018: General Information menampilkan teks pending email change read-only

27. Verifikasi Identity di General Information menampilkan teks `Pending email change to rinaputri.new@qwertysystem.net` di bawah Email (langkah 1 TC-GS-USER-1018 dipenuhi langkah 24)
28. Verifikasi teks pending email change tanpa tombol Cancel dan Resend

### TC-GS-USER-359: Header Detail user Inactive menampilkan badge Inactive

29. Klik menu User di sidebar Global Settings
30. Klik icon Search, ketik `Jane Smith`, tekan Enter
31. Klik Name `Jane Smith` di User List
32. Verifikasi badge `Inactive` tampil di Header
33. Verifikasi switch Active di Header OFF

### TC-GS-USER-360: User Type badge `Total Control` di General Information

34. Klik menu User di sidebar Global Settings
35. Klik icon Search, ketik `Andi Wijaya`, tekan Enter
36. Klik Name `Andi Wijaya` di User List
37. Verifikasi Access & Status: User Type badge `Total Control`

### TC-GS-USER-361: User Type badge `Read Only` di General Information

38. Klik menu User di sidebar Global Settings
39. Klik icon Search, ketik `Doni Pratama`, tekan Enter
40. Klik Name `Doni Pratama` di User List
41. Verifikasi Access & Status: User Type badge `Read Only`

### TC-GS-USER-362: User Type badge `Admin` di General Information

42. Klik menu User di sidebar Global Settings
43. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
44. Klik Name `Ahmad Fauzi` di User List
45. Verifikasi Access & Status: User Type badge `Admin`

### TC-GS-USER-363: User Type badge `Basic` di General Information

46. Klik menu User di sidebar Global Settings
47. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
48. Klik Name `Dewi Lestari` di User List
49. Verifikasi Access & Status: User Type badge `Basic`

### TC-GS-USER-364: Info Temporary User di General Information

50. Verifikasi Access & Status menampilkan `Temporary until [tanggal Temporary Until Dewi Lestari]` dengan tanggal dalam format General Settings (langkah 1 TC-GS-USER-364 dipenuhi langkah 48)

### TC-GS-USER-273: Edit Profile dari menu [⋯] header Detail membuka Popup Edit pre-filled

51. Klik `[⋯]` di Header Detail Dewi Lestari (langkah 1 TC-GS-USER-273 dipenuhi langkah 48)
52. Klik `Edit Profile`
53. Verifikasi Popup `Edit User` terbuka
54. Verifikasi Popup `Edit User` pre-filled data Dewi Lestari (nama `Dewi Lestari` dan Position `Staff`)
55. Klik `✕` pada header Popup `Edit User` (form belum diubah)

### TC-GS-USER-365: Kembali dari Detail lewat Back browser mempertahankan state List

56. Klik menu User di sidebar Global Settings
57. Pilih 10 baris per halaman pada Pagination
58. Klik icon Search, ketik `a`, tekan Enter
59. Klik header kolom Email
60. Pindah ke halaman 2
61. Klik Name baris pertama di halaman 2
62. Klik tombol Back browser
63. Verifikasi kotak Search berisi keyword `a`
64. Verifikasi sort kolom Email tetap aktif
65. Verifikasi User List berada di halaman 2

### TC-GS-USER-366: Refresh F5 mempertahankan Search, Sort, Filter, dan halaman User List

66. Klik icon Filter pada toolbar User List (Search `a` dan sort Email sudah aktif dari TC-GS-USER-365)
67. Pilih Division `Finance`
68. Klik `[Apply]`
69. Pindah ke halaman 2
70. Tekan F5
71. Verifikasi kotak Search berisi keyword `a`
72. Verifikasi Filter Division `Finance` tetap aktif
73. Verifikasi sort kolom Email tetap aktif
74. Verifikasi User List berada di halaman 2

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Urutan TC sumber diubah: TC-GS-USER-1054 dan TC-GS-USER-1018 dimajukan masing-masing tepat sesudah TC yang membuka Detail yang sama (TC-GS-USER-356 dan TC-GS-USER-358) agar tidak ada pembukaan Detail ulang; TC-GS-USER-273 diletakkan sesudah TC-GS-USER-364 karena memakai Detail Dewi Lestari yang sama; TC-GS-USER-365 dan TC-GS-USER-366 di akhir karena memakai ukuran halaman 10 dan mengubah state List.
- Spec melewati sekitar 35 langkah (74 langkah, di antaranya 21 langkah pembukaan Detail berulang berupa klik menu User, Search, dan klik Name) karena empat belas TC berada di satu kelas harness (fungsional, baca saja, tanpa aksi yang mengubah data), satu layar (User Detail dan User List), dan tiap blok TC berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (100 baris per halaman agar John Doe tampil tanpa Search), 17 sampai 18, 22 sampai 23, 29 sampai 30, 34 sampai 35, 38 sampai 39, 42 sampai 43, 46 sampai 47, dan 56 (kembali ke User List dan mencari user target), 55 (menutup Popup `Edit User` yang belum diubah lewat `✕`; tanpa dialog `Unsaved Changes` karena form tidak dirty), dan 57 (10 baris per halaman agar halaman 1 ada).
- Asersi absence (langkah 7, 13, 16, dan 28) berada di layar yang sudah menampilkan pembandingnya pada langkah sebelumnya (badge `Active` dan menu `[⋯]` pada langkah 6, General Information pada langkah 10, Tab `Role` aktif pada langkah 14 dan 15, teks pending email pada langkah 27). Spec tidak menambah asersi di luar Expected TC.
- Langkah 1 TC-GS-USER-1018, TC-GS-USER-364, dan TC-GS-USER-273 ("Klik Name" atau "Buka Detail") dipenuhi pembukaan Detail pada langkah 24 dan 48; Search `a` dan sort Email pada langkah 1 TC-GS-USER-366 sudah aktif dari langkah 58 sampai 59.
- Pembagian TC lintas spec: Tab `Role` aktif default (TC-GS-USER-1054) diverifikasi hanya di spec ini; isi Tab Role diverifikasi di spec 063 dan 064.
- Temuan untuk QA:
  - TC-GS-USER-365 dan TC-GS-USER-366 menyebut "pindah ke halaman 2" tanpa ukuran halaman; spec memakai 10 baris per halaman (default) dan mem-seed sebelas user Finance berhuruf `a` agar halaman 2 ada setelah filter Division `Finance`. Tabel Pre-setup tidak menyebut user mana yang berdivisi Finance.
  - TC-GS-USER-365 langkah 2 "Klik Name salah satu baris" tidak menyebut baris; spec memilih baris pertama di halaman 2.
  - TC-GS-USER-364 Expected "Temporary until [tanggal]" tanpa tanggal mutlak (Pre-setup hanya "+30 hari"); tanggal dibaca lewat kemampuan yang disediakan tim FE/BE.
  - TC-GS-USER-273 Expected "pre-filled data Dewi Lestari" tanpa daftar field; spec mengasersi nama dan Position `Staff`.
  - TC-GS-USER-356 Expected b.i tidak menyebut isi Identity per user (nilai Position, Division, Email John Doe); spec mengasersi struktur kolom sesuai TC.
