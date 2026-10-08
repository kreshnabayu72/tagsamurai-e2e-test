---
id: TC-GS-USER-E2E-159-user-log-tanpa-reset-authenticator
title: Reset Authenticator tidak tercatat di Tab User Log
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-618
coverage:
  web: automated
---

# Reset Authenticator tidak tercatat di Tab User Log

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Target "Karina Sari" adalah User Basic biasa dengan Authenticator enrolled
- Reset Authenticator membutuhkan akun MFA yang bisa dikendalikan skrip, disediakan tim FE
- Spec ini mereset Authenticator target, jadi target dienroll ulang oleh seeding sebelum run berikutnya

## Test Steps

1. Buka User Detail "Karina Sari" > Tab User Log dan catat jumlah baris
2. Reset Authenticator target dan konfirmasi dengan `[Reset]`
3. Muat ulang Tab User Log dan verifikasi tidak ada baris baru akibat reset
4. Buka Tab Changelog dan verifikasi ada entri "Reset Authenticator" pada Field "Authenticator Enrollment" dari "Enrolled" ke "Not Enrolled"
5. Buka Activity Log dan verifikasi aksi yang sama tercatat

## Notes

- Sumber `user.md` §8.4 (Must NOT) dan §9.2 [F-USER-11]. Pasangan `TC-GS-USER-E2E-037`.
