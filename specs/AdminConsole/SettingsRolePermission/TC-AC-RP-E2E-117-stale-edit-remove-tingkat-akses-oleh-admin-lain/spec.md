---
id: TC-AC-RP-E2E-117-stale-edit-remove-tingkat-akses-oleh-admin-lain
title: "Target Berubah sejak Render: Edit CRUD, Remove Total Control, Read Only, dan Group Manager yang Sudah Diubah Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-394
  - TC-AC-RP-395
  - TC-AC-RP-396
  - TC-AC-RP-397
coverage:
  web: automated
---

# Target Berubah sejak Render: Edit CRUD, Remove Total Control, Read Only, dan Group Manager yang Sudah Diubah Admin Lain

## Prerequisites

- Mode: FE+BE (backend nyata; Sesi A lewat UI, Sesi B lewat sesi API)
- Akun aktor Sesi A: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`, Pre-setup #1), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun UI di tengah spec. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Pelaku kedua (Sesi B, Total Control; Pre-setup #24): sesi API untuk akun `Siti Nurhaliza` yang sama (`Spectra.env.AC_RP_TC_PASSWORD`); hanya memicu perubahan state, tanpa asersi di sesinya (bukan konteks kedua kelas c; tidak butuh `P-2`).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`John Dohan`, `Jane Smith`), #13 (Total Control `John Doe`; Read Only `Dewi Anggraini`), #14 (penugasan Group Manager `Jane Smith` — `Region Jawa`), #15 (peran individual `Manage device master data`: `John Dohan` C/R/U), dan #24 (dua sesi). Target aksi adalah data Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-117` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): sesi API aktor (dinyatakan di `suite.md`); kemampuan membaca state data lewat fixture BE (peran individual `John Dohan`, peran individual dan tingkat akses `John Doe` dan `Dewi Anggraini`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini (peran `John Dohan`, tingkat akses `John Doe` dan `Dewi Anggraini`, penugasan Group Manager `Jane Smith`) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama), dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-394: Edit CRUD atas baris peran yang sudah dihapus admin lain

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Remove peran `John Dohan` pada `Manage device master data` hingga tersimpan
4. Tunggu aksi selesai (Sesi B tersimpan)
5. Sesi A: centang D baris `John Dohan`
6. Verifikasi toast netral "This permission is no longer available."
7. Verifikasi tabel Role Detail di-refresh dan baris `John Dohan` tidak tampil
8. Verifikasi lewat fixture BE bahwa `John Dohan` tidak memegang `Manage device master data` dan tidak ada nilai D yang tersimpan (perubahan tidak tersimpan)
9. Verifikasi dialog tidak tampil
10. Pulihkan baseline: `John Dohan` kembali memegang `Manage device master data` C/R/U lewat kemampuan reset FE/BE

### TC-AC-RP-395: Remove Total Control atas target yang sudah dilepas admin lain

11. Buka halaman `Settings > Role & Permission`
12. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Remove Total Control `John Doe` hingga tersimpan
13. Tunggu aksi selesai (Sesi B tersimpan)
14. Catat lewat fixture BE peran individual `John Doe` sebagai baseline
15. Sesi A: klik `⋯` baris `John Doe` lalu klik `Remove`
16. Klik `[Remove]`
17. Verifikasi toast netral "This access level is no longer available."
18. Verifikasi daftar di-refresh dan baris `John Doe` tidak tampil di Tab Total Control
19. Verifikasi lewat fixture BE bahwa peran individual `John Doe` sama dengan baseline langkah 14
20. Pulihkan baseline: `John Doe` kembali Total Control lewat kemampuan reset FE/BE

### TC-AC-RP-396: Remove Read Only pada user yang sudah menjadi Total Control

21. Buka halaman `Settings > Role & Permission`
22. Klik tab `Read Only`
23. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Assign Total Control ke `Dewi Anggraini` hingga tersimpan
24. Tunggu aksi selesai (Sesi B tersimpan)
25. Catat lewat fixture BE peran individual `Dewi Anggraini` sebagai baseline
26. Sesi A: klik `⋯` baris `Dewi Anggraini` lalu klik `Remove`
27. Klik `[Remove]`
28. Verifikasi toast netral "This access level is no longer available."
29. Verifikasi daftar di-refresh dan baris `Dewi Anggraini` tidak tampil di Tab Read Only
30. Verifikasi lewat fixture BE bahwa tingkat akses `Dewi Anggraini` tetap Total Control
31. Verifikasi lewat fixture BE bahwa peran individual `Dewi Anggraini` sama dengan baseline langkah 25
32. Pulihkan baseline: `Dewi Anggraini` kembali Read Only lewat kemampuan reset FE/BE

### TC-AC-RP-397: Remove GM atas penugasan yang sudah dilepas

33. Buka halaman `Settings > Role & Permission`
34. Klik tab `Group Manager`
35. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Remove GM `Jane Smith` — `Region Jawa` hingga tersimpan
36. Tunggu aksi selesai (Sesi B tersimpan)
37. Sesi A: klik `⋯` baris `Jane Smith` — `Region Jawa` lalu klik `Remove`
38. Klik `[Remove]`
39. Verifikasi toast netral "This Group Manager assignment is no longer available."
40. Verifikasi daftar di-refresh dan baris `Jane Smith` — `Region Jawa` tidak tampil di Tab Group Manager
41. Pulihkan baseline: penugasan GM `Jane Smith` — `Region Jawa` kembali lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Aktor: Sesi A adalah UI `Siti Nurhaliza`; Sesi B dijalankan lewat sesi API akun yang sama sesuai keputusan pelaku kedua memakai sesi API (bagian 3 prinsip 13).
- Langkah penghubung (S-03, S-09): langkah 3, 12, 23, 35 (pemicu pelaku kedua, ditulis "hingga tersimpan", R-20), langkah 4, 13, 24, 36 ("Tunggu aksi selesai", bagian 8b butir 8), langkah 11, 21, 33 (membuka halaman agar tab awal Total Control tampil dan state hasil pemulihan dimuat), langkah 14 dan 25 (baseline peran individual), langkah 10, 20, 32, 41 (pemulihan baseline).
- Alasan di atas sekitar 35 langkah (41 langkah): keempat blok berdiri sendiri dalam satu topik "target berubah sejak render", memakai Sesi A dan Sesi B yang sama, dan tiap blok memulihkan datanya sendiri serta membuka halaman dari awal sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah blok serupa (pemicu Sesi B, tunggu, aksi Sesi A, toast, refresh) berulang per TC sesuai urutan yang diminta TC (S-04).
- Temuan untuk QA:
  - TC-AC-RP-394 sampai 397 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi. Konfirmasi bila QA menghendaki sesi UI kedua (spec dipindah ke kelas c).
  - TC-AC-RP-394 sampai 397 tidak menyebut akun Sesi B; spec memakai sesi API akun `Siti Nurhaliza` sendiri (Pre-setup #24 hanya menyebut "dua sesi paralel Total Control", S-13).
  - TC-AC-RP-394: "data di-refresh" tidak menyebut hal yang teramati; spec mengasersi tabel Role Detail dimuat ulang dan baris `John Dohan` tidak tampil.
  - TC-AC-RP-395: Expected "peran individual `John Doe` tidak disentuh lagi" tidak menyebut keadaan awal; spec membandingkan dengan baseline yang dicatat sesudah Sesi B tersimpan (Remove Total Control mereset peran individual).
  - TC-AC-RP-396: Expected "peran `Dewi Anggraini` tidak berubah" tidak menyebut keadaan awal; spec membandingkan dengan baseline yang dicatat sesudah Sesi B tersimpan.
  - TC-AC-RP-395, 396, 397: "+ refresh" tidak menyebut hal yang teramati; spec mengasersi baris target tidak tampil di tab yang bersangkutan dengan toast sebagai anchor (bagian 8b butir 2).
  - TC-AC-RP-394 sampai 397 tidak menyebut cara pemulihan "Data dipulihkan automation baseline"; mekanisme itu tidak didefinisikan di TC, PRD, atau LLD dan disebut kemampuan reset yang disediakan tim FE/BE (S-13).
