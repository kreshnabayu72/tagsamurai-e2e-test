---
id: TC-AC-DC-E2E-009-filter-category-persistensi-dan-all-categories
title: "Filter Category: All Categories Melepas Pilihan, Pilihan Dipertahankan antar Sub-tab, dan Device SKU Difilter lewat Device Name Induk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-285
  - TC-AC-DC-30
  - TC-AC-DC-31
coverage:
  web: automated
---

# Filter Category: All Categories Melepas Pilihan, Pilihan Dipertahankan antar Sub-tab, dan Device SKU Difilter lewat Device Name Induk

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori), #15 (Device Name `FN-1`, `FN-2`, `FN-3`), dan #16 (Device SKU `SKU-FN-1`, `SKU-FN-2`, `SKU-FN-3`) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pilihan filter Category (tersimpan per user) dan teks pencarian tree; keduanya dikosongkan di akhir tiap TC dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-285: Klik All Categories melepas seluruh pilihan filter Category

1. Catat total baris tabel Device Name pada footer pagination (tanpa filter Category)
2. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk`
3. Klik node `Filter Anak 1`
4. Klik baris `All Categories`
5. Verifikasi tabel Device Name menampilkan seluruh Device Name (total baris sama dengan catatan langkah 1)
6. Verifikasi tidak ada node berstatus tercentang atau partial-check
7. Verifikasi baris `All Categories` tampil tanpa kotak centang

### TC-AC-DC-30: Pilihan filter Category tetap tersimpan saat berpindah antara Device Name dan Device SKU

8. Centang kotak `Filter Anak 2`
9. Pindah ke sub-tab `Device SKU`
10. Ketik Search `Filter Anak 2` pada kolom pencarian tree, tekan Enter
11. Verifikasi node `Filter Anak 2` masih tercentang di Device SKU
12. Verifikasi tabel Device SKU hanya menampilkan `SKU-FN-2` (SKU memakai Device Name induk)
13. Klik `[×]` pada kotak pencarian tree, tekan Enter
14. Pindah kembali ke sub-tab `Device Name`
15. Ketik Search `Filter Anak 2` pada kolom pencarian tree, tekan Enter
16. Verifikasi node `Filter Anak 2` masih tercentang
17. Verifikasi tabel Device Name menampilkan `FN-2`
18. Klik `[×]` pada kotak pencarian tree, tekan Enter
19. Klik baris `All Categories`

### TC-AC-DC-31: Device SKU difilter melalui Device Name induk dengan pilihan recursive

20. Pindah ke sub-tab `Device SKU`
21. Ketik Search `Filter Induk` pada kolom pencarian tree, tekan Enter
22. Centang kotak `Filter Induk`
23. Verifikasi tabel Device SKU menampilkan `SKU-FN-1`, `SKU-FN-2`, dan `SKU-FN-3` saja (SKU dari Device Name `FN-1`, `FN-2`, `FN-3`)
24. Klik `[×]` pada kotak pencarian tree, tekan Enter
25. Klik baris `All Categories`
26. Pindah kembali ke sub-tab `Device Name`

## Notes

- Langkah penghubung (S-03): langkah 10, 15, dan 21 memakai Search untuk menampilkan node target karena state expand tree setelah berpindah sub-tab tidak dinyatakan TC (R-16); langkah 13, 18, 24 mengosongkan Search; langkah 4, 19, dan 25 melepas pilihan filter (S-09); langkah 1 mencatat baseline; langkah 26 mengembalikan sub-tab Device Name.
- TC-AC-DC-36 (pilihan filter setelah refresh atau Back) ada di spec 090.
- Temuan untuk QA: (1) TC-AC-DC-31 precondition berada di Device SKU, sedangkan hook `beforeEach` membuka Device Name; langkah 20 berpindah sub-tab. (2) Asersi Device SKU memakai Device Name induk literal Pre-setup #16 (`SKU-FN-*`) dan hanya dibaca.
