---
id: TC-AUTH-LP-E2E-002-screening-dan-validasi-field-password
title: Screening dan validasi field Password serta toggle intip
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-03
  - TC-AUTH-LP-19
  - TC-AUTH-LP-20
  - TC-AUTH-LP-23
coverage:
  web: automated
---

# Screening dan validasi field Password serta toggle intip

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `budisantoso@qwertysystem.net` aktif dengan password `QaLogin#2026`.
- User `jokosusilo@qwertysystem.net` aktif dengan hitungan gagal 0.
- Password rahasia diambil dari environment variable dan fixture.

## Test Steps

### Toggle intip mask dan unmask

1. Buka halaman Login with Password di browser web
2. Masukkan password `QaLogin#2026` pada field Password
3. Verifikasi teks password tersembunyi (tipe input bernilai `password`)
4. Klik ikon toggle intip pada field Password
5. Verifikasi teks password terlihat apa adanya (`QaLogin#2026`) dan tipe input berubah menjadi `text`
6. Klik ikon toggle intip sekali lagi
7. Verifikasi teks password kembali tersembunyi (masked)
8. Arahkan kursor mouse ke ikon toggle intip dan verifikasi tidak ada tooltip yang muncul

### Validasi field Password wajib diisi

9. Masukkan email valid `jokosusilo@qwertysystem.net` pada field Email
10. Kosongkan field Password
11. Selesaikan reCAPTCHA
12. Klik tombol [Log in]
13. Verifikasi caption inline "Password must not be empty" tampil tepat di bawah field Password
14. Verifikasi Alert pesan server tidak tampil
15. Verifikasi field Email tetap terisi `jokosusilo@qwertysystem.net` dan tidak ada sesi yang terbentuk

### Sensitivitas huruf besar dan kecil (Case-Sensitivity)

16. Masukkan email `budisantoso@qwertysystem.net` pada field Email
17. Masukkan password dengan huruf kecil semua `qalogin#2026` pada field Password
18. Selesaikan reCAPTCHA
19. Klik tombol [Log in]
20. Verifikasi Alert Danger "Incorrect email or password" tampil tepat di atas tombol [Log in]
21. Verifikasi field Password dikosongkan secara otomatis setelah penolakan kredensial

### Penanganan karakter khusus pada Password

22. Buka kembali halaman Login with Password dalam keadaan logout
23. Masukkan email `jokosusilo@qwertysystem.net` pada field Email
24. Masukkan kombinasi karakter khusus yang salah `x'"<>&%$#@!` pada field Password
25. Selesaikan reCAPTCHA
26. Klik tombol [Log in]
27. Verifikasi Alert Danger "Incorrect email or password" tampil di atas tombol [Log in]
28. Verifikasi sistem tidak menghasilkan error 500 atau unhandled exception saat menerima karakter kutip dan simbol

## Notes

- Karakter spasi pada field Password tidak boleh di-trim oleh FE maupun BE; spasi diperlakukan sebagai bagian utuh dari kredensial password.
- Password salah selalu menghasilkan Alert Danger "Incorrect email or password" di atas tombol [Log in] sesuai NC-05.
- Pengujian verifikasi spasi password (`TC-AUTH-LP-21`, `TC-AUTH-LP-22`) berstatus Manual Only karena fixture password berspasi hanya dapat diset langsung oleh tim BE; tidak dicakup spec automation ini.
