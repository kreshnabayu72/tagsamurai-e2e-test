---
id: TC-FA-GRP-E2E-022-role-matrix-positif-delete-manage-group-rd-dan-group-manager
title: "Role Matrix Positif Delete: Delete Node Kosong dan Bulk Delete Dua Node (R+D) serta Delete oleh Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-66
  - TC-FA-GRP-67
  - TC-FA-GRP-70
coverage:
  web: automated
---

# Role Matrix Positif Delete: Delete Node Kosong dan Bulk Delete Dua Node (R+D) serta Delete oleh Group Manager

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec ditulis per blok role karena langkah tiap role berbeda):

| Role | Akun (Pre-setup) | Password | Blok langkah |
|---|---|---|---|
| Manage Group R+D scope Region West (TC-FA-GRP-66, 67) | No 6 `manageGroupDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRD_PASSWORD` | langkah 1 sampai 12 |
| Group Manager scope Region West (TC-FA-GRP-70) | No 4 `groupManagerGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | langkah 13 sampai 20 |

- Login di hook `before` spec ini sebagai Manage Group R+D; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk kedua akun disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); hook suite hanya menyetel akun aktor default suite.
- Data Dinamis (di-seed di hook `before` lewat API sebagai anak langsung Region West, kosong dari aset dan user, dihapus oleh langkah spec; cleanup di hook `after` bila masih ada):

| TC | Nama TC | Nama seed |
|---|---|---|
| TC-FA-GRP-66 | West Temp | `West Temp {runId}-022` |
| TC-FA-GRP-67 | dua node kosong | `West Bulk A {runId}-022` dan `West Bulk B {runId}-022` |
| TC-FA-GRP-70 | West Temp 2 | `West Temp 2 {runId}-022` |

- Kemampuan teknis: fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Role Manage Group R+D (TC-FA-GRP-66)

1. Klik node Region West di sidebar
2. Klik (⋯) pada baris `West Temp {runId}-022`
3. Klik `Delete`
4. Klik [Delete] pada dialog konfirmasi
5. Verifikasi toast sukses `Success, group has been deleted.`
6. Verifikasi `West Temp {runId}-022` hilang dari tree sidebar dan dari tabel

### Role Manage Group R+D (TC-FA-GRP-67)

7. Centang baris `West Bulk A {runId}-022`
8. Centang baris `West Bulk B {runId}-022`
9. Klik `Delete` pada Bulk Action Bar
10. Klik [Delete] pada dialog konfirmasi
11. Verifikasi toast sukses `Success, group has been deleted.`
12. Verifikasi `West Bulk A {runId}-022` dan `West Bulk B {runId}-022` hilang dari tree sidebar dan dari tabel

### Role Group Manager (TC-FA-GRP-70)

13. Logout dari akun Manage Group R+D
14. Login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
15. Buka Fixed Asset > Settings > Groups
16. Klik node Region West di sidebar
17. Klik (⋯) pada baris `West Temp 2 {runId}-022`
18. Klik `Delete`
19. Klik [Delete] pada dialog konfirmasi
20. Verifikasi toast sukses `Success, group has been deleted.`

## Notes

- Spec 20 langkah, di bawah batas sekitar 35 langkah. Aksi hapus berada di akhir tiap blok (S-10).
- Langkah penghubung (S-03): langkah 1 dan 16 (memilih Region West agar baris target tampil), langkah 13 sampai 15 (ganti akun eksplisit).
- Absence baris pada langkah 6 dan 12 memakai toast sukses Delete sebagai anchor (8b butir 2).
- Pembagian TC lintas spec: Role Matrix positif Create ada di spec 020 dan Edit di spec 021; gating checkbox bulk di spec 023.
- Temuan untuk QA:
  - TC-FA-GRP-66, 67, 70 menyebut node `West Temp` dan `West Temp 2` serta dua node kosong tanpa nama; spec memakai node bersuffix milik spec.
  - TC-FA-GRP-67 tidak menyebut nama dua node; spec memakai `West Bulk A` dan `West Bulk B`.
