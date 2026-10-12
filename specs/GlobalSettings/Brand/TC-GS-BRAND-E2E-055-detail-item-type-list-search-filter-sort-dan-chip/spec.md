---
id: TC-GS-BRAND-E2E-055-detail-item-type-list-search-filter-sort-dan-chip
title: "Brand Detail: Search, Filter, Sort, dan Chip Filter Item Type List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-190
  - TC-GS-BRAND-191
  - TC-GS-BRAND-192
  - TC-GS-BRAND-285
  - TC-GS-BRAND-286
  - TC-GS-BRAND-287
coverage:
  web: automated
---

# Brand Detail: Search, Filter, Sort, dan Chip Filter Item Type List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, hanya dibaca, tanpa suffix `{runId}`): brand `Vertex Labs` dengan Item Type FAMS Laptop (Model `Nova 5 Pro`, `Nova Slim 3`, `Vertex Pro 14`, `Vertex Pro 16`, `Vertex Pro 20`) dan Monitor, serta Supply Printer Ink, Scanner Paper, Toner Cartridge. Total 5 baris pada accordion Item Type List; Item Type tanpa Model/Type (Toner Cartridge, Printer Ink, Scanner Paper) bernilai `—`.
- Spec tidak membuat atau mengubah data, sehingga tidak ada seeding dan cleanup. Population D-01 tidak dibutuhkan; baris Vertex Labs dicari lewat Search `Vertex Labs`.
- Kemampuan teknis: mengetik di kotak search di dalam dropdown Product Filter; klik `(X)` pada chip filter.
- Precondition TC-GS-BRAND-190, 191, 192: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand. TC-GS-BRAND-285, 286, 287 tambahan: Vertex Labs punya Item Type FAMS dan Supply (Pre-setup).
- State global yang dipulihkan: tidak ada (Search/Filter/Sort di modal tidak bertahan setelah modal ditutup; spec tetap mengosongkannya antar TC).

## Test Steps

### TC-GS-BRAND-190: Search accordion Item Type List pada Item Type, Product, dan Model/Type

1. Search `Vertex Labs` pada tabel Brand
2. Klik `⋯` pada baris Vertex Labs
3. Klik Detail → modal Brand Detail tampil
4. Klik icon Search pada Table Tools accordion Item Type List
5. Verifikasi placeholder Search `Search item type, product, or model...`
6. Search `toner`
7. Verifikasi hasil memuat Toner Cartridge
8. Search `supply`
9. Verifikasi hasil memuat 3 baris Supply Asset
10. Search `slim`
11. Verifikasi hasil memuat Laptop
12. Search `zz`
13. Verifikasi pesan `No results found`
14. Verifikasi deskripsi `Try adjusting your search or filter.`
15. Kosongkan teks Search

### TC-GS-BRAND-192: Sort accordion Item Type List: Item Type, Product, Model/Type

16. Klik header Item Type
17. Verifikasi Item Type terurut A-Z
18. Klik header Product
19. Verifikasi Product terurut A-Z
20. Klik header Model / Type
21. Verifikasi Model / Type ascending: `—` di awal, lalu jumlah chip terkecil

### TC-GS-BRAND-191: Filter Product accordion Item Type List

22. Klik Product Filter pada Table Tools accordion Item Type List
23. Verifikasi opsi Product: `Fixed Asset`, `Supply Asset` (placeholder `All products`)
24. Pilih `Fixed Asset`
25. Klik [Apply]
26. Verifikasi tabel memuat baris Laptop dan Monitor

### TC-GS-BRAND-285: Menghapus chip filter Product lewat (X) di Item Type List meng-uncheck opsi Product

27. Klik Product Filter, kosongkan pilihan Product (sisa TC-GS-BRAND-191)
28. Pilih Product `Fixed Asset` dan `Supply Asset`
29. Klik `(X)` pada chip `Supply Asset`
30. Verifikasi chip `Supply Asset` hilang
31. Verifikasi chip `Fixed Asset` tetap ada
32. Buka dropdown Product, amati checkbox
33. Verifikasi checkbox `Supply Asset` di dalam dropdown ter-uncheck
34. Verifikasi checkbox `Fixed Asset` tetap tercentang
35. Klik [Apply]
36. Verifikasi tabel hanya memuat baris Product Fixed Asset (Laptop, Monitor)

### TC-GS-BRAND-286: Meng-uncheck opsi Product di dalam dropdown menghapus chip pada Item Type List

37. Klik Product Filter, kosongkan pilihan Product (sisa TC-GS-BRAND-285)
38. Pilih Product `Fixed Asset` dan `Supply Asset`
39. Buka dropdown Product dan uncheck `Supply Asset`
40. Verifikasi chip `Supply Asset` hilang dari field
41. Verifikasi chip `Fixed Asset` tetap ada
42. Klik [Apply]
43. Verifikasi tabel hanya memuat baris Product Fixed Asset (Laptop, Monitor)

### TC-GS-BRAND-287: Search di dalam dropdown Product dan logika OR dalam field filter Item Type List

44. Klik Product Filter, kosongkan pilihan Product (sisa TC-GS-BRAND-286)
45. Buka dropdown Product, ketik `SUPPLY` pada kotak search di dalam dropdown
46. Verifikasi daftar opsi hanya memuat `Supply Asset` (tidak membedakan huruf besar kecil)
47. Ketik `zzqx` pada kotak search yang sama
48. Verifikasi daftar opsi kosong, tanpa opsi cocok
49. Kosongkan kotak search, pilih `Fixed Asset` dan `Supply Asset`
50. Klik [Apply]
51. Verifikasi tabel memuat baris Product Fixed Asset
52. Verifikasi tabel memuat baris Product Supply Asset (gabungan OR dalam satu field)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 190 (Search), 192 (Sort), lalu 191, 285, 286, 287 (Filter). Alasan: Sort dijalankan sebelum Filter mengubah dataset tabel dan Filter dijalankan berurutan. Brand Detail Vertex Labs dibuka sekali (langkah 1-3) untuk keenam TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 (mengosongkan Search sebelum Sort), langkah 27, 37, 44 (mengosongkan pilihan Product dari TC sebelumnya).
- Langkah "Buka Detail Vertex Labs" pada TC-GS-BRAND-191, 192, 285, 286, 287 tidak diulang karena modal masih terbuka dari TC sebelumnya.
- Langkah 21: urutan `—` di awal lalu jumlah terkecil mengikuti Expected Result TC-GS-BRAND-192 c.
