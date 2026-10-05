---
id: TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel
title: "Tab Session: Pembekuan kolom sticky pin/unpin, reset ke default, dan pembatalan perubahan Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-108
  - TC-GS-ACTLOG-109
  - TC-GS-ACTLOG-110
  - TC-GS-ACTLOG-111
  - TC-GS-ACTLOG-112
  - TC-GS-ACTLOG-113
  - TC-GS-ACTLOG-114
  - TC-GS-ACTLOG-115
  - TC-GS-ACTLOG-116
  - TC-GS-ACTLOG-117
  - TC-GS-ACTLOG-118
  - TC-GS-ACTLOG-119
coverage:
  web: automated
---

# Tab Session: Pembekuan kolom sticky pin/unpin, reset ke default, dan pembatalan perubahan Setup Column

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session di modal Setup Column

## Test Steps

1. Buka modal Setup Column pada Tab Session
2. Klik icon Pin pada kolom User dan Date lalu klik `[Save]`
3. Geser scrollbar horizontal tabel dan verifikasi kolom yang di-pin membeku (sticky) di sisi kiri
4. Lakukan refresh browser (F5) dan verifikasi status pin tetap bertahan
5. Buka kembali modal Setup Column, uncheck kolom Employee ID tanpa menekan tombol Save
6. Klik tombol `[Cancel]` pada modal
7. Verifikasi modal tertutup dan perubahan dibatalkan (kolom Employee ID tetap tampil di tabel)
8. Buka kembali modal Setup Column, klik tombol `[Reset to Default]`
9. Verifikasi Live Preview kembali ke konfigurasi bawaan sistem
10. Klik `[Save]` dan verifikasi tabel kembali ke urutan dan visibilitas default

## Notes

- Tombol Reset to Default mengembalikan seluruh kolom ke urutan kanonikal dan status visible bawaan.
