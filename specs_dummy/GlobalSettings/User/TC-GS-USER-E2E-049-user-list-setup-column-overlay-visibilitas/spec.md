---
id: TC-GS-USER-E2E-049-user-list-setup-column-overlay-visibilitas
title: "User List: Setup Column overlay visibilitas kolom default dan curated"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-443
  - TC-GS-USER-444
  - TC-GS-USER-445
  - TC-GS-USER-446
  - TC-GS-USER-447
  - TC-GS-USER-448
  - TC-GS-USER-449
  - TC-GS-USER-450
coverage:
  web: automated
---

# User List: Setup Column overlay visibilitas kolom default dan curated

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Overlay Column Visibility

1. Klik header kolom (⋯), verifikasi popover Column Visibility terbuka
2. Uncheck kolom 'Email' dan 'Employee ID', verifikasi kedua kolom langsung hilang dari tabel utama (Live Preview)
3. Check kolom curated 'Activation Status', verifikasi kolom tersebut muncul di tabel

## Notes

- Menggabungkan 8 test case granular (TC-GS-USER-443 s.d. TC-GS-USER-450).
