---
id: TC-GS-ROLE-E2E-066-setup-kolom-tabel-utama-fase-2-drag-reorder-dan-freeze-pinning
title: "Setup Kolom Tabel Utama Fase 2: Drag-and-Drop Reorder Kolom K1/K2 dan Sticky Freeze Pinning pada Scroll Horizontal"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-166
  - TC-GS-ROLE-167
  - TC-GS-ROLE-168
  - TC-GS-ROLE-169
coverage:
  web: automated
---

# Setup Kolom Tabel Utama Fase 2: Drag-and-Drop Reorder Kolom K1/K2 dan Sticky Freeze Pinning pada Scroll Horizontal

## Prerequisites

- Login sebagai Total Control
- Data Uji: Konfigurasi urutan kolom
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: openSetupColumnModal()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda

## Test Steps

### Setup Column — drag reorder kolom kelas K1 (TC-GS-ROLE-166)

1. Buka popup Setup Column
2. Drag tiap kolom kelas K1 (Name, Position, Division, Status, Modified By, Last Updated) ke posisi baru
3. Klik [Save]
4. F5
5. Verifikasi Urutan baru dipratinjau di tabel di balik modal dan tersimpan setelah Save
6. Verifikasi Tetap setelah F5

### Setup Column — pin kolom kelas K1 (TC-GS-ROLE-167)

7. Buka popup Setup Column
8. Pin tiap kolom kelas K1 (Name, Position, Division, Status, Modified By, Last Updated) yang tampil
9. Klik [Save]
10. Scroll horizontal tabel
11. F5
12. Verifikasi Kolom ter-pin tetap diam saat scroll horizontal
13. Verifikasi Pin tetap setelah F5

### Setup Column — drag reorder kolom kelas K2 (TC-GS-ROLE-168)

14. Buka popup Setup Column
15. Drag tiap kolom kelas K2 (Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]) ke posisi baru
16. Klik [Save]
17. F5
18. Verifikasi Urutan baru dipratinjau di tabel di balik modal dan tersimpan setelah Save
19. Verifikasi Tetap setelah F5

### Setup Column — pin kolom kelas K2 (TC-GS-ROLE-169)

20. Buka popup Setup Column
21. Pin tiap kolom kelas K2 (Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]) yang tampil
22. Klik [Save]
23. Scroll horizontal tabel
24. F5
25. Verifikasi Kolom ter-pin tetap diam saat scroll horizontal
26. Verifikasi Pin tetap setelah F5

## Notes

- Memvalidasi alur skenario "Setup Kolom Tabel Utama Fase 2: Drag-and-Drop Reorder Kolom K1/K2 dan Sticky Freeze Pinning pada Scroll Horizontal".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1 Setup Column & Example Data; global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §4.1.2; foundation/process/prd-process/prd-conventions.md §9.3.
- Sumber pemetaan test case granular: TC-GS-ROLE-166, TC-GS-ROLE-167, TC-GS-ROLE-168, TC-GS-ROLE-169.
