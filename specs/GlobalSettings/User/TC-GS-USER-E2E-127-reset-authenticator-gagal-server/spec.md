---
id: TC-GS-USER-E2E-127-reset-authenticator-gagal-server
title: 'Reset Authenticator gagal karena error server dan dialog tetap terbuka'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-73
coverage:
  web: automated
---

# Reset Authenticator gagal karena error server dan dialog tetap terbuka

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan Reset Authenticator
- User "Rina Wijaya" punya Authenticator enrolled

## Test Steps

1. Buka User Detail "Rina Wijaya" dan klik `Reset Authenticator`
2. Klik `[Reset]` di dialog saat server membalas `500`
3. Verifikasi toast "Error, failed to reset authenticator for Rina Wijaya." muncul
4. Verifikasi dialog tetap terbuka, badge tetap "Enrolled", dan tombol `[Reset]` kembali aktif dari state loading

## Notes

- Sumber `user.md` bagian 4.1 dan 7. Reset yang berhasil dicakup `TC-GS-USER-E2E-037-reset-authenticator`.
