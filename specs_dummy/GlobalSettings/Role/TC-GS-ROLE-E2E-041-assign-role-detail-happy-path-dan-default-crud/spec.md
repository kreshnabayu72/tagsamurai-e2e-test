---
id: TC-GS-ROLE-E2E-041-assign-role-detail-happy-path-dan-default-crud
title: "Penugasan Role pada Detail Berhasil: Nilai Default CRUD (Read Aktif), Eksekusi Aktor MUR, dan Refleksi Rename User"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-94
  - TC-GS-ROLE-95
  - TC-GS-ROLE-96
  - TC-GS-ROLE-100
coverage:
  web: automated
---

# Penugasan Role pada Detail Berhasil: Nilai Default CRUD (Read Aktif), Eksekusi Aktor MUR, dan Refleksi Rename User

## Prerequisites

- Login sebagai Total Control lalu Hendra Wijaya (MUR Update)
- Data Uji: Wawan Setiawan & Nina Kartika (Dinamis #5), Tari Anjani (Dinamis #12)
- Setup Hook: beforeEach: switchActor()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- User berada di Global Settings > Role & Permission > System > Detail "Import data"
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)
- User berada di Global Settings > Role & Permission > System > Detail "Manage files"
- Eko Prasetyo login di sesi B

## Test Steps

### Assign Role Manage TAG ke beberapa user oleh Total Control (TC-GS-ROLE-94)

1. Klik [+ Assign]
2. Centang Wawan Setiawan dan Nina Kartika
3. Klik [Assign]
4. Buka Tab System
5. Verifikasi Muncul toast sukses: "Success, role has been assigned."
6. Verifikasi Dua baris baru di Detail: Read checked dan disabled, Update unchecked
7. Verifikasi Tidak ada kolom Create/Delete
8. Verifikasi Tab System: Users "Manage TAG" bertambah 2

### Assign Role Import data — baris baru Read aktif, Create unchecked (TC-GS-ROLE-95)

9. Klik [+ Assign]
10. Centang Wawan Setiawan
11. Klik [Assign]
12. Verifikasi Toast sukses: "Success, role has been assigned."
13. Verifikasi Baris Wawan Setiawan: Create unchecked (enabled), Read checked dan disabled

### Assign Role oleh aktor Manage user and role dengan Update (TC-GS-ROLE-96)

14. Klik [+ Assign]
15. Amati pool
16. Centang Nina Kartika
17. Klik [Assign]
18. Verifikasi Hendra Wijaya tidak ada di pool
19. Verifikasi Toast sukses: "Success, role has been assigned."
20. Verifikasi Baris Nina Kartika tampil: Read checked, Delete unchecked

### Assign Role saat user terpilih di-rename sebelum submit (TC-GS-ROLE-100)

21. Sesi A: Detail "Manage hardware" > [+ Assign] > centang Tari Anjani
22. Sesi B: rename Tari Anjani menjadi Tari Anjana
23. Sesi A: klik [Assign]
24. Verifikasi Toast sukses: "Success, role has been assigned."
25. Verifikasi Detail menampilkan "Tari Anjana"

## Notes

- Memvalidasi alur skenario "Penugasan Role pada Detail Berhasil: Nilai Default CRUD (Read Aktif), Eksekusi Aktor MUR, dan Refleksi Rename User".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.2 [F-ROLE-03]; global-settings/role/PRD/role.md §7.1 T-06; global-settings/role/PRD/role.md §4.2 Page: Detail; global-settings/role/PRD/role.md §4.2 Page: Detail [+ Assign]; global-settings/role/PRD/role.md ROLE-LOGIC-05; global-settings/role/PRD/role.md §2.3; global-settings/role/PRD/role.md §6 V-13.
- Sumber pemetaan test case granular: TC-GS-ROLE-94, TC-GS-ROLE-95, TC-GS-ROLE-96, TC-GS-ROLE-100.
