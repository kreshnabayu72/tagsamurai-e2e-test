---
id: TC-AC-RP-E2E-022-role-matrix-visibilitas-tab-per-role
title: "Role Matrix: Visibilitas Tab Total Control, Read Only, Group Manager untuk Default User dan Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-84
  - TC-AC-RP-87
coverage:
  web: automated
---

# Role Matrix: Visibilitas Tab Total Control, Read Only, Group Manager untuk Default User dan Total Control

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, aktor kedua lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-84 | Default User | Principal | Bambang Hartono | `defaultUserRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_DU_PASSWORD` |
| TC-AC-RP-87 | Total Control | Principal | Siti Nurhaliza | `totalControlRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_TC_PASSWORD` |

- Login akun pertama (Bambang Hartono) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Kedua nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #1 dan #2 (akun aktor), #11 (data Principal), #13 (baris target `John Doe` pada Tab Total Control, `Lisa Wong` pada Tab Read Only), #14 (baris target `Jane Smith` pada Tab Group Manager).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-022`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-84: Tab Total Control, Read Only, Group Manager untuk aktor Default User

1. Verifikasi tombol "+ Assign" tampil di Tab Total Control
2. Buka overlay `⋯` baris `John Doe`
3. Verifikasi aksi `Remove` tampil enabled pada baris `John Doe`
4. Tutup overlay `⋯` dengan Esc
5. Klik tab `Read Only`
6. Verifikasi tombol "+ Assign" tampil di Tab Read Only
7. Buka overlay `⋯` baris `Lisa Wong`
8. Verifikasi aksi `Remove` tampil enabled pada baris `Lisa Wong`
9. Tutup overlay `⋯` dengan Esc
10. Klik tab `Group Manager`
11. Verifikasi tombol "+ Assign" tampil di Tab Group Manager
12. Buka overlay `⋯` baris `Jane Smith`
13. Verifikasi aksi `Remove` tampil enabled pada baris `Jane Smith`
14. Tutup overlay `⋯` dengan Esc

### TC-AC-RP-87: Tab Total Control, Read Only, Group Manager untuk aktor Total Control

15. Ganti akun: logout, lalu login sebagai Total Control `Siti Nurhaliza` (`Spectra.env.AC_RP_TC_PASSWORD`)
16. Buka halaman `Settings > Role & Permission`
17. Verifikasi tombol "+ Assign" tampil di Tab Total Control
18. Buka overlay `⋯` baris `John Doe`
19. Verifikasi aksi `Remove` tampil enabled pada baris `John Doe`
20. Tutup overlay `⋯` dengan Esc
21. Klik tab `Read Only`
22. Verifikasi tombol "+ Assign" tampil di Tab Read Only
23. Buka overlay `⋯` baris `Lisa Wong`
24. Verifikasi aksi `Remove` tampil enabled pada baris `Lisa Wong`
25. Tutup overlay `⋯` dengan Esc
26. Klik tab `Group Manager`
27. Verifikasi tombol "+ Assign" tampil di Tab Group Manager
28. Buka overlay `⋯` baris `Jane Smith`
29. Verifikasi aksi `Remove` tampil enabled pada baris `Jane Smith`
30. Tutup overlay `⋯` dengan Esc

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix visibilitas (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Role yang tidak berhak menulis (TC-AC-RP-90, 93, 96) ada di spec 122.
- Langkah penghubung (S-03): langkah 4, 9, 14, 20, 25, 30 (menutup overlay `⋯` agar klik tab berikutnya tidak terhalang) dan langkah 16 (membuka halaman setelah ganti akun). Langkah 21 dan 26 serta 5 dan 10 membuka tab yang dibutuhkan asersi berikutnya (S-14).
- Temuan untuk QA:
  - TC-AC-RP-84 dan 87 menyebut "overlay `⋯` baris `John Doe`" tanpa menyatakan aksi yang diamati selain `Remove`; Expected "aksi `Remove` tampil enabled pada baris target lain" tidak menyebut tooltip, sehingga spec tidak mengasersi tooltip.
  - TC-AC-RP-84 dan 87 mengulang langkah pada Tab Read Only (`Lisa Wong`) dan Tab Group Manager (`Jane Smith`) dengan frasa "Ulangi"; spec menuliskan ulang langkahnya utuh (S-04).
  - Post Condition TC-AC-RP-84 dan 87 bernilai "-" sehingga tidak ada yang diasersi.
