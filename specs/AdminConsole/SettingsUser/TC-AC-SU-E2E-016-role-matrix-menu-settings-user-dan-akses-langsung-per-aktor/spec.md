---
id: TC-AC-SU-E2E-016-role-matrix-menu-settings-user-dan-akses-langsung-per-aktor
title: "Role Matrix: Menu Settings > User per Aktor, Akses Langsung via URL, dan Row Scope Seluruh User Entitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-51
  - TC-AC-SU-52
  - TC-AC-SU-53
  - TC-AC-SU-55
coverage:
  web: automated
---

# Role Matrix: Menu Settings > User per Aktor, Akses Langsung via URL, dan Row Scope Seluruh User Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User (Pre-setup #1) `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DU_PASSWORD`.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor: Read Only (Pre-setup #3) `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Akun aktor: Manage user and role Read saja (U=false, Pre-setup #5) `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_READ_PASSWORD`.
- Akun aktor: Group Manager tanpa akses modul (Pre-setup #6) `groupManagerAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_GM_PASSWORD`.
- Akun aktor: Manage TAG stock saja (`Rudi Hartono`; tidak ada di Pre-setup, email disediakan tim FE), password `Spectra.env.AC_TS_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD`, `AC_MUR_READ_PASSWORD`, `AC_GM_PASSWORD`, `AC_TS_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Default User (akun aktor pertama); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun | Hasil menu Settings > User |
|---|---|---|---|
| TC-AC-SU-51 | Default User | Pre-setup #1 | tampil |
| TC-AC-SU-51 | Total Control | Pre-setup #2 | tampil |
| TC-AC-SU-51, 55 | Read Only | Pre-setup #3 | tampil; row scope seluruh user |
| TC-AC-SU-51, 55 | Manage user and role (U=true) | Pre-setup #4 | tampil; row scope seluruh user |
| TC-AC-SU-51 | Manage user and role (U=false) | Pre-setup #5 | tampil |
| TC-AC-SU-52, 53 | Group Manager saja (`Dedi Kurnia`, `Region A`) | Pre-setup #6 | tidak dirender; akses langsung ditolak |
| TC-AC-SU-52, 53 | Hanya Global Role `Manage TAG stock` (`Rudi Hartono`) | tidak ada di Pre-setup; email disediakan tim FE | tidak dirender; akses langsung ditolak |

- Total user entitas Principal (TC-AC-SU-55) dibaca lewat Fixture BE sebelum asersi (N total dari seeding, bagian 8b butir 10); jumlah literal `12` dari TC tidak dipakai. Spec tidak men-seed user.
- Kemampuan teknis: URL halaman Settings > User untuk dibuka langsung di address bar (TC-AC-SU-53) disediakan tim FE; Fixture BE dan sesi API aktor disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Blok akun Default User: TC-AC-SU-51 butir a

1. Buka grup Settings pada sidebar
2. Verifikasi Default User: item `User` tampil

### Blok akun Total Control: TC-AC-SU-51 butir b

3. Logout dari akun aktor saat ini
4. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
5. Buka grup Settings pada sidebar
6. Verifikasi Total Control: item `User` tampil

### Blok akun Read Only: TC-AC-SU-51 butir c dan TC-AC-SU-55

7. Logout dari akun aktor saat ini
8. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
9. Buka grup Settings pada sidebar
10. Verifikasi Read Only: item `User` tampil
11. Klik item `User` pada sidebar
12. Verifikasi Read Only: info pagination menampilkan total user sama dengan total user entitas
13. Verifikasi Read Only: tidak ada node Sidebar Group terpilih (tidak ada penyaringan group)

### Blok akun Manage user and role (U=true): TC-AC-SU-51 butir d dan TC-AC-SU-55

14. Logout dari akun aktor saat ini
15. Login sebagai Manage user and role (Update, U=true) (`manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_UPDATE_PASSWORD`)
16. Buka grup Settings pada sidebar
17. Verifikasi Manage user and role (U=true): item `User` tampil
18. Klik item `User` pada sidebar
19. Verifikasi Manage user and role (U=true): info pagination menampilkan total user sama dengan total user entitas
20. Verifikasi Manage user and role (U=true): tidak ada node Sidebar Group terpilih (tidak ada penyaringan group)

### Blok akun Manage user and role (U=false): TC-AC-SU-51 butir e

21. Logout dari akun aktor saat ini
22. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
23. Buka grup Settings pada sidebar
24. Verifikasi Manage user and role (U=false): item `User` tampil

### Blok akun Group Manager (`Dedi Kurnia`): TC-AC-SU-52 butir a dan TC-AC-SU-53

25. Logout dari akun aktor saat ini
26. Login sebagai Group Manager tanpa akses modul (`groupManagerAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_GM_PASSWORD`)
27. Buka grup Settings pada sidebar
28. Verifikasi Group Manager: item lain `Privacy Policy` pada grup Settings tampil
29. Verifikasi Group Manager: item `User` tidak dirender
30. Buka URL halaman Settings > User langsung di address bar
31. Verifikasi toast error `You don't have permission to do this.`
32. Verifikasi data user tidak ditampilkan
33. Verifikasi elemen yang tidak berhak tersembunyi

### Blok akun Manage TAG stock saja (`Rudi Hartono`): TC-AC-SU-52 butir b dan TC-AC-SU-53

34. Logout dari akun aktor saat ini
35. Login sebagai Manage TAG stock saja (email disediakan tim FE, password dari `Spectra.env.AC_TS_PASSWORD`)
36. Buka grup Settings pada sidebar
37. Verifikasi Manage TAG stock saja: item lain `Privacy Policy` pada grup Settings tampil
38. Verifikasi Manage TAG stock saja: item `User` tidak dirender
39. Buka URL halaman Settings > User langsung di address bar
40. Verifikasi toast error `You don't have permission to do this.`
41. Verifikasi data user tidak ditampilkan
42. Verifikasi elemen yang tidak berhak tersembunyi

## Notes

- Langkah penghubung (S-03): langkah 30 dan langkah buka URL berikutnya adalah aksi TC-AC-SU-53; Login Default User di hook `before` sehingga langkah login awal TC-AC-SU-51 tidak diulang. Hook `after` memulihkan sesi ke Default User.
- Alasan memakai blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke butir TC; urutan TC dipecah per akun (S-05) supaya tiap akun dipakai satu kali: urutan akun Default User, Total Control, Read Only, Manage user and role (U=true), Manage user and role (U=false), Group Manager, Manage TAG stock saja.
- Ukuran spec (42 langkah, di atas smell sekitar 35 langkah): Role Matrix dengan tujuh akun; tiap blok akun berdiri sendiri (login eksplisit di awal blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-52 dan TC-AC-SU-53 memakai `Dedi Kurnia` (hanya Group Manager `Region A`) dan `Rudi Hartono` (hanya Global Role `Manage TAG stock`): Pre-setup #6 hanya menyebut Group Manager tanpa akses modul; akun `Rudi Hartono` tidak ada di Tabel Pre-setup (email dan password disediakan tim FE).
  - TC-AC-SU-53 tidak menyebut URL halaman; URL disediakan tim FE. Expected a (toast error) dan b (data tidak ditampilkan; elemen yang tidak berhak tersembunyi) diasersi sebagai tiga `Verifikasi`.
  - TC-AC-SU-55 menyebut "12 user" literal; spec mengasersi total user entitas yang dibaca lewat Fixture BE karena entitas Principal berisi user Pre-setup yang jumlahnya tidak tetap.
  - TC-AC-SU-55 memakai nama aktor `Andi Wijaya` (Read Only) dan `Mike Tan` (Manage user and role) yang tidak dipetakan ke Pre-setup; spec memakai akun Pre-setup #3 dan #4.
