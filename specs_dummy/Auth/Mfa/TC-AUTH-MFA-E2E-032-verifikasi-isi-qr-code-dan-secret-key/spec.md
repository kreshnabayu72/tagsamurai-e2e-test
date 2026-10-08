---
id: TC-AUTH-MFA-E2E-032-verifikasi-isi-qr-code-dan-secret-key
title: "Verifikasi Kriptografis: Parameter URI QR Code, Format Secret Key, dan Proteksi Secret"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-109
  - TC-AUTH-MFA-117
  - TC-AUTH-MFA-120
  - TC-AUTH-MFA-123
coverage:
  web: automated
---
# Verifikasi Kriptografis: Parameter URI QR Code, Format Secret Key, dan Proteksi Secret

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `QR Tester` (`qrtester@qwertysystem.net`) profil FIRST (belum enroll).
- User `Active Secret User` (`activesecret@qwertysystem.net`) yang authenticator-nya sudah terdaftar.
- Tool inspeksi / decoder gambar canvas QR Code (`jsQR` / canvas extractor).

## Test Steps

### Verifikasi isi QR Code untuk pendaftaran TOTP standar RFC 6238

1. Buka alur Enrollment Authenticator untuk user `qrtester@qwertysystem.net`
2. Ambil gambar / canvas QR Code yang dirender pada Step 2 dan decode menjadi string URI
3. Verifikasi skema protokol URI adalah `otpauth://totp/`
4. Verifikasi label URI adalah `TAG%20Samurai:qrtester%40qwertysystem.net`
5. Verifikasi parameter URI memuat:
   - `secret`: string Base32 16-32 karakter
   - `issuer`: `TAG Samurai`
   - `algorithm`: `SHA1`
   - `digits`: `6`
   - `period`: `30`

### Verifikasi tombol [Copy key] menyalin secret key yang identik

6. Klik tombol CopyButton [Copy key] pada Step 2
7. Baca nilai clipboard sistem
8. Verifikasi string di clipboard sama persis dengan nilai parameter `secret` pada URI QR Code (tanpa karakter spasi)

### Reload (F5) pada sesi pre-auth yang sama mempertahankan secret key yang sama

9. Catat string secret key yang tampil di layar
10. Lakukan reload browser (tekan F5)
11. Verifikasi halaman tetap berada di Enrollment Authenticator dan string secret key yang ditampilkan persis sama dengan sebelumnya (sesuai NC-18)

### Proteksi Secret: Permintaan pendaftaran baru ditolak jika authenticator sudah aktif

12. Kirim request HTTP langsung ke endpoint pendaftaran secret (`/auth/mfa/authenticator/enroll`) untuk user `activesecret@qwertysystem.net` yang sudah aktif
13. Verifikasi server menolak request dan tidak mengembalikan secret baru (mencegah penyerang membaca atau mereset secret aktif tanpa hak)

## Notes

- Sesuai RFC 6238 dan keputusan NC-07, parameter TOTP bersifat baku (SHA-1, 6 digit, 30 detik).
- Secret key pending bersifat idempoten selama sesi pre-auth yang sama (NC-18).
