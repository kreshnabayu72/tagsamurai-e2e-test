---
id: TC-AC-SG-E2E-039-bulk-delete-blokir-total-seluruhnya-ber-member
title: "Pemblokiran total Bulk Delete ketika seluruh baris terpilih memiliki Total Member > 0"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-172
coverage:
  web: automated
---

# Pemblokiran total Bulk Delete ketika seluruh baris terpilih memiliki Total Member > 0

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat ≥ 2 group yang dipilih via checkbox, semuanya memiliki Total Member > 0, dan bukan seluruh populasi entitas

## Test Steps

### Pemblokiran Total Seluruhnya Ber-Member
1. Centang ≥ 2 baris group yang semuanya memiliki member (0 group yang aman diproses)
2. Klik tombol `[Delete]` pada Bulk Action Bar
3. Verifikasi dialog yang muncul adalah dialog blokir langsung bertitel plural `"Cannot Delete Groups"`
4. Verifikasi body dialog menampilkan bullet list seluruh group terpilih dengan teks `"These groups or their subgroups still have members. Remove all members before deleting."` dan tombol tunggal `[OK]`
5. Verifikasi TIDAK ADA kelompok "The following will be deleted" (karena 0 yang processable)
6. Verifikasi dialog berbeda dari dialog would-empty (tidak membahas sisa jumlah grup)
7. Klik `[OK]` dan verifikasi tidak ada group yang terhapus

## Notes

- Dialog ini adalah bentuk jamak dari dialog blok single ada-member.
