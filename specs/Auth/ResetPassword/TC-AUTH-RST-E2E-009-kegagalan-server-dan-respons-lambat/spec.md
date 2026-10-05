---
id: TC-AUTH-RST-E2E-009-kegagalan-server-dan-respons-lambat
title: Kegagalan server dan respons lambat pada alur Reset Password
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-20
  - TC-AUTH-RST-25
  - TC-AUTH-RST-41
  - TC-AUTH-RST-63
  - TC-AUTH-RST-91
coverage:
  web: automated
---

# Kegagalan server dan respons lambat pada alur Reset Password

## Prerequisites

- Belum login dan session kosong. Halaman Reset Password terbuka di browser.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- `Mode: mock`. Spec ini memakai intercept respons untuk memunculkan kegagalan server dan penundaan
  respons pada empat titik: request reset, resend, validasi link, dan submit password baru.
  Kemampuan intercept, status code yang dapat dipilih, dan penundaan respons disiapkan tim FE dan
  dicatat di `Fixture.authResetPassword.network`. Masing-masing titik punya key sendiri, misalnya
  `Fixture.authResetPassword.network.requestReset`, `.resendEmail`, `.validateToken`, dan
  `.submitPassword`, sehingga tidak bercampur satu sama lain.
- `Fixture.authResetPassword.network.failWith5xx` adalah status code kegagalan yang dipakai untuk
  disimulasikan, dan `Fixture.authResetPassword.network.delayMs` adalah durasi penundaan respons
  yang dipakai untuk simulasi respons lambat.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. Password user tersebut tersedia lewat
  `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di fixture.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy
  dan berbeda dari password lama.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut lewat API Global Settings > User, dengan masa berlaku 24 jam.
- `Fixture.authResetPassword.tokens.seedExpiredToken` adalah cara membuat satu token reset yang
  sudah kedaluwarsa milik user tersebut lewat API Global Settings > User.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset milik
  user tersebut.
- `Fixture.authResetPassword.mailbox` adalah kotak masuk uji untuk user tersebut, disiapkan tim FE
  dan dikosongkan dari email reset password sebelum spec berjalan.
- Caption toast yang dirujuk diambil dari `Fixture.authResetPassword.captions`.
- Mekanisme penyelesaian reCAPTCHA untuk environment otomasi disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.captcha`.

## Test Steps

### Request reset gagal karena server down

1. Aktifkan intercept kegagalan server pada `Fixture.authResetPassword.network.requestReset`
2. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
3. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
4. Verifikasi tidak ada navigasi ke halaman Email Sent!
5. Verifikasi toast yang tampil adalah "Internal server error."
6. Verifikasi halaman yang sama tetap terbuka
7. Verifikasi isi field Email dipertahankan
8. Verifikasi tombol "Reset Password" kembali enabled sehingga request dapat diulang
9. Verifikasi tidak ada token reset yang dibuat
10. Verifikasi tidak ada email reset yang masuk ke kotak masuk user
11. Nonaktifkan intercept

### Resend gagal karena server down

12. Buat kondisi awal dengan request reset sukses seperti pada spec 006
13. Verifikasi halaman Email Sent! tampil
14. Aktifkan intercept kegagalan server pada `Fixture.authResetPassword.network.resendEmail`
15. Klik "Resend"
16. Verifikasi toast yang tampil adalah "Error, failed to resend email."
17. Verifikasi tidak ada navigasi dari halaman Email Sent!
18. Verifikasi tidak ada token reset baru yang dibuat
19. Verifikasi token lama yang sudah ada tetap berlaku dan tidak berubah status
20. Verifikasi tidak ada email reset kedua yang masuk ke kotak masuk user
21. Nonaktifkan intercept

### Validasi link gagal karena server down

22. Aktifkan intercept kegagalan server pada `Fixture.authResetPassword.network.validateToken`
23. Buka tautan "Confirm Email" dari email reset pada kotak masuk uji
24. Verifikasi pesan yang tampil adalah "Unable to load this data."
25. Verifikasi tidak ada halaman 404 yang tampil, sehingga kegagalan pengecekan token tidak
    disamakan dengan token yang tidak berlaku
26. Verifikasi tersedia affordance untuk mencoba ulang
27. Verifikasi status token milik user tersebut tidak berubah
28. Nonaktifkan intercept

### Submit password baru gagal karena server down

29. Aktifkan intercept kegagalan server pada `Fixture.authResetPassword.network.submitPassword`
30. Buka tautan "Confirm Email" dari email reset pada kotak masuk uji
31. Verifikasi halaman Setup New Password tampil
32. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
33. Isi field Confirm Password dengan nilai yang sama
34. Klik "Reset Password"
35. Verifikasi tidak ada navigasi ke halaman Password Reset Successful
36. Verifikasi form tetap terbuka
37. Verifikasi isi field Password dan field Confirm Password dipertahankan
38. Verifikasi tombol "Reset Password" kembali enabled sehingga submit dapat diulang
39. Verifikasi status token milik user tersebut tetap "active"
40. Verifikasi password user tidak berubah
41. Nonaktifkan intercept

### Respons lambat tidak disimpulkan sukses

42. Aktifkan penundaan respons pada `Fixture.authResetPassword.network.requestReset` selama
    `Fixture.authResetPassword.network.delayMs`
43. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
44. Selesaikan widget reCAPTCHA, lalu klik "Reset Password"
45. Verifikasi halaman Email Sent! tidak tampil selama respons belum diterima
46. Verifikasi tidak ada toast sukses yang tampil selama respons belum diterima
47. Verifikasi tombol "Reset Password" tetap disabled selama request masih berjalan
48. Tunggu sampai respons definitif diterima dari server
49. Verifikasi halaman Email Sent! baru tampil setelah respons diterima
50. Nonaktifkan penundaan respons

## Notes

- Token expired disiapkan pada subbagian validasi link dan submit hanya untuk memastikan condition
  benar-benar tidak berubah saat server gagal. Kalau token aktif saja, pengamatan "status tidak
  berubah" tetap sah karena ada nilai sebelum dan sesudah yang dibandingkan.
- Kegagalan validasi link sengaja diuji terpisah dari halaman 404 karena keduanya punya copy dan
  affordance yang berbeda. Spec 015 menguji halaman 404 untuk token yang memang tidak berlaku.
- Toast diambil dari `Fixture.authResetPassword.captions` sesuai aturan e2e-conventions.md bagian 9.
- Yang diuji pada subbagian terakhir adalah ketiadaan asumsi sukses, bukan waktu respons tertentu.
  Durasi penundaan hanya alat untuk membuat kondisi tersebut, dan nilainya dicatat di fixture
  supaya tidak mengasumsikan angka final dari PRD.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password" dan "Resend". Aturan `[Submit]`
  dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas,
  bukan untuk halaman autentikasi.