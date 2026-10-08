---
id: TC-GS-DIV-E2E-046-bulk-delete-homogen-seluruh-item-bebas-relasi
title: "Bulk Delete Homogen (D-04): Seluruh Divisi Terpilih Bebas Relasi, Pembatalan Cancel, dan Konfirmasi Sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-132
  - TC-GS-DIV-133
  - TC-GS-DIV-137
coverage:
  web: automated
---

# Bulk Delete Homogen (D-04): Seluruh Divisi Terpilih Bebas Relasi, Pembatalan Cancel, dan Konfirmasi Sukses

## Prerequisites

- Login sebagai Role: Total Control
- Dua divisi bebas relasi (Engineering dan General Affairs)
- User berada di Global Settings > User > Division
- Division `Marketing` dan `Logistics` bebas relasi (TC-GS-DIV-30)
- Division `Engineering` dan `General Affairs` bebas relasi (TC-GS-DIV-30)
- Division `Risk Management` bebas relasi (TC-GS-DIV-30)

## Test Steps

### Konfirmasi Bulk Delete homogen menghapus seluruh Division terpilih (TC-GS-DIV-132)

1. Centang baris `Marketing` dan `Logistics`
2. Klik aksi `[Delete]` pada Bulk Action Bar
3. Klik `[Delete]` pada dialog
4. Verifikasi Dialog tertutup
5. Verifikasi Muncul toast sukses: `Success, division has been deleted.`
6. Verifikasi Baris `Marketing` dan `Logistics` hilang dari tabel
7. Verifikasi Bulk Action Bar tertutup dan seleksi bersih

### Cancel pada dialog Bulk Delete homogen tidak menghapus apa pun (TC-GS-DIV-133)

8. Centang baris `Engineering` dan `General Affairs`
9. Klik aksi `[Delete]` pada Bulk Action Bar
10. Klik `[Cancel]`
11. Verifikasi Dialog tertutup tanpa toast
12. Verifikasi Kedua baris tetap ada di tabel

### Bulk Delete dengan satu baris bebas relasi memakai dialog single (TC-GS-DIV-137)

13. Centang baris `Risk Management`
14. Klik aksi `[Delete]` pada Bulk Action Bar
15. Verifikasi Dialog `Delete Division` (single, bukan `Delete Divisions`) dengan bullet `Risk Management` dan `Are you sure you want to delete it? This action cannot be undone.`
16. Verifikasi Tombol `[Cancel]` dan `[Delete]`

## Notes

- Memvalidasi Dialog 4 (D-04: title "Delete Divisions", bullet daftar divisi, [Cancel] dan [Delete]) dan eksekusi penghapusan massal berhasil dengan toast sukses (PRD §4.2d, toast-copy.md §7).
- Sumber pemetaan test case granular: TC-GS-DIV-132, TC-GS-DIV-133, TC-GS-DIV-137.
