---
id: TC-AUTH-OTP-E2E-023-otp-verification-one-time-use-reuse
title: Kode OTP hanya dapat digunakan satu kali dan ditolak saat disubmit ulang
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-44
  - TC-AUTH-OTP-69
coverage:
  web: automated
---

# Kode OTP hanya dapat digunakan satu kali dan ditolak saat disubmit ulang

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Dua konteks tab browser dibuka pada alur Login with OTP untuk user yang sama (Tab A dan Tab B)

## Test Steps

1. Pada Tab A, minta kode OTP dan masukkan 6 digit kode yang benar
2. Verifikasi auto-submit berhasil, kode ditandai telah digunakan (`otp_code.used = true`), dan sesi login terbentuk di Tab A
3. Beralih ke Tab B yang masih membuka halaman Input OTP untuk sesi yang sama
4. Masukkan kembali kode OTP 6 digit yang sama persis (yang baru saja berhasil digunakan di Tab A)
5. Verifikasi auto-submit terpicu di Tab B
6. Verifikasi server menolak kode tersebut dan pesan error inline "Invalid code" muncul di Tab B
7. Verifikasi Tab B TIDAK berhasil masuk dan tidak membuat token sesi kedua dari kode yang sama
8. Menggunakan sesi admin, periksa Activity Log Session
9. Verifikasi penolakan submission ulang ini dicatat dengan status Failed dan Note "Incorrect OTP"

## Notes

- TAG Samurai menjamin sifat one-time use (OTP) secara mutlak melalui operasi atomic consume pada database (`UPDATE otp_code SET used=true WHERE id=:id AND used=false`).
