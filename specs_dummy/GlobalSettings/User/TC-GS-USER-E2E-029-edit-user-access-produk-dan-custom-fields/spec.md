---
id: TC-GS-USER-E2E-029-edit-user-access-produk-dan-custom-fields
title: "Edit User: Penambahan/pencabutan Access produk dan modifikasi nilai custom fields"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-221
  - TC-GS-USER-222
  - TC-GS-USER-223
  - TC-GS-USER-224
  - TC-GS-USER-225
  - TC-GS-USER-226
  - TC-GS-USER-227
  - TC-GS-USER-228
  - TC-GS-USER-229
  - TC-GS-USER-230
  - TC-GS-USER-231
  - TC-GS-USER-232
  - TC-GS-USER-233
  - TC-GS-USER-234
  - TC-GS-USER-235
  - TC-GS-USER-236
  - TC-GS-USER-237
  - TC-GS-USER-238
  - TC-GS-USER-239
  - TC-GS-USER-240
coverage:
  web: automated
---

# Edit User: Penambahan/pencabutan Access produk dan modifikasi nilai custom fields

## Prerequisites

- Login sebagai Role: Total Control
- User target memiliki akses multi-produk

## Test Steps

### Modifikasi Access dan Custom Fields

1. Buka modal Edit Dewi Lestari
2. Centang tambahan produk 'Supply Asset' pada checklist Access
3. Perbarui nilai Custom Field Blood Type
4. Klik '[Save]'
5. Verifikasi sel Access di User List kini menampilkan penambahan produk

## Notes

- Menggabungkan 20 test case granular (TC-GS-USER-221 s.d. TC-GS-USER-240).
