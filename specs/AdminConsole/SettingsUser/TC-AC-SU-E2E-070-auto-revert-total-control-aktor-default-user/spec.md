---
id: TC-AC-SU-E2E-070-auto-revert-total-control-aktor-default-user
title: "Auto-Revert Total Control: Dialog, Cancel, Tutup, dan Confirm oleh Default User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-249
  - TC-AC-SU-250
  - TC-AC-SU-251
  - TC-AC-SU-252
coverage:
  web: automated
---

# Auto-Revert Total Control: Dialog, Cancel, Tutup, dan Confirm oleh Default User

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Default User, `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DU_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Rina Putri {runId}-070` dengan tingkat akses Total Control; seluruh peran individual aktif CRUD penuh.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-070@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-070`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-070` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-249: Auto-Revert Total Control: dialog muncul saat uncheck Delete Global Role

1. Ketik Search `Rina Putri {runId}-070`, tekan Enter
2. Klik nama `Rina Putri {runId}-070` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Uncheck D baris `Manage TAG stock`
4. Verifikasi dialog muncul sebelum perubahan disimpan: Title `"Remove Total Control"` + `[×]`, body bullet `Rina Putri {runId}-070` + `"This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited."` + `"Are you sure you want to remove it?"`, tombol `[Cancel]` dan `[Remove]` (danger)
5. Klik `[Cancel]` pada dialog

### TC-AC-SU-250: Auto-Revert Total Control: Cancel mengembalikan checkbox

6. Uncheck D baris `Manage TAG stock`
7. Klik `[Cancel]`
8. Verifikasi dialog tertutup
9. Verifikasi D baris `Manage TAG stock` kembali `[☑]`
10. Verifikasi banner `"This user has Total Control access."` tetap tampil
11. Verifikasi tidak ada toast

### TC-AC-SU-251: Auto-Revert Total Control: tutup dialog via × setara Cancel

12. Uncheck D baris `Manage TAG stock`
13. Klik `[×]` di dialog
14. Verifikasi dialog tertutup
15. Verifikasi D baris `Manage TAG stock` kembali `[☑]`
16. Verifikasi tidak ada toast

### TC-AC-SU-252: Auto-Revert Total Control: Confirm melepas tier dan menyimpan edit

17. Uncheck D baris `Manage TAG stock`
18. Klik `[Remove]`
19. Verifikasi muncul toast sukses: `"Success, permissions have been updated. Rina Putri {runId}-070 is no longer Total Control."`
20. Verifikasi banner Total Control hilang dari Tab Role
21. Verifikasi D baris `Manage TAG stock` tetap `[☐]`
22. Verifikasi baris `Manage group` tetap C/R/U/D `[☑]` (role individual lain tidak berubah)
23. Kembali ke User List via breadcrumb
24. Verifikasi kolom Role baris `Rina Putri {runId}-070` tidak lagi menampilkan badge `Total Control`, melainkan label jumlah role aktif

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 5 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Aktor Default User login di hook `before` (Pre-setup #1); target `Rina Putri {runId}-070` adalah user seed milik spec.
- TC-249 ditutup dengan `[Cancel]` sebagai langkah penghubung; TC-250 dan TC-251 mengulang uncheck karena dialog ditutup di TC sebelumnya (S-04, S-09). TC-252 ditaruh terakhir karena melepas tier.
- Pembagian TC: TC-AC-SU-253 sampai 256 (aktor Total Control) ada di spec 071.
- Temuan untuk QA:
  - Post Condition TC-252 (tingkat akses, Role & Permission, notifikasi in-app, log Auto-Revert) tidak punya langkah observasi dan tidak diasersi.
  - Expected TC-252 butir d tidak menyebut label jumlah role aktif secara persis; spec mengasersi bahwa badge `Total Control` diganti label jumlah role.
  - TC-252 menyebut "Langkah 5" padahal hanya ada empat langkah; spec mengasersi kolom Role sesudah kembali ke User List.
