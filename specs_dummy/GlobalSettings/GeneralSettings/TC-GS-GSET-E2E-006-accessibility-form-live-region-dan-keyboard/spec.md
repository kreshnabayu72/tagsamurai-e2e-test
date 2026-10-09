---
id: TC-GS-GSET-E2E-006-accessibility-form-live-region-dan-keyboard
title: "Accessibility form: Preview text sebagai live region dan Select dapat dioperasikan via keyboard"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-13
coverage:
  web: automated
---

# Accessibility form: Preview text sebagai live region dan Select dapat dioperasikan via keyboard

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- `[simbol opsi EUR]` = simbol yang tampil pada label opsi untuk kode EUR

## Test Steps

1. Buka Global Settings > General Settings
2. Periksa elemen Preview Currency dan Preview Date & Time pada DOM
3. Verifikasi kedua Preview text memiliki atribut `aria-live` (live region)
4. Tekan `Tab` hingga fokus pada Select "Currency Code", tekan `Enter`, ketik "Euro", lalu tekan `Enter`
5. Verifikasi Select Currency Code dapat difokus, dibuka, dicari, dan dipilih via keyboard
6. Amati Preview Currency
7. Verifikasi Preview berubah menjadi "[simbol opsi EUR] 5.000,00"

## Notes

- Menguji aksesibilitas form (TC-GS-GSET-13).
