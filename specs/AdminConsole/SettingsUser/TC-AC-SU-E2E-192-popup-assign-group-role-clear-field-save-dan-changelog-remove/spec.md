---
id: TC-AC-SU-E2E-192-popup-assign-group-role-clear-field-save-dan-changelog-remove
title: "Popup Assign Group Role: Clear Field Lalu Save Melepas Role dan Mencatat Remove per Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-229
coverage:
  web: automated
---

# Popup Assign Group Role: Clear Field Lalu Save Melepas Role dan Mencatat Remove per Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-192` tanpa tingkat akses dan bukan Group Manager dengan `Manage partner` aktif di `Region A {runId}-192` dan `Region B {runId}-192`.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-192`): `Region A {runId}-192` > `Branch 1 {runId}-192` > `Floor 1 {runId}-192`; `Region A {runId}-192` > `Branch 3 {runId}-192`; `Region B {runId}-192`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-192@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-192`.
- Kemampuan baca jumlah baris Modal Changelog: User > Group Role (baseline sebelum aksi; audit trail permanen, bagian 8b butir 10) disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-192` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-229: Clear Field lalu Save: role dengan 2 group dilepas dan log Remove per group

1. Ketik Search `Budi Santoso {runId}-192`, tekan Enter
2. Klik nama `Budi Santoso {runId}-192` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik icon Changelog toolbar sub-tab Group Role
5. Catat jumlah baris `Remove` untuk `Manage partner` pada Modal Changelog: User > Group Role sebagai baseline
6. Tutup modal Changelog dengan `✕`
7. Klik `[Assign Group]` baris `Manage partner`
8. Klik `[Clear Field]`
9. Verifikasi tabel popup kosong dengan empty state Title `No groups assigned yet` + Description `Click [+ Assign Group] to add a group.`
10. Klik `[Save]`
11. Verifikasi tersimpan tanpa dialog konfirmasi
12. Verifikasi popup tertutup
13. Verifikasi muncul toast sukses: "Success, group role has been updated."
14. Verifikasi kolom Group `Manage partner` = `—`
15. Klik icon Changelog toolbar sub-tab Group Role
16. Verifikasi Modal Changelog: User > Group Role memuat 2 baris `Remove` baru untuk `Manage partner` (`Region A {runId}-192` dan `Region B {runId}-192`) sebagai selisih +2 dari baseline

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-226, 227, 228 (Save tanpa perubahan, Clear Field, Save tabel kosong) ada di spec 063.
- Baseline (S-12): Changelog adalah audit trail permanen sehingga "2 baris `Remove`" diasersi sebagai selisih terhadap baseline yang dicatat sebelum Save.
- Temuan untuk QA:
  - Post Condition TC-229 ("Role `Manage partner` tidak aktif untuk Budi Santoso") tidak punya langkah observasi tersendiri; kolom Group `—` pada Expected butir b menjadi padanannya.
