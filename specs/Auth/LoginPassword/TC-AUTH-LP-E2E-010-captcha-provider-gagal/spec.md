---
id: TC-AUTH-LP-E2E-010-captcha-provider-gagal
title: Provider reCAPTCHA gagal saat verifikasi token dan perlakuan sebagai timeout
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-18
coverage:
  web: automated
---

# Provider reCAPTCHA gagal saat verifikasi token dan perlakuan sebagai timeout

Mode: mock

Kebutuhan mock yang dicatat di sini sebagai sumber resmi bagi tim FE:

- Endpoint verifikasi token reCAPTCHA di sisi server dipaksa timeout. Intercept dipasang pada request server ke provider reCAPTCHA, bukan pada request browser ke aplikasi, karena provider dipanggil di server.
- Respons yang dipaksa adalah kegagalan koneksi atau timeout pada provider, sehingga server tidak mendapat verdict token yang sah maupun tidak sah.
- Intercept dipasang hanya selama submit pada spec ini, dan dilepas setelah selesai supaya spec lain tidak ikut terpengaruh.
- Backend tidak ikut di-mock. Yang dipaksa hanya jalur keluar server ke provider reCAPTCHA.

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Bukan platform mobile. Spec ini dijalankan di browser web.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- `Spectra.env.AUTH_PASSWORD` berisi password user uji aktif. Nilai ini tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.users.activated` berisi user berstatus Activated dan Active dengan email diketahui.
- `Fixture.authLoginPassword.users.activated.wrongPassword` berisi satu password salah.
- `Fixture.authLoginPassword.captions.captchaNotCompleted` berisi caption reCAPTCHA kosong.
- `Fixture.authLoginPassword.captions.serverErrorToast` berisi caption toast kegagalan server.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook `before` mengembalikan `failed_count` dan `lock_state` user uji ke nilai awal.
- Timeout provider disimulasikan lewat `Spectra.intercept()`, bukan dengan mengganti site key sehingga memakai reCAPTCHA dummy.

## Test Steps

### Submit dengan provider reCAPTCHA timeout

1. Pasang intercept timeout pada request server ke provider reCAPTCHA
2. Buka `/login`
3. Isi Email dengan `Fixture.authLoginPassword.users.activated.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
4. Verifikasi reCAPTCHA diselesaikan sampai tercentang di sisi browser, sehingga token terkirim
5. Klik "Log in"
6. Verifikasi form tetap terbuka, field Email dan field Password tetap terisi, dan tombol "Log in" kembali enabled
7. Verifikasi tidak ada navigasi ke Portal maupun ke layar mana pun
8. Verifikasi tidak ada layar "Confirm to Continue" maupun layar MFA yang muncul
9. Verifikasi tidak ada entri "Success" baru di User Log, sehingga provider yang gagal tidak diperlakukan sebagai login berhasil
10. Verifikasi pesan yang tampil adalah perlakuan timeout, yaitu toast kegagalan server atau caption retry, bukan klaim bahwa kredensial salah
11. Verifikasi caption "Incorrect email or password" tidak muncul, sehingga kredensial tidak dievaluasi
12. Verifikasi caption "Email is not registered yet" tidak muncul, sehingga email tetap dianggap terdaftar
13. Lepas intercept timeout
14. Verifikasi form tetap dapat dipakai ulang tanpa perlu memuat ulang halaman

### Submit ulang setelah provider pulih

15. Isi ulang field Password dengan `Spectra.env.AUTH_PASSWORD` lalu selesaikan reCAPTCHA sampai tercentang
16. Klik "Log in"
17. Verifikasi browser berpindah ke Portal — Product Hub
18. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"
19. Logout dari Portal sehingga session kosong

## Notes

- Provider reCAPTCHA down atau timeout tidak bisa dipicu dengan aman di backend nyata, sehingga spec ini memakai `Mode: mock`. Ini sesuai e2e-conventions.md bagian 6, bukan alasan mengeluarkan TC.
- Yang dimock adalah jalur server ke provider reCAPTCHA, bukan respons aplikasi ke browser. Backend tetap nyata supaya perilaku state dan pencatatan tetap teruji.
- PRD §9.6 menyatakan provider down diperlakukan sebagai timeout pada §2, yaitu toast retry. Karena itu langkah 10 ditulis sebagai dua kemungkinan tampilan yang salah satunya gagal, bukan mengunci satu string yang belum ditetapkan.
- Rollback tidak ada di sini karena tidak ada state yang berubah. Kalau ternyata lock state atau counter berubah, itu temuan dan dicatat sebagai gap TC.
- Toast kegagalan server yang sama juga dipakai pada TC-AUTH-LP-E2E-017, tapi di situ sumbernya adalah kegagalan pada endpoint login, bukan kegagalan provider CAPTCHA.
- Intercept dilepas pada langkah 13 supaya spec lain yang memakai provider reCAPTCHA asli tidak ikut terpengaruh. Karena itu suite ini disetel `parallel: false`.