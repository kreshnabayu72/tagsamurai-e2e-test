---
id: TC-GS-USER-E2E-027-edit-user-happy-path-update-profil
title: "Edit User: Happy path update informasi profil, posisi, divisi, dan verifikasi list"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-191
  - TC-GS-USER-192
  - TC-GS-USER-193
  - TC-GS-USER-194
  - TC-GS-USER-195
  - TC-GS-USER-196
  - TC-GS-USER-197
  - TC-GS-USER-198
  - TC-GS-USER-199
  - TC-GS-USER-200
  - TC-GS-USER-1009
  - TC-GS-USER-1010
coverage:
  web: automated
---

# Edit User: Happy path update informasi profil, posisi, divisi, dan verifikasi list

## Prerequisites

- Login sebagai Role: Total Control
- User target Dewi Lestari tersedia

## Test Steps

### Pembaruan Data Profil

1. Buka modal Edit user Dewi Lestari
2. Ubah Position menjadi 'Supervisor' dan Phone menjadi nomor baru
3. Klik tombol '[Save]'
4. Verifikasi toast 'User updated successfully.' tampil dan modal tertutup
5. Verifikasi baris Dewi Lestari di User List menampilkan Position baru 'Supervisor' dan Last Update terperbarui

## Notes

- Menggabungkan 12 test case granular (TC-GS-USER-191 s.d. TC-GS-USER-1010).
