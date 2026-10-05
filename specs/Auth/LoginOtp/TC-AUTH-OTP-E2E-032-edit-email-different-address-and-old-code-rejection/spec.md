---
id: TC-AUTH-OTP-E2E-032-edit-email-different-address-and-old-code-rejection
title: Penggantian ke alamat email berbeda dan penolakan kode OTP lama ("OTP invalid — email changed")
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-42
  - TC-AUTH-OTP-60
  - TC-AUTH-OTP-61
coverage:
  web: automated
---

# Penggantian ke alamat email berbeda dan penolakan kode OTP lama ("OTP invalid — email changed")

## Prerequisites

- Akun aktif A (`Fixture.auth.accountAEmail`) dan Akun aktif B (`Fixture.auth.accountBEmail`) telah disiapkan
- Akun A telah meminta kode OTP dan kode OTP pertama untuk Akun A telah tersimpan di variabel test
- Halaman Input OTP terbuka untuk Akun A

## Test Steps

### Ganti ke Alamat Email Berbeda

1. Pada halaman Input OTP milik Akun A, klik link atau tombol "Edit email"
2. Verifikasi browser kembali ke halaman Input Email dengan field Email terisi email Akun A
3. Hapus isi field Email, lalu masukkan email Akun B (`Fixture.auth.accountBEmail`)
4. Selesaikan verifikasi reCAPTCHA dan klik tombol `[Request OTP]`
5. Verifikasi toast "Success, the code has been sent." muncul dan browser diarahkan ke halaman Input OTP baru
6. Verifikasi subtitle halaman Input OTP kini menampilkan alamat email Akun B tanpa sensor

### Penolakan Kode OTP Lama Milik Akun A

7. Pada halaman Input OTP yang baru (milik Akun B), ketikkan 6 digit kode OTP lama yang sebelumnya diterbitkan untuk Akun A
8. Verifikasi auto-submit terpicu saat digit ke-6 dimasukkan
9. Verifikasi verifikasi ditolak dan pesan error inline "Invalid code" muncul di bawah kotak digit OTP
10. Menggunakan sesi admin, periksa Activity Log Session dan User Log
11. Verifikasi kegagalan ini dicatat dengan status Failed dan Note "OTP invalid — email changed"

## Notes

- TAG Samurai memvalidasi keterikatan kode OTP dengan sesi email yang sedang aktif. Kode yang diterbitkan untuk email sebelumnya ditolak secara mutlak dengan catatan audit khusus "OTP invalid — email changed".
