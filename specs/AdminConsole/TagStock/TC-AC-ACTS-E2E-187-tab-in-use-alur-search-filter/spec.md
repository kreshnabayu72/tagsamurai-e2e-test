---
id: TC-AC-ACTS-E2E-187-tab-in-use-alur-search-filter
title: "Detail SKU Tab In Use: Alur Search lalu Filter dan Filter lalu Search"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-447
  - TC-AC-ACTS-448
coverage:
  web: automated
---

# Detail SKU Tab In Use: Alur Search lalu Filter dan Filter lalu Search

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

### TC-AC-ACTS-447: Alur Search lalu Filter

2. Ketik Search `maju`, tekan Enter
3. Klik icon Filter
4. Pilih `PT Maju Bersama` pada field `Client`
5. Klik `[Apply]`
6. Verifikasi tabel memuat sedikitnya satu baris data
7. Verifikasi seluruh baris yang tampil cocok dengan keyword `maju` dan bernilai Client `PT Maju Bersama` (irisan Search dan Filter)
8. Verifikasi kotak Search masih berisi `maju` (menerapkan Filter tidak mengosongkan keyword Search)
9. Klik `[Clear Field]`
10. Klik `[Apply]`
11. Klik icon Filter untuk menutup panel
12. Klik `(←)` pada kotak Search

### TC-AC-ACTS-448: Alur Filter lalu Search

13. Klik icon Filter
14. Pilih `PT Maju Bersama` pada field `Client`
15. Klik `[Apply]`
16. Klik icon Filter untuk menutup panel
17. Ketik Search `maju`, tekan Enter
18. Verifikasi tabel memuat sedikitnya satu baris data
19. Verifikasi hasil tabel identik dengan hasil pada langkah 7
20. Klik icon Filter
21. Verifikasi field `Client` masih berisi `PT Maju Bersama` (kriteria Filter tetap aktif setelah Search)
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Klik icon Filter untuk menutup panel
25. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): `[Clear Field]`, `[Apply]`, menutup panel Filter, dan klik `(←)` pada kotak Search mereset state antar TC (S-09). Hasil alur TC-AC-ACTS-448 dibandingkan dengan hasil TC-AC-ACTS-447 pada langkah 7.
- Temuan untuk QA: TC-AC-ACTS-448 butir b "Kriteria Filter tetap aktif setelah Search" tidak menyebut cara cek; spec membuka Filter Panel dan memeriksa field `Client`.
