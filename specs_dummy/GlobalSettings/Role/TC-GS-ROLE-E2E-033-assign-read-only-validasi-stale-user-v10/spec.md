---
id: TC-GS-ROLE-E2E-033-assign-read-only-validasi-stale-user-v10
title: "Validasi Stale User V-10 pada Penugasan Read Only: Penolakan Alert Inline Saat Kandidat Dihapus Sesi Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-81
coverage:
  web: automated
---

# Validasi Stale User V-10 pada Penugasan Read Only: Penolakan Alert Inline Saat Kandidat Dihapus Sesi Lain

## Prerequisites

- Dual session context (Sesi A dan Sesi B Total Control)
- Data Uji: Wawan Setiawan (Pre-setup #11)
- Setup Hook: dualContext: sessionA, sessionB
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Read Only
- Response Assign dibuat gagal 5xx

## Test Steps

### Assign Read Only gagal 5xx (TC-GS-ROLE-81)

1. Klik [+ Assign]
2. Centang Wawan Setiawan
3. Klik [Assign]
4. Verifikasi Muncul toast error: "Error, failed to assign Read Only."
5. Verifikasi Popup tetap terbuka dengan seleksi dipertahankan
6. Verifikasi Wawan Setiawan tidak muncul di Tab Read Only

## Notes

- Memvalidasi alur skenario "Validasi Stale User V-10 pada Penugasan Read Only: Penolakan Alert Inline Saat Kandidat Dihapus Sesi Lain".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 T-04; global-settings/role/PRD/role.md §9.6 Assign access level; global-settings/role/PRD/role.md §9.6 Delta modul ini.
- Sumber pemetaan test case granular: TC-GS-ROLE-81.
