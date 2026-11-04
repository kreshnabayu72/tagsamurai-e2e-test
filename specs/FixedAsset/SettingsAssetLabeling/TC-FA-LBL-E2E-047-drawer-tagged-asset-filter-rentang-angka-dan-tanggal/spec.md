---
id: TC-FA-LBL-E2E-047-drawer-tagged-asset-filter-rentang-angka-dan-tanggal
title: "Drawer Tagged Asset: Filter rentang Min-Max Asset Value dan rentang tanggal"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-02/filter/FLD-29
  - FALB:obl/T-ALB-02/filter/FLD-28
  - FALB:obl/T-ALB-02/filter/FLD-30
  - FALB:obl/T-ALB-02/filter/FLD-23
coverage:
  web: automated
---

# Drawer Tagged Asset: Filter rentang Min-Max Asset Value dan rentang tanggal

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-59` (satu label `Tagged-{runId}-047` dengan 12 aset Active bersuffix `{runId}-047`), `DU-60` (atribut curated pada aset `DU-59`: Asset Value Commercial dan Fiscal, Last Scanned, dan Warranty Expiry dengan nilai ada dan belum ada; nilai Date berbeda menit).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label, aset, dan atribut aset; hook `before` menunggu pergantian menit (maksimum 60 detik, bagian 6) sesudah seeding kelompok aset pertama agar nilai Date seed berbeda menit; penghapusan preferensi kolom tersimpan di browser untuk tabel Tagged Asset List di hook `after`. Hook `before` membuat data `DU-59` dan `DU-60`; hook `after` menghapusnya.
- State global: konfigurasi kolom tabel Tagged Asset List tersimpan di browser (bukan di server). Spec menampilkan kolom Last Scanned dan Warranty Expiry pada langkah 4 sampai 6 dan memulihkannya pada langkah 33 sampai 35; hook `after` menghapus preferensi kolom sebagai cadangan.

## Test Steps

1. Ketik Search `DU-59`, tekan Enter
2. Klik chip Label pada baris label `DU-59` untuk membuka Drawer Tagged Asset
3. Ubah ukuran halaman Pagination menjadi 25 agar seluruh aset `DU-59` tampil dalam satu halaman
4. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
5. Centang kolom Last Scanned dan Warranty Expiry
6. Klik `[Save]`
7. Klik ikon Filter di toolbar Drawer

### FALB:obl/T-ALB-02/filter/FLD-29: Filter rentang Min-Max Asset Value

8. Verifikasi field Asset Value (Commercial) dan Asset Value (Fiscal) masing-masing berupa dua input rentang dengan placeholder `Min` dan `Max`
9. Isi `Min` dan `Max` kedua field dengan nilai Asset Value (Commercial) dan Asset Value (Fiscal) satu aset `DU-60` (batas inklusif di kedua ujung), klik `[Apply]`
10. Verifikasi aset pemilik nilai itu tampil pada tabel
11. Verifikasi aset dengan nilai Asset Value berbeda tidak tampil pada tabel
12. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter/FLD-28: Filter rentang tanggal Last Scanned

13. Verifikasi field `Last Scanned` berupa date range picker dengan placeholder `Select date`
14. Verifikasi tanggal Last Scanned aset `DU-60` yang pernah dipindai tampil pada kolom Last Scanned
15. Pilih rentang satu hari sama dengan tanggal Last Scanned aset itu pada field `Last Scanned`, klik `[Apply]`
16. Verifikasi aset itu tampil pada tabel
17. Verifikasi aset yang belum pernah dipindai tidak tampil pada tabel
18. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter/FLD-30: Filter rentang tanggal Warranty Expiry

19. Verifikasi field `Warranty Expiry` berupa date range picker dengan placeholder `Select date`
20. Verifikasi tanggal Warranty Expiry aset `DU-60` yang garansinya terisi tampil pada kolom Warranty Expiry
21. Pilih rentang satu hari sama dengan tanggal Warranty Expiry aset itu pada field `Warranty Expiry`, klik `[Apply]`
22. Verifikasi aset itu tampil pada tabel
23. Verifikasi aset yang garansinya belum diisi tidak tampil pada tabel
24. Klik `[Clear Field]`, klik `[Apply]`

### FALB:obl/T-ALB-02/filter/FLD-23: Filter rentang tanggal Last Updated

25. Verifikasi field `Last Updated` berupa date range picker dengan placeholder `Select date`
26. Verifikasi nilai Last Updated aset `DU-59` tampil pada kolom Last Updated
27. Pilih rentang yang memuat tanggal seeding pada field `Last Updated`, klik `[Apply]`
28. Verifikasi seluruh 12 aset `DU-59` tampil pada tabel
29. Pilih rentang sebelum tanggal seeding pada field `Last Updated`, klik `[Apply]`
30. Verifikasi empty state tabel menampilkan judul `No results found`
31. Klik `[Clear Field]`, klik `[Apply]`
32. Verifikasi tabel kembali menampilkan seluruh 12 aset `DU-59`
33. Klik header kolom Actions (`⋯`) pada tabel Drawer, pilih `Setup Column...`
34. Hapus centang kolom Last Scanned dan Warranty Expiry
35. Klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit Labels List ke label `DU-59`, R-16), 2 (membuka Drawer), 3 (ukuran halaman 25), 4 sampai 6 (menampilkan kolom Date sebagai precondition), 7 (membuka Filter Panel), 12, 18, 24, dan 31 (mengosongkan Filter Panel sebelum blok berikutnya, S-09), serta 33 sampai 35 (pemulihan Setup Column tanpa `Verifikasi`; 8b.14, R-24). Langkah 32 adalah pembanding yang membuktikan tabel pulih penuh setelah Filter dikosongkan (S-03).
- Anchor positif (bagian 8b butir 2): langkah 10, 16, dan 22 mendahului absence pada langkah 11, 17, dan 23; langkah 28 membuktikan tabel termuat sebelum empty state pada langkah 30. Nilai Date seed diverifikasi tampil pada langkah 14, 20, dan 26 sebelum asersi Filter tanggal (8b.15 butir b).
- Filter rentang tanggal bergranularitas hari: asersi Last Updated memakai rentang yang memuat atau mendahului tanggal seeding, bukan pemisahan menit.
- Temuan PRD: label field Filter kolom Asset Value ditulis `Asset Value ([Book])` di PRD §4.1.1 Tabel 2 kolom Label Filter, sedangkan kolom ditulis `Asset Value (Commercial)` dan `Asset Value (Fiscal)`. Spec memakai nama kolom sebagai label field pada langkah 8; PRD tidak menyatakan literal label field Filter untuk kedua buku.
- Filter kolom Measurement dan Label diasersi di spec 052; Filter kolom Name, TAG, Brand, dan Model/Type di spec 046.
