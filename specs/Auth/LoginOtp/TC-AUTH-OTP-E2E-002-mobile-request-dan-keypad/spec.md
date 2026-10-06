---
id: TC-AUTH-OTP-E2E-002-mobile-request-dan-keypad
title: "Tampilan Mobile Tanpa reCAPTCHA, Keypad Numerik Otomatis, dan Attestation Token"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-02
  - TC-AUTH-OTP-08
  - TC-AUTH-OTP-180
coverage:
  mobile: automated
---

# Tampilan Mobile Tanpa reCAPTCHA, Keypad Numerik Otomatis, dan Attestation Token

## Prerequisites

- Mode: mobile. Skenario dijalankan pada aplikasi mobile TAG Samurai (Android) atau emulator dengan Play Integrity terkonfigurasi.
- Belum login dan session kosong.
- User `Siti Lestari` (`sitilestari@qwertysystem.net`) profil BASE (Tabel Data Uji Pre-setup #2).
- User `Rizky Damayanti` (`rizkydamayanti@qwertysystem.net`) profil BASE (Tabel Data Uji Pre-setup #2).
- User `Rizky Santoso` (`rizkysantoso@qwertysystem.net`) profil BASE (Tabel Data Uji Pre-setup #2).
- Mail-catcher lingkungan uji aktif untuk verifikasi penerimaan kode OTP.
- Attestation token (Google Play Integrity) aktif pada runtime perangkat mobile uji.

## Test Steps

### Screening halaman Request OTP pada platform mobile

1. Buka aplikasi mobile TAG Samurai pada halaman Login with Password
2. Ketuk tautan [Log in with OTP] untuk membuka halaman Request OTP
3. Verifikasi tata letak mobile melebar penuh (full width canvas) tanpa bayangan card
4. Verifikasi title "Log in with OTP" dan subtitle "We'll send a 6-digit verification code to your email" tampil
5. Verifikasi field Email dan button [Request OTP] tampil
6. Verifikasi widget reCAPTCHA "I'm not a robot" tidak dirender dan tidak ada ruang kosong pengganti widget
7. Verifikasi tautan [Use password instead] tampil di bagian bawah layar

### Verifikasi keypad numerik dan autofokus pada halaman Verify OTP mobile

8. Masukkan email `rizkydamayanti@qwertysystem.net` pada field Email
9. Ketuk button [Request OTP]
10. Verifikasi halaman Verify OTP mobile tampil
11. Verifikasi kursor aktif otomatis pada kotak digit 1 tanpa perlu ketukan manual
12. Verifikasi soft keyboard perangkat mobile yang terbuka adalah keypad numerik (hanya angka 0-9)
13. Ketik digit "4"
14. Verifikasi kursor otomatis berpindah ke kotak 2 dan keypad numerik tetap terbuka
15. Ketik digit "8", "1", "9", "0" berturut-turut
16. Verifikasi keypad numerik tetap aktif hingga kotak ke-5 terisi

### Permintaan kode OTP dengan Play Integrity Attestation Token

17. Kembali ke halaman Request OTP pada aplikasi mobile
18. Masukkan email `rizkysantoso@qwertysystem.net`
19. Ketuk button [Request OTP] dengan payload attestation token dari aplikasi
20. Verifikasi request diterima oleh backend tanpa penolakan reCAPTCHA
21. Verifikasi toast "Success, the code has been sent." tampil dan halaman Verify OTP terbuka
22. Verifikasi email OTP masuk ke inbox mail-catcher untuk `rizkysantoso@qwertysystem.net`

## Notes

- Platform mobile tidak menggunakan reCAPTCHA v2 checkbox; verifikasi bot digantikan oleh Play Integrity / Device Attestation token di level native app.
- Desain antarmuka mobile memanfaatkan lebar penuh viewport tanpa kontainer kartu desktop.
- Input digit 6-kotak di mobile wajib mengaktifkan atribut inputMode="numeric" untuk memastikan keypad angka muncul secara default.
