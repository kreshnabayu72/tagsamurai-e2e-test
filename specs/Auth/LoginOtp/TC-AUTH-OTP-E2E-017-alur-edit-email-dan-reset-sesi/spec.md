---
id: TC-AUTH-OTP-E2E-017-alur-edit-email-dan-reset-sesi
title: "Alur Edit Email dari Verify OTP dan Reset Sesi Email-Request"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-86
  - TC-AUTH-OTP-87
  - TC-AUTH-OTP-88
  - TC-AUTH-OTP-89
  - TC-AUTH-OTP-94
  - TC-AUTH-OTP-95
  - TC-AUTH-OTP-96
coverage:
  web: automated
---

# Alur Edit Email dari Verify OTP dan Reset Sesi Email-Request

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Surya Utami` (`suryautami@qwertysystem.net`) profil BASE.
- User `Nadia Safitri` (`nadiasafitri@qwertysystem.net`) profil BASE.
- User `Bambang Baru` (`bambangbaru@qwertysystem.net`) profil BASE.
- Mail-catcher aktif.

## Test Steps

### Klik tautan Edit email dan navigasi keyboard

1. Buka halaman Request OTP, masukkan `suryautami@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
2. Verifikasi halaman Verify OTP tampil
3. Arahkan fokus keyboard menggunakan tombol Tab ke tautan [Edit email]
4. Tekan tombol [Enter] atau [Space] pada tautan [Edit email]
5. Verifikasi browser kembali ke halaman Request OTP
6. Verifikasi field Email terisi dengan `suryautami@qwertysystem.net` dan berada dalam keadaan fokus/dapat disunting
7. Verifikasi widget reCAPTCHA berada dalam status belum dicentang (unchecked, sesuai NC-09)

### Edit email ke email baru memulai sesi baru

8. Ubah teks pada field Email menjadi `bambangbaru@qwertysystem.net`
9. Centang widget reCAPTCHA dan klik button [Request OTP]
10. Verifikasi halaman Verify OTP tampil dengan subtitle baru: "Enter the 6-digit code sent to: bambangbaru@qwertysystem.net"
11. Verifikasi counter resend dan kuota dimulai dari awal (bersih) untuk alamat email yang baru

### Reset sesi setelah kuota habis via Edit Email (NC-03)

12. Buka Verify OTP untuk `nadiasafitri@qwertysystem.net` yang kuota resend-nya telah habis (state Exhausted)
13. Klik tautan [Edit email] untuk kembali ke Request OTP
14. Klik button [Request OTP] kembali setelah menyelesaikan reCAPTCHA
15. Verifikasi sistem memperlakukan alur Edit Email sebagai pembukaan sesi email-request baru sehingga request diterima dan kode baru diterbitkan (sesuai konsensus NC-03)

### Navigasi Use password instead dari halaman Request OTP pasca-edit

16. Pada halaman Request OTP hasil klik [Edit email], ubah email menjadi `user.edited@qwertysystem.net`
17. Klik tautan [Use password instead]
18. Verifikasi halaman Login with Password terbuka dengan field Email terisi `user.edited@qwertysystem.net`

## Notes

- Alur "Edit email" dirancang sebagai escape hatch resmi: jika user salah mengetik email atau kuota pengiriman habis pada satu sesi, pengguna dapat memperbaiki email atau memulai sesi baru melalui alur ini (NC-03).
- Widget reCAPTCHA wajib diselesaikan ulang setiap kali user kembali ke layar Request OTP via alur Edit email (NC-09).
