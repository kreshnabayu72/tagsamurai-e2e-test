---
id: TC-AUTH-RST-E2E-029-pencatatan-kondisi-request-gagal
title: Pencatatan kondisi request reset gagal di kedua surface
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-76
  - TC-AUTH-RST-77
  - TC-AUTH-RST-78
  - TC-AUTH-RST-79
coverage:
  web: automated
---

# Pencatatan kondisi request reset gagal di kedua surface

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Tiga kondisi data disiapkan lebih dulu, masing-masing punya subjek yang berbeda supaya entri yang
  dibaca tidak tertukar:
  - `Fixture.authResetPassword.users.inactive.email` adalah user yang sudah pernah diaktivasi tetapi
    Toggle Active dimatikan, sehingga berstatus Inactive.
  - `Fixture.authResetPassword.users.activated.email` adalah user aktif yang dipakai untuk memicu
    kondisi-too many reset attempts.
  - `Fixture.authResetPassword.data.unknownEmail` adalah email berformat valid yang belum pernah
    terdaftar, dipakai untuk kondisi email tidak ditemukan.
  - `Fixture.authResetPassword.data.crossEmailBurst` adalah daftar email yang dipakai untuk mengisi
    limit per IP pada kondisi too many per IP. Email-email tersebut berformat valid dan masing-masing
    belum terdaftar.
- `Fixture.authResetPassword.seedRequests.sendRequestViaApi` adalah cara mengirim request reset
  melalui endpoint yang sama dengan yang dipakai FE, untuk memicu kondisi limit tanpa membuka
  browser.
- `Fixture.authResetPassword.seedRequests.sendRequestViaApiWithProxy` adalah cara mengirim request
  dari satu sumber IP yang sama, dipakai untuk mengisi limit per IP. Kemampuan ini disiapkan tim
  FE dan dicatat di `Fixture.authResetPassword.network.fixedClientIp`.
- `Fixture.authResetPassword.limits.perIp.maxRequestsPerHour` adalah batas request per IP per jam,
  masih berstatus catatan engineering di PRD sehingga angka tidak ditulis di spec ini dan request
  dikirim berulang sampai efek yang diamati muncul.
- `Fixture.authResetPassword.limits.perEmail.maxAttempts` adalah batas percobaan per email, masih
  berstatus catatan engineering di PRD sehingga angka tidak ditulis di spec ini.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`, bersama kemampuan memfilter entri berdasarkan aksi,
  subjek, dan rentang waktu.
- Hook `beforeEach` dan `afterEach` mengembalikan counter limit per email dan per IP ke keadaan awal,
  sehingga spec ini tidak bergantung pada spec lain.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.

## Test Steps

### Akun Inactive tercatat di kedua surface

1. Catat jumlah entri terakhir pada masing-masing surface pencatatan
2. Isi field Email dengan `Fixture.authResetPassword.users.inactive.email`
3. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
4. Verifikasi caption yang tampil adalah "Your account is inactive"
5. Verifikasi kedua surface pencatatan masing-masing bertambah satu entri baru
6. Verifikasi Status entri baru pada kedua surface adalah "Failed"
7. Verifikasi Note entri baru pada kedua surface adalah "Account is inactive"
8. Verifikasi entri baru pada kedua surface menunjuk subjek yang sama, yaitu user tersebut
9. Verifikasi kedua surface mencatat entri yang sama, sehingga tidak ada entri di satu surface saja

### Too many reset attempts per email tercatat di kedua surface

10. Pastikan cooldown selesai untuk
    `Fixture.authResetPassword.users.activated.email`
11. Kirim request berulang untuk email tersebut memakai
    `Fixture.authResetPassword.seedRequests.sendRequestViaApi` sampai counter melewati batas limit
    per email
12. Catat jumlah entri terakhir pada masing-masing surface pencatatan
13. Isi field Email dengan `Fixture.authResetPassword.users.activated.email` dari browser
14. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
15. Verifikasi navigasi ke halaman Email Sent! tetap terjadi, sehingga kondisi ini disamarkan sebagai
    sukses
16. Verifikasi kedua surface pencatatan masing-masing bertambah satu entri baru
17. Verifikasi Status entri baru pada kedua surface adalah "Failed"
18. Verifikasi Note entri baru pada kedua surface adalah "Too many reset attempts"
19. Verifikasi entri baru pada kedua surface menunjuk subjek yang sama, yaitu user tersebut
20. Verifikasi entri tersebut membedakan subjek yang ada dari subjek yang tidak ada, sehingga Note-nya
    tidak sama dengan kondisi email tidak ditemukan

### Email tidak ditemukan tidak tercatat di kedua surface

21. Catat jumlah entri terakhir pada masing-masing surface pencatatan
22. Isi field Email dengan `Fixture.authResetPassword.data.unknownEmail`
23. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
24. Verifikasi caption yang tampil adalah "Email is not registered yet"
25. Verifikasi kedua surface pencatatan tidak bertambah entri baru
26. Verifikasi tidak ada entri pada kedua surface yang menyebut email tersebut
27. Verifikasi tidak ada entri dengan subjek kosong yang berasal dari request ini
28. Verifikasi counter rate limit internal tetap bertambah, sehingga anti-abuse tetap berjalan walaupun
    request tidak dicatat

### Too many per IP tidak tercatat di kedua surface

29. Pastikan cooldown selesai untuk email yang dipakai pada langkah berikutnya
30. Kirim request berulang dari satu sumber IP yang sama memakai
    `Fixture.authResetPassword.seedRequests.sendRequestViaApiWithProxy` dengan email-email dari
    `Fixture.authResetPassword.data.crossEmailBurst` sampai melewati batas limit per IP
31. Catat jumlah entri terakhir pada masing-masing surface pencatatan
32. Kirim satu request lagi dari sumber IP yang sama memakai
    `Fixture.authResetPassword.seedRequests.sendRequestViaApiWithProxy`
33. Verifikasi kedua surface pencatatan tidak bertambah entri baru untuk request tersebut
34. Verifikasi tidak ada entri pada kedua surface yang berasal dari lapisan limit per IP
35. Verifikasi request tersebut tidak dicatat walaupun memakai email berbeda-beda, sehingga lapisan
    infrastruktur tidak terekspos lewat pencatatan auth

## Notes

- Empat kondisi memakai subjek yang berbeda supaya absence of entri pada subbagian ketiga dan
  keempat tidak tertukar dengan entri dari subbagian sebelumnya. Karena itu setiap subbagian
  mencatat jumlah entri terakhir lebih dulu.
- Subbagian ketiga dan keempat sama-sama tidak menghasilkan entri, tetapi dibedakan karena alasan
  yang berbeda, yaitu tidak adanya subjek pada yang ketiga dan lapisan infrastruktur pada yang
  keempat. Verifikasi ketiadaan entri dilakukan terpisah supaya kegagalan salah satu tidak menutupi
  kegagalan yang lain.
- Angka batas limit masih catatan engineering, sehingga request dikirim berulang sampai efek yang
  diamati muncul. Jumlah request yang terpakai dicatat sebagai bahan konfirmasi angka batas, bukan
  diekspektasikan sebagai angka final.
- Verifikasi "tidak bertambah entri" dilakukan pada kedua surface sekaligus, karena yang diuji adalah
  tidak ada pencatatan sama sekali, bukan hanya tidak ada di salah satu surface.
- Note yang berbeda antara subbagian kedua dan ketiga dipakai sebagai pembuktian bahwa sistem
  memang membedakan dua kondisi yang sama-sama berstatus Failed dari sisi user.