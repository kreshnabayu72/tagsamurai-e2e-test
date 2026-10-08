---
id: TC-AUTH-ACT-E2E-012-server-error-422-409-404-mid-flight
title: Server error submit, 422 re-check policy, dan 409/404 mid-flight
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-45
  - TC-AUTH-ACT-48
  - TC-AUTH-ACT-49
coverage:
  web: automated
---

# Server error submit, 422 re-check policy, dan 409/404 mid-flight

## Prerequisites

- Token valid `active` tersedia.
- Hook `beforeEach` menyiapkan token valid baru.
- Digunakan `Spectra.intercept()` untuk memanipulasi response endpoint `POST .../set-password` (5xx/timeout, 422, 409/404 mid-flight). Mode: mock.

## Test Steps

### A. Server error saat submit

1. Siapkan ulang token valid baru. Pasang intercept pada `POST .../set-password` untuk mengembalikan 5xx atau timeout.
2. Submit password valid saat backend error.
3. Verifikasi muncul toast `"Internal server error."`.
4. Verifikasi form tetap terbuka, input dipertahankan, dan button kembali enabled (re-enabled).
5. Verifikasi status token dan user **tidak berubah** (token tetap `active`, user tetap `Pending Activation`).

### B. 422 dari server (re-check policy gagal di BE)

6. Siapkan ulang token valid baru. Pasang intercept/skenario dimana password lolos validasi FE tapi ditolak BE.
7. Submit password valid sesuai FE validation.
8. Verifikasi response 422 ditangani dengan benar: inline error/checklist abu-abu sesuai field yang gagal, form tetap terbuka.
9. Verifikasi token tetap `active`, tidak ter-consume.

### C. 409/404 mid-flight

10. Siapkan ulang token valid baru. Invalidate token tepat saat proses submit berlangsung (mid-flight) melalui API lain (simulasi concurrency).
11. Submit password valid.
12. Verifikasi response ditangani sebagai token-gone (bukan generic error) dan terjadi redirect ke halaman 404.

## Notes

- Menggunakan `Mode: mock` melalui `Spectra.intercept()`.
