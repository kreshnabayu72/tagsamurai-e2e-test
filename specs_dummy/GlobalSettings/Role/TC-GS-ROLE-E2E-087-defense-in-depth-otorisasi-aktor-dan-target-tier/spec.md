---
id: TC-GS-ROLE-E2E-087-defense-in-depth-otorisasi-aktor-dan-target-tier
title: "Pertahanan Mendalam: Penolakan API 403 Berdasarkan Batasan Wewenang Aktor dan Proteksi Target TC/RO"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-249
  - TC-GS-ROLE-252
  - TC-GS-ROLE-256
  - TC-GS-ROLE-257
coverage:
  web: automated
---

# Pertahanan Mendalam: Penolakan API 403 Berdasarkan Batasan Wewenang Aktor dan Proteksi Target TC/RO

## Prerequisites

- Login sebagai Read Only / Manage user and role; direct API mutation
- Data Uji: Siti Nurhaliza, Lina Marlina, Hendra Wijaya
- Setup Hook: beforeEach: callApiDirect()
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)
- Permintaan dikirim langsung (bypass UI) via test client yang memakai sesi aktor
- Login sbg Role: Read Only (Siti Nurhaliza sebelum upgrade) / Manage user and role Read saja (Fajar Nugroho)

## Test Steps

### Edit CRUD target Total Control oleh Manage user and role lewat permintaan langsung ditolak (TC-GS-ROLE-249)

1. Kirim permintaan: Edit CRUD Manage TAG Update untuk Ahmad Fauzi (Total Control)
2. Reload halaman terkait di UI
3. Verifikasi Ditolak 403
4. Verifikasi Ahmad Fauzi tetap Total Control

### Remove baris role target Read Only oleh Manage user and role lewat permintaan langsung ditolak (TC-GS-ROLE-252)

5. Kirim permintaan: Remove baris Manage TAG milik Rina Putri (Read Only)
6. Reload halaman terkait di UI
7. Verifikasi Ditolak 403
8. Verifikasi Baris tetap ada; Rina Putri tetap Read Only

### Assign/Remove access level oleh Manage user and role lewat permintaan langsung ditolak (TC-GS-ROLE-256)

9. Kirim permintaan: Assign Total Control ke Wawan Setiawan; Remove Read Only Rina Putri
10. Reload halaman terkait di UI
11. Verifikasi Kedua permintaan ditolak 403
12. Verifikasi Wawan Setiawan tidak di Tab Total Control; Rina Putri tetap di Tab Read Only

### Aksi tulis Detail oleh Read Only lewat permintaan langsung ditolak (TC-GS-ROLE-257)

13. Kirim permintaan: Edit CRUD, Assign Role, Remove baris pada Manage TAG
14. Reload halaman terkait di UI
15. Verifikasi Ketiga permintaan ditolak 403
16. Verifikasi Data Detail tidak berubah

## Notes

- Memvalidasi alur skenario "Pertahanan Mendalam: Penolakan API 403 Berdasarkan Batasan Wewenang Aktor dan Proteksi Target TC/RO".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.3 Defense in Depth; global-settings/role/PRD/role.md §9.4.2.
- Sumber pemetaan test case granular: TC-GS-ROLE-249, TC-GS-ROLE-252, TC-GS-ROLE-256, TC-GS-ROLE-257.
