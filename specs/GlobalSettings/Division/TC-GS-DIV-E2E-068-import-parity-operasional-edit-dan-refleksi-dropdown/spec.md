---
id: TC-GS-DIV-E2E-068-import-parity-operasional-edit-dan-refleksi-dropdown
title: "Parity Operasional: Divisi Hasil Import Tampil Normal, Dapat Diedit, dan Terfleksi ke Dropdown User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-189
  - TC-GS-DIV-256
coverage:
  web: automated
---

# Parity Operasional: Divisi Hasil Import Tampil Normal, Dapat Diedit, dan Terfleksi ke Dropdown User

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data divisi yang dibuat melalui bulk import modul Import (GAP-041)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Verifikasi divisi hasil import tampil normal pada tabel utama dengan Name dan Code yang ter-generate
3. Klik menu row action (⋯) > 'Edit' pada divisi hasil import tersebut
4. Ubah namanya menjadi 'Imported Division Renamed'
5. Klik tombol '[Save]'
6. Verifikasi toast sukses muncul dan perubahan nama berhasil tersimpan
7. Buka form Create User pada tab User List
8. Buka dropdown 'Division'
9. Verifikasi nama baru 'Imported Division Renamed' muncul dan dapat dipilih secara normal sama persis dengan divisi buatan manual

## Notes

- Memvalidasi parity operasional hasil import GAP-041 / division.md §11.
