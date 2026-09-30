---
id: TC-GS-USER-E2E-122-delete-single-gagal-server
title: 'Delete satu user gagal karena error server dan dialog tetap terbuka'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-40
coverage:
  web: automated
---

# Delete satu user gagal karena error server dan dialog tetap terbuka

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan Delete User
- User "Target Hapus" ada

## Test Steps

1. Klik row action `Delete` pada baris "Target Hapus"
2. Klik `[Delete]` di dialog "Delete User" saat server membalas `500`
3. Verifikasi toast "Error, failed to delete user." muncul
4. Verifikasi dialog "Delete User" tetap terbuka dan baris "Target Hapus" masih ada di tabel
5. Verifikasi tombol `[Delete]` kembali aktif dari state loading

## Notes

- Sumber `user.md` bagian 7. Delete yang berhasil dicakup `TC-GS-USER-E2E-005-delete-user`.
