---
id: TC-FA-LBL-E2E-033-labels-list-filter-panel-per-kolom
title: "Labels List: Filter Panel per kolom"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:defaults-ordering-spec/default-filter-tabel
  - FALB:obl/T-ALB-01/filter/FLD-03
  - FALB:obl/T-ALB-01/filter/FLD-04
  - FALB:obl/T-ALB-01/filter/FLD-05
  - FALB:obl/T-ALB-01/filter-panel
coverage:
  web: automated
---

# Labels List: Filter Panel per kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-56` (12 label bersuffix `Lst-{runId}-033-01` sampai `Lst-{runId}-033-12`). Persebaran Total Asset `DU-56` mencakup sedikitnya satu label untuk tiap nilai 0, 1, 2, dan 3; Modified By berasal dari dua pelaku (`DU-01` dan `DU-31`); semua label seed memiliki Last Updated pada tanggal seeding. `DU-31` (akun Total Control kedua, env `FA_TC2_EMAIL`, `FA_TC2_PASSWORD`) dipakai hanya sebagai pelaku kedua lewat sesi API saat seeding; tidak login di UI.
- Nilai batas filter Total Asset pada langkah 5 dan 6 (Min 1, Max 2) dipilih dari rentang Total Asset `DU-56`.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset.
- State global: tidak ada yang diubah. Hook `after` menghapus label seed `DU-56` lewat sesi API.

## Test Steps

### FALB:defaults-ordering-spec/default-filter-tabel: Tidak ada filter ter-Apply saat halaman dibuka

1. Verifikasi ikon Filter tidak menampilkan badge titik dan Labels List menampilkan sedikitnya satu baris label tanpa filter ter-Apply

### FALB:obl/T-ALB-01/filter/FLD-03: Filter kolom Total Asset

2. Ketik Search `DU-56` (nama dasar `Lst-{runId}-033`), tekan Enter
3. Klik ikon Filter di toolbar
4. Verifikasi field filter Total Asset berlabel `Total Asset` berupa rentang dengan input pertama berplaceholder `Min` dan input kedua berplaceholder `Max`
5. Isi input `Min` pada field Total Asset dengan 1
6. Isi input `Max` pada field Total Asset dengan 2
7. Klik `[Apply]`
8. Verifikasi Labels List menampilkan sedikitnya satu baris label `DU-56`
9. Verifikasi setiap baris label `DU-56` pada Labels List memiliki Total Asset 1 atau 2
10. Verifikasi baris `DU-56` ber-Total Asset 0 dan baris `DU-56` ber-Total Asset 3 tidak tampil
11. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-01/filter/FLD-04: Filter kolom Modified By

12. Verifikasi field filter Modified By berlabel `Modified By` berplaceholder `All users`
13. Buka dropdown pada field Modified By
14. Verifikasi dropdown memuat kotak pencarian dan opsi untuk user `DU-01` dan `DU-31`
15. Pilih opsi user `DU-31`
16. Verifikasi chip user `DU-31` tampil di dalam field Modified By
17. Klik `[Apply]`
18. Verifikasi baris `DU-56` yang dimodifikasi `DU-31` tampil di Labels List
19. Verifikasi baris `DU-56` yang dimodifikasi `DU-01` tidak tampil di Labels List
20. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-01/filter/FLD-05: Filter kolom Last Updated

21. Verifikasi field filter Last Updated berlabel `Last Updated` berupa date range picker berplaceholder `Select date`
22. Pilih rentang satu hari pada field Last Updated dengan tanggal awal sama dengan tanggal akhir, yaitu tanggal seeding `DU-56`
23. Klik `[Apply]`
24. Verifikasi baris label `DU-56` tampil di Labels List
25. Pilih rentang satu hari pada field Last Updated pada satu hari sebelum tanggal seeding `DU-56`
26. Klik `[Apply]`
27. Verifikasi empty state Labels List menampilkan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
28. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-01/filter-panel: Filter Panel, Apply, Clear Field, dan kombinasi antar field

29. Verifikasi Filter Panel tampil di bawah toolbar dengan field Total Asset, Modified By, dan Last Updated, tombol `[Clear Field]` di kiri dan `[Apply]` di kanan
30. Pilih opsi user `DU-31` pada field Modified By
31. Pilih rentang satu hari pada field Last Updated dengan tanggal seeding `DU-56`
32. Klik `[Apply]`
33. Verifikasi baris `DU-56` yang dimodifikasi `DU-31` pada tanggal seeding tampil di Labels List
34. Verifikasi baris `DU-56` yang dimodifikasi `DU-01` tidak tampil di Labels List (hanya baris yang memenuhi kedua kriteria tampil)
35. Klik `[Clear Field]`
36. Verifikasi field Total Asset, Modified By, dan Last Updated kosong
37. Klik `[Apply]`
38. Verifikasi baris `DU-56` yang dimodifikasi `DU-01` dan baris `DU-56` yang dimodifikasi `DU-31` tampil di Labels List

## Notes

- Langkah penghubung (S-03): langkah 2 (Search yang mempersempit tabel ke label `DU-56`, R-16), langkah 3 (membuka Filter Panel), langkah 11, 20, dan 28 (mengosongkan filter sebelum blok berikutnya, S-09).
- Anchor positif (bagian 8b butir 2): langkah 8 membuktikan hasil tersaring tidak kosong sebelum langkah 10; langkah 18 menjadi anchor langkah 19; langkah 33 menjadi anchor langkah 34; langkah 24 membuktikan rentang tanggal seeding inklusif sebelum langkah 27.
- Pembagian klausa lintas spec: `FALB:defaults-ordering-spec/default-filter-tabel` berlaku untuk Labels List (langkah 1), Tagged Asset List (spec 046), dan Modal Changelog (spec 056); tiap spec mengasersi tabelnya sendiri.
- Opsi dropdown Modified By pada langkah 14 diasersi sebagai opsi untuk user `DU-01` dan `DU-31` tanpa format teks opsi, karena PRD tidak menyatakan format teks opsi itu.
- Spec ini di atas smell 35 langkah (38 langkah). Alasan dipertahankan: seluruh blok satu kelas harness (Filter Panel) pada dataset `DU-56` yang sama, dan tiap blok diakhiri dengan `[Clear Field]` dan `[Apply]` sehingga berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
