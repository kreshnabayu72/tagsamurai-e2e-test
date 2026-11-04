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
4. Verifikasi muncul toast sukses: "Success, role has been updated."
5. Verifikasi switch `Manage language` berubah ON
6. Verifikasi tidak ada popup
7. Verifikasi checkbox R baris `Manage language` tercentang dan disabled
8. Verifikasi checkbox C baris `Manage language` unchecked dan enabled (yang applicable)
9. Verifikasi checkbox U baris `Manage language` unchecked dan enabled (yang applicable)
10. Verifikasi checkbox D baris `Manage language` unchecked dan enabled (yang applicable)
11. Tunggu toast lama hilang otomatis

### TC-AC-SU-174: Switch Global Role ON ke OFF mengunci CRUD dan menyimpan nilai inactive

12. Klik switch baris `Manage group`
13. Verifikasi switch `Manage group` berubah OFF
14. Verifikasi C/R/U/D baris `Manage group` tampil `[─]` terkunci (disabled)
15. Verifikasi muncul toast sukses: "Success, role has been updated."
16. Tunggu toast lama hilang otomatis

### TC-AC-SU-175: Switch Global Role OFF ke ON kembali memulihkan CRUD sebelumnya

17. Klik switch baris `Manage group`
18. Verifikasi muncul toast sukses: "Success, role has been updated."
19. Verifikasi switch `Manage group` ON tanpa popup
20. Verifikasi checkbox C baris `Manage group` kembali `[☐]`
21. Verifikasi checkbox R baris `Manage group` kembali `[☑]` disabled
22. Verifikasi checkbox U baris `Manage group` kembali `[☑]`
23. Verifikasi checkbox D baris `Manage group` kembali `[☑]` (bukan default R saja)
24. Tunggu toast lama hilang otomatis

### TC-AC-SU-177: Autosave centang Create pada Global Role aktif

25. Centang C baris `Manage device master data`
26. Verifikasi checkbox C baris `Manage device master data` tercentang tanpa tombol Save
27. Verifikasi muncul toast sukses: "Success, permissions have been updated."
28. Muat ulang halaman dengan F5
29. Verifikasi checkbox C baris `Manage device master data` tetap tercentang

### TC-AC-SU-178: Autosave uncheck Update dan Delete satu per satu pada Global Role aktif

30. Uncheck U baris `Manage group`
31. Verifikasi muncul toast sukses: "Success, permissions have been updated."
32. Tunggu toast lama hilang otomatis
33. Uncheck D baris `Manage group`
34. Verifikasi muncul toast sukses: "Success, permissions have been updated." (satu toast per perubahan)
35. Verifikasi U baris `Manage group` tampil `[☐]`
36. Verifikasi D baris `Manage group` tampil `[☐]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 11, 16, 24, 28, 32 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Verifikasi toast sukses diletakkan tepat sesudah klik switch (langkah 4 dan 18), sebelum asersi switch, popup, dan checkbox, supaya toast yang bersifat sementara tertangkap; "Tunggu toast lama hilang otomatis" tetap di akhir blok.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Ukuran spec (36 langkah, di atas smell sekitar 35 langkah): satu sub-tab Global Role pada satu user seed; lima TC berurutan pada `Manage group` (TC-175 dan TC-178 bergantung pada TC-174) dan tiap checkbox C, R, U, D diasersi satu `Verifikasi` per klausa (S-01), sehingga langkah bertambah tanpa pindah permukaan.
- TC-175 bergantung pada TC-174 (Dependensi TC); keduanya berurutan pada role `Manage group`. TC-178 mengandalkan `Manage group` ON dengan U dan D tercentang, yang dipulihkan TC-175.
- TC-177 butir Post "refresh halaman: C tetap tercentang" punya langkah observasi di TC dan diasersi lewat F5 (muat ulang sesi tanpa form dirty).
- Temuan untuk QA:
  - Post Condition TC-173 butir b dan c, TC-174 butir b dan c, serta TC-177 butir b (kolom Role di User List, Settings > Role & Permission) tidak punya langkah observasi di TC dan tidak diasersi.
