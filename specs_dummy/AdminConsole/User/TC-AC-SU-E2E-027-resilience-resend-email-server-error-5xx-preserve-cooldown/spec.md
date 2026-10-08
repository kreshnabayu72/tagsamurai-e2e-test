---
id: TC-AC-SU-E2E-027-resilience-resend-email-server-error-5xx-preserve-cooldown
title: "Resiliensi Server Error 5xx pada Resend Activation dan Confirmation Email Tanpa Membakar Cooldown"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-178
  - TC-AC-SU-220
coverage:
  web: automated
---

# Resiliensi Server Error 5xx pada Resend Activation dan Confirmation Email Tanpa Membakar Cooldown

## Prerequisites

- Mode: mock
- Login sebagai Total Control
- Interceptor mock disiapkan untuk merespons 500 pada endpoint resend email

## Test Steps

### Resiliensi Error Resend Activation Email
1. Buka `Admin Console > Settings > User`
2. Atur interceptor agar mengembalikan `500 Internal Server Error` pada endpoint aktivasi
3. Klik opsi `Resend Activation Email` pada menu baris user pending
4. Verifikasi toast error muncul: `"Failed to resend activation email. Please try again later."`
5. Buka kembali menu baris `[...]` user tsb
6. Verifikasi opsi `Resend Activation Email` TETAP DALAM KONDISI AKTIF (cooldown timer tidak hangus/tidak berkurang karena kegagalan server)

### Resiliensi Error Resend Confirmation Email
7. Atur interceptor mengembalikan status 500 pada endpoint confirmation email
8. Klik opsi `Resend Confirmation Email` pada menu baris
9. Verifikasi toast error muncul dan opsi menu tetap aktif tanpa terblokir cooldown timer

## Notes

Memastikan user tidak terjebak cooldown saat terjadi gangguan jaringan di backend.
