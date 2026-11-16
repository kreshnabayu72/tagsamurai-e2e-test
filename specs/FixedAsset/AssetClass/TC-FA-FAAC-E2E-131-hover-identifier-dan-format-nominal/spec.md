---
id: TC-FA-FAAC-E2E-131-hover-identifier-dan-format-nominal
title: "Tabel Asset Class: Format Nominal Berdesimal pada Capitalization Threshold dan Commercial, serta Hover Primary Identifier"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-701
  - TC-FA-FAAC-704
  - TC-FA-FAAC-707
  - TC-FA-FAAC-716
sourceRules: ["§4.1.1#r4", "T-01"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r4": [2, 16, 17, 25]
  "T-01": [7, 13, 22]
anchor: [27, 29, 31, 33]
coverage:
  web: automated
---

# Tabel Asset Class: Format Nominal Berdesimal pada Capitalization Threshold dan Commercial, serta Hover Primary Identifier

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC, termasuk HEAVY-EQ (Active) yang memiliki Asset Name ter-assign `Excavator PC200` (TC-FA-FAAC-701); Tax Depreciation Class `Bukan bangunan – Kelompok 3` Active; Asset Class B-DISPRATE dengan Method Declining Balance, Useful Life 60, Declining Rate 25.5, dan Residual Value 33.3 unit Percent (TC-FA-FAAC-716). Seed disediakan tim FE/BE (lihat `suite.md`).
- Data milik spec (dibuat lewat UI oleh langkah 3 sampai 25; dihapus lewat API di hook `before` bila sisa run sebelumnya ada dan di hook `after`): Asset Class B-DEC (Class Name `Decimal Fixture`), B-DECZ (Class Name `Decimal Zero Fixture`), dan B-HALF (Class Name `Half Decimal Fixture`). Nilai field tiap kelas: Method Straight Line, Useful Life 60, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`; Residual Value unit Amount dan Capitalization Threshold: B-DEC 2500000.99 dan 1500.99; B-DECZ 2000000.00 dan 3000000.00; B-HALF 2500000.5 dan 1500.5. Pembersihan disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini menambah tiga Asset Class dan memulihkannya di hook `after`.

## Test Steps

### TC-FA-FAAC-716: Declining Rate dan Residual Value unit Percent berdesimal pada ringkasan Commercial

1. Ketik Search `B-DISPRATE`, tekan Enter
2. Verifikasi baris B-DISPRATE menampilkan Commercial `Declining Balance · 5 yrs · 25.5%/yr · 33.3%` (satu digit desimal ditulis apa adanya, bukan `25.50%/yr` dan bukan `33.30%`)

### TC-FA-FAAC-704: Nominal berdesimal bukan nol tampil dengan desimal, nominal tanpa bagian desimal bukan nol tampil tanpa desimal

3. Klik tombol `+ Asset Class` di toolbar tabel
4. Isi Class Code `B-DEC`, Class Name `Decimal Fixture`, Method Straight Line, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
5. Pilih unit Amount pada Residual Value dan isi `2500000.99`; isi Capitalization Threshold `1500.99`
6. Klik `Submit`
7. Verifikasi toast sukses `Success, asset class has been created.`
8. Klik breadcrumb `Asset Class` untuk kembali ke tabel
9. Klik tombol `+ Asset Class` di toolbar tabel
10. Isi Class Code `B-DECZ`, Class Name `Decimal Zero Fixture` dengan field lain sama seperti langkah 4
11. Pilih unit Amount pada Residual Value dan isi `2000000.00`; isi Capitalization Threshold `3000000.00`
12. Klik `Submit`
13. Verifikasi toast sukses `Success, asset class has been created.`
14. Klik breadcrumb `Asset Class` untuk kembali ke tabel
15. Ganti isi kotak search dengan `B-DEC`, tekan Enter
16. Verifikasi baris B-DEC: Capitalization Threshold `1,500.99` dan Commercial `Straight Line · 5 yrs · 2,500,000.99` (desimal bukan nol tetap tampil dengan 2 digit, tanpa simbol mata uang)
17. Verifikasi baris B-DECZ: Capitalization Threshold `3,000,000` dan Commercial `Straight Line · 5 yrs · 2,000,000` (bagian desimal nol tidak tampil)

### TC-FA-FAAC-707: Nominal ber-1 digit desimal ditulis dengan 2 digit desimal

18. Klik tombol `+ Asset Class` di toolbar tabel
19. Isi Class Code `B-HALF`, Class Name `Half Decimal Fixture`, Method Straight Line, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
20. Pilih unit Amount pada Residual Value dan isi `2500000.5`; isi Capitalization Threshold `1500.5`
21. Klik `Submit`
22. Verifikasi toast sukses `Success, asset class has been created.`
23. Klik breadcrumb `Asset Class` untuk kembali ke tabel
24. Ganti isi kotak search dengan `B-HALF`, tekan Enter
25. Verifikasi baris B-HALF: Capitalization Threshold `1,500.50` dan Commercial `Straight Line · 5 yrs · 2,500,000.50` (bagian desimal bukan nol ditulis dengan 2 digit, bukan `1,500.5` dan bukan `2,500,000.5`)

### TC-FA-FAAC-701: Hover primary identifier Class Code dan Asset Name berubah ke warna primary Fixed Asset tanpa underline

26. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
27. Verifikasi link Class Code baris HEAVY-EQ idle berwarna netral, sama dengan teks Class Name baris yang sama (bukan biru link browser)
28. Arahkan kursor ke link Class Code `HEAVY-EQ`
29. Verifikasi hover Class Code mengubah warna teks menjadi warna primary Fixed Asset (biru) tanpa garis bawah
30. Klik link Class Code `HEAVY-EQ`, lalu klik tab `Asset Names`
31. Verifikasi link Asset Name baris `Excavator PC200` idle berwarna netral, sama dengan teks tabel biasa
32. Arahkan kursor ke link Asset Name `Excavator PC200`
33. Verifikasi hover Asset Name mengubah warna teks menjadi warna primary Fixed Asset (biru) tanpa garis bawah

## Notes

- Spec berlangkah 33 (tidak melampaui batas sekitar 35 langkah).
- Langkah penghubung (S-03): langkah 1, 15, 24, dan 26 (Search untuk menemukan baris target; kotak Search mempertahankan nilainya setelah kembali lewat Breadcrumb sehingga langkah 15, 24, dan 26 memakai "ganti isi kotak search", 8b butir 9; R-16); langkah 8, 14, dan 23 (kembali ke tabel lewat breadcrumb, bagian TC).
- Urutan TC di dalam spec: TC-FA-FAAC-716 (baca), 704 dan 707 (membuat data), lalu 701 (membuka Detail, meninggalkan tabel) pada akhir (S-10).
- Aksi pembuatan di langkah 6, 12, dan 21 diikuti `Verifikasi` toast sukses sehingga tidak memerlukan langkah "Tunggu aksi selesai" (8b butir 8).
- Langkah 16, 17, dan 25 memakai `Verifikasi` satu baris tabel untuk nilai beberapa kolom yang disebut bersama dalam satu butir Expected TC (S-01).
- Nama literal Pre-setup (HEAVY-EQ, B-DISPRATE, dan sembilan kelas contoh) serta Class Code B-DEC, B-DECZ, dan B-HALF dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai tampil persis; kelas yang dibuat spec dibersihkan di hook `after`. Kode B-DEC dan B-DECZ yang sama diseed lewat API oleh spec 114 dan 133 (suite serial; tiap spec membersihkan kelas yang dibuatnya; S-06, S-12).
- Temuan untuk QA: tidak ada.
