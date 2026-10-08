---
id: TC-AUTH-MFA-E2E-030-mfa-recovery-dan-admin-reset-authenticator
title: "MFA Recovery: Fallback ke OTP Saat Authenticator Hilang dan Admin Reset Authenticator di GS"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-64
  - TC-AUTH-MFA-75
  - TC-AUTH-MFA-100
  - TC-AUTH-MFA-105
  - TC-AUTH-MFA-175
  - TC-AUTH-MFA-176
  - TC-AUTH-MFA-177
coverage:
  web: automated
---
# MFA Recovery: Fallback ke OTP Saat Authenticator Hilang dan Admin Reset Authenticator di GS

## Prerequisites

- Akun Total Control Global Settings untuk modul User.
- User `Lost Device User` (`lostdev@qwertysystem.net`) yang telah mendaftar Authenticator namun kehilangan perangkat.
- User `Reset Auth User` (`resetauth@qwertysystem.net`) yang telah mendaftar Authenticator aktif.
- User `Reset Pwd User` (`resetpwd@qwertysystem.net`) dengan Authenticator dan trusted device aktif.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Fallback saat Authenticator hilang: Menyelesaikan MFA via OTP Email

1. Buka alur login untuk user `lostdev@qwertysystem.net` yang kehilangan akses aplikasi authenticator-nya
2. Pada halaman Choose Verification Method, pilih opsi "OTP via email" lalu klik [Login]
3. Masukkan kode OTP 6-digit yang diterima di email akun terdaftar
4. Verifikasi verifikasi berhasil dan user dapat login kembali ke Portal — Product Hub tanpa terblokir oleh hilangnya authenticator
5. Ulangi skenario fallback untuk login yang diawali dari Login with OTP

### Reset Authenticator oleh admin Global Settings > User

6. Buka form Authenticator Verification untuk user `resetauth@qwertysystem.net`
7. Di browser admin, buka `Global Settings > User > Detail` dan jalankan aksi [Reset Authenticator]
8. Kembali ke browser user, masukkan kode dari aplikasi authenticator lama lalu klik [Login]
9. Verifikasi verifikasi ditolak dengan caption "Invalid code" (sesuai EC-36)
10. Klik [Use a different method] lalu pilih kembali "Authenticator app"
11. Verifikasi halaman yang terbuka kini adalah `Enrollment Authenticator` (pengguna dibimbing untuk mendaftar ulang)

### Pengaruh Reset Password terhadap status MFA

12. Jalankan alur Reset Password sukses untuk akun user `resetpwd@qwertysystem.net` yang telah memiliki riwayat trusted device dan pendaftaran authenticator aktif
13. Lakukan login pertama kali setelah reset password dari perangkat yang sama
14. Verifikasi login tidak dianggap sebagai login pertama (first-login rule tidak terpicu)
15. Verifikasi status enrollment authenticator maupun trusted device tetap utuh tanpa reset

## Notes

- Fallback ke OTP email adalah mekanisme pemulihan bawaan saat pengguna kehilangan perangkat TOTP.
- Reset Authenticator oleh Admin GS menghapus secret TOTP aktif sehingga user wajib enroll ulang pada login berikutnya.
