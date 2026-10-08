---
id: TC-AC-SG-E2E-017-entity-suspended-blanket-read-only
title: "Kebijakan Entity Suspended: Penonaktifan seluruh kontrol mutasi Create, Edit, dan Delete"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-68
  - TC-AC-SG-169
coverage:
  web: automated
---

# Kebijakan Entity Suspended: Penonaktifan seluruh kontrol mutasi Create, Edit, dan Delete

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Workspace entitas berada dalam status Suspended (mock state / status mutator)

## Test Steps

### Verifikasi Kontrol Mutasi Terkunci (Disabled)
1. Buka halaman `Settings > Group` pada entitas berstatus Suspended
2. Verifikasi tombol `[+ New Group]` pada sidebar berstatus Disabled di UI
3. Klik tombol elipsis `[⋯]` pada baris tabel dan node sidebar
4. Verifikasi opsi `+ Add Subgroup`, `Edit`, dan `Delete` seluruhnya berstatus Disabled (tidak dapat diklik)
5. Verifikasi tidak ada modal Create atau Edit yang dapat terbuka
6. Lakukan percobaan bypass request DELETE via API langsung
7. Verifikasi backend menolak permintaan dengan status HTTP 403 Forbidden

## Notes

- Kebijakan blanket read-only berlaku tanpa pengecualian di seluruh modul Admin Console saat entitas suspended.
