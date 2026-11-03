---
id: TC-AC-SU-E2E-057-role-matrix-sub-tab-group-role-per-aktor
title: "Role Matrix: Sub-tab Group Role dan Global Role per Aktor (MUR, Read Only, MUR Tanpa Update)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-208
  - TC-AC-SU-261
  - TC-AC-SU-210
  - TC-AC-SU-211
coverage:
  web: automated
---

# Role Matrix: Sub-tab Group Role dan Global Role per Aktor (MUR, Read Only, MUR Tanpa Update)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user and role (Update aktif), `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Akun kedua (ganti akun eksplisit): un aktor pertama: Read Only, `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Akun ketiga (ganti akun eksplisit): un aktor pertama: Manage user and role (Read saja, U=false), `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_READ_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Rina Putri {runId}-057` (tingkat akses Total Control, TC-208 dan TC-261), `Budi Santoso {runId}-057` tanpa tingkat akses dan bukan Group Manager dengan `Manage active client` aktif di `Region A {runId}-057` (TC-210, TC-211).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-057`): `Region A {runId}-057` > `Branch 1 {runId}-057` > `Floor 1 {runId}-057`; `Region A {runId}-057` > `Branch 3 {runId}-057`; `Region B {runId}-057`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-057@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-057`.
- Tabel "Role yang diuji": Manage user and role (Update aktif) pada target Total Control (TC-208, TC-261); Read Only (TC-210); Manage user and role (Read saja, U=false) (TC-211). Langkah tiap role berbeda sehingga spec ditulis per blok role.
- Env var `AC_MUR_UPDATE_PASSWORD` dan `AC_MUR_READ_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan pemilik repo.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-057` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-208: Aktor Manage user and role pada target Total Control: Assign Group Disabled, Detail enabled

1. Ketik Search `Rina Putri {runId}-057`, tekan Enter
2. Klik nama `Rina Putri {runId}-057` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Hover `[Assign Group]` baris `Manage active client`
5. Verifikasi `[Assign Group]` baris `Manage active client` tampil namun disabled
6. Verifikasi tooltip `"You don't have permission to edit."` pada `[Assign Group]`
7. Hover `[Detail]` baris `Manage active client`
8. Verifikasi `[Detail]` baris `Manage active client` tampil dan enabled

### TC-AC-SU-261: Auto-Revert tidak tersedia bagi aktor Manage user and role

9. Klik Sub-tab [Global Role]
10. Coba klik checkbox D baris `Manage TAG stock`
11. Verifikasi checkbox D baris `Manage TAG stock` disabled
12. Verifikasi dialog Auto-Revert tidak pernah muncul

### TC-AC-SU-210: Aktor Read Only: Sub-tab Group Role

13. Logout dari akun Manage user and role (Update aktif)
14. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
15. Buka Settings > User lewat sidebar
16. Ketik Search `Budi Santoso {runId}-057`, tekan Enter
17. Klik nama `Budi Santoso {runId}-057` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
18. Klik Sub-tab [Group Role]
19. Amati kolom Actions
20. Verifikasi Sub-tab Group Role tanpa switch
21. Verifikasi `[Detail]` tampil dan enabled
22. Verifikasi `[Assign Group]` Hidden
23. Klik `[Detail]` baris `Manage active client`
24. Verifikasi popup Group Assignment terbuka (read-only)
25. Tutup popup dengan `[×]`

### TC-AC-SU-211: Aktor Manage user and role tanpa Update: Assign Group Hidden

26. Logout dari akun Read Only
27. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
28. Buka Settings > User lewat sidebar
29. Ketik Search `Budi Santoso {runId}-057`, tekan Enter
30. Klik nama `Budi Santoso {runId}-057` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
31. Klik Sub-tab [Group Role]
32. Amati kolom Actions
33. Verifikasi `[Detail]` tampil dan enabled
34. Verifikasi `[Assign Group]` Hidden
35. Logout dari akun Manage user and role (Read saja) dan login kembali sebagai akun default suite (Total Control)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 16, 25, 29, 35 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Spec Role Matrix ditulis per blok role (bagian 3a): langkah tiap role berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- TC-AC-SU-261 (aktor Manage user and role pada Global Role target Total Control) ditaruh di blok role yang sama dengan TC-208 karena aktor dan target identik.
- Urutan TC di spec: 208, 261, 210, 211 (per blok role).
- Temuan untuk QA:
  - TC-261 menyebut "Coba klik checkbox D baris Manage TAG stock" tanpa menyebut Sub-tab Global Role; spec menambah langkah pindah ke Sub-tab [Global Role].
