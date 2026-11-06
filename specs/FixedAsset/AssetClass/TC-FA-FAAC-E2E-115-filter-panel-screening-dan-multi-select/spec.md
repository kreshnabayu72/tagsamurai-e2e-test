---
id: TC-FA-FAAC-E2E-115-filter-panel-screening-dan-multi-select
title: "Filter Tabel Asset Class: Screening Filter Panel, Opsi Dropdown, dan Filter Tunggal Multi-Select"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-363
  - TC-FA-FAAC-364
  - TC-FA-FAAC-365
coverage:
  web: automated
---

# Filter Tabel Asset Class: Screening Filter Panel, Opsi Dropdown, dan Filter Tunggal Multi-Select

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Nilai yang dipakai asersi: Commercial Method Straight Line, Declining Balance (IT-EQ), Units of Production (MACHINERY), Not Depreciated (LAND); Tax Depreciation Class `Tanah` (LAND); Accounts Has inactive account (IT-EQ); Modified By (aktor entri Changelog terbaru): HEAVY-EQ, VEHICLES, MACHINERY, dan OFFICE-NEW = Rina P; OFFICE-OLD = Budi S; IT-EQ, STORAGE, BLDG, dan LAND = System. Seed disediakan tim FE/BE (lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-363: Screening struktur Filter Panel tabel Asset Class

1. Klik icon Filter untuk membuka Filter Panel
2. Verifikasi Filter Panel memuat sembilan field berurutan: Active | Commercial Method | Tax Depreciation Class | Accounts | Capitalization Threshold | Asset Names | Assets | Modified By | Last Updated
3. Verifikasi Active, Commercial Method, Tax Depreciation Class, Accounts, dan Modified By berupa multi-select searchable dengan placeholder berturut-turut `All statuses`, `All methods`, `All tax depreciation classes`, `All accounts`, `All users`
4. Verifikasi Capitalization Threshold, Asset Names, dan Assets berupa dua input numerik dengan placeholder `Min` dan `Max`
5. Verifikasi Last Updated berupa date range dengan placeholder `Select date`
6. Verifikasi tidak ada field filter untuk Class Code maupun Class Name
7. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-FA-FAAC-364: Isi opsi dropdown Filter Panel hanya dari data tabel tanpa opsi kosong

8. Buka dropdown Active
9. Verifikasi opsi dropdown Active: Active, Inactive
10. Buka dropdown Commercial Method
11. Verifikasi opsi dropdown Commercial Method: Straight Line, Declining Balance, Units of Production, Not Depreciated
12. Buka dropdown Tax Depreciation Class
13. Verifikasi opsi dropdown Tax Depreciation Class: Bukan bangunan – Kelompok 1, Bukan bangunan – Kelompok 2, Bukan bangunan – Kelompok 3, Bangunan permanen, Tanah
14. Buka dropdown Accounts
15. Verifikasi opsi dropdown Accounts: Complete, Incomplete, Has inactive account
16. Buka dropdown Modified By
17. Verifikasi opsi dropdown Modified By memuat Rina P, Budi S, dan System (aktor seed lain boleh ada dan tidak diasersi)
18. Verifikasi tidak ada dropdown (Active, Commercial Method, Tax Depreciation Class, Accounts, Modified By) yang memuat opsi `None` atau opsi nilai kosong

### TC-FA-FAAC-365: Filter tunggal pada field multi-select

19. Pilih Active = Inactive, klik `[Apply]`
20. Verifikasi hanya baris OFFICE-OLD yang tampil: baris OFFICE-OLD tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
21. Klik `[Clear Field]`, lalu `[Apply]`
22. Pilih Commercial Method = Units of Production, klik `[Apply]`
23. Verifikasi hanya baris MACHINERY yang tampil: baris MACHINERY tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
24. Klik `[Clear Field]`, lalu `[Apply]`
25. Pilih Tax Depreciation Class = Tanah, klik `[Apply]`
26. Verifikasi hanya baris LAND yang tampil: baris LAND tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
27. Klik `[Clear Field]`, lalu `[Apply]`
28. Pilih Accounts = Has inactive account, klik `[Apply]`
29. Verifikasi hanya baris IT-EQ yang tampil: baris IT-EQ tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
30. Klik `[Clear Field]`, lalu `[Apply]`
31. Pilih Modified By = Budi S, klik `[Apply]`
32. Verifikasi hanya baris OFFICE-OLD yang tampil: baris OFFICE-OLD tampil dan baris contoh lain (HEAVY-EQ) tidak tampil
33. Klik `[Clear Field]`, lalu `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 21, 24, 27, 30 (melepas filter antar field, S-09; sesuai langkah TC-FA-FAAC-365) dan langkah 33 (melepas filter terakhir di akhir spec, S-09; TC tidak menuliskannya tetapi spec memulihkan state tabel).
- Opsi dropdown Modified By (langkah 17) diasersi sebagai keanggotaan tiga aktor contoh, bukan daftar lengkap, karena seed lain dibuat oleh aktor lain; hasil Filter diasersi pada keanggotaan baris contoh (baris contoh target tampil, baris contoh lain tidak tampil) dan baris seed lain yang cocok tidak diasersi.
- Dropdown yang masih terbuka ditutup sebelum dropdown berikutnya dibuka (langkah 8 sampai 16); cara menutupnya ditetapkan di tahap script.
- Klausa "baris contoh lain tidak tampil" diasersi bersama baris target pada satu `Verifikasi` dengan satu baris pembanding yang dijamin ada (8b butir 2).
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan nilai persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
