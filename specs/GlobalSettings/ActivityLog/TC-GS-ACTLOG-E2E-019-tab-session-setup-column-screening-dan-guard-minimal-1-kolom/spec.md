---
id: TC-GS-ACTLOG-E2E-019-tab-session-setup-column-screening-dan-guard-minimal-1-kolom
title: "Tab Session: Screening Setup Column overlay, popup modal live preview, dan guard minimal 1 kolom visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-86
  - TC-GS-ACTLOG-87
  - TC-GS-ACTLOG-89
coverage:
  web: automated
---

# Tab Session: Screening Setup Column overlay, popup modal live preview, dan guard minimal 1 kolom visible

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session

## Test Steps

1. Klik icon Setup Column `(⋯)` pada header tabel Tab Session
2. Verifikasi quick panel overlay menampilkan 10 kolom hideable dengan checkbox enabled dan drag handle aktif
3. Buka popup modal Setup Column penuh
4. Verifikasi header modal menampilkan judul "Setup Column", teks deskripsi, dan tombol silang `[✕]`
5. Verifikasi body modal menampilkan daftar 10 kolom beserta area Live Preview
6. Verifikasi footer modal menampilkan tombol `[Reset to Default]`, `[Cancel]`, dan `[Save]`
7. Lakukan uncheck pada 9 kolom hingga hanya menyisakan kolom "User" sebagai satu-satunya kolom yang visible
8. Coba uncheck checkbox kolom "User"
9. Verifikasi checkbox "User" menjadi disabled, tidak dapat di-uncheck, dan tooltip "At least one column must remain visible." muncul
10. Centang kembali satu kolom lain dan verifikasi checkbox "User" kembali enabled

## Notes

- Guard minimal 1 kolom visible mencegah tabel kosong total akibat kesalahan uncheck semua kolom.
