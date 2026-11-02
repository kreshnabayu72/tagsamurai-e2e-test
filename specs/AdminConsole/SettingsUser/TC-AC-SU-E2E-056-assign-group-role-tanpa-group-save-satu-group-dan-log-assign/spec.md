---
id: TC-AC-SU-E2E-056-assign-group-role-tanpa-group-save-satu-group-dan-log-assign
title: "Assign Group pada Role Tanpa Group: Save Satu Group dan Changelog Assign"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-202
coverage:
  web: automated
---

# Assign Group pada Role Tanpa Group: Save Satu Group dan Changelog Assign

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-056` tanpa tingkat akses dan bukan Group Manager; `Manage allocation` tanpa group assignment.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-056`): `Region A {runId}-056` > `Branch 1 {runId}-056` > `Floor 1 {runId}-056`; `Region A {runId}-056` > `Branch 3 {runId}-056`; `Region B {runId}-056`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-056@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-056`.
- Kemampuan baca jumlah baris Modal Changelog: User > Group Role (baseline sebelum aksi; audit trail permanen, bagian 8b butir 10) disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-056` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-202: Assign Group pada role tanpa group: Save dengan 1 group mengaktifkan role dan menulis log Assign

1. Ketik Search `Budi Santoso {runId}-056`, tekan Enter
2. Klik nama `Budi Santoso {runId}-056` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik icon Changelog toolbar sub-tab Group Role
5. Catat jumlah baris `Assign` untuk `Manage allocation` pada Modal Changelog: User > Group Role sebagai baseline
6. Tutup modal Changelog dengan `✕`
7. Klik `[Assign Group]` baris `Manage allocation`
8. Klik `[+ Assign Group]`
9. Centang `Region A {runId}-056` di Popup Select Group, klik `[Select]`
10. Klik `[Save]`
11. Verifikasi popup tertutup
12. Verifikasi kolom Group `Manage allocation` menampilkan badge `Region A {runId}-056`, menandai role aktif
13. Verifikasi muncul toast sukses: "Success, group role has been assigned."
14. Klik icon Changelog toolbar sub-tab Group Role
15. Verifikasi Modal Changelog: User > Group Role memuat 1 baris `Assign` baru untuk `Manage allocation` pada `Region A {runId}-056` (selisih +1 dari baseline)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Baseline (S-12): Changelog adalah audit trail permanen sehingga "1 baris `Assign`" diasersi sebagai selisih terhadap baseline yang dicatat sebelum Save.
- Pembagian TC: TC-AC-SU-201, 203, 204 ada di spec 055.
- Temuan untuk QA:
  - Expected TC-202 butir b memuat "role aktif" tanpa elemen UI terpisah (Group Role tidak punya switch); spec memakai badge Group sebagai penanda satu `Verifikasi`.
  - Post Condition TC-202 ("Assignment Region A tersimpan dengan R saja", "Kolom Role User List bertambah 1") tidak punya langkah observasi dan tidak diasersi.
