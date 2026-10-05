---
id: TC-AUTH-RST-E2E-010-halaman-email-sent-tampilan-dan-cooldown-resend
title: Tampilan halaman Email Sent, cooldown Resend, dan navigasi Back to Login
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-21
  - TC-AUTH-RST-22
  - TC-AUTH-RST-27
  - TC-AUTH-RST-118
coverage:
  web: automated
---

# Tampilan halaman Email Sent, cooldown Resend, dan navigasi Back to Login

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. User ini bukan Default User dan bukan akun
  admin Total Control.
- `Fixture.authResetPassword.data.emailMissingInContext` adalah satu request reset yang berhasil
  tetapi konteks email pada halaman Email Sent! sengaja dibuat kosong atau null, untuk menguji
  fallback teks generik. Kemampuan membuat kondisi itu disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.seedRequests.requestWithoutEmailContext`.
- `Fixture.authResetPassword.seedRequests.requestWithEmail` adalah cara membuat satu request reset
  sukses untuk user tersebut sehingga halaman Email Sent! terbuka tanpa harus mengirim email sungguhan.
- Kotak masuk uji tidak dibutuhkan pada spec ini karena yang diuji adalah halaman, bukan isi email.
- Caption countdown yang dirujuk diambil dari `Fixture.authResetPassword.captions`.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.

## Test Steps

### Tampilan halaman Email Sent setelah request sukses

1. Buat kondisi awal dengan request reset sukses untuk
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.seedRequests.requestWithEmail`
2. Buka halaman Email Sent!
3. Verifikasi judul halaman adalah "Email Sent!"
4. Verifikasi tidak ada toast yang muncul saat halaman Email Sent! pertama kali tampil
5. Verifikasi message halaman menyebut email lengkap user tersebut tanpa masking
6. Verifikasi message halaman menggunakan bentuk sapaan yang sesuai dengan PRD
7. Verifikasi tombol "Resend" tampil
8. Verifikasi link "Log in with password" tampil
9. Verifikasi tidak ada field Email kosong di halaman ini, sehingga user tidak bisa menyalakan ulang
   request dari halaman yang sama

### Countdown Resend selama cooldown

10. Amati state tombol "Resend" segera setelah halaman Email Sent! terbuka
11. Verifikasi tombol "Resend" berada dalam keadaan disabled
12. Verifikasi teks countdown tampil dengan format menit dan detik, misalnya "Resend in 0:45"
13. Verifikasi countdown menghitung mundur seiring waktu
14. Verifikasi tombol "Resend" tetap disabled sepanjang masa cooldown
15. Verifikasi tidak ada request resend yang terkirim selama masa cooldown

### Navigasi Back to Login

16. Klik link "Log in with password" pada halaman Email Sent!
17. Verifikasi navigasi ke halaman Login with Password terjadi
18. Verifikasi field Email pada halaman Login terisi dengan email user tersebut
19. Verifikasi tidak ada toast error dan tidak ada halaman error yang tampil

### Fallback saat konteks email kosong

20. Buat kondisi awal dengan request reset sukses yang konteks emailnya kosong atau null memakai
    `Fixture.authResetPassword.seedRequests.requestWithoutEmailContext`
21. Buka halaman Email Sent!
22. Verifikasi judul halaman tetap "Email Sent!"
23. Verifikasi message halaman tetap tampil lengkap dan tidak kosong
24. Verifikasi message halaman memakai teks fallback generik yang menyebut "your email"
25. Verifikasi tidak ada literal "null" yang tampil di halaman dalam keadaan apa pun
26. Verifikasi tidak ada literal "undefined" yang tampil di halaman dalam keadaan apa pun
27. Verifikasi tidak ada error rendering atau halaman kosong

## Notes

- Spec ini sengaja tidak memakai email sungguhan untuk membuka halaman Email Sent!, karena yang
  diuji adalah tampilan halaman. Spec 006 memakai email sungguhan untuk memeriksa isi email.
- Countdown resend dibaca dari UI, bukan dari state server, karena yang diuji adalah apa yang dilihat
  user. Penegakan cooldown di sisi server ada di spec 013.
- Fallback teks generik sengaja menguji dua literal yang paling sering bocor, yaitu "null" dan
  "undefined", karena keduanya berasal dari template yang sama.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Resend" dan "Log in with password". Aturan
  `[Submit]` dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit
  entitas, bukan untuk halaman autentikasi.