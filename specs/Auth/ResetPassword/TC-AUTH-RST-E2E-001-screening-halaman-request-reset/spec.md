---
id: TC-AUTH-RST-E2E-001-screening-halaman-request-reset
title: "Screening halaman Reset Password, navigasi bolak-balik dengan Login, dan urutan fokus keyboard Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-01
  - TC-AUTH-RST-02
  - TC-AUTH-RST-03
  - TC-AUTH-RST-04
  - TC-AUTH-RST-05
coverage:
  web: automated
---

# Screening halaman Reset Password, navigasi bolak-balik dengan Login, dan urutan fokus keyboard Tab

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/reset-password`.
- Environment uji terisolasi khusus pengujian otomatis.
- Halaman Login with Password tersedia di URL `/login`.
- Akun uji `budisantoso@qwertysystem.net` tersedia pada sistem.

## Test Steps

### Screening elemen halaman Request Reset Password

1. Buka halaman Reset Password di browser web
2. Verifikasi logo TAG Samurai tampil di bagian header tengah atas
3. Verifikasi title halaman adalah "Reset Password"
4. Verifikasi subtitle halaman adalah "Enter your email and we'll send you a link to reset your password."
5. Verifikasi field Email tampil dengan label "Email", placeholder "Enter your email", dan dalam keadaan kosong
6. Verifikasi widget Google reCAPTCHA v2 tampil dengan status belum diselesaikan (unsolved)
7. Verifikasi caption "Please verify that you are not a robot" tidak tampil pada state awal
8. Verifikasi tombol [Reset Password] tampil dengan styling solid primary, lebar penuh, dan dalam keadaan enabled tanpa spinner
9. Verifikasi link teks "Log in with password" tampil di bagian tengah bawah tombol [Reset Password]
10. Verifikasi tidak ada tombol [Clear Field], tombol tutup [✕], dialog Unsaved Changes, link "Login with OTP", maupun pilihan masa berlaku token pada halaman ini

### Urutan Tab keyboard

11. Klik field Email untuk menempatkan fokus keyboard
12. Tekan tombol Tab pada keyboard lalu verifikasi fokus berpindah ke widget Google reCAPTCHA v2
13. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke tombol [Reset Password]
14. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke link "Log in with password"

### Navigasi bolak-balik dan retensi email antara Login dan Reset Password

15. Buka halaman Login with Password di browser web
16. Ketik "budisantoso@qwertysystem.net" pada field Email di form Login
17. Klik tautan [Reset here] pada halaman Login
18. Verifikasi browser berpindah ke halaman Reset Password
19. Verifikasi field Email di halaman Reset Password terisi otomatis dengan "budisantoso@qwertysystem.net" dan field tetap dapat diedit
20. Klik link teks "Log in with password" pada halaman Reset Password
21. Verifikasi browser kembali ke halaman Login with Password
22. Verifikasi field Email di form Login tetap terisi dengan "budisantoso@qwertysystem.net"

## Notes

- Sesuai PRD §4.2 Deviasi dan `auth-foundation.md` §4.0, data email yang diketik pada alur pra-autentikasi diteruskan antar halaman Login dan Reset Password menggunakan penyimpanan sesi browser (sessionStorage) yang bertahan hingga tab ditutup.
- Sesuai PRD §4.2 Deviasi, form Request Reset tidak memiliki tombol [Clear Field] atau dialog Unsaved Changes.
