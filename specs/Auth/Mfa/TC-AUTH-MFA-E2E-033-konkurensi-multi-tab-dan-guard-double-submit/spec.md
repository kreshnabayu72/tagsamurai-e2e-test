---
id: TC-AUTH-MFA-E2E-033-konkurensi-multi-tab-dan-guard-double-submit
title: "Konkurensi, Balapan Multi-Device/Tab, dan Guard Double-Submit C-2"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-118
  - TC-AUTH-MFA-119
  - TC-AUTH-MFA-137
  - TC-AUTH-MFA-191
  - TC-AUTH-MFA-194
  - TC-AUTH-MFA-195
  - TC-AUTH-MFA-196
coverage:
  web: automated
---
# Konkurensi, Balapan Multi-Device/Tab, dan Guard Double-Submit C-2

## Prerequisites

- Dua konteks browser independen (Device A dan Device B / Tab 1 dan Tab 2).
- User `Race User 1` (`race1@qwertysystem.net`) profil FIRST (belum enroll).
- User `Race User 2` (`race2@qwertysystem.net`) profil NEWDEV.
- User `Race User 3` (`race3@qwertysystem.net`) profil NEWDEVE.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Sesi pre-auth baru menghasilkan Secret Key baru dan membatalkan secret lama

1. Buka sesi enrollment untuk user `race1@qwertysystem.net` pada Browser A dan catat secret key pertama (`Secret-A`)
2. Buka sesi login baru dari Browser B untuk user yang sama hingga mencapai enrollment, dan catat secret key kedua (`Secret-B`)
3. Verifikasi sesuai keputusan NC-07, `Secret-B` berbeda dari `Secret-A`
4. Coba selesaikan verifikasi di Browser A menggunakan kode dari `Secret-A`
5. Verifikasi verifikasi di Browser A ditolak karena secret lama telah digantikan oleh sesi pre-auth baru

### Concurrency dua device: Enrollment yang diverifikasi lebih dulu menang

6. Buka sesi enrollment untuk user `race1@qwertysystem.net` pada Tab A dan Tab B
7. Masukkan kode verifikasi valid pada Tab A lalu klik [Verify] hingga sukses mendarat di Portal — Product Hub
8. Pada Tab B, klik [Verify] dengan kodenya
9. Verifikasi sesuai keputusan NC-07 dan EC-24, verifikasi di Tab B ditolak dengan caption "Invalid code"

### Dua sesi pre-auth bersamaan untuk user dan platform yang sama

10. Buka Tab 1 dan Tab 2 pada browser yang sama untuk user `race2@qwertysystem.net`
11. Pada Tab 1, login hingga mencapai Authenticator Verification
12. Pada Tab 2, lakukan login baru dengan akun yang sama hingga mencapai Choose Verification Method
13. Kembali ke Tab 1, masukkan kode TOTP valid lalu klik [Login]
14. Verifikasi aksi pada Tab 1 ditolak dan dialihkan ke login karena sesi pre-auth lama di-invalidate oleh login baru pada platform yang sama (sesuai EC-34)

### Multi-Tab verifikasi simultan: Tepat satu tab berhasil menyelesaikan login

15. Buka dua tab pada sesi pre-auth yang sama untuk user `race3@qwertysystem.net`
16. Pada Tab 1 buka OTP Verification dan isi kode valid; pada Tab 2 buka Authenticator Verification dan isi kode valid
17. Kirim verifikasi pada kedua tab secara simultan
18. Verifikasi tepat satu tab berhasil mendarat di Product Hub dan tab yang kalah dialihkan ke login

### Concurrency guard: Auto-submit bersamaan dengan klik tombol [Login] pada OTP

19. Buka form OTP Verification, ketik 5 digit pertama kode valid
20. Ketik digit ke-6 dan secara simultan klik tombol [Login] dengan cepat
21. Verifikasi form menonaktifkan tombol dan hanya memproses tepat satu request ke server tanpa error double-submit

### Double-submit guard pada tombol [Login] Authenticator dan [Verify] Enrollment

22. Pada form Authenticator Verification, klik tombol [Login] dua kali dengan sangat cepat
23. Verifikasi tombol langsung disabled pada klik pertama dan hanya satu request yang diproses
24. Pada form Enrollment Authenticator, klik tombol [Verify] dua kali dengan sangat cepat
25. Verifikasi tombol langsung disabled pada klik pertama dan aktivasi hanya diproses satu kali

## Notes

- Menegakkan kontrol konkurensi C-2 (§5.1) dan keputusan NC-07 & NC-18.
- Semua form autentikasi memiliki guard anti-double submit untuk mencegah race condition perbankan/keamanan.
