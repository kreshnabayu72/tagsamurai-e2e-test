---
id: TC-FA-FAAM-E2E-119-filter-opsi-dinamis-client-kosong-stale-dan-skeleton
title: "Filter: Opsi Dinamis (Client Kosong, Opsi Hilang, Brand Bertambah, Skeleton Dropdown)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-373
  - TC-FA-FAAM-374
  - TC-FA-FAAM-747
  - TC-FA-FAAM-748
coverage:
  web: automated
---

# Filter: Opsi Dinamis (Client Kosong, Opsi Hilang, Brand Bertambah, Skeleton Dropdown)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (client utama, tidak diubah selain seed milik spec): enam Asset Name contoh dan 30 `Seed Item` (Pre-setup #10 sampai #15, `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada); Brand `Dell` dan `Apple` muncul di data tabel (Pre-setup #10 dan #12).
- Data Dinamis (seed API di hook `before`, nama bersuffix, dihapus di hook `after`): Brand `Temp Brand {runId}-119` dan Asset Name `Temp Brand Item {runId}-119` ber-Brand itu (salinan Pre-setup #23b dan #23c).
- Client lain: client tanpa Asset Name (Pre-setup #16b, tanpa Changelog dan tanpa kategori) untuk TC-FA-FAAM-373, dan client `AutoFilterOpt` (Pre-setup #15h, tiga Asset Name ber-Brand `Dell` saja; Brand `Lenovo` ada di master Brand) untuk TC-FA-FAAM-747. Email akun Total Control kedua client tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password `Spectra.env.FA_TC_EMPTY_PASSWORD` (client Pre-setup #16b) dan `Spectra.env.FA_TC_FILTEROPT_PASSWORD` (client `AutoFilterOpt`), didaftarkan tim FE.
- Data Uji TC-FA-FAAM-747: Asset Name `Filter Opt Item {runId}-119`; Category `IT Equipment` (leaf lewat `[Select Category]`); TAG Type `QR`; Brand `Lenovo`; UoM `Unit`. Field wajib lain mengikuti isian minimal Create (Brand wajib; nilai lain tidak diperlukan TC).
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons request opsi dropdown filter Brand 3 detik (dilepas segera sesudah dipakai), sesi API aktor untuk menghapus `Temp Brand Item {runId}-119` sebagai pelaku kedua, dan seed API client.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-748: Dropdown Brand menampilkan skeleton atau spinner mini saat opsi diambil dari server
1. Aktifkan intercept jaringan yang menunda respons request opsi dropdown filter Brand selama 3 detik
2. Klik icon Filter
3. Buka dropdown Brand saat respons masih tertunda
4. Verifikasi overlay opsi Brand menampilkan skeleton / spinner mini
5. Verifikasi overlay opsi Brand bukan daftar kosong dan bukan teks `No options available`
6. Tunggu respons tiba
7. Verifikasi skeleton / spinner mini hilang
8. Verifikasi overlay opsi Brand memuat opsi `Dell` dan `Apple`
9. Lepas intercept jaringan
10. Klik icon Filter untuk menutup Filter Panel
### TC-FA-FAAM-374: Opsi filter yang sedang dipakai lalu hilang dibersihkan saat filter diterapkan ulang
11. Klik icon Filter
12. Pilih Brand `Temp Brand {runId}-119`, lalu klik `[Apply]`
13. Verifikasi baris `Temp Brand Item {runId}-119` tampil di tabel
14. Tunggu aksi selesai
15. Hapus `Temp Brand Item {runId}-119` lewat sesi API aktor hingga penghapusan tersimpan
16. Klik icon Filter
17. Klik `[Apply]` lagi
18. Klik icon Filter
19. Verifikasi nilai stale dibersihkan dari kriteria: field Brand `All brands`
20. Verifikasi hasil mengikuti kriteria yang tersisa: baris `Dell Latitude` dan `Ergonomic Chair` tampil
21. Verifikasi tidak ada pesan error yang tampil
22. Klik icon Filter untuk menutup Filter Panel
### Ganti akun: client tanpa Asset Name
23. Logout, lalu login sebagai Total Control client tanpa Asset Name (Pre-setup #16b) dengan `Spectra.env.FA_TC_EMPTY_PASSWORD`
### TC-FA-FAAM-373: Dropdown filter dengan sumber 0 baris menampilkan No options available
24. Klik icon Filter
25. Buka dropdown Brand
26. Verifikasi teks `No options available` tampil (bukan error)
27. Klik icon Filter untuk menutup Filter Panel
### Ganti akun: client AutoFilterOpt
28. Logout, lalu login sebagai Total Control client `AutoFilterOpt` (Pre-setup #15h) dengan `Spectra.env.FA_TC_FILTEROPT_PASSWORD`
### TC-FA-FAAM-747: Opsi dropdown filter Brand bertambah setelah Asset Name ber-Brand baru dibuat tanpa reload
29. Klik icon Filter
30. Buka dropdown Brand
31. Verifikasi opsi Brand hanya `Dell`
32. Klik icon Filter untuk menutup Filter Panel
33. Klik `[+ Asset Name]`
34. Isi Asset Name `Filter Opt Item {runId}-119`
35. Klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`
36. Pilih TAG Type `QR`
37. Pilih Brand `Lenovo`
38. Pilih UoM `Unit`
39. Klik `[Submit]`
40. Klik icon Filter
41. Buka dropdown Brand
42. Verifikasi opsi Brand memuat `Dell` dan `Lenovo` tanpa reload halaman
43. Klik icon Filter untuk menutup Filter Panel

## Notes

- Urutan blok: client utama lebih dulu (TC-FA-FAAM-748, TC-FA-FAAM-374), lalu dua pergantian client sesuai Prerequisites; hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup Filter Panel, "Tunggu aksi selesai" sebelum pelaku kedua (bagian 8b butir 8), dan klik `[Apply]` ulang yang menjadi aksi TC-FA-FAAM-374.
- Verifikasi baris `Temp Brand Item {runId}-119` tampil setelah Apply pada TC-FA-FAAM-374 adalah anchor positif bahwa opsi Brand sedang dipakai (S-03; alasan: membuktikan kriteria benar-benar ter-Apply sebelum pelaku kedua menghapus).
- Pelaku kedua memakai sesi API aktor, bukan konteks UI kedua; tidak ada butir P-2.
- Intercept TC-FA-FAAM-748 hanya menahan respons untuk mengamati state UI dan dilepas segera sesudah pengamatan.
- Spec melewati sekitar 35 langkah karena empat blok memakai tiga client berbeda; setiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembuatan Asset Name `Filter Opt Item {runId}-119` pada TC-FA-FAAM-747 mengikuti urutan isian Create dari TC-FA-FAAM-143 (field wajib saja); dihapus di hook `after`.
- Temuan untuk QA: Pre-setup #16b dan #15h berupa client tanpa baris akun Total Control (email tidak tertulis); TC-FA-FAAM-747 menyebut "field wajib lain" tanpa nilai, spec memakai Category `IT Equipment`, TAG Type `QR`, dan UoM `Unit` dari TC-FA-FAAM-143; Data Dinamis #106 (`Filter Opt Item 747`) bernama tanpa suffix dan berstatus "tetap ada", sedangkan spec memberi suffix dan menghapusnya.
