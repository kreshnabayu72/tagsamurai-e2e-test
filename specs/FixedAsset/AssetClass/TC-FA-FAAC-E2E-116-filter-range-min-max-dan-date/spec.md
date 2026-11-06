---
id: TC-FA-FAAC-E2E-116-filter-range-min-max-dan-date
title: "Filter Tabel Asset Class: Range Min dan Max Capitalization Threshold, Asset Names, Assets, dan Date Range Last Updated"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-366
  - TC-FA-FAAC-367
  - TC-FA-FAAC-368
coverage:
  web: automated
---

# Filter Tabel Asset Class: Range Min dan Max Capitalization Threshold, Asset Names, Assets, dan Date Range Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Nilai yang dipakai asersi: Capitalization Threshold HEAVY-EQ 5,000,000, IT-EQ 2,000,000, tujuh kelas lain bernilai Default (VEHICLES, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND, OFFICE-OLD); Asset Names HEAVY-EQ 12, IT-EQ 5, VEHICLES 3, MACHINERY dan OFFICE-NEW 2, LAND 1, BLDG, OFFICE-OLD, dan STORAGE 0; Assets HEAVY-EQ 40, IT-EQ 62, MACHINERY 7, VEHICLES 18, LAND 4, kelas lain 0; Last Updated (waktu entri Changelog terbaru): HEAVY-EQ = 28 Oct 2026 (14:30); STORAGE = 27 Oct 2026 (01:00); IT-EQ = 1 Oct 2026 (00:05); MACHINERY = 30 Sep 2026 (16:20); OFFICE-NEW = 23 Sep 2026 (10:40); OFFICE-OLD = 22 Sep 2026 (14:05); VEHICLES = 15 Sep 2026 (11:30); BLDG dan LAND = 5 Jan 2026 (belum ada entri Changelog: waktu dibuat). Seed disediakan tim FE/BE (lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-366: Filter Min dan Max pada Capitalization Threshold

1. Klik icon Filter untuk membuka Filter Panel
2. Isi Capitalization Threshold Min `3,000,000`, klik `[Apply]`
3. Verifikasi hanya baris HEAVY-EQ yang tampil: baris HEAVY-EQ tampil dan baris contoh lain (IT-EQ) tidak tampil
4. Verifikasi baris bernilai Default (VEHICLES, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND, OFFICE-OLD) tidak tampil karena filter hanya mencocokkan nominal eksplisit
5. Klik `[Clear Field]`, lalu `[Apply]`
6. Isi Capitalization Threshold Max `3,000,000`, klik `[Apply]`
7. Verifikasi hanya baris IT-EQ yang tampil: baris IT-EQ tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
8. Verifikasi baris bernilai Default (VEHICLES, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND, OFFICE-OLD) tidak tampil
9. Klik `[Clear Field]`, lalu `[Apply]`
10. Isi Capitalization Threshold Min `2,000,000` dan Max `5,000,000`, klik `[Apply]`
11. Verifikasi hanya baris HEAVY-EQ dan IT-EQ yang tampil: kedua baris tampil dan baris contoh lain (VEHICLES) tidak tampil
12. Verifikasi baris bernilai Default (VEHICLES, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND, OFFICE-OLD) tidak tampil
13. Klik `[Clear Field]`, lalu `[Apply]`

### TC-FA-FAAC-367: Filter Min dan Max pada Asset Names dan Assets

14. Isi Asset Names Min `3`, klik `[Apply]`
15. Verifikasi hanya baris HEAVY-EQ, IT-EQ, dan VEHICLES yang tampil: ketiga baris tampil dan baris contoh lain (BLDG) tidak tampil
16. Klik `[Clear Field]`, lalu `[Apply]`
17. Isi Asset Names Max `1`, klik `[Apply]`, lalu telusuri seluruh halaman hasil dari halaman 1 sampai halaman terakhir (Next)
18. Verifikasi hanya baris BLDG, LAND, OFFICE-OLD, dan STORAGE yang tampil: keempat baris tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
19. Klik `[Clear Field]`, lalu `[Apply]`
20. Isi Assets Min `40` dan Max `62`, klik `[Apply]`
21. Verifikasi hanya baris HEAVY-EQ dan IT-EQ yang tampil: kedua baris tampil dan baris contoh lain (BLDG) tidak tampil
22. Klik `[Clear Field]`, lalu `[Apply]`

### TC-FA-FAAC-368: Filter date range pada Last Updated

23. Pilih Last Updated dari 1 Sep 2026 sampai 30 Sep 2026, klik `[Apply]`
24. Verifikasi baris MACHINERY (30 Sep 2026 16:20, hari terakhir rentang), OFFICE-NEW, OFFICE-OLD, dan VEHICLES tampil
25. Verifikasi baris contoh lain tidak tampil, termasuk IT-EQ (1 Oct 2026 00:05, tepat sesudah rentang)
26. Klik `[Clear Field]`, lalu `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 5, 9, 13, 16, 19, 22 (melepas filter antar kasus, S-09; sesuai langkah TC-FA-FAAC-366 dan 367) dan langkah 26 (melepas filter di akhir spec, S-09; TC tidak menuliskannya tetapi spec memulihkan state tabel).
- Langkah 4, 8, dan 12 mengasersi klausa d TC-FA-FAAC-366 ("tidak tampil pada ketiga kasus") pada masing-masing kasus; baris pembanding yang tampil dibuktikan pada `Verifikasi` langkah 3, 7, dan 11 (8b butir 2).
- Populasi tabel melebihi 25 baris, sehingga hasil Filter dapat memuat baris seed lain yang nilainya masuk rentang; asersi hanya pada keanggotaan baris contoh. Hasil Asset Names Max `1` mencakup banyak seed bernilai 0 dan dapat melampaui satu halaman, sehingga langkah 17 menelusuri seluruh halaman (S-14). Rentang kasus lain (Capitalization Threshold, Asset Names Min `3`, Assets 40 sampai 62, Last Updated 1 Sep sampai 30 Sep 2026) hanya cocok dengan baris contoh dan sedikit seed bernilai eksplisit, sehingga hasilnya dibaca pada halaman 1 (seed dijaga tim FE/BE).
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan nilai persis, dan data hanya dibaca (S-06, S-12).
- TC-FA-FAAC-706 (Filter Min dan Max pada nominal berdesimal) ada di spec 133.
- Temuan untuk QA: tidak ada.
