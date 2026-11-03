---
id: TC-AC-ACTS-E2E-172-detail-sku-tab-available-alur-search-filter
title: "Detail SKU Tab Available: Alur Search lalu Filter dan Filter lalu Search"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-401
  - TC-AC-ACTS-402
coverage:
  web: automated
---

# Detail SKU Tab Available: Alur Search lalu Filter dan Filter lalu Search

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif

### TC-AC-ACTS-401: Alur Search lalu Filter

2. Ketik Search `tag-4f`, tekan Enter
3. Klik icon Filter
4. Pilih `Available` pada field `Status`
5. Klik `[Apply]`
6. Verifikasi tabel memuat sedikitnya satu baris data
7. Verifikasi seluruh baris yang tampil cocok dengan keyword `tag-4f` dan berstatus `Available` (irisan Search dan Filter)
8. Verifikasi kotak Search masih berisi `tag-4f` (menerapkan Filter tidak mengosongkan keyword Search)
9. Klik `[Clear Field]`
10. Klik `[Apply]`
11. Klik icon Filter untuk menutup panel
12. Klik `(←)` pada kotak Search

### TC-AC-ACTS-402: Alur Filter lalu Search

13. Klik icon Filter
14. Pilih `Available` pada field `Status`
15. Klik `[Apply]`
16. Klik icon Filter untuk menutup panel
17. Ketik Search `tag-4f`, tekan Enter
18. Verifikasi tabel memuat sedikitnya satu baris data
19. Verifikasi hasil tabel identik dengan hasil pada langkah 7
20. Klik icon Filter
21. Verifikasi field `Status` masih berisi `Available` (kriteria Filter tetap aktif setelah Search)
22. Klik icon Filter untuk menutup panel
23. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): `[Clear Field]`, `[Apply]`, menutup panel Filter, dan klik `(←)` pada kotak Search mereset state antar TC (S-09); menutup panel Filter sesudah `[Apply]` membuat langkah berikutnya deterministik. Hasil alur TC-AC-ACTS-402 dibandingkan dengan hasil TC-AC-ACTS-401 pada langkah 7.
- Temuan untuk QA: TC-AC-ACTS-402 butir b "Kriteria Filter tetap aktif setelah Search" tidak menyebut cara cek; spec membuka Filter Panel dan memeriksa field `Status`.
