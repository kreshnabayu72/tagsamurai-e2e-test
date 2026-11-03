---
id: TC-AC-CS-E2E-095-list-clear-filter-dan-clear-search-saat-kombinasi-aktif
title: "List: Clear Filter dan Clear Search Saat Kombinasi Aktif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-361
  - TC-AC-CS-362
  - TC-AC-CS-363
coverage:
  web: automated
---

# List: Clear Filter dan Clear Search Saat Kombinasi Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Pemulihan Search, Filter, dan Sort dilakukan sebagai langkah penghubung antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-361: Clear Filter saat Search dan Sort aktif

1. Ketik Search `Sejahtera`, tekan Enter
2. Klik header `Client` sekali
3. Klik ikon Filter, pilih Status `Active`, klik `[Apply]`
4. Klik `[Clear Field]`, lalu klik `[Apply]`
5. Verifikasi tabel menampilkan sedikitnya satu baris
6. Verifikasi kriteria filter terlepas
7. Verifikasi keyword `Sejahtera` dan sort Client ascending tetap aktif
8. Tutup panel Filter, klik `(←)` pada kotak Search, lalu klik header `Client` dua kali lagi

### TC-AC-CS-362: Clear Search saat Filter dan Sort aktif

9. Klik ikon Filter, pilih Status `Active`, klik `[Apply]`, lalu tutup panel Filter
10. Klik header `Client` sekali
11. Ketik Search `Sejahtera`, tekan Enter
12. Klik icon `(✕)`, lalu tekan Enter pada input kosong
13. Verifikasi keyword terlepas
14. Verifikasi tabel menampilkan sedikitnya satu baris
15. Verifikasi filter Status Active dan sort aktif tetap menyaring tabel
16. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`, tutup panel Filter, klik `(←)` pada kotak Search, lalu klik header `Client` dua kali lagi

### TC-AC-CS-363: Pemulihan dari empty state saat salah satu penyaring dilepas

17. Ketik Search `Apotek`, tekan Enter
18. Klik ikon Filter, pilih Status `Expired`, klik `[Apply]`
19. Verifikasi tabel menampilkan "No results found" dengan Description "Try adjusting your search or filter."
20. Klik `[Clear Field]`, lalu klik `[Apply]`
21. Verifikasi tabel pulih menampilkan baris yang cocok dengan keyword `Apotek`
22. Tutup panel Filter dan klik `(←)` pada kotak Search

## Notes

- Langkah penghubung: pembersihan Search, Filter, dan Sort antar blok serta penutupan panel.
- Temuan untuk QA: (1) TC-AC-CS-362 berjudul "Clear Search saat Filter dan Sort aktif" tetapi langkahnya tidak mengaktifkan Sort; spec menambahkan klik header `Client` sebagai langkah pembentuk precondition judul. (2) TC-AC-CS-361 langkah 5 menyebut `[Apply]`, `[Clear Field]`, `[Apply]` berurutan; spec mengikuti urutan TC. (3) TC-AC-CS-363 tidak menyebut baris yang dijamin ada untuk keyword `Apotek` pada status Expired; asersi empty state memakai dataset #82.
