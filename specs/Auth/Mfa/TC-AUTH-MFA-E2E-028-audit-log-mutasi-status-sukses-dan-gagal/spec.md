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
coverage:
  web: automated
---
# Audit Log: Pencatatan Mutasi Status Gagal Faktor-2, Catatan Faktor-1, dan Penundaan Success

## Prerequisites

- Akun Total Control Global Settings untuk mengakses `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- User `Log Tester 1` (`logtester1@qwertysystem.net`) profil NEWDEV.
- User `Log Tester 2` (`logtester2@qwertysystem.net`) profil NEWDEVE.
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

### Pencatatan mutasi sukses login final mengikuti Note faktor pertama

3. Selesaikan verifikasi MFA sukses untuk login yang diawali Login with Password
   - Verifikasi baris tercatat dengan Activity `Login`, Status `Success`, dan Note `Login with password`
4. Selesaikan verifikasi MFA sukses untuk login yang diawali Login with OTP
   - Verifikasi baris tercatat dengan Activity `Login`, Status `Success`, dan Note `Login with OTP`

### Konsumsi sesi pre-auth dan penundaan pencatatan Success ke faktor-2

5. Buka `Global Settings > Activity Log > Session` sebagai Total Control Global Settings
6. Lakukan login faktor-1 (password) yang memicu MFA
7. Verifikasi pada saat faktor-1 lolos dan dialihkan ke MFA, TIDAK ADA baris log `Success` yang ditulis
8. Selesaikan verifikasi faktor-2 hingga login tuntas
9. Verifikasi tepat satu baris log `Success` dengan Note `Login with password` baru ditulis setelah faktor-2 berhasil

## Notes

- Sesuai `AUTHMFA-LOGIC-04a` dan PRD §9.8, login final via MFA dicatat dengan Note yang mencerminkan faktor pertama.
- Faktor-1 tidak mencatat status Success jika MFA terpicu; pencatatan Success ditunda hingga faktor-2 selesai.
