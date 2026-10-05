---
id: TC-AUTH-ACT-E2E-002-link-valid-loading-idempotent
title: Link valid, loading state, GET idempotent, dan subtitle email penuh
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-10
  - TC-AUTH-ACT-17
  - TC-AUTH-ACT-18
  - TC-AUTH-ACT-19
coverage:
  web: automated
---

# Link valid, loading state, GET idempotent, dan subtitle email penuh

## Prerequisites

- Token valid `active` dan belum expired tersedia (disiapkan oleh hook `before`).
- Halaman `/activate?token={validToken}` dapat diakses langsung via URL.
- Subtitle email pada halaman Set Password ditampilkan penuh (tidak di-mask) sesuai spesifikasi.

## Test Steps

### A. Token valid - render halaman Set Password

1. Buka `/activate?token={validToken}` untuk token `active`, belum expired, dan belum digunakan.
2. Verifikasi halaman **Set Password** dirender.
3. Verifikasi subtitle menampilkan email tujuan lengkap: `"Set a password to log in for [email]."`.
4. Verifikasi field Password menampilkan placeholder `"Enter your password"`.
5. Verifikasi field Confirm Password menampilkan placeholder `"Re-enter your password"`.
6. Verifikasi terdapat checklist 6 baris berwarna abu-abu (state default).
7. Verifikasi tombol `"Set Password"` dalam keadaan enabled.
8. Verifikasi tidak ada CAPTCHA di halaman Set Password.

### B. Loading state saat validasi token

9. Buka `/activate?token={validToken}` dan amati fase sebelum render final.
10. Verifikasi full-page spinner tampil selama proses validasi token sebelum form/404 dirender; tidak ada flash form kosong.

### C. GET idempotent

11. Reload `/activate?token={validToken}` beberapa kali saat token masih `active` dan belum disubmit.
12. Verifikasi halaman Set Password selalu dirender (idempotent read), tidak ada efek samping/konsumsi token akibat GET berulang.
13. Verifikasi token tetap `active`, `consumed_at = null` setelah reload berulang.

## Notes

- GET request bersifat idempotent; konsumsi token hanya terjadi pada POST set-password.
- Subtitle menampilkan email penuh (reversal 2026-07-23).
