---
id: TC-AUTH-RST-E2E-004-account-status-gate-dan-urutan-evaluasi
title: Account Status Gate dan urutan evaluasi pada halaman Reset Password
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-9
  - TC-AUTH-RST-10
  - TC-AUTH-RST-11
  - TC-AUTH-RST-12
coverage:
  web: automated
---

# Account Status Gate dan urutan evaluasi pada halaman Reset Password

## Prerequisites

- Belum login dan session kosong. Halaman Reset Password terbuka di browser.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Tiga user disiapkan lebih dulu di Global Settings > User dan dikembalikan ke keadaan awal di
  `afterEach`:
  - Satu user aktif, bukan Default User dan bukan akun admin Total Control.
    Email-nya adalah `Fixture.authResetPassword.users.activated.email`.
  - Satu user yang sudah pernah diaktivasi tetapi Toggle Active dimatikan, sehingga berstatus
    Inactive. Email-nya adalah `Fixture.authResetPassword.users.inactive.email`.
  - Satu user yang sudah pernah terdaftar lalu dihapus, sehingga emailnya tidak lagi ada di
    Global Settings > User. Email-nya adalah `Fixture.authResetPassword.data.deletedUserEmail`.
- `Fixture.authResetPassword.data.unknownEmail` adalah email berformat valid yang memang belum pernah
  terdaftar, untuk membedakan kondisi belum terdaftar dari kondisi pernah terdaftar lalu dihapus.
- `Fixture.authResetPassword.data.invalidEmailFormat` adalah string yang bukan email valid.
- `Fixture.authResetPassword.data.wrongCaptchaState` adalah kondisi captcha yang sengaja dibiarkan
  belum diselesaikan pada environment otomasi.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.
- Caption error yang dirujuk diambil dari `Fixture.authResetPassword.captions`.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log, yang dipakai untuk
  verifikasi tidak-tercatat.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.

## Test Steps

### Email belum terdaftar

1. Isi field Email dengan `Fixture.authResetPassword.data.unknownEmail`, selesaikan reCAPTCHA,
   lalu klik "Reset Password"
2. Verifikasi caption inline di bawah field Email adalah "Email is not registered yet"
3. Verifikasi tidak ada navigasi ke halaman Email Sent!
4. Verifikasi tidak ada entri baru di kedua surface pencatatan, sehingga ketiadaan subjek user tidak
   pernah terekspos lewat log

### Akun Inactive

5. Kosongkan field Email dengan tombol "Clear Field", isi dengan
   `Fixture.authResetPassword.users.inactive.email`, selesaikan reCAPTCHA, lalu klik "Reset Password"
6. Verifikasi caption inline di bawah field Email adalah "Your account is inactive"
7. Verifikasi tidak ada navigasi ke halaman Email Sent!
8. Verifikasi tidak ada token reset yang dibuat untuk user tersebut
9. Verifikasi kedua surface pencatatan masing-masing memiliki satu entri baru dengan Status "Failed"
   dan Note "Account is inactive"

### Akun sudah dihapus

10. Kosongkan field Email dengan tombol "Clear Field", isi dengan
    `Fixture.authResetPassword.data.deletedUserEmail`, selesaikan reCAPTCHA, lalu klik "Reset Password"
11. Verifikasi caption inline di bawah field Email adalah "Email is not registered yet"
12. Verifikasi caption tersebut identik dengan kondisi email yang belum pernah terdaftar
13. Verifikasi caption dan halaman tidak membocorkan bahwa email tersebut pernah terdaftar
14. Verifikasi tidak ada navigasi ke halaman Email Sent!
15. Verifikasi tidak ada entri baru di kedua surface pencatatan

### Urutan evaluasi

16. Kosongkan field Email dengan tombol "Clear Field", isi dengan
    `Fixture.authResetPassword.data.invalidEmailFormat`, biarkan reCAPTCHA belum diselesaikan,
    lalu klik "Reset Password"
17. Verifikasi caption yang muncul adalah caption format email, bukan caption reCAPTCHA
18. Verifikasi caption tersebut diambil dari `Fixture.authResetPassword.captions` untuk format email
19. Verifikasi tidak ada entri baru di kedua surface pencatatan
20. Ganti field Email dengan `Fixture.authResetPassword.data.unknownEmail`, biarkan reCAPTCHA belum
    diselesaikan, lalu klik "Reset Password"
21. Verifikasi caption yang muncul adalah caption reCAPTCHA, bukan caption email belum terdaftar
22. Verifikasi caption tersebut diambil dari `Fixture.authResetPassword.captions` untuk reCAPTCHA
23. Verifikasi caption "Email is not registered yet" tidak muncul pada tahap ini, sehingga lookup
    status akun belum dijalankan
24. Verifikasi tidak ada entri baru di kedua surface pencatatan
25. Verifikasi tidak ada navigasi ke halaman mana pun pada seluruh spec ini

## Notes

- Dua subjek deleted dipakai untuk membedakan dua kondisi yang sengaja dibuat menghasilkan caption
  sama. Kalau keduanya dibedakan di UI, itu bocoru enumerasi dan bertentangan dengan PRD.
- Penghapusan user adalah langkah yang mengubah data bersama. Hook `beforeEach` menyiapkan user
  tersebut dan `afterEach` mengembalikan GLOBAL state, jadi spec ini tidak bergantung pada spec
  lain.
- Counter rate limit internal untuk anti-abuse tetap bertambah pada kondisi email belum terdaftar,
  tetapi itu counter internal yang tidak terlihat di UI dan tidak masuk surface pencatatan.
  Verifikasi counter itu tidak dilakukan di spec ini.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.
- Error caption diambil dari `Fixture.authResetPassword.captions` sesuai aturan e2e-conventions.md
  bagian 9, supaya tidak diketik ulang di banyak spec.