---
id: TC-GS-ROLE-E2E-037-remove-read-only-happy-path-single-user
title: "Pencabutan Read Only Berhasil pada User Aktif: Pembersihan Hak Akses dan Pencatatan Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-88
coverage:
  web: automated
---

# Pencabutan Read Only Berhasil pada User Aktif: Pembersihan Hak Akses dan Pencatatan Log

## Prerequisites

- Login sebagai Total Control
- Data Uji: Rina Putri (Pre-setup #4)
- Setup Hook: beforeEach: navigateTo(Tab Read Only)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Read Only
- Rahmat Hidayat Read Only

## Test Steps

### Screening dialog dan Remove Read Only (TC-GS-ROLE-88)

1. Klik Remove baris Rahmat Hidayat
2. Screening dialog
3. Klik [Remove]
4. Verifikasi Title "Remove Read Only"; body "• Rahmat Hidayat" + "This will remove Read Only from this user. Their individual permissions will be reset and they will have no access assigned. Are you sure you want to remove it?"; `[Cancel]` | `[Remove]`
5. Verifikasi Toast sukses: "Success, Read Only has been removed."
6. Verifikasi Rahmat Hidayat hilang dari Tab Read Only dan dari semua Detail

## Notes

- Memvalidasi alur skenario "Pencabutan Read Only Berhasil pada User Aktif: Pembersihan Hak Akses dan Pencatatan Log".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-01; global-settings/role/PRD/role.md §9.2 [F-ROLE-05].
- Sumber pemetaan test case granular: TC-GS-ROLE-88.
