---
id: TC-FA-RP-E2E-008-screening-detail-role-matriks-crud-global-role-dan-group-role-4
title: "Screening Detail Role: matriks CRUD Global Role dan Group Role (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-28
coverage:
  web: automated
---

# Screening Detail Role: matriks CRUD Global Role dan Group Role (4/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup: #15 (pool pengguna Company Alpha). Spec hanya membaca; tidak mengubah data.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover untuk membaca tooltip; penangkapan berkas unduhan browser untuk membaca nama berkas.
- Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-28: Toolbar Detail Role, urutan, tooltip toolbar, dan nama berkas Download

1. Klik Tab `System`
2. Klik Role Name `Manage Open API` pada section Global Role
3. Verifikasi urutan toolbar `Search | Filter | Download | Changelog | [+ Assign]`
4. Arahkan kursor ke ikon `Search` pada toolbar
5. Verifikasi tooltip `Search`
6. Arahkan kursor ke ikon `Filter` pada toolbar
7. Verifikasi tooltip `Filter`
8. Arahkan kursor ke ikon `Download` pada toolbar
9. Verifikasi tooltip `Download`
10. Arahkan kursor ke ikon `Changelog` pada toolbar
11. Verifikasi tooltip `Changelog`
12. Klik ikon `Download`
13. Verifikasi overlay Download memuat `Download as CSV` dan `Download as XLSX`
14. Klik `Download as CSV`
15. Verifikasi berkas `Role-Permission-Manage-Open-API.csv` terunduh
16. Klik ikon `Download`
17. Klik `Download as XLSX`
18. Verifikasi berkas `Role-Permission-Manage-Open-API.xlsx` terunduh

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-28).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab dan Role Name, hover ikon toolbar, dan membuka kembali overlay Download untuk pilihan format kedua.
- Expected c TC menyebut nama berkas `Role-Permission-Manage-Open-API` "dengan extension sesuai pilihan"; spec memeriksa kedua pilihan (`.csv` dan `.xlsx`). Isi berkas tidak diasersi.
- Temuan untuk QA:
  - TC-FA-RP-28 tidak menyebut pilihan format yang diunduh; spec mengunduh keduanya.
  - Post Condition TC-FA-RP-28 tidak memberi langkah observasi tambahan; tidak diasersi.
