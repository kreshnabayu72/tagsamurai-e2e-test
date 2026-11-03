---
id: TC-AC-RP-E2E-045-assign-user-to-role-screening-dan-pool
title: "Assign User to Role: Screening Popup Global Role dan Pool Kandidat per Aktor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-160
  - TC-AC-RP-161
  - TC-AC-RP-162
  - TC-AC-RP-412
coverage:
  web: automated
---

# Assign User to Role: Screening Popup Global Role dan Pool Kandidat per Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Ganti akun di tengah spec ke Manage user and role (Update) `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hendra Wijaya`, Pre-setup #4), password dari `Spectra.env.AC_RP_MUR_U_PASSWORD`, pada langkah 12.
- Data Pre-setup: #11 (tree group `Default Group`, `Region A`, `Branch 1`, `Region Jawa`, `Jakarta`, `Surabaya`, `Sumatera`), #12 (user Standard: `Teguh Santoso` Inactive, `Maya Putri` Pending Activation, `John Dohan`), #13 (pemegang Total Control dan Read Only), #14 (GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera`), #15 (`Rudi Hartono` memegang `Manage language`; `John Dohan` memegang `Manage distributor` di `Region A` dan `Branch 1`).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Spec ini tidak menyimpan perubahan data (semua popup ditutup tanpa Assign). Pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e. Sama untuk `AC_RP_MUR_U_PASSWORD`.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.

## Test Steps

### TC-AC-RP-160: Screening popup Assign User Global Role

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
3. Klik "+ Assign"
4. Verifikasi header popup "Assign User — Manage language"
5. Verifikasi Table User Picker tampil tanpa field Group
6. Verifikasi footer popup memuat `[Cancel]` dan `[Assign]`

### TC-AC-RP-161: Pool Assign User Global Role untuk aktor Total Control

7. Telusuri seluruh halaman Pagination popup dan amati seluruh baris kandidat
8. Verifikasi kandidat memuat user Standard berstatus Active, Pending Activation, dan Inactive `Teguh Santoso` yang belum memegang `Manage language`
9. Verifikasi kandidat memuat `Fajar Nugroho` (Group Manager)
10. Verifikasi kandidat tidak memuat pemegang role ini (`Rudi Hartono`, seluruh Total Control dan Read Only), Default User, maupun aktor `Siti Nurhaliza`
11. Klik `[Cancel]` untuk menutup popup

### TC-AC-RP-162: Pool Assign User Global Role untuk aktor Manage user and role

12. Ganti akun: Logout, lalu login sebagai `Hendra Wijaya` (`manageUserRoleU_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_MUR_U_PASSWORD`)
13. Klik menu `Settings > Role & Permission` di sidebar
14. Klik tab `System`
15. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
16. Klik "+ Assign"
17. Ketik Search "Fajar", tekan Enter
18. Verifikasi `Fajar Nugroho` (Group Manager `Region Jawa`) muncul di hasil Search
19. Ganti isi kotak search dengan "Rina", tekan Enter
20. Verifikasi hasil Search "Rina" (pemegang Total Control `Rina Wijaya`) menampilkan "No results found"
21. Ganti isi kotak search dengan "Anggraini", tekan Enter
22. Verifikasi hasil Search "Anggraini" (pemegang Read Only `Dewi Anggraini`) menampilkan "No results found"
23. Ganti isi kotak search dengan "Bambang", tekan Enter
24. Verifikasi hasil Search "Bambang" (Default User `Bambang Hartono`) menampilkan "No results found"
25. Ganti isi kotak search dengan "Hendra", tekan Enter
26. Verifikasi hasil Search "Hendra" (aktor `Hendra Wijaya`) menampilkan "No results found"
27. Klik `[Cancel]` untuk menutup popup

### TC-AC-RP-412: Pool Assign User Group Role untuk aktor Manage user and role

28. Klik menu `Settings > Role & Permission` di sidebar
29. Klik tab `System`
30. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
31. Klik node `Region Jawa`
32. Klik "+ Assign"
33. Verifikasi sedikitnya satu kandidat tampil di Table User Picker
34. Ketik Search "Fajar", tekan Enter
35. Verifikasi `Fajar Nugroho` (Group Manager `Region Jawa`) tidak muncul di picker
36. Klik `[Cancel]` untuk menutup popup
37. Klik node `Region A`
38. Klik "+ Assign"
39. Ketik Search "Fajar", tekan Enter
40. Verifikasi `Fajar Nugroho` muncul di picker untuk group `Region A`
41. Klik `[Cancel]` untuk menutup popup

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 7 (telusuri seluruh halaman Pagination popup sebelum asersi kandidat langkah 8 sampai 10; pola spec 033), langkah 11, 27, 36, 41 (`[Cancel]` menutup popup yang tidak dirty), langkah 13 dan 28 (klik sidebar membuka halaman bersih dan mereset Tab), serta langkah 17, 34, 39 (Search untuk menemukan kandidat target) dan langkah 19, 21, 23, 25 (ganti isi kotak search dengan nama pemegang yang harus tidak muncul, bagian 8b butir 9).
- TC-AC-RP-160 dan TC-AC-RP-161 memakai satu pembukaan popup yang sama karena hanya mengamati tanpa submit (prinsip halaman dipakai berulang).
- Asersi tambahan (S-03): langkah 33 adalah pembanding generik sebagai anchor positif bagi absence `Fajar Nugroho` di langkah 35 sesudah Search (bagian 8b butir 2). Pada TC-AC-RP-162, langkah 18 (`Fajar Nugroho` muncul di hasil Search pada popup yang sama) menjadi anchor positif bagi "No results found" pada langkah 20, 22, 24, dan 26.
- Alasan spec berada di atas sekitar 35 langkah (41 langkah): empat TC sumber memakai popup Assign User yang sama, hanya membaca dan menutup popup tanpa Assign; TC-AC-RP-162 menuntut Search per nama (empat nama, tiap nama satu aksi Search dan satu Verifikasi per klausa, S-01) sehingga menaikkan jumlah langkah, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-RP-161 Expected membaca daftar kandidat tanpa menyebut Search atau paginasi; popup memakai ukuran halaman bawaan 10 dan kandidat berjumlah sekitar 12 (`Teguh Santoso` berada di halaman 2), sehingga spec menelusuri seluruh halaman Pagination (langkah 7) sebelum asersi.
  - TC-AC-RP-412 Expected a: TC tidak menyebut anchor positif untuk absence `Fajar Nugroho`; pembanding generik ditambahkan spec (S-03).
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
