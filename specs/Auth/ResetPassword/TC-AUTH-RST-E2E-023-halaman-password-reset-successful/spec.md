---
id: TC-AUTH-RST-E2E-023-halaman-password-reset-successful
title: Halaman Password Reset Successful dan navigasinya
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-67
  - TC-AUTH-RST-68
  - TC-AUTH-RST-69
coverage:
  web: automated
---

# Halaman Password Reset Successful dan navigasinya

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User, dengan password lama yang
  diketahui dan tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di
  fixture. User ini bukan Default User dan bukan akun admin Total Control.
- `Fixture.authResetPassword.users.activated.email` adalah email user tersebut.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy dan
  berbeda dari password lama.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut dengan masa berlaku 24 jam, lewat API Global Settings > User. Kemampuan ini
  disiapkan tim FE.
- `Fixture.authResetPassword.tokens.seedConsumedToken` adalah cara membuat satu token reset yang
  statusnya sudah dipakai, dipakai pada subbagian reload link.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tertentu tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset.
- Caption halaman sukses diambil dari `Fixture.authResetPassword.captions`, supaya teks panjangnya
  tidak diketik ulang di spec ini.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Tampilan halaman sukses setelah submit

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi halaman Setup New Password tampil
4. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
5. Isi field Confirm Password dengan nilai yang sama
6. Klik "Reset Password"
7. Verifikasi navigasi ke halaman Password Reset Successful terjadi
8. Verifikasi ilustrasi sukses tampil di halaman
9. Verifikasi judul halaman adalah "Password Reset Successful"
10. Verifikasi message halaman sesuai dengan caption sukses dari
    `Fixture.authResetPassword.captions`
11. Verifikasi CTA pada halaman adalah "Go to Login Page"
12. Verifikasi tidak ada field Email, tidak ada field Password, dan tidak ada form pada halaman ini
13. Verifikasi tidak ada checklist Password Policy pada halaman ini
14. Verifikasi tidak ada widget reCAPTCHA pada halaman ini

### Navigasi CTA ke Login with Password

15. Klik "Go to Login Page"
16. Verifikasi navigasi ke halaman Login with Password terjadi
17. Verifikasi field Email pada halaman Login tampil dalam keadaan kosong
18. Verifikasi field Password pada halaman Login tampil dalam keadaan kosong
19. Verifikasi tidak ada toast error dan tidak ada halaman error yang tampil
20. Verifikasi tidak ada satu pun parameter token atau password pada URL halaman tujuan

### Membuka ulang link setelah submit sukses

21. Baca token milik user tersebut sebelum submit
22. Susun tautan reset dari token tersebut memakai
    `Fixture.authResetPassword.tokens.linkForToken`
23. Buka tautan reset tersebut di browser
24. Verifikasi halaman 404 tampil
25. Verifikasi Title pada halaman adalah "Reset Link Already Used"
26. Verifikasi CTA pada halaman adalah "Go to Login"
27. Verifikasi tidak ada halaman Setup New Password yang tampil
28. Verifikasi password user tersebut tetap sama seperti hasil submit pada langkah 6

## Notes

- Halaman sukses sengaja tidak dipakai sebagai tempat memverifikasi status token maupun lock, karena
  status token dan lock dibaca di spec 020 dari sumber yang sama.
- Verifikasi bahwa halaman sukses tidak membawa form maupun reCAPTCHA dilakukan sebagai pembuktian
  bahwa alur sudah benar-benar selesai dan tidak ada aksi tersisa di halaman tersebut.
- Subbagian ketiga memakai tautan yang disusun ulang dari token yang sama, bukan tautan dari email,
  supaya tidak bergantung pada mailbox uji.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password" dan "Go to Login Page". Aturan
  `[Submit]` dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit
  entitas, bukan untuk halaman autentikasi.