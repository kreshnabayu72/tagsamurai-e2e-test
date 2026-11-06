---
id: TC-FA-FAAC-E2E-112-search-class-code-class-name-commercial-fiscal-threshold
title: "Search Tabel Asset Class: Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Asset Names, dan Assets"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-351
  - TC-FA-FAAC-352
  - TC-FA-FAAC-353
  - TC-FA-FAAC-354
coverage:
  web: automated
---

# Search Tabel Asset Class: Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Asset Names, dan Assets

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment; Commercial Straight Line; Fiscal `Bukan bangunan – Kelompok 3 · Declining Balance`; Capitalization Threshold 5,000,000; Asset Names 12), VEHICLES, IT-EQ (Commercial `Declining Balance · 4 yrs · 50%/yr · 5%`; Capitalization Threshold 2,000,000; Assets 62), MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Fiscal `Tanah`) (Active) dan OFFICE-OLD (Inactive). Kolom lain bernilai beragam sehingga tiap kolom yang dicari punya sedikitnya dua nilai distinct (S-11). Seed disediakan tim FE/BE (lihat `suite.md`).
- Semua keyword Search diketik pada kotak Search tabel Asset Class; ukuran halaman bawaan 10. Baris contoh dikenali lewat kata kunci yang dituju, bukan lewat posisi di halaman 1, karena tabel memuat seed lain (butir populasi tabel).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-351: Search pada kolom Class Code dan Class Name

1. Ketik Search `ffice-n`, tekan Enter
2. Verifikasi hanya baris OFFICE-NEW yang tampil: baris OFFICE-NEW tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
3. Ganti isi kotak search dengan `OFFICE-NEW`, tekan Enter
4. Verifikasi hanya baris OFFICE-NEW yang tampil: baris OFFICE-NEW tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
5. Klik `✕` pada Search, tekan Enter
6. Ketik Search `avy equ`, tekan Enter
7. Verifikasi hanya baris HEAVY-EQ (Heavy Equipment) yang tampil: baris HEAVY-EQ tampil dan baris contoh lain (OFFICE-NEW) tidak tampil
8. Ganti isi kotak search dengan `AVY EQU`, tekan Enter
9. Verifikasi hanya baris HEAVY-EQ (Heavy Equipment) yang tampil: baris HEAVY-EQ tampil dan baris contoh lain (OFFICE-NEW) tidak tampil
10. Klik `✕` pada Search, tekan Enter
11. Ketik Search `zzzzzz`, tekan Enter
12. Verifikasi empty state `No results found` tampil

### TC-FA-FAAC-352: Search pada kolom Commercial dan Fiscal

13. Klik `✕` pada Search, tekan Enter
14. Ketik Search `50%/yr`, tekan Enter
15. Verifikasi hanya baris IT-EQ (`Declining Balance · 4 yrs · 50%/yr · 5%`) yang tampil: baris IT-EQ tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
16. Klik `✕` pada Search, tekan Enter
17. Ketik Search `kelompok 3`, tekan Enter
18. Verifikasi hanya baris HEAVY-EQ (`Bukan bangunan – Kelompok 3 · Declining Balance`) yang tampil: baris HEAVY-EQ tampil dan baris contoh lain (IT-EQ) tidak tampil
19. Klik `✕` pada Search, tekan Enter
20. Ketik Search `tanah`, tekan Enter
21. Verifikasi hanya baris LAND yang tampil: baris LAND tampil dan baris contoh lain (HEAVY-EQ) tidak tampil

### TC-FA-FAAC-353: Search pada kolom Capitalization Threshold

22. Klik `✕` pada Search, tekan Enter
23. Ketik Search `5,000,000`, tekan Enter
24. Verifikasi hanya baris HEAVY-EQ yang tampil (nominal tanpa simbol mata uang): baris HEAVY-EQ tampil dan baris contoh lain (IT-EQ) tidak tampil
25. Klik `✕` pada Search, tekan Enter
26. Ketik Search `default`, tekan Enter, lalu telusuri seluruh halaman hasil dari halaman 1 sampai halaman terakhir (Next)
27. Verifikasi tujuh baris bernilai Default tampil: BLDG, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES
28. Verifikasi baris HEAVY-EQ dan IT-EQ tidak tampil

### TC-FA-FAAC-354: Search pada kolom Asset Names dan Assets

29. Klik `✕` pada Search, tekan Enter
30. Ketik Search `12`, tekan Enter
31. Verifikasi hanya baris HEAVY-EQ (12 Asset Name) yang tampil: baris HEAVY-EQ tampil dan baris contoh lain (IT-EQ) tidak tampil
32. Klik `✕` pada Search, tekan Enter
33. Ketik Search `62`, tekan Enter
34. Verifikasi hanya baris IT-EQ (62 aset aktif) yang tampil: baris IT-EQ tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
35. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 5, 10, 13, 16, 19, 22, 25, 29, 32 (mengosongkan kotak Search antar kata kunci, S-09; 8b.9), langkah 26 (menelusuri seluruh halaman hasil Search `default`, yang mencakup seed lain bernilai Default dan dapat melampaui satu halaman, S-14), langkah 35 (menutup input Search dan mereset tabel di akhir spec, S-09; R-16).
- Klausa "hanya baris tersebut yang tampil di antara 9 data contoh" diasersi sebagai satu `Verifikasi` per kata kunci: baris target tampil dan satu baris contoh lain yang dijamin ada tidak tampil (8b butir 2, klausa "hanya X").
- Spec berlangkah 35, tepat pada batas sekitar 35 langkah; semua langkah satu topik (Search tabel) dan satu dataset Pre-setup, sehingga tidak dipecah.
- Nama literal Pre-setup (HEAVY-EQ, IT-EQ, OFFICE-NEW, LAND, dan sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan nilai persis, dan data hanya dibaca (S-06, S-12).
- Kata kunci numerik dan umum (`5,000,000`, `12`, `62`, `default`) dapat juga cocok dengan seed lain; asersi hanya pada keanggotaan baris contoh (baris target tampil, baris contoh lain tidak tampil).
- Temuan untuk QA: tidak ada.
