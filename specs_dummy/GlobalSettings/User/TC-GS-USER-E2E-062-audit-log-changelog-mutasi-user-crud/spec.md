---
id: TC-GS-USER-E2E-062-audit-log-changelog-mutasi-user-crud
title: "Audit Log: Pencatatan mutasi user (Create, Edit, Status, Delete) pada Changelog"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-873
  - TC-GS-USER-874
  - TC-GS-USER-875
  - TC-GS-USER-876
  - TC-GS-USER-877
  - TC-GS-USER-878
  - TC-GS-USER-879
  - TC-GS-USER-880
  - TC-GS-USER-881
  - TC-GS-USER-882
  - TC-GS-USER-883
  - TC-GS-USER-884
  - TC-GS-USER-885
  - TC-GS-USER-886
  - TC-GS-USER-887
  - TC-GS-USER-888
  - TC-GS-USER-889
  - TC-GS-USER-890
  - TC-GS-USER-891
  - TC-GS-USER-892
  - TC-GS-USER-893
  - TC-GS-USER-894
  - TC-GS-USER-895
  - TC-GS-USER-896
  - TC-GS-USER-897
  - TC-GS-USER-898
  - TC-GS-USER-899
coverage:
  web: automated
---

# Audit Log: Pencatatan mutasi user (Create, Edit, Status, Delete) pada Changelog

## Prerequisites

- Lakukan mutasi CRUD pada user di User List

## Test Steps

### Verifikasi Entri Changelog

1. Buka Modal Changelog User List
2. Verifikasi tercatat entri aksi 'Create' dengan nilai awal field
3. Verifikasi tercatat entri aksi 'Edit' memuat Old Value dan New Value spesifik
4. Verifikasi pencatatan perubahan status Deactivate dan Activate

## Notes

- Menggabungkan 27 test case granular (TC-GS-USER-873 s.d. TC-GS-USER-899).
