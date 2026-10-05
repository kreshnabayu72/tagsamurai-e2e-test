---
id: TC-AUTH-MFA-E2E-011-country-detection-same-vs-different
title: Negara sama tidak memicu MFA sedangkan perpindahan negara memicu MFA
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-15
  - TC-AUTH-MFA-16
coverage:
  web: automated
---

# Negara sama tidak memicu MFA sedangkan perpindahan negara memicu MFA

## Prerequisites

- Mode: FE+BE
- Login terakhir pengguna tercatat dari Negara ID (Indonesia)
- Pasangan negara ID ↔ SG belum terdaftar sebagai trusted pair

## Test Steps

### Login dari Negara Sama
1. Lakukan login dari IP yang berasal dari negara yang sama (Indonesia)
2. Verifikasi dimensi negara tidak memicu MFA

### Login dari Negara Berbeda
3. Lakukan logout
4. Simulasikan login dari IP yang berlokasi di negara berbeda (Singapura), meskipun jarak fisiknya relatif dekat
5. Klik tombol `[Login]`
6. Verifikasi sistem mendeteksi perbedaan negara dan mewajibkan verifikasi faktor kedua (MFA)
7. Verifikasi email alert keamanan dikirimkan ke email akun

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-11`
- Merepresentasikan `TC-AUTH-MFA-15` dan `TC-AUTH-MFA-16` (FE Ref: `TC-AUTH-MFA-FE-11`).
