---
id: TC-AUTH-RST-E2E-013-rate-limit-per-ip-dan-cooldown-60-detik
title: Rate limit per IP, cooldown 60 detik, dan independensi dua lapisan limit
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-31
  - TC-AUTH-RST-32
  - TC-AUTH-RST-33
coverage:
  web: automated
---

# Rate limit per IP, cooldown 60 detik, dan independensi dua lapisan limit

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Spec ini paling sensitif urutan di suite ini. Sebaiknya dijalankan sendirian, karena memakai
  sumber daya IP bersama dan mengubah counter limit bersama.
- `Fixture.authResetPassword.limits.perIp.maxRequestsPerHour` adalah batas request per IP per jam.
  Batas ini masih berstatus catatan engineering di PRD, sehingga angka tidak ditulis di spec ini dan
  spec mengirim request berulang sampai efek yang diamati muncul. Jumlah request yang terpakai
  dicatat sebagai bahan konfirmasi angka batas.
- `Fixture.authResetPassword.seedRequests.sendRequestViaApi` adalah cara mengirim request reset
  melalui endpoint yang sama dengan yang dipakai FE, untuk mengisi limit per IP dengan cepat tanpa
  membuka browser.
- `Fixture.authResetPassword.seedRequests.sendRequestViaApiWithProxy` adalah cara mengirim request
  dari IP yang sama pada environment uji, untuk memastikan pengujian per IP memakai satu sumber IP.
  Kemampuan ini disiapkan tim FE dan dicatat di `Fixture.authResetPassword.network.fixedClientIp`.
- `Fixture.authResetPassword.cooldown.durationSeconds` adalah durasi cooldown 60 detik yang
  ditegakkan server-side. Angka ini dibaca dari fixture, bukan ditulis di spec ini.
- `Fixture.authResetPassword.cooldown.release` adalah cara membuat cooldown selesai tanpa harus
  menunggu secara wall-clock.
- Hook `beforeEach` dan `afterEach` mengembalikan counter limit per IP dan per email ke keadaan
  awal, sehingga spec ini tidak bergantung pada spec lain.
- `Fixture.authResetPassword.users.activated.email` adalah email user aktif yang dipakai untuk
  memeriksa kondisi limit per email pada subbagian independensi.
- `Fixture.authResetPassword.data.unknownEmail` adalah email berformat valid yang belum terdaftar,
  dipakai sebagai email kedua pada subbagian independensi.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.

## Test Steps

### Rate limit per IP

1. Pastikan counter limit per IP berada di bawah batas
2. Kirim request berulang dari IP yang sama memakai
   `Fixture.authResetPassword.seedRequests.sendRequestViaApi` memakai email berbeda-beda sehingga
   limit per email tidak menjadi penyebab penolakan
3. Kirim satu request lagi dari IP yang sama setelah jumlah request melewati batas per jam
4. Verifikasi respons yang diterima adalah generik dan tidak menyebut batas atau jenis limit
5. Verifikasi request yang kena limit per IP tidak dicatat di kedua surface pencatatan auth,
   sehingga lapisan infrastruktur tidak terekspos lewat log
6. Verifikasi tidak ada entri baru pada kedua surface pencatatan untuk request tersebut

### Cooldown 60 detik antar request

7. Kirim satu request reset yang diproses normal untuk satu email
8. Catat waktu request tersebut
9. Kirim request atau resend lagi untuk email yang sama sebelum cooldown selesai
10. Verifikasi respons yang diterima tetap diproses sebagai sukses dan tidak menunjukkan error
11. Verifikasi tidak ada email reset kedua yang dibuat untuk email tersebut
12. Verifikasi tidak ada token reset kedua yang dibuat untuk email tersebut
13. Verifikasi nilai resend yang tersedia di respons tetap positif dan tidak negatif
14. Verifikasi cooldown ditegakkan di sisi server, bukan hanya dengan disablesnya tombol di UI
15. Verifikasi request baru diproses normal setelah cooldown selesai
16. Verifikasi cooldown dimulai ulang dari waktu request yang baru diproses

### Independensi limit per email dan limit per IP

17. Pastikan counter limit per email untuk
    `Fixture.authResetPassword.users.activated.email` sudah melewati batas limit per email
18. Verifikasi counter limit per IP untuk IP yang dipakai masih di bawah batas
19. Kirim request untuk `Fixture.authResetPassword.users.activated.email` dari IP tersebut
20. Verifikasi request tersebut tetap diproses dengan penyamaran respons, sesuai limit per email
21. Verifikasi email yang dipakai pada request tersebut tetap tercatat sebagai subjek
22. Kirim request untuk `Fixture.authResetPassword.data.unknownEmail` dari IP yang sama
23. Verifikasi request untuk email kedua tetap diproses normal, sehingga limit per email pada email
    pertama tidak memengaruhi email kedua
24. Verifikasi email kedua tidak kena limit per email karena counter-nya berbeda
25. Verifikasi email kedua tidak kena limit per IP karena request-nya masih di bawah batas per IP
26. Verifikasi kedua lapisan limit berjalan secara independen dan tidak saling menggantikan

## Notes

- Batas per IP dan batas per email sengaja dipisahkan menjadi dua spec karena sumber datanya
  berbeda. Limit per email terikat pada user, limit per IP terikat pada sumber jaringan, dan
  keduanya bisa aktif bersamaan.
- Angka batas per IP masih catatan engineering. Spec mengirim request berulang sampai respons generik
  muncul dan mencatat jumlah request-nya sebagai bahan konfirmasi.
- Verifikasi limit per IP memakai beberapa email berbeda-beda supaya efeknya benar-benar dari
  lapisan per IP. Kalau semua request memakai email yang sama, limit per email bisa lebih dulu
  aktif dan menutupi lapisan per IP.
- Cooldown diverifikasi lewat respons dan state server, bukan lewat disabled tombol, supaya
  ketegakannya di sisi server ikut terukur.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password" dan "Resend". Aturan `[Submit]`
  dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas,
  bukan untuk halaman autentikasi.