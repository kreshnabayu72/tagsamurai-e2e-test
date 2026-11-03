---
id: TC-AC-ACC-E2E-030-role-matrix-visibilitas-aksi-manage-active-client
title: "Role Matrix: Visibilitas Elemen dan Aksi untuk Role Manage Active Client (Read, Create, Update, Delete, Full)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-49
  - TC-AC-ACC-50
  - TC-AC-ACC-51
  - TC-AC-ACC-52
  - TC-AC-ACC-64
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen dan Aksi untuk Role Manage Active Client (Read, Create, Update, Delete, Full)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-04 | Active-Read (Manage active client: Read, exact-match Area Jakarta) | `activeReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_READ_PASSWORD` |
| A-05 | Active-Create-Only (Manage active client: Create + Read, exact-match Area Jakarta) | `activeCreateJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_CREATE_PASSWORD` |
| A-06 | Active-Update-Only (Manage active client: Update + Read, exact-match Area Jakarta) | `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_UPDATE_PASSWORD` |
| A-07 | Active-Delete-Only (Manage active client: Delete + Read, exact-match Area Jakarta dan Cabang Menteng) | `activeDeleteJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_DELETE_PASSWORD` |
| A-15 | Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng) | `activeFullJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` |

- Login di hook `before` spec ini (Active-Read, A-04); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Pre-setup `C-01` `PT Sejahtera Abadi` (Active, Default User Activated, Station `Gerbang Gudang A` dengan Tablet `Tablet Lobi 1` Active) dan fixture A3 residen `C-ROL-13` `PT Direct Jakarta` (Direct, Group `Area Jakarta`, belum pernah memiliki subscription) hanya dibaca. Pilihan baris dan Search yang diubah spec dipulihkan dalam spec.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-49: Manage active client Read-only

1. Lihat sub-tab List
2. Verifikasi sub-tab `Active` dan `Suspended` tampil dan `Active` terpilih awal
3. Verifikasi sub-tab `Archived` Hidden (bukan disabled) dan badge jumlahnya tidak tampil
4. Ketik Search `PT Sejahtera Abadi`, tekan Enter
5. Lihat toolbar, kolom Checkbox, dan `⋯` baris di sub-tab `Active`
6. Verifikasi `[+ New Client]` Hidden
7. Verifikasi kolom Checkbox dan Bulk Action Bar Hidden (aktor tanpa Update tidak punya aksi bulk)
8. Buka `⋯` baris `PT Sejahtera Abadi`
9. Verifikasi menu `⋯` hanya memuat `Detail`
10. Verifikasi `Download` dan `Changelog` tampil
11. Tutup menu `⋯` dan klik `(←)` pada kotak Search
12. Logout dari akun Active-Read
13. Login sebagai Active-Create-Only (A-05)

### TC-AC-ACC-50: Manage active client Create-Only

14. Lihat sub-tab List
15. Verifikasi sub-tab `Active` dan `Suspended` tampil dan `Active` terpilih awal
16. Verifikasi sub-tab `Archived` Hidden (bukan disabled) dan badge jumlahnya tidak tampil
17. Ketik Search `PT Sejahtera Abadi`, tekan Enter
18. Lihat toolbar, kolom Checkbox, dan `⋯` baris `PT Sejahtera Abadi` di sub-tab `Active`
19. Verifikasi `[+ New Client]` tampil
20. Verifikasi kolom Checkbox dan Bulk Action Bar Hidden
21. Buka `⋯` baris `PT Sejahtera Abadi`
22. Verifikasi `Edit`, `Suspend`, `Unsuspend`, `Change Partner`, dan `Delete` Hidden (hanya `Detail` tersedia)
23. Tutup menu `⋯`
24. Klik Company Name `PT Sejahtera Abadi` untuk membuka Detail
25. Cari toggle `Allow Self-Purchased Device Activation` pada Detail
26. Verifikasi toggle `Allow Self-Purchased Device Activation` Hidden
27. Kembali ke List dengan tombol Back browser dan klik `(←)` pada kotak Search
28. Logout dari akun Active-Create-Only
29. Login sebagai Active-Update-Only (A-06)

### TC-AC-ACC-51: Manage active client Update-Only

30. Lihat sub-tab List
31. Verifikasi sub-tab `Active` dan `Suspended` tampil dan `Active` terpilih awal
32. Verifikasi sub-tab `Archived` Hidden (bukan disabled) dan badge jumlahnya tidak tampil
33. Ketik Search `PT Sejahtera Abadi`, tekan Enter
34. Lihat toolbar dan `⋯` baris `PT Sejahtera Abadi` di sub-tab `Active`
35. Verifikasi `[+ New Client]` Hidden dan kolom Checkbox tampil
36. Buka `⋯` baris `PT Sejahtera Abadi`
37. Verifikasi menu `⋯` memuat `Detail`, `Edit`, `Change Partner`, dan `Suspend`
38. Verifikasi `Delete` Hidden
39. Tutup menu `⋯`
40. Centang baris `PT Sejahtera Abadi`
41. Klik Bulk Action
42. Verifikasi Bulk Action Bar tampil
43. Verifikasi menu Bulk Action memuat `Suspend` (tanpa `Unsuspend` karena baris terpilih berstatus Active)
44. Tutup menu Bulk Action dan hapus centang baris `PT Sejahtera Abadi`
45. Klik Company Name `PT Sejahtera Abadi` untuk membuka Detail (Active, Default User Activated)
46. Verifikasi `[Edit]` dan toggle `Allow Self-Purchased Device Activation` tampil
47. Verifikasi `[Resend Activation Email]` Hidden karena Default User sudah Activated
48. Buka Tab Asset Control
49. Verifikasi `[Generate Enrollment QR]` tampil
50. Klik baris Station `Gerbang Gudang A` untuk expand Tablet List
51. Lihat row action Station `Gerbang Gudang A` dan Tablet `Tablet Lobi 1`
52. Verifikasi row action `Deactivate` pada Station `Gerbang Gudang A` (Active) tampil
53. Verifikasi row action `Revoke` pada Tablet `Tablet Lobi 1` (Active) tampil
54. Kembali ke List dengan tombol Back browser dan klik `(←)` pada kotak Search
55. Logout dari akun Active-Update-Only
56. Login sebagai Active-Delete-Only (A-07)

### TC-AC-ACC-52: Manage active client Delete-Only

57. Lihat sub-tab List
58. Verifikasi sub-tab `Active` dan `Suspended` tampil dan `Active` terpilih awal
59. Verifikasi sub-tab `Archived` Hidden (bukan disabled) dan badge jumlahnya tidak tampil
60. Ketik Search `PT Direct Jakarta`, tekan Enter
61. Buka `⋯` baris `PT Direct Jakarta` di sub-tab `Active`
62. Verifikasi menu `⋯` `PT Direct Jakarta` memuat `Detail` dan `Delete`
63. Verifikasi `Edit`, `Suspend`, dan `Change Partner` Hidden pada baris `PT Direct Jakarta`
64. Tutup menu `⋯`
65. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
66. Buka `⋯` baris `PT Sejahtera Abadi` di sub-tab `Active`
67. Verifikasi menu `⋯` `PT Sejahtera Abadi` hanya memuat `Detail` (Delete Hidden karena sudah pernah memiliki subscription)
68. Verifikasi `Edit`, `Suspend`, dan `Change Partner` Hidden pada baris `PT Sejahtera Abadi`
69. Tutup menu `⋯`
70. Lihat toolbar dan kolom Checkbox
71. Verifikasi kolom Checkbox Hidden
72. Klik `(←)` pada kotak Search
73. Logout dari akun Active-Delete-Only
74. Login sebagai Active-Full (A-15)

### TC-AC-ACC-64: Link Manage in Client Subscription hanya untuk pemegang Read Manage allocation

75. Ketik Search `PT Sejahtera Abadi`, tekan Enter
76. Klik Company Name `PT Sejahtera Abadi` untuk membuka Detail
77. Buka Tab Subscription
78. Verifikasi konten Tab Subscription tampil
79. Verifikasi link `[Manage in Client Subscription →]` dan info banner tidak tampil (aktor tanpa akses membuka Client Subscription)
80. Kembali ke List dengan tombol Back browser dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 4, 11 sampai 13, 17, 23, 27 sampai 29, 33, 39, 44, 54 sampai 56, 60, 64, 65, 69, 72 sampai 75, 80. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Spec Role Matrix per blok role (bagian 3a): langkah tiap role berbeda dan ganti akun menuntut Step eksplisit; login akun pertama (Active-Read, A-04) dilakukan hook `before`.
- Penyimpangan urutan (S-05): TC-AC-ACC-49, 50, 51, 52, 64 (semula 49, 50, 51, 52, 64); tidak ada perubahan urutan TC sumber.
- Baris contoh untuk `⋯` pada TC-AC-ACC-49 sampai 51 tidak disebut TC; spec memakai `PT Sejahtera Abadi` yang dipakai TC-AC-ACC-50 dan 51 untuk baris yang sama.
- Pembagian TC lintas spec: role Manage archived client di spec 031; Group Manager di spec 032; Total Control dan Read Only di spec 028; role silang Active/Archived (defense) di spec 034.
- Ukuran spec (80 langkah, melewati sekitar 35 langkah): Role Matrix per blok role (lima role; langkah berbeda) pada satu dataset; tiap blok dimulai dari ganti akun eksplisit dan Search eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-49: langkah 2 "buka ⋯ baris di sub-tab Active" tidak menyebut Client; spec memakai `PT Sejahtera Abadi` (sama dengan TC-AC-ACC-50).
  - TC-AC-ACC-51: Expected butir d menyebut `[Resend Activation Email]` Hidden karena Default User Activated; spec mengasersi pada `PT Sejahtera Abadi` (Default User Activated).
