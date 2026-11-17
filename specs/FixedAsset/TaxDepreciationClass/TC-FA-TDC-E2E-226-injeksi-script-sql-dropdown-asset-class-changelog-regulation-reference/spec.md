---
id: TC-FA-TDC-E2E-226-injeksi-script-sql-dropdown-asset-class-changelog-regulation-reference
title: "Injeksi Script dan SQL: Dropdown Asset Class, Changelog, dan Regulation Reference Tampil sebagai Teks"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-870
  - TC-FA-TDC-871
  - TC-FA-TDC-872
  - TC-FA-TDC-873
sourceRules: ["§4.1.1#r42", "§4.1.1#r11", "FLD-01", "§4.1.1#r3", "§4.1.1#p5"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r42": [13, 14]
  "§4.1.1#r11": 21
  "FLD-01": 25
  "§4.1.1#r3": 31
  "§4.1.1#p5": 33
anchor: [7, 8, 15, 26, 27, 35]
coverage:
  web: automated
---

# Injeksi Script dan SQL: Dropdown Asset Class, Changelog, dan Regulation Reference Tampil sebagai Teks

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk mengubah Class Name dan Regulation Reference class hingga tersimpan, seed dan pemulihan lewat API, flag Guided Tooltip disetel true oleh hook suite, dan hook `beforeEach` mengonfirmasi `beforeunload`. Pengamatan dialog JavaScript (alert) oleh test runner. Pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- Kemampuan tambahan (disediakan tim FE/BE): membaca jumlah entri Changelog per class dan field sebagai baseline. Changelog adalah audit trail permanen, sehingga jumlah entri tidak diasersi sebagai angka absolut (S-12).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name awal `Kelompok 4`, Useful Life 20, Active, Used By 0; Regulation Reference awal nilai seed |

- Nilai uji yang diset spec pada `NB-4`: Class Name `<script>alert(1)</script>` (langkah 2), Regulation Reference `<img src=x onerror=alert(1)>` (langkah 17), lalu Class Name `'; DROP TABLE classes;--` (langkah 29). Tabel berisi tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tampil tanpa Search kecuali pada TC-FA-TDC-873.
- Kolom Regulation Reference tersembunyi secara bawaan dan ditampilkan lewat Setup Column pada langkah 19 dan 20, lalu dikembalikan pada langkah 22 dan 23.
- Pemulihan: hook `after` mengembalikan Class Name dan Regulation Reference `NB-4` ke nilai seed lewat API dan menghapus preferensi kolom di browser.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat baseline jumlah entri Changelog Class Name class `NB-4` lewat kemampuan baca log
2. Ubah Class Name `NB-4` dari `Kelompok 4` menjadi `<script>alert(1)</script>` dengan sesi API aktor Total Control, hingga perubahan tersimpan
3. Muat ulang halaman

### TC-FA-TDC-870: Class Name berisi script ditampilkan sebagai teks pada dropdown Asset Class

4. Klik tab `Asset Class`
5. Klik `+ Asset Class`
6. Klik dropdown Tax Depreciation Class
7. Verifikasi opsi dropdown menampilkan teks `<script>alert(1)</script> — 20 yrs` apa adanya
8. Verifikasi tidak ada dialog alert JavaScript yang muncul
9. Tekan Esc untuk menutup dropdown, lalu tutup form Add Asset Class tanpa mengubah field
10. Klik tab `Tax Depreciation Class`

### TC-FA-TDC-871: Class Name berisi script ditampilkan sebagai teks pada Changelog

11. Klik ikon Changelog di toolbar
12. Ketik Search `NB-4`, tekan Enter
13. Verifikasi jumlah entri Class Name `NB-4` bertambah satu dari baseline langkah 1
14. Verifikasi kolom New Value baris Class Name `NB-4` teratas menampilkan teks `<script>alert(1)</script>` apa adanya
15. Verifikasi tidak ada dialog alert JavaScript yang muncul
16. Tutup Changelog

### TC-FA-TDC-872: Regulation Reference berisi markup ditampilkan sebagai teks

17. Ubah Regulation Reference `NB-4` menjadi `<img src=x onerror=alert(1)>` dengan sesi API aktor Total Control, hingga perubahan tersimpan
18. Muat ulang halaman
19. Klik header Actions `⋯`
20. Centang kolom Regulation Reference
21. Verifikasi kolom Regulation Reference baris `NB-4` menampilkan teks `<img src=x onerror=alert(1)>` apa adanya
22. Hapus centang kolom Regulation Reference
23. Tutup Overlay Column Visibility
24. Klik link Class Code `NB-4`
25. Verifikasi field Regulation Reference menampilkan teks `<img src=x onerror=alert(1)>` apa adanya
26. Verifikasi tidak ada dialog alert JavaScript yang muncul
27. Verifikasi tidak ada gambar yang dirender
28. Klik `[×]` pada header Drawer Edit

### TC-FA-TDC-873: Class Name berisi pernyataan SQL tersimpan dan tampil sebagai teks tanpa efek samping

29. Ubah Class Name `NB-4` menjadi `'; DROP TABLE classes;--` dengan sesi API aktor Total Control, hingga perubahan tersimpan
30. Muat ulang halaman
31. Verifikasi kolom Class Name baris `NB-4` menampilkan teks `'; DROP TABLE classes;--` apa adanya
32. Ketik Search `DROP`, tekan Enter
33. Verifikasi hasil pencarian menampilkan baris `NB-4`
34. Klik `(←)` pada kotak Search
35. Verifikasi tabel tetap memuat class lain: `NB-1`, `NB-2`, `NB-3`, `BLD-P`, `BLD-NP`, dan `LAND`

## Notes

- Spec ini tidak mengubah state global selain Setup Column (dipulihkan langkah 22 dan 23, 8b.14) dan data `NB-4` milik spec.
- Langkah penghubung (S-03): langkah 1 (baseline log, S-12); langkah 2, 17, dan 29 (menyiapkan nilai uji lewat sesi API aktor; TC menyebut "disiapkan lewat API pre-setup"); langkah 3, 18, dan 30 (memuat ulang halaman); langkah 9 dan 10 (menutup dropdown dan form Add Asset Class yang field-nya tidak diubah, sehingga tanpa dialog `Unsaved Changes`, lalu kembali ke modul asal, S-14); langkah 16 (menutup Changelog); langkah 22 dan 23 (pemulihan Setup Column: hapus centang dan tutup overlay, mengikuti pola TC Setup Column tanpa `[Save]`); langkah 28 (menutup Drawer Edit yang field-nya tidak diubah); langkah 34 (mengosongkan Search, S-09).
- Asersi absence dialog alert JavaScript (langkah 8, 15, dan 26) selalu didahului `Verifikasi` teks script tampil pada surface yang sama (langkah 7, 14, dan 25) sebagai anchor positif (8b.2). Langkah 27 didahului langkah 25 pada Drawer yang sama.
- Langkah 13 membaca entri baru lewat selisih dari baseline langkah 1 (S-12); entri teratas dibaca setelah selisih terbukti (S-14).
- Temuan untuk QA:
  - TC-FA-TDC-871 mensyaratkan Class Name diubah lewat Drawer Edit; spec menyiapkan perubahan itu lewat sesi API aktor (langkah 2) agar entri Changelog Class Name terbentuk oleh aksi spec.
  - TC-FA-TDC-870 tidak menyebut cara menutup dropdown dan form Add Asset Class sesudah verifikasi; spec menutupnya tanpa memilih opsi.
  - TC-FA-TDC-872 tidak menyebut `[Save]` pada Overlay Column Visibility; spec mengikuti pola TC Setup Column lain.
  - TC-FA-TDC-873 Expected c menulis "seluruh class lain" tanpa daftar; spec mengasersi enam class seed lain pada tabel.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
