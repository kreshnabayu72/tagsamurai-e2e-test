---
id: TC-FA-FAAC-E2E-191-resilience-submit-draft-asset-name-dan-use-recommended-classes
title: "Resilience: Submit dengan Draft Asset Name dan Create Use Recommended Classes Gagal karena Error Server 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-262
  - TC-FA-FAAC-292
coverage:
  web: automated
---

# Resilience: Submit dengan Draft Asset Name dan Create Use Recommended Classes Gagal karena Error Server 5xx

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata)
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Kemampuan teknis: `Spectra.intercept` parsial yang memaksa respons HTTP 5xx pada permintaan Create (dari Halaman Detail mode Create dan dari dialog Use Recommended Classes) di atas backend nyata; intercept dilepas segera sesudah pemicu (S-09). Endpoint permintaan tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga dipilih tim FE saat script. Pembacaan jumlah Asset Class lewat kemampuan baca BE (disediakan tim FE/BE).
- State global yang diubah spec: client dikosongkan dari Asset Class untuk TC-292 (tabel Asset Class kosong, Tax Depreciation Class rekomendasi Active). TC menyebut kondisi ini sebagai "client tanpa Asset Class (seed Pre-setup)" tanpa akun; pengosongan dan pemulihannya lewat fixture BE "disediakan tim FE/BE" (tanpa endpoint karangan). Hook `after` memulihkan sembilan Asset Class contoh Pre-setup dan data TC-262 lewat fixture BE.
- Data seed TC-262 (kode dan nama literal TC, disediakan fixture BE, dibaca, tidak diubah karena submit gagal): Asset Name tanpa Asset Class `Forklift 3T` (6 aset aktif), `Laptop Standard` (120 aset aktif), `Pallet Jack Electric` (0 aset aktif); Asset Name `Delivery Van` ter-assign ke `Vehicles`.
- Data Uji TC-262: Class Code `TRUCK-EQ`; Class Name `Truck Equipment`; Method `Straight Line`; Useful Life `96`; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`. Kode `TRUCK-EQ` tidak pernah tersimpan; hook `after` menghapusnya lewat fixture BE bila ternyata tersimpan.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-262: Submit dengan draft gagal karena error server mempertahankan draft

1. Klik tombol `+ Asset Class`
2. Isi field wajib tab General dan Depreciation sesuai Data Uji TC-262
3. Klik tab `Asset Names`
4. Klik tombol `+ Assign Asset Names`
5. Centang `Forklift 3T` dan `Laptop Standard`
6. Klik `[Assign]`
7. Pasang intercept respons 5xx pada permintaan Create
8. Klik `[Submit]`
9. Lepas intercept respons 5xx
10. Verifikasi toast error `Error, failed to create asset class.`
11. Verifikasi halaman tetap terbuka dalam mode Add Asset Class
12. Verifikasi input tab General dan Depreciation dipertahankan
13. Klik tab `Asset Names`
14. Verifikasi daftar draft `Forklift 3T` dan `Laptop Standard` dipertahankan
15. Klik breadcrumb `Asset Class`
16. Verifikasi dialog `Unsaved Changes` tampil
17. Klik `[Leave]`

### TC-FA-FAAC-292: Create rekomendasi gagal 5xx

18. Atur lewat fixture BE client menjadi tanpa Asset Class (tabel Asset Class kosong) dengan Tax Depreciation Class rekomendasi Active, lalu muat ulang halaman
19. Klik link `Use recommended classes` pada EmptyState tabel
20. Centang `BLDG`
21. Pasang intercept respons 5xx pada permintaan Create rekomendasi
22. Klik `Create`
23. Lepas intercept respons 5xx
24. Verifikasi toast error `Error, failed to create asset class.`
25. Verifikasi dialog tetap terbuka dan pilihan `BLDG` dipertahankan
26. Verifikasi tidak ada Asset Class dibuat: jumlah Asset Class tetap 0
27. Klik `[×]` pada dialog
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`
30. Pulihkan lewat fixture BE sembilan Asset Class contoh Pre-setup, lalu muat ulang halaman

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan Verifikasi TC-262 mengikuti urutan state: toast (state sementara) lebih dulu, lalu halaman, input, dan daftar draft sesudah klik tab `Asset Names` (8b butir 5); TC menulis "Klik tab Asset Names" sebagai langkah terakhir sebelum observasi.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 15 sampai 17 (menutup form Create yang dirty lewat breadcrumb, S-08; `Verifikasi` dialog `Unsaved Changes` diwajibkan S-08); langkah 18 dan 30 (mengosongkan dan memulihkan data client); langkah 27 sampai 29 (menutup dialog Use Recommended Classes yang terisi, S-08). Intercept dilepas segera sesudah submit (langkah 9 dan 23; S-09).
3. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `TRUCK-EQ`, `BLDG`, dan nama Asset Name literal; nilai dipakai apa adanya tanpa suffix `{runId}`. Semua submit gagal sehingga data tidak berubah.
4. Temuan untuk QA: TC-262 tidak menyebut tombol penutup dialog sesudah gagal dan keadaan tab General; spec menutup lewat breadcrumb dan dialog `Unsaved Changes`. TC-292 mensyaratkan tabel kosong pada client yang sama dengan sembilan Asset Class contoh TC lain (TC-1 sampai 13); spec memakai pengosongan lewat fixture BE yang disediakan tim FE/BE. TC-292 tidak menyebut tombol penutup dialog sesudah gagal dan nilai baseline jumlah Asset Class; spec memakai nol karena tabel kosong, dan menutup dialog lewat `[×]` dengan dialog `Unsaved Changes` (PRD §4.2f).
