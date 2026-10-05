---
id: TC-AUTH-OTP-E2E-031-edit-email-flow-resend-reset
title: Ubah email dari halaman OTP, prefill email, dan reset sesi resend pada email sama
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-4
  - TC-AUTH-OTP-58
  - TC-AUTH-OTP-59
coverage:
  web: automated
---

# Ubah email dari halaman OTP, prefill email, dan reset sesi resend pada email sama

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Akun telah meminta OTP dan mencapai status resend count tertentu (misalnya `resend_count = 3`) di halaman Input OTP
- Kode OTP pertama telah tersimpan

## Test Steps

1. Pada halaman Input OTP yang terbuka untuk `Fixture.auth.standardUserEmail`, klik link atau tombol "Edit email"
2. Verifikasi browser berpindah kembali ke halaman Input Email Login with OTP
3. Verifikasi field Email terisi otomatis dengan `Fixture.auth.standardUserEmail` (prefilled) dan dalam kondisi dapat diedit
4. Verifikasi bahwa kode OTP sebelumnya telah di-invalidate secara server-side
5. Tanpa mengubah isi field Email (tetap menggunakan `Fixture.auth.standardUserEmail`), selesaikan verifikasi reCAPTCHA dan klik tombol `[Request OTP]`
6. Verifikasi toast notifikasi muncul dengan teks "Success, the code has been sent." dan browser kembali diarahkan ke halaman Input OTP
7. Verifikasi sesi OTP baru terbentuk dengan jatah resend penuh (counter `resend_count` di-reset kembali ke 0, bukan melanjutkan hitungan sesi sebelumnya)

## Notes

- Alur "Edit email" membatalkan kode aktif sebelumnya dan me-reset counter resend meskipun user menggunakan email yang sama persis.
- Pengujian ganti ke email berbeda dan penolakan kode lama dipisahkan ke `TC-AUTH-OTP-E2E-032`.
