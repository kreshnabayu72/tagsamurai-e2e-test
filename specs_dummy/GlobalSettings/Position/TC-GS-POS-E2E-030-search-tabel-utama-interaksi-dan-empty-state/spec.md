---
id: TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state
title: "Search tabel utama: siklus interaksi, substring, case-insensitive, trim, empty state, dan scope kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-152
  - TC-GS-POS-153
  - TC-GS-POS-154
  - TC-GS-POS-155
  - TC-GS-POS-156
  - TC-GS-POS-157
  - TC-GS-POS-158
coverage:
  web: automated
---

# Search tabel utama: siklus interaksi, substring, case-insensitive, trim, empty state, dan scope kolom

## Prerequisites

- Login sebagai Role: Total Control
- Master data Position memuat: "IT Manager", "Finance Analyst", "Warehouse Supervisor"

## Test Steps

### Siklus Interaksi Search

1. Buka Global Settings > User > Position
2. Klik ikon Search di toolbar Table Tools untuk membuka field input pencarian
3. Masukkan substring "mana" (huruf kecil)
4. Verifikasi hasil tabel menyaring record yang memuat kata tersebut case-insensitive (misal: "IT Manager")
5. Masukkan keyword dengan spasi di awal dan akhir "  analyst  "
6. Verifikasi sistem mengabaikan spasi luar dan menampilkan "Finance Analyst"

### Scope Kolom & No-Result Empty State

7. Masukkan keyword berupa tanggal/waktu (misal "2026")
8. Verifikasi pencarian tidak mencari nilai pada kolom Last Updated (hanya kolom Name)
9. Masukkan keyword acak tanpa kecocokan "xyznonexistent999"
10. Verifikasi tabel menampilkan empty state hasil pencarian: "No results found"
11. Klik tombol bersihkan `[✕]` pada input Search
12. Verifikasi seluruh baris data kembali tampil normal di tabel

## Notes

- Menggabungkan seluruh pengujian search tabel utama dari TC-GS-POS-152 s.d. 158.
