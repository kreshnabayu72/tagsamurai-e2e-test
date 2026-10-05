---
id: TC-AUTH-LP-E2E-019-mobile-login-tanpa-captcha
title: "Login with Password di mobile app: layout layar penuh tanpa reCAPTCHA dan tanpa Agreement"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-2
  - TC-AUTH-LP-17
coverage:
  mobile: automated
---

# Login with Password di mobile app: layout layar penuh tanpa reCAPTCHA dan tanpa Agreement

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi dengan perangkat atau emulator mobile yang siap dipakai, viewport di bawah 768px, dan aplikasi dalam versi mobile.
- Bukan platform web. Spec ini dijalankan di mobile app.
- Belum login dan session kosong. Halaman Login with Password terbuka di aplikasi mobile.
- Hook `before` menyediakan user uji berstatus Activated dan Active dengan kredensial benar, dibuat lewat API Global Settings > User dan direstore di `afterEach`.
- Password asli user tersebut tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.users.activated.wrongPassword` berisi satu password salah untuk membuktikan submit tidak ditolak karena CAPTCHA.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Inspeksi DOM dilakukan lewat inspeksi view pada perangkat, sehingga "tidak ada di DOM" dibuktikan dari struktur view, bukan dari ketiadaan elemen yang terlihat saja.

## Test Steps

### Tampilan default halaman Login with Password di mobile

1. Buka aplikasi mobile pada halaman Login with Password
2. Verifikasi judul layar adalah "Login with Password"
3. Verifikasi subtitle adalah "Sign in and start managing your assets", sesuai PRD §4.9
4. Verifikasi logo TAG Samurai tampil di bagian atas
5. Verifikasi field Email dengan label "Email" dan placeholder "Enter your email" tampil
6. Verifikasi field Password dengan label "Password" dan placeholder "Enter your password" tampil
7. Verifikasi tombol "Log in" tampil dan memenuhi lebar layar
8. Verifikasi tautan "Log in with OTP" dan tautan "Reset here" tampil
9. Verifikasi viewport mengisi layar penuh tanpa bayangan kartu, sesuai PRD §4.8 Mobile breakpoint
10. Verifikasi widget reCAPTCHA tidak ada di struktur view
11. Verifikasi checkbox Agreement tidak ada di halaman ini, sehingga layar Confirm to Continue tidak dipindahkan ke dalam form
12. Verifikasi tidak ada tombol "Remember me"

### Submit tanpa token reCAPTCHA pada kredensial salah

13. Isi Email dengan `Fixture.authLoginPassword.users.activated.email` dan Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword`
14. Klik "Log in" tanpa melewati langkah CAPTCHA apa pun
15. Verifikasi caption yang tampil adalah "Incorrect email or password", sehingga submit tidak ditolak karena ketiadaan token reCAPTCHA
16. Verifikasi caption "Please verify that you are not a robot" tidak muncul di platform ini
17. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Failed" dan Note "Incorrect password", sehingga request benar-benar dievaluasi server tanpa token CAPTCHA
18. Verifikasi `failed_count` bertambah satu

### Submit tanpa token reCAPTCHA pada kredensial benar

19. Isi Password dengan `Spectra.env.AUTH_PASSWORD` yang benar lalu klik "Log in"
20. Verifikasi browser berpindah ke layar MFA atau ke Portal — Product Hub sesuai hasil evaluasi tahap berikutnya
21. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"
22. Verifikasi tidak ada permintaan verifikasi token reCAPTCHA yang dikirim ke server pada submit mana pun di spec ini

## Notes

- Platform mobile tidak mengirim token reCAPTCHA karena memakai proteksi alternatif. Karena itu absennya widget bukan sekadar perbedaan tampilan, melainkan perbedaan perilaku server.
- Langkah 15 dan 17 membuktikan ketiadaan CAPTCHA tidak menggagalkan submit. Kalau caption yang muncul adalah caption CAPTCHA, berarti proteksi alternatif belum aktif.
- Subtitle mobile mengikuti wireframe §4.9 dengan bentuk jamak "assets". Subtitle web memakai bentuk tunggal "your asset". Perbedaan ini mengikuti PRD apa adanya, dan tidak dianggap konflik karena keduanya berada pada layout yang berbeda.
- Layout layar penuh tanpa bayangan kartu adalah breakpoint mobile di PRD §4.8, bukan perilaku mobile app murni. Karena viewport di bawah 768px, keduanya menghasilkan tampilan yang sama.
- Checkbox Agreement memang tidak ada di form mana pun. Layar Confirm to Continue untuk mobile punya spec sendiri di modul `auth/confirm-agreement` bila ada.
- ReCAPTCHA di web beserta caption dan Note-nya diuji di TC-AUTH-LP-E2E-009. Kegagalan provider reCAPTCHA di TC-AUTH-LP-E2E-010.
- Email prefilled dari "Edit email" adalah perilaku halaman OTP, dan ada di TC-AUTH-LP-E2E-015. Tidak ada di sini karena sumbernya bukan mobile.
- Lock per-platform independen antara web dan mobile diuji di TC-AUTH-LP-E2E-020. Spec ini sengaja berhenti sebelum lock.