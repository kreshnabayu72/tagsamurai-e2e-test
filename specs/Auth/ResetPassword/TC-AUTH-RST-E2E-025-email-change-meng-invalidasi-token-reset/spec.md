---
id: TC-AUTH-RST-E2E-025-email-change-meng-invalidasi-token-reset
title: Perubahan email yang dikonfirmasi menginvalidasi token reset aktif
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-112
coverage:
  web: automated
---

# Perubahan email yang dikonfirmasi menginvalidasi token reset aktif

## Prerequisites

- Belum login dan session kosong. Session admin di browser terpisah dari session browser yang
  dipakai untuk membuka link reset.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User, dengan email lama yang
  diketahui dan tersedia lewat `Fixture.authResetPassword.users.activated.email`. User ini bukan
  Default User dan bukan akun admin Total Control.
- `Fixture.authResetPassword.users.activated.emailBaru` adalah nilai email baru yang dipakai pada
  perubahan ini, dan email tersebut belum dipakai user lain.
- Akun admin Total Control untuk melakukan perubahan email tersedia lewat
  `Spectra.env.ADMIN_EMAIL` dan `Spectra.env.ADMIN_PASSWORD`, tidak ditulis di file ini maupun di
  fixture.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut dengan masa berlaku 24 jam, lewat API Global Settings > User. Kemampuan ini
  disiapkan tim FE.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset.
- Kotak masuk uji email lama user tersebut disiapkan tim FE dan dikosongkan dari email reset
  password sebelum spec berjalan, sehingga email yang dibaca pasti berasal dari request pada spec
  ini. Mailbox itu dicatat di `Fixture.authResetPassword.mailbox`.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Link reset berhenti berlaku setelah email berubah

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Susun tautan reset dari token tersebut memakai
    `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi tautan tersebut masih dapat dibuka dan merender halaman Setup New Password
4. Login ke Global Settings > User memakai kredensial admin Total Control
5. Buka data user dengan email `Fixture.authResetPassword.users.activated.email`
6. Ubah email user menjadi `Fixture.authResetPassword.users.activated.emailBaru`
7. Klik tombol simpan pada form Edit User
8. Tutup dialog konfirmasi perubahan email dengan mengikuti alur konfirmasi yang tersedia
9. Verifikasi perubahan email sudah terkonfirmasi dan tersimpan
10. Verifikasi email user pada Global Settings > User sudah menjadi
    `Fixture.authResetPassword.users.activated.emailBaru`
11. Buka tautan reset yang disusun pada langkah 2 di browser
12. Verifikasi halaman 404 tampil
13. Verifikasi halaman 404 yang tampil memakai varian copy Expired
14. Verifikasi status token reset milik user tersebut berubah menjadi "invalidated"
15. Verifikasi tidak ada lagi token aktif milik user tersebut setelah perubahan email
16. Verifikasi semua token aktif lain milik user tersebut, bila ada, juga di-invalidasi

### Request reset setelah email berubah memakai email baru

17. Kembali ke halaman Reset Password
18. Isi field Email dengan `Fixture.authResetPassword.users.activated.emailBaru`
19. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
20. Verifikasi navigasi ke halaman Email Sent! terjadi
21. Verifikasi email reset baru dikirim ke email baru user tersebut
22. Verifikasi tidak ada email reset yang dikirim ke email lama user tersebut
23. Verifikasi tautan pada email baru dapat dibuka dan merender halaman Setup New Password
24. Verifikasi status token yang dibuat pada langkah 18 berstatus "active"
25. Verifikasi password lama user tersebut masih dapat dipakai untuk login dengan email baru

## Notes

- Spec ini menguji arah perubahan dari luar modul reset password, yaitu perubahan email di
  Global Settings > User yang berakibat ke token reset. Arah sebaliknya, yaitu reset password yang
  menghasilkan efek ke modul lain, ada di spec 021.
- Semua token aktif milik user di-invalidasi, bukan hanya token yang sedang diuji. Yang diuji adalah
  invarian yang membuat tidak ada link reset tertinggal dengan email lama setelah email
  berubah.
- Login memakai email baru pada langkah 25 ditambahkan supaya perubahan email terbukti benar-benar
  berpindah, bukan hanya berubah label di layar.
- Email lama dan email baru diambil dari fixture, dan kredensial admin dari environment variable,
  sehingga tidak ada nilai sensitif yang ditulis di spec maupun fixture.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.