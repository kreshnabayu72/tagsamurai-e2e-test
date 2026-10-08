---
id: TC-AC-SG-E2E-046-popup-total-member-screening-phase-1-dan-filter
title: "Screening drill-down Total Member Phase 1 (Client direct only), filter, dan Column Visibility"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-84
  - TC-AC-SG-85
  - TC-AC-SG-87
  - TC-AC-SG-88
  - TC-AC-SG-162
coverage:
  web: automated
---

# Screening drill-down Total Member Phase 1 (Client direct only), filter, dan Column Visibility

## Prerequisites

- Login sebagai Role: Total Control
- Node target memiliki Total Member > 0 (Client ter-assign langsung)

## Test Steps

### Screening Drill-Down & Header
1. Klik angka pada kolom Total Member pada baris target di tabel utama
2. Verifikasi popup `"Members"` terbuka
3. Verifikasi header memuat `"Group Name: [nama]"` dan `"Total Member: [N]"`
4. Verifikasi tabel memuat 4 kolom: `Entity Name`, `Type`, `Relation Status`, `Last Updated`, dan kolom header `⋯`
### Batasan Phase 1: Client Direct Only
5. Amati nilai pada kolom `Type` di seluruh baris tabel popup
6. Verifikasi kolom Type SELALU BERNILAI `"Client"` (Phase 1 hanya mencakup direct Client assignment, ACSG-LOGIC-04)
### Screening Dropdown Filter & Search
7. Buka Filter Panel popup
8. Buka dropdown Type dan verifikasi hanya memuat opsi tunggal `"Client"`
9. Buka dropdown Relation Status dan verifikasi opsi terisi dinamis dari status entitas member
10. Uji pencarian Entity Name dan filter tanggal Last Updated
11. Klik header kolom `⋯` dan verifikasi dropdown Column Visibility terbuka tanpa row action

## Notes

- TC-AC-SG-86 (skema tabel tanpa ac_group_member) divalidasi pada pengujian backend.
