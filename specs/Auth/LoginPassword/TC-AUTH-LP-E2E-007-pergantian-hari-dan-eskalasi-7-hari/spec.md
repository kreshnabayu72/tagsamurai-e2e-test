---
id: TC-AUTH-LP-E2E-007-pergantian-hari-dan-eskalasi-7-hari
title: Pergantian hari mereset tahap 15 menit dan 1 jam, serta eskalasi tujuh hari menuju lock permanen
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-39
  - TC-AUTH-LP-40
  - TC-AUTH-LP-41
  - TC-AUTH-LP-42
  - TC-AUTH-LP-43
coverage:
  web: automated
---

# Pergantian hari mereset tahap 15 menit dan 1 jam, serta eskalasi tujuh hari menuju lock permanen

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan enam user uji dengan kondisi awal berikut, dibuat lewat API Global Settings > User dan direstore di `afterEach`:
  - `Fixture.authLoginPassword.users.lock15mOnNewDay` dengan `lock_level = 15m`, `lock_until` masih aktif, `failed_count = 3`, `consecutive_1h_days = 0`
  - `Fixture.authLoginPassword.users.lock1hOnNewDay` dengan `lock_level = 1h`, `lock_until` masih aktif, `failed_count = 3`, `consecutive_1h_days = 1`
  - `Fixture.authLoginPassword.users.requiresResetOnNewDay` dengan `lock_level = requires_reset`, `failed_count = 3`
  - `Fixture.authLoginPassword.users.permanentOnNewDay` dengan `lock_level = permanent`, `failed_count = 3`
  - `Fixture.authLoginPassword.users.escalationTarget` dengan `lock_level = none`, `failed_count = 0`, `consecutive_1h_days = 7`
  - `Fixture.authLoginPassword.users.brokenChainTarget` dengan `lock_level = none`, `failed_count = 0`, `consecutive_1h_days = 3`
- Hook `beforeEach` menyediakan pemicu pergantian `attempt_date` ke hari berikutnya tanpa menunggu sungguhan. Kebutuhan ini dicatat di sini sebagai sumber resmi bagi tim FE.
- Keenam user bukan Default User, dan password asli masing-masing tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.captions.permanent` berisi caption lock permanen.
- `Fixture.authLoginPassword.captions.requiresReset` berisi caption status requires reset.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- Lock state diverifikasi dari Global Settings > User > User Log, bukan dari asumsi jumlah submit.

## Test Steps

### Pergantian hari mereset tahap 15 menit

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.lock15mOnNewDay.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
3. Verifikasi banner lock 15 menit tampil sebelum pergantian hari
4. Jalankan pemicu pergantian hari dari hook
5. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
6. Verifikasi banner lock 15 menit tidak lagi tampil
7. Verifikasi browser berpindah ke Portal — Product Hub, sehingga siklus lock dimulai ulang
8. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"
9. Logout dari Portal sehingga session kosong

### Pergantian hari mereset tahap 1 jam

10. Isi Email dengan `Fixture.authLoginPassword.users.lock1hOnNewDay.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
11. Verifikasi banner lock 1 jam tampil sebelum pergantian hari
12. Jalankan pemicu pergantian hari dari hook
13. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
14. Verifikasi banner lock 1 jam tidak lagi tampil
15. Verifikasi browser berpindah ke Portal — Product Hub
16. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"
17. Logout dari Portal sehingga session kosong

### Pergantian hari tidak mereset status requires reset

18. Isi Email dengan `Fixture.authLoginPassword.users.requiresResetOnNewDay.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
19. Verifikasi caption requires reset tampil
20. Jalankan pemicu pergantian hari dari hook
21. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
22. Verifikasi caption requires reset tetap tampil, sehingga status ini tidak dilepas oleh pergantian hari
23. Verifikasi browser tidak berpindah ke Portal
24. Verifikasi tidak ada entri "Success" baru di User Log

### Pergantian hari tidak mereset status permanen

25. Isi Email dengan `Fixture.authLoginPassword.users.permanentOnNewDay.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
26. Verifikasi caption lock permanen tampil
27. Jalankan pemicu pergantian hari dari hook
28. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
29. Verifikasi caption lock permanen tetap tampil, sehingga status ini tidak dilepas oleh pergantian hari
30. Verifikasi browser tidak berpindah ke Portal
31. Verifikasi tidak ada entri "Success" baru di User Log

### Salah pertama pada hari kedelapan langsung menuju lock permanen

32. Verifikasi `consecutive_1h_days` milik `Fixture.authLoginPassword.users.escalationTarget` bernilai 7 dari Global Settings > User > User Log
33. Isi Email dengan `Fixture.authLoginPassword.users.escalationTarget.email` dan Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword`
34. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
35. Verifikasi banner menampilkan caption lock permanen
36. Verifikasi caption tersebut bukan caption lock 15 menit, sehingga eskalasi langsung ke permanent tanpa melalui tahap 15 menit atau 1 jam
37. Verifikasi caption tersebut bukan caption requires reset
38. Verifikasi caption lock permanen menyediakan tautan langsung menuju alur Reset Password
39. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Failed" dan Note "Account locked", bukan "Locked 15 minutes"

### Rantai eskalasi terputus saat lock 1 jam tidak tercapai

40. Verifikasi `consecutive_1h_days` milik user eskalasi terputus bernilai 3 dari Global Settings > User > User Log
41. Isi Email dengan user tersebut lalu isi Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword` dan klik "Log in"
42. Verifikasi caption "Incorrect email or password" muncul, sehingga tahap lock tidak tercapai pada hari itu
43. Isi Password dengan satu password salah lain lalu klik "Log in"
44. Verifikasi caption "Incorrect email or password" muncul lagi tanpa banner lock
45. Verifikasi jumlah entri di User Log bertambah dua dan tidak ada entri tahap lock
46. Verifikasi `consecutive_1h_days` kembali bernilai 0, sehingga rantai eskalasi terputus dan tidak diteruskan ke hari keempat

## Notes

- Spec ini memakai enam user dengan kondisi awal berbeda karena tiap skenario butuh kondisi awal yang berbeda. User pertama dan kedua menguji reset oleh pergantian hari pada tahap 15 menit dan 1 jam, user ketiga dan keempat menguji tahap yang tidak boleh direset, user kelima menguji eskalasi hari kedelapan, dan user Keenam pada langkah 40 dipakai untuk rantai yang terputus.
- Syarat user pada langkah 40 adalah kondisi awal `consecutive_1h_days = 3` dengan `lock_level = none` dan `failed_count = 0`. Kebutuhan ini termasuk data prasyarat khusus, jadi dicatat di Prerequisites.
- Simulasi pergantian hari dilakukan lewat hook, bukan menunggu sampai tengah malam. Kebutuhan kemampuan teknis ini dicatat di Prerequisites sebagai sumber resmi bagi tim FE.
- Caption `{time}` pada tahap 15 menit dan 1 jam tidak diuji di sini karena fokus spec ini pada perilaku reset oleh pergantian hari. Caption lengkap kedua tahap itu diuji di TC-AUTH-LP-E2E-005 dan TC-AUTH-LP-E2E-006.
- Note log untuk status permanent adalah "Account locked", bukan "Locked 15 minutes". Perbedaan ini yang membuktikan tahap permanent terjadi langsung tanpa melalui tahap 15 menit.
- Melepas status requires reset dan permanent hanya bisa lewat Reset Password, dan itu diuji di TC-AUTH-LP-E2E-008.
- Pembersihan lock state keenam user dilakukan di hook `afterEach` supaya tidak bergantung pada spec lain dan tetap jalan ketika spec ini dijalankan sendiri.