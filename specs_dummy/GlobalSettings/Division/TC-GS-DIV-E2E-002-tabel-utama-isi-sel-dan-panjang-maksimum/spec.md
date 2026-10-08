---
id: TC-GS-DIV-E2E-002-tabel-utama-isi-sel-dan-panjang-maksimum
title: "Tampilan Sel Data Kolom Name 120 Karakter Tanpa Truncation, Kolom Code, dan Format Last Updated"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-4
coverage:
  web: automated
---

# Tampilan Sel Data Kolom Name 120 Karakter Tanpa Truncation, Kolom Code, dan Format Last Updated

## Prerequisites

- Login sebagai Role: Total Control
- Division dengan Name 120 karakter (D-03) sudah dibuat di entitas
- User berada di Global Settings > User > Division
- Division dengan Name 120 karakter sudah dibuat (TC-GS-DIV-37)

## Test Steps

1. Buka Tab Division
2. Cari baris dengan Name 120 karakter
3. Perhatikan sel Name, Code, dan Last Updated
4. Verifikasi Name tampil utuh 120 karakter tanpa pemotongan `..` dan tanpa tooltip, kolom melebar mengikuti isi
5. Verifikasi Code tampil terisi (tidak pernah kosong)
6. Verifikasi Last Updated tampil memakai format tanggal dan jam General Settings (bukan `—`)
7. Verifikasi Tinggi baris tabel tetap konsisten pada seluruh baris

## Notes

- Memvalidasi bahwa kolom Name melebar mengikuti isi hingga 120 karakter tanpa pemotongan "..." atau tooltip, Code terisi, dan Last Updated mengikuti format General Settings (PRD §4.1.1, prd-conventions.md §9.12a).
- Sumber pemetaan test case granular: TC-GS-DIV-4.
