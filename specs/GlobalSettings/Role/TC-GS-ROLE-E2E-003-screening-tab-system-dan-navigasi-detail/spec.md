---
id: TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail
title: "Screening Tab System, 6 Role Alfabetis, Hitungan Users, Hover Link, dan Navigasi Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-3
  - TC-GS-ROLE-6
  - TC-GS-ROLE-7
  - TC-GS-ROLE-8
  - TC-GS-ROLE-9
  - TC-GS-ROLE-14
coverage:
  web: automated
---

# Screening Tab System, 6 Role Alfabetis, Hitungan Users, Hover Link, dan Navigasi Detail

## Prerequisites

- Login sebagai Role: Total Control (Ahmad Fauzi)
- Data Uji: 6 system roles katalog, baris Default User & pemegang role Manage TAG
- Setup Hook: beforeEach: navigateTo(Role & Permission > System)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia
- User berada di Global Settings > Role & Permission > System
- Hitung pemegang baris "Manage TAG" dari Detail-nya (termasuk Default User, TC, RO)

## Test Steps

### Screening halaman Role & Permission Tab System (web) (TC-GS-ROLE-3)

1. Buka Global Settings > Role & Permission
2. Klik Tab System
3. Screening halaman dari atas ke bawah
4. Verifikasi **Header**:
5. Verifikasi Breadcrumb: "Role & Permission > System"; segmen "System" bukan link
6. Verifikasi Tab: `Total Control | Read Only | System (aktif)`
7. Verifikasi Table Tools: `Search | Download | Changelog` — tidak ada Filter dan tidak ada [+ Assign]
8. Verifikasi **Body**:
9. Verifikasi Kolom: `Role Name (unsortable) | Users (unsortable) | Actions (⋯) (unsortable — header = overlay Column Visibility, body = row action Detail)`
10. Verifikasi Urutan baris tetap: Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role
11. Verifikasi Role Name tampil sebagai text link; kolom Users angka bulat tanpa pemisah ribuan, setiap baris ≥1
12. Verifikasi **Footer**: Pagination

### Buka Detail lewat klik Role Name di Tab System (TC-GS-ROLE-6)

13. Klik text link Role Name "Manage TAG"
14. Verifikasi Halaman Detail "Manage TAG" terbuka sebagai full page (bukan modal)
15. Verifikasi Breadcrumb "Role & Permission > System > Detail"

### Buka Detail lewat row action Detail di Tab System (TC-GS-ROLE-7)

16. Klik (⋯) pada baris "Manage TAG"
17. Screening overlay row action
18. Klik Detail
19. Verifikasi Overlay row action hanya berisi `Detail` dengan icon FileInfoLine (severity dark)
20. Verifikasi Halaman Detail "Manage TAG" terbuka, sama dengan jalur klik Role Name

### Kembali dari Detail ke Tab System lewat breadcrumb (TC-GS-ROLE-8)

21. Klik Role Name "Manage files"
22. Klik segmen breadcrumb "System"
23. Verifikasi Kembali ke Tab System, Tab System aktif
24. Verifikasi Breadcrumb "Role & Permission > System"

### Hover Role Name di Tab System (TC-GS-ROLE-9)

25. Arahkan kursor ke Role Name "Import data"
26. Pindahkan kursor keluar
27. Verifikasi Saat hover warna teks berubah ke warna primary Global Settings (hitam/kontras) tanpa underline
28. Verifikasi Setelah kursor keluar warna kembali ke body text

### Kolom Users Tab System menghitung semua pemegang baris termasuk TC/RO (TC-GS-ROLE-14)

29. Buka Detail "Manage TAG", catat total baris pada info pagination
30. Kembali ke Tab System
31. Bandingkan angka kolom Users "Manage TAG"
32. Verifikasi Angka Users "Manage TAG" sama dengan total baris Detail "Manage TAG"
33. Verifikasi Hitungan memuat Default User, user Total Control, dan user Read Only
34. Verifikasi Tidak ada baris role dengan Users 0

## Notes

- Memvalidasi alur skenario "Screening Tab System, 6 Role Alfabetis, Hitungan Users, Hover Link, dan Navigasi Detail".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Tab: System; global-settings/role/PRD/role.md §4.1.3; global-settings/role/PRD/role.md §2.1; global-settings/role/PRD/role.md §5; global-settings/role/PRD/role.md §4.8 Row actions Detail; global-settings/role/PRD/role.md §4.1 Row Actions per halaman; global-settings/role/PRD/role.md §4.8; global-settings/role/PRD/role.md §4.2 Page: Detail; foundation/process/prd-process/prd-conventions.md §9.2c; global-settings/role/PRD/role.md §4.1.3 Users; global-settings/role/PRD/role.md §9.2 [F-ROLE-02].
- Sumber pemetaan test case granular: TC-GS-ROLE-3, TC-GS-ROLE-6, TC-GS-ROLE-7, TC-GS-ROLE-8, TC-GS-ROLE-9, TC-GS-ROLE-14.
