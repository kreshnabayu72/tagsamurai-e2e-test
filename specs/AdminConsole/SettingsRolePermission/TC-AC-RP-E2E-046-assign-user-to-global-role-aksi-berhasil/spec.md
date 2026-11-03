---
id: TC-AC-RP-E2E-046-assign-user-to-global-role-aksi-berhasil
title: "Assign User to Global Role: Total Control, Manage user and role, dan Manage TAG stock Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-163
  - TC-AC-RP-164
  - TC-AC-RP-431
coverage:
  web: automated
---

# Assign User to Global Role: Total Control, Manage user and role, dan Manage TAG stock Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Ganti akun di tengah spec ke Manage user and role (Update) `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #4), password `Spectra.env.AC_RP_MUR_U_PASSWORD` (langkah 9); lalu ke Total Control `Distributor Nusantara` `totalControlDistRP_automated_{namaCompany}@qwertysystem.net` (`Gilang Ramadhan`, Pre-setup #8), password `Spectra.env.AC_RP_DIST_TC_PASSWORD` (langkah 18).
- Data Pre-setup: #11, #12 (`Alex Tan` dan `Sarah Kimura`, user Standard yang belum memegang `Manage language`), #19 (`Distributor Nusantara` dengan user Standard `Bayu Santoso` yang belum memegang peran apa pun).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Pemulihan baseline: data Pre-setup yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dicatat dan tidak dipulihkan.
- Kemampuan teknis: kemampuan baca state BE atas nilai tersimpan assignment `Bayu Santoso` pada `Manage TAG stock` (Expected TC-AC-RP-431 butir c menyebut respons API) disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD sehingga tidak ditulis.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e. Sama untuk `AC_RP_MUR_U_PASSWORD` dan `AC_RP_DIST_TC_PASSWORD`.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

### TC-AC-RP-163: Assign User ke Global Role happy path

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
3. Klik "+ Assign"
4. Centang `Alex Tan` lalu klik `[Assign]`
5. Verifikasi toast "Success, role has been assigned."
6. Verifikasi baris `Alex Tan` muncul dengan R checked + disabled
7. Verifikasi C, U, dan D baris `Alex Tan` tidak tercentang
8. Pulihkan baseline: lepas `Alex Tan` dari `Manage language` lewat kemampuan reset FE/BE

### TC-AC-RP-164: Assign User ke Global Role oleh Manage user and role

9. Ganti akun: Logout, lalu login sebagai `Hendra Wijaya` (`manageUserRoleU_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_MUR_U_PASSWORD`)
10. Klik menu `Settings > Role & Permission` di sidebar
11. Klik tab `System`
12. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
13. Klik "+ Assign"
14. Centang `Sarah Kimura` lalu klik `[Assign]`
15. Verifikasi toast "Success, role has been assigned."
16. Verifikasi baris `Sarah Kimura` muncul dengan R checked + disabled
17. Pulihkan baseline: lepas `Sarah Kimura` dari `Manage language` lewat kemampuan reset FE/BE

### TC-AC-RP-431: Assign user ke Manage TAG stock pada entitas Distributor

18. Ganti akun: Logout, lalu login sebagai `Gilang Ramadhan` (`totalControlDistRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_DIST_TC_PASSWORD`)
19. Klik menu `Settings > Role & Permission` di sidebar
20. Klik tab `System`
21. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
22. Klik "+ Assign"
23. Centang `Bayu Santoso` lalu klik `[Assign]`
24. Verifikasi toast sukses "Success, role has been assigned."
25. Verifikasi baris `Bayu Santoso` tampil dengan Name, Position, dan Division
26. Verifikasi tidak ada kolom C/R/U/D pada tabel
27. Baca nilai tersimpan assignment `Bayu Santoso` pada `Manage TAG stock` lewat kemampuan baca state BE
28. Verifikasi nilai tersimpan: Read aktif, C/U/D tidak aktif
29. Pulihkan baseline: lepas `Bayu Santoso` dari `Manage TAG stock` lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 8, 17, 29 (pemulihan baseline antar blok TC), langkah 9 dan 18 (ganti akun eksplisit, S-07), serta klik sidebar sesudah ganti akun (membuka halaman bersih), dan langkah 27 (observasi untuk Expected butir c).
- Tiga TC dipisah per aktor sehingga tiap blok memakai akun dan data milik TC itu.
- Temuan untuk QA:
  - TC-AC-RP-431 Expected c menyebut "respons API" tetapi TC tidak memberi cara observasi di FE; spec memakainya sebagai pembacaan state BE yang disediakan tim FE/BE tanpa mengarang endpoint (S-11, S-13).
  - TC-AC-RP-431 langkah 3 tidak menyebut `Detail` sebagai tampilan halaman Role Detail (berbeda dari TC lain yang menyebut halaman Role Detail tampil); spec menganggap Role Detail `Manage TAG stock` terbuka.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
