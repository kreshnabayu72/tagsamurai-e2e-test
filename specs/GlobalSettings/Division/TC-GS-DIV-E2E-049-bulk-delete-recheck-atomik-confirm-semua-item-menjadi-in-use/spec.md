---
id: TC-GS-DIV-E2E-049-bulk-delete-recheck-atomik-confirm-semua-item-menjadi-in-use
title: "Re-Cek Atomik Bulk Delete Saat Confirm: Seluruh Item Berubah Menjadi In-Use Menolak Batch Tanpa Toast dan Seleksi Dipertahankan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-296
coverage:
  web: automated
---

# Re-Cek Atomik Bulk Delete Saat Confirm: Seluruh Item Berubah Menjadi In-Use Menolak Batch Tanpa Toast dan Seleksi Dipertahankan

## Prerequisites

- Login sebagai Role: Total Control
- Admin A membuka dialog bulk delete untuk divisi aman, sebelum Confirm Admin B mengaitkan user ke seluruh divisi tersebut
- User berada di Global Settings > User > Division
- Division `Audit Unit A` dan `Audit Unit B` sudah ada dan bebas relasi

## Test Steps

1. Sesi Admin A centang `Audit Unit A` dan `Audit Unit B`, klik aksi `[Delete]` (dialog `Delete Divisions`)
2. Sesi Admin B memindahkan satu user ke `Audit Unit A` dan satu user lain ke `Audit Unit B`
3. Sesi Admin A klik `[Delete]`
4. Verifikasi Dialog blokir in-use muncul dengan bullet `Audit Unit A` dan `Audit Unit B` dan tombol tunggal `[OK]`
5. Verifikasi Tidak ada toast sukses maupun toast item dilewati
6. Verifikasi Setelah `[OK]`: kedua baris tetap ada dan tetap tercentang; counter `2 Divisions selected`

## Notes

- Memvalidasi aturan re-cek atomik: jika seluruh item aman berubah in-use di antara buka dialog dan Confirm, batch ditolak via Dialog 2, tanpa toast, baris tetap ada dan tetap tercentang (PRD §9.4.2 baris Bulk Delete D6, toast-copy.md).
- Sumber pemetaan test case granular: TC-GS-DIV-296.
