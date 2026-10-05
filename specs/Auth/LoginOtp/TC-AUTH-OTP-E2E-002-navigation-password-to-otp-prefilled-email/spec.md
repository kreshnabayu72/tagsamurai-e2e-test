---
id: TC-AUTH-OTP-E2E-002-navigation-password-to-otp-prefilled-email
title: Navigasi bolak-balik Login Password dan Login OTP dengan persistensi prefilled email
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-3
  - TC-AUTH-OTP-67
coverage:
  web: automated
---

# Navigasi bolak-balik Login Password dan Login OTP dengan persistensi prefilled email

## Prerequisites

- Browser berada pada status publik (belum login / unauthenticated session)
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Halaman Login with Password dapat diakses

## Test Steps

### Transisi Password ke OTP dengan Email Prefilled

1. Buka halaman Login with Password
2. Ketik email `Fixture.auth.standardUserEmail` ke dalam field Email
3. Klik link "Log in with OTP"
4. Verifikasi browser berpindah ke halaman Input Email Login with OTP
5. Verifikasi field Email langsung terisi otomatis dengan `Fixture.auth.standardUserEmail` (prefilled) tanpa user mengetik ulang

### Transisi OTP Kembali ke Password dengan Email Prefilled

6. Klik link "Use password instead" pada halaman Input Email Login with OTP
7. Verifikasi browser kembali ke halaman Login with Password
8. Verifikasi field Email pada halaman Login with Password tetap terisi dengan `Fixture.auth.standardUserEmail`
9. Verifikasi perpindahan bolak-balik ini tidak menghasilkan entri baru pada surface audit log

## Notes

- TAG Samurai menjamin kontinuitas pengisian form saat berpindah antar-metode login tanpa menghilangkan konteks email yang sudah diketik user.
