---
id: TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel
title: "Tab User Action: Pembekuan kolom sticky pin/unpin, reset ke default, dan pembatalan perubahan Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-187
  - TC-GS-ACTLOG-188
  - TC-GS-ACTLOG-189
  - TC-GS-ACTLOG-190
  - TC-GS-ACTLOG-191
  - TC-GS-ACTLOG-192
  - TC-GS-ACTLOG-193
  - TC-GS-ACTLOG-194
  - TC-GS-ACTLOG-195
  - TC-GS-ACTLOG-196
coverage:
  web: automated
---

# Tab User Action: Pembekuan kolom sticky pin/unpin, reset ke default, dan pembatalan perubahan Setup Column

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action di modal Setup Column

## Test Steps

1. Buka modal Setup Column pada Tab User Action
2. Klik icon Pin pada kolom Action dan Object lalu klik `[Save]`
3. Geser scrollbar horizontal tabel dan verifikasi kolom yang di-pin membeku (sticky) di sisi kiri
4. Lakukan refresh browser (F5) dan verifikasi status pin tetap bertahan
5. Buka kembali modal Setup Column, uncheck kolom Object tanpa menekan tombol Save
6. Klik tombol `[Cancel]` pada modal
7. Verifikasi modal tertutup dan perubahan dibatalkan (kolom Object tetap tampil di tabel)
8. Buka kembali modal Setup Column, klik tombol `[Reset to Default]`
9. Verifikasi Live Preview kembali ke konfigurasi bawaan sistem
10. Klik `[Save]` dan verifikasi tabel kembali ke urutan dan visibilitas default

## Notes

- Fitur pin sticky memudahkan penelusuran aksi dan objek saat tabel memiliki banyak kolom ke samping.
