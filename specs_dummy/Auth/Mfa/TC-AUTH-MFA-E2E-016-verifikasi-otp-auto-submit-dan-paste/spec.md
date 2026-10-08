---
id: TC-AUTH-MFA-E2E-016-verifikasi-otp-auto-submit-dan-paste
title: "Verifikasi OTP Faktor-2: Pengiriman Mail-Catcher, Auto-Submit Digit ke-6, dan Smart Paste"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-62
  - TC-AUTH-MFA-66
  - TC-AUTH-MFA-68
  - TC-AUTH-MFA-69
  - TC-AUTH-MFA-88
  - TC-AUTH-MFA-89
coverage:
  web: automated
---
# Verifikasi OTP Faktor-2: Pengiriman Mail-Catcher, Auto-Submit Digit ke-6, dan Smart Paste

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Tono Hartono` (`tonohartono@qwertysystem.net`) profil NEWDEV.
- User `Gita Gutawa` (`gitagutawa@qwertysystem.net`) profil NEWDEV.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Pengiriman email OTP faktor-2 di mail-catcher

1. Buka halaman login di browser, login dengan user `tonohartono@qwertysystem.net`
2. Pada Choose Verification Method, pilih "OTP via email" lalu klik [Login]
3. Periksa kotak masuk mail-catcher untuk `tonohartono@qwertysystem.net`
4. Verifikasi terdapat email baru dengan subject "TAG Samurai - Verification Code"
5. Verifikasi badan email memuat kode OTP 6 digit numerik yang jelas dan informasi masa berlaku 5 menit

### Auto-Submit otomatis saat digit ke-6 terisi

6. Catat 6 digit kode OTP valid dari email tersebut
7. Ketik 5 digit pertama pada kotak SegmentedInput di browser
8. Ketik digit ke-6
9. Verifikasi sistem seketika menjalankan verifikasi otomatis tanpa perlu menekan tombol [Login]
10. Verifikasi button [Login] berubah status menjadi disabled dengan indikator submitting / loading spinner
11. Verifikasi verifikasi berhasil dan browser dialihkan ke Portal — Product Hub dengan sesi web aktif

### Filter penolakan karakter non-angka pada kotak input OTP

12. Buka alur OTP Verification untuk user `gitagutawa@qwertysystem.net`
13. Pada kotak digit 1, ketik huruf `a`, huruf `Z`, dan karakter simbol `#`, `-`, `.`
14. Verifikasi karakter non-angka tidak masuk ke dalam kotak dan kotak tetap dalam keadaan kosong
15. Ketik angka `7` dan verifikasi angka masuk ke kotak 1 serta kursor maju ke kotak 2

### Smart Paste 6 digit sekaligus memecah karakter dan memicu auto-submit

16. Salin kode OTP 6 digit valid dari email ke clipboard sistem
17. Klik kotak input 1 lalu tekan `Ctrl+V` (paste)
18. Verifikasi karakter terpecah secara rapi ke kotak 1 sampai 6
19. Verifikasi sistem mendeteksi keenam kotak terisi penuh dan memicu auto-submit hingga redirect sukses ke Portal — Product Hub

### Smart Paste dari kotak tengah dan pembuangan karakter berlebih

20. Buka kembali form OTP Verification dengan sesi baru
21. Salin teks string 6 digit `987654` ke clipboard
22. Klik kotak 3 lalu tekan `Ctrl+V`
23. Verifikasi paste mengisi mulai dari kotak 3 sampai kotak 6 (`9876`), sisa digit (`54`) dibuang otomatis, dan form TIDAK melakukan auto-submit karena kotak 1 dan 2 belum terisi
24. Salin teks string yang mengandung karakter non-digit `12-34 56` ke clipboard
25. Bersihkan form, klik kotak 1 lalu tekan `Ctrl+V`
26. Verifikasi karakter tanda strip dan spasi diabaikan sehingga keenam kotak terisi angka murni `123456`

## Notes

- Sesuai `auth-foundation.md` §2c dan FI-04, pengisian digit ke-6 pada form OTP memicu auto-submit.
- Tombol [Login] tetap terlihat sebagai fallback manual.
