---
id: TC-GS-USER-E2E-017-role-matrix-negatif-aksi-tulis-oleh-read-only
title: "Role Matrix Negatif: Penolakan seluruh aksi mutasi data oleh aktor Read Only"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-68
  - TC-GS-USER-69
  - TC-GS-USER-70
  - TC-GS-USER-71
coverage:
  web: automated
---

# Role Matrix Negatif: Penolakan seluruh aksi mutasi data oleh aktor Read Only

## Prerequisites

- Login sebagai Role: Read Only (Yudi Pratomo)
- Pre-setup User tersedia di User List

## Test Steps

### Penolakan Aksi di UI

1. Buka Global Settings > User > User List
2. Verifikasi tombol '[+ User]' disabled
3. Buka menu (⋯) pada baris user mana pun, verifikasi opsi Edit, Delete, Resend Email, dan Toggle disabled atau hidden
4. Verifikasi tidak ada form modal create/edit yang dapat disubmit

## Notes

- Menggabungkan 4 test case granular (TC-GS-USER-68 s.d. TC-GS-USER-71).
