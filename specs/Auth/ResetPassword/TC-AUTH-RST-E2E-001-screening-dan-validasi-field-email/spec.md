---
id: TC-AUTH-RST-E2E-001-screening-dan-validasi-field-email
title: Screening halaman Reset Password dan validasi field Email
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-1
  - TC-AUTH-RST-4
  - TC-AUTH-RST-5
  - TC-AUTH-RST-6
  - TC-AUTH-RST-7
  - TC-AUTH-RST-8
coverage:
  web: automated
---

# Screening halaman Reset Password dan validasi field Email

## Prerequisites

- Belum login dan session kosong. Alur dimulai dari halaman Login with Password.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE, bukan
  environment yang dipakai tester manual bersamaan.
- Satu user berstatus Activated dan Active di Global Settings > User. Email dan password-nya
  diketahui, dan user ini bukan Default User maupun bukan akun admin Total Control.
- `Fixture.authResetPassword.users.activated.email` adalah email user terdaftar tersebut.
- `Fixture.authResetPassword.data.email121Chars` adalah string email valid sepanjang 121 karakter.
- `Fixture.authResetPassword.data.email120Chars` adalah string email valid sepanjang 120 karakter dan
  terdaftar sebagai user aktif, sehingga submit pada batas tersebut diproses normal.
- `Fixture.authResetPassword.data.emailWithSpaces` adalah email user aktif tersebut yang ditulis
  dengan spasi di awal dan di akhir.
- `Fixture.authResetPassword.data.unknownEmail` adalah email berformat valid yang memang belum
  terdaftar di Global Settings > User.
- Caption error yang dirujuk diambil dari `Fixture.authResetPassword.captions`, tidak diketik ulang
  di spec ini.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`, sehingga submit yang butuh captcha terlewat bisa dijalankan
  tanpa moniker manual.

## Test Steps

### Screening halaman Reset Password

1. Buka halaman Login with Password di browser
2. Klik link "Forgot your password? Reset here"
3. Verifikasi judul halaman adalah "Reset Password"
4. Verifikasi field Email tampil dengan placeholder "Enter your email"
5. Verifikasi widget reCAPTCHA tampil di halaman
6. Verifikasi tombol "Reset Password" tampil dalam keadaan enabled
7. Verifikasi link "Log in with password" tampil di halaman
8. Verifikasi tidak ada field Password pada halaman ini, dalam keadaan apa pun
9. Verifikasi tidak ada checkbox Agreement di halaman ini, dalam keadaan apa pun

### Validasi Email kosong dan format salah

10. Klik "Reset Password" tanpa mengisi Email
11. Verifikasi caption inline di bawah field Email adalah "Email must not be empty"
12. Verifikasi tidak ada navigasi ke halaman mana pun
13. Verifikasi form tetap aktif, field Email tetap dapat diisi ulang, dan tombol "Reset Password"
    tetap enabled
14. Isi Email dengan `Fixture.authResetPassword.data.unknownEmail` yang bukan format email, lalu
    klik "Reset Password"
15. Verifikasi caption inline di bawah field Email adalah "Email format is incorrect"
16. Verifikasi caption tersebut muncul tanpa perlu menyentuh widget reCAPTCHA, sehingga validasi
    format email dievaluasi lebih dulu daripada reCAPTCHA
17. Verifikasi tidak ada navigasi ke halaman mana pun

### Batas panjang Email

18. Kosongkan field Email dengan tombol "Clear Field", lalu ketik
    `Fixture.authResetPassword.data.email121Chars`
19. Verifikasi caption "Max. 120 characters" muncul saat mengetik, sebelum tombol "Reset Password"
    diklik
20. Verifikasi klik "Reset Password" diblokir dan caption "Max. 120 characters" tetap tampil
21. Hapus satu karakter terakhir sehingga panjangnya tepat 120 karakter
22. Verifikasi caption "Max. 120 characters" hilang
23. Ganti isi field Email dengan `Fixture.authResetPassword.data.email120Chars` yang terdaftar sebagai
    user aktif, selesaikan reCAPTCHA, lalu klik "Reset Password"
24. Verifikasi caption validasi Email tidak muncul dan request diteruskan ke tahap evaluasi
    berikutnya oleh server
25. Verifikasi tidak ada caption "Email format is incorrect" maupun "Email must not be empty"

### Email dengan spasi di awal dan akhir

26. Kembali ke halaman Reset Password dari halaman Email Sent! lewat link "Back to Login" lalu link
    "Forgot your password? Reset here"
27. Isi field Email dengan `Fixture.authResetPassword.data.emailWithSpaces`, selesaikan reCAPTCHA,
    lalu klik "Reset Password"
28. Verifikasi caption "Email is not registered yet" tidak muncul, sehingga spasi diperlakukan
    sebagai bagian dari input yang di-trim sebelum lookup
29. Verifikasi request diproses sebagai email user aktif tersebut dan halaman Email Sent! tampil
30. Verifikasi caption validasi Email tidak muncul sama sekali pada submit ini

## Notes

- Spec ini hanya menguji perilaku tampilan dan validasi field. Yang diproses sampai menjadi request
  nyata hanyalah batas panjang 120 karakter dan email dengan spasi, yang keduanya memang TC sumber
  tandai perlu backend. Empat kondisi lain ditolak lebih dulu oleh validasi field sehingga tidak
  menyentuh backend.
- Pada TC-AUTH-RST-8, yang diuji adalah bahwa spasi di awal dan akhir tidak membuat email gagal
  lookup. Caption "Email is not registered yet" adalah pembeda yang salah bila input tidak di-trim,
  sehingga caption itu yang dipakai sebagai pembuktian, bukan email yang benar-benar terkirim.
- Karena halaman Email Sent! hanya menampilkan konfirmasi generik, spec ini tidak memakai isi email
  sebagai pembuktian hasil trim.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password" dan "Back to Login". Aturan
  `[Submit]` dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit
  entitas, bukan untuk halaman autentikasi.
- Password user uji tidak boleh ditulis di spec maupun fixture, dan spec ini tidak memakai password
  sama sekali.
- Error caption diambil dari `Fixture.authResetPassword.captions` sesuai aturan e2e-conventions.md
  bagian 9, supaya tidak diketik ulang di banyak spec.