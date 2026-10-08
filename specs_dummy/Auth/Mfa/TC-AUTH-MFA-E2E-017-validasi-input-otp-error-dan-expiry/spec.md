---
id: TC-AUTH-MFA-E2E-017-validasi-input-otp-error-dan-expiry
title: "Validasi Input OTP: Kode Kosong, Salah, Expired >5 Menit, dan Kode Usang Pasca-Resend"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-70
  - TC-AUTH-MFA-71
  - TC-AUTH-MFA-72
  - TC-AUTH-MFA-73
  - TC-AUTH-MFA-74
  - TC-AUTH-MFA-76
  - TC-AUTH-MFA-86
coverage:
  web: automated
---
# Validasi Input OTP: Kode Kosong, Salah, Expired >5 Menit, dan Kode Usang Pasca-Resend

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Bambang Pamungkas` (`bambang@qwertysystem.net`) profil NEWDEV.
- User `Cici Farida` (`cicifarida@qwertysystem.net`) profil NEWDEV.
- User `Dodi Sudrajat` (`dodisudrajat@qwertysystem.net`) profil NEWDEV.
- Mail-catcher lingkungan uji aktif.
- Kemampuan manipulasi waktu server (time-travel) untuk pengujian batas 5 menit.

## Test Steps

### Validasi submit kode OTP kosong atau parsial

1. Buka alur OTP Verification untuk user `bambang@qwertysystem.net`
2. Biarkan keenam kotak digit kosong lalu klik button [Login]
3. Verifikasi caption error inline tampil di bawah kotak digit: "OTP must not be empty"
4. Isi hanya 3 digit pertama (`1`, `2`, `3`) dan biarkan kotak 4, 5, 6 kosong lalu klik button [Login]
5. Verifikasi caption error inline tetap "OTP must not be empty" dan kotak digit tidak dikosongkan

### Validasi kode OTP salah dan pembersihan kotak digit (Reset Focus)

6. Ketik 6 digit kode yang salah `000000`
7. Verifikasi sistem memicu verifikasi dan server menolak dengan caption error: "Invalid code"
8. Verifikasi keenam kotak digit otomatis dikosongkan dan fokus kursor kembali ke kotak 1 (sesuai FI-07 dan NC-16)
9. Ketik digit pertama `5` pada kotak 1
10. Verifikasi caption error "Invalid code" dan border merah (invalid state) seketika hilang saat digit pertama diketik ulang

### Validasi batas waktu masa berlaku OTP (TTL 5 Menit)

11. Buka sesi OTP Verification untuk user `cicifarida@qwertysystem.net` dan catat kode OTP yang diterima di email
12. Simulasikan waktu server maju 4 menit (kode berumur 4 menit, masih dalam batas <5 menit)
13. Masukkan kode OTP tersebut pada form
14. Verifikasi kode diterima dan verifikasi berhasil menuju Portal — Product Hub
15. Buka sesi baru untuk user `dodisudrajat@qwertysystem.net`, simulasikan waktu server maju 5 menit 10 detik (>5 menit)
16. Masukkan kode OTP yang sebelumnya dikirim
17. Verifikasi sistem menolak kode dengan caption error: "OTP expired"

### Validasi penolakan kode OTP lama setelah tombol Resend ditekan

18. Buka sesi OTP Verification baru, catat kode OTP pertama (`OTP-A`)
19. Tunggu hitung mundur 60 detik selesai lalu klik tombol [Resend code]
20. Catat kode OTP baru yang dikirimkan ke email (`OTP-B`)
21. Masukkan kode lama `OTP-A` ke dalam kotak digit
22. Verifikasi sesuai NC-15, kode lama `OTP-A` ditolak dengan caption error: "Invalid code" (kode lama otomatis tidak berlaku setelah resend)
23. Masukkan kode baru `OTP-B` dan verifikasi login berhasil

### Penolakan kode non-numerik yang lolos validasi klien

24. Melalui interception request, kirim payload OTP yang berisi karakter non-numerik `12a456`
25. Verifikasi server menolak request dan UI menampilkan caption "OTP must not be empty" (diperlakukan setara kode kosong)

## Notes

- Sesuai `mfa.md` §6 V-01 s.d. V-03 dan keputusan NC-12 & NC-15, kode salah menghasilkan caption `Invalid code`, kode expired menghasilkan `OTP expired`, dan kode kosong menghasilkan `OTP must not be empty`.
- Pada kesalahan kode atau expired, kotak input di-clear dan fokus dikembalikan ke kotak 1.
