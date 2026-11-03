---
id: TC-AC-RP-E2E-029-checkbox-crud-in-flight-dan-keyboard
title: "Checkbox CRUD: Nonaktif Sementara saat In-flight dan Operasi Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-113
  - TC-AC-RP-114
coverage:
  web: automated
---

# Checkbox CRUD: Nonaktif Sementara saat In-flight dan Operasi Keyboard

## Prerequisites

- Mode: FE+BE. Penundaan respons PATCH memakai `Spectra.intercept()` di atas backend nyata (Tabel Data Uji Pre-setup #23); intercept dipasang pada langkah 3 dan dilepas pada langkah 7. Autosave ke server nyata.
- Akun aktor: Total Control Principal `Siti Nurhaliza`, `totalControlRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (akun yang sama) dan melepas intercept bila masih terpasang. Nama env `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #1 (`Siti Nurhaliza`), #11 (data Principal), #12 dan #15 (`John Dohan` memegang `Manage device master data` C/R/U, D tidak tercentang). Baris `John Dohan` pada Role Detail Pre-setup bersama menjadi target aksi tulis karena TC menetapkannya sebagai target (S-06, pengecualian 2026-10-30): checkbox D dipulihkan ke tidak tercentang lewat langkah 9 dan 16 serta lewat kemampuan reset baseline yang disediakan tim FE/BE (hook `before` dan `after`, pernyataan di `suite.md`). Efek: Last Updated baris `John Dohan` dan entri Changelog `Manage device master data` bertambah pada tiap run (audit trail permanen).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding dan suffix `+{runId}-029`.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-113: Checkbox CRUD in-flight dinonaktifkan sementara

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Tahan respons PATCH lewat `Spectra.intercept()` (penundaan respons)
4. Centang checkbox D baris `John Dohan`
5. Verifikasi cell D baris `John Dohan` menampilkan nilai baru (tercentang)
6. Verifikasi cell D baris `John Dohan` disabled selama respons tertunda
7. Lepas tahanan respons PATCH
8. Verifikasi cell D baris `John Dohan` enabled kembali
9. Hapus centang checkbox D baris `John Dohan`
10. Tunggu aksi selesai (cell D baris `John Dohan` enabled kembali)
11. Tunggu toast lama hilang otomatis

### TC-AC-RP-114: Checkbox CRUD dapat dioperasikan dengan keyboard

12. Fokus checkbox D baris `John Dohan` dengan Tab
13. Tekan Space
14. Verifikasi checkbox D baris `John Dohan` berubah state (tercentang)
15. Verifikasi toast "Success, permissions have been updated." tampil
16. Hapus centang checkbox D baris `John Dohan`
17. Tunggu aksi selesai (cell D baris `John Dohan` enabled kembali)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03, S-09): langkah 9 dan 10 (memulihkan D `John Dohan` ke tidak tercentang sebelum TC-AC-RP-114 mengandalkan state awal), langkah 11 (menunggu toast autosave lama hilang agar toast pada langkah 15 berasal dari aksi Space), dan langkah 16 dan 17 (memulihkan state setelah TC-AC-RP-114). Langkah 1 membuka Tab System yang dibutuhkan langkah berikutnya (S-14).
- Asersi state sementara (langkah 5 dan 6) ditulis sebelum respons dilepas (langkah 7) sesuai bagian 8b butir 5; intercept dilepas segera setelah pemicu selesai (S-09).
- Penundaan respons hanya untuk mengamati state UI (loading), bukan kegagalan yang dipaksa, sehingga bukan kelas b dan tetap di spec fungsional (prinsip 13 butir b).
- Temuan untuk QA:
  - TC-AC-RP-113 Expected "disabled sementara sampai respons diterima, lalu enabled kembali" tidak menyebut toast hasil; spec tidak mengasersi toast pada blok itu.
  - TC-AC-RP-113 dan 114 menetapkan baris Pre-setup `John Dohan` sebagai target aksi tulis tanpa menyebut mekanisme pemulihan; spec memakai kemampuan reset baseline yang disediakan tim FE/BE (S-13) dan memulihkan lewat UI pada langkah 9 dan 16.
  - TC-AC-RP-114 langkah 4 "Fokus checkbox D ... dengan Tab" tidak menyebut elemen awal fokus; spec menuliskan sesuai TC.
  - Post Condition TC-AC-RP-113 dan 114 bernilai "-" sehingga tidak ada yang diasersi.
