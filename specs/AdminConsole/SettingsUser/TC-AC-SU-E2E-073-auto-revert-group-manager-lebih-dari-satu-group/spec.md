---
id: TC-AC-SU-E2E-073-auto-revert-group-manager-lebih-dari-satu-group
title: "Auto-Revert Group Manager: Save 0 Group dan Unassign Group Penopang GM"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-644
  - TC-AC-SU-260
coverage:
  web: automated
---

# Auto-Revert Group Manager: Save 0 Group dan Unassign Group Penopang GM

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Dedi Kurnia {runId}-073` dan `Dedi Kurnia B {runId}-073`, masing-masing Group Manager di `Region A {runId}-073` dan `Region B {runId}-073` dengan `Manage distributor` aktif di kedua group.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-073`): `Region A {runId}-073` > `Branch 1 {runId}-073` > `Floor 1 {runId}-073`; `Region A {runId}-073` > `Branch 3 {runId}-073`; `Region B {runId}-073`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-073@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-073`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-073` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-644: Auto-Revert Group Manager: unassign group penopang GM via Save popup

1. Ketik Search `Dedi Kurnia B {runId}-073`, tekan Enter
2. Klik nama `Dedi Kurnia B {runId}-073` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage distributor`
5. Klik `[🗑]` baris `Region A {runId}-073`
6. Klik `[Save]`
7. Verifikasi dialog Auto-Revert Group Manager muncul sebelum perubahan disimpan
8. Klik `[Cancel]` pada dialog
9. Verifikasi dialog tertutup
10. Verifikasi popup tetap terbuka dengan baris `Region A {runId}-073` sudah terhapus dari tabel popup
11. Verifikasi kolom Group `Manage distributor` di halaman masih memuat `Region A {runId}-073` (belum ada yang tersimpan)
12. Klik `[Save]` lagi
13. Klik `[Remove]`
14. Verifikasi popup tertutup
15. Verifikasi toast `"Success, permissions have been updated. Dedi Kurnia B {runId}-073 is no longer Group Manager."`
16. Verifikasi banner `"This user is a Group Manager for: Region B {runId}-073."`
17. Klik segmen `User` pada Breadcrumb untuk kembali ke User List

### TC-AC-SU-260: Auto-Revert Group Manager lebih dari 1 group dalam satu edit (Save 0 group)

18. Tunggu toast lama hilang otomatis
19. Ganti isi kotak Search dengan `Dedi Kurnia {runId}-073`, tekan Enter
20. Klik nama `Dedi Kurnia {runId}-073` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
21. Klik Sub-tab [Group Role]
22. Klik `[Assign Group]` baris `Manage distributor` (assignment di `Region A {runId}-073` dan `Region B {runId}-073`)
23. Klik `[Clear Field]`
24. Klik `[Save]`
25. Amati dialog
26. Verifikasi satu dialog Title `"Remove Group Manager"` dengan body bullet `Dedi Kurnia {runId}-073`, `"This change will remove Group Manager status for these groups:"` + bullet `Region A {runId}-073`, bullet `Region B {runId}-073`, lalu `"Are you sure you want to remove it?"`, tombol `[Cancel]` `[Remove]`
27. Klik `[Remove]`
28. Verifikasi muncul satu toast sukses: `"Success, permissions have been updated. Dedi Kurnia {runId}-073 is no longer Group Manager."` (tanpa nama group)
29. Verifikasi banner Group Manager hilang

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 17, 18, 19 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC di spec: 644, 260. Keduanya melepas status GM; tiap TC memakai user sendiri (`Dedi Kurnia B {runId}-073` dan `Dedi Kurnia {runId}-073`).
- Pembagian TC: TC-AC-SU-257 sampai 259 ada di spec 072.
- Temuan untuk QA:
  - Expected TC-260 butir a menulis "bullet bullet `Dedi Kurnia`" (kata bullet ganda); spec mengasersi satu bullet `Dedi Kurnia {runId}-073`.
  - Nama user di toast TC-644 memakai nama bersuffix `Dedi Kurnia B {runId}-073`.
  - Post Condition TC-260 (status GM Region A dan B, entri log dan notifikasi per group) dan TC-644 (assignment, log, notifikasi) tidak punya langkah observasi dan tidak diasersi.
