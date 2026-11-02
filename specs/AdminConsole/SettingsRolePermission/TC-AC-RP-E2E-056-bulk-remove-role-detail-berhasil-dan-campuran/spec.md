---
id: TC-AC-RP-E2E-056-bulk-remove-role-detail-berhasil-dan-campuran
title: "Bulk Remove Role Detail: Dua Baris Standard dan Campuran Standard dan Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-190
  - TC-AC-RP-191
coverage:
  web: automated
---

# Bulk Remove Role Detail: Dua Baris Standard dan Campuran Standard dan Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #12 (`Jane Smith`, `John Dohan`), #13 (Total Control `Rina Wijaya`), #15 (`Manage device master data` memuat baris `Jane Smith`, `John Dohan`, `Rina Wijaya`; `Manage distributor`: `John Dohan` `Region A` C/R/U).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`

### TC-AC-RP-190: Bulk Remove dua baris Standard

3. Centang baris `Jane Smith` dan `John Dohan`
4. Klik `Bulk Action` > `Remove` pada Bulk Action Bar
5. Verifikasi dialog tampil: Title "Remove Roles", body • Jane S, • John D, "This will remove Manage device master data from these users." dan "Are you sure you want to remove them?"
6. Klik `[Remove]`
7. Verifikasi toast "Success, user has been removed."
8. Verifikasi baris `Jane Smith` dan `John Dohan` tidak ada di tabel
9. Verifikasi Bulk Action Bar tertutup
10. Verifikasi seleksi di-reset (tidak ada baris tercentang)
11. Pulihkan baseline: `Jane Smith` dan `John Dohan` kembali memegang `Manage device master data` lewat kemampuan reset FE/BE
12. Muat ulang halaman (F5)

### TC-AC-RP-191: Bulk Remove campuran Standard dan Total Control

13. Centang baris `John Dohan` dan `Rina Wijaya`
14. Klik `Bulk Action` > `Remove` pada Bulk Action Bar
15. Verifikasi dialog tampil: Title "Remove Roles", body • Rina W — "Total Control", • John D, "This will remove Manage device master data from these users.", "Rina W will lose their access level as a result." dan "Are you sure you want to remove them?"
16. Klik `[Remove]`
17. Verifikasi toast "Success, user has been removed."
18. Klik menu `Settings > Role & Permission` di sidebar
19. Verifikasi baris `Siti Nurhaliza` tampil di Tab Total Control
20. Verifikasi `Rina Wijaya` tidak ada di Tab Total Control
21. Klik tab `System`
22. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
23. Verifikasi peran lain `John Dohan` tidak terpengaruh: baris `John Dohan` — `Region A` pada `Manage distributor` tetap ada dengan C, R, dan U tercentang
24. Pulihkan baseline: `John Dohan` dan `Rina Wijaya` kembali memegang `Manage device master data` dan `Rina Wijaya` kembali Total Control lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-AC-RP-192 sampai 194 dan 200 ada di spec 055.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 11 dan 24 (pemulihan baseline antar blok TC), langkah 12 (muat ulang halaman agar tabel memuat state hasil pemulihan; tidak ada form dirty), klik sidebar dan klik tab (menuju Tab Total Control dan Role Detail untuk observasi Expected).
- Asersi tambahan (S-03): langkah 19 memverifikasi baris `Siti Nurhaliza` (aktor, Total Control) tampil di Tab Total Control sebagai pembanding positif sebelum asersi absence `Rina Wijaya` di langkah 20 (bagian 8b butir 2).
- Dialog konfirmasi ditulis satu `Verifikasi` karena judul dan isi disebut utuh dalam satu butir Expected TC (S-01).
- Temuan untuk QA:
  - TC-AC-RP-191 Expected b: "peran lain `John Dohan` tidak terpengaruh" tidak menyebut role; spec memakai `Manage distributor` `Region A` (Pre-setup #15: C/R/U).
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
