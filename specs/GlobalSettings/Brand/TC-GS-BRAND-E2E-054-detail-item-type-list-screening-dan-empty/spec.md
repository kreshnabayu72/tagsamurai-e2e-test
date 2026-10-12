---
id: TC-GS-BRAND-E2E-054-detail-item-type-list-screening-dan-empty
title: "Brand Detail: Screening Item Type List, Empty State, dan Hover Chip Model/Type"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-184
  - TC-GS-BRAND-186
  - TC-GS-BRAND-189
  - TC-GS-BRAND-193
  - TC-GS-BRAND-262
  - TC-GS-BRAND-203
coverage:
  web: automated
---

# Brand Detail: Screening Item Type List, Empty State, dan Hover Chip Model/Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, hanya dibaca, tanpa suffix `{runId}`):
  - `Vertex Labs`: FAMS Laptop (Model `Nova 5 Pro`, `Nova Slim 3`, `Vertex Pro 14`, `Vertex Pro 16`, `Vertex Pro 20`), Monitor (Model `Vertex Ultra Long Model 000001`, 30 karakter); Supply Printer Ink, Scanner Paper, Toner Cartridge (Model/Type `—`); all-tags 4 TAG (snapshot nama, tidak dihitung). Total Item 5.
  - `Orion Tech`: bebas relasi (Total Item 0).
  - `Kestrel`: FAMS Laptop dan Supply Laptop (Item Type bernama sama di dua Product). Total Item 2.
- Fixture yang belum ada (disiapkan tim FE): Model/Type 30 karakter `Vertex Ultra Long Model 000001` pada Item Type Monitor milik Vertex Labs (precondition TC-GS-BRAND-203).
- Spec tidak membuat atau mengubah data, sehingga tidak ada seeding dan cleanup. Population D-01 tidak dibutuhkan (baris dicari lewat Search `Vertex Labs`, `Kestrel`, `Orion Tech` supaya tidak bergantung pada halaman pagination).
- Kemampuan teknis: hover (tooltip) pada chip Model/Type.
- Precondition TC-GS-BRAND-184, 186, 189, 193, 262, 203: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.
- State global yang dipulihkan: tidak ada.

## Test Steps

### TC-GS-BRAND-184: Screening Modal Brand Detail pada instance Client

1. Search `Vertex Labs` pada tabel Brand
2. Klik `⋯` pada baris Vertex Labs
3. Klik Detail → modal Brand Detail tampil
4. Verifikasi bagian Header: Title `Brand Detail`
5. Verifikasi bagian Header: `[✕]`
6. Verifikasi bagian General Info: `Vertex Labs` (bold)
7. Verifikasi bagian General Info: `Total Item: 5`
8. Verifikasi accordion `Item Type List` expanded
9. Verifikasi Table Tools accordion Item Type List: `Search | Product Filter | Download`
10. Verifikasi kolom accordion Item Type List: `Item Type (sortable) | Product (sortable) | Model / Type (sortable) | Column Visibility (⋯)`
11. Verifikasi accordion `Device SKU List` tidak dirender (instance Client)

### TC-GS-BRAND-186: Isi accordion Item Type List: Product dan Model/Type

12. Amati isi accordion Item Type List pada Brand Detail Vertex Labs yang sama
13. Verifikasi urutan baris Item Type A-Z lalu Product: Laptop (Fixed Asset), Monitor (Fixed Asset), Printer Ink (Supply Asset), Scanner Paper (Supply Asset), Toner Cartridge (Supply Asset)
14. Verifikasi baris Laptop menampilkan chip Model/Type `Nova 5 Pro`, `Nova Slim 3`, dan `+3 more` (urut A-Z)
15. Verifikasi baris Toner Cartridge menampilkan Model/Type `—`
16. Verifikasi badge Product `Fixed Asset` dan `Supply Asset` berseverity primary

### TC-GS-BRAND-193: Accordion Item Type List tanpa pagination

17. Verifikasi seluruh 5 baris tampil tanpa kontrol pagination pada accordion Item Type List

### TC-GS-BRAND-203: Hover chip Model/Type yang terpotong menampilkan nama penuh

18. Amati chip Model/Type pada baris Monitor
19. Verifikasi chip tampil `Vertex Ultra..Model 000001` (12 huruf pertama + `..` + 12 huruf terakhir, web)
20. Hover chip Model/Type pada baris Monitor
21. Verifikasi tooltip nama penuh `Vertex Ultra Long Model 000001`

### TC-GS-BRAND-262: Detail Brand dengan Item Type bernama sama di FAMS dan Supply

22. Tutup modal Brand Detail lewat `[✕]`
23. Search `Kestrel` pada tabel Brand
24. Klik `⋯` pada baris Kestrel
25. Klik Detail → modal Brand Detail tampil
26. Verifikasi General Info `Total Item: 2`
27. Verifikasi accordion Item Type List memuat dua baris berurutan (Item Type lalu Product): `Laptop` / `Fixed Asset` dan `Laptop` / `Supply Asset`

### TC-GS-BRAND-189: Empty state accordion Item Type List

28. Tutup modal Brand Detail lewat `[✕]`
29. Search `Orion Tech` pada tabel Brand
30. Klik `⋯` pada baris Orion Tech
31. Klik Detail → modal Brand Detail tampil
32. Verifikasi General Info `Total Item: 0`
33. Verifikasi empty state Title `No item types linked`
34. Verifikasi empty state description `No products or items currently reference this brand.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 184, 186, 193, 203 (semua memakai Brand Detail Vertex Labs yang dibuka sekali di langkah 1-3, karena langkah "Buka Detail Vertex Labs" identik), lalu 262 (Kestrel), lalu 189 (Orion Tech). Urutan TC sumber (184, 186, 189, 193, 262, 203) tidak dipertahankan supaya Detail Vertex Labs tidak dibuka berulang.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 23, 29 (Search untuk menemukan baris brand) dan langkah 22, 28 (menutup modal Brand Detail sebelum brand berikutnya).
- Baris brand dicari lewat Search, bukan lewat halaman pagination, supaya tidak bergantung pada Population (TC sumber menyebut `Vertex Labs` ada di halaman 3 pada 24 brand). Search dipakai hanya untuk menemukan baris, bukan objek uji.
- TC-GS-BRAND-189 menggunakan Orion Tech yang bebas relasi; bila fixture environment mengaitkan Orion Tech dengan data lain, asersi Total Item 0 gagal dan fixture perlu dibetulkan oleh tim FE.
- TC-GS-BRAND-203 mengacu ke `prd-conventions.md` §9.14 untuk format pemotongan chip (12 huruf pertama + `..` + 12 huruf terakhir pada web).
