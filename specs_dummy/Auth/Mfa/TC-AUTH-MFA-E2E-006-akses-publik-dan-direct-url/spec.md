---
id: TC-AUTH-MFA-E2E-006-akses-publik-dan-direct-url
title: "Akses Langsung ke URL MFA Tanpa Sesi Pre-Auth dan Redirection Pengguna Terotentikasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-19
  - TC-AUTH-MFA-20
  - TC-AUTH-MFA-21
coverage:
  web: automated
---
# Akses Langsung ke URL MFA Tanpa Sesi Pre-Auth dan Redirection Pengguna Terotentikasi

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- Pengguna yang sudah login secara sah di Portal — Product Hub dengan sesi web aktif.
- Rute halaman MFA: `/auth/mfa`, `/auth/mfa/otp`, `/auth/mfa/authenticator`, dan `/auth/mfa/enroll`.

## Test Steps

### Akses langsung ke URL MFA tanpa sesi pre-auth diarahkan ke /login

1. Buka browser baru tanpa cookies atau sesi pre-auth
2. Navigasikan langsung ke `/auth/mfa` (Choose Verification Method)
3. Verifikasi server/router mengalihkan pengguna ke halaman login (`/login`) tanpa pesan error
4. Uji navigasi langsung ke rute `/auth/mfa/otp`
5. Verifikasi pengguna dialihkan ke `/login`
6. Uji navigasi langsung ke rute `/auth/mfa/authenticator` dan `/auth/mfa/enroll`
7. Verifikasi semua rute MFA publik menolak akses langsung tanpa sesi pre-auth valid dan mengarahkan ke `/login`

### Pengguna yang sudah login mengakses URL MFA dialihkan ke Product Hub

8. Login ke aplikasi hingga mendarat di Portal — Product Hub dengan sesi web aktif penuh
9. Pada address bar browser, ketik URL `/auth/mfa` lalu tekan Enter
10. Verifikasi sesuai keputusan NC-18, sistem mendeteksi sesi penuh aktif dan mengalihkan browser kembali ke Portal — Product Hub (`/product-hub`)
11. Ulangi akses langsung ke rute `/auth/mfa/otp` dan `/auth/mfa/enroll` saat berstatus authenticated
12. Verifikasi browser selalu dikembalikan ke Product Hub tanpa memicu pembatalan sesi aktif

### Tab baru tanpa state sesi pre-auth diperlakukan seperti akses langsung

13. Buka tab baru pada peramban terpisah tanpa sharing session state
14. Ketik langsung URL salah satu halaman MFA
15. Verifikasi tab baru dialihkan ke halaman `/login`

## Notes

- Sesuai keputusan NC-18 dan PRD §9.3, URL MFA dilindungi oleh pre-auth session guard.
- Pengguna yang sudah login dialihkan ke Product Hub untuk mencegah re-entry state yang tidak valid.
