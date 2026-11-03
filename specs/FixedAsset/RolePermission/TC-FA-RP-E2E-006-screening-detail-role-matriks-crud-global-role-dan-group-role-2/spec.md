---
id: TC-FA-RP-E2E-006-screening-detail-role-matriks-crud-global-role-dan-group-role-2
title: "Screening Detail Role: matriks CRUD Global Role dan Group Role (2/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-19
  - TC-FA-RP-20
  - TC-FA-RP-21
  - TC-FA-RP-22
coverage:
  web: automated
---

# Screening Detail Role: matriks CRUD Global Role dan Group Role (2/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup: #15 (pool pengguna) dan #18 (pohon group Company Alpha). Spec hanya membaca; tidak mengubah data.
- Tabel "Role Group yang diuji" (urutan baris = urutan iterasi; `cb` = checkbox, `—` = tanpa checkbox):

| Role Name (Group Role) | TC | Sub-title | Create | Read | Update | Delete |
|---|---|---|---|---|---|---|
| `Manage group` | TC-FA-RP-19 | `This role allows the user to manage organizational sub-groups within assigned scope through the Groups menu.` | cb | cb | cb | cb |
| `Manage files` | TC-FA-RP-20 | `This role allows the user to manage asset-related files and documents within assigned groups through the File Manager menu.` | `—` | cb | `—` | cb |
| `Manage user & role` | TC-FA-RP-21 | `This role allows the user to manage group-level user roles, permissions, and approvers through the Settings > Role & Permission menu.` | `—` | cb | cb | `—` |
| `Manage asset license` | TC-FA-RP-21 | `This role allows the user to monitor and manage asset license quotas and addon usage within assigned groups through the License menu.` | `—` | cb | cb | `—` |
| `Manage purchase` | TC-FA-RP-22 | `This role allows the user to manage purchase orders, procurement documents, and asset purchase details and acquisition costs within assigned groups.` | cb | cb | cb | cb |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan tabel role di atas ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-19, TC-FA-RP-20, TC-FA-RP-21, dan TC-FA-RP-22: Bagian umum halaman Detail Role Group Role (diamati pada role pertama tabel)

1. Klik Tab `System`
2. Klik Role Name `Manage group` pada section Group Role
3. Verifikasi Breadcrumb tampil `Settings > Role & Permission > System > Detail`
4. Verifikasi kolom Name, Group, Position, Division tampil
5. Verifikasi toolbar `Search | Filter | Download | Changelog | [+ Assign]`
6. Klik segmen `System` pada Breadcrumb
7. Verifikasi segmen `System` dapat diklik: Tab `System` tampil kembali dengan section Group Role

### TC-FA-RP-19, TC-FA-RP-20, TC-FA-RP-21, dan TC-FA-RP-22: Title, Sidebar Group Tree, Group, dan kolom matriks per role

8. Untuk setiap baris tabel "Role Group yang diuji" (langkah 8 sampai 13): klik Role Name pada baris tabel di section Group Role
9. Verifikasi Title `[Role Name]` diikuti sub-title deskripsi pada baris tabel
10. Verifikasi Sidebar Group Tree tampil di sisi kanan dengan `All Groups` aktif
11. Verifikasi kolom Group tampil
12. Verifikasi kolom matriks Create, Read, Update, dan Delete sesuai baris tabel (`cb` = checkbox, `—` = tanpa checkbox)
13. Klik segmen `System` pada Breadcrumb

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-19, 20, 21, 22). Keempat TC memuat langkah identik dengan daftar role berbeda; hasilnya digabung dalam satu tabel "Role Group yang diuji". TC-FA-RP-23 (`View asset value`) dan TC-FA-RP-24 (`Manage asset & TAG`) ada di spec `TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3`.
- Pengulangan (bagian 8b butir 7): langkah 8 sampai 13 diulang untuk 5 baris tabel; parameter tiap iterasi ada di tabel Prerequisites. Langkah terakhir tiap iterasi (klik segmen `System`) mengembalikan ke daftar role (langkah penghubung).
- Pemecahan asersi: klausa TC yang tidak bergantung role (Breadcrumb, kolom Name, Group, Position, Division, toolbar, segmen `System` dapat diklik) diasersi sekali pada role pertama tabel; klausa per role (Title, sub-title, Sidebar Group Tree, kolom Group, kolom matriks) diasersi tiap iterasi.
- Alasan di atas sekitar 35 langkah setelah ekspansi (13 langkah nominal; blok iterasi 6 langkah dikali 5 baris menjadi 37 langkah): seluruh blok satu topik (screening Detail Role Group Role) dan satu kelas fungsional, hanya aksi baca; tiap iterasi berdiri sendiri sehingga kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, klik Role Name, dan klik segmen `System`.
- Temuan untuk QA:
  - Post Condition TC-FA-RP-19, 20, 21, dan 22 tidak memberi langkah observasi tambahan; tidak diasersi.
