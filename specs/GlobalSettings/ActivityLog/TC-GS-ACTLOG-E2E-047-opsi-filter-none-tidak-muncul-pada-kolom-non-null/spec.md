---
id: TC-GS-ACTLOG-E2E-047-opsi-filter-none-tidak-muncul-pada-kolom-non-null
title: "D5 Opsi filter None tidak muncul pada dropdown Activity dan Action karena kolom non-nullable"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-236
coverage:
  web: automated
---

# D5 Opsi filter None tidak muncul pada dropdown Activity dan Action karena kolom non-nullable

## Prerequisites

- Login sebagai Total Control membuka Filter Panel pada Tab Session dan Tab User Action

## Test Steps

1. Buka Filter Panel pada Tab Session lalu buka dropdown Activity
2. Periksa seluruh daftar opsi yang tersedia
3. Verifikasi opsi "None" tidak muncul di dalam dropdown Activity karena field Activity tidak pernah bernilai null
4. Klik tab "User Action", buka Filter Panel lalu buka dropdown Action
5. Periksa seluruh daftar opsi yang tersedia
6. Verifikasi opsi "None" tidak muncul di dalam dropdown Action karena field Action tidak pernah bernilai null

## Notes

- Opsi None hanya valid untuk kolom foreign-key atau opsional yang mengizinkan nilai null.
