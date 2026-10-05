---
id: TC-AUTH-OTP-E2E-042-mfa-handoff-unusual-login-alert
title: Deteksi login tak biasa memicu handoff MFA dan pengiriman email alert keamanan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-65
  - TC-AUTH-OTP-66
coverage:
  web: automated
---

# Deteksi login tak biasa memicu handoff MFA dan pengiriman email alert keamanan

## Prerequisites

- Akun aktif terdaftar dengan MFA aktif (`Fixture.auth.mfaUnusualLoginUser`)
- Lingkungan testing mendukung simulasi perubahan lokasi geografis (>100 km) atau fingerprint browser tak biasa
- Kotak masuk email testing dapat diinspeksi untuk verifikasi pengiriman email alert

## Test Steps

1. Simulasikan login untuk `Fixture.auth.mfaUnusualLoginUser` dari alamat IP/lokasi geografis baru (>100 km dari login terakhir) atau fingerprint browser baru
2. Buka halaman Login with OTP dan masukkan email user
3. Selesaikan reCAPTCHA, minta OTP, dan masukkan kode OTP yang benar pada halaman Input OTP
4. Verifikasi auto-submit mengarahkan browser ke halaman verifikasi MFA Authenticator
5. Verifikasi sistem secara otomatis mengirimkan email peringatan keamanan ("Unusual login detected") ke kotak masuk email user
6. Pada halaman MFA, masukkan kode TOTP yang benar dari aplikasi authenticator
7. Verifikasi login berhasil tuntas dan browser masuk ke Product Hub
8. Periksa Activity Log Session dan User Log
9. Verifikasi tercatat entri login dengan status Success dan Note "Login with OTP" tepat 1 entri

## Notes

- TAG Samurai mendeteksi anomali login berdasarkan jarak geografis dan perubahan perangkat untuk melindungi akun dari akses tak sah dengan memicu faktor autentikasi kedua dan peringatan dini ke email user.
