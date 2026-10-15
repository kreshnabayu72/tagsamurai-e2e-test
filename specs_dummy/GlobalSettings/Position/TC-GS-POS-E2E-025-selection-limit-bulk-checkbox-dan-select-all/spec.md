---
id: TC-GS-POS-E2E-025-selection-limit-bulk-checkbox-dan-select-all
title: "Volume Data: Penegakan Selection Limit pada checkbox manual ke-(limit+1) dan pembatasan Select All"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-135
  - TC-GS-POS-136
coverage:
  web: automated
---

# Volume Data: Penegakan Selection Limit pada checkbox manual ke-(limit+1) dan pembatasan Select All

## Prerequisites

- Login sebagai Total Control
- Selection Limit diatur menjadi 5 record melalui Admin Console

## Test Steps

### Batas Seleksi Manual (Limit + 1)

1. Buka tab Position
2. Centang secara manual 5 baris Position hingga mencapai batas Selection Limit (5)
3. Amati baris ke-6 yang belum terpilih
4. Verifikasi checkbox pada baris ke-6 dan seterusnya berubah menjadi disabled (tidak dapat dicentang)
5. Verifikasi tooltip pada checkbox disabled menjelaskan batas kuota seleksi telah tercapai

### Pembatasan Fitur Select All

6. Kosongkan seluruh seleksi
7. Klik checkbox header lalu klik "Select All"
8. Verifikasi sistem membatasi seleksi otomatis tepat pada 5 record pertama (sesuai Selection Limit) dan tidak memilih seluruh baris yang melebihi limit

## Notes

- Menggabungkan TC-GS-POS-135 dan 136 dalam kelas harness Volume Data Khusus.
