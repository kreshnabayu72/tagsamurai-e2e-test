---
id: TC-GS-ACTLOG-E2E-045-client-suspended-tetap-dapat-melihat-riwayat-log
title: "D1 Client Suspended/Expired tetap dapat mengakses dan melihat riwayat log Activity Log"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-232
coverage:
  web: automated
---

# D1 Client Suspended/Expired tetap dapat mengakses dan melihat riwayat log Activity Log

## Prerequisites

- Login sebagai Total Control pada entitas client yang berstatus Suspended atau Expired

## Test Steps

1. Login sebagai Total Control pada entitas client yang sedang berstatus Suspended
2. Buka menu `Global Settings > Activity Log`
3. Verifikasi halaman Activity Log tetap terbuka normal dan dapat diakses (read-only unaffected)
4. Verifikasi riwayat log pada Tab Session dan Tab User Action tetap tampil lengkap dan fitur table tools tetap berfungsi

## Notes

- Client suspended diblokir dari aksi mutasi tulis, namun hak audit log historis tetap dipertahankan.
