---
id: TC-AUTH-RST-E2E-027-layout-aplikasi-android-dan-app-link
title: "Alur Reset Password pada aplikasi native Android: ketiadaan reCAPTCHA dan penanganan App Link"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-06
  - TC-AUTH-RST-07
  - TC-AUTH-RST-08
  - TC-AUTH-RST-09
coverage:
  web: automated
---

# Alur Reset Password pada aplikasi native Android: ketiadaan reCAPTCHA dan penanganan App Link

## Prerequisites

- Pengujian alur mobile aplikasi TAG Samurai Android (`Mode: mock`).
- Device pengujian Android dengan dan tanpa aplikasi TAG Samurai Mobile terpasang.
- Akun uji `budisantoso@qwertysystem.net` berstatus aktif.

## Test Steps

### Screening form Reset Password pada aplikasi Android native

1. Buka aplikasi TAG Samurai Mobile pada perangkat Android
2. Navigasikan ke layar Reset Password dari form Login
3. Verifikasi logo TAG Samurai, title "Reset Password", dan subtitle tampil sesuai desain native
4. Verifikasi field Email tampil dengan label dan placeholder yang sesuai
5. Verifikasi widget Google reCAPTCHA v2 TIDAK dirender pada aplikasi mobile native
6. Verifikasi tombol [Reset Password] tampil dalam keadaan enabled

### Request Reset Password sukses dari aplikasi native tanpa reCAPTCHA

7. Masukkan email "budisantoso@qwertysystem.net" pada field Email
8. Klik tombol [Reset Password] tanpa melalui tahapan captcha
9. Verifikasi server mendeteksi client native (melalui header identitas aplikasi mobile) dan memproses request
10. Verifikasi layar beralih ke tampilan konfirmasi Email Sent! native
11. Verifikasi email reset berhasil terkirim ke kotak masuk pengguna

### Penanganan App Link saat aplikasi terpasang

12. Buka email reset pada perangkat Android yang telah terpasang aplikasi TAG Samurai Mobile
13. Klik tautan reset password di dalam email
14. Verifikasi sistem operasi Android mengaktifkan Android App Link
15. Verifikasi tautan membuka langsung layar Setup New Password di dalam aplikasi TAG Samurai Mobile (bukan browser web)

### Penanganan tautan saat aplikasi belum terpasang

16. Buka tautan reset pada perangkat Android yang belum terpasang aplikasi TAG Samurai Mobile
17. Verifikasi tautan membuka browser web dan secara otomatis mengarahkan pengguna ke halaman unduh aplikasi di toko aplikasi resmi (Google Play Store)

## Notes

- Sesuai PRD §4.3 FI-AUTHRST-11 dan §4.6, aplikasi Android native tidak menggunakan Google reCAPTCHA v2 web widget dan mengandalkan verifikasi identitas aplikasi mobile.
- Sesuai PRD §4.6 dan `TC-AUTH-RST-08/09`, tautan reset mendukung integrasi deep linking / App Link Android untuk membuka langsung alur native jika aplikasi telah terpasang.
