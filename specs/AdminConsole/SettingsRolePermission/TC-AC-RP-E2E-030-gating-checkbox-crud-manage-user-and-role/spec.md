---
id: TC-AC-RP-E2E-030-gating-checkbox-crud-manage-user-and-role
title: "Gating Checkbox CRUD Aktor Manage user and role: Target Standard, TC, RO, GM-target, dan Prioritas Tooltip"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-107
  - TC-AC-RP-108
  - TC-AC-RP-109
  - TC-AC-RP-110
  - TC-AC-RP-112
coverage:
  web: automated
---

# Gating Checkbox CRUD Aktor Manage user and role: Target Standard, TC, RO, GM-target, dan Prioritas Tooltip

## Prerequisites

- Mode: FE+BE. Spec hanya mengamati state dan tooltip checkbox; tidak ada checkbox yang diklik sehingga tidak ada perubahan state server.
- Akun aktor: Global Role "Manage user and role" dengan Update (R+U) `Hendra Wijaya`, `manageUserRoleU_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_MUR_U_PASSWORD`. Login di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Nama env `AC_RP_MUR_U_PASSWORD` dan `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #4 (`Hendra Wijaya`), #3 (`Dewi Anggraini`, Read Only), #6 (`Fajar Nugroho`, GM `Region Jawa` dan `Sumatera`), #11 (tree group Principal: `Region Jawa`), #12 (user Standard `John Dohan`), #13 (Total Control `Rina Wijaya`), #15 (penugasan `Manage device master data` John Dohan C/R/U, Hendra Wijaya R, Fajar Nugroho R; Group Role `Manage distributor` untuk baris `Fajar Nugroho` pada `Region Jawa`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-030`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-107: Manage user and role mengedit CRUD target Standard

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Verifikasi checkbox C/U/D baris `John Dohan` enabled

### TC-AC-RP-108: Manage user and role tidak dapat mengedit CRUD target TC dan RO

4. Hover checkbox C baris `Rina Wijaya` (TC)
5. Verifikasi checkbox C baris `Rina Wijaya` Disabled dengan tooltip "You don't have permission to edit."
6. Hover checkbox C baris `Dewi Anggraini` (RO)
7. Verifikasi checkbox C baris `Dewi Anggraini` Disabled dengan tooltip "You don't have permission to edit."

### TC-AC-RP-110: Manage user and role mengedit Peran Global target GM

8. Verifikasi checkbox C/U/D baris `Fajar Nugroho` pada Global Role enabled

### TC-AC-RP-112: Prioritas tooltip diri sendiri di atas target TC bagi Manage user and role

9. Hover checkbox C baris `Hendra Wijaya`
10. Verifikasi tooltip "You can't manage your own account from here." tampil

### TC-AC-RP-109: Manage user and role tidak dapat mengedit CRUD GM-target di group GM-nya

11. Buka halaman `Settings > Role & Permission`
12. Klik tab `System`
13. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
14. Klik node `Region Jawa`
15. Hover checkbox C baris `Fajar Nugroho`
16. Verifikasi checkbox C baris `Fajar Nugroho` Disabled dengan tooltip "You don't have permission to edit."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di dalam spec menyimpang dari nomor TC: TC-AC-RP-110 dan 112 dijalankan sebelum TC-AC-RP-109 karena keduanya memakai Role Detail Global `Manage device master data` yang sama dengan TC-AC-RP-107 dan 108, sedangkan TC-AC-RP-109 memakai Role Detail Group Role `Manage distributor`, sehingga Role Detail Global dibuka satu kali.
- Langkah penghubung (S-03): langkah 11 (membuka halaman kembali dari Role Detail Global menuju Group Role). Langkah 1 dan 12 membuka Tab System yang dibutuhkan langkah berikutnya (S-14).
- Hover pada langkah 4, 6, 9, dan 15 mendahului asersi tooltip (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-RP-110 menyebut `Fajar Nugroho` memegang `Manage device master data` R pada kolom Data Uji TC, sedangkan Pre-setup #15 mencatat penugasan yang sama; spec memakai Pre-setup #15 tanpa seeding tambahan.
  - TC-AC-RP-112 Expected hanya menyebut tooltip tanpa menyebut state Disabled; spec mengasersi tooltip sesuai kalimat TC.
  - TC-AC-RP-108 dan 109 Expected "Disabled" hanya diamati pada checkbox C yang di-hover, sedangkan kolom U/D tidak diamati terpisah di TC.
  - Post Condition TC-AC-RP-107 sampai 110 dan 112 bernilai "-" sehingga tidak ada yang diasersi.
