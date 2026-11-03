---
id: TC-AC-RP-E2E-025-role-matrix-visibilitas-approval-settings-positif
title: "Role Matrix: Visibilitas Approval Settings Manage allocation untuk Total Control dan Manage user and role (Update)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-89
  - TC-AC-RP-95
coverage:
  web: automated
---

# Role Matrix: Visibilitas Approval Settings Manage allocation untuk Total Control dan Manage user and role (Update)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, aktor kedua lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-89 | Total Control | Principal | Siti Nurhaliza | `totalControlRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_TC_PASSWORD` |
| TC-AC-RP-95 | Global Role "Manage user and role" dengan Update (R+U) | Principal | Hendra Wijaya | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` |

- Login akun pertama (Siti Nurhaliza) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Kedua nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #1 dan #4 (akun aktor), #11 (tree group Principal: `Region Jawa`), #17 (toggle `Manage allocation` `Region Jawa` ON; Approvers `Dewi Anggraini` dan `Dewi Anggreni`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-025`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-89: Approval Settings Manage allocation untuk aktor Total Control

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Region Jawa`
4. Verifikasi Toggle "Require Approval for Allocation" tampil dan enabled
5. Verifikasi sub-section Approvers menampilkan "+ Assign"
6. Klik `⋯` pada baris `Dewi Anggreni` di sub-section Approvers
7. Verifikasi row action `Remove` tampil
8. Tekan Esc untuk menutup overlay `⋯`
9. Centang satu baris `Dewi Anggreni`
10. Verifikasi `Remove` tampil setelah baris dicentang
11. Lepas centang baris `Dewi Anggreni`

### TC-AC-RP-95: Approval Settings Manage allocation untuk aktor Manage user and role (Update)

12. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" dengan Update `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)
13. Buka halaman `Settings > Role & Permission`
14. Klik tab `System`
15. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
16. Klik node `Region Jawa`
17. Verifikasi Toggle "Require Approval for Allocation" tampil dan enabled
18. Verifikasi sub-section "Approvers — Region Jawa" tampil dengan "+ Assign"
19. Klik `⋯` pada baris `Dewi Anggreni` di sub-section "Approvers — Region Jawa"
20. Verifikasi row action `Remove` tampil untuk mengelola Additional Approver
21. Tekan Esc untuk menutup overlay `⋯`
22. Centang satu baris `Dewi Anggreni`
23. Verifikasi `Remove` tampil setelah baris dicentang
24. Lepas centang baris `Dewi Anggreni`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Approval Settings untuk aktor tanpa hak tulis (TC-AC-RP-86, 92, 98) ada di spec 026.
- Langkah penghubung (S-03): langkah 13 (membuka halaman setelah ganti akun). Langkah 1 dan 14 membuka Tab System yang dibutuhkan langkah berikutnya (S-14). Langkah 6, 8, 9, 11 (TC-AC-RP-89) dan 19, 21, 22, 24 (TC-AC-RP-95) membuka dan menutup overlay `⋯` baris approver serta mencentang dan melepas satu baris agar `Remove` teramati (TC langkah 6 dan 7).
- Temuan untuk QA:
  - TC-AC-RP-89 Expected "sub-section Approvers menampilkan "+ Assign" dan `Remove`" tidak menyebut nama sub-section ("Approvers — Region Jawa" hanya muncul di TC-AC-RP-95) dan tidak menyebut baris approver mana yang menampilkan `Remove`; spec mengikuti kalimat TC.
  - TC-AC-RP-89 dan 95 menyebut "baris target" pada langkah `⋯` dan centang tanpa nama; spec memakai approver Pre-setup #17 `Dewi Anggreni`. Expected tidak membedakan `Remove` pada overlay `⋯` dan `Remove` sesudah baris dicentang; spec mengasersi keduanya.
  - Post Condition TC-AC-RP-89 dan 95 bernilai "-" sehingga tidak ada yang diasersi.
