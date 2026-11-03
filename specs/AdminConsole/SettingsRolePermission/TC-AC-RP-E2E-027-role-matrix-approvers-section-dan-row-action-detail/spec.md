---
id: TC-AC-RP-E2E-027-role-matrix-approvers-section-dan-row-action-detail
title: "Role Matrix: Approvers Section Manage TAG stock dan Row Action Detail Tab System"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-99
  - TC-AC-RP-100
  - TC-AC-RP-101
coverage:
  web: automated
---

# Role Matrix: Approvers Section Manage TAG stock dan Row Action Detail Tab System

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, sisanya lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-99 | Global Role "Manage user and role" dengan Update (R+U) | Principal | Hendra Wijaya | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` |
| TC-AC-RP-100 | Read Only | Principal | Dewi Anggraini | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` |
| TC-AC-RP-101 | Global Role "Manage user and role" tanpa Update (Read saja) | Principal | Indra Kusuma | `manageUserRoleR_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_R_PASSWORD` |

- Login akun pertama (Hendra Wijaya) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Ketiga nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; `AC_RP_TC_PASSWORD` juga baru.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #3, #4, #5 (akun aktor), #11 (data Principal), #17 (Approver `Manage TAG stock` = `Sarah Kimura`), #12 (user Standard `Sarah Kimura`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-027`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-99: Approvers Section Manage TAG stock untuk aktor Manage user and role (Update)

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
3. Buka overlay `⋯` baris `Sarah Kimura`
4. Verifikasi tombol "+ Assign" pada toolbar section Approvers tampil enabled
5. Verifikasi aksi `Remove` pada overlay `⋯` baris `Sarah Kimura` tampil enabled
6. Tutup overlay `⋯` dengan Esc

### TC-AC-RP-100: Approvers Section Manage TAG stock untuk aktor Read Only

7. Ganti akun: logout, lalu login sebagai Read Only `Dewi Anggraini` (`Spectra.env.AC_RP_RO_PASSWORD`)
8. Buka halaman `Settings > Role & Permission`
9. Klik tab `System`
10. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
11. Verifikasi tabel Approvers menampilkan baris `Sarah Kimura` secara read-only
12. Verifikasi tombol "+ Assign" dan aksi `Remove` tidak tampil (Hidden)
13. Verifikasi kolom Checkbox dan Actions `⋯` tidak tampil (Hidden)

### TC-AC-RP-101: Row action Detail Tab System tampil untuk seluruh aktor

14. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" tanpa Update `Indra Kusuma` (`Spectra.env.AC_RP_MUR_R_PASSWORD`)
15. Buka halaman `Settings > Role & Permission`
16. Klik tab `System`
17. Klik `⋯` pada baris `Manage group`
18. Verifikasi aksi `Detail` tampil
19. Klik `Detail`
20. Verifikasi Role Detail `Manage group` terbuka
21. Verifikasi Role Detail `Manage group` terbuka secara read-only

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), dan langkah tiap role berbeda (Approvers Section versus row action).
- Langkah penghubung (S-03): langkah 6 (menutup overlay), 8, dan 15 (membuka halaman setelah ganti akun). Langkah 1, 9, dan 16 membuka Tab System yang dibutuhkan langkah berikutnya (S-14).
- Langkah 11 (baris `Sarah Kimura` tampil read-only) mendahului asersi Hidden langkah 12 dan 13 sebagai anchor permukaan; urutan ini mengikuti urutan state dan bukan urutan klausa Expected TC-AC-RP-100 (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-RP-101 Expected "secara read-only" tidak merinci indikator read-only Role Detail; spec mengasersi kalimat TC (langkah 21) tanpa mengarang indikator.
  - TC-AC-RP-99 Expected tidak menyebut apakah `Remove` pada overlay baris `Sarah Kimura` memicu dialog; spec hanya mengasersi tampil dan enabled.
  - Post Condition TC-AC-RP-99 sampai 101 bernilai "-" sehingga tidak ada yang diasersi.
