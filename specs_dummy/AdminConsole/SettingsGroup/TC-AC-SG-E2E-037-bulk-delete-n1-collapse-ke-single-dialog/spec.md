---
id: TC-AC-SG-E2E-037-bulk-delete-n1-collapse-ke-single-dialog
title: "Perilaku Bulk Delete N=1: konversi otomatis ke dialog konfirmasi tunggal (aman maupun terblokir)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-170
  - TC-AC-SG-171
coverage:
  web: automated
---

# Perilaku Bulk Delete N=1: konversi otomatis ke dialog konfirmasi tunggal (aman maupun terblokir)

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia Group A (0 member) dan Group B (memiliki member)

## Test Steps

### Collapse N=1 Varian Aman
1. Centang HANYA 1 checkbox pada baris Group A (aman)
2. Verifikasi Bulk Action Bar muncul dengan counter `1 selected`
3. Klik tombol `[Delete]` pada Bulk Action Bar
4. Verifikasi dialog yang muncul adalah dialog row-action single bertitel singular `"Delete Group"` (bukan `"Delete Groups"`)
5. Verifikasi body dialog hanya memuat 1 bullet nama Group A dengan penutup `"Are you sure you want to delete it?"` (tanpa framing jamak bulk)
6. Klik `[Cancel]` untuk menutup dialog
### Collapse N=1 Varian Terblokir (Ada Member)
7. Hapus centang Group A lalu centang HANYA Group B (ada member)
8. Klik tombol `[Delete]` pada Bulk Action Bar
9. Verifikasi dialog yang muncul adalah dialog blokir tunggal singular `"Cannot Delete Group"` (bukan plural)
10. Verifikasi body dialog menampilkan bullet Group B beserta teks `"This group or its subgroups still have members..."` dengan tombol tunggal `[OK]`

## Notes

- Aturan collapse N=1 mencegah inkonsistensi copy jamak saat hanya 1 baris yang dipilih via checkbox.
