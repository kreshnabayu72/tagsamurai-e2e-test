---
id: TC-GS-ROLE-E2E-019-aksesibilitas-keyboard-dan-fokus-dialog
title: "Aksesibilitas Antarmuka: Navigasi Keyboard Tab + Space Sel CRUD dan Focus Trap Modal Dialog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-47
  - TC-GS-ROLE-48
coverage:
  web: automated
---

# Aksesibilitas Antarmuka: Navigasi Keyboard Tab + Space Sel CRUD dan Focus Trap Modal Dialog

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup #1, #10
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Doni Pratama punya baris Manage TAG dengan Update unchecked
- User berada di Global Settings > Role & Permission > Total Control

## Test Steps

### Accessibility — checkbox Detail operable keyboard dan tooltip saat fokus (TC-GS-ROLE-47)

1. Buka Detail "Manage TAG"
2. Tekan Tab sampai fokus di checkbox Update Doni Pratama, tekan Space
3. Tekan Tab sampai fokus di checkbox Update baris Budi Santoso
4. Verifikasi Langkah 2: checkbox berubah checked dan muncul toast sukses: "Success, permissions have been updated."
5. Verifikasi Langkah 3: checkbox disabled menerima fokus dan tooltip "Default User cannot be modified." tampil saat fokus

### Accessibility — dialog konfirmasi focus trapped dan Esc menutup (TC-GS-ROLE-48)

6. Klik Remove pada baris Dewi Lestari
7. Tekan Tab berulang
8. Tekan Esc
9. Verifikasi Fokus berputar di dalam dialog (Cancel, Remove)
10. Verifikasi Esc menutup dialog tanpa perubahan; baris Dewi Lestari tetap ada

## Notes

- Memvalidasi alur skenario "Aksesibilitas Antarmuka: Navigasi Keyboard Tab + Space Sel CRUD dan Focus Trap Modal Dialog".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.5.
- Sumber pemetaan test case granular: TC-GS-ROLE-47, TC-GS-ROLE-48.
