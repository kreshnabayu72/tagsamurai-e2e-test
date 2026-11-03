---
id: TC-AC-SU-E2E-025-role-matrix-kolom-checkbox-dan-bulk-action-bar-per-aktor
title: "Role Matrix: Kolom Checkbox dan Bulk Action Bar per Aktor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-73
  - TC-AC-SU-74
  - TC-AC-SU-136
  - TC-AC-SU-137
coverage:
  web: automated
---

# Role Matrix: Kolom Checkbox dan Bulk Action Bar per Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Akun aktor: Read Only (Pre-setup #3) `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Akun aktor: Manage user and role Read saja (U=false, Pre-setup #5) `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_READ_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD`, `AC_MUR_READ_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-73 | Total Control | Pre-setup #2 |
| TC-AC-SU-73, 74 | Manage user and role (U=true) | Pre-setup #4 |
| TC-AC-SU-73, 136 | Read Only | Pre-setup #3 |
| TC-AC-SU-73, 137 | Manage user and role (U=false) | Pre-setup #5 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-74 | `Dewi Lestari` | `Dewi Lestari {runId}-025` | `dewilestari+{runId}-025@qwertysystem.net` | Total Control |

- Baris Default User (Pre-setup #1) dan baris aktor sendiri dicari lewat Search atas email akun masing-masing; keduanya tidak diubah.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-73: Kolom Checkbox per aktor, Total Control

1. Verifikasi Total Control: kolom Checkbox tampil
2. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
3. Hover checkbox baris Default User
4. Verifikasi checkbox Default User tampil namun disabled dengan tooltip `Default User cannot be modified.`
5. Ganti isi kotak search dengan `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
6. Hover checkbox baris aktor sendiri
7. Verifikasi checkbox self tampil namun disabled dengan tooltip `You can't manage your own account from here.`

### TC-AC-SU-73 dan TC-AC-SU-74: Kolom Checkbox, aktor Manage user and role (U=true)

8. Logout dari akun aktor saat ini
9. Login sebagai Manage user and role (Update, U=true) (`manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_UPDATE_PASSWORD`)
10. Verifikasi Manage user and role (U=true): kolom Checkbox tampil
11. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
12. Hover checkbox baris Default User
13. Verifikasi checkbox Default User tampil namun disabled dengan tooltip `Default User cannot be modified.`
14. Ganti isi kotak search dengan `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, tekan Enter
15. Hover checkbox baris aktor sendiri
16. Verifikasi checkbox self tampil namun disabled dengan tooltip `You can't manage your own account from here.`
17. Ganti isi kotak search dengan `Dewi Lestari {runId}-025`, tekan Enter
18. Centang checkbox `Dewi Lestari {runId}-025`
19. Verifikasi checkbox `Dewi Lestari {runId}-025` enabled
20. Verifikasi checkbox `Dewi Lestari {runId}-025` tercentang
21. Verifikasi Bulk Action Bar muncul
22. Batalkan centang `Dewi Lestari {runId}-025`

### TC-AC-SU-73 dan TC-AC-SU-136: Kolom Checkbox dan Bulk Action Bar, aktor Read Only

23. Logout dari akun aktor saat ini
24. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
25. Amati tabel User List
26. Verifikasi Read Only: kolom Checkbox tidak dirender (header maupun body)
27. Verifikasi Bulk Action Bar tidak bisa muncul
28. Verifikasi kolom Name dan kolom lain tetap tampil

### TC-AC-SU-73 dan TC-AC-SU-137: Kolom Checkbox dan Bulk Action Bar, aktor Manage user and role (U=false)

29. Logout dari akun aktor saat ini
30. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
31. Amati tabel User List
32. Verifikasi Manage user and role (U=false): kolom Checkbox tidak dirender
33. Verifikasi kolom Checkbox Hidden
34. Verifikasi Bulk Action Bar tidak bisa muncul

## Notes

- Langkah penghubung (S-03): Search atas email Pre-setup (menemukan baris Default User dan self) dan Search atas suffix spec (R-16), serta langkah 22 (pulihkan seleksi, S-09).
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit; empat akun dipakai berurutan, masing-masing satu kali. Subjudul memetakan langkah ke id TC.
- Temuan untuk QA:
  - TC-AC-SU-136 butir b dan TC-AC-SU-137 butir b ("Bulk Action Bar tidak bisa muncul") tidak menyebut cara cek karena kolom Checkbox tidak dirender; spec mengasersi Bulk Action Bar tidak tampil pada tabel.
  - TC-AC-SU-73 butir b menyebut "header maupun body" untuk Read Only; diasersi sebagai satu `Verifikasi` (satu elemen kolom Checkbox).
  - Nama user TC (`Dewi Lestari`) dipakai sebagai nama bersuffix `{runId}-025` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
