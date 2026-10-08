---
id: TC-AUTH-OTP-E2E-022-handoff-mfa-authenticator-dan-login-alert
title: "Handoff MFA Authenticator Langsung Pasca-OTP dan Pengiriman Login Alert"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-112
  - TC-AUTH-OTP-113
  - TC-AUTH-OTP-114
  - TC-AUTH-OTP-115
  - TC-AUTH-OTP-129
  - TC-AUTH-OTP-174
coverage:
  web: automated
---

# Handoff MFA Authenticator Langsung Pasca-OTP dan Pengiriman Login Alert

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Mfa First` (`mfafirst@qwertysystem.net`) profil FIRST (belum pernah pasang Authenticator).
- User `Mfa Idle` (`mfaidle@qwertysystem.net`) profil IDLE (sudah punya Authenticator terdaftar).
- User `Mfa NewDev` (`mfanewdev@qwertysystem.net`) profil NEWDEV (login dari perangkat/browser baru tak dikenal).
- User `PolNew User` (`polnew@qwertysystem.net`) profil POLNEW (membutuhkan Agreement Gate dan MFA sekaligus).
- Aplikasi authenticator uji (TOTP generator) aktif untuk menghasilkan kode 6 digit time-based.
- Mail-catcher aktif.

## Test Steps

### Handoff setup MFA pada login pertama (profil FIRST)

1. Buka Request OTP untuk `mfafirst@qwertysystem.net`, masukkan kode OTP 6 digit yang valid
2. Selesaikan layar Confirm to Continue bila muncul
3. Verifikasi sistem tidak langsung membuat sesi penuh, melainkan melakukan handoff ke layar setup Authenticator App (QR code setup)
4. Verifikasi sesi sementara pre-auth diteruskan secara aman ke modul MFA

### Handoff verifikasi TOTP pada deteksi perangkat baru (profil NEWDEV)

5. Buka Request OTP untuk `mfanewdev@qwertysystem.net` dari peramban baru yang belum pernah tercatat
6. Masukkan kode OTP 6 digit yang benar
7. Verifikasi sistem mendeteksi perangkat baru dan mengarahkan pengguna ke layar verifikasi faktor kedua: "Two-Factor Authentication (Authenticator App)"
8. Ambil kode TOTP 6 digit dari aplikasi authenticator uji
9. Masukkan kode TOTP ke form verifikasi MFA
10. Verifikasi faktor kedua berhasil divalidasi dan pengguna diarahkan ke Portal — Product Hub
11. Buka mail-catcher untuk `mfanewdev@qwertysystem.net`: verifikasi terdapat email "New Device Login Alert" yang dikirimkan memberi tahu login dari perangkat baru

### Alur berurutan saat Agreement Gate dan MFA terpicu bersamaan (profil POLNEW)

12. Buka Request OTP untuk `polnew@qwertysystem.net` (profil POLNEW)
13. Masukkan kode OTP dari email
14. Verifikasi gerbang pertama yang dihadapi adalah layar "Confirm to Continue" (Agreement Gate)
15. Centang checkbox persetujuan kebijakan privasi dan klik [Continue ➔]
16. Verifikasi setelah submit persetujuan, sistem melanjutkan handoff ke gerbang kedua yaitu layar verifikasi Authenticator App (MFA)
17. Masukkan kode TOTP dari authenticator uji
18. Verifikasi verifikasi MFA berhasil dan browser diarahkan ke Portal — Product Hub
19. Periksa log audit trail di User Log: verifikasi tercatat entri login "Success" dengan detail metode yang sesuai

## Notes

- TAG Samurai tidak pernah mengizinkan pengiriman faktor kedua MFA via SMS atau Email yang sama; faktor kedua wajib menggunakan Authenticator App (TOTP).
- Urutan penegakan gerbang keamanan bersifat linear: Validasi OTP -> Agreement Gate (bila ada kebijakan baru/first login) -> MFA (bila multi-faktor aktif/perangkat baru) -> Sesi Penuh di Product Hub.
