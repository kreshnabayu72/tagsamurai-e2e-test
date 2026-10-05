---
id: TC-AUTH-MFA-E2E-033-email-alert-async-unusual-login
title: Pengiriman async email alert unusual login tanpa memblokir alur verifikasi MFA
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-68
coverage:
  web: automated
---

# Pengiriman async email alert unusual login tanpa memblokir alur verifikasi MFA

## Prerequisites

- Mode: FE+BE
- Kondisi Unusual Login terdeteksi pada Faktor-1

## Test Steps

1. Masukkan kredensial login dari kondisi unusual login
2. Klik tombol `[Login]`
3. Amati waktu transisi ke layar verifikasi faktor kedua
4. Verifikasi antarmuka langsung menyajikan layar faktor kedua tanpa menunggu antrean pengiriman email selesai (pola fire-and-forget)
5. Verifikasi email alert keamanan berhasil diterima di mailbox akun

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-33`
- Merepresentasikan `TC-AUTH-MFA-68` (FE Ref: `TC-AUTH-MFA-FE-33`).
