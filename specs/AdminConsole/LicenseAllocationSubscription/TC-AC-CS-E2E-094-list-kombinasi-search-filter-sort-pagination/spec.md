---
id: TC-AC-CS-E2E-094-list-kombinasi-search-filter-sort-pagination
title: "List: Kombinasi Search Filter Sort Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-358
  - TC-AC-CS-359
  - TC-AC-CS-360
  - TC-AC-CS-364
coverage:
  web: automated
---

# List: Kombinasi Search Filter Sort Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Data Dinamis TC-AC-CS-364 (bersuffix `{runId}-094`): satu term SAMS baru dibuat spec lewat `[+ Subscription]` dengan Client, Plan, Duration, dan Start Date valid (nilai tidak ditetapkan TC; disediakan tim FE). Term itu dibersihkan fixture backend di hook `after`. Efek: Last Updated Client terkait dan entri audit trail permanen.
- Pemulihan Search, Filter, Sort, dan page size dilakukan sebagai langkah penghubung antar blok; term baru dibersihkan fixture backend yang disediakan tim FE/BE.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-358: Alur Search lalu Filter menghasilkan irisan

1. Ketik Search `Sejahtera`, tekan Enter
2. Klik ikon Filter, pilih Status `Active`, klik `[Apply]`
3. Verifikasi tabel menampilkan sedikitnya satu baris
4. Verifikasi hasil adalah irisan baris yang memuat `Sejahtera` dan berstatus Active
5. Verifikasi menerapkan filter tidak mereset keyword Search
6. Klik `[Clear Field]`, klik `[Apply]`, tutup panel Filter, lalu klik `(←)` pada kotak Search

### TC-AC-CS-359: Alur Filter lalu Search menghasilkan irisan yang sama

7. Klik ikon Filter, pilih Status `Active`, klik `[Apply]`, lalu tutup panel Filter
8. Ketik Search `Sejahtera`, tekan Enter
9. Verifikasi tabel menampilkan sedikitnya satu baris
10. Verifikasi hasil identik dengan alur Search lalu Filter
11. Verifikasi kriteria filter tetap aktif di latar belakang
12. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`, tutup panel Filter, lalu klik `(←)` pada kotak Search

### TC-AC-CS-360: Kombinasi Search, Filter, Sort, dan Pagination aktif bersamaan

13. Ketik Search `a`, tekan Enter
14. Klik ikon Filter, pilih Product `FAMS`, klik `[Apply]`, lalu tutup panel Filter
15. Klik header `Client` sekali
16. Ubah page size menjadi 25
17. Verifikasi tabel menampilkan sedikitnya satu baris
18. Verifikasi hasil memenuhi keyword, filter Product FAMS, urutan Client ascending, dan 25 baris per halaman sekaligus
19. Verifikasi tidak ada kontrol yang saling menimpa
20. Klik header `Client` dua kali lagi, kembalikan page size ke nilai awal, klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`, tutup panel, lalu klik `(←)` pada kotak Search

### TC-AC-CS-364: Create saat tabel terfilter: record yang tidak cocok tidak muncul

21. Klik ikon Filter, pilih Product `FAMS`, klik `[Apply]`, lalu tutup panel Filter
22. Klik `[+ Subscription]`, isi form dengan data valid Product `SAMS` milik spec, lalu klik `[Submit]`
23. Tunggu aksi selesai: modal form tertutup
24. Verifikasi sedikitnya satu baris Product `FAMS` tampil pada tabel yang difilter
25. Verifikasi term SAMS baru tidak tampil pada tabel yang difilter Product FAMS
26. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`, tutup panel Filter
27. Ketik Search dengan Client term SAMS baru, tekan Enter
28. Verifikasi term SAMS baru tampil setelah filter dilepas
29. Bersihkan term SAMS baru lewat fixture backend

## Notes

- Langkah penghubung: pembersihan Search, Filter, Sort, dan page size antar blok, penutupan panel, serta pencarian term baru (R-16).
- Temuan untuk QA: (1) TC-AC-CS-364 langkah 3 "Buat term SAMS lewat `[+ Subscription]`" tidak menyebut Client, Plan, Duration, dan Start Date; spec tidak mengarang nilai dan menandai data valid disediakan tim FE. (2) TC-AC-CS-360 tidak menyebut nilai awal page size; spec mengembalikan ke nilai awal. (3) TC-AC-CS-358 dan TC-AC-CS-359 tidak menyebut jumlah baris irisan; asersi hanya relasi irisan.
