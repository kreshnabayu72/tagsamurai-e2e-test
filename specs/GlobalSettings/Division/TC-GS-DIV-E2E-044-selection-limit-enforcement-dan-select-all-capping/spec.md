---
id: TC-GS-DIV-E2E-044-selection-limit-enforcement-dan-select-all-capping
title: "Selection Limit: Penonaktifan Checkbox Melewati Batas dan Capping Parsial Select All"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-129
  - TC-GS-DIV-130
coverage:
  web: automated
---

# Selection Limit: Penonaktifan Checkbox Melewati Batas dan Capping Parsial Select All

## Prerequisites

- Login sebagai Role: Total Control
- Selection Limit diset 5 (Admin Console > Plans & Licensing > Lifecycle Settings > System Limits)
- Tabel Division terisi 32 baris tanpa filter (TC-GS-DIV-30)
- User berada di Global Settings > User > Division
- Selection Limit diset 5 dan total baris 32 (TC-GS-DIV-30)

## Test Steps

### Selection Limit: checkbox melewati batas disabled saat dicentang satu per satu (TC-GS-DIV-129)

1. Centang 5 baris pertama satu per satu
2. Coba centang baris ke-6
3. Hover checkbox baris ke-6
4. Verifikasi Baris ke-1 sampai ke-5 tercentang dan Bulk Action Bar tetap aktif
5. Verifikasi Checkbox baris ke-6 disabled
6. Verifikasi Tooltip: `You've reached the maximum selection of 5 rows.`

### Selection Limit: Select All di-cap ke batas dengan toast error persist (TC-GS-DIV-130)

7. Klik `Select All (32 records)`
8. Verifikasi Seleksi di-cap ke 5 baris pertama (bukan diblok total dan bukan dialog)
9. Verifikasi Toast error persist: `Error, only the first 5 of 32 rows were selected. Narrow your filter to include the rest.`
10. Verifikasi Bulk Action Bar tetap tampil dan dapat dipakai untuk 5 baris

## Notes

- Memvalidasi penegakan batasan kuota seleksi sistem (Selection Limit: 5): checkbox baris ke-6 disabled dengan tooltip "You've reached the maximum selection of 5 rows.", serta tombol Select All (32 records) di-cap ke 5 baris pertama dengan persistent toast error warning (prd-conventions.md §8 Selection Limit, testcase-conventions.md P1 §1e).
- Sumber pemetaan test case granular: TC-GS-DIV-129, TC-GS-DIV-130.
