---
id: TC-AUTH-LP-E2E-017-server-failure-dan-tanpa-konfirmasi
title: Kegagalan server saat submit dan tidak adanya asumsi sukses sebelum konfirmasi server
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-62
  - TC-AUTH-LP-68
coverage:
  web: automated
---

# Kegagalan server saat submit dan tidak adanya asumsi sukses sebelum konfirmasi server

Mode: mock

Kebutuhan mock yang dicatat di sini sebagai sumber resmi bagi tim FE:

- Endpoint `POST /auth/login` dipaksa membalas status `500` dengan body error untuk skenario kegagalan server. Intercept dipasang di sisi server atau proxy di depan server, bukan di browser, supaya kegagalan terjadi pada lapisan yang benar.
- Untuk skenario konfirmasi tertunda, respons `POST /auth/login` ditahan beberapa detik lalu dibalas sukses seperti normal. Penahanan membuat client berada dalam keadaan "belum menerima respons".
- Intercept dipasang hanya selama spec ini berjalan dan dilepas di `afterEach`, supaya spec lain tidak ikut terpengaruh.
- Backend tidak ikut di-mock di luar endpoint tersebut. Feature lain tetap nyata.

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan dua user uji berstatus Activated dan Active, dibuat lewat API Global Settings > User dan direstore di `afterEach`.
- Password asli kedua user tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.users.activated.wrongPassword` berisi satu password salah.
- `Fixture.authLoginPassword.captions.serverErrorToast` berisi caption toast `"Error, failed to log in."`
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook `before` mencatat jumlah entri User Log sebagai pembanding, dan hook `afterEach` mengembalikan `failed_count` serta `lock_level` ke nilai awal.
- MFA tidak diaktifkan pada kedua user, sehingga alur setelah login tidak dialihkan oleh MFA dan pengamatan tetap berada di modul ini.

## Test Steps

### Submit saat server mengembalikan error

1. Pasang intercept `500` pada `POST /auth/login`
2. Buka `/login`
3. Isi Email dengan `Fixture.authLoginPassword.users.activated.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar
4. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
5. Verifikasi toast yang tampil adalah "Error, failed to log in."
6. Verifikasi form login tetap terbuka, bukan berpindah ke layar lain
7. Verifikasi field Email dan field Password tetap terisi seperti sebelumnya, sehingga user tidak perlu mengetik ulang
8. Verifikasi tombol "Log in" kembali enabled dan tidak lagi berada pada keadaan loading, sehingga form bisa dipakai ulang
9. Verifikasi tidak ada navigasi ke Portal — Product Hub
10. Verifikasi jumlah entri di User Log tidak berubah, sehingga request yang gagal diproses server tidak dicatat sebagai percobaan login
11. Verifikasi `failed_count` tidak bertambah, sehingga kegagalan server tidak dihitung sebagai password salah
12. Verifikasi `lock_level` tetap `none`, sehingga kegagalan server tidak memicu lock

### Retry setelah server pulih

13. Lepas intercept `500`
14. Klik "Log in" lagi tanpa mengubah isi form
15. Verifikasi browser berpindah ke layar MFA atau ke Portal — Product Hub sesuai hasil evaluasi tahap berikutnya
16. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success", sehingga retry setelah kegagalan server aman dan hanya menghasilkan satu percobaan yang tercatat
17. Logout dari Portal sehingga session kosong

### Submit saat server tidak memberi konfirmasi

18. Pasang intercept yang menahan respons `POST /auth/login` beberapa detik sebelum membalas sukses
19. Isi Email dengan `Fixture.authLoginPassword.users.activated.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar
20. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
21. Verifikasi tombol "Log in" berada pada keadaan disabled dan loading selama respons belum diterima
22. Verifikasi browser tetap di halaman login selama respons belum diterima
23. Verifikasi tidak ada perubahan pada halaman Confirm to Continue, tidak ada navigasi ke Portal, dan tidak ada toast sukses
24. Verifikasi status di sisi server memang sudah berhasil, sehingga kondisi ini benar-benar "berhasil di server, belum dikonfirmasi ke client"
25. Biarkan respons sampai diterima
26. Verifikasi barulah setelah respons diterima browser berpindah ke layar MFA atau ke Portal — Product Hub
27. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success", sehingga pencatatan mengikuti keputusan server dan bukan tebakan client

## Notes

- Kegagalan server dan provider reCAPTCHA timeout menghasilkan toast yang mirip. Yang membedakan adalah sumbernya: di sini endpoint login yang mengembalikan 500, sedangkan di TC-AUTH-LP-E2E-010 yang gagal adalah jalur ke provider reCAPTCHA.
- Yang dibuktikan pada langkah 10 sampai 12 adalah server tidak mengubah state apa pun ketika request-nya gagal. Ini yang membuat retry pada langkah 14 aman.
- Intercept ditahan di sisi server atau proxy, bukan di browser. Kalau ditahan di browser, kegagalan akan terlihat sebagai network error yang tidak pernah sampai ke server, dan itu bukan kondisi yang diuji di sini.
- Penentuan sukses tanpa konfirmasi server merupakan Must NOT di PRD §4.3. Verifikasinya lewat perubahan tampilan selama respons ditahan, bukan lewat Inspect network saja, karena yang dilarang adalah perilaku antarmuka.
- Timeout pada langkah 18 memakai intercept yang sengaja menunda, bukan genuinely timeout. Ini membuat test deterministik.
- MFA sengaja tidak diaktifkan pada kedua user supaya tidak ada langkah ekstra yang mengalihkan perhatian dari verifikasi frontend.
- Karena memakai intercept global pada endpoint login, spec ini tidak boleh berjalan paralel dengan spec lain. Suite sudah disetel `parallel: false`.