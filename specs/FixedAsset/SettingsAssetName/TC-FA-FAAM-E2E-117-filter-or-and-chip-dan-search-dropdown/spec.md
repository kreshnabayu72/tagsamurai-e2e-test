---
id: TC-FA-FAAM-E2E-117-filter-or-and-chip-dan-search-dropdown
title: "Filter: OR dalam Field dan AND Antar-Field, Chip, +N more, dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-368
  - TC-FA-FAAM-369
  - TC-FA-FAAM-370
  - TC-FA-FAAM-371
  - TC-FA-FAAM-372
coverage:
  web: automated
---

# Filter: OR dalam Field dan AND Antar-Field, Chip, +N more, dan Search Dropdown

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Brand `Dell`, UoM `Unit`). Brand `Zebra` dan `Dell` adalah Brand master (Pre-setup #23); nama Asset Name ber-Brand `Zebra` tidak tertulis di Pre-setup, sehingga spec menyediakan salinan sendiri (Data Dinamis).
- Data Dinamis (suffix `{runId}-117`, seed API di hook `before`, dihapus lewat API di hook `after`): Asset Name `Zebra Item {runId}-117` (Code `ZBR117`, Category `IT Equipment`, TAG Type `QR`, Brand `Zebra`, UoM `Pcs`) sebagai baris pembanding irisan Brand `Dell` atau `Zebra` dan UoM `Pcs`.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-368: OR dalam satu field dan AND antar-field
1. Klik icon Filter
2. Pilih Brand `Dell` dan `Zebra`, lalu klik `[Apply]`
3. Verifikasi tabel menampilkan baris ber-Brand `Dell` (`Dell Latitude`) dan baris ber-Brand `Zebra` (`Zebra Item {runId}-117`) sebagai OR dalam satu field
4. Klik icon Filter, tambahkan UoM `Pcs`, lalu klik `[Apply]`
5. Verifikasi sedikitnya satu baris tampil (`Zebra Item {runId}-117`, Brand `Zebra`, UoM `Pcs`)
6. Verifikasi tabel hanya menampilkan baris yang memenuhi semua kriteria (Brand `Dell` atau `Zebra` dan UoM `Pcs`)
7. Verifikasi sedikitnya satu baris tampil (`Zebra Item {runId}-117`) sebagai pembanding asersi absence
8. Verifikasi baris `Dell Latitude` (UoM `Unit`) tidak tampil
### TC-FA-FAAM-369: Chip filter muncul di dalam field dan hapus lewat (✕) mengubah checkbox
9. Klik icon Filter, lalu klik `[Clear Field]`
10. Buka dropdown Brand dan pilih `Dell` lalu `Zebra`
11. Verifikasi chip `Dell` dan `Zebra` muncul di dalam field Brand
12. Klik `(✕)` pada chip `Zebra`
13. Verifikasi chip `Zebra` hilang dari field Brand
14. Verifikasi chip `Dell` tetap tampil
15. Buka dropdown Brand
16. Verifikasi opsi `Zebra` ter-uncheck
17. Klik `[Apply]`
18. Verifikasi tabel memakai opsi yang tersisa: baris `Dell Latitude` tampil
### TC-FA-FAAM-370: Chip filter: uncheck di dalam dropdown menghapus chip
19. Klik icon Filter, lalu klik `[Clear Field]`
20. Buka dropdown Brand dan pilih `Dell` lalu `Zebra`
21. Pada dropdown yang terbuka, uncheck `Zebra`
22. Verifikasi chip `Zebra` hilang dari field Brand
23. Verifikasi chip `Dell` tetap tampil
### TC-FA-FAAM-371: Banyak opsi terpilih diringkas menjadi chip +N more tanpa melebar
24. Klik `[Clear Field]`
25. Pilih seluruh opsi Brand yang tersedia
26. Verifikasi chip tampil sebanyak yang muat dan sisanya diringkas satu chip `+N more`
27. Verifikasi field Brand tidak melebar
28. Verifikasi field Brand tidak digulir horizontal
### TC-FA-FAAM-372: Search internal dropdown filter dan empty state
29. Klik `[Clear Field]`, lalu buka dropdown Brand
30. Ketik `del` di kotak cari dropdown
31. Verifikasi daftar menyempit ke `Dell` (substring tanpa membedakan huruf besar-kecil)
32. Ganti isi kotak cari dropdown dengan `zzz`
33. Verifikasi teks `No results found` tampil di dropdown
34. Klik icon Filter untuk menutup Filter Panel
35. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): klik `[Clear Field]` di awal tiap blok dan `[Clear Field]` lalu `[Apply]` terakhir (S-09); membuka kembali dropdown Brand pada TC-FA-FAAM-369 untuk mengamati checkbox opsi `Zebra`.
- Asersi universal (langkah 6) dan absence baris `Dell Latitude` (langkah 8) pada TC-FA-FAAM-368 didahului Verifikasi sedikitnya satu baris tampil (langkah 5 dan 7) sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA: TC-FA-FAAM-368 tidak menyebut nama Asset Name ber-Brand `Zebra` maupun UoM-nya; spec menyeed `Zebra Item {runId}-117` (Brand `Zebra`, UoM `Pcs`) sebagai baris pembanding, dan asersi tetap pada kriteria.
