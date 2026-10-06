---
id: TC-AUTH-LP-E2E-001-screening-dan-validasi-field-email
title: Screening halaman Login with Password dan validasi field Email
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-01
  - TC-AUTH-LP-02
  - TC-AUTH-LP-04
  - TC-AUTH-LP-10
  - TC-AUTH-LP-11
  - TC-AUTH-LP-12
  - TC-AUTH-LP-13
  - TC-AUTH-LP-14
  - TC-AUTH-LP-15
  - TC-AUTH-LP-16
  - TC-AUTH-LP-17
  - TC-AUTH-LP-27
  - TC-AUTH-LP-144
  - TC-AUTH-LP-145
coverage:
  web: automated
---

# Screening halaman Login with Password dan validasi field Email

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- Environment uji terisolasi khusus pengujian otomatis.
- Password valid `Spectra.env.AUTH_PASSWORD` tersedia di environment variables.
- Data fixture `Fixture.authLoginPassword` tersedia untuk nilai email valid, format tidak valid, batas karakter, dan payload injection.
- Endpoint reCAPTCHA dapat diselesaikan otomatis atau dilewati melalui token bypass uji automation.

## Test Steps

### Screening elemen halaman dan state awal

1. Buka halaman Login with Password di browser web
2. Verifikasi logo TAG Samurai tampil di bagian header
3. Verifikasi title halaman adalah "Login with Password"
4. Verifikasi subtitle halaman adalah "Sign in and start managing your assets"
5. Verifikasi field Email tampil dengan label "Email *", placeholder "Enter your email", dan dalam keadaan kosong
6. Verifikasi field Password tampil dengan label "Password *", placeholder "Enter your password", karakter tersembunyi (masked), dan ikon toggle intip tampil
7. Verifikasi widget Google reCAPTCHA v2 tampil dengan status Unsolved
8. Verifikasi tombol [Log in] tampil dengan styling solid primary, lebar penuh, dan dalam keadaan enabled
9. Verifikasi link navigasi [Log in with OTP] dan "Forgot your password? " [Reset here] tampil di bawah tombol [Log in]
10. Verifikasi tidak ada checkbox Agreement, tombol [Clear Field], tombol [Submit], tombol [Save], maupun tombol tutup [✕] pada halaman Login

### Urutan Tab keyboard

11. Klik field Email untuk meletakkan fokus
12. Tekan tombol Tab pada keyboard lalu verifikasi fokus berpindah ke field Password
13. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke ikon toggle intip Password
14. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke widget reCAPTCHA
15. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke tombol [Log in]
16. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke link [Log in with OTP]
17. Tekan tombol Tab lagi lalu verifikasi fokus berpindah ke link [Reset here]

### Validasi field Email wajib diisi

18. Kosongkan field Email
19. Isi field Password dengan `Spectra.env.AUTH_PASSWORD`
20. Selesaikan reCAPTCHA
21. Klik tombol [Log in]
22. Verifikasi caption inline "Email must not be empty" tampil tepat di bawah field Email
23. Verifikasi Alert pesan server tidak tampil
24. Verifikasi tidak ada sesi yang dibuat dan browser tetap berada di halaman Login

### Validasi format Email dan timing blur

25. Ketik `budisantoso@` pada field Email
26. Klik field Password tanpa menekan tombol [Log in] (field Email kehilangan fokus / blur)
27. Verifikasi caption inline "Email format is incorrect" langsung tampil di bawah field Email sebelum submit
28. Hapus karakter `@` sehingga menjadi `budisantoso.qwertysystem.net` (tanpa `@`)
29. Selesaikan reCAPTCHA lalu klik tombol [Log in]
30. Verifikasi caption inline "Email format is incorrect" tetap tampil di bawah field Email
31. Ganti isi field Email dengan `budisantoso@qwertysystem` (tanpa titik domain)
32. Selesaikan reCAPTCHA lalu klik tombol [Log in]
33. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
34. Ganti isi field Email dengan `budisantoso@qwertysystem.n` (karakter TLD setelah titik kurang dari 2)
35. Selesaikan reCAPTCHA lalu klik tombol [Log in]
36. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
37. Ganti isi field Email dengan `budisantoso+qa@qwertysystem.net` (mengandung karakter `+`)
38. Selesaikan reCAPTCHA lalu klik tombol [Log in]
39. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email sesuai regex sistem

### Validasi batas panjang karakter Email

40. Masukkan email dengan total 120 karakter (103 karakter `a` diikuti `@qwertysystem.net`) yang belum terdaftar
41. Selesaikan reCAPTCHA lalu klik tombol [Log in]
42. Verifikasi caption "Max. 120 characters" tidak tampil
43. Verifikasi caption inline "Email is not registered yet" tampil di bawah field Email, membuktikan 120 karakter lolos validasi panjang
44. Ketik 1 karakter tambahan pada field Email sehingga panjangnya menjadi 121 karakter
45. Verifikasi caption inline "Max. 120 characters" langsung muncul saat mengetik sebelum tombol [Log in] diklik
46. Selesaikan reCAPTCHA lalu klik tombol [Log in]
47. Verifikasi tombol [Log in] diblokir dan caption "Max. 120 characters" tetap bertahan di bawah field Email

### Keamanan validasi format (SQL Injection dan XSS)

48. Ganti isi field Email dengan string injeksi SQL `' OR 1=1 --`
49. Selesaikan reCAPTCHA lalu klik tombol [Log in]
50. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
51. Verifikasi tidak ada error server 500 atau kebocoran data database
52. Ganti isi field Email dengan string script `<script>alert(1)</script>`
53. Selesaikan reCAPTCHA lalu klik tombol [Log in]
54. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
55. Verifikasi teks ditampilkan sebagai teks murni tanpa ada dialog alert atau eksekusi script

## Notes

- Spec ini menggabungkan seluruh screening struktur login form dan validasi format, batasan karakter, serta sanitasi keamanan pada input Email.
- Sesuai PRD §9.9 dan LLD §2, regex validasi email menolak karakter `+` sebagai format tidak valid (`NC-16`).
- Batas maksimal 120 karakter memicu pesan "Max. 120 characters" secara langsung saat pengetikan melebihi kuota (`NC-08`).
