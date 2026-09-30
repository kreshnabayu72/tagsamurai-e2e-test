---
id: TC-GS-USER-E2E-121-edit-gagal-server
title: 'Edit user gagal karena error server dan form tidak direset'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-32
coverage:
  web: automated
---

# Edit user gagal karena error server dan form tidak direset

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan `PATCH` Edit User
- User "Budi Santoso" ada

## Test Steps

1. Klik row action `Edit` pada baris "Budi Santoso" lalu ubah Position
2. Klik `[Save]` saat server membalas `500`
3. Verifikasi toast "Error, failed to update user." muncul
4. Verifikasi modal Edit tetap terbuka dengan isian yang diubah tetap ada (tidak kembali ke nilai lama)
5. Verifikasi tombol `[Save]` kembali aktif dari state loading

## Notes

- Sumber `user.md` bagian 7. Alur Edit yang berhasil dicakup `TC-GS-USER-E2E-024-edit-user-success`.
