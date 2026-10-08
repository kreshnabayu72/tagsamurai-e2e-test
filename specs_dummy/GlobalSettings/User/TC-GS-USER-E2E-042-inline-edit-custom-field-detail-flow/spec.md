---
id: TC-GS-USER-E2E-042-inline-edit-custom-field-detail-flow
title: "Custom Field: Inline-edit field kustom langsung di User Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-344
  - TC-GS-USER-345
  - TC-GS-USER-346
  - TC-GS-USER-347
  - TC-GS-USER-348
  - TC-GS-USER-349
  - TC-GS-USER-350
  - TC-GS-USER-351
  - TC-GS-USER-352
  - TC-GS-USER-353
  - TC-GS-USER-354
  - TC-GS-USER-355
coverage:
  web: automated
---

# Custom Field: Inline-edit field kustom langsung di User Detail

## Prerequisites

- Login sebagai Role: Total Control
- User Detail Dewi Lestari dengan section Custom Fields terbuka

## Test Steps

### Inline Edit Field

1. Buka Detail Dewi Lestari, amati section Custom Fields
2. Klik ikon pensil (inline edit) pada field Blood Type
3. Pilih nilai baru dari popover dropdown
4. Klik tombol centang simpan, verifikasi nilai terupdate instan tanpa reload halaman
5. Klik inline edit field lain, lalu klik tombol silang (batal), verifikasi nilai lama tidak berubah

## Notes

- Menggabungkan 12 test case granular (TC-GS-USER-344 s.d. TC-GS-USER-355).
