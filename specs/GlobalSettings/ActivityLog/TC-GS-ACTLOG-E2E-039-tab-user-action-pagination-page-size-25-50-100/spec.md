---
id: TC-GS-ACTLOG-E2E-039-tab-user-action-pagination-page-size-25-50-100
title: "Tab User Action: Pergantian page size pagination 25/50/100 baris menampilkan jumlah data presisi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-201
coverage:
  web: automated
---

# Tab User Action: Pergantian page size pagination 25/50/100 baris menampilkan jumlah data presisi

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan total entri log aktif ≥100 baris

## Test Steps

1. Buka Tab User Action dan verifikasi page size bawaan adalah 10 baris
2. Ubah page size dropdown di footer ke "25"
3. Verifikasi tepat 25 baris data tampil di tabel
4. Ubah page size dropdown ke "50"
5. Verifikasi tepat 50 baris data tampil di tabel
6. Ubah page size dropdown ke "100"
7. Verifikasi tepat 100 baris data tampil di tabel dan opsi maksimum adalah 100 tanpa opsi "All"
8. Kembalikan page size ke 10 dan verifikasi pagination info tetap konsisten tanpa duplikasi data

## Notes

- Pergantian page size tidak mengubah posisi sort dan saringan aktif.
