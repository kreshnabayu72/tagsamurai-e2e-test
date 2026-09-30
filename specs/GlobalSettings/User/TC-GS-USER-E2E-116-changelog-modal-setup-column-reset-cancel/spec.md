---
id: TC-GS-USER-E2E-116-changelog-modal-setup-column-reset-cancel
title: 'Setup Column modal Changelog: Reset to Default dan Cancel'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-330
  - TC-GS-USER-331
coverage:
  web: automated
---

# Setup Column modal Changelog: Reset to Default dan Cancel

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data Changelog mock dengan lebih dari 10 baris dan nilai panjang supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom modal Changelog disimpan di browser terpisah dari User List dan Tab Changelog, dan dikembalikan ke default di langkah akhir

## Test Steps

### Cancel

1. Buka popup modal Setup Column, hapus centang `Old Value` tanpa menyimpan, lalu klik `[Cancel]`
2. Verifikasi modal tertutup dan kolom `Old Value` tetap tampil
3. Buka popup lagi, hapus centang `Old Value`, lalu klik `✕`
4. Verifikasi hasil sama

### Reset to Default

5. Hapus centang `Old Value`, klik `[Save]`, lalu buka popup lagi
6. Klik `[Reset to Default]`
7. Verifikasi Live Preview kembali ke default (semua tujuh kolom tampil)
8. Klik `[Save]` lalu refresh
9. Verifikasi tabel memakai konfigurasi default

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.3.
