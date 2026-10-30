---
id: TC-GS-BRAND-E2E-059-detail-device-sku-list-chip-category-dan-or
title: "Brand Detail Principal: Chip Filter Category dan Logika OR pada Device SKU List"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-288
  - TC-GS-BRAND-289
  - TC-GS-BRAND-290
coverage:
  web: automated
tags: [principal]
---

# Brand Detail Principal: Chip Filter Category dan Logika OR pada Device SKU List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 8). Login di hook `before` spec ini; kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_PRINCIPAL_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Principal (tetap di environment, hanya dibaca, tanpa suffix `{runId}`): brand `Signal One` dengan tiga Device SKU: `SKU-HR-001` (Category `Handheld Reader`), `SKU-TB-002` (Category `Tablet`), `SKU-GW-003` (Category `BLE Gateway`).
- Spec tidak membuat atau mengubah data, sehingga tidak ada seeding dan cleanup. Tidak ada state global yang diubah.
- TC-GS-BRAND-288, 289, 290: login sebagai Total Control (Principal), berada di Global Settings > Master Reference > Brand, dan Signal One memiliki SKU-HR-001, SKU-TB-002, dan SKU-GW-003 (Pre-setup Principal).

## Test Steps

### TC-GS-BRAND-290: Search di dalam dropdown Category dan logika OR dalam field filter Device SKU List

1. Search `Signal One` pada tabel Brand, klik `⋯` pada baris Signal One > Detail → modal Brand Detail tampil
2. Expand accordion Device SKU List, klik Filter
3. Buka dropdown Category, ketik `GATEWAY` pada kotak search di dalam dropdown
4. Verifikasi daftar opsi hanya memuat `BLE Gateway` (tidak membedakan huruf besar kecil)
5. Ketik `zzqx` pada kotak search yang sama
6. Verifikasi daftar opsi kosong, tanpa opsi cocok
7. Kosongkan kotak search di dalam dropdown, pilih Category `Handheld Reader` dan `Tablet`, klik [Apply]
8. Verifikasi tabel memuat SKU-HR-001 dan SKU-TB-002 (gabungan OR dalam satu field)
9. Verifikasi tabel tidak memuat SKU-GW-003

### TC-GS-BRAND-289: Meng-uncheck opsi Category di dalam dropdown menghapus chip pada Device SKU List

10. Klik Filter, hapus semua pilihan Category yang masih terpasang dari langkah 7 sehingga filter Category kosong, klik [Apply]
11. Klik Filter, pilih Category `Handheld Reader` dan `Tablet`
12. Buka dropdown Category dan uncheck `Tablet`
13. Verifikasi chip `Tablet` hilang
14. Verifikasi chip `Handheld Reader` tetap
15. Klik [Apply]
16. Verifikasi hanya baris SKU-HR-001 yang tampil

### TC-GS-BRAND-288: Menghapus chip filter Category lewat (X) di Device SKU List meng-uncheck opsinya

17. Klik Filter, hapus semua pilihan Category yang masih terpasang dari langkah 11 sehingga filter Category kosong, klik [Apply]
18. Klik Filter, pilih Category `Handheld Reader` dan `Tablet`
19. Klik `(X)` pada chip `Tablet`
20. Verifikasi chip `Tablet` hilang
21. Verifikasi chip `Handheld Reader` tetap
22. Buka dropdown Category dan amati checkbox
23. Verifikasi checkbox `Tablet` ter-uncheck
24. Klik [Apply]
25. Verifikasi hanya baris SKU-HR-001 yang tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sumber (290 lebih dulu): TC-GS-BRAND-290 mencakup pengecekan Search di dalam dropdown (tanpa aksi Apply) dan membangun kondisi dua opsi terpilih, lalu 289 dan 288 sebagai variasi dari topik yang sama (cara melepas pilihan Tablet) berurutan.
- Langkah penghubung: langkah 1 (membuka Detail lewat Search), langkah 10 dan 17 (mengosongkan filter Category sebelum TC berikutnya) tidak tertulis di Langkah Uji TC sumber; tujuannya agar tiap TC mulai dari filter kosong, sesuai Langkah Uji TC yang mulai dari "Pilih Category" pada dropdown baru.
