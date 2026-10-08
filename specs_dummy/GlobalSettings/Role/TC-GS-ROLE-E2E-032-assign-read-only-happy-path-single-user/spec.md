---
id: TC-GS-ROLE-E2E-032-assign-read-only-happy-path-single-user
title: "Penugasan Read Only Berhasil untuk User Tunggal: Refleksi Tab Read Only dan Pencatatan Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-80
coverage:
  web: automated
---

# Penugasan Read Only Berhasil untuk User Tunggal: Refleksi Tab Read Only dan Pencatatan Log

## Prerequisites

- Login sebagai Total Control
- Data Uji: Rahmat Hidayat (Dinamis #4)
- Setup Hook: beforeEach: openModalAssignRO()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Read Only
- Rahmat Hidayat tanpa access level, punya baris Manage files (R,D)

## Test Steps

### Assign Read Only ke user (TC-GS-ROLE-80)

1. Klik [+ Assign]
2. Centang Rahmat Hidayat
3. Klik [Assign]
4. Buka Detail "Manage files" dan "Manage user and role"
5. Verifikasi Muncul toast sukses: "Success, Read Only has been assigned."
6. Verifikasi Rahmat Hidayat tampil di Tab Read Only dengan Modified By "Ahmad F"
7. Verifikasi Detail "Manage files": Read checked, Delete unchecked
8. Verifikasi Detail "Manage user and role": baris baru Read checked, Create/Update/Delete unchecked

## Notes

- Memvalidasi alur skenario "Penugasan Read Only Berhasil untuk User Tunggal: Refleksi Tab Read Only dan Pencatatan Log".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.2 [F-ROLE-04]; global-settings/role/PRD/role.md §7.1 T-04.
- Sumber pemetaan test case granular: TC-GS-ROLE-80.
