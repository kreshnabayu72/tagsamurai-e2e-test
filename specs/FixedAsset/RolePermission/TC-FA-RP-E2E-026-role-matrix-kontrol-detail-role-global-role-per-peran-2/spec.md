---
id: TC-FA-RP-E2E-026-role-matrix-kontrol-detail-role-global-role-per-peran-2
title: "Role Matrix: kontrol Detail Role Global Role per peran (2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-94
  - TC-FA-RP-95
  - TC-FA-RP-96
  - TC-FA-RP-97
coverage:
  web: automated
---

# Role Matrix: kontrol Detail Role Global Role per peran (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Pre-setup #6, role pertama pada tabel); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix, bagian 3a); urutan baris = urutan pemakaian; spec ditulis per blok role karena hasil per role berbeda dan ganti akun menuntut Step eksplisit:

| Role | Pre-setup | TC | Email | Env var password |
|---|---|---|---|---|
| Manage global user & role (Update) (Hendra Wijaya) | #6 | TC-FA-RP-94 | `murGlobal_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobal.email`) | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
| Manage user & role (Group, Update, `IT Infrastructure`) (Gita Maharani) | #7 | TC-FA-RP-95 | `murGroup_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGroup.email`) | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| Manage global user & role tanpa Update (Bayu Prakoso) | #8 | TC-FA-RP-96 | `murReadOnlyGate_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobalReadOnly.email`) | `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD` |
| Manage user & role tanpa Update (Group, `IT Infrastructure`) (Wulan Sari) | #9 | TC-FA-RP-97 | `murGroupReadOnly_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGroupReadOnly.email`) | `Spectra.env.FA_MUR_GROUP_RO_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna; Ahmad Fauzi sebagai target Standard pada Detail Role Global Role `Manage accounting`), #39 (Detail Role Global Role `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata). Spec hanya membaca; menu `[⋯]` dibuka tanpa memilih `Remove`.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama pengguna ditambahkan tim FE.
- Kemampuan teknis: hover untuk membaca tooltip checkbox. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-94: Manage global user & role (Update)

1. Klik Tab `System`, lalu klik Role Name `Manage accounting` pada section Global Role
2. Verifikasi `[+ Assign]` tampil (Show)
3. Klik `[⋯]` pada baris Ahmad Fauzi (Standard)
4. Verifikasi menu baris memuat `Remove` dengan status Enabled untuk target Standard
5. Tutup menu `[⋯]` dengan Esc
6. Verifikasi kolom Checkbox multi-select dan `Bulk Action` tampil
7. Verifikasi checkbox Create, Update, Delete pada baris Ahmad Fauzi Enabled untuk target Standard
8. Arahkan kursor ke checkbox Read pada baris Ahmad Fauzi
9. Verifikasi checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

### TC-FA-RP-95: Manage user & role (Group, Update, `IT Infrastructure`)

10. Logout dari akun Manage global user & role (Update), lalu login sebagai Manage user & role (Group, Update) dengan `Spectra.env.FA_MUR_GROUP_PASSWORD`
11. Buka menu Settings > Role & Permission dari sidebar
12. Klik Tab `System`, lalu klik Role Name `Manage accounting` pada section Global Role
13. Verifikasi `[+ Assign]` Hidden (Global Role)
14. Verifikasi aksi `Remove` Hidden
15. Verifikasi kolom Checkbox multi-select dan `Bulk Action` Hidden
16. Verifikasi checkbox Create, Update, Delete Hidden
17. Verifikasi seluruh baris penugasan tetap dapat dibaca

### TC-FA-RP-96: Manage global user & role tanpa Update

18. Logout dari akun Manage user & role (Group, Update), lalu login sebagai Manage global user & role tanpa Update dengan `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD`
19. Buka menu Settings > Role & Permission dari sidebar
20. Klik Tab `System`, lalu klik Role Name `Manage accounting` pada section Global Role
21. Verifikasi `[+ Assign]` Hidden
22. Verifikasi aksi `Remove` Hidden
23. Verifikasi kolom Checkbox multi-select dan `Bulk Action` Hidden
24. Arahkan kursor ke checkbox Create pada baris Ahmad Fauzi
25. Verifikasi checkbox Create, Update, Delete pada baris Ahmad Fauzi Disabled dengan tooltip `Read Only access cannot modify data.`
26. Arahkan kursor ke checkbox Read pada baris Ahmad Fauzi
27. Verifikasi checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

### TC-FA-RP-97: Manage user & role tanpa Update (Group, `IT Infrastructure`)

28. Logout dari akun Manage global user & role tanpa Update, lalu login sebagai Manage user & role (Group) tanpa Update dengan `Spectra.env.FA_MUR_GROUP_RO_PASSWORD`
29. Buka menu Settings > Role & Permission dari sidebar
30. Klik Tab `System`, lalu klik Role Name `Manage accounting` pada section Global Role
31. Verifikasi `[+ Assign]` Hidden (Global Role)
32. Verifikasi aksi `Remove` Hidden
33. Verifikasi kolom Checkbox multi-select dan `Bulk Action` Hidden
34. Verifikasi checkbox Create, Update, Delete Hidden (bukan Disabled)
35. Verifikasi seluruh baris penugasan tetap dapat dibaca

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-94, 95, 96, 97). TC-FA-RP-91, 92, dan 93 ada di spec `TC-FA-RP-E2E-025-role-matrix-kontrol-detail-role-global-role-per-peran-1`.
- Spec Role Matrix ditulis per blok role (bagian 3a, keputusan 2026-10-30): hasil per role berbeda dan akun pertama login di hook `before`; ganti akun pada langkah 10, 18, dan 28. Title tanpa kata Positif atau Negatif karena spec memuat tampil dan Hidden; `caseType` Negative mengikuti tiga dari empat TC sumber.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun, membuka menu dan tab, membuka dan menutup menu `[⋯]`, dan hover checkbox untuk membaca tooltip.
- Anchor Hidden (8b butir 2): Detail Role `Manage accounting` yang sudah termuat dengan baris penugasan yang dapat dibaca menjadi anchor permukaan untuk Hidden `[+ Assign]`, `Remove`, kolom Checkbox, dan checkbox CRUD.
- Alasan di atas sekitar 35 langkah (35 langkah): empat blok role berdiri sendiri pada satu kelas fungsional dan satu topik (kontrol Detail Role Global Role per role); kegagalan satu role tidak membuat role lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-94 sampai 97 menyebut "baris Ahmad Fauzi (Standard)"; spec memakai baris itu sebagai target tanpa mengubahnya.
  - TC-FA-RP-96 expected d memuat tooltip untuk tiga checkbox (Create, Update, Delete); spec membaca tooltip pada checkbox Create dan memverifikasi status Disabled ketiganya sesuai satu butir TC.
  - TC-FA-RP-94 expected c menyebut `Bulk Action` tampil tanpa seleksi; spec hanya memverifikasi kolom Checkbox multi-select dan `Bulk Action` tampil.
  - Post Condition TC-FA-RP-94 sampai 97 tidak memberi langkah observasi tambahan; tidak diasersi.
