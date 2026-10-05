---
id: TC-AUTH-RST-E2E-012-rate-limit-per-email-5-per-24-jam
title: Rate limit per email lima kali per 24 jam dengan penyamaran respons
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-28
  - TC-AUTH-RST-30
  - TC-AUTH-RST-86
coverage:
  web: automated
---

# Rate limit per email lima kali per 24 jam dengan penyamaran respons

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. User ini bukan Default User dan bukan akun
  admin Total Control.
- User tersebut belum melakukan request maupun resend apa pun dalam 24 jam terakhir, sehingga
  counter awal benar-benar nol. Hook `beforeEach` memverifikasi dan mengembalikan counter tersebut
  ke keadaan awal, `afterEach` mengembalikannya juga, sehingga spec ini tidak bergantung pada spec
  lain.
- `Fixture.authResetPassword.seedRequests.occupyPerEmailQuota` adalah cara mengisi counter
  `password_reset_attempt` milik user tersebut sampai batas bawah limit, yaitu sebelum percobaan
  berikutnya. Kemampuan ini disiapkan tim FE. Jumlah percobaan yang dipakai untuk mengisi quota
  diambil dari `Fixture.authResetPassword.limits.perEmail.window` dan
  `Fixture.authResetPassword.limits.perEmail.maxAttempts`, bukan angka yang ditulis di spec ini.
- `Fixture.authResetPassword.seedRequests.sendRequestViaApi` adalah cara mengirim request reset
  melalui endpoint yang sama dengan yang dipakai FE, tanpa membuka browser, untuk mengisi quota
  dengan cepat.
- `Fixture.authResetPassword.users.activated.email` belum menyentuh limit per IP, sehingga efek
  yang diamati murni berasal dari limit per email.
- `Fixture.authResetPassword.limits.perEmail.maxAttempts` masih berstatus catatan engineering di
  PRD. Verifikasi dilakukan dengan mengirim request berulang sampai penyamaran yang diamati muncul,
  dan jumlah request yang terpakai dicatat sebagai bahan konfirmasi angka batas, bukan
  mengasumsikan angka final.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.
- Toast yang dirujuk diambil dari `Fixture.authResetPassword.captions`.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.

## Test Steps

### Percobaan setelah quota per email habis disamarkan sebagai sukses

1. Pastikan counter `password_reset_attempt` user tersebut berada di bawah batas limit
2. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
3. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
4. Verifikasi navigasi ke halaman Email Sent! terjadi
5. Catat tampilan halaman Email Sent! sebagai pembanding
6. Pastikan cooldown selesai, lalu isi ulang field Email dengan email yang sama dan kirim request
   berikutnya memakai `Fixture.authResetPassword.seedRequests.sendRequestViaApi` sampai counter
   melewati batas limit
7. Kirim satu request lagi dari browser memakai langkah 2 sampai 3
8. Verifikasi navigasi ke halaman Email Sent! tetap terjadi
9. Verifikasi message pada halaman Email Sent! identik dengan tampilan pada langkah 5
10. Verifikasi tidak ada caption error, tidak ada badge limit, dan tidak ada countdown berbeda
11. Verifikasi tidak ada elemen UI yang membedakan kondisi terbatas dari kondisi sukses
12. Verifikasi tidak ada perbedaan struktur halaman antara kondisi terbatas dan kondisi sukses

### Percobaan setelah quota per email habis dicatat

13. Catat jumlah entri terakhir pada kedua surface pencatatan
14. Pastikan cooldown selesai, lalu kirim satu request lagi dari browser memakai email yang sama
15. Verifikasi kedua surface pencatatan masing-masing memiliki satu entri baru
16. Verifikasi Status entri baru adalah "Failed"
17. Verifikasi Note entri baru adalah "Too many reset attempts"
18. Verifikasi subjek user teridentifikasi pada entri tersebut, sehingga percobaan yang kena limit
    dicatat karena subjeknya memang ada

### Limit per email tetap ditegakkan untuk email yang tidak terdaftar

19. Pastikan cooldown selesai
20. Kirim request dengan `Fixture.authResetPassword.data.unknownEmail` yang tidak terdaftar memakai
    `Fixture.authResetPassword.seedRequests.sendRequestViaApi` sampai counter melewati batas limit
21. Verifikasi request pada email yang tidak terdaftar tetap diproses tanpa error yang berbeda
22. Verifikasi counter `password_reset_attempt` bertambah pada email tersebut, sehingga quota
    per email tetap ditegakkan walaupun tidak ada subjek user

### Request dan resend berbagi satu quota

23. Pastikan counter `password_reset_attempt` user tersebut berada di bawah batas limit
24. Kirim request reset untuk user tersebut melalui browser
25. Pastikan cooldown selesai
26. Klik "Resend" pada halaman Email Sent!
27. Pastikan cooldown selesai, lalu ulangi klik "Resend" sampai jumlah request dan resend
    mendekati batas limit
28. Verifikasi counter `password_reset_attempt` terakumulasi dari request maupun resend
29. Verifikasi request dan resend memakai satu counter yang sama, bukan dua counter terpisah
30. Verifikasi setelah jumlah gabungan melewati batas limit, request berikutnya disamarkan sebagai
    sukses

## Notes

- Spec ini memakai `Fixture.authResetPassword.seedRequests.sendRequestViaApi` untuk mengisi quota
  supaya tidak perlu melakukan puluhan klik manual. Endpoint yang dipakai adalah endpoint yang sama
  dengan FE, sehingga percobaan yang terhitung benar-benar percobaan dari sisi server.
- Angka batas limit belum final di PRD. Spec ini mengirim request berulang sampai efek yang
  diamati muncul, lalu mencatat jumlah request-nya sebagai bahan konfirmasi, dan tidak menulis
  angka batas sebagai ekspektasi.
- Yang diuji pada subbagian pertama adalah penyamaran, yaitu tidak adanya pembedaan UI. Karena itu
  pembanding diambil dari halaman sukses pada langkah 5, bukan dari expectations PRD.
- Limit per IP dan cooldown 60 detik punya spec sendiri di spec 013, supaya efeknya tidak
  tertukar dengan limit per email.
- Toast dan caption diambil dari `Fixture.authResetPassword.captions` sesuai aturan
  e2e-conventions.md bagian 9.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password" dan "Resend". Aturan `[Submit]`
  dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas,
  bukan untuk halaman autentikasi.