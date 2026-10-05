---
id: TC-AUTH-RST-E2E-002-rekap-tampil-di-mobile-browser
title: Tampilan reCAPTCHA pada halaman Reset Password di mobile browser
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-2
coverage:
  web: automated
---

# Tampilan reCAPTCHA pada halaman Reset Password di mobile browser

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Run dilakukan pada browser dengan viewport mobile, misalnya 390 x 844 piksel, sehingga halaman
  dirender dalam kondisi responsive mobile. Kemampuan mengatur viewport per spec disiapkan tim FE
  dan dicatat di `Fixture.authResetPassword.viewport`.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya diketahui dan user
  ini bukan Default User maupun bukan akun admin Total Control.
- `Fixture.authResetPassword.users.activated.email` adalah email user terdaftar tersebut.
- `Fixture.authResetPassword.captcha.widgetType` adalah jenis widget reCAPTCHA yang dipakai halaman
  ini pada environment otomasi.

## Test Steps

1. Atur viewport browser ke ukuran mobile sesuai `Fixture.authResetPassword.viewport`
2. Buka halaman Login with Password di browser
3. Klik link "Forgot your password? Reset here"
4. Verifikasi judul halaman adalah "Reset Password"
5. Verifikasi field Email tampil dengan placeholder "Enter your email"
6. Verifikasi widget reCAPTCHA tetap tampil di halaman
7. Verifikasi widget reCAPTCHA yang tampil adalah varian checkbox, bukan varian invisible
8. Verifikasi widget reCAPTCHA terender dalam mode compact tanpa menutupi atau meluberkan field lain
9. Verifikasi tombol "Reset Password" tampil dalam keadaan enabled
10. Verifikasi link "Log in with password" tampil di halaman
11. Verifikasi tidak ada tombol close, tidak ada elemen yang keluar dari batas viewport, dan tidak
    ada elemen yang terpotong separuh
12. Verifikasi halaman dapat di-scroll sampai seluruh isi halaman terlihat
13. Verifikasi tidak ada pesan error atau crash yang muncul pada kondisi ini
14. Kembalikan viewport browser ke ukuran desktop

## Notes

- Spec ini membedakan mobile browser dari native app. TC-AUTH-RST-3 memakai native app dan
  berada di spec terpisah karena perbedaan platformnya, bukan hanya ukuran layar.
- Yang diuji adalah ketiadaan varian invisible, bukan kebenaran tag site key reCAPTCHA. Verifikasi
  resmi atas key dipakai tim FE di luar cakupan E2E.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan `[Save]`
  pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan untuk
  halaman autentikasi.