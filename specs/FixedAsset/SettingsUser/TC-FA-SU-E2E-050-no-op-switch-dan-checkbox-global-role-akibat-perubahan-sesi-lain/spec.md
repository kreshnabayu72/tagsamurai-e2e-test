---
id: TC-FA-SU-E2E-050-no-op-switch-dan-checkbox-global-role-akibat-perubahan-sesi-lain
title: "No-op Switch dan Checkbox Global Role Akibat Perubahan Sesi Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-169
  - TC-FA-SU-170
coverage:
  web: automated
---

# No-op Switch dan Checkbox Global Role Akibat Perubahan Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor (Admin A, sesi UI): Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua (Admin B, Pre-setup #13): akun yang sama dengan sesi API aktor (lihat `suite.md`); hanya memicu perubahan state sehingga tidak memakai sesi UI kedua.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23): target Gita Permata dengan Manage asset ID configuration OFF tanpa nilai tersimpan, serta Manage accounting ON dengan Update tidak tercentang. Seed API memulihkan keadaan ini di hook `before` dan `after` (Catatan TC).
- Baseline log: langkah 5 dan 16 mencatat jumlah entri `Assign` (TC-FA-SU-169) dan `Edit` (TC-FA-SU-170) setelah aksi Admin B, pada Tab Changelog target, Tab System Log aktor, dan Activity Log (kemampuan baca disediakan tim FE/BE; bagian 8b butir 10). Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Kemampuan teknis (disediakan tim FE/BE): jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC).
- State global dan pemulihan: penugasan Global Role Gita berubah (Manage asset ID configuration ON; Update Manage accounting tercentang) dan dipulihkan lewat seed API di hook `after`; entri log Assign dan Edit dari Admin B bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-169: Switch ke nilai yang sudah berlaku

1. Buka Detail Gita Permata > Tab Role > Sub-tab Global Role (Admin A)
2. Verifikasi switch Manage asset ID configuration OFF pada tampilan Admin A
3. Admin B (sesi API) menyalakan switch Manage asset ID configuration Gita Permata hingga tersimpan
4. Tunggu aksi selesai: permintaan sesi API Admin B selesai
5. Catat jumlah entri `Assign` Gita Permata di Tab Changelog sebagai baseline
6. Admin A klik switch Manage asset ID configuration pada tampilan basi
7. Verifikasi toast "Success, role has been updated."
8. Verifikasi switch Manage asset ID configuration ON (tampilan di-refresh ke state server)
9. Buka Tab Changelog Gita Permata, muat ulang sampai entri tampil
10. Verifikasi entri `Assign` dari Admin B tampil di Tab Changelog
11. Verifikasi jumlah entri `Assign` di Tab Changelog sama dengan baseline langkah 5 (tidak ada entri log baru)

### TC-FA-SU-170: Checkbox ke nilai yang sudah berlaku

12. Buka Tab Role > Sub-tab Global Role Gita Permata (Admin A)
13. Verifikasi checkbox Update baris Manage accounting tidak tercentang pada tampilan Admin A
14. Admin B (sesi API) mencentang Update Manage accounting Gita Permata hingga tersimpan
15. Tunggu aksi selesai: permintaan sesi API Admin B selesai
16. Tunggu entri `Edit` dari Admin B muncul lewat kemampuan baca, lalu catat jumlah entri `Edit` di Tab Changelog, Tab System Log aktor, dan Activity Log sebagai baseline
17. Admin A centang Update pada baris Manage accounting pada tampilan basi
18. Verifikasi toast "Success, permissions have been updated."
19. Buka Tab Changelog Gita Permata, muat ulang halaman
20. Verifikasi jumlah entri `Edit` di Tab Changelog sama dengan baseline langkah 16
21. Buka Tab System Log aktor
22. Verifikasi jumlah entri `Edit` di Tab System Log aktor sama dengan baseline langkah 16
23. Buka Activity Log
24. Verifikasi jumlah entri `Edit` di Activity Log sama dengan baseline langkah 16

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Pelaku kedua lewat sesi API (R-20): langkah 3 dan 14 hanya memicu perubahan state dan bukan objek asersi; tidak memakai `P-2` (keputusan 2026-10-30).
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 4 dan 15 (menunggu aksi pelaku kedua selesai, bagian 8b butir 8), langkah 5 dan 16 (mencatat baseline lewat kemampuan baca tanpa navigasi UI), langkah 9, 12, 19, 21, dan 23 (membuka surface log atau sub-tab).
- Asersi tambahan di luar Expected TC: langkah 2 dan 13 (tampilan Admin A masih menunjukkan nilai lama) membuktikan tampilan basi; langkah 8 menerjemahkan "tampilan di-refresh ke state server" pada Expected b TC-FA-SU-169; langkah 10 adalah anchor positif bagi asersi jumlah langkah 11 (bagian 8b butir 2); toast langkah 18 menjadi anchor bagi asersi jumlah langkah 20, 22, dan 24.
- Temuan untuk QA:
  - Judul TC-FA-SU-169 menyebut "toast sukses aksi yang sama" sedangkan Expected a menulis "bukan toast no-op"; spec mengasersi toast "Success, role has been updated." sesuai Expected.
  - Expected b TC-FA-SU-169 ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Tab Changelog target. Expected b TC-FA-SU-170 menyebut "tiga permukaan log" dan diasersi pada ketiganya.
  - TC-FA-SU-170 Langkah Uji 4 ("Hitung entri `Edit`") tidak menyebut surface; spec menghitung pada Tab Changelog target, Tab System Log aktor, dan Activity Log sesuai Expected b.
  - Post Condition kedua TC ("tidak ada entri log tambahan dari sesi basi") diasersi lewat Expected b dan tidak diasersi terpisah.
