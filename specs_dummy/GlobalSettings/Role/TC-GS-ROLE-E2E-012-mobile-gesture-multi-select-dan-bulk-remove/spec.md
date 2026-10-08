---
id: TC-GS-ROLE-E2E-012-mobile-gesture-multi-select-dan-bulk-remove
title: "Gesture Layar Sentuh Mobile Android: Long-Press Multi-Select dan Aksi Bulk Remove pada Detail"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-32
coverage:
  web: automated
---

# Gesture Layar Sentuh Mobile Android: Long-Press Multi-Select dan Aksi Bulk Remove pada Detail

## Prerequisites

- Viewport emulasi mobile/touch; login sebagai Total Control
- Data Uji: Pre-setup #10 (Doni Pratama dkk.)
- Setup Hook: beforeEach: setMobileViewport()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Aplikasi Android native

## Test Steps

### Mobile — Detail multi-select lewat long press dan bulk Remove (TC-GS-ROLE-32)

1. Buka Role & Permission > System > Detail "Manage TAG" di aplikasi mobile
2. Long-press card Doni Pratama
3. Amati sticky bottom bar
4. Verifikasi Card per user menampilkan toggle Read dan Update saja (tanpa Create/Delete)
5. Verifikasi Long press masuk mode checkbox: card Doni Pratama tercentang dan sticky bottom bar menampilkan aksi bulk Remove
6. Verifikasi Row action Remove tetap tersedia via [⋯] pada card

## Notes

- Memvalidasi alur skenario "Gesture Layar Sentuh Mobile Android: Long-Press Multi-Select dan Aksi Bulk Remove pada Detail".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.6; global-settings/role/PRD/role.md §4.8 Bulk; foundation/process/prd-process/prd-conventions.md §13.4.
- Sumber pemetaan test case granular: TC-GS-ROLE-32.
