---
id: TC-AUTH-MFA-E2E-046-concurrency-double-submit-race
title: Proteksi balapan double submit atau auto submit ganda pada verifikasi faktor kedua
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-89
coverage:
  web: automated
---

# Proteksi balapan double submit atau auto submit ganda pada verifikasi faktor kedua

## Prerequisites

- Mode: FE+BE
- Halaman verifikasi faktor kedua dengan kode benar yang siap disubmit

## Test Steps

1. Picu pengiriman dua submission verifikasi secara hampir bersamaan (melalui rapid double-click CTA atau balapan auto-submit)
2. Verifikasi double-submit guard pada frontend dan backend memproses tepat satu evaluasi
3. Verifikasi tidak ada efek samping ganda, tidak ada sesi ganda, dan hanya ada 1 log login yang tercatat

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-46`
- Merepresentasikan `TC-AUTH-MFA-89` (FE Ref: `TC-AUTH-MFA-FE-46`).
