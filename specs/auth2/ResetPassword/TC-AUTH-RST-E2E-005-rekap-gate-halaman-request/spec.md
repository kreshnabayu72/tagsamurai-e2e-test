---
id: TC-AUTH-RST-E2E-005-rekap-gate-halaman-request
title: reCAPTCHA gate pada halaman permintaan Reset Password
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-13
  - TC-AUTH-RST-14
coverage:
  web: automated
---

# reCAPTCHA gate pada halaman permintaan Reset Password

## Prerequisites

- Belum login dan session kosong. Halaman Reset Password terbuka di browser.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya diketahui dan user
  ini bukan Default User maupun bukan akun admin Total Control.
- `Fixture.authResetPassword.users.activated.email` adalah email user terdaftar tersebut.
- `Fixture.authResetPassword.data.invalidEmailFormat` adalah string yang bukan email valid, dipakai
  untuk memastikan validasi format email dievaluasi lebih dulu daripada reCAPTCHA.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.
- Caption error yang dirujuk diambil dari `Fixture.authResetPassword.captions`.

## Test Steps

### Submit tanpa menyelesaikan reCAPTCHA

1. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
2. Verifikasi widget reCAPTCHA tampil dalam keadaan belum diselesaikan
3. Klik "Reset Password"
4. Verifikasi caption inline adalah "Please verify that you are not a robot"
5. Verifikasi tidak ada navigasi ke halaman Email Sent!
6. Verifikasi tidak ada email reset yang terkirim ke kotak masuk user
7. Verifikasi tidak ada token reset yang dibuat
8. Verifikasi tidak ada entri baru di kedua surface pencatatan, sehingga kegagalan captcha tidak
   menghasilkan entri log untuk subjek yang belum terverifikasi
9. Verifikasi field Email tetap terisi dan tombol "Reset Password" kembali enabled

### Submit setelah reCAPTCHA diselesaikan

10. Selesaikan widget reCAPTCHA pada field yang sama
11. Verifikasi widget reCAPTCHA menampilkan tanda sudah terverifikasi
12. Klik "Reset Password"
13. Verifikasi caption reCAPTCHA tidak muncul lagi
14. Verifikasi caption validasi Email tidak muncul
15. Verifikasi navigasi ke halaman Email Sent! terjadi
16. Verifikasi tidak ada navigasi ke halaman 404 atau halaman lain

### Urutan validasi format email terhadap reCAPTCHA

17. Kembali ke halaman Reset Password dari halaman Email Sent! lewat link "Back to Login" lalu link
    "Forgot your password? Reset here"
18. Isi field Email dengan `Fixture.authResetPassword.data.invalidEmailFormat`, biarkan reCAPTCHA
    belum diselesaikan, lalu klik "Reset Password"
19. Verifikasi caption yang muncul adalah caption format email, bukan caption reCAPTCHA
20. Verifikasi caption reCAPTCHA tidak muncul pada submit ini

## Notes

- Spec ini menguji gate captcha pada halaman permintaan saja. Ketiadaan reCAPTCHA di native app
  ada di TC-AUTH-RST-3 dan di spec 003.
- Kegagalan provider reCAPTCHA atau timeout provider diperlakukan sebagai kegagalan server dan
  diuji di spec 009, bukan di spec ini.
- Caption "Please verify that you are not a robot" diambil dari
  `Fixture.authResetPassword.captions` sesuai aturan e2e-conventions.md bagian 9.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.