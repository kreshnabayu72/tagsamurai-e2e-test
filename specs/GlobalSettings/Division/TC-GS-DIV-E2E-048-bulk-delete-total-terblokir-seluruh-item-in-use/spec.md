---
id: TC-GS-DIV-E2E-048-bulk-delete-total-terblokir-seluruh-item-in-use
title: "Pemblokiran Total Bulk Delete (D-02): Seluruh Divisi Terpilih In-Use dengan Bullet Diperluas dan Tombol Tunggal OK"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-136
  - TC-GS-DIV-138
coverage:
  web: automated
---

# Pemblokiran Total Bulk Delete (D-02): Seluruh Divisi Terpilih In-Use dengan Bullet Diperluas dan Tombol Tunggal OK

## Prerequisites

- Login sebagai Role: Total Control
- Pilih >=2 divisi yang semuanya in-use (Human Resources dan Operations)
- User berada di Global Settings > User > Division
- Division `Human Resources` dan `Operations` dipakai user
- Division `Compliance` dipakai Non-Login User

## Test Steps

### Bulk Delete seluruhnya in-use menampilkan Dialog blokir dengan bullet diperluas (TC-GS-DIV-136)

1. Centang baris `Human Resources` dan `Operations`
2. Klik aksi `[Delete]` pada Bulk Action Bar
3. Verifikasi Dialog `Cannot Delete Data` tampil (bukan Dialog `Delete Divisions` dengan kelompok kosong)
4. Verifikasi Body: bullet `Human Resources — still in use` dan `Operations — still in use`, lalu `These divisions are still in use. Remove the references before deleting.`
5. Verifikasi Satu tombol `[OK]`; tidak ada toast sukses

### Bulk Delete dengan satu baris in-use memakai dialog blokir single (TC-GS-DIV-138)

6. Centang baris `Compliance`
7. Klik aksi `[Delete]` pada Bulk Action Bar
8. Verifikasi Dialog `Cannot Delete Data` bentuk single: bullet `Compliance — still in use`, lalu `This division is still in use. Remove the references before deleting.`
9. Verifikasi Satu tombol `[OK]`

## Notes

- Memvalidasi bahwa saat seluruh item terpilih in-use, sistem menampilkan Dialog 2 (D-02) dengan bullet diperluas dan tombol tunggal [OK], BUKAN Dialog 3 dengan bagian "will be deleted" kosong (PRD §4.2d tabel evaluasi bulk).
- Sumber pemetaan test case granular: TC-GS-DIV-136, TC-GS-DIV-138.
