---
id: TC-AUTH-MFA-E2E-028-audit-log-mutasi-status-sukses-dan-gagal
title: "Audit Log: Pencatatan Mutasi Status Gagal Faktor-2, Catatan Faktor-1, dan Penundaan Success"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-158
  - TC-AUTH-MFA-159
  - TC-AUTH-MFA-160
  - TC-AUTH-MFA-161
  - TC-AUTH-MFA-162
  - TC-AUTH-MFA-163
  - TC-AUTH-MFA-164
  - TC-AUTH-MFA-165
  - TC-AUTH-MFA-166
  - TC-AUTH-MFA-178
  - TC-AUTH-MFA-207
coverage:
  web: automated
---
# Audit Log: Pencatatan Mutasi Status Gagal Faktor-2, Catatan Faktor-1, dan Penundaan Success

## Prerequisites

- Akun Total Control Global Settings untuk mengakses `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- User `Log Tester 1` (`logtester1@qwertysystem.net`) profil NEWDEV.
- User `Log Tester 2` (`logtester2@qwertysystem.net`) profil NEWDEVE.
- User `Wulan Wijaya` (`wulanwijaya@qwertysystem.net`) profil NEWDEV.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Pencatatan mutasi kegagalan faktor-2 OTP di kedua surface log

1. Pada alur OTP Verification untuk user `logtester1@qwertysystem.net`:
   - Lakukan submit kode kosong: verifikasi baris tercatat dengan Status `Failed`, Note `Empty OTP`
   - Lakukan submit kode salah: verifikasi baris tercatat dengan Status `Failed`, Note `Incorrect OTP`
   - Lakukan submit kode expired (>5 menit): verifikasi baris tercatat dengan Status `Failed`, Note `OTP expired`
   - Lakukan submit setelah email akun diganti di GS: verifikasi baris tercatat dengan Status `Failed`, Note `OTP invalid — email changed`

### Pencatatan mutasi kegagalan faktor-2 Authenticator di kedua surface log

2. Pada alur Authenticator Verification untuk user `logtester2@qwertysystem.net`:
   - Lakukan submit kode kosong: verifikasi baris tercatat dengan Status `Failed`, Note `Empty OTP`
   - Lakukan submit kode salah: verifikasi baris tercatat dengan Status `Failed`, Note `Incorrect OTP`
   - Lakukan submit kode TOTP yang sudah pernah dipakai sukses di dalam drift window: verifikasi baris tercatat dengan Status `Failed`, Note `Incorrect OTP`

### Pencatatan percobaan salah ke-5: OTP/TOTP dicatat Failed, Enrollment tidak dicatat (V-18 & V-19)

3. Pada alur OTP Verification untuk user `wulanwijaya@qwertysystem.net`:
   - Masukkan kode salah 5 kali berturut-turut hingga sesi pre-auth di-invalidate dan browser dialihkan ke `/login`
   - Buka `Global Settings > Activity Log > Session` sebagai Total Control Global Settings
   - Verifikasi tepat 5 entri `Failed` baru tercatat untuk user tersebut, dengan entri ke-5 mencatat Note `Incorrect OTP` (sesuai PRD §9.8 V-18)
4. Pada sesi baru alur Enrollment Authenticator untuk user yang sama:
   - Masukkan kode verifikasi enrollment salah 5 kali berturut-turut hingga sesi hangus dan dialihkan ke `/login`
   - Periksa kembali `Global Settings > Activity Log > Session`
   - Verifikasi TIDAK ADA entri log `Failed` baru yang ditulis untuk percobaan enrollment (sesuai PRD §9.8 V-19 dan `auth-foundation.md` §10)

### Pencatatan mutasi sukses login final mengikuti Note faktor pertama

5. Selesaikan verifikasi MFA sukses untuk login yang diawali Login with Password
   - Verifikasi baris tercatat dengan Activity `Login`, Status `Success`, dan Note `Login with password`
6. Selesaikan verifikasi MFA sukses untuk login yang diawali Login with OTP
   - Verifikasi baris tercatat dengan Activity `Login`, Status `Success`, dan Note `Login with OTP`

### Konsumsi sesi pre-auth dan penundaan pencatatan Success ke faktor-2

7. Buka `Global Settings > Activity Log > Session` sebagai Total Control Global Settings
8. Lakukan login faktor-1 (password) yang memicu MFA
9. Verifikasi pada saat faktor-1 lolos dan dialihkan ke MFA, TIDAK ADA baris log `Success` yang ditulis
10. Selesaikan verifikasi faktor-2 hingga login tuntas
11. Verifikasi tepat satu baris log `Success` dengan Note `Login with password` baru ditulis setelah faktor-2 berhasil

## Notes

- Sesuai `AUTHMFA-LOGIC-04a` dan PRD §9.8, login final via MFA dicatat dengan Note yang mencerminkan faktor pertama.
- Sesuai PRD §9.8 V-18 dan V-19, percobaan salah ke-5 pada OTP/TOTP tetap dicatat Failed sebelum sesi di-invalidate, sedangkan kegagalan enrollment tidak pernah dicatat.
- Faktor-1 tidak mencatat status Success jika MFA terpicu; pencatatan Success ditunda hingga faktor-2 selesai.
