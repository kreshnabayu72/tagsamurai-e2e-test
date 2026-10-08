---
id: TC-AC-SG-E2E-009-context-header-dan-dual-entry-point
title: "Karakteristik Group Context Header murni display dan kesetaraan dual entry point"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-15
  - TC-AC-SG-16
  - TC-AC-SG-17
  - TC-AC-SG-29
coverage:
  web: automated
---

# Karakteristik Group Context Header murni display dan kesetaraan dual entry point

## Prerequisites

- Login sebagai Role: Total Control atau Manage group
- Terdapat node level 1 `"Region A"` dan subgroup `"Branch 1"`

## Test Steps

### Group Context Header Display Info
1. Buka `Settings > Group` dalam status default "All Groups"
2. Verifikasi Group Context Header hanya berupa display teks polos tanpa Group Code dan tanpa tombol menu elipsis `[⋯]`
3. Klik node `"Region A"` di sidebar hingga menjadi header aktif
4. Verifikasi Group Context Header tetap murni display info (`Region A | Total User | Total Member`) tanpa icon/menu elipsis aksi apa pun
### Dual Entry Point Row Action vs Sidebar
5. Klik elipsis `[⋯]` pada baris `"Branch 1"` di tabel utama, amati opsi menu yang muncul (`+ Add Subgroup`, `Edit`, `Delete`)
6. Klik elipsis `[⋯]` pada node `"Branch 1"` di sidebar, amati opsi menu yang muncul
7. Verifikasi opsi menu pada kedua entry point identik dan memicu modal form yang setara
### Single Entry Point untuk Node Header
8. Saat `"Region A"` sedang aktif sebagai header (tidak tampil sebagai baris di tabel)
9. Verifikasi satu-satunya jalan untuk melakukan `Edit`, `Delete`, atau `+ Add Subgroup` pada Region A adalah melalui elipsis `[⋯]` di sidebar

## Notes

- Group Context Header tidak memiliki aksi apa pun untuk menjaga konsistensi parity FAMS (ACSG-LOGIC-05).
