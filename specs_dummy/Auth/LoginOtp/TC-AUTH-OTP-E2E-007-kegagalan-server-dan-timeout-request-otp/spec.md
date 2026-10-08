---
id: TC-AUTH-OTP-E2E-007-kegagalan-server-dan-timeout-request-otp
title: "Penanganan Kegagalan Server 5xx dan Network Timeout pada Request OTP"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-31
  - TC-AUTH-OTP-32
coverage:
  web: automated
---

# Penanganan Kegagalan Server 5xx dan Network Timeout pada Request OTP

## Prerequisites

- Mode: mock / network intercept. Digunakan intercept HTTP pada endpoint request OTP (`POST /auth/otp/request` atau rute setara).
- Belum login dan session kosong. Halaman `Auth > Login with OTP > Request OTP` (`/login/otp`) terbuka di browser.
- User `Ratna Utami` (`ratnautami@qwertysystem.net`) profil BASE.
- User `Taufik Safitri` (`taufiksafitri@qwertysystem.net`) profil BASE.

## Test Steps

### Penanganan respons server error 500 / 503

1. Buka halaman Request OTP di browser
2. Masukkan email `ratnautami@qwertysystem.net` ke field Email
3. Centang widget reCAPTCHA v2
4. Konfigurasikan mock/intercept jaringan untuk mengembalikan response status `500 Internal Server Error`
5. Klik button [Request OTP]
6. Verifikasi toast banner error muncul dengan pesan kegagalan server: "Internal server error. Please try again later."
7. Verifikasi halaman tidak berpindah ke Verify OTP (tetap berada di halaman Request OTP)
8. Verifikasi field Email mempertahankan teks `ratnautami@qwertysystem.net`
9. Verifikasi button [Request OTP] kembali enabled dan spinner loading hilang
10. Verifikasi widget reCAPTCHA kembali ke keadaan belum dicentang sehingga wajib dicentang ulang

### Penanganan network timeout dan koneksi terputus

11. Buka kembali halaman Request OTP dalam sesi baru
12. Masukkan email `taufiksafitri@qwertysystem.net` ke field Email
13. Centang widget reCAPTCHA v2
14. Konfigurasikan intercept jaringan untuk mensimulasikan network abort / timeout
15. Klik button [Request OTP]
16. Verifikasi toast banner error muncul dengan pesan koneksi jaringan: "Network connection failed. Please check your internet connection."
17. Verifikasi pengguna tidak dialihkan ke halaman lain
18. Verifikasi form tetap interaktif untuk pengulangan submit saat jaringan pulih

## Notes

- Bila terjadi kegagalan infrastruktur server 5xx atau koneksi jaringan, sistem tidak boleh mengunci form atau mengarahkan ke halaman 404/500 utuh; state form dipertahankan dengan pesan kesalahan yang informatif.
- Widget reCAPTCHA wajib di-reset ke status unchecked setelah terjadi kesalahan server apa pun untuk mencegah token replay.
