---
id: TC-FA-RP-E2E-005-screening-detail-role-matriks-crud-global-role-dan-group-role-1
title: "Screening Detail Role: matriks CRUD Global Role dan Group Role (1/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-16
  - TC-FA-RP-17
  - TC-FA-RP-18
coverage:
  web: automated
---

# Screening Detail Role: matriks CRUD Global Role dan Group Role (1/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup: #15 (pool pengguna Company Alpha). Spec hanya membaca; tidak mengubah data.
- Tabel "Role Global yang diuji" (urutan baris = urutan iterasi; kolom TC = sumber; sel matriks `cb` = checkbox, `—` = tanpa checkbox):

| Role Name (Global Role) | TC | Sub-title | Create | Read | Update | Delete |
|---|---|---|---|---|---|---|
| `Manage asset master data` | TC-FA-RP-16 | `This role allows the user to manage asset master records, categories, and custom fields through the Asset Master, Categories, and Custom Fields menus.` | cb | cb | cb | cb |
| `Manage accounting` | TC-FA-RP-16 | `This role allows the user to manage the Chart of Accounts, asset classes, tax depreciation classes, and accounting preferences, and automatically view asset depreciation data across all groups, through the Accounting menu.` | cb | cb | cb | cb |
| `Import data` | TC-FA-RP-17 | `This role allows the user to import asset records and master data into the system through the Import menu.` | cb | cb | `—` | `—` |
| `Manage asset transactional policy` | TC-FA-RP-18 | `This role allows the user to manage policies and operational rules for asset transactions through the Asset Transactional Policy menu.` | `—` | cb | cb | `—` |
| `Manage transaction settings` | TC-FA-RP-18 | `This role allows the user to manage global transaction settings through the Transaction Settings menu.` | `—` | cb | cb | `—` |
| `Manage asset ID configuration` | TC-FA-RP-18 | `This role allows the user to manage formatting and numbering rules for asset codes through the Custom Asset ID menu.` | `—` | cb | cb | `—` |
| `Manage global license` | TC-FA-RP-18 | `This role allows the user to monitor and manage concurrent user login sessions and allocate the global asset license quota in the License menu.` | `—` | cb | cb | `—` |
| `Manage global user & role` | TC-FA-RP-18 | `This role allows the user to manage user roles, permissions, and approvers across all groups — including assigning users to any group — through the Settings > Role & Permission menu.` | `—` | cb | cb | `—` |
| `Manage Open API` | TC-FA-RP-18 | `This role allows the user to manage API credentials and third-party integration settings through the Open API menu.` | `—` | cb | cb | `—` |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan tabel role di atas ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-16, TC-FA-RP-17, dan TC-FA-RP-18: Bagian umum halaman Detail Role Global Role (diamati pada role pertama tabel)

1. Klik Tab `System`
2. Klik Role Name `Manage asset master data` pada section Global Role
3. Verifikasi Breadcrumb tampil `Settings > Role & Permission > System > Detail`
4. Verifikasi kolom Name, Position, Division tampil
5. Verifikasi kolom Checkbox pinned kiri
6. Verifikasi toolbar `Search | Filter | Download | Changelog | [+ Assign]`
7. Klik segmen `System` pada Breadcrumb
8. Verifikasi segmen `System` dapat diklik: Tab `System` tampil kembali dengan section Global Role

### TC-FA-RP-16, TC-FA-RP-17, dan TC-FA-RP-18: Title, sub-title, dan kolom matriks per role

9. Untuk setiap baris tabel "Role Global yang diuji" (langkah 9 sampai 13): klik Role Name pada baris tabel di section Global Role
10. Verifikasi Title `[Role Name]` diikuti sub-title deskripsi pada baris tabel
11. Verifikasi tidak ada Sidebar Group Tree dan tidak ada kolom Group
12. Verifikasi kolom matriks Create, Read, Update, dan Delete sesuai baris tabel (`cb` = checkbox, `—` = tanpa checkbox)
13. Klik segmen `System` pada Breadcrumb

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-16, 17, 18). Ketiga TC memuat langkah identik (klik Role Name tiap role, perhatikan header, tabel, toolbar, klik segmen `System`) dengan daftar role berbeda; hasilnya digabung dalam satu tabel "Role Global yang diuji".
- Pengulangan (bagian 8b butir 7): langkah 9 sampai 13 diulang untuk 9 baris tabel; parameter tiap iterasi (Role Name, sub-title, sel matriks) ada di tabel Prerequisites. Langkah terakhir tiap iterasi (klik segmen `System`) mengembalikan ke daftar role (langkah penghubung).
- Pemecahan asersi: klausa TC yang tidak bergantung role (Breadcrumb, kolom Name, Position, Division, kolom Checkbox pinned, toolbar, segmen `System` dapat diklik) diasersi sekali pada role pertama tabel (blok pertama); klausa per role (Title, sub-title, tidak ada Sidebar Group Tree dan kolom Group, kolom matriks) diasersi tiap iterasi.
- Alasan di atas sekitar 35 langkah setelah ekspansi (13 langkah nominal; blok iterasi 5 langkah dikali 9 baris menjadi 53 langkah): seluruh blok satu topik (screening Detail Role Global Role) dan satu kelas fungsional, hanya aksi baca; tiap iterasi berdiri sendiri sehingga kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, klik Role Name, dan klik segmen `System`.
- Temuan untuk QA:
  - TC-FA-RP-16 expected b menulis "Pada tiap role: Title ... tidak ada Sidebar Group Tree dan tidak ada kolom Group"; spec memeriksanya tiap iterasi.
  - Post Condition TC-FA-RP-16, 17, dan 18 tidak memberi langkah observasi tambahan; tidak diasersi.
