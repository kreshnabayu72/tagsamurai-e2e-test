---
id: TC-GS-BRAND-E2E-036-filter-panel-used-by-items-rentang
title: "Filter Panel Tabel Brand: Rentang Used By (Items)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-135
  - TC-GS-BRAND-263
  - TC-GS-BRAND-264
  - TC-GS-BRAND-265
  - TC-GS-BRAND-266
  - TC-GS-BRAND-278
  - TC-GS-BRAND-145
coverage:
  web: automated
---

# Filter Panel Tabel Brand: Rentang Used By (Items)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data brand.
- Akun: Total Control Client A, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (Last Updated sebelum hari uji) dengan angka `Used By (Items)`: Acme Corp 1 (FAMS: Forklift), Brightway 0, Duo Brand 2 (FAMS: Router; Supply: Cable), Helix Works 0, Kestrel 2 (FAMS: Laptop; Supply: Laptop), Lumina Co 0, Nimbus Gear 0, Northwind Co 1 (Supply: Copy Paper), Orion Tech 0, Tagline Co 0 (all-tags: snapshot nama, tidak dihitung), Vertex Labs 5 (FAMS: Laptop, Monitor; Supply: Printer Ink, Scanner Paper, Toner Cartridge), Zenith Corp 1 (FAMS: Drill).
- Brand Ten Co (D-39) dan Big Co (D-40) tidak boleh ada di environment selama spec ini berjalan, karena keduanya melampaui angka tertinggi Vertex Labs; kedua fixture dibuat dan dibersihkan oleh spec pemakainya.
- Cleanup: hook `after` memulihkan Filter, visibilitas kolom (Used By (Items) visible), dan Sort tabel ke default.
- Kemampuan teknis: Column Visibility lewat header kolom Actions (`⋯`); pengetikan keystroke ke input Filter Panel (`Min` dan `Max`); pemantauan request jaringan (status respons List).
- TC-GS-BRAND-135 sampai TC-GS-BRAND-145: Login sebagai Total Control, berada di Brand tab; tidak ada prasyarat data lain.

## Test Steps

### TC-GS-BRAND-135: Screening Filter Panel tabel Brand

1. Klik Filter
2. Verifikasi field `Used By (Items)` berupa rentang dua input dengan placeholder `Min` dan `Max`
3. Verifikasi field `Last Updated` berupa date range picker dengan placeholder `Select date`
4. Verifikasi tombol Filter Panel `[Clear Field]` (kiri) dan `[Apply]` (kanan) sesuai komponen

### TC-GS-BRAND-278: Input filter Used By (Items) hanya menerima angka bulat 0 ke atas

5. Ketik `-3` di field Min
6. Verifikasi field Min berisi `3` (tanda minus tidak masuk)
7. Kosongkan field Min
8. Ketik `2.5` di field Min
9. Verifikasi field Min berisi `25` (titik tidak masuk)
10. Kosongkan field Min
11. Ketik `2,5` di field Min
12. Verifikasi field Min berisi `25` (koma tidak masuk)
13. Kosongkan field Min
14. Ketik `abc` di field Min
15. Verifikasi field Min tetap kosong (huruf tidak masuk)
16. Ketik `-3` di field Max
17. Verifikasi field Max berisi `3` (tanda minus tidak masuk)
18. Kosongkan field Max
19. Ketik `2.5` di field Max
20. Verifikasi field Max berisi `25` (titik tidak masuk)
21. Kosongkan field Max
22. Ketik `2,5` di field Max
23. Verifikasi field Max berisi `25` (koma tidak masuk)
24. Kosongkan field Max
25. Ketik `abc` di field Max
26. Verifikasi field Max tetap kosong (huruf tidak masuk)
27. Verifikasi tidak ada pesan error di field Min
28. Verifikasi tidak ada pesan error di field Max
29. Klik [Clear Field]

### TC-GS-BRAND-263: Filter Used By (Items) hanya Min

30. Isi Min `5` dan biarkan Max kosong
31. Klik [Apply]
32. Verifikasi tabel hanya menampilkan Vertex Labs (angka `5`)
33. Verifikasi brand dengan angka di bawah 5 tidak tampil

### TC-GS-BRAND-264: Filter Used By (Items) hanya Max

34. Buka Filter Panel
35. Klik [Clear Field]
36. Isi Max `0` dan biarkan Min kosong
37. Klik [Apply]
38. Verifikasi tabel menampilkan brand dengan angka `0`, termasuk Orion Tech
39. Verifikasi Acme Corp (`1`) dan Vertex Labs (`5`) tidak tampil

### TC-GS-BRAND-265: Filter Used By (Items) Min dan Max inklusif

40. Buka Filter Panel
41. Klik [Clear Field]
42. Isi Min `1` dan Max `2`
43. Klik [Apply]
44. Verifikasi tabel memuat brand dengan angka `1` dan `2` (Acme Corp, Duo Brand, Kestrel, Northwind Co, Zenith Corp) karena batas inklusif
45. Verifikasi Orion Tech (`0`) dan Vertex Labs (`5`) tidak tampil

### TC-GS-BRAND-266: Filter Used By (Items) Min lebih besar dari Max menghasilkan empty state

46. Buka Filter Panel
47. Klik [Clear Field]
48. Isi Min `5` dan Max `2`
49. Klik [Apply]
50. Verifikasi respons List sukses (server tidak menolak permintaan)
51. Verifikasi empty state `No results found` dengan teks `Try adjusting your search or filter.`
52. Verifikasi tidak ada pesan error
53. Verifikasi tidak ada copy khusus modul

### TC-GS-BRAND-145: Filter Used By (Items) tetap berlaku saat kolom Used By (Items) di-hide

54. Buka Filter Panel
55. Klik [Clear Field]
56. Isi Min `5`
57. Klik [Apply]
58. Klik header kolom Actions (`⋯`) untuk membuka Overlay Column Visibility
59. Sembunyikan kolom Used By (Items)
60. Verifikasi tabel tetap hanya menampilkan Vertex Labs
61. Buka Filter Panel
62. Verifikasi field Used By (Items) tetap tersedia di Filter Panel
63. Tampilkan kembali kolom Used By (Items) lewat Overlay Column Visibility
64. Buka Filter Panel
65. Klik [Clear Field]
66. Klik [Apply]

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-BRAND-278 (keystroke di panel yang masih terbuka dari screening) ditaruh tepat sesudah TC-GS-BRAND-135 dan TC-GS-BRAND-145 (hide kolom) ditaruh paling akhir; urutan sumber 135, 263, 264, 265, 266, 278, 145.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 10, 13, 18, 21, dan 24 (mengosongkan field Min atau Max sebelum nilai ketik berikutnya), langkah 29, 35, 41, 47, dan 55 ([Clear Field] di Filter Panel untuk memulai tiap TC dari filter kosong), serta pemulihan state di akhir spec (langkah 63 menampilkan kembali kolom Used By (Items), langkah 64 sampai 66 membuka Filter Panel, mengosongkan, dan menerapkan filter kosong; hook `after` menjadi cadangan).
- Langkah 5 sampai 28 mengetik `-3`, `2.5`, `2,5`, dan `abc` ke field Min lalu ke field Max, masing-masing dengan Verifikasi terpisah per nilai sesuai Expected Result a TC-GS-BRAND-278.
- Angka `Used By (Items)` per brand diambil dari Tabel Data Uji Pre-setup (Referensi); brand Tagline Co dan Vertex Labs (snapshot all-tags) tidak dihitung pada angka Used By.
- Spec memuat dua TC "UI Only" (TC-GS-BRAND-135 dan TC-GS-BRAND-278) yang tetap dijalankan di atas backend nyata bersama TC filter lain karena dataset dan layar yang sama.
- Fixture Ten Co (D-39) dan Big Co (D-40) tidak ada selama spec ini berjalan (lihat Prerequisites); TC-GS-BRAND-263 mengasumsikan Vertex Labs sebagai angka tertinggi.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
