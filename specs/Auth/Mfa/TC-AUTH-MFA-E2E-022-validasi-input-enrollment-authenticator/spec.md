---
id: TC-AUTH-MFA-E2E-022-validasi-input-enrollment-authenticator
title: "Validasi Input Enrollment Authenticator: Kode Kosong, Salah Percobaan 1–4, dan Pembersihan Slot"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-110
  - TC-AUTH-MFA-111
  - TC-AUTH-MFA-112
  - TC-AUTH-MFA-124
coverage:
  web: automated
---
# Validasi Input Enrollment Authenticator: Kode Kosong, Salah Percobaan 1–4, dan Pembersihan Slot

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Vicky Alamsyah` (`vickyalamsyah@qwertysystem.net`) profil FIRST (belum enroll).
- User `Maya Wijaya` (`mayawijaya@qwertysystem.net`) profil FIRST (belum enroll).
- Aplikasi authenticator uji tersedia.

## Test Steps

### Validasi kode verifikasi enrollment kosong atau parsial

1. Buka alur Enrollment Authenticator untuk user `vickyalamsyah@qwertysystem.net`
2. Biarkan kotak digit kosong lalu klik button [Verify]
3. Verifikasi caption error inline tampil di bawah kotak digit: "Code must not be empty" (sesuai V-07 dan NC-12)
4. Masukkan hanya 3 digit (`1`, `2`, `3`) dan klik button [Verify]
5. Verifikasi caption error inline tetap: "Code must not be empty"

### Validasi kode verifikasi enrollment salah pada percobaan 1 s.d. 4

6. Masukkan 6 digit kode salah `000000` lalu klik button [Verify]
7. Verifikasi caption error inline tampil: "Invalid code"
8. Verifikasi pengguna tetap berada di halaman Enrollment Authenticator dan kotak digit dikosongkan (fokus kembali ke kotak 1)
9. Ulangi memasukkan kode salah pada percobaan 2, 3, dan 4
10. Verifikasi pada percobaan 1 sampai 4, halaman tetap berada di Enrollment Authenticator dan enrollment belum aktif

### Penolakan kode enrollment non-numerik yang lolos filter FE

11. Kirim langsung request verifikasi enrollment dengan payload kode non-numerik `12a456` untuk user `mayawijaya@qwertysystem.net`
12. Verifikasi request ditolak, enrollment belum aktif, dan UI menampilkan caption "Code must not be empty"
13. Verifikasi tidak ada entri log yang dicatat (kegagalan enrollment tidak dicatat, sesuai V-07 dan NC-12)

## Notes

- Sesuai keputusan NC-12, caption error untuk kode verifikasi enrollment kosong atau parsial adalah `Code must not be empty`.
- Kegagalan verifikasi pada tahap enrollment tidak dicatat di audit log.
