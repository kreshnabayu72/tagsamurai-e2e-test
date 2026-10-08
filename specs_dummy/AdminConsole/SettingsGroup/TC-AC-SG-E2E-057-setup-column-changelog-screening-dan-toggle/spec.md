---
id: TC-AC-SG-E2E-057-setup-column-changelog-screening-dan-toggle
title: "Setup Column Modal Changelog: screening 3 zona, toggle kolom Action, dan guard minimal 1 kolom tersisa"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-109
  - TC-AC-SG-213
  - TC-AC-SG-214
  - TC-AC-SG-215
coverage:
  web: automated
---

# Setup Column Modal Changelog: screening 3 zona, toggle kolom Action, dan guard minimal 1 kolom tersisa

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terbuka

## Test Steps

### Screening Modal Setup Column Changelog
1. Klik header menu elipsis `[⋯]` pada toolbar Modal Changelog
2. Verifikasi modal Setup Column terbuka dengan 3 zona lengkap
3. Verifikasi 7 kolom data bertipe Hideable (`Date`, `Action`, `Group Name`, `Field`, `Old Value`, `New Value`, `Modified By`)
### Toggle Hide/Unhide Kolom Action
4. Hilangkan centang pada kolom `Action`
5. Verifikasi Live Preview seketika menyembunyikan kolom Action
6. Klik `[Save]` dan verifikasi kolom Action hilang dari tabel Changelog
### Guard Minimal 1 Kolom Tersisa
7. Buka kembali Setup Column
8. Uncheck seluruh kolom hingga tersisa 1 kolom terakhir
9. Verifikasi checkbox kolom terakhir otomatis disabled dan memunculkan tooltip 🔖 `"At least one column must remain visible."`

## Notes

- Seluruh 7 kolom Changelog bersifat hideable.
