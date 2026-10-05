---
id: TC-AUTH-LP-E2E-015-navigasi-email-handoff
title: Navigasi keluar halaman Login dan email handoff ke Login with OTP serta Reset Password
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-3
  - TC-AUTH-LP-52
  - TC-AUTH-LP-53
  - TC-AUTH-LP-54
coverage:
  web: automated
---

# Navigasi keluar halaman Login dan email handoff ke Login with OTP serta Reset Password

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan user uji berstatus Activated dan Active dengan kredensial benar, dibuat lewat API Global Settings > User dan direstore di `afterEach`.
- Password asli user tersebut tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.users.emailHandoff` berisi email uji yang dipakai pada langkah navigasi, dipilih supaya tidak sama dengan user lain di spec ini.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- URL tujuan tiap navigasi diamati lewat address bar dan query parameter-nya, sesuai PRD §4.7 ayat 1 yang menyebut pengalihan email lewat `?email=`.
- Halaman Login with OTP milik modul `auth/login-otp`. Yang diuji di sini handoff email dari modul ini, bukan langkah internal OTP.

## Test Steps

### Email terbawa ke Login with OTP

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.emailHandoff.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
3. Catat jumlah entri di User Log sebagai pembanding
4. Klik tautan "Log in with OTP"
5. Verifikasi browser berpindah ke halaman Login with OTP
6. Verifikasi query parameter `email` pada address bar bernilai `Fixture.authLoginPassword.users.emailHandoff.email`
7. Verifikasi field Email di halaman Login with OTP terisi dengan email yang sama tanpa perlu diketik ulang
8. Verifikasi jumlah entri di User Log tidak berubah, sehingga navigasi keluar dari halaman ini bukan percobaan login dan tidak dicatat

### Email terbawa ke Reset Password

9. Kembali ke `/login`
10. Isi Email dengan `Fixture.authLoginPassword.users.emailHandoff.email`
11. Klik tautan "Reset here"
12. Verifikasi browser berpindah ke halaman Reset Password
13. Verifikasi query parameter `email` pada address bar bernilai `Fixture.authLoginPassword.users.emailHandoff.email`
14. Verifikasi field Email di halaman Reset Password terisi dengan email yang sama
15. Verifikasi jumlah entri di User Log tidak berubah, sehingga navigasi ini juga bukan percobaan login

### Klik tautan tanpa email diisi

16. Kembali ke `/login`
17. Pastikan field Email kosong
18. Klik tautan "Log in with OTP"
19. Verifikasi browser tetap berpindah ke halaman Login with OTP
20. Verifikasi tidak ada caption error validasi Email yang muncul, sehingga navigasi tidak diblokir form
21. Verifikasi field Email di halaman tujuan kosong
22. Kembali ke `/login` lalu pastikan field Email kosong
23. Klik tautan "Reset here"
24. Verifikasi browser tetap berpindah ke halaman Reset Password
25. Verifikasi tidak ada caption error validasi Email yang muncul
26. Verifikasi field Email di halaman tujuan kosong

### Kembali dari OTP lewat Edit email

27. Kembali ke `/login`
28. Isi Email dengan `Fixture.authLoginPassword.users.emailHandoff.email`
29. Klik tautan "Log in with OTP" lalu verifikasi field Email terbawa
30. Kembali ke halaman Login with OTP dan klik "Edit email"
31. Verifikasi browser kembali ke halaman Login with Password
32. Verifikasi field Email terisi otomatis dengan email yang tadi diketik, sesuai PRD §4.10 default field value
33. Verifikasi field Password kosong, sehingga credentials yang diketik sebelumnya tidak terbawa
34. Verifikasi jumlah entri di User Log tidak berubah

## Notes

- Navigasi keluar dari halaman ini tidak pernah mengirim request login, sehingga tidak menambah `failed_count` dan tidak menulis entri User Log. Langkah 8, 15, dan 34 adalah pembuktian itu.
- Mekanisme handoff adalah query parameter `?email=` sesuai PRD §4.7 ayat 1. Karena itu verifikasi dilakukan pada address bar, bukan hanya pada isi field tujuan.
- Kasus tanpa email yang diisi sengaja ikut di sini karena §4.7 tidak mewajibkan email terisi untuk navigasi, dan TC-AUTH-LP-54 secara eksplisit menyatakan navigasi tetap terjadi tanpa error.
- Email prefilled dari "Edit email" diuji di spec ini, bukan di spec lain, karena itu satu-satunya jalur yang memunculkan email terisi otomatis di halaman Login with Password.
- Halaman Login with OTP dan Reset Password punya TC-nya masing-masing di modulnya. Yang di sini hanya bukti bahwa email berhasil dibawa, bukan alur OTP atau resetnya.
- Spec ini memakai satu user uji, karena semua skenario hanya bergantung pada string email dan tidak mengubah state akun.
- Jumlah entri User Log dibaca dari User Log user uji itu sendiri, bukan log gabungan, supaya tidak tertimpa spec lain.