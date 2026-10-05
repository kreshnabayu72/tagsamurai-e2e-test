---
id: TC-AUTH-MFA-E2E-026-authenticator-drift-window-tolerance
title: Toleransi drift window kode TOTP diterima dalam batas pergeseran waktu 1 step
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-44
coverage:
  web: automated
---

# Toleransi drift window kode TOTP diterima dalam batas pergeseran waktu 1 step

## Prerequisites

- Mode: FE+BE
- Halaman Authenticator Verification terbuka
- Jam perangkat klien/authenticator bergeser sedikit (±30 detik, drift window ±1 step)

## Test Steps

1. Generate kode TOTP dari interval waktu tepat 1 step sebelum atau 1 step sesudah waktu server saat ini
2. Masukkan kode 6 digit tersebut ke dalam field
3. Klik tombol `[Login]`
4. Verifikasi server menerima kode karena masih berada dalam batas toleransi clock drift ±1 step (~90 detik total)
5. Verifikasi proses login berhasil difinalisasi

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-26`
- Merepresentasikan `TC-AUTH-MFA-44` (FE Ref: `TC-AUTH-MFA-FE-26`).
