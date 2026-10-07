---
id: TC-GS-ACTLOG-E2E-012-role-matrix-negatif-pengguna-tanpa-akses
title: "Role Matrix Negatif: Penolakan Akses Menu dan Direct URL untuk Pengguna Tanpa Akses"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-30
  - TC-GS-ACTLOG-31
  - TC-GS-ACTLOG-32
  - TC-GS-ACTLOG-33
  - TC-GS-ACTLOG-34
coverage:
  web: automated
---

# Role Matrix Negatif: Penolakan Akses Menu dan Direct URL untuk Pengguna Tanpa Akses

## Prerequisites

- Akun uji tanpa akses Activity Log:
- 1. Create-Only Brand (pemegang capability individual tanpa access level)
- 2. Full CRUD Brand (pemegang capability modul tanpa access level)
- 3. System Role
- 4. Admin Console See-All (akses baca Admin Console tanpa akses GS)

## Test Steps

### Pemeriksaan Menu Sidebar (Hidden)
1. Login sebagai Create-Only Brand, periksa sidebar Global Settings, verifikasi menu 'Activity Log' tersembunyi (Hidden).
2. Login sebagai Full CRUD Brand, verifikasi menu 'Activity Log' tersembunyi (Hidden).
3. Login sebagai System Role, verifikasi menu 'Activity Log' tersembunyi (Hidden).
4. Login sebagai Admin Console See-All, verifikasi menu 'Activity Log' di Global Settings tersembunyi (Hidden).
### Penolakan Akses Direct URL
5. Menggunakan sesi Admin Console See-All, buka langsung URL '/global-settings/activity-log/session' di address bar browser.
6. Verifikasi sistem memblokir akses, memunculkan toast error "You don't have permission to do this.", dan tidak menampilkan data log.
7. Menggunakan sesi Create-Only Brand, buka langsung URL '/global-settings/activity-log/session'.
8. Verifikasi akses diblokir dengan toast error "You don't have permission to do this.".
9. Buka langsung URL '/global-settings/activity-log/user-action' dengan sesi Create-Only Brand.
10. Verifikasi akses diblokir dengan toast error "You don't have permission to do this." tanpa redirect ke halaman unauthorized terpisah.

## Notes

- Akses menu Activity Log terlindungi penuh di UI dan server (defense-in-depth).
