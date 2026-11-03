---
id: TC-AC-RP-E2E-024-role-matrix-visibilitas-role-detail-negatif
title: "Role Matrix: Visibilitas Role Detail untuk Default User, Read Only, dan Manage user and role tanpa Update"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-85
  - TC-AC-RP-91
  - TC-AC-RP-97
coverage:
  web: automated
---

# Role Matrix: Visibilitas Role Detail untuk Default User, Read Only, dan Manage user and role tanpa Update

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server (hover tidak mengubah checkbox).
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, sisanya lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-85 | Default User | Principal | Bambang Hartono | `defaultUserRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_DU_PASSWORD` |
| TC-AC-RP-91 | Read Only | Principal | Dewi Anggraini | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` |
| TC-AC-RP-97 | Global Role "Manage user and role" tanpa Update (Read saja) | Principal | Indra Kusuma | `manageUserRoleR_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_R_PASSWORD` |

- Login akun pertama (Bambang Hartono) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Ketiga nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; `AC_RP_TC_PASSWORD` juga baru.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #2, #3, #5 (akun aktor), #11 (data Principal), #12 (user Standard `John Dohan`), #15 (penugasan `Manage device master data` John Dohan C/R/U sebagai baris target).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-024`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-85: Role Detail untuk aktor Default User

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

### TC-AC-RP-91: Role Detail untuk aktor Read Only

13. Ganti akun: logout, lalu login sebagai Read Only `Dewi Anggraini` (`Spectra.env.AC_RP_RO_PASSWORD`)
14. Buka halaman `Settings > Role & Permission`
15. Klik tab `System`
16. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
17. Verifikasi baris `John Dohan` tampil pada tabel Role Detail
18. Verifikasi tombol "+ Assign", row action `Remove`, kolom checkbox multi-select, dan Bulk Action tidak tampil (Hidden)
19. Hover checkbox C baris `John Dohan`
20. Verifikasi checkbox C/U/D seluruh baris Disabled dengan tooltip "Read Only access cannot modify data."
21. Hover checkbox R baris `John Dohan`
22. Verifikasi checkbox Read Disabled dengan tooltip "Read access is required and can only be removed by removing the role."

### TC-AC-RP-97: Role Detail untuk aktor Manage user and role tanpa Update

23. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" tanpa Update `Indra Kusuma` (`Spectra.env.AC_RP_MUR_R_PASSWORD`)
24. Buka halaman `Settings > Role & Permission`
25. Klik tab `System`
26. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
27. Verifikasi baris `John Dohan` tampil pada tabel Role Detail
28. Verifikasi tombol "+ Assign", row action `Remove`, kolom checkbox multi-select, dan Bulk Action tidak tampil (Hidden)
29. Hover checkbox C baris `John Dohan`
30. Verifikasi checkbox C/U/D seluruh baris Disabled dengan tooltip "Read Only access cannot modify data."
31. Hover checkbox R baris `John Dohan`
32. Verifikasi checkbox Read Disabled dengan tooltip "Read access is required and can only be removed by removing the role."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix visibilitas Role Detail negatif (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), dan langkah role Default User berbeda dari dua role lain (elemen tulis tampil versus Hidden). Role Detail untuk aktor yang berhak menulis (TC-AC-RP-88 dan 94) ada di spec 023.
- Langkah penghubung (S-03): langkah 14 dan 24 (membuka halaman setelah ganti akun). Langkah 1, 15, dan 25 membuka Tab System yang dibutuhkan langkah berikutnya (S-14). Langkah 4, 6, 7, dan 9 (TC-AC-RP-85) membuka dan menutup overlay `⋯` baris `John Dohan` serta mencentang dan melepas satu baris agar row action `Remove` dan Bulk Action teramati (TC langkah 6 dan 7); baris target TC `John Dohan` (Pre-setup #15).
- Langkah 17 dan 27 (baris `John Dohan` tampil) adalah pembanding generik untuk asersi universal "seluruh baris" pada langkah 20 dan 30 dan anchor permukaan Role Detail untuk asersi Hidden pada langkah 18 dan 28 (bagian 8b butir 2); keduanya tidak ada di TC.
- Temuan untuk QA:
  - TC-AC-RP-85 Expected menyatakan checkbox C/U/D baris `John Dohan` enabled dan R tetap checked dan disabled (sejalan TC-AC-RP-73); spec mengasersi C, U, D, dan R sebagai Verifikasi terpisah.
  - TC-AC-RP-91 dan 97 menyebut "checkbox C/U/D seluruh baris Disabled" tetapi langkah hanya meng-hover satu baris (`John Dohan`); tooltip diamati pada baris itu, sedangkan state Disabled seluruh baris tidak punya cara pengamatan tambahan di TC.
  - TC-AC-RP-97 Expected menyebut tooltip "Read Only access cannot modify data." untuk aktor Manage user and role tanpa Update (bukan Read Only); spec menuliskannya persis seperti TC.
  - Post Condition TC-AC-RP-85, 91, dan 97 bernilai "-" sehingga tidak ada yang diasersi.
