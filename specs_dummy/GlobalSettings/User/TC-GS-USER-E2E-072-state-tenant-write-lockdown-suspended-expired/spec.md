---
id: TC-GS-USER-E2E-072-state-tenant-write-lockdown-suspended-expired
title: "State Tenant: Write-lockdown kontrol tulis saat Client berstatus Suspended atau Expired"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-984
  - TC-GS-USER-1021
  - TC-GS-USER-1022
  - TC-GS-USER-1023
  - TC-GS-USER-1024
  - TC-GS-USER-1025
  - TC-GS-USER-1026
coverage:
  web: automated
---

# State Tenant: Write-lockdown kontrol tulis saat Client berstatus Suspended atau Expired

## Prerequisites

- Client berstatus Suspended atau Expired

## Test Steps

### Penguncian Kontrol Tulis Tenant

1. Buka Global Settings > User > User List pada client yang berstatus Suspended
2. Hover tombol '[+ User]' dan switch Active, verifikasi kontrol disabled dengan tooltip permission
3. Buka menu (⋯), verifikasi opsi Edit dan Delete disabled
4. Coba kirim mutasi data langsung via request, verifikasi toast error bahwa workspace sedang suspended/expired

## Notes

- Menggabungkan 7 test case granular (TC-GS-USER-984 s.d. TC-GS-USER-1026).
