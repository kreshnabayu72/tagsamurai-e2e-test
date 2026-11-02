---
id: TC-AC-SU-E2E-055-assign-group-role-tanpa-group-popup-awal-tutup-dan-leave
title: "Assign Group pada Role Tanpa Group: Popup Awal, Tutup Bersih, dan Tutup Dirty"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-201
  - TC-AC-SU-203
  - TC-AC-SU-204
coverage:
  web: automated
---

# Assign Group pada Role Tanpa Group: Popup Awal, Tutup Bersih, dan Tutup Dirty

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-055` tanpa tingkat akses dan bukan Group Manager; `Manage allocation` tanpa group assignment.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-055`): `Region A {runId}-055` > `Branch 1 {runId}-055` > `Floor 1 {runId}-055`; `Region A {runId}-055` > `Branch 3 {runId}-055`; `Region B {runId}-055`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-055@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-055`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-055` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-201: Klik Assign Group pada role tanpa group: popup terbuka dengan tabel kosong

1. Ketik Search `Budi Santoso {runId}-055`, tekan Enter
2. Klik nama `Budi Santoso {runId}-055` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage allocation`
5. Verifikasi popup `"Assign Group Role — Manage allocation"` terbuka dengan tabel kosong
6. Verifikasi empty state Title `No groups assigned yet` + Description `Click [+ Assign Group] to add a group.`
7. Verifikasi tidak ada toast
8. Klik `[×]`
9. Verifikasi kolom Group baris `Manage allocation` tetap `—`

### TC-AC-SU-203: Tutup popup bersih via × tidak mengubah apa pun

10. Klik `[Assign Group]` baris `Manage allocation`
11. Tanpa mengubah apa pun, klik `[×]` di popup
12. Verifikasi popup langsung tertutup tanpa dialog Unsaved Changes
13. Verifikasi kolom Group baris `Manage allocation` tetap `—`
14. Verifikasi tidak ada toast

### TC-AC-SU-204: Tutup popup dirty lalu Leave tidak menyimpan apa pun

15. Klik `[Assign Group]` baris `Manage allocation`
16. Klik `[+ Assign Group]`
17. Centang `Region A {runId}-055` di Popup Select Group, klik `[Select]`
18. Tekan Esc
19. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
20. Klik `[Leave]`
21. Verifikasi popup tertutup
22. Verifikasi kolom Group baris `Manage allocation` tetap `—`
23. Verifikasi tidak ada toast

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-202 (Save pertama pada role tanpa group) ada di spec 056.
- Temuan untuk QA:
  - Expected TC-201 butir b ("tetap `—` selama belum ada Save") diamati sesudah popup ditutup lewat `[×]`, karena kolom berada di balik popup.
  - Post Condition TC-203 dan TC-204 tidak punya langkah observasi tersendiri; dialog `Unsaved Changes` pada TC-204 diasersi menurut S-08.
