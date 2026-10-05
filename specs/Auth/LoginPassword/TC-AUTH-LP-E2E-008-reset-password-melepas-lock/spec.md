---
id: TC-AUTH-LP-E2E-008-reset-password-melepas-lock
title: Reset Password yang berhasil melepas seluruh lock dan counter
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-44
  - TC-AUTH-LP-87
coverage:
  web: automated
---

# Reset Password yang berhasil melepas seluruh lock dan counter

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang menyiapkan mailbox uji.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan empat user uji dengan kondisi awal berikut, dibuat lewat API Global Settings > User dan direstore di `afterEach`:
  - `Fixture.authLoginPassword.users.lock15mBeforeReset` dengan `lock_level = 15m`, `lock_until` masih aktif, `failed_count = 3`, `consecutive_1h_days = 0`
  - `Fixture.authLoginPassword.users.lock1hBeforeReset` dengan `lock_level = 1h`, `lock_until` masih aktif, `failed_count = 3`, `consecutive_1h_days = 1`
  - `Fixture.authLoginPassword.users.requiresResetBeforeReset` dengan `lock_level = requires_reset`, `failed_count = 3`
  - `Fixture.authLoginPassword.users.permanentBeforeReset` dengan `lock_level = permanent`, `failed_count = 3`
- Hook `before` juga menyiapkan satu user dengan `lock_level = none`, `failed_count = 0`, dan `consecutive_1h_days = 3`, dipakai untuk membuktikan counter consecutive ikut ter-reset.
- Mailbox uji yang sudah ter-seed dengan domain milik environment otomasi, bukan domain riil. Email reset password tiap user dan tautan reset-nya diketahui oleh hook sebelum spec berjalan.
- Password baru tiap user dibuat unik per run dan tersedia lewat `Spectra.env.AUTH_NEW_PASSWORD`, tidak ditulis di spec maupun fixture.
- Alur Reset Password milik modul `auth/reset-password`. Yang diuji di sini hanya handoff dari modul itu ke state lock, bukan langkah internal Reset Password itu sendiri.
- Lock state diverifikasi dari Global Settings > User > User Log, bukan dari asumsi jumlah submit.

## Test Steps

### Melepas lock 15 menit

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.lock15mBeforeReset.email` dan Password dengan satu nilai lalu klik "Log in"
3. Verifikasi caption lock 15 menit tampil, sehingga kondisi awal terkunci memang aktif
4. Jalankan alur Reset Password lengkap untuk user tersebut melalui tautan reset dari mailbox uji
5. Verifikasi alur Reset Password selesai dengan sukses dan password user berubah
6. Buka `/login` lalu isi Email dengan email user tersebut dan Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
7. Verifikasi caption lock 15 menit tidak lagi tampil
8. Verifikasi browser berpindah ke Portal — Product Hub, sehingga login diproses normal
9. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"

### Melepas lock 1 jam

10. Logout dari Portal sehingga session kosong
11. Isi Email dengan `Fixture.authLoginPassword.users.lock1hBeforeReset.email` dan Password dengan satu nilai lalu klik "Log in"
12. Verifikasi caption lock 1 jam tampil
13. Jalankan alur Reset Password lengkap untuk user tersebut
14. Isi Email dengan email user tersebut dan Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
15. Verifikasi caption lock 1 jam tidak lagi tampil
16. Verifikasi browser berpindah ke Portal — Product Hub
17. Logout dari Portal sehingga session kosong

### Melepas status requires reset

18. Isi Email dengan `Fixture.authLoginPassword.users.requiresResetBeforeReset.email` dan Password dengan satu nilai lalu klik "Log in"
19. Verifikasi caption requires reset tampil
20. Jalankan alur Reset Password lengkap untuk user tersebut
21. Isi Email dengan email user tersebut dan Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
22. Verifikasi caption requires reset tidak lagi tampil
23. Verifikasi browser berpindah ke Portal — Product Hub
24. Logout dari Portal sehingga session kosong

### Melepas status permanen

25. Isi Email dengan `Fixture.authLoginPassword.users.permanentBeforeReset.email` dan Password dengan satu nilai lalu klik "Log in"
26. Verifikasi caption lock permanen tampil
27. Jalankan alur Reset Password lengkap untuk user tersebut
28. Isi Email dengan email user tersebut dan Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
29. Verifikasi caption lock permanen tidak lagi tampil
30. Verifikasi browser berpindah ke Portal — Product Hub
31. Logout dari Portal sehingga session kosong

### Counter consecutive ikut ter-reset

32. Isi Email dengan email user yang `consecutive_1h_days`-nya bernilai 3 lalu isi Password dengan satu nilai dan klik "Log in"
33. Verifikasi caption "Incorrect email or password" muncul tanpa banner lock
34. Jalankan alur Reset Password lengkap untuk user tersebut
35. Isi Email dengan email user tersebut dan Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
36. Verifikasi browser berpindah ke Portal — Product Hub
37. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success", sehingga chain eskalasi seven hari sudah terputus oleh Reset Password

## Notes

- Spec ini memakai lima user dengan kondisi awal berbeda karena tiap tahap lock hanya bisa dilepas lewat Reset Password dan tiap tahap butuh akun terpisah supaya tidak saling menimpa. Kalau satu user dipakai, tahap berikutnya tidak akan tercapai karena user yang sama sudah tidak terkunci.
- Yang diuji di spec ini adalah efek Reset Password terhadap state lock modul ini, bukan langkah internal Reset Password. Detail alur itu milik modul `auth/reset-password` dengan TC-nya sendiri.
- Kebutuhan mailbox uji dan email reset per user dicatat di Prerequisites sebagai sumber resmi bagi tim FE, sesuai e2e-conventions.md bagian 2. Hambatan teknis tidak boleh menjadi alasan mengeluarkan TC.
- Reset Password yang berhasil mereset `failed_count`, `lock_level`, `lock_until`, dan `consecutive_1h_days` secara penuh, bukan sebagian. Langkah 32 sampai 37 membuktikan bagian terakhir itu.
- Verifikasi dilakukan dari sisi modul login, yaitu dengan mencoba login lagi setelah reset. Ini yang membedakan spec ini dari kemungkinan duplikat di modul Reset Password.
- Pembersihan state kelima user dilakukan di hook `afterEach` supaya tidak bergantung pada spec lain dan tetap jalan ketika spec ini dijalankan sendiri.