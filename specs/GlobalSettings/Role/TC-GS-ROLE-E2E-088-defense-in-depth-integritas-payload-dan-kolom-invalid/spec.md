---
id: TC-GS-ROLE-E2E-088-defense-in-depth-integritas-payload-dan-kolom-invalid
title: "Pertahanan Mendalam: Integritas Payload Form, Proteksi Kolom Invalid, Default User Skipping, dan Partial Success"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-258
  - TC-GS-ROLE-259
  - TC-GS-ROLE-260
  - TC-GS-ROLE-261
coverage:
  web: automated
---

# Pertahanan Mendalam: Integritas Payload Form, Proteksi Kolom Invalid, Default User Skipping, dan Partial Success

## Prerequisites

- Login sebagai Total Control; direct API mutation
- Data Uji: Payload tampering test data
- Setup Hook: beforeEach: callApiDirect()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Permintaan dikirim langsung (bypass UI) via test client yang memakai sesi aktor
- Server dibuat menolak satu baris (failure injection pada Bulk Remove)

## Test Steps

### Nilai Read=false pada permintaan Edit CRUD diabaikan (TC-GS-ROLE-258)

1. Kirim permintaan: Edit CRUD Manage TAG milik Wawan Setiawan dengan Read=false dan Update=true
2. Reload halaman terkait di UI
3. Verifikasi Permintaan sukses
4. Verifikasi Detail: Read tetap checked, Update checked

### Flag kolom yang tidak berlaku diabaikan (TC-GS-ROLE-259)

5. Kirim permintaan: Edit CRUD Manage TAG milik Wawan Setiawan dengan Create=true dan Update=true
6. Reload halaman terkait di UI
7. Verifikasi Permintaan sukses tanpa error
8. Verifikasi Update checked; tidak ada kolom Create di Detail Manage TAG
9. Verifikasi Changelog hanya memuat entry Field Update

### Bulk Remove berisi baris Default User lewat permintaan langsung (TC-GS-ROLE-260)

10. Kirim permintaan: Bulk Remove Manage hardware untuk Budi Santoso dan Nina Kartika
11. Reload halaman terkait di UI
12. Verifikasi Baris Nina Kartika terhapus
13. Verifikasi Baris Budi Santoso tetap ada (dihitung gagal)
14. Verifikasi Changelog hanya entry Remove Nina Kartika

### Partial success Bulk Remove menampilkan toast sukses parsial (TC-GS-ROLE-261)

15. Detail "Manage hardware": centang 2 baris
16. Bulk Action > Remove > [Remove]
17. Verifikasi Toast sukses: "Success, user has been removed. Some items were skipped."
18. Verifikasi Baris yang berhasil hilang; baris gagal tetap ada
19. Verifikasi Bulk Action Bar tertutup dan seleksi di-reset ke 0 termasuk baris yang gagal

## Notes

- Memvalidasi alur skenario "Pertahanan Mendalam: Integritas Payload Form, Proteksi Kolom Invalid, Default User Skipping, dan Partial Success".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.3 Defense in Depth; global-settings/role/PRD/role.md §9.4.2; global-settings/role/PRD/role.md §7.1 T-11; global-settings/role/PRD/role.md §9.6; foundation/process/prd-process/prd-conventions.md §8.
- Sumber pemetaan test case granular: TC-GS-ROLE-258, TC-GS-ROLE-259, TC-GS-ROLE-260, TC-GS-ROLE-261.
