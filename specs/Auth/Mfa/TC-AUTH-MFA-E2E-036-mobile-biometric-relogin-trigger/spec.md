---
id: TC-AUTH-MFA-E2E-036-mobile-biometric-relogin-trigger
title: "Aplikasi Mobile Android: Faktor-1 Biometric Re-Login Memicu Evaluasi MFA"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-54
coverage:
  mobile: automated
---
# Aplikasi Mobile Android: Faktor-1 Biometric Re-Login Memicu Evaluasi MFA

## Prerequisites

- Perangkat uji mobile Android (atau emulator) dengan aplikasi TAG Samurai terpasang.
- Pengguna `Naufal Hakim` (`naufalhakim@qwertysystem.net`) profil MOB (memiliki faktor-1 Biometric Re-login aktif).
- Layanan biometrik perangkat (fingerprint / face unlock) dikonfigurasi aktif.

## Test Steps

### Faktor-1 Biometric Re-login memicu Choose Verification Method

1. Buka aplikasi mobile TAG Samurai pada perangkat Android
2. Pilih alur Biometric Re-login untuk akun `naufalhakim@qwertysystem.net`
3. Berikan input biometrik yang sah pada dialog prompt sensor biometrik perangkat
4. Verifikasi autentikasi biometrik faktor-1 berhasil lolos
5. Verifikasi sistem mengevaluasi kriteria MFA dan menampilkan halaman `Auth > MFA > Choose Verification Method` di aplikasi mobile
6. Verifikasi kedua opsi verifikasi faktor kedua ("OTP via email" dan "Authenticator app") tersedia lengkap dan berfungsi normal

## Notes

- Sesuai PRD §11 dan F-AUTHMFA-01, alur Biometric Re-login pada mobile tunduk pada evaluasi dan kebijakan pemicu MFA yang sama dengan Login with Password.
