---
id: TC-AC-SU-E2E-047-sub-tab-global-role-switch-dan-autosave-crud
title: "Sub-tab Global Role: Switch dan Autosave CRUD"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-173
  - TC-AC-SU-174
  - TC-AC-SU-175
  - TC-AC-SU-177
  - TC-AC-SU-178
coverage:
  web: automated
---

# Sub-tab Global Role: Switch dan Autosave CRUD

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-047` tanpa tingkat akses dan bukan Group Manager; Global Role: `Manage language` OFF tanpa nilai C/R/U/D tersimpan, `Manage group` ON (C ☐ R ☑ U ☑ D ☑), `Manage device master data` ON (C ☐).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-047@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-047`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-047` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-173: Switch Global Role OFF ke ON pertama kali (tanpa nilai tersimpan)

1. Ketik Search `Budi Santoso {runId}-047`, tekan Enter
2. Klik nama `Budi Santoso {runId}-047` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik switch baris `Manage language`
4. Verifikasi switch `Manage language` berubah ON
5. Verifikasi tidak ada popup
6. Verifikasi checkbox R baris `Manage language` tercentang dan disabled
7. Verifikasi checkbox C, U, D baris `Manage language` unchecked dan enabled (yang applicable)
8. Verifikasi muncul toast sukses: "Success, role has been updated."
9. Tunggu toast lama hilang otomatis

### TC-AC-SU-174: Switch Global Role ON ke OFF mengunci CRUD dan menyimpan nilai inactive

10. Klik switch baris `Manage group`
11. Verifikasi switch `Manage group` berubah OFF
12. Verifikasi C/R/U/D baris `Manage group` tampil `[─]` terkunci (disabled)
13. Verifikasi muncul toast sukses: "Success, role has been updated."
14. Tunggu toast lama hilang otomatis

### TC-AC-SU-175: Switch Global Role OFF ke ON kembali memulihkan CRUD sebelumnya

15. Klik switch baris `Manage group`
16. Verifikasi switch `Manage group` ON tanpa popup
17. Verifikasi CRUD kembali ke C `[☐]`, R `[☑]` disabled, U `[☑]`, D `[☑]` (bukan default R saja)
18. Verifikasi muncul toast sukses: "Success, role has been updated."
19. Tunggu toast lama hilang otomatis

### TC-AC-SU-177: Autosave centang Create pada Global Role aktif

20. Centang C baris `Manage device master data`
21. Verifikasi checkbox C baris `Manage device master data` tercentang tanpa tombol Save
22. Verifikasi muncul toast sukses: "Success, permissions have been updated."
23. Muat ulang halaman dengan F5
24. Verifikasi checkbox C baris `Manage device master data` tetap tercentang

### TC-AC-SU-178: Autosave uncheck Update dan Delete satu per satu pada Global Role aktif

25. Uncheck U baris `Manage group`
26. Verifikasi muncul toast sukses: "Success, permissions have been updated."
27. Tunggu toast lama hilang otomatis
28. Uncheck D baris `Manage group`
29. Verifikasi muncul toast sukses: "Success, permissions have been updated." (satu toast per perubahan)
30. Verifikasi U dan D baris `Manage group` tampil `[☐]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 9, 14, 19, 23, 27 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- TC-175 bergantung pada TC-174 (Dependensi TC); keduanya berurutan pada role `Manage group`. TC-178 mengandalkan `Manage group` ON dengan U dan D tercentang, yang dipulihkan TC-175.
- TC-177 butir Post "refresh halaman: C tetap tercentang" punya langkah observasi di TC dan diasersi lewat F5 (muat ulang sesi tanpa form dirty).
- Temuan untuk QA:
  - Post Condition TC-173 butir b dan c, TC-174 butir b dan c, serta TC-177 butir b (kolom Role di User List, Settings > Role & Permission) tidak punya langkah observasi di TC dan tidak diasersi.
