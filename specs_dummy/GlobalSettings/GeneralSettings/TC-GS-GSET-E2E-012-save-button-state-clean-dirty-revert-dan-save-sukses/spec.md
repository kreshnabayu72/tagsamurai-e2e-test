---
id: TC-GS-GSET-E2E-012-save-button-state-clean-dirty-revert-dan-save-sukses
title: "Save: state disabled/enabled saat Unchanged/berubah/revert, dan Save sukses Total Control hingga persistensi F5"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-28
  - TC-GS-GSET-29
  - TC-GS-GSET-42
coverage:
  web: automated
---

# Save: state disabled/enabled saat Unchanged/berubah/revert, dan Save sukses Total Control hingga persistensi F5

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### State Button Save

1. Buka Global Settings > General Settings dan amati Button "Save" saat form baru dimuat
2. Verifikasi Button "Save" disabled (tetap tampil)
3. Pilih Session Idle Timeout `1 hour`
4. Verifikasi Button "Save" enabled
5. Pilih kembali Session Idle Timeout `30 minutes`
6. Verifikasi Button "Save" kembali disabled (form kembali ke nilai tersimpan)

### Save Sukses dan Persistensi

7. Pilih Session Idle Timeout `1 hour` lalu klik `[Save]`
8. Verifikasi toast sukses "Success, general settings has been saved."
9. Refresh halaman (F5)
10. Verifikasi Session Idle Timeout `1 hour` (tersimpan)

### Revert Currency Code Tanpa Dialog

11. Pilih Currency Code `USD`
12. Pilih kembali Currency Code `IDR`
13. Amati Button "Save"
14. Verifikasi Button "Save" disabled; tidak ada dialog dan tidak ada request tersimpan

## Notes

- Menggabungkan TC-GS-GSET-28 (Save sukses Total Control), TC-GS-GSET-29 (state Button Save), dan TC-GS-GSET-42 (revert Currency Code mematikan Save tanpa dialog).
