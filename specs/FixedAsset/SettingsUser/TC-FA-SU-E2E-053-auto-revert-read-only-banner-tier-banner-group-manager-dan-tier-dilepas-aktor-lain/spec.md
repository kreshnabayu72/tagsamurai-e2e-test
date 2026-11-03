---
id: TC-FA-SU-E2E-053-auto-revert-read-only-banner-tier-banner-group-manager-dan-tier-dilepas-aktor-lain
title: "Auto-Revert Read Only, Banner Tier, Banner Group Manager, dan Tier Dilepas Aktor Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-176
  - TC-FA-SU-179
  - TC-FA-SU-180
  - TC-FA-SU-181
coverage:
  web: automated
---

# Auto-Revert Read Only, Banner Tier, Banner Group Manager, dan Tier Dilepas Aktor Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (langkah 30, Admin A TC-FA-SU-179): Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua (Admin B, Pre-setup #13): akun yang sama dengan sesi API aktor (lihat `suite.md`); hanya memicu perubahan state sehingga tidak memakai sesi UI kedua.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23; pohon grup #21): Lina Marlina (Total Control), Citra Lestari (Read Only), Gita Permata (tanpa tier), Oscar Pranata (Group Manager IT Infrastructure dan Accounts Payable), dan Ahmad Dahlan (Default User). Lina Marlina memiliki Manage accounting ON dengan Update tercentang (mengikuti TC-FA-SU-175); Citra Lestari memiliki Manage asset ID configuration OFF. Seed API memulihkan tier dan penugasan ini di hook `before` dan `after` (Catatan TC).
- Baseline log: hook `before` mencatat jumlah entri `Auto-Revert` Lina dan Citra di Tab Changelog target (kemampuan baca disediakan tim FE/BE; bagian 8b butir 10); langkah 36 mencatat ulang untuk TC-FA-SU-179. Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global dan pemulihan: tier Read Only Citra dilepas oleh blok TC-FA-SU-176, status Group Manager Oscar pada Accounts Payable dilepas oleh blok TC-FA-SU-181, dan tier Total Control Lina dilepas oleh Admin B pada blok TC-FA-SU-179; ketiganya dipulihkan lewat seed API di hook `after`. Entri `Auto-Revert` dan `Edit` bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-180: Banner tier di Sub-tab Global Role dan Group Role

1. Ketik Search `Lina`, tekan Enter di User List, klik nama Lina Marlina, lalu buka Tab Role > Sub-tab Global Role
2. Verifikasi banner `This user has Total Control access.` tampil di atas tabel Sub-tab Global Role
3. Verifikasi banner tanpa tombol aksi
4. Verifikasi tabel Sub-tab Global Role memuat baris role
5. Verifikasi tabel Sub-tab Global Role tidak menyisipkan baris `Total Control` atau `Read Only`
6. Klik Sub-tab Group Role
7. Verifikasi banner `This user has Total Control access.` tampil di atas tabel Sub-tab Group Role
8. Klik Sub-tab Transaction Role
9. Verifikasi tabel Sub-tab Transaction Role tampil
10. Verifikasi banner tidak tampil di Sub-tab Transaction Role
11. Kembali ke User List, ketik Search `Citra`, tekan Enter, klik nama Citra Lestari, lalu buka Tab Role > Sub-tab Global Role
12. Verifikasi banner `This user has Read Only access.` tampil di atas tabel Sub-tab Global Role
13. Klik Sub-tab Group Role
14. Verifikasi banner `This user has Read Only access.` tampil di atas tabel Sub-tab Group Role
15. Kembali ke User List, ketik Search `Gita`, tekan Enter, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
16. Verifikasi tabel Sub-tab Global Role Gita Permata memuat baris role
17. Verifikasi tidak ada banner tier atau Group Manager di Sub-tab Global Role Gita Permata

### TC-FA-SU-181: Banner Group Manager

18. Kembali ke User List, ketik Search `Oscar`, tekan Enter, klik nama Oscar Pranata, lalu buka Tab Role > Sub-tab Group Role
19. Verifikasi banner `This user is a Group Manager for: Accounts Payable, IT Infrastructure.` tampil dengan grup berurut A-Z
20. Lepas status Group Manager Oscar Pranata pada grup Accounts Payable lewat edit Group Role
21. Verifikasi banner menampilkan sisa grup kelolaan saja: `This user is a Group Manager for: IT Infrastructure.`

### TC-FA-SU-176: Auto-Revert Read Only

22. Kembali ke User List, ketik Search `Citra`, tekan Enter, klik nama Citra Lestari, lalu buka Tab Role > Sub-tab Global Role
23. Nyalakan switch pada baris Manage asset ID configuration
24. Verifikasi dialog Title `Remove Read Only` dengan Body bullet `• Citra Lestari`, kalimat `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`
25. Klik `[Remove]`
26. Verifikasi toast "Success, permissions have been updated. Citra Lestari is no longer Read Only."
27. Verifikasi banner `This user has Read Only access.` hilang dari Sub-tab Global Role
28. Buka Tab Changelog Citra Lestari, muat ulang sampai entri tampil
29. Verifikasi entri `Auto-Revert` / Object `Read Only` / Field `Access Level` / Old Value `Read Only` / New Value `—` tercatat satu kali (selisih 1 dari baseline)

### TC-FA-SU-179: Tier sudah dilepas aktor lain sebelum konfirmasi

30. Ganti akun: logout, login sebagai Default User Ahmad Dahlan (`Spectra.env.FA_DU_PASSWORD`), lalu buka Fixed Asset > Settings > User
31. Buka Detail Lina Marlina > Tab Role > Sub-tab Global Role (Admin A)
32. Hapus centang Update pada baris Manage accounting
33. Verifikasi dialog Title `Remove Total Control` tampil
34. Admin B (sesi API) melepas tier Total Control Lina Marlina lewat Settings > Role & Permission hingga tersimpan
35. Tunggu aksi selesai: permintaan sesi API Admin B selesai
36. Baca jumlah entri `Auto-Revert` Lina Marlina di Tab Changelog lewat kemampuan baca log tanpa menutup dialog Admin A, ulangi tiap 5 detik sampai entri `Auto-Revert` dari Admin B tampil, lalu catat baseline (termasuk entri dari Admin B)
37. Admin A klik `[Remove]`
38. Verifikasi checkbox Update baris Manage accounting tidak tercentang setelah tab di-refresh ke state server (edit Admin A tetap diterapkan)
39. Buka Tab Changelog Lina Marlina, muat ulang sampai entri tampil
40. Verifikasi entri `Edit` dari Admin A tampil di Tab Changelog Lina Marlina
41. Verifikasi jumlah entri `Auto-Revert` Lina Marlina di Tab Changelog sama dengan baseline langkah 36 (hanya satu entri dari Admin B, tidak ada entri kedua)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Urutan: TC-FA-SU-180 (screening banner) mendahului TC-FA-SU-176 yang melepas tier Read Only Citra; TC-FA-SU-181 mendahului TC-FA-SU-176 dan 179; TC-FA-SU-179 terakhir karena membutuhkan ganti akun ke Default User.
- Pelaku kedua lewat sesi API (R-20): langkah 34 hanya memicu perubahan state dan bukan objek asersi; tidak memakai `P-2` (keputusan 2026-10-30).
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 11, 15, 18, dan 22 (Search untuk menemukan baris target, R-16), langkah 6, 8, 13, 28, dan 39 (membuka sub-tab atau surface log), langkah 30 (ganti akun eksplisit, S-07), langkah 35 (menunggu aksi pelaku kedua selesai, bagian 8b butir 8), langkah 36 (mencatat baseline hanya sesudah entri eventual dari Admin B tampil, NC-03; dibaca lewat kemampuan baca log supaya dialog Admin A tetap terbuka).
- Asersi tambahan di luar Expected TC: langkah 4, 9, 16, dan 40 adalah anchor positif bagi asersi absence di langkah sesudahnya (bagian 8b butir 2); langkah 21 menjadi pembuktian Expected b TC-FA-SU-181 ("sisa grup kelolaan saja").
- Spec ini 41 langkah. Alasan melewati sekitar 35 langkah: keempat blok satu topik (Auto-Revert dan banner tier pada Sub-tab Role Detail User); blok screening dan blok aksi berdiri sendiri karena tier dan Group Manager dipulihkan lewat seed API sebelum blok berikutnya.
- Temuan untuk QA:
  - Expected c TC-FA-SU-181 ("banner Group Manager dapat tampil bersama banner tier lain") tidak punya data uji: Pre-setup #9 hanya memuat Group Manager tanpa tier; tidak diasersi.
  - TC-FA-SU-181 Langkah Uji 2 ("lepas status Group Manager lewat edit Group Role") tidak merinci jalur UI; spec menulis satu langkah dan menandainya sebagai kemampuan edit Group Role yang diuji di spec lain.
  - Post Condition TC-FA-SU-176 (peran individual, notifikasi in-app) dan TC-FA-SU-179 (tier dilepas aktor lain) tidak punya langkah observasi tersendiri dan tidak diasersi di luar Expected (S-01).
  - Expected c TC-FA-SU-176 menyebut entri `Auto-Revert` tercatat tanpa menyebut surface; spec memakai Tab Changelog target sesuai Langkah Uji 4.
