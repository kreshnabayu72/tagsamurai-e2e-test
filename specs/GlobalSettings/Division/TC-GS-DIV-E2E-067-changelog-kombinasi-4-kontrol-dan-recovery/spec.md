---
id: TC-GS-DIV-E2E-067-changelog-kombinasi-4-kontrol-dan-recovery
title: "Kombinasi Penuh Search, Filter, Sort, dan Pagination pada Modal Changelog Serta Independensi Pembersihan Masing-Masing Kontrol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-226
  - TC-GS-DIV-227
  - TC-GS-DIV-228
  - TC-GS-DIV-229
coverage:
  web: automated
---

# Kombinasi Penuh Search, Filter, Sort, dan Pagination pada Modal Changelog Serta Independensi Pembersihan Masing-Masing Kontrol

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terisi data riwayat
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)
- Riwayat memuat lebih dari 10 entri

## Test Steps

### Kombinasi Search, Filter, Sort, dan Pagination pada Modal Changelog (TC-GS-DIV-226)

1. Klik icon Changelog di Table Tools
2. Cari `a` lalu Enter
3. Filter Action = `Create` lalu Apply
4. Klik header Division Name sampai descending
5. Ubah page size ke 25
6. Verifikasi Seluruh kondisi berlaku bersamaan: irisan Search dan Filter terurut Division Name Z-A dengan page size 25

### Clear Filter Modal Changelog saat Search dan Sort aktif mempertahankan keduanya (TC-GS-DIV-227)

7. Klik icon Changelog di Table Tools
8. Cari `a` lalu Enter
9. Filter Action = `Create` lalu Apply
10. Klik header Date sampai Oldest First
11. Buka Filter, klik `[Clear Field]` dan `[Apply]`
12. Verifikasi Keyword `a` dan sort Date Oldest First tetap aktif setelah filter dilepas

### Clear Search Modal Changelog saat Filter dan Sort aktif mempertahankan keduanya (TC-GS-DIV-228)

13. Klik icon Changelog di Table Tools
14. Filter Action = `Create` lalu Apply
15. Cari `a` lalu Enter dan klik header Date sampai Oldest First
16. Klik `(✕)` lalu Enter pada input kosong
17. Verifikasi Filter Action `Create` dan sort Date Oldest First tetap aktif setelah Search dikosongkan

### Ganti kolom sort Modal Changelog saat Search dan Filter aktif tidak mereset saringan (TC-GS-DIV-229)

18. Klik icon Changelog di Table Tools
19. Cari `a` lalu Enter dan filter Action = `Create` lalu Apply
20. Klik header Action
21. Klik header Division Name
22. Verifikasi Sort berpindah ke kolom Division Name dan ikon sort Action kembali netral
23. Verifikasi Search dan Filter tetap aktif

## Notes

- Memvalidasi irisan presisi keempat kontrol pada Modal Changelog: membersihkan filter mempertahankan search dan sort, membersihkan search mempertahankan filter, dan pergantian kolom sort tidak mereset saringan aktif (PRD §4.1.2, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-226, TC-GS-DIV-227, TC-GS-DIV-228, TC-GS-DIV-229.
