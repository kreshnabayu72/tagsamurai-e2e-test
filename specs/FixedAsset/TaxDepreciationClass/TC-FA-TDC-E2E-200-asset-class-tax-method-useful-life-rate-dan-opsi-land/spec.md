---
id: TC-FA-TDC-E2E-200-asset-class-tax-method-useful-life-rate-dan-opsi-land
title: "Asset Class: Opsi Tax Method, Useful Life dan Rate, serta Opsi Class Land"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-733
  - TC-FA-TDC-734
  - TC-FA-TDC-735
  - TC-FA-TDC-736
  - TC-FA-TDC-737
  - TC-FA-TDC-738
  - TC-FA-TDC-739
coverage:
  web: automated
---

# Asset Class: Opsi Tax Method, Useful Life dan Rate, serta Opsi Class Land

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleData`, fixture belum ada): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL). Nilai yang diasersi: NB-4 (`Bukan bangunan – Kelompok 4`, Active, Allowed Methods `Straight Line` dan `Declining Balance`, versi Current Useful Life 20, Straight Line Rate 5%, Declining Balance Rate 10%); NB-SL (`Kelompok khusus Straight Line`, Active, hanya `Straight Line`, Useful Life 16); BLD-P (`Bangunan permanen`, Active, Building, hanya `Straight Line`, Useful Life 20); LAND (`Tanah`, Active); BLD-NP (`Bangunan tidak permanen`, Active, versi Current Useful Life 10 dan Straight Line Rate 10%, serta satu versi Scheduled mulai Jan 2027).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class dan versi lewat API; membuka Drawer Create Asset Class, memilih opsi dropdown, dan membaca opsi serta nilai field read-only. Spec tidak mengubah data Tax Depreciation Class dan tidak menyimpan Asset Class (Drawer ditutup dengan `[Leave]`), sehingga tidak ada state yang perlu dipulihkan.
- Tidak ada state global yang diubah.

## Test Steps

1. Klik tab Asset Class
2. Klik `+ Asset Class`

### TC-FA-TDC-733: Tax Method memuat Straight Line dan Declining Balance

3. Klik dropdown Tax Depreciation Class
4. Pilih `Bukan bangunan – Kelompok 4 — 20 yrs`
5. Klik dropdown Tax Method
6. Verifikasi dropdown Tax Method memuat opsi `Straight Line` dan `Declining Balance`
7. Tekan Esc untuk menutup dropdown Tax Method

### TC-FA-TDC-738: Useful Life dan rate mengikuti versi Current

8. Verifikasi field Useful Life & Rate tampil read-only
9. Verifikasi field Useful Life & Rate menampilkan Useful Life 20, Straight Line Rate 5%, dan Declining Balance Rate 10%

### TC-FA-TDC-734: Tax Method hanya Straight Line untuk Non-building yang hanya mengizinkan Straight Line

10. Klik dropdown Tax Depreciation Class
11. Pilih `Kelompok khusus Straight Line — 16 yrs`
12. Klik dropdown Tax Method
13. Verifikasi dropdown Tax Method memuat opsi `Straight Line`
14. Verifikasi opsi `Declining Balance` tidak tampil di dropdown Tax Method
15. Tekan Esc untuk menutup dropdown Tax Method

### TC-FA-TDC-735: Tax Method hanya Straight Line untuk Building

16. Klik dropdown Tax Depreciation Class
17. Pilih `Bangunan permanen — 20 yrs`
18. Klik dropdown Tax Method
19. Verifikasi dropdown Tax Method hanya memuat opsi `Straight Line`
20. Tekan Esc untuk menutup dropdown Tax Method

### TC-FA-TDC-736: Tax Method read-only dan tidak wajib untuk class Land

21. Klik dropdown Tax Depreciation Class
22. Pilih opsi class Land (`Tanah`)
23. Verifikasi field Tax Method tampil read-only dengan nilai `—`
24. Verifikasi field Tax Method tidak wajib diisi

### TC-FA-TDC-737: Opsi class Land ditulis tanpa bagian yrs

25. Klik dropdown Tax Depreciation Class
26. Verifikasi opsi untuk class Land tampil `Tanah` tanpa bagian `yrs`
27. Verifikasi opsi NB-4 tetap tampil `Bukan bangunan – Kelompok 4 — 20 yrs`

### TC-FA-TDC-739: Versi Scheduled belum memengaruhi Useful Life dan rate

28. Pilih `Bangunan tidak permanen — 10 yrs`
29. Verifikasi field Useful Life & Rate menampilkan nilai versi Current: Useful Life 10 dan Straight Line Rate 10%
30. Klik `[×]` pada header Drawer Create Asset Class
31. Verifikasi dialog `Unsaved Changes` tampil
32. Klik `[Leave]`

## Notes

- Urutan TC di spec: 733, 738, 734, 735, 736, 737, 739. Satu Drawer Create dibuka sekali (langkah 1 dan 2) dan class dipilih berurutan di dalamnya; langkah 1 dan 2 TC-738, 733 sampai 737, dan 739 ("Klik `+ Asset Class`", "Pilih Tax Depreciation Class") dipenuhi oleh langkah 2 dan pemilihan class pada tiap blok. TC-738 memakai pilihan NB-4 dari TC-733, sehingga mengikutinya langsung (S-10).
- Langkah penghubung (S-03): langkah 1 (berpindah ke tab Asset Class), langkah 7, 15, dan 20 (menutup dropdown Tax Method), langkah 30 sampai 32 (menutup Drawer dirty lewat `[×]` dan `[Leave]`, S-08).
- Asersi tambahan di luar Expected TC (S-03): langkah 14 memecah Expected TC-734 ("hanya `Straight Line`; `Declining Balance` tidak tampil") menjadi dua `Verifikasi` (S-01) dan langkah 13 menjadi anchor positif untuk langkah 14 (8b.2); langkah 8 dan 9 memecah Expected TC-738 (read-only dan nilai).
- Temuan untuk QA:
  - TC-736 "tidak wajib diisi" tidak menyebut cara membuktikannya; spec mengasersi field Tax Method tanpa penanda wajib diisi.
  - TC-739 tidak menyebut nilai Useful Life dan rate versi Scheduled BLD-NP; asersi "bukan nilai versi Scheduled" dicakup oleh nilai versi Current yang tepat (Useful Life 10, Straight Line Rate 10%).
  - TC-736 Expected menyebut Tax Method `—` tetapi tidak menyebut Declining Balance Rate untuk class Land; tidak diasersi.
  - TC-733 sampai 739 tidak menyebut field wajib Asset Class lain; Drawer tidak disimpan sehingga tidak diperlukan.
  - Email akun Total Control tidak tertulis di TC.
