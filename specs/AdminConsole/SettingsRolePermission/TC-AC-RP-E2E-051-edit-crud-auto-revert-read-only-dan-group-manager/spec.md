---
id: TC-AC-RP-E2E-051-edit-crud-auto-revert-read-only-dan-group-manager
title: "Edit CRUD: Dialog Auto-Revert Read Only dan Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-179
  - TC-AC-RP-180
coverage:
  web: automated
---

# Edit CRUD: Dialog Auto-Revert Read Only dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #3 dan #13 (Read Only `Dewi Anggraini`, memegang `Manage preload`), #6 dan #14 (GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera`; GM juga memegang Group Role CRUD penuh pada group GM-nya), #15 (`Manage partner`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`

### TC-AC-RP-179: Edit CRUD target Read Only memunculkan dialog auto-revert Read Only

3. Centang C pada baris `Dewi Anggraini`
4. Verifikasi dialog auto-revert tampil: Title "Remove Read Only", bullet • Dewi A, body "This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited." dan "Are you sure you want to remove it?", tombol `[Cancel]` dan `[Remove]`
5. Klik `[Remove]`
6. Verifikasi toast "Success, permissions have been updated. Dewi Anggraini is no longer Read Only."
7. Verifikasi C `Manage preload` baris `Dewi Anggraini` tetap tercentang
8. Klik menu `Settings > Role & Permission` di sidebar
9. Klik tab `Read Only`
10. Verifikasi baris `Lisa Wong` tampil di Tab Read Only
11. Verifikasi `Dewi Anggraini` tidak ada di Tab Read Only
12. Pulihkan baseline: `Dewi Anggraini` kembali Read Only dan C `Manage preload` tidak tercentang lewat kemampuan reset FE/BE

### TC-AC-RP-180: Edit CRUD GM-target di group GM memunculkan dialog auto-revert Group Manager

13. Klik tab `System`
14. Pada section Group Role, klik `⋯` pada baris `Manage partner` lalu klik `Detail`
15. Klik node `Region Jawa`
16. Hapus centang U pada baris `Fajar Nugroho`
17. Verifikasi dialog auto-revert tampil: Title "Remove Group Manager", bullet • Fajar N, body "This edit will remove Group Manager status for this group. Their role permissions in this group will remain as edited." dan "Are you sure you want to remove it?", tombol `[Cancel]` dan `[Remove]`
18. Klik `[Remove]`
19. Verifikasi toast "Success, permissions have been updated. Fajar Nugroho is no longer Group Manager for Region Jawa."
20. Klik menu `Settings > Role & Permission` di sidebar
21. Klik tab `Group Manager`
22. Verifikasi baris `Fajar Nugroho` — `Sumatera` tetap ada di Tab Group Manager
23. Verifikasi baris `Fajar Nugroho` — `Region Jawa` tidak ada di Tab Group Manager
24. Klik tab `System`
25. Pada section Group Role, klik `⋯` pada baris `Manage partner` lalu klik `Detail`
26. Klik node `Region Jawa`
27. Verifikasi peran hasil editan dipertahankan: U baris `Fajar Nugroho` pada `Manage partner` `Region Jawa` tidak tercentang
28. Pulihkan baseline: `Fajar Nugroho` kembali GM `Region Jawa` dan U `Manage partner` `Region Jawa` tercentang lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-AC-RP-184 (auto-revert Group Manager lewat Detail User) ada di spec 126.
- Langkah penghubung (tanpa `Verifikasi`, S-03): klik sidebar dan klik tab (menuju Tab Read Only, Tab Group Manager, dan Role Detail untuk observasi Expected), langkah 12 dan 28 (pemulihan baseline).
- Asersi tambahan (S-03): langkah 10 memverifikasi baris `Lisa Wong` tampil di Tab Read Only sebagai pembanding positif sebelum asersi absence `Dewi Anggraini` di langkah 11; di Tab Group Manager, baris `Fajar Nugroho` — `Sumatera` (langkah 22) menjadi pembanding positif sebelum asersi absence `Region Jawa` (langkah 23) (bagian 8b butir 2).
- Dialog konfirmasi ditulis satu `Verifikasi` karena judul, isi, dan tombol disebut utuh dalam satu butir Expected TC (S-01).
- Temuan untuk QA:
  - TC-AC-RP-179 dan TC-AC-RP-180 langkah 7 (TC-AC-RP-180) tidak menyebut cara kembali dari Role Detail ke tab daftar; spec memakai klik sidebar (langkah penghubung).
  - TC-AC-RP-180 Expected c: "peran hasil editan dipertahankan" tidak menyebut nilai; spec mengasersi U `Manage partner` `Region Jawa` tidak tercentang sebagai hasil editan langkah 5 TC.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
