---
id: TC-GS-GSET-E2E-014-save-multi-field-termasuk-currency
title: "Save beberapa field sekaligus termasuk Currency Code: satu dialog Change Currency, persistensi kelima field, dan lima baris log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-43
coverage:
  web: automated
---

# Save beberapa field sekaligus termasuk Currency Code: satu dialog Change Currency, persistensi kelima field, dan lima baris log

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

1. Buka Global Settings > General Settings
2. Pilih Currency Code `USD`, Date Format `dd MMM yy`, Time Format `hh:mm a`, Time Zone Lain, dan Session Idle Timeout `2 hours`
3. Klik `[Save]` lalu klik `[Change Currency]`
4. Verifikasi Dialog Change Currency muncul sekali (setelah klik Save) dan setelah konfirmasi muncul toast sukses "Success, general settings has been saved."
5. Refresh halaman (F5)
6. Verifikasi kelima field sesuai nilai baru: `USD`, `dd MMM yy`, `hh:mm a`, Time Zone Lain, `2 hours`
7. Buka Modal Changelog dan verifikasi 5 baris baru (satu per field yang berubah)

## Notes

- Menguji Save multi-field termasuk Currency Code dan pemenuhan lima baris log (TC-GS-GSET-43).
