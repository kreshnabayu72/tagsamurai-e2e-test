---
id: TC-GS-ROLE-E2E-072-tabel-detail-setup-kolom-kunci-crud-dan-download
title: "Tabel Halaman Detail: Setup Kolom dengan Penguncian Kolom CRUD Dinamis dan Download Format Spesifik Title-Case-hyphen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-192
  - TC-GS-ROLE-193
  - TC-GS-ROLE-194
  - TC-GS-ROLE-303
coverage:
  web: automated
---

# Tabel Halaman Detail: Setup Kolom dengan Penguncian Kolom CRUD Dinamis dan Download Format Spesifik Title-Case-hyphen

## Prerequisites

- Login sebagai Total Control
- Data Uji: Detail Manage user and role
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Detail berisi ≥4 user dengan Position/Division berbeda
- User berada di Global Settings > Role & Permission > System > Detail "Manage user and role"

## Test Steps

### Setup Column Detail — kolom CRUD dinamis (TC-GS-ROLE-192)

1. Klik header (⋯)
2. Amati checkbox kolom Read dan Update di overlay/popup
3. Verifikasi Overlay dan popup Setup Column hanya mendaftar Name, Position, Division, Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]
4. Verifikasi Kolom CRUD (Read, Update) tidak tercantum sehingga tidak bisa di-hide, di-drag, maupun di-pin
5. Verifikasi Setelah menyembunyikan Position, Division, Activation Status, Temporary User, Temporary Until, TAG, dan [Custom Field aktif], kolom Read dan Update tetap tampil di tabel

### Setup Column Detail — hide/show kolom Name, Position, Division, dan kolom kurasi (TC-GS-ROLE-193)

6. Popup Setup Column: uncheck Position dan Division, check Activation Status, Temporary User, Temporary Until, TAG
7. Save
8. F5
9. Verifikasi Position dan Division tersembunyi
10. Verifikasi Activation Status, Temporary User, Temporary Until, TAG tampil
11. Verifikasi Bertahan setelah F5

### Download Detail sebagai CSV dan XLSX (TC-GS-ROLE-194)

12. Download > "Download as CSV"
13. Download > "Download as XLSX"
14. Verifikasi File "Role-Permission-Manage-TAG.csv" dan "Role-Permission-Manage-TAG.xlsx"
15. Verifikasi Tidak ada toast sukses
16. Verifikasi Kolom Read dan Update di file bernilai "Yes" (checked) atau "No" (unchecked)

### Download Detail "Manage user and role" memakai nama file Title-Case-hyphen (TC-GS-ROLE-303)

17. Download > "Download as CSV"
18. Download > "Download as XLSX"
19. Verifikasi File "Role-Permission-Manage-User-And-Role.csv" dan "Role-Permission-Manage-User-And-Role.xlsx" (nama role Title-Case dipisah hyphen)
20. Verifikasi Tidak ada toast sukses

## Notes

- Memvalidasi alur skenario "Tabel Halaman Detail: Setup Kolom dengan Penguncian Kolom CRUD Dinamis dan Download Format Spesifik Title-Case-hyphen".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.4; global-settings/role/PRD/role.md §4.2 Page: Detail; global-settings/role/PRD/role.md §4.1 Filename Download; global-settings/role/PRD/role.md §5 Download; foundation/process/prd-process/prd-conventions.md §9.9.
- Sumber pemetaan test case granular: TC-GS-ROLE-192, TC-GS-ROLE-193, TC-GS-ROLE-194, TC-GS-ROLE-303.
