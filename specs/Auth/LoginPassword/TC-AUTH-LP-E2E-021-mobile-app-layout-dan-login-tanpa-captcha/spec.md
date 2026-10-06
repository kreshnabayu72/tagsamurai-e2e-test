---
id: TC-AUTH-LP-E2E-021-mobile-app-layout-dan-login-tanpa-captcha
title: Layout aplikasi mobile, login tanpa reCAPTCHA, dan validasi Play Integrity
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-06
  - TC-AUTH-LP-70
  - TC-AUTH-LP-75
coverage:
  mobile: automated
---

# Layout aplikasi mobile, login tanpa reCAPTCHA, dan validasi Play Integrity

## Prerequisites

- User belum login; aplikasi native TAG Samurai Mobile (Android / iOS) terbuka di perangkat atau emulator.
- User `budisantoso@qwertysystem.net` berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA di mobile.
- User `jokosusilo@qwertysystem.net` berstatus Activated dan Active dengan hitungan gagal 0 di mobile.
- Administrator Total Control (Global Settings) memantau `Global Settings > Activity Log > Session` pada sesi terpisah.
- Mode: mock untuk simulasi token Play Integrity kosong atau invalid di mobile.

## Test Steps

### Screening layar login aplikasi mobile tanpa reCAPTCHA

1. Buka layar Login with Password pada aplikasi TAG Samurai Mobile
2. Verifikasi logo TAG Samurai tampil di bagian atas layar
3. Verifikasi title layar adalah "Login with Password"
4. Verifikasi subtitle layar adalah "Sign in and start managing your assets"
5. Verifikasi field Email dan field Password (dengan ikon toggle intip) tampil
6. Verifikasi tombol [Log in] berukuran lebar penuh tampil dalam keadaan enabled
7. Verifikasi link [Log in with OTP] dan link "Forgot your password? " [Reset here] tampil di bawah tombol [Log in]
8. Verifikasi widget reCAPTCHA dan caption "Please verify that you are not a robot" TIDAK dirender pada aplikasi mobile

### Login berhasil di mobile tanpa langkah reCAPTCHA

9. Masukkan email `budisantoso@qwertysystem.net` pada field Email
10. Masukkan password `QaLogin#2026` pada field Password
11. Ketuk tombol [Log in] langsung tanpa melalui verifikasi captcha
12. Verifikasi login berhasil dan aplikasi langsung beralih ke Portal — Product Hub

### Penolakan token Play Integrity kosong atau invalid

13. Logout dari aplikasi mobile dan buka kembali layar Login with Password
14. Simulasikan pengiriman token Play Integrity yang kosong atau tidak valid dari sisi aplikasi ke backend
15. Masukkan email `jokosusilo@qwertysystem.net` dan password `QaLogin#2026`
16. Ketuk tombol [Log in]
17. Verifikasi toast error "Error, failed to log in." tampil di layar aplikasi mobile
18. Verifikasi login gagal, aplikasi tetap berada di layar Login, dan sesi tidak dibuat
19. Pada sesi administrator: Periksa tabel `Global Settings > Activity Log > Session`
20. Verifikasi tercatat tepat 1 baris baru untuk user "Joko S" dengan Status "Failed" dan Note "Captcha not completed"

## Notes

- Platform mobile menggunakan proteksi bawaan OS / Play Integrity sebagai pengganti widget reCAPTCHA web (`PRD §4.6`, `§9.2 F-AUTHLP-04`, `NC-07`).
- Kegagalan verifikasi Play Integrity di mobile menghasilkan toast "Error, failed to log in." dan dicatat di log dengan Note `Captcha not completed` (`NC-07`).
