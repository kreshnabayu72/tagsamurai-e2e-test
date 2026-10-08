---
id: TC-GS-DIV-E2E-042-bulk-action-bar-screening-dan-counter-lifecycle
title: "Screening Bulk Action Bar: Munculnya Bar saat Baris Dicentang dan Pembaruan Realtime Counter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-125
  - TC-GS-DIV-126
coverage:
  web: automated
---

# Screening Bulk Action Bar: Munculnya Bar saat Baris Dicentang dan Pembaruan Realtime Counter

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Division terisi data (TC-GS-DIV-30)
- User berada di Global Settings > User > Division

## Test Steps

### Screening Bulk Action Bar saat satu baris dicentang (TC-GS-DIV-125)

1. Centang checkbox baris `Accounting`
2. Verifikasi Bulk Action Bar muncul dengan urutan: tombol `Bulk Action` (aksi `[Delete]`), teks `1 Division selected`, tombol `Select All (32 records)`, icon `(✕)`
3. Verifikasi Aksi `Delete` di bar berseverity danger

### Counter Bulk Action Bar bertambah dan berkurang realtime serta clear lewat X (TC-GS-DIV-126)

4. Centang baris `Accounting`
5. Centang baris `Administration`
6. Hilangkan centang baris `Accounting`
7. Klik icon `(✕)` pada bar
8. Verifikasi Setelah centang kedua counter `2 Divisions selected`
9. Verifikasi Setelah uncheck satu baris counter `1 Division selected`
10. Verifikasi Klik `(✕)` membatalkan seluruh seleksi dan Bulk Action Bar tertutup

## Notes

- Memvalidasi screening Bulk Action Bar (FI-04): muncul saat >=1 baris dicentang, urutan elemen (tombol Bulk Action [Delete] danger, counter teks, tombol Select All, icon X), pertambahan/pengurangan counter realtime, dan clear lewat icon X (PRD §4.1, §4.4, prd-conventions.md §8).
- Sumber pemetaan test case granular: TC-GS-DIV-125, TC-GS-DIV-126.
