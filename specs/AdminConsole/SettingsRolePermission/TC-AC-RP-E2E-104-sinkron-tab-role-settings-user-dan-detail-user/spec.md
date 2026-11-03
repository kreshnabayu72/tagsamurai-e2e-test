---
id: TC-AC-RP-E2E-104-sinkron-tab-role-settings-user-dan-detail-user
title: "Sinkronisasi ke Settings > User: Assign User to Role, Edit CRUD, Remove, dan Switch Global Role pada Tab Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-345
  - TC-AC-RP-346
  - TC-AC-RP-347
  - TC-AC-RP-348
coverage:
  web: automated
---

# Sinkronisasi ke Settings > User: Assign User to Role, Edit CRUD, Remove, dan Switch Global Role pada Tab Role

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (user Standard `Alex Tan`, `Jane Smith`), #15 (penugasan peran individual: `Manage device master data` John Dohan C/R/U, Jane Smith R, Hendra Wijaya R, Fajar Nugroho R, Maya Putri R; `Manage language` Rudi Hartono R), #16 sampai #18 sebagai data Principal pendukung, dan #26 (akses Settings > User > Detail User > Tab Role).
- Data Dinamis: spec ini tidak membuat entitas baru; target aksi adalah user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec (S-06), sehingga suffix `+{runId}-104` tidak dipakai.
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Kemampuan teknis: pembacaan nilai kolom Users baris `Manage device master data` pada Tab System (UI) untuk baseline (langkah 24); tidak ada endpoint yang dikarang.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_TC_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-345: Assign User to Role tersinkron ke Tab Role Settings > User

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
3. Klik `+ Assign`, centang `Alex Tan`, lalu klik `[Assign]`
4. Buka `Settings > User > Detail User` `Alex Tan` > Tab Role
5. Verifikasi switch Global Role `Manage language` ON
6. Verifikasi checkbox Read `Manage language` tercentang dan disabled
7. Verifikasi checkbox C, U, dan D `Manage language` tidak tercentang
8. Pulihkan baseline: `Alex Tan` kembali tanpa peran `Manage language`

### TC-AC-RP-347: Edit dari Tab Role Settings > User tersinkron ke Detail Role

9. Buka `Settings > User > Detail User` `Jane Smith` > Tab Role
10. Centang C pada `Manage device master data`
11. Buka halaman `Settings > Role & Permission`, klik tab `System`, lalu pada section Global Role klik `⋯` pada baris `Manage device master data` dan klik `Detail`
12. Verifikasi baris `Jane Smith` menampilkan C tercentang
13. Pulihkan baseline: C `Jane Smith` pada `Manage device master data` kembali tidak tercentang

### TC-AC-RP-346: Edit dan Remove dari Detail Role tersinkron ke Tab Role

14. Centang D baris `John Dohan`
15. Buka Tab Role `John Dohan` di Settings > User
16. Verifikasi Tab Role menampilkan D tercentang untuk `Manage device master data`
17. Buka kembali halaman `Settings > Role & Permission`, klik tab `System`, lalu pada section Global Role klik `⋯` pada baris `Manage device master data` dan klik `Detail`
18. Remove peran `John Dohan`: klik `⋯` baris `John Dohan`, klik `Remove`, lalu klik `[Remove]`
19. Buka kembali Tab Role `John Dohan` di Settings > User
20. Verifikasi switch `Manage device master data` OFF
21. Verifikasi konfigurasi CRUD `Manage device master data` terhapus
22. Pulihkan baseline: `John Dohan` kembali memegang `Manage device master data` dengan C, R, U

### TC-AC-RP-348: Switch Global Role OFF di Tab Role menyembunyikan baris dan tidak dihitung Users

23. Buka halaman `Settings > Role & Permission` lalu klik tab `System`
24. Catat nilai kolom Users baris `Manage device master data` pada section Global Role sebagai baseline
25. Matikan switch `Manage device master data` milik `John Dohan` di Settings > User > Tab Role
26. Buka halaman `Settings > Role & Permission` lalu klik tab `System`
27. Verifikasi nilai kolom Users baris `Manage device master data` berkurang 1 dari baseline langkah 24
28. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
29. Verifikasi baris `Jane Smith` tampil di Detail Role
30. Verifikasi baris `John Dohan` hilang dari Detail Role
31. Nyalakan kembali switch `Manage device master data` milik `John Dohan` di Settings > User > Tab Role
32. Verifikasi tidak ada popup yang tampil
33. Buka kembali Detail Role `Manage device master data` lewat `Settings > Role & Permission` > tab `System` > `⋯` > `Detail`
34. Verifikasi baris `John Dohan` muncul kembali dengan CRUD lama (C, R, U)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC-AC-RP-347 (Edit tanpa Remove) diletakkan sebelum TC-AC-RP-346 (Remove) dan TC-AC-RP-348 (mematikan switch) supaya aksi yang melepas peran `John Dohan` berada di belakang; TC-AC-RP-345 di awal karena menyentuh Global Role berbeda.
- Langkah penghubung (S-03, S-09): langkah 8, 13, dan 22 (pemulihan baseline); langkah 24 (baseline nilai Users, S-12).
- Pembanding absence (bagian 8b butir 2): baris `Jane Smith` pada Detail Role tampil sebelum asersi baris `John Dohan` hilang; Tab System dimuat sebelum nilai Users dibandingkan.
- `Verifikasi` tidak ada popup (langkah 32) ditulis tepat setelah pemicu menyalakan switch; pemicu menjadi anchor positif dan buktinya menyusul pada `Verifikasi` baris `John Dohan` muncul kembali (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-AC-RP-345 langkah 4 hanya menulis "Assign `Alex Tan`" tanpa menyebut tombol atau popup; spec memakai `+ Assign` dan `[Assign]` pada Role Detail sesuai label tombol yang dipakai TC Assign lain.
  - TC-AC-RP-346 Expected b "konfigurasi CRUD terhapus" tidak menyebut cara pengamatan; spec mengasersi di Tab Role.
  - TC-AC-RP-348 tidak menyebut baseline nilai Users; spec mencatat nilai kolom Users sebelum aksi dan mengasersi selisih satu (S-12).
  - Post Condition semua TC "Data dipulihkan automation baseline" tanpa langkah observasi tidak diasersi (S-01).
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
