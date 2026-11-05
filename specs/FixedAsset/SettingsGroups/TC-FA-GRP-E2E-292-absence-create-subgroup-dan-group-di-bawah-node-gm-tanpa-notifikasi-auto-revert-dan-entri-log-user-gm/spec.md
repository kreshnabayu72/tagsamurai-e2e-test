---
id: TC-FA-GRP-E2E-292-absence-create-subgroup-dan-group-di-bawah-node-gm-tanpa-notifikasi-auto-revert-dan-entri-log-user-gm
title: "Absence Create Subgroup dan Group di Bawah Node GM: Tanpa Notifikasi In-App, Tanpa Entri Auto-Revert, Changelog Group Hanya Create, dan Tanpa Entri Log untuk User GM"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1293
  - TC-FA-GRP-1294
  - TC-FA-GRP-1296
coverage:
  web: automated
---

# Absence Create Subgroup dan Group di Bawah Node GM: Tanpa Notifikasi In-App, Tanpa Entri Auto-Revert, Changelog Group Hanya Create, dan Tanpa Entri Log untuk User GM

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (TC-FA-GRP-1294): gmPattern Pre-setup No 28 `gmPattern_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_GMPATTERN_PASSWORD` (nama env baru yang diusulkan, mengikuti pola `FA_GRP_*`; didaftarkan pemilik repo e2e, lihat Temuan untuk QA). Ganti akun eksplisit di langkah; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang diamati (hanya dibaca, tidak login): gmPatternNested Pre-setup No 29 dan gmPatternOther Pre-setup No 30, masing-masing `<nama>_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan No 21, di-seed lewat sesi API aktor di hook `before`, dihapus di hook `after`): `GM Pattern Parent {runId}-292` (Function None, level 1) > `GM Pattern Child {runId}-292` (Assignable) dan `GM Pattern Other {runId}-292` (Assignable, level 1). Penugasan Group Manager dan baris pola GM yang sudah terbentuk di-seed lewat API: gmPattern di Parent; gmPatternNested di Parent dan Child; gmPatternOther di Other. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (dihapus di hook `after` lewat API): `Abs GM Sub A {runId}-292` (di bawah Parent), `Abs GM Level One {runId}-292` (level 1), dan `Abs GM Sub B {runId}-292` (di bawah Child, dibuat oleh gmPattern).
- State client: Addon Audit tidak berlisensi (precondition TC-FA-GRP-1293, dipastikan fixture BE yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca log Role & Permission (Action dan jumlah entri per user dan per node), membaca Changelog: Group per node, membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11).

## Test Steps

### TC-FA-GRP-1293: Create Subgroup di bawah node penugasan GM (aktor Total Control)

1. Catat baseline sebelum pemicu: jumlah notifikasi in-app gmPattern dan jumlah entri `Auto-Revert` pada log Role & Permission gmPattern
2. Klik (⋯) pada node `GM Pattern Parent {runId}-292` di sidebar
3. Klik `Add Subgroup`
4. Isi Group Name `Abs GM Sub A {runId}-292`
5. Klik [Submit]
6. Verifikasi toast sukses `Success, group has been created.`
7. Baca log Role & Permission untuk `Abs GM Sub A {runId}-292`
8. Verifikasi log memuat entri `Assign` untuk baris pola GM gmPattern pada `Abs GM Sub A {runId}-292` (anchor: Create diproses dan log tercatat)
9. Tunggu 5 detik tanpa memuat ulang halaman
10. Verifikasi jumlah notifikasi in-app gmPattern sama dengan baseline langkah 1
11. Verifikasi jumlah entri `Auto-Revert` gmPattern sama dengan baseline langkah 1
12. Buka Changelog: Group untuk `Abs GM Sub A {runId}-292`
13. Verifikasi Changelog: Group memuat baris `Create` `Abs GM Sub A {runId}-292` (anchor)
14. Verifikasi Changelog: Group tidak memuat baris selain `Create` untuk `Abs GM Sub A {runId}-292`

### TC-FA-GRP-1296: Create Group level 1 tanpa entri log untuk user GM

15. Klik [+] Group
16. Isi Group Name `Abs GM Level One {runId}-292`
17. Klik [Submit]
18. Verifikasi toast sukses `Success, group has been created.`
19. Baca log Role & Permission untuk `Abs GM Level One {runId}-292`
20. Verifikasi log memuat entri `Assign` untuk baris pola Total Control/Read Only pada `Abs GM Level One {runId}-292` (anchor)
21. Verifikasi log tidak memuat entri untuk user gmPattern, gmPatternNested, dan gmPatternOther pada `Abs GM Level One {runId}-292`

### TC-FA-GRP-1294: Create Subgroup oleh gmPattern di descendant node penugasan

22. Tunggu aksi selesai
23. Ganti akun: Logout, lalu login sebagai gmPattern dengan `Spectra.env.FA_GRP_GMPATTERN_PASSWORD`
24. Buka Fixed Asset > Settings > Groups
25. Catat baseline sebelum pemicu: jumlah notifikasi in-app gmPattern
26. Klik (⋯) pada node `GM Pattern Child {runId}-292` di sidebar
27. Klik `Add Subgroup`
28. Isi Group Name `Abs GM Sub B {runId}-292`
29. Klik [Submit]
30. Verifikasi toast sukses `Success, group has been created.`
31. Baca log Role & Permission untuk `Abs GM Sub B {runId}-292`
32. Verifikasi log memuat entri `Assign` untuk baris pola GM gmPattern pada `Abs GM Sub B {runId}-292` (anchor)
33. Verifikasi log tidak memuat entri untuk gmPatternOther pada `Abs GM Sub B {runId}-292`
34. Tunggu 5 detik tanpa memuat ulang halaman
35. Verifikasi jumlah notifikasi in-app gmPattern sama dengan baseline langkah 25

## Notes

- Spec memiliki 35 langkah, pada batas 35 langkah. Tiga blok satu kelas (absence, kelas g) yang berdiri sendiri dengan node bersuffix sendiri; kegagalan satu blok tidak menghilangkan makna blok lain. Blok TC-1294 diletakkan terakhir karena butuh ganti akun (S-10).
- Langkah penghubung (S-03): langkah 7, 19, dan 31 (observasi lewat kemampuan baca), langkah 9 dan 34 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11), langkah 12 (membuka Changelog: Group), langkah 22 (tunggu aksi selesai sebelum ganti akun, 8b butir 8), dan langkah 23 dan 24 (ganti akun eksplisit dan membuka halaman Groups sesudah login, S-07 dan S-14).
- Pembagian TC lintas spec (S-05): TC-1293 (spec asal 290), TC-1294 (spec asal 291), dan TC-1296 (spec asal 298) muncul di `sourceTc` spec ini dan satu spec asal masing-masing. Spec ini memuat aksi nyata dengan baseline sendiri untuk asersi absence: tidak ada notifikasi in-app ke gmPattern dan tidak ada entri `Auto-Revert` serta Changelog: Group hanya baris `Create` (TC-1293 Expected c, d, f); tidak ada entri log untuk user GM pada Group level 1 (TC-1296 Expected d); tidak ada notifikasi in-app ke gmPattern dan tidak ada entri untuk gmPatternOther (TC-1294 Expected c, e). Presence (toast, baris pola, entri `Assign` per baris, Modified By) diasersi di spec asal.
- Temuan untuk QA:
  - Email Pre-setup No 28 sampai 30 belum punya nilai nyata (TC: perlu data tim FE/QA). Usulan env baru `FA_GRP_GMPATTERN_PASSWORD` untuk login gmPattern perlu didaftarkan pemilik repo e2e (di luar suite).
  - Notifikasi in-app dan log dibaca lewat kemampuan baca yang disediakan tim FE/BE; TC-1293 langkah 5 dan TC-1294 langkah 4 tidak menyebut cara membukanya.
  - TC-1294 langkah 3 dan 4 membaca Role & Permission, log, dan notifikasi oleh aktor Group Manager yang tidak jelas berhak membuka modul itu; spec memakai kemampuan baca.
  - TC-1293 Expected f ("Changelog: Group hanya memuat baris `Create`") tidak menyebut node yang dimaksud selain `GM Sub A`; spec membatasinya pada node baru.
  - Mekanisme seeding penugasan GM dan baris pola yang sudah terbentuk tidak ditegaskan di TC; ditulis sebagai kemampuan tim FE/BE tanpa endpoint karangan.
