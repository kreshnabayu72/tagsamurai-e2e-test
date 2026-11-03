---
id: TC-AC-SU-E2E-054-sub-tab-group-role-baris-default-user-self-dan-tanpa-assignment
title: "Sub-tab Group Role: Default User, Akun Sendiri, dan Group Role Tanpa Group Assignment"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-205
  - TC-AC-SU-206
  - TC-AC-SU-207
  - TC-AC-SU-633
coverage:
  web: automated
---

# Sub-tab Group Role: Default User, Akun Sendiri, dan Group Role Tanpa Group Assignment

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun kedua (ganti akun eksplisit di tengah spec, TC-633): user seed `Mike Tan {runId}-054` (email `mike.tan+{runId}-054@qwertysystem.net`), password `Spectra.env.AC_SU_SEEDED_PASSWORD`; env var `AC_SU_SEEDED_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan pemilik repo.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Sarah Lee {runId}-054` (tanpa tingkat akses, bukan Group Manager; `Manage partner` tanpa group assignment) dan `Mike Tan {runId}-054` (akun yang dapat login; `Manage partner` tanpa group assignment).
- Fixture `Fixture.settingsUser` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `defaultUserName` (nama tampil Default User Principal), `totalControlName` (nama tampil akun Total Control).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-054@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-054`.
- Target Default User Principal dan akun aktor sendiri adalah akun Pre-setup yang hanya dibuka dan diamati.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-054` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-206: Baris Group Role pada Detail Default User tanpa switch, hanya Detail tampil

1. Ketik Search `Fixture.settingsUser.defaultUserName`, tekan Enter
2. Klik nama Default User di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Amati kolom Group dan Actions
5. Verifikasi tidak ada switch di baris Group Role
6. Verifikasi seluruh Group Role aktif dengan group ter-assign
7. Verifikasi `[Detail]` tampil pada kolom Actions
8. Verifikasi `[Assign Group]` Hidden (tidak dirender)
9. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-207: Self: Assign Group Hidden dan Detail tampil

10. Ketik Search `Fixture.settingsUser.totalControlName`, tekan Enter
11. Klik nama akun sendiri di User List, Settings > User > Detail terbuka dengan Tab Role aktif
12. Klik Sub-tab [Group Role]
13. Amati kolom Actions
14. Verifikasi `[Detail]` tampil dan enabled
15. Verifikasi `[Assign Group]` Hidden
16. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-205: Group Role tanpa group assignment diperlakukan server tanpa akses

17. Ketik Search `Sarah Lee {runId}-054`, tekan Enter
18. Klik nama `Sarah Lee {runId}-054` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
19. Klik Sub-tab [Group Role]
20. Amati baris `Manage partner`
21. Verifikasi kolom Group baris `Manage partner` = `—`
22. Verifikasi baris `Manage partner` tanpa switch
23. Klik Breadcrumb Settings > User untuk kembali ke User List
24. Verifikasi kolom Role baris `Sarah Lee {runId}-054` tidak menghitung `Manage partner` (menampilkan `0 roles`)

### TC-AC-SU-633: EC-18: Group Role tanpa group assignment diperlakukan tanpa akses

25. Logout dari akun Total Control
26. Login sebagai `Mike Tan {runId}-054` (`mike.tan+{runId}-054@qwertysystem.net`, password dari `Spectra.env.AC_SU_SEEDED_PASSWORD`)
27. Buka menu Partner lewat sidebar
28. Verifikasi halaman Partner tampil (header halaman)
29. Verifikasi data Partner tidak tampil
30. Verifikasi aksi tulis di halaman Partner ditolak
31. Logout dari akun `Mike Tan {runId}-054` dan login kembali sebagai akun default suite (Total Control)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 9, 10, 16, 17, 23, 31 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC di spec: 206, 207, 205, 633. TC-633 (ganti akun) ditaruh terakhir; tabel Role aktor kedua dipulihkan hook `after`.
- Temuan untuk QA:
  - TC-633 (Automation: Manual Only) tidak menyebut aksi tulis yang diuji dan tidak memberi anchor halaman Partner; spec mengasersi header halaman Partner sebagai anchor dan menulis butir aksi tulis ditolak apa adanya.
  - Akun `Mike Tan` yang dapat login tidak ada di Pre-setup; spec memakai user seed dengan password env.
  - TC-205 butir b: label kolom Role untuk 0 role (`0 roles`) diambil dari contoh Post Condition TC-173.
  - Post Condition TC-205 ("Sarah Lee tidak bisa melihat data Partner manapun") tidak punya langkah observasi dan tidak diasersi.
  - Expected TC-206 butir a ("seluruh Group Role aktif dengan group ter-assign") tidak merinci group; spec mengasersi bahwa tidak ada baris dengan `—`.
