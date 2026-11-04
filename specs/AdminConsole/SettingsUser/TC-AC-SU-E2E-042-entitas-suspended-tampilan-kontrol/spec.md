---
id: TC-AC-SU-E2E-042-entitas-suspended-tampilan-kontrol
title: "Entitas Suspended: Tampilan Kontrol Tulis di User List dan Detail User"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-161
  - TC-AC-SU-162
  - TC-AC-SU-163
  - TC-AC-SU-164
  - TC-AC-SU-191
  - TC-AC-SU-212
coverage:
  web: automated
---

# Entitas Suspended: Tampilan Kontrol Tulis di User List dan Detail User

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Distributor Nusantara, Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, password `Spectra.env.AC_DIST_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (entitas Distributor Nusantara, seed lewat Fixture BE sebelum entitas disuspend): `John Doe {runId}-042` (Activated, Active), `Mike Tan {runId}-042` (Pending Activation), `Budi Santoso {runId}-042` (tanpa tingkat akses, bukan Group Manager).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-042@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-042`.
- State tenant: entitas Distributor Nusantara dalam status Suspended; hook `before` men-seed data lalu menyuspend entitas lewat Fixture BE, hook `after` meng-unsuspend (status awal Aktif). Pemicu suspend dan unsuspend memakai kemampuan Fixture BE yang setara aksi Admin Principal di modul Distributor (disediakan tim FE/BE).
- Fixture `Fixture.settingsUser` (berkas fixture belum ada; disediakan tim FE) memuat `distributorDefaultUserName` (nama tampil Default User entitas Distributor, Pre-setup #7) dan `distributorTotalControlName` (nama tampil akun aktor Total Control Distributor Nusantara).
- Akun aktor entitas Distributor Nusantara selain Default User tidak ada di Tabel Data Uji Pre-setup (hanya #7); email dan password `Spectra.env.AC_DIST_TC_PASSWORD` / `Spectra.env.AC_DIST_MUR_PASSWORD` perlu disediakan tim FE dan didaftarkan di `executionConfig.environmentVariables` serta `.env.example` oleh pemilik repo.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-042` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-161: Entitas suspended: switch Active dan checkbox Disabled dengan tooltip

1. Ketik Search `{runId}-042`, tekan Enter
2. Hover switch Active baris `John Doe {runId}-042`
3. Verifikasi switch Active baris `John Doe {runId}-042` tampil namun disabled (muted)
4. Verifikasi tooltip `"Entity is suspended."` pada switch
5. Hover checkbox baris `John Doe {runId}-042`
6. Verifikasi checkbox baris `John Doe {runId}-042` tampil namun disabled
7. Verifikasi tooltip `"Entity is suspended."` pada checkbox

### TC-AC-SU-163: Entitas suspended: prioritas tooltip di atas Default User dan self

8. Klik `✕` pada Search, tekan Enter, lalu ketik Search `Fixture.settingsUser.distributorDefaultUserName`, tekan Enter
9. Hover switch baris Default User
10. Verifikasi tooltip `"Entity is suspended."` pada switch baris Default User
11. Klik `✕` pada Search, tekan Enter, lalu ketik Search `Fixture.settingsUser.distributorTotalControlName`, tekan Enter
12. Hover switch baris aktor sendiri
13. Verifikasi tooltip `"Entity is suspended."` pada switch baris aktor sendiri

### TC-AC-SU-162: Entitas suspended: Bulk Action Bar, Resend, dan Assign Group Hidden

14. Klik `✕` pada Search, tekan Enter, lalu ketik Search `Mike Tan {runId}-042`, tekan Enter
15. Klik `(⋯)` baris `Mike Tan {runId}-042` (Pending Activation)
16. Verifikasi row action baris `Mike Tan {runId}-042`: hanya `Detail`
17. Tutup menu `(⋯)` dengan Esc
18. Klik nama `Mike Tan {runId}-042` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
19. Hover switch sebuah baris Global Role
20. Verifikasi switch Global Role disabled
21. Verifikasi checkbox CRUD Global Role disabled
22. Verifikasi tooltip `"Entity is suspended."` pada switch Global Role
23. Verifikasi header Detail tampil dengan Breadcrumb dan Tab Role
24. Verifikasi header Detail tanpa tombol Resend
25. Klik Sub-tab [Group Role]
26. Verifikasi `[Detail]` tampil pada kolom Actions Group Role
27. Verifikasi `[Assign Group]` tidak tampil pada kolom Actions Group Role
28. Klik segmen `User` pada Breadcrumb untuk kembali ke User List

### TC-AC-SU-191: Entitas suspended: switch dan CRUD Global Role terkunci

29. Ganti isi kotak Search dengan `Budi Santoso {runId}-042`, tekan Enter
30. Klik nama `Budi Santoso {runId}-042` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
31. Hover switch sebuah baris Global Role
32. Verifikasi switch Global Role tampil namun disabled
33. Hover checkbox sebuah baris Global Role
34. Verifikasi checkbox CRUD Global Role tampil namun disabled
35. Verifikasi tooltip `"Entity is suspended."`

### TC-AC-SU-212: Entitas suspended: Assign Group Hidden dan Detail tampil

36. Klik Sub-tab [Group Role]
37. Verifikasi `[Detail]` tampil dan enabled
38. Verifikasi `[Assign Group]` Hidden

### TC-AC-SU-164: Entitas suspended: banner tampil di Dashboard, tidak di Settings > User

39. Buka Admin Console > Dashboard lewat sidebar
40. Verifikasi banner di Dashboard: `"Your organization is currently suspended. Contact your administrator for more information."`
41. Buka Settings > User lewat sidebar
42. Verifikasi tabel User List tampil
43. Verifikasi tidak ada banner suspended di Settings > User

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 8, 11, 14, 17, 28, 29 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Kelas harness h (state tenant): seluruh TC memuat tampilan baca atas entitas Suspended dan tidak memuat TC tulis.
- Urutan TC di spec: 161, 163, 162, 191, 212, 164 (hover baris di User List lebih dulu, lalu Detail, Dashboard terakhir).
- Expected TC-162 butir c menyebut switch Global Role dan CRUD disabled, tetapi langkah TC hanya membuka Sub-tab Group Role; spec menambah satu `Hover` pada Tab Role aktif (Global Role) untuk mengamati tooltip (S-03), dengan Detail `Mike Tan {runId}-042` sebagai target.
- Anchor absence di TC-162 dan TC-164: tombol `[Detail]`, Breadcrumb/Tab Role, dan tabel User List tampil lebih dulu (bagian 8b butir 2).
- Temuan untuk QA:
  - Akun aktor Total Control entitas Distributor Nusantara dan nama tampilnya tidak terpetakan ke Pre-setup (hanya Default User Distributor #7). TC menulis "Role: Total Control (entitas Distributor Nusantara (status Suspended))" tanpa akun.
  - TC-161 dan TC-163 tidak menyebut cara menyuspend; spec memakai kemampuan Fixture BE yang setara aksi Admin Principal di modul Distributor.
- Alasan spec melewati sekitar 35 langkah: seluruh blok berada pada satu kelas harness (h, entitas Suspended yang sama) dan hanya mengamati; tiap TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan data user dipakai bersama tanpa langkah tulis.
