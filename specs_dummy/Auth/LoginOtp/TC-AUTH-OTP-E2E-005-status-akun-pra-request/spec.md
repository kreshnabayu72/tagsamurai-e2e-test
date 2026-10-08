---
id: TC-AUTH-OTP-E2E-005-status-akun-pra-request
title: "Evaluasi Status Akun Pra-Request: Belum Terdaftar, Belum Aktivasi, dan Akun Inactive"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-19
  - TC-AUTH-OTP-20
  - TC-AUTH-OTP-21
coverage:
  web: automated
---

# Evaluasi Status Akun Pra-Request: Belum Terdaftar, Belum Aktivasi, dan Akun Inactive

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP > Request OTP` (`/login/otp`) terbuka di browser.
- Email belum terdaftar: `unregistered_user@qwertysystem.net` (format valid, tidak terdaftar di sistem).
- User `Fajar Lubis` (`fajarlubis@qwertysystem.net`) berstatus Pending Activation (profil PENDING).
- User `Putri Suryani` (`putrisuryani@qwertysystem.net`) berstatus Inactive / Toggle Global OFF (profil INACTIVE).
- Akun admin Total Control Global Settings aktif untuk membaca Activity Log > Session dan User Detail > User Log.

## Test Steps

### Email belum terdaftar ditolak dengan pesan spesifik tanpa log

1. Buka halaman Request OTP di browser
2. Masukkan email `unregistered_user@qwertysystem.net`
3. Centang widget reCAPTCHA dan klik button [Request OTP]
4. Verifikasi caption error inline di bawah field Email adalah "Email is not registered yet"
5. Verifikasi tidak ada kode yang diterbitkan dan form tetap di halaman Request OTP
6. Login sebagai Total Control Global Settings di tab terpisah
7. Buka `Global Settings > Activity Log > Session`
8. Verifikasi tidak ada entri baru yang tercatat untuk submit email yang belum terdaftar

### Akun belum aktivasi ditolak dan dicatat log dengan Note Account not activated

9. Logout admin dan buka kembali halaman Request OTP dalam keadaan sesi kosong
10. Masukkan email `fajarlubis@qwertysystem.net` (profil PENDING)
11. Centang reCAPTCHA dan klik button [Request OTP]
12. Verifikasi caption error inline di bawah field Email adalah "Your account has not been activated yet"
13. Verifikasi tautan atau petunjuk aktivasi tidak membocorkan kredensial
14. Buka sesi admin Total Control di tab terpisah
15. Buka `Global Settings > User > Detail (Fajar Lubis) > User Log`
16. Verifikasi terdapat satu entri baru dengan Status "Failed" dan Note "Account not activated"
17. Buka `Global Settings > Activity Log > Session` dan verifikasi entri yang sama tercatat dengan IP dan timestamp yang sesuai

### Akun inactive ditolak dan dicatat log dengan Note Account is inactive

18. Logout admin dan buka kembali halaman Request OTP
19. Masukkan email `putrisuryani@qwertysystem.net` (profil INACTIVE)
20. Centang reCAPTCHA dan klik button [Request OTP]
21. Verifikasi caption error inline di bawah field Email adalah "Your account is inactive"
22. Verifikasi kode OTP tidak diterbitkan ke email tersebut
23. Buka sesi admin Total Control di tab terpisah
24. Buka `Global Settings > User > Detail (Putri Suryani) > User Log`
25. Verifikasi terdapat satu entri baru dengan Status "Failed" dan Note "Account is inactive"
26. Buka `Global Settings > Activity Log > Session` dan verifikasi entri yang sama tercatat pada surface session

## Notes

- TAG Samurai membedakan secara tegas status akun: email belum terdaftar (tidak ada subjek user, tidak dicatat log), belum aktivasi (dicatat `Account not activated`), dan akun nonaktif (dicatat `Account is inactive`).
- Penolakan status akun terjadi di fase pra-request saat lookup akun di backend, sebelum kode OTP digenerate dan dikirim via email provider.
