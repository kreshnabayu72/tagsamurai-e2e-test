---
id: TC-AC-RP-E2E-049-edit-crud-autosave-target-standard
title: "Edit CRUD Autosave: Check, Uncheck Target Standard, dan Group Role per Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-172
  - TC-AC-RP-173
  - TC-AC-RP-174
coverage:
  web: automated
---

# Edit CRUD Autosave: Check, Uncheck Target Standard, dan Group Role per Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #12 (`Jane Smith`, `John Dohan`), #15 (`Manage device master data`: `John Dohan` C/R/U, `Jane Smith` R; `Manage distributor`: `John Dohan` `Region A` C/R/U dan `Branch 1` R).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Kemampuan teknis: muat ulang halaman (F5) pada Role Detail; tidak ada form dirty karena perubahan tersimpan otomatis.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`

### TC-AC-RP-172: Edit CRUD target Standard tersimpan otomatis

3. Centang C pada baris `Jane Smith`
4. Verifikasi toast "Success, permissions have been updated."
5. Verifikasi tidak ada tombol `[Save]` pada halaman Role Detail
6. Muat ulang halaman (F5)
7. Verifikasi checkbox C baris `Jane Smith` tetap tercentang setelah refresh

### TC-AC-RP-173: Uncheck CRUD target Standard tersimpan otomatis

8. Hapus centang U pada baris `John Dohan`
9. Verifikasi toast "Success, permissions have been updated."
10. Muat ulang halaman (F5)
11. Verifikasi nilai U baris `John Dohan` tidak tercentang setelah refresh

### TC-AC-RP-174: Edit CRUD Group Role per group independen

12. Klik menu `Settings > Role & Permission` di sidebar
13. Klik tab `System`
14. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
15. Catat nilai C, R, U, dan D baris `John Dohan` — `Region A` sebagai pembanding
16. Centang U pada baris `John Dohan` — `Branch 1`
17. Verifikasi toast sukses tampil
18. Verifikasi baris `John Dohan` — `Region A` tidak berubah dari nilai yang dicatat pada langkah 15
19. Pulihkan baseline: `Jane Smith` C dan `John Dohan` U pada `Manage device master data`, serta `John Dohan` U pada `Branch 1` `Manage distributor`, lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 6 dan 10 (muat ulang halaman untuk Expected "setelah refresh"; tidak ada form dirty), langkah 15 (mencatat pembanding untuk asersi "tidak berubah"), langkah 19 (pemulihan baseline).
- Temuan untuk QA:
  - TC-AC-RP-174 Expected: "Toast sukses" tidak menyebut teksnya; spec tidak mengasersi teks toast. Teks pada TC-AC-RP-172 dan 173 adalah "Success, permissions have been updated.".
  - TC-AC-RP-174 Expected: "baris `John Dohan` — `Region A` tidak berubah" tidak menyebut nilai awalnya; spec mencatat nilai sebelum aksi sebagai pembanding (Pre-setup #15: C/R/U).
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
