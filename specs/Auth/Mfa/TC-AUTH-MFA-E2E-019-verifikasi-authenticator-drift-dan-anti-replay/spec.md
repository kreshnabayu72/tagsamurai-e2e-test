---
id: TC-AUTH-MFA-E2E-019-verifikasi-authenticator-drift-dan-anti-replay
title: "Verifikasi Authenticator Faktor-2: Drift Window ±1 Step dan Anti-Replay Guard"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-90
  - TC-AUTH-MFA-91
  - TC-AUTH-MFA-96
  - TC-AUTH-MFA-97
  - TC-AUTH-MFA-98
  - TC-AUTH-MFA-99
coverage:
  web: automated
---
# Verifikasi Authenticator Faktor-2: Drift Window ±1 Step dan Anti-Replay Guard

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Nur Rahmawati` (`nurrahmawati@qwertysystem.net`) profil NEWDEVE (Authenticator terdaftar).
- User `Dani Setiawan` (`danisetiawan@qwertysystem.net`) profil NEWDEVE.
- Helper aplikasi authenticator uji (TOTP RFC 6238: SHA-1, 6 digit, periode 30 detik) dengan kemampuan pergeseran step waktu.

## Test Steps

### Verifikasi Authenticator berhasil pasca Login with Password dan Login with OTP

1. Buka halaman `Auth > Login with Password` (`/login`), masukkan email `nurrahmawati@qwertysystem.net` dan password valid lalu klik [Log in]
2. Pada Choose Verification Method, pilih "Authenticator app" lalu klik [Login]
3. Hasilkan kode TOTP valid 6-digit saat ini dari aplikasi authenticator uji
4. Masukkan kode ke dalam form Authenticator Verification dan klik button [Login]
5. Verifikasi verifikasi berhasil dan browser dialihkan langsung ke Portal — Product Hub
6. Buka halaman `Auth > Login with OTP` dengan user yang sama, masukkan email dan selesaikan verifikasi OTP login
7. Verifikasi halaman langsung berpindah ke Authenticator Verification
8. Masukkan kode TOTP valid baru dan klik [Login]
9. Verifikasi verifikasi berhasil langsung menuju Portal — Product Hub

### Drift window ±1 step: Penerimaan kode step sebelumnya dan berikutnya

10. Buka form Authenticator Verification untuk user `danisetiawan@qwertysystem.net`
11. Hasilkan kode TOTP dari step 30 detik yang lalu (step -1)
12. Masukkan kode tersebut dan klik [Login]
13. Verifikasi kode diterima (karena masih berada di dalam drift window -1 step) dan login berhasil
14. Lakukan logout dan buka kembali form Authenticator Verification
15. Hasilkan kode TOTP untuk step 30 detik ke depan (step +1)
16. Masukkan kode tersebut dan klik [Login]
17. Verifikasi kode diterima (di dalam drift window +1 step) dan login berhasil

### Penolakan kode TOTP di luar drift window

18. Hasilkan kode TOTP untuk step 60 detik yang lalu (step -2, di luar batas ±1 step)
19. Masukkan kode tersebut dan klik [Login]
20. Verifikasi sistem menolak kode dengan caption error inline: "Invalid code"

### Anti-Replay Guard: Penolakan kode TOTP yang sudah pernah sukses dipakai

21. Lakukan login baru sampai Authenticator Verification
22. Hasilkan kode TOTP valid untuk step saat ini (`TOTP-X`)
23. Masukkan `TOTP-X` dan klik [Login] hingga login sukses ke Portal — Product Hub
24. Lakukan logout seketika (masih dalam jendela waktu 30 detik yang sama)
25. Login kembali hingga mencapai halaman Authenticator Verification
26. Masukkan kembali kode `TOTP-X` yang sama persis
27. Verifikasi sesuai keputusan NC-06, sistem menolak pemakaian ulang kode dengan caption error: "Invalid code" (Replay Protection aktif)

## Notes

- Parameter TOTP RFC 6238 adalah SHA-1, 6 digit, periode 30 detik, drift window ±1 step (~90 detik).
- Sesuai keputusan NC-06, kode TOTP yang sudah sukses dipakai dicatat dan ditolak bila dipakai ulang di dalam drift window yang sama.
