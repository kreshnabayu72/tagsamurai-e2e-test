---
id: TC-AUTH-RST-E2E-020-submit-password-sukses-dan-reset-lock
title: Submit password baru sukses, konsumsi token, dan reset seluruh lock progression
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-58
  - TC-AUTH-RST-59
  - TC-AUTH-RST-80
  - TC-AUTH-RST-113
coverage:
  web: automated
---

# Submit password baru sukses, konsumsi token, dan reset seluruh lock progression

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User, dengan password lama yang
  diketahui dan tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di
  fixture. User ini bukan Default User dan bukan akun admin Total Control.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy dan
  berbeda dari password lama.
- `Spectra.env.AUTH_NEW_PASSWORD_2` adalah satu password baru kedua yang juga memenuhi seluruh
  Password Policy dan berbeda dari password lama serta dari
  `Spectra.env.AUTH_NEW_PASSWORD`, dipakai untuk user berikutnya pada spec ini.
- `Fixture.authResetPassword.users.activated.email` adalah email user tersebut.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut dengan masa berlaku 24 jam, lewat API Global Settings > User. Kemampuan ini
  disiapkan tim FE.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Submit password baru sukses pada user tanpa lock

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi halaman Setup New Password tampil
4. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
5. Isi field Confirm Password dengan nilai yang sama
6. Klik "Reset Password"
7. Verifikasi submit diterima dan tidak ada caption error
8. Verifikasi navigasi ke halaman Password Reset Successful terjadi
9. Verifikasi password baru user tersebut dapat dipakai untuk login
10. Verifikasi password lama user tersebut tidak lagi dapat dipakai untuk login
11. Verifikasi status token reset milik user tersebut berubah menjadi "consumed"
12. Verifikasi waktu konsumsi token terisi, sehingga token tidak bisa dipakai ulang
13. Verifikasi kedua surface pencatatan masing-masing memiliki satu entri baru dengan Status
    "Success" dan Note "Password updated successfully"
14. Verifikasi data identitas user di Global Settings > User tetap sama, yaitu nama, email, dan role
    tidak berubah

### Submit password baru berhasil melepas lock di seluruh tahap

15. Baca tahap lock user pada Global Settings > User sebelum submit
16. Buat satu token reset aktif milik user tersebut memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
17. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
18. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD_2`
19. Isi field Confirm Password dengan nilai yang sama
20. Klik "Reset Password"
21. Verifikasi navigasi ke halaman Password Reset Successful terjadi
22. Verifikasi password baru user tersebut dapat dipakai untuk login tanpa caption lock
23. Verifikasi tahap lock user pada Global Settings > User kembali ke keadaan tidak terkunci
24. Verifikasi counter failed attempts user kembali ke nol
25. Verifikasi waktu berakhir lock user dikosongkan
26. Verifikasi counter hari berturut-turut dengan percobaan gagal dalam satu jam kembali ke nol
27. Verifikasi banner lock tidak lagi tampil saat membuka halaman Login with Password

## Notes

- Spec ini sengaja tidak mengulang untuk keempat tahap lock satu per satu. Yang diuji adalah bahwa
  submit yang berhasil melepas lock dari tahap apa pun, jadi cukup satu user terkunci sebagai
  pembuktian. Keempat tahap lock beserta eskalasinya diuji lengkap di suite Auth Login with
  Password.
- Verifikasi counter lock dibaca dari Global Settings > User, bukan dari banner lock, karena banner
  hanya menampilkan tahap dan waktu absolut, bukan counter-nya.
- Username, email, dan role diperiksa ulang pada langkah 14 karena reset password hanya boleh
  mengubah kredensial dan state lock, bukan identitas user.
- `Spectra.env.AUTH_NEW_PASSWORD_2` dipakai agar submit kedua tidak memakai nilai yang sama dengan
  submit pertama dan tidak menabrak aturan password harus berbeda dari password lama.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.