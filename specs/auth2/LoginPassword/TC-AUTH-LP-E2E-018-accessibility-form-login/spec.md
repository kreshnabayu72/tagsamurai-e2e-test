---
id: TC-AUTH-LP-E2E-018-accessibility-form-login
title: "Aksesibilitas form login: urutan fokus keyboard, asosiasi caption error, dan pengumuman caption lock"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-79
  - TC-AUTH-LP-80
  - TC-AUTH-LP-81
coverage:
  web: automated
---

# Aksesibilitas form login: urutan fokus keyboard, asosiasi caption error, dan pengumuman caption lock

Mode: mock

Kebutuhan mock yang dicatat di sini sebagai sumber resmi bagi tim FE:

- State terkunci dibuat lewat API Global Settings > User, bukan dengan menunggu tiga kali submit di spec ini. Dipasang juga reader layar atau pendengar accessibility tree supaya atribut `role="alert"` benar-benar teramati.
- Hook tidak memverifikasi perilaku reader layar secara manual, hanya menyiapkan kondisi yang dibutuhkan atribut itu.

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan dua user uji, dibuat lewat API Global Settings > User dan direstore di `afterEach`:
  - `Fixture.authLoginPassword.users.a11yTarget` dengan kredensial benar dan status Activated serta Active
  - `Fixture.authLoginPassword.users.a11yLockTarget` dengan `lock_level = 15m`, `lock_until` masih aktif, dan kredensial benar
- Password asli kedua user tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.users.a11yTarget.wrongPassword` berisi satu password salah untuk memunculkan caption error.
- Hook `before` menyiapkan pendengar accessibility tree atau reader layar yang mencatat pengumuman role alert.
- `Fixture.authLoginPassword.captions.lock15m` berisi caption lock 15 menit yang dipakai pada langkah terakhir.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook `afterEach` mengembalikan `failed_count` dan `lock_level` kedua user ke nilai awal.

## Test Steps

### Semua elemen form dapat diakses keyboard

1. Buka `/login`
2. Tekan Tab berulang kali dari atas halaman lalu catat urutan elemen yang mendapat fokus
3. Verifikasi urutan fokus adalah Email Input, Password Input, Show/Hide Eye Toggle, reCAPTCHA, Log in Button, Link Log in with OTP, Link Reset here, sesuai PRD §4.8
4. Verifikasi setiap elemen yang mendapat fokus menampilkan focus ring yang terlihat jelas
5. Verifikasi Show/Hide Eye Toggle dapat diaktifkan lewat keyboard
6. Isi Password dengan satu nilai lalu verifikasi ikon eye berubah menjadi ikon eye crossed sehingga isi password terlihat
7. Kembalikan keadaan menjadi tersembunyi lewat keyboard
8. Beri fokus ke Link Log in with OTP lalu tekan Enter
9. Verifikasi navigasi ke halaman Login with OTP terjadi, sehingga tautan bukan hanya bisa diklik mouse
10. Kembali ke `/login`, beri fokus ke Link Reset here lalu tekan Enter
11. Verifikasi navigasi ke halaman Reset Password terjadi
12. Kembali ke `/login` lalu tekan Space saat Show/Hide Eye Toggle mendapat fokus
13. Verifikasi state tampilan password berubah, sehingga elemen ini juga dapat dioperasikan dengan Space, bukan hanya Enter

### Caption error terasosiasi dengan field

14. Isi Email kosong lalu klik "Log in"
15. Verifikasi caption "Email must not be empty" muncul di bawah field Email
16. Verifikasi field Email punya atribut `aria-invalid="true"`
17. Verifikasi field Email punya atribut `aria-describedby` yang menunjuk elemen caption error tersebut
18. Verifikasi atribut `aria-describedby` menunjuk elemen caption yang sama dengan yang tampil, sehingga caption yang dibacakan adalah caption yang terlihat
19. Isi Email dengan format tidak valid lalu klik "Log in"
20. Verifikasi caption "Email format is incorrect" muncul
21. Verifikasi caption yang terunjuk oleh `aria-describedby` adalah caption baru itu, sehingga asosiasi ikut berubah bersama captionnya
22. Isi Email dengan format valid lalu klik "Log in"
23. Verifikasi caption error Email hilang dan `aria-invalid` pada field Email tidak lagi aktif
24. Isi Password kosong lalu klik "Log in"
25. Verifikasi caption "Password must not be empty" muncul di bawah field Password
26. Verifikasi field Password punya `aria-invalid="true"` dan `aria-describedby` yang menunjuk caption miliknya
27. Verifikasi field Email tidak ikut diberi `aria-describedby` ke caption Password, sehingga setiap caption terikat pada field yang benar

### Caption lock diumumkan sebagai alert

28. Isi Email dengan `Fixture.authLoginPassword.users.a11yLockTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD` yang benar
29. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
30. Verifikasi caption lock 15 menit muncul di atas tombol "Log in"
31. Verifikasi elemen caption lock tersebut punya atribut `role="alert"`
32. Verifikasi pendengar accessibility tree mencatat pengumuman caption lock tanpa perlu memindahkan fokus ke caption
33. Verifikasi caption lock 15 menit bukan inline error di bawah field, karena pengumuman harus masuk sebagai alert
34. Verifikasi caption lock tersebut memuat waktu absolut dari server sesuai PRD §4.6
35. Verifikasi `failed_count` dan `lock_until` tidak berubah setelah submit selama lock aktif, sehingga caption yang tampil bukan hasil percobaan baru

## Notes

- Urutan fokus di PRD §4.8 adalah urutan yang harus dipegang. Ketidaksesuaian urutan bukan detail kecil karena menentukan apakah caption error terbaca sebelum atau sesudah user pindah ke field berikutnya.
- `aria-describedby` harus menunjuk elemen caption yang sama persis dengan yang tampil. Kalau caption berganti, asosiasinya ikut berganti. Ini diuji pada langkah 19 sampai 21.
- Caption lock memakai `role="alert"` supaya diumumkan otomatis tanpa memindahkan fokus, karena focus sudah berada di tombol submit ketika banner itu muncul.
- State terkunci dibuat lewat API Global Settings > User dengan `Mode: mock`, bukan dengan mengirim tiga password salah. Itu membuat spec ini deterministik dan tidak bergantung pada urutan spec lain.
- Tidak ada layout mobile di sini. Perilaku layar sentuh dan viewport mobile punya spec sendiri di TC-AUTH-LP-E2E-019.
- Verifikasi dilakukan lewat atribut DOM dan accessibility tree, bukan lewat pemeriksaan visual. Pemeriksaan visual tidak bisa membuktikan `aria-describedby` benar-benar menunjuk caption yang tampil.
- Hook `afterEach` mengembalikan state lock kedua user, sehingga spec ini tidak meninggalkan user terkunci untuk spec lain.