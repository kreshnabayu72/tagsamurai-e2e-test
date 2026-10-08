---
id: TC-AUTH-MFA-E2E-034-security-defense-token-tampering
title: "Defense-in-Depth: Proteksi Token Pre-Auth, One-Time Use, dan Pemisahan Purpose OTP"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-188
  - TC-AUTH-MFA-189
  - TC-AUTH-MFA-190
  - TC-AUTH-MFA-206
  - TC-AUTH-MFA-210
coverage:
  web: automated
---
# Defense-in-Depth: Proteksi Token Pre-Auth, One-Time Use, dan Pemisahan Purpose OTP

## Prerequisites

- Client HTTP untuk eksekusi direct API requests.
- Akun Total Control Global Settings untuk memeriksa Activity Log Session.
- User `Tamper User` (`tamper@qwertysystem.net`) berstatus Activated dan Active.
- User `Wulan Wijaya` (`wulanwijaya@qwertysystem.net`) profil NEWDEV.
- User `Dewi Anjani` (`dewianjani@qwertysystem.net`) profil NEWDEV.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Penolakan request verifikasi langsung tanpa preAuthToken sah

1. Kirim request HTTP POST langsung ke endpoint verifikasi faktor-2 MFA (`/auth/mfa/otp/verify`) dengan parameter token pre-auth acak/palsu
2. Verifikasi backend menolak request dengan status HTTP 401/403 dan tidak ada sesi web yang terbentuk
3. Ulangi penyerangan serupa ke endpoint `/auth/mfa/authenticator/verify`
4. Verifikasi request ditolak tanpa pemrosesan verifikasi kode

### Penolakan pemakaian ulang token pre-auth yang sudah dikonsumsi (One-Time Use Token)

5. Jalankan alur login normal dengan user `tamper@qwertysystem.net` dan catat `preAuthToken` yang diterbitkan
6. Selesaikan verifikasi faktor-2 secara sah hingga mendarat di Portal — Product Hub
7. Ambil `preAuthToken` yang baru saja dikonsumsi tersebut dan tembakkan kembali ke endpoint verifikasi melalui direct HTTP request
8. Verifikasi backend menolak penggunaan token yang telah dikonsumsi (Single-use Token Guard aktif)

### Pemisahan Purpose kode OTP: Penolakan kode Login with OTP pada faktor-2 MFA (TC-206, EC-41 & V-02)

9. Buka tab A pada `Auth > Login with OTP` (`/login/otp`), minta kode OTP untuk `wulanwijaya@qwertysystem.net`, dan catat kodenya dari mail-catcher (`purpose = 'login'`)
10. Di tab B, lakukan login via password dengan akun yang sama hingga mencapai halaman `Auth > MFA > OTP Verification`
11. Masukkan kode OTP login dari langkah 9 ke dalam form OTP Verification MFA (`purpose = 'mfa'`)
12. Verifikasi sesuai keputusan NC-19 dan PRD §9.4.2 EC-41, verifikasi ditolak dengan caption inline "Invalid code" dan kotak digit otomatis dikosongkan
13. Verifikasi hitungan percobaan salah sesi pre-auth bertambah 1
14. Buka `Global Settings > Activity Log > Session` sebagai admin Total Control
15. Verifikasi tepat 1 entri baru tercatat dengan Activity `Login`, Status `Failed`, dan Note `Incorrect OTP` (sesuai PRD §9.8 V-02)

### Penolakan kode OTP faktor-2 MFA pada alur Login with OTP (TC-210, kebalikan EC-41 & V-02)

16. Pada tab A, buka halaman `Auth > Login with Password` dan login dengan user `dewianjani@qwertysystem.net` hingga mencapai halaman `Auth > MFA > Choose Verification Method`
17. Pilih opsi "OTP via email" dan klik [Login] hingga halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 (`purpose = 'mfa'`) terkirim
18. Catat 6 digit kode OTP faktor-2 tersebut dari mail-catcher tanpa memasukkannya di tab A
19. Di tab B, buka alur `Auth > Login with OTP` (`/login/otp`), minta kode OTP login untuk `dewianjani@qwertysystem.net`, hingga mencapai halaman Verify OTP (`purpose = 'login'`)
20. Masukkan kode OTP faktor-2 MFA dari langkah 18 ke dalam kotak digit Verify OTP alur Login with OTP
21. Verifikasi backend menolak verifikasi: caption error "Invalid code" muncul di bawah kotak digit dan tidak ada sesi web yang dibuat
22. Buka `Global Settings > Activity Log > Session` sebagai admin Total Control
23. Verifikasi tepat 1 entri baru tercatat dengan Activity `Login`, Status `Failed`, dan Note `Incorrect OTP`

## Notes

- Sesuai PRD §9.3, §9.4.2 EC-41, dan keputusan NC-19, kode OTP dibatasi secara ketat oleh kolom database `purpose`.
- Pemisahan purpose berlaku dua arah: kode dari alur Login with OTP (`purpose='login'`) ditolak pada verifikasi faktor-2 MFA (`TC-206`), dan kode faktor-2 MFA (`purpose='mfa'`) ditolak pada verifikasi Login with OTP (`TC-210`). Keduanya dicatat sebagai Failed `Incorrect OTP`.
- Token pre-auth bersifat sekali pakai (one-time use) dan hangus seketika setelah sesi login final diterbitkan.

