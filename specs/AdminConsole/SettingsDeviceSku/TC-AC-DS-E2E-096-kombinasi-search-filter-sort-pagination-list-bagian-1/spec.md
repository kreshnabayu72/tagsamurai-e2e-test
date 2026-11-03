---
id: TC-AC-DS-E2E-096-kombinasi-search-filter-sort-pagination-list-bagian-1
title: "Kombinasi List: Search Lalu Filter, Filter Lalu Search, dan Kombinasi Penuh dengan Sort dan Pagination"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-327
  - TC-AC-DS-328
  - TC-AC-DS-329
coverage:
  web: automated
---

# Kombinasi List: Search Lalu Filter, Filter Lalu Search, dan Kombinasi Penuh dengan Sort dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti; Model/Type `T-OBJ` pada `TAG-ARC-OBJ`, `SRT-A` pada `SRT-ANG-01`, `SRT-B` pada `SRT-APL-01`) dan #30 (`SEED-001` sampai `SEED-119`, Model/Type `SEED`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; Search, Filter, Sort, dan ukuran halaman dipulihkan oleh langkah pemulihan di akhir tiap bagian.

## Test Steps

### TC-AC-DS-327: Search lalu Filter

1. Ketik Search `Reader`, tekan Enter
2. Klik ikon Filter
3. Pada field Brand pilih `Veltrix`
4. Klik `[Apply]`
5. Verifikasi tabel hanya memuat baris yang cocok Search `Reader` dan Brand `Veltrix`: `SFR-VEL-4P` (Device Name `4-Port Fixed Reader`, Category `Portal Reader`) dan `SFR-ZERO-01` (Category `Tunnel Reader`)
6. Verifikasi penerapan Filter tidak mereset kata kunci Search: kotak pencarian masih berisi `Reader`
7. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik `(←)` pada kotak Search

### TC-AC-DS-328: Filter lalu Search

8. Pada field Brand pilih `Veltrix`
9. Klik `[Apply]`
10. Ketik Search `Reader`, tekan Enter
11. Verifikasi hasil sama dengan urutan Search lalu Filter: baris `SFR-VEL-4P` dan `SFR-ZERO-01`
12. Verifikasi kriteria Brand `Veltrix` tetap aktif di latar belakang: Filter Panel menampilkan Brand `Veltrix`
13. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik `(←)` pada kotak Search

### TC-AC-DS-329: Kombinasi penuh Search, Filter, Sort, dan Pagination

14. Ketik Search `Arcturus`, tekan Enter
15. Pada field TAG Type pilih `Object`
16. Klik `[Apply]`
17. Klik header kolom Model/Type dua kali sampai Descending aktif
18. Ubah jumlah data per halaman menjadi 25
19. Verifikasi tabel memuat baris Brand `Arcturus` dengan TAG Type `Object` (mis. `TAG-ARC-OBJ`)
20. Verifikasi baris terurut Model/Type Descending (`T-OBJ` mendahului `SRT-B`, `SRT-B` mendahului `SRT-A`)
21. Verifikasi tabel menampilkan 25 baris per halaman
22. Verifikasi keempat kontrol tetap aktif tanpa saling menimpa: Search `Arcturus`, Filter TAG Type `Object`, Sort Model/Type Descending, dan 25 baris per halaman
23. Klik `[Clear Field]`, lalu `[Apply]`, klik header kolom Model/Type sekali sampai netral, ubah jumlah data per halaman menjadi 10, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09): langkah 7, 13, dan 23 memulihkan Search, Filter, Sort, dan ukuran halaman agar bagian berikutnya tidak mengandalkan state sebelumnya; tanpa asersi.
- Langkah 12 mengamati kriteria Filter lewat nilai ter-Apply pada Filter Panel; TC-AC-DS-328 tidak menyebut cara pengamatannya.
- Langkah 20 memakai Model/Type dari Pre-setup #29 sebagai turunan Expected "terurut Model/Type Descending"; TC tidak menyebut nilai barisnya.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `SFR-VEL-4P`, `TAG-ARC-OBJ`). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
