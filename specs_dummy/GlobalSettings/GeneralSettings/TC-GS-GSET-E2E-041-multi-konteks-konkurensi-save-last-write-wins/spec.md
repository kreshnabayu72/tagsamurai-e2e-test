---
id: TC-GS-GSET-E2E-041-multi-konteks-konkurensi-save-last-write-wins
title: "Multi-Konteks: dua admin menyimpan field yang sama — last-write-wins tanpa dialog konflik dan dua baris log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-145
coverage:
  web: automated
---

# Multi-Konteks: dua admin menyimpan field yang sama — last-write-wins tanpa dialog konflik dan dua baris log

## Prerequisites

- Dua sesi browser simultan: sesi 1 Total Control Budi Santoso, sesi 2 Total Control Andi Wijaya (entitas sama)
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

1. Sesi 1 dan sesi 2 membuka Global Settings > General Settings
2. Sesi 1 memilih Session Idle Timeout `1 hour` lalu klik `[Save]`
3. Verifikasi sesi 1 mendapat toast sukses "Success, general settings has been saved."
4. Sesi 2 (belum di-refresh) memilih Session Idle Timeout `4 hours` lalu klik `[Save]`
5. Verifikasi sesi 2 Save diterima tanpa dialog konflik dan mendapat toast sukses "Success, general settings has been saved."
6. Refresh sesi 1 dan amati Session Idle Timeout
7. Verifikasi Session Idle Timeout `4 hours` (Save terakhir menang)
8. Buka Modal Changelog dan verifikasi memuat 2 baris Field `Session Idle Timeout`, satu per Save

## Notes

- Multi-Konteks: last-write-wins tanpa version token/409 (TC-GS-GSET-145; NC-01). Butuh dua sesi browser simultan.
