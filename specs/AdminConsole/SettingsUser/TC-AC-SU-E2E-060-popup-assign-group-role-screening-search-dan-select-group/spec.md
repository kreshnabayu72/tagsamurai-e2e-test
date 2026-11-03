---
id: TC-AC-SU-E2E-060-popup-assign-group-role-screening-search-dan-select-group
title: "Popup Assign Group Role: Screening, Search Group, dan Popup Select Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-214
  - TC-AC-SU-215
  - TC-AC-SU-216
  - TC-AC-SU-217
coverage:
  web: automated
---

# Popup Assign Group Role: Screening, Search Group, dan Popup Select Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-060` tanpa tingkat akses dan bukan Group Manager; `Manage wallet & pricing` aktif di `Region A {runId}-060` (C ☑ R ☑ U ☑) dan `Branch 3 {runId}-060` (R saja); `Manage partner` aktif di `Region A {runId}-060` saja.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-060`): `Region A {runId}-060` > `Branch 1 {runId}-060` > `Floor 1 {runId}-060`; `Region A {runId}-060` > `Branch 3 {runId}-060`; `Region B {runId}-060`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-060@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-060`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-060` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-214: Screening Popup Assign Group Role dari row action Assign Group

1. Ketik Search `Budi Santoso {runId}-060`, tekan Enter
2. Klik nama `Budi Santoso {runId}-060` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage wallet & pricing`
5. Verifikasi title popup: `"Assign Group Role — Manage wallet & pricing"`
6. Verifikasi icon `[×]` di kanan atas popup
7. Verifikasi toolbar: Search placeholder `"Search groups..."` | `[+ Assign Group]`
8. Verifikasi kolom tabel: `Group | C | R | U | D | Actions (⋯)`
9. Verifikasi header Actions (⋯) = trigger Column Visibility, body Actions berisi `[🗑]`
10. Verifikasi tabel tanpa pagination
11. Verifikasi baris `Region A {runId}-060`: C `[☑]`, R `[☑]` disabled, U `[☑]`, D `—`, `[🗑]`
12. Verifikasi baris `Branch 3 {runId}-060`: C `[☐]`, R `[☑]` disabled, U `[☐]`, D `—`, `[🗑]`
13. Verifikasi footer: `[Clear Field]` (Text, Primary) | `[Save]` (Success)

### TC-AC-SU-215: Search di Popup Assign Group Role memfilter baris group

14. Ketik Search `branch`, tekan Enter
15. Verifikasi hanya baris `Branch 3 {runId}-060` tampil (case-insensitive)
16. Ganti isi kotak search dengan `zzz`, tekan Enter
17. Verifikasi tabel tanpa baris dengan empty state `"No results found"` + `"Try adjusting your search or filter."`
18. Tutup popup dengan `[×]`

### TC-AC-SU-216: Screening Popup Select Group dan exact match per node

19. Klik `[Assign Group]` baris `Manage partner`
20. Klik `[+ Assign Group]`
21. Verifikasi title Popup Select Group `"Select Group"` + `[×]`
22. Verifikasi Search placeholder `"Search groups..."`
23. Verifikasi tree penuh: `Region A {runId}-060` (disabled, sudah ter-assign), `Branch 1 {runId}-060`, `Floor 1 {runId}-060`, `Branch 3 {runId}-060`, `Region B {runId}-060`
24. Verifikasi footer `[Cancel]` (Text, Contrast) | `[Select]` disabled sebelum ada centang
25. Centang `Branch 1 {runId}-060`
26. Verifikasi centang `Branch 1 {runId}-060` tidak ikut mencentang `Floor 1 {runId}-060` (exact match per node)
27. Verifikasi `[Select]` menjadi enabled
28. Klik `[Cancel]` di Popup Select Group

### TC-AC-SU-217: Hover node yang sudah ter-assign di Popup Select Group

29. Klik `[+ Assign Group]`
30. Hover node `Region A {runId}-060`
31. Verifikasi tooltip `"This group is already assigned to this role."`
32. Klik checkbox `Region A {runId}-060`
33. Verifikasi checkbox `Region A {runId}-060` tidak bisa dicentang
34. Klik `[Cancel]` di Popup Select Group, lalu `[×]` pada Popup Assign Group Role

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 18, 34 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-218 sampai 221 ada di spec 061.
- Search `branch` pada TC-215 hanya cocok dengan `Branch 3 {runId}-060`; nama uji tidak memuat kata `branch` lain (R-13). Pembanding "sedikitnya satu baris" untuk asersi hasil tersaring dipenuhi `Verifikasi` baris `Region A {runId}-060` dan `Branch 3 {runId}-060` pada TC-214 (data yang sama).
- Alasan spec melewati sekitar 35 langkah: seluruh TC memakai satu permukaan (Popup Assign Group Role dan Select Group) dan berdiri sendiri; tiap TC membuka dan menutup popup sendiri tanpa perubahan data tersimpan, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-214 mencantumkan gaya tombol footer (Text Primary, Success) tanpa cara pengamatan; diasersi sebagai bagian satu `Verifikasi` pasangan tombol footer (S-01).
