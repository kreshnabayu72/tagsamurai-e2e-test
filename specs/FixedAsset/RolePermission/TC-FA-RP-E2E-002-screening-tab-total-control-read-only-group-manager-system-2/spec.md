---
id: TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2
title: "Screening Tab Total Control, Read Only, Group Manager, System, dan loading state (2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-12
  - TC-FA-RP-13
  - TC-FA-RP-14
  - TC-FA-RP-73
  - TC-FA-RP-74
coverage:
  web: automated
---

# Screening Tab Total Control, Read Only, Group Manager, System, dan loading state (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna; Budi Santoso dan Endah Susanti dipakai TC-FA-RP-14), #36 (baris Tab Total Control). Hook `before` memastikan lewat sesi API aktor bahwa Budi Santoso dan Endah Susanti belum memegang `Manage files` maupun `Manage accounting` (precondition TC-FA-RP-14).
- Data Dinamis (dibuat pada langkah 21, dicabut di hook `after`): penugasan Budi Santoso pada `Manage files` di `Head Office` dan `IT Infrastructure`; penugasan Endah Susanti pada `Manage accounting` dengan peran dimatikan (inactive-retained).
- Baseline kolom Users: nilai kolom Users baris `Manage files` (section Group Role) dan baris `Manage accounting` (section Global Role) dibaca pada langkah 20 sebelum seeding; asersi memakai selisih terhadap baseline, bukan angka absolut.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama pengguna ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor (lihat `suite.md`); membaca nilai kolom Users sebagai baseline; hover untuk tooltip header.
- Pemulihan: penugasan Budi Santoso dan Endah Susanti dicabut di hook `after`; Pre-setup bersama lain tidak diubah.

## Test Steps

### TC-FA-RP-12: Screening Tab System saat dibuka (3 zona dan dua section)

1. Klik Tab `System`
2. Verifikasi Breadcrumb tampil `Settings > Role & Permission > System`
3. Verifikasi Tab tampil berurutan `Total Control | Read Only | Group Manager | Transaction Role | System (aktif)`
4. Verifikasi Table Tools tampil `Search | Download | Changelog`
5. Verifikasi section `Global Role` tampil dengan deskripsi `This role applies globally, regardless of the group assigned to the user.`
6. Verifikasi section `Group Role` tampil dengan deskripsi `This role only applies within the groups assigned to the user and their sub-groups.`
7. Verifikasi tiap section berkolom `Role Name (unsortable) | Users (unsortable) | Column Visibility (⋯)`
8. Verifikasi tidak ada pagination
9. Verifikasi seluruh role tampil pada kedua section
10. Verifikasi tidak ada `[+ Assign]`, Filter, `+ Add Role`, Edit, maupun Delete role

### TC-FA-RP-13: Urutan Role Name A-Z per section

11. Verifikasi section Global Role berurutan: 1. `Import data`; 2. `Manage accounting`; 3. `Manage asset ID configuration`; 4. `Manage asset master data`; 5. `Manage asset transactional policy`; 6. `Manage global license`; 7. `Manage global user & role`; 8. `Manage Open API`; 9. `Manage transaction settings`
12. Verifikasi section Group Role berurutan: 1. `Manage asset & TAG`; 2. `Manage asset license`; 3. `Manage files`; 4. `Manage group`; 5. `Manage purchase`; 6. `Manage user & role`; 7. `View asset value`

### TC-FA-RP-73: Katalog role tanpa Add Role, Edit, Rename, atau Delete

13. Verifikasi toolbar hanya `Search | Download | Changelog`
14. Verifikasi tidak ada tombol `+ Add Role`
15. Klik `[⋯]` pada baris pertama section Global Role
16. Verifikasi menu `[⋯]` hanya memuat `Detail`, tanpa Edit, Rename, maupun Delete
17. Tutup menu `[⋯]` dengan Esc
18. Klik `[⋯]` pada baris pertama section Group Role
19. Verifikasi menu `[⋯]` hanya memuat `Detail`, tanpa Edit, Rename, maupun Delete

### TC-FA-RP-14: Kolom Users menghitung user distinct dengan penugasan aktif

20. Catat nilai kolom Users baris `Manage files` pada section Group Role dan baris `Manage accounting` pada section Global Role sebagai baseline
21. Lewat sesi API aktor, tetapkan Budi Santoso pada `Manage files` di `Head Office` dan `IT Infrastructure`, tetapkan Endah Susanti pada `Manage accounting`, lalu matikan peran `Manage accounting` milik Endah Susanti (inactive-retained) hingga tersimpan; muat ulang Tab `System`
22. Verifikasi kolom Users baris `Manage files` bertambah 1 dari baseline (Budi Santoso dengan dua penugasan group dihitung 1 user)
23. Verifikasi kolom Users baris `Manage accounting` sama dengan baseline (Endah Susanti inactive-retained tidak dihitung)
24. Verifikasi kolom Users baris Group Role selain `Manage user & role` mencakup user Total Control, Read Only, dan Default User pemegang baris pola Group Role (dihitung per user distinct, bukan per baris)
25. Verifikasi tidak ada baris Group Role selain `Manage user & role` yang menampilkan `0` pada company yang memiliki Default User (`Manage user & role` dikecualikan dari pola, `FARP-LOGIC-04b`/`24`, dan hanya menghitung penugasan individual)

### TC-FA-RP-74: Screening overlay Column Visibility tabel Tab Total Control

26. Klik Tab `Total Control`
27. Arahkan kursor ke header kolom Column Visibility `(⋯)`
28. Verifikasi tooltip header `Column Visibility`
29. Klik header kolom Column Visibility `(⋯)`
30. Verifikasi overlay Column Visibility memuat item `Setup Column...` di bagian bawah
31. Verifikasi daftar kolom `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated` berstatus centang aktif
32. Verifikasi kolom curated `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `[Custom Field aktif]` berstatus tidak tercentang
33. Verifikasi drag handle tampil pada overlay
34. Tutup overlay dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-12, 13, 14, 73, 74). TC-FA-RP-72 (loading state) ada di spec `TC-FA-RP-E2E-295-loading-state-shimmer-tabel-total-control-dan-detail-role`.
- Urutan TC di spec: TC-FA-RP-12, 13, 73, 14 (semua Tab System; TC-FA-RP-14 terakhir karena menambah penugasan), lalu TC-FA-RP-74 (Tab Total Control).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, buka dan tutup menu `[⋯]` dan overlay, hover header, serta langkah 20 (baseline kolom Users, S-12) dan 21 (precondition TC-FA-RP-14 lewat sesi API aktor, "hingga tersimpan"). Langkah 21 menggantikan "matikan switch di Settings > User" pada TC dengan pemicu API yang setara.
- Kolom Users baris `Manage files`: nilai bertambah 1 untuk Budi Santoso yang memegang dua penugasan group; hasilnya dibandingkan dengan baseline langkah 20.
- Menu `[⋯]` TC-FA-RP-73 diamati pada baris pertama tiap section (sampel); TC menyebut "tiap baris".
- Temuan untuk QA:
  - TC-FA-RP-14 merujuk Pre-setup #23 (`Company Volume`, 120 pengguna) walau langkahnya memakai Budi Santoso dan Endah Susanti dari #15; spec tidak memakai #23.
  - TC-FA-RP-14 expected c tidak menyebut angka jumlah user pemegang baris pola Group Role; langkah 24 dan 25 mengikuti teks TC (mencakup user pola, tidak ada baris selain `Manage user & role` berhitung `0`) tanpa angka absolut. Expected c diberi tanda "selaraskan setelah PRD final" di TC.
  - TC-FA-RP-14 langkah 2 mematikan peran lewat Settings > User; spec memakai sesi API aktor (S-04: dijalankan lewat seeding API).
  - Post Condition TC-FA-RP-12, 13, 14, 73, dan 74 tidak memberi langkah observasi tambahan; tidak diasersi.
