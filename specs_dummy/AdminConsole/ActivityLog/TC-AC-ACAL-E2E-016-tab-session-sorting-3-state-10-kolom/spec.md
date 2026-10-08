---
id: TC-AC-ACAL-E2E-016-tab-session-sorting-3-state-10-kolom
title: "Tab Session — Sorting 3-state pada 9 kolom sortable dan guard kolom Status tidak sortable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-68
  - TC-AC-ACAL-69
  - TC-AC-ACAL-70
  - TC-AC-ACAL-71
  - TC-AC-ACAL-72
  - TC-AC-ACAL-73
  - TC-AC-ACAL-74
  - TC-AC-ACAL-75
  - TC-AC-ACAL-76
coverage:
  web: automated
---

# Tab Session — Sorting 3-state pada 9 kolom sortable dan guard kolom Status tidak sortable

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data yang cukup dengan variasi nilai pada setiap kolom

## Test Steps

### Siklus 3-State Sort Kolom Sortable

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Klik ikon sort kolom `Date` sebanyak 3 kali berturut-turut
3. Verifikasi urutan: Klik 1 = Newest First (Desc), Klik 2 = Oldest First (Asc), Klik 3 = Netral (kembali ke default)
4. Lakukan pengujian siklus 3-state (Ascending A-Z &rarr; Descending Z-A &rarr; Netral) untuk setiap kolom berikut:
   - `User`
   - `Employee ID`
   - `Position`
   - `Division`
   - `Activity`
   - `Note`
   - `IP Address`
   - `Device / Browser`
5. Verifikasi pengurutan data di tabel berubah sesuai status sort yang aktif pada setiap klik

### Guard Kolom Status

6. Amati header kolom `Status`
7. Verifikasi tidak ada icon sort pada kolom Status dan header tidak dapat diklik untuk sorting (karena nilainya konstan `"—"`)

## Notes

- TAG Samurai menerapkan siklus sorting 3-state standar: Ascending &rarr; Descending &rarr; Neutral.
