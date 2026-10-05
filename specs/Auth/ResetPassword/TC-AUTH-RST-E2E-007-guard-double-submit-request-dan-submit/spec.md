---
id: TC-AUTH-RST-E2E-007-guard-double-submit-request-dan-submit
title: Guard double-submit pada Request Reset Password dan Submit New Password
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-19
  - TC-AUTH-RST-65
coverage:
  web: automated
---

# Guard double-submit pada Request Reset Password dan Submit New Password

## Prerequisites

- Belum login dan session kosong. Halaman Reset Password terbuka di browser.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. Password user tersebut tersedia lewat
  `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di fixture.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy
  dan berbeda dari password lama.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut lewat API Global Settings > User, dengan masa berlaku 24 jam.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset milik
  user tersebut.
- `Fixture.authResetPassword.mailbox` adalah kotak masuk uji untuk user tersebut, disiapkan tim FE
  dan dikosongkan dari email reset password sebelum spec berjalan.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.

## Test Steps

### Double-submit pada halaman permintaan

1. Pastikan kotak masuk uji kosong dari email reset password
2. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
3. Selesaikan widget reCAPTCHA
4. Klik "Reset Password" dua kali cepat berturut-turut sebelum tombol selesai diproses
5. Verifikasi tombol "Reset Password" menjadi disabled dan menampilkan indikator proses begitu
    klik pertama diproses
6. Verifikasi hanya satu request yang benar-benar dikirim ke server
7. Verifikasi navigasi ke halaman Email Sent! terjadi tepat satu kali, tanpa error ganda
8. Verifikasi hanya satu email reset masuk ke kotak masuk user
9. Verifikasi hanya satu token reset baru dibuat dan berstatus "active"
10. Verifikasi tidak ada caption error dan tidak ada toast error yang muncul

### Double-submit pada halaman Setup New Password

11. Baca email reset pada kotak masuk uji, lalu buka tautan "Confirm Email" dari email tersebut
12. Verifikasi halaman Setup New Password tampil
13. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
14. Isi field Confirm Password dengan nilai yang sama
15. Klik "Reset Password" dua kali cepat berturut-turut sebelum tombol selesai diproses
16. Verifikasi tombol "Reset Password" menjadi disabled dan menampilkan indikator proses begitu
    klik pertama diproses
17. Verifikasi hanya satu request yang benar-benar dikirim ke server
18. Verifikasi navigasi ke halaman Password Reset Successful terjadi tepat satu kali
19. Verifikasi token reset milik user tersebut berstatus "consumed" tepat satu kali
20. Verifikasi tidak ada caption error dan tidak ada toast error yang muncul

## Notes

- Yang diuji adalah jumlah request yang benar-benar diproses server, bukan hanya kondisi disabled
  tombol. Disabled tombol bisa terjadi karena kosmetik, sedangkan yang diuji adalah idempotensi di
  sisi server.
- Jumlah token dan jumlah email di kotak masuk dipakai sebagai pembuktian tambahan, karena keduanya
  mencerminkan satu aksi yang sama.
- Retry setelah client timeout punya risiko berbeda dari double-submit dan diuji terpisah di
  spec 008.
- Nilai password hanya diambil dari environment variable, tidak ditulis di spec maupun fixture.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.