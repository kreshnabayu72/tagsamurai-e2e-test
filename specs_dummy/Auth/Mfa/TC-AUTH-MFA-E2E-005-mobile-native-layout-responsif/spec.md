---
id: TC-AUTH-MFA-E2E-005-mobile-native-layout-responsif
title: "Tampilan Mobile Native Android: Keypad Numerik, Autofokus, dan Penskalaan Responsif QR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-17
  - TC-AUTH-MFA-18
coverage:
  mobile: automated
---
# Tampilan Mobile Native Android: Keypad Numerik, Autofokus, dan Penskalaan Responsif QR

## Prerequisites

- Perangkat uji mobile Android (atau emulator) dengan aplikasi TAG Samurai terpasang.
- Aplikasi dalam keadaan publik (tanpa sesi aktif).
- User `Dewi Santoso` (`dewisantoso@qwertysystem.net`) profil FIRST.
- User `Rizky Santoso` (`rizkysantoso@qwertysystem.net`) profil FIRST.

## Test Steps

### Keypad numerik dan autofokus kotak 1 di mobile

1. Buka aplikasi mobile TAG Samurai pada perangkat Android
2. Masukkan kredensial `dewisantoso@qwertysystem.net` dan password valid lalu klik [Log in]
3. Pada halaman Choose Verification Method di mobile, pilih "OTP via email" dan tap [Login]
4. Verifikasi halaman berpindah ke OTP Verification dengan card mengisi lebar layar secara proporsional
5. Verifikasi fokus kursor otomatis berada di kotak input digit 1
6. Verifikasi keyboard perangkat yang muncul secara otomatis adalah keypad numerik (hanya angka 0–9)
7. Verifikasi tombol aksi utama [Login] dan [Use a different method] disematkan di bagian bawah layar secara ergonomis

### Penskalaan responsif QR code dan salin secret key manual di mobile

8. Login menggunakan user `rizkysantoso@qwertysystem.net` pada aplikasi mobile
9. Pilih opsi "Authenticator app" dan tap [Login] untuk membuka halaman Enrollment Authenticator
10. Verifikasi gambar QR code diskalakan proporsional terhadap lebar layar mobile tanpa terpotong atau menimbulkan horizontal scrolling
11. Verifikasi string secret key teks monospace tampil di bawah QR code
12. Tap tombol [Copy key]
13. Verifikasi teks rahasia berhasil tersalin ke clipboard sistem Android untuk input manual ke aplikasi authenticator pada perangkat yang sama

## Notes

- Sesuai PRD §4.6, antarmuka mobile ditujukan untuk aplikasi native Android.
- Pada perangkat mobile, pengguna tidak dapat memindai QR code di layarnya sendiri sehingga fungsi [Copy key] menjadi jalur wajib utama.
