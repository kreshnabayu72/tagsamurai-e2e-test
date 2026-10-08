---
id: TC-GS-ROLE-E2E-080-sync-sidebar-akses-menu-realtime-pasca-mutasi
title: "Sinkronisasi Seketika Akses Menu Sidebar Global Settings Setelah Penugasan dan Pencabutan Role/Akses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-226
  - TC-GS-ROLE-227
  - TC-GS-ROLE-228
  - TC-GS-ROLE-229
  - TC-GS-ROLE-230
coverage:
  web: automated
---

# Sinkronisasi Seketika Akses Menu Sidebar Global Settings Setelah Penugasan dan Pencabutan Role/Akses

## Prerequisites

- Dual session context (Sesi admin dan sesi target user)
- Data Uji: Pre-setup #9 (Agus Salim), Pre-setup #10 (Doni Pratama)
- Setup Hook: dualContext: sessionAdmin, sessionUser
- Wawan Setiawan login di sesi B tanpa menu TAG
- Login sbg Role: Total Control di sesi A
- Doni Pratama login di sesi B
- Doni Pratama login di sesi B, Manage files Read saja
- Sari Wulandari login di sesi B
- Sari Wulandari (Total Control) login di sesi B

## Test Steps

### Assign Role membuka menu modul untuk target pada request berikutnya (TC-GS-ROLE-226)

1. Sesi A: Detail "Manage TAG" > [+ Assign] > Wawan Setiawan > [Assign]
2. Sesi B: reload halaman tanpa logout
3. Verifikasi Sesi B: menu TAG tampil
4. Verifikasi Menu Role & Permission tidak tampil

### Remove baris role menyembunyikan menu modul target (TC-GS-ROLE-227)

5. Sesi A: Remove baris Manage TAG Doni Pratama
6. Sesi B: reload
7. Verifikasi Menu TAG tidak tampil
8. Verifikasi Menu File Manager (masih Manage files Read) tetap tampil

### Edit CRUD berlaku pada request berikutnya tanpa logout (TC-GS-ROLE-228)

9. Sesi B: buka File Manager, amati aksi hapus
10. Sesi A: centang Delete Manage files Doni Pratama
11. Sesi B: reload File Manager
12. Verifikasi Langkah 1: aksi hapus file tidak tersedia
13. Verifikasi Langkah 3: aksi hapus file tersedia

### Assign Total Control menampilkan General Settings dan Activity Log untuk target (TC-GS-ROLE-229)

14. Sesi A (Total Control): assign Total Control ke Sari Wulandari
15. Sesi B: reload
16. Verifikasi Sidebar Sari Wulandari memuat User, Role & Permission, Import, TAG, Hardware, Brand, Measurement, File Manager, General Settings, Activity Log

### Remove Total Control mengosongkan sidebar target (TC-GS-ROLE-230)

17. Sesi A: Remove Total Control Sari Wulandari
18. Sesi B: reload
19. Verifikasi Sidebar Global Settings kosong
20. Verifikasi Pesan "You don't have access to any menu yet."

## Notes

- Memvalidasi alur skenario "Sinkronisasi Seketika Akses Menu Sidebar Global Settings Setelah Penugasan dan Pencabutan Role/Akses".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.2 [F-ROLE-08]; global-settings/role/PRD/role.md §9.7; global-settings/role/PRD/role.md §9.2 [F-ROLE-03]; global-settings/role/PRD/role.md §2.1; global-settings/role/PRD/role.md §10.1.
- Sumber pemetaan test case granular: TC-GS-ROLE-226, TC-GS-ROLE-227, TC-GS-ROLE-228, TC-GS-ROLE-229, TC-GS-ROLE-230.
