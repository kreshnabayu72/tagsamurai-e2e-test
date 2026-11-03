---
id: TC-GS-USER-E2E-161-role-matrix-tab-role-aktor-manage-user-and-role-update-read-dan-diri-sendiri
title: "Role Matrix: Visibilitas Switch Active dan Checkbox Tab Role per Aktor Manage user and role (Update-Only, Read-Only role, dan Akun Sendiri Full CRUD)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-1090
  - TC-GS-USER-1091
  - TC-GS-USER-1108
coverage:
  web: automated
---

# Role Matrix: Visibilitas Switch Active dan Checkbox Tab Role per Aktor Manage user and role (Update-Only, Read-Only role, dan Akun Sendiri Full CRUD)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun (Tabel Data Uji Pre-setup) | Nama user | Env var password | Target dan TC |
|---|---|---|---|---|
| Manage user and role (Update-Only: R+U) | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` (No. 6) | Bayu Saputra | `Spectra.env.GS_UPDATE_PASSWORD` | `Ahmad Fauzi {runId}-161` (Normal) dan `Andi Wijaya {runId}-161` (tier Total Control): TC-GS-USER-1090 |
| Manage user and role (Read-Only role: R saja) | `manageUserRead_automated_{namaCompany}@qwertysystem.net` (No. 8) | Eko Prasetyo | `Spectra.env.GS_READ_PASSWORD` | `Dewi Lestari {runId}-161` (Normal): TC-GS-USER-1091 |
| Manage user and role (Full CRUD) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (No. 4) | Fajar Nugroho | `Spectra.env.GS_FULLCRUD_PASSWORD` | Akun sendiri: TC-GS-USER-1108 |

- Login akun Update-Only (aktor pertama spec) dilakukan di hook `before`; Read-Only role dan Full CRUD memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Full CRUD, hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_UPDATE_PASSWORD`, `GS_READ_PASSWORD`, `GS_FULLCRUD_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after` (padanan Tabel Pre-setup):
  - `Ahmad Fauzi {runId}-161`, email `ahmadfauzi+{runId}-161@qwertysystem.net`: Normal (non-tier), keenam baris Tab Role ada (TC-GS-USER-1090).
  - `Andi Wijaya {runId}-161`, email `andiwijaya+{runId}-161@qwertysystem.net`: tier Total Control (TC-GS-USER-1090).
  - `Dewi Lestari {runId}-161`, email `dewilestari+{runId}-161@qwertysystem.net`: Basic tanpa assignment role (TC-GS-USER-1091).
- Data Pre-setup (diubah tim FE/BE, bukan spec): akun Fajar Nugroho harus memiliki baris `Manage files` dengan switch Active OFF (TC-GS-USER-1108); akun ini dipakai spec lain sehingga kondisinya harus dijaga (perlu dikonfirmasi tim FE).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD): seeding user dengan tier dan assignment role lewat API; hover elemen disabled untuk membaca tooltip.
- State global yang diubah: tidak ada. Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): hapus tiga user seed dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-USER-1090: Aktor Update-Only, switch Active enabled untuk target Normal dan disabled untuk target tier Total Control

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-161`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-161` di User List
3. Klik Tab `Role`
4. Verifikasi switch Active enabled pada keenam baris
5. Klik menu User di sidebar Global Settings
6. Klik icon Search, ketik `Andi Wijaya {runId}-161`, tekan Enter
7. Klik Name `Andi Wijaya {runId}-161` di User List
8. Klik Tab `Role`
9. Hover switch Active baris `Manage files`
10. Verifikasi switch Active baris `Manage files` tampil namun disabled dengan tooltip `"You don't have permission to edit."`

### TC-GS-USER-1091: Aktor Read-Only role, switch dan checkbox disabled dengan tooltip permission

11. Logout, lalu login sebagai Manage user and role (Read-Only role: R saja)
12. Buka Global Settings > User > User List (sub-tab Login User)
13. Klik icon Search, ketik `Dewi Lestari {runId}-161`, tekan Enter
14. Klik Name `Dewi Lestari {runId}-161` di User List
15. Klik Tab `Role`
16. Hover switch Active baris `Manage TAG`
17. Verifikasi switch Active baris `Manage TAG` tampil namun disabled dengan tooltip `"You don't have permission to edit."`
18. Hover checkbox Update baris `Manage TAG`
19. Verifikasi checkbox Update baris `Manage TAG` tampil namun disabled dengan tooltip `"You don't have permission to edit."`

### TC-GS-USER-1108: Akun sendiri, checkbox baris switch OFF memakai tooltip akun sendiri

20. Logout, lalu login sebagai Manage user and role (Full CRUD)
21. Buka Global Settings > User > User List (sub-tab Login User)
22. Klik icon Search, ketik `Fajar Nugroho`, tekan Enter
23. Klik Name `Fajar Nugroho` di User List (Detail akun sendiri)
24. Klik Tab `Role`
25. Hover checkbox Delete baris `Manage files`
26. Verifikasi checkbox Delete baris `Manage files` tampil namun disabled dengan tooltip `"You can't manage your own account from here."`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec ditulis per blok role dengan langkah ganti akun eksplisit (langkah 11 dan 20) karena akun pertama login di hook `before` dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3 kasus (b)); ini matriks visibilitas Tab Role per aktor yang memuat dua polaritas (enabled pada TC-GS-USER-1090 butir a, disabled pada butir lain), sehingga title tanpa kata Positif atau Negatif. Hasil tiap aktor berbeda sehingga langkah tidak diulang lewat perulangan tabel.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 6, 13, dan 22 (Search nama target sebelum Klik Name, R-16), 5 (kembali ke User List), 11 dan 20 (ganti akun), 12 dan 21 (membuka User List sesudah ganti akun).
- Search pada langkah 22 memakai nama akun aktor sendiri (`Fajar Nugroho`, Pre-setup tanpa suffix) karena target TC-GS-USER-1108 adalah akun sendiri.
- Baris dan checkbox yang di-hover (langkah 9, 16, 18) adalah pilihan spec karena TC tidak menyebut baris.
- Temuan untuk QA:
  - TC-GS-USER-1108 (P-6): akun aktor Fajar Nugroho harus memiliki baris `Manage files` dengan switch OFF; Tabel Pre-setup tidak menyebut kondisi itu dan akun dipakai spec lain. Perlu konfirmasi: seed oleh tim FE/BE atau akun klon.
  - TC-GS-USER-1090 langkah 4 "Hover switch Active" tidak menyebut baris; spec memilih `Manage files`.
  - TC-GS-USER-1091 langkah 2 tidak menyebut checkbox mana pada baris `Manage TAG`; spec memilih Update. Target Dewi Lestari (Basic, tanpa assignment) memiliki switch `Manage TAG` OFF sehingga tooltip permission berprioritas atas tooltip switch OFF (TC-GS-USER-1107 dan 1108).
  - TC-GS-USER-1090 Expected a tidak menyebut kondisi switch (ON atau OFF) pada keenam baris; spec mengasersi enabled.
  - TC-GS-USER-1090, 1091 memakai user Pre-setup (Ahmad Fauzi, Andi Wijaya, Dewi Lestari); spec memakai seed milik spec (S-06).
