---
id: TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip
title: "Unit Detail: Search, Filter Product, Sort, dan Chip Item Type List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-193
  - TC-GS-UOM-194
  - TC-GS-UOM-198
  - TC-GS-UOM-253
  - TC-GS-UOM-254
  - TC-GS-UOM-323
  - TC-GS-UOM-324
  - TC-GS-UOM-347
coverage:
  web: automated
---

# Unit Detail: Search, Filter Product, Sort, dan Chip Item Type List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` suite (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Layar awal Global Settings > Master Reference > Measurement dibuka di hook `beforeEach` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite (lihat bagian "Hook suite" di `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.
- Data Pre-setup Client A (tetap di environment, hanya dibaca, tanpa suffix `{runId}`): `Pieces` (Symbol `pc`) dengan Item Type FAMS `Laptop` (Fixed Asset), `Monitor` (Fixed Asset), dan Item Type Supply `Printer Ink` (Supply). Referensi Supply (SAMS) disiapkan lewat fixture backend (NC-09), disediakan tim FE. Spec tidak membuat atau mengubah data, sehingga tidak ada seeding dan cleanup data. Tiga baris dengan dua nilai Product distinct (Fixed Asset dan Supply) memenuhi syarat asersi sort dan filter (S-11).
- Baris `Pieces` dicari lewat Search nama unit supaya tidak bergantung pada halaman Pagination tabel utama.
- Precondition TC-GS-UOM-193, 194, 198, 253, 254, 323, 324, 347: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

1. Ketik Search `Pieces`, tekan Enter
2. Klik `⋯` pada baris Pieces
3. Klik Detail

### TC-GS-UOM-254: Placeholder dan opsi Filter Product pada Item Type List

4. Klik Filter Product
5. Verifikasi placeholder `All products`
6. Buka dropdown Product
7. Verifikasi opsi Product `Fixed Asset` dan `Supply`
8. Verifikasi kolom Product tampil sebagai badge
9. Tutup dropdown Product

### TC-GS-UOM-347: Filter Product pada Item Type List baru berlaku setelah Apply

10. Buka dropdown Product, centang `Supply`
11. Verifikasi sebelum [Apply] tabel tetap berisi `Laptop`, `Monitor`, dan `Printer Ink`
12. Klik [Apply]
13. Verifikasi tabel memuat `Printer Ink`
14. Verifikasi tabel tidak memuat `Laptop` dan `Monitor`

### TC-GS-UOM-194: Filter Product pada Item Type List

15. Klik Filter Product, uncheck `Supply`, lalu centang `Fixed Asset`
16. Verifikasi opsi Product hanya nilai yang ada (`Fixed Asset`, `Supply`)
17. Klik [Apply]
18. Verifikasi tabel memuat `Laptop` dan `Monitor`
19. Verifikasi tabel tidak memuat `Printer Ink`

### TC-GS-UOM-323: Menghapus chip filter Product lewat (X) di Item Type List meng-uncheck opsi Product

20. Buka Filter Product dan pilih `Fixed Asset` dan `Supply`
21. Klik `(X)` pada chip `Supply`
22. Verifikasi chip `Supply` hilang
23. Verifikasi chip `Fixed Asset` tetap ada
24. Buka dropdown Product, amati checkbox
25. Verifikasi checkbox `Supply` di dalam dropdown ter-uncheck
26. Verifikasi checkbox `Fixed Asset` tetap tercentang

### TC-GS-UOM-324: Meng-uncheck opsi Product di dalam dropdown menghapus chip pada Item Type List

27. Pilih `Fixed Asset` dan `Supply` pada Filter Product
28. Buka dropdown Product dan uncheck `Supply`
29. Verifikasi chip `Supply` hilang dari field
30. Verifikasi chip `Fixed Asset` tetap ada

### TC-GS-UOM-193: Search Item Type List mencakup Item Type dan Product

31. Kosongkan pilihan Filter Product (uncheck `Fixed Asset`), klik [Apply]
32. Ketik Search `supply`, tekan Enter
33. Verifikasi tabel memuat `Printer Ink`
34. Verifikasi tabel tidak memuat `Laptop` dan `Monitor`
35. Ganti isi kotak search dengan `lap`, tekan Enter
36. Verifikasi tabel memuat `Laptop`
37. Verifikasi tabel tidak memuat `Monitor` dan `Printer Ink`

### TC-GS-UOM-198: Empty state Item Type List saat Search tidak cocok

38. Ganti isi kotak search dengan `zzqx`, tekan Enter
39. Verifikasi Title `No results found`

### TC-GS-UOM-253: Sort 3-state kolom Item Type dan Product pada tabel Item Type List

40. Klik `(←)` pada kotak Search Item Type List
41. Verifikasi tabel memuat `Laptop`, `Monitor`, dan `Printer Ink`
42. Klik header Item Type
43. Verifikasi klik 1 ascending: `Laptop`, `Monitor`, `Printer Ink`
44. Klik header Item Type
45. Verifikasi klik 2 descending: `Printer Ink`, `Monitor`, `Laptop`
46. Klik header Item Type
47. Verifikasi klik 3 netral: kolom Item Type tanpa panah sort aktif dan urutan kembali ke default Item Type A-Z (`Laptop`, `Monitor`, `Printer Ink`)
48. Klik header Product
49. Verifikasi klik 1 ascending: `Fixed Asset`, `Fixed Asset`, `Supply`
50. Klik header Product
51. Verifikasi klik 2 descending: baris pertama `Supply`
52. Klik header Product
53. Verifikasi klik 3 netral: kolom Product tanpa panah sort aktif dan urutan kembali ke default Item Type A-Z
54. Klik header Item Type
55. Klik header Product
56. Verifikasi kolom Item Type kembali netral (tanpa panah sort aktif) setelah berpindah ke kolom Product

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Modal Unit Detail Pieces dibuka sekali (langkah 1 sampai 3) untuk delapan TC (precondition sama). Urutan TC dalam spec: TC-GS-UOM-254, 347, 194, 323, 324, 193, 198, 253. Alasan: screening Filter Product (254) lebih dulu, lalu filter yang di-Apply (347, 194), chip tanpa Apply (323, 324), Search sesudah filter dikosongkan (193, 198), dan Sort terakhir pada tabel tanpa Search aktif (S-14, S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target), 9 (menutup dropdown), 15 (mengubah pilihan filter), 31 (mengosongkan filter), 40 (mengosongkan Search), dan 54 (menyiapkan sort Item Type aktif untuk Expected c TC-GS-UOM-253).
- Langkah 11 menguji Expected a TC-GS-UOM-347 sebelum [Apply] (state sementara diasersi sebelum langkah yang mengubahnya). Langkah 13 adalah pembanding positif bagi langkah 14, dan langkah 18 bagi langkah 19, 33 bagi 34, 36 bagi 37. Langkah 41 adalah `Verifikasi` pembanding (bagian 8b butir 2): ketiga baris `Laptop`, `Monitor`, dan `Printer Ink` tampil setelah Search dikosongkan dan sebelum sort pada langkah 42; bukan dari Expected TC.
- Spec ini melewati sekitar 35 langkah (56 langkah). Alasan: seluruh TC adalah perilaku satu tabel Item Type List pada satu pembukaan Modal Unit Detail dengan satu dataset Pre-setup baca-saja, satu kelas harness (fungsional); kegagalan keras membuka Detail membuat seluruh blok kehilangan makna dan pemisahan hanya menambah pembukaan modal.
- Temuan untuk QA:
  - TC-GS-UOM-253 Expected b menulis klik 1 ascending `Fixed Asset`, `Fixed Asset`, `Supply` dan klik 2 hanya "baris pertama `Supply`"; spec mengasersi sebatas itu.
  - TC-GS-UOM-193 menulis "supply → Printer Ink" tanpa kata "hanya"; spec menafsirkan sebagai hanya baris itu dan mengasersi Laptop dan Monitor tidak tampil.
