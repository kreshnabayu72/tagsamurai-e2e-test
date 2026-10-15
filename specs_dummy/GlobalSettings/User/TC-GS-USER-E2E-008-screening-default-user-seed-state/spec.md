---
id: TC-GS-USER-E2E-008-screening-default-user-seed-state
title: "Screening state awal Default User seed di User List"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1043
coverage:
  web: automated
---

# Screening state awal Default User seed di User List

## Prerequisites

- Entitas baru hasil registrasi customer
- Default User 'Hendra Gunawan' belum pernah diedit oleh admin mana pun

## Test Steps

### Verifikasi Modified By di User List

1. Buka Global Settings > User > User List
2. Temukan baris Hendra Gunawan
3. Verifikasi sel Modified By menampilkan 'System' (bukan nama user atau admin)

## Notes

- Menggabungkan 1 test case granular (TC-GS-USER-1043 s.d. TC-GS-USER-1043).
