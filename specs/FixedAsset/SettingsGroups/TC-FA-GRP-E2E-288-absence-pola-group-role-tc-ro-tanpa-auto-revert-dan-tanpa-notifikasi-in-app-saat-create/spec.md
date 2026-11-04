---
id: TC-FA-GRP-E2E-288-absence-pola-group-role-tc-ro-tanpa-auto-revert-dan-tanpa-notifikasi-in-app-saat-create
title: "Absence Pola Group Role TC/RO: Tanpa Entri Auto-Revert saat Create Group Level 1 dan Subgroup, serta Tanpa Notifikasi In-App ke User Total Control/Read Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1289
  - TC-FA-GRP-1291
coverage:
  web: automated
---

# Absence Pola Group Role TC/RO: Tanpa Entri Auto-Revert saat Create Group Level 1 dan Subgroup, serta Tanpa Notifikasi In-App ke User Total Control/Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (Create Subgroup TC-FA-GRP-1291): Manage Group R+C scope Region West, Pre-setup No 6 `manageGroupCreate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MGRC_PASSWORD`. Ganti akun eksplisit di langkah; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Penerima yang diamati (user Total Control dan Read Only): Default User No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net`, Read Only No 3 `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`, user Total Control dengan Home Group constraint `Fixture.groupsPola.tcHome.email`, dan user Read Only dengan Home Group constraint `Fixture.groupsPola.roHome.email` (di-seed lewat API di hook `before` bersama Home Group `Home Luar {runId}-288` di luar node baru, dihapus di hook `after`). Email kedua user fixture tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Data Dinamis (dibuat oleh langkah spec, dihapus di hook `after` lewat API): `Absen Baru {runId}-288` (level 1), `Absen Baru Sub {runId}-288` (di bawah `Absen Baru {runId}-288`), `Absen Home {runId}-288` (level 1), dan `West Absen Home {runId}-288` (di bawah Region West).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role (Settings > Role & Permission) per node, membaca jumlah entri `Auto-Revert` dan entri `Assign` pada log Role & Permission per user dan per node, membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11).

## Test Steps

### TC-FA-GRP-1289: Create Group level 1 dan Subgroup tidak memicu Auto-Revert

1. Catat baseline sebelum pemicu: jumlah entri `Auto-Revert` pada log Role & Permission untuk tiap penerima (Default User, Read Only, user Total Control Home Group, user Read Only Home Group)
2. Klik [+] Group
3. Isi Group Name `Absen Baru {runId}-288`
4. Klik [Submit]
5. Verifikasi toast sukses `Success, group has been created.` untuk Create Group level 1
6. Klik (⋯) pada node `Absen Baru {runId}-288` di sidebar
7. Klik `Add Subgroup`
8. Isi Group Name `Absen Baru Sub {runId}-288`
9. Klik [Submit]
10. Verifikasi toast sukses `Success, group has been created.` untuk Create Subgroup
11. Baca tab Group Role pada `Absen Baru {runId}-288` dan `Absen Baru Sub {runId}-288` lewat kemampuan baca modul Role & Permission
12. Verifikasi pada kedua node, baris pola Group Role user Total Control dan Read Only tampil (anchor: Create diproses dan baris pola terbentuk)
13. Verifikasi jumlah entri `Auto-Revert` untuk keempat penerima sama dengan baseline langkah 1

### TC-FA-GRP-1291: Create dengan Home Group constraint tidak memicu Auto-Revert dan tanpa notifikasi in-app

14. Catat baseline sebelum pemicu: jumlah entri `Auto-Revert` pada log Role & Permission dan jumlah notifikasi in-app untuk tiap penerima (Default User, Read Only, user Total Control Home Group, user Read Only Home Group)
15. Klik [+] Group
16. Isi Group Name `Absen Home {runId}-288`
17. Klik [Submit]
18. Verifikasi toast sukses `Success, group has been created.` untuk Create Group level 1
19. Tunggu aksi selesai
20. Ganti akun: Logout, lalu login sebagai Manage Group R+C dengan `Spectra.env.FA_MGRC_PASSWORD`
21. Buka Fixed Asset > Settings > Groups
22. Klik (⋯) pada node Region West di sidebar
23. Klik `Add Subgroup`
24. Isi Group Name `West Absen Home {runId}-288`
25. Klik [Submit]
26. Verifikasi toast sukses `Success, group has been created.` untuk Create Subgroup
27. Baca log Role & Permission untuk `Absen Home {runId}-288` dan `West Absen Home {runId}-288`
28. Verifikasi log memuat entri `Assign` untuk baris pola Group Role pada kedua node (anchor: Create diproses dan log tercatat)
29. Tunggu 5 detik tanpa memuat ulang halaman
30. Verifikasi jumlah notifikasi in-app tiap penerima sama dengan baseline langkah 14
31. Verifikasi jumlah entri `Auto-Revert` untuk keempat penerima sama dengan baseline langkah 14

## Notes

- Langkah penghubung (S-03): langkah 11 dan 27 (observasi lewat kemampuan baca), langkah 19 (tunggu aksi selesai sebelum ganti akun, 8b butir 8), langkah 20 dan 21 (ganti akun eksplisit dan membuka halaman Groups sesudah login, S-07 dan S-14), dan langkah 29 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11).
- Pembagian TC lintas spec: TC-1289 dan TC-1291 muncul di `sourceTc` spec ini dan spec 285 (spec asal, S-05). Spec ini memuat aksi nyata (Create Group level 1, Subgroup, dan Subgroup oleh Manage Group R+C) dengan baseline sendiri untuk asersi absence: tidak ada entri `Auto-Revert` (TC-1289 Expected c; TC-1291 Expected b "bukan entri Auto-Revert") dan tidak ada notifikasi in-app (TC-1291 Expected c). Presence (toast, baris pola, entri `Assign`, Modified By, tier tidak terlepas) diasersi di spec 285.
- Temuan untuk QA:
  - Email user Total Control dan Read Only dengan Home Group constraint tidak ada di Pre-setup TC; spec memakai fixture baru yang ditetapkan tim FE.
  - TC-1289 Expected c "tidak ada auto-revert" tidak menyebut cara membaca selain log; tier user diasersi lewat log Role & Permission (selisih entri `Auto-Revert`) di spec ini dan lewat pembacaan tier di spec 285.
  - Notifikasi in-app tiap penerima dibaca lewat kemampuan baca yang disediakan tim FE/BE; TC-1291 langkah 4 menyebut "notifikasi in-app user TC/RO" tanpa cara membukanya.
  - TC-1291 langkah 3 dan 4 membaca Role & Permission, log, dan notifikasi oleh aktor Manage Group R+C yang tidak jelas berhak membuka modul itu; spec memakai kemampuan baca.
