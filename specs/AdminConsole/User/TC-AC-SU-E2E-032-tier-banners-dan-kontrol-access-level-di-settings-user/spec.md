---
id: TC-AC-SU-E2E-032-tier-banners-dan-kontrol-access-level-di-settings-user
title: "Banner tier di Tab Role (Total Control, Read Only, Group Manager) dan ketiadaan kontrol assign tier di Settings > User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-102
  - TC-AC-SU-103
  - TC-AC-SU-104
  - TC-AC-SU-105
coverage:
  web: automated
---

# Banner tier di Tab Role (Total Control, Read Only, Group Manager) dan ketiadaan kontrol assign tier di Settings > User

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat target pengguna dengan tier Total Control, Read Only, dan Group Manager (2 group)

## Test Steps

### Verifikasi Banner Total Control, Read Only, dan Group Manager

1. Buka Detail User > Tab Role untuk pengguna berstatus `access_level = total_control`
2. Verifikasi banner informasi muncul di atas tab: `"This user has Total Control access."`
3. Buka Detail User > Tab Role untuk pengguna berstatus `access_level = read_only`
4. Verifikasi banner informasi muncul di atas tab: `"This user has Read Only access."`
5. Buka Detail User > Tab Role untuk pengguna yang menjadi Group Manager di Group A dan Group B
6. Verifikasi banner informasi muncul: `"This user is a Group Manager for: [Group A], [Group B]."`

### Verifikasi Ketiadaan Kontrol Assign/Remove Access Level di Settings > User

1. Periksa area banner dan toolbar Tab Role pada ketiga pengguna tersebut
2. Verifikasi TIDAK ADA tombol `Assign Tier` atau `Remove Tier` di modul Settings > User
3. Verifikasi penugasan dan pencabutan tier tier access_level secara eksplisit hanya dapat dilakukan dari menu `Settings > Role & Permission`

## Notes

- Settings > User menampilkan status tier sebagai informasi dan auto-revert target.
