---
id: TC-AUTH-OTP-E2E-001-screening-request-otp
title: "Screening Halaman Request OTP, Prefill Email dari Login with Password, dan Sanitasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-01
  - TC-AUTH-OTP-03
  - TC-AUTH-OTP-04
  - TC-AUTH-OTP-05
  - TC-AUTH-OTP-10
  - TC-AUTH-OTP-101
  - TC-AUTH-OTP-157
coverage:
  web: automated
---

# Screening Halaman Request OTP, Prefill Email dari Login with Password, dan Sanitasi

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif / belum login).
- User `Budi Santoso` (`budisantoso@qwertysystem.net`) berstatus Activated dan Active (profil BASE).
- User `Andi Wulandari` (`andiwulandari@qwertysystem.net`) berstatus Activated dan Active (profil BASE).
- User `Agus Wijaya` (`aguswijaya@qwertysystem.net`) terdaftar dengan role Read Only di Global Settings (profil BASE).
- Mail-catcher lingkungan uji aktif untuk verifikasi penerimaan kode OTP.
- Environment web uji siap menerima akses publik pada rute `/login` dan `/login/otp`.

## Test Steps

### Screening elemen UI halaman Request OTP

1. Buka halaman `Auth > Login with OTP > Request OTP` (`/login/otp`) di browser
2. Verifikasi card form tampil terpusat di layar dengan logo TAG Samurai di bagian atas
3. Verifikasi title halaman adalah "Log in with OTP"
4. Verifikasi subtitle di bawah title adalah "We'll send a 6-digit verification code to your email"
5. Verifikasi field Email tampil dengan label "Email", placeholder "Enter your email", dalam keadaan kosong, dan tanpa caption error
6. Verifikasi widget Google reCAPTCHA v2 "I'm not a robot" tampil dalam keadaan belum dicentang dan tanpa caption error
7. Verifikasi button [Request OTP] tampil melebar penuh (variant solid, severity primary) dalam keadaan enabled
8. Verifikasi tautan [Use password instead] tampil terpusat di bawah button [Request OTP]
9. Verifikasi tidak ada checkbox Agreement, kotak digit OTP, tombol [Verify], tombol [Continue ➔], area Resend, maupun tautan [Edit email] di halaman ini

### Prefill dan kelanjutan input email dari Login with Password

10. Buka halaman `Auth > Login with Password` (`/login`)
11. Ketik `andiwulandari@qwertysystem.net` pada field Email
12. Klik tautan [Log in with OTP]
13. Verifikasi halaman berpindah ke `Auth > Login with OTP > Request OTP`
14. Verifikasi field Email otomatis terisi dengan `andiwulandari@qwertysystem.net`
15. Verifikasi field Email tetap dapat diedit dan widget reCAPTCHA dalam keadaan belum dicentang
16. Buka kembali halaman `Auth > Login with Password` (`/login`)
17. Ketik email tidak lengkap `john@` pada field Email
18. Klik tautan [Log in with OTP]
19. Verifikasi halaman Request OTP tampil dengan field Email terisi `john@` apa adanya tanpa caption error inline

### Buka halaman Request OTP secara langsung tanpa parameter

20. Buka rute `/login/otp` secara langsung di browser tanpa query parameter atau riwayat sesi
21. Verifikasi field Email bersih (kosong) dan menampilkan placeholder "Enter your email"
22. Verifikasi button [Request OTP] enabled dan widget reCAPTCHA belum dicentang

### Aksesibilitas publik tanpa batasan role atau capability

23. Pada halaman Request OTP, masukkan email `aguswijaya@qwertysystem.net` (user dengan role Read Only)
24. Centang widget reCAPTCHA "I'm not a robot"
25. Klik button [Request OTP]
26. Verifikasi toast "Success, the code has been sent." tampil dan halaman berpindah ke Verify OTP
27. Ambil 6 digit kode dari mail-catcher untuk `aguswijaya@qwertysystem.net` dan masukkan ke kotak digit
28. Verifikasi verifikasi otomatis berhasil dan browser diarahkan ke Portal — Product Hub dengan sesi aktif milik `Agus Wijaya` tanpa ada pemblokiran hak akses role

### Sanitasi input email terhadap karakter kontrol dan payload injection

29. Buka kembali halaman Request OTP dalam sesi baru
30. Ketik input yang disisipi karakter spasi tersembunyi/tab/kontrol: `"  budisantoso@qwertysystem.net  "`
31. Centang reCAPTCHA dan klik [Request OTP]
32. Verifikasi sistem melakukan trim spasi di awal dan akhir secara otomatis dan mengirim kode ke `budisantoso@qwertysystem.net`
33. Buka kembali halaman Request OTP, masukkan input payload script injection `<script>alert(1)</script>user@qwertysystem.net`
34. Klik [Request OTP]
35. Verifikasi input di-sanitize dan ditolak dengan caption "Email format is incorrect" tanpa mengeksekusi script atau memicu error rendering XSS

## Notes

- Modul Login with OTP adalah modul publik pra-autentikasi sehingga tidak memiliki pemeriksaan role/capability sebelum login.
- Pengetikan email pada Login with Password terbawa ke Request OTP melalui state/URL parameter yang di-sanitize.
- Karakter kontrol dan spasi luar selalu di-trim sebelum evaluasi regex format.
