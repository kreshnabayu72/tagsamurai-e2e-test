---
id: TC-AUTH-MFA-E2E-015-choose-method-screening-and-select-otp
title: Screening layar Choose Method seleksi kartu opsi dan pengiriman kode OTP via email
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-26
  - TC-AUTH-MFA-28
  - TC-AUTH-MFA-29
coverage:
  web: automated
---

# Screening layar Choose Method seleksi kartu opsi dan pengiriman kode OTP via email

## Prerequisites

- Mode: FE+BE
- User login menggunakan Password (Faktor-1) dan memicu evaluasi MFA

## Test Steps

### Screening Layar Choose Method
1. Buka halaman setelah Faktor-1 sukses dan amati antarmuka
2. Verifikasi judul halaman bertuliskan "Choose verification method"
3. Verifikasi subtitle bertuliskan "Select how you'd like to verify your identity"
4. Verifikasi terdapat dua Option Card dalam keadaan unselected: "OTP via email" (icon MailLine) dan "Authenticator app" (icon ShieldUserLine)
5. Verifikasi tombol CTA `[Login]` dalam keadaan disabled

### Interaksi Seleksi dan Submit Opsi OTP
6. Klik pada kartu opsi "OTP via email"
7. Verifikasi kartu opsi ter-highlight dengan border primary
8. Verifikasi tombol CTA `[Login]` menjadi aktif (enabled)
9. Klik tombol `[Login]`
10. Verifikasi pengguna dinavigasikan ke halaman Verifikasi OTP (MFA)
11. Verifikasi kode OTP 6 digit diterbitkan dan dikirimkan ke email user

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-15`
- Merepresentasikan `TC-AUTH-MFA-26`, `28`, `29` (FE Ref: `TC-AUTH-MFA-FE-15`).
