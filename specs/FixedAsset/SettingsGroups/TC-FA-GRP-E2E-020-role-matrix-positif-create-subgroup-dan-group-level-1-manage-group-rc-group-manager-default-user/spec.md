---
id: TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user
title: "Role Matrix Positif Create: Add Subgroup oleh Manage Group R+C dan Group Manager, [+] Group oleh Default User, Auto-Assign Creator"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-64
  - TC-FA-GRP-68
  - TC-FA-GRP-72
  - TC-FA-GRP-132
  - TC-FA-GRP-890
coverage:
  web: automated
---

# Role Matrix Positif Create: Add Subgroup oleh Manage Group R+C dan Group Manager, [+] Group oleh Default User, Auto-Assign Creator

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec ditulis per blok role karena langkah tiap role berbeda):

| Role | Akun (Pre-setup) | Password | Blok langkah |
|---|---|---|---|
| Manage Group R+C scope Region West (TC-FA-GRP-64, 132, 890) | No 6 `manageGroupCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRC_PASSWORD` | langkah 1 sampai 29 |
| Group Manager scope Region West (TC-FA-GRP-68) | No 4 `groupManagerGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | langkah 30 sampai 39 |
| Default User (TC-FA-GRP-72) | No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` | langkah 40 sampai 47 |

- Login di hook `before` spec ini sebagai Manage Group R+C; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk ketiga akun disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); hook suite hanya menyetel akun aktor default suite.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9): Global HQ > Region West > Branch West 1 > Room 301.
- Data Dinamis (dibuat oleh langkah spec, dihapus di hook `after` lewat API):

| TC | Nama TC | Nama dibuat | Induk |
|---|---|---|---|
| TC-FA-GRP-64 | West Annex | `West Annex {runId}-020` | Region West |
| TC-FA-GRP-132 | West Lab | `West Lab {runId}-020` | Region West |
| TC-FA-GRP-890 | West Log | `West Log {runId}-020` | Region West |
| TC-FA-GRP-68 | node baru di bawah Room 301 (nama tidak disebut TC) | `Room Child {runId}-020` | Room 301 |
| TC-FA-GRP-72 | DU Root | `DU Root {runId}-020` | level 1 |

- Kemampuan teknis: fixture BE (membaca assignment Manage Group aktor, menghapus data milik spec), kemampuan membaca assignment dan log modul Role & Permission, dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Role Manage Group R+C (TC-FA-GRP-64)

1. Klik (⋯) pada node Region West di sidebar
2. Klik `Add Subgroup`
3. Isi Group Name `West Annex {runId}-020`
4. Klik [Submit]
5. Verifikasi toast sukses `Success, group has been created.`
6. Klik chevron node Region West untuk expand
7. Verifikasi `West Annex {runId}-020` muncul di bawah Region West
8. Verifikasi aktor mendapat auto-assign Manage Group CRUD di `West Annex {runId}-020` sesuai pembacaan fixture BE

### Role Manage Group R+C (TC-FA-GRP-132)

9. Klik (⋯) pada node Region West di sidebar
10. Klik `Add Subgroup`
11. Isi Group Name `West Lab {runId}-020`
12. Klik [Submit]
13. Verifikasi toast sukses `Success, group has been created.`
14. Klik (⋯) pada node `West Lab {runId}-020` di sidebar
15. Verifikasi menu memuat Detail, Add Subgroup, Edit, Delete (CRUD penuh walau di parent hanya R+C)
16. Tutup menu dengan Esc
17. Baca assignment Manage Group aktor pada `West Lab {runId}-020` lewat kemampuan baca modul Role & Permission
18. Verifikasi assignment Manage Group C/R/U/D aktor di `West Lab {runId}-020` tercatat

### Role Manage Group R+C (TC-FA-GRP-890)

19. Klik (⋯) pada node Region West di sidebar
20. Klik `Add Subgroup`
21. Isi Group Name `West Log {runId}-020`
22. Klik [Submit]
23. Tunggu aksi selesai (modal Add Subgroup tertutup)
24. Baca log modul Role & Permission lewat kemampuan baca log
25. Verifikasi Role & Permission mencatat assignment Manage Group aktor ke `West Log {runId}-020`
26. Klik ikon `Changelog`
27. Ketik Search `West Log {runId}-020`, tekan Enter
28. Verifikasi Changelog: Group hanya memuat satu baris untuk `West Log {runId}-020`, yaitu baris Create
29. Tutup Modal Changelog dengan ✕

### Role Group Manager (TC-FA-GRP-68)

30. Logout dari akun Manage Group R+C
31. Login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
32. Buka Fixed Asset > Settings > Groups
33. Klik toggle expand-all pada sidebar
34. Klik (⋯) pada node Room 301 di sidebar
35. Klik `Add Subgroup`
36. Isi Group Name `Room Child {runId}-020`
37. Klik [Submit]
38. Verifikasi toast sukses `Success, group has been created.`
39. Verifikasi `Room Child {runId}-020` muncul sebagai node baru di bawah Room 301 pada sidebar

### Role Default User (TC-FA-GRP-72)

40. Logout dari akun Group Manager
41. Login sebagai Default User dengan `Spectra.env.FA_DU_PASSWORD`
42. Buka Fixed Asset > Settings > Groups
43. Klik [+] Group
44. Isi Group Name `DU Root {runId}-020`
45. Klik [Submit]
46. Verifikasi toast sukses `Success, group has been created.`
47. Verifikasi aktor tidak mendapat auto-assign creator pada `DU Root {runId}-020` sesuai pembacaan fixture BE (node `DU Root {runId}-020` tampil di sidebar)

## Notes

- Spec melewati sekitar 35 langkah (47 langkah): seluruh blok adalah satu kelas (Role Matrix positif Create) pada dataset Region West yang sama, tiap blok berdiri sendiri (satu role per blok, data dibuat dan dihapus sendiri), dan memisahkannya hanya menggandakan login, hook, dan cleanup.
- Spec ditulis per blok role karena langkah tiap role berbeda (aksi dan target berbeda) dan ganti akun menuntut langkah eksplisit (bagian 3a).
- Langkah penghubung (S-03): langkah 6 (expand Region West), langkah 16 (menutup menu), langkah 23 (tunggu aksi selesai, 8b butir 8), langkah 27 (Search di Modal Changelog untuk menemukan baris target, R-16), langkah 29 (menutup modal), langkah 30 sampai 32 dan 40 sampai 42 (ganti akun eksplisit), langkah 33 (expand-all).
- Pembagian TC lintas spec: Role Matrix positif Edit ada di spec 021, Delete di spec 022.
- Temuan untuk QA:
  - TC-FA-GRP-132 dan 890 meminta pembacaan Settings > Role & Permission oleh aktor R+C yang tidak jelas berhak mengakses modul itu; spec memakai kemampuan baca assignment dan log yang disediakan tim FE/BE.
  - Post Condition TC-FA-GRP-132 ("Total User West Lab mencakup aktor") tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-FA-GRP-68 tidak menyebut nama node baru dan TC-FA-GRP-72 tidak menyebut cara cek "tanpa auto-assign creator"; spec memakai nama bersuffix dan pembacaan fixture BE.
