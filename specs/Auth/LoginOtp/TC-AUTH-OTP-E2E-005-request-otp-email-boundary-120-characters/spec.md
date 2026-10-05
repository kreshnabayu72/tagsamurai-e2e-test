---
id: TC-AUTH-OTP-E2E-005-request-otp-email-boundary-120-characters
title: Request OTP berhasil dengan panjang karakter email tepat 120 karakter (nilai batas maksimum)
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-8
coverage:
  web: automated
---

# Request OTP berhasil dengan panjang karakter email tepat 120 karakter (nilai batas maksimum)

## Prerequisites

- Browser berada pada status publik (belum login)
- Satu akun aktif terdaftar dengan panjang email tepat 120 karakter valid (`Fixture.auth.user120CharEmail`)
- Layanan email testing siap menerima kode OTP

## Test Steps

1. Buka halaman Input Email Login with OTP
2. Masukkan alamat email sepanjang tepat 120 karakter `Fixture.auth.user120CharEmail` ke dalam field Email
3. Verifikasi tidak ada error validasi karakter atau batasan panjang yang muncul
4. Selesaikan verifikasi reCAPTCHA
5. Klik tombol `[Request OTP]`
6. Verifikasi request diproses berhasil tanpa penolakan panjang string
7. Verifikasi toast "Success, the code has been sent." muncul
8. Verifikasi browser berpindah ke halaman Input OTP dan kode OTP diterbitkan dengan masa berlaku 5 menit

## Notes

- TAG Samurai menetapkan batas maksimal panjang alamat email adalah 120 karakter. Nilai boundary tepat 120 karakter wajib diterima oleh validator frontend dan backend.
- Kasus penolakan karakter ke-121 dipisahkan ke `TC-AUTH-OTP-E2E-003`.
