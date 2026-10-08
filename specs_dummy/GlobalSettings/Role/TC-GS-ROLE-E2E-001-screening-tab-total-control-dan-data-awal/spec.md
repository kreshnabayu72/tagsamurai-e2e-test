---
id: TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-data-awal
title: "Screening Halaman Role & Permission Tab Total Control, Default Sort Name A-Z, dan Nilai Baris Default User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-1
  - TC-GS-ROLE-10
  - TC-GS-ROLE-20
  - TC-GS-ROLE-24
coverage:
  web: automated
---

# Screening Halaman Role & Permission Tab Total Control, Default Sort Name A-Z, dan Nilai Baris Default User

## Prerequisites

- Login sebagai Role: Total Control (Ahmad Fauzi)
- Data Uji: Pre-setup #1, #2, #3, #15 (Ahmad Fauzi, Budi Santoso, Dewi Lestari, Raden Mas Bagus)
- Setup Hook: before: seedSession Total Control; beforeEach: navigateTo(Role & Permission > Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup #1–#4 tersedia (Default User, TC Dewi Lestari Inactive)
- User berada di Global Settings > Role & Permission > Total Control
- Pre-setup #1–#3 tersedia
- Client uji hanya memiliki Default User sebagai Total Control dan Default User sebagai satu-satunya pemegang baris "Import data" (Pre-setup #14)
- User TC dengan nama 60 karakter tanpa foto (Pre-setup #15)

## Test Steps

### Screening halaman Role & Permission Tab Total Control (web) (TC-GS-ROLE-1)

1. Klik menu sidebar Role & Permission
2. Pastikan Tab Total Control aktif
3. Screening halaman dari atas ke bawah
4. Verifikasi **Header**:
5. Verifikasi Breadcrumb (pola "Role & Permission > Tab aktif"): "Role & Permission > Total Control"; segmen "Total Control" bukan link, berada di luar SectionCard
6. Verifikasi Tab: `Total Control (aktif) | Read Only | System`
7. Verifikasi Table Tools (rata kanan): `Search | Filter | Download | Changelog | [+ Assign]` ([+ Assign] primary)
8. Verifikasi Section description: "Total Control applies to Global Settings only — it does not grant access to other TAG Samurai products."
9. Verifikasi **Body**:
10. Verifikasi Kolom: `Name (sortable) | Position (sortable) | Division (sortable) | Status (sortable) | Modified By (sortable) | Last Updated (sortable) | Actions (⋯) (unsortable — header klik = buka overlay Column Visibility → CTA [Setup Column] di dalamnya, body per baris = row action Remove)`
11. Verifikasi Kolom Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field aktif tidak tampil (default Hidden)
12. Verifikasi Tidak ada kolom checkbox seleksi baris dan tidak ada kolom CRUD
13. Verifikasi **Footer**: Pagination default 10 baris/halaman

### Default sort Tab Total Control dan posisi baris Default User (TC-GS-ROLE-10)

14. Amati urutan baris tanpa menyentuh sort
15. Amati baris Budi Santoso
16. Verifikasi Baris terurut Name A-Z (Ahmad Fauzi, Budi Santoso, Dewi Lestari)
17. Verifikasi Baris Budi Santoso (Default User): Position "—", Division "—", Status "Active", Modified By "—", Last Updated "—"

### Tab Total Control dan Detail tidak pernah kosong (TC-GS-ROLE-20)

18. Buka Tab Total Control
19. Buka Detail "Import data"
20. Verifikasi Tab Total Control menampilkan 1 baris Budi Santoso (Default User), tidak ada empty state
21. Verifikasi Detail "Import data" menampilkan 1 baris Budi Santoso

### Name panjang tidak terpotong dan avatar placeholder (TC-GS-ROLE-24)

22. Amati sel Name user tersebut
23. Verifikasi Nama tampil utuh tanpa ".." dan kolom melebar mengikuti konten
24. Verifikasi Avatar circle placeholder generik tampil di kiri nama

## Notes

- Memvalidasi alur skenario "Screening Halaman Role & Permission Tab Total Control, Default Sort Name A-Z, dan Nilai Baris Default User".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Tab: Total Control; global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §5; foundation/process/prd-process/prd-conventions.md §27.1; foundation/process/prd-process/prd-conventions.md §31.2; global-settings/role/PRD/role.md §9.5; global-settings/role/PRD/role.md §7.1 S-07; global-settings/role/PRD/role.md §7.1 S-09; global-settings/role/PRD/role.md §4.1.1 Name; foundation/process/prd-process/prd-conventions.md §9.12a.
- Sumber pemetaan test case granular: TC-GS-ROLE-1, TC-GS-ROLE-10, TC-GS-ROLE-20, TC-GS-ROLE-24.
