---
id: TC-AUTH-MFA-E2E-002-trigger-first-login-pre-auth-session
title: Pemicu MFA karena login pertama kali dan pembentukan pre-auth session
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-2
  - TC-AUTH-MFA-7
coverage:
  web: automated
---

# Pemicu MFA karena login pertama kali dan pembentukan pre-auth session

## Prerequisites

- Mode: FE+BE
- Akun baru saja diaktivasi dan belum pernah login sukses sebelumnya (`first_login_at IS NULL`)
- Sesi login awal belum memiliki hak akses penuh

## Test Steps

1. Buka halaman Login TAG Samurai
2. Masukkan email dan password akun baru aktivasi, lalu klik `[Login]`
3. Verifikasi sistem mendeteksi kondisi login pertama (`first_login_at IS NULL`) dan mewajibkan verifikasi faktor kedua (MFA)
4. Verifikasi pengguna dialihkan ke halaman Choose Verification Method atau Setup Authenticator
5. Verifikasi sesi penuh BELUM terbentuk pada browser (pengguna belum dapat mengakses endpoint terproteksi)
6. Verifikasi token sementara `mfa_session` (pre-auth) terbentuk dengan status aktif dan masa berlaku 10 menit
7. Verifikasi belum ada entri audit log "Success" yang tertulis di Activity Log Session maupun User Log

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-02`
- Merepresentasikan `TC-AUTH-MFA-2` dan `TC-AUTH-MFA-7` (FE Ref: `TC-AUTH-MFA-FE-02`).
- Memastikan isolasi keamanan pre-auth di mana hak akses aplikasi tidak diberikan sebelum faktor kedua tuntas.
