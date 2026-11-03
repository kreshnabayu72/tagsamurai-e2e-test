---
id: TC-AC-DC-E2E-002-screening-sidebar-node-panjang-dan-klik
title: "Screening Sidebar Category: Klik Nama dan Panah Node Hanya Expand/Collapse, Drag and Drop Tidak Mengubah Urutan, dan Nama 120 Karakter Terpotong dengan Tooltip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-6
  - TC-AC-DC-7
  - TC-AC-DC-8
  - TC-AC-DC-303
coverage:
  web: automated
---

# Screening Sidebar Category: Klik Nama dan Panah Node Hanya Expand/Collapse, Drag and Drop Tidak Mengubah Urutan, dan Nama 120 Karakter Terpotong dengan Tooltip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) dan #15 (Device Name) hanya dibaca; spec tidak membuat, mengubah, atau menghapus node maupun Device Name. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Kemampuan teknis: drag and drop pada node tree (Spectra) dan hover untuk tooltip.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-8: Klik nama node Hardware dan TAG hanya expand atau collapse tanpa mengubah filter

1. Catat total baris tabel Device Name pada footer pagination (tabel tanpa filter Category)
2. Klik nama node `Hardware`
3. Verifikasi cabang `Hardware` ter-expand
4. Klik nama node `Hardware` lagi
5. Verifikasi cabang `Hardware` collapse
6. Klik nama node `TAG`
7. Verifikasi cabang `TAG` ter-expand
8. Verifikasi kotak centang `Hardware` dan `TAG` tidak berubah dan tidak ada node yang menjadi partial-check
9. Verifikasi isi tabel Device Name tidak berubah (total baris sama dengan catatan langkah 1)

### TC-AC-DC-303: Klik nama dan panah node parent non-root hanya expand atau collapse tanpa mengubah pilihan

10. Klik panah node `Hardware`
11. Verifikasi cabang `Hardware` ter-expand
12. Klik nama node `Handheld Reader`
13. Verifikasi cabang `Handheld Reader` ter-expand
14. Klik panah node `Handheld Reader`
15. Verifikasi cabang `Handheld Reader` collapse
16. Klik nama node `Handheld Reader`
17. Klik nama node `Filter Induk`
18. Verifikasi cabang `Handheld Reader` dan cabang `Filter Induk` ter-expand
19. Klik panah node `Filter Induk`
20. Verifikasi cabang `Filter Induk` collapse
21. Verifikasi kotak `Handheld Reader`, `Filter Induk`, dan `Hardware` tidak berubah dan tidak ada node yang menjadi partial-check
22. Verifikasi isi tabel Device Name tidak berubah (total baris sama dengan catatan langkah 1)

### TC-AC-DC-6: Urutan node tidak dapat diubah manual lewat drag and drop

23. Tarik node `Rugged Scanner` ke atas node `Barcode Handheld` lalu lepaskan
24. Verifikasi node `Rugged Scanner` tetap pada posisinya (terakhir di antara anak `Handheld Reader`)
25. Verifikasi urutan anak `Handheld Reader` tetap A-Z

### TC-AC-DC-7: Nama Category 120 karakter terpotong mengikuti kontainer dan tooltip menampilkan nama penuh

26. Amati label node dengan nama 120 karakter `Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudang Bes`
27. Verifikasi label node mengikuti lebar kontainer sidebar
28. Verifikasi label node tidak melebarkan panel sidebar
29. Hover node dengan nama 120 karakter
30. Verifikasi tooltip menampilkan nama penuh 120 karakter secara utuh

## Notes

- Urutan TC dalam spec: TC-AC-DC-8, 303, 6, 7. TC-AC-DC-8 dan 303 dimulai dari `Hardware` collapsed, sedangkan TC-AC-DC-6 dan 7 membutuhkan `Handheld Reader` ter-expand, yang dicapai di akhir TC-AC-DC-303 (S-10).
- Langkah penghubung (S-03): langkah 1 mencatat baseline total baris tabel untuk asersi "tidak berubah"; langkah 23 sampai 30 memakai state expand dari TC-AC-DC-303 (`Hardware` dan `Handheld Reader` ter-expand), sehingga tidak ada langkah expand ulang.
- Temuan untuk QA: (1) TC-AC-DC-7 Expected a menyebut "mengikuti lebar kontainer sidebar" tanpa nilai lebar; asersi mengikuti teks TC (label terpotong sesuai kontainer, panel tidak melebar). (2) Mekanisme drag and drop pada TC-AC-DC-6 tidak merinci perangkat input; dipakai aksi drag standar Spectra.
