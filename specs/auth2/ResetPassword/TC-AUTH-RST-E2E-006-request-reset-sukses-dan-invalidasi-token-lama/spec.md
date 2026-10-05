---
id: TC-AUTH-RST-E2E-006-request-reset-sukses-dan-invalidasi-token-lama
title: Request reset sukses dan invalidasi token aktif sebelumnya
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-15
  - TC-AUTH-RST-16
coverage:
  web: automated
---

# Request reset sukses dan invalidasi token aktif sebelumnya

## Prerequisites

- Belum login dan session kosong. Halaman Reset Password terbuka di browser.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User, tidak pernah meminta reset
  password sebelumnya dalam 24 jam terakhir. User ini bukan Default User dan bukan akun admin
  Total Control. Email-nya adalah `Fixture.authResetPassword.users.activated.email`.
- `Fixture.authResetPassword.data.unknownEmail` adalah email berformat valid yang belum terdaftar,
  dipakai untuk membandingkan isi email yang tampil di halaman Email Sent!.
- Kotak masuk uji untuk user tersebut kosong dari email reset password, sehingga email yang dibaca
  pada spec ini pasti berasal dari request pada spec ini. Mailbox uji disiapkan tim FE dan
  dicatat di `Fixture.authResetPassword.mailbox`.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.
- `Fixture.authResetPassword.tokens` adalah endpoint atau cara baca state token reset milik tim FE,
  dipakai untuk memeriksa status token. Endpoint ini hanya untuk seeding dan verifikasi, bukan
  alur yang diuji sebagai kontrak API.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut lewat API Global Settings > User, dengan masa berlaku 24 jam.

## Test Steps

### Request reset sukses

1. Pastikan kotak masuk uji kosong dari email reset password
2. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
3. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
4. Verifikasi navigasi ke halaman Email Sent! terjadi
5. Verifikasi judul halaman adalah "Email Sent!"
6. Verifikasi tidak ada toast yang muncul saat halaman Email Sent! tampil
7. Verifikasi message halaman menyebut email lengkap user tersebut tanpa masking
8. Verifikasi tombol "Resend" tampil dan tombol "Log in with password" tampil
9. Verifikasi tidak ada navigasi ke halaman 404 maupun halaman lain
10. Tunggu email reset masuk ke kotak masuk uji
11. Verifikasi email dengan subject "Reset your TAG Samurai password" masuk ke kotak masuk user
12. Verifikasi email tersebut memuat tombol "Confirm Email"
13. Verifikasi email tersebut memuat link fallback yang dapat diklik tanpa membuka editor email
14. Verifikasi state token reset milik user menunjukkan status "active"
15. Verifikasi masa berlaku token reset yang dibuat menunjukkan 24 jam sejak waktu request

### Request baru meng-invalidasi token aktif sebelumnya

16. Baca nilai token reset aktif milik user tersebut, lalu simpan sebagai token lama
17. Kembali ke halaman Reset Password dari halaman Email Sent! lewat link "Log in with password",
    lalu klik link "Forgot your password? Reset here"
18. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
19. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
20. Verifikasi navigasi ke halaman Email Sent! terjadi
21. Verifikasi request kedua diproses normal, tanpa caption error
22. Verifikasi email reset baru masuk ke kotak masuk user
23. Verifikasi state token lama menunjukkan status "invalidated"
24. Verifikasi state token baru menunjukkan status "active"
25. Verifikasi hanya ada satu token reset aktif milik user tersebut setelah request kedua
26. Verifikasi nilai token baru berbeda dari nilai token lama
27. Verifikasi masa berlaku token baru dimulai ulang dari waktu request kedua

## Notes

- Request kedua sengaja dilakukan lewat halaman permintaan dari awal, bukan lewat tombol "Resend".
  Perilaku tombol "Resend" ada di spec 011.
- Verifikasi "hanya satu token aktif" adalah bagian dari invarian yang dijaga basis data, jadi
  dibacakan lewat state token, bukan lewat jumlah email di kotak masuk.
- Email yang dibaca tetap memakai subject dan struktur yang diketik ulang di spec ini, bukan isi
  mentah, supaya spec tidak bergantung pada template email yang berubah.
- Password dan nilai token tidak boleh ditulis di spec maupun fixture. Nilai token hanya dibaca
  lewat helper dan dipakai di dalam spec ini tanpa dicatat di file.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password" dan "Log in with password".
  Aturan `[Submit]` dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan
  Edit entitas, bukan untuk halaman autentikasi.