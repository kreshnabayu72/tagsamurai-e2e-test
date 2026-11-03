---
id: TC-FA-RP-E2E-032-role-matrix-panel-approval-settings-registration-per-peran-1
title: "Role Matrix: Panel Approval Settings Registration per peran (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-112
  - TC-FA-RP-113
  - TC-FA-RP-114
  - TC-FA-RP-115
coverage:
  web: automated
---

# Role Matrix: Panel Approval Settings Registration per peran (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Siti Rahmawati); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-112 | Total Control | Penuh | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-RP-113 | Read Only | Hanya baca | Dewi Anggraini (Pre-setup #4) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| TC-FA-RP-114 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| TC-FA-RP-115 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

- Data Pre-setup yang dibaca: pohon group #18 dan seed pemegang Update Manage asset & TAG #21 (Ahmad Fauzi, Budi Santoso, Dimas Pranata, Endah Susanti, Siti Rahayu). Seeding ke kondisi Tabel Data Uji Pre-setup TC dilakukan hook `before`. Spec tidak mengubah toggle atau data.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-RP-112: Total Control

1. Klik Tab System
2. Buka Detail Role `Manage asset & TAG` (klik Role Name pada section Group Role)
3. Klik node `IT Infrastructure` di Sidebar Group Tree
4. Verifikasi Toggle `Require Approval for Registration` Enabled
5. Verifikasi Ikon info `ⓘ` keterangan approver tampil (Show) di samping label toggle

### TC-FA-RP-113: Read Only

6. Ganti akun: logout, lalu login sebagai Read Only (Dewi Anggraini)
7. Klik Tab System
8. Buka Detail Role `Manage asset & TAG` (klik Role Name pada section Group Role)
9. Klik node `IT Infrastructure` di Sidebar Group Tree
10. Hover toggle `Require Approval for Registration`
11. Verifikasi Toggle `Require Approval for Registration` Disabled dengan tooltip `Read Only access cannot modify data.`
12. Verifikasi Ikon info `ⓘ` keterangan approver tampil (Show) di samping label toggle

### TC-FA-RP-114: Group Manager

13. Ganti akun: logout, lalu login sebagai Group Manager (Fajar Nugroho, `IT Infrastructure`)
14. Klik Tab System
15. Buka Detail Role `Manage asset & TAG` (klik Role Name pada section Group Role)
16. Klik node `IT Infrastructure` di Sidebar Group Tree
17. Verifikasi Toggle `Require Approval for Registration` Enabled
18. Verifikasi Ikon info `ⓘ` keterangan approver tampil (Show) di samping label toggle

### TC-FA-RP-115: Manage global user & role (Update)

19. Ganti akun: logout, lalu login sebagai Manage global user & role (Update) (Hendra Wijaya)
20. Klik Tab System
21. Buka Detail Role `Manage asset & TAG` (klik Role Name pada section Group Role)
22. Klik node `IT Infrastructure` di Sidebar Group Tree
23. Verifikasi Toggle `Require Approval for Registration` Enabled
24. Verifikasi Ikon info `ⓘ` keterangan approver tampil (Show) di samping label toggle

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), sehingga satu blok per TC. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1, 7, 14 dan 20); hover untuk membaca tooltip (langkah 10).
- Ganti akun eksplisit (logout lalu login) pada langkah 6, 13, dan 19.
- Asersi `Hidden` memakai halaman yang sudah termuat dengan baris target yang tampil (toggle dan ikon info yang tampil) sebagai anchor permukaan (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-116 sampai TC-FA-RP-118 ada di spec 033.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Pre-setup #21 tidak menyebut node tempat toggle `Require Approval for Registration` berada pada kondisi apa; spec membuka `IT Infrastructure` sesuai Langkah Uji dan tidak mengubah toggle.
  - TC menyebut Detail Role `Manage asset & TAG` tanpa menyebut section; spec membukanya dari section Group Role karena Langkah Uji memilih node di Sidebar Group Tree.
