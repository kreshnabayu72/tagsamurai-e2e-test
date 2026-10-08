---
id: TC-AUTH-RST-E2E-003-recaptcha-gate-request
title: "Evaluasi Google reCAPTCHA v2 pada halaman Request Reset: submit tanpa captcha, token expired, dan layanan tidak terjangkau"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-19
  - TC-AUTH-RST-20
  - TC-AUTH-RST-21
  - TC-AUTH-RST-22
  - TC-AUTH-RST-120
  - TC-AUTH-RST-121
coverage:
  web: automated
---

# Evaluasi Google reCAPTCHA v2 pada halaman Request Reset: submit tanpa captcha, token expired, dan layanan tidak terjangkau

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi dengan kemampuan mock network intercept (`Mode: mock`).
- Akun uji `budisantoso@qwertysystem.net` berstatus aktif dan terdaftar.

## Test Steps

### Submit dengan field Email valid tanpa menyelesaikan reCAPTCHA

1. Buka halaman Reset Password di browser web
2. Masukkan email "budisantoso@qwertysystem.net" pada field Email
3. Biarkan widget Google reCAPTCHA v2 dalam keadaan belum dicentang (unsolved)
4. Klik tombol [Reset Password]
5. Verifikasi caption error "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
6. Verifikasi tidak ada permintaan network pengiriman token reset yang diproses ke server

### Submit dengan Email kosong dan reCAPTCHA belum dicentang sekaligus

7. Kosongkan field Email
8. Pastikan widget reCAPTCHA tetap dalam keadaan belum dicentang
9. Klik tombol [Reset Password]
10. Verifikasi caption inline "Email must not be empty" tampil di bawah field Email
11. Verifikasi caption error "Please verify that you are not a robot" tampil di bawah widget reCAPTCHA secara bersamaan
12. Verifikasi kedua pesan error tampil serentak tanpa saling menutupi

### Submit dengan token reCAPTCHA yang kedaluwarsa

13. Masukkan email "budisantoso@qwertysystem.net" pada field Email
14. Selesaikan verifikasi reCAPTCHA
15. Simulasikan token reCAPTCHA kedaluwarsa (expired session pada widget captcha)
16. Klik tombol [Reset Password]
17. Verifikasi caption error "reCAPTCHA verification expired. Please check the box again." tampil di bawah widget reCAPTCHA
18. Verifikasi tombol [Reset Password] tidak mengirimkan payload token kedaluwarsa ke server

### Kegagalan layanan reCAPTCHA provider (Outage)

19. Intercept permintaan verifikasi reCAPTCHA dengan kegagalan koneksi atau error 5xx dari server reCAPTCHA
20. Klik tombol [Reset Password]
21. Verifikasi toast error atau caption penolakan "Verification service is unavailable. Please try again later." tampil di layar
22. Verifikasi form tidak mengirimkan request reset ke endpoint internal TAG Samurai

### Penegakan keamanan server (Defense-in-Depth)

23. Kirimkan HTTP request langsung ke endpoint `/request` tanpa parameter token reCAPTCHA dan tanpa header mobile client
24. Verifikasi server mendeteksi request berasal dari web client dan menolak request dengan status HTTP 400
25. Kirimkan HTTP request langsung ke endpoint `/request` dengan token reCAPTCHA palsu atau invalid
26. Verifikasi server menolak request dengan status HTTP 400 atau 422 dan tidak ada token reset atau email yang diterbitkan

## Notes

- Sesuai keputusan NC-15, saat field Email dan reCAPTCHA sama-sama kosong/belum diselesaikan, kedua caption error ditampilkan bersamaan pada field masing-masing.
- Sesuai PRD §9.4.2 baris 6 dan §9.4.3 Must NOT 3, client web wajib menyertakan token reCAPTCHA yang valid; request tanpa captcha akan ditolak tegas oleh server.
