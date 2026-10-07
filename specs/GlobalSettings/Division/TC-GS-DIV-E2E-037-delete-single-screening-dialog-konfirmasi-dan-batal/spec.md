---
id: TC-GS-DIV-E2E-037-delete-single-screening-dialog-konfirmasi-dan-batal
title: "Screening Dialog Konfirmasi Delete Single (D-01) dan Pembatalan via Tombol Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-114
  - TC-GS-DIV-115
coverage:
  web: automated
---

# Screening Dialog Konfirmasi Delete Single (D-01) dan Pembatalan via Tombol Cancel

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia divisi bebas relasi (Finance)
- User berada di Global Settings > User > Division
- Division `Public Relations` bebas relasi ada (TC-GS-DIV-65)

## Test Steps

### Screening Dialog Konfirmasi Delete single (TC-GS-DIV-114)

1. Buka row action baris `Public Relations` lalu klik `Delete`
2. Verifikasi Title `Delete Division` (severity danger)
3. Verifikasi Body: bullet `Public Relations`, lalu `Are you sure you want to delete it? This action cannot be undone.`
4. Verifikasi Tombol `[Cancel]` (text, contrast) dan `[Delete]` (filled, danger)

### Cancel pada dialog Delete tidak menghapus Division (TC-GS-DIV-115)

5. Buka row action baris `Public Relations` lalu klik `Delete`
6. Klik `[Cancel]`
7. Verifikasi Dialog tertutup tanpa toast
8. Verifikasi Baris `Public Relations` tetap ada di tabel

## Notes

- Memvalidasi Dialog 1 (D-01: title "Delete Division", bullet nama divisi, body "Are you sure...", tombol [Cancel] dan [Delete]) dan pembatalan tidak menghapus data (PRD §4.2d).
- Sumber pemetaan test case granular: TC-GS-DIV-114, TC-GS-DIV-115.
