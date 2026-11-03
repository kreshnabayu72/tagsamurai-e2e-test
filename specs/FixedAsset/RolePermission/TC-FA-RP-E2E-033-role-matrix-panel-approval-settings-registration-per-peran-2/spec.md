---
id: TC-FA-RP-E2E-033-role-matrix-panel-approval-settings-registration-per-peran-2
title: "Role Matrix: Panel Approval Settings Registration per peran (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-116
  - TC-FA-RP-117
  - TC-FA-RP-118
coverage:
  web: automated
---

# Role Matrix: Panel Approval Settings Registration per peran (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role (Group, Update) (Gita Maharani); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-116 | Manage user & role (Group, Update, `IT Infrastructure`) | Manage dengan Update | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| TC-FA-RP-117 | Manage global user & role tanpa Update | Manage tanpa Update | Bayu Prakoso (Pre-setup #8) | `murReadOnlyGate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD` |
| TC-FA-RP-118 | Manage user & role tanpa Update (Group, `IT Infrastructure`) | Manage tanpa Update | Wulan Sari (Pre-setup #9) | `murGroupReadOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_RO_PASSWORD` |

- Data Pre-setup yang dibaca: pohon group #18 dan seed pemegang Update Manage asset & TAG #21 (Ahmad Fauzi, Budi Santoso, Dimas Pranata, Endah Susanti, Siti Rahayu). Seeding ke kondisi Tabel Data Uji Pre-setup TC dilakukan hook `before`. Spec tidak mengubah toggle atau data.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-RP-116: Manage user & role (Group, Update)

1. Klik Tab System
2. Buka Detail Role `Manage asset & TAG` (klik Role Name pada section Group Role)
3. Klik node `IT Infrastructure` di Sidebar Group Tree
4. Verifikasi Toggle `Require Approval for Registration` Enabled
5. Verifikasi Ikon info `ⓘ` keterangan approver tampil (Show) di samping label toggle

### TC-FA-RP-117: Manage global user & role tanpa Update

6. Ganti akun: logout, lalu login sebagai Manage global user & role tanpa Update (Bayu Prakoso)
7. Klik Tab System
8. Buka Detail Role `Manage asset & TAG` (klik Role Name pada section Group Role)
9. Klik node `IT Infrastructure` di Sidebar Group Tree
10. Hover toggle `Require Approval for Registration`
11. Verifikasi Toggle `Require Approval for Registration` Disabled dengan tooltip `Read Only access cannot modify data.`
12. Verifikasi Ikon info `ⓘ` keterangan approver tampil (Show) di samping label toggle

### TC-FA-RP-118: Manage user & role tanpa Update (Group)

13. Ganti akun: logout, lalu login sebagai Manage user & role tanpa Update (Group, `IT Infrastructure`) (Wulan Sari)
14. Klik Tab System
15. Buka Detail Role `Manage asset & TAG` (klik Role Name pada section Group Role)
16. Klik node `IT Infrastructure` di Sidebar Group Tree
17. Hover toggle `Require Approval for Registration`
18. Verifikasi Toggle `Require Approval for Registration` Disabled dengan tooltip `Read Only access cannot modify data.`
19. Verifikasi Ikon info `ⓘ` keterangan approver tampil (Show) di samping label toggle

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), sehingga satu blok per TC. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1, 7 dan 14); hover untuk membaca tooltip (langkah 10 dan 17).
- Ganti akun eksplisit (logout lalu login) pada langkah 6 dan 13.
- Asersi `Hidden` memakai halaman yang sudah termuat dengan baris target yang tampil (toggle dan ikon info yang tampil) sebagai anchor permukaan (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-112 sampai TC-FA-RP-115 ada di spec 032.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Pre-setup #21 tidak menyebut node tempat toggle `Require Approval for Registration` berada pada kondisi apa; spec membuka `IT Infrastructure` sesuai Langkah Uji dan tidak mengubah toggle.
  - TC menyebut Detail Role `Manage asset & TAG` tanpa menyebut section; spec membukanya dari section Group Role karena Langkah Uji memilih node di Sidebar Group Tree.
  - `caseType` Negative karena dua dari tiga TC sumber menguji toggle yang Disabled.
