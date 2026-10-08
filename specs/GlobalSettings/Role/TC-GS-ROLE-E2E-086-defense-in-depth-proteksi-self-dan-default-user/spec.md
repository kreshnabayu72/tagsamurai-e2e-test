---
id: TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user
title: "Pertahanan Mendalam (Defense-in-Depth): Penolakan API 403 untuk Mutasi pada Akun Sendiri dan Default User"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-247
  - TC-GS-ROLE-248
  - TC-GS-ROLE-250
  - TC-GS-ROLE-251
  - TC-GS-ROLE-253
  - TC-GS-ROLE-254
  - TC-GS-ROLE-255
coverage:
  web: automated
---

# Pertahanan Mendalam (Defense-in-Depth): Penolakan API 403 untuk Mutasi pada Akun Sendiri dan Default User

## Prerequisites

- Login sebagai Total Control (Ahmad Fauzi); direct API mutation
- Data Uji: Ahmad Fauzi (Self) dan Budi Santoso (Default User)
- Setup Hook: beforeEach: callApiDirect()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Permintaan dikirim langsung (bypass UI) via test client yang memakai sesi aktor
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)

## Test Steps

### Edit CRUD diri sendiri lewat permintaan langsung ditolak (TC-GS-ROLE-247)

1. Kirim permintaan: Edit CRUD Manage TAG Update untuk Ahmad Fauzi
2. Reload halaman terkait di UI
3. Verifikasi Permintaan ditolak (403 Forbidden)
4. Verifikasi Detail "Manage TAG": nilai Ahmad Fauzi tidak berubah
5. Verifikasi Tidak ada entry log baru

### Edit CRUD Default User lewat permintaan langsung ditolak (TC-GS-ROLE-248)

6. Kirim permintaan: Edit CRUD Manage TAG Update untuk Budi Santoso
7. Reload halaman terkait di UI
8. Verifikasi Ditolak 403
9. Verifikasi Budi Santoso tetap di Tab Total Control dan nilainya tidak berubah (tidak ada auto-revert)

### Remove baris role Default User lewat permintaan langsung ditolak (TC-GS-ROLE-250)

10. Kirim permintaan: Remove baris Manage TAG milik Budi Santoso
11. Reload halaman terkait di UI
12. Verifikasi Ditolak 403
13. Verifikasi Baris Budi Santoso tetap ada

### Remove baris role diri sendiri lewat permintaan langsung ditolak (TC-GS-ROLE-251)

14. Kirim permintaan: Remove baris Manage user and role milik Hendra Wijaya
15. Reload halaman terkait di UI
16. Verifikasi Ditolak 403
17. Verifikasi Baris tetap ada

### Remove access level Default User lewat permintaan langsung ditolak (TC-GS-ROLE-253)

18. Kirim permintaan: Remove Total Control Budi Santoso
19. Reload halaman terkait di UI
20. Verifikasi Ditolak 403
21. Verifikasi Budi Santoso tetap di Tab Total Control

### Remove access level diri sendiri lewat permintaan langsung ditolak (TC-GS-ROLE-254)

22. Kirim permintaan: Remove Total Control Ahmad Fauzi
23. Reload halaman terkait di UI
24. Verifikasi Ditolak 403
25. Verifikasi Ahmad Fauzi tetap Total Control

### Assign Role ke diri sendiri lewat permintaan langsung ditolak (TC-GS-ROLE-255)

26. Kirim permintaan: Assign Role Manage TAG dengan user = Hendra Wijaya
27. Reload halaman terkait di UI
28. Verifikasi Ditolak 403
29. Verifikasi Tidak ada baris baru

## Notes

- Memvalidasi alur skenario "Pertahanan Mendalam (Defense-in-Depth): Penolakan API 403 untuk Mutasi pada Akun Sendiri dan Default User".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.3 Defense in Depth; global-settings/role/PRD/role.md §9.4.2.
- Sumber pemetaan test case granular: TC-GS-ROLE-247, TC-GS-ROLE-248, TC-GS-ROLE-250, TC-GS-ROLE-251, TC-GS-ROLE-253, TC-GS-ROLE-254, TC-GS-ROLE-255.
