---
id: TC-AUTH-MFA-E2E-062-logging-device-browser-canonical-format
title: Kolom Device atau Browser pada entri log login final tercatat dalam format kanonikal
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-123
coverage:
  web: automated
---

# Kolom Device atau Browser pada entri log login final tercatat dalam format kanonikal

## Prerequisites

- Mode: FE+BE
- Login final via MFA sukses
- User-Agent klien ter-parse secara valid

## Test Steps

1. Lakukan login final via MFA dari peramban web
2. Buka Global Settings > Activity Log > Session dan User Log
3. Temukan baris entri login final yang baru saja tercipta
4. Verifikasi kolom Device / Browser terisi dengan format kanonikal `"[Browser] on [OS]"` (misalnya `"Chrome on Windows"`), tanpa versi angka, sesuai konvensi platform `auth-foundation.md` §9 (`GAP-178`)

## Notes

- TC Frontend Ref: `— (Gap-fill GAP-178)`
- Merepresentasikan `TC-AUTH-MFA-123` (`GAP-178`).
