---
id: TC-GS-USER-E2E-120-create-gagal-server
title: 'Create user gagal karena error server dan form tidak direset'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-24
coverage:
  web: automated
---

# Create user gagal karena error server dan form tidak direset

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan `POST` Create User
- Position dan Division valid ada di master data

## Test Steps

1. Klik `[+ User]` dan isi semua field wajib dengan data valid
2. Klik `[Submit]` saat server membalas `500`
3. Verifikasi toast "Error, failed to create user." muncul
4. Verifikasi modal Create tetap terbuka dengan semua isian tetap ada (tidak direset)
5. Verifikasi tombol `[Submit]` kembali aktif dari state loading sehingga bisa dicoba ulang

## Notes

- Sumber `user.md` bagian 7. Alur Create yang berhasil dicakup `TC-GS-USER-E2E-002-create-users-success-flow-stay-open`, dan langkah gagal server di spec itu (langkah 5 sampai 7) dipertahankan sebagai versi awal.
