---
id: TC-AUTH-MFA-E2E-012-geo-ip-service-failure-fail-open
title: Penanganan kegagalan layanan Geo-IP dengan fail open untuk dimensi lokasi
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-17
coverage:
  web: automated
---

# Penanganan kegagalan layanan Geo-IP dengan fail open untuk dimensi lokasi

## Prerequisites

- Mode: mock
- Mode: mock (intersep respons panggilan Geo-IP lookup mengembalikan timeout atau HTTP 500)
- Login dari device yang sudah dikenal, bukan first login, dan bukan idle ≥30 hari

## Test Steps

1. Konfigurasikan mock interceptor agar lookup ke provider Geo-IP gagal (HTTP 500 / timeout)
2. Masukkan email dan password valid akun reguler pada halaman Login
3. Klik tombol `[Login]`
4. Verifikasi evaluasi dimensi lokasi dan negara dilewati (fail-open) sehingga pengguna tidak diblokir oleh gangguan pihak ketiga
5. Verifikasi pengguna dapat menyelesaikan login tanpa hambatan verifikasi anomali lokasi

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-12`
- Merepresentasikan `TC-AUTH-MFA-17` (FE Ref: `TC-AUTH-MFA-FE-12`).
- Kebijakan fail-open hanya berlaku pada dimensi lokasi/negara, bukan pada lookup kredensial internal atau status akun.
