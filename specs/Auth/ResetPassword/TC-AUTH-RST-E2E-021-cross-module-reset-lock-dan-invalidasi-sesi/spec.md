---
id: TC-AUTH-RST-E2E-021-cross-module-reset-lock-dan-invalidasi-sesi
title: "Cross-module: reset password sukses membersihkan lock Login dan menginvalidasi sesi aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-111
  - TC-AUTH-RST-120
coverage:
  web: automated
---

# Cross-module: reset password sukses membersihkan lock Login dan menginvalidasi sesi aktif

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Dua user berstatus Activated dan Active di Global Settings > User, dengan password lama yang
  diketahui dan tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di
  fixture. Keduanya bukan Default User dan bukan akun admin Total Control.
  - `Fixture.authResetPassword.users.lockedRequiresReset.email` adalah user yang terkunci pada tahap
    requires reset, dipakai untuk subbagian verifikasi lock dari sisi Login.
  - `Fixture.authResetPassword.users.activatedWithSession.email` adalah user yang punya sesi aktif
    di platform mobile, dipakai untuk subbagian invalidasi sesi. User ini tidak pernah login di web
    pada run ini.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy dan
  berbeda dari password lama.
- `Spectra.env.AUTH_NEW_PASSWORD_2` adalah satu password baru kedua yang juga memenuhi seluruh
  Password Policy dan berbeda dari password lama serta dari
  `Spectra.env.AUTH_NEW_PASSWORD`, dipakai untuk user kedua pada spec ini.
- `Fixture.authResetPassword.users.lock.requiresReset` adalah cara mengunci user pada tahap requires
  reset lewat Global Settings > User, sehingga tahap lock beserta counter-nya siap. Kemampuan
  ini disiapkan tim FE dan dikembalikan ke keadaan awal di `afterEach`.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tertentu dengan masa berlaku 24 jam, lewat API Global Settings > User.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.sessions.seedActiveMobileSession` adalah cara membuat satu sesi aktif
  milik user pada platform mobile. Kemampuan ini disiapkan tim FE.
- `Fixture.authResetPassword.sessions.readSessionState` adalah cara membaca status sesi user
  beserta sesi turunannya.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Reset sukses membersihkan lock, diverifikasi dari sisi Login with Password

1. Kunci `Fixture.authResetPassword.users.lockedRequiresReset.email` pada tahap requires reset
   memakai `Fixture.authResetPassword.users.lock.requiresReset`
2. Verifikasi user tersebut memang terkunci pada Global Settings > User
3. Buat satu token reset aktif milik user tersebut memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
4. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
5. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
6. Isi field Confirm Password dengan nilai yang sama
7. Klik "Reset Password"
8. Verifikasi navigasi ke halaman Password Reset Successful terjadi
9. Buka halaman Login with Password dan login dengan email serta
   `Spectra.env.AUTH_NEW_PASSWORD` milik user tersebut
10. Verifikasi login diproses normal
11. Verifikasi tidak ada caption lock yang tampil setelah login
12. Verifikasi tidak ada pengembalian ke halaman Login dengan Password karena masih terkunci
13. Verifikasi user tersebut tidak lagi terkunci pada Global Settings > User
14. Verifikasi tahap lock user pada Global Settings > User kembali ke keadaan tidak terkunci

### Reset sukses menginvalidasi seluruh sesi aktif user

15. Buat satu sesi aktif untuk
    `Fixture.authResetPassword.users.activatedWithSession.email` pada platform mobile memakai
    `Fixture.authResetPassword.sessions.seedActiveMobileSession`
16. Verifikasi sesi tersebut tercatat aktif beserta sesi turunannya
17. Buat satu token reset aktif milik user tersebut memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
18. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
19. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD_2`
20. Isi field Confirm Password dengan nilai yang sama
21. Klik "Reset Password"
22. Verifikasi navigasi ke halaman Password Reset Successful terjadi
23. Verifikasi status sesi mobile user tersebut berubah menjadi logout paksa
24. Verifikasi sesi turunan milik sesi tersebut ikut berakhir
25. Verifikasi dialog "Password Changed" tampil pada platform mobile saat request atau heartbeat
    berikutnya dilakukan
26. Verifikasi request berikutnya pada platform mobile tidak lagi dilayani sebagai sesi aktif
27. Verifikasi kedua surface pencatatan masing-masing memiliki satu entri baru dengan Note
    "Logged out (password changed)"
28. Verifikasi tidak ada entri pencatatan yang menyebut maupun membocorkan nilai password

## Notes

- Spec ini memeriksa efek reset password dari luar modul reset password, yaitu dari sisi Login
  with Password dan dari sisi Session Management. Kedua sisi itu punya suite sendiri, dan yang diuji
  di sini adalah bahwa reset password menghasilkan efek yang benar pada keduanya.
- Dua user dipisahkan supaya lock yang dihapus pada subbagian pertama tidak bercampur dengan sesi
  yang diinvalidasi pada subbagian kedua, dan supaya nilai password baru tidak saling menggantikan.
- Sesi dibaca dari state sesi, bukan dari dialog di mobile, supaya kondisi sebenarnya terukur.
  Dialog pada langkah 25 dipakai sebagai pembuktian tambahan bahwa user diberi tahu, bukan sebagai
  sumber kebenaran status sesi.
- Email dan role user tidak diubah oleh reset password, sehingga pengenalan user pada sesi tetap
  memakai identitas yang sama.
- Nilai password hanya diambil dari environment variable, tidak ditulis di spec maupun fixture.