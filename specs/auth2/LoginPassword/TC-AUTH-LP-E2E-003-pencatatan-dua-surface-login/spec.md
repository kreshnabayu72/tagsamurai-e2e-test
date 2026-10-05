---
id: TC-AUTH-LP-E2E-003-pencatatan-dua-surface-login
title: Pencatatan login sukses di kedua surface serta format kolom Device Browser dan IP Address
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-55
  - TC-AUTH-LP-57
  - TC-AUTH-LP-59
  - TC-AUTH-LP-94
coverage:
  web: automated
---

# Pencatatan login sukses di kedua surface serta format kolom Device Browser dan IP Address

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- `Fixture.authLoginPassword.users.routine` berisi user berstatus Activated dan Active yang sudah pernah login sebelumnya, sudah menerima Privacy Policy versi terbaru, dan `last_logout_at`-nya kurang dari 30 hari sehingga tidak memicu layar Confirm to Continue. User ini bukan Default User dan dibuat lewat API Global Settings > User.
- `Spectra.env.AUTH_PASSWORD` berisi password asli user tersebut. Nilai ini tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.data.unregisteredEmail` berisi email yang memang belum terdaftar di Global Settings > User.
- `Fixture.authLoginPassword.data.invalidEmailFormat` berisi email dengan format tidak valid.
- `Fixture.authLoginPassword.log.activityLogPath` berisi rute halaman Global Settings > Activity Log > Session.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- `Fixture.authLoginPassword.captions.notes` berisi seluruh enum Note kanon yang boleh muncul di kedua surface.
- `Fixture.authLoginPassword.expected.userAgent` berisi User-Agent browser yang dipakai saat run ini, yaitu Chrome di Windows.
- Pencatatan dicek lewat UI Global Settings oleh user dengan role Total Control pada entity Client, bukan lewat query database. Sesi admin dibuka lewat hook dan ditutup di `afterEach` supaya spec ini dapat dijalankan sendiri.

## Test Steps

### Login sukses tercatat di kedua surface

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.routine.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
4. Verifikasi browser berpindah ke Portal — Product Hub
5. Catat jumlah baris pada kedua surface sebelum login berikutnya sebagai pembanding
6. Verifikasi kolom Activity Log > Session yang tersedia adalah Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, dan Device / Browser
7. Verifikasi kolom Date berada pada posisi pertama, dan tidak ada kolom Modified By maupun Last Updated
8. Buka User Detail milik `Fixture.authLoginPassword.users.routine` lalu verifikasi tab User Log menampilkan kolom Date, Activity, Status, Note, IP Address, dan Device / Browser
9. Verifikasi kedua surface memakai sekumpulan kolom yang sama untuk field yang sama, sehingga tidak ada kolom yang hanya ada di satu surface

### Entri login sukses

10. Kembali ke `/login` dan login lagi dengan user yang sama untuk menghasilkan entri kedua yang mudah dibedakan
11. Verifikasi browser berpindah ke Portal — Product Hub
12. Kembali ke Activity Log > Session
13. Verifikasi satu entri baru muncul dengan Activity "Login"
14. Verifikasi Status entri tersebut adalah "Success"
15. Verifikasi Note entri tersebut adalah "Login with password"
16. Verifikasi jumlah baris bertambah tepat satu
17. Buka User Detail milik user tersebut lalu buka tab User Log
18. Verifikasi satu entri baru muncul dengan isi yang sama persis pada kedua surface, sehingga satu attempt login hanya menghasilkan satu entri per surface
19. Verifikasi tanggal dan IP Address pada entri di User Log sama dengan nilai pada entri di Activity Log
20. Verifikasi tidak ada entri "Success" ganda untuk satu attempt login
21. Logout dari Portal sehingga session kosong

### Kolom IP Address terisi sesuai sumbernya

22. Catat IP address yang dipakai environment run ini sebagai pembanding
23. Isi Email dengan `Fixture.authLoginPassword.users.routine.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`, selesaikan reCAPTCHA, lalu klik "Log in"
24. Verifikasi browser berpindah ke Portal — Product Hub
25. Verifikasi kolom IP Address pada entri login yang baru terisi dan tidak kosong
26. Verifikasi nilai IP Address tersebut berasal dari direct socket atau dari leftmost trusted `X-Forwarded-For` sesuai konfigurasi proxy environment ini
27. Verifikasi nilai yang sama muncul pada entri di User Log
28. Logout dari Portal sehingga session kosong

### Format Device / Browser kanonikal

29. Catat User-Agent browser yang dipakai run ini dari `Fixture.authLoginPassword.expected.userAgent`
30. Isi Email dengan `Fixture.authLoginPassword.users.routine.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`, selesaikan reCAPTCHA, lalu klik "Log in"
31. Verifikasi browser berpindah ke Portal — Product Hub
32. Verifikasi kolom Device / Browser pada entri login yang baru terisi
33. Verifikasi format Device / Browser adalah "Browser on OS" tanpa nomor versi
34. Verifikasi format tersebut bukan "OS / Browser versi"
35. Verifikasi nilai yang sama muncul pada entri di User Log
36. Logout dari Portal sehingga session kosong

### Attempt tanpa subjek user tidak dicatat

37. Buka `/login` lalu catat jumlah baris pada kedua surface sebagai pembanding
38. Isi Email dengan `Fixture.authLoginPassword.users.routine.email`, biarkan Password kosong, selesaikan reCAPTCHA, lalu klik "Log in"
39. Verifikasi caption "Email must not be empty" muncul
40. Isi Email dengan `Fixture.authLoginPassword.data.invalidEmailFormat` dan Password dengan satu nilai, lalu klik "Log in"
41. Verifikasi caption "Email format is incorrect" muncul
42. Isi Email dengan `Fixture.authLoginPassword.data.unregisteredEmail` dan Password dengan satu nilai, lalu klik "Log in"
43. Verifikasi caption "Email is not registered yet" muncul
44. Kembali ke Activity Log > Session lalu verifikasi tidak ada entri baru untuk ketiga attempt tersebut
45. Buka User Log user tersebut lalu verifikasi tidak ada entri baru untuk ketiga attempt tersebut
46. Verifikasi jumlah baris pada kedua surface sama dengan pembanding, sehingga attempt tanpa subjek user tidak pernah dicatat

## Notes

- Spec ini memverifikasi pencatatan lewat UI Global Settings, karena Auth hanya menulis event dan dua surface tersebut yang menampilkannya. Tidak ada query database yang dipakai.
- Spec ini sengaja melakukan login sukses berulang dengan user yang sama pada langkah 1, 10, 23, dan 30. Tiap login dipakai untuk satu hal yang berbeda, yaitu screening kolom, kesesuaian entri, IP Address, dan format Device / Browser. Jumlah attempt dibatasi empat kali agar spec ini tetap mudah ditelusuri saat membaca pembanding jumlah baris.
- Attempt gagal yang teridentifikasi sudah dicatat di TC-AUTH-LP-E2E-004 bersama Note "Incorrect password". Spec ini tidak mengulangnya supaya tidak ada dua spec yang membuktikan hal sama.
- Attempt dengan password salah tercatat, sedangkan attempt dengan email kosong, format salah, dan email belum terdaftar tidak pernah tercatat. Perbedaan itu justru yang diuji pada langkah 37 sampai 46.
- Nilai IP Address yang terisi berasal dari leftmost trusted `X-Forwarded-For` bila request lewat proxy terdaftar, atau dari direct socket bila tidak ada proxy. Keduanya diterima dan tidak dibedakan di spec ini karena perbedaan itu milik konfigurasi environment, bukan perilaku UI.
- Device / Browser yang tidak terparse dari User-Agent harus dirender `—`, bukan string kosong. Environment run ini memakai User-Agent yang terparse, sehingga kasus render `—` tidak diuji di sini dan dicatat sebagai kebutuhan environment tambahan di bawah.
- Kolom yang dirujuk pada langkah 6 sampai 9 mengikuti PRD §8.1 dan §8.2. Aturan Event Stream meletakkan kolom Date pada posisi pertama.
- Spec ini tidak membuat user dan tidak mengubah data. Yang bertambah hanya entri log, dan itu efek samping dari login itu sendiri. Penghapusan entri log bukan tanggung jawab modul ini.
- Sesi admin untuk membuka kedua surface dibuka lewat hook, bukan ditulis sebagai langkah login di dalam spec. Ini supaya langkah di spec ini hanya berisi aksi yang memang milik modul ini.