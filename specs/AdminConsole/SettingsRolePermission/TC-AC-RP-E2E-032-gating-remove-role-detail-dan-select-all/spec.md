---
id: TC-AC-RP-E2E-032-gating-remove-role-detail-dan-select-all
title: "Gating Remove dan Select All Role Detail untuk Aktor Manage user and role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-115
  - TC-AC-RP-116
  - TC-AC-RP-119
coverage:
  web: automated
---

# Gating Remove dan Select All Role Detail untuk Aktor Manage user and role

## Prerequisites

- Mode: FE+BE. Spec hanya mengamati state, tooltip, dan seleksi lokal; tidak ada `Remove` yang dijalankan sehingga tidak ada perubahan state server.
- Akun aktor: Global Role "Manage user and role" dengan Update (R+U) `Hendra Wijaya`, `manageUserRoleU_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_MUR_U_PASSWORD`. Login di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Nama env `AC_RP_MUR_U_PASSWORD` dan `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #4 (`Hendra Wijaya`), #2 (`Bambang Hartono`, Default User), #3 (`Dewi Anggraini`, Read Only), #6 (`Fajar Nugroho`, GM `Region Jawa`), #11 (tree group Principal: `Region Jawa`), #12 (user Standard `Jane Smith`, `John Dohan`, `Maya Putri`), #13 (Total Control `Rina Wijaya`), #15 (penugasan `Manage device master data` John Dohan, Jane Smith, Maya Putri, Fajar Nugroho, dan Hendra Wijaya; Group Role `Manage distributor` untuk baris `Rina Wijaya`, `Dewi Anggraini`, `Fajar Nugroho` pada `Region Jawa`).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-032`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-115: Manage user and role: Remove dan checkbox baris TC, RO, GM-target Disabled

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
3. Klik node `Region Jawa`
4. Hover checkbox multi-select baris `Rina Wijaya`
5. Verifikasi checkbox multi-select baris `Rina Wijaya` Disabled dengan tooltip "You don't have permission to edit."
6. Klik `⋯` baris `Rina Wijaya`
7. Hover aksi `Remove`
8. Verifikasi aksi `Remove` baris `Rina Wijaya` Disabled dengan tooltip "You don't have permission to edit."
9. Tutup overlay `⋯` dengan Esc
10. Hover checkbox multi-select baris `Dewi Anggraini`
11. Verifikasi checkbox multi-select baris `Dewi Anggraini` Disabled dengan tooltip "You don't have permission to edit."
12. Klik `⋯` baris `Dewi Anggraini`
13. Hover aksi `Remove`
14. Verifikasi aksi `Remove` baris `Dewi Anggraini` Disabled dengan tooltip "You don't have permission to edit."
15. Tutup overlay `⋯` dengan Esc
16. Hover checkbox multi-select baris `Fajar Nugroho`
17. Verifikasi checkbox multi-select baris `Fajar Nugroho` Disabled dengan tooltip "You don't have permission to edit."
18. Klik `⋯` baris `Fajar Nugroho`
19. Hover aksi `Remove`
20. Verifikasi aksi `Remove` baris `Fajar Nugroho` Disabled dengan tooltip "You don't have permission to edit."
21. Tutup overlay `⋯` dengan Esc

### TC-AC-RP-116: Remove dan checkbox baris Default User Disabled untuk semua aktor tulis

22. Buka halaman `Settings > Role & Permission`
23. Klik tab `System`
24. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
25. Hover checkbox multi-select baris `Bambang Hartono`
26. Verifikasi checkbox multi-select baris `Bambang Hartono` Disabled dengan tooltip "Default User cannot be modified."
27. Klik `⋯` baris `Bambang Hartono`
28. Hover aksi `Remove`
29. Verifikasi aksi `Remove` baris `Bambang Hartono` Disabled dengan tooltip "Default User cannot be modified."
30. Tutup overlay `⋯` dengan Esc

### TC-AC-RP-119: Select All Role Detail tidak memilih baris Disabled

31. Klik checkbox Select All di header tabel
32. Verifikasi hanya baris yang checkbox-nya enabled terpilih (`Fajar Nugroho`, `Jane Smith`, `John Dohan`, `Maya Putri`)
33. Verifikasi baris `Bambang Hartono`, `Hendra Wijaya` (diri sendiri), serta baris TC dan RO tidak ikut terpilih
34. Verifikasi baris yang tidak terpilih tidak dihitung di counter seleksi
35. Klik checkbox Select All di header tabel untuk melepas seleksi

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 4 sampai 21 mengulang pola yang sama untuk tiga baris target (`Rina Wijaya`, `Dewi Anggraini`, `Fajar Nugroho`): hover checkbox multi-select, `Verifikasi`, buka `⋯`, hover `Remove`, `Verifikasi`, tutup overlay. Parameter tiap iterasi adalah nama baris pada langkah itu; `Verifikasi` tetap satu per elemen (S-01). Spec ini mencapai sekitar 35 langkah karena iterasi ini dan seluruhnya satu kelas (gating Remove dan seleksi pada Role Detail yang berdiri sendiri); kegagalan satu blok TC tidak membuat blok lain kehilangan makna karena tiap blok membuka Role Detail sendiri.
- Urutan TC di dalam spec mengikuti nomor TC; TC-AC-RP-116 dan 119 memakai Role Detail Global `Manage device master data` yang sama dan dijalankan berurutan tanpa membuka ulang. TC-AC-RP-117 dan 118 (aktor Total Control) ada di spec 123.
- Langkah penghubung (S-03, S-09): langkah 9, 15, 21, dan 30 (menutup overlay `⋯`), langkah 22 (membuka halaman kembali dari Group Role menuju Role Detail Global), dan langkah 35 (melepas seleksi setelah TC-AC-RP-119). Langkah 1, 3, dan 23 membuka Tab System dan node group yang dibutuhkan langkah berikutnya (S-14).
- Hover pada langkah 4, 7, 10, 13, 16, 19, 25, dan 28 mendahului asersi tooltip (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-RP-119 Expected "tidak dihitung di counter" tidak menyebut format counter atau angkanya; spec mengasersi bahwa baris yang tidak terpilih tidak dihitung, tanpa mengarang teks counter.
  - TC-AC-RP-115 dan 116 menyebut hover "aksi `Remove`" tanpa menyatakan bahwa aksi itu berada pada overlay `⋯` baris; spec membuka overlay `⋯` baris sebelum hover `Remove` (langkah 6, 12, 18, 27).
  - Baris TC dan RO pada Role Detail Global `Manage device master data` (TC-AC-RP-119 Expected) tidak disebut namanya; spec mengasersi sesuai kalimat TC.
  - Post Condition TC-AC-RP-115, 116, dan 119 bernilai "-" sehingga tidak ada yang diasersi.
