---
id: TC-GS-USER-E2E-050-user-list-setup-column-modal-reorder-dan-pin
title: "User List: Setup Column modal pengaturan urutan, pin kolom, reset to default, dan cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-451
  - TC-GS-USER-452
  - TC-GS-USER-453
  - TC-GS-USER-454
  - TC-GS-USER-455
  - TC-GS-USER-456
  - TC-GS-USER-457
  - TC-GS-USER-458
  - TC-GS-USER-459
  - TC-GS-USER-460
  - TC-GS-USER-461
  - TC-GS-USER-462
  - TC-GS-USER-463
  - TC-GS-USER-464
  - TC-GS-USER-465
  - TC-GS-USER-466
  - TC-GS-USER-467
  - TC-GS-USER-468
  - TC-GS-USER-469
  - TC-GS-USER-470
  - TC-GS-USER-471
  - TC-GS-USER-472
  - TC-GS-USER-473
  - TC-GS-USER-474
  - TC-GS-USER-475
coverage:
  web: automated
---

# User List: Setup Column modal pengaturan urutan, pin kolom, reset to default, dan cancel

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Modal Setup Column

1. Dari overlay Column Visibility, klik tombol '[Setup Column]'
2. Verifikasi modal Setup Column terbuka dengan daftar seluruh kolom
3. Lakukan drag & drop reorder urutan kolom, pin kolom Name ke kiri
4. Klik tombol '[Save]', verifikasi struktur tabel terupdate sesuai konfigurasi baru
5. Buka kembali modal, klik '[Reset to Default]', verifikasi tata letak kolom kembali ke standar pabrik

## Notes

- Menggabungkan 25 test case granular (TC-GS-USER-451 s.d. TC-GS-USER-475).
