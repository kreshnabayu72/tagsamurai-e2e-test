---
id: TC-AC-ACAL-E2E-027-tab-user-action-populate-opsi-filter-dinamis
title: "Tab User Action — Populasi opsi dropdown filter Action, Object, dan Modified By secara dinamis"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-143
  - TC-AC-ACAL-144
  - TC-AC-ACAL-145
coverage:
  web: automated
---

# Tab User Action — Populasi opsi dropdown filter Action, Object, dan Modified By secara dinamis

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data dari beberapa Action, Object, dan Modified By tertentu saja

## Test Steps

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Klik tombol `[Filter]` pada toolbar
3. Buka dropdown field `Action`
4. Verifikasi daftar pilihan hanya memuat jenis-jenis Action yang DISTINCT dan benar-benar tercatat pada riwayat log saat ini
5. Buka dropdown field `Object`
6. Verifikasi daftar pilihan hanya memuat DISTINCT Object (misal: Distributor, Partner, Client) yang tercatat di log
7. Buka dropdown field `Modified By`
8. Verifikasi daftar pilihan hanya memuat DISTINCT nama pengguna yang telah melakukan mutasi data pada riwayat log

## Notes

- Memastikan filter dropdown terisi dinamis dari endpoint `/v2/analytics-reporting/change-logs/options`.
