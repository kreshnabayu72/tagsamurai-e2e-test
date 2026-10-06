---
id: TC-AC-SU-E2E-023-resend-email-server-error-retry-tanpa-konsumsi-cooldown
title: "Resiliensi server error 5xx pada Resend Activation dan Confirmation Email tanpa mengonsumsi cooldown"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-178
  - TC-AC-SU-220
coverage:
  web: automated
---

# Resiliensi server error 5xx pada Resend Activation dan Confirmation Email tanpa mengonsumsi cooldown

## Prerequisites

- Mode: mock
- Login sebagai Role: Principal Total Control
- Simulasi mock respons 500 pada endpoint POST resend email

## Test Steps

### Simulasi Gagal Resend Activation Email

1. Konfigurasikan mock agar endpoint POST resend activation email mengembalikan status 500
2. Buka User List dan klik `Resend Activation Email` pada pengguna Pending Activation
3. Verifikasi toast error muncul: `"Error, failed to send email."`
4. Verifikasi cooldown 60 detik TIDAK dimulai dan tombol tetap Enabled sehingga admin dapat langsung melakukan retry

### Simulasi Gagal Resend Confirmation Email

1. Konfigurasikan mock agar endpoint POST resend confirmation email mengembalikan status 500
2. Klik `Resend Confirmation Email` pada pengguna Pending Email Confirmation
3. Verifikasi toast error muncul: `"Error, failed to send email."`
4. Verifikasi tombol tetap Enabled untuk retry tanpa terkunci cooldown

## Notes

- Kegagalan jaringan tidak boleh mengorbankan cooldown pengguna.
