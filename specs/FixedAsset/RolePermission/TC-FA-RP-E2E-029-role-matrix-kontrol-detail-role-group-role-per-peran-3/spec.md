---
id: TC-FA-RP-E2E-029-role-matrix-kontrol-detail-role-group-role-per-peran-3
title: "Role Matrix: kontrol Detail Role Group Role per peran (3/3)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-104
coverage:
  web: automated
---

# Role Matrix: kontrol Detail Role Group Role per peran (3/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role tanpa Update (Group) (Wulan Sari); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-104 | Manage user & role tanpa Update (Group, `IT Infrastructure`) | Manage tanpa Update | Wulan Sari (Pre-setup #9) | `murGroupReadOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_RO_PASSWORD` |

- Data Pre-setup yang dibaca: pool pengguna Standard #15 (Ahmad Fauzi sebagai target Standard), pohon group #18 (`Data Center` sebagai node uji), dan penugasan #33. Seeding ke kondisi Tabel Data Uji Pre-setup TC dilakukan hook `before`. Spec tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-RP-104: Manage user & role tanpa Update (Group)

1. Klik Tab System
2. Klik Role Name `Manage files` pada section Group Role
3. Klik node `Data Center` di Sidebar Group Tree
4. Verifikasi `[+ Assign]` Hidden
5. Verifikasi Aksi `Remove` Hidden pada baris Ahmad Fauzi
6. Verifikasi Kolom Checkbox multi-select dan `Bulk Action` Hidden
7. Verifikasi Checkbox Create, Update, Delete baris Ahmad Fauzi Disabled
8. Hover checkbox Update baris Ahmad Fauzi
9. Verifikasi Checkbox Create, Update, Delete Disabled dengan tooltip `Read Only access cannot modify data.` (tooltip dibaca pada checkbox Update)
10. Hover checkbox Read baris Ahmad Fauzi
11. Verifikasi Checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), sehingga satu blok per TC. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); hover untuk membaca tooltip (langkah 8 dan 10).
- Asersi `Hidden` memakai halaman yang sudah termuat dengan baris target yang tampil (baris Ahmad Fauzi) sebagai anchor permukaan (bagian 8b butir 2).
- Spec memuat satu blok role karena TC-FA-RP-98 sampai TC-FA-RP-103 ada di spec 027 dan 028.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Expected d dan e tidak menyebut checkbox mana yang di-hover untuk tooltip; spec membaca tooltip pada checkbox Update (mewakili Create, Update, Delete) dan pada checkbox Read.
  - Baris Ahmad Fauzi diasumsikan ada pada halaman pertama node `Data Center` (Pre-setup #39).
  - `caseType` Negative karena satu-satunya TC sumber menguji kontrol yang Hidden atau Disabled.
