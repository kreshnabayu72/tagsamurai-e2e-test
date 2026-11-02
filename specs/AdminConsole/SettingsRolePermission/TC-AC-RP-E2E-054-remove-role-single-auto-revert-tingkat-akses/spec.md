---
id: TC-AC-RP-E2E-054-remove-role-single-auto-revert-tingkat-akses
title: "Remove Role Single: Baris Total Control dan Baris GM-Target Memicu Auto-Revert dalam Satu Transaksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-188
  - TC-AC-RP-189
coverage:
  web: automated
---

# Remove Role Single: Baris Total Control dan Baris GM-Target Memicu Auto-Revert dalam Satu Transaksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #13 (Total Control `Rina Wijaya`), #14 (GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera`), #15 (`Manage language` dengan baris `Rina Wijaya`; `Manage preload` dengan baris `Rina Wijaya`; `Manage partner` dengan baris `Fajar Nugroho`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

### TC-AC-RP-188: Remove baris TC memicu auto-revert dalam satu transaksi

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
3. Catat nilai C, R, U, dan D baris `Rina Wijaya` pada `Manage preload` sebagai pembanding peran lain
4. Klik menu `Settings > Role & Permission` di sidebar
5. Klik tab `System`
6. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
7. Klik `⋯` baris `Rina Wijaya` lalu `Remove`
8. Verifikasi dialog auto-revert Total Control tampil: Title "Remove Total Control", body "These users will lose Total Control access:" dengan bullet • Rina W, lalu "Are you sure you want to remove it?" (tanpa kata "edit"), tombol `[Cancel]` dan `[Remove]`
9. Klik `[Remove]`
10. Verifikasi toast "Success, permissions have been updated. Rina Wijaya is no longer Total Control."
11. Verifikasi baris `Rina Wijaya` tidak ada di tabel `Manage language`
12. Klik menu `Settings > Role & Permission` di sidebar
13. Verifikasi baris `Siti Nurhaliza` tampil di Tab Total Control
14. Verifikasi `Rina Wijaya` tidak ada di Tab Total Control
15. Klik tab `System`
16. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
17. Verifikasi peran lain tidak direset: nilai C, R, U, dan D baris `Rina Wijaya` pada `Manage preload` sama dengan nilai yang dicatat pada langkah 3
18. Pulihkan baseline: `Rina Wijaya` kembali Total Control dan memegang `Manage language` lewat kemampuan reset FE/BE

### TC-AC-RP-189: Remove baris GM-target memicu auto-revert GM

19. Klik menu `Settings > Role & Permission` di sidebar
20. Klik tab `System`
21. Pada section Group Role, klik `⋯` pada baris `Manage partner` lalu klik `Detail`
22. Klik node `Region Jawa`
23. Klik `⋯` baris `Fajar Nugroho` lalu `Remove`
24. Verifikasi dialog auto-revert Group Manager tampil: Title "Remove Group Manager", body "These users will lose Group Manager access:" dengan bullet • Fajar N, lalu "Are you sure you want to remove it?" (tanpa kata "edit"), tombol `[Cancel]` dan `[Remove]`
25. Klik `[Remove]`
26. Verifikasi toast "Success, permissions have been updated. Fajar Nugroho is no longer Group Manager for Region Jawa."
27. Verifikasi baris `Fajar Nugroho` — `Region Jawa` tidak ada di tabel `Manage partner`
28. Klik menu `Settings > Role & Permission` di sidebar
29. Klik tab `Group Manager`
30. Verifikasi baris `Fajar Nugroho` — `Sumatera` tampil di Tab Group Manager
31. Verifikasi baris `Fajar Nugroho` — `Region Jawa` tidak ada di Tab Group Manager (GM `Region Jawa` lepas)
32. Pulihkan baseline: `Fajar Nugroho` kembali GM `Region Jawa` dan memegang `Manage partner` lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3 (mencatat pembanding peran lain sebelum aksi), klik sidebar dan klik tab (menuju Tab Total Control, Tab Group Manager, dan Role Detail untuk observasi Expected), langkah 18 dan 32 (pemulihan baseline).
- Asersi tambahan (S-03): langkah 13 memverifikasi baris `Siti Nurhaliza` (aktor, Total Control) tampil di Tab Total Control sebagai pembanding positif sebelum asersi absence `Rina Wijaya` di langkah 14; langkah 30 memverifikasi baris `Fajar Nugroho` — `Sumatera` (GM lain) tampil di Tab Group Manager sebagai pembanding positif sebelum asersi absence `Region Jawa` di langkah 31 (bagian 8b butir 2).
- Dialog konfirmasi ditulis satu `Verifikasi` karena judul, isi, dan tombol disebut utuh dalam satu butir Expected TC (S-01).
- Temuan untuk QA:
  - TC-AC-RP-188 Expected b: "peran lain tidak direset" tidak menyebut role atau nilainya; spec memakai `Manage preload` baris `Rina Wijaya` (role yang diketahui memuat baris `Rina Wijaya` pada TC-AC-RP-176 sampai 178) dengan nilai dicatat sebelum aksi sebagai pembanding.
  - TC-AC-RP-188 dan 189 tidak menyebut cara kembali dari Role Detail ke tab daftar; spec memakai klik sidebar.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
