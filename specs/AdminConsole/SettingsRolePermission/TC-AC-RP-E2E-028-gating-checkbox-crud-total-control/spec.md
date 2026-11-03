---
id: TC-AC-RP-E2E-028-gating-checkbox-crud-total-control
title: "Gating Checkbox CRUD Aktor Total Control: Target Standard, TC, RO, GM-target, Default User, dan Diri Sendiri"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-102
  - TC-AC-RP-103
  - TC-AC-RP-104
  - TC-AC-RP-105
coverage:
  web: automated
---

# Gating Checkbox CRUD Aktor Total Control: Target Standard, TC, RO, GM-target, Default User, dan Diri Sendiri

## Prerequisites

- Mode: FE+BE. Spec hanya mengamati state dan tooltip checkbox; tidak ada checkbox yang diklik sehingga tidak ada perubahan state server.
- Akun aktor: Total Control Principal `Siti Nurhaliza`, `totalControlRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #1 (`Siti Nurhaliza`), #2 (`Bambang Hartono`, Default User), #3 (`Dewi Anggraini`, Read Only), #6 (`Fajar Nugroho`, GM `Region Jawa`), #11 (tree group Principal: `Region Jawa`), #12 (user Standard `John Dohan`, `Jane Smith`), #13 (Total Control `Rina Wijaya`), #15 (penugasan `Manage device master data` John Dohan C/R/U dan Jane Smith R; Group Role `Manage distributor` untuk baris `Rina Wijaya`, `Dewi Anggraini`, `Fajar Nugroho` pada `Region Jawa`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-028`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-102: Total Control mengedit CRUD target Standard

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Verifikasi checkbox C/U/D baris `John Dohan` enabled
4. Verifikasi checkbox C/U/D baris `Jane Smith` enabled

### TC-AC-RP-104: Checkbox CRUD baris Default User Disabled bagi Total Control

5. Hover checkbox C baris `Bambang Hartono`
6. Verifikasi checkbox C/U/D baris `Bambang Hartono` Disabled dengan tooltip "Default User cannot be modified."

### TC-AC-RP-105: Checkbox CRUD baris diri sendiri Disabled bagi Total Control

7. Hover checkbox C baris `Siti Nurhaliza`
8. Verifikasi checkbox C/U/D baris `Siti Nurhaliza` Disabled dengan tooltip "You can't manage your own account from here."

### TC-AC-RP-103: Total Control dapat mengedit CRUD target TC, RO, dan GM-target

9. Buka halaman `Settings > Role & Permission`
10. Klik tab `System`
11. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
12. Klik node `Region Jawa`
13. Verifikasi checkbox C/U/D baris `Rina Wijaya` (TC) enabled
14. Verifikasi checkbox C/U/D baris `Dewi Anggraini` (RO) enabled
15. Verifikasi checkbox C/U/D baris `Fajar Nugroho` (GM-target) enabled

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di dalam spec menyimpang dari nomor TC: TC-AC-RP-104 dan 105 dijalankan sebelum TC-AC-RP-103 karena ketiganya memakai Role Detail Global `Manage device master data` yang sama dengan TC-AC-RP-102, sedangkan TC-AC-RP-103 memakai Role Detail Group Role `Manage distributor`, sehingga Role Detail Global dibuka satu kali.
- Langkah penghubung (S-03): langkah 9 (membuka halaman kembali dari Role Detail Global menuju Group Role). Langkah 1 dan 10 membuka Tab System yang dibutuhkan langkah berikutnya (S-14).
- Hover pada langkah 5 dan 7 mendahului asersi tooltip pada langkah 6 dan 8 (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-RP-102 Expected "Checkbox C/U/D kedua baris enabled" tidak merinci kolom R; kolom R pada Role Detail Global disabled menurut TC-AC-RP-73. Spec mengikuti kalimat TC dan mengasersi C/U/D.
  - TC-AC-RP-102 dan 103 tidak memiliki tooltip pada kondisi enabled; spec hanya mengasersi enabled.
  - TC-AC-RP-104 dan 105 hanya meng-hover checkbox C sedangkan Expected menyebut C/U/D; spec mengasersi C/U/D sesuai kalimat TC dengan tooltip diamati pada C.
  - Post Condition TC-AC-RP-102 sampai 105 bernilai "-" sehingga tidak ada yang diasersi.
