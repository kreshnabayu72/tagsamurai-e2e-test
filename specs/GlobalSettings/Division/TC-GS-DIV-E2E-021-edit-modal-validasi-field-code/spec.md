---
id: TC-GS-DIV-E2E-021-edit-modal-validasi-field-code
title: "Validasi Field Code Edit: Batas 15 Karakter, Whitelist Karakter, dan Duplikat Existing"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-266
  - TC-GS-DIV-267
coverage:
  web: automated
---

# Validasi Field Code Edit: Batas 15 Karakter, Whitelist Karakter, dan Duplikat Existing

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat divisi 'Human Capital' (Code 'HC') dan divisi 'Logistics' (Code 'LGST')

## Test Steps

1. Buka modal Edit pada baris divisi 'Human Capital'
2. Ketik string 16 karakter pada field Code dan verifikasi muncul pesan error 'Max. 15 characters'
3. Ketik karakter di luar whitelist seperti 'HC#DEV' dan verifikasi muncul pesan error 'Code contains invalid characters'
4. Ketik kode yang menyamai divisi lain: 'lgst' (huruf kecil dari 'LGST')
5. Klik tombol '[Save]'
6. Verifikasi muncul pesan error inline 'Code already exists', data tidak tersimpan, dan modal tetap terbuka

## Notes

- Validasi kode pada form edit simetris dengan validasi form create (division.md §6).
