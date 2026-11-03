---
id: TC-AC-RP-E2E-021-role-matrix-akses-menu-negatif
title: "Role Matrix: Akses Menu dan URL Langsung Ditolak 403 (Negatif)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-79
  - TC-AC-RP-80
  - TC-AC-RP-81
coverage:
  web: automated
---

# Role Matrix: Akses Menu dan URL Langsung Ditolak 403 (Negatif)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah state server.
- Role yang diuji (urutan eksekusi; aktor pertama login di hook `before` spec ini, sisanya lewat Step `Ganti akun`):

| TC | Role | Entitas | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-AC-RP-79 | Total Control | Client Sejahtera | Ayu Lestari | `totalControlClientRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_CLIENT_TC_PASSWORD` |
| TC-AC-RP-80 | Group Manager (tanpa Manage user and role) | Principal | Fajar Nugroho | `groupManagerRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_GM_PASSWORD` |
| TC-AC-RP-81 | Global Role "Manage language" saja | Principal | Rudi Hartono | `manageLanguageRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_LANG_PASSWORD` |

- Login akun pertama (Ayu Lestari) dilakukan di hook `before` spec ini. Akun ini (entitas Client) tidak memiliki akses halaman Role & Permission, sehingga halaman `Settings > Role & Permission` tidak dapat dibuka oleh hook `beforeEach` suite untuk spec ini dan spec dimulai dari landing Admin Console (lihat Temuan untuk QA). Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `Spectra.env.AC_RP_TC_PASSWORD`). Ketiga nama env password baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; `AC_RP_TC_PASSWORD` juga baru.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #10 (`Client Sejahtera`, akun `Ayu Lestari`), #6 (`Fajar Nugroho`, GM `Region Jawa` dan `Sumatera`), #7 (`Rudi Hartono`), #11 (data Principal).
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding, suffix `+{runId}-021`, maupun cleanup.
- URL halaman Role & Permission dibuka lewat akses URL langsung pada browser; nilai URL berasal dari aplikasi (tidak tertulis di TC).
- Flag Guided Tooltip halaman ini, pemulihan baseline, dan sesi API aktor mengikuti pernyataan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-79: Entitas Client tidak memiliki akses Role & Permission

1. Buka sidebar Settings
2. Verifikasi sedikitnya satu item menu lain pada sidebar Settings tampil
3. Verifikasi menu "Role & Permission" tidak tampil
4. Akses URL halaman Role & Permission secara langsung
5. Verifikasi akses ditolak `403`
6. Verifikasi toast error "You don't have permission to do this." tampil
7. Verifikasi tidak ada data Role & Permission yang tampil
8. Verifikasi tidak ada redirect dari URL yang diakses

### TC-AC-RP-80: Group Manager tanpa akses ke menu Role & Permission

9. Ganti akun: logout, lalu login sebagai Group Manager `Fajar Nugroho` (`Spectra.env.AC_RP_GM_PASSWORD`)
10. Buka sidebar Settings
11. Verifikasi sedikitnya satu item menu lain pada sidebar Settings tampil
12. Verifikasi menu "Role & Permission" tidak tampil
13. Akses URL halaman Role & Permission secara langsung
14. Verifikasi akses ditolak `403`
15. Verifikasi toast error "You don't have permission to do this." tampil
16. Verifikasi tidak ada redirect dari URL yang diakses

### TC-AC-RP-81: Role lain tanpa Manage user and role tidak memiliki akses

17. Ganti akun: logout, lalu login sebagai Global Role "Manage language" `Rudi Hartono` (`Spectra.env.AC_RP_LANG_PASSWORD`)
18. Buka sidebar Settings
19. Verifikasi sedikitnya satu item menu lain pada sidebar Settings tampil
20. Verifikasi menu "Role & Permission" tidak tampil
21. Akses URL halaman Role & Permission secara langsung
22. Verifikasi akses ditolak `403`
23. Verifikasi toast error "You don't have permission to do this." tampil
24. Verifikasi tidak ada redirect dari URL yang diakses

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix negatif (bagian 3a konvensi) yang ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah 2, 11, dan 19 adalah anchor absence item menu (bagian 8b butir 2): item menu lain pada sidebar Settings yang sama tampil sebelum absence menu "Role & Permission" diasersi. Langkah 7 (tanpa data Role & Permission) didahului toast `403` pada langkah 6 sebagai anchor bahwa respons server sudah diproses.
- TC-AC-RP-80 Expected "GM tidak memperoleh Manage user and role dari status GM-nya" adalah kesimpulan dari menu tidak tampil dan akses URL ditolak `403` (langkah 12 sampai 15) dan tidak teramati terpisah, sehingga tidak diasersi dengan langkah sendiri (S-03).
- TC-AC-RP-80 dan 81 tidak menulis klausa "tanpa data Role & Permission" pada Expected, sehingga langkah itu hanya ada pada blok TC-AC-RP-79.
- Temuan untuk QA:
  - Hook `beforeEach` suite membuka `Settings > Role & Permission`, yang tidak dapat dibuka akun entitas Client (aktor pertama spec ini); hook perlu mengecualikan spec 021, atau aktor pertama dipindah ke akun dengan akses.
  - TC-AC-RP-79 Precondition b berbunyi "User berada di Admin Console" sedangkan TC lain memakai "Settings > Role & Permission"; spec mengikuti TC.
  - Post Condition TC-AC-RP-79 sampai 81 bernilai "-" sehingga tidak ada yang diasersi.
