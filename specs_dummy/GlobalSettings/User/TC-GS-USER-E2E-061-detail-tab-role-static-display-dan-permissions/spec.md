---
id: TC-GS-USER-E2E-061-detail-tab-role-static-display-dan-permissions
title: "Detail User: Tampilan statis tab Role, matriks permission, dan non-sortable columns"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-871
  - TC-GS-USER-872
coverage:
  web: automated
---

# Detail User: Tampilan statis tab Role, matriks permission, dan non-sortable columns

## Prerequisites

- Buka User Detail target tab Role

## Test Steps

### Screening Tab Role

1. Verifikasi kolom Active, Role Name, Create, Read, Update, Delete
2. Verifikasi seluruh header kolom tab Role bersifat non-sortable (tidak dapat diurutkan)
3. Verifikasi tidak ada search box maupun filter panel pada tab Role

## Notes

- Menggabungkan 2 test case granular (TC-GS-USER-871 s.d. TC-GS-USER-872).
