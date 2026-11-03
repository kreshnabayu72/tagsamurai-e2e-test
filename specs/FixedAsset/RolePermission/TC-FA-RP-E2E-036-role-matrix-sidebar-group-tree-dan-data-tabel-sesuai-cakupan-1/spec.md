---
id: TC-FA-RP-E2E-036-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-1
title: "Role Matrix: Sidebar Group Tree dan data tabel sesuai cakupan peran (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-122
  - TC-FA-RP-123
  - TC-FA-RP-124
  - TC-FA-RP-127
  - TC-FA-RP-128
coverage:
  web: automated
---

# Role Matrix: Sidebar Group Tree dan data tabel sesuai cakupan peran (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-122, TC-FA-RP-124, TC-FA-RP-127, TC-FA-RP-128 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| TC-FA-RP-123 | Manage user & role (Group, Update, `IT Infrastructure`) | Manage dengan Update | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |

- Data Pre-setup yang dibaca: pohon group #18, seed Group Manager beragam #43 (Fajar Nugroho `IT Infrastructure`, Kevin Susanto `Data Center`, Lina Marlina `Head Office`), pool Home Group #17, dan pool pengguna #15 (Detail Role `Manage accounting`: Ahmad Fauzi, Citra Lestari). Tiga user Total Control yang di-seed hook `before` dari pool Pre-setup #17: Gunawan Halim (Home Group `Data Center`), Hesti Rahma (Home Group `Logistics Warehouse`), dan Indra Kusuma (tanpa Home Group), ditetapkan Total Control lewat seed API; hook `after` mengembalikan ketiganya ke kondisi Pre-setup #17 (tanpa tingkat akses).
- State global yang diubah: tingkat akses tiga user #17 (dipulihkan hook `after`).

## Test Steps

### TC-FA-RP-122: Group Manager, Sidebar Group Tree pada Tab Group Manager

1. Klik Tab Group Manager
2. Verifikasi Pohon pada Tab Group Manager memuat `Head Office` (ancestor, non-selectable), `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
3. Verifikasi `Logistics Warehouse` dan `Dock 1` tidak dirender
4. Catat jumlah baris Tab Group Manager sebagai baseline sebelum klik node
5. Klik node `Head Office`
6. Verifikasi Klik `Head Office` tidak memilih node
7. Verifikasi Klik `Head Office` tidak menyaring tabel (jumlah baris sama dengan baseline langkah 4)
8. Klik node `Data Center`
9. Verifikasi Klik `Data Center` memilih node
10. Verifikasi Klik `Data Center` menyaring tabel ke baris penugasan langsung: baris Kevin Susanto di `Data Center` tampil
11. Verifikasi Baris Fajar Nugroho di `IT Infrastructure` tidak tampil setelah `Data Center` dipilih

### TC-FA-RP-124: Group Manager, Tab Total Control hanya user ber-Home Group dalam cakupan

12. Klik Tab Total Control
13. Verifikasi Hanya user Total Control ber-Home Group `Data Center` yang tampil (Gunawan Halim)
14. Verifikasi User ber-Home Group `Logistics Warehouse` (Hesti Rahma) dan user tanpa Home Group (Indra Kusuma) tidak tampil

### TC-FA-RP-127: Group Manager, Tab Group Manager hanya penugasan dalam cakupan

15. Klik Tab Group Manager
16. Klik `All Groups` di Sidebar Group Tree
17. Verifikasi Baris Fajar Nugroho (`IT Infrastructure`) dan Kevin Susanto (`Data Center`) tampil
18. Verifikasi Baris Lina Marlina di `Head Office` (ancestor di luar cakupan) tidak tampil

### TC-FA-RP-128: Group Manager, Detail Role Global Role hanya baca

19. Klik Tab System
20. Buka Detail Role `Manage accounting` (klik Role Name pada section Global Role)
21. Verifikasi Seluruh baris penugasan Global Role tampil (read-only), termasuk baris Ahmad Fauzi dan Citra Lestari
22. Verifikasi `[+ Assign]`, `Remove`, dan checkbox CRUD Hidden

### TC-FA-RP-123: Manage user & role (Group, Update), Sidebar Group Tree pada Tab Group Manager

23. Ganti akun: logout, lalu login sebagai Manage user & role (Group, Update, `IT Infrastructure`) (Gita Maharani)
24. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab Group Manager
25. Verifikasi Pohon pada Tab Group Manager memuat `Head Office` (ancestor, non-selectable), `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk`
26. Verifikasi `Logistics Warehouse` dan `Dock 1` tidak dirender
27. Catat jumlah baris Tab Group Manager sebagai baseline sebelum klik node
28. Klik node `Head Office`
29. Verifikasi Klik `Head Office` tidak memilih node
30. Verifikasi Klik `Head Office` tidak menyaring tabel (jumlah baris sama dengan baseline langkah 27)
31. Klik node `Data Center`
32. Verifikasi Klik `Data Center` memilih node
33. Verifikasi Klik `Data Center` menyaring tabel ke baris penugasan langsung: baris Kevin Susanto di `Data Center` tampil
34. Verifikasi Baris Fajar Nugroho di `IT Infrastructure` tidak tampil setelah `Data Center` dipilih

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1, 12, 15 dan 19); membuka halaman Role & Permission setelah ganti akun (langkah 24); mencatat baseline jumlah baris (langkah 4, 27) dan membuka Detail Role lewat Role Name (langkah 20).
- Ganti akun eksplisit (logout lalu login) pada langkah 23.
- Asersi tidak tampil pada langkah 3, 11, 14, 17, 18, 22, 26, 34 memakai baris atau node yang tampil pada `Verifikasi` sebelumnya sebagai anchor positif (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-125, TC-FA-RP-126, dan TC-FA-RP-1018 ada di spec 037.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-FA-RP-124, TC-FA-RP-125, dan TC-FA-RP-126 Precondition d menyebut tiga user Total Control tanpa nama; spec memakai Gunawan Halim (`Data Center`), Hesti Rahma (`Logistics Warehouse`), dan Indra Kusuma (tanpa Home Group) dari Pre-setup #17. Pre-setup #36 memuat sembilan user Total Control lain, sehingga "hanya" tidak dapat dijamin; spec mengasersi kehadiran Gunawan Halim dan ketidakhadiran Hesti Rahma serta Indra Kusuma.
  - Expected b TC-FA-RP-122 dan TC-FA-RP-123 "tidak menyaring tabel" tidak menyebut acuan; spec mencatat jumlah baris sebelum klik sebagai baseline (langkah penghubung) lalu membandingkan.
  - Expected a TC-FA-RP-128 "Seluruh baris penugasan" tidak menyebut jumlah; spec memakai baris Ahmad Fauzi dan Citra Lestari (Pre-setup #15) sebagai wakil.
  - Urutan TC di spec ini mengikuti kelompok Tab (Group Manager, Total Control, Group Manager, System) untuk akun Group Manager sebelum ganti akun; TC-FA-RP-123 dijalankan terakhir sesudah ganti akun.
