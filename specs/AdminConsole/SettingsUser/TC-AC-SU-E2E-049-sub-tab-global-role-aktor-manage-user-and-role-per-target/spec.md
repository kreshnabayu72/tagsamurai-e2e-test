---
id: TC-AC-SU-E2E-049-sub-tab-global-role-aktor-manage-user-and-role-per-target
title: "Sub-tab Global Role: Aktor Manage user and role per Target (Total Control, Read Only, Standar, Group Manager)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-185
  - TC-AC-SU-186
  - TC-AC-SU-187
  - TC-AC-SU-188
  - TC-AC-SU-190
coverage:
  web: automated
---

# Sub-tab Global Role: Aktor Manage user and role per Target (Total Control, Read Only, Standar, Group Manager)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user and role (Update aktif), `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Akun kedua (ganti akun eksplisit di tengah spec): Manage user and role (Read saja, U=false), `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_READ_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Rina Putri {runId}-049` (tingkat akses Total Control), `Andi Wijaya {runId}-049` (tingkat akses Read Only), `Budi Santoso {runId}-049` (tanpa tingkat akses, bukan Group Manager; `Manage group` ON dengan C ☐, `Manage language` OFF), `Dedi Kurnia {runId}-049` (Group Manager di `Region A {runId}-049`; `Manage group` ON dengan C ☐).
- Group Tree milik spec (seed lewat Fixture BE, suffix `{runId}-049` pada setiap nama): `Region A {runId}-049`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-049@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-049`.
- Env var `AC_MUR_UPDATE_PASSWORD` dan `AC_MUR_READ_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan pemilik repo.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-049` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-185: Aktor Manage user and role pada target Total Control: Global Role terkunci

1. Ketik Search `Rina Putri {runId}-049`, tekan Enter
2. Klik nama `Rina Putri {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Verifikasi banner `"This user has Total Control access."` tampil
4. Hover switch baris `Manage group`
5. Verifikasi tooltip `"You don't have permission to edit."`
6. Hover checkbox C baris `Manage group`
7. Verifikasi tooltip `"You don't have permission to edit."`
8. Verifikasi seluruh switch dan CRUD Global Role tampil namun disabled
9. Klik switch baris `Manage group`
10. Verifikasi klik tidak memicu dialog
11. Verifikasi klik tidak memicu toast
12. Klik segmen `User` pada Breadcrumb untuk kembali ke User List

### TC-AC-SU-186: Aktor Manage user and role pada target Read Only: Global Role terkunci

13. Ganti isi kotak Search dengan `Andi Wijaya {runId}-049`, tekan Enter
14. Klik nama `Andi Wijaya {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
15. Hover switch baris `Manage group`
16. Verifikasi banner `"This user has Read Only access."` tampil
17. Verifikasi switch dan CRUD Global Role tampil namun disabled
18. Verifikasi tooltip `"You don't have permission to edit."`
19. Klik segmen `User` pada Breadcrumb untuk kembali ke User List

### TC-AC-SU-187: Aktor Manage user and role mengedit Global Role target standar sampai sukses

20. Ganti isi kotak Search dengan `Budi Santoso {runId}-049`, tekan Enter
21. Klik nama `Budi Santoso {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
22. Centang C baris `Manage group`
23. Verifikasi muncul toast sukses: "Success, permissions have been updated."
24. Tunggu toast lama hilang otomatis
25. Klik switch baris `Manage language` ke ON
26. Verifikasi muncul toast sukses: "Success, role has been updated."
27. Verifikasi tidak ada dialog Auto-Revert
28. Klik segmen `User` pada Breadcrumb untuk kembali ke User List

### TC-AC-SU-188: Aktor Manage user and role pada target Group Manager: Global Role tetap bisa diedit

29. Ganti isi kotak Search dengan `Dedi Kurnia {runId}-049`, tekan Enter
30. Klik nama `Dedi Kurnia {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
31. Verifikasi banner `"This user is a Group Manager for: Region A {runId}-049."` tampil
32. Verifikasi switch dan CRUD Global Role enabled
33. Centang C baris `Manage group`
34. Verifikasi muncul toast sukses: "Success, permissions have been updated."
35. Verifikasi tidak ada dialog Auto-Revert

### TC-AC-SU-190: Aktor Manage user and role tanpa Update membuka Sub-tab Global Role

36. Logout dari akun Manage user and role (Update aktif)
37. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
38. Buka Settings > User lewat sidebar
39. Ketik Search `Budi Santoso {runId}-049`, tekan Enter
40. Klik nama `Budi Santoso {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
41. Hover switch sebuah baris Global Role
42. Verifikasi switch dan CRUD Global Role tampil namun disabled
43. Verifikasi tooltip `"You don't have permission to edit."`
44. Logout dari akun Manage user and role (Read saja) dan login kembali sebagai akun default suite (Total Control)

## Notes

- Spec ini matriks visibilitas per aktor dan target (bagian 3a): memuat asersi terkunci (disabled dengan tooltip untuk target Total Control, Read Only, dan aktor Read saja) bersama enabled dan toast sukses (target standar dan Group Manager) dalam satu spec; polaritas campuran disengaja; `caseType` Negative mengikuti bagian 8.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 12, 13, 19, 20, 24, 28, 29, 39, 44 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Ganti akun eksplisit di TC-190: dua akun aktor MUR berbeda (Update aktif dan Read saja); perulangan role tidak dipakai karena langkah tiap target berbeda (bagian 3a).
- Hook `after` mengembalikan sesi ke akun default suite (Total Control) bila spec berhenti sebelum langkah pemulihan terakhir.
- Temuan untuk QA:
  - Post Condition TC-187 ("Modified By ... = aktor Manage user and role") dan TC-188 ("Status Group Manager Dedi Kurnia di Region A tetap") tidak punya langkah observasi dan tidak diasersi.
  - Nama group `Region A` pada banner diasersi dengan nama bersuffix milik spec.
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada permukaan dan kelas harness yang sama dan berdiri sendiri (target user milik spec per TC); kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian langkah hanya penghubung (pencarian target dan kembali ke User List).
