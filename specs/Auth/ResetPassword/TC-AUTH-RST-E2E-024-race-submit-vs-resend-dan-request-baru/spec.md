---
id: TC-AUTH-RST-E2E-024-race-submit-vs-resend-dan-request-baru
title: Race lintas aksi antara Submit New Password dan Resend atau Request baru
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-115
  - TC-AUTH-RST-116
coverage:
  web: automated
---

# Race lintas aksi antara Submit New Password dan Resend atau Request baru

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- `Mode: mock`. Spec ini memakai intercept respons untuk menahan respons submit sampai aksi lain
  dikirim, sehingga kedua request benar-benar berada di server dalam jendela waktu yang dekat.
  Kemampuan intercept dan penundaan respons disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.network`, dengan key terpisah untuk
  `Fixture.authResetPassword.network.submitPassword` dan
  `Fixture.authResetPassword.network.resendEmail` atau
  `Fixture.authResetPassword.network.requestReset`.
- `Fixture.authResetPassword.network.delayMs` adalah durasi penundaan yang dipakai untuk menyamakan
  waktu kedatangan kedua request. Nilainya diambil dari fixture, bukan diasumsikan sebagai angka
  final.
- Dua user berstatus Activated dan Active di Global Settings > User, dengan password lama yang
  diketahui dan tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di
  fixture. Keduanya bukan Default User dan bukan akun admin Total Control.
  - `Fixture.authResetPassword.users.activated.email` adalah user untuk race Submit versus Resend.
  - `Fixture.authResetPassword.users.activatedSecondary.email` adalah user untuk race Submit versus
    Request baru.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy dan
  berbeda dari password lama.
- `Spectra.env.AUTH_NEW_PASSWORD_2` adalah satu password baru kedua yang juga memenuhi seluruh
  Password Policy dan berbeda dari password lama user kedua.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tertentu dengan masa berlaku 24 jam, lewat API Global Settings > User.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca daftar token reset milik
  user beserta statusnya.
- `Fixture.authResetPassword.cooldown.release` adalah cara membuat cooldown selesai tanpa harus
  menunggu secara wall-clock.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Submit di tab A berlomba dengan Resend di tab B

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Buka tautan reset dari token tersebut di tab A memakai
   `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi halaman Setup New Password tampil pada tab A
4. Isi field Password pada tab A dengan `Spectra.env.AUTH_NEW_PASSWORD`
5. Isi field Confirm Password pada tab A dengan nilai yang sama
6. Buat halaman Email Sent pada tab B untuk user yang sama, lalu pastikan cooldown selesai dengan
    `Fixture.authResetPassword.cooldown.release`
7. Aktifkan penundaan respons pada `Fixture.authResetPassword.network.submitPassword`
8. Klik "Reset Password" pada tab A
9. Klik "Resend" pada tab B nyaris bersamaan
10. Verifikasi kedua request benar-benar dikirim ke server, bukan hanya satu yang terkirim
11. Verifikasi hasil akhir tab A konsisten, yaitu navigasi ke halaman Password Reset Successful atau
    redirect ke halaman 404, tanpa error yang tidak terduga
12. Verifikasi hasil akhir tab B tetap menampilkan halaman Email Sent!
13. Verifikasi status token yang dipakai di tab A berakhir pada satu status final, yaitu "consumed"
    atau "invalidated", dan tidak ambigu
14. Verifikasi hanya satu status final yang tercatat untuk token tersebut
15. Verifikasi bila token berakhir "invalidated", password user tersebut tidak berubah dan submit di
    tab A ditolak dengan caption link reset kedaluwarsa
16. Verifikasi bila token berakhir "invalidated", kedua surface pencatatan masing-masing memiliki satu
    entri baru dengan Status "Failed" dan Note "Reset link expired"
17. Verifikasi bila token berakhir "consumed", password user tersebut hanya berubah satu kali dan
    seluruh lock progression ter-reset seperti pada submit sukses
18. Verifikasi token baru dari Resend tetap aktif dan dapat dipakai untuk menyelesaikan reset
19. Verifikasi tidak pernah ada dua token aktif milik user tersebut pada saat yang bersamaan
20. Verifikasi tidak ada kondisi campuran, yaitu password berubah sementara token juga berubah
    status menjadi tidak aktif tanpa ada aksi yang menyatakannya
21. Nonaktifkan penundaan respons

### Submit di tab A berlomba dengan Request baru dari halaman awal di tab B

22. Buat satu token reset aktif milik
    `Fixture.authResetPassword.users.activatedSecondary.email` memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
23. Buka tautan reset dari token tersebut di tab A memakai
    `Fixture.authResetPassword.tokens.linkForToken`
24. Verifikasi halaman Setup New Password tampil pada tab A
25. Isi field Password pada tab A dengan `Spectra.env.AUTH_NEW_PASSWORD_2`
26. Isi field Confirm Password pada tab A dengan nilai yang sama
27. Buka halaman Reset Password dari awal pada tab B
28. Isi field Email pada tab B dengan email user yang sama
29. Aktifkan penundaan respons pada `Fixture.authResetPassword.network.submitPassword`
30. Klik "Reset Password" pada tab A
31. Klik "Reset Password" pada tab B nyaris bersamaan
32. Verifikasi kedua request benar-benar dikirim ke server, bukan hanya satu yang terkirim
33. Verifikasi hasil akhir tab A konsisten, yaitu navigasi ke halaman Password Reset Successful atau
    redirect ke halaman 404, tanpa error yang tidak terduga
34. Verifikasi hasil akhir tab B konsisten, yaitu navigasi ke halaman Email Sent!
35. Verifikasi status token yang dipakai di tab A berakhir pada satu status final, yaitu "consumed"
    atau "invalidated", dan tidak ambigu
36. Verifikasi bila token berakhir "invalidated", password user tersebut tidak berubah dan submit di
    tab A ditolak dengan caption link reset kedaluwarsa
37. Verifikasi bila token berakhir "consumed", password user tersebut hanya berubah satu kali
38. Verifikasi request pada tab B diproses normal pada kedua kemungkinan hasil, sehingga tab B tidak
    menampilkan error yang tidak diharapkan
39. Verifikasi bila request pada tab B diproses dan menghasilkan token baru, token lama pada tab A
    tidak kembali menjadi aktif
40. Verifikasi password yang sudah tersimpan tidak terpengaruh oleh request pada tab B
41. Verifikasi hanya satu token aktif milik user tersebut pada saat yang bersamaan
42. Verifikasi tidak ada kondisi campuran antara password yang sudah berubah dan token yang berubah
    status
43. Nonaktifkan penundaan respons

## Notes

- Yang diuji pada spec ini adalah hasil akhir yang konsisten, bukan urutan siapa yang menang. Hasil
  akhir yang benar berbeda antara kedua kemungkinan, dan keduanya sama-sama sah karena
  keduanya mempertahankan invarian.
- Invarian yang dijaga di kedua subbagian adalah password hanya berubah satu kali atau tidak sama
  sekali, token yang dipakai di tab A berakhir pada satu status final, dan tidak pernah ada dua
  token aktif milik user yang sama pada saat bersamaan.
- Keduanya tidak boleh dikaburkan dengan mengasumsikan satu hasil tertentu, karena penundaan respons
  tidak menjamin request mana yang lebih dulu ter-commit di server.
- Dua user dipisahkan supaya token dan counter dari subbagian pertama tidak ikut memengaruhi
  subbagian kedua.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable, tidak
  ditulis di spec maupun fixture.