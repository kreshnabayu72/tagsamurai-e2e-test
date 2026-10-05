---
id: TC-AUTH-OTP-E2E-043-session-management-concurrent-limit
title: Login sukses via OTP menyerahkan evaluasi batas sesi konkuren ke Session Management
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-104
coverage:
  web: automated
---

# Login sukses via OTP menyerahkan evaluasi batas sesi konkuren ke Session Management

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Akun telah memiliki satu sesi aktif di perangkat lain (misalnya perangkat mobile)

## Test Steps

1. Pada sesi web browser, buka halaman Login with OTP untuk `Fixture.auth.standardUserEmail`
2. Minta OTP dan masukkan 6 digit kode yang benar pada halaman Input OTP
3. Verifikasi auto-submit berhasil dan sesi autentikasi web terbentuk
4. Verifikasi sistem menyerahkan evaluasi batas sesi aktif ke modul Session Management
5. Verifikasi bahwa pasangan 1 sesi web dan 1 sesi mobile diizinkan aktif secara bersamaan sesuai aturan modul Session Management

## Notes

- TAG Samurai memperbolehkan kombinasi 1 sesi browser web dan 1 sesi aplikasi mobile aktif bersamaan. Evaluasi batas sesi secara mendalam merupakan domain modul Session Management.
