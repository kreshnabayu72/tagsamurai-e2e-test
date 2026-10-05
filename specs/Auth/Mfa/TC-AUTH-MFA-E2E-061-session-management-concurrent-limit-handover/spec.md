---
id: TC-AUTH-MFA-E2E-061-session-management-concurrent-limit-handover
title: Login final via MFA menyerahkan evaluasi batas sesi konkuren ke Session Management
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-116
coverage:
  web: automated
---

# Login final via MFA menyerahkan evaluasi batas sesi konkuren ke Session Management

## Prerequisites

- Mode: FE+BE
- User telah memiliki sesi aktif di perangkat lain

## Test Steps

1. Lakukan login final via MFA sukses dari perangkat kedua
2. Verifikasi modul MFA berhasil memvalidasi faktor kedua dan menerbitkan sesi penuh
3. Verifikasi evaluasi batas konkuren (1 web + 1 mobile) diserahkan sepenuhnya ke modul Session Management tanpa pemblokiran sepihak oleh MFA

## Notes

- TC Frontend Ref: `— (Manual di FE doc)`
- Merepresentasikan `TC-AUTH-MFA-116`.
