---
id: TC-AC-SU-E2E-019-role-matrix-switch-active-read-only-manage-user-and-role-tanpa-update
title: "Role Matrix: Switch Active untuk Aktor Read Only dan Manage user and role, Switch Header Detail, serta Prioritas Tooltip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-59
  - TC-AC-SU-60
  - TC-AC-SU-61
  - TC-AC-SU-79
coverage:
  web: automated
---

# Role Matrix: Switch Active untuk Aktor Read Only dan Manage user and role, Switch Header Detail, serta Prioritas Tooltip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only (Pre-setup #3) `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Akun aktor: Manage user and role Read saja (U=false, Pre-setup #5) `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_READ_PASSWORD`.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Env var `AC_MUR_READ_PASSWORD`, `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-59 | Read Only | Pre-setup #3 |
| TC-AC-SU-60 | Manage user and role (U=false) | Pre-setup #5 |
| TC-AC-SU-61, 79 | Manage user and role (U=true) | Pre-setup #4 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-59, 60, 61 | `Rudi Hartono` | `Rudi Hartono {runId}-019` | `rudihartono+{runId}-019@qwertysystem.net` | tanpa role (kosong) |
| TC-AC-SU-59, 61 | `Dewi Lestari` | `Dewi Lestari {runId}-019` | `dewilestari+{runId}-019@qwertysystem.net` | Total Control |
| TC-AC-SU-79 | `Fajar Nugroho` | `Fajar Nugroho {runId}-019` | `fajarnugroho+{runId}-019@qwertysystem.net` | Total Control dan nonaktif di Global Settings |

- Baris Default User (Pre-setup #1) dan baris aktor sendiri dicari lewat Search atas email akun masing-masing; keduanya tidak diubah.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-59: Switch Active seluruh baris, aktor Read Only

1. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
2. Hover switch Active baris Default User
3. Verifikasi switch Active baris Default User tampil namun disabled dengan tooltip `Read Only access cannot modify data.`
4. Ganti isi kotak search dengan `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
5. Hover switch Active baris aktor sendiri (self)
6. Verifikasi switch Active baris aktor sendiri (self) tampil namun disabled dengan tooltip `Read Only access cannot modify data.`
7. Ganti isi kotak search dengan `{runId}-019`, tekan Enter
8. Hover switch Active baris `Rudi Hartono {runId}-019`
9. Verifikasi switch Active baris `Rudi Hartono {runId}-019` tampil namun disabled dengan tooltip `Read Only access cannot modify data.`
10. Hover switch Active baris `Dewi Lestari {runId}-019`
11. Verifikasi switch Active baris `Dewi Lestari {runId}-019` tampil namun disabled dengan tooltip `Read Only access cannot modify data.`

### TC-AC-SU-60: Switch Active, aktor Manage user and role tanpa Update

12. Logout dari akun aktor saat ini
13. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
14. Ketik Search `{runId}-019`, tekan Enter
15. Hover switch Active baris `Rudi Hartono {runId}-019`
16. Verifikasi switch Active baris `Rudi Hartono {runId}-019` tampil namun disabled dengan tooltip `You don't have permission to edit.`
17. Ganti isi kotak search dengan `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
18. Hover switch Active baris Default User
19. Verifikasi switch Active baris Default User tampil namun disabled dengan tooltip `You don't have permission to edit.`

### TC-AC-SU-61: Switch Active header Detail User mengikuti aturan baris List

20. Logout dari akun aktor saat ini
21. Login sebagai Manage user and role (Update, U=true) (`manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_UPDATE_PASSWORD`)
22. Ketik Search `Dewi Lestari {runId}-019`, tekan Enter
23. Klik Name `Dewi Lestari {runId}-019`
24. Hover switch Active di header Detail
25. Verifikasi switch header `Dewi Lestari {runId}-019` tampil namun disabled dengan tooltip `You don't have permission to edit.`
26. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
27. Ganti isi kotak search dengan `Rudi Hartono {runId}-019`, tekan Enter
28. Klik Name `Rudi Hartono {runId}-019`
29. Verifikasi switch header `Rudi Hartono {runId}-019` enabled
30. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
31. Ganti isi kotak search dengan `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, tekan Enter
32. Klik Name baris aktor sendiri
33. Hover switch Active di header Detail
34. Verifikasi switch header aktor sendiri tampil namun disabled dengan tooltip `You can't manage your own account from here.`
35. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-79: Prioritas tooltip saat target nonaktif di Global Settings sekaligus Total Control

36. Ganti isi kotak search dengan `Fajar Nugroho {runId}-019`, tekan Enter
37. Hover switch Active baris `Fajar Nugroho {runId}-019`
38. Verifikasi switch Active baris `Fajar Nugroho {runId}-019` tetap tampil (visible) namun disabled
39. Verifikasi tampil satu tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`
40. Verifikasi tooltip `You don't have permission to edit.` tidak tampil
41. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), langkah 26 dan langkah kembali ke daftar lain (kembali ke Settings > User), langkah 41 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit; tiga akun (Read Only, Manage user and role Read saja, Manage user and role Update) dipakai berurutan, masing-masing satu kali. Tooltip diasersi segera sesudah hover (bagian 8b butir 5).
- Ukuran spec (41 langkah, di atas smell sekitar 35 langkah): Role Matrix dengan tiga akun dan empat TC; tiap blok akun berdiri sendiri (login eksplisit di awal blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-59, 60, 61 memakai nama aktor `Andi Wijaya`, `Yoga Pratama`, dan `Mike Tan` yang tidak dipetakan ke Pre-setup; spec memakai akun Pre-setup #3, #5, dan #4.
  - TC-AC-SU-79 butir c memakai kata "Must NOT"; diasersi sebagai tooltip tidak tampil, anchor positif adalah tooltip yang benar (butir b) pada surface yang sama.
  - Nama user TC (`Rudi Hartono`, `Dewi Lestari`, `Fajar Nugroho`) dipakai sebagai nama bersuffix `{runId}-019` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
