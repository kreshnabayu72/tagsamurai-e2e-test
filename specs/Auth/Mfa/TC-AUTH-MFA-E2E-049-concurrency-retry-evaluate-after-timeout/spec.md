---
id: TC-AUTH-MFA-E2E-049-concurrency-retry-evaluate-after-timeout
title: Retry evaluasi kebutuhan MFA pasca timeout bersifat idempoten
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-92
coverage:
  web: automated
---

# Retry evaluasi kebutuhan MFA pasca timeout bersifat idempoten

## Prerequisites

- Mode: mock
- Mode: mock (simulasikan timeout pada endpoint evaluasi MFA)

## Test Steps

1. Lakukan request evaluasi MFA yang mengalami timeout
2. Kirimkan retry request evaluasi dengan parameter yang sama
3. Verifikasi hasil evaluasi kedua bersifat konsisten dan idempoten
4. Verifikasi tidak tercipta state duplikat di backend

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-49`
- Merepresentasikan `TC-AUTH-MFA-92` (FE Ref: `TC-AUTH-MFA-FE-49`).
