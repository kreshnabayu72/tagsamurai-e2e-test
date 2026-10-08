---
id: TC-GS-USER-E2E-070-security-defense-in-depth-direct-api-tampering
title: "Security: Defense-in-depth penolakan request direct API tampering tanpa wewenang (403)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-969
  - TC-GS-USER-970
  - TC-GS-USER-971
  - TC-GS-USER-972
  - TC-GS-USER-973
  - TC-GS-USER-974
  - TC-GS-USER-976
  - TC-GS-USER-977
  - TC-GS-USER-978
  - TC-GS-USER-983
  - TC-GS-USER-975
coverage:
  web: automated
---

# Security: Defense-in-depth penolakan request direct API tampering tanpa wewenang (403)

## Prerequisites

- Mode: FE+BE dengan intercept/direct payload tampering

## Test Steps

### Penolakan Direct API Tampering

1. Kirim request POST create user langsung oleh token Read Only, verifikasi server menolak 403 Forbidden
2. Kirim request PATCH edit user langsung oleh token Read Only, verifikasi penolakan 403
3. Kirim request DELETE user langsung oleh Update-Only holder, verifikasi penolakan 403
4. Kirim request penonaktifan akun sendiri atau penghapusan Default User secara langsung, verifikasi penolakan 403

## Notes

- Menggabungkan 11 test case granular (TC-GS-USER-969 s.d. TC-GS-USER-975).
