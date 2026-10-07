---
id: TC-AUTH-MFA-E2E-023-batas-percobaan-salah-lintas-metode
title: "Batas 5 Percobaan Salah Lintas Metode: Invalidation Sesi Pre-Auth dan Redirection Login"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-129
  - TC-AUTH-MFA-130
  - TC-AUTH-MFA-131
  - TC-AUTH-MFA-132
  - TC-AUTH-MFA-133
  - TC-AUTH-MFA-134
  - TC-AUTH-MFA-135
coverage:
  web: automated
---
# Batas 5 Percobaan Salah Lintas Metode: Invalidation Sesi Pre-Auth dan Redirection Login

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Kusuma Wardani` (`kusumawardani@qwertysystem.net`) profil NEWDEV.
- User `Lukman Hakim` (`lukmanhakim@qwertysystem.net`) profil NEWDEV.
- User `Made Suardana` (`madesuardana@qwertysystem.net`) profil FIRST (belum enroll).
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Akumulasi 5 percobaan salah lintas metode membatalkan sesi pre-auth

1. Buka alur OTP Verification untuk user `kusumawardani@qwertysystem.net`
2. Masukkan kode OTP yang salah 2 kali (percobaan 1 dan 2)
3. Verifikasi masing-masing percobaan menghasilkan caption "Invalid code"
4. Klik button Text [Use a different method], pilih "Authenticator app", lalu klik [Login]
5. Pada form Authenticator Verification, masukkan kode TOTP yang salah 2 kali (percobaan 3 dan 4)
6. Verifikasi hitungan percobaan salah dipertahankan lintas metode (total 4 percobaan salah terkumpul)
7. Masukkan kode salah ke-5 pada form Authenticator
8. Verifikasi pada percobaan ke-5, sesi pre-auth seketika dibatalkan (preAuthToken di-invalidate) dan browser langsung dialihkan ke halaman login (`/login`) tanpa pesan error (sesuai F-AUTHMFA-01 dan NC-05)

### Kode benar pada percobaan ke-6 ditolak karena sesi sudah dibatalkan

9. Pada halaman login tempat user dialihkan, coba kirimkan kode OTP/TOTP yang sebenarnya valid menggunakan token sesi lama melalui request API
10. Verifikasi request ditolak karena sesi pre-auth telah hangus permanen

### Kode kosong dan kegagalan enrollment dihitung dalam batas 5 percobaan

11. Buka sesi MFA baru untuk user `madesuardana@qwertysystem.net` pada halaman Enrollment Authenticator
12. Klik tombol [Verify] dengan kotak kosong 3 kali (kode kosong dihitung, sesuai NC-05)
13. Masukkan kode salah 2 kali lagi (total 5 percobaan gagal)
14. Verifikasi pada kegagalan ke-5 pengguna langsung dialihkan ke halaman login

### Kuota percobaan salah di-reset setelah login ulang dari faktor-1

15. Buka kembali halaman login dan lakukan login ulang dari awal dengan email `lukmanhakim@qwertysystem.net` dan password valid
16. Verifikasi sesi pre-auth baru diterbitkan dengan kuota 5 percobaan yang bersih kembali

## Notes

- Sesuai keputusan NC-05, batas 5 percobaan salah bersifat akumulatif lintas metode (OTP, TOTP, enrollment) dan kode kosong ikut dihitung.
- Pada percobaan salah ke-5, token pre-auth langsung di-invalidate dan pengguna dialihkan ke login.
