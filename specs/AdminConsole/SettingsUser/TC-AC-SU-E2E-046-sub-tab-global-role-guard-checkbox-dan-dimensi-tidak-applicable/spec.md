---
id: TC-AC-SU-E2E-046-sub-tab-global-role-guard-checkbox-dan-dimensi-tidak-applicable
title: "Sub-tab Global Role: Checkbox Terkunci, Read Mandatory, dan Dimensi Tidak Applicable"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-176
  - TC-AC-SU-179
  - TC-AC-SU-180
coverage:
  web: automated
---

# Sub-tab Global Role: Checkbox Terkunci, Read Mandatory, dan Dimensi Tidak Applicable

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-046` tanpa tingkat akses dan bukan Group Manager; Global Role: `Manage TAG stock` OFF, `Manage group` ON (C ☐ R ☑ U ☑ D ☑), `Manage hardware stock` ON.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-046@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-046`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-046` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-176: Checkbox CRUD terkunci saat switch OFF tidak bisa diklik

1. Ketik Search `Budi Santoso {runId}-046`, tekan Enter
2. Klik nama `Budi Santoso {runId}-046` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik sel C, R, U, D baris `Manage TAG stock`
4. Verifikasi sel C, R, U, D baris `Manage TAG stock` tetap `[─]`, tidak berubah
5. Verifikasi tidak ada toast

### TC-AC-SU-179: Checkbox Read mandatory tidak bisa di-uncheck saat role aktif

6. Klik checkbox R baris `Manage group`
7. Verifikasi checkbox R baris `Manage group` tetap `[☑]` dan disabled
8. Verifikasi tidak ada toast
9. Muat ulang halaman dengan F5
10. Verifikasi checkbox R baris `Manage group` tetap `[☑]` (tidak ada perubahan tersimpan)

### TC-AC-SU-180: Dimensi tidak applicable tampil `—` di switch ON dan OFF

11. Amati sel U baris `Manage hardware stock`
12. Verifikasi sel U baris `Manage hardware stock` tampil `—` tanpa bracket dan tidak bisa diklik
13. Klik switch baris `Manage hardware stock` ke OFF
14. Amati sel U baris `Manage hardware stock`
15. Verifikasi sel U baris `Manage hardware stock` tetap `—` (bukan `[─]`)
16. Verifikasi sel C, R, D baris `Manage hardware stock` menjadi `[─]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 9 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC lintas spec: TC-AC-SU-170, 171, 172 (screening Sub-tab Global Role) ada di spec 045.
- TC-180 ditaruh terakhir karena mengubah role (switch OFF) dan menyimpan perubahan.
- Langkah penghubung `F5` di TC-179 (S-03): Sub-tab Global Role tanpa dirty form sehingga muat ulang tidak memicu dialog; dipakai sebagai observasi "tidak ada perubahan tersimpan" yang tidak punya langkah di TC.
- Temuan untuk QA:
  - Expected TC-179 butir b ("tidak ada perubahan tersimpan") dan TC-176 butir b ("tidak ada toast") tidak punya langkah observasi tertentu; spec mengasersi state sesudah muat ulang.
  - Autosave switch OFF pada TC-180 menghasilkan toast yang tidak disebut Expected TC dan tidak diasersi.
