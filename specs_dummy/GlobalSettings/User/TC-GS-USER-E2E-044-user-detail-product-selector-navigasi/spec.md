---
id: TC-GS-USER-E2E-044-user-detail-product-selector-navigasi
title: "User Detail: Navigasi Product Selector dan sinkronisasi hak akses per produk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-371
  - TC-GS-USER-372
  - TC-GS-USER-373
  - TC-GS-USER-374
  - TC-GS-USER-375
  - TC-GS-USER-376
  - TC-GS-USER-377
  - TC-GS-USER-378
  - TC-GS-USER-379
  - TC-GS-USER-380
  - TC-GS-USER-1018
  - TC-GS-USER-1019
  - TC-GS-USER-1020
coverage:
  web: automated
---

# User Detail: Navigasi Product Selector dan sinkronisasi hak akses per produk

## Prerequisites

- User target memiliki akses multi-produk (Fixed Asset, Supply Asset)

## Test Steps

### Navigasi Product Selector

1. Buka User Detail target, amati dropdown Product Selector di toolbar
2. Pindah pilihan produk dari 'Global Settings' ke 'Fixed Asset'
3. Verifikasi data role dan permissions menyesuaikan dengan konteks produk yang dipilih

## Notes

- Menggabungkan 13 test case granular (TC-GS-USER-371 s.d. TC-GS-USER-1020).
