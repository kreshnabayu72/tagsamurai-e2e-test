---
id: TC-FA-RP-E2E-025-role-matrix-kontrol-detail-role-global-role-per-peran-1
title: "Role Matrix: kontrol Detail Role Global Role per peran (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-91
  - TC-FA-RP-92
  - TC-FA-RP-93
coverage:
  web: automated
---

# Role Matrix: kontrol Detail Role Global Role per peran (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2, role pertama pada tabel); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix, bagian 3a); urutan baris = urutan pemakaian; spec ditulis per blok role karena hasil per role berbeda dan ganti akun menuntut Step eksplisit:

| Role | Pre-setup | TC | Email | Env var password |
|---|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | TC-FA-RP-91 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |
| Read Only (Dewi Anggraini) | #4 | TC-FA-RP-92 | `readOnly_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.readOnly.email`) | `Spectra.env.FA_RO_PASSWORD` |
| Group Manager (Fajar Nugroho, `IT Infrastructure`) | #5 | TC-FA-RP-93 | `groupManager_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.groupManager.email`) | `Spectra.env.FA_GM_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna; Ahmad Fauzi sebagai target Standard pada Detail Role Global Role `Manage accounting`), #39 (Detail Role Global Role `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata). Spec hanya membaca; menu `[⋯]` dibuka tanpa memilih `Remove`.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama pengguna ditambahkan tim FE.
- Kemampuan teknis: hover untuk membaca tooltip checkbox. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-91: Detail Role Global Role (`Manage accounting`) bagi Total Control

1. Klik Tab `System`, lalu klik Role Name `Manage accounting` pada section Global Role
2. Verifikasi `[+ Assign]` tampil (Show)
3. Klik `[⋯]` pada baris Ahmad Fauzi (Standard)
4. Verifikasi menu baris memuat `Remove` dengan status Enabled untuk target Standard
5. Tutup menu `[⋯]` dengan Esc
6. Verifikasi kolom Checkbox multi-select dan `Bulk Action` tampil
7. Verifikasi checkbox Create, Update, Delete pada baris Ahmad Fauzi Enabled untuk target Standard
8. Arahkan kursor ke checkbox Read pada baris Ahmad Fauzi
9. Verifikasi checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

### TC-FA-RP-92: Detail Role Global Role (`Manage accounting`) bagi Read Only

10. Logout dari akun Total Control, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
11. Buka menu Settings > Role & Permission dari sidebar
12. Klik Tab `System`, lalu klik Role Name `Manage accounting` pada section Global Role
13. Verifikasi `[+ Assign]` Hidden
14. Verifikasi aksi `Remove` Hidden
15. Verifikasi kolom Checkbox multi-select dan `Bulk Action` Hidden
16. Arahkan kursor ke checkbox Create pada baris Ahmad Fauzi
17. Verifikasi checkbox Create, Update, Delete pada baris Ahmad Fauzi Disabled dengan tooltip `Read Only access cannot modify data.`
18. Arahkan kursor ke checkbox Read pada baris Ahmad Fauzi
19. Verifikasi checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

### TC-FA-RP-93: Detail Role Global Role (`Manage accounting`) bagi Group Manager (Fajar Nugroho, `IT Infrastructure`)

20. Logout dari akun Read Only, lalu login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
21. Buka menu Settings > Role & Permission dari sidebar
22. Klik Tab `System`, lalu klik Role Name `Manage accounting` pada section Global Role
23. Verifikasi `[+ Assign]` Hidden (Global Role)
24. Verifikasi aksi `Remove` Hidden
25. Verifikasi kolom Checkbox multi-select dan `Bulk Action` Hidden
26. Verifikasi checkbox Create, Update, Delete Hidden
27. Verifikasi seluruh baris penugasan tetap dapat dibaca

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-91, 92, 93). TC-FA-RP-94 sampai 97 ada di spec `TC-FA-RP-E2E-026-role-matrix-kontrol-detail-role-global-role-per-peran-2`.
- Spec Role Matrix ditulis per blok role (bagian 3a, keputusan 2026-10-30): hasil per role berbeda dan akun pertama login di hook `before`; ganti akun pada langkah 10 dan 20. Title tanpa kata Positif atau Negatif karena spec memuat tampil dan Hidden; `caseType` Positive mengikuti TC-FA-RP-91 (alur utama role yang berhak).
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun, membuka menu dan tab, membuka dan menutup menu `[⋯]`, dan hover checkbox untuk membaca tooltip.
- Anchor Hidden (8b butir 2): Detail Role `Manage accounting` yang sudah termuat dengan baris penugasan yang dapat dibaca menjadi anchor permukaan untuk Hidden `[+ Assign]`, `Remove`, kolom Checkbox, dan checkbox CRUD.
- Temuan untuk QA:
  - TC-FA-RP-91 sampai 93 menyebut "baris Ahmad Fauzi (Standard)"; spec memakai baris itu sebagai target tanpa mengubahnya.
  - TC-FA-RP-92 expected d memuat tooltip untuk tiga checkbox (Create, Update, Delete); spec membaca tooltip pada checkbox Create dan memverifikasi status Disabled ketiganya sesuai satu butir TC.
  - TC-FA-RP-91 expected c menyebut `Bulk Action` tampil tanpa seleksi; spec hanya memverifikasi kolom Checkbox multi-select dan `Bulk Action` tampil.
  - Post Condition TC-FA-RP-91, 92, dan 93 tidak memberi langkah observasi tambahan; tidak diasersi.
