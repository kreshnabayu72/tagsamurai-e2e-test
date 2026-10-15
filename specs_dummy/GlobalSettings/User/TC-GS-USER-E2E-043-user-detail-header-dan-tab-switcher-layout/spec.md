---
id: TC-GS-USER-E2E-043-user-detail-header-dan-tab-switcher-layout
title: "User Detail: Screening layout header, breadcrumb navigasi, dan default tab switcher"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-356
  - TC-GS-USER-357
  - TC-GS-USER-358
  - TC-GS-USER-359
  - TC-GS-USER-360
  - TC-GS-USER-361
  - TC-GS-USER-362
  - TC-GS-USER-363
  - TC-GS-USER-364
  - TC-GS-USER-365
  - TC-GS-USER-366
  - TC-GS-USER-367
  - TC-GS-USER-368
  - TC-GS-USER-369
  - TC-GS-USER-370
  - TC-GS-USER-1054
coverage:
  web: automated
---

# User Detail: Screening layout header, breadcrumb navigasi, dan default tab switcher

## Prerequisites

- Login sebagai Role: Total Control
- Buka User Detail Dewi Lestari

## Test Steps

### Screening Header dan Tab Awal

1. Verifikasi breadcrumb menampilkan 'User > Detail'
2. Verifikasi header memuat Avatar, Full Name, Email, status badge Active, dan menu tindakan [⋯]
3. Verifikasi tab 'Role' aktif secara default saat pertama kali membuka Detail User (TC-1054)
4. Verifikasi ketersediaan switcher tab: Role, Responsibilities, Non-Login User, Changelog, System Log, User Log

## Notes

- Menggabungkan 16 test case granular (TC-GS-USER-356 s.d. TC-GS-USER-1054).
