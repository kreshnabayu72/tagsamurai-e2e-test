---
id: TC-GS-ROLE-E2E-067-setup-kolom-tabel-utama-fase-3-reset-discard-dan-isolasi-tabel
title: "Setup Kolom Tabel Utama Fase 3: Reset to Default, Pembatalan Discard via Esc/X, dan Independensi Konfigurasi per Tabel"
priority: Low
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-170
  - TC-GS-ROLE-171
  - TC-GS-ROLE-173
coverage:
  web: automated
---

# Setup Kolom Tabel Utama Fase 3: Reset to Default, Pembatalan Discard via Esc/X, dan Independensi Konfigurasi per Tabel

## Prerequisites

- Login sebagai Total Control
- Data Uji: Konfigurasi kolom
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: openSetupColumnModal()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda

## Test Steps

### Setup Column — Reset to Default (TC-GS-ROLE-170)

1. Ubah konfigurasi kolom lalu Save
2. Buka popup Setup Column > [Reset to Default] > [Save]
3. Verifikasi Kolom kembali default: tampil Name, Position, Division, Status, Modified By, Last Updated; tersembunyi Activation Status, Temporary User, Temporary Until, TAG, [Custom Field aktif]
4. Verifikasi Tetap setelah F5

### Setup Column — tutup tanpa Save membatalkan perubahan (TC-GS-ROLE-171)

5. Buka popup Setup Column
6. Uncheck Position
7. Klik (X)
8. Ulangi, tekan Esc
9. Verifikasi Popup tertutup
10. Verifikasi Kolom Position tetap tampil di tabel

### Setup Column — konfigurasi terpisah per tabel (TC-GS-ROLE-173)

11. Tab Total Control: hide Division > Save
12. Buka Tab Read Only dan Detail "Manage TAG"
13. Verifikasi Tab Read Only dan Detail tetap menampilkan Division
14. Verifikasi Tab Total Control tetap tanpa Division

## Notes

- Memvalidasi alur skenario "Setup Kolom Tabel Utama Fase 3: Reset to Default, Pembatalan Discard via Esc/X, dan Independensi Konfigurasi per Tabel".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1 Setup Column & Example Data; global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §4.1.2; foundation/process/prd-process/prd-conventions.md §9.3.
- Sumber pemetaan test case granular: TC-GS-ROLE-170, TC-GS-ROLE-171, TC-GS-ROLE-173.
