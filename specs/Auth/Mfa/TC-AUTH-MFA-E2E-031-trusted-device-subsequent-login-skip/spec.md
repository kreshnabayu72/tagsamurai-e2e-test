---
id: TC-AUTH-MFA-E2E-031-trusted-device-subsequent-login-skip
title: Login berikutnya dari device dan lokasi yang telah trusted tidak memicu MFA
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-60
coverage:
  web: automated
---

# Login berikutnya dari device dan lokasi yang telah trusted tidak memicu MFA

## Prerequisites

- Mode: FE+BE
- User telah menyelesaikan alur MFA sukses dari browser ini
- Data `device_id` dan lokasi telah di-upsert ke tabel `trusted_device`

## Test Steps

1. Lakukan logout dari aplikasi
2. Pada browser yang sama, buka kembali halaman Login
3. Masukkan email dan password valid, lalu klik `[Login]`
4. Verifikasi sistem mencocokkan identitas perangkat dan koordinat lokasi tepercaya
5. Verifikasi MFA tidak terpicu oleh dimensi perangkat maupun lokasi dan pengguna langsung mendarat di Portal

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-31`
- Merepresentasikan `TC-AUTH-MFA-60` (FE Ref: `TC-AUTH-MFA-FE-31`).
