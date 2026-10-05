---
id: TC-AUTH-OTP-E2E-041-mfa-handoff-idle-user
title: Handoff ke MFA Authenticator setelah verifikasi OTP sukses pada user idle >= 30 hari
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-64
  - TC-AUTH-OTP-66
coverage:
  web: automated
---

# Handoff ke MFA Authenticator setelah verifikasi OTP sukses pada user idle >= 30 hari

## Prerequisites

- Akun aktif terdaftar dengan MFA aktif yang telah idle / tidak aktif login selama >= 30 hari (`Fixture.auth.mfaIdleUser`)
- Aplikasi Authenticator terkonfigurasi dengan kunci TOTP valid untuk user tersebut

## Test Steps

1. Buka halaman Login with OTP dan masukkan email `Fixture.auth.mfaIdleUser`
2. Selesaikan reCAPTCHA, minta OTP, dan ambil kode 6 digit dari email user
3. Masukkan 6 digit kode OTP yang benar pada halaman Input OTP
4. Verifikasi auto-submit mengarahkan browser ke halaman verifikasi MFA Authenticator (faktor kedua)
5. Verifikasi pada jalur Login with OTP, verifikasi Step-2 langsung menuju metode Authenticator App tanpa alternatif via SMS/OTP
6. Pada halaman MFA Authenticator, masukkan kode TOTP 6 digit yang valid
7. Selesaikan verifikasi hingga berhasil masuk ke Product Hub
8. Periksa Activity Log Session dan User Log
9. Verifikasi tercatat entri login baru dengan status Success dan Note "Login with OTP" tepat 1 entri total

## Notes

- TAG Samurai mewajibkan re-verifikasi faktor kedua untuk akun yang telah melewati periode dormansi (idle >= 30 hari) guna mencegah pengambilalihan akun.
