---
id: TC-AC-ACAL-E2E-013-tab-session-populate-opsi-filter-dinamis
title: "Tab Session — Populasi opsi dropdown filter User, Position, dan Division terisi secara dinamis dari log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-51
  - TC-AC-ACAL-52
  - TC-AC-ACAL-53
coverage:
  web: automated
---

# Tab Session — Populasi opsi dropdown filter User, Position, dan Division terisi secara dinamis dari log

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data dari beberapa User, Position, dan Division tertentu saja
- Terdapat data User di master data platform yang belum pernah login/membuat sesi di Admin Console

## Test Steps

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Klik tombol `[Filter]` pada toolbar
3. Buka dropdown field `User`
4. Verifikasi daftar opsi dropdown hanya memuat nama-nama User yang DISTINCT dan benar-benar tercatat pada log Tab Session saat ini (User yang tidak memiliki riwayat log tidak muncul)
5. Buka dropdown field `Position`
6. Verifikasi daftar opsi hanya memuat DISTINCT Position yang dimiliki oleh user pada riwayat log saat ini
7. Buka dropdown field `Division`
8. Verifikasi daftar opsi hanya memuat DISTINCT Division yang terdapat pada riwayat log saat ini

## Notes

- Memastikan filter dropdown terisi dinamis (data-driven) dari endpoint `/v2/analytics-reporting/session-logs/options`, bukan hardcoded atau mengambil seluruh master data tanpa filter riwayat.
