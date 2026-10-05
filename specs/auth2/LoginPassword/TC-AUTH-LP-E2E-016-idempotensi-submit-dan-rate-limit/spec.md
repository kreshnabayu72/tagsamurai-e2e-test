---
id: TC-AUTH-LP-E2E-016-idempotensi-submit-dan-rate-limit
title: Idempotensi dan guard double-submit, serta rate limit per IP
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-60
  - TC-AUTH-LP-61
  - TC-AUTH-LP-63
coverage:
  web: automated
---

# Idempotensi dan guard double-submit, serta rate limit per IP

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE, dengan IP request yang stabil dan bukan IP bersama.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan dua user uji, dibuat lewat API Global Settings > User dan direstore di `afterEach`:
  - `Fixture.authLoginPassword.users.doubleSubmitTarget` dengan kredensial benar dan `failed_count` awal 0
  - `Fixture.authLoginPassword.users.rateLimitTarget` dengan kredensial benar dan `failed_count` awal 0
- Password asli kedua user tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.users.doubleSubmitTarget.wrongPassword` berisi satu password salah untuk skenario klik ganda pada percobaan gagal.
- Kebutuhan intercept dicatat di Prerequisites sebagai sumber resmi bagi tim FE: jumlah request dan payload-nya diamati dari sisi browser, dan respons request pertama pada skenario retry ditahan sebelum sampai ke client.
- `Fixture.authLoginPassword.captions.tooManyRequests` berisi caption `"Too many requests. Please try again later."`
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Threshold rate limit belum ditetapkan dan masih `[TODO Engineering]`. Spec ini menjalankan request berulang sampai caption atau status HTTP 429 muncul, lalu mencatat jumlah request yang dibutuhkan sebagai bahan konfirmasi threshold. Ketidakpastian ini tidak menjadi alasan mengeluarkan TC.
- Hook `afterEach` mengembalikan `failed_count`, `lock_level`, dan counter rate limit ke nilai awal.

## Test Steps

### Klik ganda saat percobaan gagal

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.doubleSubmitTarget.email` dan Password dengan `Fixture.authLoginPassword.users.doubleSubmitTarget.wrongPassword`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang
4. Catat jumlah request `POST /auth/login` yang terkirim sebagai pembanding
5. Klik "Log in" lalu langsung klik lagi pada tombol yang sama secepat mungkin
6. Verifikasi tombol "Log in" berubah menjadi keadaan disabled dan loading setelah klik pertama
7. Verifikasi jumlah request yang terkirim bertambah tepat satu, sehingga klik kedua tidak mengirim request kedua
8. Verifikasi caption "Incorrect email or password" muncul satu kali
9. Verifikasi `failed_count` bertambah tepat satu di User Log, bukan dua
10. Verifikasi jumlah entri di User Log bertambah tepat satu

### Klik ganda saat percobaan berhasil

11. Isi ulang Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu selesaikan reCAPTCHA sampai tercentang
12. Klik "Log in" lalu langsung klik lagi pada tombol yang sama secepat mungkin
13. Verifikasi jumlah request yang terkirim bertambah tepat satu
14. Verifikasi hanya satu sesi yang terbentuk di User Log
15. Verifikasi jumlah entri User Log bertambah tepat satu dengan Status "Success"
16. Logout dari Portal sehingga session kosong

### Retry setelah client timeout

17. Pasang intercept yang menahan respons request login pertama sehingga client timeout, sementara request pertama tetap diproses server sampai selesai
18. Isi Email dengan `Fixture.authLoginPassword.users.doubleSubmitTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar
19. Verifikasi reCAPTCHA diselesaikan sampai tercentang
20. Klik "Log in" dan tunggu sampai client keburu timeout
21. Verifikasi tidak ada navigasi sukses yang terjadi, sehingga client memang belum menerima konfirmasi server
22. Lepas intercept dan biarkan request pertama selesai diproses
23. Kirim ulang submit yang sama tanpa perubahan pada email, password, maupun token reCAPTCHA
24. Verifikasi jumlah entri User Log bertambah paling banyak satu untuk dua submit, sehingga state tidak berubah dua kali
25. Verifikasi `failed_count` tidak bertambah, sehingga submit yang diproses berhasil tidak dihitung sebagai percobaan gagal kedua
26. Verifikasi hanya satu sesi yang terbentuk
27. Logout dari Portal sehingga session kosong

### Rate limit per IP terlampaui

28. Catat jumlah request login yang sudah terkirim dari IP environment ini sebagai pembanding
29. Kirim request login berulang dari IP yang sama tanpa jeda, memakai email `Fixture.authLoginPassword.users.rateLimitTarget.email` dan password yang benar
30. Verifikasi request yang melewati threshold mendapat status HTTP `429 Too Many Requests`
31. Verifikasi caption yang tampil adalah "Too many requests. Please try again later."
32. Verifikasi caption tersebut muncul tanpa banner lock, sehingga ini bukan lock per user
33. Verifikasi tidak ada entri baru di User Log milik `Fixture.authLoginPassword.users.rateLimitTarget`, sehingga rate limit tidak punya subjek user
34. Verifikasi `failed_count` milik user tersebut tidak bertambah, sehingga rate limit tidak ikut menaikkan counter lock per user
35. Verifikasi `lock_level` milik user tersebut tetap `none`, sehingga lock per user tidak terbentuk dari request yang kena rate limit
36. Verifikasi request yang sudah terlampaui tetap ditolak, sehingga throttle tidak hanya muncul sekali
37. Catat jumlah request login yang dibutuhkan sampai caption 429 muncul sebagai bahan konfirmasi threshold
38. Verifikasi request dari IP lain tidak terpengaruh, sehingga throttle benar-benar per IP

## Notes

- Rate limit per IP adalah lapisan infrastruktur tanpa subjek user. Karena itu ia tidak masuk surface User Log dan tidak menambah `failed_count`. Ini dibedakan dari lock per user di spec 004 sampai 007.
- Threshold rate limit belum ditetapkan di PRD §9.2 dan masih `[TODO Engineering]`. Jumlah request pada langkah 37 dicatat sebagai bahan konfirmasi, bukan sebagai angka yang diasumsikan sudah final.
- Intercept pada langkah 17 menahan respons di sisi client, bukan membatalkan request. Ini yang membuat kondisi "server sudah diproses, client belum menerima" bisa terjadi tanpa merusak state.
- Retry memakai email, password, dan token reCAPTCHA yang sama persis, sesuai TC-AUTH-LP-61. Karena itu kalau ada penghitungan attempt di sisi server, bedanya hanya di idempotency key.
- Guard double-submit di sisi client ditulis sebagai "tombol disabled dan loading setelah klik pertama". Verifikasi jumlah request di langkah 7 adalah bukti tidak adanya request kedua, bukan hanya tampilan tombol.
- Karena request pada skenario rate limit terhitung terhadap IP environment CI, spec ini tidak boleh berjalan paralel dengan spec lain yang melakukan submit login. Suite sudah disetel `parallel: false`.
- Hook `afterEach` mengembalikan counter rate limit ke nilai awal. Kalau environment tidak menyediakan cara mengosongkan counter itu, kebutuhan tersebut dicatat di gap-spec, bukan dibiarkan bocor ke spec lain.