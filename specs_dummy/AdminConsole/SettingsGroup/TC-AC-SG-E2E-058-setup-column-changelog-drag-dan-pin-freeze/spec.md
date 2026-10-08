---
id: TC-AC-SG-E2E-058-setup-column-changelog-drag-dan-pin-freeze
title: "Setup Column Modal Changelog: interaksi Drag-and-Drop reorder urutan kolom dan freeze Pin scroll"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-216
  - TC-AC-SG-217
coverage:
  web: automated
---

# Setup Column Modal Changelog: interaksi Drag-and-Drop reorder urutan kolom dan freeze Pin scroll

## Prerequisites

- Login sebagai Role: Total Control
- Modal Setup Column pada Changelog terbuka

## Test Steps

### Drag Reorder Kolom Changelog
1. Drag baris `Modified By` dan posisikan di urutan pertama setelah `Date`
2. Klik `[Save]`
3. Verifikasi pada tabel Changelog, kolom `Modified By` kini tampil langsung setelah `Date`
### Pin Freeze Kolom Field
4. Buka kembali Setup Column
5. Aktifkan Pin pada kolom `Field`
6. Klik `[Save]`
7. Lakukan scroll horizontal pada tabel Changelog
8. Verifikasi kolom `Field` freeze membeku di kiri saat discroll horizontal

## Notes

- Menguji interaksi drag dan pin sticky khusus pada modal Changelog.
