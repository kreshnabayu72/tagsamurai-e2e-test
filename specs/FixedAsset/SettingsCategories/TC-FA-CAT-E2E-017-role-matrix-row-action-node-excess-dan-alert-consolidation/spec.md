---
id: TC-FA-CAT-E2E-017-role-matrix-row-action-node-excess-dan-alert-consolidation
title: "Role Matrix: Row Action Node Excess dan Alert Category Consolidation per Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-50
  - TC-FA-CAT-51
  - TC-FA-CAT-52
  - TC-FA-CAT-53
  - TC-FA-CAT-54
  - TC-FA-CAT-55
  - TC-FA-CAT-56
coverage:
  web: automated
---

# Role Matrix: Row Action Node Excess dan Alert Category Consolidation per Role

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Role yang diuji (bagian 3a; langkah identik tetapi ganti akun menuntut Step eksplisit, sehingga spec ditulis per blok role). Semua akun berada di client CatExcess (Pre-setup #31); email memakai `{namaCompany}` CatExcess:

| Role | Pre-setup | Akun | Password |
|---|---|---|---|
| Total Control | #1 | `Fixture.settingsCategories.totalControlExcess` (`totalControl_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_TC_PASSWORD` |
| Delete-Only | #6 | `Fixture.settingsCategories.deleteOnlyExcess` (`deleteOnly_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_DO_PASSWORD` |
| Update-Only | #5 | `Fixture.settingsCategories.updateOnlyExcess` (`updateOnly_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_UO_PASSWORD` |
| Create-Only | #4 | `Fixture.settingsCategories.createOnlyExcess` (`createOnly_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_CO_PASSWORD` |
| Create-Update-Delete | #7 | `Fixture.settingsCategories.createUpdateDeleteExcess` (`createUpdateDelete_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_CUD_PASSWORD` |
| Read Only | #2 | `Fixture.settingsCategories.readOnlyExcess` (`readOnly_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_RO_PASSWORD` |
| Group Manager Capability CRUD | #9 | `Fixture.settingsCategories.gmCapabilityExcess` (`gmCapability_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_GMCAP_PASSWORD` |

- Login di hook `before` spec ini sebagai Total Control di client CatExcess; halaman dibuka hook `beforeEach` suite. Ganti akun ke role lain memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, client CatMain).
- Env var `FA_TC_PASSWORD`, `FA_DO_PASSWORD`, `FA_UO_PASSWORD`, `FA_CO_PASSWORD`, `FA_CUD_PASSWORD`, `FA_RO_PASSWORD`, dan `FA_GMCAP_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim). Satu nama satu arti: password akun role tersebut di semua client Categories.
- Data Pre-setup: client CatExcess (Pre-setup #31: plan Starter setelah downgrade, cap 5, T-0 sudah lewat, 9 kategori; node Excess `Heavy Equipment`; jumlah kategori melebihi cap sehingga Alert Category Consolidation tampil untuk Total Control). Spec hanya membaca; tidak ada data yang dibuat.
- Seed client CatExcess dan pemulihannya lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-50: Menu row action node Excess untuk aktor Total Control

1. Klik elipsis (⋯) pada baris `Heavy Equipment`
2. Verifikasi menu memuat Detail dan Delete
3. Verifikasi Edit dan + Add Subcategory Hidden (CRU Lock) terlepas dari capability aktor

### TC-FA-CAT-51: Menu row action node Excess untuk aktor Delete-Only

4. Ganti akun: Logout, lalu login sebagai Delete-Only (Pre-setup #6) di client CatExcess
5. Buka Fixed Asset > Settings > Categories
6. Klik elipsis (⋯) pada baris `Heavy Equipment`
7. Verifikasi menu memuat Detail dan Delete
8. Verifikasi Edit dan + Add Subcategory Hidden (CRU Lock) terlepas dari capability aktor

### TC-FA-CAT-52: Menu row action node Excess untuk aktor Update-Only

9. Ganti akun: Logout, lalu login sebagai Update-Only (Pre-setup #5) di client CatExcess
10. Buka Fixed Asset > Settings > Categories
11. Klik elipsis (⋯) pada baris `Heavy Equipment`
12. Verifikasi menu memuat Detail saja
13. Verifikasi Edit dan + Add Subcategory Hidden (CRU Lock) terlepas dari capability aktor

### TC-FA-CAT-53: Menu row action node Excess untuk aktor Create-Only

14. Ganti akun: Logout, lalu login sebagai Create-Only (Pre-setup #4) di client CatExcess
15. Buka Fixed Asset > Settings > Categories
16. Klik elipsis (⋯) pada baris `Heavy Equipment`
17. Verifikasi menu memuat Detail saja
18. Verifikasi Edit dan + Add Subcategory Hidden (CRU Lock) terlepas dari capability aktor

### TC-FA-CAT-54: Alert Category Consolidation Hidden untuk aktor non-Total Control saat count melebihi cap

19. Ganti akun: Logout, lalu login sebagai Create-Update-Delete (Pre-setup #7) di client CatExcess
20. Buka Fixed Asset > Settings > Categories
21. Verifikasi Category Context Header tampil
22. Verifikasi Alert dan tombol `[Choose Categories]` tidak dirender untuk aktor Create-Update-Delete
23. Klik elipsis (⋯) pada baris `Heavy Equipment`
24. Verifikasi aktor tetap dapat Detail dan Delete pada node Excess: menu memuat Detail dan Delete

### TC-FA-CAT-55: Alert Category Consolidation Hidden untuk Read Only saat count melebihi cap

25. Ganti akun: Logout, lalu login sebagai Read Only (Pre-setup #2) di client CatExcess
26. Buka Fixed Asset > Settings > Categories
27. Verifikasi Category Context Header tampil
28. Verifikasi Alert dan tombol `[Choose Categories]` tidak dirender untuk Read Only

### TC-FA-CAT-56: Group Manager pemegang capability CRUD tidak melihat Alert Consolidation

29. Ganti akun: Logout, lalu login sebagai Group Manager Capability CRUD (Pre-setup #9) di client CatExcess
30. Buka Fixed Asset > Settings > Categories
31. Verifikasi Category Context Header tampil
32. Verifikasi Alert Category Consolidation Hidden karena entry point Wizard hanya untuk Total Control

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role dengan langkah ganti akun eksplisit (bagian 3a, KEPUTUSAN 2026-10-30): akun pertama (Total Control) login di hook `before`; tiap blok berikutnya diawali langkah ganti akun dan langkah membuka halaman.
- Spec memuat polaritas positif (menu memuat Detail dan Delete) dan negatif (Hidden) dalam satu matriks visibilitas per role; title tanpa kata Positif atau Negatif (bagian 3a).
- Langkah penghubung (S-03): langkah 4, 5, 9, 10, 14, 15, 19, 20, 25, 26, 29, dan 30 (ganti akun dan buka halaman). Langkah 21, 27, dan 31 (Category Context Header tampil) adalah anchor permukaan untuk asersi Hidden berikutnya (8b butir 2); TC tidak menulisnya sebagai Expected.
- Langkah 23 (klik elipsis `Heavy Equipment` untuk TC-FA-CAT-54) ditambahkan karena Expected b meminta Detail dan Delete pada node Excess tetapi Langkah Uji TC hanya membuka halaman.
- Baris `Heavy Equipment` hanya dibuka menunya dan tidak diubah (S-06).
- Temuan untuk QA:
  - TC-FA-CAT-53 pada kolom ACC hanya menulis role Create-Only tanpa nomor Pre-setup; spec memakai Pre-setup #4 (Create-Only).
  - TC-FA-CAT-50 sampai TC-FA-CAT-56 tidak menyebut email akun per client CatExcess; spec menulis email dengan `{namaCompany}` CatExcess ("ditetapkan tim FE") dan password per role.
  - TC-FA-CAT-54 Expected a hanya menyebut aktor Create-Update-Delete tidak melihat Alert; TC tidak menyebut apakah Alert tampil untuk Total Control di client yang sama sebagai pembanding (prasyarat Pre-setup #31 menyatakannya).
