---
id: TC-FA-RP-E2E-071-remove-group-manager-2
title: "Remove Group Manager (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-238
  - TC-FA-RP-1036
coverage:
  web: automated
---

# Remove Group Manager (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login akun pertama di hook `before`; akun berikutnya lewat langkah ganti akun eksplisit):

| Urutan | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| 1 | Total Control | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Group Manager (`IT Infrastructure`) | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #18 (pohon group), #33 (Seed Manage user & role Group; baris Group Role `Manage asset & TAG` Budi Santoso di `Data Center` dan `Dock 1`), #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #13 (Kevin Susanto: Group Manager di `Data Center`; baris pola GM di `Data Center` dan `Rack A1` (Group Role katalog selain `Manage user & role` CRUD penuh sesuai kolom berlaku, Role Transaksi Asset Admin dan Approver pada tiap Jenis Transaksi); baris non-pola: Group Role `Manage user & role` di `Data Center`, `Manage files` Read dan Delete di `Helpdesk`, Global Role `Manage accounting` hanya Read).
- Sesi kedua: sesi API Total Control (Pre-setup #2, Siti Rahmawati, `Spectra.env.FA_TC_PASSWORD`) meng-Remove Group Manager Fajar Nugroho pada TC-FA-RP-238; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): baris Global Role Kevin Susanto dan baris non-pola Group Role `Manage user & role` di `Data Center` dicatat sebagai baseline untuk TC-FA-RP-1036 Expected b, d, dan e.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1036: Remove Group Manager menghapus baris pola GM pada node penugasan dan descendant, tetapi tidak baris non-pola, node di luar subtree, atau Global Role, dan pola ditulis ulang saat Assign ulang

1. Catat baris Global Role Kevin Susanto (`Manage accounting` hanya Read) dan baris non-pola Group Role `Manage user & role` di `Data Center` lewat fixture BE sebagai baseline
2. Klik Tab `Group Manager`
3. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`, klik `[Remove]`
4. Tunggu aksi selesai: dialog tertutup
5. Buka Tab System lalu Detail Role `Manage group` dan klik node `Data Center`
6. Verifikasi tabel Detail Role `Manage group` tampil (anchor permukaan termuat)
7. Verifikasi baris Group Role Kevin Susanto pada node `Data Center` tidak ada (baris pola GM dihapus di node penugasan)
8. Klik node `Rack A1`
9. Verifikasi baris Group Role Kevin Susanto pada descendant `Rack A1` tidak ada (baris pola GM dihapus di seluruh descendant)
10. Buka Detail Role `Manage user & role` dan klik node `Data Center`
11. Verifikasi baris `Manage user & role` Kevin Susanto di `Data Center` tetap ada dan sama dengan baseline (non-pola)
12. Buka Detail Role `Manage files` dan klik node `Helpdesk`
13. Verifikasi baris Kevin Susanto pada `Helpdesk` (di luar subtree) tetap ada
14. Buka Detail Role `Manage accounting` pada section Global Role
15. Verifikasi baris Global Role Kevin Susanto tidak berubah dari baseline
16. Di Tab `Group Manager` klik `[+ Assign]`, pilih Kevin Susanto untuk `Data Center`, klik `[Assign]`
17. Tunggu aksi selesai: popup tertutup
18. Klik node `Data Center` di Sidebar Group Tree
19. Verifikasi penugasan Group Manager Kevin Susanto di `Data Center` kembali di Tab Group Manager
20. Buka kembali Detail Role `Manage group` pada node `Data Center`
21. Verifikasi tabel Detail Role `Manage group` tampil (anchor permukaan termuat)
22. Verifikasi baris pola Group Role Kevin Susanto ditulis ulang pada `Data Center` dengan CRUD penuh sesuai kolom berlaku
23. Klik node `Rack A1`
24. Verifikasi baris pola Group Role Kevin Susanto ditulis ulang pada `Rack A1` dengan CRUD penuh sesuai kolom berlaku
25. Buka Detail Role `Manage user & role` dan klik node `Data Center`
26. Verifikasi baris `Manage user & role` Kevin Susanto di `Data Center` tidak berubah dari baseline
27. Pulihkan Kevin Susanto beserta baris pola GM dan baris non-pola-nya (Pre-setup #13) lewat seeding API

### TC-FA-RP-238: Wewenang inherited Group Manager berhenti setelah Remove

28. Logout dari akun Total Control (Siti Rahmawati)
29. Login sebagai Group Manager (`groupManager_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_GM_PASSWORD`)
30. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `System`
31. Sesi 1 (Fajar Nugroho) membuka Detail Role `Manage files` dan memilih node `Data Center`
32. Remove Group Manager Fajar Nugroho di `IT Infrastructure` lewat sesi API Total Control hingga tersimpan
33. Sesi 1 memuat ulang halaman Detail Role
34. Verifikasi node `Data Center` tidak lagi dirender di Sidebar Group Tree bagi Fajar Nugroho
35. Verifikasi `[+ Assign]` dan `Remove` tidak lagi tersedia untuk Group Role di `Data Center`
36. Pulihkan penugasan Group Manager Fajar Nugroho di `IT Infrastructure` lewat seeding API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 36 langkah. Di atas 35 langkah karena spec memuat dua TC (TC-FA-RP-1036 dan 238) dan blok 1036 memerlukan satu Verifikasi per klausa Expected (a sampai e) ditambah pembanding baris non-pola; tidak ada pengulangan yang dapat diringkas. Melewati 35 karena spec memuat dua TC (TC-FA-RP-1036 dan 238) dan blok 1036 memerlukan satu Verifikasi per klausa Expected (a sampai e) ditambah pembanding baris non-pola; tidak ada pengulangan yang dapat diringkas.
- Langkah penghubung (S-03): langkah 1–2, 4, 17–18, 28–30. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 27, 36; tidak ada `Verifikasi`.
- Penyimpangan urutan (S-05 catatan urutan): TC-FA-RP-1036 (aktor Total Control) dijalankan lebih dulu, lalu TC-FA-RP-238 (aktor Group Manager) agar ganti akun hanya sekali (langkah 22–24; login akun pertama di hook `before`).
- TC-FA-RP-238 memakai dua sesi (Manual Only (d) di TC): sesi 2 adalah pelaku kedua yang hanya memicu Remove sehingga memakai sesi API (suite.md; langkah ditulis "... hingga ... tersimpan", R-20), bukan konteks kedua kelas c.
- Absence baris pada TC-FA-RP-1036 (`Data Center` dan `Rack A1` pada `Manage group`) memakai tabel Detail Role yang termuat sebagai anchor permukaan (langkah 6); `Verifikasi` pembanding baris non-pola (`Manage user & role`) dan baris `Helpdesk` yang tetap ada menunjukkan Detail Role yang sama tampil.
- Temuan untuk QA:
  - TC-FA-RP-238 Expected b ("`[+ Assign]` dan `Remove` tidak lagi tersedia untuk Group Role di `Data Center`") sesudah Expected a (node `Data Center` tidak dirender) tidak dapat diamati pada node yang tidak ada; spec mengasersinya pada halaman Detail Role sesudah muat ulang.
  - TC-FA-RP-1036 Expected e ("CRUD penuh sesuai kolom berlaku") diamati pada Detail Role `Manage group` saja (TC langkah 6); kolom yang berlaku untuk `Manage group` tidak dirinci di TC, spec mengasersi CRUD penuh sesuai kolom berlaku tanpa menyebut kolom. Expected e "baris non-pola tidak berubah" tidak punya langkah buka di TC; spec membuka kembali `Manage user & role` di langkah 23.
  - Post Condition TC-FA-RP-238 tidak ada; pemulihan penugasan Group Manager Fajar Nugroho dilakukan di langkah seeding dan hook `after`.
