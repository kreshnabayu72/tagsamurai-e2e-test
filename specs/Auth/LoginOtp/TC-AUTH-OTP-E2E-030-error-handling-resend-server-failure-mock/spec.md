---
id: TC-AUTH-OTP-E2E-030-error-handling-resend-server-failure-mock
title: Penanganan kegagalan server 500 saat Resend OTP tanpa pengurangan kuota resend
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-51
  - TC-AUTH-OTP-72
coverage:
  web: automated
---

# Penanganan kegagalan server 500 saat Resend OTP tanpa pengurangan kuota resend

## Prerequisites

- Mode: mock (intersep HTTP pada endpoint `POST /v2/iam/auth/otp/request` saat aksi resend)
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka dan tombol "Resend code" dalam status enabled

## Test Steps

1. Konfigurasikan intersep endpoint `POST /v2/iam/auth/otp/request` untuk mengembalikan status HTTP 500 saat permintaan resend dikirimkan
2. Klik tombol "Resend code"
3. Verifikasi toast notifikasi error muncul dengan teks "Error, failed to send the code."
4. Verifikasi counter kuota jatah resend (`resend_count`) TIDAK bertambah karena kegagalan terjadi di layer infrastruktur/transport
5. Verifikasi kode OTP aktif yang ada sebelumnya TIDAK di-invalidate (tetap dapat digunakan untuk login)
6. Verifikasi kegagalan server transport ini TIDAK dicatat pada Activity Log Session maupun User Log

## Notes

- TAG Samurai membedakan kegagalan transport/server dengan kegagalan logika bisnis. Error 500 pada resend melindungi kuota user agar tidak hangus sia-sia akibat gangguan jaringan.
