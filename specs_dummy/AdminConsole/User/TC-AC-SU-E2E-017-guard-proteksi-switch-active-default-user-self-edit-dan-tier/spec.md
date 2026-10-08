---
id: TC-AC-SU-E2E-017-guard-proteksi-switch-active-default-user-self-edit-dan-tier
title: "Guard Proteksi Switch Active: Default User, Self-Edit, Suspended, dan Tier Locked"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-30
  - TC-AC-SU-31
  - TC-AC-SU-32
  - TC-AC-SU-33
  - TC-AC-SU-34
  - TC-AC-SU-35
  - TC-AC-SU-36
  - TC-AC-SU-160
coverage:
  web: automated
---

# Guard Proteksi Switch Active: Default User, Self-Edit, Suspended, dan Tier Locked

## Prerequisites

- Login sebagai Administrator Total Control
- Terdapat data Default User, User Self (akun saat ini), User Global Inactive, User Tier Total Control, dan User Tier Read Only

## Test Steps

### Guard Default User dan Self-Edit
1. Buka menu `Admin Console > Settings > User`
2. Temukan baris `Default User` pada tabel
3. Verifikasi switch kolom Active berstatus disabled (tidak dapat diklik)
4. Hover pada switch Default User dan verifikasi tooltip informatif: `"Default user cannot be deactivated"`
5. Temukan baris akun yang sedang login saat ini (`Self`)
6. Verifikasi switch Active berstatus disabled
7. Hover pada switch Self dan verifikasi tooltip: `"You cannot deactivate your own account"`

### Guard Status Global dan Tier Locked
8. Temukan baris user dengan `isActiveGlobal = false` (dinonaktifkan dari Global Settings)
9. Verifikasi switch Active berstatus disabled dengan tooltip: `"User is deactivated at Global Settings level"`
10. Temukan baris user yang memiliki tier `Total Control` dan `Read Only`
11. Verifikasi switch Active berstatus disabled sesuai aturan proteksi tier integritas entitas

## Notes

Memastikan invariant kepatuhan tata kelola akun tidak dapat dilanggar melalui interaksi baris tabel.
