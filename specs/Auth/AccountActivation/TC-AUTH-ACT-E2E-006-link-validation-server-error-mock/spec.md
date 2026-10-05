---
id: TC-AUTH-ACT-E2E-006-link-validation-server-error-mock
title: Validasi link saat server error (5xx/timeout) → error state + "[Try Again]", bukan 404
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-16
coverage:
  web: automated
---

# Validasi link saat server error (5xx/timeout) → error state + "[Try Again]", bukan 404

## Prerequisites

- Token valid `active` tersedia.
- Digunakan `Spectra.intercept()` untuk memicu 5xx/timeout pada endpoint validasi token GET. Mode: mock untuk kasus ini.

## Test Steps

1. Pasang intercept pada endpoint validasi GET `/auth/activation/{token}` untuk mengembalikan 5xx atau timeout.
2. Buka `/activate?token={validToken}` saat backend error.
3. Verifikasi muncul error state dengan tombol `[Try Again]` (sesuai C-2 convention).
4. Verifikasi **tidak** menampilkan halaman 404.
5. Verifikasi token tetap `active` dan tidak berubah status.

## Notes

- Kasus ini menggunakan `Mode: mock` melalui `Spectra.intercept()`.
