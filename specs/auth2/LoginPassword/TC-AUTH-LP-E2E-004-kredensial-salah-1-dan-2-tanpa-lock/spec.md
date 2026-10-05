---
id: TC-AUTH-LP-E2E-004-kredensial-salah-1-dan-2-tanpa-lock
title: Kredensial salah pada percobaan pertama dan kedua tanpa memicu lock
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-31
  - TC-AUTH-LP-32
  - TC-AUTH-LP-56
  - TC-AUTH-LP-64
coverage:
  web: automated
---

# Kredensial salah pada percobaan pertama dan kedua tanpa memicu lock

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan user uji dengan `failed_count = 0` dan `lock_level = none` untuk hari berjalan, dibuat lewat API Global Settings > User dan direstore ke kondisi awal di `afterEach`. User ini bukan Default User.
- `Fixture.authLoginPassword.users.activated.email` adalah email user uji tersebut.
- `Fixture.authLoginPassword.users.activated.wrongPassword` adalah satu password salah yang tetap ditolak untuk user tersebut.
- Password asli user uji tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon untuk keperluan verifikasi log.
- `Fixture.authLoginPassword.log.activityLogPath` berisi rute halaman Global Settings > Activity Log > Session.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Lock state user uji diverifikasi ulang dari Global Settings > User > User Log, bukan dari asumsi jumlah submit.
- Sesi admin untuk membuka kedua surface dibuka pada langkah spec ini dan ditutup di akhir spec, sehingga spec ini dapat dijalankan sendiri.

## Test Steps

### Percobaan salah yang pertama

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.activated.email` dan Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
4. Verifikasi caption inline di bawah field Password adalah "Incorrect email or password"
5. Verifikasi caption tersebut sama pada percobaan berikutnya, sehingga tidak ada pembedaan jumlah percobaan
6. Verifikasi caption tidak menyebutkan bahwa password salah secara eksplisit
7. Verifikasi tidak ada banner lock yang muncul
8. Verifikasi form tetap aktif, field Email, field Password, dan tombol "Log in" tetap enabled

### Percobaan salah yang kedua

9. Isi kembali field Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword` lalu klik "Log in"
10. Verifikasi caption inline di bawah field Password adalah "Incorrect email or password"
11. Verifikasi tidak ada banner lock yang muncul setelah percobaan kedua
12. Verifikasi form tetap aktif dan tombol "Log in" tetap enabled

### Pencatatan di kedua surface

13. Login sebagai user dengan role Total Control pada entity Client
14. Buka Activity Log > Session lalu verifikasi dua entri baru muncul untuk user uji
15. Verifikasi kedua entri memiliki Status "Failed"
16. Verifikasi kedua entri memiliki Note "Incorrect password"
17. Verifikasi kedua entri memiliki kolom IP Address dan Device / Browser yang terisi
18. Buka User Detail milik user uji lalu buka tab User Log
19. Verifikasi dua entri baru muncul dengan isi yang sama pada kedua surface

## Notes

- Percobaan pertama dan kedua memakai user yang sama secara berurutan karena keduanya beracuan pada state lock yang sama, yaitu masih belum terkunci. Ini satu topik aksi, sehingga digabung di satu spec sesuai e2e-conventions.md bagian 3 prinsip 1.
- Verifikasi counter `failed_count` bertambah tepat satu kali per attempt dilakukan dengan membaca User Log, bukan dengan memeriksa banner. Banner hanya menampilkan lock, bukan counter.
- Gagal kredensial adalah kondisi yang tercatat, berbeda dari email kosong, format salah, dan belum terdaftar yang tidak pernah dicatat. Kasus tidak-teridentifikasi tersebut ada di TC-AUTH-LP-E2E-003.
- Percobaan ketiga yang memicu lock 15 menit sengaja tidak ada di spec ini. Topik aksi berbeda dengan kondisi data yang berubah drastis, jadi dipisah ke TC-AUTH-LP-E2E-005 sesuai e2e-conventions.md bagian 3 prinsip 1.
- Spec ini tidak membuat user permanen. Hook menyediakan user uji dan mengembalikan lock state-nya ke awal setelah spec selesai, supaya tidak bergantung pada spec lain.
- Pembukaan sesi admin ditulis sebagai langkah di dalam spec ini, bukan diserahkan ke hook suite, supaya spec ini tidak bergantung pada spec lain maupun urutan run.