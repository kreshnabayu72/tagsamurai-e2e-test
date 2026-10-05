---
id: TC-AUTH-LP-E2E-020-lock-per-platform-independen
title: "Lock per-platform independen: user terkunci di web tetap bisa login di mobile"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-45
coverage:
  mobile: automated
---

# Lock per-platform independen: user terkunci di web tetap bisa login di mobile

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang menyiapkan dua konteks sekaligus, yaitu browser web dan perangkat mobile.
- Dua konteks memakai user uji yang sama. Sesi web dan sesi mobile dipisahkan agar login di satu platform tidak membangun session di platform lain.
- Hook `before` menyiapkan user uji berstatus Activated dan Active dengan kredensial benar, lalu mengembalikan `failed_count`, `lock_level`, dan `lock_until` ke nilai awal di `afterEach`.
- Password asli user tersebut tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.users.platformSplit.wrongPassword` berisi satu password salah untuk memicu lock di web saja.
- `Fixture.authLoginPassword.captions.lock15m` berisi caption lock 15 menit.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook dapat membaca catatan lock per platform dari User Log, sehingga platform web dan platform mobile bisa dibedakan.

## Test Steps

### Kunci user lewat tiga percobaan salah di web

1. Buka `/login` di browser web
2. Isi Email dengan `Fixture.authLoginPassword.users.platformSplit.email` dan Password dengan `Fixture.authLoginPassword.users.platformSplit.wrongPassword`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
4. Verifikasi caption "Incorrect email or password" muncul
5. Ulangi langkah 2 dan 3 dua kali lagi, menyelesaikan reCAPTCHA ulang setiap kali
6. Verifikasi banner lock 15 menit muncul, sehingga tiga percobaan salah di platform web sudah menghasilkan lock
7. Verifikasi catatan lock pada User Log tercatat untuk platform web
8. Verifikasi `lock_level` tercatat pada tahap 15 menit dan `lock_until` terisi

### Login yang benar di mobile tetap diterima

9. Buka aplikasi mobile pada halaman Login with Password dengan akun yang sama
10. Verifikasi tidak ada widget reCAPTCHA di mobile
11. Isi Email dengan email yang sama dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar
12. Klik "Log in"
13. Verifikasi tidak ada banner lock 15 menit yang tampil di mobile, sehingga lock web tidak terbawa ke platform mobile
14. Verifikasi caption "Your account is locked" tidak muncul di mobile
15. Verifikasi browser berpindah ke layar MFA atau ke Portal — Product Hub sesuai hasil evaluasi tahap berikutnya
16. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" untuk platform mobile
17. Verifikasi catatan lock platform web tetap pada tahap 15 menit dan tidak berubah menjadi `requires_reset` maupun `permanent`
18. Verifikasi catatan lock platform mobile terpisah dan tidak sedang terkunci
19. Logout dari Portal sehingga session kosong

### Submit di web tetap terkunci setelah login mobile berhasil

20. Kembali ke browser web yang masih berada di halaman Login with banner lock
21. Verifikasi banner lock 15 menit masih tampil, sehingga lock web tidak dilepas oleh login yang berhasil di platform lain
22. Verifikasi jumlah entri di User Log tidak bertambah dari submit di web, sesuai aturan submit saat lock aktif tidak dicatat
23. Verifikasi `failed_count` tidak bertambah dari submit di web

## Notes

- Lock dicatat per platform, jadi lock web dan lock mobile tidak saling menimpa. Ini yang dibuktikan oleh langkah 17 sampai 18.
- Login berhasil di mobile pada langkah 12 sampai 15 adalah bukti utama bahwa lock bersifat independen. Kalau caption lock ikut muncul, berarti penguncian tidak per platform.
- Lock masih bisa dilepas hanya lewat Reset Password di platform tempat lock itu terjadi, dan itu diuji di TC-AUTH-LP-E2E-008.
- Submit di web pada langkah 21 sampai 23 memakai aturan submit saat lock aktif: tetap enabled, ditolak lebih awal, tidak dievaluasi, dan tidak dicatat. Aturan yang sama diuji di TC-AUTH-LP-E2E-004 dan TC-AUTH-LP-E2E-005.
- Email dan Password di mobile tidak memakai reCAPTCHA, sesuai TC-AUTH-LP-E2E-019, sehingga langkah 12 tidak melewati langkah CAPTCHA.
- Spec ini memakai satu user dengan dua konteks. Dua user terpisah tidak akan bisa membuktikan independensi, karena pengunciannya bisa berasal dari user yang berbeda.
- Hook mengembalikan state lock di akhir spec, sehingga user uji tidak meninggalkan lock aktif untuk spec lain.
- Karena memakai satu user dan dua konteks, spec ini tidak boleh berjalan paralel dengan spec lain yang memakai user uji atau state lock yang sama. Suite sudah disetel `parallel: false`.