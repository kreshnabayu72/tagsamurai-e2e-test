---
id: TC-AC-RP-E2E-020-role-matrix-akses-menu-positif
title: "Role Matrix: Akses Menu Role & Permission per Entitas dan Role (Positif)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-76
  - TC-AC-RP-77
  - TC-AC-RP-78
  - TC-AC-RP-82
  - TC-AC-RP-83
coverage:
  web: automated
---

# Role Matrix: Akses Menu Role & Permission per Entitas dan Role (Positif)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, sisanya lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-76 | Total Control | Principal | Siti Nurhaliza | `totalControlRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_TC_PASSWORD` |
| TC-AC-RP-77 | Total Control | Distributor Nusantara | Gilang Ramadhan | `totalControlDistRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_DIST_TC_PASSWORD` |
| TC-AC-RP-78 | Default User | Partner Mandiri | Wulan Sari | `defaultUserPartRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_PART_DU_PASSWORD` |
| TC-AC-RP-82 | Read Only | Principal | Dewi Anggraini | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` |
| TC-AC-RP-83 | Global Role "Manage user and role" dengan Update (R+U) | Principal | Hendra Wijaya | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` |

- Login akun pertama (Siti Nurhaliza) dilakukan di hook `before` spec ini; halaman `Settings > Role & Permission` dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Kelima nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #1 sampai #5 dan #8, #9 (akun aktor di atas), #11 (data Principal), #13 (pemegang Total Control: 6 baris; Read Only: 2 baris), #14 (penugasan Group Manager: 3 baris), #19 (entitas `Distributor Nusantara` dan `Partner Mandiri`), #15 dan #17 (jumlah role Tab System: 10 Global Role dan 6 Group Role).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-020`, maupun cleanup.
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-76: Menu tampil untuk entitas Principal

1. Buka sidebar Settings
2. Verifikasi menu "Role & Permission" tampil di sidebar Settings
3. Klik menu "Role & Permission"
4. Verifikasi halaman terbuka dengan Tab Total Control aktif

### TC-AC-RP-77: Menu tampil untuk entitas Distributor

5. Ganti akun: logout, lalu login sebagai Total Control `Distributor Nusantara` `Gilang Ramadhan` (`Spectra.env.AC_RP_DIST_TC_PASSWORD`)
6. Buka sidebar Settings
7. Verifikasi menu "Role & Permission" tampil
8. Klik menu "Role & Permission"
9. Verifikasi halaman terbuka dengan keempat tab (Total Control, Read Only, Group Manager, System)

### TC-AC-RP-78: Menu tampil untuk entitas Partner

10. Ganti akun: logout, lalu login sebagai Default User `Partner Mandiri` `Wulan Sari` (`Spectra.env.AC_RP_PART_DU_PASSWORD`)
11. Buka sidebar Settings
12. Verifikasi menu "Role & Permission" tampil
13. Klik menu "Role & Permission"
14. Verifikasi halaman terbuka dengan keempat tab (Total Control, Read Only, Group Manager, System)

### TC-AC-RP-82: Aktor Read Only melihat seluruh tab dengan data penuh

15. Ganti akun: logout, lalu login sebagai Read Only `Dewi Anggraini` (`Spectra.env.AC_RP_RO_PASSWORD`)
16. Buka halaman `Settings > Role & Permission`
17. Verifikasi Tab Total Control dapat dibuka dan menampilkan 6 baris
18. Klik tab `Read Only`
19. Verifikasi Tab Read Only dapat dibuka dan menampilkan 2 baris
20. Klik tab `Group Manager`
21. Verifikasi Tab Group Manager dapat dibuka dan menampilkan 3 baris
22. Klik tab `System`
23. Verifikasi Tab System dapat dibuka dan menampilkan 10 Global Role dan 6 Group Role
24. Verifikasi data seluruh entitas tampil tanpa filter group

### TC-AC-RP-83: Aktor Manage user and role melihat seluruh tab entity-wide

25. Ganti akun: logout, lalu login sebagai Global Role "Manage user and role" dengan Update `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)
26. Buka halaman `Settings > Role & Permission`
27. Verifikasi Tab Total Control dapat dibuka
28. Klik tab `Read Only`
29. Verifikasi Tab Read Only dapat dibuka
30. Klik tab `Group Manager`
31. Verifikasi Tab Group Manager dapat dibuka
32. Klik tab `System`
33. Verifikasi Tab System dapat dibuka
34. Verifikasi data keempat tab entity-wide sama seperti data aktor Total Control (langkah 17, 19, 21, dan 23)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), dan langkah tiap role berbeda (menu entitas lain versus tab dan jumlah baris).
- Langkah penghubung (S-03): langkah 16 dan 26 (membuka halaman setelah ganti akun, sebelum asersi tab). Langkah 1 pada TC-AC-RP-76 tetap dituliskan walau hook `beforeEach` sudah membuka halaman, karena TC menguji menu sidebar.
- Spec negatif entitas Client, Group Manager, dan role tanpa Manage user and role (TC-AC-RP-79 sampai 81) ada di spec 021.
- Temuan untuk QA:
  - TC-AC-RP-77 dan 78 menulis Expected "keempat tab" tanpa menyebut nama tab; spec memakai nama tab dari TC-AC-RP-82 (Total Control, Read Only, Group Manager, System).
  - TC-AC-RP-83 Expected "data entity-wide yang sama seperti Total Control" tidak menyebut jumlah baris; spec membandingkan dengan hasil aktor Total Control pada TC-AC-RP-82 (langkah 34).
  - TC-AC-RP-82 Expected "Tab System 10 + 6 role" mengikuti Tabel Data Uji Pre-setup; Pre-setup #15 dan #17 tidak merinci daftar 10 Global Role dan 6 Group Role.
  - Email akun `Gilang Ramadhan` dan `Wulan Sari` berasal dari Pre-setup #8 dan #9; Post Condition TC-AC-RP-76 sampai 83 bernilai "-" sehingga tidak ada yang diasersi.
