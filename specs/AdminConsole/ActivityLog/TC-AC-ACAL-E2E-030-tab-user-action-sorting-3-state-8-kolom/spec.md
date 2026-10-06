---
id: TC-AC-ACAL-E2E-030-tab-user-action-sorting-3-state-8-kolom
title: "Tab User Action — Sorting 3-state pada 6 kolom sortable dan guard kolom Old/New Value tidak sortable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-160
  - TC-AC-ACAL-161
  - TC-AC-ACAL-162
  - TC-AC-ACAL-163
  - TC-AC-ACAL-164
  - TC-AC-ACAL-165
  - TC-AC-ACAL-166
  - TC-AC-ACAL-167
coverage:
  web: automated
---

# Tab User Action — Sorting 3-state pada 6 kolom sortable dan guard kolom Old/New Value tidak sortable

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data aktivitas dengan nilai bervariasi

## Test Steps

### Siklus 3-State Sort Kolom Sortable

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Klik ikon sort kolom `Date` sebanyak 3 kali berturut-turut
3. Verifikasi urutan: Newest First &rarr; Oldest First &rarr; Netral
4. Lakukan pengujian siklus 3-state (Ascending A-Z &rarr; Descending Z-A &rarr; Netral) untuk setiap kolom berikut:
   - `Action`
   - `Object`
   - `Name`
   - `Field`
   - `Modified By`
5. Verifikasi pengurutan data di tabel berubah sesuai status sort yang aktif

### Guard Kolom Old Value & New Value

6. Amati header kolom `Old Value` dan `New Value`
7. Verifikasi kedua kolom tersebut tidak memiliki icon sort dan tidak dapat di-sort (karena berisi nilai free-form log content yang tidak enumerable)

## Notes

- Kolom Old Value dan New Value dikecualikan dari operasi sorting untuk menjaga performa dan relevansi data log.
