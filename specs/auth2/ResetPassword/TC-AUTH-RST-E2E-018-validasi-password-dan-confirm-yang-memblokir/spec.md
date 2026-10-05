---
id: TC-AUTH-RST-E2E-018-validasi-password-dan-confirm-yang-memblokir
title: Validasi Password dan Confirm Password yang memblokir submit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-52
  - TC-AUTH-RST-53
  - TC-AUTH-RST-54
  - TC-AUTH-RST-55
coverage:
  web: automated
---

# Validasi Password dan Confirm Password yang memblokir submit

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User, dengan password lama yang
  diketahui dan tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di
  fixture. User ini bukan Default User dan bukan akun admin Total Control.
- `Fixture.authResetPassword.users.activated.email` adalah email user tersebut.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut dengan masa berlaku 24 jam, lewat API Global Settings > User. Kemampuan ini
  disiapkan tim FE.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset, dipakai
  untuk memastikan submit yang diblokir tidak mengonsumsi token.
- `Fixture.authResetPassword.data.validPassword` adalah satu password baru yang memenuhi seluruh
  Password Policy dan berbeda dari password lama.
- `Fixture.authResetPassword.data.mismatchedConfirm` adalah satu nilai yang berbeda dari
  `Fixture.authResetPassword.data.validPassword` tetapi sama panjangnya, dipakai untuk menguji
  ketidakcocokan tanpa efek panjang.
- `Fixture.authResetPassword.captions` adalah sumber caption error yang dirujuk, supaya caption tidak
  diketik ulang di spec ini.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Password kosong

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi halaman Setup New Password tampil
4. Isi field Confirm Password dengan `Fixture.authResetPassword.data.validPassword`, biarkan field
   Password kosong
5. Klik "Reset Password"
6. Verifikasi caption yang tampil sesuai dengan caption Password kosong dari
    `Fixture.authResetPassword.captions`
7. Verifikasi tidak ada navigasi dari halaman Setup New Password
8. Verifikasi status token reset milik user tersebut tetap "active"

### Confirm Password kosong

9. Kosongkan kedua field dengan tombol "Clear Field"
10. Isi field Password dengan `Fixture.authResetPassword.data.validPassword`, biarkan field Confirm
    Password kosong
11. Klik "Reset Password"
12. Verifikasi caption yang tampil sesuai dengan caption Confirm Password kosong dari
    `Fixture.authResetPassword.captions`
13. Verifikasi caption tersebut berbeda dari caption Password kosong pada langkah 6
14. Verifikasi tidak ada navigasi dari halaman Setup New Password
15. Verifikasi status token reset milik user tersebut tetap "active"

### Confirm Password tidak sama dengan Password

16. Kosongkan kedua field dengan tombol "Clear Field"
17. Isi field Password dengan `Fixture.authResetPassword.data.validPassword`
18. Isi field Confirm Password dengan `Fixture.authResetPassword.data.mismatchedConfirm`
19. Klik "Reset Password"
20. Verifikasi caption yang tampil sesuai dengan caption ketidakcocokan dari
    `Fixture.authResetPassword.captions`
21. Verifikasi caption tersebut muncul karena kedua nilai berbeda, bukan karena salah satu tidak
    memenuhi Password Policy
22. Verifikasi checklist Password Policy tetap menampilkan semua rule sebagai terpenuhi, sehingga
    caption error bukan berasal dari rule yang gagal
23. Verifikasi tidak ada navigasi dari halaman Setup New Password
24. Verifikasi isi kedua field dipertahankan setelah submit diblokir
25. Verifikasi status token reset milik user tersebut tetap "active"

### Password sama dengan password lama

26. Kosongkan kedua field dengan tombol "Clear Field"
27. Isi field Password dengan `Spectra.env.AUTH_PASSWORD`
28. Isi field Confirm Password dengan nilai yang sama
29. Verifikasi checklist Password Policy tetap menampilkan semua rule sebagai terpenuhi
30. Klik "Reset Password"
31. Verifikasi caption yang tampil sesuai dengan caption password sama dengan yang lama dari
    `Fixture.authResetPassword.captions`
32. Verifikasi caption tersebut berbeda dari caption ketidakcocokan dan dari caption Password kosong
33. Verifikasi tidak ada navigasi dari halaman Setup New Password
34. Verifikasi status token reset milik user tersebut tetap "active"
35. Verifikasi password lama user masih berlaku, sehingga tidak ada perubahan kredensial
36. Verifikasi caption tersebut tidak membocorkan nilai password lama maupun hash-nya

### Form tetap dapat diisi ulang setelah semua submit diblokir

37. Kosongkan kedua field dengan tombol "Clear Field"
38. Isi field Password dengan `Fixture.authResetPassword.data.validPassword`
39. Isi field Confirm Password dengan nilai yang sama
40. Verifikasi semua caption error yang tadinya tampil sudah hilang
41. Verifikasi tombol "Reset Password" berada dalam keadaan enabled
42. Verifikasi checklist Password Policy menampilkan semua rule sebagai terpenuhi

## Notes

- Password lama dipakai satu kali pada subbagian keempat sebagai nilai yang ditolak, sehingga nilainya
  diambil dari environment variable dan tidak ditulis di spec maupun fixture.
- Verifikasi caption berbeda pada langkah 13 dan 32 dilakukan supaya ketiga kondisi tidak
  menghasilkan caption yang sama. Kalau sama, user tidak bisa membedakan penyebabnya.
- Verifikasi checklist tetap terpenuhi pada langkah 22 dan 29 membedakan caption validasi form dari
  caption Password Policy, supaya sumber penolakannya jelas.
- Status token dibaca di setiap subbagian sebagai pembuktian bahwa submit yang diblokir tidak
  mengonsumsi token, dan password lama masih berlaku pada langkah 35 sebagai pembuktian tidak ada
  perubahan kredensial.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.