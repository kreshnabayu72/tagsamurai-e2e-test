---
id: TC-AUTH-OTP-E2E-003-mobile-screening-request-dan-verify
title: "Tampilan Mobile Halaman Request OTP Tanpa reCAPTCHA dan Keypad Numerik pada Halaman Verify OTP"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-02
  - TC-AUTH-OTP-08
coverage:
  mobile: automated
---

# Tampilan Mobile Halaman Request OTP Tanpa reCAPTCHA dan Keypad Numerik pada Halaman Verify OTP

## Prerequisites

- Mode: FE+BE (mobile Android). Aplikasi mobile TAG Samurai terpasang pada perangkat atau emulator Android, belum login, dan halaman `Auth > Login with Password` dapat dibuka dari aplikasi.
- Tidak ada widget reCAPTCHA di aplikasi mobile; spec tidak mencentang apa pun.
- Environment variable: `OTP_PASSWORD` (password user uji Activated yang di-seed). Tidak ada password atau token di spec atau fixture.
- TC-AUTH-OTP-02 tidak membuat atau memakai data user: layar hanya dibuka dan dibaca.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-08: `Rizky Damayanti` (`rizkydamayanti+{runId}-003@qwertysystem.net`), profil BASE
- Kemampuan teknis: perangkat atau emulator Android; pengamatan keypad numerik perangkat (terbuka atau tidak) dan tata letak layar pada Android.
- Mail-catcher tidak dipakai (lihat Notes).
- Tidak ada state global yang diubah.

## Test Steps

### TC-AUTH-OTP-02: Halaman Request OTP di aplikasi mobile tidak merender widget reCAPTCHA

1. Buka aplikasi mobile TAG Samurai pada halaman Login with Password
2. Ketuk tautan [Log in with OTP]
3. Verifikasi halaman Request OTP tampil
4. Susuri halaman dari atas ke bawah
5. Verifikasi field Email tampil
6. Verifikasi button [Request OTP] tampil
7. Verifikasi widget reCAPTCHA "I'm not a robot" tidak dirender
8. Verifikasi tidak ada ruang kosong pengganti widget reCAPTCHA
9. Verifikasi kontainer melebar penuh
10. Verifikasi kontainer tanpa bayangan kartu
11. Verifikasi tautan [Use password instead] tampil di bagian bawah

### TC-AUTH-OTP-08: Kursor aktif di kotak 1 dan keypad numerik terbuka di perangkat mobile saat halaman Verify OTP tampil

12. Buka ulang halaman Request OTP di aplikasi mobile
13. Ketik `rizkydamayanti+{runId}-003@qwertysystem.net` pada field Email di halaman Request OTP
14. Ketuk button [Request OTP]
15. Verifikasi halaman Verify OTP tampil
16. Verifikasi kursor aktif pada kotak digit 1 tanpa ketukan tambahan
17. Verifikasi keypad numerik perangkat terbuka otomatis
18. Verifikasi tidak ada widget reCAPTCHA pada alur permintaan kode ini
19. Verifikasi tata letak mobile: kontainer melebar penuh
20. Verifikasi tata letak mobile: kontainer tanpa bayangan kartu
21. Verifikasi tautan [Edit email] tampil di bawah Subtitle
22. Verifikasi 6 kotak digit tampil dalam satu baris tunggal
23. Verifikasi tautan [Back to Login with Password] tampil di bagian bawah layar
24. Ketik digit `4`, `8`, `1`, `9`, `0` satu per satu pada keypad
25. Verifikasi keypad numerik tetap terbuka saat kursor berpindah dari kotak 2 sampai kotak 6

## Notes

- Mode: FE+BE (mobile Android, `coverage.mobile: automated`). Sumber: `auth/login-otp/TestCases/tc-login-otp.md`. Kedua TC bertanda Automation `Manual Only` di sumber karena butuh perangkat Android; kebutuhan itu ditulis di Prerequisites sesuai bagian 2 konvensi.
- Langkah 12 adalah langkah penghubung (membuka ulang halaman Request OTP agar TC-AUTH-OTP-08 mulai dari field Email kosong), tanpa asersi (S-03).
- Digit yang diketik pada langkah 24 hanya 5 digit sehingga verifikasi otomatis tidak terpicu; kode OTP tidak dibaca dari email pada spec ini, sehingga mail-catcher tidak dibutuhkan.
- Temuan untuk QA:
  - Request OTP di aplikasi mobile tanpa reCAPTCHA mungkin bergantung pada token attestation (Play Integrity) yang valid di perangkat atau emulator, tetapi TC-AUTH-OTP-02 dan TC-AUTH-OTP-08 tidak menyebut kebutuhan itu; spec tidak menjadikannya Prerequisites (TC-AUTH-OTP-180 dan 185 yang menyebutnya ada di E2E-004). Mohon QA mengonfirmasi apakah Play Integrity valid diperlukan pada kedua TC ini.
  - TC-AUTH-OTP-02 Pre-setup menyebut user `Siti Lestari` (BASE), tetapi langkah dan Expected hanya membaca layar Request OTP; spec tidak men-seed user itu.
  - TC-AUTH-OTP-02 langkah 1 memuat dua aksi sekaligus ("Buka aplikasi mobile → halaman Request OTP tampil (dari tautan Log in with OTP pada Login with Password)"); spec menguraikannya menjadi membuka Login with Password lalu mengetuk [Log in with OTP].
  - TC-AUTH-OTP-08 precondition c menyebut mail-catcher, tetapi tidak ada langkah atau Expected yang membaca email; spec tidak memakainya.
