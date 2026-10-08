---
id: TC-GS-DIV-E2E-012-role-matrix-positif-delete-single-dan-bulk-only
title: "Eksekusi Operasi Penghapusan oleh Aktor System Role Delete-Only (Single dan Bulk)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-28
  - TC-GS-DIV-29
coverage:
  web: automated
---

# Eksekusi Operasi Penghapusan oleh Aktor System Role Delete-Only (Single dan Bulk)

## Prerequisites

- Login sebagai Role: System Role Delete-Only
- Login sebagai Role: System Role capability Delete dan Read
- Tersedia divisi bebas relasi (Corporate Secretariat, Internal Affairs, Investor Relations)
- User berada di Global Settings > User > Division
- Division `Corporate Secretariat` bebas relasi (TC-GS-DIV-27)
- Division `Internal Affairs` dan `Investor Relations` bebas relasi (TC-GS-DIV-36, TC-GS-DIV-66)

## Test Steps

### Aktor Delete-saja berhasil menghapus Division bebas relasi (TC-GS-DIV-28)

1. Buka row action baris `Corporate Secretariat` lalu klik `Delete`
2. Klik `[Delete]` pada dialog konfirmasi
3. Verifikasi Dialog `Delete Division` tertutup
4. Verifikasi Muncul toast sukses: `Success, division has been deleted.`
5. Verifikasi Baris `Corporate Secretariat` hilang dari tabel

### Aktor Delete-saja berhasil menjalankan Bulk Delete (TC-GS-DIV-29)

6. Centang baris `Internal Affairs` dan `Investor Relations`
7. Klik aksi `[Delete]` pada Bulk Action Bar
8. Klik `[Delete]` pada dialog konfirmasi
9. Verifikasi Dialog `Delete Divisions` tampil dengan bullet `Internal Affairs` dan `Investor Relations`
10. Verifikasi Muncul toast sukses: `Success, division has been deleted.`
11. Verifikasi Kedua baris hilang dari tabel

## Notes

- Memvalidasi eksekusi penghapusan single dan bulk delete berhasil dilakukan oleh aktor Delete-only pada data bebas relasi (PRD §2, §4.8, §4.2d).
- Sumber pemetaan test case granular: TC-GS-DIV-28, TC-GS-DIV-29.
