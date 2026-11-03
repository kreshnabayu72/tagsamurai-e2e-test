---
id: TC-AC-RP-E2E-126-edit-crud-auto-revert-group-manager-lewat-detail-user
title: "Auto-Revert Group Manager: Melepas Seluruh Peran Grup dari Detail User Mencabut GM di Seluruh Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-184
coverage:
  web: automated
---

# Auto-Revert Group Manager: Melepas Seluruh Peran Grup dari Detail User Mencabut GM di Seluruh Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #6 dan #14 (GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera`; GM `Jane Smith` di `Region Jawa`), #15 (`Manage partner` dipegang `Fajar Nugroho`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab Role, Sub-tab Group Role) tersedia untuk akun Total Control; dibuka lewat sidebar `Settings > User`.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik menu `Settings > User` di sidebar
2. Ketik Search "Fajar Nugroho", tekan Enter
3. Buka Detail User `Fajar Nugroho`
4. Klik Tab `Role`
5. Klik Sub-tab `Group Role`
6. Klik `[Assign Group]` pada baris `Manage partner`
7. Klik `[Clear Field]`
8. Klik `[Save]` (Save 0 group)
9. Verifikasi dialog Auto-Revert Group Manager muncul sebelum perubahan disimpan
10. Pada dialog Auto-Revert Group Manager, klik `[Remove Group Manager]`
11. Tunggu aksi selesai (dialog tertutup)
12. Klik menu `Settings > Role & Permission` di sidebar
13. Klik tab `Group Manager`
14. Verifikasi baris `Jane Smith` — `Region Jawa` tampil di Tab Group Manager
15. Verifikasi kedua baris GM `Fajar Nugroho` (`Region Jawa` dan `Sumatera`) tidak ada di Tab Group Manager
16. Pulihkan baseline: `Fajar Nugroho` kembali GM `Region Jawa` dan `Sumatera` serta Group Role `Manage partner` lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Satu TC ini ada di spec tersendiri karena memakai halaman Settings > User; TC-AC-RP-179 dan TC-AC-RP-180 ada di spec 051.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 2 (Search untuk menemukan user target), langkah 11 (tunggu aksi selesai karena langkah berikutnya berpindah surface, bagian 8b butir 8), klik sidebar dan klik tab (menuju Tab Group Manager), langkah 16 (pemulihan baseline).
- Asersi tambahan (S-03): `Verifikasi` baris `Jane Smith` — `Region Jawa` adalah pembanding generik sebagai anchor positif bagi absence baris `Fajar Nugroho` (bagian 8b butir 2); Pre-setup #14 menyebut baris itu.
- Temuan untuk QA:
  - TC-AC-RP-184 memakai tombol dialog `[Remove Group Manager]`, sedangkan NC-01 (resolusi 2026-10-08) menetapkan `[Remove]` untuk dialog auto-revert Role & Permission; spec mengikuti TC. Konfirmasi apakah dialog di Detail User memang berbeda.
  - TC-AC-RP-184 tidak menyebut cara menemukan `Fajar Nugroho` di Settings > User; spec memakai Search.
  - TC-AC-RP-184 Expected a berbunyi "Langkah 3" dan b "Langkah 4"; spec memetakannya ke dialog dan Tab Group Manager sesuai isi.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
