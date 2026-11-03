---
id: TC-AC-CS-E2E-090-list-filter-pencarian-dalam-dropdown-dan-chip
title: "List Filter: Pencarian dalam Dropdown dan Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-340
  - TC-AC-CS-341
  - TC-AC-CS-342
  - TC-AC-CS-343
coverage:
  web: automated
---

# List Filter: Pencarian dalam Dropdown dan Chip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-340: Pencarian di dalam dropdown filter kelas entitas

1. Klik ikon Filter, buka dropdown Client, ketik `sejah` di kotak pencarian dropdown
2. Verifikasi sedikitnya satu opsi Client tampil di dropdown
3. Verifikasi daftar opsi menyempit ke Client yang memuat `sejah` (substring, tanpa membedakan huruf besar kecil)
4. Ganti isi kotak pencarian dropdown dengan `zzzz`
5. Verifikasi teks "No results found" tampil tanpa opsi cocok
6. Tutup dropdown Client, buka dropdown Plan, ketik `zzzz` di kotak pencarian dropdown
7. Verifikasi teks "No results found" tampil di dropdown Plan
8. Tutup dropdown Plan, buka dropdown Plan Owner, ketik `zzzz` di kotak pencarian dropdown
9. Verifikasi teks "No results found" tampil di dropdown Plan Owner
10. Tutup dropdown Plan Owner

### TC-AC-CS-341: Pencarian di dalam dropdown filter kelas enum

11. Buka dropdown Status, ketik `act` di kotak pencarian dropdown
12. Verifikasi dropdown Status menyempit ke `Active` (substring tanpa membedakan huruf besar kecil)
13. Tutup dropdown Status, buka dropdown Product, ketik `z` di kotak pencarian dropdown
14. Verifikasi dropdown Product memiliki kotak pencarian internal dan menampilkan teks "No results found"
15. Tutup dropdown Product, buka dropdown Type, ketik `z` di kotak pencarian dropdown
16. Verifikasi dropdown Type memiliki kotak pencarian internal dan menampilkan teks "No results found"
17. Tutup dropdown Type

### TC-AC-CS-342: Opsi terpilih tampil sebagai chip di dalam field

18. Buka dropdown Status, centang `Active`
19. Verifikasi chip "Active" tampil di dalam field Status
20. Centang `Expired`
21. Verifikasi chip "Expired" tampil di samping chip pertama dan tidak menggantikannya

### TC-AC-CS-343: Hapus chip lewat icon silang meng-uncheck opsi dan chip lain tetap

22. Klik icon `(✕)` pada chip `Active` tanpa membuka dropdown
23. Verifikasi chip `Active` hilang
24. Verifikasi chip `Expired` tetap ada
25. Buka dropdown Status
26. Verifikasi checkbox `Active` di dalam dropdown ter-uncheck
27. Verifikasi checkbox `Expired` tetap tercentang
28. Tutup dropdown Status, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Anchor positif: Verifikasi "sedikitnya satu opsi Client tampil" mendahului asersi penyempitan daftar opsi (8b.2).
- Langkah penghubung: penutupan dropdown dan `[Clear Field]` serta `[Apply]` di akhir blok.
- Temuan untuk QA: (1) TC-AC-CS-340 butir c ("Perilaku sama pada dropdown Plan dan Plan Owner") tidak punya langkah di TC; spec mengasersinya dengan keyword `zzzz` pada dropdown Plan dan Plan Owner. (2) TC-AC-CS-343 langkah 3 memilih Status `Active` dan `Expired` lalu menghapus chip; blok TC-AC-CS-342 meninggalkan kedua chip terpilih sehingga langkah pemilihan tidak diulang.
