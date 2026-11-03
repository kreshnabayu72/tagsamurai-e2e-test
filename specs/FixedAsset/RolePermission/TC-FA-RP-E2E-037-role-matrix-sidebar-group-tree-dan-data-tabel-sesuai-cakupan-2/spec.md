---
id: TC-FA-RP-E2E-037-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-2
title: "Role Matrix: Sidebar Group Tree dan data tabel sesuai cakupan peran (2/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-125
  - TC-FA-RP-126
  - TC-FA-RP-1018
coverage:
  web: automated
---

# Role Matrix: Sidebar Group Tree dan data tabel sesuai cakupan peran (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role (Group, Update) (Gita Maharani); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-125, TC-FA-RP-1018 | Manage user & role (Group, Update, `IT Infrastructure`) | Manage dengan Update | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| TC-FA-RP-126 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

- Data Pre-setup yang dibaca: pohon group #18, seed Group Manager beragam #43, penugasan Manage user & role Group #33, dan pool Home Group #17. Tiga user Total Control yang di-seed hook `before` dari pool Pre-setup #17: Gunawan Halim (Home Group `Data Center`), Hesti Rahma (Home Group `Logistics Warehouse`), dan Indra Kusuma (tanpa Home Group), ditetapkan Total Control lewat seed API; hook `after` mengembalikan ketiganya ke kondisi Pre-setup #17 (tanpa tingkat akses).
- State global yang diubah: tingkat akses tiga user #17 (dipulihkan hook `after`).

## Test Steps

### TC-FA-RP-125: Manage user & role (Group, Update), Tab Total Control

1. Verifikasi Hanya user Total Control ber-Home Group `Data Center` yang tampil (Gunawan Halim)
2. Verifikasi User ber-Home Group `Logistics Warehouse` (Hesti Rahma) dan user tanpa Home Group (Indra Kusuma) tidak tampil

### TC-FA-RP-1018: Manage user & role (Group, Update), Tab Group Manager

3. Klik Tab Group Manager
4. Klik `All Groups` di Sidebar Group Tree
5. Verifikasi Baris Fajar Nugroho di `IT Infrastructure` dan Kevin Susanto di `Data Center` tampil
6. Verifikasi Baris Lina Marlina di `Head Office` tidak tampil karena di luar cakupan `IT Infrastructure` beserta descendant

### TC-FA-RP-126: Manage global user & role (Update), Tab Total Control

7. Ganti akun: logout, lalu login sebagai Manage global user & role (Update) (Hendra Wijaya)
8. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab Total Control
9. Verifikasi Seluruh user Total Control ber-Home Group `Data Center` (Gunawan Halim) tampil
10. Verifikasi User Total Control ber-Home Group `Logistics Warehouse` (Hesti Rahma) dan user Total Control tanpa Home Group (Indra Kusuma) tampil tanpa penyaringan Home Group

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 3); membuka halaman Role & Permission setelah ganti akun (langkah 8).
- Ganti akun eksplisit (logout lalu login) pada langkah 7.
- Asersi tidak tampil memakai baris yang tampil pada `Verifikasi` sebelumnya (Gunawan Halim; Fajar Nugroho dan Kevin Susanto) sebagai anchor positif (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-122, TC-FA-RP-123, TC-FA-RP-124, TC-FA-RP-127, dan TC-FA-RP-128 ada di spec 036.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-FA-RP-124, TC-FA-RP-125, dan TC-FA-RP-126 Precondition d menyebut tiga user Total Control tanpa nama; spec memakai Gunawan Halim (`Data Center`), Hesti Rahma (`Logistics Warehouse`), dan Indra Kusuma (tanpa Home Group) dari Pre-setup #17. Pre-setup #36 memuat sembilan user Total Control lain, sehingga "hanya" tidak dapat dijamin; spec mengasersi kehadiran Gunawan Halim dan ketidakhadiran Hesti Rahma serta Indra Kusuma.
  - Expected TC-FA-RP-126 "termasuk yang ber-Home Group di luar group mana pun" tidak jelas karena `Logistics Warehouse` ada di pohon Pre-setup #18; spec memakai Hesti Rahma (`Logistics Warehouse`) dan Indra Kusuma (tanpa Home Group) sebagai wakil dan menafsirkan "di luar group mana pun" sebagai di luar cakupan aktor.
  - TC-FA-RP-1018 Langkah Uji menyebut `All Groups` aktif; spec mengklik `All Groups` sebagai langkah penghubung supaya node tidak tersaring.
  - `caseType` Edge karena dua dari tiga TC sumber bertipe Edge Case.
