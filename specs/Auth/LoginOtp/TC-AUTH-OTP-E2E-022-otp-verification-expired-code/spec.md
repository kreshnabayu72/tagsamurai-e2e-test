---
id: TC-AUTH-OTP-E2E-022-otp-verification-expired-code
title: Verifikasi OTP gagal karena kode kedaluwarsa setelah melewati masa berlaku 5 menit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-41
  - TC-AUTH-OTP-69
coverage:
  web: automated
---

# Verifikasi OTP gagal karena kode kedaluwarsa setelah melewati masa berlaku 5 menit

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka dengan kode OTP yang telah diterbitkan
- Lingkungan testing mendukung kontrol manipulasi waktu (clock skew / advance time >= 5 menit)

## Test Steps

1. Ambil kode OTP yang valid untuk sesi aktif tersebut
2. Majukan waktu server / manipulasi timestamp kadaluwarsa (`expires_at`) sehingga kode melewati masa berlaku 5 menit (`now > expires_at`)
3. Masukkan 6 digit kode OTP yang sebelumnya valid ke dalam kotak input OTP
4. Verifikasi auto-submit terpicu secara otomatis
5. Verifikasi sistem menolak verifikasi dengan menampilkan pesan error inline "Code expired" di bawah kotak digit OTP
6. Verifikasi kode OTP ditandai tidak dapat digunakan lagi
7. Menggunakan sesi admin, periksa Activity Log Session dan User Log
8. Verifikasi kegagalan karena kode kedaluwarsa ini dicatat di kedua surface log dengan status Failed dan Note "Incorrect OTP" (atau alasan spesifik expired pada sistem backend)

## Notes

- Kode OTP yang diterbitkan memiliki TTL (Time-to-Live) tepat 5 menit. Setelah 5 menit, submission kode ditolak server dan user wajib meminta kode baru via tombol Resend.
