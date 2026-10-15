---
id: TC-GS-USER-E2E-030-status-flow-single-toggle-active-dan-konfirmasi
title: "Status Flow: Single Toggle Active dialog konfirmasi Deactivate dan aktivasi langsung"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-241
  - TC-GS-USER-242
  - TC-GS-USER-243
  - TC-GS-USER-244
  - TC-GS-USER-245
  - TC-GS-USER-246
  - TC-GS-USER-247
  - TC-GS-USER-248
  - TC-GS-USER-249
  - TC-GS-USER-250
  - TC-GS-USER-1011
coverage:
  web: automated
---

# Status Flow: Single Toggle Active dialog konfirmasi Deactivate dan aktivasi langsung

## Prerequisites

- Login sebagai Role: Total Control
- User Dewi Lestari berstatus Active

## Test Steps

### Deaktivasi User

1. Klik toggle Active pada baris Dewi Lestari (dari ON ke OFF)
2. Verifikasi dialog konfirmasi Deactivate muncul dengan tombol '[Cancel]' dan '[Deactivate]'
3. Klik '[Cancel]', verifikasi toggle tetap ON dan status user tidak berubah
4. Klik toggle lagi, lalu klik '[Deactivate]'
5. Verifikasi toast sukses muncul, toggle berubah ke posisi OFF abu-abu, dan status user menjadi Inactive

### Aktivasi Kembali

6. Klik toggle Active pada baris Dewi Lestari (dari OFF ke ON)
7. Verifikasi dialog konfirmasi Activate muncul (atau aktif langsung sesuai kebijakan)
8. Konfirmasi aktivasi, verifikasi toggle kembali ON hijau

## Notes

- Menggabungkan 11 test case granular (TC-GS-USER-241 s.d. TC-GS-USER-1011).
