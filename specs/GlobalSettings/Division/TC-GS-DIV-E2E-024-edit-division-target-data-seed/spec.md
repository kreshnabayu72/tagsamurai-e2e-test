---
id: TC-GS-DIV-E2E-024-edit-division-target-data-seed
title: "Penyuntingan Divisi Seed Awal Diizinkan Mengubah Name dan Code"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-39
coverage:
  web: automated
---

# Penyuntingan Divisi Seed Awal Diizinkan Mengubah Name dan Code

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat divisi data seed bawaan 'Head Office'

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Temukan baris data seed 'Head Office'
3. Klik menu row action (⋯) > 'Edit'
4. Ubah Division Name menjadi 'Headquarters' dan Code menjadi 'HQ'
5. Klik tombol '[Save]'
6. Verifikasi toast notifikasi muncul: 'Success, division has been updated.'
7. Verifikasi nama divisi seed pada tabel utama berhasil terupdate menjadi 'Headquarters' dan Code menjadi 'HQ'

## Notes

- Record seed awal diizinkan untuk diedit sama seperti record biasa tanpa atribut yang mengunci (division.md §9.2 dan §10).
