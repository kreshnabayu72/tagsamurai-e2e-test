---
id: TC-AUTH-OTP-E2E-003-validasi-email-dan-urutan-evaluasi
title: "Validasi Field Email, Batas Karakter, Format Regex, dan Urutan Evaluasi Pra-Request"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-11
  - TC-AUTH-OTP-12
  - TC-AUTH-OTP-13
  - TC-AUTH-OTP-14
  - TC-AUTH-OTP-15
  - TC-AUTH-OTP-16
  - TC-AUTH-OTP-17
  - TC-AUTH-OTP-18
  - TC-AUTH-OTP-167
  - TC-AUTH-OTP-168
coverage:
  web: automated
---

# Validasi Field Email, Batas Karakter, Format Regex, dan Urutan Evaluasi Pra-Request

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP > Request OTP` (`/login/otp`) terbuka di browser.
- User `Rina Permata` (`rinapermata@qwertysystem.co`) terdaftar dan aktif (TLD 2 karakter).
- User `Hendra Fitriani` dengan email tepat 120 karakter (`hendrafitrianixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@qwertysystem.net`) terdaftar dan aktif.
- User `Maya Susanti` (`mayasusanti@qwertysystem.net`) terdaftar dan aktif.
- Widget reCAPTCHA v2 siap diselesaikan atau di-bypass token untuk pengujian validasi input form.

## Test Steps

### Email kosong dan urutan evaluasi awal

1. Buka halaman Request OTP di browser
2. Biarkan field Email kosong
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi caption error inline di bawah field Email adalah "Email must not be empty"
6. Verifikasi tidak ada pengalihan halaman dan form tetap dalam keadaan interaktif
7. Verifikasi pesan "Email must not be empty" muncul mendahului validasi format regex maupun batas karakter (evaluasi tahap 1)

### Validasi format email tidak sesuai standar

8. Masukkan email tanpa simbol `@` (contoh: `budisantosoqwertysystem.net`) ke field Email
9. Klik button [Request OTP]
10. Verifikasi caption error inline adalah "Email format is incorrect"
11. Masukkan email tanpa tanda titik setelah nama domain (contoh: `budisantoso@qwertysystem`)
12. Klik button [Request OTP]
13. Verifikasi caption error inline adalah "Email format is incorrect"
14. Verifikasi bahwa jika input tidak valid secara format, sistem menampilkan "Email format is incorrect" sebelum evaluasi panjang maksimum

### Batas TLD valid 2 karakter dan batas panjang tepat 120 karakter

15. Masukkan email ber-TLD tepat 2 huruf: `rinapermata@qwertysystem.co`
16. Selesaikan reCAPTCHA dan klik [Request OTP]
17. Verifikasi tidak ada penolakan format dan toast sukses pengiriman kode muncul
18. Buka kembali halaman Request OTP
19. Masukkan email tepat 120 karakter: `hendrafitrianixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@qwertysystem.net`
20. Selesaikan reCAPTCHA dan klik [Request OTP]
21. Verifikasi tidak muncul caption error panjang dan request berhasil diproses

### Deteksi real-time batas maksimum 120 karakter dan recovery

22. Masukkan email sepanjang 121 karakter ke field Email (ketik atau tempel karakter ke-121)
23. Verifikasi caption error "Max. 120 characters" langsung muncul secara real-time saat mengetik tanpa perlu klik [Request OTP]
24. Verifikasi seluruh 121 karakter tetap tersimpan di field (tidak terpotong paksa)
25. Klik button [Request OTP] saat caption "Max. 120 characters" aktif
26. Verifikasi request diblokir di sisi client dan caption "Max. 120 characters" tetap bertahan
27. Hapus 1 karakter sehingga panjang string kembali menjadi 120 karakter
28. Verifikasi caption error "Max. 120 characters" otomatis hilang seketika (real-time)

### Sanitasi spasi luar (trimming) sebelum request

29. Masukkan email dengan spasi di awal dan di akhir: `"  mayasusanti@qwertysystem.net  "`
30. Selesaikan reCAPTCHA dan klik [Request OTP]
31. Verifikasi sistem melakukan trim spasi di sisi client/server secara mulus tanpa menampilkan error format
32. Verifikasi toast sukses muncul dan halaman Verify OTP menampilkan subtitle "Enter the 6-digit code sent to: mayasusanti@qwertysystem.net" dalam keadaan bersih dari spasi

## Notes

- Urutan evaluasi field Email mengikuti hirarki: (1) Cek kekosongan string -> "Email must not be empty", (2) Cek regex format -> "Email format is incorrect", (3) Cek batas 120 karakter -> "Max. 120 characters" (sesuai NC-07).
- Karakter ke-121 tidak diblokir dari input agar pengguna menyadari kelebihan karakter melalui caption bantuan.
