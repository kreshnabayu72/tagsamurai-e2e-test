---
id: TC-AC-SG-E2E-030-delete-single-guard-has-members
title: "Guard Delete Single Kondisi #2: Pemblokiran penghapusan group yang masih memiliki Total Member > 0"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-59
coverage:
  web: automated
---

# Guard Delete Single Kondisi #2: Pemblokiran penghapusan group yang masih memiliki Total Member > 0

## Prerequisites

- Login sebagai Role: Total Control
- Group `"Branch Operational"` memiliki Total Member > 0 (mengikat entitas Client aktif)

## Test Steps

### Pemblokiran Delete Group Ber-Member
1. Buka `Settings > Group` dan cari baris `"Branch Operational"`
2. Verifikasi kolom Total Member menampilkan angka > 0
3. Klik menu elipsis `[⋯]` pada baris tersebut lalu pilih `[Delete]`
4. Verifikasi muncul dialog blokir informasi bertema danger/info `"Cannot Delete Group"`
5. Verifikasi body dialog menampilkan bullet nama group beserta pesan `"This group or its subgroups still have members. Remove all members before deleting."` dan tombol tunggal `[OK]`
6. Verifikasi tidak ada tombol konfirmasi lanjut
7. Klik `[OK]` dan verifikasi group tetap eksis di tabel

## Notes

- Kondisi #2 mengevaluasi gabungan node beserta seluruh subtree di bawahnya.
