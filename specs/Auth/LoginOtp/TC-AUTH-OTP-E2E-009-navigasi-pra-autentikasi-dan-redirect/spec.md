---
id: TC-AUTH-OTP-E2E-009-navigasi-pra-autentikasi-dan-redirect
title: "Navigasi Antar Jalur Pra-Autentikasi dan Redirect Pengguna yang Sudah Login"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-06
  - TC-AUTH-OTP-35
  - TC-AUTH-OTP-36
  - TC-AUTH-OTP-75
  - TC-AUTH-OTP-76
coverage:
  web: automated
---

# Navigasi Antar Jalur Pra-Autentikasi dan Redirect Pengguna yang Sudah Login

## Prerequisites

- Browser siap membuka rute pra-autentikasi maupun rute internal dengan sesi aktif.
- User `Galih Tanjung` (`galihtanjung@qwertysystem.net`) profil BASE.
- User `Citra Rahmawati` (`citrarahmawati@qwertysystem.net`) profil BASE.
- Sesi aktif pengguna terautentikasi disiapkan untuk pengujian redirect.

## Test Steps

### Navigasi Use password instead dari Request OTP membawa email

1. Buka halaman `Auth > Login with OTP > Request OTP` (`/login/otp`) di browser dalam keadaan belum login
2. Masukkan email `galihtanjung@qwertysystem.net` ke field Email
3. Klik tautan [Use password instead] di bawah tombol Request OTP
4. Verifikasi browser berpindah ke halaman `Auth > Login with Password` (`/login`)
5. Verifikasi field Email di halaman Login with Password sudah terisi otomatis dengan `galihtanjung@qwertysystem.net`

### Navigasi Back to Login with Password dari Verify OTP membawa email

6. Buka kembali halaman Request OTP, masukkan email `citrarahmawati@qwertysystem.net`, centang reCAPTCHA, lalu klik [Request OTP]
7. Verifikasi halaman Verify OTP tampil
8. Klik tautan [Back to Login with Password] di bagian footer layar
9. Verifikasi browser berpindah ke halaman `Auth > Login with Password` (`/login`)
10. Verifikasi field Email di halaman Login with Password sudah terisi otomatis dengan `citrarahmawati@qwertysystem.net`

### Pengalihan otomatis (redirect) pengguna yang sudah login ke Product Hub

11. Lakukan autentikasi sehingga browser memiliki sesi login aktif (token sesi tersimpan)
12. Buka alamat langsung halaman Request OTP (`/login/otp`) di URL bar browser
13. Verifikasi halaman Request OTP tidak ditampilkan dan browser langsung dialihkan (redirect) ke Portal — Product Hub
14. Buka alamat langsung halaman Verify OTP (`/login/otp/verify`) di URL bar browser
15. Verifikasi halaman Verify OTP tidak ditampilkan dan browser langsung dialihkan ke Portal — Product Hub
16. Buka alamat langsung halaman Confirm to Continue (`/login/confirm-agreement`) di URL bar browser
17. Verifikasi halaman Confirm to Continue tidak ditampilkan dan browser langsung dialihkan ke Portal — Product Hub

## Notes

- Semua halaman pra-autentikasi (Request OTP, Verify OTP, Confirm to Continue) memiliki guard redirect otomatis: pengguna dengan sesi aktif tidak diizinkan mengakses halaman login dan selalu dilempar ke Portal/Product Hub (sesuai NC-08).
- Perpindahan bolak-balik antara Login with Password dan Login with OTP menjaga kesinambungan input email pengguna agar tidak perlu mengetik ulang.
