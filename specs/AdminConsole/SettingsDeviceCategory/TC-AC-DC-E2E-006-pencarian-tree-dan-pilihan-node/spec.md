---
id: TC-AC-DC-E2E-006-pencarian-tree-dan-pilihan-node
title: "Pencarian Tree Category dan Pilihan Node: Centang Parent Memilih Descendant Tersembunyi, Teks Pencarian dan Pilihan Dipertahankan antar Sub-tab"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-299
  - TC-AC-DC-307
coverage:
  web: automated
---

# Pencarian Tree Category dan Pilihan Node: Centang Parent Memilih Descendant Tersembunyi, Teks Pencarian dan Pilihan Dipertahankan antar Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori), #15 (Device Name `FN-1`, `FN-2`, `FN-3`), dan #16 (Device SKU `SKU-FN-1`, `SKU-FN-2`, `SKU-FN-3`) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pilihan filter Category (tersimpan per user) dan teks pencarian tree; keduanya dikosongkan di akhir spec dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-299: Pencarian tree aktif: mencentang node memilih seluruh descendant termasuk yang disembunyikan pencarian

1. Ketik Search `Filter Induk` pada TreeSearchInput, tekan Enter
2. Verifikasi jalur `Hardware` > `Handheld Reader` > `Filter Induk` tampil
3. Verifikasi `Filter Anak 1`, `Filter Anak 2`, dan `Filter Anak 3` tidak tampil karena tidak cocok pencarian
4. Centang kotak `Filter Induk`
5. Verifikasi tabel Device Name menampilkan `FN-1`, `FN-2`, dan `FN-3`
6. Verifikasi `Filter Induk` tercentang penuh
7. Verifikasi `Handheld Reader` dan `Hardware` partial-check, meski descendant `Filter Induk` masih disembunyikan pencarian (status dihitung atas seluruh descendant)
8. Kosongkan isi kotak pencarian tree, tekan Enter
9. Expand `Hardware`, `Handheld Reader`, `Filter Induk`, dan `Filter Anak 2`
10. Verifikasi `Filter Anak 1`, `Filter Anak 2`, `Filter Cucu`, dan `Filter Anak 3` tercentang
11. Klik baris `All Categories`

### TC-AC-DC-307: Teks pencarian tree dan state expand dipertahankan saat berpindah sub-tab Device SKU dan kembali

12. Ketik Search `Filter Induk` pada TreeSearchInput, tekan Enter
13. Centang kotak `Filter Induk`
14. Pindah ke sub-tab `Device SKU`
15. Verifikasi kotak pencarian tree masih berisi "Filter Induk"
16. Verifikasi jalur `Hardware` > `Handheld Reader` > `Filter Induk` tetap tampil
17. Verifikasi tabel Device SKU menampilkan `SKU-FN-1`, `SKU-FN-2`, dan `SKU-FN-3`
18. Pindah kembali ke sub-tab `Device Name`
19. Verifikasi kotak pencarian tree tetap berisi "Filter Induk"
20. Verifikasi jalur `Hardware` > `Handheld Reader` > `Filter Induk` yang sama tetap tampil
21. Verifikasi tabel Device Name menampilkan `FN-1`, `FN-2`, dan `FN-3`
22. Klik `[×]` pada kotak pencarian tree, tekan Enter
23. Klik baris `All Categories`

## Notes

- Langkah penghubung (S-03): langkah 11, 22, dan 23 melepas pilihan filter dan mengosongkan Search supaya TC berikutnya dan spec lain mulai dari pilihan kosong (S-09); langkah 8 sampai 9 mengikuti TC-AC-DC-299 langkah 5 dan 6.
- Temuan untuk QA: TC-AC-DC-307 judul menyebut "state expand dipertahankan", tetapi Expected hanya menyebut jalur tetap tampil (bukan state expand node lain); spec mengikuti Expected. Tabel Device Name pada langkah 5, 17, dan 21 diasersi sebagai tepat tiga baris yang disebut TC.
