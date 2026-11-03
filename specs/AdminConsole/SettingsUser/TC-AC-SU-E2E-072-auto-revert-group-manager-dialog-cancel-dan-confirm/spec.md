---
id: TC-AC-SU-E2E-072-auto-revert-group-manager-dialog-cancel-dan-confirm
title: "Auto-Revert Group Manager: Dialog Save Popup, Cancel, dan Confirm Melepas Status Satu Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-257
  - TC-AC-SU-258
  - TC-AC-SU-259
coverage:
  web: automated
---

# Auto-Revert Group Manager: Dialog Save Popup, Cancel, dan Confirm Melepas Status Satu Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Dedi Kurnia {runId}-072` (Group Manager di `Region A {runId}-072` dan `Region B {runId}-072`); `Manage distributor` aktif di `Region A {runId}-072` dan `Region B {runId}-072` (CRUD penuh).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-072`): `Region A {runId}-072` > `Branch 1 {runId}-072` > `Floor 1 {runId}-072`; `Region A {runId}-072` > `Branch 3 {runId}-072`; `Region B {runId}-072`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-072@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-072`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-072` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-257: Auto-Revert Group Manager: dialog saat Save popup yang mengurangi CRUD group GM

1. Ketik Search `Dedi Kurnia {runId}-072`, tekan Enter
2. Klik nama `Dedi Kurnia {runId}-072` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage distributor`
5. Uncheck D baris `Region A {runId}-072`
6. Klik `[Save]`
7. Verifikasi dialog Title `"Remove Group Manager"`, body bullet `Dedi Kurnia {runId}-072` + `"This edit will remove Group Manager status for this group. Their role permissions in this group will remain as edited."` + `"Are you sure you want to remove it?"`, tombol `[Cancel]` `[Remove]`
8. Klik `[Cancel]` pada dialog
9. Klik `✕` pada popup
10. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
11. Klik `[Leave]`

### TC-AC-SU-258: Auto-Revert Group Manager: Cancel kembali ke popup dengan isi utuh

12. Klik `[Assign Group]` baris `Manage distributor`
13. Uncheck D baris `Region A {runId}-072`
14. Klik `[Save]`
15. Klik `[Cancel]`
16. Verifikasi dialog Auto-Revert tertutup
17. Verifikasi popup tetap terbuka dengan D baris `Region A {runId}-072` tetap `[☐]`
18. Verifikasi tidak ada toast
19. Klik `✕` pada popup
20. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
21. Klik `[Leave]`

### TC-AC-SU-259: Auto-Revert Group Manager: Confirm melepas status GM group itu

22. Klik `[Assign Group]` baris `Manage distributor`
23. Uncheck D baris `Region A {runId}-072`
24. Klik `[Save]`
25. Klik `[Remove]`
26. Verifikasi popup tertutup
27. Verifikasi toast `"Success, permissions have been updated. Dedi Kurnia {runId}-072 is no longer Group Manager."`
28. Verifikasi banner berubah menjadi `"This user is a Group Manager for: Region B {runId}-072."`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 8 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-260 dan 644 ada di spec 073.
- TC-257 dan TC-258 membuka popup dua kali karena TC-257 mengakhiri popup dalam keadaan dirty yang ditutup lewat Unsaved Changes `[Leave]` (S-08); TC-259 terakhir karena melepas status GM.
- Alasan spec melewati sekitar 35 langkah: seluruh TC memakai satu permukaan (Save popup Assign Group Role pada target Group Manager) dan berurutan pada user yang sama; langkah ulang hanya pembuka popup, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-257 dan TC-258 menulis target "Group Manager di Region A" (satu group) sedangkan TC-259 memakai Region A dan Region B; spec memakai satu user GM di kedua group untuk ketiga TC.
  - Post Condition TC-259 (status GM, Role & Permission Tab Group Manager, notifikasi in-app) tidak punya langkah observasi dan tidak diasersi.
