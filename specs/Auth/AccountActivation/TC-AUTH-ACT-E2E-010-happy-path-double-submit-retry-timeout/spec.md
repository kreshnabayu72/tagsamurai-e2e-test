---
id: TC-AUTH-ACT-E2E-010-happy-path-double-submit-retry-timeout
title: Happy path, double-click prevention, dan retry setelah network timeout
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-40
  - TC-AUTH-ACT-41
  - TC-AUTH-ACT-42
coverage:
  web: automated
---

# Happy path, double-click prevention, dan retry setelah network timeout

## Prerequisites

- Token valid `active` tersedia.
- Hook `beforeEach` menyiapkan token valid baru untuk menjaga isolasi antar skenario.
- Untuk retry setelah network timeout (TC-AUTH-ACT-42), dapat digunakan `Spectra.intercept()` sesuai implementasi otomasi (Mode: mock sesuai kebutuhan).

## Test Steps

### A. Happy path

1. Buka halaman Set Password dengan token valid. Isi Password dan Confirm Password dengan nilai valid (`Abcd1!23`).
2. Klik `[Set Password]` untuk meng-submit.
3. Verifikasi token berubah menjadi `consumed`.
4. Verifikasi user berubah dari `Pending Activation` menjadi `Activated` di Global Settings > User.
5. Verifikasi redirect ke halaman Activation Success.

### B. Double-submit (double-click)

6. Siapkan ulang token valid baru. Isi form dengan password valid.
7. Klik tombol `[Set Password]` dua kali dengan cepat, berturut-turut.
8. Verifikasi hanya 1 request yang diproses (button disabled + spinner setelah klik pertama).
9. Verifikasi tidak terjadi aktivasi ganda atau error ganda.
10. Verifikasi token `consumed` tepat 1× dan user `Activated` tepat 1×.

### C. Retry setelah network timeout

11. Siapkan ulang token valid baru. Pasang intercept pada POST set-password sehingga request pertama menghasilkan network timeout (response loss) untuk memicu retry otomatis dari client.
12. Lakukan submit dengan password valid.
13. Verifikasi tidak terjadi double-activation. Retry kedua ditolak sebagai token sudah dipakai (404/409 sesuai response API).
14. Verifikasi token `consumed` tepat 1×, user `Activated` 1×.

## Notes

- Semua skenario yang mengubah state menggunakan token valid baru melalui `beforeEach`.
