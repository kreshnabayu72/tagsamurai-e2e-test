---
id: TC-GS-ROLE-E2E-015-role-matrix-visibilitas-menu-sidebar-per-aktor
title: "Role Matrix: Visibilitas Menu Sidebar Role & Permission per Aktor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-33
  - TC-GS-ROLE-34
  - TC-GS-ROLE-282
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu Sidebar Role & Permission per Aktor

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel di bawah.
- Langkah tiap role sama (login, buka Global Settings, amati sidebar); yang berbeda hanya akun dan hasil yang diharapkan. Karena hasil pada role Hendra Wijaya dan Yusuf Hidayat memuat asersi tambahan, langkah ditulis per blok role.

Role yang diuji (Tabel Data Uji Pre-setup #1, #4, #5, #6, #7, #8):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-33 | Total Control | Ahmad Fauzi | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-ROLE-33 | Read Only | Siti Nurhaliza | disediakan tim FE | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-ROLE-33 | Manage user and role Read saja | Fajar Nugroho | `manageUserAndRoleRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_READ_PASSWORD` (env baru) |
| TC-GS-ROLE-33 | Manage user and role Create, Read, Delete tanpa Update | Lina Marlina | `manageUserAndRoleCreateDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRD_PASSWORD` (env baru) |
| TC-GS-ROLE-33, TC-GS-ROLE-282 | Manage user and role C/R/U/D (tanpa access level) | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |
| TC-GS-ROLE-34 | Manage TAG Read saja | Yusuf Hidayat | `manageTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGETAG_READ_PASSWORD` (env baru) |

- Login Total Control (role pertama) dilakukan di hook `before`; role berikutnya memakai langkah ganti akun eksplisit (logout lalu login). Karena spec berakhir di akun Yusuf Hidayat, hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; env baru didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data: memakai data Pre-setup; spec tidak membuat, mengubah, atau menghapus data. Hendra Wijaya tidak memegang access level (Total Control atau Read Only).
- Layar awal spec: Global Settings dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-33: Menu Role & Permission tampil untuk aktor yang punya akses baca

1. Verifikasi menu "Role & Permission" tampil pada sidebar untuk Total Control
2. Logout, lalu login sebagai Read Only
3. Buka Global Settings
4. Verifikasi menu "Role & Permission" tampil pada sidebar untuk Read Only
5. Logout, lalu login sebagai Manage user and role Read saja
6. Buka Global Settings
7. Verifikasi menu "Role & Permission" tampil pada sidebar untuk Manage user and role Read saja
8. Logout, lalu login sebagai Manage user and role Create, Read, Delete tanpa Update
9. Buka Global Settings
10. Verifikasi menu "Role & Permission" tampil pada sidebar untuk Manage user and role tanpa Update
11. Logout, lalu login sebagai Manage user and role C/R/U/D
12. Buka Global Settings
13. Verifikasi menu "Role & Permission" tampil pada sidebar untuk Manage user and role C/R/U/D

### TC-GS-ROLE-282: Menu General Settings dan Activity Log tidak tampil untuk pemegang role individual tanpa access level

14. Verifikasi menu "User" tampil pada sidebar
15. Verifikasi menu "Role & Permission" tampil pada sidebar
16. Verifikasi menu "General Settings" dan "Activity Log" tidak tampil pada sidebar

### TC-GS-ROLE-34: Menu Role & Permission tersembunyi untuk user tanpa role Manage user and role

17. Logout, lalu login sebagai Manage TAG Read saja
18. Buka Global Settings
19. Verifikasi menu "TAG" tampil pada sidebar
20. Verifikasi menu "Role & Permission" tidak tampil pada sidebar

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi) berupa matriks visibilitas menu sidebar per aktor yang memuat polaritas tampil dan tidak tampil; `caseType` Positive mengikuti alur dominan (lima dari enam role yang diuji berhasil melihat menu Role & Permission).
- Urutan TC sumber diubah: Total Control dijalankan pertama karena akun hook `before`; Hendra Wijaya (TC-GS-ROLE-33 Expected c) dijalankan terakhir di blok TC-GS-ROLE-33 supaya TC-GS-ROLE-282 memakai sesi yang sama tanpa login tambahan; TC-GS-ROLE-34 terakhir karena Yusuf Hidayat tanpa akses Role & Permission.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): logout lalu login ke role berikutnya (langkah 2, 5, 8, 11, 17).
- Langkah 14 dan 15 menjadi anchor positif untuk asersi absence pada langkah 16; langkah 19 (menu "TAG" tampil) menjadi anchor positif untuk langkah 20. Langkah 15 mengulang asersi langkah 13 karena Expected a TC-GS-ROLE-282 memuatnya sendiri.
- Urutan Expected TC-GS-ROLE-34 diubah: menu "TAG" (Expected b) diverifikasi lebih dulu daripada menu "Role & Permission" tidak tampil (Expected a) supaya absence punya anchor positif (bagian 8b butir 2).
- Langkah 1 memakai sesi hook `before` tanpa langkah buka, karena layar awal dibuka di hook `beforeEach`.
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-GS-ROLE-33 dan TC-GS-ROLE-282 tidak memberi cara membedakan sidebar sebelum dan sesudah login selain "buka Global Settings"; spec memakai layar Global Settings sebagai titik amati.
  - TC-GS-ROLE-33 Expected a sampai e tidak menyebut menu lain di sidebar; hanya menu "Role & Permission" yang diasersi untuk lima aktor pertama.
  - Email Siti Nurhaliza tidak ada di Pre-setup TC; ditulis "disediakan tim FE".
