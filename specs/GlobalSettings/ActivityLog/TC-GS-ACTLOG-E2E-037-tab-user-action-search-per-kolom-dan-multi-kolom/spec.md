---
id: TC-GS-ACTLOG-E2E-037-tab-user-action-search-per-kolom-dan-multi-kolom
title: "Tab User Action: Search Substring, Case-Insensitive, Modified By Nama Lengkap, dan Guard Date"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-150
  - TC-GS-ACTLOG-151
  - TC-GS-ACTLOG-152
  - TC-GS-ACTLOG-153
  - TC-GS-ACTLOG-154
  - TC-GS-ACTLOG-155
  - TC-GS-ACTLOG-156
  - TC-GS-ACTLOG-157
coverage:
  web: automated
---

# Tab User Action: Search Substring, Case-Insensitive, Modified By Nama Lengkap, dan Guard Date

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log User Action bervariasi

## Test Steps

### Pencarian Substring & Case-Insensitive
1. Buka Tab User Action, cari substring pada kolom Action ('Edit'), Object ('Brand'), Name ('Siti'), Field ('Division'), Old Value ('Marketing'), New Value ('Finance').
2. Verifikasi pencarian case-insensitive menghasilkan data yang sama (misal 'EDIT', 'brand', 'SITI').
### Pencarian Nama Admin Modified By
3. Masukkan nama depan 'hendra', verifikasi menemukan baris Modified By 'Hendra P'.
4. Masukkan nama belakang 'pratama', verifikasi menemukan baris 'Hendra P' (mencocokkan full underlying name).
### Guard Kolom Date & Kolom Tersembunyi
5. Masukkan keyword format tanggal (misal '14 Jun 2026'), verifikasi tidak ada baris yang cocok ('No results found').
6. Sembunyikan kolom Field via Setup Column, cari kata kunci 'Division', verifikasi tidak ditemukan.
7. Tampilkan kembali kolom Field, cari 'Division', verifikasi baris kembali ditemukan.
### Spasi & Pencarian Multi-Kolom
8. Masukkan keyword dengan spasi '  Brand  ', verifikasi spasi dipangkas dan hasil pencarian valid.
9. Masukkan keyword 'finance', verifikasi baris yang cocok pada New Value maupun Name/Object tampil bersamaan.

## Notes

- Pencarian teks Tab User Action mencakup 7 kolom visible dan mendukung pencarian nama lengkap admin.
