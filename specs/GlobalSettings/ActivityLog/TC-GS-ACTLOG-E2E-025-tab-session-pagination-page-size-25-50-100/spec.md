---
id: TC-GS-ACTLOG-E2E-025-tab-session-pagination-page-size-25-50-100
title: "Tab Session: Pergantian page size pagination 25/50/100 baris menampilkan jumlah data presisi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-200
coverage:
  web: automated
---

# Tab Session: Pergantian page size pagination 25/50/100 baris menampilkan jumlah data presisi

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session dengan total entri log aktif ≥100 baris

## Test Steps

1. Buka Tab Session dan verifikasi page size bawaan adalah 10 baris
2. Ubah page size dropdown di footer ke "25"
3. Verifikasi tepat 25 baris data tampil di tabel
4. Ubah page size dropdown ke "50"
5. Verifikasi tepat 50 baris data tampil di tabel
6. Ubah page size dropdown ke "100"
7. Verifikasi tepat 100 baris data tampil di tabel dan opsi maksimum adalah 100 tanpa opsi "All"
8. Kembalikan page size ke 10 dan verifikasi pagination info tetap konsisten tanpa duplikasi data

## Notes

- Pilihan page size kanonikal TAG Samurai: 10, 25, 50, dan 100.
