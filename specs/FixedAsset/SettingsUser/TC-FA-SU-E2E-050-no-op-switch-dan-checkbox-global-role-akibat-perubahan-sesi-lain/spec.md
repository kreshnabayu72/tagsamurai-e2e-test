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
- Baseline log: langkah 6 dan 17 mencatat jumlah entri `Assign` (TC-FA-SU-169) dan `Edit` (TC-FA-SU-170) setelah entri aksi Admin B tampil (ditunggu lewat kemampuan baca), pada Tab Changelog target, Tab System Log aktor, dan Activity Log (kemampuan baca disediakan tim FE/BE; bagian 8b butir 10). Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Kemampuan teknis (disediakan tim FE/BE): jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC).
- State global dan pemulihan: penugasan Global Role Gita berubah (Manage asset ID configuration ON; Update Manage accounting tercentang) dan dipulihkan lewat seed API di hook `after`; entri log Assign dan Edit dari Admin B bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-169: Switch ke nilai yang sudah berlaku

1. Ketik Search `Gita Permata`, tekan Enter
2. Buka Detail Gita Permata > Tab Role > Sub-tab Global Role (Admin A)
3. Verifikasi switch Manage asset ID configuration OFF pada tampilan Admin A
4. Admin B (sesi API) menyalakan switch Manage asset ID configuration Gita Permata hingga tersimpan
5. Tunggu aksi selesai: permintaan sesi API Admin B selesai
6. Tunggu entri `Assign` dari Admin B muncul lewat kemampuan baca, lalu catat jumlah entri `Assign` Gita Permata di Tab Changelog sebagai baseline
7. Admin A klik switch Manage asset ID configuration pada tampilan basi
8. Verifikasi toast "Success, role has been updated."
9. Verifikasi switch Manage asset ID configuration ON (tampilan di-refresh ke state server)
10. Buka Tab Changelog Gita Permata, muat ulang sampai entri tampil
11. Verifikasi entri `Assign` dari Admin B tampil di Tab Changelog
12. Verifikasi jumlah entri `Assign` di Tab Changelog sama dengan baseline langkah 6 (tidak ada entri log baru)

### TC-FA-SU-170: Checkbox ke nilai yang sudah berlaku

13. Buka Tab Role > Sub-tab Global Role Gita Permata (Admin A)
14. Verifikasi checkbox Update baris Manage accounting tidak tercentang pada tampilan Admin A
15. Admin B (sesi API) mencentang Update Manage accounting Gita Permata hingga tersimpan
16. Tunggu aksi selesai: permintaan sesi API Admin B selesai
17. Tunggu entri `Edit` dari Admin B muncul lewat kemampuan baca, lalu catat jumlah entri `Edit` di Tab Changelog, Tab System Log aktor, dan Activity Log sebagai baseline
18. Admin A centang Update pada baris Manage accounting pada tampilan basi
19. Verifikasi toast "Success, permissions have been updated."
20. Buka Tab Changelog Gita Permata, muat ulang halaman
21. Verifikasi jumlah entri `Edit` di Tab Changelog sama dengan baseline langkah 17
22. Buka Tab System Log aktor
23. Verifikasi jumlah entri `Edit` di Tab System Log aktor sama dengan baseline langkah 17
24. Buka Activity Log
25. Verifikasi jumlah entri `Edit` di Activity Log sama dengan baseline langkah 17

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Pelaku kedua lewat sesi API (R-20): langkah 4 dan 15 hanya memicu perubahan state dan bukan objek asersi; tidak memakai `P-2` (keputusan 2026-10-30).
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 5 dan 16 (menunggu aksi pelaku kedua selesai, bagian 8b butir 8), langkah 6 dan 17 (menunggu entri Admin B tampil lalu mencatat baseline lewat kemampuan baca tanpa navigasi UI, NC-03), langkah 10, 13, 20, 22, dan 24 (membuka surface log atau sub-tab).
- Langkah penghubung Search (R-16, S-03; bagian 8b butir 9 dan 13): langkah 1 mencari baris target dengan nama persis sebelum aksi pada baris itu, tanpa `Verifikasi`; tabel User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman).
- Asersi tambahan di luar Expected TC: langkah 3 dan 14 (tampilan Admin A masih menunjukkan nilai lama) membuktikan tampilan basi; langkah 9 menerjemahkan "tampilan di-refresh ke state server" pada Expected b TC-FA-SU-169; langkah 11 adalah anchor positif bagi asersi jumlah langkah 12 (bagian 8b butir 2); toast langkah 19 menjadi anchor bagi asersi jumlah langkah 21, 23, dan 25.
- Temuan untuk QA:
  - Judul TC-FA-SU-169 menyebut "toast sukses aksi yang sama" sedangkan Expected a menulis "bukan toast no-op"; spec mengasersi toast "Success, role has been updated." sesuai Expected.
  - Expected b TC-FA-SU-169 ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Tab Changelog target. Expected b TC-FA-SU-170 menyebut "tiga permukaan log" dan diasersi pada ketiganya.
  - TC-FA-SU-170 Langkah Uji 4 ("Hitung entri `Edit`") tidak menyebut surface; spec menghitung pada Tab Changelog target, Tab System Log aktor, dan Activity Log sesuai Expected b.
  - Post Condition kedua TC ("tidak ada entri log tambahan dari sesi basi") diasersi lewat Expected b dan tidak diasersi terpisah.
