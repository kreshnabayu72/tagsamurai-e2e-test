---
id: TC-FA-FAAC-E2E-006-use-recommended-classes-create-berhasil
title: "Use Recommended Classes: Create Berhasil Satu Baris dengan Perubahan, Baris LAND Tanpa Asset Name, dan Delapan Baris Sekaligus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-284
  - TC-FA-FAAC-644
  - TC-FA-FAAC-283
coverage:
  web: automated
---

# Use Recommended Classes: Create Berhasil Satu Baris dengan Perubahan, Baris LAND Tanpa Asset Name, dan Delapan Baris Sekaligus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state client): client belum memiliki Asset Class (tabel kosong, EmptyState tampil), Tax Depreciation Class rekomendasi Active, dan tersedia Asset Name tanpa Asset Class (untuk TC-FA-FAAC-644), disiapkan di hook `before` lewat fixture BE. Hook `after` menghapus Asset Class yang dibuat spec ini dan memulihkan state client ke nilai awal. Seed disediakan tim FE/BE (lihat `suite.md`).
- Data masukan TC-FA-FAAC-284: Class Code `HEQ-1`, Class Name `Heavy Equipment Custom`.
- Kemampuan teknis: fixture BE untuk menghapus Asset Class yang dibuat spec dan untuk membaca nilai tersimpan Asset Class (Depreciation Start Convention, Tax Depreciation Start Rule, Residual Value dan unit); disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`); spec ini membuat Asset Class dengan kode rekomendasi (nama literal dari dialog) dan menghapusnya antar blok serta di hook `after`.

## Test Steps

### TC-FA-FAAC-284: Create satu Asset Class rekomendasi dengan Class Code dan Class Name yang diubah

1. Klik link `Use recommended classes` pada EmptyState tabel
2. Centang baris HEAVY-EQ
3. Ubah Class Code baris HEAVY-EQ menjadi `HEQ-1`
4. Ubah Class Name baris HEAVY-EQ menjadi `Heavy Equipment Custom`
5. Klik `Create`
6. Verifikasi toast sukses `Success, asset class has been created.`
7. Verifikasi tabel hanya memuat satu Asset Class `HEQ-1` dengan Class Name `Heavy Equipment Custom`
8. Verifikasi nilai Commercial dan Fiscal Asset Class `HEQ-1` sama dengan nilai rekomendasi baris HEAVY-EQ (`Straight Line · 10 yrs`; `Bukan bangunan – Kelompok 3`, `Declining Balance`)
9. Hapus Asset Class yang dibuat spec ini lewat fixture BE hingga tabel kosong, lalu muat ulang halaman

### TC-FA-FAAC-644: Use Recommended Classes membuat Asset Class tanpa Asset Name

10. Catat jumlah Asset Name tanpa Asset Class pada banner di atas tabel sebagai baseline
11. Klik link `Use recommended classes` pada EmptyState
12. Centang baris LAND
13. Klik `[Create]`
14. Verifikasi toast sukses `Success, asset class has been created.`
15. Verifikasi baris Class Code `LAND` tampil di tabel
16. Klik link Class Code `LAND`
17. Klik tab Asset Names
18. Verifikasi tab Asset Names tidak memuat Asset Name
19. Klik breadcrumb `Asset Class`
20. Verifikasi jumlah Asset Name tanpa Asset Class pada banner sama dengan baseline
21. Hapus Asset Class `LAND` lewat fixture BE hingga tabel kosong, lalu muat ulang halaman

### TC-FA-FAAC-283: Create delapan Asset Class rekomendasi sekaligus

22. Klik link `Use recommended classes` pada EmptyState tabel
23. Centang kedelapan baris (BLDG, HEAVY-EQ, MACH, VEH, LT-VEH, IT-EQ, OFC-EQ, LAND)
24. Klik `Create`
25. Verifikasi toast sukses `Success, asset class has been created.`
26. Verifikasi tabel memuat delapan Asset Class dengan Class Code BLDG, HEAVY-EQ, MACH, VEH, LT-VEH, IT-EQ, OFC-EQ, LAND
27. Verifikasi kedelapan Asset Class berstatus Active
28. Verifikasi kolom Accounts kedelapan Asset Class menampilkan ikon merah (akun kosong)
29. Verifikasi kolom Asset Names kedelapan Asset Class bernilai 0
30. Verifikasi Fiscal Asset Class LAND menampilkan `Tanah` tanpa Tax Method
31. Verifikasi kolom Capitalization Threshold kedelapan Asset Class bernilai `Default`
32. Verifikasi Depreciation Start Convention kedelapan Asset Class bernilai `Full month from in-service date` lewat kemampuan baca BE
33. Verifikasi Tax Depreciation Start Rule kedelapan Asset Class bernilai `Month of expenditure` lewat kemampuan baca BE
34. Verifikasi Residual Value kedelapan Asset Class kosong dengan unit `Percent` lewat kemampuan baca BE

## Notes

- Langkah penghubung (S-03): langkah 9 dan 21 (menghapus Asset Class yang dibuat blok sebelumnya lewat fixture BE agar tabel kosong kembali untuk blok berikutnya; muat ulang halaman menampilkan EmptyState; S-06, S-09), langkah 10 (baseline banner untuk TC-FA-FAAC-644), langkah 19 (kembali ke daftar lewat breadcrumb).
- Langkah 14 dan 15 membuktikan Expected TC-644 "Asset Class LAND dibuat" (toast sukses dan baris LAND di tabel) sebelum Detail LAND dibuka.
- Urutan TC dalam spec: 284, 644, 283. Blok yang membuat satu baris lebih dulu; blok delapan baris di akhir dan dibersihkan hook `after` (S-10).
- Nama literal Class Code rekomendasi (BLDG, HEAVY-EQ, MACH, VEH, LT-VEH, IT-EQ, OFC-EQ, LAND) berasal dari isi tetap dialog dan nama `HEQ-1`/`Heavy Equipment Custom` dari TC; tidak diberi suffix karena Class Code maksimum 15 karakter. Cleanup hanya menghapus yang dibuat spec ini, suite serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAC-283 butir c (Depreciation Start Convention, Tax Depreciation Start Rule, Residual Value) tidak punya langkah observasi di Detail; spec membacanya lewat kemampuan baca BE (langkah 32 sampai 34), tanpa endpoint karangan.
  - TC-FA-FAAC-284 langkah 2 menyebut mengubah Class Code dan Class Name sekaligus; spec menuliskannya dua langkah (langkah 3 dan 4).
  - TC-FA-FAAC-644 tidak menyebut cara membaca "hitungan banner"; spec memakai jumlah pada teks banner dan mencatat baseline sebelum Create (langkah 10).
