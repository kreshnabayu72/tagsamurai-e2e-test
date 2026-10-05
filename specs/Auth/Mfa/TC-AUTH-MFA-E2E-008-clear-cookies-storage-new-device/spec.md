---
id: TC-AUTH-MFA-E2E-008-clear-cookies-storage-new-device
title: Pembersihan cookies atau storage browser terdeteksi sebagai device baru
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-11
coverage:
  web: automated
---

# Pembersihan cookies atau storage browser terdeteksi sebagai device baru

## Prerequisites

- Mode: FE+BE
- User pernah login sukses dan melakukan trust device di browser ini

## Test Steps

1. Bersihkan seluruh cookies, local storage, dan session storage pada browser
2. Buka kembali halaman Login TAG Samurai
3. Masukkan email dan password valid, lalu klik `[Login]`
4. Verifikasi browser menghasilkan `device_id` baru yang belum terdaftar
5. Verifikasi sistem mewajibkan verifikasi faktor kedua (MFA) sesuai pola remember-me standar industri

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-08`
- Merepresentasikan `TC-AUTH-MFA-11` (FE Ref: `TC-AUTH-MFA-FE-08`).
