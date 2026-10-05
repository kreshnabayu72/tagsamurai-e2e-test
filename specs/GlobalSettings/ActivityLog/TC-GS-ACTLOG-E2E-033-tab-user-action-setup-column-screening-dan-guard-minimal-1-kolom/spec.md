---
id: TC-GS-ACTLOG-E2E-033-tab-user-action-setup-column-screening-dan-guard-minimal-1-kolom
title: "Tab User Action: Screening Setup Column overlay, popup modal live preview, dan guard minimal 1 kolom visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-169
  - TC-GS-ACTLOG-170
  - TC-GS-ACTLOG-172
coverage:
  web: automated
---

# Tab User Action: Screening Setup Column overlay, popup modal live preview, dan guard minimal 1 kolom visible

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action

## Test Steps

1. Klik icon Setup Column `(⋯)` pada header tabel Tab User Action
2. Verifikasi quick panel overlay menampilkan 8 kolom hideable dengan checkbox enabled dan drag handle aktif
3. Buka popup modal Setup Column penuh
4. Verifikasi header modal menampilkan judul "Setup Column", teks deskripsi, dan tombol silang `[✕]`
5. Verifikasi body modal menampilkan daftar 8 kolom beserta area Live Preview
6. Verifikasi footer modal menampilkan tombol `[Reset to Default]`, `[Cancel]`, dan `[Save]`
7. Lakukan uncheck pada 7 kolom hingga hanya menyisakan kolom "Action" sebagai satu-satunya kolom yang visible
8. Coba uncheck checkbox kolom "Action"
9. Verifikasi checkbox "Action" menjadi disabled, tidak dapat di-uncheck, dan tooltip "At least one column must remain visible." muncul
10. Centang kembali satu kolom lain dan verifikasi checkbox "Action" kembali enabled

## Notes

- Guard 1 kolom visible berlaku identik di kedua tab.
