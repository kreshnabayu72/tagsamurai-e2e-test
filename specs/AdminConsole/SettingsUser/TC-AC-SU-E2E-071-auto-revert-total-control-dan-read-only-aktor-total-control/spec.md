---
id: TC-AC-SU-E2E-071-auto-revert-total-control-dan-read-only-aktor-total-control
title: "Auto-Revert Total Control dan Read Only: Pemicu Checkbox, Switch, dan Save Popup oleh Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-256
  - TC-AC-SU-253
  - TC-AC-SU-254
  - TC-AC-SU-255
coverage:
  web: automated
---

# Auto-Revert Total Control dan Read Only: Pemicu Checkbox, Switch, dan Save Popup oleh Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Rina Putri {runId}-071 C` (Total Control; peran individual aktif CRUD penuh; TC-256), `Andi Wijaya {runId}-071` (Read Only; TC-253), `Rina Putri {runId}-071` (Total Control; TC-254), `Rina Putri {runId}-071 B` (Total Control; `Manage partner` aktif di `Region A {runId}-071` dengan U ☑; TC-255).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-071`): `Region A {runId}-071` > `Branch 1 {runId}-071` > `Floor 1 {runId}-071`; `Region A {runId}-071` > `Branch 3 {runId}-071`; `Region B {runId}-071`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-071@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-071`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-071` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-256: Edit target Total Control yang tetap sesuai pola: tanpa dialog Auto-Revert

1. Ketik Search `Rina Putri {runId}-071 C`, tekan Enter
2. Klik nama `Rina Putri {runId}-071 C` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik checkbox D baris `Manage TAG stock` (uncheck)
4. Verifikasi dialog Auto-Revert muncul (pola menyimpang)
5. Klik `[Cancel]`
6. Amati banner
7. Verifikasi banner Total Control tetap tampil
8. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-253: Auto-Revert Read Only: dialog dan Confirm saat mencentang Create

9. Ketik Search `Andi Wijaya {runId}-071`, tekan Enter
10. Klik nama `Andi Wijaya {runId}-071` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
11. Centang C baris `Manage group`
12. Verifikasi dialog Title `"Remove Read Only"`, body bullet `Andi Wijaya {runId}-071` + `"This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited."` + `"Are you sure you want to remove it?"`, tombol `[Cancel]` `[Remove]`
13. Klik `[Remove]`
14. Verifikasi toast `"Success, permissions have been updated. Andi Wijaya {runId}-071 is no longer Read Only."`
15. Verifikasi banner Read Only hilang
16. Verifikasi C baris `Manage group` tetap `[☑]`
17. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-254: Auto-Revert Total Control dipicu switch Global Role OFF

18. Ketik Search `Rina Putri {runId}-071`, tekan Enter
19. Klik nama `Rina Putri {runId}-071` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
20. Klik switch baris `Manage language` ke OFF
21. Verifikasi dialog `"Remove Total Control"` muncul sebelum switch tersimpan
22. Klik `[Remove]`
23. Verifikasi switch `Manage language` OFF
24. Verifikasi banner Total Control hilang
25. Verifikasi toast `"Success, permissions have been updated. Rina Putri {runId}-071 is no longer Total Control."`
26. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-255: Auto-Revert Total Control dipicu Save popup Assign Group Role

27. Tunggu toast lama hilang otomatis
28. Ketik Search `Rina Putri {runId}-071 B`, tekan Enter
29. Klik nama `Rina Putri {runId}-071 B` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
30. Klik Sub-tab [Group Role]
31. Klik `[Assign Group]` baris `Manage partner`
32. Uncheck U baris `Region A {runId}-071`
33. Klik `[Save]`
34. Verifikasi dialog `"Remove Total Control"` muncul saat Save
35. Klik `[Remove]`
36. Verifikasi popup tertutup
37. Verifikasi banner Total Control hilang
38. Verifikasi toast `"Success, permissions have been updated. Rina Putri {runId}-071 B is no longer Total Control."`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 8, 9, 17, 18, 26, 27, 28 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC di spec: 256 (tanpa menyimpan), 253, 254, 255; TC yang melepas tier memakai user sendiri karena tier tidak dapat dikembalikan dalam spec.
- Pembagian TC: TC-AC-SU-249 sampai 252 (aktor Default User) ada di spec 070.
- Temuan untuk QA:
  - Expected TC-256 ("Dialog hanya muncul saat pola menyimpang") tidak merinci; spec mengasersi dialog tampil saat uncheck D dan banner tetap setelah Cancel. Judul TC ("tanpa dialog Auto-Revert") bertentangan dengan Expected-nya yang menyebut dialog; spec mengikuti Expected.
  - Post Condition TC-253, 254, 255 (tingkat akses, notifikasi in-app, assignment tersimpan) tidak punya langkah observasi dan tidak diasersi.
  - Nama `Rina Putri {runId}-071 B` muncul di toast TC-255 sebagai nama bersuffix.
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada permukaan dan kelas harness yang sama dan berdiri sendiri (target user milik spec per TC); kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian langkah hanya penghubung (pencarian target dan kembali ke User List).
