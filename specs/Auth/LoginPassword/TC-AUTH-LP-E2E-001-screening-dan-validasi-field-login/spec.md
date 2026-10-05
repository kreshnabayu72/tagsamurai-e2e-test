---
id: TC-AUTH-LP-E2E-001-screening-dan-validasi-field-login
title: Screening halaman Login with Password, validasi field Email dan Password, serta catatan log tiap kondisi
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-1
  - TC-AUTH-LP-4
  - TC-AUTH-LP-5
  - TC-AUTH-LP-6
  - TC-AUTH-LP-7
  - TC-AUTH-LP-9
  - TC-AUTH-LP-11
  - TC-AUTH-LP-12
  - TC-AUTH-LP-13
  - TC-AUTH-LP-93
coverage:
  web: automated
---

# Screening halaman Login with Password, validasi field Email dan Password, serta catatan log tiap kondisi

## Prerequisites

- Belum login dan session kosong. Halaman `/login` (Login with Password) terbuka di browser.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE, bukan environment yang dipakai tester manual bersamaan.
- Hook `before` menyiapkan satu user berstatus Activated dan Active di Global Settings > User dengan `failed_count = 0` dan `lock_level = none`, lalu mengembalikannya ke kondisi awal di `afterEach`. User ini bukan Default User maupun bukan akun admin Total Control.
- `Spectra.env.AUTH_PASSWORD` berisi password asli user tersebut. Nilai ini memakai pola sederhana tanpa spasi di awal maupun akhir, tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.users.activated.email` berisi email user terdaftar tersebut.
- `Fixture.authLoginPassword.users.activated.wrongPassword` berisi satu password salah yang tetap ditolak untuk user tersebut.
- `Fixture.authLoginPassword.users.activated.passwordWithSpaces` berisi password asli user tersebut dengan satu spasi di awal dan satu spasi di akhir.
- `Fixture.authLoginPassword.data.unregisteredEmail` berisi email berformat valid yang memang belum terdaftar di Global Settings > User.
- `Fixture.authLoginPassword.data.invalidEmailFormat` berisi string yang bukan email valid.
- `Fixture.authLoginPassword.data.tooLongEmail` berisi string 121 karakter.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon, termasuk `Empty password` dan `Incorrect password`.
- `Fixture.authLoginPassword.log.activityLogPath` berisi rute halaman Global Settings > Activity Log > Session.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Caption error yang dirujuk diambil dari `Fixture.authLoginPassword.captions`, tidak diketik ulang di spec ini.
- Sesi admin untuk membuka kedua surface log dibuka pada langkah spec ini dan ditutup di akhir spec, sehingga spec ini dapat dijalankan sendiri.
- Verifikasi jumlah entri selalu membandingkan jumlah baris pada surface yang sama sebelum dan sesudah submit, bukan mengandalkan caption.

## Test Steps

### Screening halaman login

1. Buka halaman Login with Password di browser
2. Verifikasi judul halaman adalah "Login with Password"
3. Verifikasi subtitle di bawah judul adalah "Sign in and start managing your asset"
4. Verifikasi field Email tampil dengan placeholder "Enter your email"
5. Verifikasi field Password tampil dengan placeholder "Enter your password"
6. Verifikasi teks pada field Password tersembunyi (masked) secara default
7. Verifikasi widget reCAPTCHA tampil di halaman
8. Verifikasi tidak ada checkbox Agreement di halaman ini, dalam keadaan apa pun
9. Verifikasi tombol "Log in" tampil dalam keadaan enabled
10. Verifikasi link "Log in with OTP" dan link "Forgot your password? Reset here" tampil
11. Verifikasi tidak ada tombol "Remember me" di halaman

### Email kosong tidak pernah dicatat

12. Biarkan field Email kosong, isi Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword`, selesaikan reCAPTCHA, lalu klik "Log in"
13. Verifikasi caption inline di bawah field Email adalah "Email must not be empty"
14. Verifikasi caption tersebut tidak menyebabkan navigasi ke halaman mana pun
15. Verifikasi form tetap aktif, kedua field tetap dapat diisi ulang, dan tombol "Log in" tetap enabled
16. Login sebagai user dengan role Total Control pada entity Client
17. Buka Activity Log > Session lalu verifikasi tidak ada entri baru dari submit pada langkah 12
18. Buka User Detail milik `Fixture.authLoginPassword.users.activated` lalu buka tab User Log
19. Verifikasi tidak ada entri baru pada kedua surface, sehingga submit tanpa email tidak punya subjek user

### Format email salah tidak pernah dicatat

20. Logout dari akun admin sehingga session kosong, lalu buka `/login`
21. Isi Email dengan `Fixture.authLoginPassword.data.invalidEmailFormat` dan Password dengan satu nilai, selesaikan reCAPTCHA, lalu klik "Log in"
22. Verifikasi caption inline di bawah field Email adalah "Email format is incorrect"
23. Verifikasi tidak ada navigasi ke halaman mana pun
24. Verifikasi jumlah entri tidak bertambah pada kedua surface, sehingga format email salah tidak punya subjek user

### Email belum terdaftar memakai caption khusus dan tetap tidak dicatat

25. Ganti Email dengan `Fixture.authLoginPassword.data.unregisteredEmail` yang berformat valid, selesaikan reCAPTCHA, lalu klik "Log in"
26. Verifikasi caption inline di bawah field Email adalah "Email is not registered yet"
27. Verifikasi caption tersebut dibedakan dari caption password salah, sehingga keberadaan email terkonfirmasi secara eksplisit
28. Verifikasi jumlah entri tidak bertambah pada kedua surface, sehingga email yang belum terdaftar tidak punya subjek user

### Email melebihi 120 karakter ditolak saat mengetik

29. Ganti Email dengan `Fixture.authLoginPassword.data.tooLongEmail`, lalu ketik karakter demi karakter tanpa menekan tombol "Log in"
30. Verifikasi caption "Max. 120 characters" muncul saat mengetik, sebelum tombol "Log in" diklik
31. Verifikasi klik "Log in" diblokir dan caption "Max. 120 characters" tetap tampil
32. Verifikasi tidak ada request login yang terkirim, sehingga penolakan ini terjadi di sisi klien

### Password kosong dicatat dengan Note Empty password

33. Ganti Email kembali ke `Fixture.authLoginPassword.users.activated.email` dan biarkan field Password kosong
34. Verifikasi `failed_count` user tersebut bernilai 0 dari Global Settings > User > User Log sebagai pembanding
35. Selesaikan reCAPTCHA lalu klik "Log in"
36. Verifikasi caption inline di bawah field Password adalah "Password must not be empty"
37. Verifikasi field Password tetap kosong dan field Email tetap terisi
38. Verifikasi tidak ada navigasi ke Portal maupun ke layar mana pun
39. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Failed" dan Note "Empty password", sehingga password kosong punya subjek user yang sudah ter-resolve dari email
40. Verifikasi jumlah entri di Activity Log > Session juga bertambah satu dengan isi yang sama, sehingga satu attempt hanya menghasilkan satu entri per surface
41. Verifikasi `failed_count` bertambah satu, sehingga attempt ini ikut dihitung sebagai percobaan login

### Password salah membocorkan informasi dan dikosongkan otomatis

42. Isi Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword`, selesaikan reCAPTCHA, lalu klik "Log in"
43. Verifikasi caption inline di bawah field Password adalah "Incorrect email or password"
44. Verifikasi caption tersebut tidak menyebutkan bahwa password salah secara eksplisit, sehingga tidak membocorkan informasi lebih dari yang sudah diketahui
45. Verifikasi field Password otomatis dikosongkan setelah login gagal, sementara isi field Email tetap bertahan
46. Verifikasi form tetap aktif, field Email, field Password, dan tombol "Log in" tetap enabled

### Password dengan spasi di awal dan akhir tidak di-trim

47. Catat `failed_count` user tersebut dari Global Settings > User > User Log sebagai pembanding
48. Isi Password dengan `Fixture.authLoginPassword.users.activated.passwordWithSpaces` lalu selesaikan reCAPTCHA dan klik "Log in"
49. Verifikasi login ditolak dengan caption "Incorrect email or password"
50. Verifikasi caption tersebut muncul karena spasi diperlakukan sebagai bagian dari password, bukan karena spasi di-trim sebelum verifikasi
51. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Failed" dan Note "Incorrect password"
52. Verifikasi jumlah entri di Activity Log > Session juga bertambah satu dengan isi yang sama
53. Verifikasi `failed_count` bertambah satu dari nilai pembanding

### Tampilkan dan sembunyikan password

54. Isi field Password dengan satu nilai, lalu klik ikon mata
55. Verifikasi teks password terlihat dan tooltip pada ikon adalah "Show password"
56. Klik lagi ikon mata
57. Verifikasi teks password kembali tersembunyi dan tooltip pada ikon adalah "Hide password"
58. Verifikasi nilai pada field Password tidak hilang saat ikon mata diklik

## Notes

- Spec ini menggabungkan seluruh TC yang bentuknya sama-sama "satu submit, satu caption, satu catatan log", yaitu kelima email kosong, format salah, email belum terdaftar, password kosong, dan password dengan spasi. Kelima kasus itu memang berbeda perlakuan: tiga yang pertama tidak pernah dicatat, sedangkan dua yang terakhir dicatat. Perbedaan itu justru yang membuat mereka layak digabung di satu spec.
- Password kosong **wajib** memakai email yang valid dan terdaftar. Kalau email ikut dikosongkan, validasi email yang lebih dulu menangkap dan tidak ada request yang terkirim, sehingga Note `Empty password` tidak akan pernah muncul.
- Email kosong, format salah, dan email belum terdaftar tidak punya subjek user, jadi tidak boleh menghasilkan entri log. Password kosong dan password dengan spasi punya subjek user yang sudah ter-resolve, jadi keduanya tercatat.
- Verifikasi "tidak ada entri baru" dilakukan pada kedua surface, bukan hanya satu. Kalau hanya satu surface yang dicek, perbedaan antara dua surface bisa lolos.
- `failed_count` dibaca dari User Log, bukan dari banner. Banner hanya menampilkan tahap lock, bukan counter.
- Percobaan dengan kredensial benar sengaja tidak ada di spec ini supaya efek samping login tidak ikut teruji. Login berhasil ada di TC-AUTH-LP-E2E-002. Sisa lock yang muncul dari spec ini karena counter bertambah ada di TC-AUTH-LP-E2E-004.
- Pengosongan field Password saat login gagal berasal dari TC-AUTH-LP-93 dan diuji pada langkah 42 sampai 46.
- Password user uji tidak boleh ditulis di spec maupun fixture. Nilai asli diambil dari `Spectra.env.AUTH_PASSWORD`, dan varian ber-spasi diambil dari fixture, sesuai e2e-conventions.md bagian 5.
- Error caption dan enum Note diambil dari fixture sesuai aturan e2e-conventions.md bagian 9, supaya tidak diketik ulang di banyak spec.
- Pembersihan `failed_count` dilakukan di hook `afterEach`, sehingga spec ini tidak meninggalkan counter yang memengaruhi spec lain.