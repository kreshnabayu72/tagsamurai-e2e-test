---
id: TC-AUTH-RST-E2E-008-retry-setelah-client-timeout
title: Retry setelah client timeout pada Request dan Submit New Password
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-66
  - TC-AUTH-RST-84
  - TC-AUTH-RST-85
coverage:
  web: automated
---

# Retry setelah client timeout pada Request dan Submit New Password

## Prerequisites

- Belum login dan session kosong. Halaman Reset Password terbuka di browser.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. Password user tersebut tersedia lewat
  `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di fixture.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy
  dan berbeda dari password lama.
- `Mode: mock`. Spec ini butuh kemampuan menunda respons server setelah request diterima server.
  Kemampuan intercept dan penundaan respons disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.network.delayResponse`. Penundaan dibuat dengan tetap mengirim
  request ke server, sehingga server benar-benar memprosesnya, tetapi responsnya tidak sampai ke
  client tepat waktu.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut lewat API Global Settings > User, dengan masa berlaku 24 jam.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status dan jumlah token
  reset milik user tersebut.
- `Fixture.authResetPassword.mailbox` adalah kotak masuk uji untuk user tersebut, disiapkan tim FE
  dan dikosongkan dari email reset password sebelum spec berjalan.
- `Fixture.authResetPassword.users.activated.email` sudah bebas dari cooldown 60 detik dan belum
  menyentuh batas rate limit 5 kali per 24 jam, sehingga efek yang diamati benar-benar berasal dari
  token satu kali pakai dan cooldown, bukan dari rate limit.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.

## Test Steps

### Retry Request setelah client timeout

1. Pastikan kotak masuk uji kosong dari email reset password
2. Aktifkan penundaan respons untuk request reset pada endpoint yang sesuai
3. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
4. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
5. Tunggu sampai client menganggap request timeout, sementara server sudah memprosesnya
6. Kirim ulang request yang sama dengan menekan tombol "Reset Password" lagi setelah form tetap
   tersedia
7. Verifikasi server memproses request kedua dan menolak atau meredamnya, sehingga tidak ada
   token kedua dan tidak ada email kedua yang dibuat
8. Verifikasi hanya satu token reset aktif milik user tersebut setelah retry
9. Verifikasi hanya satu email reset masuk ke kotak masuk user
10. Verifikasi caption dan toast yang tampil tidak berupa error server generik, sehingga response
    kedua tidak diperlakukan sebagai kegagalan umum
11. Nonaktifkan penundaan respons

### Retry Submit setelah client timeout

12. Aktifkan penundaan respons untuk request submit password baru pada endpoint yang sesuai
13. Buka tautan "Confirm Email" dari email reset pada langkah sebelumnya
14. Verifikasi halaman Setup New Password tampil
15. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
16. Isi field Confirm Password dengan nilai yang sama
17. Klik "Reset Password"
18. Tunggu sampai client menganggap submit timeout, sementara server sudah memprosesnya
19. Kirim ulang submit dengan token yang sama, lalu tekan tombol "Reset Password" lagi
20. Verifikasi response kedua diperlakukan sebagai kondisi token sudah dipakai, bukan sebagai error
    generik
21. Verifikasi token reset milik user tersebut berstatus "consumed" tepat satu kali
22. Verifikasi hanya satu perubahan password yang terjadi, sehingga tidak ada reset kredensial kedua
23. Verifikasi password baru user tetap dapat dipakai untuk login dan password lama tidak lagi
    berlaku
24. Nonaktifkan penundaan respons

## Notes

- Yang diuji adalah bahwa request pertama benar-benar diproses server meski responsnya tidak
  sampai ke client. Kalau penundaan respons dilakukan sebelum request dikirim, retry kedua akan
  terlihat seperti request biasa dan spec ini tidak lagi menguji apa yang dimaksud.
- Pada retry Request, penolakan datang dari cooldown 60 detik per email. Pada retry Submit,
  penolakan datang dari token satu kali pakai. Keduanya diuji karena mekanismenya berbeda.
- Verifikasi bahwa password baru berlaku dilakukan di spec ini karena itu satu-satunya cara
  memastikan tidak ada reset kredensial kedua.
- Nilai password hanya diambil dari environment variable, tidak ditulis di spec maupun fixture.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.