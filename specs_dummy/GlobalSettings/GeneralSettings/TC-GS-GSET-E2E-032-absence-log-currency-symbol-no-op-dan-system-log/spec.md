---
id: TC-GS-GSET-E2E-032-absence-log-currency-symbol-no-op-dan-system-log
title: "Asersi Absence: Currency Symbol tidak dicatat, Save tanpa perubahan tidak menghasilkan log, dan tidak ada System Log pada Detail User"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-110
  - TC-GS-GSET-112
  - TC-GS-GSET-113
coverage:
  web: automated
---

# Asersi Absence: Currency Symbol tidak dicatat, Save tanpa perubahan tidak menghasilkan log, dan tidak ada System Log pada Detail User

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Currency Code Tidak Mencatat Currency Symbol

1. Pilih Currency Code `USD`, klik `[Save]` lalu `[Change Currency]`
2. Buka Modal Changelog dan Activity Log
3. Verifikasi perubahan menghasilkan tepat 1 baris (Field `Currency Code`) dan tidak ada baris Field `Currency Symbol` atau `Decimal Places`
4. Buka dropdown filter Field di Changelog
5. Verifikasi opsi filter Field tidak memuat `Currency Symbol` maupun `Decimal Places`

### Save Tanpa Perubahan Tidak Menghasilkan Log

6. Buka Modal Changelog dan catat jumlah baris
7. Tutup modal, amati Button "Save" dan coba klik
8. Verifikasi Button "Save" disabled dan klik tidak mengirim request
9. Buka Modal Changelog dan hitung baris lagi
10. Verifikasi jumlah baris sama dengan jumlah pada langkah 6

### Tidak Ada System Log pada Detail User

11. Pilih Session Idle Timeout `1 hour` lalu Save
12. Buka Global Settings > User > Detail user Budi Santoso > tab System Log
13. Verifikasi tab System Log tidak memuat entri perubahan General Settings (anchor: entri login terakhir user tetap tampil)

## Notes

- Menggabungkan asersi absence TC-GS-GSET-110, 112, dan 113.
