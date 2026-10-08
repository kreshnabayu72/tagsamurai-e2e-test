---
id: TC-GS-ROLE-E2E-075-modal-changelog-setup-kolom-download-dan-resilience
title: "Modal Changelog: Preferensi Setup Kolom, Download 4 Varian CSV/XLSX, dan Ketahanan Error Server 500"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-203
  - TC-GS-ROLE-204
  - TC-GS-ROLE-205
coverage:
  web: automated
---

# Modal Changelog: Preferensi Setup Kolom, Download 4 Varian CSV/XLSX, dan Ketahanan Error Server 500

## Prerequisites

- Login sebagai Total Control; intercept error 500
- Data Uji: Dataset Changelog
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: openChangelogModal()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Changelog Tab Total Control berisi entry
- Keempat changelog berisi entry
- Response Download Changelog dibuat gagal 5xx

## Test Steps

### Setup Column Modal Changelog (TC-GS-ROLE-203)

1. Klik header (⋯) di modal
2. [Setup Column]: uncheck Field > Save
3. Tutup lalu buka modal lagi
4. Reset to Default > Save
5. Verifikasi Overlay: Date, Action, User Name, Field, Old Value, New Value, Modified By checked & enabled (varian System/Detail: Role — User menggantikan User Name)
6. Verifikasi Field tersembunyi dan tetap tersembunyi saat modal dibuka lagi
7. Verifikasi Reset mengembalikan tujuh kolom
8. Verifikasi Setup Column Tab Total Control (tabel utama) tidak berubah

### Download Modal Changelog per varian (TC-GS-ROLE-204)

9. Download CSV dari Changelog Tab Total Control, Read Only, System, Detail "Manage TAG"
10. Download XLSX dari Changelog Tab Total Control
11. Verifikasi "Changelog-Role-Permission-Total-Control.csv"
12. Verifikasi "Changelog-Role-Permission-Read-Only.csv"
13. Verifikasi "Changelog-Role-Permission-System.csv"
14. Verifikasi "Changelog-Role-Permission-Manage-TAG.csv"
15. Verifikasi "Changelog-Role-Permission-Total-Control.xlsx"
16. Verifikasi Tidak ada toast sukses

### Download Modal Changelog gagal (TC-GS-ROLE-205)

17. Changelog Tab Total Control > Download CSV
18. Verifikasi Muncul toast error: "Error, failed to download Changelog-Role-Permission-Total-Control."
19. Verifikasi Tidak ada file terunduh

## Notes

- Memvalidasi alur skenario "Modal Changelog: Preferensi Setup Kolom, Download 4 Varian CSV/XLSX, dan Ketahanan Error Server 500".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Modal: Changelog; global-settings/role/PRD/role.md §4.1.6; foundation/process/prd-process/prd-conventions.md §9.10; global-settings/role/PRD/role.md §4.1 Filename Download; global-settings/role/PRD/role.md §5 Download; foundation/process/prd-process/prd-conventions.md §9.9; global-settings/role/PRD/role.md §6 V-15; foundation/process/prd-process/prd-conventions.md §7.
- Sumber pemetaan test case granular: TC-GS-ROLE-203, TC-GS-ROLE-204, TC-GS-ROLE-205.
