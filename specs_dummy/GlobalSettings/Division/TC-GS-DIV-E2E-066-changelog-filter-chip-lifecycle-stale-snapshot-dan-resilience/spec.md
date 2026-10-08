---
id: TC-GS-DIV-E2E-066-changelog-filter-chip-lifecycle-stale-snapshot-dan-resilience
title: "Filter Changelog: Siklus Manipulasi Chip, Overflow Chip, Loading State Dropdown, dan Persistensi Snapshot Master Terhapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-231
  - TC-GS-DIV-232
  - TC-GS-DIV-233
  - TC-GS-DIV-294
  - TC-GS-DIV-295
coverage:
  web: automated
---

# Filter Changelog: Siklus Manipulasi Chip, Overflow Chip, Loading State Dropdown, dan Persistensi Snapshot Master Terhapus

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terisi riwayat
- Divisi yang telah dihapus masih memiliki riwayat mutasi (snapshot)
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)
- Division `Snapshot Unit` (Code `SNU`) dibuat lewat `[+ Division]` sehingga memiliki entri Changelog Create (Tabel Data Uji Dinamis D-21)
- Riwayat memuat lebih dari 8 nama Division berbeda
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L); entri hasil TC-GS-DIV-101 dan TC-GS-DIV-102 ada

## Test Steps

### Dropdown filter Changelog menampilkan loading saat opsi masih diambil (TC-GS-DIV-231)

1. Klik icon Changelog di Table Tools
2. Tahan (delay) respons opsi filter
3. Buka Filter lalu buka dropdown Division Name
4. Verifikasi Dropdown menampilkan skeleton atau spinner (bukan daftar kosong tanpa indikator)
5. Verifikasi Opsi tampil setelah respons diterima

### Filter Division Name tetap berlaku pada snapshot setelah Division dihapus pihak lain (TC-GS-DIV-232)

6. Klik icon Changelog di Table Tools
7. Filter Division Name = `Snapshot Unit` lalu Apply
8. Admin lain menghapus Division `Snapshot Unit`
9. Muat ulang Modal Changelog dan filter ulang Division Name
10. Verifikasi Entri Changelog `Snapshot Unit` tetap tampil karena kolom Division Name adalah snapshot teks, bukan FK
11. Verifikasi Opsi `Snapshot Unit` tetap ada pada dropdown Division Name

### Banyak opsi terpilih pada field filter Changelog menampilkan overflow chip (TC-GS-DIV-233)

12. Klik icon Changelog di Table Tools
13. Buka Filter dan centang 8 opsi Division Name
14. Verifikasi Chip yang melebihi lebar field Division Name tersembunyi di belakang field (tidak wrap ke baris baru dan tidak ada ringkasan `+N more`)
15. Verifikasi 8 opsi tetap terpilih dan tetap berlaku sebagai kriteria filter setelah `[Apply]`

### Hapus chip lewat X pada field filter Division Name, Field, dan Modified By (TC-GS-DIV-294)

16. Klik icon Changelog di Table Tools lalu buka Filter
17. Pada field Division Name centang `Accounting and Tax` dan `Procurement`, klik `(X)` pada chip `Procurement` tanpa membuka dropdown
18. Pada field Field centang `Division Name` dan `Code`, klik `(X)` pada chip `Code`
19. Pada field Modified By centang `Sari D` dan `Rina M`, klik `(X)` pada chip `Rina M`
20. Buka dropdown tiap field
21. Verifikasi Tiap chip yang di-X hilang dari field sedangkan chip lain tetap ada
22. Verifikasi Di dalam dropdown checkbox opsi yang chip-nya dihapus ter-uncheck dan checkbox opsi lain tetap tercentang

### Uncheck opsi di dalam dropdown menghapus chip pada Division Name, Field, dan Modified By (TC-GS-DIV-295)

23. Klik icon Changelog di Table Tools lalu buka Filter
24. Pada field Division Name centang `Accounting and Tax` dan `Procurement`, lalu uncheck `Procurement` dari dalam dropdown yang terbuka
25. Pada field Field centang `Division Name` dan `Code`, lalu uncheck `Code` dari dalam dropdown
26. Pada field Modified By centang `Sari D` dan `Rina M`, lalu uncheck `Rina M` dari dalam dropdown
27. Verifikasi Pada ketiga field chip opsi yang di-uncheck hilang dari field sedangkan chip opsi lain tetap ada

## Notes

- Memvalidasi siklus hapus chip via icon (X) di form dan uncheck di dalam dropdown, penanganan overflow chip horizontal, tampilan loading skeleton pada dropdown filter, dan persistensi opsi nama divisi pada filter riwayat meskipun master divisi tersebut telah dihapus (PRD §4.1.2).
- Sumber pemetaan test case granular: TC-GS-DIV-231, TC-GS-DIV-232, TC-GS-DIV-233, TC-GS-DIV-294, TC-GS-DIV-295.
