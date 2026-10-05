---
id: TC-AUTH-LP-E2E-009-captcha-gate-web
title: CAPTCHA gate pada halaman web dan urutan evaluasi sebelum status akun
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-15
  - TC-AUTH-LP-16
  - TC-AUTH-LP-30
coverage:
  web: automated
---

# CAPTCHA gate pada halaman web dan urutan evaluasi sebelum status akun

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE, dengan konfigurasi reCAPTCHA v2 Checkbox yang site key dan secret key-nya sudah benar.
- Bukan platform mobile. Spec ini dijalankan di browser web.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- `Spectra.env.AUTH_PASSWORD` berisi password user uji aktif. Nilai ini tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.users.activated` berisi user berstatus Activated dan Active yang sudah melewati seluruh gate.
- `Fixture.authLoginPassword.users.pendingActivation` berisi user berstatus Pending Activation dengan email diketahui.
- `Fixture.authLoginPassword.captions.captchaNotCompleted` berisi caption reCAPTCHA kosong.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook `before` mengembalikan `failed_count` dan `lock_level` user uji ke nilai awal, sehingga spec ini tidak bergantung pada spec lain.
- Jumlah entri log dibaca dari User Log milik masing-masing user uji, bukan dari log gabungan.

## Test Steps

### Submit tanpa menyelesaikan reCAPTCHA

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.activated.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
3. Verifikasi widget reCAPTCHA tampil dan belum tercentang
4. Klik "Log in" tanpa menyelesaikan reCAPTCHA
5. Verifikasi caption di atas tombol adalah "Please verify that you are not a robot"
6. Verifikasi caption tersebut muncul di atas tombol, bukan inline di bawah field Email maupun Password
7. Verifikasi form tetap aktif dan tombol "Log in" tetap enabled
8. Verifikasi browser tidak berpindah ke Portal maupun ke layar mana pun
9. Buka User Log milik `Fixture.authLoginPassword.users.activated` lalu verifikasi satu entri baru muncul dengan Status "Failed" dan Note "Captcha not completed"
10. Verifikasi entri tersebut bukan Note "Incorrect password", sehingga kredensial tidak dievaluasi

### Submit dengan reCAPTCHA terpecahkan

11. Isi ulang field Password dengan `Spectra.env.AUTH_PASSWORD` lalu selesaikan reCAPTCHA sampai tercentang
12. Verifikasi tidak ada caption lagi di atas tombol
13. Klik "Log in"
14. Verifikasi submit tidak lagi ditolak oleh caption reCAPTCHA, sehingga gate CAPTCHA tidak memblokir tahap berikutnya
15. Verifikasi browser berpindah ke Portal — Product Hub, sehingga evaluasi berikutnya berupa Agreement dan status akun tidak terpicu
16. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"
17. Logout dari Portal sehingga session kosong

### Token reCAPTCHA hanya berlaku untuk satu kali submit

18. Isi Email dengan `Fixture.authLoginPassword.users.activated.email` dan Password dengan `Fixture.authLoginPassword.users.activated.wrongPassword`
19. Verifikasi reCAPTCHA selesai terpecahkan, lalu klik "Log in"
20. Verifikasi caption "Incorrect email or password" muncul
21. Verifikasi field Password dikosongkan setelah login gagal
22. Isi Password kembali dengan nilai salah lain tanpa menyelesaikan reCAPTCHA ulang, lalu klik "Log in"
23. Verifikasi caption "Please verify that you are not a robot" muncul kembali
24. Verifikasi kredensial tidak dievaluasi dan caption password salah tidak muncul

### Urutan evaluasi CAPTCHA sebelum status akun

25. Catat jumlah entri di User Log milik `Fixture.authLoginPassword.users.pendingActivation` sebagai pembanding
26. Isi Email dengan `Fixture.authLoginPassword.users.pendingActivation.email` dan Password dengan satu nilai
27. Klik "Log in" tanpa menyelesaikan reCAPTCHA
28. Verifikasi caption yang muncul adalah "Please verify that you are not a robot"
29. Verifikasi caption "Your account has not been activated" tidak muncul, sehingga reCAPTCHA dievaluasi sebelum status akun
30. Verifikasi jumlah entri di User Log bertambah satu dengan Note "Captcha not completed"
31. Verifikasi entri tersebut bukan Note "Account is not activated", sehingga hanya kondisi pertama yang gagal yang dicatat

## Notes

- Urutan evaluasi lengkap ada di PRD §9.2. Spec ini hanya menguji dua hal terkait urutan, yaitu reCAPTCHA sebelum status akun, dan reCAPTCHA sebelum evaluasi kredensial. Status akun sendiri diuji di TC-AUTH-LP-E2E-011.
- Langkah 15 membuktikan bahwa reCAPTCHA terpecahan tidak membuat login berhenti. CAPTCHA hanya gerbang, bukan kondisi akhir.
- Token reCAPTCHA yang lolos hanya berlaku untuk satu kali submit. Ini dicatat di PRD §9.2 F-AUTHLP-04 dan TC-AUTH-LP-16. Penjadwalan ulang token adalah perilaku provider, bukan FE, jadi verifikasinya lewat submit kedua tanpa menyelesaikan ulang.
- Provider reCAPTCHA yang sedang down atau timeout ada di TC-AUTH-LP-E2E-010 dengan mode mock, karena tidak bisa dipicu dengan aman di backend nyata.
- Spec ini memakai dua user berbeda: satu aktif untuk gate CAPTCHA dan satu pending activation untuk urutan evaluasi. Kalau satu user dipakai, pengujian urutan tidak bisa dilakukan karena kondisi yang satu lebih dulu menutupi yang lain.
- User pending activation dibuat lewat API Global Settings > User dan dikembalikan ke status awal di `afterEach`, sehingga spec ini tidak bergantung pada spec lain.
- Widget reCAPTCHA tidak tampil di mobile, dan itu diuji di TC-AUTH-LP-E2E-019.