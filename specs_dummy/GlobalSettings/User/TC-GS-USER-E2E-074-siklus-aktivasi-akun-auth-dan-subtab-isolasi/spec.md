---
id: TC-GS-USER-E2E-074-siklus-aktivasi-akun-auth-dan-subtab-isolasi
title: "Lifecycle Auth: Pembaruan status aktivasi akun, kedaluwarsa link, dan isolasi sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-988
  - TC-GS-USER-989
  - TC-GS-USER-990
  - TC-GS-USER-991
  - TC-GS-USER-992
  - TC-GS-USER-993
coverage:
  web: automated
---

# Lifecycle Auth: Pembaruan status aktivasi akun, kedaluwarsa link, dan isolasi sub-tab

## Prerequisites

- User baru berstatus Pending Activation

## Test Steps

### Aktivasi Akun dan Kedaluwarsa

1. User membuka link aktivasi dan membuat password
2. Refresh User List, verifikasi status berubah menjadi Activated dan badge hilang
3. Verifikasi isolasi state Setup Column antara sub-tab Login User dan Non-Login User bekerja independen

## Notes

- Menggabungkan 6 test case granular (TC-GS-USER-988 s.d. TC-GS-USER-993).
