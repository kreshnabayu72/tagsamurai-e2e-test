---
id: TC-AUTH-OTP-E2E-014-request-otp-new-code-invalidates-previous
title: Permintaan OTP baru meng-invalidate kode sebelumnya dan navigasi kembali ke Login Password
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-26
  - TC-AUTH-OTP-112
coverage:
  web: automated
---

# Permintaan OTP baru meng-invalidate kode sebelumnya dan navigasi kembali ke Login Password

## Prerequisites

- Browser berada pada status publik (belum login)
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Sesi OTP pertama telah dilakukan dan kode pertama telah tersimpan

## Test Steps

### Navigasi Kembali ke Login Password dari Halaman OTP

1. Pada halaman Input OTP yang terbuka untuk `Fixture.auth.standardUserEmail`, klik link "Back to Login with Password"
2. Verifikasi browser berpindah ke halaman Login with Password (`/login-password`)
3. Verifikasi navigasi ini tidak menghasilkan entri baru pada audit log

### Invalidation Kode OTP Aktif Sebelumnya oleh Permintaan Baru

4. Dari halaman Login Password, klik kembali link "Log in with OTP"
5. Masukkan kembali email `Fixture.auth.standardUserEmail`
6. Selesaikan verifikasi reCAPTCHA lalu klik `[Request OTP]`
7. Verifikasi toast "Success, the code has been sent." muncul dan browser kembali ke halaman Input OTP dengan kode baru
8. Coba masukkan kode OTP pertama yang dikirimkan pada sesi sebelumnya
9. Verifikasi kode OTP lama ditolak karena telah di-invalidate secara server-side meskipun masa 5 menit belum habis
10. Masukkan kode OTP baru yang baru saja diterbitkan
11. Verifikasi kode baru diterima dan proses verifikasi berjalan normal

## Notes

- TAG Samurai menerapkan aturan hanya 1 kode OTP aktif per user pada satu waktu. Permintaan kode baru dari sesi terpisah langsung membatalkan kode aktif sebelumnya.
