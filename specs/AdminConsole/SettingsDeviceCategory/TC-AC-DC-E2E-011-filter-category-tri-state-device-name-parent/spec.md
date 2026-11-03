---
id: TC-AC-DC-E2E-011-filter-category-tri-state-device-name-parent
title: "Filter Category Tri-State: Hardware Partial-Check Dipilih Penuh, Parent Partial-Check dan Tercentang Penuh pada Device Name yang Merujuk Parent"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-292
  - TC-AC-DC-294
  - TC-AC-DC-295
  - TC-AC-DC-296
coverage:
  web: automated
---

# Filter Category Tri-State: Hardware Partial-Check Dipilih Penuh, Parent Partial-Check dan Tercentang Penuh pada Device Name yang Merujuk Parent

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) dan #15 (Device Name: `HR-100`, `TS-200`, `TS-210`, `FN-1`, `FN-2`, `FN-3`, `RB-01` sampai `RB-12`) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Data Dinamis milik spec (Pre-setup Dinamis #6): Device Name `IND-1-{runId}-011` dengan Category `Industrial Scanner` (node Pre-setup yang punya anak `Rugged` dan `Rugged Kit`). Dibuat lewat sesi API aktor (kemampuan disediakan tim BE/FE; nilai field wajib Device Name lain disediakan tim FE) pada langkah 20, dan dihapus lewat API oleh hook `after` tanpa mengasumsikan setup berhasil penuh. Device Name `IND-1` hanya ada pada TC-AC-DC-294 dan 295 (data dinamis #6).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pilihan filter Category (tersimpan per user); dikosongkan lewat `All Categories` setelah tiap TC dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-292: Mengklik kotak Hardware yang berstatus partial-check memilih seluruh descendant

1. Catat total baris tabel Device Name pada footer pagination (tanpa filter Category)
2. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk`
3. Centang kotak `Hardware`
4. Hapus centang `Filter Anak 1`
5. Klik kotak `Hardware` yang partial-check
6. Expand `Smart Fixed Reader`, `Rantai L3`, `Rantai L4`, `Rantai L5`, dan `Rantai L6`
7. Verifikasi kotak `Hardware` dan seluruh descendant-nya tercentang, termasuk `Filter Anak 1`
8. Verifikasi tabel menampilkan gabungan Device Name seluruh descendant `Hardware` termasuk `FN-1` (total 18 baris pada footer pagination, data Pre-setup #15)
9. Verifikasi kotak `TAG` tidak berubah
10. Klik baris `All Categories`

### TC-AC-DC-296: Mengklik kotak parent partial-check memilih seluruh descendant dan mengklik kotak tercentang melepasnya

11. Expand `Filter Anak 2`
12. Klik node `Filter Anak 1`
13. Verifikasi tabel Device Name hanya menampilkan `FN-1`
14. Klik kotak `Filter Induk` yang partial-check
15. Verifikasi `Filter Induk`, `Filter Anak 1`, `Filter Anak 2`, `Filter Cucu`, dan `Filter Anak 3` tercentang
16. Verifikasi tabel menampilkan `FN-1`, `FN-2`, dan `FN-3`
17. Klik kotak `Filter Induk` yang tercentang
18. Verifikasi seluruh node cabang `Filter Induk` tidak tercentang dan tidak ada partial-check
19. Verifikasi tabel menampilkan seluruh Device Name (total baris sama dengan catatan langkah 1)

### TC-AC-DC-294: Kotak parent partial-check tidak menampilkan Device Name yang merujuk parent itu sendiri

20. Buat Device Name `IND-1-{runId}-011` dengan Category `Industrial Scanner` lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman dengan F5
21. Expand `Hardware`, `Handheld Reader`, dan `Industrial Scanner`
22. Klik node `Rugged`
23. Verifikasi tabel hanya menampilkan `TS-200`
24. Verifikasi `IND-1-{runId}-011` dan `TS-210` tidak tampil
25. Verifikasi `Industrial Scanner` berstatus partial-check
26. Klik baris `All Categories`

### TC-AC-DC-295: Kotak parent tercentang penuh menampilkan Device Name parent itu sendiri dan seluruh descendant

27. Centang kotak `Industrial Scanner`
28. Verifikasi tabel menampilkan tepat tiga Device Name: `IND-1-{runId}-011`, `TS-200`, `TS-210`
29. Verifikasi `Industrial Scanner`, `Rugged`, dan `Rugged Kit` berstatus tercentang
30. Klik baris `All Categories`

## Notes

- Urutan TC dalam spec: TC-AC-DC-292, 296, 294, 295. TC-AC-DC-292 dan 296 memerlukan keadaan tanpa `IND-1` (data dinamis #6 membatasi `IND-1` pada TC-AC-DC-294, 295, dan 301), sehingga Device Name dibuat pada langkah 20 sebelum TC-AC-DC-294 (S-10).
- Langkah penghubung (S-03): langkah 1 mencatat baseline; langkah 6 meng-expand cabang `Smart Fixed Reader` supaya seluruh descendant yang diasersi terlihat (S-14); `All Categories` (langkah 10, 26, 30) melepas pilihan (S-09); langkah 20 memuat ulang halaman agar tree dan tabel memuat Device Name baru dan state expand kembali ke kondisi awal.
- Nama Device Name dinamis memakai suffix `{runId}-011` (S-12); TC menulis literal `IND-1` sehingga asersi memakai nama bersuffix.
- Temuan untuk QA: (1) Data Dinamis #6 menyebut `IND-1` dibuat automation baseline; spec membuat Device Name milik sendiri bersuffix dan hanya membaca node Pre-setup `Industrial Scanner`. (2) Ukuran halaman default tabel Device Name tidak ditulis TC; total baris diasersi lewat footer pagination (langkah 8 dan 19).
