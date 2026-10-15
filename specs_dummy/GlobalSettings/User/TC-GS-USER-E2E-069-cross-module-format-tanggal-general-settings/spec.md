---
id: TC-GS-USER-E2E-069-cross-module-format-tanggal-general-settings
title: "Cross-Module Sync: Penerapan format tanggal General Settings dan pembatalan token Auth"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-965
  - TC-GS-USER-966
  - TC-GS-USER-967
  - TC-GS-USER-968
coverage:
  web: automated
---

# Cross-Module Sync: Penerapan format tanggal General Settings dan pembatalan token Auth

## Prerequisites

- General Settings dikonfigurasi ke format tanggal khusus (MM/DD/YYYY)

## Test Steps

### Format Tanggal dan Token

1. Verifikasi seluruh tampilan tanggal di User List, Detail, dan Changelog mengikuti format General Settings
2. Konfirmasi perubahan email user, verifikasi link reset password lama otomatis dibatalkan/tidak berlaku

## Notes

- Menggabungkan 4 test case granular (TC-GS-USER-965 s.d. TC-GS-USER-968).
