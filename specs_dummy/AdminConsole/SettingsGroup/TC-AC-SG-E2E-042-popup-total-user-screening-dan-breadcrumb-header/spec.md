---
id: TC-AC-SG-E2E-042-popup-total-user-screening-dan-breadcrumb-header
title: "Screening popup drill-down Total User, breadcrumb full path header, dan inklusi akun Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-79
  - TC-AC-SG-80
  - TC-AC-SG-83
  - TC-AC-SG-155
coverage:
  web: automated
---

# Screening popup drill-down Total User, breadcrumb full path header, dan inklusi akun Total Control

## Prerequisites

- Login sebagai Role: Total Control
- Node subgroup level 2 `"Branch 1"` di bawah `"Region A"` dengan Total User > 0

## Test Steps

### Drill-Down & Breadcrumb Header
1. Buka `Settings > Group` dan cari baris `"Branch 1"`
2. Klik angka pada kolom Total User
3. Verifikasi popup `"Users"` terbuka
4. Verifikasi header popup menampilkan 2 baris terpisah:
   - Baris 1: Full path breadcrumb `"Group Name: Region A › Branch 1"`
   - Baris 2: `"Total User: [N]"`
5. Verifikasi tabel popup memuat 5 kolom default: `Name`, `Email`, `Position`, `Division`, `Group Role`
### Inklusi Aktor Total Control & Read Only
6. Amati daftar user pada tabel popup
7. Verifikasi akun Total Control dan Read Only entitas SELALU MUNCUL di dalam daftar (karena scope mereka full-tree)
8. Tutup popup, buka popup pada node dengan 0 penugasan lokal, verifikasi popup tetap terbuka normal merender user TC/RO

## Notes

- Header popup subgroup menampilkan full path breadcrumb untuk disambiguasi nama yang sama di cabang lain.
