---
id: TC-AUTH-RST-E2E-027-plan-gating-lintas-tier-dan-entitas
title: Ketersediaan fitur Reset Password lintas tier dan entitas
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-114
coverage:
  web: automated
---

# Ketersediaan fitur Reset Password lintas tier dan entitas

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- `Fixture.authResetPassword.plans` adalah daftar seluruh tier plan yang tersedia, yaitu Starter,
  Growth, Professional, Enterprise, dan Custom. Jumlah dan nama tier diambil dari fixture, bukan
  ditulis sebagai daftar di spec ini, supaya ikut mengikuti perubahan produk.
- Untuk setiap tier, `Fixture.authResetPassword.plans.createUserForTier` adalah cara membuat satu
  user aktif milik entitas pada tier tersebut lewat Global Settings > User. Kemampuan ini disiapkan
  tim FE.
- Untuk setiap tier, `Fixture.authResetPassword.plans.emailForTier` adalah email user yang dibuat
  pada langkah sebelumnya.
- Password user uji tersedia lewat `Spectra.env.AUTH_PASSWORD`, dan password baru tersedia lewat
  `Spectra.env.AUTH_NEW_PASSWORD`, keduanya tidak ditulis di file ini maupun di fixture.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tertentu dengan masa berlaku 24 jam, lewat API Global Settings > User.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset.
- Kotak masuk uji disiapkan tim FE dan dicatat di `Fixture.authResetPassword.mailbox`, dipakai untuk
  memeriksa bahwa email tetap dikirim pada semua tier.
- `Fixture.authResetPassword.viewport` adalah ukuran viewport yang dipakai, sehingga hasil yang sama
  dibandingkan pada kondisi layar yang sama.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Alur penuh berulang pada seluruh tier

1. Baca daftar tier dari `Fixture.authResetPassword.plans`
2. Untuk tier pertama pada daftar tersebut, buat satu user aktif memakai
    `Fixture.authResetPassword.plans.createUserForTier`
3. Buka halaman Reset Password dan isi field Email dengan
    `Fixture.authResetPassword.plans.emailForTier`
4. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
5. Verifikasi navigasi ke halaman Email Sent! terjadi
6. Verifikasi email reset terkirim ke email user tersebut
7. Buat satu token reset aktif milik user tersebut memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
8. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
9. Verifikasi halaman Setup New Password tampil
10. Verifikasi checklist Password Policy tampil lengkap pada tier tersebut
11. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
12. Isi field Confirm Password dengan nilai yang sama
13. Klik "Reset Password"
14. Verifikasi navigasi ke halaman Password Reset Successful terjadi
15. Verifikasi status token reset milik user tersebut berubah menjadi "consumed"
16. Verifikasi password baru user tersebut dapat dipakai untuk login
17. Catat tampilan halaman permintaan, halaman Email Sent, halaman Setup New Password, dan halaman
    Password Reset Successful sebagai pembanding tier pertama
18. Untuk setiap tier berikutnya pada daftar tersebut, ulangi langkah 2 sampai 17
19. Verifikasi tidak ada tier yang menampilkan tombol Upgrade, Upsell, atau permintaan upgrade
20. Verifikasi tidak ada tier yang menyembunyikan sebagian alur, menu, atau CTA
21. Verifikasi judul, subtitle, caption, dan label pada keempat halaman identik di semua tier
22. Verifikasi urutan fokus keyboard pada keempat halaman identik di semua tier
23. Verifikasi tidak ada perbedaan perilaku yang bergantung pada tier, termasuk perbedaan penolakan,
    penundaan, dan batasan laju

### Tidak ada gating pada halaman yang tidak terkait tier

24. Buka halaman Reset Password untuk user pada tier tertinggi
25. Verifikasi halaman dapat diakses tanpa ada permintaan upgrade
26. Verifikasi field Email dapat diisi pada tier apa pun tanpa dibatasi
27. Verifikasi halaman Setup New Password dapat diakses pada tier apa pun tanpa ada permintaan
    upgrade
28. Verifikasi tidak ada penyesuaian Password Policy berdasarkan pada tier, sehingga checklist identik
    di semua tier

## Notes

- Tier diambil dari fixture dan diproses satu per satu, sehingga tier baru atau tier yang dihapus
  otomatis ikut teruji tanpa perlu mengubah spec ini.
- Email tetap dikirim pada semua tier karena itu bagian dari verifikasi bahwa fitur benar-benar
  bekerja, bukan sekadar terlihat tersedia.
- Yang diuji adalah kesetaraan perilaku dan tampilan, bukan ketersediaan entry point dari halaman
  profil atau menu. Entry point Reset Password berasal dari halaman Login with Password dan tidak
  bergantung pada tier.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password" dan "Go to Login Page". Aturan
  `[Submit]` dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit
  entitas, bukan untuk halaman autentikasi.