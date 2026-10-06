---
id: TC-GS-DIV-E2E-042-tabel-utama-sorting-3-state-name-code-dan-last-updated
title: "Sorting 3-State (Ascending, Descending, Default) Kolom Name, Code, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-62
  - TC-GS-DIV-63
  - TC-GS-DIV-269
coverage:
  web: automated
---

# Sorting 3-State (Ascending, Descending, Default) Kolom Name, Code, dan Last Updated

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat minimal 3 data divisi dengan nama, kode, dan tanggal bervariasi

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik header kolom 'Name' 1x dan verifikasi data terurut Ascending (A-Z) dengan panah ke atas
3. Klik header kolom 'Name' 2x dan verifikasi data terurut Descending (Z-A) dengan panah ke bawah
4. Klik header kolom 'Name' 3x dan verifikasi sort kolom Name kembali ke kondisi default (tanpa indikator sort aktif)
5. Klik header kolom 'Code' 1x, 2x, dan 3x lalu verifikasi transisi siklus sort 3-state kolom Code
6. Klik header kolom 'Last Updated' 1x (Newest First), 2x (Oldest First), dan 3x (Default)
7. Verifikasi seluruh transisi sort 3-state berjalan akurat tanpa error

## Notes

- Menerapkan aturan sort 3-klik kanonikal platform GAP-002 dan division.md §9.5.
