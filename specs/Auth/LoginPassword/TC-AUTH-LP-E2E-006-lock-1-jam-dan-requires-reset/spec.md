---
id: TC-AUTH-LP-E2E-006-lock-1-jam-dan-requires-reset
title: Lock 1 jam setelah window 15 menit lewat dan status requires reset
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-36
  - TC-AUTH-LP-37
  - TC-AUTH-LP-38
coverage:
  web: automated
---

# Lock 1 jam setelah window 15 menit lewat dan status requires reset

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan user uji dengan `lock_level = 15m` dan `lock_until` yang masih aktif, `failed_count = 3`, dan `consecutive_1h_days = 0`, dibuat lewat API Global Settings > User. User ini bukan Default User.
- Hook `before` juga menyediakan user kedua dengan `lock_level = 1h` dan `lock_until` yang masih aktif, `failed_count = 3`.
- Hook `before` menyediakan user ketiga dengan `lock_level = requires_reset`, tanpa `lock_until`, dan `failed_count = 3`.
- Hook `beforeEach` menyediakan pemicu waktu untuk melewati window lock aktif tanpa menunggu sungguhan. Kebutuhan ini dicatat di sini sebagai sumber resmi bagi tim FE.
- `Fixture.authLoginPassword.users.lock15mTarget` berisi email user pada tahap 15 menit aktif.
- `Fixture.authLoginPassword.users.lock1hTarget` berisi email user pada tahap 1 jam aktif.
- `Fixture.authLoginPassword.users.requiresResetTarget` berisi email user pada tahap requires reset.
- `Fixture.authLoginPassword.users.wrongPasswords` berisi tujuh password salah yang berbeda, semuanya ditolak untuk ketiga user tersebut. Indeks `[0]` sampai `[3]` dipakai oleh user tahap 15 menit karena butuh tiga attempt setelah window lewat, dan indeks `[4]` sampai `[6]` dipakai oleh user tahap 1 jam karena butuh tiga attempt lagi setelah window 1 jam lewat. Password asli ketiga user tersedia lewat `Spectra.env.AUTH_PASSWORD`, `Spectra.env.AUTH_PASSWORD_2`, dan `Spectra.env.AUTH_PASSWORD_3`.
- `Fixture.authLoginPassword.captions.lock1h` berisi caption lock 1 jam dengan placeholder `{time}` yang diganti nilai absolut dari server saat runtime.
- `Fixture.authLoginPassword.captions.requiresReset` berisi caption status requires reset.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon, termasuk `Locked 1 hour` dan `Locked requires reset`.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Lock state ketiga user diverifikasi dari `Fixture.authLoginPassword.log.userLogPath`, bukan dari asumsi jumlah submit.
- Sesi admin untuk membuka User Log dibuka pada spec ini dan ditutup kembali di akhir spec, sehingga spec ini dapat dijalankan sendiri.

## Test Steps

### Lock 1 jam terbentuk setelah window 15 menit lewat

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.lock15mTarget.email` dan Password dengan `Fixture.authLoginPassword.users.wrongPasswords[0]`
3. Verifikasi banner lock 15 menit tampil, sehingga submit pertama masuk tahap yang sedang terkunci dan tidak dievaluasi
4. Biarkan window 15 menit berlalu lewat pemicu waktu
5. Verifikasi jumlah entri di User Log tidak bertambah akibat langkah 2 sampai 4
6. Isi Password dengan `Fixture.authLoginPassword.users.wrongPasswords[1]` lalu klik "Log in"
7. Verifikasi caption "Incorrect email or password" muncul
8. Isi Password dengan `Fixture.authLoginPassword.users.wrongPasswords[2]` lalu klik "Log in"
9. Verifikasi caption "Incorrect email or password" muncul
10. Isi Password dengan `Fixture.authLoginPassword.users.wrongPasswords[3]` lalu klik "Log in"
11. Verifikasi banner di atas tombol menampilkan caption lock 1 jam dengan waktu absolut yang terisi
12. Verifikasi caption tersebut berbeda dari caption lock 15 menit
13. Verifikasi field Email, field Password, dan tombol "Log in" tetap enabled
14. Verifikasi caption "Please reset your password." tidak muncul pada tahap ini
15. Verifikasi jumlah entri di User Log bertambah satu dari kondisi awal, sehingga percobaan keempat menghasilkan tepat satu entri baru
16. Verifikasi entri baru tersebut ber-Status "Failed" dengan Note "Locked 1 hour", sehingga catatan lock memakai Note kanon tersendiri dan bukan `Locked 15 minutes`
17. Verifikasi `lock_level` bernilai "1h" dan `lock_until` terisi waktu absolut yang sama dengan `{time}` pada banner
18. Verifikasi `consecutive_1h_days` bernilai 1, sehingga lock 1 jam ini tercatat sebagai hari pertama untuk eskalasi 7 hari

### Submit selama window lock 1 jam aktif

19. Catat jumlah entri di User Log sebagai pembanding
20. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
21. Verifikasi banner lock 1 jam yang sama tetap tampil dan kredensial tidak dievaluasi
22. Verifikasi tidak ada navigasi ke halaman mana pun
23. Isi Password dengan `Fixture.authLoginPassword.users.wrongPasswords[0]` lalu klik "Log in"
24. Verifikasi banner lock 1 jam yang sama tetap tampil dan kredensial tidak dievaluasi
25. Verifikasi jumlah entri di User Log tetap sama dengan pembanding, sehingga submit selama lock 1 jam tidak pernah dicatat
26. Verifikasi `lock_level` dan `lock_until` tidak berubah

### Status requires reset

27. Logout bila ada sesi, lalu buka `/login` dan biarkan window 1 jam berlalu lewat pemicu waktu
28. Verifikasi jumlah entri di User Log tetap sama, sehingga window 1 jam yang lewat sendiri tidak menulis entri baru
29. Isi Email dengan `Fixture.authLoginPassword.users.lock1hTarget.email` dan Password dengan `Fixture.authLoginPassword.users.wrongPasswords[4]`
30. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
31. Verifikasi caption "Incorrect email or password" muncul
32. Isi Password dengan `Fixture.authLoginPassword.users.wrongPasswords[5]` lalu klik "Log in"
33. Verifikasi caption "Incorrect email or password" muncul
34. Isi Password dengan `Fixture.authLoginPassword.users.wrongPasswords[6]` lalu klik "Log in"
35. Verifikasi banner menampilkan caption requires reset
36. Verifikasi caption tersebut bukan caption lock 15 menit maupun lock 1 jam
37. Verifikasi banner menyediakan tautan langsung menuju alur Reset Password
38. Verifikasi jumlah entri di User Log bertambah tiga dari pembanding sebelumnya
39. Verifikasi dua entri pertama ber-Status "Failed" dengan Note "Incorrect password", sehingga attempt biasa tetap memakai Note password salah
40. Verifikasi entri terakhir ber-Status "Failed" dengan Note "Locked requires reset", sehingga tahap ketiga memakai Note kanon terminal
41. Verifikasi `lock_level` bernilai "requires_reset" dan `lock_until` kosong, sehingga tahap ini tidak punya window waktu

### Submit pada status requires reset

42. Catat jumlah entri di User Log sebagai pembanding
43. Isi Email dengan `Fixture.authLoginPassword.users.requiresResetTarget.email` dan Password dengan password asli user tersebut lewat env yang tersedia, lalu klik "Log in"
44. Verifikasi caption requires reset tetap tampil dan kredensial tidak dievaluasi
45. Verifikasi jumlah entri di User Log tetap sama dengan pembanding
46. Verifikasi tidak ada navigasi ke Portal

## Notes

- Spec ini memakai tiga user berbeda karena tiap tahap lock butuh kondisi awal yang berbeda. User pertama bermula pada lock 15 menit aktif, user kedua pada lock 1 jam aktif, dan user ketiga sudah pada status requires reset. Kalau satu user dipakai, tahap berikutnya tidak akan tercapai karena counter globalnya sudah terpakai.
- Tujuh password salah dibagi dua: `[0]` sampai `[3]` untuk user tahap 15 menit, `[4]` sampai `[6]` untuk user tahap 1 jam. Jumlah ketujuh itu muncul karena kedua tahap memang butuh tiga attempt masing-masing di user yang berbeda, bukan karena satu user butuh tujuh attempt.
- Note kanon dibedakan per tahap lock, dan itu yang diuji di sini: `Locked 15 minutes` di spec 005, `Locked 1 hour` di spec ini, `Locked requires reset` di spec ini juga. Dua attempt biasa di spec ini tetap memakai `Incorrect password`, jadi perbedaan antara attempt biasa dan attempt yang memicu lock ikut terverifikasi.
- Penambahan counter tidak terjadi pada tahap lock maupun saat submit selama lock aktif. Karena itu jumlah entri di User Log adalah pembanding yang benar untuk membuktikan bahwa submit selama window aktif tidak dievaluasi dan tidak dicatat.
- Lock 15 menit sebagai subjek uji ada di TC-AUTH-LP-E2E-005. Di sini tahap itu hanya dipakai sebagai kondisi awal, bukan sebagai subjek uji.
- Status permanent dan eskalasi 7 hari ada di TC-AUTH-LP-E2E-007, karena butuh kondisi awal berupa `consecutive_1h_days` bernilai 7.
- Caption pada banner memakai nilai absolut dari server untuk `{time}` dan tidak ada countdown. Nilai itu diambil dari fixture caption, tidak diketik ulang.
- Pergantian waktu disimulasikan lewat pemicu yang disediakan hook `beforeEach`, bukan menunggu 15 menit atau 1 jam sungguhan. Kebutuhan kemampuan teknis ini dicatat di Prerequisites sebagai sumber resmi bagi tim FE.
- Pembersihan lock state ketiga user dilakukan di hook `afterEach` supaya tidak bergantung pada spec lain dan tetap jalan ketika spec ini dijalankan sendiri.