---
id: TC-AUTH-RST-E2E-003-rekap-tidak-tampil-di-native-app
title: Ketiadaan reCAPTCHA pada halaman Reset Password di native app
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-3
coverage:
  mobile: automated
---

# Ketiadaan reCAPTCHA pada halaman Reset Password di native app

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Spec ini berjalan pada native app, bukan pada browser. Device emulator atau simulator sudah aktif
  sesuai konfigurasi `androidConfig` atau `iosConfig` di `spectra.config.ts`.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya diketahui dan user
  ini bukan Default User maupun bukan akun admin Total Control.
- `Fixture.authResetPassword.users.activated.email` adalah email user terdaftar tersebut.

## Test Steps

1. Buka aplikasi pada halaman Login with Password
2. Buka halaman Reset Password dari menu atau entry point lupa password
3. Verifikasi judul halaman adalah "Reset Password"
4. Verifikasi field Email tampil dengan placeholder "Enter your email"
5. Verifikasi tidak ada widget reCAPTCHA di halaman ini, dalam keadaan apa pun
6. Verifikasi tidak ada elemen mock atau spacers kosong yang sebelumnya menampung reCAPTCHA
7. Verifikasi field Email tidak tertutup oleh elemen apa pun yang sebelumnya menampung reCAPTCHA
8. Verifikasi tombol "Reset Password" tampil dalam keadaan enabled
9. Verifikasi link "Log in with password" tampil di halaman
10. Verifikasi tidak ada caption error yang tampil pada kondisi ini
11. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
12. Verifikasi tombol "Reset Password" tetap enabled tanpa perlu menyelesaikan captcha apa pun
13. Klik "Reset Password"
14. Verifikasi tidak ada request yang tertahan oleh validasi captcha
15. Verifikasi request diteruskan ke tahap evaluasi berikutnya oleh server

## Notes

- Spec ini menjalankan platform native app, sedangkan TC-AUTH-RST-2 memakai mobile browser dan
  berada di spec terpisah. Keduanya diotomasikan.
- Ketiadaan reCAPTCHA di native app adalah perilaku yang diharapkan, bukan kegagalan, karena
  proteksi pada alur reset diberikan oleh token satu kali pakai dan TTL, bukan oleh captcha.
- Yang diuji di sini hanya ketiadaan widget. Verifikasi bahwa halaman Setup New Password juga tidak
  menampilkan reCAPTCHA ada di TC-AUTH-RST-57 dan sudah tercakup di spec 017.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan `[Save]`
  pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan untuk
  halaman autentikasi.