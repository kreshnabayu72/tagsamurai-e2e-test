---
id: TC-AC-DC-E2E-010-filter-category-tri-state-dasar
title: "Filter Category Tri-State Dasar: Partial-Check Parent, Centang dan Hapus Centang Hardware, Hardware Partial-Check Dipilih Penuh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-25
  - TC-AC-DC-29
  - TC-AC-DC-290
  - TC-AC-DC-291
coverage:
  web: automated
---

# Filter Category Tri-State Dasar: Partial-Check Parent, Centang dan Hapus Centang Hardware, Hardware Partial-Check Dipilih Penuh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) dan #15 (Device Name: `HR-100`, `TS-200`, `TS-210`, `FN-1`, `FN-2`, `FN-3`, `RB-01` sampai `RB-12`; 18 Device Name pada descendant `Hardware`) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Device Name `IND-1` (Pre-setup Dinamis #6) tidak ada saat spec ini berjalan. Total 18 baris untuk filter `Hardware` dan 17 baris tanpa `FN-1` diturunkan dari data Pre-setup #15 dan dibaca dari footer pagination.
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pilihan filter Category (tersimpan per user); dikosongkan lewat `All Categories` setelah tiap TC dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-25: Parent partial-check bila hanya sebagian descendant terpilih

1. Catat total baris tabel Device Name pada footer pagination (tanpa filter Category)
2. Expand `Hardware`, `Handheld Reader`, `Filter Induk`, dan `Filter Anak 2`
3. Klik node `Filter Anak 1`
4. Verifikasi `Filter Induk` partial-check
5. Verifikasi tabel Device Name menampilkan `FN-1`
6. Klik node `Filter Cucu`
7. Verifikasi tabel menampilkan `FN-1` dan `FN-2` (gabungan pilihan)
8. Verifikasi `Filter Induk` tetap partial-check karena `Filter Anak 3` belum terpilih
9. Verifikasi `Handheld Reader` dan `Hardware` partial-check
10. Verifikasi `Filter Anak 2` berstatus tercentang penuh karena satu-satunya descendant-nya (`Filter Cucu`) terpilih
11. Klik baris `All Categories`

### TC-AC-DC-29: Mencentang kotak Hardware memilih seluruh descendant dan menyaring tabel; Hardware bukan nilai filter

12. Centang kotak `Hardware`
13. Expand `Smart Fixed Reader`, `Rantai L3`, `Rantai L4`, `Rantai L5`, dan `Rantai L6`
14. Verifikasi kotak `Hardware` dan seluruh descendant-nya (`BLE Gateway`, `Handheld Reader` beserta anak-anaknya, `Smart Fixed Reader` beserta rantainya) tercentang
15. Verifikasi tabel menampilkan gabungan Device Name seluruh descendant `Hardware` tanpa Device Name lain (total 18 baris pada footer pagination)
16. Expand `TAG`
17. Verifikasi kotak `TAG` dan descendant `TAG` (`BLE`, `GPS`, `NFC`, `RFID`) tidak berubah (tidak tercentang dan tidak partial-check)
18. Klik baris `All Categories`

### TC-AC-DC-290: Hapus centang sebagian descendant setelah mencentang kotak Hardware membuat Hardware partial-check

19. Centang kotak `Hardware`
20. Verifikasi kotak `Hardware` dan seluruh descendant yang terlihat tercentang
21. Hapus centang `Filter Anak 1`
22. Verifikasi `Filter Anak 1` tidak tercentang
23. Verifikasi `Filter Induk`, `Handheld Reader`, dan `Hardware` berstatus partial-check
24. Verifikasi tabel menampilkan seluruh Device Name descendant `Hardware` kecuali `FN-1` (total 17 baris pada footer pagination)
25. Verifikasi kotak `TAG` tidak berubah
26. Klik baris `All Categories`

### TC-AC-DC-291: Menghapus centang kotak Hardware melepas seluruh pilihan descendant

27. Centang kotak `Hardware`
28. Hapus centang kotak `Hardware`
29. Verifikasi seluruh descendant `Hardware` tidak tercentang dan tidak ada node berstatus partial-check
30. Verifikasi tabel Device Name kembali menampilkan seluruh data (total baris sama dengan catatan langkah 1)

## Notes

- Langkah penghubung (S-03): langkah 1 mencatat baseline untuk asersi "seluruh data" (langkah 30); klik `All Categories` (langkah 11, 18, 26) melepas pilihan sebelum TC berikutnya (S-09); langkah 13 dan 16 meng-expand cabang `Smart Fixed Reader` dan `TAG` supaya seluruh descendant yang diasersi terlihat (S-14).
- Temuan untuk QA: (1) Ukuran halaman default tabel Device Name tidak ditulis TC; total 18 dan 17 baris diasersi lewat footer pagination. (2) TC-AC-DC-290 Expected a menyebut "seluruh descendant tercentang"; hanya node yang terlihat (setelah expand pada langkah 2 dan 13) yang diamati.
