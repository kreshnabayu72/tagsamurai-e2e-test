---
id: TC-AUTH-MFA-E2E-025-pembatalan-sesi-user-deactivated-dan-deleted
title: "Pembatalan Sesi Real-Time Saat User Di-deactivate atau Dihapus Admin Selama Alur MFA"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-138
  - TC-AUTH-MFA-139
  - TC-AUTH-MFA-140
  - TC-AUTH-MFA-141
  - TC-AUTH-MFA-142
coverage:
  web: automated
---
# Pembatalan Sesi Real-Time Saat User Di-deactivate atau Dihapus Admin Selama Alur MFA

## Prerequisites

- Browser user pada halaman MFA.
- Konteks peramban admin Total Control untuk mengelola akun user di `Global Settings > User`.
- User `Deact User 1` (`deact1@qwertysystem.net`) profil NEWDEV.
- User `Deact User 2` (`deact2@qwertysystem.net`) profil NEWDEV.
- User `Delete User` (`deluser@qwertysystem.net`) profil NEWDEV.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### User di-deactivate saat verifikasi kode dialihkan ke login dengan pesan error

1. Buka alur OTP Verification untuk user `deact1@qwertysystem.net`
2. Di jendela browser admin, ubah status user `deact1@qwertysystem.net` menjadi Inactive (Deactivate User)
3. Kembali ke browser user, masukkan kode OTP valid lalu klik [Login]
4. Verifikasi server memeriksa status user secara real-time dan menolak request
5. Verifikasi sesi pre-auth di-invalidate dan browser dialihkan ke halaman login (`/login`) dengan caption error: "Account is inactive" (sesuai V-09 dan NC-09)

### User dihapus saat verifikasi kode dialihkan ke login tanpa pesan error

6. Buka alur Authenticator Verification untuk user `deluser@qwertysystem.net`
7. Di jendela admin, lakukan aksi Delete User secara permanen
8. Kembali ke browser user, masukkan kode TOTP valid lalu klik [Login]
9. Verifikasi server menolak request dan mengalihkan browser ke `/login` tanpa caption error (sesuai V-10 dan NC-09)

### Pemeriksaan status user saat tombol Resend OTP ditekan

10. Buka alur OTP Verification untuk user `deact2@qwertysystem.net`
11. Tunggu cooldown 60 detik selesai
12. Di browser admin, nonaktifkan akun user tersebut
13. Kembali ke browser user, klik tombol [Resend code]
14. Verifikasi request resend ditolak, email baru tidak dikirim, dan browser dialihkan ke `/login` dengan caption "Account is inactive"

### Pemeriksaan status user saat memilih metode di Choose Verification Method

15. Buka sesi baru untuk user yang kemudian di-deactivate saat masih di Choose Verification Method
16. Klik opsi "OTP via email" lalu klik button [Login]
17. Verifikasi aksi ditolak dan browser dialihkan ke login dengan caption "Account is inactive"

## Notes

- Sesuai keputusan NC-09, seluruh endpoint MFA memvalidasi status user secara real-time.
- User inactive menghasilkan caption `Account is inactive`, sedangkan user deleted dialihkan tanpa caption.
