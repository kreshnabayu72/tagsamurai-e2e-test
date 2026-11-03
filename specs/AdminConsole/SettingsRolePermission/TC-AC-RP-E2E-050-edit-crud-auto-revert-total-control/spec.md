---
id: TC-AC-RP-E2E-050-edit-crud-auto-revert-total-control
title: "Edit CRUD: Dialog Auto-Revert Total Control (Cancel lalu Confirm)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-176
  - TC-AC-RP-177
  - TC-AC-RP-178
coverage:
  web: automated
---

# Edit CRUD: Dialog Auto-Revert Total Control (Cancel lalu Confirm)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #13 (Total Control `Rina Wijaya`), #15 (`Manage preload` dengan baris `Rina Wijaya`; `Manage language` CRUD penuh `Rina Wijaya`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`

### TC-AC-RP-176 dan TC-AC-RP-178: Dialog auto-revert Total Control tampil lalu di-Cancel

3. Hapus centang D pada baris `Rina Wijaya`
4. Verifikasi dialog auto-revert tampil sebelum perubahan disimpan: Title "Remove Total Control", bullet • Rina W, body "This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited." dan "Are you sure you want to remove it?", tombol `[Cancel]` dan `[Remove]`
5. Klik `[Cancel]`
6. Verifikasi checkbox D baris `Rina Wijaya` kembali tercentang
7. Verifikasi tidak ada toast tampil
8. Klik menu `Settings > Role & Permission` di sidebar
9. Verifikasi `Rina Wijaya` tetap tampil di Tab Total Control

### TC-AC-RP-177: Konfirmasi auto-revert Total Control

10. Klik tab `System`
11. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
12. Hapus centang D pada baris `Rina Wijaya`
13. Klik `[Remove]` pada dialog
14. Verifikasi toast "Success, permissions have been updated. Rina Wijaya is no longer Total Control."
15. Klik menu `Settings > Role & Permission` di sidebar
16. Verifikasi baris `Siti Nurhaliza` tampil di Tab Total Control
17. Verifikasi `Rina Wijaya` tidak ada di Tab Total Control (tingkat akses Standard)
18. Klik tab `System`
19. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
20. Verifikasi Read baris `Rina Wijaya` pada `Manage preload` tetap aktif
21. Verifikasi Delete baris `Rina Wijaya` pada `Manage preload` nonaktif
22. Klik menu `Settings > Role & Permission` di sidebar
23. Klik tab `System`
24. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
25. Verifikasi baris `Rina Wijaya` pada `Manage language` tetap CRUD penuh (tidak direset)
26. Pulihkan baseline: `Rina Wijaya` kembali Total Control dan D `Manage preload` tercentang lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: dialog TC-AC-RP-176 dan Cancel TC-AC-RP-178 memakai satu pembukaan dialog yang sama; konfirmasi TC-AC-RP-177 di akhir karena mengubah data (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): klik sidebar dan klik tab (menuju Tab Total Control dan Role Detail untuk observasi Expected), langkah 26 (pemulihan baseline). Pengamatan `Rina Wijaya` di Tab Total Control sesudah Cancel adalah observasi Expected TC-AC-RP-178 butir "tetap Total Control".
- Asersi tambahan (S-03): langkah 16 memverifikasi baris `Siti Nurhaliza` (aktor, Total Control) tampil di Tab Total Control sebagai pembanding positif sebelum asersi absence `Rina Wijaya` di langkah 17 (bagian 8b butir 2).
- Dialog konfirmasi ditulis satu `Verifikasi` karena judul, isi, dan tombol disebut utuh dalam satu butir Expected TC (S-01).
- Temuan untuk QA:
  - TC-AC-RP-176 Expected: "tampil sebelum perubahan disimpan" tidak punya cara observasi di TC; spec mengasersi dialog tampil sesudah centang dihapus tanpa langkah observasi tambahan.
  - TC-AC-RP-178 langkah tidak memuat langkah menuju Tab Total Control, padahal Expected "`Rina Wijaya` tetap Total Control" membutuhkannya; spec menambah langkah penghubung klik sidebar.
  - TC-AC-RP-177 langkah 7 menyebut `Buka Detail Manage language` tanpa menyebut cara kembali dari Role Detail; spec memakai klik sidebar lalu tab `System` (langkah penghubung).
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
