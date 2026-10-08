---
id: TC-AUTH-MFA-E2E-024-ttl-sesi-pre-auth-dan-navigasi-browser
title: "TTL Absolut Sesi Pre-Auth 10 Menit dan Dampak Navigasi Reload/Back Browser"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-125
  - TC-AUTH-MFA-126
  - TC-AUTH-MFA-127
  - TC-AUTH-MFA-128
  - TC-AUTH-MFA-136
coverage:
  web: automated
---
# TTL Absolut Sesi Pre-Auth 10 Menit dan Dampak Navigasi Reload/Back Browser

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Putra Kencana` (`putrakencana@qwertysystem.net`) profil NEWDEVE.
- User `Queen Anggun` (`queenanggun@qwertysystem.net`) profil NEWDEV.
- User `Rendi Pratama` (`rendipratama@qwertysystem.net`) profil NEWDEV.
- User `Santi Maulina` (`santimaulina@qwertysystem.net`) profil FIRST.
- User `Cindy Oktavia` (`cindyoktavia@qwertysystem.net`) profil NEWDEVE.
- Kemampuan manipulasi waktu server (time-travel) untuk pengujian TTL 10 menit.

## Test Steps

### TTL sesi pre-auth habis (10 menit) mengalihkan ke halaman login pada aksi berikutnya

1. Buka alur Authenticator Verification untuk user `putrakencana@qwertysystem.net`
2. Simulasikan waktu berlalu 10 menit 30 detik sejak faktor-1 berhasil
3. Masukkan kode TOTP valid pada form lalu klik button [Login]
4. Verifikasi aksi ditolak dan browser langsung dialihkan ke halaman login (`/login`) tanpa pesan error
5. Verifikasi tidak ada sesi penuh yang terbentuk

### Sesi pre-auth habis saat memilih metode mengalihkan ke login tanpa kirim email

6. Buka halaman Choose Verification Method untuk user `queenanggun@qwertysystem.net`
7. Simulasikan waktu berlalu 10 menit 30 detik
8. Pilih opsi "OTP via email" lalu klik button [Login]
9. Verifikasi browser langsung dialihkan ke halaman login tanpa caption error
10. Verifikasi tidak ada email OTP yang dikirimkan ke kotak masuk pengguna

### TTL sesi pre-auth bersifat absolut: Resend dan ganti metode tidak memperpanjangnya

11. Buka alur OTP Verification untuk user `rendipratama@qwertysystem.net`
12. Pada menit ke-4, klik [Use a different method]
13. Kembali ke "OTP via email" dan lakukan [Resend code] pada menit ke-8
14. Simulasikan waktu mencapai 10 menit 30 detik sejak login faktor-1 awal
15. Masukkan kode OTP yang masih berumur 2 menit
16. Verifikasi aksi tetap ditolak dan browser dialihkan ke halaman login (TTL 10 menit sesi pre-auth bersifat absolut dan tidak diperpanjang oleh resend atau navigasi)

### Sesi pre-auth habis pada form enrollment mengalihkan ke login

17. Buka form enrollment untuk user `santimaulina@qwertysystem.net`
18. Simulasikan waktu melewati 10 menit lalu klik [Verify]
19. Verifikasi browser dialihkan ke `/login` dan enrollment tidak tersimpan

### Pengaruh reload (F5) dan tombol Back browser pada halaman MFA

20. Buka halaman Authenticator Verification untuk user `cindyoktavia@qwertysystem.net`
21. Tekan tombol F5 (reload)
22. Verifikasi halaman tetap berada di Authenticator Verification dengan kotak digit kosong dan sesi pre-auth tetap valid
23. Tekan tombol Back browser
24. Verifikasi halaman kembali ke `Auth > MFA > Choose Verification Method` tanpa membatalkan sesi pre-auth

## Notes

- Sesuai `mfa.md` §9.2 F-AUTHMFA-01, TTL sesi pre-auth adalah 10 menit absolut sejak faktor-1 lolos.
- Sesuai keputusan NC-18, reload halaman mempertahankan sesi dan tombol Back mengembalikan ke langkah sebelumnya tanpa merusak sesi.
