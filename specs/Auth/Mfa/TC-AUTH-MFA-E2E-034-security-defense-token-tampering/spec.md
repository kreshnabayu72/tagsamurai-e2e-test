---
id: TC-AUTH-MFA-E2E-034-security-defense-token-tampering
title: "Defense-in-Depth: Proteksi Token Pre-Auth, One-Time Use, dan Pemisahan Purpose OTP"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-188
  - TC-AUTH-MFA-189
  - TC-AUTH-MFA-190
coverage:
  web: automated
---
# Defense-in-Depth: Proteksi Token Pre-Auth, One-Time Use, dan Pemisahan Purpose OTP

## Prerequisites

- Client HTTP untuk eksekusi direct API requests.
- User `Tamper User` (`tamper@qwertysystem.net`) berstatus Activated dan Active.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Penolakan request verifikasi langsung tanpa preAuthToken sah

1. Kirim request HTTP POST langsung ke endpoint verifikasi faktor-2 MFA (`/auth/mfa/otp/verify`) dengan parameter token pre-auth acak/palsu
2. Verifikasi backend menolak request dengan status HTTP 401/403 dan tidak ada sesi web yang terbentuk
3. Ulangi penyerangan serupa ke endpoint `/auth/mfa/authenticator/verify`
4. Verifikasi request ditolak tanpa pemrosesan verifikasi kode

### Penolakan pemakaian ulang token pre-auth yang sudah dikonsumsi (One-Time Use Token)

5. Jalankan alur login normal dengan user `tamper@qwertysystem.net` dan catat `preAuthToken` yang diterbitkan
6. Selesaikan verifikasi faktor-2 secara sah hingga mendarat di Portal — Product Hub
7. Ambil `preAuthToken` yang baru saja dikonsumsi tersebut dan tembakkan kembali ke endpoint verifikasi melalui direct HTTP request
8. Verifikasi backend menolak penggunaan token yang telah dikonsumsi (Single-use Token Guard aktif)

### Pemisahan Purpose kode OTP: Penolakan kode Login with OTP pada faktor-2 MFA

9. Ajukan kode OTP login melalui modul Login with OTP (`/login/otp`) untuk user `tamper@qwertysystem.net`
10. Catat kode OTP login tersebut dari mail-catcher (`purpose = 'login'`)
11. Buka alur login password yang memicu faktor-2 MFA OTP untuk user yang sama (`purpose = 'mfa'`)
12. Masukkan kode OTP login yang masih hangat ke dalam kotak verifikasi MFA
13. Verifikasi sesuai keputusan NC-19, sistem menolak kode tersebut dengan caption "Invalid code" (pemisahan tujuan kode `purpose='mfa'`)
14. Verifikasi percobaan ini dihitung sebagai percobaan salah pada batas 5 kuota pre-auth

## Notes

- Sesuai PRD §9.3 dan keputusan NC-19, kode OTP dibatasi secara ketat oleh kolom database `purpose`.
- Token pre-auth bersifat sekali pakai (one-time use) dan hangus seketika setelah sesi login final diterbitkan.
