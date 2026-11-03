---
id: TC-AC-SU-E2E-023-role-matrix-assign-group-hidden-disabled-enabled
title: "Role Matrix: Assign Group Hidden untuk Default User dan Self, Disabled untuk Target Total Control atau Read Only, serta Enabled pada Role tanpa Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-68
  - TC-AC-SU-69
  - TC-AC-SU-70
coverage:
  web: automated
---

# Role Matrix: Assign Group Hidden untuk Default User dan Self, Disabled untuk Target Total Control atau Read Only, serta Enabled pada Role tanpa Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor: Read Only (Pre-setup #3) `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-68, 70 | Total Control | Pre-setup #2 |
| TC-AC-SU-70 | Read Only | Pre-setup #3 |
| TC-AC-SU-69 | Manage user and role (U=true) | Pre-setup #4 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-68, 69 | `Region A` | `Region A {runId}-023` | - | Group |
| TC-AC-SU-70 | `Rudi Hartono` | `Rudi Hartono {runId}-023` | `rudihartono+{runId}-023@qwertysystem.net` | Group Role `Manage allocation` tanpa group assignment |
| TC-AC-SU-69 | `Dewi Lestari` | `Dewi Lestari {runId}-023` | `dewilestari+{runId}-023@qwertysystem.net` | Total Control; Group Role `Manage allocation` aktif di `Region A {runId}-023` |

- Data Pre-setup yang diubah (TC-AC-SU-68, S-06 pengecualian data yang tidak dapat dimiliki spec): baris Default User (Pre-setup #1) dan akun aktor Total Control (Pre-setup #2, baris self) diberi Group Role aktif di `Region A {runId}-023` lewat Fixture BE, dipulihkan ke keadaan awal di hook `after`; efek pada Last Updated dan Modified By kedua baris dicatat sebagai efek spec ini.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-68: Assign Group hidden untuk target Default User dan self

1. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
2. Klik Name baris Default User
3. Klik sub-tab Group Role
4. Verifikasi Default User: sub-tab Group Role tanpa switch
5. Verifikasi Default User: semua Group Role aktif
6. Verifikasi Default User: kolom Actions hanya `[Detail]`
7. Verifikasi Default User: `[Assign Group]` tidak dirender
8. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
9. Ganti isi kotak search dengan `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
10. Klik Name baris aktor sendiri
11. Klik sub-tab Group Role
12. Verifikasi self: sub-tab Group Role tanpa switch
13. Verifikasi self: `[Assign Group]` tidak dirender
14. Verifikasi self: `[Detail]` tampil
15. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-70: Detail dan Assign Group enabled untuk role tanpa group, aktor Total Control

16. Ganti isi kotak search dengan `Rudi Hartono {runId}-023`, tekan Enter
17. Klik Name `Rudi Hartono {runId}-023`
18. Klik sub-tab Group Role
19. Amati baris `Manage allocation`, hover `[Detail]` dan `[Assign Group]`
20. Verifikasi Total Control: baris `Manage allocation` tanpa switch
21. Verifikasi Total Control: kolom Group `—`
22. Verifikasi Total Control: `[Detail]` dan `[Assign Group]` tampil dan enabled, tanpa tooltip
23. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-70: Detail dan Assign Group, aktor Read Only

24. Logout dari akun aktor saat ini
25. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
26. Ketik Search `Rudi Hartono {runId}-023`, tekan Enter
27. Klik Name `Rudi Hartono {runId}-023`
28. Klik sub-tab Group Role
29. Verifikasi Read Only: `[Detail]` tampil dan enabled
30. Verifikasi Read Only: `[Assign Group]` tidak dirender
31. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-69: Assign Group disabled untuk target Total Control bagi Manage user and role

32. Logout dari akun aktor saat ini
33. Login sebagai Manage user and role (Update, U=true) (`manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_UPDATE_PASSWORD`)
34. Ketik Search `Dewi Lestari {runId}-023`, tekan Enter
35. Klik Name `Dewi Lestari {runId}-023`
36. Klik sub-tab Group Role
37. Hover `[Assign Group]`
38. Verifikasi `[Assign Group]` tetap tampil namun disabled dengan tooltip `You don't have permission to edit.`
39. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
40. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), langkah 8, 23, 39 dan langkah kembali ke daftar lain, langkah 40 (reset Search).
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit; tiga akun dipakai berurutan, masing-masing satu kali. Urutan TC (S-05): 68, 70 (Total Control), 70 (Read Only), 69, agar akun Total Control dipakai berurutan.
- Ukuran spec (40 langkah, di atas smell sekitar 35 langkah): Role Matrix satu permukaan (sub-tab Group Role) dengan tiga akun; tiap blok akun berdiri sendiri (login eksplisit di awal blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-68 mensyaratkan Default User dan aktor memiliki Group Role aktif; keduanya data Pre-setup, sehingga S-06 pengecualian dipakai lewat Fixture BE dan `suite.md` belum menyatakannya. Perlu keputusan pemilik.
  - TC-AC-SU-68 memakai nama aktor `Fajar Nugroho`; spec memakai akun Total Control Pre-setup #2 dan baris self dicari lewat emailnya.
  - Nama user TC (`Region A`, `Rudi Hartono`, `Dewi Lestari`) dipakai sebagai nama bersuffix `{runId}-023` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
