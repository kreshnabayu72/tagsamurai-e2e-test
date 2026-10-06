---
id: TC-GS-ROLE-E2E-008-matriks-guard-aktor-target-self-edit-dan-target-privilese
title: "Matriks Guard Aktor × Target: Proteksi Self-Edit dan Pembatasan Target Total Control / Read Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-61
  - TC-GS-ROLE-62
  - TC-GS-ROLE-63
  - TC-GS-ROLE-64
  - TC-GS-ROLE-67
coverage:
  web: automated
---

# Matriks Guard Aktor × Target: Proteksi Self-Edit dan Pembatasan Target Total Control / Read Only

## Prerequisites

- Tersedia akun aktor Total Control (totalControl2)
- Tersedia akun aktor Manage user and role Update (manageUserRoleUpdate)
- Tersedia target Default User, target user TC lain (Siti Rahmawati), target user RO (Budi Hartono), dan target reguler (Doni Pratama)

## Test Steps

1. Login sebagai akun totalControl2
2. Buka Tab System > Detail role 'Manage user and role'
3. Verifikasi baris Default User memiliki row action Remove disabled dengan tooltip "Default User must always have Total Control."
4. Verifikasi baris diri sendiri (totalControl2) memiliki checkbox CRUD disabled dan row action Remove disabled dengan tooltip "You cannot edit your own permissions."
5. Verifikasi baris Siti Rahmawati (TC lain) dan Budi Hartono (RO) memiliki checkbox yang dapat diedit oleh Total Control
6. Logout dan login sebagai akun manageUserRoleUpdate
7. Buka Tab System > Detail role 'Manage user and role'
8. Verifikasi baris diri sendiri (manageUserRoleUpdate) memiliki checkbox CRUD disabled dengan tooltip self-edit
9. Verifikasi baris Siti Rahmawati (TC) dan Budi Hartono (RO) memiliki checkbox CRUD disabled dengan tooltip pembatasan akses khusus Total Control
10. Verifikasi baris Doni Pratama (user reguler) memiliki checkbox CRUD enabled dan dapat disunting oleh aktor Update ini

## Notes

- Proteksi self-edit berlaku mutlak untuk semua tier termasuk Total Control (ROLE-LOGIC-01). Target berstatus TC/RO hanya boleh disentuh Total Control (ROLE-LOGIC-03).
