---
id: TC-AC-RP-E2E-057-bulk-remove-role-detail-stale-oleh-admin-lain
title: "Bulk Remove Role Detail: Partial Success dan 0 Baris Berhasil karena Baris Berubah oleh Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-195
  - TC-AC-RP-196
coverage:
  web: automated
---

# Bulk Remove Role Detail: Partial Success dan 0 Baris Berhasil karena Baris Berubah oleh Admin Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user and role (Update) `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hendra Wijaya`, Pre-setup #4; Sesi A), password dari `Spectra.env.AC_RP_MUR_U_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun UI di tengah spec.
- Pelaku kedua (Sesi B, Total Control): sesi API untuk `Siti Nurhaliza` (`totalControlRP_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.AC_RP_TC_PASSWORD`; hanya memicu perubahan state, tanpa asersi di sesinya (bukan konteks kedua kelas c; tidak butuh `P-2`).
- Data Pre-setup: #11, #12 (`Jane Smith`, `John Dohan`, `Maya Putri`), #15 (`Manage device master data`: `John Dohan` C/R/U, `Jane Smith` R, `Maya Putri` R, `Hendra Wijaya` R, `Fajar Nugroho` R), #18 (Riwayat Changelog seed), #24 (dua sesi: Sesi A UI, Sesi B API).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Kemampuan teknis: sesi API aktor (dinyatakan di `suite.md`); kemampuan baca jumlah entri Changelog lewat modal Changelog `Manage device master data` (Table Tools) di UI; jumlah entri dibaca sebelum aksi sebagai baseline karena Changelog adalah audit trail permanen (S-12), tanpa angka absolut.
- Env var `AC_RP_MUR_U_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e. Sama untuk `AC_RP_TC_PASSWORD`.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`

### TC-AC-RP-195: Bulk Remove partial success

3. Centang baris `Jane Smith`, `John Dohan`, dan `Maya Putri`
4. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Assign Read Only ke `Jane Smith` hingga tersimpan
5. Sesi A: klik `Bulk Action` > `Remove` pada Bulk Action Bar lalu klik `[Remove]`
6. Verifikasi toast "Success, user has been removed. Some items were skipped."
7. Verifikasi baris `John Dohan` dan `Maya Putri` tidak ada di tabel
8. Verifikasi baris `Jane Smith` ditolak per baris dan tetap ada di tabel
9. Verifikasi Bulk Action Bar tertutup
10. Verifikasi seleksi di-reset ke 0 (tidak ada baris tercentang)
11. Pulihkan baseline: `Jane Smith` kembali bukan Read Only serta `John Dohan` dan `Maya Putri` kembali memegang `Manage device master data` lewat kemampuan reset FE/BE
12. Muat ulang halaman (F5)

### TC-AC-RP-196: Bulk Remove dengan 0 baris berhasil

13. Centang baris `Jane Smith` dan `John Dohan`
14. Sesi B (sesi API `Siti Nurhaliza`, Total Control): Assign Read Only ke `Jane Smith` dan `John Dohan` hingga tersimpan
15. Sesi A: buka modal Changelog `Manage device master data` melalui Table Tools
16. Catat jumlah entri Changelog sebagai baseline
17. Tutup modal Changelog
18. Sesi A: klik `Bulk Action` > `Remove` pada Bulk Action Bar lalu klik `[Remove]`
19. Verifikasi toast "Error, failed to remove user."
20. Verifikasi baris `Jane Smith` dan `John Dohan` tetap ada di tabel (tidak ada baris terhapus)
21. Verifikasi Bulk Action Bar tertutup
22. Verifikasi seleksi di-reset ke 0 (tidak ada baris tercentang)
23. Buka modal Changelog `Manage device master data` melalui Table Tools
24. Verifikasi jumlah entri Changelog sama dengan baseline langkah 16 (tidak ada entri log baru)
25. Tutup modal Changelog
26. Pulihkan baseline: `Jane Smith` dan `John Dohan` kembali bukan Read Only lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-AC-RP-197 ada di spec 127.
- Aktor: Sesi A pada TC-AC-RP-195 dan TC-AC-RP-196 adalah `Hendra Wijaya` (Manage user and role); sesi B Total Control dijalankan lewat sesi API `Siti Nurhaliza` sesuai keputusan Admin B memakai sesi API (bagian 3 prinsip 13).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4 dan 14 (pemicu pelaku kedua, ditulis "hingga tersimpan", R-20), langkah 16 (baseline jumlah entri Changelog), langkah 17 dan 25 (tutup modal Changelog), langkah 11 dan 26 (pemulihan baseline), langkah 12 (muat ulang halaman agar tabel memuat state hasil pemulihan).
- P-1: asersi "tidak ada entri log" pada TC-AC-RP-196 ditulis di spec ini sebagai `Verifikasi` berbaseline karena konteksnya bergantung pada state baris yang baru diubah Sesi B; spec absence (kelas g) tidak memuat aksi nyata untuk TC ini (S-05). Baseline: jumlah entri Changelog `Manage device master data` sebelum aksi.
- Temuan untuk QA:
  - TC-AC-RP-195 dan TC-AC-RP-196 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi. Konfirmasi bila QA menghendaki sesi UI kedua.
  - TC-AC-RP-196 Expected: "tidak ada entri log" tidak menyebut surface log; spec memakai modal Changelog `Manage device master data` (Catatan TC menyebut modal Changelog per role).
  - TC-AC-RP-195 langkah 4 menggabungkan login Sesi A dan pemilihan baris; spec memakai login Hendra di hook `before` dan memilih baris sebagai langkah.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
