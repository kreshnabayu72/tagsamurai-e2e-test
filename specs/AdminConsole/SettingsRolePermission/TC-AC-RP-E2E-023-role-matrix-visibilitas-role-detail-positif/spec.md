---
id: TC-AC-RP-E2E-023-role-matrix-visibilitas-role-detail-positif
title: "Role Matrix: Visibilitas Role Detail untuk Total Control dan Manage user and role (Update)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-88
  - TC-AC-RP-94
coverage:
  web: automated
---

# Role Matrix: Visibilitas Role Detail untuk Total Control dan Manage user and role (Update)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server (hover tidak mengubah checkbox).
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, aktor kedua lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-88 | Total Control | Principal | Siti Nurhaliza | `totalControlRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_TC_PASSWORD` |
| TC-AC-RP-94 | Global Role "Manage user and role" dengan Update (R+U) | Principal | Hendra Wijaya | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` |

- Login akun pertama (Siti Nurhaliza) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Kedua nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #1 dan #4 (akun aktor), #11 (data Principal), #12 (user Standard `John Dohan`), #15 (penugasan `Manage device master data` John Dohan C/R/U sebagai baris target).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-023`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-88: Role Detail untuk aktor Total Control

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Verifikasi tombol "+ Assign" dan checkbox multi-select tampil
4. Klik `⋯` pada baris `John Dohan`
5. Verifikasi row action `Remove` tampil
6. Tekan Esc untuk menutup overlay `⋯`
7. Centang satu baris `John Dohan`
8. Verifikasi Bulk Action tampil
9. Lepas centang baris `John Dohan`
10. Hover checkbox C baris `John Dohan`
11. Verifikasi checkbox C, U, dan D baris `John Dohan` enabled
12. Verifikasi checkbox R baris `John Dohan` tercentang dan Disabled

### TC-AC-RP-94: Role Detail untuk aktor Manage user and role (Update)

13. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" dengan Update `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)
14. Buka halaman `Settings > Role & Permission`
15. Klik tab `System`
16. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
17. Verifikasi tombol "+ Assign" dan checkbox multi-select tampil
18. Klik `⋯` pada baris `John Dohan`
19. Verifikasi row action `Remove` tampil
20. Tekan Esc untuk menutup overlay `⋯`
21. Centang satu baris `John Dohan`
22. Verifikasi Bulk Action tampil
23. Lepas centang baris `John Dohan`
24. Hover checkbox C baris `John Dohan`
25. Verifikasi checkbox C, U, dan D baris `John Dohan` enabled
26. Verifikasi checkbox R baris `John Dohan` tercentang dan Disabled

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Role Detail untuk aktor tanpa hak tulis (TC-AC-RP-85, 91, 97) ada di spec 024.
- Langkah penghubung (S-03): langkah 14 (membuka halaman setelah ganti akun). Langkah 1 dan 15 membuka Tab System yang dibutuhkan langkah berikutnya (S-14). Langkah 4, 6, 7, 9 (TC-AC-RP-88) dan 18, 20, 21, 23 (TC-AC-RP-94) membuka dan menutup overlay `⋯` baris `John Dohan` serta mencentang dan melepas satu baris agar row action `Remove` dan Bulk Action teramati (TC langkah 6 dan 7); baris target TC `John Dohan` (Pre-setup #15).
- Temuan untuk QA:
  - TC-AC-RP-88 dan 94 menyebut langkah "Hover checkbox C baris `John Dohan`" tanpa Expected tooltip; Expected hanya menyatakan checkbox CRUD enabled sehingga tooltip tidak diasersi.
  - Expected TC menyatakan checkbox C/U/D baris `John Dohan` enabled dan R tetap checked dan disabled (sejalan TC-AC-RP-73); spec mengasersi C, U, D, dan R sebagai Verifikasi terpisah.
  - Post Condition TC-AC-RP-88 dan 94 bernilai "-" sehingga tidak ada yang diasersi.
