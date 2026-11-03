---
id: TC-AC-RP-E2E-053-remove-role-single-cancel-confirm-dan-group-role
title: "Remove User dari Role Single: Cancel, Confirm, dan Group Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-185
  - TC-AC-RP-186
  - TC-AC-RP-187
coverage:
  web: automated
---

# Remove User dari Role Single: Cancel, Confirm, dan Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #12 (`John Dohan`), #15 (`Manage device master data`: `John Dohan` C/R/U; `Manage distributor`: `John Dohan` `Region A` C/R/U dan `Branch 1` R).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`

### TC-AC-RP-186: Cancel dialog Remove Role

3. Klik `⋯` baris `John Dohan` lalu `Remove`
4. Klik `[Cancel]`
5. Verifikasi dialog tertutup
6. Verifikasi baris `John Dohan` tetap ada

### TC-AC-RP-185: Screening dan Confirm dialog Remove Role target Standard

7. Buka halaman `Settings > Role & Permission`, lalu klik tab `System`
8. Catat jumlah Users pada baris `Manage device master data` di Tab System sebagai baseline
9. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
10. Klik `⋯` baris `John Dohan` lalu `Remove`
11. Verifikasi dialog tampil: Title "Remove Role"; body • John D, "This will remove Manage device master data from this user." dan "Are you sure you want to remove it?"; tombol `[Cancel]` (Text, Contrast) dan `[Remove]` (destructive)
12. Klik `[Remove]`
13. Verifikasi toast "Success, user has been removed."
14. Verifikasi baris `John Dohan` tidak ada di tabel
15. Klik menu `Settings > Role & Permission` di sidebar
16. Klik tab `System`
17. Verifikasi jumlah Users `Manage device master data` di Tab System berkurang 1 dari baseline langkah 8
18. Pulihkan baseline: `John Dohan` kembali memegang `Manage device master data` lewat kemampuan reset FE/BE

### TC-AC-RP-187: Remove Role Group Role menghapus baris group itu saja

19. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
20. Klik `⋯` baris `John Dohan` — `Branch 1` lalu `Remove`
21. Klik `[Remove]`
22. Verifikasi toast "Success, user has been removed."
23. Verifikasi baris `John Dohan` — `Region A` tetap ada
24. Pulihkan baseline: `John Dohan` — `Branch 1` kembali memegang `Manage distributor` lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan menyimpang dari nomor TC: TC-AC-RP-186 (Cancel) lebih dulu karena menghapus baris `John Dohan` pada TC-AC-RP-185 mengubah data (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 8 (baseline jumlah Users di blok TC-AC-RP-185 sendiri, S-12), langkah 7 dan 9 (buka halaman, tab `System`, dan Detail untuk blok TC-AC-RP-185), klik sidebar dan klik tab (menuju Tab System untuk observasi jumlah Users), langkah 18 dan 24 (pemulihan baseline).
- Dialog konfirmasi ditulis satu `Verifikasi` karena judul, isi, dan tombol disebut utuh dalam satu butir Expected TC (S-01).
- Temuan untuk QA:
  - TC-AC-RP-185 Expected b: "Users ... di Tab System berkurang 1" tidak menyebut jumlah awal; spec mencatat baseline dari seeding (bagian 8b butir 10).
  - TC-AC-RP-187 Expected tidak menyebut baris `John Dohan` — `Branch 1` hilang; hanya `Region A` tetap. Spec mengikuti TC.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
