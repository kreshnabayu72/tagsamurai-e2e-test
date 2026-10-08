---
id: TC-GS-ROLE-E2E-057-bulk-remove-resilience-server-500-dan-double-submit
title: "Ketahanan Pencabutan Massal: Penanganan Kegagalan Server 500 dan Guard Klik Ganda Cepat"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-133
  - TC-GS-ROLE-135
coverage:
  web: automated
---

# Ketahanan Pencabutan Massal: Penanganan Kegagalan Server 500 dan Guard Klik Ganda Cepat

## Prerequisites

- Login sebagai Total Control; mock intercept HTTP 500
- Data Uji: Baris terpilih pada Detail Manage hardware
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: setupMock500()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"
- Response Bulk Remove dibuat gagal 5xx

## Test Steps

### Bulk Remove gagal 5xx (TC-GS-ROLE-133)

1. Centang 2 baris eligible
2. Klik Bulk Action > Remove > [Remove]
3. Verifikasi Muncul toast error: "Error, failed to remove user."
4. Verifikasi Kedua baris tetap ada dan tetap tercentang

### Klik ganda [Remove] dialog Bulk Remove (TC-GS-ROLE-135)

5. Centang 2 baris
6. Bulk Action > Remove
7. Klik [Remove] dua kali cepat
8. Verifikasi Satu toast sukses: "Success, user has been removed."
9. Verifikasi Changelog memuat tepat 1 entry Remove per baris

## Notes

- Memvalidasi alur skenario "Ketahanan Pencabutan Massal: Penanganan Kegagalan Server 500 dan Guard Klik Ganda Cepat".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 T-10; global-settings/role/PRD/role.md §9.6; global-settings/role/PRD/role.md §9.4.2 klik ganda.
- Sumber pemetaan test case granular: TC-GS-ROLE-133, TC-GS-ROLE-135.
