---
id: TC-AC-SU-E2E-048-sub-tab-global-role-baris-default-user-dan-self-terkunci
title: "Sub-tab Global Role: Detail Default User dan Akun Sendiri Terkunci"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-183
  - TC-AC-SU-184
coverage:
  web: automated
---

# Sub-tab Global Role: Detail Default User dan Akun Sendiri Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Fixture `Fixture.settingsUser` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `defaultUserName` (nama tampil Default User Principal), `totalControlName` (nama tampil akun Total Control).
- Target adalah akun Pre-setup (Default User Principal dan akun aktor sendiri) yang hanya dibuka dan di-hover; tidak ada aksi tulis yang berhasil.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-048` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-183: Baris Global Role pada Detail Default User terkunci penuh

1. Ketik Search `Fixture.settingsUser.defaultUserName`, tekan Enter
2. Klik nama Default User di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Verifikasi banner `"This user has Total Control access."` tampil di atas sub-tab
4. Verifikasi semua switch Global Role ON dan tetap tampil (visible) namun disabled
5. Verifikasi semua checkbox CRUD applicable tercentang dan disabled
6. Hover switch salah satu baris Global Role
7. Verifikasi tooltip `"Default User cannot be modified."` pada switch
8. Hover checkbox C baris yang sama
9. Verifikasi tooltip `"Default User cannot be modified."` pada checkbox
10. Klik switch dan checkbox tersebut
11. Verifikasi klik tidak mengubah apa pun
12. Verifikasi tidak ada dialog Auto-Revert
13. Verifikasi tidak ada toast
14. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-184: Aktor membuka Tab Role miliknya sendiri: edit Global Role terkunci

15. Ketik Search `Fixture.settingsUser.totalControlName`, tekan Enter
16. Klik nama akun sendiri di User List, Settings > User > Detail terbuka dengan Tab Role aktif
17. Hover switch sebuah baris Global Role
18. Verifikasi switch Global Role tetap tampil namun disabled
19. Verifikasi tooltip `"You can't manage your own account from here."` pada switch
20. Hover checkbox C sebuah baris Global Role
21. Verifikasi checkbox CRUD tetap tampil namun disabled
22. Verifikasi tooltip `"You can't manage your own account from here."` pada checkbox
23. Klik checkbox C yang disabled
24. Verifikasi tidak ada dialog Auto-Revert walau aktor bertier Total Control

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 14, 15, 23 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung "Klik checkbox C yang disabled" di TC-184 (S-03): pemicu supaya absence dialog Auto-Revert bermakna; TC tidak memberi langkah klik.
- Temuan untuk QA:
  - Nama tampil Default User dan akun Total Control aktor tidak terpetakan ke Pre-setup (email saja); spec memakai kunci fixture yang disediakan tim FE.
