---
id: TC-GS-USER-E2E-097-list-retensi-search-filter-sort
title: 'Search, Filter, Sort, dan seleksi baris di User List tidak saling mereset'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-213
  - TC-GS-USER-214
  - TC-GS-USER-215
  - TC-GS-USER-217
coverage:
  web: automated
---

# Search, Filter, Sort, dan seleksi baris di User List tidak saling mereset

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Data User List punya beberapa Division, Position, dan nama yang bervariasi
- Spec ini tidak mengubah data

## Test Steps

1. Ketik keyword di Search lalu Enter, terapkan Filter Division, dan urutkan kolom `Name`
2. Klik `[Clear Field]` pada Filter Panel lalu `[Apply Filter]`
3. Verifikasi kriteria Filter dilepas, sedangkan keyword Search dan arah Sort tetap aktif
4. Terapkan Filter Division lagi lalu hapus teks di search box dan tekan `Enter`
5. Verifikasi keyword dikosongkan, sedangkan Filter dan arah Sort tetap aktif
6. Terapkan Search lagi, lalu klik sort kolom `Position`
7. Verifikasi Sort berpindah ke `Position` tanpa mereset Search dan Filter
8. Centang satu baris, lalu terapkan Search dan Filter, kemudian kosongkan keduanya
9. Verifikasi centang pada baris itu tetap bertahan

## Notes

- Sumber `user.md` bagian 4.4 dan `prd-conventions.md` bagian 9.6 (Search, Filter, dan Sort adalah tiga state independen).
