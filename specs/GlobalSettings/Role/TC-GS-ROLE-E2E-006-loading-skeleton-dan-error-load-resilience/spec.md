---
id: TC-GS-ROLE-E2E-006-loading-skeleton-dan-error-load-resilience
title: "Tampilan Loading State dan Pemulihan Error Load 500 via Tombol Try Again di Seluruh Surface"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-15
  - TC-GS-ROLE-16
  - TC-GS-ROLE-17
coverage:
  web: automated
---

# Tampilan Loading State dan Pemulihan Error Load 500 via Tombol Try Again di Seluruh Surface

## Prerequisites

- Login sebagai Role: Total Control; Spectra.intercept respons 500
- Data Uji: Data seed standar
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: setupNetworkMock()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Response list diperlambat (network throttle)
- Response list Tab Total Control dibuat gagal 5xx satu kali
- Response list tiap surface dibuat gagal 5xx

## Test Steps

### Loading state per surface (TC-GS-ROLE-15)

1. Buka Tab Total Control
2. Buka Tab Read Only
3. Buka Tab System
4. Buka Detail "Manage TAG"
5. Klik [+ Assign] di Tab Total Control
6. Klik Changelog di Tab Total Control
7. Verifikasi Tab Total Control: loading component tampil sebelum tabel terisi
8. Verifikasi Tab Read Only: loading component
9. Verifikasi Tab System: loading component
10. Verifikasi Detail: loading component
11. Verifikasi Popup Assign Total Control: loading component di tabel picker
12. Verifikasi Modal Changelog: loading component

### Error load Tab Total Control dan pulih via Try Again (TC-GS-ROLE-16)

13. Buka Tab Total Control
14. Klik [Try Again]
15. Verifikasi Langkah 1: area tabel menampilkan "Unable to load this data." + [Try Again], bukan empty state
16. Verifikasi Langkah 2: tabel termuat normal

### Error load pada Tab Read Only, Tab System, Detail, Table User Picker, dan Modal Changelog (TC-GS-ROLE-17)

17. Buka Tab Read Only
18. Buka Tab System
19. Buka Detail "Manage TAG"
20. Buka Popup Assign Total Control
21. Buka Modal Changelog Tab Total Control
22. Verifikasi Tab Read Only: "Unable to load this data." + [Try Again]
23. Verifikasi Tab System: idem
24. Verifikasi Detail: idem
25. Verifikasi Popup Assign Total Control: idem di area tabel picker
26. Verifikasi Modal Changelog: idem

## Notes

- Memvalidasi alur skenario "Tampilan Loading State dan Pemulihan Error Load 500 via Tombol Try Again di Seluruh Surface".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7 S-01; global-settings/role/PRD/role.md §7 S-04.
- Sumber pemetaan test case granular: TC-GS-ROLE-15, TC-GS-ROLE-16, TC-GS-ROLE-17.
