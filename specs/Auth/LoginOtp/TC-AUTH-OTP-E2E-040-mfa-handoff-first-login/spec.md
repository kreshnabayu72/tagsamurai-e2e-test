---
id: TC-AUTH-OTP-E2E-040-mfa-handoff-first-login
title: Handoff ke MFA Authenticator setelah verifikasi OTP sukses pada user login pertama
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-39
  - TC-AUTH-OTP-63
  - TC-AUTH-OTP-66
coverage:
  web: automated
---

# Handoff ke MFA Authenticator setelah verifikasi OTP sukses pada user login pertama

## Prerequisites

- Akun terdaftar dengan MFA aktif dan memenuhi pemicu MFA pada login pertama (`Fixture.auth.mfaFirstLoginUser`)
- Aplikasi Authenticator terkonfigurasi dengan kunci TOTP valid untuk user uji

## Test Steps

1. Buka halaman Login with OTP dan masukkan email `Fixture.auth.mfaFirstLoginUser`
2. Minta OTP dan masukkan 6 digit kode OTP yang benar pada halaman Input OTP
3. Verifikasi auto-submit terpicu
4. Verifikasi browser otomatis di-redirect ke halaman MFA Step-2
5. Verifikasi pada jalur Login with OTP, verifikasi Step-2 langsung menuju metode Authenticator App tanpa pilihan metode OTP lagi (karena faktor pertama sudah berupa OTP)
6. Verifikasi pada titik ini entri log "Login with OTP" dengan status Success BELUM dicatat karena sesi penuh belum terbentuk
7. Pada halaman MFA Authenticator, masukkan token TOTP 6 digit yang valid dari aplikasi authenticator
8. Selesaikan alur autentikasi hingga berhasil masuk ke Product Hub
9. Periksa Activity Log Session dan User Log
10. Verifikasi entri baru tercatat dengan status Success dan Note "Login with OTP" tepat 1 entri total untuk keseluruhan proses login ini

## Notes

- Berbeda dari Login with Password yang menyediakan pilihan antara OTP atau Authenticator, Login with OTP langsung mengarahkan faktor kedua ke Authenticator.
- Handoff MFA untuk user idle >= 30 hari dipisahkan ke `TC-AUTH-OTP-E2E-041`.
- Deteksi login tak biasa (>100 km) dipisahkan ke `TC-AUTH-OTP-E2E-042`.
