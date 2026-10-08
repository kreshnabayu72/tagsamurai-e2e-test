---
id: TC-GS-ROLE-E2E-002-screening-tab-read-only-dan-empty-state
title: "Screening Tab Read Only, Eksklusi Default User, dan Empty State Saat Tanpa User Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-2
  - TC-GS-ROLE-11
  - TC-GS-ROLE-18
coverage:
  web: automated
---

# Screening Tab Read Only, Eksklusi Default User, dan Empty State Saat Tanpa User Read Only

## Prerequisites

- Login sebagai Role: Total Control (Ahmad Fauzi)
- Data Uji: Pre-setup #4 (Siti Nurhaliza, Rina Putri), Pre-setup #14 (Client tanpa RO)
- Setup Hook: beforeEach: navigateTo(Role & Permission > Read Only)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup #4 (Siti Nurhaliza RO Active, Rina Putri RO Inactive) tersedia
- User berada di Global Settings > Role & Permission > Total Control
- Dewi Lestari TC dengan status user Inactive (Pre-setup #3)
- Client uji tanpa user Read Only (Pre-setup #14)
- User berada di Global Settings > Role & Permission > Read Only

## Test Steps

### Screening halaman Role & Permission Tab Read Only (web) (TC-GS-ROLE-2)

1. Buka Global Settings > Role & Permission
2. Klik Tab Read Only
3. Screening halaman dari atas ke bawah
4. Verifikasi **Header**:
5. Verifikasi Breadcrumb: "Role & Permission > Read Only"; segmen "Read Only" bukan link
6. Verifikasi Tab: `Total Control | Read Only (aktif) | System`
7. Verifikasi Table Tools: `Search | Filter | Download | Changelog | [+ Assign]`
8. Verifikasi Section description: "Read Only applies to Global Settings only — it does not grant access to other TAG Samurai products."
9. Verifikasi **Body**:
10. Verifikasi Kolom: `Name (sortable) | Position (sortable) | Division (sortable) | Status (sortable) | Modified By (sortable) | Last Updated (sortable) | Actions (⋯) (unsortable — header = overlay Column Visibility, body = row action Remove)`
11. Verifikasi Baris Siti Nurhaliza (Status Active) dan Rina Putri (Status Inactive) tampil; tidak ada baris Default User
12. Verifikasi Tidak ada kolom checkbox seleksi dan tidak ada kolom CRUD
13. Verifikasi **Footer**: Pagination default 10 baris/halaman

### User Inactive tetap tampil di Tab Total Control (TC-GS-ROLE-11)

14. Amati baris Dewi Lestari
15. Verifikasi Baris Dewi Lestari tampil dengan badge Status "Inactive"
16. Verifikasi Row action Remove pada baris itu enabled

### Empty state Tab Read Only tanpa user Read Only (TC-GS-ROLE-18)

17. Amati area tabel
18. Verifikasi Illustration + Title "No users assigned" + Description "Users with read only access will appear here."

## Notes

- Memvalidasi alur skenario "Screening Tab Read Only, Eksklusi Default User, dan Empty State Saat Tanpa User Read Only".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Tab: Read Only; global-settings/role/PRD/role.md §4.1.2; global-settings/role/PRD/role.md §5; global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §9.7; global-settings/role/PRD/role.md §7.1 S-06.
- Sumber pemetaan test case granular: TC-GS-ROLE-2, TC-GS-ROLE-11, TC-GS-ROLE-18.
