---
id: TC-GS-ROLE-E2E-007-empty-state-pencarian-no-results-found
title: "Empty State Hasil Pencarian No Results Found pada Tab Total Control, Read Only, System, dan Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-19
coverage:
  web: automated
---

# Empty State Hasil Pencarian No Results Found pada Tab Total Control, Read Only, System, dan Detail

## Prerequisites

- Login sebagai Role: Total Control
- Data Uji: Keyword tanpa hasil: zzqx
- Setup Hook: beforeEach: navigateTo(Tab aktif)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia

## Test Steps

### No-result state pada Tab Total Control, Read Only, System, dan Detail (TC-GS-ROLE-19)

1. Di Tab Total Control: Search "zzqx" + Enter
2. Ulangi di Tab Read Only
3. Ulangi di Tab System
4. Ulangi di Detail "Manage TAG"
5. Verifikasi Tab Total Control: Illustration + Title "No results found" + Description "Try adjusting your search or filter."
6. Verifikasi Tab Read Only: idem
7. Verifikasi Tab System: idem
8. Verifikasi Detail: idem

## Notes

- Memvalidasi alur skenario "Empty State Hasil Pencarian No Results Found pada Tab Total Control, Read Only, System, dan Detail".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 S-06; global-settings/role/PRD/role.md §7.1 S-07; global-settings/role/PRD/role.md §7.1 S-08; global-settings/role/PRD/role.md §7.1 S-09.
- Sumber pemetaan test case granular: TC-GS-ROLE-19.
