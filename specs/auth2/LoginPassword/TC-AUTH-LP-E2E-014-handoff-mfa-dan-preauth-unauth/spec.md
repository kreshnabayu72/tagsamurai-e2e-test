---
id: TC-AUTH-LP-E2E-014-handoff-mfa-dan-preauth-unauth
title: Handoff ke MFA, pre-auth web yang tidak punya device, dan alur pre-auth unauthorized
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-48
  - TC-AUTH-LP-49
  - TC-AUTH-LP-50
coverage:
  web: automated
---

# Handoff ke MFA, pre-auth web yang tidak punya device, dan alur pre-auth unauthorized

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan dua user uji, dibuat lewat API Global Settings > User dan direstore di `afterEach`:
  - `Fixture.authLoginPassword.users.mfaTarget` dengan kredensial benar dan MFA aktif, dan device serta geolokasi belum tercatat sehingga login memicu MFA
  - `Fixture.authLoginPassword.users.noDeviceMfaTarget` dengan kredensial benar dan MFA aktif, tetapi device-nya belum pernah tercatat sama sekali
- Password asli kedua user tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- MFA milik modul `auth/login-mfa`. Yang diuji di sini adalah handoff dari modul ini ke layar MFA, bukan langkah internal MFA itu sendiri.
- Kebutuhan untuk menguji pre-auth unauthorized dicatat di Prerequisites sebagai sumber resmi bagi tim FE: pre-auth device token dapat dibuat lewat API admin. Token dibuat secara stateless supaya tidak bergantung pada spec lain.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook `after` mengembalikan device dan geolokasi kedua user ke keadaan semula.

## Test Steps

### Handoff ke MFA setelah password benar

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.mfaTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
4. Verifikasi browser berpindah ke layar MFA, sehingga modul ini menghentikan prosesnya dan menyerahkan ke modul MFA
5. Verifikasi tidak ada navigasi langsung ke Portal — Product Hub pada langkah ini
6. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password", sehingga pencatatan sukses terjadi di akhir alur login, bukan setelah MFA selesai
7. Selesaikan alur MFA dengan kode OTP yang benar untuk user tersebut
8. Verifikasi browser berpindah ke Portal — Product Hub setelah MFA selesai

### Pre-auth web tanpa device

9. Logout dari Portal sehingga session kosong
10. Isi Email dengan `Fixture.authLoginPassword.users.noDeviceMfaTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
11. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
12. Verifikasi browser berpindah ke layar MFA
13. Verifikasi tidak ada layar error device, sehingga user tanpa device sebelumnya tetap dapat masuk lewat MFA
14. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"
15. Selesaikan alur MFA dengan kode OTP yang benar untuk user tersebut
16. Verifikasi browser berpindah ke Portal — Product Hub

### Pre-auth unauthorized

17. Logout dari Portal sehingga session kosong
18. Buat satu pre-auth device token lewat API admin, lalu pakai token itu pada context browser yang sama
19. Buka `/login` lalu isi Email dengan `Fixture.authLoginPassword.users.mfaTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
20. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
21. Verifikasi browser berpindah ke layar MFA
22. Verifikasi pre-auth token yang dipakai valid, sehingga prosesnya tidak berhenti di tahap pre-auth
23. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password", sehingga alur unauthorized tidak menambah entri gagal
24. Selesaikan alur MFA dengan kode OTP yang benar untuk user tersebut
25. Verifikasi browser berpindah ke Portal — Product Hub
26. Logout dari Portal sehingga session kosong

## Notes

- Modul ini berhenti tepat sebelum MFA. Detail MFA seperti masa berlaku OTP, jumlah percobaan OTP, dan tampilan input-nya bukan bagian dari spec ini.
- Pencatatan `Login with password` sebagai sukses terjadi setelah password diverifikasi, sehingga di spec ini ia muncul sebelum MFA selesai. Ini yang dibuktikan oleh langkah 6.
- Pre-auth token dibuat lewat API admin karena jalur ini tidak punya UI yang bisa dipakai user biasa. Kebutuhan itu dicatat di Prerequisites, bukan dianggap alasan mengeluarkan TC.
- Device dan geolokasi dikembalikan oleh hook `after`, sehingga spec ini tidak meninggalkan user yang tercatat sudah pernah login dari perangkat CI.
- Spec ini memakai dua user karena satu user dipakai untuk handoff normal dan satu untuk kondisi tanpa device. Kalau satu user dipakai, pengujian tanpa device tidak bisa dilakukan karena device sudah tercatat pada login sebelumnya.
- Alur pre-auth unauthorized milik modul `auth/login-pre-auth`, dan yang diuji di sini hanya bahwa token yang valid diteruskan tanpa menambah entri gagal. Pengujian token invalid dan kedaluwarsa di modul tersebut.
- Error OTP salah dan lockout MFA juga milik modul `auth/login-mfa`, bukan di sini.