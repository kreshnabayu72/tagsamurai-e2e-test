---
id: TC-AUTH-OTP-E2E-009-request-otp-deactivated-mid-flow
title: Request OTP diblokir saat akun dinonaktifkan admin di tengah alur (dua sesi simultan)
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-100
  - TC-AUTH-OTP-70
coverage:
  web: automated
---

# Request OTP diblokir saat akun dinonaktifkan admin di tengah alur (dua sesi simultan)

## Prerequisites

- Dua sesi browser simultan: Sesi User Publik (Browser A) dan Sesi Admin Console (Browser B)
- Akun user yang awalnya berstatus Active (`Fixture.auth.midFlowUser`)
- Akun admin dengan hak akses mengelola user di Global Settings

## Test Steps

1. Pada Browser A, buka halaman Login with OTP dan ketikkan email `Fixture.auth.midFlowUser` ke dalam field Email
2. Selesaikan verifikasi reCAPTCHA pada Browser A (tapi jangan klik tombol submit terlebih dahulu)
3. Beralih ke Browser B (Sesi Admin), buka menu Global Settings > User List
4. Temukan baris user `Fixture.auth.midFlowUser`, lalu ubah status toggle aktif menjadi OFF (deactivate)
5. Konfirmasikan dialog penonaktifan user hingga berhasil
6. Kembali ke Browser A, segera klik tombol `[Request OTP]`
7. Verifikasi server mengevaluasi status akun secara real-time pada saat request tiba di backend
8. Verifikasi pengiriman OTP ditolak dan toast notifikasi error "Error, your account is inactive. Please contact the administrator to activate your account." muncul
9. Verifikasi halaman tetap berada di Input Email dan tidak ada kode OTP yang terkirim
10. Pada Browser B, periksa Activity Log Session
11. Verifikasi percobaan login ditolak ini tercatat dengan status Failed dan Note "User is inactive"

## Notes

- Pengecekan status akun dieksekusi secara real-time pada layer database/API, sehingga perubahan izin oleh administrator langsung membatalkan alur yang sedang berjalan.
