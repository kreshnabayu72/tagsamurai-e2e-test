---
id: TC-GS-BRAND-E2E-057-detail-device-sku-list-principal-distributor-screening
title: "Brand Detail: Device SKU List pada Instance Principal dan Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-187
  - TC-GS-BRAND-188
  - TC-GS-BRAND-198
  - TC-GS-BRAND-199
  - TC-GS-BRAND-259
coverage:
  web: automated
tags: [principal]
---

# Brand Detail: Device SKU List pada Instance Principal dan Distributor

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai (dengan langkah ganti akun eksplisit):
  - Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Akun aktor pertama: login di hook `before` spec ini.
  - Total Control (Distributor), Bima Saputra, `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD` (fixture baru, belum ada; disediakan tim FE/QA). Login lewat UI di langkah 35.
  - Total Control Client A, Sari Dewi, `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`: akun default suite, hanya dipakai hook `after` untuk memulihkan sesi.
- Environment variable: `GS_PRINCIPAL_TC_PASSWORD`, `GS_DISTRIBUTOR_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, hanya dibaca, tanpa suffix `{runId}`):
  - Instance Principal: `Signal One` (Device SKU `SKU-HR-001` Handheld Reader A1 / Handheld Reader, `SKU-TB-002` Tablet T10 / Tablet, `SKU-GW-003` BLE Gateway G2 / BLE Gateway; Total Item 3; Item Type List kosong), `Quiet Brand` (bebas, 0 SKU), `Mixed One` (1 Item Type FAMS `Gateway Kit` / Product Fixed Asset dan 1 Device SKU `SKU-MX-001` Mixed Reader M1 / Handheld Reader; Total Item 2; fixture baru, belum ada; disediakan tim FE/QA; dipakai TC-GS-BRAND-199).
  - Instance Distributor: `Aero Dist` (1 Device SKU `SKU-DS-001` Distributor Reader A1 / Handheld Reader; fixture baru, belum ada; disediakan tim FE/QA).
- Spec tidak membuat atau mengubah data brand, sehingga tidak ada seeding dan cleanup data. Baris brand dicari lewat Search nama brand.
- Kemampuan teknis: login/logout dalam satu spec (ganti akun dan ganti instance Principal ke Distributor); logout dan login ulang di hook `after`; membaca dan menghapus key `localStorage` browser.
- State global yang dipulihkan:
  - Konfigurasi kolom accordion Item Type List (kolom Product) dan Device SKU List (kolom Category) disimpan di `localStorage` browser dengan key unik per tabel (PRD brand.md §4.2h; prd-conventions.md §9.3), bukan per user, sehingga berlaku lintas akun pada browser yang sama. Dikembalikan ke default di langkah 25 dan di hook `after` bila langkah itu tidak sempat jalan, lewat penghapusan key `localStorage` kedua tabel atau `[Reset to Default]` pada Column Visibility masing-masing.
  - Sesi: spec berakhir pada sesi Total Control (Distributor); hook `after` logout dari akun Distributor dan login kembali sebagai akun default suite (Total Control Client A, Sari Dewi, `GS_TC_PASSWORD`).
- Precondition TC-GS-BRAND-187, 188, 198, 199: login sebagai Total Control (Principal) dan berada di Global Settings > Master Reference > Brand. TC-GS-BRAND-259: login sebagai Total Control (Distributor).

## Test Steps

### TC-GS-BRAND-187: Accordion Device SKU List pada instance Principal: default collapsed dan isi

1. Search `Signal One` pada tabel Brand
2. Klik `⋯` pada baris Signal One
3. Klik Detail → modal Brand Detail tampil
4. Verifikasi General Info `Total Item: 3`
5. Verifikasi accordion Device SKU List default collapsed
6. Verifikasi accordion Item Type List expanded
7. Expand accordion Device SKU List
8. Verifikasi kedua accordion boleh terbuka bersamaan (Item Type List tetap expanded)
9. Verifikasi kolom Device SKU List `SKU Code | Device Name | Category | Column Visibility (⋯)`
10. Verifikasi baris terurut SKU A-Z: SKU-GW-003, SKU-HR-001, SKU-TB-002
11. Verifikasi badge Category berseverity primary

### TC-GS-BRAND-198: Pagination accordion Device SKU List

12. Verifikasi seluruh 3 baris Device SKU tampil tanpa kontrol pagination

### TC-GS-BRAND-199: Setup Column accordion Item Type List dan Device SKU List (Detail Mixed One)

13. Tutup modal Brand Detail lewat `[✕]`
14. Search `Mixed One` pada tabel Brand
15. Klik `⋯` pada baris Mixed One, lalu klik Detail → modal Brand Detail tampil
16. Klik header Column Visibility (⋯) di accordion Item Type List
17. Uncheck Product
18. Verifikasi kolom Product hilang dari Item Type List
19. Expand accordion Device SKU List (Item Type List tetap expanded)
20. Verifikasi kolom Category di Device SKU List tetap tampil (konfigurasi Item Type List tidak memengaruhi Device SKU List)
21. Klik header Column Visibility (⋯) di accordion Device SKU List
22. Uncheck Category
23. Verifikasi kolom Category hilang dari Device SKU List
24. Verifikasi kolom Product di Item Type List tetap hilang sesuai konfigurasinya sendiri (konfigurasi Device SKU List tidak memengaruhi Item Type List)
25. Pemulihan: centang kembali Product pada Column Visibility Item Type List dan Category pada Column Visibility Device SKU List

### TC-GS-BRAND-188: Accordion Device SKU List tetap dirender dengan empty state saat 0 SKU

26. Tutup modal Brand Detail lewat `[✕]`
27. Search `Quiet Brand` pada tabel Brand
28. Klik `⋯` pada baris Quiet Brand, lalu klik Detail → modal Brand Detail tampil
29. Expand accordion Device SKU List
30. Verifikasi accordion Device SKU List tampil
31. Verifikasi empty state Title `No hardware SKUs linked`
32. Verifikasi empty state description `No hardware SKUs currently reference this brand.`

### TC-GS-BRAND-259: Accordion Device SKU List dirender pada instance Distributor

33. Tutup modal Brand Detail lewat `[✕]`
34. Logout dari akun Total Control (Principal)
35. Login sebagai Total Control (Distributor) `totalControlDistributor_automated_qaTeam1@qwertysystem.net` dengan `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD`
36. Buka Global Settings > Master Reference > Brand
37. Search `Aero Dist` pada tabel Brand
38. Klik `⋯` pada baris Aero Dist, lalu klik Detail → modal Brand Detail tampil
39. Verifikasi accordion Item Type List expanded
40. Verifikasi accordion Device SKU List collapsed tampil
41. Verifikasi General Info `Total Item: 1`
42. Expand accordion Device SKU List
43. Verifikasi baris `SKU-DS-001` / `Distributor Reader A1` / `Handheld Reader`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 187, 198 (Signal One, satu modal Detail terbuka), lalu 199 (Mixed One), lalu 188 (Quiet Brand), lalu 259 (Distributor, akun berbeda). Alasan: Signal One dibuka sekali; TC-GS-BRAND-198 memakai Detail Signal One yang sudah terbuka dengan Device SKU List expanded dari TC-GS-BRAND-187 (langkah "Buka Detail Signal One, expand Device SKU" sudah terpenuhi); TC-GS-BRAND-259 memakai akun berbeda sehingga di akhir.
- Urutan langkah TC-GS-BRAND-199 mengikuti TC: uncheck Product di Item Type List (langkah 16-18), lalu expand Device SKU List dan uncheck Category (langkah 19-23). Expected c ("konfigurasi satu tabel tidak memengaruhi tabel lain") diwujudkan di langkah 20 dan 24.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 14, 27, 37 (Search untuk menemukan baris brand), langkah 13, 26, 33 (menutup modal Brand Detail sebelum brand berikutnya), dan langkah 25 (pemulihan konfigurasi kolom; hook `after` sebagai cadangan).
- TC-GS-BRAND-259 (instance Distributor) berbeda akun dan instance dari empat TC lain; digabung di spec ini dengan langkah ganti akun eksplisit (langkah 34-36), dan sesi dipulihkan di hook `after`.
- TC-GS-BRAND-199 memakai brand Principal `Mixed One` (Item Type dan Device SKU sama-sama terisi) agar kedua accordion punya kolom yang bisa di-uncheck; Signal One tidak dipakai karena Item Type List-nya kosong.
