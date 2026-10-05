---
id: TC-AUTH-MFA-E2E-047-concurrency-retry-verify-after-timeout
title: Penanganan retry submit verifikasi faktor kedua setelah network timeout client
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-90
coverage:
  web: automated
---

# Penanganan retry submit verifikasi faktor kedua setelah network timeout client

## Prerequisites

- Mode: mock
- Mode: mock (intersep koneksi untuk mensimulasikan verify pertama sukses di server tetapi response timeout di sisi client)

## Test Steps

1. Simulasikan client melakukan retry verifikasi dengan kode yang sama setelah timeout
2. Verifikasi sistem menolak retry karena sesi pre-auth telah di-consume pada pemrosesan pertama
3. Verifikasi tidak terjadi double-login maupun duplikasi penulisan log audit

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-47`
- Merepresentasikan `TC-AUTH-MFA-90` (FE Ref: `TC-AUTH-MFA-FE-47`).
