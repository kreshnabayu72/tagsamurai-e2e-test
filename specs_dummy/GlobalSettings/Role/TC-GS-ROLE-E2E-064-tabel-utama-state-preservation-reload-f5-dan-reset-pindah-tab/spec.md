---
id: TC-GS-ROLE-E2E-064-tabel-utama-state-preservation-reload-f5-dan-reset-pindah-tab
title: "State Preservation Tabel Utama: Persistensi Filter/Sort Pasca-Reload F5 dan Reset Bersih Saat Pindah Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-160
  - TC-GS-ROLE-161
coverage:
  web: automated
---

# State Preservation Tabel Utama: Persistensi Filter/Sort Pasca-Reload F5 dan Reset Bersih Saat Pindah Tab

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup data tabel utama
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda

## Test Steps

### Refresh F5 mempertahankan Search, Filter, Sort, dan halaman (TC-GS-ROLE-160)

1. Tab Total Control: Search "a", Filter Status Active, Sort Name Z-A, halaman 2
2. Tekan F5
3. Verifikasi Keyword, filter, sort, halaman, dan page size tetap sama setelah refresh

### State Search/Filter/Sort saat pindah Tab Total Control ↔ Read Only ↔ System (TC-GS-ROLE-161)

4. Tab Total Control: Search "a" + Filter Status Active
5. Klik Tab Read Only
6. Kembali ke Tab Total Control
7. Verifikasi Tab Read Only tampil dengan kondisi default (tanpa search/filter)
8. Verifikasi Kembali ke Tab Total Control: search dan filter direset ke default

## Notes

- Memvalidasi alur skenario "State Preservation Tabel Utama: Persistensi Filter/Sort Pasca-Reload F5 dan Reset Bersih Saat Pindah Tab".
- Aturan PRD terkait: global-settings/role/PRD/role.md §5 Pagination; foundation/process/prd-process/prd-conventions.md §27.1c; global-settings/role/PRD/role.md §5.
- Sumber pemetaan test case granular: TC-GS-ROLE-160, TC-GS-ROLE-161.
