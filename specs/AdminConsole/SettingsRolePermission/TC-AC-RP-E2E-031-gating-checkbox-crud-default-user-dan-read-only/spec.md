---
id: TC-AC-RP-E2E-031-gating-checkbox-crud-default-user-dan-read-only
title: "Gating Checkbox CRUD Aktor Default User dan Read Only: Tooltip dan Prioritas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-106
  - TC-AC-RP-111
coverage:
  web: automated
---

# Gating Checkbox CRUD Aktor Default User dan Read Only: Tooltip dan Prioritas

## Prerequisites

- Mode: FE+BE. Spec hanya mengamati tooltip checkbox; tidak ada checkbox yang diklik sehingga tidak ada perubahan state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, aktor kedua lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-106 | Default User | Principal | Bambang Hartono | `defaultUserRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_DU_PASSWORD` |
| TC-AC-RP-111 | Read Only | Principal | Dewi Anggraini | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` |

- Login akun pertama (Bambang Hartono) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Kedua nama env password dan `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #2 dan #3 (akun aktor; baris target `Bambang Hartono` dan `Dewi Anggraini`), #11 (data Principal), #13 (Total Control `Rina Wijaya`), #15 (Role Global `Manage device master data`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-031`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-106: Default User tidak dapat mengedit CRUD miliknya sendiri

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Hover checkbox C baris `Bambang Hartono`
4. Verifikasi checkbox baris `Bambang Hartono` Disabled dengan tooltip "Default User cannot be modified."

### TC-AC-RP-111: Prioritas tooltip Read Only di atas kondisi target

5. Ganti akun: logout, lalu login sebagai Read Only `Dewi Anggraini` (`Spectra.env.AC_RP_RO_PASSWORD`)
6. Buka halaman `Settings > Role & Permission`
7. Klik tab `System`
8. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
9. Hover checkbox C baris `Bambang Hartono`
10. Verifikasi checkbox C baris `Bambang Hartono` menampilkan tooltip "Read Only access cannot modify data."
11. Hover checkbox C baris `Dewi Anggraini` (diri sendiri)
12. Verifikasi checkbox C baris `Dewi Anggraini` menampilkan tooltip "Read Only access cannot modify data."
13. Hover checkbox C baris `Rina Wijaya`
14. Verifikasi checkbox C baris `Rina Wijaya` menampilkan tooltip "Read Only access cannot modify data."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (S-03): langkah 6 (membuka halaman setelah ganti akun). Langkah 1 dan 7 membuka Tab System yang dibutuhkan langkah berikutnya (S-14). Hover pada langkah 3, 9, 11, dan 13 mendahului asersi tooltip (bagian 8b butir 5).
- Ekspresi "prioritas Default User di atas diri sendiri" pada Expected TC-AC-RP-106 adalah penjelasan atas tooltip yang tampil (aktor Default User adalah baris sendiri sekaligus Default User) dan tidak menjadi klausa terpisah; tooltip diasersi pada langkah 4.
- Temuan untuk QA:
  - TC-AC-RP-106 Expected hanya menyebut "Checkbox Disabled" untuk hover pada C; kolom U/D tidak diamati terpisah di TC.
  - TC-AC-RP-111 Expected "ketiga checkbox" tidak menyebut kolom yang di-hover; spec memakai checkbox C sesuai langkah TC.
  - Post Condition TC-AC-RP-106 dan 111 bernilai "-" sehingga tidak ada yang diasersi.
