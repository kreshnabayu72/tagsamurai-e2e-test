---
id: TC-GS-ROLE-E2E-038-remove-access-level-resilience-server-500-dan-double-submit
title: "Ketahanan Dialog Remove Total Control & Read Only: Penanganan Server 500 dan Guard Klik Ganda Cepat"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-89
  - TC-GS-ROLE-90
  - TC-GS-ROLE-91
coverage:
  web: automated
---

# Ketahanan Dialog Remove Total Control & Read Only: Penanganan Server 500 dan Guard Klik Ganda Cepat

## Prerequisites

- Login sebagai Total Control; mock intercept HTTP 500
- Data Uji: Lukman Hakim, Rina Putri
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: setupMock500()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Response Remove dibuat gagal 5xx
- User berada di Global Settings > Role & Permission > Read Only
- Lukman Hakim (Pre-setup #18) Total Control (Given)

## Test Steps

### Remove Total Control gagal 5xx (TC-GS-ROLE-89)

1. Klik Remove baris Maya Anggraini
2. Klik [Remove]
3. Verifikasi Muncul toast error: "Error, failed to remove Total Control."
4. Verifikasi Maya Anggraini tetap di Tab Total Control dengan baris role tidak berubah

### Remove Read Only gagal 5xx (TC-GS-ROLE-90)

5. Klik Remove baris Rina Putri
6. Klik [Remove]
7. Verifikasi Muncul toast error: "Error, failed to remove Read Only."
8. Verifikasi Rina Putri tetap di Tab Read Only

### Klik ganda [Remove] dialog Remove Total Control (TC-GS-ROLE-91)

9. Klik Remove baris Lukman Hakim
10. Klik [Remove] dua kali cepat
11. Verifikasi Satu toast sukses: "Success, Total Control has been removed."
12. Verifikasi Changelog Tab Total Control memuat tepat 1 entry Remove untuk Lukman Hakim

## Notes

- Memvalidasi alur skenario "Ketahanan Dialog Remove Total Control & Read Only: Penanganan Server 500 dan Guard Klik Ganda Cepat".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 T-03; global-settings/role/PRD/role.md §9.6; global-settings/role/PRD/role.md §7.1 T-05; global-settings/role/PRD/role.md §9.4.2 klik ganda.
- Sumber pemetaan test case granular: TC-GS-ROLE-89, TC-GS-ROLE-90, TC-GS-ROLE-91.
