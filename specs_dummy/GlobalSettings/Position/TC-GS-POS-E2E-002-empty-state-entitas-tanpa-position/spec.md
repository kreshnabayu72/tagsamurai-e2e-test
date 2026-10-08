---
id: TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position
title: "Empty state pada entitas baru tanpa record Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-7
  - TC-GS-POS-296
coverage:
  web: automated
---

# Empty state pada entitas baru tanpa record Position

## Prerequisites

- Login sebagai Role: Total Control pada entitas "Client Kosong"
- Entitas Client Kosong baru diprovisioning dan memiliki 0 record Position (tanpa seed Default User Position)

## Test Steps

### Verifikasi Katalog Kosong

1. Buka Global Settings > User > Position pada entitas Client Kosong
2. Verifikasi tabel menampilkan ilustrasi kosong dengan judul "No position yet" dan deskripsi "Get started by creating your first position."
3. Verifikasi di dalam area empty state tidak terdapat tombol CTA duplicate
4. Verifikasi tombol primary "[+ Position]" tetap tampil dan aktif di area Table Tools pojok kanan atas

## Notes

- Menggabungkan TC-GS-POS-7 dan 296 untuk menguji kondisi entitas murni tanpa master data Position.
