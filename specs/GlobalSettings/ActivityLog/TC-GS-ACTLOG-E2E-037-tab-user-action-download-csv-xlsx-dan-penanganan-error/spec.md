---
id: TC-GS-ACTLOG-E2E-037-tab-user-action-download-csv-xlsx-dan-penanganan-error
title: "Tab User Action: Download log CSV/XLSX sesuai filter aktif (≤5.000 baris) dan penanganan kegagalan server"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-197
  - TC-GS-ACTLOG-198
coverage:
  web: automated
---

# Tab User Action: Download log CSV/XLSX sesuai filter aktif (≤5.000 baris) dan penanganan kegagalan server

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan filter aktif (≤5.000 baris)

## Test Steps

1. Terapkan filter Action "Edit" pada Tab User Action
2. Klik icon Download pada toolbar lalu pilih opsi "CSV"
3. Verifikasi file `Activity-Log-User-Action.csv` berhasil diunduh tanpa toast sukses
4. Klik icon Download lalu pilih opsi "XLSX"
5. Verifikasi file `Activity-Log-User-Action.xlsx` berhasil diunduh
6. Simulasikan kegagalan backend (mock 500) pada endpoint export
7. Klik icon Download lalu pilih opsi "CSV"
8. Verifikasi toast error "Error, failed to download Activity-Log-User-Action." muncul di layar

## Notes

- Format penamaan file ekspor Tab User Action adalah `Activity-Log-User-Action.[csv/xlsx]`.
