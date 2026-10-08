---
id: TC-GS-USER-E2E-126-resend-email-gagal-server
title: 'Resend email gagal karena error server dan tidak masuk cooldown'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-58
coverage:
  web: automated
---

# Resend email gagal karena error server dan tidak masuk cooldown

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan Resend
- User "Umar Belum" berstatus Pending Activation dan user "Rudi Reset" berstatus Activated dengan email pending

## Test Steps

### Resend Activation

1. Klik `Resend Activation Email` pada "Umar Belum" saat server membalas `500`
2. Verifikasi toast "Error, failed to send activation email to Umar Belum." muncul
3. Verifikasi tombol Resend kembali aktif dan tidak masuk cooldown 60 detik

### Resend Confirmation

4. Klik `Resend Confirmation Email` pada "Rudi Reset" saat server membalas `500`
5. Verifikasi toast "Error, failed to send confirmation email to Rudi Reset." muncul
6. Verifikasi tombol Resend kembali aktif dan tidak masuk cooldown

## Notes

- Sumber `user.md` bagian 4.4 dan 7. Cooldown hanya berlaku setelah pengiriman berhasil. Resend yang berhasil dicakup `TC-GS-USER-E2E-029-resend-email` dan `030-resend-cooldown`.
