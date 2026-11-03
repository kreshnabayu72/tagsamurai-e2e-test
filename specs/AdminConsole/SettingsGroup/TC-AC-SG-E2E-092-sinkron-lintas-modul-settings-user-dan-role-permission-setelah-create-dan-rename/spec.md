---
id: TC-AC-SG-E2E-092-sinkron-lintas-modul-settings-user-dan-role-permission-setelah-create-dan-rename
title: "Sinkron Lintas Modul: Group Baru dan Rename Terefleksi di Settings > User dan Role & Permission"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-341
  - TC-AC-SG-343
  - TC-AC-SG-348
coverage:
  web: automated
---

# Sinkron Lintas Modul: Group Baru dan Rename Terefleksi di Settings > User dan Role & Permission

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke Settings > User (Sidebar Group, Detail user > Tab Role > Group Role > Assign Group) dan Settings > Role & Permission (Detail Group Role) tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before`, dihapus hook `after`; setiap nama bersuffix `{runId}-092`): `Region C Asal {runId}-092` (level 1, tanpa entitas) untuk TC-AC-SG-343; `Region A Asal {runId}-092` (level 1, tanpa entitas) dengan Group Role `Manage partner` pada `Sari Dewi` (user Pre-setup #18) untuk TC-AC-SG-348. Pohon Uji Utama (Pre-setup #16) tidak diubah.
- Data yang dibuat langkah spec: `Region Lintas {runId}-092` (TC-AC-SG-341) dan hasil rename `Region C Lintas {runId}-092` dan `Region A Peran {runId}-092`. Hook `after` menghapus `Region Lintas {runId}-092` lewat Fixture BE; hasil rename ikut dihapus bersama data milik spec.
- User untuk membuka popup Select Group: `Yoga Pratama` (user Pre-setup #18, memiliki Group Role `Manage allocation`). Popup hanya dibuka dan ditutup tanpa menyimpan.
- Kemampuan teknis: Fixture BE (seeding group dan penugasan Group Role, pemulihan; disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-341: Group baru muncul di Sidebar Group dan popup Select Group pada Settings > User

1. Klik `[+] Group` di Sidebar Group Tree
2. Ketik `Region Lintas {runId}-092` lalu klik `[Submit]`
3. Tunggu aksi selesai (dialog/popup tertutup)
4. Buka Settings > User lewat sidebar
5. Verifikasi Sidebar Group User List memuat `Region Lintas {runId}-092`
6. Buka Detail user `Yoga Pratama` > Tab Role > Sub-tab Group Role
7. Klik `[Assign Group]` pada baris role `Manage allocation`
8. Klik `[+ Assign Group]`
9. Verifikasi popup Select Group memuat `Region Lintas {runId}-092`
10. Tutup popup Select Group dengan `✕`
11. Tutup popup Assign Group dengan `✕`

### TC-AC-SG-343: Rename group langsung terefleksi di Settings > User dan dropdown Select Group

12. Buka halaman Settings > Group lewat sidebar
13. Klik ikon `⋯` pada node `Region C Asal {runId}-092` di sidebar lalu `Edit`
14. Ubah nama menjadi `Region C Lintas {runId}-092` lalu klik `[Save]`
15. Tunggu aksi selesai (dialog/popup tertutup)
16. Buka Settings > User lewat sidebar
17. Verifikasi Sidebar Group User List memuat `Region C Lintas {runId}-092`
18. Verifikasi Sidebar Group User List tidak memuat `Region C Asal {runId}-092`
19. Buka Detail user `Yoga Pratama` > Tab Role > Sub-tab Group Role
20. Klik `[Assign Group]` pada baris role `Manage allocation`
21. Klik `[+ Assign Group]`
22. Verifikasi popup Select Group memuat `Region C Lintas {runId}-092`
23. Verifikasi popup Select Group tidak memuat `Region C Asal {runId}-092`
24. Tutup popup Select Group dengan `✕`
25. Tutup popup Assign Group dengan `✕`

### TC-AC-SG-348: Group Role Detail menampilkan nama group terbaru setelah rename

26. Buka halaman Settings > Group lewat sidebar
27. Klik ikon `⋯` pada node `Region A Asal {runId}-092` di sidebar lalu `Edit`
28. Ubah nama menjadi `Region A Peran {runId}-092` lalu klik `[Save]`
29. Tunggu aksi selesai (dialog/popup tertutup)
30. Buka Settings > Role & Permission > Detail Group Role `Manage partner`
31. Verifikasi baris penugasan `Sari Dewi` menampilkan group `Region A Peran {runId}-092`

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 3, 15, dan 29 (`Tunggu aksi selesai (dialog/popup tertutup)`, bagian 8b butir 8) menunggu popup Create atau Edit tertutup sebelum surface berganti; membuka kembali Settings > Group atau Settings > User lewat sidebar dan menutup popup Select Group dan Assign Group dengan `✕` (langkah 10, 11, 24, 25); popup hanya dibuka dan tidak diubah sehingga tidak ada dialog `Unsaved Changes`.
- "Live join, tanpa refresh data manual" pada TC-AC-SG-341 Expected tidak punya langkah sendiri: spec tidak menyisipkan langkah muat ulang data antara Create dan `Verifikasi` pada langkah 5 dan 9.
- Absence nama lama (langkah 18 dan 23) didahului `Verifikasi` nama baru pada surface yang sama (langkah 17 dan 22) sebagai anchor positif (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-AC-SG-342, 351, dan 352 ada di spec 117.
- TC-AC-SG-343 dan TC-AC-SG-348 menarget node Pre-setup `Region C` dan `Region A`; spec memakai node milik spec (S-06).
- Temuan untuk QA:
  - TC-AC-SG-341 dan TC-AC-SG-343 menyebut "Buka Detail user" atau "popup Select Group" tanpa menyebut user; spec memakai `Yoga Pratama` (Group Role `Manage allocation`, Pre-setup #18) dan tidak menyimpan penugasan.
  - TC-AC-SG-343 Expected menyebut "Sidebar Group dan popup Select Group" tanpa menyebut Settings > User tab mana yang memuat popup Select Group; spec memakai alur Detail user > Tab Role > Group Role > `[Assign Group]` > `[+ Assign Group]` seperti TC-AC-SG-341.
  - TC-AC-SG-348: Group Role `Manage partner` pada `Sari Dewi` di group Pre-setup `Region A` bergantung pada seed; spec men-seed penugasan itu pada `Region A Asal {runId}-092` lewat Fixture BE.
