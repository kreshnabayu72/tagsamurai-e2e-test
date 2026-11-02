---
id: TC-FA-GRP-E2E-273-tab-assets-ketersediaan-kolom-setup-column-per-hak-aktor
title: "Tab Assets Ketersediaan Kolom di Setup Column per Hak Aktor: View Asset Value, Manage Purchase, Manage Accounting, dan Tanpa Hak Bergerbang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1240
  - TC-FA-GRP-1241
  - TC-FA-GRP-1242
  - TC-FA-GRP-1243
coverage:
  web: automated
---

# Tab Assets Ketersediaan Kolom di Setup Column per Hak Aktor: View Asset Value, Manage Purchase, Manage Accounting, dan Tanpa Hak Bergerbang

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Role yang diuji (langkah beda per role sehingga ditulis per blok role dengan Ganti akun eksplisit):

| Role | Akun | Env password |
|---|---|---|
| viewAssetValueGroups (Pre-setup No 12: Group Role View asset value pada Value Gate Node A) | `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD` |
| managePurchaseGroups (No 14: Group Role Manage purchase pada Value Gate Node A saja) | `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD` |
| manageAccountingGroups (No 13: Global Role Manage accounting, lisensi FA-7 aktif) | `manageAccountingGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GRP_MANAGEACCOUNTING_PASSWORD` |
| noValueAccess (No 16: tanpa View asset value, Manage purchase, maupun Manage accounting) | `noValueAccess_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD` |

- Login akun pertama (viewAssetValueGroups) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup tambahan (hanya dibaca): Value Gate Node A (Tabel Dinamis No 10, G1-G6) dan Value Gate Node B (No 11); custom field Tabel Dinamis No 13: Cost Center dan Insurance Policy (General), PO Number dan Purchase Date (Purchasing), Cost Account (Accounting). Node di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-273` (mekanisme seeding disediakan tim FE/BE). Langkah dan asersi memakai nama bersuffix itu.
- Penyebutan `Asset Value` pada TC tanpa nama buku berarti kolom `Asset Value (Commercial)` (Catatan TC).
- Setup Column: spec hanya membaca daftar; tidak ada konfigurasi disimpan.
- State global: tidak ada yang diubah.

## Test Steps

### TC-1240: Pemegang View asset value
1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column
3. Verifikasi Asset Value dan Warranty Expiry tersedia
4. Verifikasi Cost Center dan Insurance Policy (General) tersedia
5. Verifikasi PO Number, Purchase Date (Purchasing), dan Cost Account (Accounting) tidak ada di daftar
6. Tutup Popup Setup Column
### TC-1241: Pemegang Manage purchase (>=1 group)
7. Ganti akun: Logout, login sebagai managePurchaseGroups (`managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`), buka Fixed Asset > Settings > Groups
8. Buka Detail Value Gate Node A (Tab Assets)
9. Buka Popup Setup Column
10. Verifikasi Asset Value, Warranty Expiry, Cost Center, Insurance Policy, PO Number, dan Purchase Date tersedia
11. Verifikasi Cost Account (Accounting) tidak ada di daftar
12. Tutup popup; buka Detail Value Gate Node B, buka Popup Setup Column
13. Verifikasi kolom Purchasing (PO Number dan Purchase Date) tetap tersedia pada Value Gate Node B karena aktor memegang Manage purchase di >=1 group
14. Tutup Popup Setup Column
### TC-1242: Pemegang Manage accounting
15. Ganti akun: Logout, login sebagai manageAccountingGroups (`manageAccountingGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_MANAGEACCOUNTING_PASSWORD`), buka Fixed Asset > Settings > Groups
16. Buka Detail Value Gate Node A (Tab Assets)
17. Buka Popup Setup Column
18. Verifikasi Asset Value, Warranty Expiry, Cost Center, Insurance Policy, dan Cost Account tersedia
19. Verifikasi PO Number dan Purchase Date (Purchasing) tidak ada di daftar
20. Tutup Popup Setup Column
### TC-1243: Aktor tanpa hak bergerbang
21. Ganti akun: Logout, login sebagai noValueAccess (`noValueAccess_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`), buka Fixed Asset > Settings > Groups
22. Buka Detail Value Gate Node A (Tab Assets)
23. Buka Popup Setup Column
24. Verifikasi Asset Value dan Warranty Expiry tersedia
25. Verifikasi Cost Center dan Insurance Policy tersedia
26. Verifikasi PO Number, Purchase Date, dan Cost Account tidak ada di daftar
27. Tutup Popup Setup Column

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix per blok role: langkah tiap role berbeda (daftar kolom berbeda) dan Ganti akun menuntut Step eksplisit sehingga akun pertama login di hook `before` (bagian 3a). Bagian sesudah tiap Ganti akun tetap bermakna walau bagian sebelumnya gagal keras.
- Langkah penghubung (S-03): "Tutup Popup Setup Column" di akhir tiap blok dan tutup popup sebelum membuka Value Gate Node B (TC-1241); empat langkah Ganti akun (tiga di antaranya antar blok).
- Temuan untuk QA:
  - TC-1243 Expected a menulis Warranty "tetap ada bagi semua pemanggil; selnya `No access`" tetapi kolom hanya diamati di Popup Setup Column, tanpa langkah yang membuka kolom; sel `No access` pada aktor ini diuji di spec 275, sehingga tidak diasersi di sini.
  - TC-1240 Expected b menulis "Cost Center dan Insurance Policy (General) tersedia" sedangkan TC-1243 memakai kalimat yang sama untuk aktor tanpa hak; konsisten dengan custom field General tidak bergerbang.
