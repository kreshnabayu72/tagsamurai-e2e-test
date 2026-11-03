---
id: TC-AC-SU-E2E-018-role-matrix-switch-active-manage-user-and-role-dan-total-control
title: "Role Matrix: Switch Active per Target untuk Aktor Manage user and role (Update) dan Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-56
  - TC-AC-SU-57
  - TC-AC-SU-99
coverage:
  web: automated
---

# Role Matrix: Switch Active per Target untuk Aktor Manage user and role (Update) dan Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Manage user and role (Update, U=true); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-56, 99 | Manage user and role (U=true) | Pre-setup #4 |
| TC-AC-SU-57 | Total Control | Pre-setup #2 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-56, 57 | `Dewi Lestari` | `Dewi Lestari {runId}-018` | `dewilestari+{runId}-018@qwertysystem.net` | Total Control |
| TC-AC-SU-56, 57 | `Andi Wijaya` | `Andi Wijaya {runId}-018` | `andiwijaya+{runId}-018@qwertysystem.net` | Read Only |
| TC-AC-SU-56, 57 | `Dedi Kurnia` | `Dedi Kurnia {runId}-018` | `dedikurnia+{runId}-018@qwertysystem.net` | Group Manager |
| TC-AC-SU-56, 57 | `Rudi Hartono` | `Rudi Hartono {runId}-018` | `rudihartono+{runId}-018@qwertysystem.net` | tanpa role (kosong) |
| TC-AC-SU-56 | `Hana Pratiwi` | `Hana Pratiwi {runId}-018` | `hanapratiwi+{runId}-018@qwertysystem.net` | tanpa role (kosong); nonaktif di Global Settings |
| TC-AC-SU-57 | `Fajar Nugroho` | `Fajar Nugroho {runId}-018` | `fajarnugroho+{runId}-018@qwertysystem.net` | Total Control (TC lain) |

- Baris Default User (Pre-setup #1) dan baris aktor sendiri dicari lewat Search atas email akun masing-masing; keduanya tidak diubah.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-56: Switch Active per target, aktor Manage user and role (Update)

1. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
2. Hover switch Active baris Default User
3. Verifikasi switch Active baris Default User tampil namun disabled dengan tooltip `Default User cannot be modified.`
4. Ganti isi kotak search dengan `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, tekan Enter
5. Hover switch Active baris aktor sendiri (self)
6. Verifikasi switch Active baris aktor sendiri (self) tampil namun disabled dengan tooltip `You can't manage your own account from here.`
7. Ganti isi kotak search dengan `{runId}-018`, tekan Enter
8. Hover switch Active baris `Dewi Lestari {runId}-018`
9. Verifikasi switch Active baris `Dewi Lestari {runId}-018` tampil namun disabled dengan tooltip `You don't have permission to edit.`
10. Hover switch Active baris `Andi Wijaya {runId}-018`
11. Verifikasi switch Active baris `Andi Wijaya {runId}-018` tampil namun disabled dengan tooltip `You don't have permission to edit.`
12. Verifikasi switch Active baris `Dedi Kurnia {runId}-018` enabled
13. Verifikasi switch Active baris `Rudi Hartono {runId}-018` enabled
14. Hover switch Active baris `Hana Pratiwi {runId}-018`
15. Verifikasi switch Active baris `Hana Pratiwi {runId}-018` tampil namun disabled dengan tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`

### TC-AC-SU-99: Switch Active baris diri sendiri Disabled dengan tooltip

16. Ganti isi kotak search dengan `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, tekan Enter
17. Hover switch Active baris aktor sendiri (self)
18. Verifikasi switch Active baris aktor sendiri (self) tampil namun disabled dengan tooltip `You can't manage your own account from here.`
19. Klik switch Active baris aktor sendiri
20. Verifikasi tidak ada dialog

### TC-AC-SU-57: Switch Active per target, aktor Total Control

21. Logout dari akun aktor saat ini
22. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
23. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
24. Hover switch Active baris Default User
25. Verifikasi switch Active baris Default User tampil namun disabled dengan tooltip `Default User cannot be modified.`
26. Ganti isi kotak search dengan `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
27. Hover switch Active baris aktor sendiri (self)
28. Verifikasi switch Active baris aktor sendiri (self) tampil namun disabled dengan tooltip `You can't manage your own account from here.`
29. Ganti isi kotak search dengan `{runId}-018`, tekan Enter
30. Verifikasi switch Active baris `Andi Wijaya {runId}-018` enabled
31. Verifikasi switch Active baris `Fajar Nugroho {runId}-018` enabled
32. Verifikasi switch Active baris `Dedi Kurnia {runId}-018` enabled
33. Verifikasi switch Active baris `Rudi Hartono {runId}-018` enabled
34. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), langkah 34 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit dan langkah tiap role berbeda target; blok aktor Total Control berdiri sendiri sesudah ganti akun. Tooltip diasersi segera sesudah hover (bagian 8b butir 5); "tampil namun disabled, tooltip X" adalah satu elemen komposit (S-01).
- Perubahan urutan TC (S-05): 56, 99, 57 agar aktor Manage user and role dipakai berurutan sebelum ganti akun ke Total Control.
- Temuan untuk QA:
  - TC-AC-SU-56 memakai `Mike Tan` sebagai aktor dan TC-AC-SU-57 memakai `Dewi Lestari` sebagai aktor; nama aktor tidak dipetakan ke Pre-setup. Spec memakai akun Pre-setup #4 dan #2 dan mengidentifikasi baris self lewat email aktor.
  - TC-AC-SU-57 target "self" adalah aktor Total Control; target `Fajar Nugroho` (TC lain) di-seed sebagai Total Control milik spec.
  - Nama user TC (`Dewi Lestari`, `Andi Wijaya`, `Dedi Kurnia`, `Rudi Hartono`, `Hana Pratiwi`, `Fajar Nugroho`) dipakai sebagai nama bersuffix `{runId}-018` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
