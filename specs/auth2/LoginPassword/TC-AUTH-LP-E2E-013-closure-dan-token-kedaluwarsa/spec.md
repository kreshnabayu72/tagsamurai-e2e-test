---
id: TC-AUTH-LP-E2E-013-closure-dan-token-kedaluwarsa
title: Penutupan layar Confirm to Continue dan preAuthToken kedaluwarsa
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-25
  - TC-AUTH-LP-26
coverage:
  web: automated
---

# Penutupan layar Confirm to Continue dan preAuthToken kedaluwarsa

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan dua user uji, dibuat lewat API Global Settings > User dan direstore di `afterEach`. Keduanya punya `first_login_at` kosong supaya trigger agreement aktif:
  - `Fixture.authLoginPassword.users.firstLogin` untuk bagian penutupan layar
  - `Fixture.authLoginPassword.users.firstLoginTokenExpiry` untuk bagian token kedaluwarsa
- Password asli kedua user tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di spec maupun fixture.
- `Fixture.authLoginPassword.users.firstLoginTokenExpiry.shortTokenTtl` berisi nilai TTL token yang sengaja dibuat sangat pendek oleh hook, supaya token kedaluwarsa bisa dipancing tanpa menunggu 10 menit sungguhan.
- Hook bisa membaca token confirm-agreement dari session storage atau dari request inspect browser, sehingga kedaluwarsa token bisa dibuktikan dari sisi klien.
- `Fixture.authLoginPassword.captions.agreementRequired` berisi caption error agreement belum dicentang.
- `Fixture.authLoginPassword.captions.tokenExpired` berisi caption kegagalan akibat token kedaluwarsa.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon, termasuk `Consent not given`.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- `Fixture.authLoginPassword.log.errorCodes.tokenExpired` berisi kode `TOKEN_EXPIRED` yang dikembalikan server pada status 422.
- Sesi admin untuk membuka User Log dibuka pada spec ini dan ditutup kembali di akhir spec, sehingga spec ini dapat dijalankan sendiri.
- Hook `afterEach` menghapus token confirm-agreement yang masih tertinggal di browser supaya spec ini tidak meninggalkan preAuthToken menggantung.

## Test Steps

### Tutup layar dan kembali ke halaman Login

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.firstLogin.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
4. Verifikasi browser berpindah ke layar "Confirm to Continue"
5. Verifikasi checkbox agreement tampil dalam keadaan unchecked dan tombol "Continue to Dashboard ➔" tetap enabled
6. Verifikasi jumlah entri di User Log milik `Fixture.authLoginPassword.users.firstLogin` masih 1 dari submit pada langkah 3, sehingga ada pembanding yang jelas
7. Tutup layar lewat tombol close atau kontrol back di browser tanpa sempat mencentang checkbox
8. Verifikasi browser kembali ke halaman `/login` yang penuh
9. Verifikasi field Password dikosongkan
10. Verifikasi checkbox agreement tidak ada di halaman Login, sehingga consent tidak pernah terekam sebagai sudah dicentang
11. Verifikasi token confirm-agreement yang tersisa di browser tidak lagi dipakai, sehingga sesi setengah jadi tidak bisa dilanjutkan di luar layar itu
12. Verifikasi jumlah entri di User Log bertambah satu dari pembanding pada langkah 6
13. Verifikasi entri baru tersebut ber-Status "Failed" dengan Note "Consent not given", sehingga menutup layar diperlakukan sebagai upaya login gagal dan dicatat
14. Verifikasi entri baru itu tercatat pada user yang sama, karena `user_id` sudah ter-resolve dari password benar sehingga tidak ada ambiguitas perusahaan tujuan log
15. Verifikasi jumlah entri di Activity Log > Session juga bertambah satu dengan isi yang sama, sehingga satu attempt hanya menghasilkan satu entri per surface
16. Verifikasi tidak ada entri ber-Status "Success" dari langkah ini, sehingga menutup layar tidak pernah dianggap login berhasil
17. Verifikasi `user_privacy_consent` tidak tersimpan, sehingga consent tidak tercatat hanya karena layar sempat terbuka

### Buka ulang dan selesaikan dari awal

18. Isi ulang Email dengan `Fixture.authLoginPassword.users.firstLogin.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
19. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
20. Verifikasi browser berpindah ke layar "Confirm to Continue" dan checkbox kembali unchecked, sehingga percobaan baru dimulai dari keadaan bersih
21. Centang checkbox lalu klik "Continue to Dashboard ➔"
22. Verifikasi browser berpindah ke layar MFA atau ke Portal — Product Hub, sehingga consent berhasil dipulihkan dari awal
23. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Success" dan Note "Login with password"
24. Verifikasi `user_privacy_consent` tersimpan setelah continue berhasil, sehingga hanya persetujuan eksplisit yang mengaktifkan consent

### Token confirm-agreement kedaluwarsa

25. Isi Email dengan `Fixture.authLoginPassword.users.firstLoginTokenExpiry.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
26. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
27. Verifikasi browser berpindah ke layar "Confirm to Continue"
28. Verifikasi jumlah entri di User Log milik `Fixture.authLoginPassword.users.firstLoginTokenExpiry` masih 1 dari submit pada langkah 26 sebagai pembanding
29. Tunggu dan biarkan TTL dari `Fixture.authLoginPassword.users.firstLoginTokenExpiry.shortTokenTtl` habis tanpa menyentuh kontrol apa pun
30. Verifikasi tidak ada toast sukses yang muncul lebih awal, sehingga layar tidak menandai login sebagai berhasil hanya karena checkbox pernah tampil
31. Verifikasi jumlah entri di User Log tetap sama dengan pembanding pada langkah 28, sehingga kedaluwarsa token dengan sendirinya tidak langsung menulis entri
32. Centang checkbox lalu klik "Continue to Dashboard ➔"
33. Verifikasi request confirm-agreement dikirim ke server, sehingga kegagalan token expired terjadi karena validasi server dan bukan karena gate checkbox di sisi klien
34. Verifikasi response request tersebut berstatus 422 dengan kode "TOKEN_EXPIRED", sehingga kedaluwarsa token dibedakan dari kegagalan agreement lain
35. Verifikasi caption "You need to agree to the Privacy Policy to continue" tidak muncul sebagai penyebab utama, sehingga kegagalan ini bukan karena checkbox belum dicentang
36. Verifikasi pesan yang tampil adalah kegagalan confirm agreement akibat token kedaluwarsa sesuai `Fixture.authLoginPassword.captions.tokenExpired`
37. Verifikasi browser dialihkan ke halaman Login penuh, bukan ke Portal, sehingga proses harus dimulai ulang dari faktor-1
38. Verifikasi field Password dikosongkan pada halaman Login tujuan
39. Verifikasi checkbox agreement tidak tampil lagi di halaman Login tujuan
40. Verifikasi jumlah entri di User Log bertambah satu dari pembanding pada langkah 31
41. Verifikasi entri baru tersebut ber-Status "Failed" dengan Note "Consent not given", sehingga login yang dibatalkan token juga dicatat sebagai consent gagal
42. Verifikasi `user_privacy_consent` tidak tersimpan, sehingga percobaan yang gagal tidak dianggap sudah menyetujui policy

## Notes

- Dua bagian spec ini diuji berurutan pada dua user berbeda, bukan pada satu user yang dipakai dua kali. User pertama dipakai untuk membuktikan bahwa penutupan layar menulis entri gagal dan bahwa percobaan berikutnya masih bisa berhasil dari awal. User kedua dipakai untuk kondisi token kedaluwarsa, karena nilai TTL pendek sudah menempel pada token yang diterbitkan pada percobaan pertama.
- Token confirm-agreement punya masa berlaku 10 menit. Setelah kedaluwarsa, token tidak boleh dipakai ulang dan alur harus diulang dari halaman Login penuh, sama seperti pola session token yang sudah expired di modul ini.
- Kebutuhan token dengan TTL pendek dicatat di Prerequisites sebagai sumber resmi bagi tim FE. Menunggu kedaluwarsa bukan sesuatu yang bisa ditunda dengan wait panjang karena akan membuat suite lambat dan flaky.
- Memverifikasi kedaluwarsa dari sisi klien lewat session storage atau request inspect dipilih karena itu yang bisa diamati tanpa mengakses database.
- Catatan log `Consent not given` dipakai oleh kedua bagian, jadi spec ini sekaligus membuktikan bahwa itu Note kanon untuk batalnya consent, bukan Note khusus satu pemicu saja.
- Bukti pembeda antara dua bagian ini ada di langkah 33 sampai 37. Tanpa assert status 422 dan redirect ke Login penuh, spec ini hanya membuktikan "ada error", dan itu akan lolos walau server mengembalikan 500 atau FE menahan pengguna tetap di layar Confirm to Continue.
- Spec ini sengaja tidak menguji percobaan confirm ulang memakai token yang sama setelah kedaluwarsa, karena perilaku tersebut punya risiko request ganda dan diuji di modul `auth/password-reset` untuk Cookie Auth Token-nya sendiri.
- Sisa token dihapus oleh hook `afterEach`, sehingga spec ini tidak meninggalkan preAuthToken aktif yang bisa dipakai spec lain.