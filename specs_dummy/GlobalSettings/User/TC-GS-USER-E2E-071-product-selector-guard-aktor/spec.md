---
id: TC-GS-USER-E2E-071-product-selector-guard-aktor
title: 'Opsi Product Selector yang tidak boleh dibaca aktor hilang dari daftar'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-456
coverage:
  web: automated
---

# Opsi Product Selector yang tidak boleh dibaca aktor hilang dari daftar

## Prerequisites

- Login sebagai aktor yang punya izin Read Settings > User di Global Settings tetapi tidak di FAMS
- User "Ahmad Fauzi" punya Access ke FAMS dan Global Settings
- Spec ini tidak mengubah data

## Test Steps

1. Buka User Detail "Ahmad Fauzi" lalu buka selector "Viewing: [Global Settings ▾]"
2. Verifikasi opsinya hanya Global Settings dan FAMS tidak muncul sama sekali, bukan tampil dalam keadaan disabled atau abu-abu

## Notes

- Sumber `user.md` bagian 9.2 ([F-USER-16]). Opsi disembunyikan agar keberadaan produk yang kontennya tidak boleh dilihat aktor tidak bocor.
- Sisi positif (aktor dengan izin di kedua produk) dicakup `TC-GS-USER-E2E-070-product-selector-opsi-dan-navigasi`.
