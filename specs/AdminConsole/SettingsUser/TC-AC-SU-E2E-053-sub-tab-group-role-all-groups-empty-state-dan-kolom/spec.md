---
id: TC-AC-SU-E2E-053-sub-tab-group-role-all-groups-empty-state-dan-kolom
title: "Sub-tab Group Role: All Groups, Role Tanpa Group, dan Kolom Tanpa Switch"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-198
  - TC-AC-SU-199
  - TC-AC-SU-200
  - TC-AC-SU-645
coverage:
  web: automated
---

# Sub-tab Group Role: All Groups, Role Tanpa Group, dan Kolom Tanpa Switch

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-053` tanpa tingkat akses dan bukan Group Manager; Group Role: `Manage partner` aktif di kelima group, `Manage allocation` tanpa group, `Manage active client` aktif di `Region A {runId}-053` (C ☑ R ☑ U ☐ D ☐).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-053`): `Region A {runId}-053` > `Branch 1 {runId}-053` > `Floor 1 {runId}-053`; `Region A {runId}-053` > `Branch 3 {runId}-053`; `Region B {runId}-053`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-053@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-053`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-053` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-198: Group Summary Badge: ter-assign ke semua group tampil All Groups

1. Ketik Search `Budi Santoso {runId}-053`, tekan Enter
2. Klik nama `Budi Santoso {runId}-053` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Amati kolom Group baris `Manage partner`
5. Verifikasi sel menampilkan badge tunggal `All Groups`, bukan 2 badge + `+N more`

### TC-AC-SU-645: Tab Group Role tidak punya kolom Active maupun switch di tiap baris

6. Amati header tabel
7. Verifikasi header: `Role Name`, `Group`, Actions (⋯)
8. Verifikasi tidak ada kolom `Active`
9. Klik header kolom Actions (⋯)
10. Verifikasi overlay Column Visibility hanya memuat `Role Name` dan `Group`
11. Tutup overlay dengan Esc
12. Amati baris `Manage active client` dan `Manage allocation`
13. Verifikasi tidak ada switch di baris mana pun
14. Verifikasi aksi baris hanya `[Detail]` dan `[Assign Group]`

### TC-AC-SU-199: Role tanpa group: tanpa switch, Group `—`, Detail dan Assign Group enabled, Detail menampilkan empty state

15. Amati baris `Manage allocation`
16. Verifikasi baris `Manage allocation` tidak punya switch
17. Verifikasi kolom Group baris `Manage allocation` = `—`
18. Hover `[Detail]` baris `Manage allocation`
19. Verifikasi `[Detail]` tampil dan enabled, tanpa tooltip
20. Hover `[Assign Group]` baris `Manage allocation`
21. Verifikasi `[Assign Group]` tampil dan enabled, tanpa tooltip
22. Klik `[Detail]` baris `Manage allocation`
23. Verifikasi popup Group Assignment (read-only) terbuka dengan subtitle `Manage allocation`
24. Verifikasi empty state Title `No groups assigned yet` + Description `This role has no group assignments.`
25. Tutup popup dengan `[×]`

### TC-AC-SU-200: Role dengan group: Detail menampilkan CRUD per group dan Assign Group enabled

26. Klik `[Detail]` baris `Manage active client`
27. Verifikasi popup Group Assignment terbuka dengan baris `Region A {runId}-053`: C ☑ R ☑ U ○ D ○
28. Tutup popup dengan `[×]`
29. Verifikasi `[Detail]` baris `Manage active client` enabled
30. Verifikasi `[Assign Group]` baris `Manage active client` enabled

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 11, 25, 28 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC di spec: 198, 645, 199, 200 (screening kolom lebih dulu, lalu popup read-only).
- Pembagian TC: TC-AC-SU-194, 195, 196, 197, 666 ada di spec 051 dan 052.
- Temuan untuk QA:
  - Post Condition TC-199 ("Role `Manage allocation` tidak dihitung di kolom Role User List Budi Santoso") tidak punya langkah observasi dan tidak diasersi; Expected TC-200 butir b dicek sesudah popup ditutup karena tombol berada di baris halaman.
