---
id: TC-GS-ACTLOG-E2E-023-tab-session-download-csv-xlsx-dan-penanganan-error
title: "Tab Session: Download log CSV/XLSX sesuai filter aktif (≤5.000 baris) dan penanganan kegagalan server"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-120
  - TC-GS-ACTLOG-121
coverage:
  web: automated
---

# Tab Session: Download log CSV/XLSX sesuai filter aktif (≤5.000 baris) dan penanganan kegagalan server

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session dengan filter aktif (≤5.000 baris)

## Test Steps

1. Terapkan filter Activity "Login" pada Tab Session
2. Klik icon Download pada toolbar lalu pilih opsi "CSV"
3. Verifikasi file `Activity-Log-Session.csv` berhasil diunduh tanpa toast sukses
4. Klik icon Download lalu pilih opsi "XLSX"
5. Verifikasi file `Activity-Log-Session.xlsx` berhasil diunduh
6. Simulasikan kegagalan backend (mock 500) pada endpoint export
7. Klik icon Download lalu pilih opsi "CSV"
8. Verifikasi toast error "Error, failed to download Activity-Log-Session." muncul di layar

## Notes

- Unduhan langsung tanpa toast sukses berlaku untuk dataset kecil (≤5.000 baris).
