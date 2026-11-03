---
id: TC-AC-RP-E2E-052-edit-crud-tanpa-auto-revert-dan-susun-ulang
title: "Edit CRUD: Assignment Descendant, Peran Global Target GM, dan Susun Ulang Peran Manual Tanpa Auto-Revert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-181
  - TC-AC-RP-182
  - TC-AC-RP-183
coverage:
  web: automated
---

# Edit CRUD: Assignment Descendant, Peran Global Target GM, dan Susun Ulang Peran Manual Tanpa Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #13 (Total Control `Rina Wijaya`), #14 (GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera`), #15 (`Fajar Nugroho` memegang `Manage partner` R langsung di `Jakarta`; `Manage device master data` R untuk `Fajar Nugroho`; `Manage preload` dengan baris `Rina Wijaya`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage partner` lalu klik `Detail`

### TC-AC-RP-181: Edit assignment langsung di descendant tidak memicu auto-revert GM ancestor

3. Klik node `Jakarta`
4. Centang C pada baris `Fajar Nugroho` — `Jakarta`
5. Verifikasi toast "Success, permissions have been updated."
6. Verifikasi tidak ada dialog auto-revert tampil
7. Klik menu `Settings > Role & Permission` di sidebar
8. Klik tab `Group Manager`
9. Verifikasi baris `Fajar Nugroho` — `Region Jawa` tetap ada di Tab Group Manager
10. Pulihkan baseline: C `Fajar Nugroho` — `Jakarta` pada `Manage partner` tidak tercentang lewat kemampuan reset FE/BE

### TC-AC-RP-182: Edit Peran Global target GM tidak melepas GM

11. Klik tab `System`
12. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
13. Centang C pada baris `Fajar Nugroho`
14. Verifikasi toast "Success, permissions have been updated."
15. Verifikasi tidak ada dialog auto-revert tampil
16. Klik menu `Settings > Role & Permission` di sidebar
17. Klik tab `Group Manager`
18. Verifikasi baris GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera` tetap ada di Tab Group Manager
19. Pulihkan baseline: C `Fajar Nugroho` pada `Manage device master data` tidak tercentang lewat kemampuan reset FE/BE

### TC-AC-RP-183: Menyusun ulang peran manual tidak mengembalikan tingkat akses

20. Klik tab `System`
21. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
22. Hapus centang D baris `Rina Wijaya`
23. Klik `[Remove]` pada dialog auto-revert (konfirmasi)
24. Tunggu toast lama hilang otomatis
25. Centang kembali D baris `Rina Wijaya`
26. Verifikasi toast "Success, permissions have been updated."
27. Verifikasi tidak ada dialog auto-revert tampil
28. Klik menu `Settings > Role & Permission` di sidebar
29. Verifikasi baris `Siti Nurhaliza` tampil di Tab Total Control
30. Verifikasi `Rina Wijaya` tidak ada di Tab Total Control
31. Pulihkan baseline: `Rina Wijaya` kembali Total Control dan D `Manage preload` tercentang lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`, S-03): klik sidebar dan klik tab (menuju Tab Group Manager dan Tab Total Control untuk observasi Expected), langkah 24 (menunggu toast konfirmasi hilang agar toast berikutnya tidak tertukar, R-12), langkah 10, 19, 31 (pemulihan baseline).
- Asersi tambahan (S-03): langkah 29 memverifikasi baris `Siti Nurhaliza` (aktor, Total Control) tampil di Tab Total Control sebagai pembanding positif sebelum asersi absence `Rina Wijaya` di langkah 30 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-RP-183 Expected berbunyi "Langkah 3 menampilkan toast ... tanpa dialog", tetapi langkah 3 TC adalah membuka Role Detail; yang dimaksud adalah langkah 5 (centang kembali D). Spec mengasersi toast dan ketiadaan dialog sesudah centang kembali.
  - TC-AC-RP-183 tidak menyebut toast atau dialog sesudah konfirmasi di langkah 4; spec tidak mengasersinya (tidak ada Expected padanan).
  - TC-AC-RP-181 dan 182: "tidak ada dialog auto-revert" diasersi sesudah toast sukses sebagai anchor bahwa respons sudah diproses (bagian 8b butir 11).
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
