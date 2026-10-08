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
  - TC-AUTH-LP-27
  - TC-AUTH-LP-156
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

### Plus-addressing diterima dan login diproses

37. Ganti isi field Email dengan `budisantoso+qa@qwertysystem.net` (mengandung karakter `+`)
38. Verifikasi caption inline "Email format is incorrect" tidak tampil (plus-addressing diterima sistem)
39. Selesaikan reCAPTCHA lalu klik tombol [Log in]
40. Verifikasi login berhasil dan browser menuju Portal — Product Hub (plus-addressing diproses seperti email biasa)
41. Logout dan buka kembali halaman Login with Password

### Kapitalisasi email bersifat case-insensitive

42. Masukkan email `BudiSantoso@QwertySystem.net` (kapitalisasi campuran) pada field Email
43. Masukkan password `Spectra.env.AUTH_PASSWORD` pada field Password
44. Selesaikan reCAPTCHA lalu klik tombol [Log in]
45. Verifikasi caption inline "Email is not registered yet" tidak tampil
46. Verifikasi login berhasil dan browser menuju Portal — Product Hub dengan sesi milik `budisantoso@qwertysystem.net`
47. Logout dan buka kembali halaman Login with Password

## Notes

- Spec ini mencakup screening struktur login form serta validasi format dan normalisasi (plus-addressing, case-insensitive) pada input Email; uji keamanan injeksi SQL/XSS dipecah ke E2E-024 dan uji batas panjang karakter (120/121, format menang atas panjang) dipecah ke E2E-029 (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).
- Sesuai PRD `V-AUTHLP-02` dan `auth-foundation.md` §4.0a, karakter `+` (plus-addressing) diterima sebagai format email valid dan login diproses ke akun yang sama; kapitalisasi email bersifat case-insensitive (`TC-AUTH-LP-27`, `TC-AUTH-LP-156`).
