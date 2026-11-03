---
id: TC-AC-RP-E2E-127-bulk-remove-role-detail-baris-sudah-dihapus-admin-lain
title: "Bulk Remove Role Detail: Baris yang Sudah Dihapus Admin Lain Dianggap Sukses"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-197
coverage:
  web: automated
---

# Bulk Remove Role Detail: Baris yang Sudah Dihapus Admin Lain Dianggap Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Sesi A adalah sesi UI akun ini.
- Pelaku kedua (Sesi B): sesi API untuk akun Total Control yang sama (`totalControlRP_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.AC_RP_TC_PASSWORD`; hanya memicu perubahan state, tanpa asersi di sesinya (bukan konteks kedua kelas c; tidak butuh `P-2`). TC tidak menyebut akun Sesi B (lihat Temuan untuk QA).
- Data Pre-setup: #11, #12 (`Jane Smith`, `John Dohan`), #15 (`Manage device master data`: `John Dohan` C/R/U, `Jane Smith` R), #18 (Riwayat Changelog seed), #24 (dua sesi: Sesi A UI, Sesi B API).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Kemampuan teknis: sesi API aktor (dinyatakan di `suite.md`); kemampuan baca jumlah entri Changelog lewat modal Changelog `Manage device master data` (Table Tools); jumlah dibaca sebelum aksi sebagai baseline karena Changelog adalah audit trail permanen (S-12), tanpa angka absolut.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Sesi A: centang baris `Jane Smith` dan `John Dohan`
4. Sesi B (sesi API Total Control): Remove peran `Jane Smith` pada `Manage device master data` hingga tersimpan
5. Tunggu aksi selesai (Sesi B tersimpan)
6. Sesi A: buka modal Changelog `Manage device master data` melalui Table Tools
7. Catat jumlah entri Changelog sebagai baseline
8. Tutup modal Changelog
9. Sesi A: klik `Bulk Action` > `Remove` pada Bulk Action Bar lalu klik `[Remove]`
10. Verifikasi toast "Success, user has been removed."
11. Verifikasi toast tidak memuat "Some items were skipped." (baris `Jane Smith` yang sudah hilang tidak dihitung gagal)
12. Buka modal Changelog `Manage device master data` melalui Table Tools
13. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline langkah 7 (hanya untuk baris `John Dohan`; tidak ada entri tambahan untuk baris `Jane Smith`)
14. Tutup modal Changelog
15. Pulihkan baseline: `Jane Smith` dan `John Dohan` kembali memegang `Manage device master data` lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. TC-AC-RP-195 dan TC-AC-RP-196 ada di spec 057.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4 (pemicu pelaku kedua, "hingga tersimpan", R-20), langkah "Tunggu aksi selesai" sesudah pemicu (bagian 8b butir 8), langkah 7 (baseline jumlah entri Changelog), langkah 15 (pemulihan baseline).
- P-1: asersi "tidak menghasilkan entri log tambahan" pada TC-AC-RP-197 ditulis di spec ini sebagai `Verifikasi` berbaseline karena konteksnya bergantung pada state baris yang baru dihapus Sesi B; spec absence (kelas g) tidak memuat aksi nyata untuk TC ini (S-05).
- Temuan untuk QA:
  - TC-AC-RP-197 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi.
  - TC-AC-RP-197 tidak menyebut akun Sesi B ataupun akun Sesi A (Precondition hanya menyebut login Total Control `Siti Nurhaliza`); spec memakai `Siti Nurhaliza` untuk Sesi A (UI) dan sesi API akun yang sama untuk Sesi B.
  - TC-AC-RP-197 Expected: "tidak menghasilkan entri log tambahan" tidak menyebut surface log dan jumlah entri; spec memakai modal Changelog `Manage device master data` dan mengasumsikan satu entri per baris yang berhasil dihapus (sejalan dengan TC-AC-RP-329 "entri per baris berhasil").
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
