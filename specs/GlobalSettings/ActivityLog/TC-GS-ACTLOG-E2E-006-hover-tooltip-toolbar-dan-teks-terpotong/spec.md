---
id: TC-GS-ACTLOG-E2E-006-hover-tooltip-toolbar-dan-teks-terpotong
title: "Hover Tooltip pada Table Tools dan Nama Lengkap User serta Modified By"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-12
  - TC-GS-ACTLOG-13
  - TC-GS-ACTLOG-14
coverage:
  web: automated
---

# Hover Tooltip pada Table Tools dan Nama Lengkap User serta Modified By

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Terdapat entri Session dengan user 'John Doe' dan entri User Action dengan admin 'Hendra Pratama'

## Test Steps

### Tooltip Toolbar & Column Visibility
1. Buka Tab Session, arahkan kursor ke icon Search, verifikasi tooltip 'Search' muncul.
2. Arahkan kursor ke icon Filter, verifikasi tooltip 'Filter' muncul.
3. Arahkan kursor ke icon Download, verifikasi tooltip 'Download' muncul.
4. Arahkan kursor ke header kolom Actions (⋯), verifikasi tooltip 'Column Visibility' muncul.
5. Buka Tab User Action dan lakukan verifikasi tooltip pada keempat kontrol yang sama.
### Hover Tooltip Nama Lengkap
6. Pada Tab Session, amati sel kolom User untuk baris pengguna 'John Doe'.
7. Verifikasi teks yang tampil adalah nama ringkas 'John D'.
8. Arahkan kursor (hover) ke teks 'John D', verifikasi tooltip menampilkan nama lengkap 'John Doe'.
9. Pada Tab User Action, amati sel kolom Modified By untuk baris admin 'Hendra Pratama'.
10. Verifikasi teks yang tampil adalah nama ringkas 'Hendra P'.
11. Arahkan kursor (hover) ke teks 'Hendra P', verifikasi tooltip menampilkan nama lengkap 'Hendra Pratama'.

## Notes

- Tampilan nama ringkas menghemat ruang kolom tabel sambil mempertahankan aksesibilitas nama lengkap via tooltip.
