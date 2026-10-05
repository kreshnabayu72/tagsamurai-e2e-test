---
id: TC-AUTH-MFA-E2E-045-account-status-deactivated-or-deleted-mid-flow
title: Penanganan akun dinonaktifkan atau dihapus admin di tengah proses verifikasi MFA
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-87
  - TC-AUTH-MFA-88
coverage:
  web: automated
---

# Penanganan akun dinonaktifkan atau dihapus admin di tengah proses verifikasi MFA

## Prerequisites

- Mode: FE+BE
- User berada di halaman verifikasi faktor kedua dengan `mfa_session` aktif

## Test Steps

### User Dinonaktifkan (Deactivated) di Tengah Alur
1. Melalui sesi Admin pada aplikasi lain, ubah status user menjadi Inactive (Deactivate)
2. Pada halaman verifikasi MFA user, masukkan kode valid dan submit
3. Verifikasi server mendeteksi status inaktif, membatalkan `mfa_session`, dan me-redirect ke halaman Login
4. Verifikasi di halaman Login muncul pesan peringatan "Your account is inactive" (bukan di halaman MFA)

### User Dihapus (Deleted) di Tengah Alur
5. Buat sesi MFA baru untuk akun lain
6. Melalui sesi Admin, hapus user tersebut (Delete)
7. Coba selesaikan verifikasi faktor kedua
8. Verifikasi `mfa_session` dibatalkan, diredirect ke Login, dan email diperlakukan sebagai belum terdaftar (anti-enumeration)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-45`
- Merepresentasikan `TC-AUTH-MFA-87` dan `TC-AUTH-MFA-88` (FE Ref: `TC-AUTH-MFA-FE-45`).
