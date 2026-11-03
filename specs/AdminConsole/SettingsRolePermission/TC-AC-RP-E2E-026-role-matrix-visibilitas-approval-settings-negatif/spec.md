---
id: TC-AC-RP-E2E-026-role-matrix-visibilitas-approval-settings-negatif
title: "Role Matrix: Visibilitas Approval Settings Manage allocation untuk Default User, Read Only, dan Manage user and role tanpa Update"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-86
  - TC-AC-RP-92
  - TC-AC-RP-98
coverage:
  web: automated
---

# Role Matrix: Visibilitas Approval Settings Manage allocation untuk Default User, Read Only, dan Manage user and role tanpa Update

## Prerequisites

- Mode: FE+BE. Klik toggle oleh aktor tanpa hak tulis tidak boleh mengubah state server; spec tidak mengubah state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, sisanya lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-86 | Default User | Principal | Bambang Hartono | `defaultUserRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_DU_PASSWORD` |
| TC-AC-RP-92 | Read Only | Principal | Dewi Anggraini | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` |
| TC-AC-RP-98 | Global Role "Manage user and role" tanpa Update (Read saja) | Principal | Indra Kusuma | `manageUserRoleR_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_R_PASSWORD` |

- Login akun pertama (Bambang Hartono) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Ketiga nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; `AC_RP_TC_PASSWORD` juga baru.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #2, #3, #5 (akun aktor), #11 (tree group Principal: `Region Jawa`), #17 (toggle `Manage allocation` `Region Jawa` ON; Approvers `Dewi Anggraini` dan `Dewi Anggreni`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-026`, maupun cleanup.
- Kemampuan teknis (disediakan tim FE; mekanismenya tidak tertulis di TC, PRD, atau LLD): memantau request jaringan yang dikirim browser untuk asersi "tidak ada request" pada langkah 22 dan 36 (S-13).
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-86: Approval Settings Manage allocation untuk aktor Default User

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

### TC-AC-RP-92: Approval Settings Manage allocation untuk aktor Read Only

12. Ganti akun: logout, lalu login sebagai Read Only `Dewi Anggraini` (`Spectra.env.AC_RP_RO_PASSWORD`)
13. Buka halaman `Settings > Role & Permission`
14. Klik tab `System`
15. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
16. Klik node `Region Jawa`
17. Hover toggle "Require Approval for Allocation"
18. Verifikasi toggle "Require Approval for Allocation" tampil bernilai ON (nilai `Region Jawa`)
19. Verifikasi toggle Disabled dengan tooltip "Read Only access cannot modify data."
20. Klik toggle "Require Approval for Allocation"
21. Verifikasi klik tidak mengubah nilai toggle (tetap ON)
22. Verifikasi tidak ada request yang dikirim oleh klik toggle
23. Verifikasi sub-section Approvers tampil read-only
24. Verifikasi kontrol tulis "+ Assign" dan `Remove` tidak tampil (Hidden)
25. Verifikasi kolom Checkbox dan Actions `⋯` tabel Approvers tidak tampil (Hidden)

### TC-AC-RP-98: Approval Settings Manage allocation untuk aktor Manage user and role tanpa Update

26. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" tanpa Update `Indra Kusuma` (`Spectra.env.AC_RP_MUR_R_PASSWORD`)
27. Buka halaman `Settings > Role & Permission`
28. Klik tab `System`
29. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
30. Klik node `Region Jawa`
31. Hover toggle "Require Approval for Allocation"
32. Verifikasi toggle "Require Approval for Allocation" tampil bernilai ON (nilai `Region Jawa`)
33. Verifikasi toggle Disabled dengan tooltip "Read Only access cannot modify data."
34. Klik toggle "Require Approval for Allocation"
35. Verifikasi klik tidak mengubah nilai toggle (tetap ON)
36. Verifikasi tidak ada request yang dikirim oleh klik toggle
37. Verifikasi sub-section Approvers tampil read-only
38. Verifikasi kontrol tulis "+ Assign" dan `Remove` tidak tampil (Hidden)
39. Verifikasi kolom Checkbox dan Actions `⋯` tabel Approvers tidak tampil (Hidden)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix visibilitas Approval Settings negatif (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), dan langkah role Default User berbeda dari dua role lain. Approval Settings untuk aktor yang berhak menulis (TC-AC-RP-89 dan 95) ada di spec 025.
- Langkah penghubung (S-03): langkah 13 dan 27 (membuka halaman setelah ganti akun). Langkah 1, 14, dan 28 membuka Tab System yang dibutuhkan langkah berikutnya (S-14). Langkah 6, 8, 9, dan 11 (TC-AC-RP-86) membuka dan menutup overlay `⋯` baris approver `Dewi Anggreni` serta mencentang dan melepas satu baris agar `Remove` teramati (TC langkah 6 dan 7). Hover pada langkah 17 dan 31 mendahului asersi tooltip (bagian 8b butir 5).
- Alasan spec berada di atas sekitar 35 langkah (39 langkah): tiga blok role (Default User, Read Only, Manage user and role tanpa Update) memakai halaman Role Detail `Manage allocation` yang sama dan dipisah hanya oleh Step `Ganti akun` (prinsip halaman dipakai berulang, bagian 3 dan 3a konvensi).
- Asersi Hidden langkah 24, 25, 38, dan 39 berlaku pada sub-section Approvers yang sudah tampil read-only (langkah 23 dan 37) sebagai anchor permukaan (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-AC-RP-92 dan 98 menulis langkah "Hover toggle ... lalu klik toggle"; spec memisah menjadi hover (asersi tooltip) dan klik (asersi nilai tetap dan tidak ada request), dengan mekanisme memantau request sebagai kemampuan yang disediakan tim FE.
  - TC-AC-RP-98 Expected menyebut tooltip "Read Only access cannot modify data." untuk aktor Manage user and role tanpa Update; spec menuliskannya persis seperti TC.
  - TC-AC-RP-86 menyebut "baris target" pada langkah `⋯` dan centang tanpa nama; spec memakai approver Pre-setup #17 `Dewi Anggreni`. Expected tidak membedakan `Remove` pada overlay `⋯` dan `Remove` sesudah baris dicentang; spec mengasersi keduanya.
  - Post Condition TC-AC-RP-86, 92, dan 98 bernilai "-" sehingga tidak ada yang diasersi.
