---
id: TC-AUTH-RST-E2E-026-akses-user-sedang-login
title: "Perilaku akses halaman Reset Password dan tautan token oleh user yang telah memiliki sesi aktif"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-10
  - TC-AUTH-RST-11
coverage:
  web: automated
---

# Perilaku akses halaman Reset Password dan tautan token oleh user yang telah memiliki sesi aktif

## Prerequisites

- User telah login ke TAG Samurai dan memiliki sesi aktif di browser web (berada di dashboard Portal).
- Token reset aktif valid milik user tersedia dari alur sebelumnya (tautan tersedia di mail-catcher).

## Test Steps

### Akses halaman Request Reset Password oleh user yang sedang login

1. Pastikan browser berada dalam kondisi sesi user terotentikasi (sudah login di Portal)
2. Buka URL halaman Request Reset Password (`/reset-password`)
3. Verifikasi sistem mendeteksi adanya sesi login aktif
4. Verifikasi pengguna secara otomatis dialihkan (redirect) kembali ke dashboard Portal Product Hub
5. Coba akses URL `/email-sent` secara langsung saat masih dalam sesi login
6. Verifikasi sistem juga mengalihkan pengguna kembali ke Portal

### Akses tautan token reset dari email oleh user yang sedang login

7. Masih dalam kondisi browser memegang sesi login aktif, buka tautan reset password yang valid (`/setup-new-password?token={valid_token}`)
8. Verifikasi sistem TIDAK mengalihkan pengguna ke Portal
9. Verifikasi halaman Setup New Password tetap ditampilkan secara penuh
10. Verifikasi pengguna dapat melanjutkan alur penggantian password melalui form tersebut hingga tuntas

## Notes

- Sesuai keputusan NC-11 dan `auth-foundation.md` §7a, halaman form publik awal (Request Reset dan Email Sent!) mengalihkan user yang sudah login ke Portal, sedangkan tautan reset spesifik yang memuat token valid (Setup New Password) tetap dapat diakses agar user yang sengaja meminta reset dapat menyelesaikan prosesnya.
