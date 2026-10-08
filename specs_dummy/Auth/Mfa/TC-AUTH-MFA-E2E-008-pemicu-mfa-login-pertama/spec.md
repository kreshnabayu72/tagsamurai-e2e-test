---
id: TC-AUTH-MFA-E2E-008-pemicu-mfa-login-pertama
title: "Pemicu MFA Login Pertama Kali: Wajib Faktor-2, Tanpa Alert, dan Pencatatan Device Awal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-24
  - TC-AUTH-MFA-25
  - TC-AUTH-MFA-149
coverage:
  web: automated
---
# Pemicu MFA Login Pertama Kali: Wajib Faktor-2, Tanpa Alert, dan Pencatatan Device Awal

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Kurniawan Dwi` (`kurniawan@qwertysystem.net`) profil FIRST (`first_login_at` masih NULL, belum pernah login ke platform).
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Login pertama kali memicu MFA Choose Verification Method

1. Buka halaman `Auth > Login with Password` (`/login`) di browser
2. Masukkan email `kurniawan@qwertysystem.net` dan password valid
3. Centang reCAPTCHA dan klik button [Log in]
4. Verifikasi sistem mendeteksi kondisi login pertama kali (`first_login_at` IS NULL)
5. Verifikasi halaman berpindah ke `Auth > MFA > Choose Verification Method` (`/auth/mfa`)

### Login pertama kali tidak mengirimkan email alert unusual login

6. Segera periksa kotak masuk mail-catcher untuk `kurniawan@qwertysystem.net`
7. Verifikasi TIDAK ADA email alert "TAG Samurai - Unusual Login Attempt Detected" yang dikirimkan (karena login pertama adalah kondisi inisialisasi yang diharapkan, bukan anomali)

### Penyelesaian faktor-2 login pertama mendaftarkan trusted device awal

8. Pilih opsi "OTP via email" lalu klik [Login]
9. Ambil kode OTP dari mail-catcher dan masukkan ke dalam form OTP Verification
10. Verifikasi login berhasil tuntas dan browser dialihkan ke Portal — Product Hub
11. Verifikasi browser uji saat ini kini tercatat sebagai trusted device pertama untuk user tersebut
12. Verifikasi kolom `first_login_at` user kini terisi timestamp saat ini

## Notes

- Sesuai `AUTHMFA-LOGIC-01a` dan PRD §9.2 F-AUTHMFA-02, login pertama wajib MFA namun tidak menghasilkan email alert unusual login.
