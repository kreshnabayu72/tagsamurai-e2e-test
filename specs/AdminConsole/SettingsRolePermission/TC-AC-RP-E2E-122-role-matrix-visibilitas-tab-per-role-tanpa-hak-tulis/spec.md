---
id: TC-AC-RP-E2E-122-role-matrix-visibilitas-tab-per-role-tanpa-hak-tulis
title: "Role Matrix: Visibilitas Tab Total Control, Read Only, Group Manager untuk Role tanpa Hak Tulis"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-90
  - TC-AC-RP-93
  - TC-AC-RP-96
coverage:
  web: automated
---

# Role Matrix: Visibilitas Tab Total Control, Read Only, Group Manager untuk Role tanpa Hak Tulis

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, sisanya lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-90 | Read Only | Principal | Dewi Anggraini | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` |
| TC-AC-RP-93 | Global Role "Manage user and role" dengan Update (R+U) | Principal | Hendra Wijaya | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` |
| TC-AC-RP-96 | Global Role "Manage user and role" tanpa Update (Read saja) | Principal | Indra Kusuma | `manageUserRoleR_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_R_PASSWORD` |

- Login akun pertama (Dewi Anggraini) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Ketiga nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; `AC_RP_TC_PASSWORD` juga baru.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #3, #4, #5 (akun aktor), #11 (data Principal), #13 (baris target `John Doe` pada Tab Total Control, `Lisa Wong` pada Tab Read Only), #14 (baris target `Jane Smith` pada Tab Group Manager).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-122`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-90: Tab Total Control, Read Only, Group Manager untuk aktor Read Only

1. Verifikasi ikon Changelog dan Download tampil di Tab Total Control
2. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `John Doe` tidak tampil (Hidden) di Tab Total Control
3. Klik tab `Read Only`
4. Verifikasi ikon Changelog dan Download tampil di Tab Read Only
5. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `Lisa Wong` tidak tampil (Hidden) di Tab Read Only
6. Klik tab `Group Manager`
7. Verifikasi ikon Changelog dan Download tampil di Tab Group Manager
8. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `Jane Smith` tidak tampil (Hidden) di Tab Group Manager

### TC-AC-RP-93: Tab Total Control, Read Only, Group Manager untuk aktor Manage user and role (Update)

9. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" dengan Update `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)
10. Buka halaman `Settings > Role & Permission`
11. Verifikasi ikon Changelog dan Download tampil di Tab Total Control
12. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `John Doe` tidak tampil (Hidden) di Tab Total Control
13. Klik tab `Read Only`
14. Verifikasi ikon Changelog dan Download tampil di Tab Read Only
15. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `Lisa Wong` tidak tampil (Hidden) di Tab Read Only
16. Klik tab `Group Manager`
17. Verifikasi ikon Changelog dan Download tampil di Tab Group Manager
18. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `Jane Smith` tidak tampil (Hidden) di Tab Group Manager

### TC-AC-RP-96: Tab Total Control, Read Only, Group Manager untuk aktor Manage user and role tanpa Update

19. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" tanpa Update `Indra Kusuma` (`Spectra.env.AC_RP_MUR_R_PASSWORD`)
20. Buka halaman `Settings > Role & Permission`
21. Verifikasi ikon Changelog dan Download tampil di Tab Total Control
22. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `John Doe` tidak tampil (Hidden) di Tab Total Control
23. Klik tab `Read Only`
24. Verifikasi ikon Changelog dan Download tampil di Tab Read Only
25. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `Lisa Wong` tidak tampil (Hidden) di Tab Read Only
26. Klik tab `Group Manager`
27. Verifikasi ikon Changelog dan Download tampil di Tab Group Manager
28. Verifikasi tombol "+ Assign" dan aksi `Remove` pada kolom Actions baris `Jane Smith` tidak tampil (Hidden) di Tab Group Manager

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix visibilitas (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Role yang berhak menulis (TC-AC-RP-84 dan 87) ada di spec 022.
- Absence "+ Assign" dan `Remove` didahului `Verifikasi` ikon Changelog dan Download tampil pada tab yang sama sebagai anchor positif (bagian 8b butir 2). Langkah 2, 5, 8 dan seterusnya mengasersi daftar elemen yang sama-sama tidak ada dalam satu `Verifikasi` (S-01).
- Langkah penghubung (S-03): langkah 10 dan 20 (membuka halaman setelah ganti akun) serta klik tab `Read Only` dan `Group Manager`. TC menulis "Perhatikan ... overlay `⋯` baris `John Doe`"; karena Expected menyatakan kolom Actions tidak memuat `Remove`, spec tidak membuka overlay dan mengasersi ketiadaan `Remove` pada kolom Actions baris target.
- Temuan untuk QA:
  - TC-AC-RP-90, 93, 96 menyebut "overlay `⋯` baris `John Doe`" sedangkan Expected menyatakan kolom Actions tidak memuat aksi `Remove`; TC tidak menyatakan apakah tombol `⋯` tetap ada tanpa aksi lain. Spec hanya mengasersi ketiadaan `Remove` dan "+ Assign".
  - TC-AC-RP-90, 93, 96 mengulang langkah pada Tab Read Only dan Tab Group Manager dengan frasa "Ulangi"; spec menuliskan ulang langkahnya utuh (S-04).
  - Post Condition TC-AC-RP-90, 93, 96 bernilai "-" sehingga tidak ada yang diasersi.
