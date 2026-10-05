---
id: TC-AUTH-RST-E2E-022-submit-dengan-token-tidak-valid
title: Submit password baru saat token tidak lagi berlaku
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-60
  - TC-AUTH-RST-61
  - TC-AUTH-RST-62
  - TC-AUTH-RST-81
coverage:
  web: automated
---

# Submit password baru saat token tidak lagi berlaku

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Tiga user berstatus Activated dan Active di Global Settings > User, dengan password lama yang
  diketahui dan tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di
  fixture. Ketiganya bukan Default User dan bukan akun admin Total Control.
  - `Fixture.authResetPassword.users.activated.email` adalah user untuk kasus token expired.
  - `Fixture.authResetPassword.users.activatedSecondary.email` adalah user untuk kasus token sudah
    dipakai.
  - `Fixture.authResetPassword.users.activatedTertiary.email` adalah user untuk kasus penolakan
    policy dari server.
- `Spectra.env.AUTH_NEW_PASSWORD` adalah satu password baru yang memenuhi seluruh Password Policy dan
  berbeda dari password lama.
- `Spectra.env.AUTH_NEW_PASSWORD_2` dan `Spectra.env.AUTH_NEW_PASSWORD_3` adalah password baru untuk
  user kedua dan ketiga, masing-masing juga memenuhi seluruh Password Policy dan berbeda dari
  password lama user tersebut.
- `Fixture.authResetPassword.tokens.seedExpiredToken` adalah cara membuat token yang statusnya aktif
  tapi sudah melewati masa berlaku.
- `Fixture.authResetPassword.tokens.seedConsumedToken` adalah cara membuat token yang statusnya
  sudah dipakai.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat token aktif yang dipakai
  sebagai pemicu kegagalan submit pada kasus penolakan policy.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tertentu tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset.
- `Mode: mock`. Untuk kasus penolakan policy, spec memakai intercept respons pada endpoint submit
  password baru yang mengembalikan penolakan beserta daftar rule yang gagal. Kemampuan intercept
  disiapkan tim FE dan dicatat di `Fixture.authResetPassword.network.submitPassword`, dan rule
  yang dikembalikan diambil dari `Fixture.authResetPassword.checklist`.
- `Fixture.authResetPassword.logs.surface` adalah daftar dua surface pencatatan, yaitu Global
  Settings > Activity Log > Session dan Global Settings > User > User Log.
- Kemampuan membaca kedua surface log disiapkan tim FE dan dicatat di
  `Fixture.authResetPassword.logs.readable`.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Token expired di tengah proses submit

1. Buat token milik `Fixture.authResetPassword.users.activated.email` yang statusnya expired memakai
   `Fixture.authResetPassword.tokens.seedExpiredToken`
2. Buka tautan reset dari token tersebut sebelum submit memakai
   `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi halaman Setup New Password tampil
4. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD`
5. Isi field Confirm Password dengan nilai yang sama
6. Buat token tersebut kedaluwarsa di sisi server tanpa memuat ulang halaman
7. Klik "Reset Password"
8. Verifikasi submit ditolak dan redirect ke halaman 404 dengan varian Expired
9. Verifikasi caption yang tampil sesuai dengan caption link reset kedaluwarsa dari
    `Fixture.authResetPassword.captions`
10. Verifikasi password user tersebut tidak berubah
11. Verifikasi password lama user tersebut masih dapat dipakai untuk login
12. Verifikasi status token tersebut tetap "expired" dan tidak berubah menjadi "consumed"
13. Verifikasi kedua surface pencatatan masing-masing memiliki satu entri baru dengan Status "Failed"
    dan Note "Reset link expired"

### Token sudah dipakai saat submit

14. Buat token milik `Fixture.authResetPassword.users.activatedSecondary.email` memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
15. Buka tautan reset dari token tersebut di tab pertama memakai
    `Fixture.authResetPassword.tokens.linkForToken`
16. Verifikasi halaman Setup New Password tampil pada tab pertama
17. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD_2`
18. Isi field Confirm Password dengan nilai yang sama
19. Klik "Reset Password" pada tab pertama
20. Verifikasi navigasi ke halaman Password Reset Successful terjadi pada tab pertama
21. Verifikasi password baru user tersebut dapat dipakai untuk login
22. Buka tautan reset yang sama di tab kedua memakai
    `Fixture.authResetPassword.tokens.linkForToken`
23. Isi field Password dengan satu password baru lain yang juga memenuhi seluruh Password Policy
24. Isi field Confirm Password dengan nilai yang sama
25. Klik "Reset Password" pada tab kedua
26. Verifikasi submit ditolak dan redirect ke halaman 404 dengan varian Already Used
27. Verifikasi caption yang tampil sesuai dengan caption link reset sudah dipakai dari
    `Fixture.authResetPassword.captions`
28. Verifikasi password user tersebut tidak berubah lagi, sehingga kredensial dari tab pertama tetap
    berlaku
29. Verifikasi kedua surface pencatatan masing-masing memiliki satu entri baru untuk submit di tab
    kedua dengan Status "Failed" dan Note "Reset link already used"

### Penolakan policy dari server

30. Buat token milik `Fixture.authResetPassword.users.activatedTertiary.email` memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
31. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
32. Verifikasi halaman Setup New Password tampil
33. Aktifkan intercept penolakan pada `Fixture.authResetPassword.network.submitPassword` yang
    mengembalikan daftar rule gagal dari `Fixture.authResetPassword.checklist`
34. Isi field Password dengan `Spectra.env.AUTH_NEW_PASSWORD_3`
35. Isi field Confirm Password dengan nilai yang sama
36. Verifikasi checklist Password Policy menampilkan semua rule sebagai terpenuhi sebelum klik tombol
37. Klik "Reset Password"
38. Verifikasi submit ditolak oleh server
39. Verifikasi caption rule yang gagal tampil dalam warna merah sesuai rule yang dikembalikan server
40. Verifikasi caption yang tampil sesuai dengan daftar rule yang dikembalikan server
41. Verifikasi caption yang tampil bukan caption validasi form, sehingga sumber penolakan jelas
42. Verifikasi tidak ada navigasi dari halaman Setup New Password
43. Verifikasi status token tersebut tetap "active"
44. Verifikasi password user tersebut tidak berubah
45. Verifikasi kedua surface pencatatan masing-masing memiliki satu entri baru dengan Status "Failed"
    dan Note "Password does not meet requirements"
46. Verifikasi nonaktifkan intercept pada `Fixture.authResetPassword.network.submitPassword`

## Notes

- Kasus token expired dibuat dengan membiarkan halaman terbuka dulu, lalu membuat token kedaluwarsa
  sebelum submit. Kalau tokennya sudah expired sejak awal, halaman yang tampil sudah 404 dan submit
  tidak pernah terjadi.
- Kasus token sudah dipakai memakai dua tab dengan link yang sama, karena itu memang cara_status
  token berubah menjadi dipakai di tengah alur.
- Kasus penolakan policy memakai `Mode: mock` karena kondisi itu tidak bisa dipicu dari sisi FE:
  password sudah lolos semua validasi FE, tetapi server menolak. Yang diuji adalah bahwa FE
  menampilkan caption sesuai rule yang dikembalikan server dan tidak salah mengira submit berhasil.
- Token yang ditolak pada kasus pertama dan kedua tidak berubah statusnya, sehingga masih bisa
  dipakai sebagai bukti bahwa penolakan terjadi karena alasan yang benar.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable, tidak
  ditulis di spec maupun fixture.