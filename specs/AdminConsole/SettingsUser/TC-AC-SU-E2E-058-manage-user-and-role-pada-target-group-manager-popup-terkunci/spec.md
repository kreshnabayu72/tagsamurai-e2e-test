---
id: TC-AC-SU-E2E-058-manage-user-and-role-pada-target-group-manager-popup-terkunci
title: "Aktor Manage user and role pada Target Group Manager: Baris Group GM Terkunci di Popup"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-209
  - TC-AC-SU-242
  - TC-AC-SU-243
coverage:
  web: automated
---

# Aktor Manage user and role pada Target Group Manager: Baris Group GM Terkunci di Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user and role (Update aktif), `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Dedi Kurnia {runId}-058` (Group Manager di `Region A {runId}-058`); Group Role: `Manage partner` aktif di `Region A {runId}-058` (CRUD penuh) dan `Region B {runId}-058` (R saja), `Manage active client` aktif di `Region A {runId}-058` (materialisasi Group Manager), `Manage wallet & pricing` hanya di `Region B {runId}-058` (di luar Group Manager).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-058`): `Region A {runId}-058` > `Branch 1 {runId}-058` > `Floor 1 {runId}-058`; `Region A {runId}-058` > `Branch 3 {runId}-058`; `Region B {runId}-058`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-058@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-058`.
- Env var `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan pemilik repo.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-058` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-209: Aktor Manage user and role pada target Group Manager: hanya baris/CRUD group GM di popup yang terkunci

1. Ketik Search `Dedi Kurnia {runId}-058`, tekan Enter
2. Klik nama `Dedi Kurnia {runId}-058` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Verifikasi banner `"This user is a Group Manager for: Region A {runId}-058."` tampil
5. Verifikasi Sub-tab Group Role tanpa switch
6. Verifikasi `[Assign Group]` enabled di semua baris
7. Verifikasi `[Detail]` enabled di semua baris
8. Klik `[Assign Group]` baris `Manage active client`
9. Hover checkbox C baris `Region A {runId}-058`
10. Verifikasi checkbox CRUD baris `Region A {runId}-058` tampil namun disabled
11. Verifikasi tooltip `"You don't have permission to edit."` pada CRUD
12. Hover `[🗑]` baris `Region A {runId}-058`
13. Verifikasi `[🗑]` baris `Region A {runId}-058` tampil namun disabled
14. Verifikasi tooltip `"You don't have permission to edit."` pada `[🗑]`
15. Tutup popup dengan `[×]`
16. Klik `[Assign Group]` baris `Manage wallet & pricing`
17. Verifikasi baris `Region B {runId}-058` editable (tidak ada baris group GM yang terkunci)
18. Tutup popup dengan `[×]`

### TC-AC-SU-243: Aktor Manage user and role pada target Group Manager: node group GM disabled di Select Group

19. Klik `[Assign Group]` baris `Manage partner`
20. Klik `[+ Assign Group]`
21. Hover node `Region A {runId}-058`
22. Verifikasi node `Region A {runId}-058` disabled dengan tooltip `"This group is already assigned to this role."`
23. Verifikasi node `Branch 1 {runId}-058`, `Floor 1 {runId}-058`, dan `Branch 3 {runId}-058` (belum ter-assign) enabled
24. Klik `[Cancel]` di Popup Select Group, lalu `[×]` pada popup

### TC-AC-SU-242: Aktor Manage user and role pada target Group Manager: baris group GM terkunci di popup

25. Klik `[Assign Group]` baris `Manage partner` (tombol enabled)
26. Verifikasi popup Assign Group Role terbuka
27. Hover checkbox C baris `Region A {runId}-058`
28. Verifikasi checkbox CRUD baris `Region A {runId}-058` tampil namun disabled
29. Verifikasi tooltip `"You don't have permission to edit."` pada CRUD
30. Hover `[🗑]` baris `Region A {runId}-058`
31. Verifikasi `[🗑]` baris `Region A {runId}-058` tampil namun disabled
32. Verifikasi tooltip `"You don't have permission to edit."` pada `[🗑]`
33. Centang C baris `Region B {runId}-058`
34. Verifikasi baris `Region B {runId}-058` editable
35. Klik `[Clear Field]`
36. Verifikasi baris `Region B {runId}-058` terhapus dari tabel popup
37. Verifikasi baris `Region A {runId}-058` tetap ada
38. Klik `✕` pada popup
39. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
40. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 15, 18, 24 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC di spec: 209, 243, 242 (TC-242 mengubah isi popup dan ditutup lewat Unsaved Changes `[Leave]`).
- Pembagian TC: TC-AC-SU-213 dan 244 ada di spec 059.
- Temuan untuk QA:
  - Data TC-209 saling bertentangan: "semua Group Role aktif di Region A" sedangkan "`Manage wallet & pricing` hanya di Region B". Spec mengikuti butir khusus TC (wallet & pricing hanya di `Region B {runId}-058`).
  - TC-209 butir b menyebut "`[Assign Group]` dan `[Detail]` enabled di semua baris"; spec menulis satu `Verifikasi` per tombol.
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada permukaan dan kelas harness yang sama dan berdiri sendiri (target user milik spec per TC); kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian langkah hanya penghubung (pencarian target dan kembali ke User List).
