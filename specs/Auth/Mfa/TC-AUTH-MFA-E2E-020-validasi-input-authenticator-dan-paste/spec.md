---
id: TC-AUTH-MFA-E2E-020-validasi-input-authenticator-dan-paste
title: "Validasi Input Authenticator: Filter Angka, Smart Paste, Kode Kosong, dan Pembersihan Slot"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-09
  - TC-AUTH-MFA-10
  - TC-AUTH-MFA-93
  - TC-AUTH-MFA-94
  - TC-AUTH-MFA-95
  - TC-AUTH-MFA-101
  - TC-AUTH-MFA-102
  - TC-AUTH-MFA-103
  - TC-AUTH-MFA-104
coverage:
  web: automated
---
# Validasi Input Authenticator: Filter Angka, Smart Paste, Kode Kosong, dan Pembersihan Slot

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Farhan Hakim` (`farhanhakim@qwertysystem.net`) profil NEWDEVE.
- User `Intan Permata` (`intanpermata@qwertysystem.net`) profil NEWDEVE.

## Test Steps

### Filter karakter non-angka pada Authenticator Verification

1. Buka form Authenticator Verification untuk user `farhanhakim@qwertysystem.net`
2. Ketik karakter alfabet `A`, `b`, simbol `@`, `$`, dan tanda baca pada kotak 1
3. Verifikasi kotak 1 tetap kosong dan karakter non-angka tidak diizinkan masuk
4. Ketik angka `4` dan verifikasi angka masuk ke kotak 1 serta kursor berpindah ke kotak 2

### Smart paste kode 6 digit dan pembersihan karakter non-digit

5. Salin string `123456` ke clipboard
6. Klik kotak 1 lalu tekan `Ctrl+V`
7. Verifikasi keenam kotak terisi `1`, `2`, `3`, `4`, `5`, `6` dan form TIDAK auto-submit
8. Salin string `89-01 23` ke clipboard
9. Bersihkan kotak, klik kotak 1 lalu tekan `Ctrl+V`
10. Verifikasi karakter spasi dan tanda strip dibuang otomatis sehingga terisi `890123`

### Smart paste mulai dari kotak tengah

11. Bersihkan form, klik kotak 4 lalu tempelkan string 6 digit `654321`
12. Verifikasi hanya digit `6`, `5`, `4` yang masuk ke kotak 4, 5, 6; sisa digit dibuang dan kotak 1, 2, 3 tetap kosong

### Validasi kode TOTP kosong atau parsial

13. Bersihkan seluruh kotak lalu klik button [Login]
14. Verifikasi caption error inline tampil: "Code must not be empty" (sesuai V-05 dan NC-12)
15. Masukkan hanya 2 digit lalu klik button [Login]
16. Verifikasi caption error tetap: "Code must not be empty"

### Reset fokus dan pembersihan kotak saat kode TOTP salah

17. Masukkan 6 digit kode yang salah `999999` lalu klik button [Login]
18. Verifikasi caption error inline tampil: "Invalid code"
19. Verifikasi keenam kotak input otomatis dikosongkan dan fokus kembali ke kotak 1 (sesuai FI-07 dan NC-16)
20. Ketik digit pertama `1` pada kotak 1
21. Verifikasi caption error "Invalid code" dan border merah langsung hilang saat pengetikan ulang dimulai

### Penolakan payload non-numerik yang lolos validasi FE

22. Kirim payload verifikasi dengan nilai non-numerik `12a456` langsung ke backend
23. Verifikasi request ditolak dengan pesan error setara kode kosong ("Code must not be empty")

## Notes

- Sesuai keputusan NC-12, caption error untuk form TOTP kosong atau parsial adalah `Code must not be empty`.
- Sesuai keputusan NC-16, form TOTP mengosongkan slot dan mengembalikan fokus ke kotak 1 saat kode salah.
