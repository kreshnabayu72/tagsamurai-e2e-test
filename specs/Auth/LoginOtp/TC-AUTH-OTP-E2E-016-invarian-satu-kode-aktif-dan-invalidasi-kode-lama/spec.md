---
id: TC-AUTH-OTP-E2E-016-invarian-satu-kode-aktif-dan-invalidasi-kode-lama
title: "Invarian Satu Kode Aktif per User dan Invalidasi Kode Lama saat Terbit Kode Baru"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-52
  - TC-AUTH-OTP-53
  - TC-AUTH-OTP-54
  - TC-AUTH-OTP-64
  - TC-AUTH-OTP-121
  - TC-AUTH-OTP-125
  - TC-AUTH-OTP-141
coverage:
  web: automated
---

# Invarian Satu Kode Aktif per User dan Invalidasi Kode Lama saat Terbit Kode Baru

## Prerequisites

- Belum login dan session kosong.
- User `Kartika Harahap` (`kartikaharahap@qwertysystem.net`) profil BASE.
- User `Budi Kusuma` (`budikusuma@qwertysystem.net`) profil BASE.
- User `Siti Saputra` (`sitisaputra@qwertysystem.net`) profil BASE.
- User `Putri Santoso` (`putrisantoso@qwertysystem.net`) profil BASE.
- User `Dimas Lestari` (`dimaslestari@qwertysystem.net`) profil BASE.
- Mail-catcher aktif untuk memantau kode masuk secara berurutan.
- Akun admin Total Control Global Settings aktif untuk memeriksa entri log.

## Test Steps

### Invalidasi kode pertama saat kode kedua diterbitkan via Resend

1. Buka halaman Request OTP, masukkan `kartikaharahap@qwertysystem.net`, kirim permintaan OTP
2. Catat Kode A dari email pertama yang diterima di mail-catcher
3. Tunggu hingga tombol [Resend code] aktif (setelah 60 detik)
4. Klik [Resend code] untuk menerbitkan Kode B
5. Catat Kode B dari email kedua
6. Pada layar Verify OTP, masukkan Kode A (kode lama)
7. Verifikasi Kode A ditolak dengan caption error "Incorrect verification code. Please try again."
8. Periksa log: tercatat entri "Failed" dengan Note "Incorrect OTP" (atau penanda kode usang pasca-resend)
9. Masukkan Kode B (kode baru)
10. Verifikasi Kode B diterima dan pengguna berhasil dialihkan ke Product Hub

### Invalidasi kode saat Request OTP ulang via Edit Email (email sama)

11. Buka Request OTP untuk `sitisaputra@qwertysystem.net`, kirim kode pertama (Kode X)
12. Pada layar Verify OTP, klik tautan [Edit email]
13. Tanpa mengubah email (tetap `sitisaputra@qwertysystem.net`), centang reCAPTCHA dan klik [Request OTP]
14. Catat kode baru (Kode Y) di mail-catcher
15. Masukkan Kode X (kode lama sebelum edit) ke kotak digit layar Verify OTP
16. Verifikasi Kode X ditolak oleh backend
17. Masukkan Kode Y (kode baru)
18. Verifikasi Kode Y diterima dan login berhasil

### Penolakan kode lintas email (Cross-email token submit)

19. Buka Request OTP untuk `putrisantoso@qwertysystem.net`, catat Kode P
20. Buka Request OTP untuk email berbeda `dimaslestari@qwertysystem.net`, catat Kode D
21. Pada layar Verify OTP milik `dimaslestari@qwertysystem.net`, masukkan Kode P milik `Putri Santoso`
22. Verifikasi sistem menolak kode tersebut sebagai kode salah
23. Verifikasi sistem tidak mengizinkan pertukaran kode antar subjek email yang berbeda
24. Periksa log di Activity Log Session: verifikasi tercatat "Failed" dengan indikasi penolakan kode tidak cocok

## Notes

- TAG Samurai menerapkan invarian ketat: hanya ada TEPAT SATU kode OTP aktif per akun user pada satu waktu.
- Setiap penerbitan kode baru (baik melalui Resend maupun pengajuan ulang Request OTP) secara otomatis membatalkan (invalidate) semua kode OTP yang pernah diterbitkan sebelumnya untuk user tersebut.
