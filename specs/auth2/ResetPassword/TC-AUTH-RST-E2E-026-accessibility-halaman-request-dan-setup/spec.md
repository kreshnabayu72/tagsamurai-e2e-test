---
id: TC-AUTH-RST-E2E-026-accessibility-halaman-request-dan-setup
title: Aksesibilitas halaman permintaan reset dan halaman Setup New Password
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-104
  - TC-AUTH-RST-105
  - TC-AUTH-RST-106
  - TC-AUTH-RST-107
  - TC-AUTH-RST-108
coverage:
  web: automated
---

# Aksesibilitas halaman permintaan reset dan halaman Setup New Password

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- `Mode: mock` untuk simulasi buta warna pada checklist. Kemampuan simulasi buta warna disiapkan tim
  FE dan dicatat di `Fixture.authResetPassword.a11y.colorBlindSimulation`, dengan nilai mode yang
  dipakai diambil dari fixture. Simulasi bisa diwujudkan lewat filter CSS grayscale pada halaman,
  sehingga tidak memerlukan device atau ekstensi browser khusus.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. User ini bukan Default User dan bukan akun
  admin Total Control.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut dengan masa berlaku 24 jam, lewat API Global Settings > User.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.checklist` adalah daftar rule pada checklist beserta labelnya.
- `Fixture.authResetPassword.captions` adalah sumber toast yang dirujuk.
- Nilai token hanya dibaca lewat helper dan tidak ditulis di spec maupun fixture.

## Test Steps

### Urutan fokus keyboard pada halaman permintaan

1. Buka halaman Reset Password di browser
2. Muat ulang halaman supaya fokus berada di awal dokumen
3. Tekan Tab berulang kali sambil membaca urutan fokus
4. Verifikasi urutan fokus pertama adalah field Email
5. Verifikasi urutan fokus berikutnya adalah widget reCAPTCHA
6. Verifikasi urutan fokus berikutnya adalah tombol "Reset Password"
7. Verifikasi urutan fokus terakhir adalah link "Log in with password"
8. Verifikasi setiap elemen fokus menampilkan indikator fokus yang terlihat
9. Verifikasi tidak ada elemen fokus yang terlewat atau muncul dua kali
10. Verifikasi urutan fokus tidak berubah setelah field Email diisi dan dikosongkan kembali

### Urutan fokus keyboard pada halaman Setup New Password

11. Buat satu token reset aktif milik
    `Fixture.authResetPassword.users.activated.email` memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
12. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
13. Verifikasi halaman Setup New Password tampil
14. Muat ulang halaman supaya fokus berada di awal dokumen
15. Tekan Tab berulang kali sambil membaca urutan fokus
16. Verifikasi urutan fokus pertama adalah field Password
17. Verifikasi urutan fokus berikutnya adalah tombol ikon mata pada field Password
18. Verifikasi urutan fokus berikutnya adalah field Confirm Password
19. Verifikasi urutan fokus berikutnya adalah tombol ikon mata pada field Confirm Password
20. Verifikasi urutan fokus terakhir adalah tombol "Reset Password"
21. Verifikasi setiap elemen fokus menampilkan indikator fokus yang terlihat
22. Verifikasi tidak ada elemen fokus yang terlewat atau muncul dua kali

### Ikon mata dapat dioperasikan dengan keyboard

23. Isi field Password dan field Confirm Password dengan satu nilai yang memenuhi seluruh rule
24. Berikan fokus ke tombol ikon mata pada field Password memakai tombol Tab
25. Tekan tombol Enter
26. Verifikasi teks pada field Password menjadi terlihat
27. Berikan fokus ke tombol ikon mata pada field Confirm Password memakai tombol Tab
28. Tekan tombol Space
29. Verifikasi teks pada field Confirm Password menjadi terlihat
30. Verifikasi ikon mata pada field yang lain tidak ikut berubah, sehingga keduanya dapat
    dioperasikan secara independen
31. Verifikasi atribut label pada ikon mata adalah "Show password" saat tersembunyi dan
    "Hide password" saat terlihat
32. Verifikasi nilai pada kedua field tidak hilang saat ikon diklik lewat keyboard

### Checklist tidak hanya bergantung pada warna

33. Aktifkan `Fixture.authResetPassword.a11y.colorBlindSimulation` pada halaman
34. Verifikasi seluruh halaman tetap terbaca secara utuh tanpa kehilangan elemen
35. Isi field Password dengan satu nilai yang memenuhi sebagian rule
36. Verifikasi baris checklist yang belum terpenuhi tetap dapat dibedakan dari yang sudah terpenuhi
37. Verifikasi setiap baris checklist memiliki penanda selain warna, misalnya ikon atau bentuk
38. Verifikasi status setiap baris checklist tetap dapat dibaca lewat teksnya, bukan hanya lewat
    warna
39. Verifikasi caption panjang maksimum, ketika tampil, juga dapat dibaca tanpa bergantung pada warna
40. Verifikasi setiap caption error yang tampil memiliki penanda selain warna
41. Nonaktifkan `Fixture.authResetPassword.a11y.colorBlindSimulation`

### Pengumuman toast untuk pembaca layar

42. Isi field Email dengan `Fixture.authResetPassword.users.activated.email`
43. Klik "Reset Password" tanpa menyelesaikan reCAPTCHA supaya toast error muncul
44. Verifikasi atribut pengumuman pada toast adalah "polite"
45. Verifikasi toast error tetap tampil selama sekitar lima detik
46. Verifikasi toast error hilang setelah durasinya habis
47. Selesaikan reCAPTCHA lalu klik "Reset Password" supaya toast sukses muncul
48. Verifikasi toast sukses tampil selama sekitar tiga detik
49. Verifikasi toast sukses hilang setelah durasinya habis
50. Verifikasi tidak ada toast yang muncul bersamaan dalam waktu yang sangat berdekatan
51. Verifikasi toast tidak menutupi isi halaman atau memblokir elemen fokus

## Notes

- TC-AUTH-RST-107 berstatus `Manual Only` di TC granular. Sesuai e2e-conventions.md bagian 2 label
  tersebut bukan alasan mengeluarkan TC, jadi TC ini tetap masuk spec dan disimulasikan lewat filter
  grayscale yang dicatat di Prerequisites.
- Durasi toast pada langkah 45 dan 48 dibaca dari fixture `Fixture.authResetPassword.captions`
  sebagai konfirmasi perkiraan, bukan angka eksak. Yang diuji adalah toast punya dua durasi yang
  berbeda dan toast sukses lebih pendek.
- Atribut pengumuman toast diperiksa langsung pada elemennya, bukan lewat perilaku pembaca layar,
  karena yang terakhir sulit diotomasikan tanpa alat pembaca layar sungguhan.
- Urutan fokus diuji pada kedua halaman karena keduanya punya komposisi elemen berbeda, dan urutan
  yang benar di satu halaman tidak menjamin benar di halaman lain.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.