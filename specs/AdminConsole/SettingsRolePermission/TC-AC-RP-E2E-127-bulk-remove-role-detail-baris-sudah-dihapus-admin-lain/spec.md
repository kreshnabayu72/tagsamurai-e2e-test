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
- Data Pre-setup: #11, #12 (`Jane Smith`, `John Dohan`), #15 (`Manage device master data`: `John Dohan` C/R/U, `Jane Smith` R), #24 (dua sesi: Sesi A UI, Sesi B API).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Kemampuan teknis: sesi API aktor (dinyatakan di `suite.md`); kemampuan baca jumlah entri audit trail pelaku (Detail User `Siti Nurhaliza` > Tab System Log dan Activity Log Admin Console) yang disediakan tim FE/BE (8b butir 10), dipakai untuk baseline dan pembacaan sesudah aksi tanpa berpindah halaman, supaya Sesi A tetap berada di Role Detail dengan baris yang dicentang; jumlah dibaca sebelum aksi sebagai baseline karena audit trail permanen (S-12), tanpa angka absolut.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Sesi A: centang baris `Jane Smith` dan `John Dohan`
4. Sesi B (sesi API Total Control): Remove peran `Jane Smith` pada `Manage device master data` hingga tersimpan
5. Tunggu aksi selesai (Sesi B tersimpan)
6. Catat baseline jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console pelaku
7. Sesi A: klik `Bulk Action` > `Remove` pada Bulk Action Bar lalu klik `[Remove]`
8. Verifikasi toast "Success, user has been removed."
9. Verifikasi toast tidak memuat "Some items were skipped." (baris `Jane Smith` yang sudah hilang tidak dihitung gagal)
10. Verifikasi selisih jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log terhadap baseline langkah 6 hanya entri Remove `John Dohan` (tidak ada entri log tambahan untuk baris `Jane Smith`)
11. Verifikasi selisih jumlah entri Activity Log Admin Console pelaku terhadap baseline langkah 6 hanya entri Remove `John Dohan` (tidak ada entri log tambahan untuk baris `Jane Smith`)
12. Pulihkan baseline: `Jane Smith` dan `John Dohan` kembali memegang `Manage device master data` lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. TC-AC-RP-195 dan TC-AC-RP-196 ada di spec 057.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4 (pemicu pelaku kedua, "hingga tersimpan", R-20), langkah "Tunggu aksi selesai" sesudah pemicu (bagian 8b butir 8), langkah 6 (baseline jumlah entri Detail User pelaku > Tab System Log dan Activity Log Admin Console, S-12; ditulis sesudah pemicu Sesi B dan sebelum aksi Sesi A sesuai urutan TC), langkah 12 (pemulihan baseline).
- P-1: asersi "tidak menghasilkan entri log tambahan" pada TC-AC-RP-197 (langkah 10 dan 11, satu `Verifikasi` per surface) ditulis di spec ini sebagai `Verifikasi` berbaseline karena konteksnya bergantung pada state baris yang baru dihapus Sesi B; spec absence (kelas g) tidak memuat aksi nyata untuk TC ini (S-05).
- Temuan untuk QA:
  - TC-AC-RP-197 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi.
  - TC-AC-RP-197 tidak menyebut akun Sesi B ataupun akun Sesi A (Precondition hanya menyebut login Total Control `Siti Nurhaliza`); spec memakai `Siti Nurhaliza` untuk Sesi A (UI) dan sesi API akun yang sama untuk Sesi B.
  - TC-AC-RP-197 Expected menyebut surface Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console; spec mengasersi keduanya dengan baseline (langkah 6) sebelum pemicu Sesi A. Redaksi Expected ditandai tidak pasti oleh TC editor ("tidak menghasilkan entri log tambahan; selisih hanya entri Remove `John Dohan`"): spec mengikuti teks TC apa adanya, yaitu selisih terhadap baseline hanya entri Remove `John Dohan` tanpa entri untuk `Jane Smith`; jumlah entri per baris yang berhasil dihapus tidak disebut TC. Mohon QA mengonfirmasi redaksi dan apakah pelaku Sesi B (akun yang sama dengan Sesi A) menambah entri sebelum baseline.
  - TC-AC-RP-197 Expected "baris yang sudah hilang (`Jane Smith`) tidak dihitung gagal" tidak menyebut teks UI; langkah 9 menurunkannya dari toast parsial TC-AC-RP-195 ("Success, user has been removed. Some items were skipped.") dengan mengasersi toast tidak memuat "Some items were skipped.". Teks itu bukan teks Expected TC-AC-RP-197 yang hanya menyebut toast "Success, user has been removed." (S-03, S-15).
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
