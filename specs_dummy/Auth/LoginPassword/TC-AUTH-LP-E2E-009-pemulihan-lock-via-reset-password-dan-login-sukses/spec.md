---
id: TC-AUTH-LP-E2E-009-pemulihan-lock-via-reset-password-dan-login-sukses
title: Pemulihan lock via Reset Password dan reset counter pasca-reset
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-61
  - TC-AUTH-LP-62
  - TC-AUTH-LP-63
coverage:
  web: automated
---

# Pemulihan lock via Reset Password dan reset counter pasca-reset

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `doniprasetyo@qwertysystem.net` berstatus Requires Reset.
- User `putraanugrah@qwertysystem.net` baru menyelesaikan alur Reset Password dari status Requires Reset.
- User `panjikusuma@qwertysystem.net` baru menyelesaikan alur Reset Password dari status Permanent.

## Test Steps

### Pemulihan Requires Reset via alur Reset Password

1. Buka halaman Login with Password di browser web
2. Masukkan email `doniprasetyo@qwertysystem.net` dengan password lama `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
3. Verifikasi Alert Danger "Please reset your password" tampil
4. Klik tautan [Reset password] pada Alert Danger
5. Selesaikan proses reset password menggunakan token valid dan password baru `NewPass#2026`
6. Kembali ke halaman Login with Password
7. Masukkan email `doniprasetyo@qwertysystem.net` dan password baru `NewPass#2026`
8. Selesaikan reCAPTCHA lalu klik tombol [Log in]
9. Verifikasi login berhasil dan browser langsung menuju Portal — Product Hub

### Reset counter kegagalan dan rantai hari pasca-Reset Password

10. Buka kembali halaman Login with Password
11. Masukkan email `putraanugrah@qwertysystem.net` (yang baru reset password) dengan password salah `SalahPass#1`
12. Selesaikan reCAPTCHA lalu klik [Log in] (salah ke-1)
13. Verifikasi Alert Danger "Incorrect email or password" tampil
14. Ulangi submit password salah ke-2 dan ke-3
15. Verifikasi pada salah ke-3, akun terkunci 15 menit (bukan Requires Reset), membuktikan counter harian kembali ke 0
16. Masukkan email `panjikusuma@qwertysystem.net` (yang baru reset dari status Permanent) dengan password salah `SalahPass#1`
17. Selesaikan reCAPTCHA lalu klik [Log in]
18. Verifikasi Alert Danger "Incorrect email or password" tampil biasa dan Alert Permanent tidak tampil, membuktikan rantai hari berturut-turut dikosongkan

## Notes

- Reset Password sukses mereset seluruh counter failed attempt, lock level, dan riwayat consecutive days (`AUTHLP-LOGIC-02f`).
- Semantik reset counter oleh login berhasil (termasuk password kosong/tanpa reCAPTCHA, login sukses, password benar berujung Agreement, dan password benar setelah tahap 1 jam lewat) dipecah ke spec tersendiri E2E-026 (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).
