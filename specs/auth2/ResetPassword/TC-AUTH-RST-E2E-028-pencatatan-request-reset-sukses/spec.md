---
id: TC-AUTH-RST-E2E-028-pencatatan-request-reset-sukses
title: Pencatatan request reset sukses di kedua surface beserta IP dan Device atau Browser
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-75
  - TC-AUTH-RST-83
  - TC-AUTH-RST-119
coverage:
  web: automated
---

# Pencatatan request reset sukses di kedua surface beserta IP dan Device atau Browser

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. User ini bukan Default User dan bukan akun
  admin Total Control, sehingga pencatatannya tidak tercampur dengan entri pengguna lain.
- User tersebut belum melakukan request reset apa pun pada run ini, sehingga entri yang dibaca
  berasal dari request pada spec ini.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`, bersama kemampuan memfilter entri berdasarkan aksi,
  subjek, dan rentang waktu.
- `Fixture.authResetPassword.logs.expectedClientIp` adalah nilai IP yang diharapkan tercatat pada
  entri. Nilai itu dibaca dari fixture, bukan ditulis di spec ini, karena bergantung pada-topology
  environment uji.
- `Fixture.authResetPassword.logs.expectedDeviceBrowser` adalah nilai Device atau Browser yang
  diharapkan tercatat pada entri, mengikuti User-Agent dari browser environment uji dan dibaca dari
  fixture.
- `Fixture.authResetPassword.network.fixedClientIp` adalah cara memastikan request pada spec ini
  datang dari satu sumber IP yang sama, supaya kolom IP Address tidak berubah-ubah antar request.
- `Fixture.authResetPassword.mailbox` adalah kotak masuk uji untuk user tersebut, disiapkan tim FE.
- Kotak masuk uji dikosongkan dari email reset password sebelum spec berjalan.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.
- Nilai tidak sensitif yang dirujuk diambil dari fixture, dan tidak ada nilai sensitif yang ditulis
  di spec maupun fixture.

## Test Steps

### Request reset sukses tercatat di kedua surface

1. Pastikan kotak masuk uji kosong dari email reset password
2. Catat jumlah entri terakhir pada masing-masing surface pencatatan
3. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
4. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
5. Verifikasi navigasi ke halaman Email Sent! terjadi
6. Verifikasi kedua surface pencatatan masing-masing bertambah satu entri baru
7. Verifikasi entri baru pada kedua surface memiliki Aksi yang sama, yaitu request reset password
8. Verifikasi Status entri baru pada kedua surface adalah "Success"
9. Verifikasi Note entri baru pada kedua surface adalah "Password reset requested"
10. Verifikasi waktu pencatatan pada kedua surface identik atau berselisih paling sedikit
11. Verifikasi entri baru pada kedua surface menunjuk subjek yang sama, yaitu user tersebut
12. Verifikasi kedua entri merujuk aksi yang sama, sehingga tidak ada entri di satu surface saja
13. Verifikasi entri baru tidak membocorkan nilai password, nilai token, atau isi email penuh yang
    tidak perlu ditampilkan

### Kolom IP Address

14. Verifikasi kolom IP Address pada entri baru di kedua surface terisi
15. Verifikasi nilai IP Address pada kedua surface sama satu sama lain
16. Verifikasi nilai IP Address sesuai dengan `Fixture.authResetPassword.logs.expectedClientIp`
17. Verifikasi nilai IP Address sesuai dengan sumber request yang sebenarnya, yaitu leftmost
    address pada X-Forwarded-For bila ada, atau alamat socket langsung bila tidak ada
18. Verifikasi nilai IP Address tidak berasal dari nilai yang dipalsukan di dalam form atau payload,
    sehingga tidak bisa dipakai memancing pencatatan IP yang keliru

### Kolom Device atau Browser

19. Verifikasi kolom Device atau Browser pada entri baru di kedua surface terisi
20. Verifikasi nilai Device atau Browser pada kedua surface sama satu sama lain
21. Verifikasi nilai Device atau Browser sesuai dengan
    `Fixture.authResetPassword.logs.expectedDeviceBrowser`
22. Verifikasi formatnya adalah nama Browser diikuti nama OS, misalnya "Chrome on Windows"
23. Verifikasi formatnya tidak memuat nomor versi, sehingga nilainya stabil antar user agent
24. Verifikasi urutan kata pada formatnya adalah Browser dahulu lalu OS, bukan OS dahulu
25. Verifikasi formatnya bukan pola OS, garis miring, Browser, dan nomor versi
26. Verifikasi User-Agent yang tidak terparse menghasilkan nilai pengganti berupa garis horizontal,
    bukan string kosong atau teks error

## Notes

- Verifikasi kolom IP dan Device atau Browser tidak dilakukan pada entri acak, tapi pada entri yang
  dibaca pada langkah 6, supaya jelas kolom itu memang terisi untuk aksi yang diuji.
- Pencatatan Device atau Browser mengikuti format kanonikal lintas produk, dengan Browser dibaca lebih
  dulu dan tanpa nomor versi. Verifikasi format dilakukan pada nilai yang muncul, bukan hanya pada
  regex internal.
- Dua subbagian kolom dibaca dari entri yang sama supaya tidak ada entri tambahan yang menutupi
  nilai yang diuji.
- Yang tidak diuji di spec ini adalah entri untuk kondisi gagal, karena itu punya Note yang berbeda
  dan berada di spec 029. Spec ini hanya menutup kasus sukses beserta kolom IP dan Device atau
  Browser.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.