---
id: TC-FA-TDC-E2E-247-search-kolom-non-searchable-effective-from-last-updated-dan-active
title: "Search: Kolom Non-Searchable Effective From, Last Updated, dan Active"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-496
  - TC-FA-TDC-497
sourceRules: ["§5#b2", "ST-23", "§4.1.1#b3", "§5#b3"]
smoke: []
dependsOn: []
trace:
  "§5#b2": [6, 8]
  "ST-23": [6, 8, 14, 16]
  "§4.1.1#b3": [14, 16, 21]
  "§5#b3": 21
coverage:
  web: automated
---

# Search: Kolom Non-Searchable Effective From, Last Updated, dan Active

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. NB-1 dan NB-4 memiliki Effective From `Jan 2026`; NB-OLD berstatus Inactive dan 8 class lain Active; tidak ada kolom lain yang memuat teks `Active` atau `Inactive`. Kolom Last Updated Hidden (default) dan ditampilkan oleh langkah spec; teks Last Updated NB-SL disalin dari selnya.
- Data uji (keyword Search, literal TC): `Jan 2026`, teks Last Updated NB-SL yang disalin, `Inactive`, `Active`; Filter Panel Active = `Inactive`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Overlay Column Visibility; menyalin teks sel; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: Search, Filter, dan konfigurasi kolom (Last Updated ditampilkan lalu disembunyikan kembali oleh langkah di spec). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Guard kolom non-searchable: Effective From dan Last Updated (TC-FA-TDC-496)

1. Klik header Actions `⋯`
2. Centang kolom Last Updated
3. Tutup Overlay Column Visibility
4. Salin teks Last Updated baris NB-SL dari selnya
5. Ketik Search `Jan 2026`, tekan Enter
6. Verifikasi (Effective From) tabel menampilkan `No results found` walau NB-1 dan NB-4 bernilai `Jan 2026`
7. Ganti isi kotak search dengan teks Last Updated NB-SL yang disalin, tekan Enter
8. Verifikasi (Last Updated) tabel menampilkan `No results found`
9. Klik `(←)` pada kotak Search
10. Klik header Actions `⋯`
11. Hapus centang kolom Last Updated
12. Tutup Overlay Column Visibility

### Kolom Active tidak dicari (TC-FA-TDC-497)

13. Ketik Search `Inactive`, tekan Enter
14. Verifikasi tabel menampilkan `No results found` (NB-OLD tidak tersaring menurut status)
15. Ganti isi kotak search dengan `Active`, tekan Enter
16. Verifikasi tabel menampilkan `No results found` (8 class Active tidak tersaring menurut status)
17. Klik `(←)` pada kotak Search
18. Klik icon Filter
19. Pilih Active `Inactive` pada Filter Panel
20. Klik `[Apply]`
21. Verifikasi tabel hanya menampilkan baris NB-OLD lewat Filter Panel
22. Klik `Clear all` pada chip filter

## Notes

- Langkah penghubung (S-03): langkah 1 sampai 3 (menampilkan kolom Last Updated yang Hidden agar teksnya dapat disalin), langkah 9 dan 17 (menutup kotak Search dan mereset tabel; S-09), langkah 10 sampai 12 (pemulihan Setup Column agar Last Updated kembali Hidden; 8b.14, R-24), langkah 22 (melepas Filter sebelum akhir spec). Hook `after` hanya cadangan.
- Asersi `No results found` pada langkah 6, 8, 14, dan 16 adalah Empty State hasil Search yang diproses sehingga menjadi anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-496 Expected b menyebut teks Last Updated tanpa nilainya; spec menyalin teks dari sel NB-SL sesuai Data Uji TC.
  - TC-FA-TDC-496 langkah tidak menyebut cara menampilkan kolom Last Updated (Hidden default); spec menambah langkah penghubung lewat Overlay Column Visibility.
  - TC-FA-TDC-497 langkah 3 memakai Filter Panel tanpa menyebut Search dikosongkan lebih dulu; spec mengosongkannya (langkah 17) agar irisan Search tidak memengaruhi hasil Filter.
  - Email akun Total Control tidak tertulis di TC.
