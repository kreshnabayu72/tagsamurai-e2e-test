---
id: TC-AC-DC-E2E-090-filter-category-persistensi-refresh-dan-back
title: "Filter Category: Pilihan Dipertahankan Setelah F5 atau Back, State Expand dan Pencarian Tree Direset"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-36
coverage:
  web: automated
---

# Filter Category: Pilihan Dipertahankan Setelah F5 atau Back, State Expand dan Pencarian Tree Direset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) dan #15 (Device Name `FN-1`) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pilihan filter Category (tersimpan per user); dikosongkan lewat `All Categories` di akhir spec dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-36: Pilihan filter Category setelah refresh atau kembali dari halaman lain

1. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk`
2. Klik node `Filter Anak 1`
3. Ketik Search `Filter` pada TreeSearchInput, tekan Enter
4. Muat ulang halaman dengan F5
5. Verifikasi state expand tree direset ke kondisi awal (`Hardware` dan `TAG` collapsed)
6. Verifikasi kotak pencarian tree kosong
7. Verifikasi tabel Device Name menampilkan `FN-1`
8. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk`
9. Verifikasi node `Filter Anak 1` tetap tercentang
10. Klik item menu navigasi `Activity Log` di sidebar aplikasi
11. Tekan tombol Back browser
12. Verifikasi tabel Device Name menampilkan `FN-1`
13. Verifikasi state expand tree direset ke kondisi awal (`Hardware` dan `TAG` collapsed)
14. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk`
15. Verifikasi node `Filter Anak 1` tetap tercentang
16. Klik baris `All Categories`

## Notes

- Urutan Expected disesuaikan dengan urutan state (8b butir 5): state expand direset diasersi sebelum node di-expand untuk mengamati centang `Filter Anak 1` (langkah 5 sampai 9 dan 12 sampai 15). Node yang tercentang hanya teramati setelah jalurnya di-expand.
- Langkah penghubung (S-03): langkah 8 dan 14 meng-expand jalur node; langkah 16 melepas pilihan filter (S-09).
- Temuan untuk QA: (1) TC-AC-DC-36 menyebut "item menu navigasi lain di sidebar aplikasi" tanpa nama; spec memakai `Activity Log`. (2) Nilai Expected "tabel Device Name menampilkan `FN-1`" bergantung pada Device Name literal Pre-setup #15 yang dibaca saja.
