---
id: TC-GS-USER-E2E-033-delete-single-happy-path-penghapusan-user
title: "Delete Single: Happy path penghapusan user tunggal dan verifikasi pembersihan list"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-269
  - TC-GS-USER-270
  - TC-GS-USER-271
  - TC-GS-USER-272
  - TC-GS-USER-273
coverage:
  web: automated
---

# Delete Single: Happy path penghapusan user tunggal dan verifikasi pembersihan list

## Prerequisites

- Login sebagai Role: Total Control
- User target Rudi Hakim tersedia

## Test Steps

### Eksekusi Delete User

1. Buka dialog Delete pada baris Rudi Hakim, klik '[Delete]'
2. Verifikasi toast sukses 'User deleted successfully.' tampil
3. Verifikasi baris Rudi Hakim hilang secara permanen dari User List
4. Cari nama Rudi Hakim via Search bar, verifikasi hasil pencarian kosong

## Notes

- Menggabungkan 5 test case granular (TC-GS-USER-269 s.d. TC-GS-USER-273).
