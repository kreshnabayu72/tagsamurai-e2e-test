---
id: TC-AUTH-RST-E2E-011-resend-berhasil-dan-invalidasi-token-lama
title: Resend email reset berhasil, invalidasi token lama, dan resend tidak dicatat
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-23
  - TC-AUTH-RST-24
  - TC-AUTH-RST-26
coverage:
  web: automated
---

# Resend email reset berhasil, invalidasi token lama, dan resend tidak dicatat

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. User ini bukan Default User dan bukan akun
  admin Total Control.
- User tersebut belum menyentuh batas rate limit 5 kali per 24 jam, sehingga resend pada spec ini
  bukan percobaan yang di-ratelimit.
- `Fixture.authResetPassword.seedRequests.requestWithEmail` adalah cara membuat satu request reset
  sukses sehingga halaman Email Sent! terbuka dan cooldown berjalan.
- `Fixture.authResetPassword.cooldown.release` adalah cara membuat cooldown 60 detik selesai tanpa
  harus menunggu 60 detik secara wall-clock. Kemampuan ini disiapkan tim FE. Nilai durasi cooldown
  yang sebenarnya tetap diambil dari `Fixture.authResetPassword.cooldown.durationSeconds`, bukan
  diasumsikan di spec ini.
- `Fixture.authResetPassword.mailbox` adalah kotak masuk uji untuk user tersebut, disiapkan tim FE
  dan dikosongkan dari email reset password sebelum spec berjalan.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca daftar token reset milik
  user tersebut beserta statusnya.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.
- Toast yang dirujuk diambil dari `Fixture.authResetPassword.captions`.

## Test Steps

### Resend berhasil setelah cooldown selesai

1. Buat kondisi awal dengan request reset sukses untuk
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.seedRequests.requestWithEmail`
2. Verifikasi halaman Email Sent! tampil
3. Pastikan cooldown selesai dengan `Fixture.authResetPassword.cooldown.release`
4. Verifikasi tombol "Resend" berada dalam keadaan enabled
5. Verifikasi countdown sudah tidak tampil
6. Klik "Resend"
7. Verifikasi toast yang tampil adalah "Success, the email has been resent."
8. Verifikasi halaman Email Sent! tetap tampil dan tidak ada navigasi ke halaman lain
9. Verifikasi countdown dimulai ulang dari awal
10. Verifikasi tombol "Resend" kembali disabled selama cooldown baru
11. Tunggu email reset kedua masuk ke kotak masuk uji
12. Verifikasi email reset kedua masuk ke kotak masuk user dengan subject yang sama
13. Verifikasi hanya satu email reset yang valid pada waktu yang bersamaan, yaitu yang terakhir dikirim

### Token lama di-invalidasi oleh resend

14. Baca daftar token reset milik user tersebut dan simpan nilai token dari request pertama sebagai
    token lama
15. Buka tautan "Confirm Email" dari email reset pertama pada kotak masuk uji
16. Verifikasi halaman 404 tampil, sehingga token lama tidak lagi berlaku walau belum lewat 24 jam
17. Verifikasi halaman 404 yang tampil memakai varian copy Expired
18. Verifikasi tautan reset dari email kedua masih dapat dibuka

### Resend normal tidak dicatat

19. Catat jumlah entri terakhir pada kedua surface pencatatan sebelum resend berikutnya
20. Pastikan cooldown selesai dengan `Fixture.authResetPassword.cooldown.release`
21. Klik "Resend"
22. Verifikasi toast sukses resend tampil
23. Verifikasi jumlah entri pada kedua surface pencatatan tidak bertambah
24. Verifikasi tidak ada entri baru pada kedua surface pencatatan untuk aksi resend normal ini
25. Verifikasi entri dari request awal tetap ada dan tidak berubah, sehingga pencatatan hanya terjadi
    pada request pertama

## Notes

- Ketiga subbagian memakai satu user yang sama karena resend hanya berlaku pada user yang sama dan
  pada cooldown satu user yang sama. Spec tidak bergantung pada hasil spec lain.
- Yang diuji pada subbagian terakhir adalah ketiadaan entri baru, bukan ketiadaan perubahan pada
  entri lama. Keduanya dibedakan supaya regex pencarian log tidak salah baca.
- Reset cooldown lewat helper bukan berarti cooldown tidak ditegakkan server. Penegakan cooldown
  server-side diuji di spec 013.
- Nilai token hanya dibaca lewat helper dan dipakai di dalam spec ini tanpa dicatat di file, sesuai
  aturan e2e-conventions.md bagian 5.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Resend" dan "Log in with password". Aturan
  `[Submit]` dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit
  entitas, bukan untuk halaman autentikasi.