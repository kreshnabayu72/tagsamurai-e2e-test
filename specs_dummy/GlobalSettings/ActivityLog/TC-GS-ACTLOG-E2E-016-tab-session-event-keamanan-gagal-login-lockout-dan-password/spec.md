---
id: TC-GS-ACTLOG-E2E-016-tab-session-event-keamanan-gagal-login-lockout-dan-password
title: "Tab Session: Event Keamanan Login Gagal Bad Credentials, Account Locked, Client Suspended, dan Sesi Password"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-42
  - TC-GS-ACTLOG-43
  - TC-GS-ACTLOG-44
  - TC-GS-ACTLOG-46
  - TC-GS-ACTLOG-47
coverage:
  web: automated
---

# Tab Session: Event Keamanan Login Gagal Bad Credentials, Account Locked, Client Suspended, dan Sesi Password

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log uji untuk: kegagalan password, penguncian akun, login pada tenant suspended, alur reset password, dan change password

## Test Steps

### Login Gagal: Bad Credentials
1. Buka Tab Session, filter Activity = 'Login'.
2. Cari entri kegagalan login dengan kredensial salah.
3. Verifikasi kolom Activity 'Login', Status 'Failed', dan Note memuat 'Bad credentials' atau alasan kegagalan yang sesuai.
### Login Gagal: Account Locked
4. Cari entri pengguna yang terblokir setelah 5 kali gagal memasukkan password.
5. Verifikasi baris menampilkan Activity 'Login', Status 'Failed', dan Note 'Account locked' atau batas percobaan terlampaui.
### Login Gagal: Client Suspended
6. Cari entri upaya login pada Client yang berstatus ditangguhkan (Suspended/Expired).
7. Verifikasi Activity 'Login', Status 'Failed', dan Note mencantumkan indikasi entitas tidak aktif.
### Sesi Reset Password & Change Password
8. Cari entri sesi permohonan reset password melalui tautan email.
9. Verifikasi tercatat di Tab Session dengan Activity 'Reset Password'.
10. Cari entri pengubahan password mandiri di profil akun pengguna.
11. Verifikasi tercatat di Tab Session dengan Activity 'Change Password' dan Status 'Success'.

## Notes

- Seluruh kegagalan autentikasi dan mutasi kredensial dicatat secara terperinci untuk kebutuhan forensik keamanan.
