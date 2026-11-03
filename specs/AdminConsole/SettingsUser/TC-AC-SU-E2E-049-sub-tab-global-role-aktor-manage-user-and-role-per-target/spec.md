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
5. Hover checkbox C baris `Manage group`
6. Verifikasi seluruh switch dan CRUD Global Role tampil namun disabled
7. Verifikasi tooltip `"You don't have permission to edit."`
8. Klik switch baris `Manage group`
9. Verifikasi klik tidak memicu dialog
10. Verifikasi klik tidak memicu toast
11. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-186: Aktor Manage user and role pada target Read Only: Global Role terkunci

12. Ketik Search `Andi Wijaya {runId}-049`, tekan Enter
13. Klik nama `Andi Wijaya {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
14. Hover switch baris `Manage group`
15. Verifikasi banner `"This user has Read Only access."` tampil
16. Verifikasi switch dan CRUD Global Role tampil namun disabled
17. Verifikasi tooltip `"You don't have permission to edit."`
18. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-187: Aktor Manage user and role mengedit Global Role target standar sampai sukses

19. Ketik Search `Budi Santoso {runId}-049`, tekan Enter
20. Klik nama `Budi Santoso {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
21. Centang C baris `Manage group`
22. Verifikasi muncul toast sukses: "Success, permissions have been updated."
23. Tunggu toast lama hilang otomatis
24. Klik switch baris `Manage language` ke ON
25. Verifikasi muncul toast sukses: "Success, role has been updated."
26. Verifikasi tidak ada dialog Auto-Revert
27. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-188: Aktor Manage user and role pada target Group Manager: Global Role tetap bisa diedit

28. Ketik Search `Dedi Kurnia {runId}-049`, tekan Enter
29. Klik nama `Dedi Kurnia {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
30. Verifikasi banner `"This user is a Group Manager for: Region A {runId}-049."` tampil
31. Verifikasi switch dan CRUD Global Role enabled
32. Centang C baris `Manage group`
33. Verifikasi muncul toast sukses: "Success, permissions have been updated."
34. Verifikasi tidak ada dialog Auto-Revert

### TC-AC-SU-190: Aktor Manage user and role tanpa Update membuka Sub-tab Global Role

35. Logout dari akun Manage user and role (Update aktif)
36. Login sebagai Manage user and role (Read saja, U=false) (`manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MUR_READ_PASSWORD`)
37. Buka Settings > User lewat sidebar
38. Ketik Search `Budi Santoso {runId}-049`, tekan Enter
39. Klik nama `Budi Santoso {runId}-049` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
40. Hover switch sebuah baris Global Role
41. Verifikasi switch dan CRUD Global Role tampil namun disabled
42. Verifikasi tooltip `"You don't have permission to edit."`
43. Logout dari akun Manage user and role (Read saja) dan login kembali sebagai akun default suite (Total Control)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 11, 12, 18, 19, 23, 27, 28, 38, 43 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Ganti akun eksplisit di TC-190: dua akun aktor MUR berbeda (Update aktif dan Read saja); perulangan role tidak dipakai karena langkah tiap target berbeda (bagian 3a).
- Hook `after` mengembalikan sesi ke akun default suite (Total Control) bila spec berhenti sebelum langkah pemulihan terakhir.
- Temuan untuk QA:
  - Post Condition TC-187 ("Modified By ... = aktor Manage user and role") dan TC-188 ("Status Group Manager Dedi Kurnia di Region A tetap") tidak punya langkah observasi dan tidak diasersi.
  - Nama group `Region A` pada banner diasersi dengan nama bersuffix milik spec.
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada permukaan dan kelas harness yang sama dan berdiri sendiri (target user milik spec per TC); kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian langkah hanya penghubung (pencarian target dan kembali ke User List).
