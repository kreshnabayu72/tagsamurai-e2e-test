---
id: TC-GS-ROLE-E2E-065-setup-kolom-tabel-utama-fase-1-overlay-dan-modal-ceklis
title: "Setup Kolom Tabel Utama Fase 1: Overlay Visibilitas, Modal Screening, Toggles Kolom K1/K2, dan Guard 1 Kolom Terakhir"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-162
  - TC-GS-ROLE-163
  - TC-GS-ROLE-164
  - TC-GS-ROLE-165
  - TC-GS-ROLE-172
coverage:
  web: automated
---

# Setup Kolom Tabel Utama Fase 1: Overlay Visibilitas, Modal Screening, Toggles Kolom K1/K2, dan Guard 1 Kolom Terakhir

## Prerequisites

- Login sebagai Total Control
- Data Uji: Kolom K1 (6 kolom) & K2 (5 kolom)
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: openSetupColumnModal()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda

## Test Steps

### Screening overlay Column Visibility Tab Total Control dan Tab Read Only (TC-GS-ROLE-162)

1. Tab Total Control: klik header (⋯)
2. Ulangi di Tab Read Only
3. Verifikasi Item "Setup Column..." di bagian bawah panel Column Visibility (di bawah daftar kolom)
4. Verifikasi Checked & enabled: Name, Position, Division, Status, Modified By, Last Updated
5. Verifikasi Unchecked & enabled: Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]
6. Verifikasi Drag handle tersedia tiap kolom
7. Verifikasi Tab Read Only identik

### Screening popup Setup Column Tab Total Control (TC-GS-ROLE-163)

8. Klik header (⋯) > [Setup Column]
9. Screening popup
10. Verifikasi **Header**: Title "Setup Column", icon close (X)
11. Verifikasi **Body**: daftar kolom (checked: Name, Position, Division, Status, Modified By, Last Updated; unchecked: Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]), drag handle, icon Pin
12. Verifikasi **Footer**: `[Reset to Default]` (text, primary) | `[Save]` (filled, success), tanpa [Cancel]

### Setup Column — Hide kolom kelas K1 default tampil lalu Save (TC-GS-ROLE-164)

13. Buka popup Setup Column
14. Untuk tiap kolom (Name, Position, Division, Status, Modified By, Last Updated) ubah checkbox (kecuali Name pada Hide K1 dibiarkan agar ≥1 kolom tersisa)
15. Amati tabel di balik modal
16. Klik [Save]
17. Tekan F5
18. Verifikasi Tabel di balik modal langsung mempratinjau perubahan tiap kolom Name, Position, Division, Status, Modified By, Last Updated
19. Verifikasi Setelah Save tabel mencerminkan perubahan
20. Verifikasi Tetap setelah F5

### Setup Column — Show kolom kelas K2 kurasi tersembunyi lalu Save (TC-GS-ROLE-165)

21. Buka popup Setup Column
22. Untuk tiap kolom (Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]) ubah checkbox (kecuali Name pada Show K1 dibiarkan agar ≥1 kolom tersisa)
23. Amati tabel di balik modal
24. Klik [Save]
25. Tekan F5
26. Verifikasi Tabel di balik modal langsung mempratinjau perubahan tiap kolom Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]
27. Verifikasi Setelah Save tabel mencerminkan perubahan
28. Verifikasi Tetap setelah F5

### Setup Column — kolom terakhir yang tampil tidak bisa di-uncheck (TC-GS-ROLE-172)

29. Buka popup Setup Column
30. Uncheck semua kolom kecuali Name
31. Hover checkbox Name
32. Verifikasi Checkbox Name disabled
33. Verifikasi Tooltip "At least one column must remain visible."

## Notes

- Memvalidasi alur skenario "Setup Kolom Tabel Utama Fase 1: Overlay Visibilitas, Modal Screening, Toggles Kolom K1/K2, dan Guard 1 Kolom Terakhir".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1 Setup Column & Example Data; global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §4.1.2; foundation/process/prd-process/prd-conventions.md §9.3.
- Sumber pemetaan test case granular: TC-GS-ROLE-162, TC-GS-ROLE-163, TC-GS-ROLE-164, TC-GS-ROLE-165, TC-GS-ROLE-172.
