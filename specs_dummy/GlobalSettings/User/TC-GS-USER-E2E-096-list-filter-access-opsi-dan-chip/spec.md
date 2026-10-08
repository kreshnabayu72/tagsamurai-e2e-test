---
id: TC-GS-USER-E2E-096-list-filter-access-opsi-dan-chip
title: 'Filter Access di User List: isi opsi, pencarian, logika OR, dan chip'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-203
  - TC-GS-USER-204
  - TC-GS-USER-205
  - TC-GS-USER-256
coverage:
  web: automated
---

# Filter Access di User List: isi opsi, pencarian, logika OR, dan chip

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Entity punya user dengan Access ke Global Settings dan FAMS, dan tidak ada user yang ber-Access ke produk lain yang tidak dipakai (mis. SIEM)
- Sedikitnya satu user dengan Access ke empat produk atau lebih supaya chip melebihi satu baris
- Spec ini tidak mengubah data

## Test Steps

1. Buka Filter Panel lalu buka dropdown field Access
2. Verifikasi opsi hanya berisi produk yang sedang di-Access oleh minimal satu user di tabel (produk yang tidak dipakai siapa pun tidak muncul)
3. Ketik "FAMS" di pencarian dalam dropdown
4. Verifikasi opsi tersaring hanya yang cocok dengan "FAMS"
5. Hapus teks pencarian, pilih `FAMS` dan `Global Settings`, lalu klik `[Apply Filter]`
6. Verifikasi baris yang ditampilkan adalah user dengan Access mencakup `FAMS` atau `Global Settings` (OR dalam satu field)
7. Buka Filter Panel dan pilih empat opsi Access atau lebih lalu klik `[Apply Filter]`
8. Verifikasi chip terpilih tampil di field dan kelebihan ditampilkan "+N more"
9. Klik `(X)` pada satu chip
10. Verifikasi satu opsi terlepas tanpa menutup dropdown dan tanpa mereset opsi lain
11. Buka dropdown Access dan hapus centang satu checkbox yang sudah tercentang di dalam dropdown
12. Verifikasi chip yang bersangkutan langsung hilang dari field, chip lain tetap ada
13. Tutup dropdown lalu klik `[Apply Filter]`
14. Verifikasi hasil filter mengikuti opsi yang tersisa

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.5 (isi opsi, search-within-dropdown, OR, chip).
