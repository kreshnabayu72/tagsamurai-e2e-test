---
id: TC-GS-ROLE-E2E-021-assign-total-control-picker-screening-dan-pool-eligibility
title: "Screening Modal Table User Picker Assign Total Control, Kelayakan Pool, dan Ketiadaan Column Visibility"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-51
  - TC-GS-ROLE-52
  - TC-GS-ROLE-53
  - TC-GS-ROLE-54
  - TC-GS-ROLE-76
coverage:
  web: automated
---

# Screening Modal Table User Picker Assign Total Control, Kelayakan Pool, dan Ketiadaan Column Visibility

## Prerequisites

- Login sebagai Total Control (Ahmad Fauzi)
- Data Uji: Pre-setup #1, #3, #11, #12 (Tono Wibowo)
- Setup Hook: beforeEach: openModalAssignTC()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Kandidat Pre-setup #11 tersedia
- Pre-setup #1–#12 tersedia

## Test Steps

### Screening Popup Assign Total Control (TC-GS-ROLE-51)

1. Klik [+ Assign]
2. Screening popup dari atas ke bawah
3. Verifikasi **Header**: Title "Assign Total Control"
4. Verifikasi **Toolbar**: `Search | Filter`; placeholder Search "Search..."
5. Verifikasi **Body**:
6. Verifikasi Kolom: `Checkbox (header = select all halaman) | Name (sortable) | Email (sortable) | Position (sortable) | Division (sortable) | Status (sortable)`
7. Verifikasi Baris terurut Name A-Z
8. Verifikasi Status tampil badge Active/Inactive
9. Verifikasi **Footer**:
10. Verifikasi Pagination picker sendiri
11. Verifikasi `[Cancel]` (text, contrast) | `[Assign]` (filled, primary, enabled walau 0 terpilih)

### Pool Popup Assign Total Control (TC-GS-ROLE-52)

12. Klik [+ Assign]
13. Amati daftar user di picker (semua halaman)
14. Verifikasi Tampil: Sari Wulandari (Active), Maya Anggraini (Inactive), Rudi Hartono (Pending Activation), Siti Nurhaliza (Read Only), Hendra Wijaya, Doni Pratama
15. Verifikasi Tidak tampil: Ahmad Fauzi, Budi Santoso, Dewi Lestari (sudah Total Control)
16. Verifikasi Tidak tampil: Tono Wibowo (Access Global Settings tidak dicentang)

### Picker menampilkan dua user bernama sama yang dibedakan Email dan Position (TC-GS-ROLE-53)

17. Klik [+ Assign]
18. Amati baris Ahmad Fauzan
19. Verifikasi Dua baris "Ahmad Fauzan": ahmad.fz@client.com / IT Staff / IT dan ahmad.fauzan@client.com / Warehouse Staff / Logistics

### Submit Assign Total Control tanpa memilih user (TC-GS-ROLE-54)

20. Klik [+ Assign]
21. Klik [Assign] tanpa mencentang user
22. Verifikasi Teks error inline "You must pick a user" (danger) rata kanan, 4px di atas tombol footer
23. Verifikasi Popup tetap terbuka, tidak ada dialog, tidak ada toast
24. Verifikasi Tidak ada user yang ter-assign

### Column Visibility / Setup Column pada Popup Assign (TC-GS-ROLE-76)

25. Klik [+ Assign]
26. Cari trigger Column Visibility (⋯) di header tabel picker
27. Verifikasi Header tabel picker tidak memiliki trigger Column Visibility (⋯) dan tidak ada tombol [Setup Column]
28. Verifikasi Kolom tetap Checkbox | Name | Email | Position | Division | Status

## Notes

- Memvalidasi alur skenario "Screening Modal Table User Picker Assign Total Control, Kelayakan Pool, dan Ketiadaan Column Visibility".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Popup: Table User Picker; global-settings/role/PRD/role.md §4.1.5; foundation/process/prd-process/prd-conventions.md §37; global-settings/role/PRD/role.md ROLE-LOGIC-06a; global-settings/role/PRD/role.md ROLE-LOGIC-06b; global-settings/role/PRD/role.md §4.2; global-settings/role/PRD/role.md §4.1.5 Tabel Contoh Data; global-settings/role/PRD/role.md §6 V-09; foundation/process/prd-process/prd-conventions.md §37.2.
- Sumber pemetaan test case granular: TC-GS-ROLE-51, TC-GS-ROLE-52, TC-GS-ROLE-53, TC-GS-ROLE-54, TC-GS-ROLE-76.
