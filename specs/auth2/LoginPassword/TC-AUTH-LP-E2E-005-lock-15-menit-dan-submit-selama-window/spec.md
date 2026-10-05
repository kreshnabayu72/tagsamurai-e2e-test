---
id: TC-AUTH-LP-E2E-005-lock-15-menit-dan-submit-selama-window
title: Lock 15 menit dan penolakan submit selama window lock aktif
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-33
  - TC-AUTH-LP-34
  - TC-AUTH-LP-35
  - TC-AUTH-LP-92
coverage:
  web: automated
---

# Lock 15 menit dan penolakan submit selama window lock aktif

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan dua user uji dengan `failed_count = 0` dan `lock_level = none` untuk hari berjalan, dibuat lewat API Global Settings > User dan direstore ke kondisi awal di `afterEach`. Keduanya bukan Default User.
- `Fixture.authLoginPassword.users.lockTarget` adalah user yang akan dikunci pada bagian single-tab, dengan email dan password diketahui.
- `Fixture.authLoginPassword.users.multiTabTarget` adalah user kedua untuk bagian multi-tab, dengan `failed_count = 0` dan `lock_level = none` terverifikasi dari Global Settings > User > User Log.
- `Fixture.authLoginPassword.users.lockTarget.wrongPasswords` berisi tiga password salah yang berbeda, dipakai berurutan pada bagian multi-tab.
- Password asli kedua user tersedia lewat `Spectra.env.AUTH_PASSWORD` dan `Spectra.env.AUTH_PASSWORD_2`, tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.captions.lock15m` adalah caption lock 15 menit dengan placeholder `{time}` yang diganti nilai absolut dari server saat runtime.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon, termasuk `Locked 15 minutes`.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook `beforeEach` menyediakan pemicu waktu yang hanya perlu dipanggil, sehingga window 15 menit bisa dilewati tanpa menunggu 15 menit sungguhan.
- Emulator browser dan jendela browser yang terpisah tersedia untuk bagian multi-tab.
- Sesi admin untuk membuka User Log dibuka pada bagian single-tab dan ditutup kembali di akhir spec, sehingga spec ini dapat dijalankan sendiri.

## Test Steps

### Percobaan ketiga memicu lock 15 menit

1. Buka `/login`
2. Login sebagai user dengan role Total Control pada entity Client, lalu buka `Fixture.authLoginPassword.log.userLogPath` milik `Fixture.authLoginPassword.users.lockTarget`
3. Verifikasi jumlah entri sebelum Lock in adalah 2, sehingga ada pembanding yang jelas untuk ketiga attempt
4. Logout dari akun admin sehingga session kosong, lalu buka kembali `/login`
5. Isi Email dengan `Fixture.authLoginPassword.users.lockTarget.email` dan Password dengan `Fixture.authLoginPassword.users.lockTarget.wrongPasswords[0]`
6. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
7. Verifikasi caption "Incorrect email or password" muncul, sehingga ini masih percobaan pertama dan akun belum terkunci
8. Isi kembali Password dengan `Fixture.authLoginPassword.users.lockTarget.wrongPasswords[1]` lalu klik "Log in"
9. Verifikasi caption "Incorrect email or password" muncul lagi
10. Isi kembali Password dengan `Fixture.authLoginPassword.users.lockTarget.wrongPasswords[2]` lalu klik "Log in"
11. Verifikasi banner di atas tombol menampilkan caption lock 15 menit dengan waktu absolut yang terisi
12. Verifikasi caption tidak berubah dan tidak ada countdown yang berjalan
13. Verifikasi field Email tetap enabled
14. Verifikasi field Password tetap enabled
15. Verifikasi tombol "Log in" tetap enabled, sehingga lock tidak menonaktifkan form
16. Verifikasi caption "Please reset your password." tidak muncul pada tahap ini
17. Kembali ke sesi admin pada tab terpisah dan buka `Fixture.authLoginPassword.log.userLogPath` milik `Fixture.authLoginPassword.users.lockTarget`
18. Verifikasi jumlah entri bertambah satu dari pembanding, sehingga percobaan ketiga menghasilkan tepat satu entri baru
19. Verifikasi entri baru tersebut ber-Status "Failed" dengan Note "Locked 15 minutes", sehingga catatan lock memakai Note kanon tersendiri dan bukan `Incorrect password`
20. Verifikasi `lock_level` bernilai "15m" dan `lock_until` terisi waktu absolut yang sama dengan `{time}` pada banner

### Submit selama window lock 15 menit aktif

21. Catat jumlah entri di `Fixture.authLoginPassword.log.userLogPath` milik `Fixture.authLoginPassword.users.lockTarget` sebagai pembanding
22. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
23. Verifikasi banner lock 15 menit yang sama tetap tampil
24. Verifikasi kredensial benar tidak dievaluasi, sehingga password benar tetap ditolak
25. Verifikasi tidak ada navigasi ke Portal maupun ke layar mana pun
26. Isi Password dengan `Fixture.authLoginPassword.users.lockTarget.wrongPasswords[0]` lalu klik "Log in"
27. Verifikasi banner lock 15 menit yang sama tetap tampil dan kredensial tidak dievaluasi
28. Verifikasi jumlah entri di User Log tetap sama dengan pembanding, sehingga submit selama lock tidak pernah dicatat
29. Verifikasi lock state tidak berubah dan tidak ada counter baru yang bertambah

### Lock 15 menit yang sudah lewat

30. Biarkan window 15 menit berlalu lewat pemicu waktu yang disediakan hook `beforeEach`
31. Verifikasi jumlah entri di User Log tetap sama dengan pembanding, sehingga pergantian waktu tidak menulis entri baru
32. Verifikasi `lock_level` tidak berubah menjadi "1h" maupun "requires_reset", sehingga lock yang sudah lewat hanya membuka blokir tanpa langsung menaikkan tahap
33. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
34. Verifikasi banner lock 15 menit tidak lagi tampil
35. Verifikasi browser berpindah ke Portal — Product Hub, sehingga lock tidak lagi memblokir login
36. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success", sehingga submit setelah window lewat dicatat sebagai login berhasil biasa
37. Logout dari Portal sehingga session kosong

### Akumulasi counter lintas tab

38. Verifikasi `failed_count` milik `Fixture.authLoginPassword.users.multiTabTarget` bernilai 0 dan `lock_level` bernilai "none" dari `Fixture.authLoginPassword.log.userLogPath`
39. Buka dua tab browser lain pada halaman `/login` dengan akun yang sama
40. Pada Tab A, isi Email dengan `Fixture.authLoginPassword.users.multiTabTarget.email` dan Password dengan `Fixture.authLoginPassword.users.multiTabTarget.wrongPasswords[0]`, selesaikan reCAPTCHA, lalu klik "Log in"
41. Verifikasi caption "Incorrect email or password" muncul pada Tab A
42. Pada Tab B, isi Password dengan `Fixture.authLoginPassword.users.multiTabTarget.wrongPasswords[1]` lalu klik "Log in"
43. Verifikasi caption "Incorrect email or password" muncul pada Tab B
44. Pada Tab C, isi Password dengan `Fixture.authLoginPassword.users.multiTabTarget.wrongPasswords[2]` lalu klik "Log in"
45. Verifikasi banner lock 15 menit tampil pada Tab C
46. Verifikasi field Email, field Password, dan tombol "Log in" tetap enabled pada Tab C
47. Verifikasi jumlah entri di User Log bertambah tiga untuk ketiga attempt lintas tab
48. Verifikasi entri paling baru ber-Status "Failed" dengan Note "Locked 15 minutes", sehingga Note kanon yang sama dipakai untuk lock lintas tab
49. Kembali ke Tab A yang masih terbuka, ganti Email dengan `Fixture.authLoginPassword.users.multiTabTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`, lalu klik "Log in"
50. Verifikasi banner lock 15 menit yang sama langsung menolak submit tanpa evaluasi kredensial
51. Verifikasi kredensial benar pada Tab A tetap ditolak
52. Verifikasi jumlah entri di User Log tidak bertambah lagi, sehingga submit di tab yang lebih lama tidak dicatat
53. Verifikasi lock state tetap sama dengan yang terbentuk pada langkah 45

## Notes

- Spec ini menggabungkan lock 15 menit pada percobaan ketiga, submit selama window aktif, lock yang sudah lewat, dan akumulasi counter lintas tab. Keempatnya membentuk satu rangkaian berurutan yang menghasilkan state lock yang sama, jadi digabung dalam satu spec sesuai e2e-conventions.md bagian 3 prinsip 1.
- Bagian single-tab dan bagian multi-tab memakai user berbeda. Kalau user yang sama dipakai, lock yang terbentuk di bagian single-tab akan membuat bagian multi-tab tidak bisa diuji. Ini pemisahan kondisi data, bukan pengulangan.
- Simulasi pergantian waktu lewat hook, bukan menunggu 15 menit sungguhan. Kebutuhan kemampuan teknis ini dicatat di Prerequisites sebagai sumber resmi bagi tim FE.
- Counter `failed_count` diverifikasi dari User Log, bukan dari banner. Banner hanya menampilkan tahap lock dan waktu absolut, bukan counter.
- Eskalasi ke lock 1 jam ada di TC-AUTH-LP-E2E-006, bukan di sini, karena butuh window 15 menit sudah lewat dan tiga attempt tambahan, yaitu kondisi data yang berbeda total.
- Catatan log `Locked 15 minutes` sengaja diuji di bagian single-tab sekaligus bagian multi-tab. Dua bagian itu memakai user berbeda, jadi mengulang assert Note di bagian kedua bukan pengulangan inkonstisten, melainkan memastikan Note yang sama terbentuk dari sumber percobaan yang berbeda.
- Submit selama window lock tidak menghasilkan entri apa pun, baik di User Log maupun di Activity Log. Karena itu pembanding diambil tepat sebelum submit dan langsung dibaca sesudahnya, bukan di akhir spec.
- Verifikasi `lock_level` dan `lock_until` diambil dari User Log, bukan dari banner. Banner hanya menampilkan caption dan waktu absolut yang sudah dirender ke `{time}`.
- Pembersihan lock state dilakukan di hook `afterEach` supaya tidak bergantung pada spec lain dan tetap jalan kalau spec ini dijalankan sendiri. Yang direstore hanya lock state user uji; tidak ada aksi menghapus data di spec ini.