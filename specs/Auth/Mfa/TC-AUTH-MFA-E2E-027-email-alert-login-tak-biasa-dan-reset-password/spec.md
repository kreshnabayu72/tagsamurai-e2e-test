---
id: TC-AUTH-MFA-E2E-027-email-alert-login-tak-biasa-dan-reset-password
title: "Template Email Alert Login Tak Biasa, Fallback Lokasi, dan Link Reset Password"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-152
  - TC-AUTH-MFA-153
  - TC-AUTH-MFA-154
  - TC-AUTH-MFA-155
  - TC-AUTH-MFA-156
  - TC-AUTH-MFA-157
coverage:
  web: automated
---
# Template Email Alert Login Tak Biasa, Fallback Lokasi, dan Link Reset Password

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- Browser uji B (device baru).
- User `Farhan Setiawan` (`farhansetiawan@qwertysystem.net`) profil NEWDEVE.
- User `Galang Pratama` (`galangpratama@qwertysystem.net`) profil NEWDEVE.
- User `Hani Oktavia` (`hanioktavia@qwertysystem.net`) profil NEWDEVE.
- Mail-catcher lingkungan uji aktif.
- Mock interceptor email service untuk simulasi kegagalan pengiriman email alert.

## Test Steps

### Email alert dikirim segera saat login tak biasa terdeteksi (sebelum MFA selesai)

1. Buka browser uji B pada halaman `Auth > Login with Password` (`/login`)
2. Masukkan email `farhansetiawan@qwertysystem.net` dan password valid lalu klik [Log in]
3. Halaman berpindah ke `Auth > MFA > Choose Verification Method`
4. Sebelum memilih metode atau memasukkan kode apa pun, segera periksa kotak masuk mail-catcher untuk `farhansetiawan@qwertysystem.net`
5. Verifikasi email alert telah terkirim seketika saat faktor-1 mendeteksi anomali (tidak menunggu penyelesaian faktor-2)

### Verifikasi isi template email alert sesuai spesifikasi

6. Buka pesan email alert di mail-catcher
7. Verifikasi subjek email adalah "TAG Samurai - Unusual Login Attempt Detected"
8. Verifikasi konten email memuat:
   - Nama perangkat / browser (Device info)
   - Lokasi geografis (Kota / Negara)
   - Alamat IP penyerang/pengguna
   - Timestamp waktu kejadian
   - Tombol CTA [Reset Password]

### Tombol [Reset Password] pada email alert membuka formulir reset password

9. Klik tombol [Reset Password] di dalam badan email
10. Verifikasi browser membuka halaman `Auth > Reset Password > Request Reset` (`/reset-password`)
11. Verifikasi field Email pada halaman tersebut otomatis terisi dengan `farhansetiawan@qwertysystem.net`

### Fallback lokasi "Unknown location" saat informasi geo-IP tidak terparse

12. Lakukan login untuk user `galangpratama@qwertysystem.net` dari alamat IP privat atau IP uji tanpa pemetaan kota/negara
13. Periksa email alert yang diterima di mail-catcher
14. Verifikasi bagian lokasi pada email menampilkan fallback teks: "Unknown location" tanpa error rendering

### Kegagalan pengiriman email alert tidak memblokir alur login

15. Konfigurasikan mock untuk mensimulasikan kegagalan pada layanan pengiriman email alert (email provider down / timeout)
16. Lakukan login dengan user `hanioktavia@qwertysystem.net` dari browser uji B
17. Verifikasi halaman Choose Verification Method tetap muncul normal
18. Selesaikan verifikasi faktor-2 Authenticator dengan kode valid
19. Verifikasi login berhasil tuntas ke Portal — Product Hub (pengiriman email alert bersifat asynchronous dan fire-and-forget sehingga tidak memblok proses login pengguna)

### Retry setelah timeout pada faktor-1 tidak menghasilkan email alert ganda

20. Simulasikan network timeout sesaat saat tombol [Log in] ditekan pada faktor-1, lalu lakukan retry klik [Log in]
21. Periksa kotak masuk mail-catcher
22. Verifikasi hanya tepat satu email alert yang dikirimkan (deduplikasi attempt aktif)

## Notes

- Sesuai PRD §9.2 F-AUTHMFA-09, email alert dikirim secara asinkron segera setelah deteksi anomali terjadi.
- Kegagalan antrean email tidak menggagalkan login autentikasi pengguna.
