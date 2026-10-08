---
id: TC-AUTH-OTP-E2E-002-mobile-request-dan-keypad
title: "Tampilan Mobile Tanpa reCAPTCHA, Keypad Numerik Otomatis, dan Attestation Token"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-02
  - TC-AUTH-OTP-08
  - TC-AUTH-OTP-180
  - TC-AUTH-OTP-185
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
- Failure injection harness untuk mensimulasikan token attestation kosong atau tidak valid (untrusted device).
- Akun Total Control Global Settings aktif untuk memverifikasi entri log.

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

### Permintaan kode OTP dengan Play Integrity Attestation Token yang sah

17. Kembali ke halaman Request OTP pada aplikasi mobile
18. Masukkan email `rizkysantoso@qwertysystem.net`
19. Ketuk button [Request OTP] dengan payload attestation token dari aplikasi
20. Verifikasi request diterima oleh backend tanpa penolakan reCAPTCHA
21. Verifikasi toast "Success, the code has been sent." tampil dan halaman Verify OTP terbuka
22. Verifikasi email OTP masuk ke inbox mail-catcher untuk `rizkysantoso@qwertysystem.net`

### Penolakan attestation token kosong atau invalid pada Request OTP (EC-51, TC-185)

23. Buka halaman Request OTP pada aplikasi mobile dengan kondisi attestation injection dimatikan (token kosong atau dimanipulasi menjadi invalid)
24. Masukkan email `rizkysantoso@qwertysystem.net`
25. Ketuk button [Request OTP]
26. Verifikasi backend menolak permintaan dengan status HTTP 422 (diperlakukan sebagai captcha kosong)
27. Verifikasi toast error tampil dengan pesan: "Error, failed to log in."
28. Verifikasi aplikasi tetap berada di halaman Request OTP dan tidak ada email OTP yang dikirimkan
29. Di sesi admin Total Control: buka `Global Settings > Activity Log > Session`
30. Verifikasi tercatat tepat 1 entri baru dengan Activity "Login", Status "Failed", dan Note "Captcha not completed"

### Penolakan attestation token invalid pada Resend Code (EC-52, TC-185)

31. Pulihkan attestation valid, ulangi langkah Request OTP hingga halaman Verify OTP tampil untuk `rizkysantoso@qwertysystem.net`
32. Catat kode OTP asli yang masih aktif
33. Tunggu hingga countdown 60 detik selesai dan tombol [Resend code] aktif
34. Simulasikan attestation token kembali invalid saat mengetuk [Resend code]
35. Verifikasi toast error tampil dengan pesan: "Error, failed to send the code."
36. Verifikasi kode OTP lama yang sebelumnya terbit tetap berstatus valid
37. Verifikasi TIDAK ADA entri log baru yang dicatat di Activity Log Session (karena kegagalan Resend tidak pernah dicatat di log)

### Verify OTP tidak mensyaratkan token reCAPTCHA maupun attestation (EC-53)

38. Pada halaman Verify OTP mobile yang sama, masukkan 6 digit kode OTP valid
39. Verifikasi verifikasi berhasil diproses dan pengguna berhasil login masuk ke Portal/Product Hub
40. Verifikasi bahwa tahap Verify tidak memvalidasi ulang attestation token maupun reCAPTCHA token karena platform sesi sudah ditetapkan sejak tahap Request OTP

## Notes

- Platform mobile tidak menggunakan reCAPTCHA v2 checkbox; verifikasi bot digantikan oleh Play Integrity / Device Attestation token di level native app.
- Sesuai PRD §9.2 F-AUTHOTP-09 dan EC-51–EC-53:
  - Bukti klien mobile (attestation token) diverifikasi server strictly pada Request OTP dan Resend.
  - Attestation invalid pada Request OTP ditolak 422, memunculkan toast "Error, failed to log in.", dan dicatat Failed / `Captcha not completed`.
  - Attestation invalid pada Resend memunculkan toast "Error, failed to send the code.", kode lama tetap valid, dan tidak dicatat di log.
  - Layar Verify OTP tidak mensyaratkan reCAPTCHA maupun attestation; platform verifikasi mengikuti sesi Request OTP.
